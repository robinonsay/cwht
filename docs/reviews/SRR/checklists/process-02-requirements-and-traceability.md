---
# Peer-review record (charter section 5; 01 section 13; 08 section 3.2). Copy of
# docs/templates/peer-review-checklist-requirements.md, product type "Plans and process documents"
# (section G, all items, and A8). Slug process-02-requirements-and-traceability as assigned by the
# dispatching session (01 section 13 would give plan-02-requirements-and-traceability; package H1 (c)
# names that slug; see Cross items X-3).
id: INSP-020
checklist: peer-review-checklist-requirements
checklist_revision: C
checklist_file: docs/reviews/SRR/checklists/process-02-requirements-and-traceability.md
product: docs/process/02-requirements-and-traceability.md
# product_commit: last commit touching 02 at the review baseline HEAD adcfe0946d2f1b5cd8f41a8f91eb4219a7fb99a1
# (docs/requirements/README.md was last touched at 4e3f8913366c60e79a9ace6a1b4f36f24adc3479); the working tree equals HEAD for both files
product_commit: "b301df2f96aa979b602c0c4cde9c7f85da979843"
# product_files: git rev-parse HEAD:<path> at adcfe09 (record drift rule, package section 2.3, R13)
product_files: ["docs/process/02-requirements-and-traceability.md@fcdc544555477f0115535348f8ce388453a9034f", "docs/requirements/README.md@89bef4fc2a310767db3655c60f16849ef59eba0c"]
product_size: 02 in 14 sections, 776 lines; README.md 102 lines (layout, related-artifact table of 11 rows, procedure, commands, identifier rules)
sprint: SRR-prep
author_agent: "author:process (Claude main session, lead SE; 02 revision D of b301df2 and README of 4e3f891)"
reviewer_agent: "reviewer:INSP-020"
criticality: neither
# assurance_required: false; 07 section 2.1.1 row "Other process documents (docs/process/0N-*.md except 03, 05 and this plan)" is No in every column
assurance_required: false
assurance_reviewer_agent: none
iteration: 1
# readiness_met: false because R3 (author self-check against sections A to G) is not on record for 02 or README; see Readiness
readiness_met: false
# reviewer_verdict: no Major finding; every Minor finding is "Lien: fix before PDR" (convergence rule of 2026-09-26)
# verdict: held at NEEDS CHANGES only by readiness R3 (not a finding), as in INSP-006, INSP-010 and INSP-022;
# it becomes APPROVED (with liens) on re-issue once the author self-check is filed or the owner waives it (decision 115)
reviewer_verdict: APPROVED
assurance_verdict: not-required
verdict: NEEDS CHANGES
findings_major: 0
findings_minor: 8
findings_open: 0
findings_fixed: 0
findings_verified: 0
# findings_deferred: the 8 liens (fix before PDR)
findings_deferred: 8
assurance_findings_major: 0
assurance_findings_minor: 0
assurance_tasks_applied: []
deferred_rids: []
items_no: [CK-REQ-A8, CK-REQ-G1, CK-REQ-G4, CK-REQ-G7]
effort_turns: 45
effort_minutes: 55
record_status: Open
date: 2026-09-26
date_closed: null
---

# Peer review record INSP-020: requirements and traceability process (02) and the requirements README

**Product:** `docs/process/02-requirements-and-traceability.md` (blob `fcdc5445`, last commit `b301df2`, revision D) and `docs/requirements/README.md` (blob `89bef4fc`, last commit `4e3f891`), both as committed at the review baseline HEAD `adcfe0946d2f1b5cd8f41a8f91eb4219a7fb99a1`; `git diff --quiet HEAD` on both paths is clean. **Checklist:** `docs/templates/peer-review-checklist-requirements.md` revision C, product type "Plans and process documents": section G (CK-REQ-G1 to G8) and CK-REQ-A8, the plan review items `docs/process/08-agent-briefing.md` section 3.1 assigns to process documents. Sections A1 to A7 and B to F apply to requirement files and are N/A. **Gate:** SRR, package `docs/reviews/SRR/package.md` section 2 item H1 (c) (the record `plan-02-requirements-and-traceability` not yet filed) and readiness item R6. **Answer legend:** Yes = Pass, No = Fail, N/A = not applicable; every answer carries its evidence.

