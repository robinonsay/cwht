---
# Peer-review record front matter (charter sections 2 and 5; docs/process/01-lifecycle-and-reviews.md
# section 13; docs/process/07-software-engineering-plan.md sections 2.1.1, 10.2 and 15). This is the
# paired software assurance record of INSP-039 (docs/reviews/PDR/checklists/cm-plan-05.md, the file review
# of CR-007 against the software CM plan 05), the record path PDR work plan WP-PDR-05 "Records" names.
# Checklist applied: docs/templates/peer-review-checklist-software-assurance.md revision A as on its CR-012
# branch (cr/CR-012-pdr-checklist-templates at 7784672, blob 5b135285; CR-012 Submitted, not merged).
# tools/validate_docs.py requires the checklist field to name a template that exists on main, so the field
# names peer-review-checklist-requirements revision C (section G and CK-REQ-A8, the route 08 section 3.5
# gives plans, the form of the SRR pair INSP-030) and checklist_software_assurance records the template
# actually applied; the delta after CR-012 merges switches the field (as INSP-040 cross item X-1 does).
# Every product_files blob equals the paired record's list and git rev-parse HEAD:<path> at d566e01.
id: INSP-047
checklist: peer-review-checklist-requirements
checklist_revision: C
checklist_software_assurance: "docs/templates/peer-review-checklist-software-assurance.md@5b13528504868b2add0f0b1e329c63aa2b54cdf4 (revision A, CR-012 branch head 7784672)"
checklist_file: docs/reviews/PDR/checklists/cm-plan-05-software-assurance.md
product: docs/cm/cr/CR-007-cm-plan-pdr-rows.md
# delta iteration 2 (2026-09-29): product_commit is 7668322, the last commit of the CR file on main (revision 4,
# status Implemented); iteration 1 value "9032a02a37e5bcf5f7f766bf2458af5f82fa5680"
product_commit: "7668322aaae2df9892ea5102ec4a5bea857708ce"
# delta iteration 2: the CR file entry 92b200ad (revision 1) is replaced by abec03c5 (revision 4), equal to
# git rev-parse HEAD:<path> and git hash-object at main dd7b976; every hunk of git diff 92b200ad abec03c5 is verified
# (section "Delta iteration 2"). The entry "docs/lessons-learned.md@ec30a264fdef25ff291ddad5b1ebebbed8f9dee9" is dropped
# (re-pin, precedent INSP-060 in fd12ced and INSP-034 in 23e2388): the file is an append-only log outside the assurance
# scope (iteration 1 Product paragraph: an input to the INSP-039 workspace note), and its only change since, entry 18 at
# 391f0e5 with its tag-index row, bears on nothing this record reviewed. The other six blobs equal HEAD.
product_files: ["docs/cm/cr/CR-007-cm-plan-pdr-rows.md@abec03c5d593d0dff16428fe1f447419865fae10", "docs/reviews/PDR/package.md@967117cff3521ad00c59ba33a81de3e6381850e9", "docs/reviews/PDR/rfa-rid-log.json@7b2860b209db8582356bb38e0e168cc28d2107ed", "docs/reviews/PDR/checklists/.gitkeep@e69de29bb2d1d6434b8b29ae775ad8c2e48c5391", "docs/reviews/PDR/figures/.gitkeep@e69de29bb2d1d6434b8b29ae775ad8c2e48c5391", "docs/reviews/PDR/slides/.gitkeep@e69de29bb2d1d6434b8b29ae775ad8c2e48c5391", "docs/process/configuration-status.md@07909eb643e44f5e57dff38c3a30de1a4099df4f"]
# inputs read (not reviewed), blobs at HEAD d566e01: 05 (equal to baseline/srr), rmm.json, the VDD template,
# 07, allocation schema, TV-012, the SRR pair INSP-030
input_files: ["docs/process/05-configuration-and-data-management.md@f8de2081f7542ed0bbe47897d8b63e845b8c3114", "docs/process/rmm.json@e326ddd1b7296d7d7fe172be6f33535cee3192d7", "docs/templates/version-description.md@030e8865c656ea0924ecd0196e7e1c6076bede3d", "docs/process/07-software-engineering-plan.md@bfe05f4327e79fa15c24d2cf8c14249804f946a8", "docs/reviews/PDR/checklists/cm-plan-05.md@886bf23b8cab446bb48329479b6b0878bdbf0a6e", "docs/process/07-software-engineering-plan.md@e11abe3096ba85231ee94496e8b94cd59cc36a2a (delta iteration 2, branch cr/CR-007-cm-plan-pdr-rows at f68e47a, section 2.1.1 read for finding-2 and finding-3)", "docs/plan/status/status-2026-09-28.md@b95bd8df6b50bb6a631da07380a404b91e2df6c7 (delta iteration 2, section 4, the owner's option B condition)", "docs/cm/cr/CR-007-cm-plan-pdr-rows.md@ee11ec70e70a9f8eea2611a9c2f0b59e62415369 (delta iteration 2, revision 3 as at 65331c6, for the revision 4 word diff)"]
paired_record: INSP-039
product_type: plans
criticality: neither
# product_size: iteration 1 value "1 CR, change items C1 to C16 against 05 ..."; delta iteration 2 on revision 4
product_size: 1 CR at revision 4 (507 lines), change items C1 to C16 against 05 (16 sections, Table 4-1 55 rows, Table 4-2), rmm.json 3 rows, 2 templates, and C17 (a) to (g) against 07; delta 92b200ad..abec03c5, 304 insertions and 43 deletions
sprint: PDR-prep
author_agent: "author:WP-PDR-05 (Claude, CM function)"
reviewer_agent: "sa-reviewer:WP-PDR-05-cm-plan-05"
assurance_required: true
assurance_reviewer_agent: "sa-reviewer:WP-PDR-05-cm-plan-05 (software assurance function; paired file review INSP-039 by reviewer:WP-PDR-05 (independent reviewer, CM lens))"
# iteration 2: the delta on CR-007 revision 4 (abec03c5), section "Delta iteration 2" at the end
iteration: 2
readiness_met: true
# reviewer_verdict and assurance_verdict: APPROVED; 0 Major, 3 Minor (rule C1: Minor findings ride with the
# first APPROVED verdict and become liens if not fixed in the CR revision before OD-36)
# delta iteration 2: APPROVED on abec03c5; finding-1 to finding-3 not fixed by revisions 2 to 4, now liens due the CDR
# readiness declaration (rule C1); new Minor finding-4 and finding-5, liens; 0 Major
reviewer_verdict: APPROVED
assurance_verdict: APPROVED
# verdict: APPROVED. Both reviews of the product are APPROVED (INSP-039 reviewer_verdict APPROVED; this record),
# readiness met, no Major open, and every product blob is on main (the lead SE branch-only convention does not
# apply: only the checklist template is branch-only). INSP-039 still reads assurance_verdict NEEDS CHANGES and
# no paired_record; its reviewer updates it to name INSP-047 (07 section 10.2 Record row; cross item X-1)
# delta iteration 2: verdict held at NEEDS CHANGES (iteration 1 value APPROVED). The paired file review INSP-039 is
# reviewer APPROVED on CR blob 22c4455f (revision 2) only, and revisions 3 and 4 have no file review yet; 07 section
# 10.2 sets neither record to APPROVED until both reviews are APPROVED, so this record waits for the INSP-039 delta on
# abec03c5 (cross item X-4), as INSP-039 iteration 2 waits for this one. The software lead then sets verdict: APPROVED
# on both records if that delta is APPROVED and the blobs agree.
verdict: NEEDS CHANGES
findings_major: 0
findings_minor: 5
findings_open: 5
findings_fixed: 0
findings_verified: 0
findings_deferred: 0
assurance_findings_major: 0
assurance_findings_minor: 5
assurance_tasks_applied: ["swe-134 7.1 task 5", "swe-022 7.1 task 1", "swe-013 7.1 task 1", "swe-024 7.1 task 1", "swe-024 7.1 task 2", "swe-024 7.1 task 3", "swe-039 7.1 task 7", "swe-039 7.1 task 8", "swe-121 7.1 task 1", "swe-125 7.1 task 1", "swe-139 7.1 task 1", "swe-087 7.1 task 3", "swe-090 7.1 task 1", "swe-079 7.1 task 1", "swe-080 7.1 task 1", "swe-080 7.1 task 2", "swe-080 7.1 task 3", "swe-081 7.1 task 1", "swe-081 7.1 task 2", "swe-082 7.1 task 1", "swe-082 7.1 task 2", "swe-083 7.1 task 1", "swe-084 7.1 task 1", "swe-085 7.1 task 1", "swe-085 7.1 task 2", "swe-187 7.1 task 1", "swe-187 7.1 task 2", "swe-063 7.1 task 1", "swe-063 7.1 task 2", "swe-136 7.1 task 1", "swe-200 7.1 task 1"]
swe134_items_checked: []
deferred_rids: []
# items_no: delta iteration 2 adds "swe-080 7.1 task 2" (finding-4, finding-5); iteration 1 value
# [SA-A1, SA-E1, "swe-063 7.1 task 1", "swe-081 7.1 task 2"]
items_no: [SA-A1, SA-E1, "swe-063 7.1 task 1", "swe-081 7.1 task 2", "swe-080 7.1 task 2"]
# effort: iteration 1 (34 turns, 55 min), delta iteration 2 (28, 45)
effort_turns: 62
effort_minutes: 100
record_status: Open
date: 2026-09-27
date_closed: null
---

