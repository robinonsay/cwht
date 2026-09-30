---
id: INSP-021
checklist: peer-review-checklist-requirements
checklist_revision: C
checklist_file: docs/reviews/SRR/checklists/process-04-verification-and-validation.md
product: docs/process/04-verification-and-validation.md
# product_commit: the review baseline HEAD (the product files were last changed at b301df2 (04) and 4e3f891 (docs/vv/README.md))
# product_commit at the close-out delta (2026-09-26): HEAD 26011f1; the iteration 1 baseline was adcfe0946d2f1b5cd8f41a8f91eb4219a7fb99a1
# product_commit at the close-out item C delta (2026-09-27): HEAD 08922d9 (was 26011f1)
# product_commit at the CR-013 delta (2026-09-29): branch cr/CR-013-process-04-07-semp-srr-liens head 41c588c (was 08922d9 on main)
product_commit: "41c588cddc9a97cec536482dc2bd164e2bf81ea3"
# product_files: HEAD blobs delta-verified at the post-SRR-ruling delta (2026-09-26, HEAD ebe5873): 04 changed at d992052 (CR-002 step 1, SRR decision 113), CR-002 added at d992052 and reviewed as the change record of that edit; iteration 2 verified 04 blob 76bb24c3f3f43c1f7d3eb1b1be156824488153a8 at 33ac1ce; iteration 1 reviewed 04 blob ecff54d70d1c3bb8c90be0803f4b9720596adfc0 at adcfe09
product_files: ["docs/process/04-verification-and-validation.md@7617007ec517f76c286a15f469dfcd01c5d2cbde", "docs/vv/README.md@878869d346d936e4ad38ef5a51ef18175a0774fa", "docs/cm/cr/CR-002-inspection-for-documentary-requirements.md@c007177f7c3a50bc9ad2f0e4fcdeb798f530c045"]
# CR-013 delta (2026-09-29, branch head 41c588c): 04 changed at 41c588c (0b197bba, the baseline/srr blob, to 7617007e; CR-013 section 1.1, the liens finding-2, 3, 4 and 9); README and CR-002 unchanged
# close-out item C delta (2026-09-27, HEAD 08922d9): CR-002 changed at 8b86c16 (36224b45 to c007177f, section 6 independent Class I impact review, SRR close-out item C, RFA-SRR-008); 04 and README unchanged
# close-out delta (2026-09-26, HEAD 26011f1): CR-002 changed at bf654e6 (73070823 to 36224b45, SRR close-out items 5 and 7); 04 and README unchanged
product_size: 18 sections (601 lines) plus docs/vv/README.md (35 lines) plus CR-002 (150 lines, delta only)
sprint: SRR-prep
author_agent: "author:process-04 (Claude main session, lead SE; maintainer per the 04 header)"
reviewer_agent: "reviewer:INSP-021"
criticality: neither
# assurance_required: false; 07 section 2.1.1 row "Other process documents (docs/process/0N-*.md except 03, 05 and this plan)" is No
assurance_required: false
assurance_reviewer_agent: none
iteration: 2
# readiness_met: true at the re-issue of 2026-09-26 (package item R8): R3 met by the author self-check filed at ca22e37 and confirmed by the reviewer; see Re-issue
readiness_met: true
# post-SRR-ruling delta (2026-09-26, HEAD ebe5873): CR-002 step 1 verified, no new Major; new Minor finding-6 and finding-7 (CR-002) are liens due PDR; verdict stays APPROVED
# close-out item C delta (2026-09-27, HEAD 08922d9): 8b86c16 verified (CR-002 section 6 filled by the independent reviewer); new Minor finding-10 is a lien due PDR; no Major open; verdict stays APPROVED
# close-out delta (2026-09-26, HEAD 26011f1): bf654e6 verified, finding-7 Verified (CR-002 step 5 landed before the tag at c774851); new Minor finding-8 and finding-9 are liens due PDR; no Major open; verdict stays APPROVED
# CR-013 delta (2026-09-29, branch head 41c588c): finding-2, 3, 4 and 9 Verified on 04 blob 7617007e; no new finding in this record (the product findings of the same blob are INSP-058 finding-1 to 3, not repeated); no Major open; verdict stays APPROVED
# reviewer_verdict: finding-1 Verified at iteration 2; every Minor finding is "Lien: fix before PDR" (convergence rule of 2026-09-26)
# verdict: APPROVED (with liens finding-2 to finding-4, fix before PDR) at the re-issue of 2026-09-26 without a further product review;
# iteration 2 held it at NEEDS CHANGES only on readiness R3 (finding-5), which the author self-check now meets (finding-5 Verified)
reviewer_verdict: APPROVED
assurance_verdict: not-required
verdict: APPROVED
findings_major: 1
findings_minor: 9
findings_open: 0
findings_fixed: 0
# findings_verified: 3 (finding-1, 5, 7) before the CR-013 delta; 7 after it (finding-2, 3, 4, 9 added)
findings_verified: 7
# the four Minor findings are liens "fix before PDR" (convergence rule of 2026-09-26), listed in the lien table, not Deferred RIDs
findings_deferred: 0
assurance_findings_major: 0
assurance_findings_minor: 0
assurance_tasks_applied: []
deferred_rids: []
# items_no: R3 answered Yes at the re-issue (finding-5 Verified)
items_no: [CK-REQ-G1, CK-REQ-G7]
# effort: 117 turns, 150 minutes before the CR-013 delta, which adds 14 turns and 25 minutes
effort_turns: 131
effort_minutes: 175
record_status: Open
date: 2026-09-26
date_closed: null
---

# Peer review record INSP-021: V&V process (`docs/process/04-verification-and-validation.md`) and `docs/vv/README.md`

Checklist: `docs/templates/peer-review-checklist-requirements.md` revision C, product type "Plans and process documents" (section G, all items, and A8), the plan review items that `docs/process/08-agent-briefing.md` section 3.1 (author row "plans and process documents") and section 3.5 assign to plans. `docs/vv/README.md` is the directory guide the 04 process governs (its line 3) and is reviewed with the same items. Gate fed: SRR (package `docs/reviews/SRR/package.md` section 2, H1 (c) and R6: the missing record for 04; 05 Table 4-2 row 2).

Review baseline: HEAD `adcfe0946d2f1b5cd8f41a8f91eb4219a7fb99a1`. Reviewed blobs: `docs/process/04-verification-and-validation.md` `ecff54d7` (last changed at `b301df2`), `docs/vv/README.md` `878869d3` (last changed at `4e3f891`); both equal HEAD and neither file differs in the working tree (`git status --short` empty for both).

Independence: the reviewer did not author either file and did not edit them. Search first: `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` preceded every manual search (queries: lien-table record format; LTspice wrapper naming; SE HB verification versus validation wording; author self-check for 04); `grep -n` was used afterwards only to pin hits. Every SE-NN, SWE-NNN and 47 CFR citation used here was pinned in `docs/references/md/`.

## Record

### Findings

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | reviewer | Major | CK-REQ-G1 | 04 line 146 (section 6), line 188 (OQ-VV-001 row "Receipt ADR (charter section 9; charter issue C2 of section 18)"), line 487 (section 13 row 5), line 516 (section 14 row 3.4), line 525 (row 5.3), line 555 (section 16 SRR row), line 558 (TRR row), line 599 (C2) | 04 says the tinySA Ultra receipt "is recorded by ADR before TRR, charter section 9" and makes a "receipt ADR" the OQ-VV-001 closure record and a TRR row 5 entrance item. Charter section 9 (`00-charter.md` line 130) says the receipt "is recorded by a receipt-inspection report and a TV-NNN record before TRR, closing OQ-VV-001". The charter changed at `4e3f891` (`git show 4e3f891 -- docs/process/00-charter.md`) and adopted exactly the resolution 04 proposes in C2; 04 was revised afterwards (`b301df2`) and still attributes the superseded wording to the charter. The plan contradicts its parent on a TRR entrance control (08 section 3.2: violating the charter is Major; same defect as INSP-005 finding-1 on the SEMP, which the SEMP has since fixed; 04 is now the only product carrying "receipt ADR", per a repository search). Fix: at all eight places use the charter wording (receipt inspection report `docs/vv/reports/receipt-inspection-<n>.md` plus the tinySA TV record `docs/cm/tool-validation/TV-NNN-tinysa.md`, ADR-021 stays the purchase decision); mark C2 Resolved against charter `4e3f891`. | Verified | Not needed | |
| <a id="finding-2"></a>finding-2 | reviewer | Minor | CK-REQ-G1 | 04 line 78 (section 4 Emulation row); line 598 (C1) | (a) 04 calls `ACC-EMU-001` "a research proposal name and not a charter section 6 identifier; charter issue C1". Charter section 6 (line 109) now defines `ACC-<TOOL>-NNN`, "accreditation scope statement, held inside its TV-NNN record (e.g. ACC-EMU-001)", the first resolution C1 proposes; C1 still reads Open. (b) The same row names the emulation crate `cwht-emu` ("`firmware/emu/` (`cwht-emu`, 07 section 9.4)"); 07 names no such crate (07 lines 26, 61, 160, 189: `firmware/emu/` scenarios, harness fixed by the PDR emulator ADR). Fix: cite `ACC-EMU-001` as the charter section 6 scope statement inside the emulator TV record and mark C1 Resolved; drop `cwht-emu` or match 07. | Lien: fix before PDR | Pending | |
| <a id="finding-3"></a>finding-3 | reviewer | Minor | CK-REQ-G7 | 04 line 146; line 413 (section 10.6); line 519 (section 14 row 4.2) with line 593 (A10); line 567 (section 17) | Statements in the body contradict the tree and the document's own section 18 statuses: (a) line 146 says `sigrok-cli` "has no `tools/toolchain.lock.md` row at this date, alignment item A13", but the lock has the rows (lines 45 and 46) and A13 (line 596) reads Resolved; (b) line 413 says "`docs/plan/tpm.json` carries no NCR entry at this revision", but `tpm.json` line 969 holds TPM-019 `ncr-trend` and A12 (line 595) reads Resolved; (c) line 519 plans a new risk "RSK-019 if no other risk is added first" and A10 reads Open, but `docs/risk/register.json` holds RSK-059 "No qualification testing at the environmental extremes"; (d) line 567 says 01 section 3.5 "labels these rows NA (wording alignment item A14)", but 01 line 147 reads "Customized (NA)" and A14 (line 597) reads Resolved. Fix: restate the four places from the current tree, cite RSK-059, set A10 Resolved. | Lien: fix before PDR | Pending | |
| <a id="finding-4"></a>finding-4 | reviewer | Minor | CK-REQ-G7 | 04 section 7.4 lines 258, 263, 269, 274 (row 7.3.2), 277 (row 7.3.5); section 4 line 95 | (a) Rows 7.3.2 (retired list as its own report section) and 7.3.5 (`VAL_PHASE_MISSING`) are due "before SRR", and line 269 says "the gate's readiness declaration is blocked until its unit test passes". Neither exists at HEAD: `tools/traceability.py` has no `VAL_PHASE_MISSING` code (grep, only `PHASE_CLAUSE` parsing) and `docs/reviews/SRR/traceability-report.md` gives only the retired count (lines 12, 13, 21), no list. 02 section 8.5 row T-19 (line 559) dates the same report section PDR, so 02 and 04 disagree on the due gate, and the SRR package does not carry the item. (b) The section 7.4 observation is dated 2026-09-25 at `b8214ca` with the tools untracked and 258 tests; at HEAD both tools are tracked (`git ls-files`) and the suite has 392 tests. (c) Line 95 names the LTspice wrapper `tools/run_sim.py`; the lock's planned-script table (line 117) and 08 section 1 name `tools/ltspice-batch.sh` (ADR-018 section 2 allows either name). Fix: re-date rows 7.3.2 and 7.3.5 to PDR in line with 02 T-19 (no `TC-VAL` case exists yet, so nothing is unchecked today) or implement them before the declaration; re-observe section 7.4 at the SRR commit; name the lock's wrapper. | Lien: fix before PDR | Pending | |
| <a id="finding-5"></a>finding-5 | reviewer | Minor | R3 | author return | No author self-check of 04 or `docs/vv/README.md` against checklist sections G and A8, and no brief acceptance criteria, came with this assignment or exist in the repository (claude-context search for an 04 author self-check found none; section 18 is an alignment list, not a self-check). Readiness R3 is not met and `readiness_met` is false. Fix: the 04 author files the self-check with the next re-review brief, or Robin extends package decision 115 to this record. | Verified (re-issue 2026-09-26: author self-check filed at `ca22e37`, confirmed in section "Re-issue") | Not needed (decision 115 not required) | |

