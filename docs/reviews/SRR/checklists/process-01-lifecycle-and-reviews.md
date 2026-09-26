---
# Peer-review record (charter section 5; 01 section 13; 08 section 3.2). Copy of
# docs/templates/peer-review-checklist-requirements.md, product type "Plans and process documents"
# (section G, all items, and A8). Slug process-01-lifecycle-and-reviews as assigned by the dispatching
# session (01 section 13 would give plan-01-lifecycle-and-reviews; package H1 (c) names that slug; see Cross items X-1).
id: INSP-019
checklist: peer-review-checklist-requirements
checklist_revision: C
checklist_file: docs/reviews/SRR/checklists/process-01-lifecycle-and-reviews.md
product: docs/process/01-lifecycle-and-reviews.md
# product_commit: last commit touching 01 at the review baseline HEAD adcfe0946d2f1b5cd8f41a8f91eb4219a7fb99a1
# (the four templates were last touched at 4e3f8913366c60e79a9ace6a1b4f36f24adc3479); the working tree equals HEAD for all five files
product_commit: "b301df2f96aa979b602c0c4cde9c7f85da979843"
# product_files: git rev-parse HEAD:<path> at adcfe09 (record drift rule, package section 2.3, R13); the example log is
# reviewed with its schema (08 section 3.5 row "review-package.md, decision-memo.md, rfa-rid-log.schema.json, rfa-rid-log.example.json")
product_files: ["docs/process/01-lifecycle-and-reviews.md@eabbbd57953c84164e848f36dc327542ac015c00", "docs/templates/review-package.md@4ed480e2438fc6d81a673519dc537f09c3d43fbb", "docs/templates/decision-memo.md@1d3ce437a3fb1ae053068b8e363fe90780064c5a", "docs/templates/rfa-rid-log.schema.json@38898b0c260c3292fbc65c59d632790ad4e650f7", "docs/templates/rfa-rid-log.example.json@0e913114286a3099875f4c9fd67f2b0ce5ef67cd"]
product_size: 01 in 15 sections, 955 lines; review-package.md 21 sections, 305 lines; decision-memo.md 13 sections, 159 lines; rfa-rid-log.schema.json 305 lines; example log 5 items
sprint: SRR-prep
author_agent: "author:process (Claude main session, lead SE; 01 revision of b301df2, templates of 4e3f891)"
reviewer_agent: "reviewer:INSP-019"
criticality: neither
# assurance_required: false; 07 section 2.1.1 row "Other process documents (docs/process/0N-*.md except 03, 05 and this plan)"
# is No in every column, and tools/validate_docs.py ASSURANCE_WHOLE_PRODUCTS does not list 01
assurance_required: false
assurance_reviewer_agent: none
iteration: 1
# readiness_met: false because R3 (author self-check against sections A to G) is not on record for 01 or the templates; see Readiness
readiness_met: false
# reviewer_verdict: no Major finding; every Minor finding is "Lien: fix before PDR" (convergence rule of 2026-09-26)
# verdict: held at NEEDS CHANGES only by readiness R3 (not a finding), as in INSP-006, INSP-010 and INSP-022;
# it becomes APPROVED (with liens) on re-issue once the author self-check is filed or the owner waives it (decision 115)
reviewer_verdict: APPROVED
assurance_verdict: not-required
verdict: NEEDS CHANGES
findings_major: 0
findings_minor: 5
findings_open: 0
findings_fixed: 0
findings_verified: 0
# findings_deferred: the 5 liens (fix before PDR)
findings_deferred: 5
assurance_findings_major: 0
assurance_findings_minor: 0
assurance_tasks_applied: []
deferred_rids: []
items_no: [CK-REQ-G1, CK-REQ-G2]
effort_turns: 45
effort_minutes: 55
record_status: Open
date: 2026-09-26
date_closed: null
---

# Peer review record INSP-019: life cycle, review gates and RFA/RID process (01) and the review templates

