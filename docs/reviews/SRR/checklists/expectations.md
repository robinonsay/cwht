---
# Peer-review record front matter (charter section 5; docs/process/01-lifecycle-and-reviews.md
# section 13 is the single field list; docs/process/08-agent-briefing.md section 3.2).
id: INSP-001
checklist: peer-review-checklist-requirements
checklist_revision: C
checklist_file: docs/reviews/SRR/checklists/expectations.md
# product: the expectations product (SE-35, SE-37). Three files reviewed as one product; the
# JSON is the record, the .md its rendering, stakeholder-inputs.md the SI source log.
product: docs/requirements/l0-stakeholder/expectations.json
# product_commit: last commit that touched the three files (git log -1 -- docs/requirements/l0-stakeholder/)
# at the iteration 3 review baseline HEAD adcfe0946d2f1b5cd8f41a8f91eb4219a7fb99a1
product_commit: "8a37f8e"
# product_files: committed blobs re-reviewed at iteration 3 (git rev-parse HEAD:<path> at adcfe09).
# Iteration 2 reviewed the uncommitted working tree (json 01caefba, md 14fe59f0; not in the object store);
# iteration 1 reviewed json 3bdc1cd7, md b75d73c1 at 28e49e6. stakeholder-inputs.md is bcc2ec9f throughout.
product_files: ["docs/requirements/l0-stakeholder/expectations.json@59e7efba9e64da33285e4f780b2a3bae2753f45c", "docs/requirements/l0-stakeholder/expectations.md@3ac5617dc1c2933eed86c1f88c7bb88286b3f866", "docs/requirements/l0-stakeholder/stakeholder-inputs.md@bcc2ec9f0822b3b3866b10329fe1ce4ddc9e7841"]
product_size: 1 Need, 7 Goals, 22 Objectives, 13 MOEs, 28 constraints, 10 stakeholders, 36 SI rows
sprint: SRR-prep
author_agent: "author:expectations (Claude main session, lead systems engineer; commit 28e49e6)"
reviewer_agent: "reviewer:expectations"
# criticality and assurance: expectations are not a product of 07 sections 2.1.1 or 14.1
criticality: neither
assurance_required: false
assurance_reviewer_agent: none
# iteration 3: readiness R3 still No (finding-11, decision 115), so readiness_met stays false
iteration: 3
readiness_met: false
reviewer_verdict: NEEDS CHANGES
assurance_verdict: not-required
verdict: NEEDS CHANGES
findings_major: 2
findings_minor: 10
# iteration 3: finding-11 and finding-12 are liens "fix before PDR" (convergence rule of 2026-09-26),
# counted as deferred; no finding is Open
findings_open: 0
findings_fixed: 0
findings_verified: 10
findings_deferred: 2
assurance_findings_major: 0
assurance_findings_minor: 0
assurance_tasks_applied: []
deferred_rids: []
# items_no: iteration 3 answers (iteration 2: R3, CK-REQ-F1; iteration 1: R3, R4, A3, A7, A8, B1, E4, F1, F2).
# CK-REQ-F1 is No only for finding-12, now a lien
items_no: [R3, CK-REQ-F1]
# effort: cumulative over iterations 1 (38 turns, 45 min), 2 (22 turns, 30 min) and 3 (26 turns, 35 min)
effort_turns: 86
effort_minutes: 110
record_status: Open
date: 2026-09-25
date_closed: null
---

# Peer review record INSP-001: stakeholder expectations (SE-35, SE-37)

**Product.** `docs/requirements/l0-stakeholder/expectations.json` (record), `expectations.md` (rendering, 02 section 8.1) and `stakeholder-inputs.md` (SI-001 to SI-036), reviewed as one product for SRR entrance rows 1 to 3 (01 section 4.3) and minimum products SE-35 and SE-37 (01 section 4.5).

Iteration 3 reviewed the committed blobs of the front matter `product_files` (HEAD `adcfe09`, last product commit `8a37f8e`); the table below is the iteration 1 product.

| File | Git blob (hash-object, equals HEAD at iteration 1) | Last commit |
|---|---|---|
| `docs/requirements/l0-stakeholder/expectations.json` | `3bdc1cd731076ad47dcbcc7292bb14bce105765f` | 28e49e6 |
| `docs/requirements/l0-stakeholder/expectations.md` | `b75d73c129bd3426cf17881f6ceff44d9c65f50e` | 28e49e6 |
| `docs/requirements/l0-stakeholder/stakeholder-inputs.md` | `bcc2ec9f0822b3b3866b10329fe1ce4ddc9e7841` | 18dff3c (SI-036) and earlier |

**Checklist.** `docs/templates/peer-review-checklist-requirements.md` revision C, product-type row "Stakeholder expectations": applicable A3, A4, A5, A7, A8; B1 to B3; E4; F1 to F3; readiness R1 to R5. Not applicable (per that row): A1, A2, A6, B4 to B7, C1 to C8, D1 to D4, E1 to E3, E5, E6, F4, G1 to G8. The per-requirement validation table and the V2 block apply to requirement files and CRs only; this record carries a per-entry results table instead (section "Per-entry results").

