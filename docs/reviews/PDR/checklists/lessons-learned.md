---
# Peer-review record front matter (charter section 5; docs/process/01-lifecycle-and-reviews.md section 13
# is the single field list; docs/process/08-agent-briefing.md section 3.2). Checklist:
# docs/templates/peer-review-checklist-requirements.md revision C, items CK-REQ-G1, G2, G3, G8 and A8 (the
# plan and process-document route; no lessons-learned checklist exists, 08 section 3.5). Record path named by
# docs/plan/pdr-work-plan.md WP-PDR-05 "Records". Product frozen at e119181 (rule C2); every product_files
# blob equals git rev-parse HEAD:<path> at 091bceb.
id: INSP-035
checklist: peer-review-checklist-requirements
checklist_revision: C
checklist_file: docs/reviews/PDR/checklists/lessons-learned.md
product: docs/lessons-learned.md
# product_commit: iteration 1 e119181 (blob ec30a264); iteration 2 (delta, 2026-09-29) 391f0e5, entry 18 (blob d250e8fb)
product_commit: "391f0e5deb9087e538da6aca5c61dc1e11d7d26b"
# iteration 2 (2026-09-29, delta): docs/lessons-learned.md re-pinned from ec30a264 to d250e8fb (entry 18, verified in
# section "Delta iteration 2"); the entry "docs/cm/cr/CR-007-cm-plan-pdr-rows.md@92b200ad5bc9e8cc41f602ddc504e2ae04b2154c" is
# dropped: the CR file is a record revised at each lifecycle step (revisions 2 to 4, 96cb7b1 to 7668322) and this record
# reviewed none of its content (precedent INSP-060, fd12ced). Every remaining blob equals git rev-parse HEAD:<path> at 9dc9d63.
product_files: ["docs/lessons-learned.md@d250e8fbe734120ad3cc208687505dfc973ef55e", "docs/reviews/PDR/package.md@967117cff3521ad00c59ba33a81de3e6381850e9", "docs/reviews/PDR/rfa-rid-log.json@7b2860b209db8582356bb38e0e168cc28d2107ed", "docs/reviews/PDR/checklists/.gitkeep@e69de29bb2d1d6434b8b29ae775ad8c2e48c5391", "docs/reviews/PDR/figures/.gitkeep@e69de29bb2d1d6434b8b29ae775ad8c2e48c5391", "docs/reviews/PDR/slides/.gitkeep@e69de29bb2d1d6434b8b29ae775ad8c2e48c5391", "docs/process/configuration-status.md@07909eb643e44f5e57dff38c3a30de1a4099df4f"]
product_size: 1 file, 3 sections, 18 entries (49 lines; iteration 1 read 17 entries, 48 lines)
sprint: PDR-prep
author_agent: "author:WP-PDR-05 (Claude, lead SE)"
reviewer_agent: "reviewer:WP-PDR-05 (independent reviewer)"
# criticality and assurance: lessons learned is Table 4-1 row 40 (Log); not a product type of 07 section 2.1.1
criticality: neither
assurance_required: false
assurance_reviewer_agent: none
# iteration 2: delta on entry 18 (391f0e5) and CR-007 re-pin, section "Delta iteration 2" at the end
iteration: 2
readiness_met: true
reviewer_verdict: APPROVED
assurance_verdict: not-required
verdict: APPROVED
findings_major: 0
# iteration 2 adds finding-2 (Minor, a lien under rule C1)
findings_minor: 2
findings_open: 2
findings_fixed: 0
findings_verified: 0
findings_deferred: 0
assurance_findings_major: 0
assurance_findings_minor: 0
assurance_tasks_applied: []
deferred_rids: []
items_no: [CK-REQ-G2]
# effort: iteration 1 8 turns, 15 minutes; iteration 2 adds 16 turns, 30 minutes
effort_turns: 24
effort_minutes: 45
record_status: Open
date: 2026-09-27
date_closed: null
---

# Peer review record INSP-035: lessons-learned file (WP-PDR-05 output 4)

