---
id: CR-012
title: Add the analysis, software assurance and tool validation checklists; update 08 sections 3.1 and 3.5
status: Submitted
class: II
originator: Claude
date_opened: 2026-09-27
phase: B
configuration_at_origination: baseline/srr (tag on 779f93f); change set prepared on branch base 573f9f5 (main); branch head 7784672 (ac9b7a5 plus the iteration 1 Major fixes)
baseline_affected: baseline/srr
affected_cis: [2, 53]
affected_paths: [docs/templates/peer-review-checklist-analysis.md, docs/templates/peer-review-checklist-software-assurance.md, docs/templates/peer-review-checklist-tool-validation.md, docs/process/08-agent-briefing.md]
affected_ids: []
related: [INSP-015, INSP-017, INSP-018, INSP-022, INSP-026, INSP-027, INSP-030, RFA-SRR-006, CR-007, CR-010]
target_release: none
branch: cr/CR-012-pdr-checklist-templates
disposition: null
disposition_date: null
relook_trigger: null
relook_by: null
merge_sha: null
date_closed: null
---

# CR-012: Add the analysis, software assurance and tool validation checklists; update 08 sections 3.1 and 3.5

Template: `docs/templates/change-request.md`. Process: `docs/process/05-configuration-and-data-management.md` §5.1 to §5.3. File location: this file, committed on `main` with `Refs: CR-012`. Status: **Submitted**. Work package: WP-PDR-03 of `docs/plan/pdr-work-plan.md` (revision 2), wave 0, "Missing checklist templates". CR-007 to CR-011 were claimed by parallel wave 0 work packages (files on `main` or branches `cr/CR-008-*` and `cr/CR-011-*`), so this CR takes CR-012.

**Where the change is.** The full product change is prepared on the branch `cr/CR-012-pdr-checklist-templates`, head `7784672` on base `573f9f5` (`ac9b7a5`, then `7784672` with the Major fixes of the template reviews INSP-032 and INSP-033, iteration 1), as the Submitted state of 05 §5.2 allows ("Branch `cr/CR-NNN-<slug>` may be opened for prototyping; nothing merges"). The exact before and after text is `git diff 573f9f5 7784672`. Nothing is merged to `main` before the owner's disposition and the section 9 verification. The blobs at `ac9b7a5` were frozen for iteration 1 of the WP-PDR-03 template reviews; the blobs at `7784672` are frozen for their iteration 2 delta (PDR work plan rule C2).

| File (Table 4-1 row) | Blob at `baseline/srr` and on `main` | Blob on the branch at `ac9b7a5` (iteration 1) | Blob on the branch at `7784672` (iteration 2) |
|---|---|---|---|
| `docs/templates/peer-review-checklist-analysis.md` (row 53) | none (new file) | `0386cc6e78da65578b1cce8b2f793cd3db224921` | unchanged |
| `docs/templates/peer-review-checklist-software-assurance.md` (row 53) | none (new file) | `22b7b6afd241d7bd2deddfe45d9318cab5f0243b` | `5b13528504868b2add0f0b1e329c63aa2b54cdf4` |
| `docs/templates/peer-review-checklist-tool-validation.md` (row 53) | none (new file) | `c94fa383a952cde434da7f63eb00ae5d699996d6` | `7be809d4ceb9a202473eb19da3627fe0cd427900` |
| `docs/process/08-agent-briefing.md` (row 2) | `01a36bac8d5f133dadd5b384f92f95f225371663` | `56c540113110b0d8916219d3cb531d6a76587713` | unchanged |

## 1. Description of the change

### 1.1 Three new checklist templates (Table 4-1 row 53)

| File | Content |
|---|---|
| `peer-review-checklist-analysis.md` | Record `docs/reviews/<REVIEW>/checklists/analysis-<product-stem>.md`. Product types (`analysis_kind`): simulation decks and checkers, budgets, thermal, RF exposure, cascades, timing, worst-case. Sections: readiness R1 to R6; A question and traceable inputs; B model validity (SWEHB `swe-070` section 3); C tools, TV status and reproducibility (SWE-070, SWE-136, 05 §9); D units and arithmetic; E results, margins, proposed TBR values and TPM estimates, credit rules of 04 §5; F every case named (PDR work plan rule C7); G1 to G7 kind-specific items; H hazards, risks, records; I visual closure; J assurance items for analyses of 07 §14.1 components. Per-case table, findings table, completion criteria, verdict format |
| `peer-review-checklist-software-assurance.md` | Paired assurance record `docs/reviews/<REVIEW>/checklists/<product-slug>-software-assurance.md` (07 §10.2). Section B is the SWE-to-task table per 07 §2.1.1 product type (requirements, plans, trade studies and ADRs, design, code, test, NCR, MC/DC and unsafe audit), with the SWEHB section 7.1 tasks to apply and the safety-critical designations of SWEHB topic 8.10 §6, plus a row "Every product type" (swe-134 task 5, swe-022 task 1) and the rule that the tasks of any other SWE the product implements are also applied (07 §15); every SC task of 8.10 §6 is in a row except those of swe-015, swe-151, swe-016 and swe-174, whose products 07 §2.1.1 does not route (stated in the template); sections A dispatch and independence, C SWE-134 items a to l against 07 §14.2, D software safety analysis and hazard traceability (SWE-205, SWE-052, SWE-184, SWE-192), E peer review and CM assurance, F assurance risks and metrics. Reliefs are cited from `rmm.json` (SWE-022 and SWE-023, T) and never assumed |
| `peer-review-checklist-tool-validation.md` | Record `docs/reviews/<REVIEW>/checklists/tool-validation-tv-nnn-<tool>.md`. Sections: readiness R1 to R5; A identification; B purposes; C known-answer test (every clause of the 05 §9.2 table row); D results and reproducibility; E limitations and re-validation triggers; F accreditation readiness and indexes; G1 to G4 kind-specific items (repository tools, external tools, emulator, instrument firmware); H SWEHB `swe-136` and `swe-070` section 7.1 tasks. The reviewer edits no TV record: the TV record author writes section 8 after the record is filed, and a delta re-issue re-pins `product_files`. `product_files` lists fixture files one by one (the record drift rule of `tools/validate_docs.py` reads blobs only), and the new field `fixture_trees` carries each fixture directory's tree hash. INSP-015 items TV-S1 to TV-S10 are carried item by item (column "Carries"), and INSP-015 findings F-01, F-02, F-04 and F-05 are made explicit checks |

