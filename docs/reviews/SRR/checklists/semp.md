---
id: INSP-005
checklist: peer-review-checklist-requirements
checklist_revision: C
checklist_file: docs/reviews/SRR/checklists/semp.md
product: docs/plan/semp.md
# product_commit: git hash-object of the working-tree file reviewed (blob; the file is uncommitted on top of HEAD 28e49e6); iteration 1 reviewed blob e129c710a71c616377b635e9a9097112313a3350, iteration 2 verified the fixes in the blob below
product_commit: "2f0588fab3411acfb37342c08f374172da6a52c7"
# product_files: the committed SEMP blob (git rev-parse HEAD:docs/plan/semp.md at 400e59d) that the delta verification of 2026-09-26 (iteration 3, R13) approves
product_files: ["docs/plan/semp.md@77fc9ea43527d838a1d92c54cdb332868c1ab450"]
product_size: 9 sections plus appendices A to F (480 lines)
sprint: SRR-prep
author_agent: "author:semp (Claude main session, lead SE; H16 AL-02-26 revision)"
reviewer_agent: "reviewer:semp"
criticality: neither
assurance_required: false
assurance_reviewer_agent: none
iteration: 3
readiness_met: true
reviewer_verdict: APPROVED
assurance_verdict: not-required
verdict: APPROVED
findings_major: 1
findings_minor: 9
findings_open: 0
findings_fixed: 0
findings_verified: 9
findings_deferred: 1
assurance_findings_major: 0
assurance_findings_minor: 0
assurance_tasks_applied: []
deferred_rids: []
items_no: [CK-REQ-G1, CK-REQ-G7, S1, S2]
effort_turns: 80
effort_minutes: 90
record_status: Open
date: 2026-09-25
date_closed: null
---

# Peer review record INSP-005: SEMP (`docs/plan/semp.md`)

Checklist: `docs/templates/peer-review-checklist-requirements.md` revision C, product type "Plans and process documents" (section G, all items, and A8), the plan review items that `docs/process/08-agent-briefing.md` section 3.1 assigns to plans. Two supplementary items S1 and S2 record the minimum content this review was asked to judge: SE-38 (SEMP per SE HB App. J) and SE-66 (baselined HSI approach). Gate fed: SRR (entrance criterion 9 of `01-lifecycle-and-reviews.md` section 4.3; package `docs/reviews/SRR/package.md` section 2 item H1 and H16 item AL-02-26).

Independence: the reviewer did not author the SEMP and did not edit it. Search first: `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` preceded every manual search; `grep -n` was used only to pin hits.

## Record