**Products:** `docs/process/01-lifecycle-and-reviews.md` (committed at `b301df2`, blob `eabbbd57`), with the review templates it governs: `docs/templates/review-package.md` (`4ed480e2`), `docs/templates/decision-memo.md` (`1d3ce437`), `docs/templates/rfa-rid-log.schema.json` (`38898b0c`) and its example `rfa-rid-log.example.json` (`0e913114`), all committed at `4e3f891` and unchanged to HEAD `adcfe0946d2f1b5cd8f41a8f91eb4219a7fb99a1`. The working tree equals HEAD for the five files (`git status --short docs/process docs/templates` prints nothing). **Checklist:** `docs/templates/peer-review-checklist-requirements.md` revision C, section G (CK-REQ-G1 to G8) and CK-REQ-A8, per its product-type table row "Plans and process documents" (the plan review items of `docs/process/08-agent-briefing.md` section 3.1). **Minimum content judged:** SE-32 (review plans), SE-34 (entrance and success criteria), SE-57 and SE-64 as `docs/process/se-compliance-matrix.json` records them; charter sections 3 and 4. **SRR context:** package `docs/reviews/SRR/package.md` section 2 item H1 (c) (record `plan-01-lifecycle-and-reviews` not yet filed) and 01 section 3.3 C5 (this reviewer records the Topic 7.09 check).

**Independence:** the reviewer did not author 01 or the templates and edited neither. **Search first:** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before every manual search (queries: SWEHB Topic 7.09 Process Asset Template checklists; `PEER_REVIEW_RECORD_SCHEMA` required fields; author self-check and decision 115). `grep -n` was used afterwards only to pin lines and identifiers in the corpus and the repository.

## Record

