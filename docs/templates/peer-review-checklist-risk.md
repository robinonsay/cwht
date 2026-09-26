---
# Peer-review record front matter (charter section 5; docs/process/06-risk-and-decision-analysis.md
# section 16). To review the risk register or a trade study, copy this whole file to
# docs/reviews/<REVIEW>/checklists/<product-slug>.md: that copy is the single peer-review record
# (there is no peer-reviews/ folder). Fill every field below, answer every applicable checklist
# item and fill the findings table. Both front-matter parsers (PyYAML and the subset parser of
# tools/validate_docs.py) strip a comment on its own line and a comment written after a value
# (" # ..."); this template keeps each comment on its own line for readability, and comment lines
# may stay or be deleted when filing. tools/validate_docs.py checks the record against the field
# list of docs/process/01-lifecycle-and-reviews.md section 13 (its PEER_REVIEW_RECORD_SCHEMA) and
# fails while the id, checklist_file, product_commit or date placeholder is left in place.
# Search first: 'grep' in an evidence column means: run mcp__claude-context__search_code on
# /Users/robinonsay/rust/cwht first (charter section 11 rule 1), then grep -n only to pin the hit.
#
# id: next free INSP-NNN (never reused, charter section 6)
id: INSP-NNN
checklist: peer-review-checklist-risk
checklist_revision: A
# checklist_file: this record's own path, docs/reviews/<REVIEW>/checklists/risk-register.md for the
# register or docs/reviews/<REVIEW>/checklists/ts-nnn-<slug>.md (lower case) for a trade study
checklist_file: docs/reviews/<REVIEW>/checklists/<product-slug>.md
# product: docs/risk/register.json, or the trade study path docs/decisions/trade-studies/TS-NNN-<slug>.md
product: docs/risk/register.json
# product_commit: quoted so that an all-digit hash stays a string
product_commit: "<commit>"
# product_size: N active risks and N candidates, or N alternatives and N criteria for a trade study
product_size: 34 risks
# sprint: the gate preparation, for example SRR-prep
sprint: SRR-prep
author_agent: <invocation id>
# reviewer_agent: never the author
reviewer_agent: <invocation id>
# criticality: neither for the register as a whole; for a trade study the highest criticality of the
# 07 section 14.1 components it decides (safety-critical | mission-critical | neither)
criticality: neither
# assurance_required: true when the product is a trade study of 06 section 14.1 class 1 item (c) or
# (h) that decides a 07 section 14.1 component; false otherwise (the SWE-086 software assurance audit
# of the register is item CK-RSK-A11 of this checklist, done by the reviewer)
assurance_required: false
# assurance_reviewer_agent: invocation id, or none when assurance_required is false
assurance_reviewer_agent: none
# iteration: 1 to 3
iteration: 1
readiness_met: true
# reviewer_verdict: APPROVED | NEEDS CHANGES (the file reviewer)
reviewer_verdict: NEEDS CHANGES
# assurance_verdict: APPROVED | NEEDS CHANGES | not-required
assurance_verdict: not-required
# verdict: set by Claude as risk manager; APPROVED only when reviewer_verdict is APPROVED and
# assurance_verdict is APPROVED or not-required
verdict: NEEDS CHANGES
findings_major: 0
findings_minor: 0
findings_open: 0
findings_fixed: 0
findings_verified: 0
findings_deferred: 0
# deferred_rids: RID-<REVIEW>-NNN entered for each Deferred finding at record closure
deferred_rids: []
# items_no: checklist ids answered No
items_no: []
effort_turns: 0
effort_minutes: 0
# record_status: Open | Closed (set by Claude as risk manager)
record_status: Open
date: 2026-MM-DD
date_closed: null
---

# Peer review checklist: risk register and trade studies

