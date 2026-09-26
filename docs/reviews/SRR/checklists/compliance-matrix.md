---
id: INSP-024
checklist: peer-review-checklist-requirements
checklist_revision: C
checklist_file: docs/reviews/SRR/checklists/compliance-matrix.md
product: docs/process/se-compliance-matrix.json
# product_commit: last commit that touched the product (b301df2, 2026-09-26); review baseline HEAD adcfe0946d2f1b5cd8f41a8f91eb4219a7fb99a1
product_commit: "b301df2"
# product_files: git rev-parse HEAD:<path> at HEAD adcfe0946d2f1b5cd8f41a8f91eb4219a7fb99a1 (the JSON source and its generated render; the working tree equals HEAD for both)
product_files: ["docs/process/se-compliance-matrix.json@790d256214e07beb736f2f414a8eaf384ecf2440", "docs/process/se-compliance-matrix.md@09426930b27e3b51182ab28086c6c73000f274d9"]
product_size: 62 Table H-1 rows (FC 49, T 4, NA 9), header block, comply codes, field notes, approval block; render 115 lines
sprint: SRR-prep
author_agent: "author:compliance (Claude main session, lead SE; commits 4e3f891 and b301df2)"
reviewer_agent: "reviewer:INSP-024"
criticality: neither
assurance_required: false
assurance_reviewer_agent: none
iteration: 1
# readiness_met: true at the re-issue of 2026-09-26 (package item R8): R3 met by the author self-check filed at ca22e37 and confirmed by the reviewer; see Re-issue
readiness_met: true
# verdict: APPROVED (with liens finding-1 to finding-7, fix before PDR) at the re-issue of 2026-09-26 without a further product review;
# iteration 1 held it at NEEDS CHANGES only on readiness R3, which the author self-check now meets
reviewer_verdict: APPROVED
assurance_verdict: not-required
verdict: APPROVED
findings_major: 0
findings_minor: 7
findings_open: 0
findings_fixed: 0
findings_verified: 0
findings_deferred: 7
assurance_findings_major: 0
assurance_findings_minor: 0
assurance_tasks_applied: []
deferred_rids: []
items_no: [CK-REQ-G1, CK-REQ-G3, CK-REQ-G6, CK-REQ-A8]
effort_turns: 51
effort_minutes: 50
record_status: Open
date: 2026-09-26
date_closed: null
---

# Peer review record INSP-024: NPR 7123.1D compliance matrix (`docs/process/se-compliance-matrix.json` and `.md`)

**Product.** `docs/process/se-compliance-matrix.json` blob `790d2562` and its generated render `docs/process/se-compliance-matrix.md` blob `09426930`, both `git rev-parse HEAD:<path>` at HEAD `adcfe0946d2f1b5cd8f41a8f91eb4219a7fb99a1` (last changed at `b301df2`, which edited the SE-11 row only; `git diff 4e3f891 b301df2`). **Checklist.** `docs/templates/peer-review-checklist-requirements.md` revision C, product type "Plans and process documents": section G (all items) and A8, the plan review items that `docs/process/08-agent-briefing.md` sections 3.1 and 3.5 assign. **Judged against.** NPR 7123.1D App. H (H.1.1 column set, H.1.3 comply codes, Table H-1 row set and signature block; `docs/references/md/npr-7123-1d/14-appendixh.md`), NPR 7123.1D sections 2.2.1.1 to 2.2.1.3, 2.2.2 and 5.2.2.2, and charter section 12 (tailoring register), with charter sections 1, 2 and 3. **Gate fed.** SRR entrance row 3 (05 Table 4-2 row 3; package section 6.11 "Record: none yet"; package H1 (c) and R6, record `plan-se-compliance-matrix` filed at the path assigned here).