### Findings

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | reviewer | Minor | CK-REQ-G1 | 01 section 15 preamble (line 945) and item 2 (line 950); section 3.5 row "Decommissioning and disposal plans" (line 155) | Section 15 item 2 still reads "Open: owner decision, carried as a charter issue in the SRR package proposed-tailoring section". The charter at HEAD (blob `131608b7`, last changed at `4e3f891`) already carries all three requested changes: line 39 (E / F row) "DR and DRR not held; SE-55 and SE-56 tailored by deviation (compliance matrix)"; line 41 "SAR carries the ORR and FRR products SE-69, SE-51, SE-52, SE-53, SE-54"; line 163 gives SE-51 and SE-52 as "tailored: ORR combined with SAR; scope relief to the operations-handbook end-of-life ... relative to App. G Tables G-17 and G-18". The preamble's status basis ("verified by the integrating session on 2026-09-25 ... every target file is still untracked at commit b8214ca") is stale for the same reason, and the section 3.5 row still says "section 15 item 2 corrects the charter's stated basis". Fix: mark item 2 Resolved at `4e3f891`, re-date the preamble to the commit that baselines 01, and drop the parenthesis in the section 3.5 row. | Lien: fix before PDR | Pending | |
| <a id="finding-2"></a>finding-2 | reviewer | Minor | CK-REQ-G1 | 01 section 13, row "Peer review record" (line 899) | The row calls itself "the single field list, copied from `PEER_REVIEW_RECORD_SCHEMA` in `tools/validate_docs.py`". At HEAD the schema also defines `product_files` (path@blob list) and `product_blob` (`tools/validate_docs.py` lines 193 to 197; `tools/README.md` line 39: "optional `product_files` and `product_blob` patterns added 2026-09-26"), and the validator applies the record drift rule: an APPROVED record fails when it names no blob or a blob that differs from HEAD (`validate_docs.py` header lines 56 to 66, `DRIFT_RULE` line 761). 01 names neither field nor the rule, so the process document no longer states a condition that decides whether a record can read APPROVED. Fix: add both optional fields and the drift rule (with its lead SE direction of 2026-09-26 and package section 2.3 basis) to the row. | Lien: fix before PDR | Pending | |
| <a id="finding-3"></a>finding-3 | reviewer | Minor | CK-REQ-G1 | 01 section 14, closing sentence (line 941) | "The compliance matrix rows for these identifiers cite this document by section." Checked against `docs/process/se-compliance-matrix.json` at HEAD: SE-32, SE-33, SE-34 and SE-47 cite `docs/process/01-lifecycle-and-reviews.md`, and SE-48 and SE-51 to SE-56 cite "01 section" in their justification; SE-35 to SE-46, SE-57, SE-60 to SE-64, SE-66 to SE-69 do not cite 01 at all (a scripted scan of every field of each row). The sentence is false for 23 of the rows the section 14 table maps. Fix: either reword the sentence to "01 cites the matrix rows", or have the matrix author add the 01 section to each row's `implementation_ref` (cross X-3). | Lien: fix before PDR | Pending | |
| <a id="finding-4"></a>finding-4 | reviewer | Minor | CK-REQ-G2 | 01 section 4.6 rows SWE-087 a and SWE-087 b (lines 259 and 260); section 13 slug list (line 899); section 2.1 row "Independent peer review or inspection" (line 57) | Record paths and the checklist set in 01 do not match the SRR record set and the templates at HEAD. (a) Section 4.6 names `docs/reviews/SRR/checklists/plan-07-software-engineering-plan.md` and `requirements-sw-<sub>.md`; the filed records are `software-plan-07.md` (INSP-010) and `requirements-tx-and-sw-keyer.md` (INSP-004). (b) Section 13 gives the slug rule `<type>-<product-stem>` with `plan-<document-stem>` and `risk-register`; the filed SRR slugs include `semp`, `cm-plan-05`, `risk-register-06`, `hazard-analysis`, `fw-b0-toolchain-proof`, `process-08-agent-briefing` and this record, and the list names no slug for the safety and visual-product checklists. (c) Section 2.1 lists the checklists as `peer-review-checklist-{requirements,design,code,test}.md`; `docs/templates/` at HEAD also holds `-risk`, `-classification`, `-safety` and `-visual-product`. A reader following 01 cannot locate the SRR evidence by the stated paths. Fix: state the slug rule the SRR set actually uses (or rename the records at re-issue) and list every checklist template, pointing to 08 section 3.5 as the single table. | Lien: fix before PDR | Pending | |
| <a id="finding-5"></a>finding-5 | reviewer | Minor | CK-REQ-G1 | `docs/templates/decision-memo.md` section 7.1 table (lines 95 to 103) | The template says "Each approval in the 03 section 9 signature block has its own line", but its table has five lines and the 03 section 9 block (`docs/process/03-software-classification-and-rmm.md` lines 382 to 395) has six: the table omits "Same risk accepted by Robin as official spokesperson for bystanders and household members (section 2.2.1; 03 section 4.4)". Its classification line names one concurrence `INSP-<NNN>` with the classification checklist, where 03 line 395 names two, INSP-009 (peer review) and INSP-017 (software assurance). A memo filled row by row from the table would omit a human-safety risk acceptance and one of the two concurrences. The template's own sentence governs, which is why this is Minor, but the SRR memo is written from this template before PDR (cross X-4). Fix: add the bystander line and name both concurrence records. | Lien: fix before PDR | Pending | |

Finding rules as in the template. The reviewer writes `Pending` in the owner ruling column, and the state appears only in the State column. No finding is Major: none makes a requirement, interface, hazard control or regulatory item wrong, none contradicts the charter on a rule, and every NASA citation checked is accurate (08 section 3.2 severity definition). Each is a stale status, an internal inconsistency or an incomplete list, of the kind recorded as Minor in INSP-005 finding-2 and finding-9 and INSP-022 finding-1 and finding-2.

### Lien table (convergence rule, charter section 4 item 3)

| Finding | Severity | Disposition | Owner | Due | Package carriage |
|---|---|---|---|---|---|
| finding-1 | Minor | Lien: fix before PDR | 01 author (Claude, lead SE) | PDR readiness declaration | Routine item (package section 20.1 L-4) |
| finding-2 | Minor | Lien: fix before PDR | 01 author (Claude, lead SE) | PDR readiness declaration | Routine item |
| finding-3 | Minor | Lien: fix before PDR | 01 author (Claude, lead SE); compliance-matrix author if the matrix is changed (cross X-3) | PDR readiness declaration | Routine item |
| finding-4 | Minor | Lien: fix before PDR | 01 author (Claude, lead SE) | PDR readiness declaration | Routine item |
| finding-5 | Minor | Lien: fix before PDR | Decision-memo template author (Claude, lead SE); the SRR memo writer applies the fix in the SRR memo itself (cross X-4) | PDR readiness declaration (template); SRR memo (memo content) | Routine item |