Each template carries the front matter of 01 §13 (the `tools/validate_docs.py` record schema); a filled copy of each passes `tools/validate_docs.py` (section 9).

### 1.2 `docs/process/08-agent-briefing.md` (Table 4-1 row 2)

| Location | Before | After |
|---|---|---|
| §3.1 author row "simulation decks and checkers" | Names the analysis checklist with "(Claude writes it before the first deck is reviewed, section 3.5; no deck is reviewed without it)" | Row "analyses and simulation decks" for decks, budgets, thermal, RF exposure, cascade and timing analyses; governing 04 sections 3 to 5 and role block 3.4; checklist `peer-review-checklist-analysis.md`, record `analysis-<product-stem>` |
| §3.1 new author row | none | "tool validation records (TV-NNN)": 05 sections 9 and 13, the TV README, the lock; checklist `peer-review-checklist-tool-validation.md`; the repository tool's source also reviewed with the code checklist (03 section 6.1.1) |
| §3.1 rows "review slide decks", "risks", "hazards" | Each says "Claude writes it before the SRR package" | The clause is removed; the checklists exist (INSP-022 finding-2, carried item C-128) |
| §3.5 rows `analysis` and `software-assurance` | "Claude writes before PDR ..." | Scope, basis and "Exists (written 2026-09-27, WP-PDR-03)" |
| §3.5 rows `visual-product` and `safety` | "Claude writes before the SRR package ..." | "Exists (written before the SRR package, committed 2026-09-26)" (C-128) |
| §3.5 new row `tool-validation` | none | Scope, basis (05 §9.1, §9.2, §13; SWE-136, SWE-070; SRR decision 117) and "Exists (written 2026-09-27, WP-PDR-03)" |
| §3.5 paragraph after the table | "The four due items above ... are the only missing checklists"; the SRR deck and hazard analysis checklists "which Claude writes before the SRR package" | Every product type named in the section has a checklist, and none is due; the PDR uses of the three new checklists; the hyphenated stem `tool-validation` added to the valid stems |

No other part of 08 changes. The §1 repository map line that lists the templates, the §3.2 reviewer block and the header are WP-PDR-12 scope (PDR work plan section 3.4) and are left for it.

## 2. Reason

- 08 §3.5 (baselined at SRR): "A review that needs a checklist that does not yet exist is not held." The analysis and software assurance checklists were scheduled "before PDR" there; every analysis, SA and TV review of the PDR phase is blocked until they exist (PDR work plan WP-PDR-03, "Blocks: every analysis, SA and TV review").
- SRR decision 117 (adopted with the consent agenda, `docs/reviews/SRR/decision-memo.md` section 8.0.1): "Claude writes `docs/templates/peer-review-checklist-tool-validation.md` before the PDR TV set."
- 07 §15 row "5.17 item 13" (baselined): closure is the SA checklist's SWE-to-task table, due PDR (INSP-018 finding-6).
- INSP-022 finding-2 (lien, RFA-SRR-006; carried item C-128): 08 treats the safety, visual-product and risk checklists as due although they exist.
- After `baseline/srr`, Table 4-1 rows 2 and 53 are CR-controlled (CR from SRR), so these non-editorial changes need a CR (05 §5.1; commit trailer `CR: CR-NNN`, 05 §4.5). Workaround while the CR is open: none that allows the blocked reviews; the reviewer of each template reads it from the branch at the frozen blob.

## 3. Alternatives considered

| Alternative | Why rejected or deferred |
|---|---|
| Do nothing | Every analysis, SA and TV review of waves 1 and 2 is blocked by 08 §3.5; SRR decision 117 and the 07 §15 closure are not met |
| Keep reviewing analyses and TV records with the code or requirements checklist plus ad hoc items (the SRR practice of INSP-015 and INSP-018) | 08 §3.5 has no "by reading" substitute; SRR decision 117 accepted that practice for SRR only |
| Merge the templates to `main` without a CR, as implementations the baseline already schedules | Rows 2 and 53 are CR-controlled from SRR; a non-editorial commit without an approved CR would be an unreviewed class-CR merge (05 §3 software assurance row) |
| Fold these changes into CR-007 (05 rows) or the WP-PDR-12 CR for 01 and 02 (PCR-2) | Different writers and dispositions; CR-007 is dispositioned at B1a and PCR-2 at B2, both later than the B0 barrier at which the PDR work plan needs these templates APPROVED |

