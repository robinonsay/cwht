---
id: CR-014
title: Close the SRR tool liens in validate_docs, review_trend, render_review_figures, complexity_gate, measurements and sw_gate
status: Submitted
class: II
originator: Claude
date_opened: 2026-09-27
phase: B
configuration_at_origination: baseline/srr (tag on 779f93f); branch cr/CR-014-tool-liens-srr from main 7bb994f, product commits 16cdd3e to 7b4e3b4, main 72d0a2f merged in at 367b3dd (branch head)
baseline_affected: baseline/srr
affected_cis: [25, 27, 28, 30, 40]
affected_paths: [tools/validate_docs.py, tools/tests/test_validate_docs.py, tools/review_trend.py, tools/tests/test_review_trend.py, tools/render_review_figures.py, tools/tests/test_render_review_figures.py, tools/tests/fixtures/review_figures/docs/design/concept.md, tools/tests/fixtures/review_figures/docs/reviews/SRR/package.md, tools/tests/fixtures/review_figures/docs/risk/register.json, tools/tests/fixtures/review_figures/docs/risk/register.md, tools/complexity_gate.py, tools/tests/test_complexity_gate.py, tools/measurements.py, tools/tests/test_measurements.py, tools/sw_gate.sh, tools/toolchain.lock.md, tools/README.md, firmware/cwht-app/src/main.rs, docs/cm/tool-validation/README.md, docs/cm/tool-validation/TV-001-python-jsonschema.md, docs/cm/tool-validation/TV-003-validate-docs.md, docs/cm/tool-validation/TV-007-review-trend.md, docs/cm/tool-validation/TV-010-render-review-figures.md, docs/cm/tool-validation/TV-012-complexity-gate.md, docs/cm/tool-validation/TV-013-measurements.md, docs/cm/tool-validation/evidence/wp-pdr-09-2026-09-27.py, docs/cm/tool-validation/evidence/wp-pdr-09-2026-09-27.log.txt, docs/cm/tool-validation/evidence/sw-gate-g0-export-2026-09-27.sh, docs/cm/tool-validation/evidence/sw-gate-g0-export-2026-09-27.log.txt, docs/cm/tool-validation/evidence/complexity-gate-2026-09-27-r4.log.txt, docs/cm/tool-validation/evidence/requirements-freeze-2026-09-27.log.txt, docs/cm/tool-validation/evidence/wp-pdr-09-renders/]
affected_ids: [TV-001, TV-003, TV-007, TV-010, TV-012, TV-013, ACC-VALDOCS-001, ACC-TREND-001, ACC-FIGS-001, ACC-COMPLEXITY-001, ACC-MEASURE-001, INSP-015, INSP-016, INSP-029, INSP-041, RID-SRR-004, RID-SRR-014, RFA-SRR-007]
related: [CR-001, CR-004, CR-005, CR-010, CR-011, RID-SRR-004, RID-SRR-014, RFA-SRR-007, INSP-015, INSP-016, INSP-029, INSP-041]
target_release: none
branch: cr/CR-014-tool-liens-srr
disposition: null
disposition_date: null
relook_trigger: null
relook_by: null
merge_sha: null
date_closed: null
---

# CR-014: Close the SRR tool liens in validate_docs, review_trend, render_review_figures, complexity_gate, measurements and sw_gate

Template: `docs/templates/change-request.md`. Process: `docs/process/05-configuration-and-data-management.md` §5. This file is committed on `main`; the branch `cr/CR-014-tool-liens-srr` carries the product changes. Work package: WP-PDR-09 of `docs/plan/pdr-work-plan.md` (revision 2), wave 1a. The plan's register of phase CRs (section 6.2) does not list this CR. It is raised because four of the changed tools are class-CR CIs since their accreditation (05 Table 4-1 row 28, "Accreditation puts the tool under CR control"): `tools/validate_docs.py` (ACC-VALDOCS-001), `tools/review_trend.py` (ACC-TREND-001), `tools/render_review_figures.py` (ACC-FIGS-001) and `tools/complexity_gate.py` (ACC-COMPLEXITY-001). The Log-class items of the same work package (`tools/measurements.py`, TV-013 not yet accredited; `tools/sw_gate.sh`, no TV record; the lock rows; the comment in `firmware/cwht-app/src/main.rs`, firmware source before its first release tag) ride on the same branch, because two APPROVED SRR records (INSP-015, INSP-016) and the WP-PDR-08 record INSP-041 name their current blobs: carried on `main` alone, they would fail the record drift rule there before the delta iterations exist (the CR-010 precedent, its section 5 steps 4 to 6).

