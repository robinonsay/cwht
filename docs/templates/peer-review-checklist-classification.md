---
# Peer-review record front matter (charter section 5; docs/process/03-software-classification-and-rmm.md
# section 3.3). To record the independent classification assessment, copy this whole file to
# docs/reviews/<REVIEW>/checklists/classification-03-software-classification-and-rmm.md: that copy
# is the single peer-review record of the assessment (there is no peer-reviews/ folder). Fill every
# field below, answer CL-1 to CL-9 and fill the findings table. Both front-matter parsers (PyYAML and
# the subset parser of tools/validate_docs.py) strip a comment on its own line and a comment written
# after a value (" # ..."); this template keeps each comment on its own line for readability, and
# comment lines may stay or be deleted when filing. tools/validate_docs.py checks the record against
# the field list of docs/process/01-lifecycle-and-reviews.md section 13 (its
# PEER_REVIEW_RECORD_SCHEMA) and fails while the id, checklist_file, product_commit or date
# placeholder is left in place.
# Search first: 'grep' in an evidence column means: run mcp__claude-context__search_code on
# /Users/robinonsay/rust/cwht first (charter section 11 rule 1), then grep -n only to pin the hit.
#
# id: next free INSP-NNN (never reused, charter section 6); the SRR decision memo section 7.1
# cites it on the classification concurrence line
id: INSP-NNN
checklist: peer-review-checklist-classification
checklist_revision: A
# checklist_file: this record's own path
checklist_file: docs/reviews/<REVIEW>/checklists/classification-03-software-classification-and-rmm.md
product: docs/process/03-software-classification-and-rmm.md
# product_commit: quoted so that an all-digit hash stays a string
product_commit: "<commit>"
# product_size: sections 3 and 4 of the record, N items classified and N components determined
product_size: 7 items classified; 9 components determined
sprint: SRR-prep
# author_agent: the author of 03 (Claude as lead SE, or the author invocation)
author_agent: <invocation id>
# reviewer_agent: the independent classification assessor (software assurance function, charter
# section 2); never the author
reviewer_agent: <invocation id>
criticality: safety-critical
# assurance_required: true; 03 is a whole-product item of 07 section 2.1.1, so tools/validate_docs.py
# requires a second, software assurance invocation distinct from author and reviewer
assurance_required: true
assurance_reviewer_agent: <invocation id>
# iteration: 1 to 3
iteration: 1
readiness_met: true
# reviewer_verdict: APPROVED (concur) | NEEDS CHANGES (dissent or open findings)
reviewer_verdict: NEEDS CHANGES
# assurance_verdict: APPROVED | NEEDS CHANGES
assurance_verdict: NEEDS CHANGES
# verdict: set by the lead SE; APPROVED only when reviewer_verdict and assurance_verdict are APPROVED
verdict: NEEDS CHANGES
findings_major: 0
findings_minor: 0
findings_open: 0
findings_fixed: 0
findings_verified: 0
findings_deferred: 0
assurance_findings_major: 0
assurance_findings_minor: 0
# assurance_tasks_applied: SWEHB section 7.1 tasks applied, for example [swe-020 7.1 task 1, swe-205 7.1 task 1]
assurance_tasks_applied: []
# deferred_rids: RID-<REVIEW>-NNN entered for each Deferred finding at record closure
deferred_rids: []
# items_no: checklist ids answered Dissent or Differences listed
items_no: []
effort_turns: 0
effort_minutes: 0
# record_status: Open | Closed (set by the lead SE)
record_status: Open
date: 2026-MM-DD
date_closed: null
---

# Peer review checklist: independent software classification assessment