Lien count: 5. Open Major: 0.

### Per-requirement validation

Not applicable: the products are a process document and templates, not requirement files (checklist product-type table).

## Readiness criteria

| # | Criterion | Answer | Evidence |
|---|---|---|---|
| R1 | The product validates: `tools/validate_docs.py` exits 0 | Yes | Run 2026-09-26 at HEAD `adcfe09` (working tree) before this record: exit 0. 01 and the two Markdown templates have no schema convention; the schema validates its own example (`PASS docs/templates/rfa-rid-log.example.json` by convention; also the 10.6 fallback one-liner on the example: `ok`) |
| R2 | `tools/traceability.py` reports no violation for the ids in the file | N/A | The products define no REQ or TC ids. `traceability.py --report-only`: 237 requirements, 170 test cases, 0 violations, 2 warnings (REQ-SYS-125, REQ-SYS-148 `SYS_UNALLOCATED`), exit 0; the regenerated `docs/vv/traceability-report.md` is byte-identical to HEAD (`git status --short docs/vv` prints nothing) |
| R3 | The author's return states the self-check against sections A to G and lists the brief's acceptance criteria | No | The assignment carries no author return for 01 or the templates. 01 section 15 records an integration status check of the cross-document actions, which is not a self-check against section G. A claude-context search for an 01 self-check found none. Package decision 115 does not list this record (cross X-2). `readiness_met: false` records this; it is not a finding |
| R4 | Every `TBR` has owner, plan, close_by; no `TBD` strings | Yes | `grep -n -i 'TBD\|as appropriate\|should consider'` on the five files: "TBD" appears only as the name of a rule or list ("TBD/TBR list", "zero TBDs", "no TBD"); no "as appropriate" or "should consider"; 0 em dashes in any file |
| R5 | For a CR: impact assessment attached | N/A | Not a CR |

## Participants

Author agent `author:process` (Claude main session as lead SE; not present). Reviewer agent `reviewer:INSP-019` (this record). Software assurance reviewer: not required. 07 section 2.1.1 (HEAD `adcfe09`) makes "Other process documents (`docs/process/0N-*.md` except 03, 05 and this plan)" No in every column, and `tools/validate_docs.py` `ASSURANCE_WHOLE_PRODUCTS` does not list 01. Owner: dispositions the liens at SRR.

## A. Format and editorial

| Id | Answer | Evidence |
|---|---|---|
| CK-REQ-A8 | Yes | Terms follow NPR 7123.1D App. F maturity terms (01 section 1 item 5 table) and App. A RFA/RID (`07-appendixa.md` line 150, "Each Center defines their own RFA/RID disposition process", which 01 section 10.1 applies). Review tokens SRR, PDR, CDR, TRR, TRR-Dn, SAR and the `RFA-<REVIEW>-NNN` / `RID-<REVIEW>-NNN` ids match charter section 6; the schema's `reviewToken` and `itemId` patterns implement them. State names (Open, Answered, Verified, Closed, Withdrawn), severities (Major, Minor, Blocking, Routine) and dispositions (Approved, Approved with liens, Not approved) are spelled identically in 01 sections 10 and 12, the schema enums and both templates. The template's minimum slide set (section 1.1, ten rows) equals charter section 4 item 2 item for item |

ITEMS N/A: CK-REQ-A1 to A7, B1 to B7, C1 to C8, D1 to D4, E1 to E6, F1 to F4 and the per-requirement validation table (the products are a process document and templates, not a requirement file or CR; checklist product-type table row "Plans and process documents": "G (all items) and A8").

## G. Plans, process documents and decision records (SWE-087 b)

