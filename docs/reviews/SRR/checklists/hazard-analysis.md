---
# Peer-review record front matter (charter section 5; docs/process/01-lifecycle-and-reviews.md
# section 13 is the single field list; docs/process/08-agent-briefing.md section 3.2).
id: INSP-008
checklist: peer-review-checklist-safety
checklist_revision: A
checklist_file: docs/reviews/SRR/checklists/hazard-analysis.md
# product: the hazard analysis; hazards.json is its source of record, reviewed as one product
product: docs/safety/hazard-analysis.md
# product_commit: review baseline HEAD at iteration 3 (the last commit touching docs/safety/ is 1543c9f,
# 0.4.2-pha; the blobs are the same at both). Iteration 1 blobs (0.3.0-pha) are in the body table;
# iteration 2 re-read the uncommitted working-tree blobs hazard-analysis.md@c20281a7d6cf64f38d678537de895ca7908fc11f
# and hazards.json@89d0cbc323b2775d326cf7cd42bc637818ec96eb (0.4.0-pha), which are not in the object store.
# Iteration 3 read b5ce99e9 and 37d6cc83 (0.4.2-pha) at adcfe09. The iteration 3 delta verification (package item R17)
# reads the R9 status edit ade0e09 (0.4.3-pha), the last commit touching docs/safety/ at HEAD 860e84e.
# product_files: git rev-parse HEAD:<path> at 860e84e, 2026-09-26
product_commit: "ade0e09"
product_files: ["docs/safety/hazard-analysis.md@49ec53f8bbde37558c1c113a656b2125cd3fdec2", "docs/safety/hazards.json@c6bf757e815bea0f8ba8d6b90d9a618875833a24"]
data_file: docs/safety/hazards.json
data_file_version: 0.4.3-pha
product_size: 15 hazards, 117 controls at iteration 1 and 118 at iteration 2, 24 open questions at iteration 1 and 26 at iteration 2, 23 single point failure entries
sprint: SRR-prep
author_agent: "author:hazards (hazard analysis author, system safety engineer role; revision 0.3.0-pha for SRR readiness items H7, H8, H9)"
reviewer_agent: "reviewer:hazards"
criticality: neither
assurance_required: false
assurance_reviewer_agent: none
# iteration: stays 3 (validate_docs.py maximum); the R17 check of ade0e09 is the iteration 3 delta verification
iteration: 3
readiness_met: true
reviewer_verdict: APPROVED
assurance_verdict: not-required
verdict: APPROVED
# finding-14 and finding-15 are new at iteration 2, finding-16 at iteration 3; the iteration 3 delta verification raises none.
# Iteration 3: Closed (Verified) 13 (Major 3, Minor 10); Lien: fix before PDR 3 (Minor: finding-14, 15, 16),
# counted in findings_deferred (convergence rule of 2026-09-26, charter section 4 item 3)
findings_major: 3
findings_minor: 13
findings_open: 0
findings_fixed: 0
findings_verified: 13
findings_deferred: 3
assurance_tasks_applied: [swe-205 7.1 task 1, swe-205 7.1 task 2, swe-205 7.1 task 3, swe-205 7.1 task 4]
deferred_rids: []
# iteration 3 answers (iteration 1: R1, R2, CK-SAF-A7, C2, C4, C5, C6, D2, D3, D5, F1, F3, G1, G2, G3, G5;
# iteration 2: R1, CK-SAF-D5, CK-SAF-G1); both remaining No items carry only Minor liens
items_no: [CK-SAF-D5, CK-SAF-G1]
# effort: iteration 1 (46 turns, 55 min), iteration 2 (28 turns, 35 min), iteration 3 (36 turns, 45 min), iteration 3 delta verification (14 turns, 20 min)
effort_turns: 124
effort_minutes: 155
record_status: Open
date: 2026-09-25
date_closed: null
---

# Peer review record INSP-008: hazard analysis and hazard data (SRR rows 14 and 15; SWE-205)

**Products reviewed (working tree of 2026-09-25, identified by git blob hash):**

| File | Blob (`git hash-object`) | Base commit | State |
|---|---|---|---|
| `docs/safety/hazard-analysis.md` (revision 0.3.0-pha) | `4251e1ac27c3e50a8d697b7dce10242c8bc8257b` | `28e49e6` (0.2.0-pha there) | modified, uncommitted |
| `docs/safety/hazards.json` (`version` 0.3.0-pha) | `4f9f38fdd5917bf00fdffef270f0c777d53ce142` | `28e49e6` (0.2.0-pha there) | modified, uncommitted |

`product_commit` names the base commit; the reviewed content is the two blobs above (package item H17).

**Checklist applied.** `docs/templates/peer-review-checklist-safety.md` revision A, all sections (R1 to R5, CK-SAF-A1 to G5). **Record path.** The assignment names this path, `checklists/hazard-analysis.md`; the checklist's Record section gives the slug `safety-hazard-analysis`. The path was kept as assigned and the difference is reported to the lead SE (see Notes). **Minimum content judged:** SRR entrance row 14 (preliminary system safety analysis and safety-critical software determination; NPR 7123.1D App. G Table G-4 entrance 6.9; SWE-205) and row 15 (single point failure and fault tolerance philosophy stated, with paragraph and requirement ids; Table G-3 5.10, Table G-4 success criterion 14), `docs/process/01-lifecycle-and-reviews.md` section 4.3. It also judges the hazard-analysis part of package items H7, H8 and H9 (`docs/reviews/SRR/package.md` section 2).

**Search-first compliance.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search. Queries: the peer-review record front matter; the paddle watchdog 128-element timing; the 1.1310 SAR limits; the research HZ-candidate items. `grep -n` and read-only Python over the JSON files came afterwards, only to pin the lines the hits pointed at. The tool was available throughout.

**Method.** The reviewer re-derived each checked value from its source rather than from the analysis text:
- `hazards.json` was read with Python and compared with every requirement file, every test-case file and `docs/risk/register.json`.
- The analysis tables were recomputed: section 4 list and counts, section 6.2 union, section 7 Hazards column, section 8.2 list.
- `history` was diffed against `git show 28e49e6:docs/safety/hazards.json`.
- Every regulatory threshold was checked against `docs/references/md/regulatory/`.
- The quoted research numbers were checked against `docs/research/rf-exposure-evaluation.md` Table 5 and F7, `audio-output-and-hearing-safety.md` F22 to F25, `keyer-verification-and-key-input-network.md` and `regulatory-corpus-and-operators.md`.
- The package decision numbers were checked against `package.md` section 13.1.