**Independence.** The reviewer did not author the matrix and did not edit it. **Search first.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` (queries: App. H compliance matrix tailoring; SE-44 rationale; DR and DRR Tables G-17 and G-18; compliance matrix author self-check) preceded every `grep`; `grep -n` was used only to pin lines the hits pointed at. **Convergence rule** (lead SE, 2026-09-26, applying charter section 4 item 3): only Major findings change products in this round; every Minor finding is dispositioned "Lien: fix before PDR" and carried by the package as a Routine item.

**Verdict (iteration 1, 2026-09-26; superseded by the re-issue at the end of this record, which reads APPROVED with liens).** Reviewer verdict **APPROVED (with liens)**: 0 Major, 7 Minor, all Lien. Record `verdict` **NEEDS CHANGES on readiness R3 only**: no author self-check against section G is on record, and the checklist completion criteria and `tools/validate_docs.py` accept APPROVED only with `readiness_met: true`. The record turns APPROVED (with liens) with no product change when the matrix author files the self-check or Robin waives R3 for this record under package decision 115 (which today names seven other records only; cross item X-1).

## Record

### Findings

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | reviewer | Minor | CK-REQ-G6, CK-REQ-G1 | JSON rows SE-62 (line 625) and SE-63 (line 635); render lines 104, 105 | SE-62 says the mass budget "is a TPM from PDR (estimated) through SAR (measured)" and SE-63 says the power budgets "are TPMs from PDR through SAR". `docs/plan/tpm.json` TPM-001 (`npr_ref` SE-62) and TPM-002 (`npr_ref` SE-63) both carry an SRR entry in `margin_policy` (TPM-001: ">= 20 % on the allocation from a bottom-up estimate"; TPM-002: ">= 20 % per mode from the concept-level estimate"), and package section 2 lists the missing SRR estimate of TPM-001 as soft criterion S8, a lien. The matrix states a later start than the TPM file it cites as implementation. Fix: say "from SRR (estimate) through SAR (measured)" in both rows, or cite the TPM-001 and TPM-002 margin policies. | Lien | Pending | PDR (lien) |
| <a id="finding-2"></a>finding-2 | reviewer | Minor | CK-REQ-G1, CK-REQ-G4 | JSON row SE-11 (line 67); render line 49 | The Product Implementation row reads "Buy: PCBWay turnkey fabrication and assembly ... DigiKey parts" and names only firmware under Make. It omits the owner's hand assembly of through-hole and exposed-pad parts (SI-031; Accepted ADR-007 "PCBWay turnkey surface-mount assembly with owner-soldered through-hole parts (kit model)"; charter section 12 row "Assembly model (SI-031)", Customized; charter section 5 hand-assembly list). SEMP section 5.5, which the row cites, states the split correctly. The row is incomplete against the charter and an Accepted ADR, not contrary to them. Fix: add the SI-031 make element and cite ADR-007 and `hardware/releases/HW-MB-rev<X>-<n>/cwht-MB-rev<X>-hand-assembly.csv`. | Lien | Pending | PDR (lien) |
| <a id="finding-3"></a>finding-3 | reviewer | Minor | CK-REQ-G1 | JSON row SE-34 (line 307); render line 73 | SE-34 says the entrance and success criteria are "tailored from NPR 7123.1D App. G Tables G-4, G-6, G-7, G-10 and G-11". Its implementation reference, `docs/process/01-lifecycle-and-reviews.md`, tailors SRR from Tables G-3 and G-4 (section 4.3 heading), PDR from G-5 and G-6 (5.3), TRR from G-10 plus SIR Table G-9 items 3.1, 3.2 and 8 (7.3) and SAR from G-11 plus Table G-12 items (8.3). The row copies the charter section 3 sentence, which carries the same short list (cross item X-2). Fix: list the tables 01 uses, or state "the tables named in 01 sections 4.3, 5.3, 6.3, 7.3 and 8.3". | Lien | Pending | PDR (lien) |
| <a id="finding-4"></a>finding-4 | reviewer | Minor | CK-REQ-G1, CK-REQ-G2 | JSON row SE-57 (line 565); render line 98 | SE-57 names only the software sprint-closure review and cites `docs/sprints/` (absent until the first sprint), `tpm.json` and `measurements.json`. The SE-57 plan is `docs/process/01-lifecycle-and-reviews.md` section 2.1 ("Technical reviews between gates (SE-32, SE-57)"), which defines five between-gate reviews: sprint closure, milestone status in every package, independent peer review before a product is cited, the PDR software architecture review and Phase E periodic status. Hardware effort before the first sprint is monitored only by the latter kinds, which the row does not mention; the row does not cite 01. Fix: summarize the 01 section 2.1 set and add it to `implementation_ref`. | Lien | Pending | PDR (lien) |
| <a id="finding-5"></a>finding-5 | reviewer | Minor | CK-REQ-G3 | JSON `approval.submitted_by` (line 21); render line 9 | Table H-1 closes with a signature block: "Submitted By: ... Program/Project Manager" and "Approved By: ... Engineering Technical Authority" (`14-appendixh.md` line 112). The matrix records "Submitted by: Claude (lead systems engineer)". Charter section 2 makes Robin the project manager and the ETA, and Claude the lead SE who prepares products. The submitter role therefore differs from the App. H template without a stated customization. Fix: record Claude as preparer and Robin as submitter (PM) and approver (ETA), or state the customization in the header. | Lien | Pending | PDR (lien) |
| <a id="finding-6"></a>finding-6 | reviewer | Minor | CK-REQ-A8 | JSON `revision_date` (line 4); render line 6 | `revision_date` reads 2026-09-25, but the committed content changed on 2026-09-26 at `b301df2` (SE-11 `justification` and `implementation_ref` now name TS-002; `git diff 4e3f891 b301df2`). The date shown to the owner at approval does not identify the revision approved. Fix: set the revision date at each content change (the render follows). | Lien | Pending | PDR (lien) |
| <a id="finding-7"></a>finding-7 | reviewer | Minor | CK-REQ-G1 | JSON row SE-35 (line 317); render line 74 | SE-35 requires "baselined stakeholder identification and expectation definitions". The justification names only the expectations ("NGO-NNN, success criteria"); the stakeholder identification, the `stakeholders` array of `expectations.json` (10 entries; package H4, 02 section 3.0 and T-21 `STAKEHOLDERS_MISSING`), is not mentioned, so half of the SE-35 product is not evidenced in the row. Fix: name the `stakeholders` array and T-21 in the justification. | Lien | Pending | PDR (lien) |

### Lien table

| Finding | Severity | Disposition | Owner | Due | Package carriage |
|---|---|---|---|---|---|
| finding-1 | Minor | Lien: fix before PDR | Compliance-matrix author (Claude, lead SE) | PDR readiness declaration | Routine item |
| finding-2 | Minor | Lien: fix before PDR | Compliance-matrix author (Claude, lead SE) | PDR readiness declaration | Routine item |
| finding-3 | Minor | Lien: fix before PDR | Compliance-matrix author (Claude, lead SE) | PDR readiness declaration | Routine item (with cross item X-2 for the charter) |
| finding-4 | Minor | Lien: fix before PDR | Compliance-matrix author (Claude, lead SE) | PDR readiness declaration | Routine item |
| finding-5 | Minor | Lien: fix before PDR | Compliance-matrix author (Claude, lead SE) | PDR readiness declaration | Routine item |
| finding-6 | Minor | Lien: fix before PDR | Compliance-matrix author (Claude, lead SE) | PDR readiness declaration | Routine item |
| finding-7 | Minor | Lien: fix before PDR | Compliance-matrix author (Claude, lead SE) | PDR readiness declaration | Routine item |

**Counts.** 7 findings: 0 Major, 7 Minor; Closed 0, Disputed-accepted 0, Lien 7, Open 0. No finding needs an owner ruling.

## Readiness criteria

| # | Criterion | Answer | Evidence |
|---|---|---|---|
| R1 | `tools/validate_docs.py` exits 0 | Yes | Run 2026-09-26 at HEAD `adcfe09`: exit 0, "validate_docs: 38 passed, 0 failed, 38 checked"; the matrix also validates directly against `se-compliance-matrix.schema.json` (jsonschema, "schema ok") |
| R2 | `tools/traceability.py` reports no violation | Yes | `--report-only` exit 0: 237 requirements, 170 test cases, 0 violations, 2 warnings (REQ-SYS-125, REQ-SYS-148 `SYS_UNALLOCATED`, outside this product) |
| R3 | The author's return states the self-check against sections A to G and lists the brief's acceptance criteria | Yes at re-issue (No at iteration 1) | Re-issue 2026-09-26: the author self-check filed at `ca22e37` lists the acceptance criteria and answers A8 and G1 to G8; confirmed in section "Re-issue". Iteration 1 text: No author return accompanied this assignment. The product's "Validation" block is the `render_compliance.py` check of row set, order, statements, rationales and the charter section 12 dispositions, not a self-check against G1 to G8; `01-lifecycle-and-reviews.md` section 15 item 1 is a resolution note. A claude-context search for a compliance-matrix self-check found none. Not a product finding; `readiness_met: false` records it |
| R4 | No `TBD`; every TBR has owner, plan, close_by | Yes | The only "TBD" string is the SE-39 statement "no TBDs"; no TBR in the matrix |
| R5 | CR impact assessment | N/A | Not a CR |

## Participants

Author agent (not present); reviewer `reviewer:INSP-024`; no software assurance reviewer (07 section 2.1.1 does not list the NPR 7123.1D matrix); owner for the disposition of the liens.

## A. Format and editorial

ITEMS N/A: CK-REQ-A1 to CK-REQ-A7 (the product is a plan-type matrix, not a requirement file; checklist product-type table).

| Id | Answer | Evidence |
|---|---|---|
| CK-REQ-A8 | No | Terminology follows the charter (FC, T, NA as App. H.1.3; "customization", "deviation" as NPR 7123.1D sections 2.2.1.2 and 2.2.2; "Decision Authority", "ETA"). No em dash (0 occurrences). The revision date does not match the committed revision (finding-6). |

## G. Plans, process documents and decision records

| Id | Answer | Evidence |
|---|---|---|
| CK-REQ-G1 | No | **Charter section 12 dispositions all hold** (checked row by row): SE-24 to SE-31 NA (no contracts); SE-44 NA by the Table H-1 rationale, whose text "will be a 'Not Applicable' in this line" for projects and single-project programs is pinned in the corpus row; SE-51 and SE-52 T, deviation, ORR combined with SAR, scope relief to the handbook end-of-life section relative to Tables G-17 and G-18 (charter line 163; the tables exist, `13-appendixg.md` G.18 and G.19); SE-55 and SE-56 T, deviation, review not held (charter section 3 E/F row; NPR 7123.1D 5.2.2.2 "If the associated life-cycle review is not held, the technical team will need to seek a waiver or deviation", `05-chapter5.md` line 62); SE-62 FC with 350 g provisional (TPM-001 `planned_value_text`); SE-65 and SE-66 FC, customized (HSI section SEMP 7.3.1 exists). **Charter section 3 combined reviews** agree: SE-35 to SE-37 at SRR, SE-40 to SE-43 at PDR, SE-47 and SE-48 at TRR, SE-69, SE-51 to SE-54 at SAR; 01 section 1 item 3 and 04 line 497 say the same. **RMM:** cited SWE-033, SWE-034, SWE-086, SWE-200 exist and agree with `render_rmm.py --check` (SWE-200 "Planned for PDR"). **Accepted ADRs:** no contradiction; ADR-007 not reflected in SE-11 (finding-2). Disagreements with sibling products: `tpm.json` (finding-1), 01 sections 4.3 to 8.3 (finding-3), 01 section 2.1 (finding-4), SE-35 content (finding-7). All Minor. |
| CK-REQ-G2 | Yes | Every one of the 62 rows names at least one repository path in `implementation_ref` following the charter section 5 tree; files not yet written (for example `docs/plan/integration-plan.md`, `docs/sprints/`, `docs/ops/operations-handbook.md`) are stated as the committed location by `field_notes.implementation_ref`. No "as appropriate", "should consider" or TBD. The SE-57 omission of 01 is finding-4. |
| CK-REQ-G3 | No | Owner approval points are stated: the `comply_codes.T` text makes the owner's approval of this matrix at SRR, as Decision Authority and ETA (SE-06), the tailoring approval, recorded in `docs/reviews/SRR/decision-memo.md`; SE-51 and SE-52 add the SAR memo acceptance of the substitute. The submitter role differs from the Table H-1 signature block (finding-5). |
| CK-REQ-G4 | Yes | The matrix is itself the tailoring record for NPR 7123.1D. Each T row carries `relief_type` (deviation, matching NPR 7123.1D 2.2.1.2 timing: approved before baseline), a `risk_evaluation` on the 06 scales (likelihood 1 "Very unlikely", consequence 1 "Negligible" or 2 "Minor", scores 1 and 2 Green, all pinned in 06 sections 6 to 8) as 2.2.1.3 requires, a substitute practice and the approval. The NA rows give the institutional reason and the project-scale equivalent. The SEMP section 9.0 mirrors the same dispositions. |
| CK-REQ-G5 | N/A | No cybersecurity content in the NPR 7123.1D matrix; cybersecurity is tailored in the RMM (SWE-154, 156, 157, 159, 210; charter section 12). |
| CK-REQ-G6 | No | Measurement rows SE-60 to SE-64 name `docs/plan/tpm.json`; the TPM ids exist (TPM-001 mass SE-62, TPM-002 power SE-63, TPM-003 review trend SE-64 computed by `tools/review_trend.py`, and the key driving parameters of SE-60: TPM-015 output power, TPM-007 spurious margin, TPM-005 MDS, TPM-008 battery life, TPM-010 and TPM-011 flash and RAM). The start phase of SE-62 and SE-63 disagrees with the TPM margin policies (finding-1). |
| CK-REQ-G7 | Yes | The only tool claim is the "Validation: PASSED" block. `tools/render_compliance.py --check` run 2026-09-26: exit 0, "rows=62 corpus=62 FC=49 T=4 NA=9", "validation PASSED and rendered file is current", so the render equals the JSON. Tool validated as TV-005 (accreditation pending, decision 114). `tools/traceability.py` and `tools/review_trend.py`, named in SE-08, SE-13, SE-17, SE-42, SE-64 and SE-68, exist. |
| CK-REQ-G8 | Yes | Verified in the corpus: Table H-1 has 62 rows (57 `SE-NN` ids plus SE-60 to SE-64 written "SE- 60" in the conversion, lines 104 to 108) with the six H.1.1 columns (line 30), and SE-06 at 6.1.5 (line 100); App. H.1.1 and H.1.3 (lines 11, 20); NPR 7123.1D 2.1.4.3 "[SE-01] through [SE-05] deleted" (`02-chapter2.md` line 48), 2.2.1.1 to 2.2.1.3 (lines 104 to 108), 2.2.2 (line 110), 5.2.2.2 (`05-chapter5.md` line 62); App. J Table J-1 lists SE-49 and SE-50 (`16-appendixj.md` lines 10, 19, 20); Tables G-17 (DR) and G-18 (DRR) (`13-appendixg.md` G.18, G.19); SE HB App. H integration plan, App. I V&V plan, App. J SEMP, App. M CM plan, App. R HSI plan, App. S ConOps outlines (file names in `nasa-se-handbook/`); SWE-033 (`npr-7150-2d/03-chapter3.md` line 13), SWE-034 (line 41), SWE-086 and SWE-200 (`05-chapter5.md`). Requirement statements and rationales are verbatim, enforced by the tool's whitespace-normalized comparison; `short_form` is labeled a paraphrase "never quoted as NASA text". No 47 CFR citation in the product. |

## Numbers and references verified against their sources

| Product claim | Source checked | Result |
|---|---|---|
| 62 rows; FC 49, T 4, NA 9 | `render_compliance.py --check`; corpus Table H-1 | Agrees |
| SE-51/52 risk: L1, C2, score 2, Green; SE-55/56: L1, C1, score 1, Green | 06 section 6 table row 1, section 7 rows 1 and 2, section 8 band grid and rule "Green when score is 4 or less" | Agrees |
| Cell hazards carried by HZ-002 and HZ-007 | `docs/safety/hazards.json`: HZ-002 charge-side fault, HZ-007 discharge-side fault | Agrees |
| 01 section 7.3 rows 10 and 11 (SE-47, SE-48); 01 sections 7.5, 8.5; 04 section 13 | 01 lines 495, 496 area (rows 10 "G-9 3.1; SE-47", 11 "G-9 3.2; SE-48"), 7.5 SE-47/SE-48 rows, 8.5 SE-53/SE-54/SE-51/SE-52 rows; 04 line 497 | Agrees |
| SE-13, SE-14, SE-19, SE-20, SE-21 "ETA approval ... (04/05/06 header)" | Headers of 04 ("ETA approval: the owner ... approves this document as the project's verification process and validation process"), 05 ("ETA approval: SE-20 and SE-21 each require ..."), 06 (re-approved at every review) | Agrees |
| SE-11: 06 section 14.1 class 1 item (h); 07 section 17.2, section 1.3 row t; TS-002 | 06 line 310 item (h); 07 section 17.2 heading "Make/buy assessment (SWE-033)"; TS-002 header "Decide by SRR", decision class item (h) | Agrees (Status "Draft" true) |
| SE-28 SI-008, SI-009; SE-62 SI-001; SE-65 SI-018 | `stakeholder-inputs.md` lines 9, 16, 17, 26 | Agrees |
| SE-44 NA basis | Corpus Table H-1 SE-44 rationale | Agrees verbatim |
| SE-62, SE-63 "from PDR" | `tpm.json` TPM-001, TPM-002 `margin_policy.SRR` | Disagrees (finding-1) |

## Cross items (outside the product; for Claude)

- **X-1.** Package decision 115 lists the self-check shortfalls of INSP-001, 002, 003, 004, 010, 011 and 014; this record (and the other records filed in this round under R6) has the same readiness R3 shortfall and should be added, so that one owner waiver or one set of self-checks turns them APPROVED.
- **X-2.** Charter section 3 (line 41) names only Tables G-4, G-6, G-7, G-10 and G-11 as the sources of the tailored criteria, while 01 also uses G-3, G-5, G-9 items and G-12 items (finding-3). The charter is not edited by agents; carry as a charter issue in the package proposed-tailoring section.
- **X-3.** `docs/process/01-lifecycle-and-reviews.md` section 15 item 2 still reads "Open: owner decision" for the charter section 3 and 12 wording on SE-51 and SE-52, but the charter at HEAD already carries both changes (lines 41 and 163). The 01 author should mark it Resolved.
- **X-4.** Package section 6.11 cites the matrix at `b301df2` and "Record: none yet"; update to INSP-024 with the blobs above.

## Tool runs (2026-09-26, HEAD `adcfe09`, repository root, `.venv/bin/python`)

| Command | Exit | Result |
|---|---|---|
| `tools/validate_docs.py` | 0 | 38 passed, 0 failed (before this record was written) |
| `tools/traceability.py --report-only` | 0 | 0 violations, 2 warnings |
| `tools/render_risk.py --check --gate SRR --hazards docs/safety/hazards.json` | 0 | 65 risks, 0 warnings, register.md current |
| `tools/render_rmm.py --check` | 0 | 100 rows; FC 75, T 17, NA 8 |
| `tools/render_compliance.py --check` | 0 | rows=62 corpus=62 FC=49 T=4 NA=9; render current |
| `python -m unittest discover -s tools/tests` | 0 | 392 tests OK |

No visual product was produced or changed by this review.

## Verdict

```
VERDICT (iteration 1): reviewer APPROVED (with liens); record NEEDS CHANGES on readiness R3 only
PRODUCT: docs/process/se-compliance-matrix.json@790d256214e07beb736f2f414a8eaf384ecf2440; docs/process/se-compliance-matrix.md@09426930b27e3b51182ab28086c6c73000f274d9 (HEAD adcfe0946d2f1b5cd8f41a8f91eb4219a7fb99a1)
FINDINGS: finding-1 to finding-7 Minor, Lien: fix before PDR
ITEMS N/A: CK-REQ-A1 to CK-REQ-A7 (plan-type product); CK-REQ-G5 (no cybersecurity content)
MEASUREMENTS: size=62 rows; items checked=9 (A8, G1 to G8); items no=4; major=0; minor=7; lien=7; open_major=0; iteration=1; turns=45; minutes=40
```

## Author self-check (readiness R3; SRR package item R7)

Filed by the author, `author:compliance` (Claude main session, lead SE, the author named in this record's front matter), on 2026-09-26 at HEAD `ade0e09`, in answer to readiness R3 ("the author's return states the self-check against sections A to G below and lists the brief's acceptance criteria") and package item R7. 01 section 13 makes this file the single peer-review record for the product and requires that no record live only in conversation, so the self-check is filed here. The matrix's own "Validation" block records a tool result, not a self-check against section G. This section is the author's only content in the record: the front matter (including `readiness_met` and `verdict`), the findings, the readiness answers and the verdict belong to the reviewer and are unchanged. The reviewer confirms this self-check and answers R3 at the re-issue (package item R8); the author does not mark its own product reviewed (08 section 3.1).

**Product files checked.** `docs/process/se-compliance-matrix.json@790d2562` and its generated render `docs/process/se-compliance-matrix.md@09426930`. Each blob equals `git rev-parse HEAD:<path>` at `ade0e09` and equals the blob this record reviewed, so the self-check covers the reviewed product. The product files are not changed by this self-check (convergence rule).

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

**Scripted scan (AC-2, AC-3).** Over both files: 0 em dashes, 0 "as appropriate" or "should consider", no `TBD` value and no TBR. Every SE id cited (66 distinct, counting the Table H-1 rows and cross references) and every SWE id cited (4 distinct) exists bracketed in the corpus (0 missing). The matrix holds 62 rows: FC 49, T 4, NA 9, matching Table H-1 of `docs/references/md/npr-7123-1d/14-appendixh.md`.

**Self-check against the checklist** (`docs/templates/peer-review-checklist-requirements.md` revision C, product type "Plans and process documents": CK-REQ-A8 and section G; A1 to A7 and sections B to F are N/A for a process document by the product-type table).

| Id | Author answer | Evidence |
|---|---|---|
| CK-REQ-A8 | No (lien only) | FC, T and NA follow NPR 7123.1D App. H.1.3; "customization" and "deviation" follow §2.2.1.2 and §2.2.2. Known defect, Minor: finding-6 (`revision_date` 2026-09-25 predates the `b301df2` content change) |
| CK-REQ-G1 | No (liens only) | Charter section 12 dispositions hold row by row (SE-24 to SE-31 NA; SE-44 NA; SE-51, 52, 55, 56 T with relief type deviation). Known disagreements, Minor: finding-1 (SE-62 and SE-63 say "from PDR" where `tpm.json` has SRR entries), finding-2 (SE-11 omits the owner's hand assembly of SI-031 and ADR-007), finding-3 (SE-34 names five App. G tables; 01 uses more), finding-4 (SE-57 omits 01 section 2.1), finding-7 (SE-35 omits the stakeholder identification) |
| CK-REQ-G2 | Yes | Each of the 62 rows names a repository path in `implementation_ref` on the charter section 5 tree; finding-4 (SE-57 reference) is carried under G1 |
| CK-REQ-G3 | No (lien only) | The owner's approval as Decision Authority and ETA (SE-06) is stated in `comply_codes.T`. Known defect, Minor: finding-5 (`approval.submitted_by` names Claude where Table H-1 names the Program/Project Manager, Robin by charter section 2) |
| CK-REQ-G4 | Yes | The matrix is the NPR 7123.1D tailoring record: each T row carries `relief_type`, `risk_evaluation`, substitute practice and approval |
| CK-REQ-G5 | N/A | No cybersecurity content; cybersecurity is tailored in the RMM |
| CK-REQ-G6 | No (lien only) | SE-60 to SE-64 name `docs/plan/tpm.json` and TPM-001 to TPM-003 exist; finding-1 carried here as well |
| CK-REQ-G7 | Yes | `tools/render_compliance.py --check` exit 0: rows 62, FC 49, T 4, NA 9, render current; the matrix validates against `se-compliance-matrix.schema.json` in `tools/validate_docs.py` |
| CK-REQ-G8 | Yes | Scripted id check above (0 missing); the `requirement_statement` fields are the Table H-1 text as the field notes state |

**Reviewer findings of this record, as the author reads them.** finding-1 to finding-7 (all Minor) are accepted as liens due PDR, owner compliance-matrix author; none is disputed.

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

Written by `reviewer:INSP-024`, the reviewer role of this record, not the author (charter section 11 rule 4; 08 section 3.1). This is the re-issue without a further product review that package section 2.1 item R8 and the iteration verdict above provide for: only readiness R3 and the product blobs are re-checked. The findings, the item answers of the review, the lien table and the counts stand as reviewed, except where this section says otherwise. **Search first:** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` (query: record readiness fields R1 to R4, author self-check, re-issue verdict APPROVED with liens) ran before any `grep`; `grep` and `git` were used afterwards only to pin lines and blobs.

