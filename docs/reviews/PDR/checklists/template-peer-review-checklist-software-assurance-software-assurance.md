---
# Peer-review record front matter (charter sections 2 and 5; docs/process/01-lifecycle-and-reviews.md section 13
# is the single field list; docs/process/07-software-engineering-plan.md sections 2.1.1, 10.2 and 15).
# This is the paired software assurance record (07 section 10.2) of the file review INSP-032
# (docs/reviews/PDR/checklists/template-peer-review-checklist-software-assurance.md, reviewer:WP-PDR-03-templates),
# requested there as "SA pair needed" (PDR work plan WP-PDR-03, wave 0).
# Checklist applied: docs/templates/peer-review-checklist-software-assurance.md revision A AS ON ITS CR-012 BRANCH
# (cr/CR-012-pdr-checklist-templates at 7784672, blob 5b13528504868b2add0f0b1e329c63aa2b54cdf4; not merged),
# which is also the product under review. The `checklist` field names peer-review-checklist-requirements
# (revision C, section G), the checklist 07 section 2.1.1 row "Software plans" routes to, because
# tools/validate_docs.py fails a record whose `checklist` names a template absent from main (line 865),
# and the lead SE convention of 2026-09-27 does not change the validator. The field `assurance_checklist`
# names the template actually applied.
# Iteration 2 (2026-09-29, re-pin delta; CR-012 section 9 pre-merge check 2 and lead SE ruling (2) of 2026-09-29):
# 08 re-pinned from 56c54011 (CR-012) to 374fd777 (CR-015 head 7efd900, the blob main holds after both merges);
# the CR-012 file is dropped from product_files after a delta on the CR-012 sections this record reviewed
# (sections 4, 8 and 9); the four blobs now equal INSP-032 iteration 3 (section "Iteration 2").
id: INSP-046
checklist: peer-review-checklist-requirements
checklist_revision: C
assurance_checklist: "docs/templates/peer-review-checklist-software-assurance.md@5b13528504868b2add0f0b1e329c63aa2b54cdf4 (revision A, branch cr/CR-012-pdr-checklist-templates at 7784672)"
checklist_file: docs/reviews/PDR/checklists/template-peer-review-checklist-software-assurance-software-assurance.md
product: docs/templates/peer-review-checklist-software-assurance.md
# product_commit and product_files: equal to INSP-032 iteration 2 (readiness R1; rule C2). Iteration 2: equal to
# INSP-032 iteration 3: product_commit the CR-015 branch head 7efd900 (base 7784672), which holds the three template
# blobs unchanged and the combined 08 blob
product_commit: "7efd900b4011a7959f99bef00cba3a0b732cf8b1"
# product_files iteration 2: 08 56c54011 replaced by 374fd777 (git rev-parse 7efd900:<path>). The entry
# "docs/cm/cr/CR-012-pdr-checklist-templates.md@91c8c6261a4b2bd9b3d789676c1188b54f022ddd" is dropped (lead SE ruling (2);
# INSP-060 and INSP-032 precedent): the CR-012 sections this record reviewed changed, so the delta reads them first
# (91c8c626 to 37ca884b, section "Iteration 2"); the CR file is a record on main appended at each lifecycle step, so a
# pin would drift at the merge. A later change to CR-012 sections 1 to 5 needs a delta of this record
product_files: ["docs/templates/peer-review-checklist-software-assurance.md@5b13528504868b2add0f0b1e329c63aa2b54cdf4", "docs/templates/peer-review-checklist-tool-validation.md@7be809d4ceb9a202473eb19da3627fe0cd427900", "docs/templates/peer-review-checklist-analysis.md@0386cc6e78da65578b1cce8b2f793cd3db224921", "docs/process/08-agent-briefing.md@374fd777b1f05e408c133ed1f222b6cb90865114"]
# inputs read (not reviewed). Iteration 2 adds, read at main 1404c67: the CR-012 file (37ca884b), INSP-032 iteration 3
# (a9b0bcd8), 08 at 56c54011 (the delta base) and docs/cm/deviations.md (entries 8 and 9)
input_files: ["docs/process/rmm.json@e326ddd1b7296d7d7fe172be6f33535cee3192d7", "docs/reviews/PDR/checklists/template-peer-review-checklist-software-assurance.md@9ab5c857c85fed2936393fa21648728b8b3bba0c", "docs/cm/cr/CR-012-pdr-checklist-templates.md@37ca884bb859b193c1c637426dae83bcd7983d68", "docs/reviews/PDR/checklists/template-peer-review-checklist-software-assurance.md@a9b0bcd892a41f9633c36b37eee5654ba678dd69", "docs/process/08-agent-briefing.md@56c540113110b0d8916219d3cb531d6a76587713", "docs/cm/deviations.md@917c8863c639be31fabe50481aaff3fec63518aa"]
paired_record: INSP-032
product_type: plans
criticality: neither
product_size: 1 template (229 lines; readiness R1 to R4, sections A to F, section B task table of 8 product-type rows plus "Every product type"); 4 further blobs carried unchanged from INSP-032. Iteration 2 delta: 08 56c54011 to 374fd777 (6 CR-015 hunks, 14 insertions, 13 deletions); CR-012 file 91c8c626 to 37ca884b (sections 4, 8 and 9 read)
sprint: PDR-prep
author_agent: "author:WP-PDR-03 (Claude as checklist owner)"
reviewer_agent: "sa-reviewer:WP-PDR-03-templates"
assurance_required: true
assurance_reviewer_agent: "sa-reviewer:WP-PDR-03-templates (software assurance function; paired file review INSP-032 by reviewer:WP-PDR-03-templates)"
# iteration 2: re-pin delta on 08 374fd777 and the CR-012 file (section "Iteration 2")
iteration: 2
readiness_met: true
# reviewer_verdict and assurance_verdict: APPROVED at iteration 1 (no Major; four Minor findings are liens due the CDR
# readiness declaration, PDR work plan rule C1)
reviewer_verdict: APPROVED
assurance_verdict: APPROVED
# verdict: held at NEEDS CHANGES under the lead SE convention of 2026-09-27 (INSP-031 practice): the reviewed blobs
# exist only on the unmerged branch cr/CR-012-pdr-checklist-templates, so tools/validate_docs.py would fail an
# APPROVED record (record drift rule). The software lead sets APPROVED in the CR-012 merge commit, or the commit right
# after it, when the blobs reach main unchanged and INSP-032 is APPROVED (07 section 10.2)
# Iteration 2: the 08 blob is the CR-015 one, so the software lead sets APPROVED on this record and INSP-032 in the
# CR-015 merge commit (or the commit right after it), with CR-012 merged first and the four blobs unchanged
verdict: NEEDS CHANGES
findings_major: 0
findings_minor: 4
# findings_open: 4 at iteration 1. Iteration 2: 0. finding-4 is Verified (CR-012 section 8 correction of record);
# finding-1 to finding-3 are liens due the CDR readiness declaration (a lien is not Open; the INSP-032 practice)
findings_open: 0
findings_fixed: 0
findings_verified: 1
findings_deferred: 0
assurance_findings_major: 0
assurance_findings_minor: 4
assurance_tasks_applied: ["swe-134 7.1 task 5", "swe-022 7.1 task 1", "swe-013 7.1 task 1", "swe-013 7.1 task 2", "swe-024 7.1 task 1", "swe-024 7.1 task 2", "swe-024 7.1 task 3", "swe-039 7.1 task 7", "swe-039 7.1 task 8", "swe-121 7.1 task 1", "swe-125 7.1 task 1", "swe-139 7.1 task 1", "swe-087 7.1 task 3", "swe-090 7.1 task 1", "swe-023 7.1 task 1", "swe-088 7.1 task 1", "swe-088 7.1 task 2", "swe-089 7.1 task 1"]
swe134_items_checked: []
deferred_rids: []
# items_no: iteration 2 drops SA-E3 (answer now Yes: the CR-012 record states the unparsed trailers and deviations
# entries 8 and 9 carry them for the owner's S1 decision); swe-023 task 1 and swe-024 task 3 stay No (liens)
items_no: ["swe-023 7.1 task 1", "swe-024 7.1 task 3"]
# effort: iteration 1 30 turns, 50 minutes; iteration 2 adds 20 turns, 35 minutes
effort_turns: 50
effort_minutes: 85
record_status: Open
date: 2026-09-27
date_closed: null
---