## Findings

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to | Disposition (iteration 2) |
|---|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 (F-01) | reviewer | Major | CK-SAF-D2, CK-SAF-F3 | `hazards.json` HZ-001, HZ-003, HZ-004, HZ-005, HZ-006, HZ-008, HZ-010, HZ-012, HZ-014 `controls[].control_req_ids`; analysis section 9 item 1 | 40 hazard-to-requirement links run one way only. 23 `REQ-SW-KEYER` and 17 `REQ-TX` requirements list a hazard in `hazard_ids` that the hazard's controls do not name (`HAZARD_INVERSE` x40: HZ-004 15, HZ-008 11, HZ-006 4, HZ-001 3, HZ-010 3, HZ-003, HZ-005, HZ-012, HZ-014 1 each). The checklist rates a one-way link Major. 04 section 7.3 rule 6 says a `HAZARD_INVERSE` disagreement "blocks the readiness declaration of every gate". SWE-052 requires the trace both ways, and SWEHB swe-205 section 7.1 task 4 asks for it for the software requirements. Section 9 item 1 defers the L2 back-links to PDR on the strength of the schema description ("REQ-SYS ... at SRR, L2 at PDR") and the 02 T-08 SRR severity W; that conflicts with 04 rule 6. Fix: add each L2 requirement to the control it implements, so that the union holds and `HAZARD_INVERSE` reads 0. Or have the owner rule on the 02/04/schema conflict at SRR as recorded tailoring, and cite that ruling in section 9 item 1. | Verified | Pending | | Closed. `traceability.py --report-only` (2026-09-25, 0.4.0-pha) reports 0 violations and no `HAZARD_INVERSE`; the reviewer's recompute over every requirement file gives 0 inverse links and the same 40 L2 links now named in `controls[].control_req_ids` (HZ-004 15, HZ-008 11, HZ-006 4, HZ-001 3, HZ-010 3, HZ-003, HZ-005, HZ-012, HZ-014 1 each), union exact for all 15 hazards. The links were added, not removed (15 REQ-SW-KEYER and 14 REQ-TX requirements still carry `hazard_ids`). Section 9 item 1 withdraws the PDR deferral against 04 section 7.3 rule 6 and SWE-052. |
| <a id="finding-2"></a>finding-2 (F-02) | reviewer | Major | CK-SAF-F1 | `hazards.json` HZ-007 `causes`, HZ-010 `causes` C4 | HZ-007 has firmware role criteria c and e: rails enabled only with both cells at 2.5 to 4.3 V, transmit inhibit below 6.4 V, power-down below 6.0 V, 60 C discharge lock-out. Yet none of its eight causes is a software cause, so firmware inaction or incorrect action is not identified: a soft cut-off that does not act, a wrong threshold, rails enabled out of window. SWEHB swe-205 section 7.1 task 1 requires every contribution "by its action, inaction, or incorrect action". The checklist rates an unidentified software contribution Major. The analysis's own pattern exists in HZ-003 C4 and HZ-002 C4. HZ-010 likewise has no software cause for criterion c: C4 is classed Design although "the reset-default pull-down left enabled" is firmware pad configuration, and a debounce or stuck-input misclassification is not named. Fix: add Software-class causes to HZ-007 and HZ-010 (and reclass or split HZ-010 C4), and re-check the per-hazard F1 column. | Verified | Pending | | Closed. `hazards.json` HZ-007 C9 (inaction: soft cut-off or lock-out misscaled, stale, wrong threshold, stalled task) and C10 (incorrect action: rails enabled outside the window), class Software; HZ-010 C6 (pad configuration, split from the former C4, which is now silicon-only Design) and C7 (debounce or stuck-input misclassification), class Software. Both `firmware_role.statement` texts tie the causes to criteria c and e (HZ-007) and c (HZ-010) with no component change. Per-hazard F1 re-checked: Yes for both. |
| <a id="finding-3"></a>finding-3 (F-03) | reviewer | Major | CK-SAF-C4 | analysis section 8.1 item 7 table | The table claims to list every control of a Critical or Catastrophic hazard not verified by Test. It lists 6 requirements; 9 more control requirements of such hazards close by Analysis and are absent:<br>- REQ-SYS-113 (HZ-003 K1, K7, RSK-006)<br>- REQ-SYS-075, REQ-SYS-157, REQ-SYS-158 (HZ-005 K4, RSK-017)<br>- REQ-SYS-172 (HZ-006 K4, RSK-016)<br>- REQ-SYS-014, REQ-SYS-015 (HZ-008 K4, RSK-011)<br>- REQ-SYS-137, REQ-SYS-138 (HZ-015 K3, "Analysis accepted per RSK-004")<br>RSK-004 names no hazard (`related.hazard_ids` empty) and does not carry HZ-015, which RSK-034 carries. The item 7 table is the list the owner accepts as SMA TA for SRR row 15, so the baseline would record an incomplete acceptance. Fix: add the nine rows with the accepting risk. Re-point REQ-SYS-137 and 138 to RSK-034, or record why RSK-004 accepts them (a cross item for the requirements author). | Verified | Pending | | Closed. Section 8.1 item 7 table now has 13 rows; the reviewer's recompute of every `control_req_ids` entry of a Critical or Catastrophic hazard whose `verification_method` is not Test (L1 and L2) finds no requirement missing (includes REQ-SYS-113, 075, 157, 158, 172, 014, 015, 137, 138, REQ-TX-005, 006, 122, 124). Every listed requirement's `verification_note` begins "Analysis accepted per RSK-". The rows whose risk does not carry the hazard (RSK-004 for REQ-SYS-137, 138; RSK-002 for REQ-SYS-010; RSK-016 for REQ-SYS-122) say so and route the correction as OQ-SAF-026, the cross route the fix named. |
| <a id="finding-4"></a>finding-4 (F-04) | reviewer | Minor | CK-SAF-C6 | analysis section 8.2 | 5 of the 23 `single_point_failures` entries in `hazards.json` are not in the section 8.2 list:<br>- HZ-002: the cells themselves<br>- HZ-005: amplifier gain-select pins<br>- HZ-006: operator discipline as the only barrier once the guest lock is released; a Critical hazard, Table G-4 success criterion 14<br>- HZ-007: holder leaf-spring contact<br>- HZ-011: the unrated Pico 2 VBUS path<br>Fix: add the rows with disposition and closing gate, or remove the entries from the data file with a reason. | Verified | Pending | | Closed. Section 8.2 rows 18 to 22 add the HZ-002 cells, HZ-005 gain-select pins, HZ-006 operator discipline (with REQ ids and the Critical-D Medium SAR acceptance), HZ-007 leaf-spring contact and HZ-011 Pico 2 VBUS path, each with disposition and closing gate; 23 `single_point_failures` entries counted in `hazards.json`, rows 1 to 22 with row 5 carrying two. |
| <a id="finding-5"></a>finding-5 (F-05) | reviewer | Minor | CK-SAF-C5 | analysis section 8.1; `docs/requirements/sys/requirements.json` rationales (cross) | The fault tolerance philosophy does not show in the requirements as row 15 asks ("paragraph and requirement ids").<br>(a) Eleven requirement rationales cite section 8.2 candidates by the 0.1.0 numbering, which section 8.2 no longer uses. REQ-SYS-118 and REQ-SYS-155 cite "candidate 6", the cell NTC row; the PA thermistor is now row 8. Also: REQ-SYS-082 and REQ-SYS-099 candidate 4 (now row 6); REQ-SYS-018 and REQ-SYS-151 candidate 8 (now row 10); REQ-SYS-156 candidate 9 (now row 11); REQ-SYS-105 and REQ-SYS-152 candidate 11 (now row 14); REQ-SYS-071 candidate 7 (now row 9); REQ-SYS-132 candidate 13 (now row 16).<br>(b) REQ-SYS-081 and REQ-SYS-083 say "three independent overcharge layers", which section 8.1 item 3 withdraws.<br>(c) REQ-SYS-118 and REQ-SYS-155 cite item 5 (Marginal hazards) for HZ-003, which has been Critical since 0.2.0 (item 4).<br>(d) Items 3, 5 and 6 of section 8.1 name no requirement ids.<br>Fix: name the requirement ids per item in section 8.1, and route the rationale corrections to the requirements author. | Verified | Pending | | Closed for the product. Section 8.1 items 3, 5 and 6 now name requirement ids (item 3 REQ-SYS-081, 082, 083, 084, 085, 086, 087, 088, 089, 096 to 099, 166; item 5 REQ-SYS-106, 049, 050, 079, 092, 002, 020, 055, 180, 110, 111, 017, 018, 151; item 6 REQ-SYS-122, 124), and item 4 carries HZ-003. The rationale corrections (a) to (c) are routed to the requirements author in section 11.2 and OQ-SAF-025 item 2 with the exact row mapping; `requirements.json` still carries the stale citations (reviewer check of REQ-SYS-118, 155, 082, 099, 018, 151, 156, 105, 152, 071, 132, 081, 083), tracked under finding-8 as an SRR-due author edit. |
| <a id="finding-6"></a>finding-6 (F-06) | reviewer | Minor | CK-SAF-D3 | requirement rationales named by `control_req_ids` (cross) | 27 control-to-requirement pairs have a rationale that names neither the hazard nor the control id (analysis section 9 item 2).<br>Hazard missing (15):<br>- REQ-SYS-054 for HZ-001 K3, HZ-003 K3, HZ-006 K6, HZ-012 K2<br>- REQ-SYS-180 for HZ-001 K10, HZ-003 K10, HZ-006 K10, HZ-012 K6, HZ-014 K8<br>- REQ-SYS-002 and REQ-SYS-005 for HZ-004 K7<br>- REQ-SYS-087 for HZ-007 K3<br>- REQ-SYS-010, REQ-SYS-015, REQ-SYS-151 for HZ-008<br>Control id missing (12):<br>- REQ-SYS-055 for HZ-001 K9, HZ-003 K8, HZ-006 K9<br>- REQ-SYS-130 for HZ-002 K4<br>- REQ-SYS-121 for HZ-006 K4<br>- REQ-SYS-008, 009, 017, 018 for HZ-008 K1, K2, K4, K5<br>Fix: the requirements author adds the hazard and control ids; the analysis lists the correction in section 11.2. | Verified | Pending | | Closed for the product. Section 11.2 "Requests recorded at 0.4.0-pha" and OQ-SAF-025 item 1 list the 27 L1 pairs and the 14 L2 pairs added at this revision. The rationale edits themselves are the requirements author's, tracked under finding-8. |
| <a id="finding-7"></a>finding-7 (F-07) | reviewer | Minor | CK-SAF-D5, R2 | analysis section 9 item 1 | The statement is stale. REQ-SYS-180, 181 and 182 no longer raise `HAZARD_REQ_NOT_TESTED`, because TC-SYS-108, 109 and 110 cite them. Meanwhile the section does not mention the 27 `HAZARD_REQ_NOT_TESTED` violations that `traceability.py` reports for hazard-tracing L2 requirements: REQ-SW-KEYER-002, 019 to 031, 033 (15; SWE-192, no exception) and REQ-TX-002, 003, 004, 007 to 015 (12). Readiness R2 is therefore not met. Fix: restate item 1 from the current tool output. The closing Test cases for `sw-keyer` and `tx` are a cross item for the test author. | Verified | Pending | | Closed. Section 9 item 1 is restated from the current tool output (0 violations; two `SYS_UNALLOCATED` warnings outside the analysis), which the reviewer reproduced (exit 0, 231 requirements, 167 test cases, 0 violations, 2 warnings). The 27 `HAZARD_REQ_NOT_TESTED` no longer appear. R2 now Yes. |
| <a id="finding-8"></a>finding-8 (F-08) | reviewer | Minor | CK-SAF-G1 | `hazards.json` OQ-SAF-006, 007, 017, 020, 021, 022, 023; analysis section 11.2 | Seven questions with `close_by: SRR` are not answered and wait on an author's edit, not an owner ruling, so the package decision list does not carry them. Package section 18.1 says none may stay Open at the readiness declaration unless the owner rules it to a later gate. The statuses are accurate; the gap is the missing action. Of these, OQ-SAF-020 item 3 (RSK-046 to HZ-008) needs an edit in `hazards.json` itself. Fix: the named authors act, or the owner re-dates each question in the SRR memo and the file records the new `close_by`. Package item H7 stays open until then. | Verified | Pending | | Open (Minor) at iteration 2; Closed at iteration 3 (see Iteration 3). The file-side actions are done and verified: OQ-SAF-020 item 3 (HZ-008 `related_risk_ids` names RSK-046 and RSK-046 `related.hazard_ids` names HZ-008; `render_risk.py --check` exit 0), OQ-SAF-021 and 023 Closed, 022 Answered, and each author-edit question now states the owner re-dating fallback. The condition the finding names still holds: OQ-SAF-006, 007, 017 and 020 (item 6) remain Open with `close_by: SRR` waiting on another author's edit, and 0.4.0-pha adds two more of the same kind (OQ-SAF-025, 026); none is answered or re-dated in a decision memo. It closes when the named authors act or the owner re-dates each in the SRR memo and `hazards.json` records the new `close_by`. Package item H7 stays open until then. |
| <a id="finding-9"></a>finding-9 (F-09) | reviewer | Minor | CK-SAF-C2, CK-SAF-C1 | analysis sections 4, 5 (HZ-015), 8.1 item 6; `hazards.json` HZ-015 K1 `type` | HZ-015 is carried at a Serious residual. Its only control with a requirement is K3 (REQ-SYS-137 and 138, closing by Analysis), and K3 addresses heat or ESD damage to parts, not the bench fire that sets the severity. So the residual does not meet the section 3.4 Serious terms (two independent controls, one neither software nor procedure, each verified by Test). Unlike the HZ-004 decline case, the analysis does not say so. The Medium target relies on controls verified by Inspection. Section 8.1 item 6 relies on K1 being equipment, but K1 is typed `Process` and mixes equipment with procedure. Fix: state the section 3.4 position of the HZ-015 residual and the path to PDR. Split K1 into the station (equipment, typed Design or Hardware interlock) and the practice (Operator procedure). | Verified | Pending | | Closed. HZ-015 K1 is the station, typed Hardware interlock, `independent_of_firmware` true; the practice is the new K6, Operator procedure. `residual_risk.condition` and section 4 state that the Serious residual does not meet the section 3.4 Serious terms and is not offered for acceptance at SRR, with the path to PDR (decision 100, OQ-SAF-019, K1 by Test, K4 to K6 by Inspection). Section 8.1 items 3 and 6 agree. |
| <a id="finding-10"></a>finding-10 (F-10) | reviewer | Minor | CK-SAF-G3 | analysis section 5, HZ-004 coverage table row 4 | "128 identical elements (3.1 s at 50 WPM)" counts element time without the inter-element spaces. That is the research derivation of `keyer-verification-and-key-input-network.md` (paddle watchdog item 3). With spaces, 128 dits take about 6.1 s at 50 WPM, the basis REQ-SYS-054 uses (20.5 s at 15 WPM). Row 4 and section 7 row j also give (ii) as 30 s without saying that REQ-SYS-054 as written caps at 10 s (TBR), which only the OQ-SAF-001 resolution records. Fix: correct the figure and state the written 10 s cap beside the 30 s proposal. | Verified | Pending | | Closed. Section 5 narrative, coverage row 4 and section 7 row j give about 6.1 s elapsed at 50 WPM with the spaces (3.1 s keyed; reviewer arithmetic: dit 24 ms, 128 x 48 ms = 6.14 s) and state the written REQ-SYS-054 cap of 128 elements or 10 s (TBR) beside the 30 s proposal. No 3.1 s-as-elapsed figure remains in either file. |
| <a id="finding-11"></a>finding-11 (F-11) | reviewer | Minor | CK-SAF-G5 | analysis section 10 | No provision covers HZ-011 at the bench, although bench firmware loads and USB logging put USB power on the unit near keyed steps. The Firmware load row names only HZ-014. Fix: add a rule (USB disconnected before any keyed step, or the VBUS inhibit case passed first) with its named abort. | Verified | Pending | | Closed. Section 10 row "USB power near keyed steps" (HZ-011, HZ-014): USB disconnected before any keyed step unless the REQ-SYS-092 inhibit case has passed on that unit, with a named abort (power switch off, USB unplugged, NCR). |
| <a id="finding-12"></a>finding-12 (F-12) | reviewer | Minor | CK-SAF-A7 | `hazards.json` HZ-004 K5, HZ-007 K1 `text` | Two control texts rest on undecided owner decisions without the section 3.6 tag "Proposed, owner decision pending at SRR". HZ-004 K5 carries T_max 10 s and the 74LVC1G123 part (D-KN2, package decision 36). HZ-007 K1 carries the S-8252 protector thresholds (D-PWR-03, package decision 72). Fix: add the tag. | Verified | Pending | | Closed. HZ-004 K5 and HZ-007 K1 `text` end with "Proposed, owner decision pending at SRR" naming D-KN2, package decision 36 and D-PWR-03, package decision 72; both decisions verified in package section 13.1 (Stuck-key and Power groups). |
| <a id="finding-13"></a>finding-13 (F-13) | reviewer | Minor | CK-SAF-G2 | `hazards.json` HZ-007, HZ-010, HZ-012 `decisions_pending` | Four items have no package section 13.1 row: A-PWR-03 (HZ-007), ANT-06 common-mode chokes and A-KN5 bounce capture (HZ-010), and ANT-03 counterpoise attachment (HZ-012). Fix: name the package decision that consolidates each (as done for decisions 36 to 41), or mark each as a PDR action rather than an SRR decision. | Verified | Pending | | Closed. `decisions_pending`: A-PWR-03 (HZ-007), ANT-06 (HZ-010) and ANT-03 (HZ-012) are marked PDR design actions with the reason; A-KN5 maps to package decision 50, whose section 13.1 row covers the debounce TBR closing by the bench capture of the owner's key and paddle. |
| <a id="finding-14"></a>finding-14 (F-14) | reviewer (iteration 2) | Minor | CK-SAF-G1 | `hazards.json` OQ-SAF-006 `resolution` | The resolution says "OPS-013 step 3 keeps 128 elements or 30 s", and the 0.4.0-pha re-check adds only "still not answered". `docs/conops/conops.md` OPS-013 step 3 now reads "128 consecutive identical elements or 10 s (TBR)" with 30 s as the D-KN3 alternative (package decision 37). Item (3) is still unanswered (the step is not the no-gap watchdog of OQ-SAF-001), so the status is right, but the evidence quoted for it is stale. Fix: restate the item (3) evidence from the current ConOps text. | Lien | Not needed | PDR | New at iteration 2; iteration 3: Lien: fix before PDR (see Iteration 3). |
| <a id="finding-15"></a>finding-15 (F-15) | reviewer (iteration 2) | Minor | CK-SAF-D5 | analysis section 9 item 3 (Marginal Analysis cases), section 8.1 item 5 | The Marginal Analysis-closing list gives REQ-SYS-050, 106, 110 and 111. A recompute of every `control_req_ids` entry of a Marginal hazard whose `verification_method` is not Test also finds REQ-SYS-168 (cell cover pinch gap, HZ-013 K3; method Analysis, "Analysis accepted per RSK-018"; RSK-018 carries HZ-013). It is missing from item 3, and section 8.1 item 5 names only REQ-SYS-110 and 111 for HZ-013. The acceptance itself is correctly recorded in the requirement; only the analysis list is incomplete. The gap was present at iteration 1 and was not raised then. Fix: add REQ-SYS-168 to section 9 item 3 and to the HZ-013 ids of section 8.1 item 5. | Lien | Not needed | PDR | New at iteration 2; iteration 3: Lien: fix before PDR (see Iteration 3). |
| <a id="finding-16"></a>finding-16 (F-16) | reviewer (iteration 3) | Minor | CK-SAF-D5, CK-SAF-G1 | analysis section 9 item 3 (line 310), section 8.1 item 7 lead-in (line 245), section 11.2 table header (line 366) | Text left stale by the 0.4.1-pha question closures. Section 9 item 3 ends: "Two of those requirement notes cite a risk that no longer carries the hazard (REQ-SYS-050 cites RSK-012 ... REQ-SYS-106 cites RSK-018 ...; OQ-SAF-017)". The committed `requirements.json` (blob `0da73012`) has REQ-SYS-050 "Analysis accepted per RSK-024 (HZ-010)" and REQ-SYS-106 "Analysis accepted per RSK-025 (HZ-009)", and section 11.2 records OQ-SAF-017 Closed, so the section contradicts both. Section 8.1 item 7 still calls its table "the complete list at 0.4.0-pha" and says rows whose risk does not carry the hazard "say so" and that OQ-SAF-026 "asks for the correction", although every row now names a risk that carries its hazard and OQ-SAF-026 is Answered. The 11.2 status column is headed "Status (2026-09-25)" but carries 2026-09-26 statuses. The data are right; only the prose is stale. Fix: delete the last sentence of section 9 item 3 (or restate it as resolved at 0.4.1-pha), restate the item 7 lead-in at the current revision, and re-date the 11.2 column header. | Lien | Not needed | PDR | New at iteration 3: Lien: fix before PDR (see Iteration 3). |

