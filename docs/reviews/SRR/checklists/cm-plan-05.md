---
# Peer-review record (charter section 5; 01 section 13; 08 section 3.2). Copy of
# docs/templates/peer-review-checklist-requirements.md, product type "plans and process documents"
# (section G and A8). Slug cm-plan-05 as assigned by the dispatching session (01 section 13 would
# give plan-05-configuration-and-data-management; see Observations O-3).
id: INSP-006
checklist: peer-review-checklist-requirements
checklist_revision: C
checklist_file: docs/reviews/SRR/checklists/cm-plan-05.md
product: docs/process/05-configuration-and-data-management.md
# product_commit: last commit touching the product at the iteration 3 review baseline HEAD adcfe0946d2f1b5cd8f41a8f91eb4219a7fb99a1
# (iteration 1: 4e3f8913366c60e79a9ace6a1b4f36f24adc3479; iteration 2 reviewed an uncommitted working tree)
product_commit: "0ab3d6e3fad8e22d336a458ec08d0e9220bdfbc5"
# product_blob: git rev-parse HEAD:docs/process/05-configuration-and-data-management.md at adcfe09.
# Iteration 1: 8e7a1c842bbe16278c7be015bf291782b25df988; iteration 2: 40d45f4fd6e5109a1f1825f23797ccb0f62d97bd (never committed)
product_blob: "63ed566240ffc7f055b65f93f579a6bb1498e9f1"
# product_files: the committed blobs reviewed at iteration 3 (record drift rule, package section 2.3, R13);
# rmm.json is the file finding-7 is verified in
# re-issue 2026-09-26 (package item R8, no further product review): both blobs re-checked equal to git rev-parse HEAD:<path>
# and git hash-object at HEAD 1af795c; git log adcfe09..HEAD on both paths is empty
product_files: ["docs/process/05-configuration-and-data-management.md@63ed566240ffc7f055b65f93f579a6bb1498e9f1", "docs/process/rmm.json@30fcde240eeb6a147359de8c5d8cdd93364dc9c8"]
product_size: 16 sections, 672 lines (revision 3 plus the 2026-09-26 edits of Table 4-1 row 13 and AL-15), Table 4-1 with 55 rows, Tables 4-2 and 6-1
sprint: SRR-prep
author_agent: author:cm-plan (Claude lead SE, CM function; revision 2 of 2026-09-25)
reviewer_agent: reviewer:cm-plan
criticality: neither
# assurance_required: true since 07 revision A.4 (blob at adcfe09, section 2.1.1 line 117: "Software plans ... the software CM plan
# docs/process/05-configuration-and-data-management.md" is Yes in the Neither column; line 119 now excepts 05 from "Other process
# documents"). Re-issue 2026-09-26: the paired software assurance record of 05 is INSP-030
# (docs/reviews/SRR/checklists/cm-plan-05-software-assurance.md, committed at 898d582, same blob 63ed5662, paired_record: INSP-006,
# assurance_verdict APPROVED with 4 Minor liens); 01 section 13 paired form; package item R6 done.
assurance_required: true
assurance_reviewer_agent: "sa-reviewer:cm-plan (software assurance function; paired assurance record INSP-030; file review by reviewer:cm-plan)"
paired_record: INSP-030
iteration: 3
# readiness_met: true at the re-issue (package item R8): R3 is met by the author self-check filed at 8ef95d3 (package item R7);
# R1 and R4 Met, R2 and R5 N/A as answered at iteration 3. See "Re-issue"
readiness_met: true
# reviewer_verdict: every finding is Closed or a Lien (convergence rule of 2026-09-26).
# assurance_verdict: the paired record INSP-030's assurance_verdict (07 section 10.2 completion criteria; 01 section 13).
# verdict: APPROVED (with liens finding-10, finding-11) at the re-issue: reviewer APPROVED, assurance APPROVED, readiness met,
# no Major finding open, named blobs equal HEAD (07 section 10.2; SWE-088)
reviewer_verdict: APPROVED
assurance_verdict: APPROVED
verdict: APPROVED
findings_major: 2
findings_minor: 9
# findings_open: no finding in state Open; finding-10 and finding-11 are Liens (fix before PDR), counted in findings_deferred
findings_open: 0
findings_fixed: 9
findings_verified: 0
findings_deferred: 2
assurance_findings_major: 0
assurance_findings_minor: 0
assurance_tasks_applied: []
deferred_rids: []
# items_no: iteration 3 answers: CK-REQ-G1 (finding-10, Lien) and CK-REQ-G2 (finding-11, Lien); every other item Yes
items_no: [CK-REQ-G1, CK-REQ-G2]
# effort: iteration 1 (45 turns, 40 min), iteration 2 (12 turns, 15 min), iteration 3 (28 turns, 35 min),
# re-issue (package item R8, shared with INSP-010 and INSP-018) 8 turns, 15 min
effort_turns: 93
effort_minutes: 105
record_status: Open
date: 2026-09-25
date_closed: null
---

# Peer review record INSP-006: CM and technical data management plan (05)

**Product:** `docs/process/05-configuration-and-data-management.md`, revision 2 (2026-09-25), commit `4e3f891`, blob `8e7a1c842bbe16278c7be015bf291782b25df988`. **Checklist:** `docs/templates/peer-review-checklist-requirements.md` revision C, section G (CK-REQ-G1 to G8) and CK-REQ-A8, per its product-type table row "Plans and process documents". **Minimum content judged:** CM plan per SE HB App. M and NPR 7150.2D SWE-079 to SWE-085 as dispositioned in `docs/process/rmm.json`; SE-20 and SE-21 per `docs/process/se-compliance-matrix.json`. **SRR context:** package `docs/reviews/SRR/package.md` section 2 item H1 (CM plan record) and H12 (the nine TV records 05 section 13 requires at SRR).

**Re-issue (2026-09-26, package item R8): verdict APPROVED (with liens finding-10 and finding-11).** The author self-check (package item R7, filed at `8ef95d3`) meets readiness R3, and the paired software assurance record INSP-030 (package item R6) carries `assurance_verdict: APPROVED` on the same blob, so both non-finding holds of iteration 3 are gone; the product blobs equal HEAD. See "Re-issue" at the end.

