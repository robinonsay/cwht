---
id: CR-015
title: Fix the SRR record liens of 01, 02, 08, the process index and the compliance matrix
status: Dispositioned
class: II
originator: Claude
date_opened: 2026-09-27
phase: B
configuration_at_origination: baseline/srr (tag on 779f93f); change set prepared on branch base 7784672 (head of cr/CR-012-pdr-checklist-templates, on main 573f9f5); branch head 7efd900; main at origination 11b1b1d
baseline_affected: baseline/srr
affected_cis: [2, 3, 53]
affected_paths: [docs/process/01-lifecycle-and-reviews.md, docs/process/02-requirements-and-traceability.md, docs/process/08-agent-briefing.md, docs/process/README.md, docs/process/se-compliance-matrix.json, docs/process/se-compliance-matrix.md, docs/templates/decision-memo.md, docs/templates/peer-review-checklist-requirements.md]
affected_ids: []
related: [INSP-019, INSP-020, INSP-022, INSP-024, RFA-SRR-006, CR-011, CR-012, CR-013, CR-016]
target_release: none
branch: cr/CR-015-process-liens-01-02-08
disposition: Approved
disposition_date: 2026-09-28
relook_trigger: null
relook_by: null
merge_sha: null
date_closed: null
---

# CR-015: Fix the SRR record liens of 01, 02, 08, the process index and the compliance matrix

Template: `docs/templates/change-request.md`. Process: `docs/process/05-configuration-and-data-management.md` §5.1 to §5.3. File location: this file, committed on `main` with `Refs: CR-015`. Status: **Submitted**. Work package: WP-PDR-12 of `docs/plan/pdr-work-plan.md` (revision 2), wave 1a, "Process document liens: 01, 02, 08, compliance matrix". This is the plan register's PCR-2 (section 6.2). CR-013 and CR-014 were claimed by the parallel wave 1a work packages WP-PDR-13 and WP-PDR-09 (branches `cr/CR-013-*` and `cr/CR-014-*`), so this CR takes CR-015; the retired-status schema CR of the same work package (PCR-3) is CR-016.

**Scope against the plan register.** The register names PCR-2 as "changes to 01 and 02 that are not Log class". The work package's other outputs are also class-CR configuration items after `baseline/srr`: 08 and `docs/process/README.md` (05 Table 4-1 row 2), the compliance matrix (row 3, CR for every field) and the two templates (row 53). One CR carries all of them, so one section 6 review and one disposition cover the work package. The only Log-class output, `docs/requirements/README.md` (row 40), was committed on `main` at `11b1b1d` with `Refs:` and is outside this CR.

**Where the change is.** The product change is prepared on `cr/CR-015-process-liens-01-02-08`, head `7efd900`, as the Submitted state of 05 §5.2 allows ("Branch `cr/CR-NNN-<slug>` may be opened for prototyping; nothing merges"). The branch starts from `7784672`, the head of `cr/CR-012-pdr-checklist-templates`, because CR-012 changes 08 sections 3.1 and 3.5 and this CR changes the same file (header, sections 1, 3.1, 3.2, 3.5 and 4). This CR therefore merges with or after CR-012, never before it, and the INSP-022 delta iteration that verifies 08 lands with or after the CR-012 merge (section 5 step 6). The exact before and after text is `git diff 7784672 7efd900`.

Frozen products for review (PDR work plan rule C2), at branch commit `7efd900`:

| File (Table 4-1 row) | Blob at `baseline/srr` | Blob at `7efd900` | Records that verify it |
|---|---|---|---|
| `docs/process/01-lifecycle-and-reviews.md` (row 2) | `eabbbd57` | `53a9983ced97332aaea645e43090243211da6466` | INSP-019 |
| `docs/templates/decision-memo.md` (row 53) | `1d3ce437` | `dd20b87dc093198f5896d9bfa9ef625068055d22` | INSP-019 |
| `docs/process/02-requirements-and-traceability.md` (row 2) | `fcdc5445` | `1f8fd1646212a1b4022993cf541db7944549058b` | INSP-020 |
| `docs/requirements/README.md` (row 40, Log; on `main` at `11b1b1d`, not on this branch) | `89bef4fc` | `156de8c06cccb7b4e29d411e91d7234dae67e70b` (on `main`) | INSP-020 |
| `docs/process/08-agent-briefing.md` (row 2; CR-012 base `56c54011` at `7784672`) | `01a36bac` | `374fd777b1f05e408c133ed1f222b6cb90865114` | INSP-022 |
| `docs/process/README.md` (row 2) | `3664073b` | `dc4fdf1708d3c661393706d8768e77d4cc65ca14` | INSP-022 |
| `docs/process/se-compliance-matrix.json` (row 3) | `790d2562` | `e0766032be5fe890739ab0d83a31d1148bab76cd` | INSP-024 |
| `docs/process/se-compliance-matrix.md` (row 3, rendered) | `09426930` | `c7fd562e9366178963f35982f97861705f8fce4a` | INSP-024 |
| `docs/templates/peer-review-checklist-requirements.md` (row 53) | as on `main` | `7fd57b3f73beeeb8bab0079eee7e6d313781bd3c` | INSP-022 (finding-5 asks for this change) |