**Reviewer.** `reviewer:expectations`, independent of the author (charter section 2; section 11 rule 4). The reviewer did not edit the product. Search first: `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before every `grep` (queries: SRR readiness shortfalls for expectations; 97.307(e) text; owner decisions on backlight and speaker; commercial 2 m CW handheld claim); `grep -n` was used afterwards only to pin lines.

**Verdict (iteration 3, 2026-09-26): NEEDS CHANGES on readiness R3 only.** No Major finding is open and no finding is Open: finding-1 to finding-10 stay Closed on the committed blobs, and finding-11 and finding-12 (Minor) are liens "fix before PDR" under the convergence rule of 2026-09-26. The record cannot read APPROVED because readiness R3 (author self-check) is still not met and the completion criteria of the checklist template and `tools/validate_docs.py` require `readiness_met: true` for APPROVED; it turns APPROVED when the author's self-check is filed or the owner waives it (decision 115). See "Iteration 3".

**Verdict (iteration 2): NEEDS CHANGES.** Both Major findings (finding-1, finding-2) are Verified closed, and eight of the nine iteration 1 Minor findings are Verified. Open: finding-11 (Minor, no author self-check on record, so readiness R3 fails) and finding-12 (Minor, raised in iteration 2). Iteration 1 verdict: NEEDS CHANGES with two Major and nine Minor findings. The section tables below are the iteration 1 answers; the iteration 2 answers are in "Closure (iteration 2)".

## Findings

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to | Disposition (iteration 2) |
|---|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | reviewer | Major | CK-REQ-B1, CK-REQ-A7 | CON-013 `rationale`; NGO-015 `rationale` | CON-013 (a constraint, "not open to trade", 02 section 3.2) says headphones-only is the audio report's D1 "which the owner adopted in the SRR brief"; NGO-015 says "no backlight in revision A is an owner decision recorded in the SRR brief". Neither decision has an `SI-NNN` row (02 section 3.1 rule 1: every owner statement is logged the day it is made; rule 3: SI rows are the only admissible evidence of stakeholder intent), and `docs/reviews/SRR/decisions-for-owner.md` lists both as still open: item 63 "Headphones only" and item 77 "Display and light", each "Needed by: SRR memo". The product would baseline a claimed owner decision that the decision list contradicts (charter section 11 rule 2). Fix: either reword both as "Proposed, owner decision pending at SRR (decisions-for-owner item 63 / item 77)", or, once Robin rules, log the rulings as new SI rows and cite them in `source_ids` and `rationale`. | Verified | Pending | | Closed. CON-013 `rationale` now reads Proposed, owner decision pending at SRR (decisions-for-owner.md item 63), with the ruling to be logged as a new SI row; NGO-015 `rationale` names D-UI-02 as Proposed, owner decision pending at SRR (item 77). `decisions-for-owner.md` lines 107 and 131 still list both as SRR-memo decisions with the last column as the package assumption, so product and decision list now agree. No claimed owner decision remains |
| <a id="finding-2"></a>finding-2 | reviewer | Major | CK-REQ-F1, CK-REQ-F2 | NGO-012 `statement`; NGO-014 `statement` | NGO-012 says the receiver "lets the operator set the receive pitch offset over +/-500 Hz in 10 Hz steps". NGO-014 says the sidetone is adjustable from 300 to 1000 Hz and "equals the receiver's CW pitch offset". The two ranges for one quantity conflict. The source is misread: `docs/research/cw-selectivity-options.md` line 127 (implication 4) is a BFO offset "adjustable over at least +/-500 Hz ... and stored per unit" to calibrate the filter-centre uncertainty, which is a per-unit calibration, not an operator control. The L1 set agrees with that reading: REQ-SYS-045 (sidetone 300 to 1000 Hz), REQ-SYS-046 (own-frequency carrier at the sidetone within 10 Hz) and REQ-SYS-144 (pitch centre is stored firmware calibration). NGO-003 also allows "nothing to configure beyond speed and pitch". Fix: restate NGO-012 so that the operator pitch is the NGO-014 sidetone range and the +/-500 Hz is a stored per-unit BFO calibration range, or drop that clause from the Objective. The ConOps text carries the same wording (cross item). | Verified | Pending | | Closed. NGO-012 `statement` now sets the operator pitch as the NGO-014 sidetone (300 to 1000 Hz in 10 Hz steps) and names the +/-500 Hz as the per-unit filter-centre calibration stored at acceptance, "not an operator control"; the `rationale` cites `cw-selectivity-options.md` implication 4 and REQ-SYS-035, 144, 045, 046. NGO-014 is unchanged and now consistent (one pitch quantity, one calibration quantity). The ConOps cross item stays with the ConOps author |
| <a id="finding-3"></a>finding-3 | reviewer | Minor | CK-REQ-A8 (WR-14) | `expectations.md` | The rendering is stale. `tools/traceability.py --report-only` reports `RENDER_STALE docs/requirements/l0-stakeholder/expectations.md: differs from the rendering of its JSON`. A re-render in a scratch copy of the repository (`--root <scratch> --render`) shows that the only difference is the missing section "7. Stakeholders", the eight-row table of the SE-35 stakeholder identification. The rendered SE-35 product therefore does not show the stakeholders (package section 6.1 says the same). Fix: `.venv/bin/python tools/traceability.py --render`, then commit. | Verified | Pending | | Closed. `traceability.py --report-only` (exit 0, 76 violations, 42 warnings in total) reports no `RENDER_STALE` and no line naming `expectations.md`, an NGO, MOE, CON or stakeholder id; `expectations.md` line 287 carries "## 7. Stakeholders" |
| <a id="finding-4"></a>finding-4 | reviewer | Minor | R4 (WR-12) | NGO-012 `rationale`; MOE-010 `success_criterion` | NGO-012: "the selectivity set is carried as TBR to the PDR selectivity trade". MOE-010: "The selectivity set is TBR until the PDR trade" and "The bench part is TBR (close by PDR)". Each TBR has a plan and a closing review, but none names an owner (charter section 7 and 08 section 1: a TBR carries owner, plan and close_by). The L0 schema has no `tbr` object, so the three fields must be in the text. Fix: name the owner of each TBR (for example the TS-001 selectivity trade author for the set and the 04 section 6.3 author for the bench source), or point to the ConOps Appendix C row that carries the owner. | Verified | Pending | | Closed. NGO-012 `rationale` gives the selectivity TBR owner (Robin at SRR and in the PDR memo; Claude as TS-001 author for the evidence), plan (TS-001 selects candidate A or B) and close_by PDR; MOE-010 `success_criterion` points the set to NGO-012 and gives the bench-source TBR owner, plan and close_by PDR. A scan of every entry that contains TBR (NGO-012, NGO-015, NGO-026, MOE-010) finds owner, plan and close_by in each; CON-020 is the policy entry |
| <a id="finding-5"></a>finding-5 | reviewer | Minor | CK-REQ-B1, CK-REQ-A7 | CON-008; CON-004; CON-003 `source_ids` | 02 section 3.2 rule 4: a constraint derived from 47 CFR cites the clause in `source_ids`. CON-008 rests on 47 CFR 15.23 but its `source_ids` are SI-035, SI-025 and SI-014 only. Its statement also leaves out the 15.23(a) condition "are not constructed from a kit" (corpus `47cfr-15.23.md` line 17), while SI-031, NGO-027 and CON-014 call the build model "kit assembly". `docs/research/part97-regulatory-basis.md` F9 settles the point ("A PCBWay-assembled board built to the owner's own design is not constructed from a kit"), but the constraint does not carry it. CON-004 derives from 47 CFR 1.1307(b), 1.1310, 2.1091 and 2.1093 and cites only 47CFR97.13(c). CON-003 derives from 97.305(c) and 97.3(a)(8) and cites neither. The corpus files for all of these exist. Fix: add the clauses to `source_ids`, and add the not-a-kit condition to CON-008 with the F9 basis. | Verified | Pending | | Closed. CON-003 `source_ids` add 47CFR97.305(c) and 47CFR97.3(a)(8); CON-004 add 47CFR1.1307(b), 1.1310, 2.1091, 2.1093 (the CON-004 household wording matches corpus 97.13(c)(1) as quoted in `part97-regulatory-basis.md` F6); CON-008 adds 47CFR15.23(a), the not-a-kit condition in its statement and the F9 basis in its rationale. Corpus files `47cfr-1.1307.md`, `47cfr-1.1310.md`, `47cfr-2.1091.md`, `47cfr-2.1093.md`, `47cfr-97.3.md`, `47cfr-97.305.md`, `47cfr-15.23.md` exist; traceability reports no unresolved clause |
| <a id="finding-6"></a>finding-6 | reviewer | Minor | CK-REQ-F1 | MOE-004 `success_criterion` | The criterion says "the 6.4 V low-battery transmit cutoff (REQ-SYS-097)". REQ-SYS-097 is a per-cell rule: refuse to start a transmission while "either cell, measured in receive, reads below 3.20 V +/-0.05 V". The two are equal only for balanced cells. With imbalance the per-cell rule trips above a 6.4 V pack voltage, so the 8 h and 6 h endurance endpoints are ambiguous. Fix: state the endpoint as REQ-SYS-097 defines it. | Verified | Pending | | Closed. MOE-004 `success_criterion` now ends each run when "the low-battery transmit inhibit of REQ-SYS-097 acts (either cell, measured in receive, below 3.20 V +/-0.05 V; 6.4 V only for a balanced pack)", which is the REQ-SYS-097 text |
| <a id="finding-7"></a>finding-7 | reviewer | Minor | CK-REQ-A3, CK-REQ-E4, CK-REQ-A4 | NGO-025, NGO-026, NGO-015 `statement`; MOE-011 `success_criterion` | 02 section 3.2 defines an Objective as a specific, measurable target, and CK-REQ-A3 and E4 apply to these entries. Several Objective terms have no bound. NGO-025 says "recharges ... in about 10 h", while MOE-004 bounds the same quantity at "at most 12 h". NGO-026 says "survives pocket carry" and "tolerates light rain" (REQ-SYS-117 quantifies the rain as IPX2 for 10 min). NGO-015 says a "small reflective display readable in daylight" ("small" is a WR-07 group B word). MOE-011 says "at most 100 mVrms +/-10 percent", which mixes an upper bound with a tolerance. Fix: give each term a number and a unit or a named test condition, and write MOE-011 as a single bound or as a nominal value with a tolerance. | Verified | Pending | | Closed. NGO-025: "in at most 12 h ... (10 h predicted)", matching MOE-004. NGO-026: 1.0 m drop on each face, 10 min IEC 60529 IPX2 upright with plugs in, at most 350 g (MOP-001) within the MOP-002 envelope, matching REQ-SYS-116 and REQ-SYS-117. NGO-015: frequency characters at least 4.0 mm, legible at 0.5 m under 300 lux or more, matching REQ-SYS-061 and REQ-SYS-165 (both TBR with owner, plan, close_by); "small" is gone. MOE-011: "90 to 110 mVrms (the 100 mVrms +/-10 percent ceiling of REQ-SYS-071)", a single range. The TBR plan wording introduced in NGO-026 is finding-12 |
| <a id="finding-8"></a>finding-8 | reviewer | Minor | CK-REQ-A7 | NGO-001 `rationale` | The rationale says "No commercial product offers a pocket 2 m true-CW transceiver with a built-in keyer for both key types (SI-018)". SI-018 states the core requirement, not a market fact. `docs/research/2m-cw-transceiver-reference-designs.md` F3 records the Mizuho MX-2, a historical 2 m SSB/CW handheld. Fix: cite the research findings (F3 to F5) and limit the claim to what they show (for example, no current product with a built-in keyer for both key types; the MX-2 is a historical precedent without one). ConOps section 1.1 repeats the claim (cross item). | Verified | Pending | | Closed. NGO-001 `rationale` now cites `2m-cw-transceiver-reference-designs.md` F1 to F5 and limits the claim to the products that survey covers, with the Mizuho MX-2 (F3) as the historical 200 mW SSB/CW handheld precedent and F1, F2, F4, F5 as portables; this matches the report text at lines 29 to 37. SI-018 is cited only as the core requirement. The ConOps section 1.1 cross item stays with the ConOps author |
| <a id="finding-9"></a>finding-9 | reviewer | Minor | CK-REQ-B3 (SE HB section 4.1.1.2.1) | `stakeholders` array | The product relies on two groups that the array does not identify. (a) Members of the licensee's household are the only non-licensees whom 47 CFR 97.13(c)(1) lets the licensee evaluate at the occupational tier (CON-004 statement; `docs/research/rf-exposure-evaluation.md` line 46), and the handbook is their information source. (b) Unlicensed third parties key under supervision per 97.115(b) (CON-006, NGO-020, OPS-019, MOE-009) and are evaluated at the general-population tier. The "public" entry covers only reusers and bystanders. Fix: add the two groups (roles `public` or `guest operator`, with `represented_by` Robin and the handbook), or widen the notes of the existing entries to cover them. Adding entries after SRR needs a CR (02 section 3.0). | Verified | Pending | | Closed. `stakeholders` adds "Members of the licensee's household" (role public; occupational limits only with the training and information of 47 CFR 97.13(c)(1), otherwise general population) and "Unlicensed third parties keying under supervision" (role guest operator; 97.115(b)), each with `represented_by` Robin, `source_ids` and a note on the CR rule. The household wording agrees with corpus 97.13(c)(1) and `rf-exposure-evaluation.md` line 46; the schema validates (validate_docs PASS) and T-21 reports no `STAKEHOLDERS_MISSING` |
| <a id="finding-10"></a>finding-10 | reviewer | Minor | CK-REQ-A8 | NGO-019 `rationale` | Editorial: a sentence starts in lower case ("... raises the cutoff window. the 0.6 m and 1.0 m rules are its F7"). The rationale also says "its F7", where "its" refers back to a report named three sentences earlier; name the report. | Verified | Pending | | Closed. NGO-019 `rationale`: "The 0.6 m and 1.0 m separation rules are docs/research/rf-exposure-evaluation.md F7"; the report is named and the sentence starts in upper case |
| <a id="finding-11"></a>finding-11 | reviewer | Minor | R3 | author return | There is no author return on record with the self-check against the checklist sections and the brief's acceptance criteria. The assignment's author summary reads "no new authoring this run", and commit 28e49e6 carries no self-check. Readiness R3 is therefore not met, and `readiness_met` is false. Fix: the author records the self-check (sections A, B and F of the checklist) in the re-review brief. | Lien: fix before PDR (iteration 3) | Pending (decision 115) | PDR | Open. The author's fix list names F-11 as fixed, but no self-check against checklist sections A, B and F and the brief's acceptance criteria was supplied with the re-review assignment, none is in the product files, and a claude-context search of the repository for an expectations author self-check found none. A fix list is an assertion, not the self-check (charter section 11 rule 2). R3 stays No and `readiness_met` stays false. Close by filing the author's self-check with the next re-review brief |
| <a id="finding-12"></a>finding-12 | reviewer (iteration 2) | Minor | CK-REQ-F1, R4 | NGO-026 `rationale` | Introduced by the finding-7 fix. NGO-026 says REQ-SYS-116 and REQ-SYS-117 carry the drop height and the IPX2 condition "as TBR: owner Robin on Claude's proposal, plan the PDR enclosure analysis, close_by PDR". The `tbr.plan` of both L1 requirements in `docs/requirements/sys/requirements.json` reads instead: Robin decides the environment set (`docs/conops/conops.md` section 4, Appendix C) at SRR; TPM-006 span reconciled at PDR. One TBR now has two different closure plans (charter section 7: a TBR carries one owner, plan and target review). Fix: quote or cite the L1 `tbr` plan in NGO-026 (or change the L1 plan by the same revision so the two agree). | Lien: fix before PDR (iteration 3) | Pending | PDR | Open (raised in iteration 2) |

## Readiness criteria

| # | Criterion | Answer | Evidence |
|---|---|---|---|
| R1 | The product validates | Yes (product); whole run exit 1 for a file outside the product | `tools/validate_docs.py`: `PASS  docs/requirements/l0-stakeholder/expectations.json  (schema: docs/requirements/l0-stakeholder/schema.json)`; the run exits 1 with `FAIL docs/design/allocation.json - schema not found: docs/design/allocation.schema.json`. That file is not part of this product and is reported under cross |
| R2 | `tools/traceability.py` reports no violation for the ids in the file | Yes | `--report-only` run: 82 violations and 52 warnings in total. None names an NGO, MOE, CON or stakeholder id: no `EXPECTATIONS_INCONSISTENT` and no `STAKEHOLDERS_MISSING` (T-21, implemented at `tools/traceability.py` line 302). One warning, `RENDER_STALE`, concerns `expectations.md` (finding-3). An independent reviewer script resolved all 36 SI rows (every row cited at least once), every `parent_id`, `ngo_ids` entry and `ops_ids` entry (22 OPS headings in `conops.md`), and a corpus file for each of the 18 cited `47CFR` clauses |
| R3 | Author self-check return | No | finding-11 |
| R4 | Every TBR has owner, plan, close_by; no to-be-determined placeholder | No | No to-be-determined placeholder string in the JSON (reviewer scan for the three-letter token). TBRs in NGO-012 and MOE-010 have no owner (finding-4). CON-020 names the TBR policy, not a TBR |
| R5 | CR impact assessment | N/A | Not a CR |

## A. Format and editorial

| Id | Answer | Evidence |
|---|---|---|
| CK-REQ-A1 | N/A | Product-type row: NGO and MOE records are not "shall" statements. A scan finds no `shall` in any NGO, MOE or CON entry (schema-enforced) |
| CK-REQ-A2 | N/A | Product-type row |
| CK-REQ-A3 | No | Most Objectives and MOE success criteria are quantified with units and bounds: NGO-009 5.0 km at 5 W and 2.0 km at 2 W; NGO-013 +/-1 percent or +/-0.5 ms and 3 ms; NGO-017 25 microwatts and 53 dB; MOE-004 8 h, 6 h, 15 min, 12 h. Exceptions: NGO-025, NGO-026, NGO-015 and MOE-011 (finding-7) |
| CK-REQ-A4 | No (Objectives); Yes (MOE success criteria) | A reviewer scan against the WR-07 list: the MOE success criteria are clean. MOE statements use "can" and "should" (MOE-007), which is acceptable because 02 section 3.2 lets an MOE statement be qualitative, and the success criterion carries the measure. Objective NGO-015 uses "small" as its only size criterion (finding-7). Modal "can" in the Objectives (NGO-011, 016, 019, 023) states a capability, not a measure, and is accepted |
| CK-REQ-A5 | Yes, with note | Objectives name functions, not parts: NGO-021 "a hardware cutoff independent of firmware", NGO-016 "limited by hardware", NGO-026 "a jack retained by the enclosure". Each is an owner-level independence or safety property with its research basis in the rationale. Part numbers and topologies appear only in rationales (NGO-014 HF3 class, CON-021) |
| CK-REQ-A6 | N/A | Product-type row. Ids are sequential with no gaps: NGO-001 to NGO-030, MOE-001 to MOE-013, CON-001 to CON-028 |
| CK-REQ-A7 | No | Every entry has a rationale that cites its SI source and research findings with F-numbers. Exceptions: finding-1 (claimed owner decisions without an SI row), finding-5 (clauses missing from `source_ids`), finding-8 (a market claim cited to SI-018) |
| CK-REQ-A8 | No | Key-type spellings "straight key" and "iambic paddle" match SI-018 and the L1 file. finding-3 (stale rendering) and finding-10 (editorial) |

## B. Stakeholder satisfaction and traceability

| Id | Answer | Evidence |
|---|---|---|
| CK-REQ-B1 | No | Parent structure per 02 section 3.2 rule 3 holds: one Need (NGO-001); every Goal (NGO-002 to NGO-008) has the Need as parent; every Objective (NGO-009 to NGO-030) has a Goal as parent. Every NGO cites at least one SI (rule 2). Every MOE cites at least one NGO and at least one OPS. Exceptions: finding-1, finding-5 |
| CK-REQ-B2 | Yes | Each Objective is necessary for its Goal. No Objective duplicates another (the finding-2 conflict is a wrong value, not a redundant entry) |
| CK-REQ-B3 | Yes, with finding-9 | Every Goal has at least one Objective: NGO-002 {009 to 012}, NGO-003 {013 to 016}, NGO-004 {017 to 022}, NGO-005 {023, 024}, NGO-006 {025, 026}, NGO-007 {027 to 029}, NGO-008 {030}. Every Goal except NGO-008 is judged by at least one MOE. NGO-008, NGO-029 and NGO-030 have no MOE and state that they are judged by Inspection through REQ-SYS-145, REQ-SYS-146 and REQ-SYS-148 (all exist, Draft). Stakeholder coverage: finding-9 |
| CK-REQ-B4 to B7 | N/A | Product-type row |

## C. Technical correctness, D. Feasibility

N/A per the product-type row (CK-REQ-C1 to C8, D1 to D4). The reviewer still checked the numbers against their sources (brief: "verify numbers against their sources"); results are in "Numbers verified" below.

## E. Verifiability

| Id | Answer | Evidence |
|---|---|---|
| CK-REQ-E1 to E3, E5, E6 | N/A | Product-type row |
| CK-REQ-E4 | No | Twelve of the thirteen MOEs have an observable pass criterion with its judging event: MOE-001 exchange content and error count; MOE-003 stages 0 to 8 without respin; MOE-006 tinySA measurement points and limits; MOE-012 13 s and 100 h log. The subjective ratings (MOE-005, MOE-011, MOE-013) are judged by named raters. MOE-007 depends on the budget number that Robin fixes at SRR (TPM-014; decision list). Exceptions: MOE-011 bound and tolerance, and the Objective terms of finding-7 |

## F. Non-redundancy and consistency

| Id | Answer | Evidence |
|---|---|---|
| CK-REQ-F1 | No | finding-2 (pitch range conflict), finding-6 (cutoff endpoint). Cross-checks that hold: tune end "5 s +/-0.5 s" (NGO-019) against "at most 5.5 s" (NGO-021, MOE-012, REQ-SYS-020); cutoff "10 s (7.5 to 13 s)" (NGO-021) against REQ-SYS-055; carrier range 144.001 to 147.999 MHz (NGO-011) against REQ-SYS-008 and REQ-SYS-009; 4.0 N m antenna moment (MOE-013) against REQ-SYS-105; -10 to +45 C (NGO-026, MOE-013) against REQ-SYS-114 |
| CK-REQ-F2 | No | finding-2: "pitch offset" names both the operator setting and the per-unit BFO calibration |
| CK-REQ-F3 | Yes | No entry states product-level design detail that belongs in L1 or L2, beyond the research-derived values that are labelled as proposals |
| CK-REQ-F4 | N/A | Product-type row |

## G. Plans

N/A per the product-type row (CK-REQ-G1 to G8).

## SE-35 and SE-37 content judgment (01 section 4.3 rows 1 to 3; 4.5)

| Criterion | Judgment | Evidence |
|---|---|---|
| SE-35 stakeholders identified (NPR 7123.1D section 5.2.2.2 item (1) "Baselined stakeholder identification and expectation definitions [SE-35]", corpus `npr-7123-1d/05-chapter5.md` line 66) | Content present; not ready to baseline | The eight `stakeholders` entries match the 02 section 3.0 table field for field (name, role, interests, represented_by, source_ids). Names are unique, the customer, user and regulator roles are present, and every source resolves (T-21 passes). Open: finding-3 (not rendered) and finding-9 (two groups missing). Robin's confirmation of the representation rule belongs in the SRR memo (H4) |
| Expectations (NGOs) ready to baseline (G-3 3.1, 5.1) | Not ready | Structure and traceability pass (B1 structure, B3). Blocking: finding-1 and finding-2. Twenty-one entries say "owner decision pending at SRR"; every decision id they cite (D-KN1 to D-KN10, RFX-D1 to D5, D-UI-03, 04 and 07, D-PWR-01 to 08, DECISION-6, 7 and 9, OQ-SE-005, audio D2 and D4, D-PCB-01) appears in `docs/reviews/SRR/package.md`, so the owner's rulings at SRR close them |
| SE-37 MOEs and success criteria defined, ready to approve (G-3 3.3; corpus `05-chapter5.md` line 70, "[SE-37]") | Ready to approve after finding-6 and finding-7 | Thirteen MOEs, each with a success criterion, `ngo_ids`, `ops_ids` and a judging event. `docs/plan/tpm.json` MOPs name MOE-001 to MOE-012. MOE-013 cites MOP-001 and MOP-002, which still point to MOE-001; this is the disclosed OQ-SE-005 dependency (the MOP-001 note), and its re-parenting on approval is a `tpm.json` edit (cross) |

## Numbers verified against sources

| Value in product | Source checked | Result |
|---|---|---|
| 53.0 dB at 5 W, 53.8 dB at 6 W; 25 microwatts; 40 dB; 10 microwatt floor (CON-002, NGO-017) | corpus `47cfr-97.307.md` (e); `docs/research/part97-regulatory-basis.md` F2 table | Agrees (10 log10(5 / 25e-6) = 53.0) |
| 26 dB bandwidth definition (MOE-006) | corpus `47cfr-97.3.md` line 31, (a)(8) | Agrees |
| 20 WPM automatic ID; 10 minutes (CON-005, NGO-020) | corpus `47cfr-97.119.md` lines 17, 21 | Agrees |
| Beacons 144.275 to 144.300 MHz automatic control (CON-006) | corpus `47cfr-97.203.md` (d); `47cfr-97.109.md` (b), (d) | Agrees |
| Third party only with the control operator present and supervising (CON-006, NGO-020) | corpus `47cfr-97.115.md` (b)(1) | Agrees |
| Technician 2 m, 144 to 148 MHz Region 2 (CON-001) | corpus `47cfr-97.301.md` (a) table row "2 m" | Agrees |
| Minimum power; 1.5 kW PEP (CON-007) | corpus `47cfr-97.313.md` (a), (b) | Agrees |
| Five or fewer units, not marketed (CON-008) | corpus `47cfr-15.23.md` (a) | Agrees on count; the kit condition is left out (finding-5) |
| No exemption below 239 MHz within 20 cm (CON-004) | corpus `fcc-19-126-extracts.md` footnote 143 | Agrees |
| +/-2.5 ppm gives +/-370 Hz at 148 MHz (NGO-011) | arithmetic | Agrees |
| 26 dB bandwidth 226 to 292 Hz at 50 WPM, 5 ms; 208HA1A (NGO-011, NGO-018) | `docs/research/regulatory-corpus-and-operators.md` lines 110, 128, 131 | Agrees |
| 10.1 km horizon; 46 km at 100 m; 109 dB; 38 to 59 dB; 5.0 km and 2.0 km candidates (NGO-002, 009, 010) | `docs/research/antenna-and-erp.md` lines 220, 253, 257, 275 | Agrees. The 109 dB is the loss at the 46.3 km horizon, not at the 30 km objective distance; the text states it next to the horizon figure, so no finding |
| 17.5 percent of 8 W/kg at 5 W continuous CW, 0.35 W/kg per W; 0.58 m and 0.91 m (NGO-019) | `docs/research/rf-exposure-evaluation.md` lines 94, 151, 163 to 175, 189 | Agrees |
| 9.5 h at 1:9 and 7.3 h at 1:4; about 280 mA and about 10 h charge (NGO-025, MOE-004) | `docs/research/power-tree-and-charging.md` lines 32, 125 | Agrees |
| 5 s straight-key timeout, 128 elements or 30 s, 10 s cutoff with 7.5 to 13 s window (NGO-021, MOE-012) | `docs/research/keyer-verification-and-key-input-network.md` lines 219, 220, 230 | Agrees |
| 121.6 dB/V earbuds; 113 to 126 dB SPL unrestricted (NGO-016, MOE-011) | `docs/research/audio-output-and-hearing-safety.md` F23, F25 | Agrees |
| USD 970 to 1830 for three units; USD 323 to 610 per unit (NGO-028, MOE-007) | `docs/plan/cost-estimate.md` line 15; arithmetic | Agrees |
| +/-500 Hz pitch offset (NGO-012) | `docs/research/cw-selectivity-options.md` line 127 | Misread (finding-2) |
| Summary counts in `expectations.md` (1, 7, 22, 13, 28, 71 Draft, 36 SI, 18 clauses) | reviewer script over the JSON | Agrees |

## Per-entry results (expectations; replaces the per-requirement table for this product type)

| Entries | Result | Findings |
|---|---|---|
| Stakeholders (8 entries) | Pass, with gaps | finding-3, finding-9 |
| NGO-001 | Fail | finding-8 |
| NGO-002 to NGO-011, NGO-013, NGO-016 to NGO-018, NGO-020 to NGO-024, NGO-027 to NGO-030 | Pass | none |
| NGO-012 | Fail | finding-2, finding-4 |
| NGO-014 | Fail | finding-2 |
| NGO-015 | Fail | finding-1, finding-7 |
| NGO-019 | Fail | finding-10 |
| NGO-025, NGO-026 | Fail | finding-7 |
| MOE-001 to MOE-003, MOE-005 to MOE-009, MOE-012, MOE-013 | Pass | none |
| MOE-004 | Fail | finding-6 |
| MOE-010 | Fail | finding-4 |
| MOE-011 | Fail | finding-7 |
| CON-001, CON-002, CON-005 to CON-007, CON-009 to CON-012, CON-014 to CON-028 | Pass | none |
| CON-003, CON-004, CON-008 | Fail | finding-5 |
| CON-013 | Fail | finding-1 |
| `stakeholder-inputs.md` SI-001 to SI-036 | Pass | Append-only, dated, verbatim. Supersessions are handled by later rows and restated in the entries that use them: SI-031 over SI-009 (NGO-007, CON-014), SI-034 over SI-013 and SI-021 (CON-016, MOE-006), SI-026 over SI-010 (NGO-005, CON-025), SI-036 closes SI-035 (CON-021). The bold core input SI-018 is present |

## Cross items (outside this record's scope)

| File | Change | Reason |
|---|---|---|
| `docs/conops/conops.md` lines 267 and 830 | Same fix as finding-2 for the "pitch offset adjustable over +/-500 Hz" wording | Same misreading of the research finding |
| `docs/conops/conops.md` section 1.1 | Same fix as finding-8 | Same unsupported market claim |
| `docs/plan/tpm.json` MOP-001, MOP-002 | Re-parent to MOE-013 if Robin approves OQ-SE-005 | Disclosed dependency (MOP-001 note) |
| `docs/design/allocation.json` | Add `docs/design/allocation.schema.json` or change the validate_docs convention | `tools/validate_docs.py` exits 1 ("schema not found"); outside this product |

## Measurements (SWE-089)

Items applicable 16, including readiness R1 to R5. Items answered No: 9 (R3, R4, A3, A7, A8, B1, E4, F1, F2). Findings: Major 2, Minor 9. Fixed 0, deferred 0. Iteration 1. Effort: 38 turns, 45 minutes. Iteration 2: one new Minor finding (finding-12); Verified 10, Open 2, deferred 0; items answered No: 2 (R3, CK-REQ-F1); effort 22 turns, 30 minutes (cumulative 60 turns, 75 minutes). Entries reviewed: 8 stakeholders, 30 NGOs, 13 MOEs, 28 constraints, 36 SI rows.

## Closure (iteration 2)

**Re-review scope.** The author reported F-01 to F-11 (this record's finding-1 to finding-11) as fixed and none disputed. The reviewer (`reviewer:expectations`, new invocation, same role; did not edit the product) re-opened the working-tree revision whose blobs are in the front matter (`expectations.json` 01caefba, `expectations.md` 14fe59f0; `stakeholder-inputs.md` unchanged, bcc2ec9f), read every changed entry against `git diff` of the JSON, and checked each fix against its source. Search first: `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any `grep` (queries: author self-check for expectations; 97.13(c)(1) household provision); `grep -n` then pinned lines in `decisions-for-owner.md` and the reference-design report.