### Findings

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to | Disposition (iteration 2) |
|---|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | reviewer | Major | CK-REQ-G1 | SEMP section 3.0 line 41 (Influencing factors); section 6.0 table row "Bench instruments" line 307 | The SEMP says the tinySA Ultra "receipt is recorded by ADR before TRR, closing OQ-VV-001", and line 307 cites charter section 9 for it. Charter section 9 (00-charter.md line 130) says the receipt "is recorded by a receipt-inspection report and a TV-NNN record before TRR, closing OQ-VV-001". The plan contradicts its parent on a TRR control and attributes the contradiction to the charter (08 section 3.2: violating the charter is Major). Fix: use the charter wording at both places (receipt-inspection report `docs/vv/reports/receipt-inspection-<n>.md` plus `docs/cm/tool-validation/TV-NNN-<tool>.md`). | Verified | Pending | | Closed. Section 3.0 line 41 and section 6.0 row "Bench instruments" line 309 now read "recorded by a receipt-inspection report `docs/vv/reports/receipt-inspection-<n>.md` and a tool validation record `docs/cm/tool-validation/TV-NNN-<tool>.md` before TRR, closing OQ-VV-001", matching charter section 9 line 130; "by ADR" occurs 0 times in the SEMP |
| <a id="finding-2"></a>finding-2 | reviewer | Minor | CK-REQ-G1 | Header "Version" row line 7; section 3.4 line 98; section 4.1 line 167; Appendix E OQ-SE-004; Appendix F F-03 and F-10 | The SEMP is aligned to charter commit b8214ca, but the charter changed at 4e3f891 (`git log -- docs/process/00-charter.md`). As a result: (a) section 3.4 says "Charter §3 still words DR/DRR as 'not applicable beyond archiving'", but charter section 3 line 39 now reads "DR and DRR not held; SE-55 and SE-56 tailored by deviation (compliance matrix)", so F-03 is already resolved; (b) section 4.1 says charter section 12 words the SWE-017 tailoring as "familiarization records", but charter section 12 line 157 now says the intent "is met by brief-time reading lists (`docs/process/08-agent-briefing.md` §2)". That makes OQ-SE-004 and F-10 moot, and "The owner's familiarization is recorded per charter §12" is no longer true. Fix: realign the header to 4e3f891; mark F-03 and F-10 resolved; withdraw OQ-SE-004 or restate it (cross: package section 13 decision 5 and `decisions-for-owner.md` item 5). | Verified | Pending | | Closed. Header Version row line 7 aligned to 4e3f891 and lists its changes; section 3.4 line 100 states DR and DRR not held with SE-55 and SE-56 Tailored (deviation), matching charter line 39; section 4.1 line 169 states the charter section 12 wording (brief-time reading lists, no familiarization record), matching charter line 157; OQ-SE-004 Withdrawn (line 455); F-03 (line 466) and F-10 (line 473) marked Resolved. The cross items outside the SEMP (`decisions-for-owner.md` item 5 still offers the withdrawn choice) are reported to the orchestrator |
| <a id="finding-3"></a>finding-3 | reviewer | Minor | CK-REQ-G7 | Section 3.2 line 67; section 4.3 table row "Allocation" and paragraph lines 183 to 185; section 7.2 rows "Firmware" and "Documentation data"; section 7.4 line 392 | Several tool-status claims are not true of the tree reviewed. (a) Rule T-18 is called "planned" (3.2) and "not yet implemented" (4.3). `tools/traceability.py` line 303 implements `SYS_UNALLOCATED` (Warning at SRR, Error from PDR), and `docs/vv/traceability-report.md` lines 369 and 370 list REQ-SYS-125 and REQ-SYS-148. (b) `tools/sw_gate.sh` exists (gates G0 to G6), but 4.3 says it is "planned with the first software sprint". (c) The known-answer test list in 4.3 omits `test_git_known_answer.py`, `test_render_review_figures.py` and `test_traceability_srr_rules.py` in `tools/tests/`, and the tool `tools/render_review_figures.py` is named nowhere. (d) Section 7.4 says to run the jsonschema one-liner "until `tools/validate_docs.py` gains the convention (§4.3)". Section 4.3 says `validate_docs.py` validates `tpm.json` today, and `tools/validate_docs.py` line 107 has the `tpm` convention (run output: `PASS docs/plan/tpm.json`), so 7.4 contradicts 4.3. Fix: restate each tool's status at the baseline commit and delete the obsolete interim command. Several of these files are uncommitted, so date each statement against the commit that baselines the SEMP. | Verified | Pending | | Closed. Section 3.2 line 67 and section 4.3 row Allocation line 185 state T-18 `SYS_UNALLOCATED` implemented (Warning at SRR, Error from PDR), true of `tools/traceability.py` line 303; line 187 dates tool status to the SRR closure revision and marks untracked items *new*, states `tools/sw_gate.sh` exists (G0 to G6), names `tools/render_review_figures.py`, and lists all 11 files of `tools/tests/` (checked by `ls`); section 7.2 rows Firmware (line 327) and Documentation data agree; the section 7.4 interim jsonschema one-liner is gone and 7.4 now says `validate_docs.py` checks `tpm.json` by convention, consistent with 4.3 |
| <a id="finding-4"></a>finding-4 | reviewer | Minor | CK-REQ-G1 | Sections 3.1 line 53, 3.2 line 67, 5.6 line 235, 6.0 line 303, 7.2 row "Firmware" line 325 | The SEMP names a workspace crate `cwht-emu` and an emulator candidate `rp2350-emu`. `07-software-engineering-plan.md` section 1.2 (line 26) places emulation scenarios in `firmware/emu/`, with the harness fixed by the PDR emulator ADR. Section 9.4 (line 380) names c1570/rp2350js at `af0114cb` or Renode as candidates. `firmware/Cargo.toml` members are `cwht-app`, `cwht-core` and `cwht-hal-mock` only, and `firmware/emu/README.md` is a placeholder. Fix: use the 07 names and candidates (cross: 08 section 1 repo map carries the same `cwht-emu` name). | Verified | Pending | | Closed. `cwht-emu` and `rp2350-emu` occur 0 times; sections 3.1 (line 55), 3.2 (line 69, crates `cwht-app`, `cwht-core`, `cwht-hal-mock` plus the `firmware/emu/` placeholder), 5.6 (line 237) and 7.2 (line 327) use `firmware/emu/`; section 6.0 line 305 names c1570/rp2350js at `af0114cb` or Renode per 07 section 9.4 |
| <a id="finding-5"></a>finding-5 | reviewer | Minor | S2 | Section 7.3.1 "HSI requirements" paragraph and table, rows "Power steps" and "Display legibility" | The HSI approach baselined for SE-66 is not reconciled with the L1 HSI set that now exists. (a) The paragraph still says "Minimum set to be defined by SRR" and cites no requirement ids, although the hsi-tagged REQ-SYS-057 to REQ-SYS-070 and REQ-SYS-165 exist (package section 13 item 2). (b) The Power steps row states "tune carrier at 0.5 W for at most 10 s". REQ-SYS-020 is "at most 5.5 s (TBR)" and the ConOps uses 5 s +/-0.5 s (package section 15 item 14, decision 36). (c) The Display row states "readable at arm's length in full sun" while REQ-SYS-165 sets 0.5 m at 300 lux (TBR). Fix: give each table row its REQ-SYS ids and make the values agree with L1 or point to the pending owner decision (decision 36; decision 77). | Verified | Pending | | Closed. Section 7.3.1 HSI requirements paragraph cites REQ-SYS-057 to REQ-SYS-070 and REQ-SYS-165 and makes the L1 file governing; Power steps row gives 0.5 W (TBR) and at most 5.5 s (TBR) with REQ-SYS-019 and REQ-SYS-020 and decision 36; Display row gives 0.5 m under 300 lux (TBR) with REQ-SYS-165 and decision 77. Values checked against `requirements.json` descriptions of REQ-SYS-019, 020, 061 and 165 |
| <a id="finding-6"></a>finding-6 | reviewer | Minor | CK-REQ-G1 | Section 5.0 table row "Product Validation"; section 8.0 line 417; Appendix F F-12; section 2.0 SWEHB row | Several numbers disagree with their sources. (a) "MOEs validated: 12 of 12 at SAR": `expectations.json` holds 13 MOEs (MOE-013 "Pocket carry and field ruggedness", Draft). (b) "USD 850 to 1670" is the unit budget basis without the instrument. It is the `cost-estimate.md` totals (970, 1830) minus only the tinySA line (120, 160), so the instrument's share of the 20 % contingency stays in. The non-instrument lines give 690 + 138 = 828 low and 1370 + 274 = 1644 high. (c) F-12 says the RSK-008 condition "does not name hardware TRL 3", but the `register.json` RSK-008 condition now does ("the RF hardware is at TRL 3 at the CDR procurement re[lease]"). Only the acceptance record remains open. (d) "268 pages scraped": charter section 1 says 267 files, 130 of them SWE pages, and `docs/references/md/swehb/` holds 267 files. Fix: correct each value, or state its basis. | Verified | Pending | | Closed. (a) Section 5.0 Product Validation row line 202 reads 13 of 13, MOE-001 to MOE-013; `expectations.json` holds 13 MOEs. (b) Section 8.0 line 415 reads USD 828 to 1644 with the basis stated (line items without the instrument, 690 to 1370, plus 20 % contingency); recomputed from `cost-estimate.md` lines 13 to 15: 970 - 160 - 120 = 690, 1830 - 300 - 160 = 1370, times 1.2 = 828 and 1644. (c) F-12 line 475 marks the condition part resolved and keeps only the acceptance record open; `register.json` RSK-008 condition names TRL 3 at the CDR procurement release. (d) Section 2.0 SWEHB row reads 267 files, 130 SWE pages, as charter section 1 line 14 |
| <a id="finding-7"></a>finding-7 | reviewer | Minor | CK-REQ-G1 | Section 3.4 gate table, TRR row | The TRR criteria source reads "Table G-10 (plus Table G-9 items 3.1 and 3.2)". `01-lifecycle-and-reviews.md` section 7.3 (line 482) tailors from "Table G-10, plus SIR Table G-9 items 3.1, 3.2 and 8". Fix: add item 8. | Verified | Pending | | Closed. Section 3.4 TRR row line 94 reads "Table G-10 (plus Table G-9 items 3.1, 3.2 and 8)", matching 01 section 7.3 |
| <a id="finding-8"></a>finding-8 | reviewer | Minor | S1 | Section 3.0 Technical Summary | SE HB App. J section 3.0 lists nine key questions. Question 5, "How will we know when we have adequately defined the problem?", has no answer. The problem, influencing factors, critical questions, constraints, customers, users, priorities and related projects are all answered. Fix: add one sentence, for example the SRR success criteria of 01 section 4.4 and the V1 to V6 validation of every L1 requirement. | Verified | Pending | | Closed. Section 3.0 now has the paragraph "Adequate definition of the problem" (line 47): the twelve SRR success criteria of 01 section 4.4 (12 rows counted) ruled Met or Met with lien, and V1 to V6 passed for every L1 requirement in `checklists/requirements-sys.md` with zero open Major RIDs. App. J section 3.0 key question 5 is answered |
| <a id="finding-9"></a>finding-9 | reviewer | Minor | CK-REQ-G1 | Appendix B (Templates) | Appendix B lists the checklists without `peer-review-checklist-safety.md` and `peer-review-checklist-visual-product.md`, which now exist in `docs/templates/`. It also says "Checklists still due are listed ... in 08 §3.5", which is out of date: only `analysis` and `software-assurance` remain due. Fix: add the two templates. | Verified | Pending | | Closed. Appendix B line 442 lists `peer-review-checklist-safety.md` and `peer-review-checklist-visual-product.md` (both present in `docs/templates/`) and states that only `analysis` and `software-assurance` remain due (08 section 3.5) |