## Per-hazard results

| Hazard | Record content and scales (B1 to B4) | Controls meet the section 3.4 response (C2 to C4) | Trace union and back-links (D1, D2) | Software contributions and components (F1, F2) | Risk link two-way (D6) | Finding ids |
|---|---|---|---|---|---|---|
| HZ-001 | Yes (Marginal-C Medium; 87.5 percent worst case recomputed) | Yes | Union yes; back-links No (3 REQ-TX) | Yes | Yes (RSK-016, RSK-030) | finding-1, finding-6 |
| HZ-002 | Yes | Yes (K1, K2 hardware by Test; Serious residual stated with the K3, K9 path) | Yes | Yes (C4) | Yes (RSK-007, safety 5) | finding-4, finding-6 |
| HZ-003 | Yes (Critical-C Serious) | No (REQ-SYS-113 Analysis, not in the section 8.1 table) | Union yes; back-links No (1) | Yes (C4) | Yes (RSK-006, RSK-026, safety 4) | finding-1, finding-3, finding-6 |
| HZ-004 | Yes | Yes (K5, K6, K12 independent; decline case stated) | Union yes; back-links No (15) | Yes | Yes (RSK-024) | finding-1, finding-6, finding-10, finding-12 |
| HZ-005 | Yes | No (REQ-SYS-075, 157, 158 Analysis, not in the table) | Union yes; back-links No (1) | Yes | Yes (RSK-017) | finding-1, finding-3, finding-4 |
| HZ-006 | Yes | No (REQ-SYS-172 Analysis, not in the table) | Union yes; back-links No (4) | Yes | Yes (RSK-016) | finding-1, finding-3, finding-4, finding-6 |
| HZ-007 | Yes | Yes (K1, K2 hardware; REQ-SYS-085 listed) | Yes | No (no software cause) | Yes (RSK-007) | finding-2, finding-4, finding-6, finding-12, finding-13 |
| HZ-008 | Yes | No (REQ-SYS-014, 015 Analysis, not in the table) | Union yes; back-links No (11) | Yes (C7, C8; components per section 6.3 item 6) | Yes (RSK-001, RSK-011) | finding-1, finding-3, finding-6 |
| HZ-009 | Yes | Yes | Yes | N/A (no firmware on any path) | Yes (RSK-025) | none |
| HZ-010 | Yes | Yes | Union yes; back-links No (3) | No (no software cause; C4 classed Design) | Yes (RSK-024) | finding-1, finding-2, finding-13 |
| HZ-011 | Yes | Yes | Yes | Yes (C2) | Yes (RSK-007, RSK-033) | finding-4, finding-11 |
| HZ-012 | Yes | Yes | Union yes; back-links No (1) | Yes (C4) | Yes (RSK-016) | finding-1, finding-6, finding-13 |
| HZ-013 | Yes | Yes | Yes | N/A (no firmware on any path) | Yes (RSK-018) | none |
| HZ-014 | Yes | Yes (K3, K4, K8 independent) | Union yes; back-links No (1) | Yes | Yes (RSK-015) | finding-1, finding-6 |
| HZ-015 | Yes | No (Serious residual outside section 3.4 terms; REQ-SYS-137, 138 Analysis per RSK-004) | Yes | N/A (no firmware on any path) | Yes (RSK-034, safety 5) | finding-3, finding-9 |