**Dispositions.** Closed (Verified): finding-1 to finding-10, each with its evidence in the Disposition column. Disputed accepted: none (nothing was disputed). Open: finding-11 (the self-check is asserted, not supplied) and finding-12 (new; the NGO-026 TBR plan disagrees with the L1 `tbr` plan of REQ-SYS-116 and REQ-SYS-117).

**Iteration 2 answers.**

| Item | Answer | Evidence |
|---|---|---|
| R1 | Yes (product) | `validate_docs.py` exit 1 for the whole run, caused only by `FAIL docs/design/allocation.json - schema not found` (outside this product, still the cross item below); `PASS docs/requirements/l0-stakeholder/expectations.json` and `PASS docs/reviews/SRR/checklists/expectations.md` |
| R2 | Yes | `traceability.py --report-only` exit 0; 76 violations and 42 warnings in total, none naming an NGO, MOE, CON or stakeholder id or `expectations.md` |
| R3 | No | finding-11 |
| R4 | Yes | Every TBR in NGO-012, NGO-015, NGO-026 and MOE-010 carries owner, plan and close_by; no to-be-determined placeholder and no em dash in the JSON (reviewer scan). The NGO-026 plan disagrees with L1 (finding-12, scored under F1) |
| CK-REQ-A3, A4, E4 | Yes | finding-7 closed |
| CK-REQ-A7, B1 | Yes | finding-1, finding-5, finding-8 closed |
| CK-REQ-A8 | Yes | finding-3, finding-10 closed |
| CK-REQ-B3 | Yes | finding-9 closed; 10 stakeholders |
| CK-REQ-F1 | No | finding-2 and finding-6 closed; finding-12 open |
| CK-REQ-F2 | Yes | finding-2 closed |