Finding rules as in the template. The reviewer writes `Pending` in the owner ruling column. The state appears only in the State column. The disposition column was added at iteration 2: Closed means the fix was verified in the product blob named by `product_commit` (State `Verified`); no finding was disputed.

### Per-requirement validation

Not applicable: the product is a plan, not a requirement file (checklist product-type table).

## Readiness criteria

| # | Criterion | Answer | Evidence |
|---|---|---|---|
| R1 | The product validates | Yes (for the product) | The SEMP is Markdown and has no `validate_docs.py` convention. `tpm.json` and its schema, which the SEMP owns, give `PASS docs/plan/tpm.json`. The overall run exits 1 on `docs/design/allocation.json` (schema `docs/design/allocation.schema.json` not found), a file outside this product (reported under cross) |
| R2 | traceability.py reports no violation for ids in the file | N/A | A plan carries no requirement ids. `traceability.py --report-only`: 231 requirements, 108 test cases, 82 violations, 52 warnings, none attributable to the SEMP |
| R3 | Author's self-check and acceptance criteria stated | Yes | The author summary in the assignment reports the H16 AL-02-26 change (section 9.0 customization list, row 10) and the pointer from section 5.2 |
| R4 | TBR fields complete; no bare TBD | Yes | `grep -n TBD` shows only measure names ("TBD and TBR count in ICDs", section 5.12, TPM-020); no bare TBD; no em dash (count 0) |
| R5 | CR impact assessment | N/A | Not a CR |