# Peer review record INSP-046: software assurance second review of the software assurance checklist template (WP-PDR-03, CR-012)

**Product.** `docs/templates/peer-review-checklist-software-assurance.md`, blob `5b135285`, on branch `cr/CR-012-pdr-checklist-templates` at `7784672` (checked with `git ls-tree 7784672`; `git merge-base --is-ancestor 7784672 main` is false, so the blob is branch-only). The other four blobs of `product_files` are carried unchanged from INSP-032 so that both records name the same blobs (R1, SA-A3); this record reviews them only where they bear on the software assurance template (08 section 3.5 row, CR-012 sections 4, 8 and 9). **Checklist applied:** the product itself, revision A as on its CR-012 branch (see the front matter for why the `checklist` field names the requirements template). **Paired record:** INSP-032 iteration 2 (committed `091bceb`, blob `9ab5c857`), file reviewer `reviewer:WP-PDR-03-templates`.

**Independence (rule C4; 07 section 2.1).** This invocation authored no part of WP-PDR-03, CR-012 or INSP-032, edited no product file, and is not the file reviewer. Author, file reviewer and assurance reviewer are three different invocations.

**Search first (charter section 11 rule 1).** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (queries: paired software assurance record fields; SWEHB SA tasking for peer reviews and checklists; NPR 7150.2D 3.7.3 items a to l; validate_docs checklist-template rule, which returned no Python hit and was then pinned by `grep -n` in the known file `tools/validate_docs.py`; commit trailer check). `grep -n` and a Python extraction of SWEHB section 7.1 lists and of SWEHB topic 8.10 section 6 were used afterwards only to pin lines.

## Record