**Independence:** the reviewer did not author 02 or the README and did not edit either. **Search first:** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` preceded every manual search (queries: plan review checklist items for 02; SE-07, SE-08, SE-17, SE-18 ETA-approved processes; `SYS_NO_VALIDATION_PATH` and `SECURITY_TAG_NO_SOURCE` in the tool catalogue; an author self-check for 02). `grep -n` was used afterwards only to pin lines; `git show HEAD:<path>` and reads of known paths are not searches.

**Convergence rule (lead SE direction 2026-09-26, charter section 4 item 3):** only Major findings change products in this round; every Minor finding is dispositioned "Lien: fix before PDR" in the lien table below and carried by the package as a Routine item.

## Record

### Findings

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | reviewer | Minor | CK-REQ-G1 | 02 section 2.2 row `SW` (line 58); README "Identifier rules" (line 102) | Both say charter section 6 omits the firmware-wide `SW` module from its module list ("section 14, CI-9"; README: "process section 14 (CI-9) carries that edit"). Charter section 6 (line 109) lists `SW for firmware-wide software requirements` in the `REQ-<MOD>-NNN` list and in the requirement-module sentence, and 02 section 14 row CI-9 (line 755) itself reads "Closed by 4e3f891". The two sentences contradict the charter and the document's own closure record. Fix: delete the clause in 02 line 58 and the last sentence of README line 102. | Lien: fix before PDR | Pending | |
| <a id="finding-2"></a>finding-2 | reviewer | Minor | CK-REQ-G1 | README "Layout" (lines 7, 22, 28) and the related-artifact table (lines 37 to 47) | The README has not changed since `4e3f891` and states repository facts that are false at HEAD: line 7 says files marked `[created before SRR]` "do not exist yet", but `tx/requirements.json` (16 requirements) and `sw/sw-keyer/requirements.json` (38) exist; line 37 "schema only" for test cases (170 cases in `sys`, `tx`, `sw-keyer`, `sw-tool`); line 39 "none yet" for ICDs (five stubs ICD-CTL-KEY, ICD-CTL-PHONES, ICD-CTL-USB, ICD-PWR-CELL, ICD-TX-ANT); line 40 hazards "version 0.2.0-pha" (`hazards.json` is 0.4.2-pha); line 41 `TPM-001` to `TPM-017` with three null `mop_id` (`tpm.json` holds TPM-001 to TPM-020 and six null `mop_id`: 003, 009, 012, 018, 019, 020); line 42 "ADR-001 to ADR-025 exist; no trade study yet" (ADR-026, TS-001 and TS-002 exist); line 44 "none before SRR" (`docs/cm/cr/CR-001-cs11-cs38-driver-construction-arms.md` exists); line 47 `measurements.json` "created at PDR" (it exists, committed `1d423e5`). The table header dates the state "2026-09-25 at 18:15", but the Layout marks are undated. Fix: refresh the layout marks and the table at a named commit. | Lien: fix before PDR | Pending | |
| <a id="finding-3"></a>finding-3 | reviewer | Minor | CK-REQ-G1 | 02 section 14: status paragraph (line 743), rows AL-02-21 (line 771), AL-02-22 (line 772), AL-02-25 (line 775), AL-02-26 (line 776) | Section 14 contradicts section 8.5 and the repository. AL-02-21 reads "Open ... Neither is in 28e49e6; an uncommitted edit ... with three known-answer tests ... failing", while section 8.5 rows T-03 and T-21 (lines 543, 561) read "done (2026-09-26)"; `STAKEHOLDERS_MISSING` is in `tools/traceability.py`, its known answers are in `tools/tests/test_traceability_srr_rules.py`, the suite runs 392 tests OK, and package section 18.2 asks the 02 author to record the closure. AL-02-22 says "no requirement file carries the tag `security` yet, so the trigger has not fired": REQ-SYS-132 and REQ-SYS-134 carry `security` (sources `NGO-005`, `OPS-011` or `OPS-001`/`OPS-021`, `CON-010`), so the trigger has fired and the planned `CON-` of kind `Process` stating the charter section 12 scope does not exist (the Process constraints are CON-017, CON-025, CON-027, CON-028). AL-02-25 and AL-02-26 read "Closed in the working tree ... Confirmed by the commit that records the edit" but name no commit; both edits are committed (01 no longer names `tools/refs/`; SEMP section 9.0 row 10, line 436, both at or before `b301df2`). Fix: refresh the four rows and the status paragraph with the commits; AL-02-22 records the trigger and its disposition (see X-6). | Lien: fix before PDR | Pending | |
| <a id="finding-4"></a>finding-4 | reviewer | Minor | CK-REQ-G1, CK-REQ-A8 | 02 section 3.0 stakeholder table (lines 127 to 136) and line 125; AL-02-21 "eight entries transcribed" (line 771) | The table lists eight stakeholders; `expectations.json`, which line 125 names as the record, holds ten. The two not in the table, "Members of the licensee's household" (role `public`) and "Unlicensed third parties keying under supervision" (role `guest operator`), each give `represented_by` "Robin ... per docs/process/02-requirements-and-traceability.md section 3.0", a basis the table does not show. The representation rule (line 138) is stated by role group and still covers both, so V2 is not broken. Fix: add the two rows (interests, representation, sources SI-030 and SI-019, SI-030) or replace the table with a pointer to `expectations.md` section 7. | Lien: fix before PDR | Pending | |
| <a id="finding-5"></a>finding-5 | reviewer | Minor | CK-REQ-G4 | 02 section 2.3 row "Reused and OSS components" (line 74); section 13 row SWE-211 (line 726) | The row says each reused-component requirement "is verified to the same level as developed code (SWE-027 item e; SWE-211; RMM rows SWE-027 and SWE-211)" and section 13 maps SWE-211 without qualification. `docs/process/rmm.json` gives both rows disposition `T`: SWE-027 relieves sub-item c (Center IP counsel); SWE-211 relieves structural coverage (line, region, MC/DC) of Rust `core` and tests its used features at feature level only (04 section 4; charter section 12 row "Non-custom software testing (SWE-211)", "Tailored, proposed for owner decision at SRR"). The document relies on both tailored requirements without mirroring the dispositions, and its sentence reads as full compliance for Rust `core`. Fix: state "(RMM rows SWE-027 and SWE-211, disposition T)" and the Rust `core` structural-coverage relief with its 04 section 4 pointer, in section 2.3 and in section 13. | Lien: fix before PDR | Pending | |
| <a id="finding-6"></a>finding-6 | reviewer | Minor | CK-REQ-G1 | 02 section 6.2 paragraph (line 385) | The dated state "2026-09-25 (read at 18:10)" is superseded and the rule in it is not followed by the products: `tpms[]` now holds TPM-001 to TPM-020 and six TPMs carry `mop_id: null` (TPM-018, TPM-019, TPM-020 added to TPM-003, 009, 012); `expectations.json` holds MOE-001 to MOE-013 and MOE-013 is named by no MOP (T-20 makes that an error only from PDR); the paragraph says the MOPs' `requirement_ids` and `tc_ids` are filled "in the commit that adds the requirement or case", yet L1 and L2 requirements cite MOP-001 to MOP-016, MOP-018 and MOP-020 in `mop_ids` while all 20 MOPs have empty `requirement_ids` and `tc_ids`. The paragraph also creates a second stored copy of the requirement-to-MOP link that no tool rule checks, against the store-once principle of section 7 (line 410). Fix: refresh the snapshot, and either make the MOP lists derived by `tools/traceability.py` (T-16) or add a T-16 agreement check; the data fix is cross item X-2. | Lien: fix before PDR | Pending | |
| <a id="finding-7"></a>finding-7 | reviewer | Minor | CK-REQ-A8 | 02 section 4.6 worked example (lines 290 to 327) | The example says its `REQ-` and `TC-` ids other than REQ-SYS-002 "are illustrative until those files exist". The files exist and the ids collide with different requirements: the real REQ-SYS-002 is "Operating modes and transitions", REQ-SYS-004 "Carrier end on an inhibit, flag or latched fault", REQ-SYS-005 "Fault-safe exit" (straight-key and paddle keying are REQ-SYS-038 and REQ-SYS-039); the real REQ-SW-KEYER-002 is "Straight-mode input selection", 003 "Self-completing paddle elements", 004 "Non-shortening inter-element space", 006 "Squeeze alternation", where the example makes 004 a key-down timeout and 006 a power-on interlock. A reader following the example to the files lands on unrelated requirements. Fix: re-key the example to the real ids, or state that its numbering is fictional and refers to `docs/templates/requirements.example.json` only. | Lien: fix before PDR | Pending | |
| <a id="finding-8"></a>finding-8 | reviewer | Minor | CK-REQ-G7 | 02 section 8.5 (line 537 and table lines 539 to 563) | Section 8.5 says the table "binds each T-rule to the codes that implement it today". Five requirements-side codes of `CHECK_CATALOGUE` (74 codes) appear nowhere in 02: `SCHEMA_ID_PATTERN_MISSING` (Warning, schema id pattern, T-01), `MODULE_UNKNOWN` (T-02), `RATIONALE_EMPTY` (WR-10, charter section 7), `HAZARD_CONTROL_UNTRACED` (T-08, software requirement named by a hazard without the back-link) and `HAZARD_REQ_NOT_ON_TARGET` (T-08 and 01 section 8.6 at SAR). Every code the table does name exists in the catalogue. Fix: add the five codes to rows T-01, T-02, T-08 and to WR-10 or T-17. | Lien: fix before PDR | Pending | |

### Lien table

| Finding | Severity | Disposition | Owner | Due | Package item |
|---|---|---|---|---|---|
| finding-1 | Minor | Lien: fix before PDR | 02 and README author (Claude, lead SE) | PDR readiness declaration | Routine item |
| finding-2 | Minor | Lien: fix before PDR | README author (Claude, lead SE) | PDR readiness declaration | Routine item |
| finding-3 | Minor | Lien: fix before PDR | 02 author (Claude, lead SE) | PDR readiness declaration | Routine item (the AL-02-22 disposition with X-6) |
| finding-4 | Minor | Lien: fix before PDR | 02 author (Claude, lead SE) | PDR readiness declaration | Routine item |
| finding-5 | Minor | Lien: fix before PDR | 02 author (Claude, lead SE) | PDR readiness declaration | Routine item |
| finding-6 | Minor | Lien: fix before PDR | 02 author (Claude, lead SE); data part X-2 | PDR readiness declaration | Routine item |
| finding-7 | Minor | Lien: fix before PDR | 02 author (Claude, lead SE) | PDR readiness declaration | Routine item |
| finding-8 | Minor | Lien: fix before PDR | 02 author with the tool owner (Claude, software lead) | PDR readiness declaration | Routine item |

**Counts.** 8 findings, all Minor, all Lien; Closed 0, Disputed-accepted 0; open Major 0. No finding needs an owner ruling.

### Per-requirement validation

N/A: the product is a process document and a README; neither defines a requirement.

## Readiness criteria (all true before the review starts)

| # | Criterion | Answer | Evidence |
|---|---|---|---|
| R1 | The product validates: `tools/validate_docs.py` exits 0 | Yes | Run 2026-09-26 at HEAD `adcfe09` before this record: exit 0 (`--quiet`, no failure). 02 and the README are Markdown and not schema-validated |
| R2 | `tools/traceability.py` reports no violation for the ids in the file | Yes | `--report-only --output <scratch>`: "237 requirements, 170 test cases, 0 violation(s), 2 warning(s)" (`SYS_UNALLOCATED` REQ-SYS-125, REQ-SYS-148); neither product defines an id |
| R3 | The author's return states the self-check against sections A to G and the brief's acceptance criteria | No | No author self-check for 02 or the README was supplied with this assignment, none is in the products, and the claude-context search for one found none. The 02 status line (line 3) lists the revision D changes, which is not the self-check (charter section 11 rule 2). Package decision 115 lists INSP-001, 002, 003, 004, 010, 011 and 014 only (cross item X-4). Not a finding; it holds `readiness_met` false |
| R4 | Every TBR has owner, plan, close_by; no `TBD` string used as a value | Yes | `TBD` occurs in 02 only as a rule subject (lines 3, 197, 235 in the WR-07 list, 460, 597) and not in the README; neither file carries a TBR value |
| R5 | For a CR: impact assessment attached | N/A | Not a CR |

## Participants

Author `author:process` (not present). Reviewer `reviewer:INSP-020` (this record). Software assurance reviewer: not required (07 section 2.1.1, row "Other process documents"). Owner: disposition at the review.

## A. Format and editorial (plan items: A8 only)

| Id | Answer | Evidence |
|---|---|---|
| CK-REQ-A1 to CK-REQ-A7 | N/A | Requirement-statement items; the product defines no requirement |
| CK-REQ-A8 | No | finding-4 (stakeholder table short of the record) and finding-7 (worked-example ids collide with the real files). Otherwise terminology matches the charter and the schemas: module tokens, statuses `Draft`, `Active`, `Verified`, `Closed`, key types "straight key" and "iambic paddles", the 3.5 mm TRS jack of ADR-009; `grep -c` for the em dash character returns 0 in both files |

## B to F

N/A for a plan or process document (template product-type table, row "Plans and process documents": G and A8).

## G. Plans, process documents and decision records (SWE-087 b)

| Id | Answer | Evidence |
|---|---|---|
| CK-REQ-G1 | No | 02 expands charter sections 5, 6 and 7 (header line 3). Checked against the charter (sections 2, 3, 5, 6, 7, 9, 11, 12), `docs/process/rmm.json` (SWE-027, 050 to 055, 184, 200, 210, 211), `docs/process/se-compliance-matrix.json` (SE-07, SE-08, SE-17, SE-18 all FC with ETA approval, consistent with the header's approval line), ADR-009 (TRS jack, used in sections 3.5 and 4.6) and ADR-024 (keyer speed). Agreements confirmed: levels and TBR limits (L1 by PDR, L2 by CDR) match charter section 7; the Verified-versus-Closed rule for host-verified software (section 4.4, lines 271 to 273; T-11) matches charter section 9; the retirement markers (section 11.3) match charter section 6; the single peer-review record in `checklists/` (section 5 line 333) matches charter section 5. Disagreements: finding-1 (charter section 6), finding-2, finding-3, finding-4 and finding-6 (statements false against the repository or the document's own section 8.5) |
| CK-REQ-G2 | Yes | Every step names what it consumes and produces with path and id scheme: sections 3.0 to 3.5 (Consumes/Produces lines 123, 142, 150, 189), the 4.1 procedure table (lines 210 to 221), 8.6 records per inconsistency kind (lines 571 to 577), 10.3 CR content, 11.1 allocation. No "as appropriate", "TBD" or "should consider" outside the WR-07 banned list and rule text (grep, section R4) |
| CK-REQ-G3 | Yes | Section 1 roles table (lines 15 to 22): Robin as Decision Authority, CCB and ETA, author, independent reviewer (never the author, charter section 2), test author, tool, software lead. Owner approval points: header (ETA approval in the SRR memo), V2 (section 5), 8.7 waivers item 2, 9 rule 5 (missed TBR liens), 10.1 (Robin sole dispositioner), 11.2 baseline flip on the memo |
| CK-REQ-G4 | No | Mirrored correctly: the single-valued `priority` customization (section 6.4) is SEMP section 9.0 row 10 (line 436); SWE-200 (RMM FC, "Planned") matches section 10.4; SWE-210 (RMM T) matches the section 2.4 Security row. Not mirrored: SWE-027 and SWE-211 dispositions (finding-5) |
| CK-REQ-G5 | N/A | The cybersecurity assessment is 07 section 16 (assets, surfaces and mitigations in 16.2, lines 688 to 693; verification 16.4; detection data 16.5), reviewed under INSP-010. The requirement-side hooks 02 owns were checked and exist: section 2.4 Security row (line 103), tag `security` obligations (line 83), ICD `Security expectations` rows (line 197), NPR 7123.1D section 3.2.3.2 and section 3.2.2.2 item h cited correctly |
| CK-REQ-G6 | Yes | Section 10.4: MSR-02 volatility with its counting rule (N_start, A, M, R, C2), formula, reporting periods, thresholds (10 % and 20 %) with the action at each, script (`tools/traceability.py --volatility`, planned PDR) and storage (`docs/plan/measurements.json`, mirrored to TPM-012); consistent with RMM SWE-200 (FC, Planned). Section 3.5 "Measures" row names the ICD measures and where they are reported |
| CK-REQ-G7 | No | True and dated: section 8.1 options equal `tools/traceability.py --help` at HEAD (`--root`, `--output`, `--json`, `--report-only`, `--quiet`, `--render`, `--regression`); the planned `--gate SRR` and `--volatility` each exit 2, as README line 90 says; every code the 8.5 "Tool codes today" column names is in `CHECK_CATALOGUE`, and the planned codes `SYS_NO_VALIDATION_PATH` and `SECURITY_TAG_NO_SOURCE` are absent, as the table says; `closing_cases` (line 606 of the tool) selects by method only, so the T-09 and T-10 module rows are truly "except module rule"; section 8.5 states the tool has no T-rule ids and no `--gate`. Incomplete: finding-8 (five catalogue codes unbound) |
| CK-REQ-G8 | Yes | Every identifier pinned in `docs/references/md/`: SE-07 (NPR 7123.1D 3.2.2.1), SE-08 (3.2.3.1), SE-17 (3.2.12.1), SE-18 (3.2.13.1), SE-35, SE-37, SE-39, SE-40, SE-42 (chapter 5 product lists), section 3.2.2.2 item h and 3.2.3.2 text; SWE-027, 050, 051, 052, 053, 054, 055, 087, 184, 200, 210, 211 bracketed in the NPR 7150.2D chapters; App. G Table G-3 entrance 3.1, G-4 entrance 5.1, 6.8, 6.11, 6.12 and success criteria 3, 4, 8, 14, G-5 entrance 5.2 and 5.3, G-6 entrance 5.1, G-7 entrance 5; SE HB sections 4.1.1.2.1, 4.1.1.2.3, 4.1.1.2.6, 4.2.1.2.1 to 4.2.1.2.6, 6.2.1.1, 6.2.1.2.3 to 6.2.1.2.5, 6.3.1.2.3, 6.5.1.2.3 (waiver text under it), Table 4.2-2, App. C C.4. The quoted phrases are verbatim in the corpus: "All relevant stakeholder groups identify and remove defects" and "A KDR can have any priority or criticality" (SE HB 4.2), "may not belong at the higher level" and "the next higher level requirements sources" (SE HB 6.2), the App. C C.4 verifiability question, the SWE-184 phrase "between the hardware, operator, and software" and the section 3.12.1 Note (NPR 7150.2D). 47 CFR files exist for 97.307 (paragraph (e) present), 97.305, 97.313, 97.119, 97.13, 1.1310, 2.1093 and the `47cfr-2.106-harmonic-bands.md` extract; the versioner API command is in the regulatory README line 8 |

## Cross items (outside this product; for Claude as integrator)

| # | Item | Owner |
|---|---|---|
| X-1 | **Section 8.5 rows due "before SRR" are not implemented:** T-07 `SYS_NO_VALIDATION_PATH` and `SECURITY_TAG_NO_SOURCE` (0 occurrences in `tools/traceability.py`), the T-09 and T-10 closing-case module rule (`closing_cases` is method-only). 02 section 1 (line 22) blocks "a gate's readiness declaration ... until the rows due at that gate exit 0 on a seeded fixture" and section 12 (line 693) lists "the section 8.5 rows due before SRR done" as an SRR deliverable; package section 2.1 (R1 to R15) and section 18.2 do not carry it. The product text is accurate, so this is not a product finding. By-hand application at HEAD by this reviewer: every one of the 181 non-retired SYS requirements cites an `OPS-` or `MOE-` id; the two `security`-tagged requirements (REQ-SYS-132, REQ-SYS-134) cite a `CON-` id; no non-software requirement is closed only by a `HostUnit` or `Emulation` case. So the data would pass; the open item is the tool rows or an owner re-plan of their due gate to PDR (which is an edit of 02 section 8.5) | Claude as software lead (implement with known-answer tests), or Robin (re-plan) |
| X-2 | `docs/plan/tpm.json`: all 20 MOPs have empty `requirement_ids` and `tc_ids` although requirements cite 18 of them in `mop_ids` (02 section 6.2 rule; finding-6) | `tpm.json` author and the L1 requirements author |
| X-3 | Slug: this record uses the assigned path `process-02-requirements-and-traceability.md`; 01 section 13 and package H1 (c) name `plan-02-requirements-and-traceability`. The package should map the two when it counts H1 (c) | Package author |
| X-4 | Readiness R3: no author self-check for 02 and the README; package decision 115 should add INSP-020 (and INSP-022) or the author files the self-check | Claude (02 author); Robin (decision 115) |
| X-5 | `docs/process/04-verification-and-validation.md` section 7.4 does not bind the evidence-side catalogue codes `VAL_TARGET_UNRESOLVED`, `NCR_NO_REQUIREMENT` and `NCR_FIELD_INVALID` (0 occurrences in 04); `tools/README.md` names them | 04 author |
| X-6 | AL-02-22 substance: REQ-SYS-132 and REQ-SYS-134 meet the `security` tag through `CON-010` (the USB connector constraint), which INSP-003 finding-22 accepted; 02 section 2.3 (line 83) asks for a `CON-` or `ADR-` "that records the cybersecurity assessment scope of charter section 12", and AL-02-22 planned a dedicated `CON-` of kind `Process`. Either the 02 author records that `CON-010` plus the `Security:` rationale item satisfies the obligation, or the expectations author adds the planned `CON-` before PDR | 02 author; expectations author |

## Tool runs (2026-09-26, HEAD `adcfe09`)

| Command | Exit | Result |
|---|---|---|
| `.venv/bin/python tools/validate_docs.py --quiet` (before the record) | 0 | no failure |
| `.venv/bin/python tools/traceability.py --report-only --output <scratch>/tr.md` | 0 | 237 requirements, 170 test cases, 0 violations, 2 warnings (`SYS_UNALLOCATED` REQ-SYS-125, REQ-SYS-148) |
| `.venv/bin/python tools/traceability.py --help`; `--gate SRR`; `--volatility` | 0; 2; 2 | options as in 02 section 8.1; planned options rejected as usage errors |
| `.venv/bin/python tools/render_rmm.py --check`; `render_compliance.py --check`; `render_risk.py --check --gate SRR --hazards docs/safety/hazards.json` | 0; 0; 0 | consulted for G4 and G1 |
| `.venv/bin/python -m unittest discover -s tools/tests` | 0 | 392 tests OK |
| `.venv/bin/python tools/validate_docs.py` (after the record) | 0 | 45 passed, 0 failed; this record PASS against the built-in peer-review record schema |

## Measurements (SWE-089)

| Measure | Value |
|---|---|
| Product size | 02: 14 sections, 776 lines; README: 102 lines |
| Items checked | 9 (CK-REQ-A8, CK-REQ-G1 to G8) plus R1 to R5 |
| Items answered No | 4 (CK-REQ-A8, CK-REQ-G1, CK-REQ-G4, CK-REQ-G7) |
| Findings by severity | Major 0, Minor 8 |
| Findings fixed, deferred (lien) | 0, 8 |
| Iteration | 1 |
| Effort | 45 turns, 55 minutes |

## Verdict (returned by the reviewer)

```
VERDICT: APPROVED (with liens) at the finding level; record verdict NEEDS CHANGES solely on readiness R3
FINDINGS:
- [Minor] CK-REQ-G1 02 section 2.2 line 58, README line 102: charter section 6 does list SW (CI-9 closed); delete the clause. Lien: fix before PDR
- [Minor] CK-REQ-G1 README lines 7 to 47: layout marks and state table false at HEAD (tx, sw-keyer, test cases, ICDs, hazards version, TPM range, ADR-026, TS-001/002, CR-001, measurements.json). Lien: fix before PDR
- [Minor] CK-REQ-G1 02 section 14 AL-02-21, 22, 25, 26: stale statuses (T-21 done, security tag trigger fired, commits unnamed). Lien: fix before PDR
- [Minor] CK-REQ-G1, A8 02 section 3.0: table has 8 stakeholders, expectations.json 10. Lien: fix before PDR
- [Minor] CK-REQ-G4 02 section 2.3 line 74, section 13: SWE-027 and SWE-211 disposition T and the Rust core relief not mirrored. Lien: fix before PDR
- [Minor] CK-REQ-G1 02 section 6.2 line 385: superseded snapshot; MOP requirement_ids rule unmet and unchecked. Lien: fix before PDR
- [Minor] CK-REQ-A8 02 section 4.6: example ids collide with the real L1 and SW-KEYER requirements. Lien: fix before PDR
- [Minor] CK-REQ-G7 02 section 8.5: five catalogue codes unbound to any T-rule. Lien: fix before PDR
ITEMS N/A: CK-REQ-A1 to A7, sections B to F (process document); CK-REQ-G5 (assessment in 07 section 16)
MEASUREMENTS: size=776+102 lines; items=9; items_no=4; major=0; minor=8; lien=8; open_major=0; iteration=1; turns=45; minutes=55
```

The record turns APPROVED (with liens), with no further finding review, when the 02 author files the self-check against section G and A8 or the owner waives R3 under package decision 115 (`tools/validate_docs.py` refuses `verdict: APPROVED` with `readiness_met: false`).

## Author self-check (readiness R3; SRR package item R7)

Filed by the author, `author:process` (Claude main session, lead SE, the author named in this record's front matter), on 2026-09-26 at HEAD `ade0e09`, in answer to readiness R3 ("the author's return states the self-check against sections A to G below and lists the brief's acceptance criteria") and package item R7. 01 section 13 makes this file the single peer-review record for the product and requires that no record live only in conversation, so the self-check is filed here. This section is the author's only content in the record: the front matter (including `readiness_met` and `verdict`), the findings, the readiness answers and the verdict belong to the reviewer and are unchanged. The reviewer confirms this self-check and answers R3 at the re-issue (package item R8); the author does not mark its own product reviewed (08 section 3.1).

**Product files checked.** `docs/process/02-requirements-and-traceability.md@fcdc5445` (revision D), `docs/requirements/README.md@89bef4fc`. Each blob equals `git rev-parse HEAD:<path>` at `ade0e09` and equals the blob this record reviewed, so the self-check covers the reviewed product. The product files are not changed by this self-check (convergence rule).

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

**Scripted scan (AC-2, AC-3).** Over both files: 0 em dashes. The one "should consider" hit (02 line 235) is inside the WR-07 banned-word list itself, not a use. `TBD` appears 11 times in 02 and not in the README, each as a rule subject (for example lines 240 WR-12, 485 T-14, 593 section 9 heading, 595 rule 1), never as a value. Every SE id cited (12 distinct) and every SWE id cited (14 distinct) exists bracketed in the corpus (0 missing).

**Self-check against the checklist** (`docs/templates/peer-review-checklist-requirements.md` revision C, product type "Plans and process documents": CK-REQ-A8 and section G; A1 to A7 and sections B to F are N/A for a process document by the product-type table).

| Id | Author answer | Evidence |
|---|---|---|
| CK-REQ-A8 | No (liens only) | Terminology follows the charter and `docs/requirements/schema.json`. Known defects, Minor: finding-4 (the section 3.0 stakeholder table lists 8 of the 10 `stakeholders` of `expectations.json`), finding-7 (section 4.6 worked-example ids collide with the real files) |
| CK-REQ-G1 | No (liens only) | 02 expands charter sections 7, 6 and 5 (header line 3). Known disagreements, Minor: finding-1 (charter section 6 already lists the `SW` module), finding-2 (README layout facts stale at HEAD), finding-3 (section 14 statuses against section 8.5), finding-4, finding-6 (section 6.2 dated TPM and MOE state) |
| CK-REQ-G2 | Yes | Sections 3.0 to 3.5 name what each step consumes and produces with path and id scheme; the 4.1 procedure table; section 11 id allocation and retirement |
| CK-REQ-G3 | Yes | Section 1 roles table: Robin as Decision Authority, CCB and ETA; author; independent reviewer; test author; tool |
| CK-REQ-G4 | No (lien only) | Tailoring mirrored except finding-5 (section 2.3 row "Reused and OSS components" and section 13 row SWE-211 state full verification where `rmm.json` gives SWE-027 and SWE-211 disposition T) |
| CK-REQ-G5 | N/A | The cybersecurity assessment is 07 section 16 |
| CK-REQ-G6 | Yes | Section 10.4: MSR-02 volatility with counting rule, formula, thresholds (10 % and 20 %), actions and script |
| CK-REQ-G7 | No (lien only) | `tools/traceability.py --help` lists exactly the options section 8.1 names (`--root`, `--output`, `--json`, `--report-only`, `--quiet`, `--render`, `--regression`); `--report-only` exits 0. Known gap, Minor: finding-8 (five requirements-side codes of `CHECK_CATALOGUE` are not bound to a T-rule in section 8.5) |
| CK-REQ-G8 | Yes | Scripted id check above (0 missing) |

**Reviewer findings of this record, as the author reads them.** finding-1 to finding-8 (all Minor) are accepted as liens due PDR, owner 02 author; none is disputed. None changes a requirement, a hazard control or a traceability rule the tool enforces today.

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