**Product types.** Section A: the risk register `docs/risk/register.json` with its rendered `docs/risk/register.md`, reviewed before every life-cycle review and before a risk leaves *Proposed* (06 sections 2 and 9). Section B: every trade study `docs/decisions/trade-studies/TS-NNN-<slug>.md`, reviewed before the report goes to the owner (06 section 14.3 step 6). A reviewer answers the section that applies and lists the other under `ITEMS N/A`. **Governing:** `docs/process/06-risk-and-decision-analysis.md` sections 4 to 8, 11, 12, 14 and 16 (the items below are copied from section 16 and carry the same numbers); NPR 7123.1D SE-19 and SE-23; NPR 7150.2D SWE-086; SE HB §6.4 and §6.8 (Table 6.8-1); charter sections 2, 4 and 11 rules 4 and 6. **Used by:** an independent reviewer agent that did not author the register entries or the trade study (charter section 2).

Answer every item Yes, No or N/A with evidence (risk id and field, trade study section, or tool output). **Major**: a Red risk without the section 8 minimums, a hazard with unverified controls carried by no risk or with a one-way link, a score that disagrees with the scales, a trade study whose recommendation does not follow from its evaluation, a missing sensitivity statement. **Minor**: wording, a missing citation, an incomplete rationale that does not change a level.

## Record

This file, copied to `docs/reviews/<REVIEW>/checklists/<product-slug>.md`, is the single peer-review record for the product (charter section 5; 06 section 16). Slugs, lower case per the `<type>-<product-stem>` rule of `docs/process/01-lifecycle-and-reviews.md` section 13: `risk-register` for the register; `ts-nnn-<slug>` for a trade study, for example `ts-003-pa-topology` for `TS-003-pa-topology.md`. `<REVIEW>` is the next gate the product feeds. The front matter above is the first thing in the file, unfenced. A risk passes the Analyze step of 06 section 9 when this record lists it as passing; Claude then moves it from *Proposed* to *Open*.

### Findings (filled by the reviewer)

| Finding | Severity | Item | Location | Description | State | Deferred to |
|---|---|---|---|---|---|---|
| finding-1 | Major or Minor | CK-RSK-xx | risk id and field, or trade study section | what is wrong and what would fix it | Open, Fixed, Verified or Deferred | `RID-<REVIEW>-NNN` and the owner decision reference, for Deferred only |

### Risks passing the Analyze check (section A only)

| Risk | Passes (Yes or No) | Finding ids |
|---|---|---|
| RSK-NNN | | |

## Readiness criteria (all true before the review starts)

| # | Criterion | Evidence |
|---|---|---|
| R1 | `/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/validate_docs.py` exits 0 | tool output line |
| R2 | Section A: `/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/render_risk.py --check` exits 0 (the gate and hazard options are item CK-RSK-A1) | tool output |
| R3 | Section B: the trade study has sections 1 to 9 of `docs/templates/trade-study.md` filled and section 10 (Decision) empty | report |
| R4 | The author's return lists the risks added, re-scored or proposed for closure, or the trade study's decision need and gate | author return |

## A. Risk register (06 section 16, "Risk register", items 1 to 11)