| Id | Answer | Evidence |
|---|---|---|
| CK-REQ-G1 | No | Checked against charter sections 2 to 9 and 12 (HEAD blob `131608b7`), `se-compliance-matrix.json`, `rmm.json`, `docs/process/05-configuration-and-data-management.md` section 4.4 and Table 4-1 rows 32 and 33, 03 section 9, 07 section 2.1.1 and ADR-001 section 2. Consistent: five event-based gates and absorbed reviews (charter section 3; ADR-001 "SAR (absorbing ORR)"); DR and DRR not held with SE-55 and SE-56 T (matrix `comply` T, `relief_type` deviation) and SE-51, SE-52 T (deviation); SE-44 NA; SE-47, SE-53, SE-54, SE-69 FC as customization; RFA and RID severities and closure deadlines equal charter section 4 item 3 (Major blocks the baseline; Minor fix before the next review, 01 section 10.2); completion items a to i equal NPR 7123.1D §5.2.3.1; baselines functional, allocated, product, as-built with pushed annotated tags (charter section 8; 01 section 2 points to 05 section 4.4 steps 1 to 6, whose tag message and post-tag record commit 01 restates correctly); L1 TBRs by PDR and L2 by CDR (charter section 7; 01 sections 5.3 row 25, 6.3 row 25); Verified versus Closed for host-verified software (charter section 9; 01 sections 8.3 row 2 and 8.4 row 5); the delta TRR rule including the on-air series (charter section 3; 01 section 7.6); the review-trend TPM `TPM-003` key `review-trend` in `docs/plan/tpm.json` (charter section 4 item 5); RMM rows cited in 01 carry the dispositions 01 states (SWE-015, 016, 018, 023, 143, 151, 154, 156, 157, 159, 210, 219 T; SWE-073, 203, 220 FC); memo template section 12 cites 05 Table 4-1 row 33 (Record class) and 01 section 13 cites row 32 for the baseline record, both correct. Disagreements: finding-1 (charter lines 39, 41, 163 against 01 section 15), finding-2 (`validate_docs.py` schema against 01 section 13), finding-3 (matrix against 01 section 14), finding-5 (03 section 9 against the memo template). No Accepted ADR is contradicted |
| CK-REQ-G2 | No | Every procedure names its artifact, path and id scheme: readiness steps 3.1 items 1 to 5 (package, per-review traceability report, review-trend plot, deck source, HTML and PNGs, readiness block); log states with required fields (10.3) and evidence kinds with reference forms (10.5, enforced by the schema: every kind of the 10.5 table has a `ref` pattern); records table (13) with writer and timing; lien identification (12.2: "There is no lien without an id"). Open decisions carry owner and event (section 8.6 SWE-219 relief "decided by the owner at SRR"; section 15 owners). No "TBD", "as appropriate" or "should consider". Exception: finding-4 (record paths and checklist list that do not resolve to the SRR records and templates) |
| CK-REQ-G3 | Yes | Section 1 item 6: chair, Decision Authority and both TAs Robin; presenter, package and deck author Claude; independent reviewers and the software assurance function as separate invocations. Section 10.4: originator the owner, assignee Claude by default, verifier an independent reviewer that did not author the fix (RID) or the owner (RFA), closer the owner, log keeper Claude. Approval points: readiness confirmation (3.1 item 5), finding adoption (10.1), severity changes (10.2), closure (10.3 Closed "Owner accepts closure"), missed-lien choice (12.2), memo signature (9 row i; memo template section 12), the SE-55 and SE-56 deviation as ETA (SE-06) in the SRR memo, and the SWE-219 and SWE-220 waivers (8.6). SE-06 verified: NPR 7123.1D §6.1.5 "The ETA shall approve ... waiver or deviation authorizations" (`06-chapter6.md` line 32) |
| CK-REQ-G4 | Yes | Section 3.5 mirrors the matrix row by row with the Customized (NA), Customized (substitute) and T vocabulary of charter section 12, and cites the RMM rows it relies on: SWE-015, SWE-016, SWE-151 T (programmatic row); SWE-154, 156, 157, 159, 210 T (System Security Plan row); SWE-018 T (section 2.1 milestone status); SWE-143 T (section 2.1 and 5.6, and the RMM implementation text agrees that adopted findings become RIDs); SWE-219 T (section 8.6); SWE-023 as tailored (5.6). All dispositions checked in `rmm.json` and `se-compliance-matrix.json` at HEAD. 01 section 1 item 3 keeps customization (combined reviews) apart from tailoring (reviews not held), as charter section 1 and SE HB §3.11.4.3 require |
| CK-REQ-G5 | N/A | 01 and the templates carry no cybersecurity section of their own. The App. G System Security Plan items are dispositioned in 3.5 as Customized (substitute) by 07 section 16, which is reviewed under INSP-010 and INSP-018; SRR success criterion 4 (section 4.4) names the USB and key-input security expectations |
| CK-REQ-G6 | Yes | Section 11 defines the review-trend TPM completely: source (every `docs/reviews/*/rfa-rid-log.json`, the package date `T`, the memo `signed` keys), measures with definitions, burndown series, thresholds (alert zones, rules applied in order, SE HB §6.7.1.2.1 colour coding), storage (`TPM-003` history in `docs/plan/tpm.json`, plot in `docs/reviews/<REVIEW>/figures/review-trend.png`), analysis rule (a Red package zone blocks the readiness declaration until a closure plan or re-review is recorded) and reporting interval (every gate, SE-61). S8 carries the other TPMs. The SWE-089 record measurements are named in 4.6 (record front matter plus `docs/plan/measurements.json`) |
| CK-REQ-G7 | Yes | Tool claims checked by running them on 2026-09-26: `tools/review_trend.py --root tools/tests/fixtures/review_trend --date 2026-10-12` reproduced every known-answer value of section 11 (six count rows, age_open median 9 max 9, age_closed median 2, closure fraction undefined, zone Green, burndown points 2026-10-03 5/1 and 2026-10-05 5/3), exit 0; the fixture memo carries `signed: 2026-10-05`; the fixture log is byte-identical to `docs/templates/rfa-rid-log.example.json` (`cmp`), and `test_fixture_log_is_the_template` exists (`tools/tests/test_review_trend.py` line 92). `review_trend.py` has the options 01 uses (`--root`, `--date`, `--package`, `--write`, `--json`; lines 538 to 542) and `traceability.py` the `--output` option of 3.1 item 2 (line 2765, writing `traceability.json` beside the report). The 10.4 item check one-liner ran on `docs/reviews/SRR/rfa-rid-log.json` (`ok`) and the 10.6 fallback one-liner on the example (`ok`). Schema behaviour matches 10.6 on mutated copies of the example: a Major RID with `lien: true` is rejected, an id of another fixed review is rejected, a `cr` evidence ref `abc` is rejected, `blocks_order` outside CDR is rejected, and a `TRR-D1` log holding a `TRR-D2` id is accepted by the schema, exactly the gap 01 says the item check closes. `tools/slides/render_deck.py` exists. Honest limits stated: the schema cannot check the `n` of `TRR-Dn` (10.4); the Topic 7.09 PAT checklists are not in the corpus (3.3 C5); SE HB App. F was removed in Rev 2 (5.3 row 23, confirmed by `28-appendix-f-functional-timing-and-state-analysis.md`) |
| CK-REQ-G8 | Yes | Every SE id in the five files (SE-06, SE-32 to SE-48, SE-51 to SE-57, SE-60 to SE-69; 35 ids) and every SWE id (61 ids) exists bracketed in the corpus (scripted check over `npr-7123-1d/*.md` and `npr-7150-2d/*.md`, 0 missing). Section mappings verified: SE-32 §5.2.1.1, SE-33 §5.2.1.5, SE-34 §5.2.2.1, SE-65 §5.2.1.3 (including "strongly recommended that Category 1 and Class A programs and projects ... develop a stand-alone HSI Plan"), SE-66 §5.2.2.2 b(3), SE-57 §5.2.2.7, SE-60 §6.2.6, SE-61 §6.2.7, SE-62 and SE-63 §6.2.8 a and b, SE-64 §6.2.9, SE-06 §6.1.5; §5.1.5 event-based reviews; §5.2.1.2; §5.2.2.2 waiver or deviation when a review is not held; §5.2.2.4 baselined means final drafts; §5.2.2.6 spectrum manager; §5.2.3.1 items a to i; App. A RFA/RID; App. H Table H-1 SE-44 rationale; App. G G.1.1 best practices, §G.9 PRR "multiple systems/units (typically greater than three or as determined by the project)", Table G-19 entrance 1 to 5 (including "Peer reviewers independent from the project") and success 1 to 4, G-4 s9, s10, s12 ("Proposed tailoring is appropriate"), s14, G-9 entrance 8 (interface verification), G-10 s11, G-11 entrance 3.1 to 3.14 and success 1 to 9, G-12 s13, and the "Software criteria and products, per NASA-HDBK-2203" items. SE HB §3.11.3, §3.11.4 ("Scaling the requirement"), §3.11.4.2 ("some relief on the scope"), §3.11.4.3 ("departures from review elements required by other NPRs need to be addressed by tailoring those documents"), §3.11.6, §4.2.1.2.4, §6.7.1.2.1 (colour-coded alert zones), App. B "Liens". NPR 7150.2D §3.7.4 note to SWE-219 and §3.7.5 SWE-220 are paraphrased with "says that" and "as SWE-220 provides", not presented as quotations, and the paraphrase is accurate. SWEHB Topic 7.09 file exists. 47 CFR 97.305 and 97.307 exist in `docs/references/md/regulatory/` |