## Readiness criteria

| # | Criterion | Answer | Evidence |
|---|---|---|---|
| R1 | `validate_docs.py` exits 0 | No (outside the product) | Exit 1: `FAIL docs/design/allocation.json (schema not found: docs/design/allocation.schema.json)`, a concurrent product. `PASS docs/safety/hazards.json (schema: docs/safety/schema.json)`. |
| R2 | `traceability.py --report-only --output <scratch>` reports none of the six hazard violation codes | No | Exit 0 (report-only). 27 `HAZARD_REQ_NOT_TESTED` (REQ-SW-KEYER 15, REQ-TX 12), 40 `HAZARD_INVERSE` warnings (sw-keyer 23, tx 17). Zero `HAZARD_ID_FORMAT`, `HAZARD_UNRESOLVED`, `HAZARD_CONTROL_UNTRACED`, `SAFETY_TAG_NO_HAZARD`, `HAZARD_REQ_NOT_ON_TARGET`. finding-1, finding-7. |
| R3 | `render_risk.py --check --gate SRR --hazards docs/safety/hazards.json` exits 0 | Yes | Exit 0: "register OK: 59 risks, 130 candidates, 0 warning(s), jsonschema used, gate SRR, hazard cross-check". H9 hazard part closed. |
| R4 | Author return states the version and the changes | Yes | Author summary: 0.3.0-pha, OQ-SAF-004 and 011 closed, REQ-SYS-180 to 182 traced, HZ-015 names RSK-034. The analysis section 4 "Changes from 0.2.0-pha" and section 13 agree with the diff against `28e49e6` (new controls HZ-001 K10, HZ-003 K10, HZ-006 K10, HZ-012 K6, HZ-014 K8; the HZ-008 component rename; no severity, likelihood, initial risk, criteria or SWE-134 change). |
| R5 | No `TBD`; every `tbr` has owner, plan, close_by | Yes | `grep -n TBD` on both files: no hit. All 17 `tbr` items on 16 controls carry the three keys (Python check). |

## A. Method, scope and scales

| Id | Answer | Evidence |
|---|---|---|
| CK-SAF-A1 | Yes | Each of the nine SEMP section 7.1 scope items (`docs/plan/semp.md` line 317) maps item by item in analysis section 1 to HZ-001/006, 012, 003, 002/007, 005, 004/008, 013, 014, 015. The additions (HZ-009, 010, 011, the HZ-008 harmonic branch, the bench test modes) and the mission-only exclusion carry reasons. |
| CK-SAF-A2 | Yes | The vector search for "HZ-candidate" returns only `audio-output-and-hearing-safety.md` lines 152 and 153 (excessive output; startle at power-on, plug or T/R), both covered by HZ-005 (C1 to C5, including the clicks). The `sources` arrays name 13 research reports, the ConOps, the register and the corpus. |
| CK-SAF-A3 | Yes | Section 3.2 equals `scales.severity` (register levels 5, 4, 3 or 2, 1). 1.1310(b) 8 W/kg per 1 g, 20 W/kg per 10 g, 6 min, and 1.1310(c) 1.6 W/kg, 30 min, agree with `47cfr-1.1310.md` (b) and (c). 97.3(a)(23) "endangers the functioning of a radionavigation service" agrees with `47cfr-97.3.md` line 67. |
| CK-SAF-A4 | Yes | Section 2: 5 units, 15 unit-years; SI-035 "at most 5 complete units" (`stakeholder-inputs.md` line 43). Section 3.3 anchors are operational and stated in the uncontrolled state. |
| CK-SAF-A5 | Yes | The matrix of section 3.4 was checked against every `initial_risk` and `residual_risk.level` (R1 schema pass). The two deviating cells (Marginal-D, Negligible-C) are stated with a reason. There is a response for all four levels. |
| CK-SAF-A6 | Yes | All 13 Requirement pending controls are excluded from the residuals and map to an OQ (HZ-002 K3, K7, K9 to OQ-SAF-008, 010, 009; HZ-004 K4, K13 to OQ-SAF-001, 002, 016; HZ-005 K3, K9 to OQ-SAF-015, 016; HZ-007 K5 to OQ-SAF-010; HZ-008 K3 to OQ-SAF-015; HZ-015 K1, K2, K4, K5 to OQ-SAF-019). Every residual has a `condition`. |
| CK-SAF-A7 | No | finding-12. Every `tbr` closes at PDR; each L1-carried number closes at PDR as charter section 7 requires. |
| CK-SAF-A8 | Yes | Section 2 agrees with SI-030, SI-031, SI-035 and SI-036, REQ-SYS-020 (at most 5.5 s, TBR), REQ-SYS-092 and 093 (VBUS inhibit, charge pause) and CON-016 (bench list without a soldering station). |

## B. Hazard records

| Id | Answer | Evidence |
|---|---|---|
| CK-SAF-B1 | Yes | All 15 records carry the SWEHB 5.24 fields with hazard-specific quantities. Spot checks: HZ-001 effects give 17.5 and 43.8 percent and 28.6 W / 11.4 W, matching `rf-exposure-evaluation.md` Table 5 and the line under it. HZ-012 gives 22.4 V peak (sqrt(2 x 5 W x 50 ohm)). HZ-008 gives the 7f band 1008 to 1036 MHz. |
| CK-SAF-B2 | Yes | HZ-001 is Marginal because the uncontrolled worst case (10 W carrier) is 87.5 percent of 8 W/kg, below the limit (the rationale states the Critical escalation rule). HZ-006 is Critical because 218.8 percent exceeds 1.6 W/kg (Table 5). HZ-003 is Critical (burn needing treatment). HZ-002, 007 and 015 are Catastrophic (fire). |
| CK-SAF-B3 | Yes | Each rationale names its anchor (for example HZ-002 B for mismatched cells, HZ-015 D for an iron left on, HZ-014 B for a wrong image). |
| CK-SAF-B4 | Yes | The HZ-001/006 split is by population and the HZ-002/007 split by energy path; no duplicate scenario. |
| CK-SAF-B5 | Yes | All 15 hazards are `Controls proposed`; none is `Identified`. |
| CK-SAF-B6 | Yes | The Python diff shows every `history` array at `28e49e6` as an unchanged prefix of the current one. The last entry equals the current severity, likelihood, risk and status for all 15 hazards. |
| CK-SAF-B7 | Yes | Section 4 was recomputed from `hazards.json` for id, severity, likelihood, initial, residual, criteria and risks: no difference. Counts: High 5, Serious 8, Medium 2 initial; Serious 2, Medium 3, Low 10 residual. They match. |

## C. Controls, fault tolerance and single point failures

| Id | Answer | Evidence |
|---|---|---|
| CK-SAF-C1 | Yes with one exception | `independent_of_firmware` agrees with the text for every Software (false) and Hardware interlock (true) control. The HZ-015 K1 type issue is part of finding-9. |
| CK-SAF-C2 | No | Every High initial hazard has an allocated independent non-software, non-procedure control: HZ-002 K1, K2, K6; HZ-004 K5, K6, K12; HZ-005 K1, K5, K7; HZ-007 K1, K2, K6; HZ-014 K3, K4, K8. The Serious residual HZ-002 has K1 and K2 closing by Test (REQ-SYS-081, 082, 083 method Test). The Serious residual HZ-015 fails (finding-9). |
| CK-SAF-C3 | Yes | No Critical or Catastrophic hazard rests on procedure or documentation alone. HZ-015 depends on K1 equipment, as section 8.1 item 6 states (finding-9 on its type). |
| CK-SAF-C4 | No | finding-3 (9 Analysis-closing requirements missing from the section 8.1 item 7 table). The 6 listed rows verified: REQ-SYS-112, 073, 076, 121, 085 and 010 are method Analysis with "Analysis accepted per RSK-" notes. |
| CK-SAF-C5 | No | finding-5. The philosophy is stated for keying, PA enable, charging and thermal (items 1 to 4), and each not-met branch is a section 8.2 row with a closing decision (rows 3, 4, 8 to decisions 38, 40, 39). |
| CK-SAF-C6 | No | finding-4 (5 of 23 entries missing). Every section 8.2 row names a hazard that carries it. |
| CK-SAF-C7 | Yes | See A6; each OQ has addressee, request and `close_by`. |
| CK-SAF-C8 | Yes | The Hazards column was recomputed from `swe134_items` for items a to l: identical. All 39 REQ-SYS ids in the Requirement column resolve and are Draft with the tag `safety`. Every row names an evidence class of charter section 9, with Emulation limited to ordering. |