## 1. Description of the change

Each change closes a record lien of the SRR review records (RFA-SRR-006, lien L-6; PDR work plan carried items C-114 to C-139). Finding references are `docs/reviews/SRR/checklists/<record>.md#finding-<n>`.

### 1.1 `docs/process/01-lifecycle-and-reviews.md` (INSP-019, `process-01-lifecycle-and-reviews.md`)

| Location | Change | Closes |
|---|---|---|
| Header | Status "Draft for SRR" becomes "Baselined at SRR (blob `eabbbd57`); revision PDR-1 proposed by CR-015" | INSP-019 O-3 |
| §1 item 6 | The owner's capacities follow charter §2 at `6ea6b1d` (Health and Medical TA, CIO/SAISO designee; SRR decision 7) | charter alignment |
| §2.1 row "Independent peer review or inspection" | The four-checklist list is replaced by a pointer to all `peer-review-checklist-*.md` templates and the single table of 08 §3.5 | finding-4 (c) |
| §3.5 row "Decommissioning and disposal plans" | The parenthesis "section 15 item 2 corrects the charter's stated basis" is removed | finding-1 |
| §3.5 new row | Software Requirements Review (SWEHB Topic 7.09, PAT-068): Customized (substitute), carried by the SRR 4.6 and PDR 5.6 rows | INSP-019 O-1 |
| §4.6 rows SWE-087 a and b | The record paths become the filed SRR records (INSP-003, INSP-004 with INSP-026; INSP-010 with INSP-018; examples of the other plan records) | finding-4 (a) |
| New §12.3 | The convergence rule for reviewer findings: delta iterations verify Major fixes only, Minor findings ride with APPROVED as record liens with owner and due gate, at most three iterations | INSP-019 O-2; INSP-022 finding-5 (01 side) |
| §13 row "Peer review record" | Slug forms as filed at SRR and PDR, the path fixed at creation (Record class, row 33) and the pointer to 08 §3.5; the optional fields `product_files` and `product_blob`; the record drift rule and the record state rule of `tools/validate_docs.py`; the lead SE convention of 2026-09-27 for records of products on an unmerged CR branch (record verdict held until the merge; first applied by INSP-031); the author self-check filed in the record (readiness R3) | finding-2; finding-4 (b); X-1 of INSP-019, INSP-020, INSP-022 |
| §14 closing sentence | "The compliance matrix rows ... cite this document by section" becomes a statement that the matrix row is the authority, with the rows that name 01 counted by script (SE-32 to SE-34 and SE-57 in `implementation_ref`; SE-47, SE-48 and SE-51 to SE-56 in the justification) | finding-3 |
| §15 lead paragraph and item 2 | Item 2 becomes Resolved at charter commit `4e3f891` (charter §3 row "E / F", the combined-review sentence and §12, verified in the charter blob of `baseline/srr`); the status basis is re-dated 2026-09-27 | finding-1; INSP-024 X-3 |
| New §16 | Review results (NPR 7123.1D §5.2.1.2; §9 additional completion item): SRR results (disposition, baseline, tailoring, criteria unchanged, lessons learned), the customizations learned at SRR with where each is now stated, and the PDR trigger with the dates the owner approved on 2026-09-27 (OD-01: readiness Tue 2026-10-06, PDR about Thu 2026-10-08, `baseline/pdr` about Fri 2026-10-09) as planning targets under the event-based rule of §1 item 2 | work plan outputs "SRR results, review schedule; the new PDR date if OD-01 approves"; gate reader F item 52 |

### 1.2 `docs/templates/decision-memo.md` (INSP-019 finding-5)

Section 7.1 gains the line "Same risk accepted as official spokesperson for bystanders and household members (03 section 4.4 ...)", and the classification line names both concurrences, the peer review record and the software assurance record (`classification-03-software-classification-and-rmm-software-assurance.md`), with `<REVIEW>` in place of `SRR` in the paths. The SRR memo already carries both (memo section 7.1, INSP-019 X-4).

### 1.3 `docs/process/02-requirements-and-traceability.md` (INSP-020, `process-02-requirements-and-traceability.md`)