### Findings

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | assurance | Minor | `swe-023 7.1 task 1` | Template section B rows `requirements` (line 148), `design` (151) and `code` (152); "Relief and limits" (line 101) | `rmm.json` row SWE-023 (disposition T, owner-approved at SRR) states in `implementation` that "The SWEHB 6.1 design-for-safety checklist (PAT-006) is applied at every safety-critical design review and the SWEHB 6.2 general software safety requirements checklist (PAT-007) at requirements and code review by the software assurance reviewer", and in `tailoring_rationale` that until the owner obtains the files "SWE-134 a to l serves as the design-for-safety checklist" (also 03 section 6.4 item 8). The template is the software assurance reviewer's consolidated checklist and cites SWE-023 as governing, but it names neither PAT-006 nor PAT-007 nor the interim substitution, and it plans `swe-023` task 1 ("Confirm that the identified safety-critical software components and data have implemented the safety-critical software assurance requirements") only in the `requirements` row, where nothing is yet implemented; the `design` and `code` rows, where the confirmation and the PAT checklists apply, do not carry it. The interim content is applied in practice (section C covers SWE-134 a to l for any product of a safety-critical or mission-critical component, and the `code` row carries `swe-134` task 2, `swe-219` and `swe-220`, the NPR-stated part SWE-023's relief keeps), so no safety conclusion changes. Fix: add `swe-023 task 1 (SC)` to the `design` and `code` rows with the text "PAT-006 at design, PAT-007 at requirements and code when filed under `docs/templates/` (`rmm.json` SWE-023; 03 section 6.4 item 8); until then section C (SWE-134 a to l) is the substitute", and the same sentence in "Relief and limits" | Open | Pending | |
| <a id="finding-2"></a>finding-2 | assurance | Minor | SA-A1 | Template section B row `plans` (line 149); 07 section 2.1.1 row "Software plans" | The `plans` row lists 07, the V&V plan software section, 03, 05 and TS-002, and the per-document sub-lists name only those. The template itself is part of the software assurance plan (it is the 07 section 15 row "5.17 item 13" closure, NPR 7150.2D 6.1 item k), but neither this row nor 07 section 2.1.1 names it, and `tools/validate_docs.py` `ASSURANCE_WHOLE_PRODUCTS` does not list it; its routing to this review rests on the file reviewer's inference in the INSP-032 front matter. A later revision of the template could be merged without a software assurance review (the template itself says it "does not widen or narrow" 07 section 2.1.1). Fix: add to the `plans` row "the software assurance checklist itself (07 section 15 row 5.17 item 13)" with its tasks (`swe-013` tasks 1 and 2, `swe-087` task 3, `swe-022` task 1), and include the 07 section 2.1.1 wording in the 07 follow-on of finding-3 | Open | Pending | |
| <a id="finding-3"></a>finding-3 | assurance | Minor | `swe-024 7.1 task 3` | CR-012 section 4 row "Documentation" (blob `91c8c626`); 07 section 15 lead paragraph (line 658) and row "5.17 item 13" (line 672) | After CR-012 merges, the software assurance plan still says the checklist is due ("until it exists the assurance reviewer applies the SWEHB sections directly"; row 5.17 item 13 "Partial at SRR ... due PDR"), and 07 section 15 still speaks of "the four checklists of section 10". CR-012 section 4 names this follow-on "for their writers", but no work package of the PDR work plan (section 3; the 07 writer order of section 5.3 is WP-PDR-17, WP-PDR-13, WP-PDR-47) and no 07 section 22 item carries it with a due event, so the change of commitment in the SA plan is recorded but not managed to closure. Fix: add the 07 section 15 update (lead paragraph, row 5.17 item 13 closed by the merged template, "four checklists", Annex A, and the finding-2 wording of 07 section 2.1.1) to the scope of the next 07 writer (WP-PDR-13 liens or WP-PDR-47) with the due event F1, and cite it in CR-012 section 5 | Open | Pending | |
| <a id="finding-4"></a>finding-4 | assurance | Minor | SA-E3 | Commit `ac9b7a5` message; CR-012 section 8 row `ac9b7a5` ("Trailer check ... yes") | In `ac9b7a5` the lines `CR: CR-012` and `Refs: CR-012, RFA-SRR-006` are separated from `Co-Authored-By:` by a blank line, so git does not parse them as trailers: `git log --format='%h %s%n%(trailers)' 573f9f5..7784672` prints only `Co-Authored-By` for `ac9b7a5` (the fix commit `7784672` parses correctly). 05 section 4.5 "Checks" row makes this exact command the reviewer's test, and the CSA (`docs/process/configuration-status.md` section 6, commit `9fd0962`) already counts the same pattern as "not parsed". CR-012 section 8 records "yes". The commit touches Table 4-1 rows 2 and 53 after their CR-from event and reaches `main` with the `--no-ff` merge. Fix: CR-012 section 8 records the `ac9b7a5` trailer as present in the body but not parsed, and the CSA lists it as a RID candidate at PDR as it does `9fd0962`; amending is permitted only while the branch is unpushed and would change the commit INSP-031 to INSP-033 iteration 1 name, so the record correction is the proportionate fix | Open | Pending | |

Finding rules applied: INSP-032 finding-2 (no `product_type` for an analysis routed by the validator) and finding-3 (R4 "filed or in progress" against 07 section 10.2) are the file review's and are not raised again; the assurance lens does not change their severity (Minor), because a reviewer of an analysis record can still apply the tasks of the SWEs the analysis implements under the section B lead rule, and R1 of this template already requires the paired record's `product_files`, which cannot be compared before it is filed. Disposition of all four findings of this record: liens due the CDR readiness declaration (PDR work plan rule C1; listed in PDR package section 15). Finding-3 and finding-4 are cheaper to fix before the CR-012 merge and F1, and this record recommends that timing.

### Task table (row `plans`, row "Every product type", and the other SWEs the product implements)