# Peer review record INSP-047: software assurance pair of INSP-039, CR-007 changes to the CM plan 05 (WP-PDR-05 output 3)

**Product.** `docs/cm/cr/CR-007-cm-plan-pdr-rows.md`, blob `92b200ad`, last committed at `9032a02` (status Submitted, Class II), with the seven other blobs of the paired record's `product_files` (WP-PDR-05 outputs 1, 2 and 4 that INSP-039 cites; they are inputs to its workspace note, not the assurance scope). Read against 05 blob `f8de2081` (equal at `HEAD` and at `baseline/srr`), `docs/process/rmm.json` blob `e326ddd1`, `docs/templates/version-description.md` blob `030e8865` and 07 blob `bfe05f43`. Identity checked with `git rev-parse HEAD:<path>` at `d566e01`: all eight blobs equal the paired record's list.

**Checklist.** `docs/templates/peer-review-checklist-software-assurance.md` revision A **as on its CR-012 branch** (`cr/CR-012-pdr-checklist-templates` at `7784672`, blob `5b135285`; not merged). Sections R, A, B, E and F are applied; section C (SWE-134 a to l) is N/A for criticality neither; section D is answered N/A item by item (no hazard or requirement is changed). `product_type` plans (07 §2.1.1 row "Software plans", Yes in every column, 05 named as "the software CM plan"); `criticality` neither (05 belongs to no 07 §14.1 component).

**Acceptance criteria (rule C7).** Every task of the section B row "Every product type" and the row `plans` with its "for 05" list; the section 7.1 tasks of every other SWE the product implements (SWE-063 and SWE-136 through C12 and C16, SWE-200 through the volatility statement); every INSP-030 finding (finding-1 to finding-5) CR-007 claims to close, each part of its fix as INSP-030 states it; the INSP-039 findings re-read under the assurance lens.

**Independence (rule C4).** This invocation authored no part of WP-PDR-05, CR-007 or INSP-039, and edited no product file; it is neither the author (`author:WP-PDR-05`) nor the file reviewer of INSP-039 (`reviewer:WP-PDR-05`). **Search first.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (queries: "INSP-039 WP-PDR-05 peer review record"; "software assurance paired record slug -software-assurance.md 07 section 2.1.1 independent assurance reviewer"; "SWEHB 7.1 Tasking for Software Assurance configuration management plan SWE-079 SWE-080 SWE-081 SWE-082"). `grep -n` and read-only scripts were used afterwards only to pin lines and to extract the section 7.1 lists.

**Relation to CR-007 section 6.** CR-007 C9 and its section 6 lead paragraph ask the software assurance reviewer to review the impact assessment in the CR's own section 6 (plan wave 1a). This record is the SA pair of the file review; it does not fill the CR section 6 slot, and it may serve as that review's input.

## Record