## 3.3 C5 check (Topic 7.09 Process Asset Templates, RSK-009 item)

01 section 3.3 C5 asks this reviewer to record the check of the software tables (sections 4.6, 5.6, 6.6, 7.5, 8.6) against the per-review PAT checklists of SWEHB Topic 7.09 as done or not possible. Result: **not possible item by item.** `docs/references/md/swehb/7-09-entrance-and-exit-criteria.md` holds only the names of the thirteen PATs (PAT-066 MCR to PAT-078 FRR, lines 77 to 413) and a description of their layout; the checklists themselves are MS Word downloads that are not in the corpus. **Done at purpose level:** the SRR tab's key purposes (software requirements aligned to system goals, clear, feasible and traceable; risks from incomplete requirements minimized) are each carried by a 4.6 row (SWE-050 software-related L1 requirements and preliminary SRS; SWE-052 traceability L0 to L1 and L1 to hazards; SWE-087 a and SWE-088 peer review of the software L1 requirements; SWE-086 software risks). Topic 7.09 also lists a SwRR (PAT-068), which 01 does not name; cwht holds no separate SwRR and carries software requirement maturity in the SRR (4.6) and PDR (5.6 SWE-050 baselined) tables, which is a customization consistent with 3.3 C5 (observation O-1, not a finding). The residual gap stays with RSK-009.