## Participants

Author agent (not present): Claude main session as lead SE, author of the SEMP. Reviewer agent: `reviewer:semp`. Software assurance reviewer: not required. The SEMP is not a product of 07 section 2.1.1, and this checklist's participants section names only 07, the software section of `docs/vv/plan.md` and 03 for plans. Owner: dispositions the findings.

## A. Format and editorial

| Id | Answer | Evidence |
|---|---|---|
| CK-REQ-A1 to CK-REQ-A7 | N/A | The product type table limits plans to section G and A8 |
| CK-REQ-A8 | Yes | Terms follow NPR 7123.1D App. A, and Appendix A defines the project terms (gate, delta TRR, DML, PBS element, hand-assembly list, status note). Key types read "straight key" and "iambic paddles" as in L1 (REQ-SYS-038, REQ-SYS-039). Keyer modes in section 7.3.1 match REQ-SYS-040 (Straight, Iambic A, Iambic B, Ultimatic, Bug) |

## B to F

| Id | Answer | Evidence |
|---|---|---|
| CK-REQ-B1 to B7, C1 to C8, D1 to D4, E1 to E6, F1 to F4 | N/A | Requirement-file items; not applicable to a plan (checklist product-type table) |

## G. Plans, process documents and decision records (SWE-087 b)