## 4. Impact assessment (CM plan §5.3)

| Field | Assessment (numbers, IDs, paths) |
|---|---|
| Performance margins | None: no TPM, MOP or budget changes |
| Safety | None: no hazard, control or 07 §14.1 component changes; the SA checklist applies the existing 07 §2.1.1 dispatch rule and 07 §14 provisions without widening or narrowing them. Hazard analysis re-issue: no. RF exposure evaluation change: no |
| Risk | None: no RSK added, closed or re-scored |
| Software classification and tailoring | None: no `rmm.json`, 03 or compliance-matrix row changes. The SA checklist cites the existing T dispositions of SWE-022 and SWE-023 |
| Interfaces | None: no ICD |
| Operations and ConOps | None: no OPS scenario, operator procedure or handbook |
| Cybersecurity | None: neither the USB firmware-load path nor the key-input command path |
| Verification | No TC added, modified or invalidated. Review records: the templates govern the review records filed after the merge **and the records already filed against revision A** on the branch (section 4.1, listed at `main` `d5a3058`, 2026-09-27). Tool validation template `7be809d4`: INSP-038, INSP-040, INSP-041, INSP-043, INSP-088. Software assurance template `5b135285`: INSP-046 to INSP-051, INSP-062, INSP-066, INSP-070, INSP-073 to INSP-075, INSP-087, INSP-101 to INSP-106. Analysis template `0386cc6e`: INSP-056, INSP-071, INSP-072, INSP-083, INSP-084; `docs/design/analysis/frequency-budget.md` line 10 names the analysis template (on the branch) for INSP-056. Their evidence stands on revision A; the disposition decides whether revision A reaches `main` unchanged (section 4.1 rule) |
| Cost | None |
| Schedule | Positive: unblocks the analysis, SA and TV reviews of waves 1a to 2b. Needs the owner's disposition at B0 (Mon 09-28) so the templates are on `main` before wave 1a (Tue 09-29). The records of section 4.1 hold their record verdict at NEEDS CHANGES until the merge (lead SE convention of 2026-09-27), except INSP-047 and INSP-088, already APPROVED. Decisions that rest on them move with the disposition: the TV accreditations of the PDR TV set (INSP-038 for TV-014, on which ACC-LTSPICE-001 rests, status note 2026-09-27 section 13; INSP-040 for TV-020 to TV-023; INSP-041 for TV-013; INSP-043 for TV-002; INSP-088 for TV-015 to TV-019), the SA closures of the wave 0 and wave 1 products (INSP-046 to INSP-051, INSP-062, INSP-066, INSP-070, INSP-073 to INSP-075, INSP-087, INSP-101 to INSP-106) and the analysis records feeding B1a and B2 (INSP-056, INSP-071, INSP-072, INSP-083, INSP-084) (PDR work plan section 5.2). Approved as submitted: no schedule effect beyond the section 5 step 8 re-issue. A condition that changes a template blob: one delta iteration or kept-with-rationale entry per affected record before its gate (section 4.1). Rejected or Deferred: every section 4.1 record stays held and the dependent accreditation and gate decisions are re-looked at B0 |
| Requirements and traceability | None: no REQ changes; volatility contribution 0 |
| Regulatory | None: no Part 97, 1, 2 or 15 clause |
| Documentation | The four files of the table above. Follow-on documentation outside this CR (named for their writers, PDR work plan section 5.3): 07 §15 row "5.17 item 13" and the section 15 lead paragraph ("until it exists") and 07 Annex A, which lists four checklists (07 writer order); 01 §13 slug list (`analysis-`, `tool-validation-`), WP-PDR-12; 08 §1 repository map and §3.2 reviewer block, and `docs/process/README.md`, WP-PDR-12; `docs/cm/tool-validation/README.md` owner action 1 ("No checklist template for TV records exists"), the tool owner of WP-PDR-07 |
| Released units | None: no unit exists |

Checklist change rule of Table 4-1 row 53 ("its CR lists every `INSP-NNN` record to re-run, or to keep with a rationale"): the three templates are new on `main`, but records have already been made against their Submitted revision A on the branch (blobs `7be809d4`, `5b135285` and `0386cc6e` at `7784672`). Those records are listed in section 4.1 with the rule that applies to them at each disposition. The rule does not re-run them if revision A merges unchanged; section 5 step 8 re-issues only their `checklist` field. Also kept without re-run: INSP-015 (TV-001 to TV-010, reviewed with the code checklist plus items TV-S1 to TV-S10 under SRR decision 117) and INSP-017, INSP-018, INSP-026, INSP-027 and INSP-030 (assurance reviews that applied the SWEHB section 7.1 tasks directly, as 07 §15 directed while the SA checklist did not exist). Rationale: each was made under the rule in force at SRR, which decision 117 and 07 §15 accepted; their delta iterations at PDR may apply the new checklists at the owning reviewer's choice. INSP-022 (08) is affected: its finding-2 lien is addressed by this change and is verified at INSP-022's next delta iteration (WP-PDR-12).

Classification rationale: Class II. The change modifies process documentation (a process document and review checklists) without impact to form, fit, function, interchangeability, interfaces, safety, verification evidence or operator procedures (05 §2, Class II definition). No requirement, ICD, hazard or test case is affected, so 05 §3 does not require the independent impact review for this class; PDR work plan rule C6 requires it for every CR raised in the phase (section 6).

