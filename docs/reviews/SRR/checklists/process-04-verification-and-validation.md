---
id: INSP-021
checklist: peer-review-checklist-requirements
checklist_revision: C
checklist_file: docs/reviews/SRR/checklists/process-04-verification-and-validation.md
product: docs/process/04-verification-and-validation.md
# product_commit: the review baseline HEAD (the product files were last changed at b301df2 (04) and 4e3f891 (docs/vv/README.md))
product_commit: "adcfe0946d2f1b5cd8f41a8f91eb4219a7fb99a1"
# product_files: committed blobs verified at iteration 2 (git rev-parse HEAD:<path> at HEAD 33ac1ce4822c9571d8fb4797c58e7c0f0152f41f); iteration 1 reviewed 04 blob ecff54d70d1c3bb8c90be0803f4b9720596adfc0 at adcfe09
product_files: ["docs/process/04-verification-and-validation.md@76bb24c3f3f43c1f7d3eb1b1be156824488153a8", "docs/vv/README.md@878869d346d936e4ad38ef5a51ef18175a0774fa"]
product_size: 18 sections (599 lines) plus docs/vv/README.md (35 lines)
sprint: SRR-prep
author_agent: "author:process-04 (Claude main session, lead SE; maintainer per the 04 header)"
reviewer_agent: "reviewer:INSP-021"
criticality: neither
# assurance_required: false; 07 section 2.1.1 row "Other process documents (docs/process/0N-*.md except 03, 05 and this plan)" is No
assurance_required: false
assurance_reviewer_agent: none
iteration: 2
# readiness_met: false because R3 (author self-check) is still not on record; see finding-5
readiness_met: false
# reviewer_verdict: finding-1 Verified at iteration 2; every Minor finding is "Lien: fix before PDR" (convergence rule of 2026-09-26)
# verdict: held at NEEDS CHANGES only by readiness R3 (validate_docs.py: APPROVED needs readiness_met true), as in INSP-019;
# it becomes APPROVED (with liens) on re-issue once the author self-check is filed or the owner waives it (decision 115)
reviewer_verdict: APPROVED
assurance_verdict: not-required
verdict: NEEDS CHANGES
findings_major: 1
findings_minor: 4
findings_open: 0
findings_fixed: 0
findings_verified: 1
# the four Minor findings are liens "fix before PDR" (convergence rule of 2026-09-26), listed in the lien table, not Deferred RIDs
findings_deferred: 0
assurance_findings_major: 0
assurance_findings_minor: 0
assurance_tasks_applied: []
deferred_rids: []
items_no: [CK-REQ-G1, CK-REQ-G7, R3]
effort_turns: 57
effort_minutes: 70
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
| <a id="finding-5"></a>finding-5 | reviewer | Minor | R3 | author return | No author self-check of 04 or `docs/vv/README.md` against checklist sections G and A8, and no brief acceptance criteria, came with this assignment or exist in the repository (claude-context search for an 04 author self-check found none; section 18 is an alignment list, not a self-check). Readiness R3 is not met and `readiness_met` is false. Fix: the 04 author files the self-check with the next re-review brief, or Robin extends package decision 115 to this record. | Lien: fix before PDR | Pending (decision 115) | |

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
| finding-5 | Minor | Lien: fix before PDR | 04 author, or Robin (decision 115) | PDR readiness declaration |

## Readiness criteria

| # | Criterion | Answer | Evidence |
|---|---|---|---|
| R1 | The product validates: `tools/validate_docs.py` exits 0 | Yes | 04 and the README are Markdown without a schema convention; run 2026-09-26 at HEAD: `validate_docs: 37 passed, 0 failed, 37 checked`, exit 0 |
| R2 | `tools/traceability.py` reports no violation for the ids in the file | N/A (a plan defines no REQ or TC ids) | `traceability.py --report-only` exit 0: 237 requirements, 170 test cases, 0 violations, 2 warnings (`SYS_UNALLOCATED` REQ-SYS-125, REQ-SYS-148; not 04 ids) |
| R3 | Author self-check against sections A to G and the brief's acceptance criteria | No | finding-5 |
| R4 | Every `TBR` has owner, plan, close_by; no `TBD` | Yes | `grep -n -w 'TBD\|as appropriate\|should consider'` on both files: no hit; open questions OQ-VV-001 to 003 name owner and gate (04 lines 186 to 190); em dash count 0 in both files |
| R5 | For a CR: impact assessment attached | N/A | Not a CR |

`readiness_met: false` (R3).

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

Iteration 1 (2026-09-26, HEAD `adcfe09`): findings: 5. Open 1 (finding-1, Major); Lien 4 (finding-2 to finding-5, Minor, fix before PDR); Closed 0; Disputed-accepted 0. Under the convergence rule the open Major finding changes the product; the record is NEEDS CHANGES until finding-1 is fixed and verified. Even with finding-1 closed, readiness R3 (finding-5) keeps the record NEEDS CHANGES until the self-check is filed or Robin waives it under decision 115, as for INSP-001, 002 and 010.

```
VERDICT: NEEDS CHANGES
PRODUCT: docs/process/04-verification-and-validation.md@ecff54d7, docs/vv/README.md@878869d3 (HEAD adcfe09)
FINDINGS:
- [Major] finding-1 CK-REQ-G1 04 sections 6, 6.3, 13, 14, 16, 18 C2: "receipt ADR" contradicts charter section 9 (receipt-inspection report and TV-NNN record). Open.
- [Minor] finding-2 CK-REQ-G1 04 section 4, C1: ACC-EMU-001 is now a charter section 6 identifier; cwht-emu not in 07. Lien: fix before PDR.
- [Minor] finding-3 CK-REQ-G7 04 lines 146, 413, 519, 567: stale statements against the lock, tpm.json TPM-019, RSK-059, 01 section 3.5. Lien: fix before PDR.
- [Minor] finding-4 CK-REQ-G7 04 section 7.4: two "before SRR" tool rows unimplemented and dated PDR in 02; stale observation; wrapper name. Lien: fix before PDR.
- [Minor] finding-5 R3: no author self-check. Lien: fix before PDR (decision 115).
ITEMS N/A: CK-REQ-A1 to A7, B1 to B7, C1 to C8, D1 to D4, E1 to E6, F1 to F4 (plan); CK-REQ-G5 (cybersecurity is in 07 section 16)
MEASUREMENTS: size=18 sections + README; items=14; no=3; turns=45; minutes=55; major=1; minor=4; lien=4; open_major=1; iteration=1
```