**Product.** Sections 3 (classification) and 4 (safety-critical determination) of `docs/process/03-software-classification-and-rmm.md`, with `docs/safety/hazards.json` as the source of record and `docs/process/07-software-engineering-plan.md` section 14.1 as the authoritative component list (charter section 10). **Governing:** NPR 7150.2D SWE-020 and the guidance paragraph after its Note (software assurance may perform an independent classification or concur with engineering's; the two technical authorities agree), SWE-176 (retain each independent classification assessment), SWE-205 (safety-critical determination), App. D (classes) and App. A (mission-critical software definition); NASA-STD-8739.8B para 3.2 criteria a to e as reproduced in `docs/references/md/swehb/7-02-classification-and-safety-criticality.md` section 1.2; charter sections 1, 2 and 10. **Used by:** an independent reviewer agent acting as the software assurance classification assessor (charter section 2) that did not author 03, plus the software assurance second review that `tools/validate_docs.py` requires for 03.

Answer CL-1 to CL-9 with **Concur** or **Dissent** (or the per-item or difference answer the Answer column names) and evidence. A dissent is a finding: **Major** when it changes a class, the safety-critical set or the mission-critical set; **Minor** otherwise. The owner, holding both the ETA and SMA TA roles, resolves any dissent in the SRR decision memo section 11 (03 section 3.3); no separate dissenting-opinion process exists.

## Record

This file, copied to `docs/reviews/<REVIEW>/checklists/classification-03-software-classification-and-rmm.md`, is the single record of the independent classification assessment (charter section 5; 03 sections 3.3 and 9). The slug follows the `<type>-<product-stem>` rule of `docs/process/01-lifecycle-and-reviews.md` section 13 with type `classification`, so it does not collide with the section G plan review of the same document (`plan-03-software-classification-and-rmm.md`). `<REVIEW>` is SRR for the first assessment and the gate of each re-run (PDR, CDR; 03 section 4.1 step 5). The SRR decision memo section 7.1 cites this record's `INSP-NNN`.

### Findings (filled by the reviewer and the assurance reviewer)

| Finding | Origin | Severity | Item | Location | Description | State | Deferred to |
|---|---|---|---|---|---|---|---|
| finding-1 | reviewer or assurance | Major or Minor | CL-n | 03 section and row, or hazard id | the dissent or difference and what would resolve it | Open, Fixed, Verified or Deferred | `RID-<REVIEW>-NNN` and the owner decision reference, for Deferred only |

## Readiness criteria (all true before the review starts)

| # | Criterion | Evidence |
|---|---|---|
| R1 | `/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/validate_docs.py` exits 0 (includes `docs/safety/hazards.json` and `docs/process/rmm.json`) | tool output line |
| R2 | `/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/render_rmm.py --check` exits 0 | tool output |
| R3 | The version of `docs/safety/hazards.json` that 03 sections 4.2 and 4.3 transcribe is stated in 03, and every difference from the current file is an open item of 03 section 6.5 | 03 header and section 6.5 |

## Checks (copied from 03 section 3.3)

| # | Check | Evidence the reviewer uses | Answer |
|---|---|---|---|
| CL-1 | Each App. D factor score of section 3.1 is consistent with D.1 and the App. D class definitions | `docs/references/md/npr-7150-2d/10-appendixd.md` | Concur or dissent, with rationale |
| CL-2 | The class of each item in the section 3.1 per-item table follows from the App. D clause it cites (Class D a.1(b) and b.1; Class C b.1 by analogy; Class E a.3, a.4, b, c.5, c.6, c.8) and from D.2 | Same | Per item |
| CL-3 | Each hazard's `firmware_role.criteria` in `hazards.json` is supported by its narrative and by the NASA-STD-8739.8B para 3.2 criteria as reproduced in SWEHB 7.02 section 1.2 | `docs/safety/hazards.json`, `docs/safety/hazard-analysis.md` section 5, `docs/references/md/swehb/7-02-classification-and-safety-criticality.md` | Per hazard |
| CL-4 | Section 4.2 equals `hazards.json` (ids, criteria, components verbatim) | `docs/safety/hazards.json` | Differences listed |
| CL-5 | Each section 4.3 criteria cell equals the union of `firmware_role.criteria` over the hazards naming the component; each type (ii) finding (section 4.1 step 3) states the hazard, the criterion and why | Sections 4.2 and 4.3 | Per component |
| CL-6 | The section 4.3.1 determination for the verification software and the rigor it assigns | Section 4.3.1, SWEHB 7.02 section 1.2 | Concur or dissent |
| CL-7 | The mission-critical list of section 4.3 against the App. A definition of Mission Critical Software | `docs/references/md/npr-7150-2d/07-appendixa.md` | Concur or dissent |
| CL-8 | Every difference between section 4.3 and 07 section 14.1, and between section 4.3 and `hazards.json`, is an open item of section 6.5 | 07 section 14.1, section 6.5 | Differences not listed |
| CL-9 | Overall classification and safety-critical determination | All of the above | Concur, or dissent with rationale |

## Completion criteria (SWE-088 b, c; SWE-176)

`verdict: APPROVED` (concurrence) when: R1 to R3 were true; CL-1 to CL-9 are answered with evidence; zero open Major findings; every Minor finding fixed, or deferred with an owner decision reference and a gate; the front matter is complete with the measurements (SWE-089) filled; the assurance reviewer has returned `APPROVED`; and `/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/validate_docs.py` passes on the record itself. The record is retained for the life of the project in git (SWE-176; 03 section 6.4 item 6).

## Verdict format (returned by the reviewer)

```
VERDICT: APPROVED | NEEDS CHANGES
FINDINGS:
- [Major] CL-4 HZ-008: 03 section 4.2 gives firmware role "none" while hazards.json 0.2.0-pha gives a, c, e.
ITEMS N/A: none
MEASUREMENTS: size=7 items, 9 components; turns=5; minutes=30; major=1; minor=0
```