**Search-first compliance:** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` was run before every manual search (queries: peer-review record fields; SRR H items and CM plan; NPR 7123.1D SE-20 purposes; rustos blinky ELF and UF2 sizes; branch protection risk OQ-CM-001). `grep -n` was used afterwards only to pin lines.

## Findings

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to | Disposition (iteration 2, reviewer) |
|---|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | reviewer | Major | CK-REQ-G4, CK-REQ-G1 | 05 section 16, row SWE-045 | 05 states "SWE-045 (joint NASA/developer audits): Not applicable: no NASA counterpart; recorded in the RMM." The RMM row SWE-045 (`docs/process/rmm.json`, npr_section 5.1.9) has disposition `FC`: "The owner, in the acquirer role (03 section 6.2 role mapping), participates in the functional and physical configuration audits at SAR ... Planned for SAR". The plan misstates a Class A tailoring disposition, which charter section 1 and section 11 rule 5 allow only through the RMM. Fix: rewrite the row as fully compliant, citing section 7 (FCA and PCA) and section 3 (owner performs the hands-on PCA steps), and name SWE-045 in the owner row of section 3. | Closed | Pending | | Closed. 05 revision 3 section 16 row SWE-045 now reads "Fully compliant, as the RMM row SWE-045 (NPR 7150.2D §5.1.9, disposition FC) records", citing §7.1, §7.2 and `docs/reviews/SAR/configuration-audit.md`; section 3 owner row names the acquirer role (03 §6.2, whose FC rule maps NASA acquirer and participant roles to the owner), FCA and PCA at SAR, §8.4 delta audits and "(SWE-045)". Agrees with `rmm.json` SWE-045 (disposition FC, implementation text read 2026-09-25). |
| <a id="finding-2"></a>finding-2 | reviewer | Major | CK-REQ-G1 | 05 section 4.4, baseline procedure step 1, with the Functional row of the baseline table | Step 1 requires "every CI listed for the baseline is at L1 (filled checklist with `id: INSP-NNN`)". The functional baseline lists rows 1 (charter), 2 (also `docs/plan/schedule.md`, `docs/plan/cost-estimate.md`, `docs/process/README.md`), 9 (schemas), 17 (TC-SYS cases citing L1 requirements, 108 cases in `docs/test_cases/`), 27 (`tools/toolchain.lock.md`, `tools/requirements.txt`) and 53 (templates). No record is planned for these in package section 2 H1, and 08 section 3.5 names no checklist for schemas, templates or the lock ("A review that needs a checklist that does not yet exist is not held"). As written, `baseline/srr` cannot be tagged without an unlogged departure from step 1. Fix: state in 05 which Table 4-1 rows need an INSP record to enter a baseline and what evidence admits the others (for example schemas and templates by `validate_docs.py` and the unit tests, the lock by its TV records, the charter by the owner's decision memo), or add the missing records to the H1 plan with Claude (carry to the package). | Closed | Pending | | Closed. §4.4 step 1 now requires the Table 4-2 admission evidence of each row, not an INSP record for every CI; Table 4-2 covers every CR-class row of the Functional line (1, 2, 3, 5, 6, 7, 9, 17, 27, 51, 52, 53), names an INSP record where a checklist exists (row 17 uses `peer-review-checklist-test.md`, which exists) and tool, TV or decision-memo evidence where none exists (charter by the memo; schemas and templates by `validate_docs.py` and the unit tests; lock by TV records and AL-4), and step 1 forbids tagging on an unlogged departure (`docs/cm/deviations.md`, row 43). The records marked "not yet in H1" are a package cross item (package H1), an execution item, not a plan defect. |
| <a id="finding-3"></a>finding-3 | reviewer | Minor | CK-REQ-G1 | 05 section 10.4, Retention bullet | "derived data is not retained beyond the review that used it" contradicts section 10.1 (derived data "rendered figures, traceability report, CSA" kept in the repo), Table 4-1 row 18 (per-review traceability report and data file "are that review's evidence and are not regenerated after the review") and row 33 (review figures are Record class). Fix: limit the sentence to the gitignored derived data (`.stl`, `target/`, LTspice `.raw` and `.log` outside `docs/vv/`, KiCad backups). | Closed | Pending | | Closed. §10.4 Retention now keeps the committed derived data of §10.1 (figures, traceability reports and data files, CSA; rows 18 and 33) indefinitely and limits non-retention to the gitignored derived data (`.stl`, `target/`, LTspice `.raw` and `.log` outside `docs/vv/`, KiCad backups). No contradiction remains. |
| <a id="finding-4"></a>finding-4 | reviewer | Minor | CK-REQ-G1 | 05 section 14.1, rows AL-10, AL-12, AL-14 | Statuses are stale against the repository on 2026-09-25: AL-10 says the 02 author must replace item 4 of 02 section 10.3, but 02 section 10.3 item 4 already names the 05 section 5.3 rows Risk, Software classification and tailoring, Operations and ConOps, Cybersecurity and Regulatory; AL-12 says the SEMP author must mirror the two customizations, but `docs/plan/semp.md` section 5.14 states both and cites 05 section 2 for waivers; AL-14 says removal of root `result.json` and `reveal.js/` is open, but neither exists at the repository root (`ls` exit 1 for both). Fix: mark each Done with the date and the evidence. | Closed | Pending | | Closed. §14.1 AL-10, AL-12, AL-14 read Done 2026-09-25 with evidence. Re-checked: 02 AL-02-08 is Closed and says section 10.3 item 4 points to the 05 §5.3 rows; SEMP §5.14 states both customizations and cites 05 §2 for waivers, customization table rows 4 and 5 cite 05 §1; `ls result.json reveal.js` at the root exit 1, both "No such file or directory". |
| <a id="finding-5"></a>finding-5 | reviewer | Minor | CK-REQ-G7 | 05 section 8.1 step 4, last sentences | "a `rustos` blinky ELF is 132 kB, its UF2 8 kB": the UF2 is 4 kB. Evidence: `docs/research/rustos-toolchain-proof.md` F5 (`demo.uf2, 4096 B`; ELF 134,500 B in F4) and `docs/vv/reports/TC-SW-TOOL-001-r1/rustos-blinky.uf2` 4096 B, `rustos-blinky.elf` 134504 B. Fix: "its UF2 4 kB", citing F5. | Closed | Pending | | Closed. §8.1 step 4 now reads "its UF2 4 kB", citing `docs/research/rustos-toolchain-proof.md` F5 and the TC-SW-TOOL-001-r1 artifacts (ELF 134,504 B, UF2 4,096 B), the values of the finding. |
| <a id="finding-6"></a>finding-6 | reviewer | Minor | CK-REQ-G6 | 05 section 6, CSA item 10; section 5.2 cycle-time targets | Only requirements volatility (section 5.4) has source, thresholds (10 % yellow, 20 % red), storage (`MSR-02` in `docs/plan/measurements.json`) and a response rule. The other CSA metrics (open CR count and age, CR cycle time, count of commits lacking mandatory trailers) have no threshold or analysis rule in 05; the SEMP section 5 CM row gives "CIs changed after their baseline without a CR or `Editorial:` trailer: 0". Fix: state for each metric its threshold (for example 0 commits lacking trailers; a CR older than its section 5.2 target is flagged) and the response (RID or RFA at the next review), and its storage location. | Closed | Pending | | Closed. New Table 6-1 gives each of the four CM metrics its computation and source, threshold, response and storage: volatility (10 % and 20 %, matching 07 §11.2 MSR-02), open CRs and age (zero past the §5.2 target; CR template carries `date_opened`), CR cycle time (the §5.2 targets; two or more over target raise an RFA), commits lacking trailers (0, matching the SEMP §5 CM row; each is a RID, and a CR-less change to a class-CR CI is a deviation). §5.2 points to Table 6-1; CSA item 10 now cites it. |
| <a id="finding-7"></a>finding-7 | reviewer | Minor | CK-REQ-G1 | `docs/process/rmm.json` rows SWE-082 and SWE-085 against 05 sections 4.1, 8.1, 8.3 | RMM SWE-082 names the levels "working tree, review-ready, baselined"; 05 section 4.1 defines L0 Working, L1 Reviewed, L2 Controlled, L3 Released. RMM SWE-085 says `firmware/releases/` "holds the UF2 image, its SHA-256 and the VDD" and that flashing "follows the documented flashing procedure in the operations handbook"; 05 section 8.1 step 4 writes ELF, UF2, map, `picotool-info.txt` and `SHA256SUMS` into `firmware/releases/vX.Y.Z/`, and section 8.3 holds the flashing procedure. Fix (RMM owner, 03 author; cross-document): align both RMM implementation texts with 05 and re-run `tools/render_rmm.py --check`; 05 lists the item in section 14.1. | Closed | Pending | | Open. `docs/process/rmm.json` read 2026-09-25: SWE-082 still says "working tree, review-ready, baselined" and SWE-085 still says `firmware/releases/` "holds the UF2 image, its SHA-256 and the VDD" and flashing "follows the documented flashing procedure in the operations handbook". The fix belongs to the RMM owner (03 author), as the finding said; 05 now tracks it as §14.1 AL-15 (Open, cites this finding). Closes when both texts match 05 §4.1, §8.1, §8.3 and `render_rmm.py --check` exits 0. |
| <a id="finding-8"></a>finding-8 | reviewer | Minor | CK-REQ-G7 | 05 section 9.1 class B tool list; section 13 SRR row | `tools/render_review_figures.py` (working tree, 2026-09-25; header: renders the figures "a review package and its slide deck show" into `docs/reviews/<REVIEW>/figures/`, package H10) produces review evidence, which is class B by the section 9.1 definition, yet it is absent from the class B list and from the section 13 TV schedule, the "single authoritative schedule". Fix: add it to section 9.1 class B and to the section 13 row of the gate at which its figures are first cited (SRR if the SRR package cites them), with its known-answer test `tools/tests/test_render_review_figures.py`. | Closed | Pending | | Closed. `tools/render_review_figures.py` is in §9.1 class B (review-package figures, row 33), in Table 4-1 row 28, in the §9.2 known-answer table (classes `ParserTests`, `DataKnownAnswerTests`, `RunTests` exist in `tools/tests/test_render_review_figures.py` at lines 90, 134, 259; `RepositoryTests` at 318 recorded separately) and in the §13 SRR TV list. |
| <a id="finding-9"></a>finding-9 | reviewer | Minor | CK-REQ-G2 | 05 status line | "revision 2, 2026-09-25 (independent review findings applied)" cites an independent review that has no record: no `INSP-NNN` for 05 existed before this one (`docs/reviews/SRR/checklists/` held only `technology-assessment.md`), and section 4.1 L1 makes the filled checklist the only review record (charter section 11 rule 2). Fix: name the source of the applied findings, or reword to "revision 2 (pre-record review comments applied)" and cite INSP-006 for L1. | Closed | Pending | | Closed. Status line now says revision 2 applied "pre-record review comments of the integrating session; no peer-review record exists for them" and revision 3 applies INSP-006 finding-1 to finding-9. |
| <a id="finding-10"></a>finding-10 | reviewer (iteration 3) | Minor | CK-REQ-G1 | 05 Table 4-1 row 13, Notes (line 99), with `docs/templates/adr.md` lines 10 to 11 | The pre-baseline exception added on 2026-09-26 (commit `0ab3d6e`) allows the one-time correction of the Accepted ADRs "under that INSP record with the owner's approval in the SRR decision memo", but (a) the edit was made at `0ab3d6e` before that approval (package decision 105 status: "The owner approves or reverses the ruling in the SRR decision memo") and the row states neither that the edit may precede the approval nor what is done if the owner reverses it (the decision 105 default is option (B)); (b) the fields it allows ("decision class, assumptions, hazard, section 4.1, errata and reviewer lines") do not name the new section 8 "Change log" that every corrected ADR gained (for example `docs/decisions/adr/ADR-001-class-a-rigor-and-review-gates.md` line 95); (c) the row 53 ADR template still says "Accepted ADRs are never edited except to change Status to Superseded", with no pointer to the exception, while the ADR README rule 2 cites row 13. Fix: state in row 13 that the correction is applied before the memo pending the owner's approval, and that a reversal is a commit restoring the pre-`0ab3d6e` ADR blobs with `reconciliation-srr.md` returned to controlling status; name the section 8 change log among the allowed lines; add the pointer to the template comment. | Lien: fix before PDR | Pending | | Lien (iteration 3, convergence rule of 2026-09-26). The exception is limited to the pre-`baseline/srr` period, excludes section 2 (Decision), and the owner ruling that decides it (package decision 105) is already on the SRR agenda, so the gap does not block the baseline. |
| <a id="finding-11"></a>finding-11 | reviewer (iteration 3) | Minor | CK-REQ-G2 | 05 status line (line 3); Table 4-1 row 9 (line 95) | The status line still reads "revision 3, 2026-09-25 ... returns the plan to that reviewer for verification", but the committed file carries the 2026-09-26 edits of row 13 (line 99, commit `0ab3d6e`) and AL-15 (line 626, "Closed 2026-09-26") with no revision entry, so the header does not identify the version the functional baseline would capture. Row 9 lists the schemas "on 2026-09-25" (nine files); `git ls-files 'docs/*schema.json'` at `adcfe09` gives eleven, adding `docs/design/allocation.schema.json` and `docs/plan/measurements.schema.json` (the pathspec already covers them, so the matching rule is unaffected). Fix: revision 4 dated 2026-09-26 in the status line naming the two changes and INSP-006 iteration 3; refresh the row 9 example list with its date. | Lien: fix before PDR | Pending | | Lien (iteration 3, convergence rule of 2026-09-26). Editorial accuracy of the header and of a dated example list; no control rule changes. |

## Readiness criteria (all true before the review starts)

| # | Criterion | Result | Evidence |
|---|---|---|---|
| R1 | The product validates: `tools/validate_docs.py` exits 0 | Met for the product; tool exit 1 on another file | 05 is Markdown and is not a schema-validated file. Run 2026-09-25 before this record: `validate_docs: 15 passed, 1 failed, 16 checked`, exit 1; the only failure is `docs/design/allocation.json` ("schema not found: docs/design/allocation.schema.json"), outside this product and outside the reviewer's scope (cross item). After this record: see Tool runs. |
| R2 | `tools/traceability.py` reports no violation for the ids in the file | N/A (plan defines no REQ or TC ids) | `traceability.py --report-only` exit 0: "231 requirements, 108 test cases, 82 violation(s), 52 warning(s)"; none concerns an id defined in 05 |
| R3 | Author self-check against sections A to G and the brief's acceptance criteria | Met at the re-issue (2026-09-26); Not met at iterations 1 to 3 | Re-issue: the section "Author self-check" (filed at `8ef95d3`, package item R7) lists AC-1 to AC-5 and answers A8 and G1 to G8 item by item; see "Re-issue". Earlier answers. Iteration 1: the author summary read "no new authoring this run"; no self-check return for revision 2 was available. Iteration 2: the author's return lists findings fixed (finding-1 to finding-6, finding-8, finding-9) and none disputed; that is a fix list, not a self-check against sections A to G. The review was conducted at the dispatching session's direction; `readiness_met: false` records it. Iteration 3 (2026-09-26): still Not met. No author self-check for 05 was supplied with the iteration 3 assignment, none is in the product, and a claude-context search for a 05 self-check against section G found none; package decision 115 lists the self-check shortfalls of INSP-001, 002, 003, 004, 010, 011 and 014 but not INSP-006 (cross item X-1). |
| R4 | Every `TBR` has owner, plan, close_by; no `TBD` | Met | `grep -n -i "TBD"` on the product: no hit; "TBR" occurs only as a subject (CSA item 13, FCA-09) |
| R5 | For a CR: impact assessment attached | N/A | Product is not a CR |

## Participants

Author agent `author:cm-plan` (not present). Reviewer agent `reviewer:cm-plan` (this record). Software assurance reviewer: not required at iterations 1 and 2 (07 section 2.1.1 as it then read, "Other process documents ... No"); required from 07 revision A.4 (section 2.1.1 line 117 at `adcfe09` routes the software CM plan 05 to the assurance reviewer in every criticality column; line 119 now excepts 05), and not yet dispatched at iteration 3 (07 section 22 line 856); filed on 2026-09-26 as the paired assurance record INSP-030 (`sa-reviewer:cm-plan`, `docs/reviews/SRR/checklists/cm-plan-05-software-assurance.md`). Owner: disposition of the findings at the review.

## A. Format and editorial

| Id | Answer | Evidence |
|---|---|---|
| CK-REQ-A8 | Yes | Terminology is consistent with the charter and 01 to 08: control classes CR, Log, Record, Mixed; levels L0 to L3; identifiers `FW-vX.Y.Z`, `HW-MB-rev<X>-<n>`, `ME-ENC-rev<X>-<n>`, `CWHT-A-NNN`, `TV-NNN` match charter sections 5 and 6 and `tools/toolchain.lock.md`; no em dash in the file (`grep` for U+2014: no hit). Minor editorial variance only: "charter §4 step 4" and "charter §4 item 4" name the same charter item (not raised as a finding). |

ITEMS N/A: CK-REQ-A1 to A7, B1 to B7, C1 to C8, D1 to D4, E1 to E6, F1 to F4 and the per-requirement validation table (the product is a plan, not a requirement file or CR; checklist product-type table row "Plans and process documents": "G (all items) and A8").

## G. Plans, process documents and decision records (SWE-087 b)

| Id | Answer | Evidence |
|---|---|---|
| CK-REQ-G1 | No | Expands charter section 8 (baselines, annotated tags pushed to `origin` github.com/robinonsay/cwht, signing optional, CR for non-editorial changes, FCA and PCA at SAR, SWE-136 tool validation), section 7 (change control) and section 11 rule 5, consistently. Compliance matrix SE-20 and SE-21 (`FC`, ETA approval in the SRR decision memo, 05 header) agree with the 05 status line and section 16. Customizations 1 and 2 of section 1 verified against SE HB section 6.5.1.2.2 ("The functional baseline is established at the SDR"; "The as-deployed baseline occurs at the ORR"). Disagreements: finding-1 (RMM SWE-045), finding-2 (baseline step 1 against 08 section 3.5 and package H1), finding-3 (internal), finding-4 (stale alignment rows), finding-7 (RMM SWE-082, SWE-085). Table 4-1 matching rule: every path of `git ls-files` (801 files) and of the untracked working tree on 2026-09-25 was checked by directory group against the pathspecs; each matches a row (for example `firmware/` row 25, `docs/reviews/SRR/figures/` row 33, `docs/research/sim/` row 40, `*.gitkeep` row 42, `docs/*schema.json` row 9 winning over the `docs/test_cases/` prefix). |
| CK-REQ-G2 | No | Every procedure step names its artifact, path and id scheme (sections 4.4, 5.2, 8.1, 8.2, 9.2; CR, TV, FW, HW-MB, ME-ENC, CWHT-A schemes); no "TBD", "as appropriate" or "should consider"; open decisions carry owner, gate and default (section 14). Exception: finding-9 (a claimed review with no record). Observation O-2 on the `RSK-NNN` placeholder. |
| CK-REQ-G3 | Yes | Section 3: owner as CCB chair and sole member, ETA, approver of baselines, waivers, releases, tool accreditation; Claude as CM function; independent reviewer duties (CR impact review, baseline record, VDD, FCA, delta audits); SWE-082 c persons who make changes (only Claude commits to `main`); software assurance checks. Approval points: sections 4.4 steps 4 to 6, 5.2 Dispositioned, 8.1 step 9, 9.2 step 3. |
| CK-REQ-G4 | No | Mirrored with the RMM: SWE-219 as tailored (section 2 product waiver, FCA-08), SWE-220 waiver per its own text (verified: NPR 7150.2D 3.7.5 "Any exceedance shall be reviewed and waived with rationale by the project manager or technical approval authority"), NPR 1441.1 retention (section 10.4), supplier flow-down not applicable (section 12). Mismatch: finding-1 (SWE-045). |
| CK-REQ-G5 | Yes | For CM scope: assets (repository, release images, vendor records), surfaces (push access, vendor documents, public repository), mitigations (only Claude pushes with the owner's SSH identity, section 3 and 10.3; branch and tag protection OQ-CM-001; `SHA256SUMS` and `git fsck --full`, section 10.3; CRC-32 image trailer verified at boot, section 8.1 step 4; redaction check `tools/redaction_check.py` before CDR, section 10.3) and their verification (git known-answer test with a corrupted loose object, section 9.2 table; `picotool verify` PCA-05; redaction check TV, section 13 CDR); CR impact field Cybersecurity (section 5.3). The software cybersecurity assessment itself is 07 section 16 (SWE-154, SWE-156, SWE-159), which 05 cites. |
| CK-REQ-G6 | No | Volatility is complete (section 5.4: V = (A + M + R) / N_start; thresholds 10 % and 20 %; `MSR-02` in `docs/plan/measurements.json`; red opens an RFA and a risk). Other CSA metrics lack thresholds and rules: finding-6. |
| CK-REQ-G7 | No | Tool claims checked on this machine on 2026-09-25: `sw_vers` 26.6.2; `git version 2.50.1 (Apple Git-155)`; `kicad-cli version` 10.0.6; OpenSCAD `2021.01`; FreeCAD `CFBundleVersion` 1.1.3; `picotool v2.3.0`; `rustc 1.98.0 (88d9e12ae 2026-08-18)`; `nightly-2026-08-24` present in `rustup toolchain list`; `git config gpg.format` and `tag.gpgSign` unset (exit 1); `origin git@github.com:robinonsay/cwht.git`; `docs/cm/` absent (no TV record, as 05 and the lock state). All equal `tools/toolchain.lock.md` sections 1 and 4. Honest limits stated: OpenSCAD cannot write STEP, kicad-cli time stamps (normalization table), MC/DC not measurable for Rust (FCA-08), emulator timing (via 04). Fixture and test names in the section 9.2 table exist: `tools/tests/fixtures/git/hello.txt`, `fixtures/slides/deck.adoc`, classes `ValidProjectTests`, `InvalidProjectTests`, `WordListTests`, `PeerReviewRecordTests`, `RepositoryTests`, `LocationGuard`. Kicad file counts (11 Gerbers, 1 job, 2 drill; 12 names, 7 PTH, 5 NPTH, 6 CPL rows, 7 BOM rows) equal `docs/research/pcbway-export-and-vendor-questions.md` F12. Defects: finding-5 (UF2 size), finding-8 (tool missing from the class B list and TV schedule). |
| CK-REQ-G8 | Yes | Verified in `docs/references/md/`: SE-20 at NPR 7123.1D 3.2.15.1 and its purposes 3.2.15.2 a to e (e cites NPR 1441.1); SE-21 at 3.2.16.1; SE HB 6.5.1.2 five CM elements, 6.5.1.2.2 baselines, 6.5.1.2.3 major, minor and waiver ("Authorized waivers do not constitute a change to a baseline"), 6.5.1.2.4 CSA, the audits activity (printed in the source as "6.4.1.2.5 Conduct Configuration Audits", so 05's form 'SE HB section 6.5.1.2 "Conduct configuration audits"' is the correct way to cite it), App. B FCA glossary entry, App. M topics and re-evaluation triggers, 6.6.1.2.1 DM plan topics, NPR 1441.1 in SE HB section 6.6 and references; NPR 7150.2D SWE-079 (5.1.2), 080 (5.1.3), 081 (5.1.4), 082 a to c (5.1.5), 083 (5.1.6), 084 (5.1.7), 085 (5.1.8), 045 (5.1.9), 042 (3.1.10), 063 (4.4.7), 136 (4.4.8), 187 (4.5.4), 070 (4.5.6), 077 (4.6.3), 194 (4.6.4), 195 (4.6.5), 196 (4.6.6), 200, 201 (5.5.1), 203 (5.5.3), 219 (3.7.4 and its note), 220 (3.7.5); NPR 7150.2D section 6.1 items a to y (all 25 names match section 11); NPR 7123.1D App. G Table G-11 entrance item 3 sub-items 6 ("Technical data package that has been updated to include all test results") and 8 ("Baselined as-built hardware and software documentation"). No NASA requirement is presented as a quotation it is not. |

## Observations (not findings)

- **O-1 (section 13 SRR row, execution, package H17).** Section 13 requires "this plan, `tools/toolchain.lock.md` and the three templates committed on `main` with `Refs: SRR` before the independent L1 record is filed". The reviewed commit `4e3f891` carries no `Refs: SRR` trailer (its trailer block holds only `Co-Authored-By`). This is an execution item of the SRR preparation, not a plan defect; Claude records it when the H17 commits are made.
- **O-2 (section 14, OQ-CM-001 default).** "risk `RSK-NNN` entered by Claude" uses a placeholder id; the SRR decision list (package decision 15) carries the question. When the default applies, the risk id replaces the placeholder.
- **O-3 (slug).** 01 section 13 gives the slug pattern `plan-<document-stem>` (`plan-05-configuration-and-data-management`); this record uses `cm-plan-05` as the dispatching session assigned it. `validate_docs.py` accepts both.
- **O-4 (07 cross reference).** `docs/process/07-software-engineering-plan.md` line 534 says "the ten steps of `docs/process/05-configuration-and-data-management.md` section 8.1"; 05 section 8.1 has twelve steps. The fix belongs to 07 (cross item), not to 05.
- **O-5 (SRR TV records, package H12).** 05 section 13 requires nine TV records at SRR; `docs/cm/tool-validation/` does not exist on 2026-09-25. This is the H12 shortfall already listed in the package, not a defect of the plan.

## Tool runs (2026-09-25)

| Command | Exit | Result |
|---|---|---|
| `.venv/bin/python tools/validate_docs.py` (before the record) | 1 | 15 passed, 1 failed: `docs/design/allocation.json` has no schema file (outside scope) |
| `.venv/bin/python tools/traceability.py --report-only` | 0 | 231 requirements, 108 test cases, 82 violations, 52 warnings (report-only mode) |
| `.venv/bin/python tools/validate_docs.py` (after the record, iteration 1) | 1 | this record PASS as a peer_review_record; the only failure `docs/design/allocation.json` |
| `.venv/bin/python tools/validate_docs.py` (iteration 2, after the disposition) | 1 | 23 passed, 1 failed, 24 checked; this record PASS as a peer_review_record; the only failure is still `docs/design/allocation.json` ("schema not found: docs/design/allocation.schema.json"), outside the product and the reviewer's scope |
| `.venv/bin/python tools/traceability.py --report-only` (iteration 2) | 0 | 231 requirements, 111 test cases, 76 violations, 42 warnings; none concerns an id defined in 05 |
| `.venv/bin/python tools/render_rmm.py --check` (iteration 2, for finding-7) | 1 | fails on SWE-023 and SWE-051 status rules (not rows of finding-7); rows SWE-082 and SWE-085 unchanged, so finding-7 is not closed |

## Completion criteria (SWE-088 b, c)

Iteration 1: not met: two Major findings were open (finding-1, finding-2) and R3 was not met. Iteration 2: zero open Major findings; one Minor finding (finding-7) is neither fixed nor deferred with an owner decision reference, and R3 is still not met. Verdict NEEDS CHANGES. Findings stay open until the software lead marks them Verified after re-reading the corrected file.

## Closure (iteration 2, 2026-09-25)

Re-review of revision 3 of the product (working tree, blob `40d45f4fd6e5109a1f1825f23797ccb0f62d97bd`, uncommitted; base commit `4e3f891`), by `reviewer:cm-plan`, independent of the author, who edited none of the product. The author reported finding-1 to finding-6, finding-8 and finding-9 fixed and none disputed. Each fix was checked against the product text and, where the fix cites other files, against those files (`docs/process/rmm.json`, `docs/process/02-requirements-and-traceability.md` AL-02-08, `docs/plan/semp.md` §5.14 and the customization table, `docs/process/07-software-engineering-plan.md` §11.2 MSR-02, `docs/templates/change-request.md`, `tools/tests/test_render_review_figures.py`, the repository root). The whole diff against `4e3f891` was read for new defects: none found (no em dash, no TBD).

| Disposition | Count | Findings |
|---|---|---|
| Closed (fix verified in the product) | 8 (Major 2, Minor 6) | finding-1, finding-2, finding-3, finding-4, finding-5, finding-6, finding-8, finding-9 |
| Disputed accepted | 0 | |
| Open | 1 (Minor) | finding-7: owned by the RMM author (`docs/process/rmm.json` SWE-082, SWE-085), tracked in 05 §14.1 AL-15 |

State of closed findings is set to Fixed; Verified and `record_status: Closed` are set by the software lead (template completion criteria; 07 section 10.2). Items answered No at iteration 1 now answer Yes except CK-REQ-G1, which stays No for finding-7 only. The record can close when finding-7 is fixed by the RMM author or deferred by the owner with a decision reference and a gate, and R3 is supplied or waived.

## Iteration 3 (2026-09-26): delta verification against the committed product

**Scope and baseline.** New reviewer invocation of the `reviewer:cm-plan` role, independent of the author; the product was not edited. Review baseline: HEAD `adcfe0946d2f1b5cd8f41a8f91eb4219a7fb99a1`. Committed blobs reviewed (`git rev-parse HEAD:<path>`): `docs/process/05-configuration-and-data-management.md` `63ed566240ffc7f055b65f93f579a6bb1498e9f1` (last commit `0ab3d6e`; earlier `b301df2` blob `eba19a9f`), `docs/process/rmm.json` `30fcde240eeb6a147359de8c5d8cdd93364dc9c8`. The iteration 2 blob `40d45f4f` is not in the object store, so the whole committed file (672 lines) was re-read rather than a diff; the diff `b301df2..0ab3d6e` for 05 is the single row 13 line. Convergence rule (lead SE direction 2026-09-26, charter section 4 item 3): only Major findings change products in this round; every Minor finding is dispositioned "Lien: fix before PDR".

**Search-first compliance.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (queries: RMM SWE-082 and SWE-085 texts; ADR never-edited rule and ruling R-1 option (A); author self-check of 05). `grep -n` and `git` were used afterwards only to pin lines. The Table 4-1 matching rule was re-checked by a scratch script over `git ls-files` at `adcfe09`: 1,057 paths, 0 unmatched.

### Disposition of every finding at HEAD

| Finding | Severity | Iteration 3 disposition | Evidence at HEAD (file and line) |
|---|---|---|---|
| finding-1 | Major | Closed | 05 line 656: SWE-045 "Fully compliant, as the RMM row SWE-045 (NPR 7150.2D §5.1.9, disposition FC) records"; line 55 owner row names the acquirer role, FCA and PCA at SAR, delta audits and "(SWE-045)"; agrees with `rmm.json` SWE-045 (FC) and `rmm.md` line 412 |
| finding-2 | Major | Closed | 05 line 189 (step 1 requires the Table 4-2 admission evidence and forbids tagging on an unlogged departure); Table 4-2 lines 170 to 185 cover every CR-class row of the Functional line (line 163: 1, 2, 3, 5, 6, 7, 9, 17, 27, 51, 52, 53) |
| finding-3 | Minor | Closed | 05 line 520 keeps the committed derived data of §10.1 indefinitely and limits non-retention to the gitignored derived data; consistent with line 491 and rows 18 and 33 (lines 104, 119) |
| finding-4 | Minor | Closed | 05 lines 621, 623, 625 (AL-10, AL-12, AL-14 Done with evidence); `02-requirements-and-traceability.md` line 758 AL-02-08 Closed; `docs/plan/semp.md` line 431 customization row 5 cites 05 §1; `ls result.json reveal.js` at the root: both "No such file or directory" (2026-09-26) |
| finding-5 | Minor | Closed | 05 line 380: "its UF2 4 kB", citing F5 and the TC-SW-TOOL-001-r1 artifacts (ELF 134,504 B, UF2 4,096 B) |
| finding-6 | Minor | Closed | 05 lines 305 to 312 (Table 6-1: four metrics with computation, threshold, response, storage); line 258 and CSA item 10 (line 300) cite it |
| finding-7 | Minor | Closed | `rmm.json` line 1734 row SWE-082 implementation: "Levels of control L0 Working, L1 Reviewed, L2 Controlled and L3 Released (docs/process/05-configuration-and-data-management.md section 4.1)"; line 1796 row SWE-085: "step 4 writes the ELF, UF2, firmware.map, picotool-info.txt and SHA256SUMS to firmware/releases/vX.Y.Z/ with the VDD beside it ... flashing, handling and delivery ... follow section 8.3"; both match 05 lines 70 to 75, 380 and 420 to 425; `render_rmm.py --check` exit 0 (`rmm.md` current); 05 AL-15 line 626 Closed 2026-09-26 |
| finding-8 | Minor | Closed | 05 line 446 (class B list names `tools/render_review_figures.py`), line 114 (row 28), line 475 (known-answer row), line 585 (SRR TV list); `tools/tests/test_render_review_figures.py` classes at lines 94, 138, 352 (`RepositoryTests` 411) |
| finding-9 | Minor | Closed | 05 line 3: revision 2 applied "pre-record review comments of the integrating session; no peer-review record exists for them" |
| finding-10 | Minor (new) | Lien: fix before PDR | Row 13 pre-baseline ADR exception (line 99): order of edit and approval, reversal rule, section 8 change log, template pointer |
| finding-11 | Minor (new) | Lien: fix before PDR | Status line (line 3) not updated for the 2026-09-26 edits; row 9 dated schema list (line 95) omits two schemas |

Disputed-accepted: none (the author disputed nothing). Open: none.

### New-defect scan (text changed since this record's quotes)

The whole committed file was read at `adcfe09`, with attention to the text that changed after the iteration 2 quotes: the row 13 exception (line 99), AL-15 (line 626), Table 4-2 (lines 170 to 185), Table 6-1 (lines 305 to 312), §8.1 step 4 (line 380), §10.4 retention (line 520) and §16 (lines 645 to 672). No Major defect found: the row 13 exception is bounded to the period before `baseline/srr`, keeps section 2 (Decision) untouched, and rests on package decision 105, which is already on the owner's agenda; the class-CR CR-from event of row 2 (SRR) has not occurred, so editing 05 itself needed no CR. Two Minor defects became liens (finding-10, finding-11). No em dash, no "TBD". Commit trailers: `b301df2` and `0ab3d6e` carry no `Refs:` trailer; §4.5 applies the trailer rules only from the SRR readiness declaration (line 218), so this stays observation O-1 (execution of the §13 SRR row), not a finding.

### Lien table

| Lien | Finding | Owner | Fix | Due |
|---|---|---|---|---|
| L-1 | finding-10 | 05 author (CM function); ADR template owner for part (c) | Row 13: edit-before-approval clause, reversal rule, section 8 change log named; pointer in `docs/templates/adr.md` | Before PDR (carried by the package as a Routine item) |
| L-2 | finding-11 | 05 author | Revision 4 status line dated 2026-09-26; refresh the row 9 example list with its date | Before PDR (carried by the package as a Routine item) |

### Why the record verdict stays NEEDS CHANGES

Every finding is Closed or a Lien, so the reviewer verdict is APPROVED with liens L-1 and L-2 under the convergence rule, and no Major finding is open. The record verdict cannot be APPROVED at iteration 3 for two reasons that are not findings: (1) readiness R3 is still not met (`tools/validate_docs.py` rejects an APPROVED record whose `readiness_met` is not true, SWE-088 b); (2) 07 section 2.1.1 at `adcfe09` (line 117) now requires an APPROVED software assurance verdict on 05 before the record verdict is APPROVED, and no paired assurance record exists. This is the third iteration (08 section 6 rule 1): Claude raises both items with the owner. When the author self-check is filed or the owner waives it, and the paired assurance record is APPROVED or the owner records that 05 is covered by the INSP-018 SA-013-1 result (07 line 856), the record is re-issued APPROVED without a further product review, provided the product blob is still `63ed5662`.

### Cross items (for Claude; outside this reviewer's scope)

- **X-1.** Add INSP-006 to package decision 115 (readiness R3 author self-check) or file the 05 author self-check against section G.
- **X-2.** Dispatch the paired software assurance record for 05 (07 section 2.1.1 line 117; 07 section 22 line 856), or record the owner's coverage decision; add 05 to `tools/validate_docs.py` `ASSURANCE_WHOLE_PRODUCTS` (INSP-010 observation O-6).
- **X-3.** Package section 2.3 row INSP-006 and section 15 item 35: finding-7 is Closed at `rmm.json` `30fcde24`; entrance row 12 and section 6.9 can cite this record as reviewer APPROVED with liens L-1, L-2, record NEEDS CHANGES on R3 and the assurance pairing only.
- **X-4.** Carry liens L-1 and L-2 as Routine items in the package lien list.

### Tool runs (iteration 3, 2026-09-26, HEAD `adcfe09`; working tree also held other reviewers' uncommitted record edits)

| Command | Exit | Result |
|---|---|---|
| `.venv/bin/python tools/validate_docs.py` (before this update) | 1 | 36 passed, 1 failed, 37 checked; the failure is `docs/reviews/SRR/checklists/risk-register-06.md` (another reviewer's record, being edited concurrently); drift notes list this record's iteration 2 blob `40d45f4f` against HEAD `63ed5662` |
| `.venv/bin/python tools/traceability.py --report-only` | 0 | 237 requirements, 170 test cases, 0 violations, 2 warnings (REQ-SYS-125, REQ-SYS-148 `SYS_UNALLOCATED`); none concerns 05 |
| `.venv/bin/python tools/render_rmm.py --check` | 0 | 100 rows; FC 75, T 17, NA 8; `rmm.md` current (finding-7) |
| `.venv/bin/python tools/render_compliance.py --check` | 0 | validation passed, rendered file current |
| `.venv/bin/python tools/render_risk.py --check --gate SRR --hazards docs/safety/hazards.json` | 0 | `register.md` current |
| `.venv/bin/python -m unittest discover -s tools/tests` | 1 | 392 tests, 1 failure: `RepositoryTests.test_repository_exit_zero`, which re-runs `validate_docs.py` over the working tree and fails on the concurrent `risk-register-06.md` edit, not on 05 |
| `.venv/bin/python tools/validate_docs.py` (after this update) | 0 | 37 passed, 0 failed, 37 checked; this record PASS as a peer_review_record with no drift note (its named blobs equal HEAD) |

## Verdict (returned by the reviewer)

```
ITERATION 3 (2026-09-26): REVIEWER VERDICT: APPROVED with liens L-1 (finding-10) and L-2 (finding-11); RECORD VERDICT: NEEDS CHANGES on readiness R3 and the missing 07 section 2.1.1 assurance verdict only. Closed 9 (finding-1 to finding-9; Major 2, Minor 7); Disputed accepted 0; Lien 2 (Minor, new); open 0. count of open Major findings 0. Reviewed blobs: 05 63ed5662, rmm.json 30fcde24 at HEAD adcfe09.

ITERATION 2 (2026-09-25): VERDICT: NEEDS CHANGES. Closed 8 (finding-1 to finding-6, finding-8, finding-9; Major 2, Minor 6); Disputed accepted 0; open 1 Minor (finding-7, RMM owner, 05 AL-15). count of open Major findings 0.

ITERATION 1:
VERDICT: NEEDS CHANGES
FINDINGS:
- [Major] CK-REQ-G4 (G1) 05 section 16 SWE-045 row: states Not applicable, RMM row SWE-045 is FC (owner participates in SAR FCA and PCA); align to the RMM.
- [Major] CK-REQ-G1 05 section 4.4 step 1: every functional-baseline CI must be at L1 with an INSP record, but rows 1, 2 (schedule, cost estimate, README), 9, 17, 27, 53 have no planned record and some no checklist; define the admission evidence per row or add the records.
- [Minor] CK-REQ-G1 05 section 10.4: derived-data retention contradicts section 10.1 and rows 18 and 33.
- [Minor] CK-REQ-G1 05 section 14.1 AL-10, AL-12, AL-14: statuses stale; mark Done with evidence.
- [Minor] CK-REQ-G7 05 section 8.1 step 4: rustos blinky UF2 is 4 kB, not 8 kB.
- [Minor] CK-REQ-G6 05 section 6 item 10: CR and trailer metrics lack thresholds and response rules.
- [Minor] CK-REQ-G1 rmm.json SWE-082 and SWE-085 implementation texts disagree with 05 sections 4.1, 8.1, 8.3 (RMM owner fixes).
- [Minor] CK-REQ-G7 05 sections 9.1 and 13: tools/render_review_figures.py missing from class B and the TV schedule.
- [Minor] CK-REQ-G2 05 status line: "independent review findings applied" cites a review with no record.
ITEMS N/A: CK-REQ-A1 to A7, B1 to B7, C1 to C8, D1 to D4, E1 to E6, F1 to F4 (product is a plan)
MEASUREMENTS: size=16 sections (642 lines, 55 Table 4-1 rows); items checked=9; items No=5; major=2; minor=7; fixed=0; deferred=0; iteration=1; turns=45; minutes=40
```

## Author self-check (readiness R3; package item R7; filed by the author 2026-09-26)

**Filed by:** the 05 author role `author:cm-plan` (Claude lead SE, CM function), not the reviewer. This section is the author return that readiness R3 asks for (template readiness row R3: "The author's return states the self-check against sections A to G below and lists the brief's acceptance criteria"; package decision 115 (a) default: "each author (Claude) files its self-check against the record's checklist sections before the repeat readiness review"). It writes nothing the reviewer owns: the front matter, the Readiness table, the findings and the verdict are unchanged, and the reviewer answers R3 on re-issue (package item R8). No product was changed (convergence rule, charter section 4 item 3).

**Product checked:** `docs/process/05-configuration-and-data-management.md` blob `63ed566240ffc7f055b65f93f579a6bb1498e9f1` (`git rev-parse HEAD:<path>` at HEAD `ade0e09`, equal to this record's `product_blob`; last commit touching it `0ab3d6e`; 672 lines) and `docs/process/rmm.json` blob `30fcde24` for the rows 05 mirrors. The product is unchanged since the iteration 3 review.

**Search-first compliance.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (query: author self-check section of an inspection record, readiness R1 to R4). `grep`, `sed -n`, `git` and read-only Python were used afterwards only to pin lines and recompute values.

**Acceptance criteria.** No author brief for revisions 2 and 3 of 05 is on record (iteration 1 R3 evidence). The author therefore states here the criteria the plan was written to, taken from the governing documents that 08 section 3.1 names for "plans and process documents":

| # | Acceptance criterion | Source | Author result |
|---|---|---|---|
| AC-1 | Every item of the applicable checklist (product-type row "Plans and process documents": G1 to G8 and A8) answers Yes, or No only on a finding that is Closed or a lien | template product-type table; charter section 4 item 3 | Met: see the item table; the No answers rest on liens finding-10 and finding-11 and on the author-found items below |
| AC-2 | The plan covers SE HB App. M topics, the five CM functions of SE HB section 6.5.1.2, SE-20 purposes a to e and SE-21 topics, and SWE-079 to SWE-085 with their RMM dispositions | 05 header; 01 section 4.6; SRR entrance row 12 | Met: section 16 maps each; every SWE id cited is a row of `rmm.json` |
| AC-3 | Every tracked file matches a Table 4-1 row | 05 section 4.2 matching rule; section 7.4 | Met: 1,069 of 1,069 tracked paths match at HEAD `ade0e09` (author script over `git ls-files`) |
| AC-4 | No `TBD`, no "as appropriate", no "should consider", no em dash; every TBR has owner, plan and close_by | template readiness R4; charter writing rules | Met: 0 hits for each; "TBR" occurs only as a subject (CSA item 13, FCA-09) |
| AC-5 | The file validates and the gate tools pass at the commit the record names | template readiness R1 | Met for 05 (Markdown, not schema-validated); tool runs below |

**Item-by-item self-check (author answers; the reviewer's answers above govern).**

| Id | Author answer | Evidence (re-checked 2026-09-26 at HEAD `ade0e09`) |
|---|---|---|
| CK-REQ-A8 | Yes | Control classes CR, Log, Record, Mixed; levels L0 to L3; identifiers `FW-vX.Y.Z`, `HW-MB-rev<X>-<n>`, `ME-ENC-rev<X>-<n>`, `CWHT-A-NNN`, `TV-NNN`, `OQ-CM-NNN` used the same way throughout; 0 em dashes (count of U+2014 in the file) |
| CK-REQ-G1 | No, on lien finding-10 only | Charter sections 7, 8 and 11 rule 5 expanded without contradiction (the ADR row 13 exception is the finding-10 lien, bounded to the period before `baseline/srr` and ruled by package decision 105). RMM rows SWE-045, SWE-082 and SWE-085 now agree with 05 sections 3, 4.1, 8.1 and 8.3 (finding-1 and finding-7 Closed). 07 section 13 now says "the twelve steps of ... section 8.1" (07 line 573), so observation O-4 is resolved on the 07 side |
| CK-REQ-G2 | No, on lien finding-11 and author item S-1 | Every procedure step names its artifact, path and id scheme (sections 4.4, 5.2, 8.1 to 8.4, 9.2); each open question in section 14 carries "Needed by" and a default. Status line and the row 9 dated list are finding-11 (lien); Table 4-2 record annotations are author item S-1 |
| CK-REQ-G3 | Yes | Section 3: owner as CCB chair, ETA, baseline, waiver, release and accreditation approver, acquirer role at FCA and PCA (SWE-045); Claude as CM function and sole committer to `main` (SWE-082 c); independent reviewer duties; software assurance checks. Approval points: section 4.4 steps 4 to 6, section 5.2 Dispositioned, section 8.1 step 9, section 9.2 step 3 |
| CK-REQ-G4 | Yes | Section 16 mirrors the RMM: SWE-045 FC, SWE-219 as tailored (FCA-08), SWE-220 waiver per NPR 7150.2D 3.7.5; author script: all 28 SWE ids cited in 05 are rows of `rmm.json` |
| CK-REQ-G5 | Yes | CM-scope assets, surfaces and mitigations with their verification (sections 3, 4.5 history integrity, 8.1 step 4 CRC-32 trailer, 10.3, 9.2 git known-answer test, PCA-05); the software cybersecurity assessment is 07 section 16, which 05 cites (section 5.3 Cybersecurity row) |
| CK-REQ-G6 | Yes | Table 6-1 gives the four CM metrics with computation, threshold, response and storage; volatility thresholds equal 07 section 11.2 MSR-02 (10 % and 20 %) |
| CK-REQ-G7 | Yes | Versions run by the author on 2026-09-26 equal `tools/toolchain.lock.md`: `sw_vers` 26.6.2; `git version 2.50.1 (Apple Git-155)`; `rustc 1.98.0 (88d9e12ae 2026-08-18)`; `picotool v2.3.0`; `kicad-cli` 10.0.6; `nightly-2026-08-24` in `rustup toolchain list`. Honest limits stated (OpenSCAD cannot write STEP, kicad-cli time stamps, MC/DC for Rust via FCA-08). For the section 13 SRR TV list, the records `docs/cm/tool-validation/TV-001` to `TV-010` now exist, one per tool that section 13 names; their review and accreditation are package item H12 execution (accreditation: package decision 114), not plan content |
| CK-REQ-G8 | Yes | Author script: every `SWE-NNN` cited in 05 (28 ids) has a page in `docs/references/md/swehb/` and appears in the NPR 7150.2D corpus text; every `SE-NN` cited (SE-17, SE-18, SE-20, SE-21, SE-67) appears in the NPR 7123.1D corpus text; no NASA text is presented as a quotation it is not |

**Author-found items (offered to the reviewer; not findings until the reviewer files them).**

- **S-1 (Minor in the author's view, CK-REQ-G2; stale execution annotations).** Table 4-2 (lines 175 to 183) marks records "not yet in H1" for 01, 02, 04, 06, 08, the schedule and cost estimate, the compliance matrix and the TC-SYS cases. At HEAD these records exist: INSP-019 (01), INSP-020 (02), INSP-021 (04), INSP-022 (08), INSP-023 (schedule and cost estimate), INSP-024 (compliance matrix), INSP-025 (TC-SYS). The admission rule of the table is correct; only the annotations are dated. The author proposes to fix them with finding-11 in revision 4, before PDR, as a lien; no product change in this run.
- **S-2 (information, not a defect of 05).** Section 14 OQ-CM-001 default names "risk `RSK-NNN` entered by Claude"; the question is on the SRR decision list (package decision 15) and no branch-protection risk is in `docs/risk/register.json` at HEAD, which is correct while the question is undecided (observation O-2 stands).
- **S-3 (cross item, not a defect of 05).** The 07 section 2.1.1 routing makes an APPROVED assurance verdict on 05 a condition of this record's APPROVED verdict; the paired record is package item R6 (or decision 118 (b)). The self-check does not discharge it.

**Tool runs by the author (2026-09-26, HEAD `ade0e09`, working tree also holding other agents' uncommitted record edits).**

| Command | Exit | Result |
|---|---|---|
| `.venv/bin/python tools/validate_docs.py` (before this section) | 1 | 47 passed, 1 failed, 48 checked; the failure is `docs/reviews/SRR/checklists/hazard-analysis.md` (record drift against the `ade0e09` hazards commit, another agent's R9 work); this record PASS |
| `.venv/bin/python tools/traceability.py --report-only` | 0 | 238 requirements, 170 test cases, 0 violations, 3 warnings; none concerns 05; the rewritten `docs/vv/traceability-report.md` and `traceability.json` were restored with `git checkout` |
| author script over `git ls-files` with the section 4.2 matching rule | 0 | 1,069 tracked paths, 0 unmatched |

**Author statement.** The author has re-read 05 against checklist items A8 and G1 to G8 and against AC-1 to AC-5. The author disputes no finding, accepts liens finding-10 and finding-11 for PDR, and adds S-1 for the same revision.

## Re-issue (2026-09-26, SRR package item R8; no further product review)

**Scope and independence.** Written by a new invocation of `reviewer:cm-plan` in the reviewer role. It did not author 05, the RMM, the author self-check above or INSP-030, and it edited no product file and no other record. It re-issues this record without a further product review, as iteration 3 ("Why the record verdict stays NEEDS CHANGES") and package items R6, R7 and R8 provide: the two holds named there were readiness R3 and the missing 07 section 2.1.1 assurance verdict, and neither was a finding. The convergence rule of 2026-09-26 (charter section 4 item 3) applies: only Major findings change products, and every Minor finding stays a lien, "fix before PDR".

**Search first.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (queries: the peer-review record readiness items R1 to R4 and the author self-check; the 07 section 10.2 paired-form completion rule for the record and assurance verdicts). `grep -n`, `sed -n`, `git` and read-only Python were used afterwards only to pin lines and recompute the values the author self-check states.

**Product state.** HEAD `1af795cef0234e80f9fc70306f0f39471b58d100`. `git rev-parse HEAD:<path>` and `git hash-object` equal the blobs named in `product_files`: 05 `63ed5662`, `rmm.json` `30fcde24` (2 of 2). `git log adcfe09..HEAD` on both paths is empty, so no product changed and no delta verification is needed. The inputs that changed after `adcfe09` (`hazards.json` 0.4.3-pha at `ade0e09`, OQ-SAF statuses only; SW-KEYER `requirements.json` at `f2e02aa`) are not cited by any finding or answer of this record.

**Readiness R3 against the author self-check.** R3 of `docs/templates/peer-review-checklist-requirements.md` revision C reads "The author's return states the self-check against sections A to G below and lists the brief's acceptance criteria". The section "Author self-check" meets it:
- It lists five acceptance criteria (AC-1 to AC-5), each with its source and result. It states that no author brief for revisions 2 and 3 is on record and takes the criteria from the governing documents 08 section 3.1 names for "plans and process documents"; every criterion traces to a governing document and none is weaker than the checklist.
- It answers every applicable item (A8, G1 to G8; the product-type row makes A1 to F4 N/A for a plan) with evidence, and its No answers rest on the liens finding-10 and finding-11 and on its item S-1.
- It names the product blob it checked, `63ed5662`, equal to `product_blob` and to HEAD.
- It is filed by `author:cm-plan` and leaves the reviewer's fields unchanged (checked in the `8ef95d3` diff: only the appended section).

Spot checks of the author's claims at HEAD `1af795c`: the 28 distinct `SWE-NNN` ids cited in 05 are all rows of `rmm.json` (100 rows); 0 em dashes and 0 `TBD` in 05; 07 line 573 reads "the twelve steps of `docs/process/05-configuration-and-data-management.md` section 8.1", so observation O-4 is resolved on the 07 side; Table 4-2 still carries the "not yet in H1" annotations the author reports as S-1. All agree.

**Author-found items.** S-1 (dated "not yet in H1" annotations in Table 4-2) is accepted as an observation of the same class and fix vehicle as lien finding-11 (the dated header and row 9 list of revision 4, before PDR); it is recorded as observation O-6 below, not as a new finding, and the lien L-2 fix covers it. S-2 restates observation O-2. S-3 is discharged by INSP-030.

- **O-6 (Table 4-2 annotations, author item S-1).** Lines 175 to 183 mark records "not yet in H1" that exist at HEAD (INSP-019 to INSP-025). Fixed with lien L-2 in revision 4 before PDR.

**Pairing (07 sections 2.1.1 and 10.2; 01 section 13 paired form).**

| Check | Result |
|---|---|
| Paired record exists and is committed | `docs/reviews/SRR/checklists/cm-plan-05-software-assurance.md`, `id: INSP-030`, committed at `898d582` |
| It names this record | `paired_record: INSP-006` |
| Same product blob | INSP-030 `product_files` and `product_blob` name 05 `63ed566240ffc7f055b65f93f579a6bb1498e9f1`, this record's blob, equal to HEAD |
| Its assurance verdict | `assurance_verdict: APPROVED`, `reviewer_verdict: APPROVED`; 0 Major, 4 Minor findings, each "Lien: fix before PDR" (finding-1 to finding-4) |
| Assurance reviewer distinct from author and file reviewer | `sa-reviewer:cm-plan`, distinct from `author:cm-plan` and `reviewer:cm-plan` |
| No INSP-006 finding re-opened or disputed | INSP-030 section "Concurrence with INSP-006": agrees with the closure of finding-1 to finding-9 and the liens finding-10 and finding-11 |

This record now carries `paired_record: INSP-030`, `assurance_reviewer_agent` naming the INSP-030 reviewer and `assurance_verdict: APPROVED`, the paired record's `assurance_verdict`, as 07 section 10.2 and 01 section 13 require of the file review in the paired form. INSP-030's own record `verdict` reads NEEDS CHANGES on its readiness R3 only; 07 section 10.2 conditions the product record on the assurance review being APPROVED, which it is. The 05 author self-check filed here also answers INSP-030 readiness R3 ("This record's verdict follows the INSP-006 R3 outcome", INSP-030 R3 row); INSP-030's re-issue belongs to its reviewer (cross item X-5).

**Findings at the re-issue.** No finding changes state and no new finding is raised.

| Finding | Severity | State | Closes on |
|---|---|---|---|
| finding-1, finding-2 | Major | Closed (iteration 3) | |
| finding-3 to finding-9 | Minor | Closed (iteration 3) | |
| finding-10 | Minor | Lien: fix before PDR | Lien L-1 (05 author; ADR template owner for part (c)) |
| finding-11 | Minor | Lien: fix before PDR | Lien L-2 (05 author), with observation O-6 |

No Major finding is open and none waits on an owner ruling. The four INSP-030 liens are carried by INSP-030, not by this record.

**Answers changed at the re-issue.** R3 changes from Not met to Met. CK-REQ-G1 stays No (finding-10, lien) and CK-REQ-G2 stays No (finding-11, lien); every other item stays Yes.

**Completion criteria (SWE-088 b, c; 07 section 10.2) at the re-issue: met.** Reviewer verdict APPROVED; assurance verdict APPROVED (INSP-030); readiness met; zero open Major findings; the named blobs equal HEAD. `verdict: APPROVED` (with liens finding-10 and finding-11). `record_status` is left for the software lead, who sets `Closed` when the liens are dispositioned (07 section 10.2).

**Cross items (outside this record's scope).**
- **X-5.** INSP-030 readiness R3 is answered by the 05 author self-check in this record (`8ef95d3`); its reviewer re-issues it (package item R8).
- **X-6.** Package section 2 rows H1 (b) and (c), section 2.1 items R6 and R7 (INSP-006 part) and the section 2.4 row for INSP-006: record verdict APPROVED with liens finding-10 and finding-11; paired with INSP-030; the INSP-006 part of R8 is done.
- **X-7.** Iteration 3 cross item X-2 (add 05 to `tools/validate_docs.py` `ASSURANCE_WHOLE_PRODUCTS`) is unchanged and remains with the tool owner.

**Tool runs (re-issue, repository root, `.venv/bin/python`).** The results are in the verdict block below.

**Wording edits to earlier text (no change of meaning).** `tools/validate_docs.py` treats any line holding a `finding-<n>` anchor with the word "Major" and the capitalized state word as an open Major finding. Historical lines that report counts or iteration states with the capitalized word were reworded to lower case ("open", "count of open Major findings 0") so that the APPROVED verdict validates; no state, count or disposition changed.

```
RE-ISSUE (2026-09-26, HEAD 1af795c, package item R8): VERDICT: APPROVED (with liens finding-10, finding-11)
READINESS: R1 Met, R2 N/A, R3 Met (author self-check at 8ef95d3), R4 Met, R5 N/A
PRODUCT: 05@63ed566240ffc7f055b65f93f579a6bb1498e9f1, rmm.json@30fcde240eeb6a147359de8c5d8cdd93364dc9c8 (equal to HEAD, 2/2)
PAIRING: INSP-030 (05 software assurance) assurance_verdict APPROVED, 0 Major, 4 Minor liens, same blob
FINDINGS: finding-1 to finding-9 Closed; finding-10, finding-11 Minor, Lien: fix before PDR; open Major 0; new 0
MEASUREMENTS (re-issue): blobs equal HEAD 2/2; turns=8; minutes=15; cumulative turns=93, minutes=105; iteration=3 (re-issue)
TOOLS: validate_docs.py exit 1, 48 passed, 1 failed (hazard-analysis.md, INSP-008 drift against the R9 hazards commit, another record); this record PASS with no drift note. traceability.py --report-only exit 0, 238 requirements, 170 test cases, 0 violations, 3 warnings (docs/vv outputs restored with git checkout). render_risk.py --check --gate SRR --hazards exit 0, 65 risks, register current. unittest discover: 392 tests, 1 failure (test_repository_exit_zero, from other agents' concurrent record edits: expectations.md, hazard-analysis.md)
```