### Disposition (iteration 2, 2026-09-26, HEAD `33ac1ce`)

| Finding | Author action | Author commit | Reviewer verification | State |
|---|---|---|---|---|
| finding-1 | Fixed | `33ac1ce` (`git log -1 -- docs/process/04-verification-and-validation.md`; 8 lines changed, 8 insertions, 8 deletions) | `git show 33ac1ce`: all eight places now use the charter wording. Section 6 line 146, OQ-VV-001 closure record (line 188), section 13 row 5 (line 487), section 14 rows 3.4 (line 516) and 5.3 (line 525), section 16 SRR (line 555) and TRR (line 558) rows name the receipt inspection report `docs/vv/reports/receipt-inspection-<n>.md` plus the tinySA TV record `docs/cm/tool-validation/TV-NNN-tinysa.md`, ADR-021 stays the purchase decision; C2 (line 599) reads Resolved against charter `4e3f891` and quotes charter section 9 line 130 exactly. `git show HEAD:docs/process/04-verification-and-validation.md \| grep -n -i 'receipt ADR\|ADR before'` gives only the C2 history quotation; the remaining "by ADR" hits are the PDR emulator ADR (line 556) and the signal generator row (line 174), unrelated. The diff introduces no new defect: no em dash added (count 0 in the blob), no citation added, the other lines of the changed paragraphs are unchanged (the stale A13 clause on line 146 is the pre-existing finding-3 (a) lien, not new). `docs/vv/README.md` unchanged (blob `878869d3`) | Verified |

### Lien table (convergence rule of 2026-09-26, charter section 4 item 3: a Minor RID is fixed before the next review and does not block the baseline; carried by the package as Routine items)

| Finding | Severity | Disposition | Owner | Due |
|---|---|---|---|---|
| finding-2 | Minor | Lien: fix before PDR | 04 author (Claude, lead SE) | PDR readiness declaration |
| finding-3 | Minor | Lien: fix before PDR | 04 author (Claude, lead SE) | PDR readiness declaration |
| finding-4 | Minor | Lien: fix before PDR | 04 author (Claude, lead SE); `tools/traceability.py` owner if implemented instead of re-dated | PDR readiness declaration |

## Readiness criteria

| # | Criterion | Answer | Evidence |
|---|---|---|---|
| R1 | The product validates: `tools/validate_docs.py` exits 0 | Yes | 04 and the README are Markdown without a schema convention; run 2026-09-26 at HEAD: `validate_docs: 37 passed, 0 failed, 37 checked`, exit 0 |
| R2 | `tools/traceability.py` reports no violation for the ids in the file | N/A (a plan defines no REQ or TC ids) | `traceability.py --report-only` exit 0: 237 requirements, 170 test cases, 0 violations, 2 warnings (`SYS_UNALLOCATED` REQ-SYS-125, REQ-SYS-148; not 04 ids) |
| R3 | Author self-check against sections A to G and the brief's acceptance criteria | Yes at re-issue (No at iterations 1 and 2) | finding-5 Verified at re-issue 2026-09-26: the author self-check filed at `ca22e37` lists the acceptance criteria and answers A8 and G1 to G8; see section "Re-issue" |
| R4 | Every `TBR` has owner, plan, close_by; no `TBD` | Yes | `grep -n -w 'TBD\|as appropriate\|should consider'` on both files: no hit; open questions OQ-VV-001 to 003 name owner and gate (04 lines 186 to 190); em dash count 0 in both files |
| R5 | For a CR: impact assessment attached | N/A | Not a CR |

`readiness_met: false` (R3) at iterations 1 and 2; `true` at the re-issue (section "Re-issue").

## A. Format and editorial

| Id | Answer | Evidence |
|---|---|---|
| CK-REQ-A8 | Yes | Terms match the charter and the schema: evidence classes Simulation, HostUnit, Emulation, Inspection, Bench, OnAir (04 section 4; charter section 9); key types "straight key" and "iambic paddles" (04 lines 33, 320, 336); statuses Draft, Active, Passed, Failed, Blocked, Verified, Closed as in the schemas (04 section 5.3). Items A1 to A7 and sections B to F: N/A (plan) |

## G. Plans, process documents and decision records (SWE-087 b)

| Id | Answer | Evidence |
|---|---|---|
| CK-REQ-G1 | No | 04 expands charter section 9 and the V&V parts of sections 3, 5, 7, 10 (header line 3). Checked against charter sections 3, 6, 7, 9, 10, 12: consistent on Verified versus Closed for host-verified software (04 5.2, 5.3; charter line 131), dev-board `credit: false` convention (04 line 83; charter line 41), MC/DC method and nightly MSR-14 as required non-credit (04 section 12; charter line 137), SWE-211 relief (04 section 4; charter line 159), test-only case modules (04 line 24; charter line 109). RMM: SWE-192 FC, SWE-211 T, SWE-219 T, SWE-073, SWE-193, SWE-203 FC match 04 sections 3, 4, 12, 17 (`rmm.json`). Compliance matrix: SE-13, SE-14 FC citing 04 and the SRR memo; SE-47, SE-48 FC citing the TRR package; SE-51, SE-52 T; SE-53, SE-54, SE-69 FC, as 04 section 13 states. ADR-021 (tinySA), ADR-011 (emulator order only), ADR-018 consistent. Disagreements: finding-1 (charter section 9), finding-2 (charter section 6; 07) |
| CK-REQ-G2 | Yes | Every step names its artifact and id scheme: cases `TC-<MOD>-NNN` in `docs/test_cases/<module>/test_cases.json`, reports `docs/vv/reports/<TC-ID>-r<N>.md`, NCRs `docs/vv/ncr/NCR-NNN.md` with the status lifecycle of 10.7, ADP `docs/vv/adp/<unit>/`, receipt `receipt-inspection-<n>.md`, V&V plan sections with the gate that writes each (section 14), gate products (section 16). The README layout table gives path, trigger and format for every entry. Open questions name the decider and the gate |
| CK-REQ-G3 | Yes | Section 2 table: owner as test director, witness and NCR disposition authority; Claude as test conductor; independent test author, procedure reviewer and assurance reviewer; independence recorded through 8.3 item 10. Owner approval points: ETA approval in the SRR memo (header), TRR and on-air `TRR-Dn` authorization (6.3, 13), NCR dispositions (10.4, 10.7), waivers (12), SAR acceptance (5.3) |
| CK-REQ-G4 | Yes | Tailoring relied on is mirrored: SWE-211 T (section 4 and RMM row), SWE-219 T (section 12 and RMM row), SE-51 and SE-52 T (section 13 and matrix rows), NPR 7150.2D section 4.5.1 NPR 8705.2 note NA (section 17). The RMM side of alignment items A3 (`meta` note on NPR 8705.2) and A4 (SWE-071 pointer to section 8.2 and `CASE_STALE`) is still missing at HEAD (`rmm.json` has no "8705" string in `meta`; the SWE-071 row names neither); that is an RMM product item, cross item X1 |
| CK-REQ-G5 | N/A | Cybersecurity assets, threats and mitigations live in 07 section 16 (charter section 12 row); 04 carries the cyber regression cases (section 10.5 line 394) |
| CK-REQ-G6 | Yes | Measurements named with source and rule: MSR-13 and MSR-14 (section 12), MSR-27 (section 10.6), MSR-01, 03, 04, 23 via `docs/vv/traceability.json` (README line 11; the file carries exactly these four keys at HEAD); thresholds and storage are in 07 section 11.2 (lines 500 to 526) and `docs/plan/measurements.json` |
| CK-REQ-G7 | No | True and dated: kicad-cli lock path, emulator "not selected" (lock line 48), cargo-llvm-cov 0.9.1 (lock line 25), `.gitignore` lines 31 and 32 un-ignore `docs/vv/**/*.log` and `*.raw` as 04 line 544 and README line 13 say, `traceability.py --help` options match line 262 at HEAD; honest limits stated (no Rust MC/DC, emulator order only, no oscilloscope, power meter or generator). Defects: finding-3, finding-4 |
| CK-REQ-G8 | Yes | Pinned in the corpus: NPR 7150.2D SWE-062, 186 (section 4.4), SWE-065, 066, 068, 070, 071, 073, 187, 189, 190, 191, 192, 193, 211 (section 4.5), SWE-194 (4.6.4), SWE-201 to 204 (5.5), SWE-136, 063, 034, 087, 134, 219, 220; SWE-202 note classes match the 10.3 severity column verbatim in substance; SWE-203 note (component list, mandatory code audits for critical defects); SWE-073 note (high-fidelity simulation); section 4.5.3 note (best practice, independent organization) and section 4.5.1 NPR 8705.2 sentence. NPR 7123.1D SE-13 (3.2.8.1), SE-14 (3.2.9.1), 3.2.8.2 MOP sentence, SE-47, 48, 51, 52, 53, 54, 68, 69 (`05-chapter5.md` lines 98 to 120), App. G Tables G-9, G-10, G-11. SE HB section 2.4, App. B glossary questions "Did I build the product right?" and "Am I building the right product?" (`24-appendix-b-glossary.md` lines 749, 763), section 5.3 "Methods of Verification" and Table 5.3-1, section 6.1 run-for-record and "buy off" note (`15-6-1-technical-planning.md` lines 287, 305), section 5.4 anticipated operators and users. 47 CFR 97.307(e) (25 uW for 25 W or less; -16.02 dBm), 97.307(a) and (b), 97.305, 1.1310, 2.1093 exist in the regulatory corpus. No NASA requirement is presented as a quotation it is not |