**Product:** `docs/lessons-learned.md`, blob `ec30a264`, created at `e119181`. Identity: `git rev-parse HEAD:docs/lessons-learned.md` and `git hash-object` give `ec30a264` at `091bceb`. **Checklist:** `docs/templates/peer-review-checklist-requirements.md` revision C, CK-REQ-G1, G2, G3, G8 and A8 (the other section G items are N/A for a log). **Acceptance criteria (rule C7):** RFA-SRR-003 requested action (`docs/reviews/SRR/rfa-rid-log.json`: "Create docs/lessons-learned.md with the ten entries of package section 19 before the PDR readiness declaration"); plan WP-PDR-05 output 4 ("the ten SRR package §19 entries plus the lessons of section 1.4", C-206, S10); each of the ten `LL-proposed-1` to `LL-proposed-10` rows of `docs/reviews/SRR/package.md` §19 and each of the seven lessons L1 to L7 of plan §1.4; charter §5 path; 08 §1 repo map ("tagged by area"); 05 Table 4-1 row 40 class.

**Independence (rule C4):** this invocation authored no part of WP-PDR-05 and edited no product file. **Search first:** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search. `grep -n` was used afterwards only to pin lines.

## Record

### Findings

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | reviewer | Minor | CK-REQ-G2 | Entry 8, "Applied in" cell (line 26) | The cell names "08 section 5 change carried by WP-PDR-12" as the vehicle for adding the author self-check to the 08 §5 return format. WP-PDR-12's outputs list 08 "header, repo map, §3.1, §3.2, §3.5" (`docs/plan/pdr-work-plan.md` line 308) and not §5, so no planned work package carries the action the entry says is carried. Fix: either the lead SE adds 08 §5 to the WP-PDR-12 outputs (cross item), or the entry names the actual vehicle (for example the author brief template of 08 §3.1). | Open | Pending | |

## Readiness criteria

| # | Criterion | Result | Evidence |
|---|---|---|---|
| R1 | Product validates | Yes | Markdown with no schema; this record passes the validator |
| R2 | Traceability clean | N/A | No requirement or test case |
| R3 | Author self-check | Yes | Author summary of WP-PDR-05 names output 4 and its sources |
| R4 | No TBD | Yes | `grep -c TBD`: 0; em dashes: 0 |
| R5 | CR impact assessment | N/A | Not a CR |

## G. Plans, process documents and decision records (SWE-087 b), applied to a log

| Id | Answer | Evidence |
|---|---|---|
| CK-REQ-G1 | Yes | Path is charter §5 "Lessons learned"; class Log agrees with 05 Table 4-1 row 40; area tags satisfy the 08 §1 repo map line; rule 5 ties the file to 01 §3.2 S10 ("Lessons learned reviewed and new entries recorded", 01 line 91) and the package template §19 |
| CK-REQ-G2 | No, on finding-1 | Every entry names its source artifact and an "Applied in" vehicle; entry 8's vehicle is not in the plan (finding-1) |
| CK-REQ-G3 | Yes | Owner, author and the package author's use at each gate (rule 5) are stated |
| CK-REQ-G4 | N/A | No tailored requirement relied on |
| CK-REQ-G5 | N/A | No cybersecurity content |
| CK-REQ-G6 | N/A | No measurement defined |
| CK-REQ-G7 | N/A | No tool claim beyond `tools/validate_docs.py` usage |
| CK-REQ-G8 | Yes | RFA-SRR-003 quotation is verbatim from the log `requested_action` and memo line 110; the package §19 citation resolves (`a6d0959` holds the ten rows, identical in the §19 text at `HEAD`) |
| CK-REQ-A8 | Yes | Consistent terms; entry numbering rule stated (no charter §6 id scheme exists for lessons, which the file states) |

## Every case named (rule C7)