| Id | Answer | Evidence |
|---|---|---|
| CK-REQ-G1 | No | Checked against charter sections 1 to 12, `se-compliance-matrix.json` (SE-44, SE-51, SE-52, SE-55, SE-56, SE-61, SE-65, SE-66 rows), `rmm.json`, 01 sections 3.5, 4.3 and 7.3, 05 section 1 and 07 sections 1.2, 9.4 and 14.1. Consistent: gates and absorbed reviews (charter section 3); the safety-critical and mission-critical component list (section 7.1 equals charter section 10); baselines and the two 05 section 1 baseline customizations; the SE-44 NA and SE-51, SE-52, SE-55 and SE-56 T dispositions; the SE-65 and SE-66 FC rows naming the SEMP HSI section. Disagreements: finding-1 (charter section 9), finding-2 (charter sections 3 and 12, stale alignment), finding-4 (07 sections 1.2 and 9.4), finding-6 (expectations.json, cost-estimate.md, register.json, charter section 1), finding-7 (01 section 7.3), finding-9 (08 section 3.5 and `docs/templates/`) |
| CK-REQ-G2 | Yes | Every process row of the section 5.0 table names its work products with paths and CM class, its ID scheme and the gate from which a CR is needed. Every open owner question carries an `OQ-SE-NNN` id, a "needed by" review and a default (Appendix E). No "as appropriate" or "should consider" (grep). The section 7.3.1 TBR rule names `close_by: PDR` |
| CK-REQ-G3 | Yes | Section 4.1 role table (owner as DA, PM, ETA, SMA TA, HMTA, CCB; Claude; author, reviewer and test-author agents; vendors). Independence of the TA and its residual risk are covered by OQ-SE-002, citing NPR 7123.1D sections 2.1.6.4 and 2.1.6.5 (verified in `npr-7123-1d/02-chapter2.md` lines 86 and 94). Approval points are named per process in the 5.0 table and in section 3.4 |
| CK-REQ-G4 | Yes | Section 9.0 mirrors the matrix dispositions (SE-44 NA; SE-51, SE-52, SE-55 and SE-56 T; SE-62 FC). The RMM tailorings it relies on are cited: SWE-219 (sections 5.14 and 7.1), SWE-017 (section 4.1), SWE-211 (section 5.5) and SWE-154 group (section 7.6). The customization list keeps tailoring out, per charter section 1 |
| CK-REQ-G5 | N/A | The SEMP carries no cybersecurity section of its own. Section 7.6 points to charter section 12 and 07 section 16 (exists, line 631), which is reviewed under the 07 record |
| CK-REQ-G6 | Yes | Section 5.0 gives a measure and target for each process. Section 7.4 names TPM source (`tpm.json`), thresholds (`conventions.status_rule`), storage (history entries with `credit`), reporting interval (identical to `tpm.json` `conventions.reporting_interval`, verified) and the red-TPM rule. The count "20 MOPs and 20 TPMs" was verified (20 and 20), and all 20 TPM ids, keys and `mop_id` links in the section 7.4 table equal `tpm.json` |
| CK-REQ-G7 | No | Checked against `tools/toolchain.lock.md` (kicad-cli 10.0.6, OpenSCAD 2021.01, FreeCAD 1.1.3, nightly-2026-08-24 rows exist) and against the repository tree. The SEMP states the tool limits honestly: no Rust MC/DC instrumentation, emulator for event ordering only, OpenSCAD cannot write STEP. It also states `tools/ltspice-batch.sh` and `tools/scad2step.py` are uncommitted, which is still true. Status claims out of date or self-contradictory: finding-3 |
| CK-REQ-G8 | Yes | Verified in the corpus (search, then `grep -n`): NPR 7123.1D sections 2.2.2.2, 2.1.6.4, 2.1.6.5, 3.1.5.10, 3.2.1, 5.1.5, 5.1.6, 5.2.1.3, 5.2.2.2 (including the "not held" and "combined" sentences), 5.2.2.6, 5.2.2.7 [SE-57], 5.2.3.1, 6.1.1.5, 6.2.2, 6.2.4, and App. G section G.9 with Table G-8 ("typically greater than three or as determined by the project") and Table G-19. Also verified: App. E TRL 4 and TRL 5 definitions; SE-06 to SE-23, SE-35 to SE-43, SE-45 to SE-48, SE-51 to SE-69 at their stated reviews (`05-chapter5.md` lines 62 to 127); SE HB section 4.2.1.2.3 quote "A KDR can have any priority or criticality" (verbatim, `05-4-2-technical-requirements-definition.md`); SE HB sections 3.11.4.2 and 3.11.4.3; SE HB section 6.5.1.2.2 (functional baseline at SDR, as-deployed baseline); SE HB section 6.7.1.2.1 (colour-coded alert zones); SE HB App. J sections J.1 and 7.4 trend list; App. R section 5.2.1; NPR 7150.2D section 3.7.4 [SWE-219] and its note. Regulatory: 47 CFR 97.307(e) (25 µW at 5 W is 53 dBc, as TPM-007 states), 97.313(a), 97.13(c)(1), and FCC 19-126 footnote 143 (no portable exemption below 239 MHz). No NASA requirement is presented as a quotation it is not. |