### 4.1 Review records made against revision A (Table 4-1 row 53; impact review IR-F1)

Records filed on `main` that apply a Submitted template blob of this CR, as their front matter and header comment name it. Listed at `main` `d5a3058` (2026-09-27) with `git grep -l -e 0386cc6e -e 5b135285 -e 7be809d4 -- 'docs/reviews/*/checklists/*.md'`, keeping the records that apply the blob (the template reviews INSP-031 to INSP-033 review it and are step 3; INSP-081 names the blob only for its pair INSP-087). Claude re-runs the listing and adds to this table every record filed before the disposition (section 5 step 5). "Applied-template field" is where the record names revision A; "Record verdict" is the front matter `verdict` at `d5a3058` (held at NEEDS CHANGES until the merge under the lead SE convention of 2026-09-27, unless it reads APPROVED).

| Template (blob at `7784672`) | Record | Product reviewed | `checklist` field today | Applied-template field | Record verdict |
|---|---|---|---|---|---|
| Tool validation `7be809d4` | INSP-038 `tool-validation-tv-014-to-tv-019.md` | TV-014 (LTspice, wrapper) | `peer-review-checklist-code` | `checklist_tool_validation`; cross item X-5 | NEEDS CHANGES (reviewer APPROVED) |
| Tool validation `7be809d4` | INSP-040 `tool-validation-rust-toolchain.md` | TV-020 to TV-023 | `peer-review-checklist-code` | header "Item set applied"; cross item X-1 | NEEDS CHANGES (reviewer APPROVED) |
| Tool validation `7be809d4` | INSP-041 `tool-validation-tv-013.md` | TV-013 | `peer-review-checklist-code` | header "Item set applied" | NEEDS CHANGES (reviewer APPROVED) |
| Tool validation `7be809d4` | INSP-043 `tool-validation-tv-002.md` | TV-002 | `peer-review-checklist-code` | header "Item set applied" | NEEDS CHANGES (reviewer APPROVED) |
| Tool validation `7be809d4` | INSP-088 `tool-validation-tv-015-to-tv-019.md` | TV-015 to TV-019 | `peer-review-checklist-code` | `checklist_tool_validation` | APPROVED |
| Software assurance `5b135285` | INSP-046 `template-peer-review-checklist-software-assurance-software-assurance.md` | SA template (SA pair of INSP-032; also a step 3 record) | `peer-review-checklist-requirements` | `assurance_checklist` | NEEDS CHANGES (reviewer APPROVED) |
| Software assurance `5b135285` | INSP-047 `cm-plan-05-software-assurance.md` | 05 CM plan | `peer-review-checklist-requirements` | `checklist_software_assurance` | APPROVED |
| Software assurance `5b135285` | INSP-048 `tool-validation-rust-toolchain-software-assurance.md` | TV-020 to TV-023 (SA pair of INSP-040) | `peer-review-checklist-code` | `assurance_checklist` | NEEDS CHANGES (reviewer APPROVED) |
| Software assurance `5b135285` | INSP-049 `tool-validation-tv-013-software-assurance.md` | TV-013 (SA pair of INSP-041) | `peer-review-checklist-code` | `assurance_checklist` | NEEDS CHANGES (reviewer APPROVED) |
| Software assurance `5b135285` | INSP-050 `classification-03-software-classification-and-rmm-software-assurance.md` | 03 classification | `peer-review-checklist-classification` | `checklist_software_assurance` | NEEDS CHANGES (reviewer APPROVED) |
| Software assurance `5b135285` | INSP-051 `tool-validation-tv-002-software-assurance.md` | TV-002 (SA pair of INSP-043) | `peer-review-checklist-code` | `assurance_checklist` | NEEDS CHANGES (reviewer APPROVED) |
| Software assurance `5b135285` | INSP-062 `trade-studies-ts-001-ts-002-software-assurance.md` | TS-001, TS-002 | `peer-review-checklist-design` | `assurance_checklist` | NEEDS CHANGES (reviewer APPROVED) |
| Software assurance `5b135285` | INSP-066 `adrs-001-to-027-software-assurance.md` | ADR-001 to ADR-027 | `peer-review-checklist-design` | `checklist_software_assurance` | NEEDS CHANGES (reviewer NEEDS CHANGES) |
| Software assurance `5b135285` | INSP-070 `code-tools-traceability-software-assurance.md` | `tools/traceability.py` | `peer-review-checklist-code` | `assurance_checklist` | NEEDS CHANGES (reviewer APPROVED) |
| Software assurance `5b135285` | INSP-073 `software-plan-07-software-assurance.md` | 07 software plan | `peer-review-checklist-requirements` | `checklist_software_assurance` | NEEDS CHANGES (reviewer APPROVED) |
| Software assurance `5b135285` | INSP-074 `ts-007-synthesizer-and-reference-software-assurance.md` | TS-007 | `peer-review-checklist-risk` | `assurance_checklist` | NEEDS CHANGES (reviewer APPROVED) |
| Software assurance `5b135285` | INSP-075 `analysis-keyer-host-study-software-assurance.md` | keyer host study (SA pair of INSP-071; item SA-A4 also cites the analysis blob `0386cc6e`) | `peer-review-checklist-design` | `assurance_checklist` | NEEDS CHANGES (reviewer NEEDS CHANGES) |
| Software assurance `5b135285` | INSP-087 `ts-011-enclosure-software-assurance.md` | TS-011 (SA pair of INSP-081) | `peer-review-checklist-risk` | `assurance_checklist` | NEEDS CHANGES (reviewer NEEDS CHANGES) |
| Software assurance `5b135285` | INSP-101 `tool-validation-tv-003-tv-007-tv-010-tv-012-software-assurance.md` | TV-003, TV-007, TV-010, TV-012 | `peer-review-checklist-code` | `assurance_checklist` | NEEDS CHANGES (reviewer APPROVED) |
| Software assurance `5b135285` | INSP-102 `code-wp-sw-09-software-assurance.md` | WP-SW-09 code | `peer-review-checklist-code` | `assurance_checklist` | NEEDS CHANGES (reviewer APPROVED) |
| Software assurance `5b135285` | INSP-103 `code-wp-sw-01-software-assurance.md` | WP-SW-01 code | `peer-review-checklist-code` | `assurance_checklist` | NEEDS CHANGES (reviewer NEEDS CHANGES) |
| Software assurance `5b135285` | INSP-104 `code-wp-sw-02-software-assurance.md` | WP-SW-02 code | `peer-review-checklist-code` | `assurance_checklist` | NEEDS CHANGES (reviewer NEEDS CHANGES) |
| Software assurance `5b135285` | INSP-105 `code-wp-sw-03-software-assurance.md` | WP-SW-03 code | `peer-review-checklist-code` | `assurance_checklist` | NEEDS CHANGES (reviewer NEEDS CHANGES) |
| Software assurance `5b135285` | INSP-106 `code-wp-sw-11-software-assurance.md` | WP-SW-11 code | `peer-review-checklist-code` | `assurance_checklist` | NEEDS CHANGES (reviewer NEEDS CHANGES) |
| Analysis `0386cc6e` | INSP-056 `analysis-frequency-budget-and-clock-plan.md` | `frequency-budget.md`, `clock-plan.md` (the note names the analysis template at line 10) | `peer-review-checklist-design` | header comment; cross item X-1 | NEEDS CHANGES (reviewer APPROVED) |
| Analysis `0386cc6e` | INSP-071 `analysis-keyer-host-study.md` | `keyer-host-study.md` | `peer-review-checklist-design` | `checklist_analysis` | NEEDS CHANGES (reviewer APPROVED) |
| Analysis `0386cc6e` | INSP-072 `analysis-ui-design.md` | `ui-design.md` | `peer-review-checklist-design` | `checklist_analysis` | NEEDS CHANGES (reviewer APPROVED) |
| Analysis `0386cc6e` | INSP-083 `analysis-shielding-estimate.md` | `shielding-estimate.md` | `peer-review-checklist-design` | `checklist_analysis` | NEEDS CHANGES (reviewer APPROVED) |
| Analysis `0386cc6e` | INSP-084 `analysis-mechanical-tolerance-stack.md` | `mechanical-tolerance-stack.md` | `peer-review-checklist-design` | `checklist_analysis` | NEEDS CHANGES (reviewer APPROVED) |

