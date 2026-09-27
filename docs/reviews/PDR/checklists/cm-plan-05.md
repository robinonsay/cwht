---
# Peer-review record front matter (charter section 5; docs/process/01-lifecycle-and-reviews.md section 13
# is the single field list; docs/process/08-agent-briefing.md section 3.2). Checklist:
# docs/templates/peer-review-checklist-requirements.md revision C, section G and CK-REQ-A8 plus readiness R5
# (product type "Plans and process documents"; a CR against 05 that touches no requirement). Record path named
# by docs/plan/pdr-work-plan.md WP-PDR-05 "Records" (delta of INSP-006 and INSP-030 scope). Iteration 1 reviews
# the proposed 05 text of CR-007 (Submitted, frozen at 9032a02, rule C2) against 05 blob f8de2081
# (baseline/srr); the delta on the implemented 05 blob is CR-007 section 5 step 7. This record also carries the
# verification note of WP-PDR-05 output 1 (PDR workspace), for which the plan names no record.
# Every product_files blob equals git rev-parse HEAD:<path> at a900969 (iteration 1). Iteration 2 (delta, rule C1)
# re-freezes the CR at blob 22c4455f (commit 96cb7b1, revision 2, which contains the ca228b9 section 6.1
# append); the other seven blobs are unchanged and equal HEAD 3aed3c4.
id: INSP-039
checklist: peer-review-checklist-requirements
checklist_revision: C
checklist_file: docs/reviews/PDR/checklists/cm-plan-05.md
product: docs/cm/cr/CR-007-cm-plan-pdr-rows.md
product_commit: "96cb7b1ea9754e725151377a21732c3f2a488e20"
product_files: ["docs/cm/cr/CR-007-cm-plan-pdr-rows.md@22c4455fc26011e5cd0d5b96fa0c05896ff22f1d", "docs/reviews/PDR/package.md@967117cff3521ad00c59ba33a81de3e6381850e9", "docs/reviews/PDR/rfa-rid-log.json@7b2860b209db8582356bb38e0e168cc28d2107ed", "docs/reviews/PDR/checklists/.gitkeep@e69de29bb2d1d6434b8b29ae775ad8c2e48c5391", "docs/reviews/PDR/figures/.gitkeep@e69de29bb2d1d6434b8b29ae775ad8c2e48c5391", "docs/reviews/PDR/slides/.gitkeep@e69de29bb2d1d6434b8b29ae775ad8c2e48c5391", "docs/process/configuration-status.md@07909eb643e44f5e57dff38c3a30de1a4099df4f", "docs/lessons-learned.md@ec30a264fdef25ff291ddad5b1ebebbed8f9dee9"]
product_size: 1 CR, change items C1 to C17 against 05 and 07 (C17 at revision 2) (16 sections, Table 4-1 55 rows, Table 4-2), rmm.json 3 rows, 2 templates
sprint: PDR-prep
author_agent: "author:WP-PDR-05 (Claude, CM function)"
reviewer_agent: "reviewer:WP-PDR-05 (independent reviewer, CM lens)"
criticality: neither
# assurance_required: true. 05 is the software CM plan, 07 section 2.1.1 row "Software plans" (Yes in every
# column), and CR-007 C9 itself routes a CR that changes a 07 section 2.1.1 Yes product to the software
# assurance reviewer. The assurance reviewer is a separate invocation (rule C4; 07 section 2.1.1); it is not
# yet assigned (SA pair needed; paired record to be filed as cm-plan-05-software-assurance.md).
assurance_required: true
assurance_reviewer_agent: "not yet assigned (SA pair needed; paired record docs/reviews/PDR/checklists/cm-plan-05-software-assurance.md)"
iteration: 2
readiness_met: true
reviewer_verdict: APPROVED
# assurance_verdict stays NEEDS CHANGES until the paired assurance record is APPROVED (07 section 10.2), so the
# record verdict is NEEDS CHANGES on the pairing only; the file review found no Major finding.
# Iteration 2: INSP-047 is APPROVED at iteration 1 on CR blob 92b200ad only; revision 2 (C17) changes the
# software assurance plan 07, so the pairing holds until the INSP-047 delta on blob 22c4455f is APPROVED.
assurance_verdict: NEEDS CHANGES
verdict: NEEDS CHANGES
findings_major: 0
findings_minor: 4
findings_open: 4
findings_fixed: 0
findings_verified: 0
findings_deferred: 0
assurance_findings_major: 0
assurance_findings_minor: 0
assurance_tasks_applied: []
deferred_rids: []
items_no: [CK-REQ-G1, CK-REQ-G2, CK-REQ-G8]
# effort: iteration 1 (30 turns, 60 min) plus iteration 2 delta (22 turns, 35 min)
effort_turns: 52
effort_minutes: 95
record_status: Open
date: 2026-09-27
date_closed: null
---