### Findings

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | assurance | Minor | swe-063 7.1 task 1, swe-081 7.1 task 1, SA-E1 | CR-007 C11 (line 98) and C15 (line 118); §4 Documentation row (line 156); front matter `affected_paths` (line 12); `docs/templates/version-description.md` §1 row "Embedded version string" (line 33) and §2 flavour row (line 46) | INSP-030 finding-3 asked for three things: a flavour build identity, "list it in VDD section 2", and rejection of a flavour suffix on a delivered unit. C11 gives the identity (`vX.Y.Z+<short S>.<flavour>`) and the rejection, but no change item touches the VDD template: §1 still states the embedded version string as `vX.Y.Z+<short S>` only, and the §2 flavour row names files, SHA-256 and the Cargo feature but not the embedded version each flavour reports. The VDD is the record against which `picotool info -a` is compared (05 §8.3 step 2, PCA-05, the anomaly contact rule), so for a flavour image the VDD gives no expected identity string, and the SWE-063 confirmation of a correct VDD has no row to check it against. INSP-039 read the flavour hash as already carried (its lien table row INSP-030 finding-3, "VDD §2 already carries each flavour with its SHA-256"), which is true for the hash and not for the identity. Fix: add C15 (c) for `docs/templates/version-description.md` (Table 4-1 row 53): the §2 flavour row (or a §1 row) states "embedded version `vX.Y.Z+<short S>.<flavour>` (`picotool info -a`)"; add the template to `affected_paths` and the §4 Documentation row; C11 (a) then cites it | Open | Pending | |
| <a id="finding-2"></a>finding-2 | assurance | Minor | SA-A1, CK-REQ-G1, swe-134 7.1 task 5 | CR-007 C6 (e) Part B lead paragraph (line 69) and rows 10 and 15 (lines 75, 79); 07 §2.1.1 lead sentence (07 line 112) and table (lines 114 to 123) | 07 §2.1.1 is "the single rule for dispatching the software assurance reviewer". Part B's lead paragraph follows it ("a record whose product is a 07 §2.1.1 "Yes" product needs its software assurance pair"), but rows 10 and 15 then require SA pairs for products that the 07 §2.1.1 table does not list: the ICDs with a software side (`ICD-CTL-SW`, `ICD-TX-SW`, `ICD-PWR-SW`, `ICD-SW-HOST` and any ICD one of whose sides is a 07 §14.1 component) and the hazard analysis (`hazard-analysis.md`, `hazards.json`). The PDR work plan schedules those pairs (WP-PDR-16 line 356, WP-PDR-36 line 611), and SA review of them is well founded (swe-134 7.1 task 5, participation in reviews affecting safety-critical products; swe-081 7.1 task 2, hazard reports and safety analysis), so the defect is not the extra review but a second dispatch rule: after the merge 05 would admit to `baseline/pdr` on SA pairs that 07 does not require, `tools/validate_docs.py` would not require `assurance_reviewer_agent` for them (its `ASSURANCE_WHOLE_PRODUCTS` follows 07), and the software lead would have two tables to reconcile. The SA template (branch `7784672`) says it "does not widen or narrow that table" and routes such a gap to the software lead as a cross item. Fix: either (a) have Part B rows 10 and 15 cite their basis (plan WP-PDR-16 and WP-PDR-36; swe-134 task 5; swe-081 task 2) and send a cross item to the 07 writer (WP-PDR-13, plan section 5.3) to add the hazard analysis and the software-side ICDs to the 07 §2.1.1 table, naming the dependency in the Schedule row; or (b) word rows 10 and 15 as "SA pair per the PDR work plan" without making it admission evidence | Open | Pending | |
| <a id="finding-3"></a>finding-3 | assurance | Minor | swe-081 7.1 task 2 | CR-007 C4 (line 56); C6 (e) Part B row 11 `docs/design/allocation.json` (line 77); C9 (line 94); C10 (line 96) | C4 makes the `code` paths of `docs/design/allocation.json` the identification of safety-critical and mission-critical code (the fix of INSP-030 finding-4, SWE-081); C10 makes the CR Safety field and the CSA criticality sub-rows depend on it, and C9 routes a CR to software assurance when its Safety field names a 07 §14.1 component. The map therefore decides which code changes reach the software assurance reviewer. Part B row 11 admits `allocation.json` on `peer-review-checklist-design.md` and tool runs only, with no software assurance review, while the architecture row beside it has its SA pair. A path omitted from the map, or placed under the wrong component, silently under-routes a safety-critical change. (INSP-039 finding-3, on how the map is keyed, is a different defect; this finding holds whichever key is chosen.) Fix: in Part B row 11 for `allocation.json`, add "the `code` map of the 07 §14.1 components (Table 4-1 row 25) confirmed by the software assurance reviewer, in the `design-architecture-software-assurance.md` record or its own pair" | Open | Pending | |

**INSP-039 findings under the assurance lens (not raised again; 07 section 10.2, template finding rules).** finding-1 (C7 gives the §7.4 checks to software assurance while §7.4 line 366 still names the independent reviewer): concur at Minor. Under swe-082 7.1 tasks 1 and 2, C7 and C9 give software assurance its part in control activities and the audit is performed whichever role is named, so no safety conclusion changes; the fix INSP-039 gives also closes INSP-030 finding-1 part (c). finding-2 (c) (C13 omits the TV-012 item A extension to blob `ddf10798`, confirmed at TV-012 lines 196 and 197): concur at Minor; under swe-136 7.1 task 1 the plan must state the accredited blob, since tool accreditation is confirmed against it. finding-3 (C4 keys the map by module): concur at Minor; with the rule "the highest criticality of any unit in the module applies to all its paths", which errs toward more assurance review, the assurance concern is met. finding-4 (interacting CRs): concur at Minor; this review confirmed that CR-010's `rmm.json` hunks leave rows SWE-063, SWE-085 and SWE-136 byte-identical to `main` (JSON row comparison of `main` and `cr/CR-010-apply-srr-decisions-9-and-40`), so C16 and CR-010 do not conflict.

### Task table