**Product blobs (record drift rule, package section 2.3).** At HEAD `8ef95d3` `git rev-parse HEAD:<path>` equals the reviewed blob for every `product_files` entry: `se-compliance-matrix.json@790d2562`, `se-compliance-matrix.md@09426930`. `git log --oneline adcfe09..HEAD -- <path>` prints nothing for any of them, so no product changed after the review and no delta verification is needed. The working tree equals HEAD for the product files (`git status --short` on them prints nothing).

**Readiness R3 confirmed.** The author self-check above (filed at `ca22e37` by the author named in the front matter, not by this reviewer) meets both halves of R3 ("the author's return states the self-check against sections A to G below and lists the brief's acceptance criteria"): (a) it lists acceptance criteria AC-1 to AC-7 with a result and evidence for each; the original author briefs are not in the repository, and the criteria are restated from the rules 08 section 1 (WRITING, CITATIONS, SCOPE, COMMANDS) and section 3.1 (row "plans and process documents") impose on every process-document brief, plus the convergence rule, which is the complete set a brief for this product could carry; (b) it answers every applicable item (CK-REQ-A8 and G1 to G8) Yes, No or N/A with evidence, and A1 to A7 and sections B to F N/A by the product-type table, as this record does. Every author No coincides with a reviewer No and names the same findings (A8, G1, G3 and G6, on finding-1 to finding-7); no author answer is Yes where this record answers No; the author disputes no finding and adds no finding. The self-check changed nothing the reviewer owns (`git show ca22e37 -- <this record>` adds only the self-check section) and changed no product.