| Location | Change | Closes |
|---|---|---|
| Header | Status and approval state the SRR baseline (blob `fcdc5445`, decision 1) and this revision | status |
| §2.2 row `SW` | The clause "charter section 6 omits it from its module list (section 14, CI-9)" is removed | finding-1 |
| §2.3 row "Reused and OSS components"; §13 rows SWE-027 and SWE-211 | The RMM dispositions T of SWE-027 (item c) and SWE-211 (no structural coverage of Rust `core`, feature-level tests, 04 §4) are stated where the rows rely on them | finding-5 |
| §3.0 stakeholder table | The two entries of `expectations.json` missing from the table (household members; supervised unlicensed third parties) are added, and the JSON is named as the record | finding-4 |
| §4.6 worked example | The `REQ-` and `TC-` ids are stated as fictional, with the real ids that collide named | finding-7 |
| §6.2 paragraph | The snapshot is re-read at `baseline/srr` (TPM-001 to TPM-020, six null `mop_id`, MOE-013 without a MOP); a "Single stored link" rule makes the requirement's `mop_ids` the one stored link, limits a MOP's `requirement_ids` and `tc_ids` to the value-carrying requirement and its closing case, sends the data fill to the `tpm.json` writer (WP-PDR-29, INSP-020 X-2) and the agreement check to the tool owner (WP-PDR-06, T-16) | finding-6 |
| §14 lead paragraph and status refresh | CI-10 closed by SRR decision 103; the status refresh re-dated 2026-09-27 at `7bb994f` | finding-3 |
| §14 rows CI-3, CI-10, AL-02-20, AL-02-21, AL-02-22, AL-02-25, AL-02-26 | CI-3 points to CR-016; CI-10 closed; AL-02-20 re-checked and sent to the 07 writer (WP-PDR-17, 13, 47 order) before WP-PDR-35; AL-02-21 closed by `1d423e5`; AL-02-22 records that the trigger fired (REQ-SYS-132, REQ-SYS-134 cite `CON-010`) and sends the dedicated `CON-` of kind Process to the L0 writer (WP-PDR-10, then WP-PDR-02), due before the PDR readiness declaration; AL-02-25 and AL-02-26 closed by `b301df2` | finding-3; INSP-020 X-6; work plan output "AL-02-20 aligned with 07 §4 item 2" |

INSP-020 finding-8 (five catalogue codes missing from the §8.5 table) is not changed here: CR-011 (WP-PDR-06) rewrites §8.5 and adds `SCHEMA_ID_PATTERN_MISSING`, `MODULE_UNKNOWN`, `RATIONALE_EMPTY`, `HAZARD_CONTROL_UNTRACED` and `HAZARD_REQ_NOT_ON_TARGET` to rows T-01, T-02, T-17 and T-08 on its branch. The INSP-020 delta verifies finding-8 on the CR-011 blob once CR-011 merges. `git merge-tree` of this branch with `cr/CR-011-traceability-pdr-rules` reports no conflict (author run, 2026-09-27).

### 1.4 `docs/process/08-agent-briefing.md` (INSP-022, `process-08-agent-briefing.md`)

| Location | Change | Closes |
|---|---|---|
| Header | Approval at SRR, the CRs that change it (CR-012, CR-015), "Aligned to: charter commit `6ea6b1d`" (the charter of `baseline/srr`) | finding-1 |
| §1 repo map | `traceability.json` in `docs/vv/` and in the per-review files; `<TC-ID>-r<N>/` run artifacts; `docs/design/sw/<module>.md`; `firmware/devcheck/` and `THIRD-PARTY-NOTICES.md` as planned (charter §5 at `6ea6b1d`); `docs/lessons-learned.md` exists; the template list names all eleven checklists; the tools line restated at `7bb994f` with `measurements.py`, `unsafe_audit.py`, `complexity_gate.py`, `ltspice-batch.sh`, `emu_run.sh` and the fifteen test modules, and the planned tools with their gates | finding-1; finding-2 (repo map); finding-3 (a), (c) |
| §3.1 | "trade studies" gets its own row with `peer-review-checklist-risk.md` section B (record `ts-nnn-<slug>`); architecture, allocation and ADRs keep design A, B, H | finding-4 |
| §3.2 reviewer block | A Minor finding rides with APPROVED as a record lien with owner and due gate (01 §12.3); delta iterations verify Major fixes only; the record names the frozen blobs in `product_files`, and a record of blobs on an unmerged CR branch holds its verdict until the merge | finding-5 |
| §3.5 "Review record" paragraph | The slug follows the forms of 01 §13 | INSP-022 X-1 |
| §4 assignment block | The REVIEW RECORD line carries the frozen blobs as `path@blob` and the branch name (PDR work plan rule C2) | drift rule alignment |

INSP-022 finding-2 (checklists treated as due in §3.1 and §3.5) is fixed by CR-012 on the base of this branch; this CR completes the §1 template list and the process index row.

### 1.5 `docs/process/README.md` (INSP-022 finding-1, -2, -3 (b), -6; X-1)

The record slug sentence points to 01 §13; a "Tailoring markers" paragraph makes the RMM the authority for every T or NA row, and SWE-023 (03 row), SWE-157 and SWE-159 (07 row) are marked "(tailored)"; the row statuses read "Baselined at SRR"; the 00 and README rows cite charter commit `6ea6b1d`; the templates row lists all eleven checklists as existing; the tools row is restated at `7bb994f`.

### 1.6 `docs/process/se-compliance-matrix.json` and its render (INSP-024, `compliance-matrix.md`)

| Location | Change | Closes |
|---|---|---|
| `status`, `approval` | The matrix is Baselined at SRR; `submitted_by` is Robin as Program/Project Manager with Claude as preparer, `approved_by` is Robin as ETA and Decision Authority on 2026-09-26, and `approval_memo` cites memo section 7 (the tailoring rows moved from proposed to approved, 01 §9 additional completion item) | finding-5; work plan output "tailoring rows moved from proposed to approved" |
| `revision_date`, `field_notes.revision_date` | 2026-09-27, with the rule that the date is set in every content change | finding-6 |
| SE-11 | The SI-031 make element (owner hand assembly), ADR-007 and the hand-assembly list are added | finding-2 |
| SE-34 | The App. G tables are the ones 01 §4.3, 5.3, 6.3, 7.3 and 8.3 name | finding-3 |
| SE-35 | The stakeholder identification (the `stakeholders` array, 02 §3.0, T-21) is named beside the expectations | finding-7 |
| SE-57 | The five between-gate reviews of 01 §2.1, with 01 §2.1 in `implementation_ref` | finding-4 |
| SE-62, SE-63 | The TPMs run from SRR through SAR under the `margin_policy` of TPM-001 and TPM-002 | finding-1 (carried item C-133) |