| Task | Safety-critical designation (SWEHB 8.10 section 6) | Applied | Result and evidence | Relief (N/A only) | Finding ids |
|---|---|---|---|---|---|
| swe-134 7.1 task 5 | SC | Yes | This review is the assurance participation in the review of a product 07 §2.1.1 routes here (row "Software plans") | | none |
| swe-022 7.1 task 1 | SC | Yes | Performed against the project software assurance plan (07 §15) by this record; the NASA-STD-8739.8 part is relieved | `rmm.json` SWE-022 T (the standard is not in the corpus) | none |
| swe-013 7.1 task 1 | SC | Yes | After CR-007, 05 keeps every SCMP element INSP-030 SA-079-1 listed and adds the Part B admission rows the allocated baseline needs (05 §4.4 line 164) | | none |
| swe-013 7.1 task 2 | SC | N/A | The software assurance plan is 07 §15, not this product | 07 §15 (07 is the software assurance plan, 07 §2.1.1 row "Software plans") | none |
| swe-024 7.1 task 1 | SC | Yes | The changed plan text is checked against NPR 7150.2D through the SWE tasks below; no new non-compliance; the NASA-STD-8739.8 part is relieved (`rmm.json` SWE-022 T) | | finding-2 |
| swe-024 7.1 task 2 | SC | Yes | Corrective actions: each INSP-030 and INSP-006 lien carries its closure rationale in the CR table (lines 31 to 43) and the INSP-039 lien table; two closures are partial (INSP-039 finding-1; finding-1 here) | | finding-1 |
| swe-024 7.1 task 3 | SC | Yes | The change of commitment (05 §4.4 "all three parts before PDR" narrowed to Part B now, product and as-built parts before CDR and SAR) is recorded in C6 (b) and put to the owner as Q2 | | none |
| swe-039 7.1 task 7 | | Yes | The assurance findings are kept in this record's findings table; the INSP-030 findings are carried to CR-007 by id (CR lines 36 to 40) | | none |
| swe-039 7.1 task 8 | SC | Yes | Each INSP-030 finding has a response in a named change item (CR lines 36 to 40); the owner ruling column here is Pending for Claude's transcription (01 §10.1) | | none |
| swe-121 7.1 task 1 | SC | Yes | C16 changes implementation texts only; `disposition`, `tailoring_rationale`, `residual_risk` and `status` unchanged (C16 line 120); C8 bounds the tailoring CR row so that a tailoring change still needs owner approval (charter §1) | | none |
| swe-125 7.1 task 1 | SC | Yes | C16 keeps the RMM consistent with 05 (AL-16, C14); the three "before" texts are verbatim in `e326ddd1` (exact-substring check, 3 of 3); `tools/render_rmm.py --check` is in step 5 | | none |
| swe-125 7.1 task 2 | SC | N/A | The NASA-STD-8739.8 matrix cannot be kept without the standard | `rmm.json` SWE-022 T | none |
| swe-139 7.1 task 1 | SC | Yes | Class A rigor kept: no requirement of 05 is relieved; the change adds routes (C7, C9, C12) | | none |
| swe-087 7.1 task 3 | | Yes | C7 and C9 add software assurance tasking to 05, which is part of the assurance tasking of 07 §15; this record is its peer review | | none |
| swe-090 7.1 task 1 | | Yes | Table 6-1 metrics unchanged in definition (C10 adds CSA sub-rows only); volatility contribution 0 stated (§4 line 154) | | none |
| swe-154 7.1 task 1, swe-156 7.1 task 1, swe-159 7.1 tasks 1 and 2 | | N/A | The template applies them to "the cybersecurity section (07 section 16)"; 05 has none. The CR's Cybersecurity field was checked under swe-080 task 1 | 07 §16 (cybersecurity plan) | none |
| swe-079 7.1 task 1 | | Yes | After CR-007, 05 still meets the SCMP content INSP-030 SA-079-1 confirmed; the additions (Part B, rows 56 and 57, §9.2 rows) fill the identification and tool gaps | | none |
| swe-080 7.1 task 1 | SC | Yes | Impact analysis of CR-007 itself: Safety field (line 145) correct, no `HZ-NNN` or 07 §14.1 component changes; C11 makes a fault-injection image (a hazard-control defeat path, INSP-030 finding-3) visible and rejectable on delivery, which reduces risk; Cybersecurity field (line 150) correct, USB load and key-input paths unchanged. C9 adds the assurance impact analysis INSP-030 finding-1 (a) asked for | | none |
| swe-080 7.1 task 2 | | Yes | a: CR-007 is on `main` with `Refs: CR-007` (`e119181`, `9032a02`); b: no `cr/CR-007-*` branch exists before disposition; c and d: implementation plan steps 3 to 7 with tool runs and the section 9 delta records | | none |
| swe-080 7.1 task 3 | | Yes | 05 is Table 4-1 row 2, CR-controlled from SRR; `git log baseline/srr..HEAD` on 05, 03, 07, `rmm.json` and the three templates is empty, so no change to them bypassed a CR | | none |
| swe-081 7.1 task 1 | | Yes | C5 rows 56 and 57 give the two unmatched paths a row (INSP-039 matcher: 2 unmatched, then 0); C11 gives each flavour its own identity; the VDD part of that identity is finding-1 | | finding-1 |
| swe-081 7.1 task 2 | SC | No | C4 and C10 identify safety-critical code (INSP-030 finding-4 closed in principle), but the map that routes changes to assurance is admitted without assurance review | | finding-3 |
| swe-082 7.1 task 1 | | Yes | C7 (§3 roles), C9 (§5.2 Assessed and Verified, mandatory whatever the class), C12 (§8.1 step 8) and C15 (a) (CR template) give software assurance its part; the §7.4 naming is INSP-039 finding-1 | | none |
| swe-082 7.1 task 2 | | Yes | Spot audit at `d566e01` against 05 §4.5 and §5.1: no class-CR CI changed after its CR-from event without a CR (swe-080 task 3 row). Seven commits in `baseline/srr..HEAD` carry no `Refs:` trailer (`51600e8`, `ab2af2d`, `1fe9c1a`, `091bceb`, `d9a78e0`, `f38159d`, `da6adbe`); the first CSA issue counted 3 (Table 6-1, Red), and four review-record commits since then add to it. This is execution, not a defect of CR-007; cross item X-2 | | none |
| swe-083 7.1 task 1 | | Yes | C10 adds CSA item 2 criticality sub-rows; step 9 regenerates the CSA after the merge | | none |
| swe-084 7.1 task 1 | | Yes | FCA and PCA unchanged except PCA-05, which C11 (d) makes reject a flavour suffix | | none |
| swe-085 7.1 task 1 | | Yes | C11 (a) to (f) keep flavour images out of delivery (§8.3 step 2 NCR and re-flash); C16 aligns the RMM SWE-085 text with 05 (first release candidate before CDR) | | none |
| swe-085 7.1 task 2 | | Yes | C7 names the §7.4 checks as the SWE-085 task 2 audit; no release exists yet, so no delivery audit is due | | none |
| swe-187 7.1 task 1 | | Yes | Flavour builds are configuration-identified by C11 before any credited Bench run (05 §8.1 "Build flavours", SWE-187) | | none |
| swe-187 7.1 task 2 | | Yes | Unchanged: release directories are never pruned and FCA-03, FCA-04 hash checks remain | | none |
| swe-063 7.1 task 1 | | No | C16 moves the first VDD to the first release candidate before CDR, consistent with 05 §13 CDR row (line 588) and 07 FW-B2 (line 162); the VDD template is not updated for flavour identity | | finding-1 |
| swe-063 7.1 task 2 | | Yes | C12 gives the software assurance reviewer the VDD row "Security and coding-standard confirmation (SWEHB 5.16 j)", which exists verbatim in the template (line 161), against the `tools/sw_gate.sh` log at S | | none |
| swe-136 7.1 task 1 | | Yes | C16 SWE-136 text matches 05 §9.2 step 3 (line 454: owner records "Accredited for purposes 1 to n at version v", entered in the lock; lock §5 is the validation status summary) and SRR decision 114 (memo line 371: TV-001 to TV-010 accredited); C13 adds the three known-answer rows; the TV-012 accredited blob is INSP-039 finding-2 (c) | | none |
| swe-200 7.1 task 1 | | Yes | The CR states volatility contribution 0 (no requirement changed; §4 line 154) | | none |

## Readiness criteria

| # | Criterion | Result | Evidence |
|---|---|---|---|
| R1 | Product committed and frozen; `product_files` equal to the paired record's list | Yes | `git rev-parse HEAD:<path>` at `d566e01` equals all eight blobs of INSP-039 `product_files`; CR-007 last changed at `9032a02` |
| R2 | 07 §2.1.1 row and criticality identified | Yes | Row "Software plans" (07 line 116: names "the software CM plan `docs/process/05-configuration-and-data-management.md`"), Yes for neither; 05 belongs to no 07 §14.1 component |
| R3 | `validate_docs.py` exit 0 on the product's files; `traceability.py --report-only` with a scratch `--output` reports no violation for the ids touched | Yes | `validate_docs.py` exit 1 only on the pre-existing record `docs/reviews/SRR/checklists/tool-validation-tv-001-to-tv-010.md` (another work package's record); no product file fails. `traceability.py --report-only --output <scratch>/tr.md`: exit 0, 0 violations, 2 warnings (REQ-SYS-125, REQ-SYS-148, not touched by CR-007) |
| R4 | Paired file review filed under its own invocation; this reviewer authored nothing and is not that reviewer | Yes | INSP-039 filed at `24ee338`, `author_agent` "author:WP-PDR-05", `reviewer_agent` "reviewer:WP-PDR-05 (independent reviewer, CM lens)"; this invocation is `sa-reviewer:WP-PDR-05-cm-plan-05` |