## D. Traceability and risk linkage

| Id | Answer | Evidence |
|---|---|---|
| CK-SAF-D1 | Yes | Recomputed union of `control_req_ids` minus `requirement_ids` for all 15 hazards: differences none. |
| CK-SAF-D2 | No | The hazards.json-to-requirement direction holds: every named requirement lists the hazard and carries `safety`; zero `HAZARD_CONTROL_UNTRACED` and `SAFETY_TAG_NO_HAZARD`; zero REQ-SYS inverse. The requirement-to-hazards.json direction fails for 40 L2 links (finding-1). |
| CK-SAF-D3 | No | finding-6 (27 pairs). |
| CK-SAF-D4 | N/A | No control names a `REQ-SW-*` requirement at this revision (Python check). The `Depends on:` rule applies once finding-1 adds them. |
| CK-SAF-D5 | No | finding-7 (27 `HAZARD_REQ_NOT_TESTED`). Every REQ-SYS control requirement has a closing Test case or an Analysis note (finding-3 for the table). |
| CK-SAF-D6 | Yes | R3 pass. Each hazard's risks name it back, and each risk's safety level is at or above the mapped level (for example HZ-015 to RSK-034 safety 5; HZ-003 to RSK-006, RSK-026 at 4; HZ-001 Marginal to RSK-030 at 2, within the 3-or-2 mapping). Section 12 equals the register `related.hazard_ids`. |
| CK-SAF-D7 | Yes | Section 9 item 1 names `requirement_ids` and `controls[].control_req_ids`, the fields `tools/traceability.py` reads (lines 1450, 1469). Report section 9 lists all 15 hazards. |

## E. Safety-critical software determination (SWE-205)

| Id | Answer | Evidence |
|---|---|---|
| CK-SAF-E1 | Yes | `safety_critical` is true exactly when `criteria` is non-empty (12 of 15). HZ-009, 013 and 015 are empty with no firmware role. The criteria a to e quoted in section 6.1 follow `7-02-classification-and-safety-criticality.md` section 1.2 as the analysis states. |
| CK-SAF-E2 | Yes | The union rule was recomputed over `firmware_role.components`. Keyer a,b,c (HZ-001, 004, 010); TXSEQ a,b,c,e (HZ-001, 003, 004, 006, 007, 008, 011, 012); SW-PWR c,e; thermal b,e; audio b,c; safe-state manager a,b,c,e (HZ-001 to 007, 011, 014); SCHED a,b,c,e (HZ-001 to 007, 011, 012); SW-SYNTH and the verification unit a,c,e (HZ-008). Differences from section 6.2: none. |
| CK-SAF-E3 | Yes | The 03 and 07 differences are listed in section 11.1 items 1 and 2 and carried by OQ-SAF-014, 022 and 023 with `close_by` SRR (finding-8 on their open state). |
| CK-SAF-E4 | Yes | The ALC set-point and envelope shaper (mission-critical) are not in any `components` list. SW-SYNTH is named for HZ-008 only as a proposed safety-critical component (section 6.3 item 6, decision 9). |

## F. Software assurance tasks (SWEHB swe-205 section 7.1)

| Id | Answer | Evidence |
|---|---|---|
| CK-SAF-F1 | No | Task 1 ("action, inaction, or incorrect action", swe-205 line 540). Software causes are present for HZ-001, 002, 003, 004, 005, 006, 008, 011, 012 and 014, and absent for HZ-007 and HZ-010 (finding-2). |
| CK-SAF-F2 | Yes | Tasks 2 and 3: components use the 03 section 4.3 and 07 section 14.1 names. The one renamed component since `28e49e6` (HZ-008 frequency verification unit, "requirement pending" to "REQ-SYS-182, package decision 40") is assessed with criteria a, c, e. |
| CK-SAF-F3 | No | Task 4 (traceability both ways) fails for 23 `REQ-SW-KEYER` links (finding-1). `HAZARD_CONTROL_UNTRACED` is 0. |
| CK-SAF-F4 | Yes | `assurance_tasks_applied` lists tasks 1 to 4; results are in F1 to F3. |

## G. Open questions, regulation and gate maturity

| Id | Answer | Evidence |
|---|---|---|
| CK-SAF-G1 | No | All 24 entries have addressee, hazard ids, request, status and `close_by`. OQ-SAF-004 and 011 are Closed with a resolution, which the reviewer verified: the REQ-SYS-053 statement and rationale name the Bug-mode dah; REQ-SYS-002 `hazard_ids` has HZ-011; REQ-SYS-149 implements HZ-011 K3; the REQ-SYS-092 rationale names its own VBUS sense. Eight wait on package decisions 9 and 36 to 41 (verified in section 13.1). Seven SRR-due questions wait on author edits (finding-8). |
| CK-SAF-G2 | No | Every decision number cited (9, 17, 19, 20, 22, 23, 29, 35 to 41, 44, 64, 72, 75, 100) resolves to the matching section 13.1 row. The decision 38 default "Not adopted" agrees with `decisions-for-owner.md` line 62. Four ids have no row (finding-13). |
| CK-SAF-G3 | No | Regulation is correct:<br>- 97.307(e): 25 uW and 40 dB, which is 53 dB at 5 W (`47cfr-97.307.md` line 25)<br>- 97.13(c)(1)<br>- 97.115(b)(1)<br>- 2.1093(b), (d)(1), (d)(3), (d)(4)<br>- 1.1310(b), (c), (e)(2)<br>- 2.106 US78 at 1030 MHz (`47cfr-2.106-harmonic-bands.md` line 298)<br>Research figures are correct: rf-exposure F6, F7 (17.5, 43.8, 87.5, 218.8 and 106.3 percent) and F3 (0.58 m, 0.91 m); audio F22 and F25. One research-derived timing figure is inconsistent (finding-10). |
| CK-SAF-G4 | Yes | SRR maturity holds: all known hazards with causes, proposed controls and risk (SWEHB 5.24 phases 0 and 1). The PDR items (no Requirement pending, final single point failure list) are scheduled in section 9 item 4. |
| CK-SAF-G5 | No | Section 10 covers assembly, dummy-load-only RF, power-on staging, the stuck-key abort for a continuous key-down and a stream, test modes, thermal limits, cells, headphones, exposure, ESD, firmware load and mechanics. HZ-011 is missing (finding-11). |

## SRR row and package item assessment

- **Row 14** is Partially met. The hazard list, the preliminary controls and the SWE-205 determination are complete and consistent: the section 6.2 union and the section 7 recompute show no difference. The two-way trace to the L2 software and TX requirements is not (finding-1), and HZ-007 and HZ-010 lack software causes (finding-2).
- **Row 15** is Partially met. The philosophy is stated for keying, PA enable, charging and thermal. The decline cases of decisions 38 to 40 are recorded (section 8.3), which closes the hazard-analysis part of H8. The requirement-id reflection and the section 8.1 item 7 exceptions are incomplete (finding-3, finding-5), and the section 8.2 list misses 5 entries (finding-4).
- **H7** is reconciled in the file: statuses are accurate and OQ-SAF-004 and 011 are correctly closed. It is not closed at the gate while seven SRR-due questions wait on author edits (finding-8).
- **H9** (HZ-015 back-link) is closed: R3 exits 0.

## Measurements (SWE-089)

- Items checked: 48 (R1 to R5 and 43 CK-SAF items).
- Items answered No: 16 (`items_no`). N/A: 1 (CK-SAF-D4).
- Findings: Major 3, Minor 10. Fixed 0, deferred 0.
- Iteration 1; about 46 turns and 55 minutes.
- Iteration 2: items answered No 3 (R1, CK-SAF-D5, CK-SAF-G1); CK-SAF-D4 now answered Yes. Findings: Major 3, Minor 12 (two new). Verified 12, open 3 (Minor), deferred 0. About 28 further turns and 35 minutes (front matter totals 74 and 90).

## Notes

- **Commands run (2026-09-25):**
  - `validate_docs.py` exit 1 (allocation.json schema missing, outside the product; hazards.json PASS).
  - `traceability.py --report-only --output <scratchpad>/traceability-report.md` exit 0 (76 violations, 42 warnings; hazard codes as R2).
  - `render_risk.py --check --gate SRR --hazards docs/safety/hazards.json` exit 0.
  - `render_rmm.py --check` exit 1 (SWE-023 and SWE-051 status rows, outside the product).
  - `render_compliance.py --check` exit 0.
  - `python -m unittest discover -s tools/tests`: 331 run, 1 failure (`test_validate_docs.RepositoryTests.test_repository_exit_zero`, the same allocation.json failure).
- **Record slug.** The assignment path `checklists/hazard-analysis.md` differs from the checklist's `safety-hazard-analysis.md`. The validator pattern accepts both; the lead SE decides whether to rename it.
- **Rendered visuals.** This product has no rendered visual; none were produced by this review.

## Closure (iteration 2, 2026-09-25)

**Re-review scope.** The author reported F-01 to F-13 (finding-1 to finding-13) fixed and none disputed, at revision 0.4.0-pha. The reviewer (`reviewer:hazards`, a new invocation in the same role) did not edit the product. It re-read the working-tree blobs in the front matter (`hazard-analysis.md` c20281a7, `hazards.json` 89d0cbc3; both modified and uncommitted against `28e49e6`, package item H17) and checked each fix against its source rather than against the author's change log:
- `hazards.json` was read with Python against every `docs/requirements/**/requirements.json` file (union, inverse links, the section 8.1 item 7 recompute, the `Depends on:` items of the 15 `REQ-SW-KEYER` requirements a control now names), `docs/risk/register.json` (RSK-002, 004, 034, 046) and `git show 28e49e6:docs/safety/hazards.json` (every `history` array is still an unchanged prefix; the last entry equals the current values for all 15 hazards).
- Package decisions 36, 50, 72, 81 and 100 were checked against `docs/reviews/SRR/package.md` section 13.1.
- The ConOps OPS-013 text was read for OQ-SAF-006 (finding-14).
- Scans: no em dash in either product file; no TBD; all 17 `tbr` items carry owner, plan and close_by.