**SE-35 and SE-37 judgment (iteration 2).** SE-35: stakeholders identified and rendered (10 entries); ready to baseline once the owner confirms the representation rule in the SRR memo (H4). Expectations: no Major finding open; the entries marked "owner decision pending at SRR" close with the owner's rulings. SE-37: ready to approve (finding-6 and finding-7 closed).

**Counts.** Major 2 (both Verified, 0 open). Minor 10 (8 Verified, 2 open: finding-11, finding-12). Deferred 0. `readiness_met` false (R3). `reviewer_verdict` NEEDS CHANGES: 07 section 10.2 completion criteria need every Minor finding fixed or deferred and readiness met. The record stays `record_status: Open`; iteration 3 verifies the self-check and the NGO-026 plan, or the owner defers either to PDR by decision memo.

## Iteration 3 (2026-09-26, re-review against the committed blobs; SRR package items R8 and R13 rule)

**Scope and independence.** Review baseline HEAD `adcfe0946d2f1b5cd8f41a8f91eb4219a7fb99a1`. Reviewed blobs (`git rev-parse HEAD:<path>`): `expectations.json` `59e7efba9e64da33285e4f780b2a3bae2753f45c`, `expectations.md` `3ac5617dc1c2933eed86c1f88c7bb88286b3f866`, `stakeholder-inputs.md` `bcc2ec9f0822b3b3866b10329fe1ce4ddc9e7841` (unchanged since `18dff3c`). The product was last committed at `8a37f8e`. The iteration 2 blob `01caefba` is not in the object store (`git cat-file -e` fails; package section 2.3), so the reviewer read the whole `git diff --word-diff 28e49e6 HEAD` of the JSON and compared every changed entry with the text quoted in the iteration 2 dispositions. Reviewer: `reviewer:expectations`, a new invocation of the reviewer role; it did not author and did not edit the product (charter section 11 rule 4). Search first: `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any `grep` (queries: author self-check for expectations INSP-001; decision 115 self-check filing; REQ-SYS-116 TBR plan; validate_docs record drift rule; TS-NNN-synthesizer-reference numbering); `grep -n` was used afterwards only to pin lines. Convergence rule of 2026-09-26 (lead SE, applying charter section 4 item 3): in this round only Major findings change products, and every Minor finding is dispositioned "Lien: fix before PDR".

**Tool runs at HEAD `adcfe09`.** `tools/validate_docs.py`: exit 0, 37 passed, 0 failed; `PASS docs/requirements/l0-stakeholder/expectations.json`. `tools/traceability.py --report-only`: exit 0, 237 requirements, 170 test cases, 0 violations, 2 warnings (`SYS_UNALLOCATED` REQ-SYS-125 and REQ-SYS-148, outside this product); no line names an NGO, MOE, CON or stakeholder id, and no `RENDER_STALE` for `expectations.md`. Reviewer script over the JSON: 10 stakeholders, 30 NGOs, 13 MOEs, 28 constraints; no em dash and no to-be-determined token.

**Disposition of every finding at HEAD.**

| Finding | Severity | Disposition (iteration 3) | Evidence at HEAD (`expectations.json` blob `59e7efba`) |
|---|---|---|---|
| finding-1 | Major | Closed | CON-013 `rationale` (line 640): "Proposed, owner decision pending at SRR (docs/reviews/SRR/decisions-for-owner.md item 63 ...)"; NGO-015 `rationale` (line 226): D-UI-02 "Proposed, owner decision pending at SRR (docs/reviews/SRR/decisions-for-owner.md item 77)". No claimed owner decision remains |
| finding-2 | Major | Closed | NGO-012 `statement` (line 195): operator pitch is the NGO-014 sidetone, 300 to 1000 Hz in 10 Hz steps; the +/-500 Hz is "a per-unit calibration stored at acceptance ... not an operator control"; `rationale` (line 196) separates the two quantities (REQ-SYS-035, 144, 045, 046) |
| finding-3 | Minor | Closed | `traceability.py --report-only` exit 0 with no `RENDER_STALE`; `expectations.md` blob `3ac5617d` is the rendering of the JSON |
| finding-4 | Minor | Closed | NGO-012 `rationale` (line 196) and MOE-010 `success_criterion` (line 485) give owner, plan and close_by PDR for each TBR |
| finding-5 | Minor | Closed | CON-003 `source_ids` (line 551) add 47CFR97.305(c), 47CFR97.3(a)(8); CON-004 (line 560) add 47CFR1.1307(b), 1.1310, 2.1091, 2.1093; CON-008 (lines 594 to 596) carries 47CFR15.23(a), the not-a-kit condition and the F9 basis |
| finding-6 | Minor | Closed | MOE-004 `success_criterion` (line 419) ends each run on the REQ-SYS-097 inhibit, "either cell, measured in receive, below 3.20 V +/-0.05 V", which matches the REQ-SYS-097 description at HEAD |
| finding-7 | Minor | Closed | NGO-025 (line 325) "at most 12 h ... (10 h predicted)"; NGO-026 (line 335) 1.0 m drop on each face, 10 min IPX2, at most 350 g (MOP-001 threshold "350 (provisional allocation, charter section 12)"; charter section 12, SE-62 row, "provisional allocation 350 g"); NGO-015 (line 225) 4.0 mm and 300 lux, matching REQ-SYS-061 and REQ-SYS-165 at HEAD; MOE-011 (line 496) "90 to 110 mVrms" |
| finding-8 | Minor | Closed | NGO-001 `rationale` (line 86) cites `2m-cw-transceiver-reference-designs.md` F1 to F5 with the Mizuho MX-2 (F3) as the historical precedent |
| finding-9 | Minor | Closed | `stakeholders` entries "Members of the licensee's household" and "Unlicensed third parties keying under supervision" (lines 26 to 41); 10 entries |
| finding-10 | Minor | Closed | NGO-019 `rationale` (line 266): "The 0.6 m and 1.0 m separation rules are docs/research/rf-exposure-evaluation.md F7" |
| finding-11 | Minor | Lien: fix before PDR | Still not fixed: no author self-check against checklist sections A, B and F and the brief's acceptance criteria came with the iteration 3 assignment, none is in the product files, and the claude-context searches above found none (the only hits are this record and decision 115). Owner ruling pending: decision 115 (waive or not; the package recommends no waiver). Readiness R3 stays No |
| finding-12 | Minor | Lien: fix before PDR | Still not fixed: NGO-026 `rationale` (line 336) still gives the REQ-SYS-116 and REQ-SYS-117 TBR as "owner Robin on Claude's proposal, plan the PDR enclosure analysis, close_by PDR", while the `tbr.plan` of both requirements at HEAD reads "Robin decides the environment set (docs/conops/conops.md section 4, Appendix C) at SRR; TPM-006 span reconciled at PDR." |

Disputed-accepted: none (the author disputed nothing).

**Scan for new defects in text changed since this record's quotes.** The HEAD JSON carries every iteration 2 fix quoted in the Disposition column. One change is not quoted there: CON-028 `rationale` (line 775) now names "the synthesizer and reference trade study of docs/design/concept.md section 11.2, TS-NNN-synthesizer-reference, number assigned at creation per docs/process/06-risk-and-decision-analysis.md section 13 item 3" instead of "TS-002". This agrees with `docs/design/concept.md` section 11.2 (TS-002 is the firmware runtime make/buy study; the synthesizer study is `TS-NNN-synthesizer-reference` until its file exists) and with ADR-013; it is correct and closes a stale id. The other re-checked values hold at HEAD: REQ-SYS-061 (4.0 mm TBR), REQ-SYS-165 (300 lux TBR), REQ-SYS-071 (100 mVrms +/-10 percent TBR), REQ-SYS-097 (3.20 V +/-0.05 V TBR); MOP-001 350 g; SE-35 and SE-37 at corpus `npr-7123-1d/05-chapter5.md` lines 66 and 70. New Major findings: none. New Minor findings: none.

**Lien table (convergence rule of 2026-09-26; carried by the package as Routine items, section 20.1 L-6).**

| Finding | Severity | Disposition | Owner | Fix | Due |
|---|---|---|---|---|---|
| finding-11 | Minor | Lien: fix before PDR | Expectations author (Claude, lead SE); Robin for decision 115 | File the author self-check against checklist sections A, B and F and the brief's acceptance criteria, or the owner waives it by decision 115 | PDR readiness declaration |
| finding-12 | Minor | Lien: fix before PDR | Expectations author (Claude) | Cite or quote the L1 `tbr` plan of REQ-SYS-116 and REQ-SYS-117 in NGO-026, or change the L1 plan in the same revision so the two agree | PDR readiness declaration |

**Iteration 3 answers.** R1 Yes (`validate_docs.py` exit 0). R2 Yes (`traceability.py --report-only` exit 0, no violation or warning naming this product). R3 No (finding-11, lien; decision 115). R4 Yes (every TBR has owner, plan, close_by; no to-be-determined placeholder). R5 N/A. CK-REQ-A3, A4, A5, A7, A8, B1, B2, B3, E4, F2, F3 Yes (unchanged from iteration 2 on the committed blob). CK-REQ-F1 No (finding-12, lien).

**Verdict and reason.** Open Major findings: 0. Findings: 12 (Major 2, Minor 10); Closed 10, Disputed-accepted 0, Lien 2, Open 0. Under the convergence rule the findings alone would give APPROVED (with liens). The record nevertheless stays **NEEDS CHANGES**, and only because readiness R3 is false: the checklist completion criteria ("readiness R1 to R5 were true") and `tools/validate_docs.py` ("APPROVED needs readiness_met true") do not allow APPROVED with `readiness_met: false`, and the reviewer cannot set R3 to Yes without the self-check (charter section 11 rule 2). The record becomes APPROVED (with liens) without any product change when either the author's self-check is filed and checked, or Robin waives R3 for this record by decision 115; the re-issue then only updates `product_files` if the product has changed. SE-35, SE-37: no Major finding against the stakeholders, expectations or MOEs; ready to baseline and approve subject to the owner rulings named in the entries and H4.

**Measurements (SWE-089), iteration 3.** Items re-checked 16 (R1 to R5 and the 11 applicable items); items answered No 2 (R3, CK-REQ-F1); findings re-dispositioned 12 (Closed 10, Lien 2); new findings 0; effort 26 turns, 35 minutes (cumulative 86 turns, 110 minutes).

```
ITERATION 3 (2026-09-26): VERDICT: NEEDS CHANGES (readiness R3 only; decision 115). Closed 10 (Major 2, Minor 8); Disputed accepted 0; Lien 2 (finding-11, finding-12, Minor, fix before PDR); Open 0. Open Major 0. Blobs: expectations.json 59e7efba, expectations.md 3ac5617d, stakeholder-inputs.md bcc2ec9f (HEAD adcfe09).
```

## Completion

Iteration 3: no finding is Open and no Major finding remains; finding-11 and finding-12 are liens "fix before PDR". The verdict stays NEEDS CHANGES only for readiness R3 (decision 115); see "Iteration 3". Iteration 2 text follows.


Iteration 2: finding-1 and finding-2 are Verified; the verdict stays NEEDS CHANGES only for the open Minor findings and readiness R3 (see "Closure (iteration 2)"). Iteration 1 text follows. The verdict is NEEDS CHANGES while finding-1 and finding-2 are Open (charter section 4 item 3: a Major finding blocks the baseline). Re-review (iteration 2) after the author's revision; the Minor findings are fixed in the same revision or deferred with an owner decision reference.

## Author self-check (readiness R3; finding-11; package item R7; filed 2026-09-26)

**Written by the expectations author, not the reviewer.** Author: `author:expectations` (Claude in the requirements author role of 08 section 3.1, for the expectations product of commit 28e49e6). This section is the author's return that readiness R3 of `docs/templates/peer-review-checklist-requirements.md` revision C asks for ("The author's return states the self-check against sections A to G below and lists the brief's acceptance criteria"). It is filed in this record because 01 section 13 says no record lives only in conversation and 07 section 10.2 (Readiness criteria row) says the brief's acceptance criteria are listed in the review record. Every other section, the front matter, the R3 answer, finding-11 and `readiness_met` belong to the reviewer and are unchanged; the reviewer answers R3 again when it re-issues the record (package item R8). No product file was changed (convergence rule, charter section 4 item 3).

**Product state checked.** HEAD `5b1f2cf`. `git hash-object` of `expectations.json` (`59e7efba`), `expectations.md` (`3ac5617d`) and `stakeholder-inputs.md` (`bcc2ec9f`) equals both the HEAD blob and the blob named in `product_files`, so the self-check applies to the blobs the reviewer read at iteration 3.

**Search first.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (queries: where an author self-check and readiness R3 are recorded; decision 115 and the self-check location). `grep -n` and Python scans on known paths followed, only to pin lines.

**Method.** A Python scan (scratchpad script, not a repository file) over `expectations.json`: `shall` count; the WR-07 group B word list of 02 section 4.2 applied to every `statement`; `rationale` and `source_ids` present; every `SI-NNN` resolves in `stakeholder-inputs.md` and every SI row is cited by at least one L0 entry; the Need, Goal and Objective parent structure; MOE `ngo_ids` and `ops_ids` resolve (NGO ids in the file, OPS ids in `docs/conops/conops.md`); Regulatory constraints cite a `47CFR` clause and SI-014; TBR entries; em dashes; statuses. Judgment items were answered by re-reading the entries the scan or the findings named.

### Brief's acceptance criteria

The authoring brief of commit 28e49e6 is not on record. The acceptance criteria below are the ones the expectations row of the 08 section 3.1 author role block names as governing: 02 section 3.2 (entry definitions and rules 1 to 5) and section 3.0 (stakeholders), `docs/requirements/l0-stakeholder/schema.json`, SE HB App. S, and the checklist product-type row for expectations.

| AC | Acceptance criterion | Source | Result | Evidence |
|---|---|---|---|---|
| AC-1 | The file validates against `l0-stakeholder/schema.json` | 02 section 3.2 Produces | Met | `tools/validate_docs.py`: `PASS docs/requirements/l0-stakeholder/expectations.json` |
| AC-2 | No expectation statement contains `shall` | 02 section 3.2 rule 1 | Met | Scan: 0 of 71 entries |
| AC-3 | Every NGO cites at least one `SI-NNN`; every MOE cites at least one NGO and at least one `OPS-NNN`, all resolving | 02 section 3.2 rule 2 | Met | Scan: 30 of 30 NGOs cite an SI; 13 of 13 MOEs have resolving `ngo_ids` and `ops_ids`; all 36 SI rows are cited |
| AC-4 | Exactly one Need; every Goal's parent is the Need; every Objective's parent is a Goal | 02 section 3.2 rule 3 | Met | Need NGO-001; Goals NGO-002 to 008 parent NGO-001; 22 Objectives each parented to a Goal; every Need and Goal has a child |
| AC-5 | Regulatory constraints cite the 47 CFR clause in `47CFR<part>.<section>` form together with SI-014 | 02 section 3.2 rule 4 | Met with exception | Every Regulatory constraint cites a `47CFR` clause. CON-006 (sources `47CFR97.7` ... , SI-019, SI-030) and CON-007 (`47CFR97.313(a)`, `(b)`, SI-003) do not also cite SI-014. New Minor discrepancy (author exception E-1 below) |
| AC-6 | Every entry is Draft; the file is baselined only by the SRR memo | 02 section 3.2 rule 5; 08 section 3.1 Status | Met | Every status `Draft`; `baseline` null |
| AC-7 | `stakeholders` names every group with a role and SI sources | 02 section 3.0 | Met | 10 stakeholders (customer, user, 2 guest operator, 2 public, regulator, 2 vendor, supplier), each with `source_ids` (finding-9 Verified) |
| AC-8 | No TBD; each TBR has owner, plan and close_by, one plan per TBR | charter section 7; readiness R4 | Met with lien | No TBD; TBR in NGO-012, NGO-015, NGO-026, MOE-010 carries all three fields (CON-020 names the policy). NGO-026's plan differs from the L1 `tbr.plan` of REQ-SYS-116 and 117 (finding-12, lien) |
| AC-9 | No em dash | 08 section 1 writing rules | Met | Scan: 0 |

### Self-check against the checklist sections for expectations (A3, A4, A5, A7, A8; B1 to B3; E4; F1 to F3)

| Item | Author answer | Evidence |
|---|---|---|
| CK-REQ-A3 | Yes | Objectives and MOE success criteria carry number, unit and bound (for example NGO-009 5.0 km at 5 W and 2.0 km at 2 W; MOE-001 at most one character error in 20); finding-7 Verified |
| CK-REQ-A4 | Yes | The group B scan hits only NGO-001 ("safe", "small group") and CON-023 ("small LCD"). NGO-001 is the Need, the single problem statement that 02 section 3.2 defines as not a solution and not measured; its terms are made measurable by the Objectives (NGO-021 hardware cutoff, NGO-017 emission limits) and by CON-001 (the group is the licensed friends). CON-023 is a quoted owner constraint on the control set, not a criterion; the display is sized by L1. Neither entry is an Objective or MOE criterion, which the item governs |
| CK-REQ-A5 | Yes | Part numbers and topologies appear only in rationales; the independence properties of NGO-016, NGO-021 and NGO-026 are owner-level (reviewer answer re-read) |
| CK-REQ-A7 | Yes, with exception E-1 | Every entry has a rationale citing its SI source; finding-1, 5 and 8 Verified. E-1 (CON-006, CON-007 without SI-014) |
| CK-REQ-A8 | Yes | "straight key" and "iambic paddle" as in SI-018 and L1; `expectations.md` render current (`tools/traceability.py --report-only`: no `RENDER_STALE`) |
| CK-REQ-B1 | Yes | AC-3, AC-4 |
| CK-REQ-B2 | Yes | No Objective duplicates another; each supports its Goal (reviewer answer re-read) |
| CK-REQ-B3 | Yes | AC-4 and AC-7; every Goal has an Objective |
| CK-REQ-E4 | Yes | Every MOE `success_criterion` contains a measurable pass condition (scan: 13 of 13 contain a number); subjective ratings have named raters (finding-7 Verified) |
| CK-REQ-F1 | No (lien) | finding-12: NGO-026 TBR plan versus REQ-SYS-116 and 117 `tbr.plan`. Fix before PDR as the lien table assigns |
| CK-REQ-F2 | Yes | finding-2 Verified ("pitch offset" split) |
| CK-REQ-F3 | Yes | No L0 entry holds product-level design detail beyond labelled proposals |

The other items are N/A for this product type (checklist product-type row): A1, A2, A6, B4 to B7, C, D, E1 to E3, E5, E6, F4 and G.

**Author exception E-1 (new, Minor, for the reviewer to disposition).** 02 section 3.2 rule 4 asks a constraint derived from 47 CFR to cite SI-014 with its clause; CON-006 and CON-007 cite the clauses and other SI rows but not SI-014. Proposed fix (before PDR, under the convergence rule): add SI-014 to both `source_ids`. No product change is made in this run.

### Author's statement

The self-check agrees with the reviewer's iteration 3 answers item for item and disputes no finding. It adds one Minor discrepancy (E-1). finding-12 is a lien the author fixes before the PDR readiness declaration. Commands: `tools/validate_docs.py` before this section: exit 1, 47 passed, 1 failed, 48 checked; the one failure is `docs/reviews/SRR/checklists/hazard-analysis.md` (record drift against the hazard files committed at `ade0e09`), outside this record and present before the edit. `tools/traceability.py --report-only` (output to the scratchpad): exit 0, 238 requirements, 170 test cases, 0 violations, 3 warnings, none naming an NGO, MOE, CON or stakeholder id.