## A. Dispatch, independence and record integrity

| Id | Answer | Evidence |
|---|---|---|
| SA-A1 | No, on finding-2 | The product is routed correctly (07 line 116, Yes for neither). The product itself adds a second dispatch rule in 05 Part B rows 10 and 15 (finding-2) |
| SA-A2 | Yes | Three invocations: author `author:WP-PDR-05`, file reviewer `reviewer:WP-PDR-05`, this assurance reviewer; recorded in both records (INSP-039 names the pair as "not yet assigned", cross item X-1) |
| SA-A3 | Yes | Same product `docs/cm/cr/CR-007-cm-plan-pdr-rows.md`, same `product_commit` `9032a02`, same eight blobs |
| SA-A4 | Yes | INSP-039 applied `peer-review-checklist-requirements.md` revision C section G and CK-REQ-A8 with readiness R5, the route 08 §3.5 and 07 §10.1 give plans; every item G1 to G8 and A8 is answered with evidence; SWE-088 criteria a to d met (checklist, readiness, findings tracked with state, participants named) |

## B. SWE-to-task table

| Id | Answer | Evidence |
|---|---|---|
| SA-B1 | Yes | Task table above: the "Every product type" row, the `plans` row with its "for 05" list, and SWE-063, SWE-136 and SWE-200, which the product implements (C12, C16, §4 volatility). `assurance_tasks_applied` lists every Yes and No row |
| SA-B2 | Yes | N/A rows: swe-013 task 2 (07 §15), swe-125 task 2 (`rmm.json` SWE-022 T), swe-154, swe-156, swe-159 (07 §16); the product is of criticality neither |
| SA-B3 | Yes | swe-081 task 2 carries finding-3; swe-063 task 1 carries finding-1 |

## C. SWE-134 items a to l

N/A for every item: `criticality` neither (07 §14.1 lists no CM plan component), so `swe134_items_checked` is empty. CR-007 changes no safety-critical provision; its effect on safety-critical code is the routing of C4, C9 and C10, assessed under swe-081 task 2.

## D. Software safety analysis and hazard traceability

| Id | Answer | Evidence |
|---|---|---|
| SA-D1 | N/A | No `HZ-NNN` changes (CR §4 Safety, line 145); no software contribution is added or removed |
| SA-D2 | N/A | No component is created or renamed; 07 §14.1 unchanged |
| SA-D3 | N/A | No requirement changes (CR §4 line 154); R3 shows 0 violations |
| SA-D4 | N/A | No safety-tagged software requirement changes |
| SA-D5 | N/A | No hazard-tracing requirement changes |
| SA-D6 | N/A | The hazard analysis is not re-issued (CR §4 line 145); nothing in CR-007 changes it |

## E. Peer review, change and configuration assurance

| Id | Answer | Evidence |
|---|---|---|
| SA-E1 | No, on finding-1 | INSP-030 findings under CR-007: finding-1 closed by C7, C9, C12 and C15 (a) except the §7.4 naming (INSP-039 finding-1); finding-2 closed by C14 and C16 (before texts verbatim in `e326ddd1`, after texts consistent with 05 lines 454 and 588, 07 line 162 and SRR memo line 371); finding-3 closed by C11 except the VDD part (finding-1 here); finding-4 closed by C4 and C10, with INSP-039 finding-3 and finding-3 here; finding-5 closed by C5 row 56 (Record, append only) |
| SA-E2 | Yes | INSP-039 and this record both carry `findings_*`, `items_no`, `effort_turns`, `effort_minutes`, `iteration` (07 §10.3) |
| SA-E3 | Yes | CR file on `main` with `Refs: CR-007` at each commit (`e119181`, `9032a02`, 05 row 31); no class-CR CI changed after its CR-from event without a CR (swe-080 task 3 row). The trailer gaps on Record and Log commits are cross item X-2 |
| SA-E4 | N/A | No item under test and no credit run; CR-007 changes no test configuration |

## F. Assurance risks, metrics and reporting

| Id | Answer | Evidence |
|---|---|---|
| SA-F1 | Yes | No assurance concern that is not a product defect needs a risk entry: the trailer gap (X-2) is already measured by Table 6-1 in the CSA as Red with its response (RID candidate at PDR) |
| SA-F2 | Yes | Front matter carries `findings_*`, `assurance_findings_major` 0 and `assurance_findings_minor` 3 (the same findings, counted once, 07 §10.2), `items_no`, effort |
| SA-F3 | Yes | Verdict, open findings, tasks applied and reliefs are stated in this record |

## Completion criteria and verdict

Readiness R1 to R4 were true; every task SA-B1 requires is in the task table; every applicable item of sections A, E and F is answered and sections C and D are N/A with their reasons; zero Major findings. The three Minor findings are open: the template's completion criterion (every Minor fixed or deferred) and PDR work plan rule C1 ("Minor findings after the first APPROVED verdict become liens") differ on iteration 1; this record follows rule C1 and 08 §3.2 ("Minor findings ride with APPROVED"), as INSP-039 does. The findings are written for the CR author to fix in the CR revision before OD-36; a finding not fixed then is a lien due at the CDR readiness declaration (rule C1). `assurance_verdict: APPROVED`. With INSP-039 `reviewer_verdict: APPROVED`, both reviews of the product are APPROVED and all reviewed blobs are on `main`, so the record `verdict` is APPROVED (07 §10.2).

## Cross items (returned to Claude)

- **X-1.** INSP-039 (`cm-plan-05.md`) still reads `assurance_reviewer_agent: "not yet assigned ..."`, `assurance_verdict: NEEDS CHANGES`, `verdict: NEEDS CHANGES` and no `paired_record`. Its reviewer updates it to `paired_record: INSP-047`, names this reviewer and copies `assurance_verdict: APPROVED` (07 §10.2 Record row; the reviewer of each record updates its own record).
- **X-2.** Trailer audit (swe-082 task 2): seven commits in `baseline/srr..HEAD` at `d566e01` have no `Refs:` trailer, four of them review-record commits made after the first CSA issue (`091bceb`, `d9a78e0`, `f38159d`, `da6adbe`), which counted three. Table 6-1 "Commits lacking mandatory trailers" stays Red; the next CSA issue counts them.
- **X-3.** After CR-012 merges, the delta iteration of this record switches `checklist` to `peer-review-checklist-software-assurance` revision A and drops `checklist_software_assurance`.