## `docs/vv/README.md` (same items)

No finding. The layout table matches 04 sections 7.4, 9, 10, 11, 12 and 15 and the CM plan: the report CM keys `source_commit`, `firmware_elf_sha256`, `procedure_blob`, `harness_versions` exist in `docs/templates/verification-report.md` (lines 46 to 69) and are the FCA-03 and FCA-04 inputs of 05 (lines 326, 327); 01 section 7.3 row 9, section 8.3 rows 7 and 20 exist as cited; `TC-EXAMPLE-006` is the dev-board example (`docs/templates/test_cases.example.json` line 152); the workflow paragraph states Verified on the credited report and Closed on the SAR memo commit with the PCA-05 line, as charter section 9 does. The README does not repeat the finding-1 wording.

## Cross items (outside this record's scope; for the integrating session)

- X1: RMM author: alignment items A3 and A4 of 04 section 18 are due "before SRR" and still open at HEAD (`rmm.json` `meta` has no NPR 8705.2 note; the SWE-071 row does not cite 04 section 8.2 or rule 7.3.11). 04 section 17 line 569 depends on A3.
- X2: package: H1 (c) and R6 name this record `plan-04-verification-and-validation`; the assignment filed it as `process-04-verification-and-validation.md`. Update the package reference. The two "before SRR" tool rows of finding-4 are not in package section 2.1; either the re-date (finding-4 fix) or a readiness item is needed.
- X3: package section 20.1 L-6 (Routine liens) gains INSP-021 finding-2 to finding-5 when this record is integrated.

## Tool runs (2026-09-26, HEAD `adcfe09`, repository root, `.venv/bin/python`)

| Command | Exit | Result |
|---|---|---|
| `tools/validate_docs.py` | 0 | 37 passed, 0 failed (before this record); after writing it: `PASS docs/reviews/SRR/checklists/process-04-verification-and-validation.md`, 40 passed, 0 failed, exit 0 (the count includes records other reviewers filed meanwhile) |
| `tools/traceability.py --report-only` | 0 | 237 requirements, 170 test cases, 0 violations, 2 warnings (REQ-SYS-125, REQ-SYS-148); `docs/vv/` unchanged afterwards (`git status --short docs/vv/` empty) |
| `tools/render_risk.py --check --gate SRR --hazards docs/safety/hazards.json` | 0 | 65 risks, 159 candidates, 0 warnings, hazard cross-check; `register.md` current |
| `tools/render_rmm.py --check` | 0 | 100 rows; FC 75, T 17, NA 8; `rmm.md` current |
| `tools/render_compliance.py --check` | 0 | validation passed, rendered file current |
| `python -m unittest discover -s tools/tests` | 0 | 392 tests OK |

No image was produced by this review, so no render to inspect.

## Measurements (SWE-089)

| Measure | Value |
|---|---|
| Product size | 04: 18 sections, 599 lines; README: 35 lines |
| Items checked | 14 (G1 to G8, A8, R1 to R5) |
| Items answered No | 3 (G1, G7, R3) |
| Items N/A | A1 to A7, B to F, G5, R2, R5 |
| Findings by severity | Major 1, Minor 4 |
| Findings fixed, deferred | 0, 0 (4 liens) |
| Iteration | 1 |
| Effort | 45 turns, 55 minutes |

## Verdict

Iteration 2 (2026-09-26, HEAD `33ac1ce`, 04 blob `76bb24c3`, README blob `878869d3`): finding-1 Verified; findings 2 to 5 stay Lien: fix before PDR. No Major finding is open. reviewer_verdict APPROVED (with liens); the record verdict is held at NEEDS CHANGES only by readiness R3 (finding-5, decision 115), because `tools/validate_docs.py` refuses APPROVED with `readiness_met: false`; it turns APPROVED (with liens) on re-issue once the self-check is filed or Robin waives it.

```
VERDICT: NEEDS CHANGES (readiness R3 only; reviewer_verdict APPROVED with 4 liens)
PRODUCT: docs/process/04-verification-and-validation.md@76bb24c3, docs/vv/README.md@878869d3 (HEAD 33ac1ce)
FINDINGS:
- [Major] finding-1 CK-REQ-G1: fixed at 33ac1ce, Verified.
- [Minor] finding-2 to finding-5: Lien: fix before PDR.
MEASUREMENTS: iteration=2; major=1; minor=4; verified=1; lien=4; open_major=0; turns=57; minutes=70
```

Iteration 1 (2026-09-26, HEAD `adcfe09`): findings: 5. Unfixed 1 at iteration 1 (finding-1, Major; Verified at iteration 2; state word reworded at the re-issue because the `open_major_findings` check of `tools/validate_docs.py` reads any line naming a finding with both severity and state words as current); Lien 4 (finding-2 to finding-5, Minor, fix before PDR); Closed 0; Disputed-accepted 0. Under the convergence rule the open Major finding changes the product; the record is NEEDS CHANGES until finding-1 is fixed and verified. Even with finding-1 closed, readiness R3 (finding-5) keeps the record NEEDS CHANGES until the self-check is filed or Robin waives it under decision 115, as for INSP-001, 002 and 010.

```
VERDICT: NEEDS CHANGES
PRODUCT: docs/process/04-verification-and-validation.md@ecff54d7, docs/vv/README.md@878869d3 (HEAD adcfe09)
FINDINGS:
- [Major] finding-1 CK-REQ-G1 04 sections 6, 6.3, 13, 14, 16, 18 C2: "receipt ADR" contradicts charter section 9 (receipt-inspection report and TV-NNN record). Unfixed at iteration 1; Verified at iteration 2.
- [Minor] finding-2 CK-REQ-G1 04 section 4, C1: ACC-EMU-001 is now a charter section 6 identifier; cwht-emu not in 07. Lien: fix before PDR.
- [Minor] finding-3 CK-REQ-G7 04 lines 146, 413, 519, 567: stale statements against the lock, tpm.json TPM-019, RSK-059, 01 section 3.5. Lien: fix before PDR.
- [Minor] finding-4 CK-REQ-G7 04 section 7.4: two "before SRR" tool rows unimplemented and dated PDR in 02; stale observation; wrapper name. Lien: fix before PDR.
- [Minor] finding-5 R3: no author self-check. Lien: fix before PDR (decision 115).
ITEMS N/A: CK-REQ-A1 to A7, B1 to B7, C1 to C8, D1 to D4, E1 to E6, F1 to F4 (plan); CK-REQ-G5 (cybersecurity is in 07 section 16)
MEASUREMENTS: size=18 sections + README; items=14; no=3; turns=45; minutes=55; major=1; minor=4; lien=4; open_major=1; iteration=1
```

## Author self-check (readiness R3; SRR package item R7)