Rule at each disposition (Table 4-1 row 53):

| Disposition | Effect on the records above |
|---|---|
| Approved, template blobs unchanged | Every record stands on the blob that merges. No re-run. Section 5 step 8 re-issues each record's `checklist` field |
| Approved with conditions that change a template blob | For each record against a changed template, before the condition's fix merges, this CR records one of two entries per record in a table appended to this section: (a) **delta iteration**: the owning reviewer re-answers the items whose text changed (`git diff 7784672 <fix commit> -- <template>`), as a new iteration of that record; or (b) **kept with rationale**: the changed items are not items the record answered (for example a G-kind item of another kind, or an SA section marked N/A in the record), named item by item. Records against an unchanged template follow the row above. Then section 5 step 8 |
| Rejected | Revision A never reaches `main`. Each record is re-run with a checklist on `main`, or kept with a rationale entry in this CR, before the product it reviews is credited at a gate. The accreditations and gate decisions of the section 4 Schedule row are re-looked at B0 |
| Deferred | Every record stays held at NEEDS CHANGES; no re-issue until the re-look disposition |

## 5. Implementation plan

| Step | Artifact and path | Responsible | Done (SHA) |
|---|---|---|---|
| 1 | Product change on `cr/CR-012-pdr-checklist-templates` (the four files of the table above) | Claude, WP-PDR-03 author | `ac9b7a5` |
| 2 | This CR file on `main`, state Submitted | Claude, WP-PDR-03 author | the commit that adds this file (`Refs: CR-012`) |
| 3 | Template review records `docs/reviews/PDR/checklists/template-peer-review-checklist-analysis.md`, `template-peer-review-checklist-software-assurance.md`, `template-peer-review-checklist-tool-validation.md` against the blobs of step 1 (PDR work plan WP-PDR-03; checklist `peer-review-checklist-requirements.md` section G) | Independent reviewer | |
| 4 | Section 6 impact review | Independent reviewer that did not author this CR | |
| 5 | Owner disposition (section 7), at B0 with the template review verdicts. Before it, Claude re-runs the section 4.1 listing and adds any record filed since `d5a3058` to the section 4.1 table | Owner | |
| 6 | Merge `git merge --no-ff cr/CR-012-pdr-checklist-templates` with message `merge(CR-012): <title>`; any Major fix from step 3 lands on the branch first, as a new commit with `CR: CR-012` | Claude (CM function) | |
| 7 | Section 9 verification | Independent reviewer | |
| 8 | Re-issue of the section 4.1 records after the merge. For each record, the owning reviewer (the record's `reviewer_agent` role, a new invocation; for a paired SA record, its assurance reviewer) re-issues the record as a delta that changes only the checklist fields: `checklist` names the merged template (`peer-review-checklist-tool-validation`, `peer-review-checklist-software-assurance` or `peer-review-checklist-analysis`) with `checklist_revision: A`, and the applied-template field (`checklist_tool_validation`, `checklist_software_assurance`, `assurance_checklist`, `checklist_analysis` or the header comment) names the merged blob on `main`. This closes the cross items that plan the switch (INSP-038 X-5, INSP-040 X-1, INSP-056 X-1, and the "delta after CR-012 merges" notes of the others). Where a delta iteration or a kept-with-rationale entry of section 4.1 applies, it is done in the same re-issue. A paired SA record switches to `peer-review-checklist-software-assurance` even where its `checklist` today copies the file review's checklist (INSP-046, INSP-048, INSP-049, INSP-051, INSP-075, INSP-087 and the others of section 4.1). No record of section 4.1 keeps its current `checklist` field: its header or cross item states that the field is a stand-in because `tools/validate_docs.py` rejects a `checklist` naming a template absent from `main`. Record verdicts follow the lead SE convention of 2026-09-27 (set in the merge commit or the commit after it). `tools/validate_docs.py` passes on every re-issued record | Owning reviewer of each record; Claude (CM function) tracks completion in section 8 | |

Verification of the implementation (what the independent reviewer will check): `git diff 573f9f5 <merge>` touches exactly the four paths; after step 8, every record of section 4.1 names the merged template in `checklist` and the merged blob in its applied-template field, or carries its section 4.1 entry; the three template blobs on `main` equal the blobs the step 3 records APPROVED; `tools/validate_docs.py` exits as on the base (no new failure); `python -m unittest discover -s tools/tests` shows no new failure; a filled copy of each template passes `tools/validate_docs.py` (the procedure of section 9, row 3).

## 6. Independent review of the impact assessment

Not required by 05 §3 for this Class II change (no requirement, ICD, hazard or test case is affected). Required by PDR work plan rule C6 before the owner's disposition: not yet performed. The reviewer must not have authored this CR or the templates.

| Item | Reviewer (agent invocation) | Date | Finding | Resolution |
|---|---|---|---|---|
| | | | | |

Reviewer concurrence: pending.

### 6.1 Impact review round 1: independent reviewer (2026-09-27)

Reviewer: independent reviewer agent (CR-012 impact review invocation), a separate invocation that authored no part of this CR, of the three templates or the 08 hunks, and none of the records INSP-031 to INSP-033 or INSP-038 to INSP-050. Date 2026-09-27. The table and the "pending" line above are the template placeholders and are left as written; this round is the first review entry. Configuration reviewed: this file at blob `91c8c626` on `main` at `fefcf55`; branch `cr/CR-012-pdr-checklist-templates` at `7784672`. Method: `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` first (queries: the three template names and "a checklist that does not yet exist"; "No checklist template for TV records exists", the `analysis-` and `tool-validation-` slugs), then `grep` and `git` only to pin lines and blobs; `git diff main...cr/CR-012-pdr-checklist-templates`; `tools/validate_docs.py` on `main`.

| Item | Reviewer (agent invocation) | Date | Finding | Resolution |
|---|---|---|---|---|
| IR-F1 (Major) Records already made on the Submitted blobs are not in the assessment | Independent reviewer agent (CR-012 impact review) | 2026-09-27 | §4 row Verification says "The templates govern future review records only", and the row 53 paragraph says "the three templates are new, so no record was made against an earlier revision of them". At `fefcf55` this is no longer true: the branch blobs of revision A are already applied by filed PDR records. Tool validation template `7be809d4`: INSP-038 (TV-014, `tool-validation-tv-014-to-tv-019.md`), INSP-040 (TV-020 to TV-023), INSP-041 (TV-013), INSP-043 (TV-002). Software assurance template `5b135285`: INSP-046, INSP-047 (verdict APPROVED), INSP-048, INSP-049, INSP-050. INSP-038 cross item X-5 and INSP-040 cross item X-1 already plan to switch the `checklist` field after the merge. The analysis template `0386cc6e` is cited by `docs/design/analysis/frequency-budget.md` (line 10) for its coming record. The consequence for the disposition is not stated. "Approved" as submitted keeps these records valid. But "Approved with conditions" that change a template blob (INSP-046 recommends its finding-3 and finding-4 before the merge), or "Rejected", leaves each of these records applied to a revision that never reached `main`. Under the Table 4-1 row 53 rule each then needs a re-run or a kept-with-rationale entry in this CR. The accreditation and B0/B1a decisions that rest on the TV and SA records (plan §5.2) would also move. The owner would decide at B0 without this list. | Author: in §4 rows Verification and Schedule and in the row 53 paragraph, list the records above (and any filed before the disposition) as made against revision A at the named blobs. State that a condition changing a template blob triggers a delta iteration or a kept-with-rationale entry for each. Add a §5 step after the merge: the owning reviewer of each record re-issues it with `checklist` naming the merged template (the cross items), or the CR states why the field stays as it is |
| IR-F2 (Minor) Follow-on documents missed or without a carrier | Independent reviewer agent (CR-012 impact review) | 2026-09-27 | §4 row Documentation omits `docs/plan/semp.md` Appendix B line 450: "Two checklists remain due, `peer-review-checklist-analysis.md` and `peer-review-checklist-software-assurance.md`, both written by Claude before PDR". It names the 07 follow-ons (line 658 "the four checklists of section 10", line 672 row "5.17 item 13" "Partial at SRR", Annex A lines 889 to 896) only by "07 writer order". No open CR carries them: the 07 and SEMP diffs of `cr/CR-013-process-04-07-semp-srr-liens` (WP-PDR-13) and `cr/CR-010-apply-srr-decisions-9-and-40` (WP-PDR-17) contain none of these edits. After the merge, the baselined 07 and SEMP would contradict 08 §3.5. This concurs with INSP-046 finding-3. | Author: add the SEMP line to the row. For each follow-on, name the carrying CR (for example a CR-013 revision, since WP-PDR-13 owns the SEMP and the 07 lien slot) and the due point (before F1) |
| IR-F3 (Minor) INSP-022 finding-2 is only partly addressed | Independent reviewer agent (CR-012 impact review) | 2026-09-27 | The row 53 paragraph says INSP-022's "finding-2 lien is addressed by this change". Only its 08 §3.1 and §3.5 parts are. The 08 §1 template list (line 29) and `docs/process/README.md` line 45 are fixed by CR-015 (its §1, line 97). INSP-031 item CR-1 raised this; the text is unchanged at `91c8c626`. | Author: "partly addressed by this change; completed by CR-015" |
| IR-F4 (Minor) Interacting CR-015 not recorded | Independent reviewer agent (CR-012 impact review) | 2026-09-27 | `cr/CR-015-process-liens-01-02-08` is stacked on this branch (base `7784672`; `git log main..cr/CR-015-*` includes `ac9b7a5` and `7784672`). Its §5 step 6 merges only after CR-012, and its owner question Q4 asks for that order. `related` lists CR-007 and CR-010 but not CR-015. A rejection, or a condition that changes 08 or a template, forces a rebase of CR-015 and a repeat of its section 9 checks and of the INSP-022 delta. | Author: add CR-015 to `related`. In §4 row Schedule, state the merge order and the effect of a non-Approved disposition on CR-015 |
| IR-F5 (Minor) Route of the template records to APPROVED, and a CR file pinned as a product | Independent reviewer agent (CR-012 impact review) | 2026-09-27 | §5 does not state the lead SE convention of 2026-09-27: the record verdict is held until the merge and set in the merge commit or the one after it (INSP-031 item CR-2). Also, INSP-032, INSP-033 and INSP-046 pin this CR file in `product_files` at `91c8c626`, and INSP-031 pins `02f27964`, which already drifts (`validate_docs.py` note on `main`). Every later edit of this file drifts them: this round, §7, §8 to §11. When their `verdict` is set to APPROVED at the merge, the record drift rule then fails them. | Author: in §5 step 6, state the convention. Also state that the commit which sets the verdicts re-pins, or drops, the CR file in those `product_files`. The CR is an input to those reviews, not their product |
| IR-F6 (Minor) §8 trailer claim for `ac9b7a5`; stale base for the §9 tool check | Independent reviewer agent (CR-012 impact review) | 2026-09-27 | In `ac9b7a5`, a blank line separates `CR: CR-012` from `Co-Authored-By`, so `git log --format='%(trailers)'` returns only the Co-Authored-By line. The §8 answer "yes" holds only for the message body; `7784672` carries the trailer correctly. This concurs with INSP-046 finding-4. Separately, §5 and §9 compare the tool runs with base `573f9f5`. `main` has since moved: at `fefcf55`, `validate_docs.py` reports 63 passed and 8 failed, all record drift from other work. The failures are in the CR-007 records, the SRR ADR, TS-001/TS-002, 02 and TV-001 to TV-010 records, and none are caused by this CR. | Author: §8 row `ac9b7a5`: "present in the body; not parsed as a trailer (INSP-046 finding-4)". §5 and §9: compare against the first parent of the merge commit, not `573f9f5` |

Items checked with no finding:

- Class II is correct under 05 §2: no requirement, ICD, hazard, test case, form, fit or function changes.
- `affected_cis` [2, 53] and `affected_paths` match the branch. `git diff --stat main...cr/CR-012-pdr-checklist-templates` touches exactly the four paths (803 insertions, 9 deletions). `git ls-tree 7784672` gives the §1 table blobs exactly (`0386cc6e`, `5b135285`, `7be809d4`, `56c54011`). 08 has not changed on `main` since `573f9f5`, so the merge has no 08 conflict from `main`.
- Effectivity is the merge before wave 1a, with `target_release: none` and no released unit.
- No requirement or control is weakened:
  - The 08 §3.5 software assurance row widens from "second review of safety-critical products" to every product that 07 §2.1.1 marks Yes. This aligns 08 with 07, not the reverse.
  - The removed interim clause ("until then the assurance reviewer uses the design, code and test checklists plus 07 §14") is obsolete once the template exists.
  - The removed parenthetical "no deck is reviewed without it" is still covered by the unchanged general rule of §3.5: "A review that needs a checklist that does not yet exist is not held".
  - The SA template's exclusion of the 8.10 §6 tasks of swe-015, swe-151, swe-016 and swe-174 follows the 07 §2.1.1 routing, which routes none of their products.
- `tools/validate_docs.py` enforces only the lower-case file-name rule (line 168) and the checklist pattern (line 221), so the `analysis-` and `tool-validation-` record names and the `tool-validation` stem need no tool change.
- The `docs/cm/tool-validation/README.md` owner action 1 follow-on is named.
- The verification-of-implementation plan (§5, §9) is adequate once the IR-F5 and IR-F6 amendments are made.

Reviewer concurrence: concur with Class II and with the change. Do not concur with disposition until IR-F1 is resolved. **Impact review complete, with findings: 1 Major (IR-F1), 5 Minor (IR-F2 to IR-F6).** The CR stays Submitted for the author to revise §4 and §5 and re-submit for a re-check of IR-F1. The author resolves the Minor findings in the same revision or states why not.

## 7. CCB disposition (owner)

| Field | Value |
|---|---|
| Decision | Not dispositioned |
| Class confirmed | |
| Date | |
| Conditions | |
| Rationale | |
| Waiver scope (if Approved (waiver)) | n/a |
| Re-look trigger and re-look-by review (if Deferred) | |
| Source | |

Disposition history (append only):

| Date | Decision | New target | Source |
|---|---|---|---|
| | | | |

## 8. Implementation record

| Commit | Files | Trailer check (`CR: CR-012` present) |
|---|---|---|
| `ac9b7a5` (branch `cr/CR-012-pdr-checklist-templates`, prototype) | the four files of the table above | yes |
| `7784672` (branch, Major fixes of INSP-032 finding-1 and INSP-033 finding-1 and finding-2, template review iteration 1) | `peer-review-checklist-software-assurance.md`, `peer-review-checklist-tool-validation.md` | yes |

Traceability report after implementation: not affected (no requirement, test case or hazard file changes); renders regenerated: none (no visual product).

## 9. Verification of implementation

| Impact item | Planned closure (from §4/§5) | Evidence (report path, TC id, analysis file) | Result |
|---|---|---|---|
| Scope | Diff touches exactly the four paths | `git diff --stat 573f9f5 ac9b7a5`: 4 files, 792 insertions, 9 deletions (author run, 2026-09-27); after the fixes, `git diff --stat 573f9f5 7784672`: 4 files, 803 insertions, 9 deletions | Pending independent verification |
| Tools unaffected | `tools/validate_docs.py` and the unit tests show no new failure against the base | Author run on `main` at `573f9f5` (the change is not on `main`, and neither tool reads the templates' bodies or 08): `validate_docs.py` 50 passed, 1 failed; the failure is pre-existing SRR record drift (`risk-register-06.md` and `tool-validation-tv-001-to-tv-010.md` name blobs that later wave 0 commits changed), not this change; unit tests 453 run, 1 failure (`RepositoryTests.test_repository_exit_zero`, the same drift), 11 skipped | Pending independent verification |
| Filled templates validate | A copy of each template, with only the placeholders filled, passes the record schema | Author run on a `git archive` export of `573f9f5` with the branch files overlaid: `validate_docs.py --root <export>`: the three sample records `analysis-rx-cascade.md`, `requirements-sw-keyer-software-assurance.md`, `tool-validation-tv-014-ltspice.md` PASS; 54 passed, 0 failed. After the fixes (author run, 2026-09-27): export of `7784672` made a git work tree, with a filled copy of the tool validation template at verdict APPROVED (TV-001, the 7 fixture files of `tools/tests/fixtures/schema/` listed by blob, the tree in `fixture_trees`) committed: `validate_docs.py --root <probe>` PASS on that record under the record drift rule; a negative control with the fixture directory as a `product_files` entry FAIL ("is not in HEAD; record drift rule"), the INSP-033 finding-2 reproduction | Pending independent verification |

Independent verifier (agent invocation): pending.

## 10. Closure

| Field | Value |
|---|---|
| Owner merge approval | |
| Merge commit | |
| Waiver entered in CSA item 12 and affected VDDs | n/a |
| CSA regenerated | |
| Date closed | |

## 11. History

| Date | State | By | Commit on main | Note |
|---|---|---|---|---|
| 2026-09-27 | Submitted | Claude (WP-PDR-03 author) | the commit that adds this file | Created with the impact assessment complete; product change prototyped on `cr/CR-012-pdr-checklist-templates` at `ac9b7a5`; section 6 review (rule C6) and the WP-PDR-03 template reviews pending |
| 2026-09-27 | Submitted | Claude (WP-PDR-03 author) | the commit that records this row | Template reviews iteration 1 (`5f57f93`): INSP-031 no Major; INSP-032 1 Major, INSP-033 2 Major. The Majors are fixed on the branch at `7784672` (step 6: fix on the branch first, `CR: CR-012`); Minor findings wait (PDR work plan rule C1). Iteration 2 delta of INSP-032 and INSP-033 and the section 6 review pending |
| 2026-09-27 | Submitted | Claude (WP-PDR-03 author) | the commit that records this row | Section 6.1 round 1 IR-F1 (Major) fixed: section 4 rows Verification and Schedule and the row 53 paragraph list the 29 records made against revision A (new section 4.1, listed at `d5a3058`, with the rule at each disposition); new section 5 step 8 re-issues each record's checklist field after the merge. IR-F2 to IR-F6 (Minor) wait (PDR work plan rule C1). Re-submitted for the round 2 re-check of IR-F1 |