No row's `comply` value, `relief_type` or `risk_evaluation` changes. `tools/render_compliance.py` regenerated the `.md`; `--check` exits 0 (62 rows, FC 49, T 4, NA 9).

### 1.7 `docs/templates/peer-review-checklist-requirements.md` (INSP-022 finding-5)

The completion criteria admit a Minor finding "recorded in the record's lien table as a lien with the owner of the fix and its due gate" (01 §12.3) beside "fixed" and "deferred with an owner decision reference"; `checklist_revision` becomes D. Nothing else in the checklist changes.

## 2. Reason

- RFA-SRR-006 (lien L-6, `docs/reviews/SRR/decision-memo.md` section 6): every SRR record lien is fixed in its product and verified by the owning reviewer before the PDR readiness declaration. INSP-019 (5 liens), INSP-020 (8), INSP-022 (6) and INSP-024 (7) are the four records of this work package (carried items C-114 to C-139).
- 01 §9, additional completion item: 01 is updated with the review's results, "After SRR this is done by `CR-NNN`".
- 01 §9, additional completion item: approved tailoring rows move from "proposed" to "approved" in `se-compliance-matrix.json` (the RMM did so at `9bdf33c`).
- After `baseline/srr`, Table 4-1 rows 2, 3 and 53 are CR-controlled, so these non-editorial changes need a CR (05 §5.1; commit trailer `CR: CR-NNN`, 05 §4.5). Workaround while the CR is open: none needed; the SRR text stays in force and the liens stay open.

## 3. Alternatives considered