| Id | Check | Evidence to inspect |
|---|---|---|
| CK-RSK-A1 | `/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/render_risk.py --check --gate <REVIEW> --hazards /Users/robinonsay/rust/cwht/docs/safety/hazards.json` exits 0 (validation, stale-render comparison, gate and hazard link rules in one command) | tool output, pasted |
| CK-RSK-A2 | Every *Proposed* risk has been checked against sections 4 to 8 and moved to *Open*, or a defect is recorded as a finding | risk list above |
| CK-RSK-A3 | Every statement has one departure or one family admitted by the section 4 family rule, a dated or cited condition, and no solution language | `statement` of each risk |
| CK-RSK-A4 | Every likelihood rationale names its anchor; every consequence rationale names the driving dimension | `likelihood_rationale`, `consequence_rationale` |
| CK-RSK-A5 | Every Red risk has at least two active steps with artifacts and due gates, one trigger with actor and timing, a fallback, a strategy of Mitigate, Research or Elevate, and, from its first gate review, a `plan_approval` naming the decision memo, ADR or CR that records the owner's approval | `mitigation` of each Red risk |
| CK-RSK-A6 | Every Red risk has a REQ or HZ link (from PDR on) | `related` |
| CK-RSK-A7 | Every hazard with unverified controls has a linked risk and the link is two-way | CK-RSK-A1 output; `docs/safety/hazards.json` `related_risk_ids` |
| CK-RSK-A8 | Aggregate risks (tagged `aggregate`, with `related.risk_ids` children) have likelihood equal to the maximum of their active children; the tool enforces this, the reviewer confirms the child list is complete | aggregate risks |
| CK-RSK-A9 | Every risk with a Low confidence has a Research strategy, a re-assessment trigger or a hazard-analysis step | Low-confidence risks |
| CK-RSK-A10 | Changes since the previous review are listed in the package and match the history entries; every candidate named in an artifact committed since the previous review has a disposition | package risk section; `history`; `candidates` |
| CK-RSK-A11 | Software assurance audit (SWEHB SWE-086 tab 7, tasks 1 and 2): every software risk (category or tag software) has all six steps of section 9 evidenced (record, analysis, plan, tracking, control decision, communication in the package); the software risks of 07 sections 16.2 and 21 are all in the register; the risk management process for the software activities is audited against 06; the result, including the software-risk list and the measures table, is recorded in this record | `register.md` SWE-086 row; 07 sections 16.2 and 21 |

## B. Trade study (06 section 16, "Trade study", items 1 to 10)

| Id | Check | Evidence to inspect |
|---|---|---|
| CK-RSK-B1 | The decision class rule of 06 section 14.1 requires a trade study, and the decision maker and gate are stated | report section 1 |
| CK-RSK-B2 | Every enhancing criterion has an operational definition and a 1 to 5 scale with anchors; mandatory criteria are pass or fail; the "Criteria considered" line covers safety, first power-on, cost, schedule, performance margin and system security | report section 3 |
| CK-RSK-B3 | Weights are integers summing to 100 with a stated rationale | weights table |
| CK-RSK-B4 | Alternatives cover the decision space; the do-nothing alternative is present or its absence is explained; pruned alternatives are listed | report section 3.2 |
| CK-RSK-B5 | Every score cell links evidence and carries a confidence | evaluation matrix |
| CK-RSK-B6 | The weighted totals recompute correctly | recomputation by the reviewer |
| CK-RSK-B7 | The uncertainty and sensitivity statement follows 06 section 14.4, including method limitations, and its verdict is consistent with the recommendation | report section 6 |
| CK-RSK-B8 | Every surviving alternative has its risks listed in the four-part format on the 06 section 6 and 7 scales | report section 8 |
| CK-RSK-B9 | The recommendation is the highest total, or the deviation is explained and the criteria revised | report section 7 |
| CK-RSK-B10 | The Dissent section is present (even if "none") and the Decision section is empty until the owner decides | report sections 9 and 10 |

## Completion criteria (SWE-088 b, c)

`verdict: APPROVED` when: the readiness criteria that apply were true; every applicable item is answered and the others are listed as N/A; zero open Major findings; every Minor finding fixed, or deferred with an owner decision reference and a gate; the front matter is complete with the measurements (SWE-089) filled; and `/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/validate_docs.py` passes on the record itself. On record closure each Deferred finding becomes `RID-<REVIEW>-NNN` in the `rfa-rid-log.json` of its named gate, citing this `INSP-NNN` and the finding id, and is listed in `deferred_rids`.

## Verdict format (returned by the reviewer)

```
VERDICT: APPROVED | NEEDS CHANGES
FINDINGS:
- [Major] CK-RSK-A5 RSK-034 mitigation: plan_approval missing after the SRR memo was signed.
- [Minor] CK-RSK-A4 RSK-012 consequence_rationale: name the driving dimension.
ITEMS N/A: CK-RSK-B1 to CK-RSK-B10 (product is the register)
MEASUREMENTS: size=34 risks; turns=4; minutes=25; major=1; minor=1
```