## 1. Description of the change

| Carried item (plan section 10.1) and source | Product and change | Commit |
|---|---|---|
| C-172: INSP-015 F-08 | `tools/validate_docs.py` header: the latest iteration section starts at the FIRST heading that names the highest iteration, as the code, TV-003 purpose 7 and the function docstring already said | `16cdd3e` |
| C-173: INSP-015 F-09 | `tools/validate_docs.py` record state rule (purpose 7): a record whose highest named iteration is 1 is read whole; a section headed "Findings" is read wherever it stands, in its place in document order; `F-07` and `finding-7` are one finding (`finding_key`), so a master-table `F-21` row is superseded by a later `finding-21` row. Without `finding_key` the widened read would have failed INSP-010 on its master-table row `F-21`, which its later rows close | `16cdd3e` |
| C-186: SRR lien L-7 (RFA-SRR-007; INSP-006 X-2, INSP-013) and SRR decision 9 | `tools/validate_docs.py`: `ASSURANCE_WHOLE_PRODUCTS` adds `docs/process/05-configuration-and-data-management.md` and `docs/decisions/trade-studies/TS-002-firmware-runtime-make-buy.md` (07 section 2.1.1 software plans row); `SW-SYNTH` moves from `MISSION_CRITICAL_MODULES` to `SAFETY_CRITICAL_MODULES` (its transmit frequency-word path, decision 9; 07 section 22 tool-constants row; CR-010 section 4 names this follow-on). The menu override module waits for the PDR architecture ADR (WP-PDR-32, wave 2) | `16cdd3e` |
| C-170: RID-SRR-004 | `tools/review_trend.py` figure: whole-day ticks, each date labelled once, at most 8 per panel; the series starts at zero the day before the first item, so a log raised on one date draws its rise; markers where a series moves; the closed label turns upward near the axis; the T label moves to the top band | `067966c` |
| C-072: RID-SRR-014; C-203: INSP-029 finding-5; C-204: INSP-029 finding-6 | `tools/render_review_figures.py`: the SRR package generators `docs/reviews/SRR/figures/risk-matrix.py` and `concept-block-diagram.py` are folded in. "risk" scores with `tools/render_risk.py` and cross-checks the `docs/risk/register.md` matrix table; "concept" parses the Mermaid block of concept section 5 against a `ConceptLayout` with the script's layout checks. `CONCEPT_LAYOUT_SRR` reproduces the SRR package render pixel for pixel; `CONCEPT_LAYOUT_SLIDE` and the new risk layout hold every text at 14.5 pt or more (20 px on the slide). A board footer must quote the package section's wording; the SRR success footer now says "an owner ruling" as package section 20 does. A run renders into a temporary folder and writes nothing when a check fails. The SRR figure set is unchanged and the SRR package renders are not re-written (they are package records) | `012d53c` |
| C-175: INSP-015 F-11 | `tools/complexity_gate.py` `let_else_sites`: the binding `=` of a `let` directly after a `>` that closes a type annotation is found (the first depth-0 `=` not part of `==` or `=>`) | `fcb9ba7` |
| C-185: SRR lien L-7 | `tools/measurements.py`: every check-result line begins `measurements: PASS` or `measurements: FAIL`, so no tool line reads as a `sw_gate.sh` step line (`PASS <step>`, `FAIL <step>`); exit statuses unchanged | `e024b24` |
| C-179: INSP-016 F-16 (L-016-5) | `tools/sw_gate.sh` G0: clone mode as before; export mode for a `git archive` export of rustos (the CR-004 clean-export rule): the export's tree hash, computed in a temporary repository, equals the lock's "tree of the pin" `39d8d8a9` (added to the lock section 3 rustos row) | `dacc6e9` |
| C-178: INSP-016 F-13 (L-016-2); CR-001 section 5 step 2 | `firmware/cwht-app/src/main.rs`: the comment above the driver-construction failure arm cites CR-001 as Approved and the amended CS-11; comment only, same line count (`main.rs:30 main CC 4` unchanged), `rustfmt --check` exit 0 | `f924595` |
| C-171 and C-174: INSP-015 F-07, F-10; C-176: F-12; C-177: F-13 (owner reading); C-182 | TV-003 run 7, TV-007 run 4, TV-010 run 5, TV-012 run 4, TV-013 run 4 on an export of `f924595`, each with its purpose amendment, section 8 pending review and a proposed ACC extension; F-07 corrections by dated entries in TV-010 and the TV index (README owner action 3 closed); F-10: TV-007 runs with the current `validate_docs.py` and its proposed extension names both blobs, lock qualifiers; F-12: the lock rows, section 1.4 finding 9, section 5 rows and the `sw_gate.sh` separator, TV-001 limitation 4 closed; F-13 re-asked of the owner in TV-012 section 9; C-182: `tools/requirements.txt` equals `pip freeze` (35 of 35) | `7b4e3b4` |
| Merge of `main` | `main` at `72d0a2f` merged into the branch; one conflict (`tools/toolchain.lock.md`, the WP-PDR-07 rows of `2bfe001`) resolved by re-applying the WP-PDR-09 entries on main's lock; no CR-014 product blob changed | `367b3dd` |