## Observations (not findings)

- **O-1 (SwRR).** Topic 7.09 describes a Software Requirements Review with its own PAT; 01 does not mention it. A one-line customization entry in 3.5 or 4.7 would make the omission explicit.
- **O-2 (convergence rule).** The lead SE convergence rule of 2026-09-26 (Minor findings as "Lien: fix before PDR" in a record that reads APPROVED with liens) is not described in 01 section 10 or 12, which treat liens only at the RFA/RID level. INSP-022 finding-5 already carries the matching 08 and template change; the 01 author should align sections 10.1 and 13 in the same change.
- **O-3 (header).** The 01 header carries "Status: Draft for SRR" without a revision number or date, so the version the functional baseline captures is identified only by its commit (`b301df2`). The baseline record lists the blob, so this is not a defect.

## Measurements (SWE-089)

| Measure | Value |
|---|---|
| Product size | 01: 15 sections, 955 lines; review-package.md 305 lines; decision-memo.md 159 lines; schema 305 lines; example 5 items |
| Items checked | 9 (G1 to G8, A8) plus R1 to R5 and the 3.3 C5 check |
| Items answered No | 2 (CK-REQ-G1, CK-REQ-G2); readiness R3 No |
| Items N/A | A1 to A7, B to F (37 items), G5 |
| Findings by severity | Major 0, Minor 5 |
| Findings fixed, deferred | 0 fixed; 5 deferred as liens (fix before PDR) |
| Iteration | 1 |
| Effort | 45 turns, 55 minutes |