Filed by the author, `author:process` (Claude main session, lead SE, the author named in this record's front matter), on 2026-09-26 at HEAD `ade0e09`, in answer to readiness R3 ("the author's return states the self-check against sections A to G below and lists the brief's acceptance criteria") and package item R7. 01 section 13 makes this file the single peer-review record for the product and requires that no record live only in conversation, so the self-check is filed here. This section is the author's only content in the record: the front matter (including `readiness_met` and `verdict`), the findings, the readiness answers and the verdict belong to the reviewer and are unchanged. The reviewer confirms this self-check and answers R3 at the re-issue (package item R8); the author does not mark its own product reviewed (08 section 3.1).

**Product files checked.** `docs/process/04-verification-and-validation.md@76bb24c3` (last changed at `33ac1ce`, the finding-1 fix), `docs/vv/README.md@878869d3`. Each blob equals `git rev-parse HEAD:<path>` at `ade0e09` and equals the blob this record reviewed, so the self-check covers the reviewed product. The product files are not changed by this self-check (convergence rule).

**Search first.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (queries: author self-check and readiness R1 to R4 of a record; author self-check sections against section G items CK-REQ-G1 to G8). `grep -n` was used afterwards only to pin lines.

**Acceptance criteria of the author brief.** The original author assignments for these revisions are not on record, so the criteria stated here are the ones 08 section 1 (WRITING, CITATIONS, SCOPE, COMMANDS) and section 3.1 (row "plans and process documents") impose on every author brief for a process document, plus the lead SE convergence rule of 2026-09-26. Each criterion is listed with the author's result:

| # | Criterion (source) | Result | Evidence |
|---|---|---|---|
| AC-1 | The document expands its charter sections and contradicts neither the charter, the RMM, the compliance matrix nor an Accepted ADR (08 section 3.1; CK-REQ-G1) | Met except for the Minor liens named under CK-REQ-G1 below | Section G table below |
| AC-2 | Decision-complete writing: no `TBD` as a value, no "as appropriate" or "should consider" without naming who decides and when, no em dash (08 section 1 WRITING) | Met | Scripted scan below |
| AC-3 | Only corpus-verified identifiers are cited; no NASA requirement is paraphrased as a quotation (08 section 1 CITATIONS; CK-REQ-G8) | Met | Scripted id check below |
| AC-4 | Every step names the artifact it produces or consumes with path and id scheme (08 section 1 WRITING; CK-REQ-G2) | Met; any Minor lien against it is named under CK-REQ-G2 below | Section G table below |
| AC-5 | `tools/validate_docs.py` passes the product files (08 section 1 COMMANDS; readiness R1) | Met | Tool runs below |
| AC-6 | Scope: the author edits neither the charter nor a schema nor another author's file (08 section 1 SCOPE) | Met | This self-check adds only this section; the product files are unchanged since the reviewed blobs |
| AC-7 | Convergence rule (charter section 4 item 3): only Major findings change products before SRR; Minor findings are liens due PDR | Met | No Major finding is open against the product; the liens are accepted below and not fixed in this round |

**Scripted scan (AC-2, AC-3).** Over both files: 0 em dashes, 0 "as appropriate" or "should consider", 0 `TBD`, 0 `TBR`. Every SE id cited (11 distinct) and every SWE id cited (28 distinct) exists bracketed in the corpus (0 missing).

**Self-check against the checklist** (`docs/templates/peer-review-checklist-requirements.md` revision C, product type "Plans and process documents": CK-REQ-A8 and section G; A1 to A7 and sections B to F are N/A for a process document by the product-type table).

| Id | Author answer | Evidence |
|---|---|---|
| CK-REQ-A8 | Yes | Evidence classes Simulation, HostUnit, Emulation, Inspection, Bench and OnAir match charter section 9 and `docs/test_cases/schema.json`; Verified and Closed are used as charter section 9 defines them |
| CK-REQ-G1 | No (lien only) | 04 expands charter section 9 and the V&V parts of sections 3, 5, 7 and 10 (header line 3). finding-1 (Major) is fixed at `33ac1ce` and Verified by the reviewer: 04 has 0 occurrences of "receipt ADR" and 12 of "receipt-inspection", matching charter section 9. Known gap, Minor: finding-2 (`ACC-EMU-001` is now a charter section 6 identifier; C1 status stale) |
| CK-REQ-G2 | Yes | Cases `TC-<MOD>-NNN` in `docs/test_cases/<module>/test_cases.json`, reports `docs/vv/reports/<TC-ID>-rN.md`, NCRs `docs/vv/ncr/NCR-NNN.md`, V&V plan `docs/vv/plan.md` (sections 7 to 10, 14) |
| CK-REQ-G3 | Yes | Section 2: owner as test director, witness and NCR disposition authority; Claude as test conductor; independent test author, procedure reviewer and assurance reviewer |
| CK-REQ-G4 | Yes | SWE-211 and SWE-219 T (sections 4 and 12, RMM rows), SE-51 and SE-52 T (section 13, matrix rows); `render_rmm.py --check` and `render_compliance.py --check` exit 0 |
| CK-REQ-G5 | N/A | Cybersecurity is 07 section 16; 04 carries only the cyber regression cases (section 10.5) |
| CK-REQ-G6 | Yes | MSR-13 and MSR-14 (section 12), MSR-27 (section 10.6) and the `docs/vv/traceability.json` measures named with source and rule |
| CK-REQ-G7 | No (liens only) | kicad-cli 10.0.6 and the lock paths hold (`kicad-cli version` prints `10.0.6`). Known gaps, Minor: finding-3 (stale statements against the lock, `tpm.json` TPM-019, RSK-059 and 01 section 3.5), finding-4 (section 7.4 rows 7.3.2 and 7.3.5 due "before SRR" are not implemented in `tools/traceability.py`) |
| CK-REQ-G8 | Yes | Scripted id check above (0 missing) |

**Reviewer findings of this record, as the author reads them.** finding-1 (Major) is Verified. finding-2 to finding-4 (Minor) are accepted as liens due PDR, owner 04 author; none is disputed. finding-5 (R3) is the gap this section fills; its closure is the reviewer's call at re-issue.

**Tool runs by the author (2026-09-26, HEAD `ade0e09`, repository root, `.venv/bin/python`).**

| Command | Exit | Result |
|---|---|---|
| `tools/validate_docs.py` (after this section was added) | 1 | 47 passed, 1 failed. The one failure is `docs/reviews/SRR/checklists/hazard-analysis.md` (INSP-008): its APPROVED `product_files` name the hazard blobs `b5ce99e9` and `37d6cc83`, and commit `ade0e09` (package item R9, hazard status edits) moved HEAD to `49ec53f8` and `c6bf757e` (record drift rule). It is outside this product and this author's scope; reported to the lead SE. This record and the product files PASS |
| `tools/traceability.py --report-only` | 0 | 238 requirements, 170 test cases, 0 violations, 3 warnings (`SYS_UNALLOCATED` REQ-SYS-125 and REQ-SYS-148; `HAZARD_INVERSE` REQ-SW-KEYER-039); the regenerated `docs/vv/traceability-report.md` and `docs/vv/traceability.json` are outside scope and were restored with `git checkout` |
| `tools/render_compliance.py --check` | 0 | rows 62, FC 49, T 4, NA 9; validation PASSED and the render is current |
| `tools/render_rmm.py --check` | 0 | `rmm.md` current |
| `tools/render_risk.py --check --gate SRR --hazards docs/safety/hazards.json` | 0 | 65 risks, 159 candidates, 0 warnings; hazard cross-check passes |
| `python -m unittest discover -s tools/tests` | 1 | 392 tests, 1 failure: `test_validate_docs.RepositoryTests.test_repository_exit_zero`, caused by the same INSP-008 record drift; no failure touches this product |

**Author statement.** The self-check finds no Major defect and no defect beyond the reviewer's findings, which the author accepts as Minor liens due PDR without dispute. Readiness R3 is offered as met by this section, subject to the reviewer's confirmation at re-issue.

## Re-issue (reviewer; SRR package item R8; 2026-09-26)

Written by `reviewer:INSP-021`, the reviewer role of this record, not the author (charter section 11 rule 4; 08 section 3.1). This is the re-issue without a further product review that package section 2.1 item R8 and the iteration verdict above provide for: only readiness R3 and the product blobs are re-checked. The findings, the item answers of the review, the lien table and the counts stand as reviewed, except where this section says otherwise. **Search first:** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` (query: record readiness fields R1 to R4, author self-check, re-issue verdict APPROVED with liens) ran before any `grep`; `grep` and `git` were used afterwards only to pin lines and blobs.

**Product blobs (record drift rule, package section 2.3).** At HEAD `8ef95d3` `git rev-parse HEAD:<path>` equals the reviewed blob for every `product_files` entry: `04-verification-and-validation.md@76bb24c3`, `docs/vv/README.md@878869d3`. `git log --oneline 33ac1ce..HEAD -- <path>` prints nothing for any of them, so no product changed after the review and no delta verification is needed. The working tree equals HEAD for the product files (`git status --short` on them prints nothing).

**Readiness R3 confirmed.** The author self-check above (filed at `ca22e37` by the author named in the front matter, not by this reviewer) meets both halves of R3 ("the author's return states the self-check against sections A to G below and lists the brief's acceptance criteria"): (a) it lists acceptance criteria AC-1 to AC-7 with a result and evidence for each; the original author briefs are not in the repository, and the criteria are restated from the rules 08 section 1 (WRITING, CITATIONS, SCOPE, COMMANDS) and section 3.1 (row "plans and process documents") impose on every process-document brief, plus the convergence rule, which is the complete set a brief for this product could carry; (b) it answers every applicable item (CK-REQ-A8 and G1 to G8) Yes, No or N/A with evidence, and A1 to A7 and sections B to F N/A by the product-type table, as this record does. Every author No coincides with a reviewer No and names the same findings (G1 and G7, on finding-2 to finding-4); no author answer is Yes where this record answers No; the author disputes no finding and adds no finding. The self-check changed nothing the reviewer owns (`git show ca22e37 -- <this record>` adds only the self-check section) and changed no product.

**Reviewer spot checks of the self-check (2026-09-26, HEAD `8ef95d3`).** 04 at HEAD has 0 occurrences of "receipt ADR" (finding-1 stays Verified). `kicad-cli version` prints `10.0.6` (author G7). Em dash count 0, and no `TBD`, `TBR`, "as appropriate" or "should consider" in either file, as the author's scan says.

**Observation (not a finding).** The author's G1 answer counts 12 occurrences of "receipt-inspection" in 04; `grep -o` at HEAD counts 14. The substance, that every closure record uses the charter section 9 wording, holds.

**Readiness at re-issue.** R1 Yes (`tools/validate_docs.py` at HEAD `8ef95d3` passes this record and fails only on the INSP-008 drift outside this product; the product files carry no schema convention). R2 as reviewed. R3 **Yes** (changed from No: the self-check above, confirmed here). R4 Yes (re-confirmed: 0 em dashes, and `TBD` only as the name of a rule or list, in every product file at HEAD). R5 N/A. `readiness_met: true`.

**Finding-5 (readiness R3 as a Minor finding) Verified.** The self-check is the fix finding-5 asked for ("the 04 author files the self-check with the next re-review brief"); it is Verified and leaves the lien table. Liens now: finding-2 to finding-4 (3). Counts: 5 findings; Verified 2 (finding-1 Major, finding-5 Minor); Lien 3; none open.

**Open Major findings needing an owner ruling:** none. No finding of this record waits on a package decision; package decision 115 (owner waiver of the self-check) is no longer needed for this record.

**Tool runs at re-issue (2026-09-26, HEAD `8ef95d3`, repository root, `.venv/bin/python`).** `tools/validate_docs.py` exit 1: 48 passed, 1 failed of 49; this record PASS as APPROVED (record drift check included); the one failure is `docs/reviews/SRR/checklists/hazard-analysis.md` (INSP-008, record drift against the hazard blobs committed at `ade0e09` for package item R9), outside this record's scope and reported to the lead SE; `tools/traceability.py --report-only` exit 0, 0 violations, 3 warnings (`SYS_UNALLOCATED` REQ-SYS-125 and REQ-SYS-148, `HAZARD_INVERSE` REQ-SW-KEYER-039; none in this product), with the regenerated `docs/vv/traceability-report.md` and `traceability.json` restored by `git checkout`; `tools/render_risk.py --check --gate SRR --hazards docs/safety/hazards.json` exit 0; `python -m unittest discover -s tools/tests` exit 1: 392 tests, 1 failure, `test_validate_docs.RepositoryTests.test_repository_exit_zero`, caused by the same INSP-008 drift; no failure touches this record or its product.

**Measurements (re-issue).** Items re-checked: R1 to R5 and the product blobs; items answered No: 0; new findings: 0; effort 6 turns, 10 minutes (added to the front matter totals).

```
RE-ISSUE (2026-09-26, HEAD 8ef95d3, package item R8): VERDICT: APPROVED (with liens)
FINDINGS: finding-1 Major Verified (iteration 2); finding-5 Minor (R3) Verified at re-issue; finding-2 to finding-4 Minor, Lien: fix before PDR (unchanged); open Major 0
READINESS: R1 Yes, R2 N/A, R3 Yes (author self-check at ca22e37 confirmed), R4 Yes, R5 N/A; readiness_met true
PRODUCT: docs/process/04-verification-and-validation.md@76bb24c3, docs/vv/README.md@878869d3 (unchanged since 33ac1ce)
MEASUREMENTS: re-issue items=R1 to R5 + blobs; no=0; new findings=0; verified=1 (finding-5); turns=6; minutes=10; cumulative turns=63, minutes=80
```

`record_status` stays Open: the liens are neither Verified nor Deferred by an owner decision, and the software lead closes the record (07 section 10.2, action tracking).

## Post-SRR-ruling delta (reviewer; SRR package item R16; 2026-09-26, HEAD `ebe5873`)

Written by `reviewer:INSP-021`, the reviewer role of this record, not the author (charter section 11 rule 4; 08 section 3.1); the reviewer edited no product. The owner approved the SRR on 2026-09-26 (`docs/reviews/SRR/minutes.md`: disposition Approved with liens; key decisions K1 to K17 and the consent agenda ruled as recommended). This section delta-verifies every commit that touched this record's products after the last verified blobs, and adds CR-002 to `product_files` as the change record of the only product edit. Everything above this section stands as recorded.

**Search first.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` (query: CR-002 change request, verification and validation process 04, SRR ruling) ran before any `grep`; `grep`, `git log` and `git show` were used afterwards only to pin lines, commits and blobs.

**Commits in scope.** `git log --oneline 33ac1ce..HEAD -- docs/process/04-verification-and-validation.md docs/vv/README.md` prints one commit, `d992052` ("docs(04): CR-002 admits Inspection for documentary hazard controls (SRR decision 113)"); `git log -- docs/cm/cr/CR-002-inspection-for-documentary-requirements.md` prints the same single commit. `docs/vv/README.md` is unchanged (blob `878869d3`). Reviewed blobs at HEAD `ebe5873`: 04 `0b197bba`, README `878869d3`, CR-002 `73070823`; the working tree equals HEAD for all three.

**Ruling applied.** SRR decision 113 (key decision K12, owner ruling 2026-09-26; `decisions-for-owner.md` line 144), Recommendation cell, which is the ruling text: "Approve the CR; Claude writes it and the four method changes." The row asks for "a CR to 04 rule 7.3.6 admitting Inspection for requirements that state a documentary or physical property, so REQ-SYS-122 (handbook content), REQ-SYS-124 (engraved legend), REQ-SYS-137 and REQ-SYS-138 (placement split) close by Inspection instead of Analysis." Decision 30 (same K12, Recommendation "REQ-SYS-122 moves to Inspection if decision 113 is approved") is consistent with it.

**Delta verification of `d992052` against 04 (`git show d992052 -- docs/process/04-verification-and-validation.md`, 3 hunks, 5 insertions, 3 deletions).**

| Change (04 line at HEAD) | Check | Result |
|---|---|---|
| Header, new paragraph "Changes after the SRR approval" (line 7) | Names CR-002 by path, SRR decision 113 and the ruling date, and lists the three places changed; consistent with the header's "Change authority: owner, via `CR-NNN` after SRR" | Correct |
| Section 3 paragraph "Hazard-tracing requirements" (line 68) | Inserts the Inspection route between the Test route and the Analysis route for non-software modules only; the `REQ-SW-*` sentence (every hazard-tracing `REQ-SW-*` by Test, SWE-192, RMM row FC) is unchanged, so no RMM or compliance row is contradicted (RMM row SWE-192 unchanged; `render_compliance.py --check` exit 0; `render_rmm.py --check` fails only on row SWE-033, cross item X7). The route is bounded to "a documentary or physical property" with the three named examples, which match the four requirements of the ruling. It agrees with the method rule in the preceding paragraph of the same section ("If it states a physical or documentary property, the method is Inspection"), which is the INSP-003 finding-17 contradiction the ruling cures. "Credit row `I`, section 5.2" exists: the section 5.2 table row `I` is Inspection, closing, credit event "CDR (design data), receipt (as-built), baselining review (documents)" | Correct |
| Rule 7.3.6 (line 248) | Three alternatives for a non-software hazard-tracing requirement (Test; Inspection with a closing Inspection case and the `Inspection accepted per CR-002` note; Analysis with a register risk); the software sentence and the `HAZARD_INVERSE` sentence are unchanged. Consistent with rule 3 (a case is closing only with the requirement's method and credit row `I` with Inspection) and with CR-002 section 1 item 2, which quotes the before and after text exactly | Correct |
| Section 7.4 row 7.3.6 (line 280) | Adds the tool change (accept the Inspection route) with an interim hand check by the procedure reviewer, recorded in the gate's traceability review; status stays "partly"; due PDR, matching CR-002 section 4 row Schedule ("item 7 before the PDR readiness declaration") | Correct; see finding-7 for the interim tool state |

No new defect in 04: 0 em dashes in the blob; no `TBD`, `TBR`, "as appropriate" or "should consider" added; no new SE, SWE or CFR citation; the finding-2 to finding-4 liens are untouched by the diff (their cited 04 line numbers are now 2 higher, because of the new header paragraph; the text they cite is unchanged). The applied change is the one the ruling ordered, no broader: it does not admit Inspection for any hazard control that states a number or behavior (CR-002 section 3 row 2 rejects that). CK-REQ-G1 and CK-REQ-G7 keep their answers (No, on the liens only); G2 to G4, G6 and G8 stay Yes for the changed text.

**Delta review of CR-002 (`73070823`, added at `d992052`).** Checked against the ruling and the tree: the before text of item 1 and item 2 matches `git show d992052^:docs/process/04-verification-and-validation.md`; the source row, the quoted recommendation and the decision 30 quotation match `decisions-for-owner.md` lines 143 and 144; INSP-003 finding-17 exists as cited (`requirements-sys.md` line 108); the "before" notes (RSK-016 for REQ-SYS-122 and 124, RSK-034 for REQ-SYS-137 and 138) match `git show cd61450^:docs/requirements/sys/requirements.json`; the hazard list of the Safety row matches the trace union `tools/traceability.py` reports for REQ-SYS-122; the CCB disposition (Approved, 2026-09-26, class to be confirmed) and the lifecycle departure (Dispositioned before the Class I Assessed state) are disclosed and logged as `docs/cm/deviations.md` entry 1 with a closure plan. Scope is correct: SWE-192, the RMM and the compliance matrix are unchanged. Two Minor findings follow.

**Implementation state at HEAD (steps 2 to 5, other authors' products; read, not reviewed here).** Step 2 is done at `cd61450` (the four requirements carry method Inspection and notes beginning `Inspection accepted per CR-002`); step 3 is done at `ebe5873` (TC-SYS-085, 086, 091 retyped; commit body "SRR decision 113 (CR-002 item 5)"); step 4 is not done (`docs/safety/hazard-analysis.md` line 261 still reads "close by the Analysis method accepted per RSK-016"); step 5 is not done, and `tools/traceability.py --report-only` at HEAD reports 4 violations, `HAZARD_REQ_NOT_TESTED` for REQ-SYS-122, 124, 137 and 138 ("has method Inspection and no verification_note beginning 'Analysis accepted per RSK-NNN'").

### Delta findings (2026-09-26, HEAD `ebe5873`)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-6"></a>finding-6 | reviewer | Minor | CK-REQ-G7 | CR-002 section 5 (column "Done (SHA)") and section 8 (implementation record) | The CR's implementation tracking is behind the tree: section 5 and section 8 record only step 1, but step 2 landed at `cd61450` and step 3 at `ebe5873`; neither commit carries the `CR: CR-002` trailer that section 8's "Trailer check" column records (`git show -s --format=%B cd61450 ebe5873`: decision 113 is cited in the body, no `CR:` line). Step 4 (hazard analysis section 8.1), scheduled "before the `baseline/srr` tag" in section 4 row Schedule, is not done (hazard-analysis line 261). Fix: fill section 5 and section 8 with `cd61450` and `ebe5873` and the trailer result; complete step 4 or re-date it; route step 4 to the hazard analysis author (cross item X5) | Lien: fix before PDR | Not needed | |
| <a id="finding-7"></a>finding-7 | reviewer | Minor | CK-REQ-G7 | CR-002 section 4 rows Verification and Schedule; section 5 closing paragraph | The impact assessment does not state the interim effect of landing steps 2 and 3 before step 5: from `cd61450` `tools/traceability.py --report-only` reports 4 `HAZARD_REQ_NOT_TESTED` violations for REQ-SYS-122, 124, 137 and 138 (observed at HEAD `ebe5873`), while SRR package section 4 criterion S4 ("Traceability report passes", Hard) was met on 0 violations and the `baseline/srr` tag follows R16. 04 itself is decision-complete on the point (row 7.3.6, line 280: the procedure reviewer checks the Inspection route by hand until the tool accepts it), so the defect is the CR's missing statement, not the plan. Fix: either move step 5 (tool rule and known-answer test) before the tag, or state in section 4 that the four violations are expected until step 5, are hand-checked per 04 row 7.3.6, and are recorded in the SRR traceability review (cross item X4) | Lien: fix before PDR | Not needed | |

Findings closed by the rulings: none needed. This record had no open Major finding before the rulings (finding-1 Verified at iteration 2, `33ac1ce`), and no ruling bears on the liens finding-2 to finding-4 (decisions 1, 30, 99 and 113 were checked; decision 1 approves 04 for the functional baseline on this record's APPROVED verdict, as recorded above). The liens stand unchanged, due at the PDR readiness declaration.

### Lien table (post-SRR-ruling delta)

| Finding | Severity | Disposition | Owner | Due |
|---|---|---|---|---|
| finding-2 | Minor | Lien: fix before PDR | 04 author (Claude, lead SE) | PDR readiness declaration |
| finding-3 | Minor | Lien: fix before PDR | 04 author (Claude, lead SE) | PDR readiness declaration |
| finding-4 | Minor | Lien: fix before PDR | 04 author (Claude, lead SE); `tools/traceability.py` owner if implemented instead of re-dated | PDR readiness declaration |
| finding-6 | Minor | Lien: fix before PDR | CR-002 originator (Claude) | PDR readiness declaration (step 4 part: before `baseline/srr` as CR-002 schedules it, or re-dated) |
| finding-7 | Minor | Lien: fix before PDR | CR-002 originator (Claude); `tools/traceability.py` owner for step 5 | PDR readiness declaration |

### Cross items (post-SRR-ruling delta; for the integrating session)

- X4: lead SE and `tools/traceability.py` owner: the tree at HEAD `ebe5873` gives 4 `HAZARD_REQ_NOT_TESTED` violations (REQ-SYS-122, 124, 137, 138) from CR-002 steps 2 and 3 without step 5. Before the `baseline/srr` tag, either implement CR-002 step 5 or record the hand check of 04 row 7.3.6 in the SRR traceability review and re-state package criterion S4.
- X5: hazard analysis author (INSP-008): CR-002 step 4 is open; `docs/safety/hazard-analysis.md` section 8.1 line 261 still closes REQ-SYS-122 and REQ-SYS-124 by "the Analysis method accepted per RSK-016".
- X7: RMM author: `tools/render_rmm.py --check` fails at HEAD `ebe5873` on row SWE-033 (status Planned while every named path exists); outside this record's products.
- X6: CR-002 section 6 (independent review of the impact assessment) is assigned to the INSP-003 reviewer; this delta does not perform it and does not close `docs/cm/deviations.md` entry 1.

**Tool runs (2026-09-26, HEAD `ebe5873`, repository root, `.venv/bin/python`).**

| Command | Exit | Result |
|---|---|---|
| `tools/validate_docs.py` (after writing this section) | 1 | 37 passed, 13 failed, 50 checked; this record PASS as APPROVED with the three `product_files` blobs at HEAD (record drift check included). The 13 failures are other SRR records (for example `hazard-analysis.md`, `test-cases-sys.md`, `conops-and-concept.md`) whose products changed in the R16 commits and whose reviewers re-issue them in this run; none is this record |
| `tools/traceability.py --report-only` | 0 | 245 requirements, 173 test cases, 4 violations (`HAZARD_REQ_NOT_TESTED` REQ-SYS-122, 124, 137, 138; finding-7), 2 warnings (`SYS_UNALLOCATED` REQ-SYS-125, REQ-SYS-148); `docs/vv/traceability-report.md` and `traceability.json` restored with `git checkout` |
| `tools/render_rmm.py --check` | 1 | one failure, row SWE-033 ("status 'Planned' but every named path exists"), not an 04 row and not touched by `d992052`; cross item X7 |
| `tools/render_compliance.py --check` | 0 | validation passed, render current |

**Measurements (delta).** Commits verified: 1 (`d992052`); product hunks checked: 4 in 04, 1 new file (CR-002); items re-checked: CK-REQ-G1 to G8, A8, R1, R4; new findings: 2 Minor, 0 Major; effort 22 turns, 30 minutes (added to the front matter totals).

```
POST-SRR-RULING DELTA (2026-09-26, HEAD ebe5873, package item R16): VERDICT: APPROVED (with liens)
COMMITS: d992052 (04 CR-002 step 1, SRR decision 113 (owner ruling 2026-09-26)): applies the ruling correctly; no new Major
FINDINGS: finding-1 Major Verified (unchanged); finding-5 Verified (unchanged); finding-2 to finding-4 Minor, Lien: fix before PDR (unchanged); new finding-6 and finding-7 Minor (CR-002 tracking and interim traceability state), Lien: fix before PDR; open Major 0
PRODUCT: docs/process/04-verification-and-validation.md@0b197bba, docs/vv/README.md@878869d3, docs/cm/cr/CR-002-inspection-for-documentary-requirements.md@73070823
MEASUREMENTS: commits=1; new major=0; new minor=2; lien=5; open_major=0; turns=22; minutes=30; cumulative turns=85, minutes=110
```

## Close-out delta (reviewer; SRR close-out items 5 and 7; 2026-09-26, HEAD `26011f1`)

Written by `reviewer:INSP-021`, the reviewer role of this record, not the author (charter section 11 rule 4; 08 section 3.1); the reviewer edited no product. Trigger: record drift reported by `tools/validate_docs.py`: `product_files` named CR-002 at blob `73070823` while HEAD holds `36224b45`. Rulings in force: the owner's close-out concurrence "I concur with your recommendations" (`docs/reviews/SRR/minutes.md`, section "Close-out decisions (after the first close-out run)", commit `dd39332`), items 1 to 12 ruled as recommended; item 5 reads "update `tools/traceability.py` now (CR-002 step 5), then re-validate and re-accredit it, rather than record a deviation"; item 7 reads "CR-002 is Class I". Convergence rule (charter section 4 item 3): only open Major findings and ruled work change products before the gate; new Minor findings are liens due PDR. Everything above this section stands as recorded.

**Search first.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` (query: SRR close-out item 5 traceability CR-002 step 5 brought forward before `baseline/srr`; item 7 CR-002 Class I) ran before any `grep`; `grep`, `git log` and `git show` were used afterwards only to pin lines, commits and blobs.

**Commits in scope.** `git log --oneline ebe5873..HEAD` over the three product files prints one commit, `bf654e6` ("TV-002 run 5 and CR-002 step 5 record ..."), which touches CR-002 only (9 lines: 6 insertions, 3 deletions; 4 hunks). 04 is unchanged (blob `0b197bba`) and `docs/vv/README.md` is unchanged (blob `878869d3`). The other files of `bf654e6` (`docs/cm/tool-validation/TV-002-traceability.md`, `tools/README.md`) and the tool commit `c774851` are not this record's products; they are reviewed by INSP-015 re-issue 3 (`26011f1`, APPROVED with liens), which is the independent review of TV-002 run 5. This record covers no tool validation record, so it makes no accreditation effective. Reviewed blobs at HEAD `26011f1`: 04 `0b197bba`, README `878869d3`, CR-002 `36224b45`; the working tree equals HEAD for all three.

**Delta verification of `bf654e6` against CR-002 (`git show bf654e6 -- docs/cm/cr/CR-002-inspection-for-documentary-requirements.md`).**

| Change (CR-002 line at HEAD) | Check | Result |
|---|---|---|
| Section 5 step 5 "Done (SHA)" cell (line 80): `c774851`, brought forward from the PDR readiness declaration to before the tag by close-out item 5, re-validation TV-002 run 5 | `c774851` exists and changes `tools/traceability.py` and `tools/tests/test_traceability.py` only; its message states rule 7.3.6 now accepts the `Inspection accepted per CR-002` route for modules other than `SW` and `SW-<SUB>`, which is CR-002 item 7 and 04 rule 7.3.6 (line 248). Close-out item 5 is quoted correctly from the minutes. Repository run at HEAD `26011f1`: `tools/traceability.py --report-only` exit 0, 245 requirements, 173 test cases, 0 violations, 2 warnings (`SYS_UNALLOCATED` REQ-SYS-125, 148); the four `HAZARD_REQ_NOT_TESTED` of finding-7 are gone. Known answers re-run: `unittest discover -s tools/tests -k InspectionRouteTests` ran 6 tests, OK | Correct |
| Section 7 "Class confirmed" (line 99) and new disposition history row (line 112) | Close-out item 7 "CR-002 is Class I" and the owner statement are quoted verbatim from `minutes.md`; the superseded value is kept inside the cell ("Before that ruling the field read: ..."), so no history is lost; the history row is appended, not rewritten | Correct |
| Section 8 implementation record, new row `c774851` (line 119) | `git show -s --format=%B c774851` carries the trailer `CR: CR-002`; the files listed match `git show --stat c774851` | Correct |
| Section 9 row "Tool rule" (line 131) | The verification evidence named (`InspectionRouteTests` variants, TV-002 run 5, 182 tests, TV-002 section 4.1 run R-2 exit 0 with 0 violations) matches TV-002 lines 29 to 35 and the repository run above; it states that the independent verification is by the INSP-015 delta, which is now done at `26011f1` (APPROVED with liens) | Correct; the cell's "pending" is now stale, see finding-8 |
| Section 10 new row (line 150) | Appended row, state Dispositioned, commit `c774851` and "the commit that records this row"; consistent with sections 5, 7 and 8 | Correct |

No new defect of Major weight: no requirement, method, hazard control, RMM or compliance row changes; the edit records work that the rulings ordered and that the tree confirms. 0 em dashes in blob `36224b45`; no `TBD`, `TBR`, "as appropriate" or "should consider" added; the one new citation (close-out items 5 and 7, `dd39332`) resolves. The CR still leaves some cells that `bf654e6` made stale (finding-8), and 04 row 7.3.6 now lags the tool (finding-9); both are documentary and Minor.

**Effect on earlier findings.**
- finding-7 (Minor, CR-002 interim traceability state): Verified. Its first fix alternative, "move step 5 (tool rule and known-answer test) before the tag", is what close-out item 5 ordered and `c774851` implemented; `bf654e6` records it in section 5 and section 8; the interim state the finding described no longer exists (0 violations at HEAD `26011f1`). Cross item X4 of the post-SRR-ruling delta is resolved by the same commits.
- finding-6 (Minor, CR-002 tracking): stays a lien. Section 5 and section 8 still record neither step 2 (`cd61450`) nor step 3 (`ebe5873`), neither commit carries `CR: CR-002` (`git show -s --format=%B cd61450 ebe5873 | grep -c '^CR:'` prints 0), and step 4 is still open (`docs/safety/hazard-analysis.md` line 261 still reads "close by the Analysis method accepted per RSK-016"; cross item X5 stands).
- finding-1 and finding-5 stay Verified; finding-2 to finding-4 stay liens (04 unchanged).

### Delta findings (2026-09-26, HEAD `26011f1`)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-8"></a>finding-8 | reviewer | Minor | CK-REQ-G7 | CR-002 line 64 (section 4 row Schedule), line 70 (classification rationale), line 121 (section 8), line 131 (section 9 row Tool rule) | `bf654e6` updated sections 5, 7, 8, 9 and 10 but left four statements that now contradict them: line 64 still schedules "item 7 before the PDR readiness declaration" though section 5 records it done before the tag under close-out item 5; line 70 still says "the class is confirmed at the next owner exchange" though section 7 records the confirmation; line 121 still reads "pending steps 2 to 5" though step 5 is done and the repository run gives 0 violations; line 131 still reads independent verification "pending" though INSP-015 re-issue 3 (`26011f1`) is APPROVED. Fix: re-state the four places as dated updates that keep the original text (as section 7 already does) | Lien: fix before PDR | Not needed | |
| <a id="finding-9"></a>finding-9 | reviewer | Minor | CK-REQ-G7 | 04 line 280 (section 7.4 row 7.3.6) | The row still lists the Inspection route under "missing" with "until the tool accepts it, the procedure reviewer checks each such requirement by hand", due PDR, and calls the tool change "CR-002 implementation step 3"; CR-002 section 5 numbers it step 5 (step 3 is the TC-SYS retyping), and since `c774851` the tool accepts the route. The wrong step number was introduced at `d992052` and not caught by the post-SRR-ruling delta; the "missing" text became stale at `c774851`. The `HAZARD_INVERSE` promotion part of the row is unaffected. Fix: move the Inspection route to the "implemented" column citing `c774851` and CR-002 step 5, under a CR-002 change note in the 04 header | Lien: fix before PDR | Not needed | |

### Lien table (close-out delta)

| Finding | Severity | Disposition | Owner | Due |
|---|---|---|---|---|
| finding-2 | Minor | Lien: fix before PDR | 04 author (Claude, lead SE) | PDR readiness declaration |
| finding-3 | Minor | Lien: fix before PDR | 04 author (Claude, lead SE) | PDR readiness declaration |
| finding-4 | Minor | Lien: fix before PDR | 04 author (Claude, lead SE); `tools/traceability.py` owner if implemented instead of re-dated | PDR readiness declaration |
| finding-6 | Minor | Lien: fix before PDR | CR-002 originator (Claude) | PDR readiness declaration (step 4 part: before `baseline/srr` as CR-002 schedules it, or re-dated) |
| finding-8 | Minor | Lien: fix before PDR | CR-002 originator (Claude) | PDR readiness declaration |
| finding-9 | Minor | Lien: fix before PDR | 04 author (Claude, lead SE) | PDR readiness declaration |

### Cross items (close-out delta; for the integrating session)

- X4: resolved by `c774851` and `bf654e6` (0 violations at HEAD `26011f1`); no action.
- X5 stands: CR-002 step 4 (hazard analysis section 8.1) is open; CR-002 schedules it before the `baseline/srr` tag.
- X6 stands: CR-002 section 6 (independent impact review) is still pending; close-out item 8 orders an RFA for it, due before PDR.
- X7: closed; `tools/render_rmm.py --check` exits 0 at HEAD `26011f1`.

**Tool runs (2026-09-26, HEAD `26011f1`, repository root, `.venv/bin/python`).**

| Command | Exit | Result |
|---|---|---|
| `tools/validate_docs.py` (after writing this section) | 0 | 50 passed, 0 failed, 50 checked; this record PASS as APPROVED with the three `product_files` blobs at HEAD (record drift check included) |
| `tools/traceability.py --report-only` | 0 | 245 requirements, 173 test cases, 0 violations, 2 warnings (`SYS_UNALLOCATED` REQ-SYS-125, REQ-SYS-148); `docs/vv/traceability-report.md` and `traceability.json` restored with `git checkout` |
| `unittest discover -s tools/tests -k InspectionRouteTests` | 0 | 6 tests, OK |
| `unittest discover -s tools/tests` | 0 | 415 tests, OK (before this section was written, `test_validate_docs.RepositoryTests.test_repository_exit_zero` failed on this record's drift only; it passes after it) |
| `tools/render_rmm.py --check` | 0 | 100 rows, render current |
| `tools/render_compliance.py --check` | 0 | validation passed, render current |

**Measurements (delta).** Commits verified: 1 (`bf654e6`, CR-002 part; `c774851` read for the step 5 claim); product hunks checked: 4 in CR-002; items re-checked: CK-REQ-G1, G7, A8, R1, R4; findings verified: 1 (finding-7); new findings: 2 Minor, 0 Major; effort 20 turns, 25 minutes (added to the front matter totals).

```
CLOSE-OUT DELTA (2026-09-26, HEAD 26011f1, SRR close-out items 5 and 7): VERDICT: APPROVED (with liens)
COMMITS: bf654e6 (CR-002 step 5 record and Class I confirmation): applies close-out items 5 and 7 correctly; no new Major
FINDINGS: finding-7 Verified (c774851, bf654e6); finding-1 and finding-5 Verified (unchanged); finding-2, 3, 4, 6 Lien (unchanged); new finding-8 and finding-9 Minor, Lien: fix before PDR; open Major 0
PRODUCT: docs/process/04-verification-and-validation.md@0b197bba, docs/vv/README.md@878869d3, docs/cm/cr/CR-002-inspection-for-documentary-requirements.md@36224b45
MEASUREMENTS: commits=1; new major=0; new minor=2; verified=1; lien=6; open_major=0; turns=20; minutes=25; cumulative turns=105, minutes=135
```

## Close-out item C delta (reviewer; SRR close-out item C; 2026-09-27, HEAD `08922d9`)

Written by `reviewer:INSP-021`, the reviewer role of this record, not the author (charter section 11 rule 4; 08 section 3.1); the reviewer edited no product and authored neither CR-002 nor its section 6 review. Trigger: record drift reported by `tools/validate_docs.py`: `product_files` named CR-002 at blob `36224b45` while HEAD holds `c007177f` (SRR package section 2.3, R13). Ruling in force: close-out item C (`docs/reviews/SRR/minutes.md`, section "Close-out decisions A to C and repository protection", commit `786822a`), which reads in part "perform all three impact reviews before the tag. This closes RFA-SRR-008 early." Convergence rule (charter section 4 item 3): only open Major findings and ruled work change products before the gate; new Minor findings are liens due PDR. Everything above this section stands as recorded.

**Search first.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` (query: CR-002 independent Class I impact review section 6 RFA-SRR-008) ran before any `grep`; `grep`, `sed -n`, `git log` and `git show` were used afterwards only to pin lines, commits and blobs.

**Commits in scope.** `git log --oneline 26011f1..HEAD` over the three product files prints one commit, `8b86c16` ("CM: independent Class I impact reviews of CR-002, CR-004 and CR-005 ..."), which changes CR-002 in one hunk (2 insertions, 2 deletions, section 6 only). Its CR-004 and CR-005 hunks are not this record's products. 04 is unchanged (blob `0b197bba`) and `docs/vv/README.md` is unchanged (blob `878869d3`). Reviewed blobs at HEAD `08922d9`: 04 `0b197bba`, README `878869d3`, CR-002 `c007177f`; the working tree equals HEAD for all three. This record covers no tool validation record, so it makes no accreditation effective.

**Delta verification of `8b86c16` against CR-002 (`git show 8b86c16 -- docs/cm/cr/CR-002-inspection-for-documentary-requirements.md`).**

| Change (CR-002 line at HEAD) | Check | Result |
|---|---|---|
| Section 6 table row (line 90): "Impact assessment" pending row filled as "Impact assessment, class", reviewer, date 2026-09-27, findings 1 to 3, resolution | Item C orders the review before the tag; the row names a separate reviewer and cites item C and `docs/cm/deviations.md` entry 4 for acting in place of the INSP-003 reviewer (entry 4 and its closure at `bb2485e` confirm). Evidence pinned: `docs/safety/hazard-analysis.md` lines 257 to 259, 261, 310, 110 and 169 and `docs/safety/hazards.json` HZ-015 `verification_note` and `residual_risk.condition` still state or imply the Analysis route (finding-1 of the review, same scope as INSP-008 finding-17); CR-002 `affected_cis` is `[2, 7, 15, 17, 28]` and omits rows 30 and 40 (its finding-2); 04 line 280 still lists the Inspection route as missing (its finding-3, the same defect as this record's finding-9). Class I agrees with close-out item 7. Known answer re-run: `unittest discover -s tools/tests -k InspectionRouteTests` ran 6 tests, OK. The review's statement that no finding changes the owner's basis holds: at HEAD the four requirements, three closing cases, 04 rule 7.3.6 and the tool carry the change and `tools/traceability.py --report-only` gives 0 violations | Correct |
| Section 6 concurrence line (line 92): "pending" replaced by "Concur with comments (findings 1 to 3, Minor) ..." | The superseded value is kept inside the line ("Before this review the line read: pending."); consistent with the table row | Correct |

No new defect of Major weight: the commit records a review that the ruling ordered, changes no requirement, method, hazard control, risk, RMM or compliance row, and its three findings are Minor and already carried as liens. 0 em dashes in blob `c007177f`; no `TBD`, `TBR`, "as appropriate" or "should consider" added; the new citations (`786822a`, deviations entry 4, `0da559a`, `d992052`, `cd61450`, `ebe5873`, `c774851`, `bfea9c7`, `bf654e6`, `26011f1`) resolve. One documentary gap remains (finding-10).

**Effect on earlier findings.**
- Cross item X6 of the post-SRR-ruling and close-out deltas (CR-002 section 6 pending): resolved by `8b86c16`; deviations entries 1 and 4 closed at `bb2485e`. RFA-SRR-008 is Answered in `docs/reviews/SRR/rfa-rid-log.json`; its verification is the owner's.
- finding-8 (Minor): stays a lien; `8b86c16` did not touch lines 64, 70, 121 or 131, and line 131's "pending" INSP-015 verification is still stale.
- finding-9 (Minor): stays a lien; the impact review raised the same defect as its finding-3, owner the 04 maintainer, due PDR.
- finding-6 (Minor): stays a lien; step 4 (hazard analysis section 8.1) is still open (line 261 unchanged), now also carried by the review's finding-1 and INSP-008 finding-17 to PDR. Cross item X5 stands with that re-dating.
- finding-1, finding-5 and finding-7 stay Verified; finding-2 to finding-4 stay liens (04 unchanged).

### Delta findings (2026-09-27, HEAD `08922d9`)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-10"></a>finding-10 | reviewer | Minor | CK-REQ-G7 | CR-002 line 86 (section 6 lead paragraph) and line 90 (section 6 table row) | `8b86c16` filled the section 6 table but left the lead paragraph reading "Not yet performed ... The independent reviewer of INSP-003 reviews this section together with step 2", which now contradicts the row below it, and it replaced the row's "pending (INSP-003 reviewer)" cell without keeping the prior value, unlike the concurrence line and unlike CR-005 section 6, which carries a dated "Superseded 2026-09-27" note. Fix: add a dated note after the lead paragraph that the review is recorded below under item C in place of the INSP-003 reviewer (deviations entry 4), and record the prior cell value | Lien: fix before PDR | Not needed | |

### Lien table (close-out item C delta)

| Finding | Severity | Disposition | Owner | Due |
|---|---|---|---|---|
| finding-2 | Minor | Lien: fix before PDR | 04 author (Claude, lead SE) | PDR readiness declaration |
| finding-3 | Minor | Lien: fix before PDR | 04 author (Claude, lead SE) | PDR readiness declaration |
| finding-4 | Minor | Lien: fix before PDR | 04 author (Claude, lead SE); `tools/traceability.py` owner if implemented instead of re-dated | PDR readiness declaration |
| finding-6 | Minor | Lien: fix before PDR | CR-002 originator (Claude) | PDR readiness declaration (step 4 part carried with INSP-008 finding-17 and the CR-002 impact review finding-1) |
| finding-8 | Minor | Lien: fix before PDR | CR-002 originator (Claude) | PDR readiness declaration |
| finding-9 | Minor | Lien: fix before PDR | 04 author (Claude, lead SE) | PDR readiness declaration |
| finding-10 | Minor | Lien: fix before PDR | CR-002 originator (Claude, configuration manager) | PDR readiness declaration |

### Cross items (close-out item C delta; for the integrating session)

- X5 stands: CR-002 step 4 (hazard analysis section 8.1) is open at HEAD `08922d9`; CR-002 section 4 row Schedule still places it before the `baseline/srr` tag, while INSP-008 finding-17 and the CR-002 impact review finding-1 carry it to PDR. The baseline record should show it as a lien, not a tag blocker, or the CR Schedule row should be re-dated by a dated note.
- X6: resolved by `8b86c16` and `bb2485e`.

**Tool runs (2026-09-27, HEAD `08922d9`, repository root, `.venv/bin/python`).**

| Command | Exit | Result |
|---|---|---|
| `tools/validate_docs.py` (before this section) | 1 | 49 passed, 1 failed; the one failure is this record (record drift on CR-002) |
| `tools/validate_docs.py` (after writing this section) | 0 | 50 passed, 0 failed, 50 checked; this record PASS as APPROVED with the three `product_files` blobs at HEAD (record drift check included) |
| `tools/traceability.py --report-only` | 0 | 245 requirements, 173 test cases, 0 violations, 2 warnings (`SYS_UNALLOCATED` REQ-SYS-125, REQ-SYS-148); `docs/vv/traceability-report.md` and `traceability.json` restored with `git checkout` |
| `unittest discover -s tools/tests -k InspectionRouteTests` | 0 | 6 tests, OK |
| `unittest discover -s tools/tests` | 0 | 424 tests, OK |
| `tools/render_rmm.py --check` | 0 | `docs/process/rmm.md` is current |
| `tools/render_compliance.py --check` | 0 | validation passed, render current |
| `tools/render_risk.py --check --gate SRR --hazards docs/safety/hazards.json` | 0 | `docs/risk/register.md` is current |

**Measurements (delta).** Commits verified: 1 (`8b86c16`, CR-002 part; `bb2485e` read for the deviations closure); product hunks checked: 1 in CR-002; items re-checked: CK-REQ-G1, G7, A8, R1, R4; findings verified: 0; new findings: 1 Minor, 0 Major; effort 12 turns, 15 minutes (added to the front matter totals).

```
CLOSE-OUT ITEM C DELTA (2026-09-27, HEAD 08922d9, SRR close-out item C, RFA-SRR-008): VERDICT: APPROVED (with liens)
COMMITS: 8b86c16 (CR-002 section 6 independent Class I impact review): applies close-out item C correctly; no new Major
FINDINGS: finding-1, 5, 7 Verified (unchanged); finding-2, 3, 4, 6, 8, 9 Lien (unchanged); new finding-10 Minor, Lien: fix before PDR; open Major 0
PRODUCT: docs/process/04-verification-and-validation.md@0b197bba, docs/vv/README.md@878869d3, docs/cm/cr/CR-002-inspection-for-documentary-requirements.md@c007177f
MEASUREMENTS: commits=1; new major=0; new minor=1; verified=0; lien=7; open_major=0; turns=12; minutes=15; cumulative turns=117, minutes=150
```

## CR-013 delta (reviewer; CR-013 SRR record re-issue; 2026-09-29, branch head `41c588c`)

Written by `reviewer:INSP-021`, a new invocation of this record's reviewer role (plan rule C4), acting also as the WP-PDR-55 configuration manager for the CR-013 merge. It authored no part of CR-013, of WP-PDR-13, of CR-010 or of either branch commit, and it edited no product. Trigger: CR-013 (`docs/cm/cr/CR-013-process-04-07-semp-srr-liens.md`, Class II, Approved 2026-09-28) changes 04 from blob `0b197bba` (`baseline/srr`) to `7617007e`, so this APPROVED record fails the record drift rule (SRR package section 2.3, R13) wherever the new blob is at HEAD. CR-013 section 6.1 IR-F1 asks for this update: the PDR delta record INSP-058 (`docs/reviews/PDR/checklists/process-04-verification-and-validation.md`) verified the same blob but does not change this record's `product_files`. The re-issue is committed on the CR branch, records only, as CR-010 section 5 step 5 does for its records, so that the merge brings the blob and the record that names it into `main` in one commit. Everything above this section stands as recorded.

**Search first.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` (query: CR-013 merge batch 1 pre-merge checks section 9 SRR record re-issue) ran before any `grep`; `grep`, `git show`, `git diff` and `git ls-tree` were used afterwards only to pin lines, commits and blobs.

**Commits in scope.** `git log --oneline ab2af2d..41c588c -- docs/process/04-verification-and-validation.md` prints one commit, `41c588c` (the CR-013 prototype, `CR: CR-013`); the CR-010 commit `5cd87cf` does not touch 04. `git log ab2af2d..main` over 04 is empty, so `main` still holds `0b197bba` and the merge brings `7617007e` unchanged. README `878869d3` and CR-002 `c007177f` are unchanged on the branch and on `main` (`git rev-parse` at both). Reviewed blobs at `41c588c`: 04 `7617007e` (603 lines), README `878869d3`, CR-002 `c007177f`.

**Delta verification of `41c588c` against this record's liens (`git diff --word-diff 5cd87cf 41c588c -- docs/process/04-verification-and-validation.md`; line numbers of blob `7617007e`).**

| Finding | Fix at | Checked against | Result |
|---|---|---|---|
| finding-2 (a) | Line 82 (section 4 Emulation row) cites `ACC-EMU-001` as "an `ACC-<TOOL>-NNN` identifier of charter section 6 held inside that TV record"; line 602 (C1) reads Resolved against charter `4e3f891` | Charter section 6 on `main` line 111: "`ACC-<TOOL>-NNN` accreditation scope statement, held inside its TV-NNN record (e.g. ACC-EMU-001)" | Verified |
| finding-2 (b) | Line 82: "`firmware/emu/` (harness, vendoring form and file format fixed by the PDR emulator ADR, 07 sections 1.2 and 9.4)"; `cwht-emu` removed | `git show 41c588c:docs/process/04-verification-and-validation.md \| grep -c cwht-emu` is 0; 07 names no such crate | Verified |
| finding-3 (a) | Line 150: `sigrok-cli` and the sigrok-pico capture firmware not installed, lock section 1 carries a row for each with its TV due TRR, A13 resolved | `tools/toolchain.lock.md` on `main` lines 47 and 48: both rows "Not installed", "TV pending (due TRR)" | Verified |
| finding-3 (b) | Line 417 (section 10.6): `tpm.json` registers TPM-019 (`ncr-trend`), preliminary at SRR, owner decides at PDR (SE-40; SEMP F-14; A12 resolved) | `docs/plan/tpm.json` on `main` lines 969 and 970: `TPM-019`, key `ncr-trend` | Verified |
| finding-3 (c) | Line 523 (section 14 row 4.2) cites RSK-059; line 597 (A10) reads Resolved | `docs/risk/register.json` on `main` line 5129: RSK-059 "No qualification testing at the environmental extremes" | Verified |
| finding-3 (d) | Line 571 (section 17): 01 section 3.5 labels the rows "Customized (NA)", A14 resolved | 01 on `main` line 141: "**Customized (NA):** the item is omitted for an institutional or physical reason" | Verified |
| finding-4 (a) | Lines 278 and 281 (rows 7.3.2 and 7.3.5): due PDR, re-dated in line with 02 T-19; row 7.3.2 states the SRR report gave the retired count (2) without the list | 02 section 8.5 row T-19 on `main` line 559, Due column "PDR"; `docs/reviews/SRR/traceability-report.md` "Requirements Retired: 2", no list; `tools/traceability.py` on `main` has no `VAL_PHASE_MISSING` (grep count 0), so the rows are correctly not marked implemented | Verified |
| finding-4 (b) | Line 262 and the `unittest` row: re-observed 2026-09-27 at `main` `7bb994f` in a clean worktree, tool blob `12de3545` committed at `c774851` | `git rev-parse 7bb994f:tools/traceability.py` and `c774851:tools/traceability.py` both `12de3545`; `git log 7bb994f..main -- tools/traceability.py` is empty, so the observation still describes the tool on `main`. The file count "16" is wrong (15 modules at `7bb994f`): INSP-058 finding-1, not repeated | Verified (with INSP-058 finding-1 carried there) |
| finding-4 (c) | Line 99 (section 4 tool accreditation): `tools/ltspice-batch.sh` (ADR-018; `41d150e`; `tools/tests/test_ltspice_batch.py`; TV-014, not accredited on 2026-09-27) | `git ls-tree main`: `tools/ltspice-batch.sh`, `tools/tests/test_ltspice_batch.py` and `docs/cm/tool-validation/TV-014-ltspice-batch.md` exist; `41d150e` is "tool(ltspice): add the headless LTspice batch wrapper" | Verified |
| finding-9 | Line 282 (row 7.3.6): the Inspection route "Implemented, no longer open", accepted by `HAZARD_REQ_NOT_TESTED` since `c774851` (CR-002 step 5; `InspectionRouteTests`); line 7 header note records CR-002 step 5; the `HAZARD_INVERSE` promotion stays open and names CR-011 | `tools/tests/test_traceability.py` on `main` line 283 `class InspectionRouteTests`; CR-002 section 5 numbers the tool change step 5. The sentence sits in the "Open task" column, not the "Check codes today" column the finding named: INSP-058 finding-2 (placement, Minor), not repeated | Verified (placement remainder carried by INSP-058 finding-2) |

**Rest of the diff.** The other hunks (header Status, the CR-013 change note, rows 7.3.4, 7.3.11, 7.3.12 and the option sentence naming CR-011, section 12 target-only entries, section 18 A3 and A4 re-dated) were read for new defects. The only one of weight is the 7.3.4 Due cell, which moves `CLOSED_NOT_INSTALLED` from CDR to PDR: INSP-058 finding-3 and CR-013 section 6.1 IR-F3, both open and not repeated here. The A3 and A4 statements hold on `main` (`rmm.json` `meta` has no NPR 8705.2 note; row SWE-071 still names the planned stale-test option). 0 em dashes in blob `7617007e`; no bare `TBD`, "as appropriate" or "should consider" added. No new Major.

**Effect on earlier findings.** finding-2, finding-3, finding-4 and finding-9 move from Lien to Verified (the SRR liens this record carried against 04 are closed on blob `7617007e`). finding-6, finding-8 and finding-10 are defects of the CR-002 record, not of 04; CR-013 section 1.4 routes them to WP-PDR-47 (carried item C-096), and they stay liens. finding-1, finding-5 and finding-7 stay Verified.

**Lien table (CR-013 delta).**

| Finding | Severity | Disposition | Owner | Due |
|---|---|---|---|---|
| finding-6 | Minor | Lien: fix before PDR | CR-002 originator (Claude); WP-PDR-47 | PDR readiness declaration |
| finding-8 | Minor | Lien: fix before PDR | CR-002 originator (Claude); WP-PDR-47 | PDR readiness declaration |
| finding-10 | Minor | Lien: fix before PDR | CR-002 originator (Claude, configuration manager); WP-PDR-47 | PDR readiness declaration |

**Validity of this re-issue.** The record names 04 blob `7617007e`. If the CR-013 author changes 04 before the merge (CR-013 section 6.1 IR-F2 re-observation of section 7.4, or IR-F3 on row 7.3.4), this record fails the drift rule again and needs a further delta by this role before the merge.

**Tool runs (2026-09-29, CR-013 worktree at `41c588c` plus this edit, `.venv/bin/python`).**

| Command | Exit | Result |
|---|---|---|
| `tools/validate_docs.py` (before this section) | 1 | 43 passed, 7 failed; this record fails the drift rule on 04 `0b197bba` |
| `tools/validate_docs.py` (after this section) | 1 | this record PASS (APPROVED, the three named blobs at HEAD); the remaining failures are the other SRR records of CR-010 and CR-013 (see the CR-013 section 9 pre-merge check) |

**Measurements (delta).** Commits verified: 1 (`41c588c`, 04 part); product hunks checked: 19 in 04 (`git diff -U0`); findings verified: 4 (finding-2, 3, 4, 9); new findings: 0; effort 14 turns, 25 minutes (added to the front matter totals).

```
CR-013 DELTA (2026-09-29, branch cr/CR-013-process-04-07-semp-srr-liens head 41c588c): VERDICT: APPROVED (with liens)
COMMITS: 41c588c (CR-013 prototype, 04 part): closes finding-2, 3, 4 and 9; no new Major
FINDINGS: finding-1, 2, 3, 4, 5, 7, 9 Verified; finding-6, 8, 10 Lien (CR-002 record, WP-PDR-47); new 0; open Major 0
PRODUCT: docs/process/04-verification-and-validation.md@7617007e, docs/vv/README.md@878869d3, docs/cm/cr/CR-002-inspection-for-documentary-requirements.md@c007177f
MEASUREMENTS: commits=1; new major=0; new minor=0; verified=4; lien=3; open_major=0; turns=14; minutes=25; cumulative turns=131, minutes=175
```