# Peer review record INSP-039: CR-007 changes to the CM plan 05 (WP-PDR-05 output 3), with the PDR workspace note

**Product:** `docs/cm/cr/CR-007-cm-plan-pdr-rows.md`, blob `92b200ad`, last committed at `9032a02` (status Submitted, Class II), read against 05 blob `f8de2081` (equal at `HEAD` and at `baseline/srr`), `docs/process/rmm.json` blob `e326ddd1` and `docs/templates/`. **Checklist:** `docs/templates/peer-review-checklist-requirements.md` revision C, section G and CK-REQ-A8, readiness R5. **Acceptance criteria (rule C7):** (1) every lien the CR claims to close, each item of its fix as the source record states it: INSP-006 finding-10 (a) to (c), finding-11 and observation O-6, finding-12; INSP-030 finding-1 (every location it names: 05 §3 rows at lines 58 and 60, §5.2 Assessed and Verified, §7.4, §8.1 step 8), finding-2 (a) and (b), finding-3 (flavour identity, VDD, §8.3 step 2, PCA-05, anomaly rule), finding-4, finding-5; baseline check 3 OBS-1; SRR lien L-7 §9.2 rows; (2) 05 §4.4: a Table 4-2 part for every CR-class row of the Allocated line (8, 10, 11 in its three files, 15, 16, 17, 34, 48, 50, 54, the functional baseline as amended, the informational rows 21, 23, 24 and the outside-set rows 25, 26, 28); (3) every "before" string of section 1 equal to the 05 or `rmm.json` text at the stated line; (4) 05 §5.3 impact fields all answered.

**Independence (rule C4):** this invocation authored no part of WP-PDR-05 or CR-007 and edited no product file. It is the file review only; the software assurance lens is a separate invocation (fix request "SA pair needed"). **Scope note:** CR-007 section 6 (independent impact review before disposition, plan wave 1a) is its own slot in the CR file; this record may serve as its input, and the findings below are written for the CR author to resolve before OD-36. **Search first:** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search. `grep -n` was used afterwards only to pin lines.

## Record