## Observations (no finding)

- **O-1.** C9 Verified row, added sentence: "For a CR the Assessed row routes to the software assurance reviewer, that reviewer also confirms ..." lacks "that" after "For a CR"; the author can fix it with the findings.
- **O-2.** C11 (a) says "the script sets `CWHT_BUILD_ID` with the suffix". `vX.Y.Z+<short S>.<flavour>` is valid SemVer build metadata (dot-separated identifiers after `+`), so tools that parse the version keep working.

## Commands

| Command | Exit | Result |
|---|---|---|
| `git rev-parse HEAD:<path>` for the eight `product_files` at `d566e01` | 0 | All equal to INSP-039's list |
| `git show cr/CR-012-pdr-checklist-templates:docs/templates/peer-review-checklist-software-assurance.md` | 0 | Template revision A, blob `5b135285`, 229 lines |
| Section 7.1 extraction from `docs/references/md/swehb/swe-NNN-*.md` for SWE-013, 022, 024, 039, 063, 079 to 085, 087, 090, 121, 125, 134, 136, 139, 154, 156, 159, 187, 200 | 0 | Task texts used in the task table |
| Exact-substring check of the C16 "before" texts in `git show e326ddd1` | 0 | 3 of 3 present |
| JSON comparison of rows SWE-063, SWE-085, SWE-136 on `main` and `cr/CR-010-apply-srr-decisions-9-and-40` | 0 | Identical |
| `git log baseline/srr..HEAD` on 05, 03, 07, `rmm.json`, the change-request, ADR and VDD templates | 0 | Empty |
| Trailer scan of `git log baseline/srr..HEAD` | 0 | 7 commits without `Refs:`, `CR:` or `Editorial:` (X-2) |
| `.venv/bin/python tools/traceability.py --report-only --output <scratch>/tr.md` | 0 | 0 violations, 2 warnings; no repository report file written |
| `.venv/bin/python tools/validate_docs.py` | 1 | This record PASS; the one failure is the pre-existing SRR record `tool-validation-tv-001-to-tv-010.md` |

## Verdict format

```
ASSURANCE VERDICT: APPROVED
PRODUCT: docs/cm/cr/CR-007-cm-plan-pdr-rows.md@92b200ad (and the seven INSP-039 product_files) at 9032a02; PAIRED RECORD: INSP-039
PRODUCT TYPE: plans; CRITICALITY: neither
FINDINGS:
- [Minor] swe-063 7.1 task 1 (SA-E1) C11 gives flavours an embedded identity but no change item puts it in the VDD template (INSP-030 finding-3 "list it in VDD section 2").
- [Minor] SA-A1 Part B rows 10 and 15 require SA pairs for ICDs and the hazard analysis, which 07 section 2.1.1 (the single dispatch rule) does not list.
- [Minor] swe-081 7.1 task 2 the allocation.json code map that routes safety-critical changes to assurance (C4, C9, C10) is admitted in Part B row 11 without assurance review.
TASKS APPLIED: swe-134 task 5, swe-022 task 1, swe-013 task 1, swe-024 tasks 1 to 3, swe-039 tasks 7 and 8, swe-121 task 1, swe-125 task 1, swe-139 task 1, swe-087 task 3, swe-090 task 1, swe-079 task 1, swe-080 tasks 1 to 3, swe-081 tasks 1 and 2, swe-082 tasks 1 and 2, swe-083 task 1, swe-084 task 1, swe-085 tasks 1 and 2, swe-187 tasks 1 and 2, swe-063 tasks 1 and 2, swe-136 task 1, swe-200 task 1
TASKS N/A (relief): swe-013 task 2 (07 section 15), swe-125 task 2 (rmm.json SWE-022 T), swe-154 task 1, swe-156 task 1, swe-159 tasks 1 and 2 (07 section 16)
SWE-134 ITEMS CHECKED: none (criticality neither)
MEASUREMENTS: size=16 change items; tasks=36; tasks_no=2; turns=34; minutes=55; major=0; minor=3
```

## Delta iteration 2 (2026-09-29, CR-007 revision 4 at `7668322`; software assurance reviewer, new invocation)

**Scope.** On `main` at `c9f611d`, `tools/validate_docs.py` failed this record on record drift: it pinned `docs/cm/cr/CR-007-cm-plan-pdr-rows.md` at `92b200ad` (revision 1), and the file is now `abec03c5` (`git rev-parse HEAD:<path>` and `git hash-object <path>`, last commit `7668322`, revision 4, status Implemented on branch `cr/CR-007-cm-plan-pdr-rows`), and it pinned `docs/lessons-learned.md` at `ec30a264` (now `d250e8fb`, entry 18 at `391f0e5`). The CR is this record's product and its sections 1 to 5 changed in revisions 2, 3 and 4, so this is a delta, not a re-pin: it verifies every hunk of `git diff 92b200ad abec03c5` (304 insertions, 43 deletions) under the assurance lens, states the current state of finding-1 to finding-3, and names the new blob. The lessons-learned entry is dropped from `product_files` with its reason in the front matter (INSP-060 and INSP-034 precedent). The five other blobs equal `HEAD`. This delta reviews the CR file on `main`. The implemented blobs on the branch (05 `987fed52`, 07 `e11abe30`, `rmm.json` `76117854`, `rmm.md` `0ba6a670`, `docs/templates/change-request.md` `ce226b64`, `docs/templates/adr.md` `5c5e6d4b`, all at `f68e47a`) are the CR-007 section 5 step 7 delta of this record, which is a separate task (cross item X-5); they were read here only where a finding needed them.

**Independence (rule C4).** A new invocation of the software assurance reviewer role (07 §2.1.1). It authored no part of CR-007 (any revision, section 6.8 or the branch commits), WP-PDR-05, INSP-039, the section 6 impact reviews or iteration 1 of this record, and edited no product file. **Search first (rule C3).** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (queries: the INSP-060 re-pin precedent; INSP-027 and TS-002 delta practice). `git diff`, `git show`, `grep -n`, `sed -n` and `awk` were used afterwards only to extract sections and pin lines.

**Method.** Sections 1 to 5 of the three versions were extracted: revision 1 (`92b200ad`), revision 3 as reviewed in sections 6.6 and 6.7 (`ee11ec70`, at `65331c6`) and revision 4 (`abec03c5`). `git diff --no-index -U0` of 1 against 4 lists the hunks; `--word-diff` of 3 against 4 isolates the revision 4 changes, which were compared one by one with the section 8 table "Differences of the committed text". Sections 6.1 to 6.8, 7 and 8 were read in full. Sections 6 to 12 are review and lifecycle records appended to the CR; they are read for the state of the findings and are not a product change.

### Hunks verified (92b200ad to abec03c5)