## Tool runs (2026-09-26, HEAD `adcfe09`, working tree)

| Command | Exit | Result |
|---|---|---|
| `.venv/bin/python tools/validate_docs.py --quiet` (before this record) | 0 | no failure |
| `.venv/bin/python tools/validate_docs.py` (after this record) | 0 | this record PASS as a peer-review record (drift note only: record verdict NEEDS CHANGES) |
| `.venv/bin/python tools/traceability.py --report-only` | 0 | 237 requirements, 170 test cases, 0 violations, 2 warnings |
| `.venv/bin/python -m unittest discover -s tools/tests` | 0 | 392 tests OK on three consecutive runs; one earlier run in the same minute reported one failure that did not recur (concurrent edits by other review invocations in `docs/reviews/SRR/checklists/` during the run are the likely cause; not attributable to these products) |
| `.venv/bin/python tools/review_trend.py --root tools/tests/fixtures/review_trend --date 2026-10-12` | 0 | every section 11 known-answer value reproduced |
| 10.4 item check on `docs/reviews/SRR/rfa-rid-log.json`; 10.6 fallback on the example log | 0, 0 | `ok`, `ok` |

## Cross items (outside this record's scope; for the lead SE)

- **X-1 (slug).** This record uses the slug `process-01-lifecycle-and-reviews` as assigned; 01 section 13 and package H1 (c) name `plan-01-lifecycle-and-reviews`. The package H1 (c) list should be updated to the filed path.
- **X-2 (decision 115).** Package decision 115 (author self-checks) lists INSP-001, 002, 003, 004, 010, 011 and 014; add INSP-019. This record turns APPROVED (with liens) without product change once the 01 author's self-check against section G is filed or the owner waives R3.
- **X-3 (matrix references, finding-3).** If the fix chosen is to change the matrix, the compliance-matrix author adds the 01 section to the `implementation_ref` of SE-35 to SE-46, SE-57, SE-60 to SE-64 and SE-66 to SE-69 and re-runs `tools/render_compliance.py --check`.
- **X-4 (SRR memo, finding-5).** Whoever writes `docs/reviews/SRR/decision-memo.md` includes the sixth 03 section 9 approval line (owner as spokesperson for bystanders and household members) and names both INSP-009 and INSP-017 on the classification line, regardless of when the template is fixed.

## Verdict

```
ITERATION 1 (2026-09-26): VERDICT: NEEDS CHANGES (readiness R3 only; decision 115). reviewer_verdict APPROVED (with liens).
FINDINGS:
- [Minor] CK-REQ-G1 01 section 15 item 2 and preamble, 3.5 row: charter change already made at 4e3f891; status stale. Lien: fix before PDR.
- [Minor] CK-REQ-G1 01 section 13: field list omits product_files, product_blob and the record drift rule of validate_docs.py. Lien: fix before PDR.
- [Minor] CK-REQ-G1 01 section 14: "matrix rows cite this document by section" false for 23 rows. Lien: fix before PDR.
- [Minor] CK-REQ-G2 01 sections 4.6, 13, 2.1: record paths, slug list and checklist list do not match the SRR records and templates. Lien: fix before PDR.
- [Minor] CK-REQ-G1 decision-memo.md section 7.1: omits the 03 section 9 bystander risk line; one concurrence named where 03 names two. Lien: fix before PDR.
ITEMS N/A: CK-REQ-A1 to A7, B1 to B7, C1 to C8, D1 to D4, E1 to E6, F1 to F4 (process document and templates), CK-REQ-G5 (cybersecurity in 07 section 16)
MEASUREMENTS: size=01 955 lines + 4 templates; items=9; no=2; major=0; minor=5; lien=5; open_major=0; iteration=1; turns=45; minutes=55
PRODUCTS: 01@eabbbd57, review-package.md@4ed480e2, decision-memo.md@1d3ce437, rfa-rid-log.schema.json@38898b0c, rfa-rid-log.example.json@0e913114 (HEAD adcfe09)
```
