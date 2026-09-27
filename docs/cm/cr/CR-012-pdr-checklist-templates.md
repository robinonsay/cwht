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
| Verification | None: no TC added, modified or invalidated. The templates govern future review records only |
| Cost | None |
| Schedule | Positive: unblocks the analysis, SA and TV reviews of waves 1a to 2b. Needs the owner's disposition at B0 (Mon 09-28) so the templates are on `main` before wave 1a (Tue 09-29) |
| Requirements and traceability | None: no REQ changes; volatility contribution 0 |
| Regulatory | None: no Part 97, 1, 2 or 15 clause |
| Documentation | The four files of the table above. Follow-on documentation outside this CR (named for their writers, PDR work plan section 5.3): 07 §15 row "5.17 item 13" and the section 15 lead paragraph ("until it exists") and 07 Annex A, which lists four checklists (07 writer order); 01 §13 slug list (`analysis-`, `tool-validation-`), WP-PDR-12; 08 §1 repository map and §3.2 reviewer block, and `docs/process/README.md`, WP-PDR-12; `docs/cm/tool-validation/README.md` owner action 1 ("No checklist template for TV records exists"), the tool owner of WP-PDR-07 |
| Released units | None: no unit exists |

Checklist change rule of Table 4-1 row 53 ("its CR lists every `INSP-NNN` record to re-run, or to keep with a rationale"): the three templates are new, so no record was made against an earlier revision of them. Kept without re-run: INSP-015 (TV-001 to TV-010, reviewed with the code checklist plus items TV-S1 to TV-S10 under SRR decision 117) and INSP-017, INSP-018, INSP-026, INSP-027 and INSP-030 (assurance reviews that applied the SWEHB section 7.1 tasks directly, as 07 §15 directed while the SA checklist did not exist). Rationale: each was made under the rule in force at SRR, which decision 117 and 07 §15 accepted; their delta iterations at PDR may apply the new checklists at the owning reviewer's choice. INSP-022 (08) is affected: its finding-2 lien is addressed by this change and is verified at INSP-022's next delta iteration (WP-PDR-12).

Classification rationale: Class II. The change modifies process documentation (a process document and review checklists) without impact to form, fit, function, interchangeability, interfaces, safety, verification evidence or operator procedures (05 §2, Class II definition). No requirement, ICD, hazard or test case is affected, so 05 §3 does not require the independent impact review for this class; PDR work plan rule C6 requires it for every CR raised in the phase (section 6).

## 5. Implementation plan

| Step | Artifact and path | Responsible | Done (SHA) |
|---|---|---|---|
| 1 | Product change on `cr/CR-012-pdr-checklist-templates` (the four files of the table above) | Claude, WP-PDR-03 author | `ac9b7a5` |
| 2 | This CR file on `main`, state Submitted | Claude, WP-PDR-03 author | the commit that adds this file (`Refs: CR-012`) |
| 3 | Template review records `docs/reviews/PDR/checklists/template-peer-review-checklist-analysis.md`, `template-peer-review-checklist-software-assurance.md`, `template-peer-review-checklist-tool-validation.md` against the blobs of step 1 (PDR work plan WP-PDR-03; checklist `peer-review-checklist-requirements.md` section G) | Independent reviewer | |
| 4 | Section 6 impact review | Independent reviewer that did not author this CR | |
| 5 | Owner disposition (section 7), at B0 with the template review verdicts | Owner | |
| 6 | Merge `git merge --no-ff cr/CR-012-pdr-checklist-templates` with message `merge(CR-012): <title>`; any Major fix from step 3 lands on the branch first, as a new commit with `CR: CR-012` | Claude (CM function) | |
| 7 | Section 9 verification | Independent reviewer | |

Verification of the implementation (what the independent reviewer will check): `git diff 573f9f5 <merge>` touches exactly the four paths; the three template blobs on `main` equal the blobs the step 3 records APPROVED; `tools/validate_docs.py` exits as on the base (no new failure); `python -m unittest discover -s tools/tests` shows no new failure; a filled copy of each template passes `tools/validate_docs.py` (the procedure of section 9, row 3).

## 6. Independent review of the impact assessment

Not required by 05 §3 for this Class II change (no requirement, ICD, hazard or test case is affected). Required by PDR work plan rule C6 before the owner's disposition: not yet performed. The reviewer must not have authored this CR or the templates.

| Item | Reviewer (agent invocation) | Date | Finding | Resolution |
|---|---|---|---|---|
| | | | | |

Reviewer concurrence: pending.

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