Search first: `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any `grep` (queries: "peer review record closure block disposition column findings Closed Disputed accepted re-review"; "OPS-013 stuck key headphones in key jack after boot squeeze iambic toggling stream"). `grep -n` then pinned lines only. The tool was available throughout.

**Dispositions.**

| Disposition | Count | Findings |
|---|---|---|
| Closed (fix verified in the product, state Verified) | 12 (Major 3, Minor 9) | finding-1 to finding-7, finding-9 to finding-13 |
| Disputed accepted (state Withdrawn) | 0 | none disputed |
| Open | 3 (Minor) | finding-8 (SRR-due questions OQ-SAF-006, 007, 017, 020 item 6, 025 and 026 wait on other authors' edits or an owner re-dating); finding-14 (new: OQ-SAF-006 evidence text stale against the current ConOps); finding-15 (new: REQ-SYS-168 missing from the Marginal Analysis list) |

Major findings open: 0; Minor findings open: 3. finding-5 and finding-6 are closed for this product (requirement ids named in section 8.1; the rationale corrections routed in section 11.2 and OQ-SAF-025); the stale rationales themselves remain in `docs/requirements/sys/requirements.json` and are counted once, under finding-8.

**Iteration 2 answers** (items that changed; all others stand as at iteration 1).

| Item | Answer | Evidence |
|---|---|---|
| R1 | No (outside the product) | `validate_docs.py` exit 1: 31 passed, 2 failed, both outside the product (`docs/design/allocation.json` and `docs/plan/measurements.json`, schema not found). `PASS docs/safety/hazards.json` and `PASS docs/reviews/SRR/checklists/hazard-analysis.md` |
| R2 | Yes | `traceability.py --report-only --output <scratchpad>` exit 0: 231 requirements, 167 test cases, 0 violations, 2 warnings (`SYS_UNALLOCATED` REQ-SYS-125, 148); none of the six hazard codes. finding-1, finding-7 closed |
| R3 | Yes | `render_risk.py --check --gate SRR --hazards docs/safety/hazards.json` exit 0: "register OK: 65 risks, 159 candidates, 0 warning(s), jsonschema used, gate SRR, hazard cross-check" |
| R4 | Yes | Header and section 13 state 0.4.0-pha with the changes finding by finding; they agree with the reviewer's checks above |
| R5 | Yes | No TBD in either file; 17 `tbr` items complete |
| CK-SAF-A7 | Yes | finding-12 closed |
| CK-SAF-C2, CK-SAF-C1 | Yes | finding-9 closed: HZ-015's Serious residual is declared outside the section 3.4 terms and not offered for acceptance, with its path; K1 typed Hardware interlock, K6 Operator procedure |
| CK-SAF-C4 | Yes | finding-3 closed (13-row table, recompute complete) |
| CK-SAF-C5 | Yes | finding-5 closed for the product |
| CK-SAF-C6 | Yes | finding-4 closed (23 of 23 entries) |
| CK-SAF-D2, CK-SAF-F3 | Yes | finding-1 closed: both directions hold, 0 inverse links |
| CK-SAF-D3 | Yes | finding-6 closed for the product (listed in section 11.2); the edits are tracked under finding-8 |
| CK-SAF-D4 | Yes (was N/A) | Controls now name 15 `REQ-SW-KEYER` requirements; each is Draft, tagged `safety`, and has a `Depends on:` item whose REQ and OPS ids all resolve (hardware ids such as REQ-SYS-047, 051, 055, 119, REQ-TX-003, 014; OPS-013), per 02 section 4.3 item 4 |
| CK-SAF-D5 | No | finding-7 closed. Every Critical or Catastrophic Analysis-closing control requirement is in the section 8.1 item 7 table; of the Marginal ones REQ-SYS-168 (HZ-013 K3) is missing from section 9 item 3 (finding-15) |
| CK-SAF-F1 | Yes | finding-2 closed; Software causes now named for every hazard with a firmware role |
| CK-SAF-G1 | No | finding-8, finding-14 |
| CK-SAF-G2 | Yes | finding-13 closed |
| CK-SAF-G3 | Yes | finding-10 closed |
| CK-SAF-G5 | Yes | finding-11 closed |

**Per-hazard results at iteration 2.** HZ-001, 003 to 008, 010, 012, 014 and 015 now read Yes in every column of the per-hazard table (back-links hold, the section 8.1 item 7 table is complete, HZ-007 and HZ-010 name Software causes, HZ-015's position is stated). HZ-002, 009 and 011 are unchanged. HZ-013 reads Yes except that REQ-SYS-168 is missing from the section 9 item 3 list (finding-15). The per-hazard table above keeps the iteration 1 answers as the record of what was found.

**SRR rows and package items.** Row 14: Met for this product (two-way trace and software causes closed). Row 15: Met for this product (item 7 exceptions complete, requirement ids named, section 8.2 complete); the requirement-rationale reflection is the requirements author's edit (OQ-SAF-025). H9: closed (R3). H7: not closed while finding-8 is open. H8 hazard part: closed (section 8.3, unchanged).

**Commands run (2026-09-25, iteration 2).**
- `validate_docs.py` exit 1 (R1 above; the product and this record PASS).
- `traceability.py --report-only --output <scratchpad>/tr.md` exit 0.
- `render_risk.py --check --gate SRR --hazards docs/safety/hazards.json` exit 0.
- `render_rmm.py --check` exit 0.
- `render_compliance.py --check` exit 0.
- `python -m unittest discover -s tools/tests`: 331 run, 1 failure (the repository-wide validate_docs exit-zero test, the same two missing schemas outside the product).

**Verdict.** No Major finding is open. `readiness_met` stays false only because R1 fails on files outside the product, and the validator ties APPROVED to `readiness_met` true, so the recorded verdict is NEEDS CHANGES. It becomes APPROVED, with finding-8, finding-14 and finding-15 as Minor findings riding with it (08 section 3.2), once `validate_docs.py` exits 0. `record_status` stays open for the lead SE to set Closed with `date_closed` (07 section 10.2) once finding-8, finding-14 and finding-15 are Verified or deferred by the owner with a decision reference and a gate.

```
ITERATION 2 (2026-09-25): VERDICT: NEEDS CHANGES (readiness R1 outside the product). Closed 12 (finding-1 to finding-7, finding-9 to finding-13; Major 3, Minor 9); Disputed accepted 0; open 3 Minor (finding-8, finding-14, finding-15). open Major 0.
```

## Iteration 3 (2026-09-26, re-review against the committed blobs; SRR package items R8, R14 and H6)

**Scope and independence.** Iteration 2 re-read working-tree blobs (`hazard-analysis.md` `c20281a7`, `hazards.json` `89d0cbc3`) that differ from the committed files and are not in the git object store (package section 2.3). This iteration therefore re-checks every finding, not only the three open ones, against the committed blobs at review baseline HEAD `adcfe0946d2f1b5cd8f41a8f91eb4219a7fb99a1`: `docs/safety/hazard-analysis.md` `b5ce99e93b96b6a2654f7cbe9ac5e23b8a2e1dbb` and `docs/safety/hazards.json` `37d6cc832ed8f164e5f7e6e911a8656a56720c9f` (revision 0.4.2-pha; last commit touching `docs/safety/` is `1543c9f`; working tree clean for both files). It also verifies the hazard parts of ConOps appendix D items D6 and D10 that INSP-003 iteration 3 and package item R14 hand to this reviewer, and the cross-product answers of OQ-SAF-007, OQ-SAF-025 and OQ-SAF-026 that the file marks "awaiting the INSP-008 reviewer's verification". The reviewer is a new invocation of `reviewer:hazards`; it authored none of the product and edits none of it (charter section 11 rule 4). The convergence rule of 2026-09-26 (charter section 4 item 3: a Minor RID is fixed before the next review and does not block the baseline) applies: every Minor finding, old or new, is dispositioned "Lien: fix before PDR".

**Search first.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any `grep` (queries: "hazard analysis 0.4.2-pha changes HZ-004 K2 ConOps appendix D D6 D10 hazard parts"; "validate_docs record drift rule product_files blobs differ from HEAD APPROVED record"). `grep -n` then pinned lines only. The tool was available throughout.

**Method.** `git diff 08d1496 HEAD -- docs/safety/` gives the 0.4.1-pha and 0.4.2-pha text changes (header, sections 3.2, 7 rows c and l, 11.1, 11.2, 12, 13; `hazards.json` HZ-004 K2 text and history, OQ-SAF-017, 019 and 020). Because the 0.4.0-pha blob that iteration 2 read is not recoverable, every iteration 2 closure was recomputed at HEAD with Python over `hazards.json`, every `docs/requirements/**/requirements.json` file, `docs/risk/register.json` and `git show 28e49e6:docs/safety/hazards.json`: control union against `requirement_ids` (15 of 15 exact), forward links and inverse links (0 missing each way), every non-Test control requirement per hazard and severity, the 23 `single_point_failures` entries, Software-class causes, `history` prefixes and last entries, `tbr` completeness (17 of 17 with owner, plan, close_by), and the rationale of every control requirement for its hazard id and control id (0 pairs missing). No TBD and no em dash in either file.

**Disposition table.**

| Finding | Severity | Iteration 3 disposition | Evidence at HEAD (file and line) |
|---|---|---|---|
| finding-1 | Major | Closed (Verified) | `traceability.py --report-only` exit 0: 237 requirements, 170 test cases, 0 violations, no `HAZARD_INVERSE`; recompute: 0 inverse and 0 forward gaps, union exact for 15 hazards; `hazard-analysis.md` line 308 (section 9 item 1) withdraws the PDR deferral |
| finding-2 | Major | Closed (Verified) | `hazards.json` HZ-007 C9 (line 2017) and C10 (line 2022), HZ-010 C6 (line 2769) and C7 (line 2774), all class Software |
| finding-3 | Major | Closed (Verified) | `hazard-analysis.md` lines 245 to 262 (section 8.1 item 7): the recompute of every non-Test control requirement of a Critical or Catastrophic hazard (REQ-SYS-010, 014, 015, 073, 075, 076, 085, 112, 113, 121, 122, 124, 137, 138, 157, 158, 172; REQ-TX-005, 006) finds each in the table. The REQ-SYS-137 and 138 rows now cite RSK-034 and REQ-SYS-010 cites RSK-011, matching the committed verification notes |
| finding-4 | Minor | Closed (Verified) | `hazard-analysis.md` lines 286 to 292 (section 8.2 rows 18 to 22 and the 23-entry note); 23 `single_point_failures` entries in `hazards.json` |
| finding-5 | Minor | Closed (Verified) | Section 8.1 items 3 to 6 name requirement ids (lines 241 to 244). The rationale corrections are now in the committed `requirements.json` `0da73012`: REQ-SYS-118 and 155 cite item 4 and row 8, 082 and 099 row 6, 018 and 151 row 10, 156 row 11, 105 and 152 row 14, 071 row 9, 132 row 16; REQ-SYS-081 and 083 cite item 3 and no longer claim three independent layers (OQ-SAF-025 item 2 verified) |
| finding-6 | Minor | Closed (Verified) | Script check over `sys`, `tx` and `sw/sw-keyer` rationales: every `control_req_ids` pair names its hazard id and control id (0 missing; OQ-SAF-025 item 1 verified) |
| finding-7 | Minor | Closed (Verified) | Line 308 restated from the tool output; reproduced at HEAD (0 violations, 2 `SYS_UNALLOCATED` warnings outside the analysis) |
| finding-8 | Minor | Closed (Verified) | No SRR-due question now waits on an author edit that the decision list does not carry. OQ-SAF-017 and 020 are Closed (line 386, 389); the cross-product answers are verified here: OQ-SAF-007 (dated F13 addendum at `docs/research/keyer-verification-and-key-input-network.md` line 238), OQ-SAF-025 (finding-5, finding-6 rows above), OQ-SAF-026 (REQ-SYS-137, 138 cite RSK-034; REQ-SYS-010 cites RSK-011; REQ-SYS-122 names a carrying risk per hazard; REQ-SYS-113 stays Analysis with the OQ-VV-003 condition stated). OQ-SAF-006 items 1, 2 and 4 are answered in `docs/conops/conops.md` (rule F7, line 245); its items 3 and 5 wait on package decisions 37 and 41 (`package.md` lines 733, 734) with the re-dating fallback of decision 116 (line 1027), so the package carries them |
| finding-9 | Minor | Closed (Verified) | `hazards.json` HZ-015 K1 Hardware interlock with `independent_of_firmware` true, K6 Operator procedure; `residual_risk.condition` states the section 3.4 position and the path to PDR; `hazard-analysis.md` line 112 and line 244 (item 6) |
| finding-10 | Minor | Closed (Verified) | Line 229 (section 7 row j): about 6.1 s elapsed at 50 WPM and the written REQ-SYS-054 cap of 128 or 10 s (TBR) beside the 30 s proposal |
| finding-11 | Minor | Closed (Verified) | Line 330, section 10 row "USB power near keyed steps" with the named abort |
| finding-12 | Minor | Closed (Verified) | `hazards.json` HZ-004 K5 text (line 1118) ends with the section 3.6 tag and package decision 36; HZ-007 K1 (line 2060) with decision 72 |
| finding-13 | Minor | Closed (Verified) | `decisions_pending`: A-PWR-03 (HZ-007), ANT-06 (HZ-010) and ANT-03 (HZ-012) are PDR design actions with the reason; A-KN5 maps to package decision 50 |
| finding-14 | Minor | Lien: fix before PDR | Not fixed: the OQ-SAF-006 `resolution` (`hazards.json` line 4114) still reads "OPS-013 step 3 keeps 128 elements or 30 s", while `docs/conops/conops.md` line 218 (Table 3.4-4 row 3) and line 537 (OPS-013 step 3) give 128 elements or 10 s (TBR) with 30 s as the decision 37 alternative. The 2026-09-26 update adds items 2 and 4 but does not restate the item 3 evidence. Status Open is still right |
| finding-15 | Minor | Lien: fix before PDR | Not fixed: section 9 item 3 (line 310) lists REQ-SYS-050, 106, 110 and 111 as the Marginal Analysis cases, and section 8.1 item 5 (line 243) names REQ-SYS-110 and 111 for HZ-013; REQ-SYS-168 (HZ-013 K3, Analysis accepted per RSK-018) is in neither |
| finding-16 | Minor | Lien: fix before PDR (new) | Section 9 item 3 (line 310) still says REQ-SYS-050 cites RSK-012 and REQ-SYS-106 cites RSK-018 (OQ-SAF-017), which the committed requirements and section 11.2 (line 386) contradict; the section 8.1 item 7 lead-in (line 245) and the 11.2 column header (line 366) are stale in the same way (findings table above) |

Disputed accepted: none; the author disputed no finding.

**New defects scan.** Concentrated on the text changed since the iteration 2 quotes (the 0.4.1-pha and 0.4.2-pha diff) and on the parts that iteration 2 could only check on uncommitted blobs. No new Major defect:
- **ConOps appendix D item D10, hazard part: verified.** HZ-004 K2 (`hazards.json` line 1063) states that the Straight-on-tip selection is accepted while the KEY inhibit is active (REQ-SYS-163), because a mono plug holds the ring closed, and that the REQ-SYS-052 interlock then re-runs on the inputs the new mode uses. This agrees with REQ-SYS-163 ("accept a key-input mode menu selection while any key input reads closed") and REQ-SYS-052 ("each power-on, reset or key-mode change until each input the mode uses reads open for 500 ms (TBR)") in `requirements.json` `0da73012`. `control_req_ids`, severity, likelihood, risk and status are unchanged, and the new `history` entry keeps the earlier entries as an unchanged prefix. The last entry equals the current values.
- **ConOps appendix D item D6, hazard part: verified.** Section 7 row l (line 231) applies the full safe state (PA off, key up, T/R to receive, charge disabled, audio muted) on reset, panic, latched fault (ConOps Table 3.4-4 rows 9 to 15) and on power-down. Inhibit-class causes and flags (rows 1 to 8), the key-down timeouts included, apply the transmit part only, so the stuck-key sidetone keeps sounding and charging is unchanged. Row c (line 222) points to row l. This matches the REQ-SYS-130 statement and rationale and REQ-SYS-004. Power-down is this analysis's addition and does not conflict with REQ-SYS-130.
- **Section 3.2 (line 48), section 12 (line 419) and the OQ-SAF-020 closure.** The quoted 06 section 7 level 4 text ("the operator, a bystander or any other person") is at `docs/process/06-risk-and-decision-analysis.md` line 106 (HEAD blob `7a92d21f`, as cited).
- **OQ-SAF-017 closure and the REQ-SYS-122 refinement carried to OQ-SAF-019.** REQ-SYS-050 and REQ-SYS-106 cite RSK-024 and RSK-025. `render_risk.py --check --gate SRR --hazards` exit 0 confirms that those risks carry HZ-010 and HZ-009. The carried refinement is recorded in OQ-SAF-019 with close_by PDR.
- The only new defect is the stale prose of finding-16 (Minor).

**Lien table** (convergence rule of 2026-09-26; each is carried by the package as a Routine item).

| Finding | Severity | Disposition | Owner | Due |
|---|---|---|---|---|
| finding-14 | Minor | Lien: fix before PDR | Hazard analysis author (restate the OQ-SAF-006 item 3 evidence from the current ConOps text) | PDR readiness declaration |
| finding-15 | Minor | Lien: fix before PDR | Hazard analysis author (add REQ-SYS-168 to section 9 item 3 and section 8.1 item 5) | PDR readiness declaration |
| finding-16 | Minor | Lien: fix before PDR | Hazard analysis author (remove or restate the stale OQ-SAF-017, OQ-SAF-026 and date text in sections 9 item 3, 8.1 item 7 and 11.2) | PDR readiness declaration |

**Iteration 3 answers** (items that changed from iteration 2; all others stand).

| Item | Answer | Evidence |
|---|---|---|
| R1 | Yes | `validate_docs.py --root <scratchpad export of HEAD adcfe09 by git archive>` exit 0. In the shared working tree it first exited 1 (35 passed, 2 failed) because of another agent's uncommitted edit to a different review record, outside this product; the final run after this record was written exits 0 (37 passed, 0 failed, no drift note for this record). `PASS docs/safety/hazards.json` and `PASS docs/reviews/SRR/checklists/hazard-analysis.md` in every run |
| R2 | Yes | `traceability.py --report-only --output <scratchpad>/tr.md` exit 0: 237 requirements, 170 test cases, 0 violations, 2 warnings (`SYS_UNALLOCATED` REQ-SYS-125, 148), none of the six hazard codes |
| R3 | Yes | `render_risk.py --check --gate SRR --hazards docs/safety/hazards.json` exit 0: "register OK: 65 risks, 159 candidates, 0 warning(s), jsonschema used, gate SRR, hazard cross-check" |
| R4 | Yes | Header (line 3) and section 13 (lines 431, 432) state 0.4.1-pha and 0.4.2-pha and their changes; they agree with the `git diff 08d1496 HEAD` |
| R5 | Yes | No TBD in either file; 17 `tbr` items complete |
| CK-SAF-D5 | No (Minor only) | finding-15 and finding-16 (liens). Every Critical or Catastrophic Analysis-closing control requirement is in the section 8.1 item 7 table |
| CK-SAF-G1 | No (Minor only) | finding-14 (lien). finding-8 closed: every SRR-due question is Closed, Answered (verified above) or waits on a numbered package decision |
| CK-SAF-D3 | Yes | finding-6 closed in the requirements too (0 pairs missing) |
| CK-SAF-C4, C5 | Yes | finding-3 and finding-5 re-verified at HEAD, including the corrected risk citations |

**Record edits for the validator.** Three iteration 2 summary lines (the "Dispositions" count line, the "Verdict" paragraph and the iteration 2 verdict block) had the state word in capitals beside a finding id and the severity word, which the validator's open-severity scan reads as an unresolved finding. The word is now lower case there; the content is unchanged. The findings table State column now reads Verified for finding-8 and Lien for finding-14 and finding-15. finding-16 is added.

**Commands run (2026-09-26, iteration 3).**
- `validate_docs.py`: exit 0 on the HEAD export; in the working tree exit 1 at first (2 failures in another agent's record, outside this product), then exit 0 on the final run (37 passed, 0 failed) with this record PASS and no record drift note.
- `traceability.py --report-only --output <scratchpad>/tr.md`: exit 0.
- `render_risk.py --check --gate SRR --hazards docs/safety/hazards.json`: exit 0.
- `render_rmm.py --check`: exit 0.
- `render_compliance.py --check`: exit 0.
- `python -m unittest discover -s tools/tests`: 392 run, 1 failure at the first run (`test_validate_docs.RepositoryTests.test_repository_exit_zero`, the same transient working-tree failure outside this product); final run: 392 run, OK (exit 0).

**Rendered visuals.** This product has no rendered visual, and this review produced none.

**Cross items (outside this record's scope; for the lead SE).**
1. OQ-SAF-007, OQ-SAF-025 and OQ-SAF-026 read "Answered ... awaiting the INSP-008 reviewer's verification". This iteration verifies them, so the hazard analysis author may set them Closed. This is a status edit, not a finding.
2. Package item H7 still lists OQ-SAF-006 as open. Its remaining items 3 and 5 close on decisions 37 and 41, or by re-dating under decision 116. The package, not this record, decides whether H7 closes on the rulings.
3. The package section 2.3 row for INSP-008 can now read the committed blobs `b5ce99e9` and `37d6cc83`.

**Verdict.** No Major finding is open. Findings 1 to 13 are Closed (Verified), and finding-14, 15 and 16 are Minor liens (fix before PDR). R1 to R5 hold on the committed product. The verdict is APPROVED with 3 liens (08 section 3.2; convergence rule). `record_status` stays for the lead SE to set Closed with `date_closed` (07 section 10.2) once the liens are carried by the package.

```
ITERATION 3 (2026-09-26): VERDICT: APPROVED (with liens). Reviewed hazard-analysis.md b5ce99e9 and hazards.json 37d6cc83 at HEAD adcfe09. Closed 13 (finding-1 to finding-13; Major 3, Minor 10); Disputed accepted 0; Liens 3 (finding-14, finding-15, finding-16: Minor, fix before PDR); open Major 0. ConOps appendix D D6 and D10 hazard parts verified.
```

## Iteration 3 delta verification (2026-09-26, R9 status edit `ade0e09`; SRR package item R17)

**Scope and independence.** Delta only: the hazard analysis author's status edit at `ade0e09` (revision 0.4.3-pha, package item R9), which sets OQ-SAF-007, OQ-SAF-025 and OQ-SAF-026 to Closed on the verification recorded at iteration 3 (finding-8 row and cross item 1). Base: the iteration 3 blobs `b5ce99e9` and `37d6cc83` (`ade0e09^`). Result: `hazard-analysis.md` `49ec53f8bbde37558c1c113a656b2125cd3fdec2` and `hazards.json` `c6bf757e815bea0f8ba8d6b90d9a618875833a24`, which are the HEAD blobs at `860e84e` (no commit after `ade0e09` touches `docs/safety/`; working tree clean). The reviewer is a new invocation of `reviewer:hazards`; it authored none of the product and edited none of it (charter section 11 rule 4). The convergence rule of 2026-09-26 (charter section 4 item 3) applies: no product content changes in this round, and Minor findings stay liens due PDR.

**Search first.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (queries: "OQ-SAF-007 OQ-SAF-025 OQ-SAF-026 Closed INSP-008 iteration 3 verification 0.4.3-pha"; "validate_docs record state rule readiness_met verdict product_files drift"). Manual commands afterwards only read known paths and diffs. The tool was available throughout.

**Method and results.**
- `git show ade0e09 --name-only`: only `docs/safety/hazard-analysis.md` and `docs/safety/hazards.json` change.
- `hazards.json`, structural Python diff of `ade0e09^` against `ade0e09` (every key, list length and value): exactly 7 differences. `version` 0.4.2-pha to 0.4.3-pha; for each of OQ-SAF-007, 025 and 026, `status` Answered to Closed and `resolution` extended. Each new `resolution` keeps the old text as an unchanged prefix (appended 284, 354 and 361 characters) and cites this record's iteration 3 finding-8 row with the evidence that iteration 3 verified: the dated F13 addendum at `docs/research/keyer-verification-and-key-input-network.md` line 238 (OQ-SAF-007); finding-5 and finding-6 Closed with 0 control pairs missing their hazard or control id (OQ-SAF-025); REQ-SYS-137 and 138 cite RSK-034, REQ-SYS-010 cites RSK-011, REQ-SYS-122 names a carrying risk per hazard, and REQ-SYS-113 stays Analysis with the OQ-VV-003 condition (OQ-SAF-026). These match the iteration 3 finding-8 row word for word in substance. `close_by` stays SRR. No hazard, control, cause, level, `history`, `tbr`, single point failure or requirement link changes.
- `hazard-analysis.md`, line diff: 5 lines. Line 3 revision 0.4.2-pha to 0.4.3-pha; line 364 (section 11.2 lead-in) appends an "Update at 0.4.3-pha" sentence; lines 376, 394 and 395 (the OQ-SAF-007, 025 and 026 rows) read "Closed (0.4.3-pha, 2026-09-26)" with "verified by INSP-008 iteration 3"; one new section 13 row (line 433) records the status-only revision. Nothing else changes.
- Consistency: recount over `hazards.json` gives 19 SRR-due questions at 9 Closed, 1 Answered (OQ-SAF-022) and 9 Open, as the line 364 update states, and 26 questions in all with 16 Open, as package section 18.1 revision 6 states. The section 11.2 row statuses equal the JSON statuses for the three questions. No em dash and no TBD added in either file.
- `render_risk.py --check --gate SRR --hazards docs/safety/hazards.json`: exit 0 ("register OK: 65 risks, 159 candidates, 0 warning(s), jsonschema used, gate SRR, hazard cross-check").

**Observation (no finding).** The new resolutions cite "Iteration 3 finding-8 row and answer 1"; the iteration 3 section numbers the relevant text as cross item 1, not an answer. The finding-8 row alone carries the evidence, so the citation resolves; recorded here for the author's next edit, not raised.

**Liens unchanged.** The edit does not touch the text of finding-14 (OQ-SAF-006 `resolution` item 3), finding-15 (section 9 item 3 and section 8.1 item 5) or finding-16 (section 9 item 3 last sentence, section 8.1 item 7 lead-in, section 11.2 column header still "Status (2026-09-25)"); all three remain as at iteration 3.

| Finding | Severity | Delta verification disposition | Evidence at HEAD `860e84e` |
|---|---|---|---|
| finding-14 | Minor | Lien: fix before PDR | OQ-SAF-006 `resolution` unchanged by `ade0e09` |
| finding-15 | Minor | Lien: fix before PDR | Section 9 item 3 and section 8.1 item 5 unchanged by `ade0e09` |
| finding-16 | Minor | Lien: fix before PDR | Stale prose unchanged; the 11.2 header still reads 2026-09-25 |

finding-1 to finding-13 stay Closed (Verified) from iteration 3; the delta touches none of their evidence. Disputed accepted: none.

**Delta verification answers.** R3 Yes (render_risk exit 0 above). CK-SAF-G1 stays No (Minor only; finding-14). R1 Yes for this product and record: `validate_docs.py` reports `PASS docs/safety/hazards.json` and `PASS docs/reviews/SRR/checklists/hazard-analysis.md` (no record drift: `product_files` equal the HEAD blobs). The run exits 1 (48 passed, 1 failed) only on `docs/reviews/SRR/checklists/tool-validation-tv-001-to-tv-010.md`, another record whose `product_files` name `tools/validate_docs.py` and its test at blobs older than HEAD after the R18 commits; outside this product and record. All other items stand as at iteration 3.

**Commands run (2026-09-26, delta verification).**
- `git show ade0e09 -- docs/safety/`, Python structural diff and line diff as above.
- `render_risk.py --check --gate SRR --hazards docs/safety/hazards.json`: exit 0.
- `validate_docs.py`: exit 1, 48 passed, 1 failed (the tool-validation record above, outside this product); this record and `hazards.json` PASS.
- `python -m unittest discover -s tools/tests`: 400 run, 1 failure (`test_validate_docs.RepositoryTests.test_repository_exit_zero`, the same repository-wide exit 1 outside this product).

**Verdict.** The R9 status edit is exactly the three status changes and their citations that iteration 3 verified, with the analysis consistent and no other change. No Major finding is open; finding-14, 15 and 16 remain Minor liens (fix before PDR). Readiness met. The verdict stays APPROVED with 3 liens (convergence rule). `record_status` stays for the lead SE (07 section 10.2).

```
ITERATION 3 DELTA VERIFICATION (2026-09-26): VERDICT: APPROVED (with liens). Delta-verified ade0e09 (0.4.3-pha): OQ-SAF-007, 025, 026 Closed with the iteration 3 citations; no other change. HEAD blobs hazard-analysis.md 49ec53f8, hazards.json c6bf757e. render_risk --check exit 0. Liens 3 (finding-14, 15, 16: Minor, fix before PDR); open Major 0.
```