### Findings

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | reviewer | Minor | CK-REQ-G1 | CR-007 C7 (line 90) against 05 §7.4 (line 366) | C7 rewrites the 05 §3 "Software assurance" row so that the software assurance reviewer "performs the interim configuration checks of §7.4 at each review", but no change item touches §7.4, which keeps "At SRR, PDR, CDR, TRR and every `TRR-Dn` the independent reviewer performs the record-side checks only". After the merge 05 would give the same checks to two roles in two places, which is the ambiguity INSP-030 finding-1 names ("it is not stated whether these are one role or two", location "section 7.4 (line 365)"). C-084 is then not fully closed. Fix: add a change item for §7.4 naming the software assurance reviewer (§3) as the performer, or both roles with the split stated. | Open | Pending | |
| <a id="finding-2"></a>finding-2 | reviewer | Minor | CK-REQ-G8 | C10 (line 96); C6 Part B row 8 (line 74); C13 closing note (line 110) | Three citations or stated facts are wrong. (a) C10 places the 05 §5.3 Safety field at line 265; at blob `f8de2081` line 265 is "Performance margins" and Safety is line 266 (the CR states its line numbers are those of `f8de2081`). (b) Part B row 8 cites "02 §8 rule 5" for L2 TBRs closing no later than CDR; 02 §8 is the `tools/traceability.py` rule list (T-14 enforces the limit) and the policy is 02 §9 item 2 ("L1 TBRs close by PDR and L2 TBRs by CDR"). (c) The note on TV-012 says ACC-COMPLEXITY-001 dates from SRR close-out item 4 and INSP-015 re-issue 3, but TV-012 §9 (lines 196 and 197) records a second extension under close-out item A to blob `ddf10798` (commit `106bc3a`), which the first CSA issue item 9 reports as effective on INSP-015 re-issue 4. Fix: line 266; cite 02 §9 item 2 (and T-14); state the item A extension and the current accredited blob. | Open | Pending | |
| <a id="finding-3"></a>finding-3 | reviewer | Minor | CK-REQ-G2 | C4 (line 56); C10 (line 96) | C4 identifies the files of each 07 §14.1 component as the `code` paths of the `docs/design/allocation.json` elements "whose `module` is that component". The 07 §14.1 components are finer than modules: `SW-SAFE` implements four components (thermal unit, safe-state manager, configuration guard `cfg_guard`, frequency verification unit), the thermal component spans `SW-SAFE` and `SW-TXSEQ`, only the frequency-word units of `SW-SYNTH` are safety-critical while the remainder of frequency control is mission-critical (charter §10), and the menu override module is fixed only by the PDR architecture ADR (07 lines 589 to 600). The allocation schema's element `module` is a module id (`^(RX\|TX\|PWR\|CTL\|ME\|SW)(-[A-Z][A-Z0-9]*)?$`), so a module-keyed map cannot give each path one criticality for the CSA item 2 sub-rows C10 adds. Fix: key the map by allocation element (one element per 07 §14.1 unit, criticality stated), or state the rule for a module with mixed criticality (for example: the highest criticality of any unit in it applies to all its paths). | Open | Pending | |
| <a id="finding-4"></a>finding-4 | reviewer | Minor | R5, CK-REQ-G2 | Front matter `related` (line 14); §4 rows Schedule and Documentation (lines 153, 156); C6 Part B lead paragraph (line 69) and rows 8, 11 (budgets), 34, 48 | The impact assessment names CR-003 and CR-006 as the interacting CRs. Three CRs raised in the same wave interact and are not named: CR-012 (Submitted; the three checklists Part B names exist only on `cr/CR-012-pdr-checklist-templates`, and Part B rows 11 budgets, 34 and 48 need `peer-review-checklist-analysis.md`); CR-011 (Submitted; Part B row 8 and the verification plan use "`tools/traceability.py` with the PDR rules"); CR-010 (Submitted; changes `rmm.json`, the file C16 changes, through the same WP-PDR-17 writer slot; its branch does not touch the SWE-063, SWE-085 or SWE-136 rows, so the hunks are disjoint). Part B therefore depends on two other dispositions before freeze F1. Fix: add CR-010, CR-011 and CR-012 to `related` and to the Schedule row with the order of merge, and state the Part B fallback if CR-011 or CR-012 is not merged by F1 (for example, the admission row names the SRR checklist route of 08 §3.5 until then). | Open | Pending | |

The four findings are Minor: each is a completeness or accuracy defect of the proposal that the author can fix before the owner's disposition (rule C6), and none would make an admitted CI wrong. Rule C1 applies after the first APPROVED record verdict.

## Readiness criteria

| # | Criterion | Result | Evidence |
|---|---|---|---|
| R1 | Product validates | Yes | CR front matter matches `docs/templates/change-request.md`; `tools/validate_docs.py` checks no CR schema; this record passes the validator |
| R2 | Traceability clean | N/A | No requirement or test case is changed (CR §4 "Requirements and traceability") |
| R3 | Author self-check | Yes | CR §5 verification paragraph (line 175) lists the checks; author summary of WP-PDR-05 |
| R4 | No TBD | Yes | The two `TBD` strings (lines 74, 75) are admission criteria "zero TBD", not placeholders; em dashes: 0 |
| R5 | CR impact assessment | Yes, with finding-4 | CR §4 answers every 05 §5.3 field (Performance margins, Safety, Risk, Software classification and tailoring, Interfaces, Operations and ConOps, Cybersecurity, Verification, Cost, Schedule, Requirements and traceability, Regulatory, Documentation, Released units) with a classification rationale |

## G. Plans, process documents and decision records (SWE-087 b)

