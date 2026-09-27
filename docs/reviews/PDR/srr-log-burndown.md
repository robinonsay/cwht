# SRR log and lien burndown

**Status:** Working product of the PDR phase (review record folder, 05 Table 4-1 row 33). **Author:** Claude, review secretary, `docs/plan/pdr-work-plan.md` WP-PDR-15, output "a burndown table for package §15". **Date:** 2026-09-27, wave 1a, read at `main` `553ea12` (no commit after `b77a9e5` touches the SRR log or the SRR records) plus the WP-PDR-15 commit that adds this file. **Use:** input to `docs/reviews/PDR/package.md` section 14 ("Prior RFA/RID trend", open items with closure plans) and section 15. The package author (WP-PDR-49) re-reads every state from the log and the records at F2. This file is updated by WP-PDR-15 at each log transition and is not a source of truth for states: `docs/reviews/SRR/rfa-rid-log.json` is.

**Rules applied** (`docs/process/01-lifecycle-and-reviews.md` section 10.3). The assignee moves an item from Open to Answered with a response and evidence. A RID moves to Verified only on an independent reviewer's record (`verification.record`). An RFA moves to Verified only on the owner's check. Only the owner closes a Verified item (PDR plan OD-11). No state is skipped. Tool rule (`tools/README.md`, `validate_docs.py`): the record named in `verification.record` must carry, in its front matter `product`, exactly the item's `product` string. The "Record needed" column below states that string.

## 1. Log states at 2026-09-27

`tools/review_trend.py --date 2026-09-27` (TV-007, ACC-TREND-001; read-only, no `--write`), run before this file's commit: SRR zone **Green**. 22 raised (14 Minor RIDs, 8 Routine RFAs), 0 Verified, 0 Closed, 0 Withdrawn, 0 overdue. `closure_fraction_at_gate` is undefined until the PDR memo is signed, and every item is due at the PDR readiness declaration (Tue 10-06, plan section 5.2). Rule 1 of 01 section 11 makes the SRR zone Red at the PDR gate if closure_fraction_at_gate is below 0.8, closure_fraction_at_gate is closed / (raised - withdrawn) (01 section 11). With no item withdrawn, at least 18 of the 22 items must be Closed when the PDR memo is signed (plan risk PR-11).

| State | Before WP-PDR-15 | After this commit |
|---|---|---|
| Open | 20 | 19 |
| Answered | 2 (RID-SRR-010, RFA-SRR-008) | 3 (adds RFA-SRR-003) |
| Verified | 0 | 0 |
| Closed or Withdrawn | 0 | 0 |

## 2. The 22 log items

"Fix WP" and "C-item" are from PDR plan section 10.1. The verifier follows 01 section 10.3.

