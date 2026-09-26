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
# product_commit: last commit touching the product (the working-tree file equals it: git status clean for the path)
product_commit: "4e3f8913366c60e79a9ace6a1b4f36f24adc3479"
# product_blob: git hash-object of the reviewed file. Iteration 1: 8e7a1c842bbe16278c7be015bf291782b25df988
# (equal to the commit). Iteration 2 (re-review of revision 3, working tree, uncommitted): below
product_blob: "40d45f4fd6e5109a1f1825f23797ccb0f62d97bd"
product_size: 16 sections, 670 lines (revision 3), Table 4-1 with 55 rows, Table 4-2 and Table 6-1 added
sprint: SRR-prep
author_agent: author:cm-plan (Claude lead SE, CM function; revision 2 of 2026-09-25)
reviewer_agent: reviewer:cm-plan
criticality: neither
# assurance_required: false; 07 section 2.1.1 row "Other process documents (docs/process/0N-*.md except 03 and this plan)" is No
assurance_required: false
assurance_reviewer_agent: none
iteration: 2
# readiness_met: false because R3 (author self-check return against sections A to G) is still not available; see Readiness
readiness_met: false
reviewer_verdict: NEEDS CHANGES
assurance_verdict: not-required
verdict: NEEDS CHANGES
findings_major: 2
findings_minor: 7
findings_open: 1
findings_fixed: 8
findings_verified: 0
findings_deferred: 0
assurance_findings_major: 0
assurance_findings_minor: 0
assurance_tasks_applied: []
deferred_rids: []
# items_no: iteration 1 answers; at iteration 2 only CK-REQ-G1 stays No (finding-7, cross-document)
items_no: [CK-REQ-G1, CK-REQ-G2, CK-REQ-G4, CK-REQ-G6, CK-REQ-G7]
# effort: iteration 1 (45 turns, 40 min) plus iteration 2 (12 turns, 15 min)
effort_turns: 57
effort_minutes: 55
record_status: Open
date: 2026-09-25
date_closed: null
---

# Peer review record INSP-006: CM and technical data management plan (05)

**Product:** `docs/process/05-configuration-and-data-management.md`, revision 2 (2026-09-25), commit `4e3f891`, blob `8e7a1c842bbe16278c7be015bf291782b25df988`. **Checklist:** `docs/templates/peer-review-checklist-requirements.md` revision C, section G (CK-REQ-G1 to G8) and CK-REQ-A8, per its product-type table row "Plans and process documents". **Minimum content judged:** CM plan per SE HB App. M and NPR 7150.2D SWE-079 to SWE-085 as dispositioned in `docs/process/rmm.json`; SE-20 and SE-21 per `docs/process/se-compliance-matrix.json`. **SRR context:** package `docs/reviews/SRR/package.md` section 2 item H1 (CM plan record) and H12 (the nine TV records 05 section 13 requires at SRR).