| Hunk | Change | Assurance check | Result |
|---|---|---|---|
| Front matter | `status` Implemented; `disposition` Approved, 2026-09-28; 07 added to `affected_paths`; INSP-010, INSP-018 to `affected_ids`; CR-010, CR-013 to `related` | Disposition matches section 7 (Decision Approved, 2026-09-28, two history rows); 07 is the C17 target; the template's `affected_ids` list names requirement, test, ICD, hazard and similar ids, so the omission of INSP-009 and INSP-017 there is not a defect | Pass |
| Status line and revision 2, 3, 4 paragraphs (lines 27 to 33) | Bookkeeping; revision 4 names the branch from `908d21a` and commits `cc4c138`, `66ac317`, `60645f8`, `f68e47a` | The four commits exist on the branch in that order (`git log` in the CR worktree). The approval basis claimed for the revision 4 changes is finding-4 | finding-4 |
| C1 | Date and revision number filled (2026-09-29, revision 4) | Placeholder only | Pass |
| C7 | Revision 2 and 3 text: the assurance role names 07 §2.1.1 as the single dispatch rule, its CR tasks and hold points | 07 §2.1.1 stays the single rule and C7 cites it (IR-F1 fix, verified in section 6.3; SA-F2, section 6.7). No revision 4 change | Pass |
| C9 | Assessed row routes by the 07 §2.1.1 triggers by number; the CM function (§3) records the routing; Verified row: the paired assurance delta is the confirmation; closure without implementation | Numbering agrees with C17 (b) rows 1 and 2 (triggers (1) to (4)); the precedence sentence stays; the DR-F1, DR-F2, DR-F3, SA-F3 and SA3-F1 to SA3-F3 wording is as section 6.8 states | Pass |
| C11 (d) | First word of the PCA-05 cell in lower case | Sentence case only; the flavour-suffix rejection is unchanged | Pass |
| C12 | The confirmation includes the advisory database commit and date (SA-F4) | Agrees with C17 (b) row 3 | Pass |
| C13 | TV-013 row at run 3 (18 tests); §13 note with tool blobs and the ACC-COMPLEXITY-001 extension | Blobs `cc3aaa2a`, `ddf10798`, `abe25acb` equal `git rev-parse 908d21a:<path>` for `tools/unsafe_audit.py`, `tools/complexity_gate.py`, `tools/measurements.py` (SA-F5) | Pass |
| C15 (a) | Template summary of the triggers and the section 9 sentence | Agrees with C9 and C17 (b); names no actor (DR-F1 response) | Pass |
| C16 | SWE-063 and SWE-085 read "Planned for CDR, before the gate:" | `tools/render_rmm.py` `GATE_MARKER_RE` (line 83) matches only "Planned for <gate>", so the revision 3 wording "Planned before CDR:" fails the check, as section 8 says; the meaning is unchanged | Pass |
| C17 (a) to (g) | New change item against 07 (revision 2), rewritten for SA-F1 and SA-F2 (revision 3) and for SA-F3, SA-F4, DR-F1 to DR-F3 and SA3-F1 to SA3-F3 (revision 4) | 07 §2.1.1 at `f68e47a` carries the three CR, release and configuration-check rows and the hold-point paragraph; the §16.2 rows cited as basis exist (07 lines 697 to 702: "Firmware image integrity" with RSK-015, "Keying and control inputs", "Debug access", "Diagnostic interface" with RSK-061 and CS-33, "Build and supply chain"); the §23 row is A.10 (line 891). No product row for ICDs, the hazard analysis or `allocation.json` is added (finding-2, finding-3) | Pass |
| Revision 4 note (line 156) | Section 1 equals the committed text at `f68e47a`, with six blobs | The six blobs equal `git rev-parse f68e47a:<path>` (six of six). The revision 3 to 4 word diff has hunks only at the items the section 8 table lists, plus the section 4 and 5 rows that revision 4 says change this record only | Pass |
| Section 4 rows and classification rationale | Safety, Interfaces, Cybersecurity (SA-F6), Verification (SA-F7), Schedule, Documentation | Cybersecurity names the two 07 §16.2 rows and the control C11 adds, with cross items to the 07 writer and the risk owner; Verification adds the INSP-009 and INSP-017 deltas and the template listing; the rationale keeps Class II on stated grounds | Pass |
| Section 5 steps and verification paragraph | Steps 3 to 6 done with SHAs; step 5a "(a) to (g)" (DR-F4); step 7 adds the SA-F7 records | Steps 1 and 2 were not brought up to date | finding-5 |

### Effect of revisions 2 to 4 on finding-1 to finding-3

- **finding-1 (VDD flavour identity) is not fixed.** C15 still changes only the CR and ADR templates, `affected_paths` does not name `docs/templates/version-description.md`, and the §2 flavour row of the template is unchanged on the branch (`f68e47a` line 46: files, hash and Cargo feature, no embedded version string). Section 6.8 routes a related VDD field (the advisory database commit and date, SA-F4) to the VDD template owner "with INSP-047 finding-1", outside this CR.
- **finding-2 (second dispatch rule in Part B rows 10 and 15) is not fixed.** Rows 10 and 15 (lines 81 and 85) still require assurance pairs for the software-side ICDs and for the hazard analysis, and the 07 §2.1.1 table at `f68e47a` still has no product row for either: C17 (b) trigger (3) routes CRs that change such an ICD, not the ICD's own review. Section 6.8 (SA3-F2 response, line 383) leaves row 10 unchanged on purpose, citing this finding as open; that is consistent with the fix options of iteration 1.
- **finding-3 (the row 25 map admitted without assurance review) is not fixed.** Part B row 11 for `docs/design/allocation.json` (line 83) is unchanged. C17 (b) row 1 now routes a CR that changes a row 25 map path, which strengthens the use of the map but not the review of the map itself.

All three stay Open. Under PDR work plan rule C1 they are now liens due at the CDR readiness declaration, as iteration 1 and CR section 6.8 state.

### New findings of the delta