| Source case | Entry | Check | Result |
|---|---|---|---|
| `LL-proposed-1` to `LL-proposed-10` (SRR package §19) | 1 to 10 | Date, lesson and action compared row by row with `docs/reviews/SRR/package.md` §19: same dates, same lesson text (entry 5 adds "of the SRR package", entry 9 adds "that"; meaning unchanged), same actions | Complete |
| Plan §1.4 L1 to L7 | 11 to 17 | Each lesson, source and application compared with plan §1.4 lines 56 to 62: L1 to entry 11, L2 to 12, L3 to 13, L4 to 14 (the entry names CR-002, CR-004 and CR-005, as `docs/cm/deviations.md` entries 1 to 3 do; plan L4 names only two), L5 to 15, L6 to 16 (109 recounted: this reviewer's count at `9fd0962` is 109 `tbr` objects in `docs/requirements/sys/requirements.json`), L7 to 17 | Complete |
| RFA-SRR-003 (L-3), C-206, S10 | whole file | File exists with the ten entries; the RFA state move is WP-PDR-15's after this record (the CSA item 13 says so) | Met |
| Area index | section 3 | Every entry appears exactly once under its area tag | Agrees |

## Commands

| Command | Exit | Result |
|---|---|---|
| `git rev-parse HEAD:docs/lessons-learned.md`; `git hash-object` | 0 | `ec30a264` both |
| `.venv/bin/python tools/validate_docs.py` | 1 | This record PASS; the two failures are pre-existing records of other work packages (record drift) |

## Verdict format

```
VERDICT: APPROVED
FINDINGS:
- [Minor] CK-REQ-G2 entry 8 names WP-PDR-12 as the vehicle for an 08 section 5 change that WP-PDR-12 does not list.
ITEMS N/A: CK-REQ-G4, CK-REQ-G5, CK-REQ-G6, CK-REQ-G7
MEASUREMENTS: size=17 entries; items=9; items_no=1; turns=8; minutes=15; major=0; minor=1
```

## Delta iteration 2 (2026-09-29, entry 18 and re-pin; reviewer, new invocation)

**Why and scope (rules C1 and C2).** On `main` at `9dc9d63`, `tools/validate_docs.py` failed this record on record drift: the product moved from `ec30a264` to `d250e8fb` (commit `391f0e5`, "entry 18, parts lifecycle as a mandatory screen for part-selecting studies", `Refs: TS-012, WP-PDR-54, WP-PDR-05`), and the context file CR-007 moved from `92b200ad` to `abec03c5`. This delta verifies every changed hunk of the product since `ec30a264` and re-pins the CR. Product: `docs/lessons-learned.md` blob `d250e8fb`; `git rev-parse HEAD:docs/lessons-learned.md` and `git hash-object` both give `d250e8fb` at `9dc9d63`; `git log --format=%h -- docs/lessons-learned.md` lists only `391f0e5` and `e119181`, so `git diff ec30a264 d250e8fb` is the whole change: 2 insertions, 1 deletion (the entry 18 row, and the index row `risk` from `1` to `1, 18`).

**Independence (rule C4) and search first.** A new invocation of this record's reviewer role. It authored no part of WP-PDR-05, entry 18, TS-012, the lifecycle research, the status note or iteration 1 of this record, and edited no product file. `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any `grep`. The rustos tree was not read and no web page was read.

**CR-007 re-pin.** This record reviewed no CR-007 content (the CR appears only in entry 14's "Applied in" cell, which did not change). The CR file is revised at each lifecycle step, so it is dropped from `product_files` (precedent: INSP-060 in `fd12ced`). The other six blobs equal `git rev-parse HEAD:<path>` at `9dc9d63`.

### Entry 18 against its sources (every claim, rule C7)

| Claim in entry 18 | Source read | Result |
|---|---|---|
| Date 2026-09-29, area `risk`, gate PDR, state Planned | Rule 4 area list (`risk` is a tag; 06 is the risk and decision analysis plan and holds the trade-study rules, 06 §14); commit date of `391f0e5`; the gate is PDR because the decision was taken in the PDR phase | Agrees |
| TS-012 did not weight lifecycle status; sourcing folded into M2, C5 and RSK-038 | TS-012 at `6497900` §10, "Lead SE reading" item 1: "it folded sourcing into M2, C5 and the section 7.1 risks, with RSK-038 (stock and end of life) as the carrier" | Agrees (condensed; the 7.1 risks are carried by RSK-038) |
| The recommended A4 rests on the End-of-Life NXP AFT05MS004NT1 | TS-012 §10 item 2; INSP-110 (`ts-012-design-to-cost.md`) "Findings (iteration 1)" finding-1 (Major): the NXP page marks the AFT05MS004N "End of Life" | Agrees |
| Owner quote "I'm leaning towards A5 if it doesn't use outdated components", and "A5" | `docs/plan/status/status-2026-09-29.md` section 4 (added at `f35eb78`) and section 5 (added at `13176ee`): both are exact substrings of the verbatim statements | Agrees |
| 39 of 39 A5 parts Active | `docs/research/a5-parts-lifecycle-2026-09-29.md` at `f193784`: "Result: 39 of 39 entries Active"; 39 table rows with status Active | Agrees |
| The owner chose A5, not the recommendation | TS-012 §10 "Decision" and status note section 5 | Agrees |
| Source cell ids | `6497900`, `f193784`, `f35eb78`, `13176ee` each exist and touch the named file; TS-012 §10 carries "Lead SE reading" items 1 to 3 and "Lessons learned" | Agrees |
| Action: lifecycle screen (Active at the maker, source and read date) as a mandatory criterion, or ask the owner at opening | TS-012 §10 "Lessons learned" candidate entry; the entry adds "read date" and "recorded before the recommendation goes to the owner", which narrow it and match the research note's columns | Agrees |
| Applied in: next part-selecting study (for example the WP-PDR-27 TS-004 and TS-011 re-scores), and 06 §14 at its next revision | `docs/plan/pdr-work-plan.md` revision 7: WP-PDR-54 carries the entry itself ("Also: the `docs/lessons-learned.md` entry of TS-012 §10"); WP-PDR-27 outputs select products (TS-011 "with one recommended product" coating) but name no lifecycle criterion; no WP output revises 06 §14 (WP-PDR-18 fixes 06 §15 and §17 text only; WP-PDR-51 records the 06 re-approval) | finding-2 |
| Index row `risk`: 1, 18 | Section 3 of `d250e8fb` | Agrees; every entry 1 to 18 appears once |
| Style | `grep -c TBD`: 0; em dashes: 0; rule 3 (append only): entries 1 to 17 unchanged by the diff | Agrees |

### Findings of the delta

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| finding-1 | reviewer | Minor | CK-REQ-G2 | Entry 8, "Applied in" cell | Unchanged by `391f0e5`: WP-PDR-12 outputs still do not list 08 §5. Lien (rule C1) | Open | Pending | CDR readiness declaration |
| <a id="finding-2"></a>finding-2 | reviewer | Minor | CK-REQ-G2 | Entry 18, "Applied in" cell (line 36) | The entry names two vehicles, and neither carries the action in the plan. WP-PDR-27 (the example study) selects at least one product, the TS-011 coating ("with one recommended product"), but its outputs name no lifecycle criterion, and the entry makes it conditional ("if they select parts"). No work package of plan revision 7 revises 06 §14, so "the 06 section 14 trade-study rules at their next revision" has no planned owner or date. This is the class of entry 8's finding-1. Fix: the lead SE adds the lifecycle screen to the WP-PDR-27 brief or outputs (cross item to the plan writer), and names the vehicle and due event for the 06 §14 change (for example a CR against 06 raised with the 06 re-approval of WP-PDR-51), or the entry names the vehicles that do carry it | Open | Pending | CDR readiness declaration |

Open Major: 0. New findings: 1 Minor (finding-2), a lien under rule C1, since this record's first APPROVED verdict was at iteration 1.

**Observation (no finding).** Rule 5 says "The PDR package section 19 lists entries 1 to 17"; `docs/reviews/PDR/package.md` section 19 at `967117cf` is still the template placeholder, and after entry 18 the package author's list under the same rule is entries 1 to 18. The rule itself tells the package author to list every entry added since the last review, so nothing is lost; the sentence can be updated when the package is written (WP-PDR-48).

### Delta verdict

```
DELTA ITERATION 2 (2026-09-29): VERDICT: APPROVED
FINDINGS:
- [Minor] finding-1 (iteration 1) Open, lien.
- [Minor] CK-REQ-G2 finding-2: entry 18 names WP-PDR-27 and a 06 section 14 revision as vehicles; neither carries the lifecycle screen in plan revision 7.
PRODUCTS: docs/lessons-learned.md@d250e8fb (391f0e5); CR-007 dropped (not reviewed content); six other blobs unchanged
MEASUREMENTS: size=1 entry + 1 index row; claims checked=11; items_no=1; turns=16; minutes=30; cumulative turns=24, minutes=45; major=0; minor=1 new
```