**Search-first compliance:** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` was run before every manual search (queries: peer-review record fields; SRR H items and CM plan; NPR 7123.1D SE-20 purposes; rustos blinky ELF and UF2 sizes; branch protection risk OQ-CM-001). `grep -n` was used afterwards only to pin lines.

## Findings

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to | Disposition (iteration 2, reviewer) |
|---|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | reviewer | Major | CK-REQ-G4, CK-REQ-G1 | 05 section 16, row SWE-045 | 05 states "SWE-045 (joint NASA/developer audits): Not applicable: no NASA counterpart; recorded in the RMM." The RMM row SWE-045 (`docs/process/rmm.json`, npr_section 5.1.9) has disposition `FC`: "The owner, in the acquirer role (03 section 6.2 role mapping), participates in the functional and physical configuration audits at SAR ... Planned for SAR". The plan misstates a Class A tailoring disposition, which charter section 1 and section 11 rule 5 allow only through the RMM. Fix: rewrite the row as fully compliant, citing section 7 (FCA and PCA) and section 3 (owner performs the hands-on PCA steps), and name SWE-045 in the owner row of section 3. | Fixed | Pending | | Closed. 05 revision 3 section 16 row SWE-045 now reads "Fully compliant, as the RMM row SWE-045 (NPR 7150.2D §5.1.9, disposition FC) records", citing §7.1, §7.2 and `docs/reviews/SAR/configuration-audit.md`; section 3 owner row names the acquirer role (03 §6.2, whose FC rule maps NASA acquirer and participant roles to the owner), FCA and PCA at SAR, §8.4 delta audits and "(SWE-045)". Agrees with `rmm.json` SWE-045 (disposition FC, implementation text read 2026-09-25). |
| <a id="finding-2"></a>finding-2 | reviewer | Major | CK-REQ-G1 | 05 section 4.4, baseline procedure step 1, with the Functional row of the baseline table | Step 1 requires "every CI listed for the baseline is at L1 (filled checklist with `id: INSP-NNN`)". The functional baseline lists rows 1 (charter), 2 (also `docs/plan/schedule.md`, `docs/plan/cost-estimate.md`, `docs/process/README.md`), 9 (schemas), 17 (TC-SYS cases citing L1 requirements, 108 cases in `docs/test_cases/`), 27 (`tools/toolchain.lock.md`, `tools/requirements.txt`) and 53 (templates). No record is planned for these in package section 2 H1, and 08 section 3.5 names no checklist for schemas, templates or the lock ("A review that needs a checklist that does not yet exist is not held"). As written, `baseline/srr` cannot be tagged without an unlogged departure from step 1. Fix: state in 05 which Table 4-1 rows need an INSP record to enter a baseline and what evidence admits the others (for example schemas and templates by `validate_docs.py` and the unit tests, the lock by its TV records, the charter by the owner's decision memo), or add the missing records to the H1 plan with Claude (carry to the package). | Fixed | Pending | | Closed. §4.4 step 1 now requires the Table 4-2 admission evidence of each row, not an INSP record for every CI; Table 4-2 covers every CR-class row of the Functional line (1, 2, 3, 5, 6, 7, 9, 17, 27, 51, 52, 53), names an INSP record where a checklist exists (row 17 uses `peer-review-checklist-test.md`, which exists) and tool, TV or decision-memo evidence where none exists (charter by the memo; schemas and templates by `validate_docs.py` and the unit tests; lock by TV records and AL-4), and step 1 forbids tagging on an unlogged departure (`docs/cm/deviations.md`, row 43). The records marked "not yet in H1" are a package cross item (package H1), an execution item, not a plan defect. |
| <a id="finding-3"></a>finding-3 | reviewer | Minor | CK-REQ-G1 | 05 section 10.4, Retention bullet | "derived data is not retained beyond the review that used it" contradicts section 10.1 (derived data "rendered figures, traceability report, CSA" kept in the repo), Table 4-1 row 18 (per-review traceability report and data file "are that review's evidence and are not regenerated after the review") and row 33 (review figures are Record class). Fix: limit the sentence to the gitignored derived data (`.stl`, `target/`, LTspice `.raw` and `.log` outside `docs/vv/`, KiCad backups). | Fixed | Pending | | Closed. §10.4 Retention now keeps the committed derived data of §10.1 (figures, traceability reports and data files, CSA; rows 18 and 33) indefinitely and limits non-retention to the gitignored derived data (`.stl`, `target/`, LTspice `.raw` and `.log` outside `docs/vv/`, KiCad backups). No contradiction remains. |
| <a id="finding-4"></a>finding-4 | reviewer | Minor | CK-REQ-G1 | 05 section 14.1, rows AL-10, AL-12, AL-14 | Statuses are stale against the repository on 2026-09-25: AL-10 says the 02 author must replace item 4 of 02 section 10.3, but 02 section 10.3 item 4 already names the 05 section 5.3 rows Risk, Software classification and tailoring, Operations and ConOps, Cybersecurity and Regulatory; AL-12 says the SEMP author must mirror the two customizations, but `docs/plan/semp.md` section 5.14 states both and cites 05 section 2 for waivers; AL-14 says removal of root `result.json` and `reveal.js/` is open, but neither exists at the repository root (`ls` exit 1 for both). Fix: mark each Done with the date and the evidence. | Fixed | Pending | | Closed. §14.1 AL-10, AL-12, AL-14 read Done 2026-09-25 with evidence. Re-checked: 02 AL-02-08 is Closed and says section 10.3 item 4 points to the 05 §5.3 rows; SEMP §5.14 states both customizations and cites 05 §2 for waivers, customization table rows 4 and 5 cite 05 §1; `ls result.json reveal.js` at the root exit 1, both "No such file or directory". |
| <a id="finding-5"></a>finding-5 | reviewer | Minor | CK-REQ-G7 | 05 section 8.1 step 4, last sentences | "a `rustos` blinky ELF is 132 kB, its UF2 8 kB": the UF2 is 4 kB. Evidence: `docs/research/rustos-toolchain-proof.md` F5 (`demo.uf2, 4096 B`; ELF 134,500 B in F4) and `docs/vv/reports/TC-SW-TOOL-001-r1/rustos-blinky.uf2` 4096 B, `rustos-blinky.elf` 134504 B. Fix: "its UF2 4 kB", citing F5. | Fixed | Pending | | Closed. §8.1 step 4 now reads "its UF2 4 kB", citing `docs/research/rustos-toolchain-proof.md` F5 and the TC-SW-TOOL-001-r1 artifacts (ELF 134,504 B, UF2 4,096 B), the values of the finding. |
| <a id="finding-6"></a>finding-6 | reviewer | Minor | CK-REQ-G6 | 05 section 6, CSA item 10; section 5.2 cycle-time targets | Only requirements volatility (section 5.4) has source, thresholds (10 % yellow, 20 % red), storage (`MSR-02` in `docs/plan/measurements.json`) and a response rule. The other CSA metrics (open CR count and age, CR cycle time, count of commits lacking mandatory trailers) have no threshold or analysis rule in 05; the SEMP section 5 CM row gives "CIs changed after their baseline without a CR or `Editorial:` trailer: 0". Fix: state for each metric its threshold (for example 0 commits lacking trailers; a CR older than its section 5.2 target is flagged) and the response (RID or RFA at the next review), and its storage location. | Fixed | Pending | | Closed. New Table 6-1 gives each of the four CM metrics its computation and source, threshold, response and storage: volatility (10 % and 20 %, matching 07 §11.2 MSR-02), open CRs and age (zero past the §5.2 target; CR template carries `date_opened`), CR cycle time (the §5.2 targets; two or more over target raise an RFA), commits lacking trailers (0, matching the SEMP §5 CM row; each is a RID, and a CR-less change to a class-CR CI is a deviation). §5.2 points to Table 6-1; CSA item 10 now cites it. |
| <a id="finding-7"></a>finding-7 | reviewer | Minor | CK-REQ-G1 | `docs/process/rmm.json` rows SWE-082 and SWE-085 against 05 sections 4.1, 8.1, 8.3 | RMM SWE-082 names the levels "working tree, review-ready, baselined"; 05 section 4.1 defines L0 Working, L1 Reviewed, L2 Controlled, L3 Released. RMM SWE-085 says `firmware/releases/` "holds the UF2 image, its SHA-256 and the VDD" and that flashing "follows the documented flashing procedure in the operations handbook"; 05 section 8.1 step 4 writes ELF, UF2, map, `picotool-info.txt` and `SHA256SUMS` into `firmware/releases/vX.Y.Z/`, and section 8.3 holds the flashing procedure. Fix (RMM owner, 03 author; cross-document): align both RMM implementation texts with 05 and re-run `tools/render_rmm.py --check`; 05 lists the item in section 14.1. | Open | Pending | | Open. `docs/process/rmm.json` read 2026-09-25: SWE-082 still says "working tree, review-ready, baselined" and SWE-085 still says `firmware/releases/` "holds the UF2 image, its SHA-256 and the VDD" and flashing "follows the documented flashing procedure in the operations handbook". The fix belongs to the RMM owner (03 author), as the finding said; 05 now tracks it as §14.1 AL-15 (Open, cites this finding). Closes when both texts match 05 §4.1, §8.1, §8.3 and `render_rmm.py --check` exits 0. |
| <a id="finding-8"></a>finding-8 | reviewer | Minor | CK-REQ-G7 | 05 section 9.1 class B tool list; section 13 SRR row | `tools/render_review_figures.py` (working tree, 2026-09-25; header: renders the figures "a review package and its slide deck show" into `docs/reviews/<REVIEW>/figures/`, package H10) produces review evidence, which is class B by the section 9.1 definition, yet it is absent from the class B list and from the section 13 TV schedule, the "single authoritative schedule". Fix: add it to section 9.1 class B and to the section 13 row of the gate at which its figures are first cited (SRR if the SRR package cites them), with its known-answer test `tools/tests/test_render_review_figures.py`. | Fixed | Pending | | Closed. `tools/render_review_figures.py` is in §9.1 class B (review-package figures, row 33), in Table 4-1 row 28, in the §9.2 known-answer table (classes `ParserTests`, `DataKnownAnswerTests`, `RunTests` exist in `tools/tests/test_render_review_figures.py` at lines 90, 134, 259; `RepositoryTests` at 318 recorded separately) and in the §13 SRR TV list. |
| <a id="finding-9"></a>finding-9 | reviewer | Minor | CK-REQ-G2 | 05 status line | "revision 2, 2026-09-25 (independent review findings applied)" cites an independent review that has no record: no `INSP-NNN` for 05 existed before this one (`docs/reviews/SRR/checklists/` held only `technology-assessment.md`), and section 4.1 L1 makes the filled checklist the only review record (charter section 11 rule 2). Fix: name the source of the applied findings, or reword to "revision 2 (pre-record review comments applied)" and cite INSP-006 for L1. | Fixed | Pending | | Closed. Status line now says revision 2 applied "pre-record review comments of the integrating session; no peer-review record exists for them" and revision 3 applies INSP-006 finding-1 to finding-9. |

## Readiness criteria (all true before the review starts)

| # | Criterion | Result | Evidence |
|---|---|---|---|
| R1 | The product validates: `tools/validate_docs.py` exits 0 | Met for the product; tool exit 1 on another file | 05 is Markdown and is not a schema-validated file. Run 2026-09-25 before this record: `validate_docs: 15 passed, 1 failed, 16 checked`, exit 1; the only failure is `docs/design/allocation.json` ("schema not found: docs/design/allocation.schema.json"), outside this product and outside the reviewer's scope (cross item). After this record: see Tool runs. |
| R2 | `tools/traceability.py` reports no violation for the ids in the file | N/A (plan defines no REQ or TC ids) | `traceability.py --report-only` exit 0: "231 requirements, 108 test cases, 82 violation(s), 52 warning(s)"; none concerns an id defined in 05 |
| R3 | Author self-check against sections A to G and the brief's acceptance criteria | Not met | Iteration 1: the author summary read "no new authoring this run"; no self-check return for revision 2 was available. Iteration 2: the author's return lists findings fixed (finding-1 to finding-6, finding-8, finding-9) and none disputed; that is a fix list, not a self-check against sections A to G. The review was conducted at the dispatching session's direction; `readiness_met: false` records it. |
| R4 | Every `TBR` has owner, plan, close_by; no `TBD` | Met | `grep -n -i "TBD"` on the product: no hit; "TBR" occurs only as a subject (CSA item 13, FCA-09) |
| R5 | For a CR: impact assessment attached | N/A | Product is not a CR |

## Participants

Author agent `author:cm-plan` (not present). Reviewer agent `reviewer:cm-plan` (this record). Software assurance reviewer: not required (07 section 2.1.1, "Other process documents ... No"). Owner: disposition of the findings at the review.

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

Iteration 1: not met: two Major findings were Open (finding-1, finding-2) and R3 was not met. Iteration 2: zero open Major findings; one Minor finding (finding-7) is neither fixed nor deferred with an owner decision reference, and R3 is still not met. Verdict NEEDS CHANGES. Findings stay Open until the software lead marks them Verified after re-reading the corrected file.

## Closure (iteration 2, 2026-09-25)

Re-review of revision 3 of the product (working tree, blob `40d45f4fd6e5109a1f1825f23797ccb0f62d97bd`, uncommitted; base commit `4e3f891`), by `reviewer:cm-plan`, independent of the author, who edited none of the product. The author reported finding-1 to finding-6, finding-8 and finding-9 fixed and none disputed. Each fix was checked against the product text and, where the fix cites other files, against those files (`docs/process/rmm.json`, `docs/process/02-requirements-and-traceability.md` AL-02-08, `docs/plan/semp.md` §5.14 and the customization table, `docs/process/07-software-engineering-plan.md` §11.2 MSR-02, `docs/templates/change-request.md`, `tools/tests/test_render_review_figures.py`, the repository root). The whole diff against `4e3f891` was read for new defects: none found (no em dash, no TBD).

| Disposition | Count | Findings |
|---|---|---|
| Closed (fix verified in the product) | 8 (Major 2, Minor 6) | finding-1, finding-2, finding-3, finding-4, finding-5, finding-6, finding-8, finding-9 |
| Disputed accepted | 0 | |
| Open | 1 (Minor) | finding-7: owned by the RMM author (`docs/process/rmm.json` SWE-082, SWE-085), tracked in 05 §14.1 AL-15 |

State of closed findings is set to Fixed; Verified and `record_status: Closed` are set by the software lead (template completion criteria; 07 section 10.2). Items answered No at iteration 1 now answer Yes except CK-REQ-G1, which stays No for finding-7 only. The record can close when finding-7 is fixed by the RMM author or deferred by the owner with a decision reference and a gate, and R3 is supplied or waived.

## Verdict (returned by the reviewer)

```
ITERATION 2 (2026-09-25): VERDICT: NEEDS CHANGES. Closed 8 (finding-1 to finding-6, finding-8, finding-9; Major 2, Minor 6); Disputed accepted 0; Open 1 Minor (finding-7, RMM owner, 05 AL-15). Open Major 0.

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