| Id | Answer | Evidence |
|---|---|---|
| CK-REQ-G1 | No, on finding-1 | Class II is correct: adding Table 4-1 rows after SRR is "a Class II CR against this plan" (05 §4.2 row rules, line 83), and 05 §4.4 names a Class II CR for the admission rows. C6 (b) narrows the 05 §4.4 sentence (all three parts before PDR) to Part B now and the CDR and SAR parts later; the CR says so and asks the owner (Q2). No conflict with the charter (§7 L2 TBRs by CDR; §8 tags) or with `rmm.json` after C16. Internal conflict: finding-1 |
| CK-REQ-G2 | No, on finding-3 and finding-4 | Every change item names its 05 location, before and after text; the implementation plan names each step's artifact, owner and SHA column; Part B names each record path (all found in the plan section 3 WPs). Gaps: finding-3, finding-4 |
| CK-REQ-G3 | Yes | C7 and C9 state the software assurance reviewer's independence (a separate invocation, other than the file reviewer) and its approval points; the owner remains CCB (§7) |
| CK-REQ-G4 | Yes | C8 bounds the tailoring CR row to disposition, `tailoring_rationale`, `residual_risk` (Table 4-1 row 3); C16 changes implementation texts only and keeps `disposition`, `tailoring_rationale`, `residual_risk` and `status`; the three "before" texts are verbatim in `rmm.json` blob `e326ddd1` (checked by exact substring) |
| CK-REQ-G5 | Yes | §4 Cybersecurity row: no change to the USB load or key-input paths; C11 makes a fault-injection image visible in `picotool info -a` |
| CK-REQ-G6 | Yes | CSA item 2 sub-rows (C10) and the Table 6-1 metrics are unchanged in definition; volatility contribution 0 stated |
| CK-REQ-G7 | Yes | C13 known answers checked: `tools/tests/test_unsafe_audit.py` 14 tests, `test_complexity_gate.py` 27, `test_measurements.py` 16 (count of `def test_`); fixture directories `unsafe_audit/`, `complexity_gate/`, `measurements/` exist; TV-011 line 33 (nine sites), TV-013 line 42 (1608 B, 8200 B). `tools/render_risk.py` accepts `--check --gate --hazards` (lines 901 to 903), as Part B row 15 uses. C11 states `tools/release.sh` does not exist yet, which is true |
| CK-REQ-G8 | No, on finding-2 | SE HB §6.5.1.2.3 (minor-change basis), SWE-081, SWE-082, SWE-085, SWE-063 task citations resolve to the INSP-030 sources; 01 §12.2 "a hazard without an allocated control requirement (PDR onward)" is verbatim (01 line 875). Wrong citations: finding-2 |
| CK-REQ-A8 | Yes | Terms match 05 (Parts A and B, rows, classes, CR-from); no em dashes |

## Every case named (rule C7)

**(1) Liens the CR closes.**