| Id | Type | SRR source | C-item | Fix WP | State | Evidence so far | Next transition and who | Record needed (`product` field, exact) |
|---|---|---|---|---|---|---|---|---|
| RID-SRR-001 | RID Minor | package §15 item 2 (TPM-002 receive allocation) | C-006 | WP-PDR-29 | Open | none | Answered when WP-PDR-29 re-allocates TPM-002 (decision 98, RSK-058 S1) | `docs/plan/tpm.json`: no existing record has this product; the WP-PDR-29 TPM record must name it |
| RID-SRR-002 | RID Minor | item 3 (`conventions.instruments` text) | C-007 | WP-PDR-29 | Open | none | Answered on the tpm.json convention edit | `docs/plan/tpm.json` (as above) |
| RID-SRR-003 | RID Minor | item 7 (REQ-SYS-054 against decision 37) | C-018 (content by WP-PDR-11) | WP-PDR-11 (CR-008, Submitted; prototype on branch `cr/CR-008-srr-liens-l1-and-tc-sys`) | Open | CR-008 reviewed by INSP-044 iteration 1 (reviewer verdict APPROVED, record NEEDS CHANGES, `c199eb2`) | Answered after CR-008 is dispositioned and merged (evidence kind `cr`, the item is a baselined L1 requirement, 01 section 10.5); Verified by the INSP-003 role in a delta of `docs/reviews/SRR/checklists/requirements-sys.md` | `docs/requirements/sys/requirements.json`: INSP-003 has this product. INSP-044's product is `CR-008` and does not qualify |
| RID-SRR-004 | RID Minor | item 8 (review-trend date labels) | C-170 | WP-PDR-09 | Open | none at HEAD (`tools/review_trend.py` unchanged since `779f93f`) | Answered on the tool fix with its known-answer test | `tools/review_trend.py`: no existing record has this product (INSP-015's product is `docs/cm/tool-validation/ ...`) |
| RID-SRR-005 | RID Minor | item 10, ConOps appendix D item D9 (ADR-015 guest lock) | C-144 | WP-PDR-14 | Open | none at HEAD | Answered on the ADR-015 correction route (decision 105) | `docs/decisions/adr/ADR-015-operator-model-ops-a-guest-lock.md`: INSP-011's product is the directory `docs/decisions/adr/` and does not qualify (the same gap as RID-SRR-010) |
| RID-SRR-006 | RID Minor | item 10, D11 (hazard phases against ConOps modes) | C-048 | WP-PDR-16 | Open | none | Answered in the 0.6.0-pha re-issue | `docs/safety/hazards.json`: INSP-008's product is `docs/safety/hazard-analysis.md` and does not qualify |
| RID-SRR-007 | RID Minor | item 10, D12 (HZ-001 K6 to cite OPS-022) | C-049 | WP-PDR-16 | Open | none | As RID-SRR-006 | `docs/safety/hazards.json` (as above) |
| RID-SRR-008 | RID Minor | item 10, D13 (pocket-carry MOPs to MOE-013) | C-008 | WP-PDR-29 | Open | none | Answered on the re-parenting (decision 96) | `docs/plan/tpm.json` (as RID-SRR-001) |
| RID-SRR-009 | RID Minor | item 10, D14 (research F3 sentence) | C-205 | WP-PDR-30 | Open | none at HEAD (`docs/research/rf-exposure-evaluation.md` unchanged since `779f93f`) | Answered on the F3 correction | `docs/research/rf-exposure-evaluation.md`: no existing record has this product |
| RID-SRR-010 | RID Minor | item 10, D15 (ADR-014 tier basis) | C-145 | WP-PDR-15 (fix already made) | **Answered** 2026-09-26 | ADR-014 erratum line, commit `5122a6b`; checked by the INSP-011 post-ruling delta 2 (`877ffac`), whose product is the ADR directory | Verified by an independent reviewer record whose product is the ADR-014 file (PDR plan WP-PDR-15 output, C-145) | `docs/decisions/adr/ADR-014-licensed-operators-only.md` |
| RID-SRR-011 | RID Minor | item 10, D17 (weak-signal source for MOE-010) | C-065 | WP-PDR-43 (OD-26) | Open | none | Answered on the OQ-VV question and the tinySA TV note | `docs/process/04-verification-and-validation.md`: INSP-021 has this product |
| RID-SRR-012 | RID Minor | item 11, 04 alignment A3 (RMM meta, NPR 8705.2) | C-070 | WP-PDR-17 (CR-010, Submitted; branch `cr/CR-010-apply-srr-decisions-9-and-40`) | Open | none on `main` | Answered on the RMM change (Log class per decision 10 (c) or a CR, per the RID text) | `docs/process/rmm.json`: INSP-009 and INSP-017 have product `docs/process/03-software-classification-and-rmm.md` and do not qualify |
| RID-SRR-013 | RID Minor | item 11, A4 (RMM SWE-071 citation) | C-071 | WP-PDR-17 | Open | none on `main` | As RID-SRR-012 | `docs/process/rmm.json` (as above) |
| RID-SRR-014 | RID Minor | item 38 (figure generators outside the tool set) | C-072 | WP-PDR-09 | Open | none | Answered when the generators are folded into `tools/render_review_figures.py` or given TV records | `docs/reviews/SRR/figures/risk-matrix.py`: no existing record has this product |
| RFA-SRR-001 | RFA Routine (L-1) | 126 requirement TBR liens (101 L1, 25 L2) | C-001, C-002 | WP-PDR-45 (values from WPs 19 to 30, 33, 40) | Open | none | Answered when every L1 TBR is closed (E-25); owner verifies | owner check (RFA) |
| RFA-SRR-002 | RFA Routine (L-2) | mass and envelope estimates, TPM-001 and TPM-016 | C-005 | WP-PDR-29 | Open | none | Answered on the budgets; owner verifies | owner check |
| RFA-SRR-003 | RFA Routine (L-3) | lessons-learned file (S10) | C-206 | WP-PDR-05 | **Answered** 2026-09-27 (this commit) | `docs/lessons-learned.md` at `e119181` (blob `ec30a264`); INSP-035 APPROVED at `a900969` | Owner verifies, then closes (OD-11) | owner check |
| RFA-SRR-004 | RFA Routine (L-4) | package-level Minor items (section 3 below) | C-199 to C-201 and the RIDs of L-4 | WP-PDR-15 with the RID WPs | Open | Errata E-1 to E-5 (`docs/reviews/SRR/errata.md`); BR §10 C-1 | Answered when every section 3 row is fixed and independently verified; owner verifies | owner check |
| RFA-SRR-005 | RFA Routine (L-5) | cross-document items due at PDR: 03 X9, X10; 04 A11; SEMP F-06, F-15; OQ-SAF questions with close_by PDR; package §15 items 55 and 66 | C-079, C-080 (03 X9, X10), C-064 (A11), C-111, C-112 (SEMP F-06, F-15), C-182 (item 55) | WP-PDR-08, 43, 06, 07, 16, 09 | Open | none | Answered when every L-5 item closes | owner check |
| RFA-SRR-006 | RFA Routine (L-6) | 122 record liens plus the INSP-011 erratum E-10 of the 30 SRR records (SRR package section 20.2) | the record-finding rows of plan §10.1 | Group C and D WPs and WP-PDR-09, 35, 36, 46, 47 | Open | Delta iterations so far: INSP-007 re-issue 3 (`aadc0ba`, finding-18); INSP-044 and INSP-045 (CR-008, iteration 1) | Answered when each SRR record's delta closes its liens; owner verifies | owner check |
| RFA-SRR-007 | RFA Routine (L-7) | package-level Routine items from revision 3: ADR citations in `source_ids`; ADR back-reference in `tools/traceability.py`; 05 §9.2 known-answer rows; `measurements.py` PASS lines; `ASSURANCE_WHOLE_PRODUCTS`; REQ-SYS-122 note; hazard-line stamps of ADR-015, 022, 023, 026 | C-093, C-183, C-184, C-185, C-186 and the L-7 rows of C-019 to C-025 and C-146 to C-157 | WP-PDR-05, 06, 09, 11, 14 | Open | none | Answered when every L-7 item closes | owner check |
| RFA-SRR-008 | RFA Routine | CR-002 independent Class I impact review | C-097 | done at SRR close-out | **Answered** 2026-09-27 | `8b86c16` (CR-002 section 6 review), `bb2485e` (deviations entries 1 to 4 closed) | Owner verifies (OD-11); WP-PDR-15 transcribes the verification | owner check |

## 3. L-4 items (RFA-SRR-004): SRR package section 15 items not held by a record

| §15 item | Subject | Route | State 2026-09-27 | Independent verification |
|---|---|---|---|---|
| 2, 3 | TPM-002 allocation; tpm.json convention | RID-SRR-001, RID-SRR-002 | Open (WP-PDR-29) | per RID |
| 8 | Review-trend date labels | RID-SRR-004 | Open (WP-PDR-09) | per RID |
| 10 (Minor D items) | ConOps appendix D D9, D11 to D15, D17 | RID-SRR-005 to 011 | D15 Answered (RID-SRR-010); others Open | per RID |
| 11 | RMM A3, A4 | RID-SRR-012, 013 | Open (WP-PDR-17) | per RID |
| 38 | Figure generators | RID-SRR-014 | Open (WP-PDR-09) | per RID |
| 55 | `tools/requirements.txt` pins (AL-4); also named in L-5 | C-182 (WP-PDR-09 "confirmation") | Fixed before the tag: 35 `==` pins at `be270f1` (R16), unchanged at `779f93f` and at HEAD; baseline record §2a row 27 records the AL-4 comparison | INSP-015 role at the WP-PDR-09 delta |
| 58 | Deck title named package revision 3 | C-199; erratum E-1 | Fixed in the deck re-write; presented deck `64e53ee` reads "package revision 8 final" | INSP-029 role note in `docs/reviews/SRR/checklists/srr-deck.md` |
| 71 | Decision 94 "tools not installed" | C-200; erratum E-3 | Erratum filed (`docs/reviews/SRR/errata.md`, pointer in `decisions-for-owner.md` "Errata") | reviewer of the errata file |
| 77 residual | Decision 114 recommendation "(INSP-015 APPROVED)"; K17 preamble | C-201; erratum E-4 | Erratum filed; K17 preamble needs no correction (its revision 8 final sentence is current) | reviewer of the errata file |

## 4. Other SRR package section 15 items open at the SRR memo

These items are held by a record lien (L-6, RFA-SRR-006) or by L-5 or L-7, not by L-4. They are listed so that section 15 of the SRR package burns down to zero. Record liens close in the owning record's delta iteration (plan section 3.4 rule).

| §15 item | Holder | Fix WP (plan §10.1) |
|---|---|---|
| 23 | INSP-001 finding-12 | WP-PDR-10 (CR-009) |
| 25 | INSP-002 finding-19 | WP-PDR-10 (CR-009) |
| 29 | INSP-003 finding-17 | WP-PDR-11 |
| 34 | INSP-004 finding-17 | WP-PDR-35 (C-027) |
| 37 | INSP-007 finding-16 | WP-PDR-18 (C-140 to C-143) |
| 40, 41 | INSP-008 finding-14, finding-15 | WP-PDR-16 (C-050 to C-055) |
| 42 | INSP-009 finding-5, INSP-017 finding-3 | WP-PDR-17 (C-070 to C-078) |
| 43 | INSP-017 finding-7 | WP-PDR-17 |
| 45 | INSP-010 finding-14 | WP-PDR-13 (C-100 to C-107) |
| 47, 48 | INSP-011 F-05 to F-08, F-10, F-11 | WP-PDR-14 (C-146 to C-157) |
| 49 | INSP-012 finding-1 (CTL and PWR residual) | WP-PDR-36 (C-167 to C-169) |
| 54 | INSP-016 F-04 | WP-PDR-09 and WP-PDR-47 (INSP-016 delta) |
| 56 | `tools/render_review_figures.py` figure-set defects | WP-PDR-09 |
| 60 | INSP-013 finding-11 (TS-001 and TS-002 Status lines) | WP-PDR-14 (C-159 to C-165) |
| 66 | Stale `docs/vv/traceability-report.md` (L-5) | WP-PDR-06 and WP-PDR-48 |
| INSP-029 finding-3, 5, 6 | Deck liens | C-202 (erratum E-2; PDR side WP-PDR-50), C-203 and C-204 (WP-PDR-09, WP-PDR-50) |

Majors 27, 46, 52 and 53 closed before `baseline/srr` through R16 and the close-out (baseline record §0.4.2 P1). They are not liens.