## Supplementary items (minimum content judged for SRR)

| Id | Check | Answer | Evidence |
|---|---|---|---|
| S1 | SE-38: the SEMP follows SE HB App. J and is ready to baseline at SRR (NPR 7123.1D sections 5.2.2.2 b(1) and 6.2.4; 01 section 4.3 row 9) | No (Minor gap only) | All App. J sections are present and in order. Title and signatory block: header table. Sections 1.0 to 3.6 (3.2 includes the PBS and WBS explanation). Section 4.0: all 17 specialty topics, with NEPA and launch approval dispositioned. Sections 4.1 to 4.3. Section 5.0: the App. J section 5.0 items as table columns for all 17 processes (SE-07 to SE-23, verified), plus 5.1 to 5.17. Sections 6.0, 7.1 to 7.6, 8.0 (answers the four key questions) and 9.0 (matrices plus the NPR section 2.2.2.2 customization list, rows 1 to 10). Appendices glossary, templates, plan summary, references. Update points follow NPR section 6.2.2 (verified). The H16 AL-02-26 item is closed: row 10 exists and section 5.2 points to it. Gaps: finding-8 (App. J section 3.0 key question 5); the consistency findings 1 to 4, 6, 7 and 9 |
| S2 | SE-66: a baselined HSI approach (NPR 7123.1D section 5.2.1.3 [SE-65]; section 5.2.2.2 b(3) [SE-66]) | No (Minor) | Section 7.3.1 follows the App. R outline: relevance; domains and roles, with co-ownership by ETA, SMA TA and HMTA as section 5.2.1.3 requires; requirements; methods and products by phase; entry and exit criteria per gate. It covers the section 5.2.1.3 human populations: operators and users (owner, friends), maintainers (cells, firmware) and assemblers (owner's hand soldering, "Charging, firmware update and hand soldering" row). It routes HSI risks through the register (App. R section 5.3). The decision not to write a stand-alone HSI Plan cites section 5.2.1.3 accurately and is correctly left to the owner as project manager (OQ-SE-001, customization row 6). Gap: finding-5 |

## Measurements (SWE-089)

| Measure | Value |
|---|---|
| Product size | 9 sections plus appendices A to F, 483 lines |
| Items checked | 11 (G1 to G8, A8, S1, S2), plus R1 to R5 |
| Items answered No | 4 (G1, G7, S1, S2) |
| Items N/A | A1 to A7, B to F (37 items), G5 |
| Findings by severity | Major 1, Minor 8 |
| Findings fixed, deferred | 0, 0 |
| Findings verified at iteration 2 | 9 (Major 1, Minor 8) |
| Iteration | 2 |
| Effort | 75 turns, 75 minutes (iteration 1: 45 turns, 50 minutes; iteration 2: 30 turns, 25 minutes) |

## Verdict

```
VERDICT: NEEDS CHANGES
FINDINGS:
- [Major] CK-REQ-G1 SEMP 3.0 and 6.0: tinySA receipt "recorded by ADR" contradicts charter section 9 (receipt-inspection report and TV-NNN record).
- [Minor] CK-REQ-G1 header, 3.4, 4.1, App. E OQ-SE-004, App. F F-03, F-10: stale alignment to charter b8214ca; F-03 and F-10 already resolved in the charter.
- [Minor] CK-REQ-G7 3.2, 4.3, 7.2, 7.4: T-18, sw_gate.sh, test list and tpm.json convention statuses out of date or self-contradictory.
- [Minor] CK-REQ-G1 3.1, 3.2, 5.6, 6.0, 7.2: cwht-emu and rp2350-emu versus 07 firmware/emu/ and rp2350js or Renode.
- [Minor] S2 7.3.1: HSI table not reconciled with the hsi-tagged L1 set; 10 s tune versus REQ-SYS-020.
- [Minor] CK-REQ-G1 5.0, 8.0, F-12, 2.0: MOE count 12 versus 13, unit budget arithmetic, stale F-12, SWEHB 268 versus 267.
- [Minor] CK-REQ-G1 3.4 TRR row: Table G-9 item 8 missing.
- [Minor] S1 3.0: App. J key question 5 unanswered.
- [Minor] CK-REQ-G1 App. B: two existing checklist templates missing from the list.
ITEMS N/A: CK-REQ-A1 to A7, B1 to B7, C1 to C8, D1 to D4, E1 to E6, F1 to F4 (plan), CK-REQ-G5 (cybersecurity is in 07 section 16)
MEASUREMENTS: size=9 sections + App. A to F; items=11; no=4; turns=45; minutes=50; major=1; minor=8
```

The block above is the iteration 1 verdict, kept as filed.

## Closure (iteration 2)

Re-review of the author's fixes (return: fixed finding-1 to finding-9, disputed none) against the working-tree SEMP, blob `2f0588fab3411acfb37342c08f374172da6a52c7` (480 lines, uncommitted on top of HEAD 28e49e6). Same reviewer role, new invocation; the reviewer did not edit the product. Search first: `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` preceded the manual `grep -n` pins. Each finding was checked at the cited SEMP line and against its source (charter lines 14, 39, 130 and 157; `tools/traceability.py` line 303; the `tools/tests/` listing; `requirements.json`; `expectations.json`; `cost-estimate.md`; `register.json` RSK-008; 01 sections 4.4 and 7.3; `docs/templates/`).

| Finding | Severity | Disposition | Where closed |
|---|---|---|---|
| finding-1 | Major | Closed | SEMP lines 41 and 309 |
| finding-2 | Minor | Closed | SEMP lines 7, 100, 169, 455, 466, 473 |
| finding-3 | Minor | Closed | SEMP lines 67, 185, 187, 327, section 7.4 |
| finding-4 | Minor | Closed | SEMP lines 55, 69, 237, 305, 327 |
| finding-5 | Minor | Closed | SEMP section 7.3.1 paragraph and rows Power steps, Display legibility |
| finding-6 | Minor | Closed | SEMP lines 202, 415, 475 and the section 2.0 SWEHB row |
| finding-7 | Minor | Closed | SEMP line 94 |
| finding-8 | Minor | Closed | SEMP line 47 |
| finding-9 | Minor | Closed | SEMP line 442 |

Regression pass on the revised product: no em dash (count 0); no bare TBD (the five TBD hits are the TPM-020 measure name and the review-agenda "TBD/TBR list"); no new inconsistency with the charter found in the changed passages.

Counts: 9 findings, 9 Closed (Verified), 0 Disputed accepted, 0 Open; open Major 0, open Minor 0.

Residual outside the product (not a finding against the SEMP): `docs/reviews/SRR/decisions-for-owner.md` item 5 and package section 13 decision 5 still offer the withdrawn OQ-SE-004 choice between "familiarization records" and the RMM wording; they are reported to the lead SE as a cross item.

```
VERDICT (iteration 2): APPROVED
FINDINGS: none open (finding-1 to finding-9 Verified)
MEASUREMENTS: size=9 sections + App. A to F, 480 lines; verified=9; open=0; major_open=0; minor_open=0; iteration=2
```

`record_status` stays `Open` for the lead SE to set `Closed` with `date_closed` (07 section 10.2: the software lead closes the record once every finding is Verified or Deferred, which is now the case).

## Delta verification (iteration 3, 2026-09-26, SRR package items R13 and H17)

**Scope.** The iteration 2 approval named the working-tree blob `2f0588fa`, which is not in the git object store; the committed SEMP is blob `77fc9ea4` (`git rev-parse HEAD:docs/plan/semp.md` at `400e59d`, first committed at `b301df2`). The package names the edits made after the approval (package section 2.3, R13): appendix F items F-07 and F-13 resolutions with the new cost totals, and the tool and schema status text of lines 130 and 187. The verifier is the integrator invocation of 2026-09-26, which did not author the SEMP (charter section 11 rule 4). Search first: `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any `grep` (queries on the TPM-014 cost envelope and on the tool status text).

| Changed passage (committed blob `77fc9ea4`) | Checked against | Result |
|---|---|---|
| Appendix F F-07 (line 470): resolved 2026-09-26, the assessment reports DML-n with the section 6.0 TRL mapping | `docs/plan/technology-assessment.md` lines 16 to 18 (committed): the DML scale with its App. E TRL mapping | Consistent |
| Appendix F F-13 (line 476): instrument line outside the unit budget, each contingency exactly 20 %, unit total USD 828 to 1644 for three units under ADR-025 | `docs/plan/cost-estimate.md` lines 5, 14, 15, 17, 18: unit budget 828 to 1644, contingency 20 % on each line, total envelope 972 to 1836 | Consistent; also consistent with finding-6 (b) and with `docs/plan/tpm.json` TPM-014 as updated 2026-09-26 (cbe 548, low 276) |
| Line 130: `docs/plan/measurements.json` SRR seed exists (2026-09-25, appended 2026-09-26), schema `measurements.schema.json` | Both files exist and `tools/validate_docs.py` validates `measurements.json` against the schema (PASS, 2026-09-26) | Consistent |
| Line 187: tool status at the SRR closure revision | `tools/` on 2026-09-26 | One stale statement, finding-10 below |

<a id="finding-10"></a>**finding-10, Minor, Lien: fix before PDR.** Location: section 4.3 line 187. Line 187 says `tools/measurements.py` is "planned with the first software sprint, 07 §11" and does not name `tools/unsafe_audit.py`, `tools/complexity_gate.py` or their known-answer tests (`test_unsafe_audit.py`, `test_complexity_gate.py`, `test_measurements.py`); all three tools and tests exist and are committed with the SRR closure products of 2026-09-26 (TV-011 to TV-013). Fix: restate the tool status at the next SEMP revision. Citation: CK-REQ-G7 (plan statements true of the tree). Disposition under the convergence rule of 2026-09-26 (charter section 4 item 3: a Minor RID is fixed before the next review and does not block the baseline): Lien, fix before PDR, carried by the package as a Routine item.

**Lien table.**

| Finding | Severity | Disposition | Owner | Due |
|---|---|---|---|---|
| finding-10 | Minor | Lien: fix before PDR | SEMP author (Claude, lead SE) | PDR readiness declaration |

**Result.** The committed SEMP blob `77fc9ea4` carries every iteration 2 fix (finding-1 to finding-9 re-checked at the lines the iteration 2 closure names; the line numbers are unchanged) and the post-approval edits are consistent with their sources, except the Minor finding-10, which is a lien. Findings: 10, of which 9 Closed (Verified) and 1 Lien; open Major 0.

```
VERDICT (iteration 3, delta verification): APPROVED (with liens)
PRODUCT: docs/plan/semp.md@77fc9ea43527d838a1d92c54cdb332868c1ab450
FINDINGS: finding-10 Minor, Lien: fix before PDR
MEASUREMENTS: verified=9; lien=1; open_major=0; iteration=3; turns=5; minutes=15
```