| Lien (source) | Fix asked in the source record | Change item | Result |
|---|---|---|---|
| INSP-006 finding-10 (a) edit before approval, reversal | State the order and the reversal rule | C3: the exception is closed, approved by SRR decision 105 option (A), so no reversal arises | Closed by C3 |
| INSP-006 finding-10 (b) section 8 change log | Name it among the allowed lines | C3 names "a new section 8 "Change log"" | Closed |
| INSP-006 finding-10 (c) ADR template pointer | Pointer in `docs/templates/adr.md` | C15 (b) | Closed |
| INSP-006 finding-11 status line | Revision 4 status line | C1 (text verified against 05 line 3) | Closed |
| INSP-006 finding-11 row 9 list | Refresh the dated schema list | C2: eleven files, equal to the CSA item 2 row 9 list and to `git ls-files 'docs/*schema.json'` | Closed |
| INSP-006 O-6 (author S-1) | Replace "not yet in H1" annotations | C6 (c): INSP-019, 020, 021, 006 with 030, 007, 010 with 018, 022, 005, 023, 024, 025, each checked against the SRR record front matter ids | Closed |
| INSP-006 finding-12 | Bound §5.1 row 2 | C8 (before text equal to 05 line 229) | Closed |
| INSP-030 finding-1: §3 rows (lines 58, 60) | Give SA a part | C7 | Closed |
| INSP-030 finding-1: §5.2 Assessed, Verified | Route CRs to SA | C9 (before texts equal to 05 lines 251, 255) | Closed |
| INSP-030 finding-1: §8.1 step 8 | SA confirms the VDD row | C12 (before text equal to 05 line 385) | Closed |
| INSP-030 finding-1: §7.4 | One role or two | none | **Open: finding-1** |
| INSP-030 finding-2 (a) SWE-136, (b) SWE-063 and SWE-085 | Restate the three RMM texts | C14 (AL-16) and C16 | Closed |
| INSP-030 finding-3 | Flavour identity; VDD; §8.3 step 2; PCA-05; anomaly rule | C11 (a) to (f) (before texts equal to 05 lines 152, 346, 391, 424, 432); VDD §2 already carries each flavour with its SHA-256 (05 line 391) | Closed |
| INSP-030 finding-4 | Code map, CSA criticality column, Safety field cites it | C4, C10 | Closed, with finding-3 on the map key |
| INSP-030 finding-5 | Table 4-1 row for `docs/plan/status/` | C5 row 56 (Record) | Closed |
| Baseline check 3 OBS-1 | Row 2 README wording | C6 (d) (before text equal to 05 line 177) | Closed |
| SRR lien L-7 (RFA-SRR-007) part | §9.2 rows for three tools and a §13 note | C13 | Closed, with finding-2 (c) on the note |
| P-29 | Allocated-baseline rows | C6 (e) Part B | Closed |

**(2) Part B covers the Allocated line of 05 §4.4 (line 164).** Functional baseline as amended (rows 1, 2, 3, 5, 6, 7, 9, 17, 27, 51, 52, 53): Part B row 1. Row 8: yes. Row 10: yes. Row 11 architecture, allocation, budgets: three rows, yes. Row 15: yes. Row 16: yes. Row 17 other cases: yes. Row 34 definitions: yes. Row 48: yes. Row 50: yes. Row 54: yes. Informational 21, 23, 24: yes. Outside the set 25, 26, 28: yes. No row missing.

**(3) Before strings.** C1 (line 3), C2 (95), C3 (99), C4 (111), C6 (170, 177), C7 (58, 60), C8 (229), C9 (251, 255), C11 (152, 346, 385, 391, 424, 432), C16 (three `rmm.json` rows) were compared with `git show f8de2081` and `rmm.json` blob `e326ddd1`: every quoted "before" text is present. The only wrong line number is C10 (finding-2 (a)).

**(4) Rows 56 and 57.** A reviewer matcher that parses the Table 4-1 pathspecs of `f8de2081` and applies the 05 §4.2 precedence rule to the 1217 files of `9fd0962` gives two unmatched files and no ambiguous match; with rows 56 (`docs/plan/status/`) and 57 (`docs/plan/*-work-plan.md`) added, the unmatched list is empty and no path matches two rows with equal precedence.

## PDR workspace verification note (WP-PDR-05 output 1; the plan names no record for it)

| Check | Evidence | Result |
|---|---|---|
| `docs/reviews/PDR/package.md` copied from `docs/templates/review-package.md` | `diff` of the template against blob `967117cf`: only the review token (`PDR`, `pdr.adoc`, `baseline/pdr`), the prior review row (SRR, Approved with liens, 2026-09-26, memo commit `0bcea39`), the purpose (verbatim 01 §5.1 first sentence, line 279), the section numbers 5.3, 5.4 and 5.6, and a dated skeleton paragraph differ; no section is deleted; 86 `<...>` tokens remain for WP-PDR-49 | Agrees with output 1 |
| `rfa-rid-log.json` empty, schema `docs/templates/rfa-rid-log.schema.json` | `tools/validate_docs.py`: "PASS docs/reviews/PDR/rfa-rid-log.json (schema: docs/templates/rfa-rid-log.schema.json)"; `items: []` | Agrees |
| `checklists/`, `figures/`, `slides/` | `.gitkeep` files, empty blob `e69de29b`, matching Table 4-1 row 42 (`*.gitkeep`) | Agrees |
| Commit | `e119181`, trailer `Refs: PDR, CR-007, RFA-SRR-003` parsed by git | Agrees |