| Task | Safety-critical designation (SWEHB 8.10 section 6) | Applied | Result and evidence | Relief (N/A only) | Finding ids |
|---|---|---|---|---|---|
| swe-134 7.1 task 5 | SC | Yes | This record is the assurance participation in the review of a product 07 section 2.1.1 routes (row "Software plans", Yes in every column) | | none |
| swe-022 7.1 task 1 | SC | Yes | Performed against the project SA plan (07 section 15; this template as its tasking part) with the SWEHB quotations of NASA-STD-8739.8B | NASA-STD-8739.8 part: `rmm.json` SWE-022 T (standard not in the corpus; owner-accepted at SRR decision 8) | none |
| swe-013 7.1 task 1 | SC | Yes | Expected content present: the SWE-to-task table per 07 section 2.1.1 product type (all eight Yes rows, INSP-032 "Every case named"), SWE-134 a to l (section C; paraphrases checked against `npr-7150-2d/03-chapter3.md` lines 189 to 211, none changes an item's scope), hazard traceability (section D), peer review and CM (section E), metrics (section F); tailoring for Class A with the T rows SWE-022 and SWE-023 cited, both verified T in `rmm.json`. Gaps: finding-1 (SWE-023 implementation commitment), finding-2 (own routing) | | finding-1, finding-2 |
| swe-013 7.1 task 2 | SC | Yes | The template is the 07 section 15 row "5.17 item 13" closure: SWEHB 5.17 item 13 asks for the NPR requirements to be implemented and the associated tasking; section B plans the section 7.1 tasking per product type in the form of SWEHB topic 8.15 (8.15 lines 26 to 44, tasking checklist per SWE and milestone). The plan text that must record the closure is finding-3 | | finding-3 |
| swe-024 7.1 task 1 | SC | Yes | Assessed for NPR 7150.2 compliance: every cited SWE and task exists (INSP-032: 61 SWE pages, every task number; this record spot-checked the `plans` row SWEs 013, 024, 039, 121, 125, 139 and 087 against their section 7.1 lists and 8.10 section 6 lines 10 to 16 and 44: numbers and SC marks match). NASA-STD-8739.8 compliance cannot be assessed beyond the SWEHB quotations | NASA-STD-8739.8 part: `rmm.json` SWE-022 T | none |
| swe-024 7.1 task 2 | SC | Yes | Corrective actions closed with rationale: INSP-032 finding-1 (Major) Verified at iteration 2 on blob `5b135285` with a per-part check table; INSP-032 findings 2 and 3 carried as liens with owner and due event | | none |
| swe-024 7.1 task 3 | SC | No | The change of commitment (checklist moves from due to existing) is recorded in CR-012 and 08 section 3.5 (blob `56c54011` line 154 "Exists (written 2026-09-27, WP-PDR-03)"), but the SA plan text 07 section 15 is left to an untracked follow-on | | finding-3 |
| swe-039 7.1 task 7 | | Yes | The findings table (one row per discrepancy, owner ruling column), SA-F1 (assurance concerns to the register with tag `assurance`) and SA-F3 (package "Software assurance findings" section) keep the list of SA discrepancies, risks and concerns | | none |
| swe-039 7.1 task 8 | SC | Yes | Owner ruling column transcribed by Claude (01 section 10.1); Deferred findings become `RID-<REVIEW>-NNN` citing the record; Minor findings after APPROVED become liens (completion criteria, line 214) | | none |
| swe-121 7.1 task 1 | SC | Yes | The two tailored rows the template relies on (SWE-022, SWE-023) carry the owner's approval (`rmm.json` `tailoring_rationale`: SRR decision 8, owner ruling 2026-09-26); the template cites no tailoring that is not in `rmm.json` | | none |
| swe-121 7.1 task 2 | SC | N/A | A tailoring matrix of NASA-STD-8739.8 requirements cannot be developed without the standard. The template states this relief for `swe-125` task 2 but not for `swe-121` task 2 in the `plans` row; the relief is on record in `rmm.json`, so SA-B2 is met for a reviewer who reads that row. Noted, not a finding | `rmm.json` SWE-022 T | none |
| swe-125 7.1 task 1 | SC | Yes | `docs/process/rmm.json` is maintained (blob `e326ddd1` at `main` HEAD) and every disposition the template cites matches it: SWE-022 T, SWE-023 T, SWE-036 FC, SWE-068 FC, SWE-192 FC, SWE-015 T, SWE-151 T, SWE-016 T, SWE-174 NA (Python read of the rows) | | none |
| swe-125 7.1 task 2 | SC | N/A | As stated in the template's `plans` row | `rmm.json` SWE-022 T | none |
| swe-139 7.1 task 1 | SC | Yes | The template applies the Class A and safety-criticality split of 07 sections 2.1.1 and 14.1 (`criticality` field, section C gate on safety-critical or mission-critical, section B `code` row "every file of a safety-critical or mission-critical component, and every file that contains `unsafe`", equal to 07 line 121) | | none |
| swe-087 7.1 task 3 | | Yes | This record: peer review of a software assurance plan part | | none |
| swe-090 7.1 task 1 | | Yes | SA-F2 supplies MSR-20 (findings by severity and state, including the assurance counts) and MSR-21 (effort) of 07 section 11.2 lines 519 and 520, rolled up per 07 section 10.3 line 457; the front matter carries `assurance_findings_*`, `items_no`, `effort_*` | | none |
| swe-154 7.1 task 1, swe-156 7.1 task 1, swe-159 7.1 tasks 1 and 2 | | N/A | The `plans` row applies them "for the cybersecurity section (07 section 16)"; the template has no cybersecurity section (INSP-032 CK-REQ-G5 N/A) | 07 section 16 (the cybersecurity section is in 07, not in this product) | none |
| `plans` sub-lists for 07, 03, 05, the V&V plan and TS-002 (swe-036, swe-020, swe-176, swe-205, swe-079 to swe-085, swe-187, swe-065 part a, swe-071, swe-191, swe-192, swe-033, swe-027) | mixed | N/A | Each sub-list applies only to the document it names; this product is none of them. SWE-036 (07 section 1.3) is not implemented by the template | 07 section 2.1.1 row "Software plans" (the named documents) | none |
| swe-023 7.1 task 1 | SC | No | The template implements the SA reviewer's part of SWE-023 as tailored, but omits the PAT-006 and PAT-007 commitment and the interim substitution of `rmm.json` SWE-023 and plans the task only at requirements review | Standard's own list: `rmm.json` SWE-023 T | finding-1 |
| swe-088 7.1 task 1 | | Yes | NPR 7150.2D 5.3.3 a to d for reviews held with this template: a checklist (sections A to F), readiness and completion criteria (R1 to R4; completion criteria line 214), action tracking (findings table states and RIDs), required participants (SA-A2, the three distinct invocations; `assurance_reviewer_agent` form accepted by `tools/validate_docs.py`) | | none |
| swe-088 7.1 task 2 | | Yes | Actions resolved: findings stay Open until Claude re-reads the fixed blobs and marks them Verified (line 214); SA-E1 | | none |
| swe-089 7.1 task 1 | | Yes | Front matter carries the SWE-089 fields (finding counts by severity and state, `effort_turns`, `effort_minutes`, `iteration`), and SA-E2 checks both records | | none |

Not applied, with reason: `swe-088` task 3 (audit of the peer-review process) is a process audit, not a product review task; the section 7.1 tasks of SWE-134 other than 5, SWE-205, SWE-052, SWE-184, SWE-192, SWE-219 and SWE-220 are tasks the template plans for other product types, not SWEs this product implements (it cites them as governing the reviews it plans).

## Readiness criteria

| # | Criterion | Result | Evidence |
|---|---|---|---|
| R1 | Product committed and frozen; `product_files` equal to the paired record's | Yes | `git ls-tree 7784672` gives the four branch blobs of `product_files`; `git rev-parse 4552943:docs/cm/cr/CR-012-pdr-checklist-templates.md` gives `91c8c626`; the list is character for character the INSP-032 list |
| R2 | 07 section 2.1.1 row and criticality identified | Yes | `product_type: plans`, `criticality: neither` (07 line 117, row "Software plans", Yes in every column; the template belongs to no 07 section 14.1 component). The row is inferred: finding-2 |
| R3 | `tools/validate_docs.py` exits 0 on the product's files; traceability clean for the ids touched | Yes | `/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/validate_docs.py --root <git archive export of 7784672> --quiet`: exit 0. This record, filled from the template, also passes on `main` (see "Validation"). Traceability: the product touches no REQ, TC or HZ id (CR-012 section 4 "Requirements and traceability: None", confirmed by `git diff --stat 573f9f5 7784672`: four files, all templates or 08), so no `--report-only` run is needed and none was made |
| R4 | Paired file review filed under its own invocation; this reviewer independent | Yes | INSP-032 filed (`5f57f93` iteration 1, `091bceb` iteration 2); `author_agent` "author:WP-PDR-03 (Claude as checklist owner)", `reviewer_agent` "reviewer:WP-PDR-03-templates"; this invocation is neither |

## A. Dispatch, independence and record integrity

| Id | Answer | Evidence |
|---|---|---|
| SA-A1 | Yes, with finding-2 | Row "Software plans" of 07 section 2.1.1 (line 117), Yes for criticality neither; the template is the SA plan's tasking part (07 section 15 row "5.17 item 13", line 672); SWEHB `swe-087` 7.1 task 3. The row does not name the template (finding-2) |
| SA-A2 | Yes | Three invocations: author:WP-PDR-03, reviewer:WP-PDR-03-templates, sa-reviewer:WP-PDR-03-templates; recorded in both records (INSP-032 names the SA pair as "not yet assigned"; the software lead updates it, see "Record verdict") |
| SA-A3 | Yes | Same `product` and the same five blobs as INSP-032 iteration 2; no product change after `7784672` (`git log --oneline -3 cr/CR-012-pdr-checklist-templates` head is `7784672`) |
| SA-A4 | Yes | INSP-032 used `peer-review-checklist-requirements.md` revision C section G and CK-REQ-A8, the checklist 07 section 2.1.1 row "Software plans" and 08 section 3.5 assign to plans, and answered every item with evidence (G1 to G8, A8; G5 N/A with reason); `swe-088` 7.1 task 1 criteria a to d met by that record |

## B. SWE-to-task table

| Id | Answer | Evidence |
|---|---|---|
| SA-B1 | Yes | Every task of the `plans` row, of "Every product type" and of the SWEs the product implements (SWE-022, SWE-023, SWE-088, SWE-089) is in the task table; `assurance_tasks_applied` lists every Yes and No row |
| SA-B2 | Yes | Every N/A row cites `rmm.json` SWE-022 T, 07 section 16 or 07 section 2.1.1; criticality is neither, and no SC task is N/A without relief |
| SA-B3 | Yes | The two No rows carry finding-1 and finding-3 |

## C. SWE-134 items a to l

N/A for this product (`criticality: neither`; 07 section 2.1.1 row "Software plans"). `swe134_items_checked` is empty. The template's own section C text was checked item by item against NPR 7150.2D 3.7.3 (`docs/references/md/npr-7150-2d/03-chapter3.md` lines 189 to 211) as part of `swe-013` task 1: each of SA-C-a to SA-C-l keeps the item's scope; item d drops "of software functions" from the heading but its check ("Every override of the component") keeps the scope.

## D. Software safety analysis and hazard traceability

| Id | Answer | Evidence |
|---|---|---|
| SA-D1 to SA-D6 | N/A | The product belongs to no 07 section 14.1 component and changes no hazard, control, component or requirement (CR-012 section 4 rows "Safety" and "Requirements and traceability": None; `git diff --stat 573f9f5 7784672` touches only the three templates and 08). Relief: 07 sections 2.1.1 and 14.1 (section D applies to the product's component) |

## E. Peer review, change and configuration assurance

| Id | Answer | Evidence |
|---|---|---|
| SA-E1 | Yes | INSP-032 finding-1 (Major) Verified at iteration 2 against blob `5b135285` part by part; findings 2 and 3 liened with owner and due event; none closed without evidence |
| SA-E2 | Yes | INSP-032 and this record carry the SWE-089 fields (INSP-032: 32 turns, 55 minutes cumulative, 1 Major, 2 Minor) |
| SA-E3 | No | `7784672` carries a parsed `CR: CR-012` trailer; `ac9b7a5` does not (finding-4). CR-012 is on `main` with `Refs: CR-012` (`02e5d49`, `4552943`); nothing is merged before the owner's disposition (CR-012 section 5 step 6) |
| SA-E4 | N/A | Test and code rows only (template line 202); this product is a plan |

## F. Assurance risks, metrics and reporting

| Id | Answer | Evidence |
|---|---|---|
| SA-F1 | Yes | The one assurance concern that is not a product defect, that PAT-006, PAT-007 and NASA-STD-8739.8 are not in the corpus (owner permission OD-21 not given), is carried by the existing RSK-009 (`docs/risk/register.json`, "SWEHB corpus incomplete or garbled for applicable SWE rows", Mitigating) and by the residual risk of `rmm.json` SWE-022 and SWE-023, as PDR work plan OD-21 states; no new entry is submitted |
| SA-F2 | Yes | Front matter: `findings_*`, `assurance_findings_*`, `items_no`, `effort_turns`, `effort_minutes` |
| SA-F3 | Yes | Verdict, four Minor liens, tasks applied and reliefs used are in this record alone |

## Section G of the checklist of record (`peer-review-checklist-requirements.md` revision C): concurrence with INSP-032

The file review answered section G; this record does not re-answer it and concurs with each answer: G1 No (INSP-032 finding-3; finding-1 Verified), G2 No (INSP-032 finding-2), G3 Yes, G4 Yes, G5 N/A, G6 Yes, G7 Yes, G8 Yes, A8 Yes. Additional assurance evidence for G4: the reliefs the template cites were re-read in `rmm.json` (task table, `swe-125` task 1). For G1: this record's finding-1 (template against `rmm.json` SWE-023) and finding-3 (template against 07 section 15 after merge) are further disagreements with governing documents, both Minor.

## Validation

`/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/validate_docs.py` on `main` with this record: the record passes; the run exits 1 on the pre-existing SRR record drift of `docs/reviews/SRR/checklists/tool-validation-tv-001-to-tv-010.md` (present before this record, not caused by it). A copy of this record with `checklist: peer-review-checklist-software-assurance` and `checklist_revision: A`, placed in the export of `7784672`, also passes `validate_docs.py --root <export>`, which shows that the template yields a valid paired record once CR-012 merges.

## Record verdict

The assurance reviewer's verdict is APPROVED with four Minor liens (finding-1 to finding-4, due the CDR readiness declaration; finding-3 and finding-4 recommended before the CR-012 merge and F1). No Major finding is open. The record `verdict` stays NEEDS CHANGES under the lead SE convention of 2026-09-27: the reviewed blobs exist only on `cr/CR-012-pdr-checklist-templates`. The software lead sets `verdict: APPROVED` on this record and on INSP-032 in the CR-012 merge commit, or the commit right after it, when the blobs reach `main` unchanged; before that, the INSP-032 reviewer updates INSP-032 with `paired_record: INSP-046`, `assurance_reviewer_agent` naming this invocation and `assurance_verdict: APPROVED` (07 section 10.2 Record row; each reviewer updates only its own record).

```
ASSURANCE VERDICT: APPROVED (record verdict held NEEDS CHANGES: branch-only blobs, lead SE convention 2026-09-27)
PRODUCT: docs/templates/peer-review-checklist-software-assurance.md@5b135285 (and the four INSP-032 blobs) at 7784672; PAIRED RECORD: INSP-032
PRODUCT TYPE: plans; CRITICALITY: neither
FINDINGS:
- [Minor] finding-1 swe-023 7.1 task 1: rmm.json SWE-023 PAT-006/PAT-007 commitment and interim SWE-134 substitution absent; task planned only in the requirements row.
- [Minor] finding-2 SA-A1: plans row and 07 section 2.1.1 do not name the SA checklist itself.
- [Minor] finding-3 swe-024 7.1 task 3: 07 section 15 follow-on named in CR-012 section 4 but carried by no WP or due event.
- [Minor] finding-4 SA-E3: ac9b7a5 CR and Refs trailers not parsed; CR-012 section 8 says yes.
TASKS APPLIED: swe-134 7.1 task 5, swe-022 7.1 task 1, swe-013 7.1 tasks 1 and 2, swe-024 7.1 tasks 1 to 3, swe-039 7.1 tasks 7 and 8, swe-121 7.1 task 1, swe-125 7.1 task 1, swe-139 7.1 task 1, swe-087 7.1 task 3, swe-090 7.1 task 1, swe-023 7.1 task 1, swe-088 7.1 tasks 1 and 2, swe-089 7.1 task 1
TASKS N/A (relief): swe-121 7.1 task 2 and swe-125 7.1 task 2 (rmm.json SWE-022 T); swe-154, swe-156, swe-159 (07 section 16); plans sub-lists for 07, 03, 05, V&V plan, TS-002 (07 section 2.1.1)
SWE-134 ITEMS CHECKED: none (criticality neither)
MEASUREMENTS: size=1 template, 229 lines; tasks=18 applied, 6 N/A rows; tasks_no=2; turns=30; minutes=50; major=0; minor=4
```

## Iteration 2: re-pin delta on the combined 08 blob and the CR-012 file (2026-09-29, `main` `1404c67`, branch heads `7784672` and `7efd900`)

**Why.** CR-012 section 9 (pre-merge check 2 and the independent verification, pre-merge part) found that this record is the only CR-012 step 3 record that fails the verdict trial. It pins 08 at `56c54011`, which CR-015 replaces with `374fd777`. It also pins the CR-012 file at `91c8c626`, which later lifecycle steps changed (now `37ca884b`). The paired file review INSP-032 was re-pinned at its iteration 3 (`0142ad4`) and now names four blobs that differ from this record's five. That breaks R1 and SA-A3 of the pair. Lead SE ruling (2) of 2026-09-29 governs the CR file: the re-pin drops it when the CR sections this record reviewed are unchanged, and otherwise the reviewer makes a delta.

**Scope (rule C1).** A delta. The three template blobs are unchanged: `git rev-parse 7efd900:<path>` gives `5b135285`, `7be809d4` and `0386cc6e`, equal to `7784672`, and `git log 573f9f5..1404c67` on the four product paths is empty. The product of this record, the software assurance template, is therefore not re-reviewed. The delta reads two things under the assurance lens: (a) the six CR-015 hunks of 08 (`git diff 56c54011 374fd777`); and (b) the hunks of `git diff 91c8c626 37ca884b` in the CR-012 sections this record reviewed (section 4, section 8 and section 9, and the section 5 step that governs this record). It states the current state of finding-1 to finding-4. Checklist as at iteration 1.

**Independence (rule C4) and search first.** This is a new invocation of this record's software assurance reviewer role (07 section 2.1.1), `sa-reviewer:WP-PDR-03-templates`. It authored no part of CR-010, CR-012, CR-013 or CR-015 or their branch commits. It authored none of their record deltas (INSP-031 to INSP-033 iterations 1 to 3, INSP-022, INSP-060) and no part of CR-012 section 9. It edited no product file. `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any `grep`, with three queries: "INSP-050 CR-010 software assurance record product_files findings_open"; "INSP-060 drops CR file from product_files reason record-text edits drift"; "findings_open counts liens Minor findings ride with APPROVED lesson L1 findings_open 0". After that, `git`, `grep -n` and `tools/check_commit_msg.py` were used only to pin lines, blobs and trailers.

### The six CR-015 hunks of 08 (`56c54011` to `374fd777`, 14 insertions, 13 deletions), read under the assurance lens

| Hunk | 08 location at `374fd777` | Bears on the software assurance template? | Result |
|---|---|---|---|
| 1 | Header, line 3 | No. It names the CRs that change 08 and the SRR baseline blob | No effect |
| 2 | Section 1 repository map (lines 21 to 33) | Yes, in part. The `docs/templates/` line now lists `peer-review-checklist-software-assurance.md` with the other checklists, and it says "every checklist exists" | Agrees with the section 3.5 row that CR-012 sets to "Exists" (line 155). No effect on a finding |
| 3 | Section 3.1, lines 82 and 83 | Yes. Trade studies get their own row, with "the SA pair where 07 section 2.1.1 says Yes" | Agrees with the template's `trade-study-or-adr` row, which plans the pair where the decision constrains a 07 section 14.1 component. It widens no dispatch the template relies on |
| 4 | Section 3.2 reviewer block, lines 112 and 113 | Yes. A Minor finding rides with APPROVED as a record lien (01 section 12.3). Blobs are named as `path@blob`. The verdict is held while a record reviews blobs on a branch only | The held-verdict and `path@blob` rules agree with the template's completion criteria and R1. The lien rule does not match the template's Minor-finding clause (line 214). That mismatch is INSP-031 finding-3 (Minor, lien). This record concurs and does not raise it again |
| 5 | Section 3.5 "Review record" paragraph, line 162 | No. The slug follows 01 section 13 | The record form of this template (`<product-slug>-software-assurance.md`) is the 01 section 13 paired form. No effect |
| 6 | Section 4 assignment block, line 174 | No. The REVIEW RECORD line asks for frozen blobs and the branch name | Agrees with template R1. No effect |

The 11 lines CR-012 adds to 08 are present unchanged at `374fd777`, including the section 3.5 row for this template (line 155). None of the 9 lines CR-012 removes comes back. This agrees with INSP-031 iteration 3 and CR-012 section 9 and was re-checked here against `git show 7efd900:docs/process/08-agent-briefing.md`. No new finding.

### The CR-012 file (`91c8c626` to `37ca884b`; dropped from `product_files`)

At iteration 1 this record read CR-012 where it bears on the software assurance template: section 4 (the impact fields, above all Documentation and Safety), section 8 (the implementation record) and section 9 (verification). `git diff 91c8c626 37ca884b` (188 insertions, 22 deletions) changes the following:

| CR-012 location | Change | Effect on this record |
|---|---|---|
| Front matter; lead paragraph | `status`, `disposition` (Approved 2026-09-28), `disposition_date` | None |
| Section 4, rows Safety, Software classification and tailoring, Documentation | Unchanged | finding-3 unchanged. The Documentation row still names the 07 section 15 follow-on "for their writers", with no work package and no due event |
| Section 4, rows Verification and Schedule; section 4.1 (new) | The records already made against revision A are listed with the rule for each disposition. This record is listed with its `checklist` field `peer-review-checklist-requirements` and `assurance_checklist`, record verdict held | Correct for this record. Revision A is approved unchanged, so this record stands on the blob that merges |
| Section 5, step 5 text and step 8 (new) | After the merge, every section 4.1 record is re-issued with `checklist: peer-review-checklist-software-assurance` revision A and the merged blob, including this record by its assurance reviewer | This is the switch that iteration 1's front matter notes ("the delta after CR-012 merges switches the field"). It is not done here, because the template is not yet on `main`. It is done at step 8 |
| Section 8 | The trailer cells of `ac9b7a5` and `7784672` now state that the `CR:` and `Refs:` lines are in the message body only, and that `tools/check_commit_msg.py` fails both commits (`ac9b7a5`: REFS_MISSING and CR_TRAILER_MISSING; `7784672`: REFS_MISSING). The cells cite `docs/cm/deviations.md` entry 8 (`c9f611d`) and entry 9 (`48f596a`). The lead SE accepts this correction of record, the branch is not rewritten, and the owner decides entries 8 and 9 at S1 | finding-4 Verified (below). `tools/check_commit_msg.py --range 573f9f5..7784672` run here reproduces the same three failures |
| Section 9 | Pre-merge check 2 and the independent verification, pre-merge part. Row 3 ("Filled templates validate") is Verified on the trial CR-012 merge, with a filled copy of the software assurance template for 07 (product type plans) at NEEDS CHANGES and at APPROVED. INSP-046 is named as the only failing record in the verdict trial | Row 3 is assurance evidence that the template yields a valid record once merged. The failing-record item is closed by this delta |
| Sections 6.1, 6.2, 7, 10 and 11 | Impact reviews, disposition, closure and history | Not reviewed by this record |

Sections 1, 2 and 3 of CR-012 are unchanged. After this delta, the CR-012 sections this record reviewed have been read up to `37ca884b`. Their later changes will be record text of the CM steps: section 8 step state, the section 9 post-merge part and sections 10 and 11. The CR file is therefore dropped from `product_files`, as it is from INSP-032, and is identified here as reviewed at `91c8c626`, with the delta read up to `37ca884b`. A later change to CR-012 sections 1 to 5 needs a delta of this record.

### SA-E3 re-answered

| Id | Answer | Evidence |
|---|---|---|
| SA-E3 | Yes | CR route: this CR file is on `main` with `Refs: CR-012`, and nothing merges before the disposition and the section 9 checks. `7784672` and `ac9b7a5` still fail the commit-message checker. They are not rewritten, because the step 3 reviews froze them (plan rule C2). The nonconformance is now recorded truthfully in CR-012 section 8 and carried by `docs/cm/deviations.md` entries 8 and 9 for the owner's S1 decision (lead SE ruling (7) of 2026-09-29). That meets the configuration assurance aim of the item, which is that no departure from 05 section 4.5 goes unrecorded. The owner's decision on entries 8 and 9 does not hold this record |

### Findings (iteration 2; current state of every finding of this record)

| Finding | Severity | State | Disposition |
|---|---|---|---|
| finding-1 | Minor | Lien: fix before CDR | Template blob `5b135285` is unchanged: the `design` and `code` rows still do not carry `swe-023` task 1, and PAT-006 and PAT-007 are not named. Owner: Claude as checklist owner. Due: the CDR readiness declaration (plan rule C1) |
| finding-2 | Minor | Lien: fix before CDR | Unchanged. The `plans` row of `5b135285` and 07 section 2.1.1 (at `main` and at CR-013 `0ad37a43`) do not name the software assurance checklist itself. Owner: Claude as checklist owner, with the 07 author. Due: the CDR readiness declaration |
| finding-3 | Minor | Lien: fix before CDR | Unchanged. The 07 section 15 lead paragraph still says "the four checklists of section 10", and row "5.17 item 13" still reads "Partial at SRR" (lines 658 and 672 at `0ad37a43`; the same at `main`). The CR-012 section 4 Documentation row and section 5 name no work package or due event for this follow-on. Owner: the next 07 writer of plan section 5.3. Due: the CDR readiness declaration |
| finding-4 | Minor | Verified | Fixed in the record text. CR-012 section 8 no longer says "yes": it states that the trailers are not parsed, gives the checker's failure codes and cites deviations entries 8 and 9. The deviations register now does the job that the fix asked the CSA to do: it lists both commits for the PDR independent reviewer and the owner's S1 decision. Re-checked with `tools/check_commit_msg.py --range 573f9f5..7784672` (FAIL, the three codes) |

Open Major: 0. Open Minor: 0 (finding-1 to finding-3 are liens; finding-4 is Verified). New findings in this delta: 0. INSP-031 finding-3 is concurred with and not raised again.

### Checks run

- Blobs: `git rev-parse 7efd900:<path>` and `git rev-parse <trial merge>:<path>` both equal the four `product_files` entries. They are character for character the INSP-032 iteration 3 list (R1, SA-A3), and `product_commit` equals INSP-032's `7efd900`. `git merge-base --is-ancestor 7784672 7efd900` is true.
- 08: `git diff --word-diff -U0 56c54011 374fd777` (6 hunks). The CR-012 lines of 08 were checked against `git show 7efd900:docs/process/08-agent-briefing.md`.
- CR-012 file: `git diff --stat` and `git diff --word-diff 91c8c626 37ca884b` in sections 4, 5, 8 and 9. `tools/check_commit_msg.py --range 573f9f5..7784672` gave 3 FAIL lines, the same as section 8.
- `tools/validate_docs.py` on `main` with this delta in the working tree: this record PASSES. Drift of the branch-only blobs is printed as notes, as expected for a held verdict.
- Verdict trial: a detached scratch worktree of `main` at `1404c67`, then a trial `git merge --no-ff 7784672` (CR-012) followed by `git merge --no-ff 7efd900` (CR-015). There, `git rev-parse HEAD:<path>` gives the four `product_files` blobs. With this record copied in at `verdict: APPROVED`, this record PASSES with no drift note, and `validate_docs.py` reports 117 passed, 0 failed. With INSP-032 also at `verdict: APPROVED`, both PASS and the result is still 117 passed, 0 failed. Negative control: the iteration 1 text at `verdict: APPROVED` FAILS on its two old pins (08 `56c54011` differs from `374fd777`; CR-012 `91c8c626` differs from `37ca884b`). The worktree was removed and no ref was kept.

### Record verdict (iteration 2)

**`reviewer_verdict: APPROVED`, `assurance_verdict: APPROVED`**, unchanged. The liens are finding-1 to finding-3 (Minor, due the CDR readiness declaration), and finding-4 is Verified. The record `verdict` stays **NEEDS CHANGES** under the lead SE convention: 08 `374fd777` and the three template blobs reach `main` only when both CR-012 and CR-015 have merged. The software lead sets `verdict: APPROVED` on this record and on INSP-032 in the CR-015 merge commit, or in the commit right after it. If CR-017 (batch 2) later re-blobs 08, both records need a further delta first. After the CR-012 merge, section 5 step 8 re-issues this record's `checklist` field.

```
DELTA ITERATION 2 (2026-09-29): ASSURANCE VERDICT: APPROVED (unchanged); record verdict held until the CR-015 merge commit (CR-012 merged first)
PRODUCTS: templates 5b135285, 7be809d4, 0386cc6e (unchanged); 08 56c54011 -> 374fd777 (CR-015 head 7efd900); CR-012 file dropped (reviewed at 91c8c626; sections 4, 5, 8, 9 read to 37ca884b); equal to INSP-032 iteration 3
CHECKS: 6 CR-015 hunks of 08 read under the SA lens; 11 CR-012 lines of 08 present, 9 removed lines not restored; SA-E3 re-answered Yes
FINDINGS: finding-4 Verified (CR-012 section 8 correction; deviations entries 8 and 9); finding-1 to finding-3 Minor liens due CDR; new findings 0; open Major 0
MEASUREMENTS: hunks=6 (08) plus 4 sections (CR file); items re-answered=1; iteration 2 turns=20, minutes=35; cumulative turns=50, minutes=85
```