| Alternative | Why rejected or deferred |
|---|---|
| Do nothing | RFA-SRR-006 would stay open at the PDR readiness declaration (01 §10.2: a Routine RFA closes before the next gate's readiness declaration) |
| Split into one CR per document (01 and 02 as PCR-2; 08, the index, the matrix and the templates each on their own) | Five section 6 reviews and five dispositions for one work package's Class II text changes; one CR with one frozen branch is reviewable in one pass and the owner dispositions it once at B2 |
| Base the branch on `main` instead of the CR-012 branch | 08 would then carry two branches editing sections 3.1 and 3.5, and the INSP-022 delta would verify a text that CR-012 then changes again; basing on CR-012 makes the merge order explicit |
| Fix INSP-020 finding-8 here as well | CR-011 already rewrites 02 §8.5 with the five codes; editing the same table here would conflict with CR-011 |
| Re-key the 02 §4.6 worked example to the real ids | The real L1 and SW-KEYER ids are being edited by CR-008 and the PDR TBR closure; a fictional-id statement keeps the example stable (INSP-020 finding-7 offers both fixes) |
| Make the MOP `requirement_ids` and `tc_ids` derived by the tool now | A tool change belongs to the tool owner's writer slot (PDR work plan §5.3, `tools/traceability.py` WP-PDR-06 only); this CR states the rule and routes the check |

## 4. Impact assessment (CM plan §5.3)

| Field | Assessment (numbers, IDs, paths) |
|---|---|
| Performance margins | None: no TPM, MOP or budget value changes; the SE-62 and SE-63 justifications quote the existing TPM-001 and TPM-002 `margin_policy` text |
| Safety | None: no hazard, control or 07 §14.1 component changes. Hazard analysis re-issue: no. RF exposure evaluation change: no |
| Risk | None: no RSK added, closed or re-scored |
| Software classification and tailoring | Compliance matrix: text of the FC rows SE-11, SE-34, SE-35, SE-57, SE-62 and SE-63 and the `status`, `approval` and `revision_date` fields; no `comply`, `relief_type` or `risk_evaluation` changes; the approval block records the SRR tailoring approval already given (memo section 7). RMM and 03: None. 02 §2.3 and §13 and the process index now mirror the existing RMM T dispositions of SWE-023, SWE-027, SWE-157, SWE-159 and SWE-211 (SWE-121) |
| Interfaces | None: no ICD |
| Operations and ConOps | None: no OPS scenario, operator procedure or handbook |
| Cybersecurity | None: neither the USB firmware-load path nor the key-input command path. AL-02-22 routes a `CON-` for the cybersecurity scope to the L0 writer; that change is not made here |
| Verification | None: no TC added, modified or invalidated. The review-process text (01 §12.3, §13; 08 §3.2, §4) states rules the SRR records already followed |
| Cost | None |
| Schedule | None on the critical path: disposition at B2 Fri 10-02 (OD-37), so 01 and 02 freeze at F1 on a known basis. If late, 01 and 02 freeze on their current text and this CR is carried after PDR (register "If late"); the liens then stay open as RFA-SRR-006 items |
| Requirements and traceability | None: no REQ, TC, NGO, MOE or CON changes; volatility contribution 0. `tools/traceability.py --report-only` on the branch: 245 requirements, 173 test cases, 0 violations, 2 warnings (`SYS_UNALLOCATED` REQ-SYS-125, REQ-SYS-148), the same as on `main`; the two report files were restored with `git checkout` |
| Regulatory | None: no 47 CFR clause |
| Documentation | Changed by this CR: the eight paths of the front matter. Changed outside it: `docs/requirements/README.md` (Log, `11b1b1d`). Requests to other writers (PDR work plan §5.3), not changed here: 07 §4 item 2 (AL-02-20) and 07 §10.1 row b (INSP-022 X-3, trade studies to the risk checklist section B) to the 07 writer (WP-PDR-13 slot); the dedicated cybersecurity `CON-` (AL-02-22) to the L0 writer (WP-PDR-10, then WP-PDR-02); MOP `requirement_ids` and `tc_ids` and the MOE-013 MOP (INSP-020 X-2) to the `tpm.json` writer (WP-PDR-29); the T-16 MOP agreement check to the tool owner (WP-PDR-06); the SEMP review schedule (01 §9) to the SEMP writer (WP-PDR-13, WP-PDR-46); charter §3 sentence on the App. G tables (INSP-024 X-2) to the charter edit list (OD-31, drafted by WP-PDR-13) |
| Released units | None: no unit exists |

Checklist change rule of Table 4-1 row 53 ("its CR lists every `INSP-NNN` record to re-run, or to keep with a rationale") for `peer-review-checklist-requirements.md` revision D: every record filed against revision C or earlier is kept without re-run. Rationale: revision D changes only the completion criteria, to state the convergence rule (lead SE direction of 2026-09-26) under which every SRR and PDR record that used this checklist already carried its Minor findings as liens; no item, section or measurement changes. `docs/templates/decision-memo.md` is a template, not a checklist, and invalidates no record.

Classification rationale: Class II. The change corrects and completes process documentation, a template and the text of fully compliant matrix rows, without impact to form, fit, function, interchangeability, interfaces, safety, verification evidence or operator procedures (05 §2, Class II definition). No requirement, ICD, hazard or test case is affected, so 05 §3 does not require the independent impact review; PDR work plan rule C6 requires it for every CR raised in the phase.

## 5. Implementation plan

| Step | Artifact and path | Responsible | Done (SHA) |
|---|---|---|---|
| 1 | Product change on `cr/CR-015-process-liens-01-02-08` (the eight paths of the front matter), branch base `7784672` | Claude, WP-PDR-12 author | `7efd900` |
| 2 | This CR file on `main`, state Submitted | Claude, WP-PDR-12 author | the commit that adds this file (`Refs: CR-015`) |
| 3 | Delta iterations of the four SRR records against the frozen blobs of the table above: INSP-019 (`docs/reviews/SRR/checklists/process-01-lifecycle-and-reviews.md`), INSP-020 (`process-02-requirements-and-traceability.md`; finding-8 on the CR-011 blob), INSP-022 (`process-08-agent-briefing.md`), INSP-024 (`compliance-matrix.md`). Each verifies every lien finding of its record and names the new blobs in `product_files`. Under the lead SE convention of 2026-09-27 each record is committed on `main` with `reviewer_verdict` set and its record `verdict` held until the merge | Independent reviewers (new invocations of each record's reviewer role, plan rule C4) | |
| 4 | Section 6 impact review | Independent reviewer that did not author this CR (register slot Thu 10-01) | |
| 5 | Owner disposition (section 7), OD-37 at B2 Fri 10-02 | Owner | |
| 6 | Merge after CR-012 is merged: rebase or merge `main` into the branch if `main` changed the eight paths, re-run the checks of section 9, then `git merge --no-ff cr/CR-015-process-liens-01-02-08` with message `merge(CR-015): <title>`; any Major fix from step 3 or 4 lands on the branch first with `CR: CR-015`, followed by a delta of the affected record. The record verdicts of step 3 are set in the merge commit or the commit right after it. If CR-012 is rejected or its branch head moves, this branch is rebased on the resulting 08 and re-frozen, and the INSP-022 delta repeats | Claude (CM function), with the owner's merge approval | |
| 7 | Section 9 verification | Independent reviewer | |

Verification of the implementation (what the independent reviewer will check): `git diff <CR-012 merge> <CR-015 merge>` touches exactly the eight paths; the blobs on `main` equal the blobs the step 3 records verified; `tools/validate_docs.py` shows no failure that names a CR-015 path or a record of step 3; `tools/render_compliance.py --check` exits 0; the unit tests show no new failure; `tools/traceability.py --report-only` shows no new violation.

## 6. Independent review of the impact assessment

Not required by 05 §3 for this Class II change (no requirement, ICD, hazard or test case is affected). Required by PDR work plan rule C6 before the owner's disposition: not yet performed. The reviewer must not have authored this CR or the branch change.

| Item | Reviewer (agent invocation) | Date | Finding | Resolution |
|---|---|---|---|---|
| | | | | |

Reviewer concurrence: pending.

### 6.1 Impact review round 1: independent reviewer (2026-09-27)

Source: record INSP-060, `docs/reviews/PDR/checklists/cr-015-process-01-02-08.md`, section "Section 6 impact review of CR-015" (committed at `b133a4b`; reviewer `reviewer:WP-PDR-12-iteration-1`, which authored no part of this CR, the branch or the README commit; `reviewer_verdict: APPROVED`, 0 Major, 3 Minor; record `verdict` held at NEEDS CHANGES until the merge under the lead SE convention of 2026-09-27). The table and the "pending" line above are the template placeholders and are left as written; this round is the first review entry. It is entered here by a separate invocation (lead SE transcription, INSP-060 cross item X-5) that authored no part of this CR, its branch or INSP-060, and which re-checked effectivity at entry (last paragraph). Configuration reviewed by INSP-060: this file at blob `8a77b0ab` on `main` at `9009412`; branch `cr/CR-015-process-liens-01-02-08` at `7efd900` (base `7784672`, the CR-012 head); `docs/requirements/README.md` on `main` at `11b1b1d`.

| Item | Reviewer (agent invocation) | Date | Finding | Resolution |
|---|---|---|---|---|
| Class (05 §2) | INSP-060 reviewer | 2026-09-27 | Concur, Class II. Field diff of the matrix by script: only `status`, `revision_date`, `field_notes.revision_date`, `approval` and the justification or `implementation_ref` of SE-11, 34, 35, 57, 62, 63 change; no `comply`, `relief_type` or `risk_evaluation` value; no requirement, ICD, hazard or test case | No action |
| Performance margins; Safety; Risk; Interfaces; Operations and ConOps; Cybersecurity; Cost; Regulatory; Released units | INSP-060 reviewer | 2026-09-27 | Concur None for each | No action |
| Software classification and tailoring | INSP-060 reviewer | 2026-09-27 | Concur: matrix text and approval block only; RMM and 03 unchanged. The 02 §2.3 mirror of SWE-027 misstates the RMM substitute (INSP-060 finding-2, Minor) | Author: reword per INSP-060 finding-2 on the branch before the disposition, or carry as a record lien (rule C1) |
| Verification | INSP-060 reviewer | 2026-09-27 | Concur None: no case added, changed or invalidated; checklist revision D changes only the completion criteria, and keeping every revision C record with a rationale meets the Table 4-1 row 53 rule | No action |
| Schedule (INSP-060 finding-3, Minor) | INSP-060 reviewer | 2026-09-27 | Partly concur: the CR-012 dependency is stated; the CR-011 and CR-016 dependencies (both change 02) are missing, and §5 step 6 and the verification criterion "blobs on `main` equal the blobs the step 3 records verified" cannot hold if either merges first | Author: name CR-011 and CR-016 in §4 Schedule with the merge order; state in step 6 that a merge of `main` that re-blobs a verified file is followed by a delta of INSP-060; restate the criterion as "equal the blobs of the latest delta iteration" |
| Review-process text (INSP-060 finding-1, Minor) | INSP-060 reviewer | 2026-09-27 | 01 §12.3 items 1 to 3 and the 08 §3.2 sentence "one gate later" do not fix one due event for a record lien | Author: one due rule in 01 §12.3 item 2, 08 §3.2 and the checklist revision D criteria, per INSP-060 finding-1 |
| Requirements and traceability | INSP-060 reviewer | 2026-09-27 | Concur None; re-run at `7efd900`: `traceability.py --report-only` 0 violations, 2 warnings | No action |
| Documentation | INSP-060 reviewer | 2026-09-27 | Concur: the eight paths and the named requests to other writers. Two routed 07 changes (07 §10.1 row b; AL-02-20, 07 §4 item 2) are not in the CR-013 prototype at `41c588c` (INSP-060 X-1) | Lead SE: add both to the WP-PDR-13 revision of CR-013 or to WP-PDR-47, before WP-PDR-35 |
| Section 9 author evidence | INSP-060 reviewer | 2026-09-27 | Re-run, all Yes: scope 8 files; `validate_docs.py` failures are drift only; unit tests 453 run, 1 failure (`test_repository_exit_zero`), 14 skipped; `render_compliance.py --check` exit 0 (62 rows, FC 49, T 4, NA 9); `git merge-tree` with `main` and CR-008 to CR-011, CR-013, CR-014, CR-016 clean | No action |
| Effectivity at entry (IR-F4, Minor) | Lead SE transcription invocation | 2026-09-27 | The 08 §1 tools line at blob `374fd777` reads "`ltspice-batch.sh` (ADR-018 wrapper; TV-014 not accredited, so LTspice runs wait for the owner's accreditation)". The owner accredited ACC-LTSPICE-001 (OD-24b) for wrapper blob `88b71475` at `bb09ad2`, and TV-014 section 9 records it at `1db319a`. At the merge this sentence is stale | Author: restate the LTspice entry of 08 §1 (and check the `docs/process/README.md` tools row) on the branch before the disposition, with a delta of INSP-060; or carry as a record lien |
| Effectivity at entry (IR-F5, Minor) | Lead SE transcription invocation | 2026-09-27 | New 01 §16 fixes the PDR planning targets of OD-01 (readiness Tue 2026-10-06, PDR about Thu 2026-10-08, `baseline/pdr` about Fri 2026-10-09), and §4 Schedule relies on B2 Fri 10-02. Status note 2026-09-27 §11 ("Plan usage") says the PDR date is re-planned after the TS-012 decision. The text is marked as planning targets under the event-based rule of 01 §1 item 2, so no gate rule is wrong, but the dates can go stale before the merge | Author: at the step 6 re-check, align 01 §16 and §4 Schedule with the re-planned dates if the TS-012 re-plan moves them, with a delta of INSP-060 |

Effectivity re-check at entry (lead SE transcription invocation, 2026-09-27, `main` at `d5a3058`): this file is still blob `8a77b0ab`; `cr/CR-015-process-liens-01-02-08` is still `7efd900` and `cr/CR-012-pdr-checklist-templates` still `7784672`; `main` has not changed any of the eight paths since `11b1b1d` (`git diff --stat 11b1b1d HEAD` on them is empty); `git merge-tree --write-tree` of `7efd900` with `main`, CR-011, CR-013 and CR-016 is clean; `git diff --stat 7784672 7efd900` is still exactly the eight paths (136 insertions, 84 deletions). The search for missed items ran `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` first, then `grep -n` on the branch blobs and the status note to pin lines; it found IR-F4 and IR-F5 and nothing that changes the class or adds a requirement, ICD, hazard or test case impact.

Reviewer concurrence (round 1): concur with Class II and with the change (INSP-060). No Major finding. Five Minor findings (INSP-060 finding-1 to finding-3; IR-F4, IR-F5) may be fixed on the branch before the disposition, with a delta iteration of INSP-060, or carried as record liens under rule C1. The owner may disposition CR-015 on this review.

## 7. CCB disposition (owner)

| Field | Value |
|---|---|
| Decision | Approved |
| Class confirmed | II (proposed II; concurred by INSP-060, section 6) |
| Date | 2026-09-28 |
| Conditions | None stated by the owner. The merge follows section 5 steps 6 and 7, after CR-012 merges (Q4) |
| Rationale | Fixes the 26 SRR record liens of INSP-019, INSP-020, INSP-022 and INSP-024. Section 6 (INSP-060): no Major; INSP-060 finding-1 to finding-3, IR-F4 and IR-F5 Minor and open |
| Waiver scope (if Approved (waiver)) | n/a |
| Re-look trigger and re-look-by review (if Deferred) | |
| Source | Chat transcription by Claude (configuration manager) on 2026-09-28. The presenter asked the owner to approve CR-007 to CR-016, the SRR lien fixes that passed their impact reviews (recommendation: approve all ten). Owner statement, verbatim: "Um, and then, yeah, I think you're uh, good to continue." The lead SE reads it as approval of item 1 as recommended, with the branches to merge after the section 9 checks (`docs/plan/status/status-2026-09-28.md` section 1, commit `e288add`, which transcribes the full statement); the owner is asked to correct any line |

Disposition history (append only):

| Date | Decision | New target | Source |
|---|---|---|---|
| 2026-09-28 | Approved | none | owner, `status-2026-09-28.md` section 1 (`e288add`), transcribed by Claude (configuration manager) |

## 8. Implementation record

| Commit | Files | Trailer check (`CR: CR-015` present) |
|---|---|---|
| `7efd900` (branch `cr/CR-015-process-liens-01-02-08`, prototype) | the eight paths of the front matter | yes |

Traceability report after implementation: not affected (no requirement, test case or hazard file changes); renders regenerated: `docs/process/se-compliance-matrix.md` (text render, no image).

## 9. Verification of implementation

| Impact item | Planned closure (from §4/§5) | Evidence (report path, TC id, analysis file) | Result |
|---|---|---|---|
| Scope | Diff touches exactly the eight paths | `git diff --stat 7784672 7efd900`: 8 files, 136 insertions, 84 deletions (author run, 2026-09-27) | Pending independent verification |
| Tools unaffected | `tools/validate_docs.py` and the unit tests show no new failure against the base | Author run in a worktree of the branch, with and without the change (`git stash`): `validate_docs.py` fails the same 3 SRR records either way, all by the record drift rule: `risk-register-06.md` and `tool-validation-tv-001-to-tv-010.md` (products changed by wave 0 commits) and `process-08-agent-briefing.md` (INSP-022, whose 08 blob the CR-012 base already changes); unit tests 453 run, 1 failure either way (`RepositoryTests.test_repository_exit_zero`, the same drift), 14 skipped. Once the branch carries this change, INSP-019, INSP-020, INSP-022 and INSP-024 name the `baseline/srr` blobs and fail the drift rule on the branch until their step 3 deltas. On `main`, INSP-020 fails the drift rule from `11b1b1d` (the Log-class `docs/requirements/README.md` fix) until its step 3 delta names the new README blob | Pending independent verification |
| Matrix render | `render_compliance.py --check` exit 0 | Author run at `7efd900`: "validation PASSED and rendered file is current"; rows 62, FC 49, T 4, NA 9 | Pending independent verification |
| Merge feasibility | No conflict with `main` or the open CR branches | `git merge-tree --write-tree` of the branch with `main` (`11b1b1d`) and with `cr/CR-008-*`, `cr/CR-009-*`, `cr/CR-010-*`, `cr/CR-011-*`, `cr/CR-013-*`, `cr/CR-014-*`: no conflict (author run, 2026-09-27) | Pending independent verification |

Independent verifier (agent invocation): pending.

Configuration manager pre-merge check (2026-09-28; performed at the disposition, not the independent verification, which stays pending). Method: `git merge-tree --write-tree` of the branch head with `main` (no conflict), then a trial `git merge --no-ff` in a detached scratch worktree of `main` (discarded afterwards, no ref kept), `tools/validate_docs.py` and `tools/traceability.py --report-only` on the trial merge, and the failure set compared with the baseline. Baseline on `main` at `e288add`: `tools/validate_docs.py` 102 passed, 8 failed (all record drift already on `main`: SRR `adrs-001-to-025.md`, `process-02-requirements-and-traceability.md`, `tool-validation-tv-001-to-tv-010.md`, `trade-studies-ts-001-ts-002.md`, `trade-study-ts-002-software-assurance.md`; PDR `cm-plan-05-software-assurance.md`, `configuration-status.md`, `lessons-learned.md`); `python -m unittest discover -s tools/tests` 596 run, 1 failure (`test_repository_exit_zero`, the same drift), 14 skipped; `tools/traceability.py --report-only` 0 violations, 2 warnings. Branch head `7efd900`, stacked on the CR-012 head `7784672`. Scope: `git diff --stat 7784672 7efd900` 8 files, 136 insertions, 84 deletions (section 9 row 1 reproduced). Trial merge of CR-012 then CR-015: `validate_docs.py` 99 passed, 11 failed; three new failures, the SRR records `process-01-lifecycle-and-reviews.md` (INSP-019), `process-08-agent-briefing.md` (INSP-022) and `compliance-matrix.md` (INSP-024), which still name the `baseline/srr` blobs (INSP-020 already fails on `main`). INSP-060 carries their deltas but does not change their `product_files`, and it pins this file at `8a77b0ab`, which this disposition commit changes, so its verdict cannot be set APPROVED without a re-pin by its reviewer. `traceability.py --report-only`: 0 violations, 2 warnings. Merge held: CR-012 not merged; the four SRR records not re-issued.

## 10. Closure

| Field | Value |
|---|---|
| Owner merge approval | 2026-09-28, with the disposition: "their branches merge after the section 9 checks" (lead SE reading, `docs/plan/status/status-2026-09-28.md` section 1). Merge held at the disposition: see the section 9 configuration manager pre-merge check |
| Merge commit | |
| Waiver entered in CSA item 12 and affected VDDs | n/a |
| CSA regenerated | |
| Date closed | |

## 11. History

| Date | State | By | Commit on main | Note |
|---|---|---|---|---|
| 2026-09-27 | Submitted | Claude (WP-PDR-12 author) | the commit that adds this file | Created with the impact assessment complete; product change prototyped on `cr/CR-015-process-liens-01-02-08` at `7efd900` (base `7784672`, the CR-012 head); the step 3 record deltas and the section 6 review (rule C6) pending |
| 2026-09-27 | Submitted | Claude (lead SE transcription) | the commit that records this row | Section 6 round 1 entered from INSP-060 (`b133a4b`): concur Class II, 0 Major, 3 Minor; two Minor effectivity items added at entry (IR-F4 LTspice accreditation text in 08 §1, IR-F5 PDR dates after the TS-012 re-plan); the step 3 deltas are INSP-060; disposition pending (OD-37) |
| 2026-09-28 | Dispositioned (Approved) | Claude (configuration manager), transcribing the owner | the commit that records this row (`Refs: CR-015`) | Owner approval of CR-007 to CR-016 as recommended (`status-2026-09-28.md` section 1); merge held at the disposition: after CR-012; SRR records INSP-019, INSP-022, INSP-024 drift (re-issues not done) (section 9 pre-merge check) |

## 12. Questions for the owner (answer with the disposition)

| # | Question | Recommendation |
|---|---|---|
| Q1 | Approve CR-015, which fixes the 26 SRR record liens of 01, 02, 08, the process index and the compliance matrix and records the SRR results and the PDR dates you approved in 01 section 16? | Approve, after the section 6 review and the four record deltas report no Major finding |
| Q2 | Confirm Class II | Confirm: process text, two templates and the text of fully compliant matrix rows; no requirement, ICD, hazard or test case |
| Q3 | Confirm the compliance-matrix approval block: submitted by you as Program/Project Manager (Claude as preparer), approved by you as Engineering Technical Authority on 2026-09-26 with the SRR memo section 7 | Confirm: it records the approval the SRR memo already holds, in the Table H-1 roles |
| Q4 | Accept the merge order: CR-015 merges with or after CR-012 | Accept: both change 08, and the INSP-022 delta then verifies the final 08 once |

Answers recorded with the disposition (2026-09-28; the lead SE reading of the owner's approval "as recommended", the owner is asked to correct any answer): Q1 approved. Q2 Class II confirmed. Q3 confirmed: the compliance-matrix approval block as proposed. Q4 accepted: CR-015 merges with or after CR-012.