## Observations (no finding)

- **O-1.** Part A rows 3, 5, 6, 7, 51 and 52 keep "In H1" in the Record column after C6 (b) deletes the sentence that defined "not yet in H1"; the meaning (SRR package §2 item H1) is still readable. The author may name the records there as C6 (c) does for the other rows.
- **O-2.** CR-003 revision 3 also changes 05 (§4 Documentation row); the CR states the rebase rule (C1). The two hunk sets are disjoint on `f8de2081` as far as this reviewer checked (CR-003 lines 13, 154, §8.2, row 23; CR-007 elsewhere, C11 (b) edits line 152, adjacent to the line 154 row).

## Commands

| Command | Exit | Result |
|---|---|---|
| `git rev-parse HEAD:<path>` for the eight `product_files`; `git rev-parse HEAD:docs/process/05-configuration-and-data-management.md baseline/srr:<same>` | 0 | Frozen blobs equal; 05 `f8de2081` at both |
| Exact-substring check of the C16 "before" texts in `docs/process/rmm.json` | 0 | 3 of 3 present |
| `grep -c "    def test_"` on the three test files | 0 | 14, 27, 16 |
| Reviewer matcher over `git ls-tree -r 9fd0962` with and without rows 56, 57 | 0 | 2 unmatched, then 0; 0 ambiguous |
| `.venv/bin/python tools/validate_docs.py` | 1 | This record PASS; the two failures are pre-existing records of other work packages (record drift) |

## Verdict format

```
VERDICT: APPROVED (file review); record verdict NEEDS CHANGES until the software assurance pair is APPROVED
FINDINGS:
- [Minor] CK-REQ-G1 C7 gives the section 7.4 checks to software assurance but section 7.4 still names the independent reviewer (INSP-030 finding-1 part not closed).
- [Minor] CK-REQ-G8 C10 line 265 should be 266; Part B row 8 cites 02 section 8 rule 5 for 02 section 9 item 2; C13 omits the TV-012 item A extension.
- [Minor] CK-REQ-G2 C4 keys the safety-critical code map by module although 07 section 14.1 components are units within modules.
- [Minor] R5 CK-REQ-G2 impact assessment omits the interacting CR-010, CR-011 and CR-012 and the Part B fallback.
ITEMS N/A: none of section G; sections A to F (no requirement changed)
MEASUREMENTS: size=16 change items; items=9; items_no=3; turns=30; minutes=60; major=0; minor=4
```

## Iteration 2: delta on the drifted CR blob (2026-09-27, `main` HEAD `3aed3c4`)