**Reviewer spot checks of the self-check (2026-09-26, HEAD `8ef95d3`).** `tools/render_compliance.py --check` exit 0 with the NA rows SE-24 to SE-31 and SE-44, "validation PASSED and rendered file is current" (author G7 and the 62 rows FC 49, T 4, NA 9). The JSON still reads `revision_date` 2026-09-25 and `approval.submitted_by` "Claude (lead systems engineer)", so the author's A8 (finding-6) and G3 (finding-5) No answers describe the product at HEAD. Em dash count 0 in both files; the single `TBD` is the SE-39 statement "no TBDs".



**Readiness at re-issue.** R1 Yes (`tools/validate_docs.py` at HEAD `8ef95d3` passes this record and fails only on the INSP-008 drift outside this product; the matrix validates against `se-compliance-matrix.schema.json` within it). R2 as reviewed. R3 **Yes** (changed from No: the self-check above, confirmed here). R4 Yes (re-confirmed: 0 em dashes, and `TBD` only as the name of a rule or list, in every product file at HEAD). R5 N/A. `readiness_met: true`.

**Open Major findings needing an owner ruling:** none. No finding of this record waits on a package decision; package decision 115 (owner waiver of the self-check) is no longer needed for this record.

**Tool runs at re-issue (2026-09-26, HEAD `8ef95d3`, repository root, `.venv/bin/python`).** `tools/validate_docs.py` exit 1: 48 passed, 1 failed of 49; this record PASS as APPROVED (record drift check included); the one failure is `docs/reviews/SRR/checklists/hazard-analysis.md` (INSP-008, record drift against the hazard blobs committed at `ade0e09` for package item R9), outside this record's scope and reported to the lead SE; `tools/traceability.py --report-only` exit 0, 0 violations, 3 warnings (`SYS_UNALLOCATED` REQ-SYS-125 and REQ-SYS-148, `HAZARD_INVERSE` REQ-SW-KEYER-039; none in this product), with the regenerated `docs/vv/traceability-report.md` and `traceability.json` restored by `git checkout`; `tools/render_risk.py --check --gate SRR --hazards docs/safety/hazards.json` exit 0; `python -m unittest discover -s tools/tests` exit 1: 392 tests, 1 failure, `test_validate_docs.RepositoryTests.test_repository_exit_zero`, caused by the same INSP-008 drift; no failure touches this record or its product.

**Measurements (re-issue).** Items re-checked: R1 to R5 and the product blobs; items answered No: 0; new findings: 0; effort 6 turns, 10 minutes (added to the front matter totals).

```
RE-ISSUE (2026-09-26, HEAD 8ef95d3, package item R8): VERDICT: APPROVED (with liens)
FINDINGS: finding-1 to finding-7 Minor, Lien: fix before PDR (unchanged); open Major 0
READINESS: R1 Yes, R2 Yes, R3 Yes (author self-check at ca22e37 confirmed), R4 Yes, R5 N/A; readiness_met true
PRODUCT: docs/process/se-compliance-matrix.json@790d2562; docs/process/se-compliance-matrix.md@09426930 (unchanged since adcfe09)
MEASUREMENTS: re-issue items=R1 to R5 + blobs; no=0; new findings=0; turns=6; minutes=10; cumulative turns=51, minutes=50
```

`record_status` stays Open: the liens are neither Verified nor Deferred by an owner decision, and the software lead closes the record (07 section 10.2, action tracking).