| Finding | Origin | Severity | Item | Location | Description | State | Disposition |
|---|---|---|---|---|---|---|---|
| <a id="finding-4"></a>finding-4 | assurance | Minor | swe-080 7.1 task 2 (item b) | CR-007 revision 4 paragraph (line 33); section 7 Conditions (line 397); section 8 table of differences | The revision 4 paragraph says section 1 changes by the fixes "that the owner's option B condition assigns to step 3 (section 7 Conditions)" and lists SA-F3 to SA-F5, DR-F1 to DR-F3 and SA3-F1 to SA3-F3. The owner's condition (section 7 Conditions; `status-2026-09-28.md` section 4) assigns only "SA-F3 to SA-F7" to step 3; DR-F1 to DR-F4 and SA3-F1 to SA3-F3 were raised afterwards, in sections 6.6 and 6.7, and assigned to step 3 by those reviewers as corrections inside the approved scope. The committed 05 and 07 text therefore differs from the revision 3 text the owner approved by seven reviewer-assigned fixes, one of which (SA3-F2) widens triggers (2) and (3) to more CRs, and the CR states an owner assignment that the owner did not make. No unapproved text is baselined, because the merge approval (step 8) is still ahead and section 8 lists every difference with its finding | Open | Lien: fix before CDR (rule C1). Fix (CM function, CR-007 author): state that DR-F1 to DR-F4 and SA3-F1 to SA3-F3 were assigned to step 3 by the section 6.6 and 6.7 reviewers, and put the section 8 table of differences, SA3-F2's widening named, in the owner's merge approval request at step 8, with the owner's answer recorded in section 10 |
| <a id="finding-5"></a>finding-5 | assurance | Minor | swe-080 7.1 task 2 (item a) | CR-007 section 5 steps 1 and 2 (lines 197 and 198) | Revision 4 fills the Done cells of steps 3 to 6, but step 1 still reads "Pending: the delta impact review of revision 3 ... step 3 waits for it" and steps 1 and 2 have empty Done cells. The plan table therefore shows step 3 done while its own precondition reads pending, although the delta impact reviews were recorded on 2026-09-28 (sections 6.6 at `8527083` and 6.7 at `65331c6`) before the branch was cut from `908d21a`, and the disposition was recorded at `a17af87` with its confirmation at `584f361`. An auditor reading the table cannot see from it that the hold was kept | Open | Lien: fix before CDR (rule C1). Fix (CM function): at the next CR-007 lifecycle update, mark step 1 done with the five review commits (`ca228b9`, `3a52115`, `6830dcc`, `8527083`, `65331c6`) and step 2 done (`a17af87`, `584f361`) |

### Findings (delta iteration 2; current state of every finding of this record)

| Finding | Origin | Severity | Item | Location | State | Disposition | Deferred to |
|---|---|---|---|---|---|---|---|
| finding-1 | assurance | Minor | swe-063 7.1 task 1, swe-081 7.1 task 1, SA-E1 | C11, C15; VDD template §1 and §2 | Open | Lien: fix before CDR (rule C1); not fixed by revisions 2 to 4 | CDR readiness declaration |
| finding-2 | assurance | Minor | SA-A1, CK-REQ-G1, swe-134 7.1 task 5 | C6 (e) Part B rows 10 and 15 (lines 81, 85); 07 §2.1.1 | Open | Lien: fix before CDR (rule C1); not fixed; kept open on purpose by CR section 6.8 | CDR readiness declaration |
| finding-3 | assurance | Minor | swe-081 7.1 task 2 | C6 (e) Part B row 11 `allocation.json` (line 83) | Open | Lien: fix before CDR (rule C1); not fixed | CDR readiness declaration |
| finding-4 | assurance | Minor | swe-080 7.1 task 2 | Revision 4 paragraph; section 7 Conditions; section 8 | Open | Lien: fix before CDR (rule C1); new in delta iteration 2 | CDR readiness declaration |
| finding-5 | assurance | Minor | swe-080 7.1 task 2 | Section 5 steps 1 and 2 | Open | Lien: fix before CDR (rule C1); new in delta iteration 2 | CDR readiness declaration |

Lien count: 5. Open Major: 0.

### Task answers at the delta

As iteration 1, with these changes: swe-080 7.1 task 2 No (finding-4, finding-5); swe-080 7.1 task 1 Yes (the section 4 fields of revision 4 are correct: no `HZ-NNN`, 07 §14.1 component, ICD text, 07 §16 mitigation text or `RSK-NNN` score changes; SA-F6 names the two 07 §16.2 rows the C11 control strengthens); swe-082 7.1 task 1 Yes (C17 puts the reviewer's CR, release and configuration-check tasks in 07 §2.1, §2.1.1 and §15); swe-081 7.1 task 2 No (finding-3); swe-063 7.1 task 1 No (finding-1); SA-A1 No (finding-2). Readiness R1 to R4: R1 holds for the CR blob and the five other blobs at `HEAD`; the pairing part of R1 does not (INSP-039 names `22c4455f`), which is why the record verdict is held.

### Record verdict, delta iteration 2

`assurance_verdict: APPROVED` and `reviewer_verdict: APPROVED` on `abec03c5`: no Major finding; the five Minor findings are liens under rule C1. `verdict` is held at NEEDS CHANGES: the paired file review INSP-039 is APPROVED only on `22c4455f` (revision 2), and 07 §10.2 sets neither record to APPROVED until both reviews are APPROVED. When INSP-039 files its delta on `abec03c5` APPROVED, the software lead sets `verdict: APPROVED` on both records. `record_status` stays Open.

### Cross items (returned to Claude)

- **X-4.** INSP-039 (`cm-plan-05.md`) delta on CR-007 `abec03c5` (revisions 3 and 4) by its file-review role; its fields `paired_record: INSP-047` and `assurance_reviewer_agent` (iteration 1 cross item X-1) are still unset.
- **X-5.** CR-007 section 5 step 7: the delta of this record on the implemented blobs at `f68e47a` (05, 07, `rmm.json`, `rmm.md` and the two templates in `product_files`, as SA-F7 asks), after or with the INSP-039 step 7 delta. finding-1 to finding-5 are re-read there.
- **X-6.** Iteration 1 cross item X-3 stands: CR-012 is not merged (`docs/templates/peer-review-checklist-software-assurance.md` is not on `main`), so the `checklist` field is unchanged.

### Tool runs (2026-09-29, `.venv/bin/python`)

| Command | Exit | Result |
|---|---|---|
| `tools/validate_docs.py` (before this update, `main` `c9f611d`) | 1 | 110 passed, 7 failed; this record failed on drift (CR-007 `92b200ad` against `abec03c5`; lessons learned `ec30a264` against `d250e8fb`) |
| `git rev-parse f68e47a:<path>` for the six revision 4 note blobs; `908d21a:<path>` for the three C13 tools | 0 | Six of six and three of three as stated |
| `tools/validate_docs.py` (after this update) | 1 | 116 passed, 1 failed (`docs/reviews/SRR/checklists/adrs-001-to-025.md`, another record); this record PASS with no drift note (every named blob equals `HEAD`) |

```
DELTA ITERATION 2 (2026-09-29, CR-007 revision 4 at 7668322): ASSURANCE VERDICT: APPROVED; RECORD VERDICT: NEEDS CHANGES (held for the INSP-039 delta on abec03c5)
PRODUCT: docs/cm/cr/CR-007-cm-plan-pdr-rows.md@abec03c5 (equal to HEAD) and five other blobs; docs/lessons-learned.md dropped (re-pin)
FINDINGS: finding-1 to finding-3 Minor, Open, not fixed by revisions 2 to 4 (finding-2 kept open on purpose by CR section 6.8); new finding-4 and finding-5 Minor, Open; all five liens due the CDR readiness declaration; open Major 0
MEASUREMENTS (delta): turns=28; minutes=45; cumulative turns=62, minutes=100; major=0; minor=2 new; lien=5
```