**Scope (rule C1).** Iteration 2 is a delta. The assignment named the drift as blob `92b200ad` to `a504624e` (`ca228b9`, the section 6.1 append). At `HEAD` the CR has moved further: `96cb7b1` (revision 2, the author's response to IR-F1) makes it blob `22c4455f`. This iteration reviews every hunk of `git diff 92b200ad 22c4455f` (1 file, 74 insertions, 18 deletions), which contains the `ca228b9` append. The other seven `product_files` blobs equal `git rev-parse HEAD:<path>` (checked by script). The hunks are: front matter `affected_paths` (07 added), `affected_ids` (INSP-010, INSP-018), `related` (CR-010, CR-013); status line and a revision 2 paragraph; C7, C9, C12 and C15 (a) now cite 07 §2.1.1 as the single dispatch rule; new C17 (07 §2.1, §2.1.1, §2.2, §15, §23); section 4 Safety, Software classification, Verification, Schedule and Documentation rows and the classification rationale; section 5 steps 1, 5a and 7 and the verification paragraph; section 6.1 (CM-lens impact review round 1, reviewer text) and 6.2 (author response); a section 11 history row; Q4. C1 to C6, C8, C10, C11, C13, C14 and C16 are unchanged. The CR is on `main` (no `cr/` branch content), so no branch-only hold applies. Checklist: `peer-review-checklist-requirements.md` revision C, section G and CK-REQ-A8, as at iteration 1.

**Independence (rule C4).** This invocation authored no part of CR-007, WP-PDR-05, the section 6.1 review, INSP-047 or any implementing change, and edited no product file. File review only; the software assurance lens is INSP-047. **Search first.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran (query: rule C1 delta iteration practice) before any `grep`; `grep -n`, `sed -n` and `git` were used afterwards only to pin lines in known paths.

### Delta checks

| Check | Evidence | Result |
|---|---|---|
| C17 "before" texts and line numbers | 07 blob `bfe05f43` equals `HEAD`, `8c57710` and `baseline/srr` (`git rev-parse`). Line 108 (§2.1 row), 112 (lead sentence, quoted "the single rule for dispatching the software assurance reviewer"), 116 (requirement files and "CRs touching them"), 123 (NCR row, followed by the MC/DC row at 124), 126 (Basis), 139 (§2.2 row, "Sections 2.1.1, 14 and 15 of this file;"), 665 (§15 row, "verification of sprint acceptance criteria (section 3.4 Phase 4);") read with `sed -n` | Every before string and insertion point present at the stated line |
| C17 (b) Neither column | 07 §2.1.1 rows with Yes under Neither: Software plans (line 117), NCR touching firmware (123), code containing `unsafe` (121) | Agrees with the parenthesis of the new "Change requests" row |
| C17 (c) SWEHB basis | `swe-080` §7.1 tasks 1 and 2 (corpus lines 623 to 636), `swe-082` §7.1 tasks 1 and 2 (692 to 698), `swe-063` §7.1 task 2 (719 to 725), `swe-085` §7.1 task 2 | Each task exists with the content the paraphrase names; see O-3 |
| Cross references added by revision 2 | C12 names 07 §2.1.1 row "Firmware releases and interim configuration checks" and C15 (a) row "Change requests", both equal to the C17 (b) row names; INSP-010 is `docs/reviews/SRR/checklists/software-plan-07.md` and INSP-018 its assurance pair; CR-013 section 5 step 4 (line 149) schedules the INSP-010 and INSP-018 deltas the Verification row cites; plan §5.3 row for 07 (line 1017) names WP-PDR-17, WP-PDR-13, WP-PDR-47 | Agree |
| Schedule row: CR-010 and CR-013 07 hunks | `git diff -U0 main...cr/CR-010-apply-srr-decisions-9-and-40` and `...cr/CR-013-process-04-07-semp-srr-liens` on 07: hunks at 31, 150, 215, 317 to 356, 401, 446, 465, 492, 543 to 646, 728, 787, 808, 849 to 867, 885 and 972 | Matches the row; none at 108, 112 to 126, 139 or 665 |
| Validator claim of C17 closing paragraph | `tools/validate_docs.py` `assurance_reason` (line 693) derives from the record's product path (`ASSURANCE_WHOLE_PRODUCTS`, line 253; 07 §14.1 modules) and reads no CR file | True |
| R4 on the new text | `TBD`: the two admission-criterion strings of iteration 1 only; em dashes: 0 | Unchanged, Yes |

### Effect of revision 2 on the four findings

- **finding-1** is not fixed, and C17 widens it. After the merge the §7.4 interim configuration checks would be given to the software assurance reviewer in 05 §3 (C7), 07 §2.1 (C17 (a)), 07 §2.1.1 new row "Firmware releases and interim configuration checks" (C17 (b)) and 07 §15 (C17 (e)), while 05 §7.4 (line 366, unchanged by any item) still reads "the independent reviewer performs the record-side checks only". The fix is unchanged: a change item for 05 §7.4 naming the performer, now also consistent with the C17 (b) row. Severity stays Minor: no admitted CI would be wrong, and both texts name an independent invocation.
- **finding-2** is not fixed: C10 still places the Safety field at line 265 (it is 266, as section 6.1 of the CR also found); Part B row 8 and the C13 note are unchanged.
- **finding-3** is not fixed: C4 and C10 unchanged.
- **finding-4** is partly addressed: `related` and the Schedule row now name CR-010 and CR-013 for their 07 hunks. Still missing: CR-011 and CR-012 (the Part B dependencies), CR-010's `rmm.json` change through the WP-PDR-17 slot beside C16, and the Part B fallback.

**Scan of the delta for new defects.** No new finding. C9 now says 07 §2.1.1 governs where the 05 summary differs, which gives the precedence 05 lacked. The C17 (b) "Change requests" row keeps the first row's scope for requirement files ("this row's case"), so the two rows do not conflict.

### Observations (no finding)

- **O-3.** C17 (c) paraphrases `swe-080` §7.1 task 2 as "confirm that changes are approved before implementation and that their implementation is complete", which is items b and c. Items a (the project tracks the changes) and d (the project tests the changes) are left out. The citation resolves; the author may quote all four items or name "items b and c".
- **O-4.** INSP-047 finding-2 (Part B rows 10 and 15 route ICDs and the hazard analysis to assurance, which 07 §2.1.1 does not list) is the same kind of two-rule defect as IR-F1. C17 does not close it, and CR section 6.2 says so.

### Findings (iteration 2; current state of every finding of this record)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| finding-1 | reviewer | Minor | CK-REQ-G1 | C7; C17 (a), (b), (e); 05 §7.4 (line 366) | §7.4 checks given to the software assurance reviewer in four places and to the independent reviewer in 05 §7.4; see above | Open | Pending | |
| finding-2 | reviewer | Minor | CK-REQ-G8 | C10; C6 Part B row 8; C13 note | Unchanged at `22c4455f` | Open | Pending | |
| finding-3 | reviewer | Minor | CK-REQ-G2 | C4; C10 | Unchanged at `22c4455f` | Open | Pending | |
| finding-4 | reviewer | Minor | R5, CK-REQ-G2 | Front matter `related`; §4 Schedule and Documentation rows; C6 Part B | CR-010 (07 part) and CR-013 now named; CR-011, CR-012, CR-010's `rmm.json` change and the Part B fallback still not named | Open | Pending | |

The four findings stay Open, as at iteration 1 and as CR section 6.2 carries them to the owner at OD-36. Under rule C1 they become liens due at the CDR readiness declaration when the first APPROVED record verdict is set, unless the author fixes them before implementation.

### Record verdict, iteration 2

`reviewer_verdict: APPROVED`: no Major finding, and the revision 2 hunks introduce none. `assurance_verdict` and `verdict` stay NEEDS CHANGES. The paired record INSP-047 (`cm-plan-05-software-assurance.md`) is APPROVED at iteration 1 on blob `92b200ad` only. Revision 2 changes the software assurance plan 07 (C17), so the pairing holds until INSP-047 files a delta on `22c4455f` APPROVED. The software lead then sets the record `verdict`.

### Commands (iteration 2)

| Command | Exit | Result |
|---|---|---|
| `git rev-parse` of CR-007 at `9032a02`, `ca228b9`, `96cb7b1`; script comparing the eight `product_files` with `HEAD` | 0 | `92b200ad`, `a504624e`, `22c4455f`; seven of eight equal before the update, eight of eight after |
| `git diff 92b200ad 22c4455f` read in full | 0 | 74 insertions, 18 deletions, hunks listed under Scope |
| `git rev-parse HEAD: 8c57710: baseline/srr:` on 07; `sed -n` of 07 lines 5, 108, 112 to 126, 139, 665 | 0 | `bfe05f43` at all three; before texts present |
| `git diff -U0 main...cr/CR-010-*` and `main...cr/CR-013-*` on 07 | 0 | Hunk lines as the Schedule row states |
| `.venv/bin/python tools/validate_docs.py` | 1 | This record PASS; 101 passed, 8 failed: INSP-047, INSP-034 and INSP-035 on the same CR-007 drift (their own deltas), five SRR records pre-existing |

```
VERDICT (iteration 2, 2026-09-27): reviewer APPROVED; record verdict NEEDS CHANGES (held: INSP-047 delta on 22c4455f pending)
PRODUCT: docs/cm/cr/CR-007-cm-plan-pdr-rows.md 22c4455f at 96cb7b1 (revision 2; includes ca228b9 section 6.1)
FINDINGS: finding-1 to finding-4 Minor Open (finding-1 widened by C17; finding-4 partly addressed); no Major; new findings 0
MEASUREMENTS: diff hunks read 9 (every changed line); C17 before strings checked 7; blobs re-checked 8; new findings 0; iteration 2 22 turns, 35 minutes; cumulative 52 turns, 95 minutes
```