Blobs at the branch head: `tools/validate_docs.py` `e5b692e1`, `tools/review_trend.py` `9e451fa2`, `tools/render_review_figures.py` `7607e7c2`, `tools/complexity_gate.py` `e9cfd465`, `tools/measurements.py` `cec467f1`, `tools/sw_gate.sh` `6048c801`, `firmware/cwht-app/src/main.rs` `3006d072`.

Not in this CR (plan WP-PDR-09 items outside wave 1a or outside the author's reach): the menu override module constant (after WP-PDR-32); the TV-002 part of INSP-015 F-10 (`tools/traceability.py`, WP-PDR-06, CR-011; TV-002 runs 6 and 7 go to the lock when CR-011 merges); the owner's confirmation of the first ACC-COMPLEXITY-001 reading (INSP-015 F-13); the owner's acceptance of TC-SW-TOOL-001 run 6 (INSP-016 F-17, lien L-016-7); the `pico2` `cfg_attr` change and pin CR of lien L-016-6 (FW-B1, the owner as rustos maintainer).

## 2. Reason

The SRR liens of the tools are due before the PDR readiness declaration (INSP-015 re-issue 4 finding table F-07 to F-13; INSP-016 close-out delta 2 liens L-016-2, L-016-5; RID-SRR-004, RID-SRR-014; RFA-SRR-007 item L-7; INSP-029 findings 5 and 6), and plan WP-PDR-09 closes them. Workaround while the CR is open: none needed for correctness; the accredited blobs on `main` stay in use, with their liens stated in the records.

## 3. Alternatives considered

| Alternative | Why rejected or deferred |
|---|---|
| Do nothing | The liens are due before PDR readiness (INSP-015 "Lien: fix before PDR"); RID-SRR-004 and RID-SRR-014 stay open, and the next deck would show the risk matrix and concept diagram below the 20 px floor again |
| Commit the four accredited tools on `main` as Log changes | Not allowed: class-CR CIs since accreditation (05 Table 4-1 row 28) |
| Carry the Log-class items (`measurements.py`, `sw_gate.sh`, lock, `main.rs`, TV records) on `main` | APPROVED records INSP-015 and INSP-016 name their blobs; on `main` they would fail the record drift rule until the delta iterations are committed, and INSP-041 of WP-PDR-08 would lose its reviewed blob mid-review |
| Give the two SRR figure generators TV records and a 03 placement instead of folding them (RID-SRR-014 option 2) | Two more class B tools with records; the fold keeps one controlled generator with one TV record (TV-010), and the SRR render is the fold's own known answer |
| Amend the lock rule to the clone method of run 5 D20 instead of a G0 export mode (INSP-016 F-16 option 2) | The CR-004 lock rule asks for an export; the export mode makes G0 check what the rule asks, with a known answer, and keeps the clone mode |

## 4. Impact assessment (CM plan §5.3)

| Field | Assessment (numbers, IDs, paths) |
|---|---|
| Performance margins | None: no TPM or MOP value changes. The review-trend figure (TPM-003) changes its drawing only; its counts and zones are unchanged (`KnownAnswerTests`, `ZoneTests` unchanged) |
| Safety | None to a hazard or control. `SW-SYNTH` is classed safety-critical in the tool as the SRR decision memo already rules (decision 9); the assurance review it triggers is the same as before (07 section 2.1.1 requires it for both classes). No 07 section 14.1 component changes; hazard analysis and RF exposure evaluation unchanged |
| Risk | None added or re-scored |
| Software classification and tailoring | None: `rmm.json` and the compliance matrix unchanged. The tool constants follow 07 section 2.1.1 and section 14.1 (decision 9) |
| Interfaces | None |
| Operations and ConOps | None |
| Cybersecurity | None |
| Verification | Tool validation, on an export of `f924595` (`docs/cm/tool-validation/evidence/wp-pdr-09-2026-09-27.py` and `.log.txt`: every identity equal to the commit; each selection twice; 0 skipped): TV-003 run 7, 157 tests; TV-007 run 4, 25; TV-010 run 5, 55; TV-012 run 4, 28, with the gate row unchanged; TV-013 run 4, 20. The new known answers fail on each previous blob; five targeted mutants of the fold checks each fail their test. `sw_gate.sh` G0: 5 layouts, 5 MATCH (`evidence/sw-gate-g0-export-2026-09-27.log.txt`); the full gate was not run by this change (the next TC-SW-TOOL-001 run does it). Records invalidated as evidence for the changed blobs (record drift rule): INSP-015 (`docs/reviews/SRR/checklists/tool-validation-tv-001-to-tv-010.md`, APPROVED: TV-001, TV-003, TV-007, TV-010 records, the TV README and the lock; its README and lock entries drift on `main` already) and INSP-016 (`fw-b0-toolchain-proof.md`, APPROVED: `main.rs`, `sw_gate.sh`); both get delta iterations, which are also the lien verifications the plan names (01 section 10.3). INSP-041 (`tool-validation-tv-013.md`, NEEDS CHANGES) names `measurements.py` `abe25acb`: its delta follows (TV-013 section 8 foresaw it). NEEDS CHANGES PDR records that name the lock or the READMEs (INSP-038, INSP-040, INSP-042, INSP-043, their SA pairs) show a drift note only. No test case, report or requirement status changes |
| Cost | None |
| Schedule | Needed before the PDR readiness declaration (plan B4, Tue 10-06); the ACC extensions follow the reviews, the disposition and the merge |
| Requirements and traceability | None added, modified or retired; volatility contribution 0. `tools/traceability.py --report-only` on the branch: 0 violations, 2 warnings, the same as `main` |
| Regulatory | None |
| Documentation | On the branch: `tools/README.md`, the TV records and the TV index, the lock. Not on the branch, for their writers: CR-001 section 5 step 2 "Done (SHA)" (`f924595` on this branch; CM function, at the merge); the SRR log items RID-SRR-004, RID-SRR-014 and RFA-SRR-007 (L-7 parts) move to Answered by the log secretary (WP-PDR-15) after the delta verifications; the deck of the next review uses a figure set that names "risk" and "concept" with `CONCEPT_LAYOUT_SLIDE` (WP-PDR-49, WP-PDR-50) |
| Released units | None |

Classification rationale: Class II. The change modifies class B evidence-generating tools, a gate script, a code comment and the records that describe them; it changes no requirement, interface, safety control, filed verification evidence or operator procedure, and none of the tools can change a released image (05 §5.1). The rule C6 impact review is performed before the disposition (lesson L4).

## 5. Implementation plan

| Step | Artifact and path | Responsible | Done (SHA) |
|---|---|---|---|
| 1 | Tool, test, fixture and comment changes of section 1 on the branch | Claude (tool owner, WP-PDR-09) | `16cdd3e`, `067966c`, `012d53c`, `fcb9ba7`, `e024b24`, `dacc6e9`, `f924595` |
| 2 | TV-003 run 7, TV-007 run 4, TV-010 run 5, TV-012 run 4, TV-013 run 4, TV-001 limitation 4, the TV index, the lock and `tools/README.md`, with the evidence and renders | Claude (tool owner) | `7b4e3b4` |
| 3 | `main` merged into the branch (lock conflict resolved) | Claude | `367b3dd` |
| 4 | Section 6 impact review of this CR | Independent reviewer (did not author CR-014 or WP-PDR-09) | pending |
| 5 | Product review frozen at the branch blobs: `docs/reviews/PDR/checklists/tool-validation-tv-003-tv-007-tv-010-tv-012.md` (plan WP-PDR-09 Records; checklist `peer-review-checklist-tool-validation` with `peer-review-checklist-code`, CR-012) and its software assurance pair (tools used for credit) | Reviewer agents | pending |
| 6 | Delta iterations of the SRR records INSP-015 (F-07 to F-12 against this branch; F-13 stays with the owner) and INSP-016 (F-13, F-16), naming the branch blobs; lead SE convention of 2026-09-27: reviewer verdict set, record verdict held until the merge, committed on `main` | Their reviewers | pending |
| 7 | INSP-041 delta on `measurements.py` `cec467f1` (WP-PDR-08) | WP-PDR-08 reviewer | pending |
| 8 | Owner disposition (section 7); merge `merge(CR-014): ...` with `--no-ff`; the record verdicts of steps 5 to 7 set in the merge commit or right after it; then the owner's decisions on the proposed extensions ACC-VALDOCS-001, ACC-TREND-001, ACC-FIGS-001, ACC-COMPLEXITY-001 (and ACC-MEASURE-001 at its own decision) | Owner; Claude merges and transcribes | pending |
| 9 | CSA regenerated | Claude (CM function) | pending |

Verification of the implementation (what the independent reviewer checks): the evidence procedure re-run on an export of the branch head gives the same counts and mutation results; each carried item of section 1 against its source finding text; the SRR concept render reproduced pixel for pixel with `CONCEPT_LAYOUT_SRR`; the five PNGs of `evidence/wp-pdr-09-renders/` and the two fixture PNGs opened; `tools/validate_docs.py` on the branch fails only the record drift of INSP-015 and INSP-016 beyond `main`'s own failures; the G0 evidence repeated on a fresh export and clone.

## 6. Independent review of the impact assessment

Required by plan rule C6 (lesson L4), although a Class II CR that touches no requirement, ICD, hazard or test case would not need it (05 §5.2).

| Item | Reviewer (agent invocation) | Date | Finding | Resolution |
|---|---|---|---|---|
| Pending | | | | |

Reviewer concurrence: pending.

## 7. CCB disposition (owner)

| Field | Value |
|---|---|
| Decision | Pending |
| Class confirmed | Pending (proposed II) |
| Date | |
| Conditions | Proposed: merge only after section 5 steps 4 to 7 |
| Rationale | |
| Waiver scope (if Approved (waiver)) | n/a |
| Re-look trigger and re-look-by review (if Deferred) | |
| Source | |

Disposition history (append only):

| Date | Decision | New target | Source |
|---|---|---|---|
| | | | |

## 8. Implementation record

| Commit | Files | Trailer check (`CR: CR-014` present) |
|---|---|---|
| `16cdd3e` | `tools/validate_docs.py`, `tools/tests/test_validate_docs.py` | yes |
| `067966c` | `tools/review_trend.py`, `tools/tests/test_review_trend.py` | yes |
| `012d53c` | `tools/render_review_figures.py`, `tools/tests/test_render_review_figures.py`, four fixture files | yes |
| `fcb9ba7` | `tools/complexity_gate.py`, `tools/tests/test_complexity_gate.py` | yes |
| `e024b24` | `tools/measurements.py`, `tools/tests/test_measurements.py` | yes |
| `dacc6e9` | `tools/sw_gate.sh`, `tools/toolchain.lock.md` (rustos tree of the pin), `evidence/sw-gate-g0-export-2026-09-27.sh` | yes |
| `f924595` | `firmware/cwht-app/src/main.rs` | yes (and `CR: CR-001`) |
| `7b4e3b4` | TV-001, TV-003, TV-007, TV-010, TV-012, TV-013, the TV README, `tools/README.md`, the lock, evidence and renders | yes |
| `367b3dd` | merge of `main` at `72d0a2f` | yes |

Traceability report after implementation: not regenerated on the branch (`--report-only` run, files restored); renders regenerated: `docs/cm/tool-validation/evidence/wp-pdr-09-renders/` (evidence, not package figures).

## 9. Verification of implementation

| Impact item | Planned closure (from §4/§5) | Evidence (report path, TC id, analysis file) | Result |
|---|---|---|---|
| | | | |

## 10. Closure

| Field | Value |
|---|---|
| Owner merge approval | |
| Merge commit | |
| Waiver entered in CSA item 12 and affected VDDs | n/a |
| CSA regenerated | |
| Date closed | |

## 11. History

| Date | State | By | Commit on main | Note |
|---|---|---|---|---|
| 2026-09-27 | Submitted | Claude (tool owner, WP-PDR-09) | this commit | Branch head `367b3dd`; section 6 review requested (rule C6) |
