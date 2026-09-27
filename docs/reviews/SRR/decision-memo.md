---
review: SRR
package_revision: 8
disposition: Approved with liens
signed: 2026-09-26
baseline_tag: null
revoked: null
---

# SRR Decision Memo

Template: `docs/templates/decision-memo.md`. This memo is the review board report and the Decision Authority's decision record required by NPR 7123.1D §5.2.3.1 items b, g and i, completed per `docs/process/01-lifecycle-and-reviews.md` section 9 ("the review process" below). Claude (review secretary) wrote it from `docs/reviews/SRR/minutes.md`, `docs/reviews/SRR/package.md` and `docs/reviews/SRR/decisions-for-owner.md`; it is signed by the transcription of the owner's approval wording in section 12. The memo is amended, never rewritten: later changes are appended in section 13.

`baseline_tag` stays `null` until `baseline/srr` exists: the owner directed that the tag is applied after the post-ruling work R16 is verified by the reviewers (minutes, Disposition; section 10).

## 1. Identification

| Field | Value |
|---|---|
| Review | SRR (combined with MCR; charter section 3) |
| Package | `docs/reviews/SRR/package.md` revision 8 final with the lead SE current-status edit and the readiness-confirmation Minors M1 to M4, at commit `a6d0959` |
| Slide deck presented | `docs/reviews/SRR/slides/srr.adoc` at commit `64e53ee`, 42 slides (`slides/png/slide-01.png` to `slide-42.png`), verified by the INSP-029 delta re-issue at `0a583b9`. The owner read all 42 slides as a PDF before the walk-through; the read-aloud corrections of package section 2.2 were given in chat (minutes, "Deck read-through") |
| Minutes | `docs/reviews/SRR/minutes.md`, committed at `7647516` (rulings and disposition), with the OA-1 and OA-2 record added at `0a6f461` (owner statements transcribed verbatim) |
| Rulings source | `docs/reviews/SRR/decisions-for-owner.md` revision 6 amended, at commit `5ebe90c`: each ruling's text is the "Recommendation" cell of its row (minutes, "Rulings") |
| RFA/RID log | `docs/reviews/SRR/rfa-rid-log.json`, which passed `tools/validate_docs.py` (the log and this memo PASS; the whole repository passed 50 of 50 checks before the first R16 product commit, after which the record drift rule flags the records R16 re-verifies) and the item check of review process section 10.4 on 2026-09-26 |
| Chair and Decision Authority | Robin Onsay (also Engineering TA, SMA TA, and, by decision 7, Health and Medical TA and CIO/SAISO designee) |
| Presenter | Claude (lead systems engineer, main session) |
| Purpose of the gate | Confirm that the functional and performance requirements respond to the owner's expectations (NGOs, MOEs, ConOps) and can be achieved within the project's means, that the concept is feasible, and that the plans are sufficient to begin preliminary design; the SRR also serves as the MCR (review process section 4.1) |

## 2. Sessions

| Session | Date | Package revision | Slides presented | Outcome |
|---|---|---|---|---|
| 1 | 2026-09-26 | 8 final (`a6d0959`) | 01 to 42 (read by the owner as a PDF, with the section 2.2 read-aloud corrections; walk-through in conversation) | Convened as a pre-review session (package section 2). The owner ruled key decisions K1 to K17 as recommended, then approved the SRR: dispositioned **Approved with liens** (liens L-1 to L-7), adopting the consent agenda, the candidate RIDs and the proposed tailoring as recommended and confirming readiness (row S1). OA-1 and OA-2 were first recorded as deferred to PDR; the owner then brought the Pico 2 and both were performed in the same session, all Pass (minutes, "OA-1 and OA-2 performed (deferral reversed)") |

## 3. Entrance criteria summary

Status as the package states it (package section 4, revision 8 final, deck amendment tabulation): **Met 25, Partially met 10, Not met 4** of 39 rows (11 standing rows S1 to S11 and 28 SRR rows).

- Row S1 (agenda and success criteria agreed; Hard) was Not met pending the owner's confirmation. The owner's approval confirms readiness (minutes, Disposition), so S1 is Met on 2026-09-26.
- Hard rows not Met at the package date, each waiting on an owner ruling or on the post-ruling work R16 (package sections 2.1 and 4): S3 (Not met: INSP-003, INSP-011 and INSP-016 NEEDS CHANGES on 5 open Major findings), 20 (Not met: FW-B0 Blocked), and 5, 7, 8, 10, 14, 15, 22, 23 and 25 (Partially met). The rulings recorded in section 8 are the rulings these rows waited on; the R16 edits and the reviewer verifications close them (section 9, conditions 1 and 2).
- Row 20, owner part: OA-1 (FW-B0 flash and observe, TC-SW-TOOL-001 steps 11 and 12) and OA-2 (picotool verify known answer) were at first not performed and were recorded as deferred to PDR (minutes, Disposition). The owner reversed the deferral in the same session ("I grabbed the pico so I'm ready to test the flash whenever you are.") and Claude ran every command on board "1" (RP2350, chip id `0xf9c6e0eff60605d1`): step 11, rustos blinky, 60 to 63 cycles in 60 s (window 10 to 120), Pass; step 12, cwht-app, 18 cycles in 60 s (window 3 to 45), Pass; OA-2, the true image verifies and the one-byte-altered copy fails at `0x1000002f`, Pass (minutes, "OA-1 and OA-2 performed (deferral reversed)"). This closes the owner part of row 20; the raw outputs are filed with the TC-SW-TOOL-001 run 4 report and INSP-016 re-verifies the evidence (R16). No tailoring of row 20 remains.
- Soft criteria not met, accepted as liens: S8 (TPM-001 and TPM-016 have no estimate) as RFA-SRR-002 (lien L-2); S10 (`docs/lessons-learned.md` absent) as RFA-SRR-003 (lien L-3). Row S8 is Partially met, row S10 Not met.
- Hard criteria found unmet during the review: none beyond the package statement above; no new shortfall was raised at the session.

**Secretary's note on the rule.** Review process sections 4.2 and 12.1 convene the gate only when the Hard rows are met, and list an unmet Hard criterion found during the review as a cause of *Not approved*. The owner gave the approval at the pre-review session, with the Hard rows above still closing through R16. This memo transcribes the approval as given and records the owner's own sequencing as conditions (section 9): R16 is performed and verified by the reviewers, and only then is `baseline/srr` created. The owner may instead direct a re-convened gate session after R16; that choice would be an amendment in section 13.

## 4. Success criteria assessment (§5.2.3.1 c)

The owner approved the requested disposition as a whole and did not rule criterion by criterion. The table therefore gives the presenter assessment of package section 20 (Met 10, Partially met 4, Not met 4) and the closure path; no per-criterion chair ruling was given.

| # | Success criterion (short) | Package assessment | Lien id | Closure path |
|---|---|---|---|---|
| 4.4-1 | L1 requirements respond to NGOs, MOEs, ConOps; achievable | Partially met (INSP-003 finding-6, Major) | none | Decision 30 (item (g) record, section 8.1) closes finding-6; the INSP-003 reviewer verifies in R16 |
| 4.4-2 | Requirements and plans mature enough for Phase B | Not met (14 L1 TBRs and the safety and regulatory key decisions unruled; INSP-003 NEEDS CHANGES) | RFA-SRR-001 (L-1, the TBRs carried to PDR) | The 14 SRR TBRs close in this memo (section 8.3); K1 to K17 ruled; INSP-003 re-issue in R16 |
| 4.4-3 | Allocation and control process sound; L2 plan to PDR | Met | none | CR control starts at `baseline/srr` |
| 4.4-4 | External and major internal interfaces identified | Met | RFA-SRR-006 (INSP-012 record liens) | none |
| 4.4-5 | V&V approach determined for every requirement | Partially met (INSP-003 finding-6 on the ten regulatory methods) | none | Decision 30 (section 8.1); decision 113 CR to 04 rule 7.3.6 |
| 4.4-6 | Major risks identified, assessed, with viable mitigations | Met | RFA-SRR-006 (INSP-007 record liens) | Decision 14 approves the 32 Red plans |
| 4.4-7 | Objectives clear and consistent; concept feasible | Met | RFA-SRR-006 (INSP-002 record liens) | none |
| 4.4-8 | Concept evaluation criteria prioritized; existing assets considered | Partially met (decision 107 pending) | none | Decision 107 ruled (A0 with the TS-002 section 8 revisit triggers); ADR-027 records it in R16 |
| 4.4-9 | Technical planning sufficient for Phase B | Met | RFA-SRR-006 (INSP-005 record liens) | Decision 1 approves the plans |
| 4.4-10 | HSI aspects sufficient for the next phase | Met | none | Decision 2 confirms HSI as a SEMP section |
| 4.4-11 | Fault tolerance philosophy reflected in requirements | Partially met (decisions 38 to 40 pending) | none | Decisions 38, 39 and 40 adopt REQ-SYS-180, 181 and 182 with their values (section 8.3) |
| 4.4-12 | Software components meet the SRR-point criteria | Not met (FW-B0 Blocked, INSP-016 F-01 and F-02 Major; TV records not accredited; SWE-033 pending) | none | Decisions 108, 109, 110, 114, 107 and 115 (b) ruled; R16 (a) runs the installs, `tools/sw_gate.sh` and INSP-016 iteration 4; OA-1 and OA-2 performed 2026-09-26, Pass |
| C1 | Gate-specific criteria met or on accepted liens | Not met | none | Follows 4.4-1 to 4.4-12 through R16 |
| C2 | Compliance with charter, SEMP, RMM and compliance matrix | Met | RFA-SRR-006 (INSP-024 record liens) | none |
| C3 | TBD and TBR items with plans and closure events | Met | RFA-SRR-001 | none |
| C4 | Proposed tailoring appropriate and recorded | Met | none | Approved in section 7 |
| C5 | Software components meet the life-cycle criteria | Not met | none | As 4.4-12 |
| C6 | Risks identified, assessed, mitigated with accepted residual | Met | none | Residual risks accepted by decisions 11, 32, 3 and 6 (section 8) |

## 5. RFA/RID summary (§5.2.3.1 a, d)

| Type | Severity | Raised | Closed at signing | Verified pending | Answered | Open | Withdrawn |
|---|---|---|---|---|---|---|---|
| RID | Major | 0 | 0 | 0 | 0 | 0 | 0 |
| RID | Minor | 14 | 0 | 0 | 0 | 14 | 0 |
| RFA | Blocking | 0 | 0 | 0 | 0 | 0 | 0 |
| RFA | Routine | 7 | 0 | 0 | 0 | 7 | 0 |

Agreement on disposition of every item: yes (every item is a lien with owner, plan and due event, section 6). Major RIDs and Blocking RFAs are all Closed: not applicable (none raised).

Source of the items. No RFA or RID was raised by the owner slide by slide. The approval adopts the candidate RIDs of package section 15 as the package recommends: the 14 RIDs are the section 15 items whose proposed handling is a Minor RID (items 2, 3, 8, 11 (A3 and A4), 38, the Open Minor ConOps appendix D items D9, D11, D12, D13, D14, D15 and D17 of item 10) and item 7, whose handling is a RID against REQ-SYS-054 when the ruling changes it (decision 37 does). The 7 Routine RFAs record the accepted liens L-1 to L-7, as package section 20.1 states for every accepted lien.

Reviewer findings adopted: 0 individually as RIDs, 0 as RFAs, 0 No action. The Minor findings of the 30 records INSP-001 to INSP-030 dispositioned "Lien: fix before PDR" (122 plus the INSP-011 erratum E-10, package section 20.2) are carried as one lien, RFA-SRR-006 (L-6). The five open Major findings (INSP-003 finding-6, INSP-011 F-01 and F-04, INSP-016 F-01 and F-02) were not adopted as RIDs: they close through the rulings and R16 before the tag and are never liens (package section 15 items 27, 46, 52, 53). Recording these dispositions against each `#finding-<n>` entry in the records is the records' reviewers' work at their next iteration.

## 6. Liens (§5.2.3.1 e)

Every item below was Open at signing, carries `lien: true` in the log and a same-state history entry "Lien accepted in docs/reviews/SRR/decision-memo.md" dated 2026-09-26. Due for every lien: before the PDR readiness declaration (the L2 requirement TBRs by CDR at the latest, charter section 7; their files give PDR).

| Lien id | Type | Owner | Closure plan | Due (event or date) | blocks-order (CDR only) | Status at signing |
|---|---|---|---|---|---|---|
| RID-SRR-001 | RID Minor (L-4) | Claude | TPM-002 receive allocation below the research budget: Re-allocate the TPM-002 receive power at PDR with the power allocation of decision 98 (SRR decision 98, owner ruling 2026-09-26: approve with the PDR TPM definitions) and the RSK-058 S1 step; an independent reviewer verifies. | PDR readiness declaration | n/a | Open |
| RID-SRR-002 | RID Minor (L-4) | Claude | tpm.json instruments convention names an ADR for the tinySA receipt: Reword the convention to the charter section 9 record (receipt-inspection report plus TV-NNN before TRR); editorial per 05 section 2 while unbaselined, otherwise under a CR. | PDR readiness declaration | n/a | Open |
| RID-SRR-003 | RID Minor (R16 requirement edit) | Claude | REQ-SYS-054 paddle watchdog against the ruled no-gap form of HZ-004 K4: Rewrite REQ-SYS-054 to the no-gap form, add or edit the squeeze-limit requirement of OQ-SAF-002, confirm REQ-SYS-053 covers the Bug dah, update the citing test cases and the ConOps Table 3.4-4 row 3 (decision 42 (a)); performed in package item R16 before baseline/srr and verified by the L1 requirements reviewer (INSP-003). | PDR readiness declaration | n/a | Open |
| RID-SRR-004 | RID Minor (L-4) | Claude | Review-trend plot repeats x-axis date labels: Fix the date axis so each date is labelled once, add a known-answer test in tools/tests/test_review_trend.py, re-render and inspect the plot; the tool validation record of the tool is updated. Include the single-date case seen when the secretary opened the render of 2026-09-26 (21 items raised on one date): the step lines draw no visible line or marker, and the '0 closed + withdrawn' annotation sits on the date labels. | PDR readiness declaration | n/a | Open |
| RID-SRR-005 | RID Minor (L-4) | Claude | ADR-015 section 2 overstates the guest lock: Restate as no transmission by accident, release being a deliberate licensee action under the operator rules card, consistent with SRR decisions 17 and 19 (owner ruling 2026-09-26: accept ADR-015; guest lock option a) and the ADR correction route of decision 105. | PDR readiness declaration | n/a | Open |
| RID-SRR-006 | RID Minor (L-4) | Claude | Hazard phases differ from the ConOps modes: Adopt ConOps Table 3.4-5 as the mapping or rename the phases to the mode names; the hazard analysis reviewer (INSP-008) verifies. | PDR readiness declaration | n/a | Open |
| RID-SRR-007 | RID Minor (L-4) | Claude | HZ-001 K6 does not cite OPS-022: Cite OPS-022 in HZ-001 K6; the hazard analysis reviewer (INSP-008) verifies. | PDR readiness declaration | n/a | Open |
| RID-SRR-008 | RID Minor (L-4) | Claude | Pocket-carry MOPs and TPMs parent to the range MOE: Re-parent them to MOE-013 as SRR decision 96 rules (owner ruling 2026-09-26: add and re-parent); run tools/validate_docs.py and tools/traceability.py. | PDR readiness declaration | n/a | Open |
| RID-SRR-009 | RID Minor (L-4) | Claude | RF exposure research F3 sentence contradicts its Table 2: Correct the sentence to 0.41 m for a 1 W carrier (0.26 m or less keying CW at 1 W; 0.29 m for the 0.5 W carrier) so ADR-014, HZ-006 and the handbook do not inherit the error. | PDR readiness declaration | n/a | Open |
| RID-SRR-010 | RID Minor (L-4) | Claude | ADR-014 exposure tier basis under OPS-B: Cite the OET 65 Supplement B controlled-environment statement and the OPS-B tier row of ConOps appendix C, consistent with SRR decision 18 (owner ruling 2026-09-26: keep the 1 W limit for OPS-B until a dated owner record confirms the controlled-environment basis). | PDR readiness declaration | n/a | Open |
| RID-SRR-011 | RID Minor (L-4) | Claude | No weak-signal source for the MOE-010 bench part: Open an OQ-VV question for the weak-signal source with close_by PDR, and confirm the MOE-006 span in the tinySA TV record. | PDR readiness declaration | n/a | Open |
| RID-SRR-012 | RID Minor (L-4) | Claude | RMM meta does not disposition NPR 8705.2: Add a meta note: not applicable, cwht is not a human-rated space system, citing 01 section 3.5; run tools/render_rmm.py --check. The RMM is approved at SRR (decision 6), so after baseline/srr the change is Log class per decision 10 (c) or a CR. | PDR readiness declaration | n/a | Open |
| RID-SRR-013 | RID Minor (L-4) | Claude | RMM row SWE-071 cites a stale-test flag planned for PDR: Cite 04 section 8.2 and rule 7.3.11 in row SWE-071; run tools/render_rmm.py --check. | PDR readiness declaration | n/a | Open |
| RID-SRR-014 | RID Minor (L-4) | Claude | Package figure generators outside the tool set: Fold both generators into tools/render_review_figures.py with known-answer tests, or give each a TV record and a 03 placement; re-render and inspect the figures. | PDR readiness declaration | n/a | Open |
| RFA-SRR-001 | RFA Routine (L-1) | Robin (Claude produces the evidence) | L-1: close the TBRs carried to PDR: Robin decides each value on Claude's evidence per the plan in its tbr object; the closed values are recorded in the PDR decision memo (L2 TBRs by CDR at the latest, charter section 7). | PDR readiness declaration | n/a | Open |
| RFA-SRR-002 | RFA Routine (L-2) | Claude | L-2: mass and envelope estimates for TPM-001 and TPM-016: Produce the bottom-up mass estimate and the CAD envelope in docs/design/budgets.md and enter the estimates in docs/plan/tpm.json before the PDR readiness declaration. | PDR readiness declaration | n/a | Open |
| RFA-SRR-003 | RFA Routine (L-3) | Claude | L-3: create the lessons-learned file: Create docs/lessons-learned.md with the ten entries of package section 19 before the PDR readiness declaration. | PDR readiness declaration | n/a | Open |
| RFA-SRR-004 | RFA Routine (L-4) | Claude | L-4: package-level Minor items not held by a record: Fix each item in its product and have an independent reviewer verify it before the PDR readiness declaration. | PDR readiness declaration | n/a | Open |
| RFA-SRR-005 | RFA Routine (L-5) | Claude | L-5: cross-document items due at PDR: Carry out the action stated in each item before the PDR readiness declaration; the owning reviewer verifies. | PDR readiness declaration | n/a | Open |
| RFA-SRR-006 | RFA Routine (L-6) | Claude | L-6: record liens of the 30 SRR review records: Fix each finding in its product; the reviewer of the owning record verifies it at the record's next iteration, before the PDR readiness declaration. | PDR readiness declaration | n/a | Open |
| RFA-SRR-007 | RFA Routine (L-7) | Claude | L-7: package-level Routine items carried from revision 3: Fix each item in its product or tool; an independent reviewer verifies before the PDR readiness declaration. | PDR readiness declaration | n/a | Open |

TBR liens (review process section 12.2: a TBR lien keeps its `REQ-<MOD>-NNN` id). Owner: Robin decides on Claude's evidence; plan: each requirement's `tbr` object; due: PDR memo; status: Open. They are the requirement part of lien L-1 (RFA-SRR-001 carries the TPM and hazard-control TBRs, which have no requirement id):

- `docs/requirements/sw/sw-keyer/requirements.json` (11): REQ-SW-KEYER-009, REQ-SW-KEYER-014, REQ-SW-KEYER-017, REQ-SW-KEYER-018, REQ-SW-KEYER-020, REQ-SW-KEYER-021, REQ-SW-KEYER-022, REQ-SW-KEYER-026, REQ-SW-KEYER-032, REQ-SW-KEYER-036, REQ-SW-KEYER-039.
- `docs/requirements/sys/requirements.json` (101): REQ-SYS-004, REQ-SYS-008, REQ-SYS-009, REQ-SYS-010, REQ-SYS-011, REQ-SYS-012, REQ-SYS-014, REQ-SYS-015, REQ-SYS-018, REQ-SYS-019, REQ-SYS-020, REQ-SYS-022, REQ-SYS-023, REQ-SYS-024, REQ-SYS-025, REQ-SYS-026, REQ-SYS-027, REQ-SYS-028, REQ-SYS-029, REQ-SYS-030, REQ-SYS-031, REQ-SYS-032, REQ-SYS-033, REQ-SYS-034, REQ-SYS-035, REQ-SYS-036, REQ-SYS-037, REQ-SYS-044, REQ-SYS-048, REQ-SYS-049, REQ-SYS-052, REQ-SYS-053, REQ-SYS-054, REQ-SYS-055, REQ-SYS-058, REQ-SYS-059, REQ-SYS-061, REQ-SYS-062, REQ-SYS-064, REQ-SYS-067, REQ-SYS-068, REQ-SYS-069, REQ-SYS-071, REQ-SYS-072, REQ-SYS-073, REQ-SYS-074, REQ-SYS-076, REQ-SYS-078, REQ-SYS-081, REQ-SYS-082, REQ-SYS-083, REQ-SYS-084, REQ-SYS-085, REQ-SYS-086, REQ-SYS-087, REQ-SYS-088, REQ-SYS-089, REQ-SYS-095, REQ-SYS-097, REQ-SYS-098, REQ-SYS-099, REQ-SYS-100, REQ-SYS-102, REQ-SYS-103, REQ-SYS-105, REQ-SYS-106, REQ-SYS-107, REQ-SYS-112, REQ-SYS-113, REQ-SYS-114, REQ-SYS-115, REQ-SYS-116, REQ-SYS-117, REQ-SYS-118, REQ-SYS-131, REQ-SYS-136, REQ-SYS-139, REQ-SYS-141, REQ-SYS-147, REQ-SYS-149, REQ-SYS-151, REQ-SYS-152, REQ-SYS-153, REQ-SYS-154, REQ-SYS-155, REQ-SYS-156, REQ-SYS-158, REQ-SYS-159, REQ-SYS-160, REQ-SYS-161, REQ-SYS-162, REQ-SYS-164, REQ-SYS-165, REQ-SYS-166, REQ-SYS-167, REQ-SYS-168, REQ-SYS-169, REQ-SYS-172, REQ-SYS-176, REQ-SYS-177, REQ-SYS-183.
- `docs/requirements/tx/requirements.json` (14): REQ-TX-002, REQ-TX-003, REQ-TX-004, REQ-TX-005, REQ-TX-006, REQ-TX-008, REQ-TX-009, REQ-TX-010, REQ-TX-011, REQ-TX-012, REQ-TX-013, REQ-TX-014, REQ-TX-015, REQ-TX-016.
- Total: 126 requirement TBR liens (101 L1 and 25 L2, as package section 13 and lien L-1 state).

Package lien map (section 20.1): L-1 is RFA-SRR-001 with the TBR liens above; L-2 is RFA-SRR-002; L-3 is RFA-SRR-003; L-4 is RFA-SRR-004 with RID-SRR-001, 002, 004 to 014; L-5 is RFA-SRR-005; L-6 is RFA-SRR-006; L-7 is RFA-SRR-007. RID-SRR-003 (REQ-SYS-054 after decision 37) is part of the R16 requirement edits.

Checked that none of the items that may never be liens (review process section 12.2) is present: none present. No Major RID and no Blocking RFA is in the log; the SRR traceability report passes (package row S4: 0 violations, 3 warnings); no TBD exists in an item to be baselined (row S5). The five open Major reviewer findings are not liens: they close before the tag (section 9). Each Minor RID's due is the PDR readiness declaration (review process section 10.2).

## 7. Tailoring approved (success criterion C4; App. G Table G-4 s12 "Proposed tailoring is appropriate"; SE HB §3.11.6 approval via the compliance matrix)

The owner's approval "approves the proposed tailoring of section 17" (minutes, Disposition), with the reliefs signed in owner capacities by key decisions K3 (decisions 6, 7, 8) and K2 (decision 9), and the SE deviation by consent decision 4. Every row of package section 17 is approved with its matrix rationale as written.

| Matrix | Row | Disposition | Rationale accepted | Recorded in matrix at commit |
|---|---|---|---|---|
| `rmm.json` | SWE-027 Conditions for COTS, GOTS, MOTS, OSS and reused software | T | yes (decision 6 (RMM approval)) | `ae8abd2` |
| `rmm.json` | SWE-015 Software cost estimate models | T | yes (decision 6 (RMM approval)) | `ae8abd2` |
| `rmm.json` | SWE-151 Cost estimate conditions | T | yes (decision 6 (RMM approval)) | `ae8abd2` |
| `rmm.json` | SWE-174 Submit planning parameters to Center repository | NA | yes (decision 6 (RMM approval)) | `ae8abd2` |
| `rmm.json` | SWE-016 Software schedule | T | yes (decision 6 (RMM approval)) | `ae8abd2` |
| `rmm.json` | SWE-018 Regular schedule reviews | T | yes (decision 6 (RMM approval)) | `ae8abd2` |
| `rmm.json` | SWE-046 Developer-provided schedule | T | yes (decision 6 (RMM approval)) | `ae8abd2` |
| `rmm.json` | SWE-017 Project-specific software training | T | yes (decision 6 (RMM approval)) | `ae8abd2` |
| `rmm.json` | SWE-022 Software assurance, safety and IV&V per NASA-STD-8739.8 | T | yes (decision 8) | `ae8abd2` |
| `rmm.json` | SWE-141 Software IV&V on Category 1 and 2 projects | NA | yes (decision 6 (RMM approval)) | `ae8abd2` |
| `rmm.json` | SWE-131 IV&V Project Execution Plan | NA | yes (decision 6 (RMM approval)) | `ae8abd2` |
| `rmm.json` | SWE-178 IV&V access to artifacts | NA | yes (decision 6 (RMM approval)) | `ae8abd2` |
| `rmm.json` | SWE-179 Respond to IV&V issues and risks | NA | yes (decision 6 (RMM approval)) | `ae8abd2` |
| `rmm.json` | SWE-023 Implement NASA-STD-8739.8 safety-critical requirements | T | yes (decision 8) | `ae8abd2` |
| `rmm.json` | SWE-219 100 percent MC/DC coverage of safety-critical components | T | yes (decisions 6 and 8) | `ae8abd2` |
| `rmm.json` | SWE-032 CMMI-DEV rating of the development organization | NA | yes (decision 6 (RMM approval)) | `ae8abd2` |
| `rmm.json` | SWE-147 Reusability requirements for Government purposes | NA | yes (decision 6 (RMM approval)) | `ae8abd2` |
| `rmm.json` | SWE-148 Contribute reuse candidates to NASA catalog | NA | yes (decision 6 (RMM approval)) | `ae8abd2` |
| `rmm.json` | SWE-156 Software cybersecurity assessment | T | yes (decision 7) | `ae8abd2` |
| `rmm.json` | SWE-154 Cybersecurity risks and mitigations | T | yes (decision 7) | `ae8abd2` |
| `rmm.json` | SWE-157 Protection of communications-capable systems (NASA-STD-1006) | T | yes (decision 7) | `ae8abd2` |
| `rmm.json` | SWE-159 Test cybersecurity mitigations | T | yes (decision 7) | `ae8abd2` |
| `rmm.json` | SWE-210 Requirements for adversarial-action detection data | T | yes (decision 7) | `ae8abd2` |
| `rmm.json` | SWE-143 Software architecture review | T | yes (decision 6 (RMM approval)) | `ae8abd2` |
| `rmm.json` | SWE-211 Test embedded OSS and reused components | T | yes (decision 6) | `ae8abd2` |
| `se-compliance-matrix.json` | SE-24 | NA | yes (tailoring approval (package section 17)) | `b301df2` |
| `se-compliance-matrix.json` | SE-25 | NA | yes (tailoring approval (package section 17)) | `b301df2` |
| `se-compliance-matrix.json` | SE-26 | NA | yes (tailoring approval (package section 17)) | `b301df2` |
| `se-compliance-matrix.json` | SE-27 | NA | yes (tailoring approval (package section 17)) | `b301df2` |
| `se-compliance-matrix.json` | SE-28 | NA | yes (tailoring approval (package section 17)) | `b301df2` |
| `se-compliance-matrix.json` | SE-29 | NA | yes (tailoring approval (package section 17)) | `b301df2` |
| `se-compliance-matrix.json` | SE-30 | NA | yes (tailoring approval (package section 17)) | `b301df2` |
| `se-compliance-matrix.json` | SE-31 | NA | yes (tailoring approval (package section 17)) | `b301df2` |
| `se-compliance-matrix.json` | SE-44 | NA | yes (tailoring approval (package section 17)) | `b301df2` |
| `se-compliance-matrix.json` | SE-51 | T | yes (decision 4) | `b301df2` |
| `se-compliance-matrix.json` | SE-52 | T | yes (decision 4) | `b301df2` |
| `se-compliance-matrix.json` | SE-55 | T | yes (decision 4) | `b301df2` |
| `se-compliance-matrix.json` | SE-56 | T | yes (decision 4) | `b301df2` |

SRR only: the deviation for the reviews not held, SE-55 and SE-56 (DR and DRR; compliance matrix rows T, relief type deviation), with the operations-handbook end-of-life section as substitute practice, and the SE-51 and SE-52 scope relief (ORR combined with SAR), are approved by the owner as Engineering Technical Authority, per SE-06 and review process sections 1 item 3 and 3.5: **approved** (SRR decision 4, adopted with the consent agenda, owner ruling 2026-09-26).

Also approved with the tailoring (package section 17, closing paragraph): the combined-review customizations (MCR into SRR, SDR into PDR, SIR into TRR, ORR and FRR into SAR); the review process section 3.5 App. G customizations; the charter wording items (a) to (c) of decision 10 as a pre-baseline Log change; and, decision 106 being adopted, the 06 section 14.1 customization of `docs/decisions/adr/reconciliation-srr.md` section 7 R-2, to be recorded in the SEMP (R16).

### 7.1 RMM approval (decision 6) and owner capacities (decision 7)

Per `docs/process/03-software-classification-and-rmm.md` section 9 (decision record and owner signature block):

- `rmm.json` content approved at commit `ae8abd2` (100 rows: FC 75, T 17, NA 8; `tools/render_rmm.py --check` on 2026-09-26 prints these counts and lists; `docs/process/rmm.md` is current). The `meta.approval` fields of `rmm.json` (`approved_by`, `approved_on`, memo) and the approval notes in the relieved rows were written in R16 at `9bdf33c` (SWE-126 b); the row dispositions approved are those of `ae8abd2`.
- T rows approved: SWE-027, SWE-015, SWE-151, SWE-016, SWE-018, SWE-046, SWE-017, SWE-022, SWE-023, SWE-219, SWE-156, SWE-154, SWE-157, SWE-159, SWE-210, SWE-143, SWE-211.
- NA rows approved: SWE-174, SWE-141, SWE-131, SWE-178, SWE-179, SWE-032, SWE-147, SWE-148.
- Rows approved with liens: RID-SRR-012 (RMM `meta` NPR 8705.2 note) and RID-SRR-013 (row SWE-071 citation); RFA-SRR-006 carries the record lien against the RMM (INSP-030 finding-2, RMM owner).
- Reliefs of decision 6: SWE-211 (Rust `core` tested at feature level, no structural coverage) and SWE-219 (independently reviewed MC/DC independence-pair tables, stable region coverage, nightly branch and condition coverage MSR-14 as required non-credit evidence); RSK-010 carries the SWE-219 residual.

Each approval line of the 03 section 9 signature block, transcribed from the owner's actual wording. The owner's words are the two statements of the minutes; no capacity-specific wording was given, so each line quotes the statement that carries it.

| Approval (03 section 9) | Owner wording, verbatim | Date |
|---|---|---|
| RMM approval as ETA and SMA TA (decision 6: approve both reliefs; RSK-010 carries the SWE-219 residual) | "I concur with your recommendations for the key decisions." | 2026-09-26 |
| Relief for SWE-154, 156, 157, 159 and 210, as CIO/SAISO designee (decision 7) | "I concur with your recommendations for the key decisions." | 2026-09-26 |
| Health and medical implications of the SWE-022, SWE-023 and SWE-219 tailoring, reviewed as HMTA (decision 8) | "I concur with your recommendations for the key decisions." | 2026-09-26 |
| Human safety risk of the SWE-022, SWE-023 and SWE-219 tailoring, accepted as the risk taker (decision 8: accept, with RSK-010 and the hazard analysis as the record) | "I concur with your recommendations for the key decisions." | 2026-09-26 |
| Same risk accepted as official spokesperson for bystanders and household members (03 section 4.4; each other operator signs in the as-built record before hand-over) | Not given as a separate statement: decision 8 names the HMTA and risk-taker lines only. The approved `rmm.json` content (decision 6) states this acceptance in the residual risk of rows SWE-022, SWE-023 and SWE-219, but 03 section 9 asks for its own line; it stays empty until the owner states it (owner action) | |
| Classification and safety-critical determination (03 sections 3 and 4), approved as SMA TA with independent concurrence INSP-009 (`docs/reviews/SRR/checklists/classification-03-software-classification-and-rmm.md`) and INSP-017 (`docs/reviews/SRR/checklists/classification-03-software-classification-and-rmm-software-assurance.md`), checklist `docs/templates/peer-review-checklist-classification.md` (decision 9: concur, with frequency control safety-critical and the menu override command path safety-critical as 03 proposes) | "I concur with your recommendations for the key decisions." | 2026-09-26 |

Owner capacities (decision 7, ruled as recommended): the Health and Medical Technical Authority and CIO/SAISO designee capacities are added to the owner's roles in charter section 2. The charter section 2 edit follows as R16 work, with the decision 10 wording items.

## 8. Decisions taken at the review

All rulings below were given on 2026-09-26 and are transcribed by decision number. The ruling text of each is the "Recommendation" cell of its row in `decisions-for-owner.md` at `5ebe90c`, copied verbatim. Where a cell carries a dated "Status" note (decisions 105, 106), the note is the pre-ruling status and not part of the ruling. Items whose "Needed by" names a later gate (consent preamble item (d)) are confirmed now as the plan and ruled finally at that gate.

### 8.0 Key decisions K1 to K17 (owner statement: "I concur with your recommendations for the key decisions.")

| Decision | Key | Title | Ruling (Recommendation cell, verbatim) | Needed by |
|---|---|---|---|---|
| 36 | K1 | Tune carrier and hardware cutoff window (joint) | Option a with the 74LVC1G123 and a capacitor chosen from its DC-bias curve (R-KN1). | SRR memo |
| 37 | K1 | Firmware stuck-key limits | 5 s manual timeout including the Bug dah; the HZ-004 K4 no-gap watchdog with the 2 s squeeze limit, because it also bounds a toggling stream. | SRR memo |
| 41 | K1 | Bench test-mode guard | Adopt. | SRR memo |
| 42 | K1 | Mode classes, PRACTICE flag and bench-test limits (ConOps section 3.4, Table 3.4-4 and appendix C) | (a), ruled after decisions 37 and 41. Reason: the HZ-004 K13 TBR sizes the timeout from the longest bench measurement a test mode must support (element timing at 5 WPM, about 60 s), so a 60 s cap leaves no margin, while 120 s stays below the 150 s to 180 s backstop of decision 38. | SRR memo |
| 38 | K2 | Transmission-length hardware backstop | Adopt with the 150 s to 180 s window. | SRR memo |
| 39 | K2 | Hardware over-temperature cutoff | Adopt with 95 C +/-3 C and 100 ms. | SRR memo |
| 40 | K2 | Independent frequency verification before transmit | Adopt with the 10 kHz window and 100 ms. | SRR memo |
| 9 | K2 | Software classification and safety-critical determination, including frequency control | Concur, with frequency control safety-critical (it removes single point failure row 4) and the override command path safety-critical as 03 proposes. | SRR memo |
| 33 | K2 | Exposure accumulator classification | Convenience function. | SRR memo |
| 6 | K3 | RMM approval with the SWE-211 and SWE-219 reliefs | Approve both reliefs; RSK-010 carries the SWE-219 residual. | SRR memo |
| 7 | K3 | Cybersecurity relief and owner capacities | Approve both. | SRR memo |
| 8 | K3 | Health and medical review and risk acceptance of the SWE-022, SWE-023, SWE-219 tailoring | Accept, with RSK-010 and the hazard analysis as the record. | SRR memo |
| 14 | K4 | Red risk plans and RSK-009 | Approve all 32 plans; RSK-009 closes on its closure criteria (target PDR). | SRR memo |
| 11 | K4 | Hardware TRL 3 at procurement release | Accept at SRR and reconfirm in the CDR memo. | SRR memo; reconfirmed at CDR |
| 32 | K4 | SAR evidence by analogy | Accept the analogy; no FDTD estimate in revision A. | SRR memo |
| 3 | K4 | No independent human Technical Authority | Accept as stated in SEMP section 4.1. | SRR memo |
| 17 | K5 | Operator model and ADR-015 | OPS-A default, OPS-B only by a dated record; accept ADR-015. | SRR memo |
| 18 | K5 | OPS-B exposure tier | Keep the 1 W limit for OPS-B until a dated owner record confirms the controlled-environment basis; cite OET 65 Supplement B in ADR-014. | SRR memo |
| 19 | K5 | Receive-only guest lock and its release | Include, option a. | SRR memo |
| 20 | K5 | Guest keying at all | Allow, restricted to 0.5 W and 1 W with the control operator present. | SRR memo |
| 63 | K6 | Headphones only | Headphones only. | SRR memo |
| 64 | K6 | Audio level policy | (a). | SRR memo |
| 70 | K7 | Charger IC | BQ25887. | SRR memo |
| 72 | K7 | Pack protection topology | S-8252 plus BQ29209; add both requirements. | SRR memo |
| 73 | K7 | Cell holders | Two 1043P. | SRR memo |
| 74 | K7 | 5 V bus and power switch | Synchronous buck with SYNC; mechanical switch. | SRR memo |
| 75 | K7 | Operation while charging | Receive allowed, charge paused, hardware transmit inhibit; record by ADR. | SRR memo |
| 76 | K7 | Battery-life floor at 1:4 and low-battery limits | Adopt. | SRR memo |
| 85 | K7 | Environment set | Adopt (TBR); RSK-059 carries the absence of qualification testing. | SRR memo |
| 53 | K8 | Receiver architecture family | Confirm the single-conversion superhet. | SRR memo |
| 54 | K8 | CW selectivity candidates and the TBR set | As TS-001 section 8.4: carry both with A as the planning baseline; A's eligibility against the REQ-SYS-024 lower limit depends on the Inrad tolerance quote (decision 101). | SRR memo; TS-001 closes at PDR |
| 55 | K8 | Front-end current budget | Lower-current stage (TS-001 section 8.4): a 7 dB system NF already meets REQ-SYS-022, and in the F23 model the 97 mA MMIC moves the 1:9 life of the low build from 13.0 h to 10.4 h (TPM-002 red, RSK-058). The PDR cascade budget confirms it. | SRR memo (interim direction); PDR (budget) |
| 58 | K8 | PA device, fallback and drop list | As TS-001 section 8.4: P1 primary; P3 then P4 as the fallback; GRF5604 returns only with a REQ-SYS-112 CR or vendor dissipation data; send the Guerrilla RF request anyway (decision 101). The device choice becomes an L2 TX constraint requirement traced to SI-028 at PDR. | SRR memo; TS-003 at PDR |
| 107 | K9 | Firmware runtime and HAL (TS-002, SWE-033) | Approve A0 with the four revisit triggers of TS-002 section 8. | SRR memo |
| 110 | K9 | rustos licence and manifest work item | MIT, matching the cwht licence (SI-025, ADR-017), and approve the manifest work item. | SRR (before the FW-B0 re-run) |
| 108 | K10 | CR-001: driver-construction failure arms and the panic handler | Approve. | SRR memo (before FW-B1) |
| 109 | K10 | Toolchain downloads for the software gate | Approve the four installs; the optional crate download is not needed for the ranking (TS-002 is robust). | SRR (before the FW-B0 re-run) |
| 105 | K11 | R-1: route for correcting the 21 Accepted ADRs of the register's scope | (A): one self-contained file per decision at the functional baseline, no decision content changed. **Status 2026-09-26:** ruled option (A) by the lead SE and applied: the 22 Accepted ADR files carry the corrections in a dated section 8 change log (decision sections untouched), `reconciliation-srr.md` is marked superseded by the ADR files, and the allowance sentence is in 05 Table 4-1 row 13. The owner approves or reverses the ruling in the SRR decision memo; INSP-011 iteration 3 verified F-02 and F-03 Closed on the committed ADR blobs, conditional on this ruling not being reversed, and recorded the ADR-001 to ADR-025 correction residuals as liens (F-12 is noted with this decision). | SRR memo |
| 106 | K11 | R-2: class 1 choices recorded without a trade study | Adopt (i) and (ii). **Status 2026-09-26:** open for the owner's ruling (not ruled by the lead SE). | SRR memo |
| 111 | K11 | ADR-024 identification-memory clause against REQ-SYS-007 | With decision 21 ruled 'not in revision A', record in the ADR correction of decision 105 that the ADR-024 clause constrains any future memory only and creates no revision A requirement. | SRR memo |
| 30 | K12 | Method for regulatory requirements not closed by Test | Accept for all ten; REQ-SYS-015 moves to Test by CR if the tinySA TV record shows an adequate RBW; REQ-SYS-122 moves to Inspection if decision 113 is approved. | SRR memo |
| 113 | K12 | Inspection for documentary requirements (CR to 04 rule 7.3.6) | Approve the CR; Claude writes it and the four method changes. | SRR memo |
| 29 | K12 | Harmonic design target and filter goals (ADR-022), with owner choice V-5 | Adopt; accept ADR-022 with the HZ-008 link (OQ-SAF-021). V-5: options a and c, because 47 CFR 97.307(e) applies at the antenna port, TC-TX-009 to TC-TX-011 measure from the filter test point to the antenna port, and the third band covers the 7f aeronautical band of HZ-008; the ADR-022 section 2 text is then corrected by the route of decision 105. | SRR memo |
| 25 | K12 | Frequency reference and band-edge guard versus keying sidebands (ADR-023; the guard-versus-sideband item named in the REQ-SYS-008 rationale) | (a): a 1.2 kHz guard with the +/-2.5 ppm reference; accept ADR-023 with its section 2 item (2) revised to the 1.2 kHz guard before acceptance; the authors then change REQ-SYS-008, REQ-SYS-009 and REQ-TX-002 to 144.0012 to 147.9988 MHz (TBR) and the guard wording of the REQ-SYS-008, REQ-SYS-010 and REQ-TX-006 rationales (item R16). Reason: it gives up only 200 Hz more per edge than revision 4, needs no change of reference grade and keeps the -60 dB design level in band; (b) puts the margin into a tolerance the bench cannot measure, (c) gives up the in-band claim for the keying sidebands, (d) gives up 2 kHz per edge. | SRR memo; error budget and TS-006 confirm at PDR |
| 90 | K13 | Unit cost budget | USD 610 per unit; the instrument line is already outside the unit budget (SEMP F-13 resolved 2026-09-26). | SRR memo |
| 86 | K13 | Build quantity | Confirm now: five fabricated; three assembled as the planning value, up to five decided at CDR against the quote. | SRR memo (confirmation); CDR (assembled count) |
| 104 | K14 | Readiness of entrance row 25 and SWE-050 on the Draft L2 files | Yes: close row 25 and H15 on the Draft files; INSP-004 is re-issued APPROVED at `5f647f2` (delta verification of SW-KEYER `4d22b399` and `d3c0c236`, readiness R3 met, `paired_record: INSP-026`); option (b) lapses. | SRR memo (readiness confirmation) |
| 112 | K14 | Self-derived SW-KEYER requirements | Concur with all five. | SRR memo |
| 114 | K15 | Accreditation of the SRR tool validation records | Accredit each record as proposed (INSP-015 APPROVED). | SRR memo |
| 47 | K16 | Semi break-in hang and lead-in (ADR-026, superseding ADR-010) | Adopt as written and accept ADR-026; Claude then sets ADR-010 Status to 'Superseded by ADR-026' and ConOps section 3 follows by the routed items. | SRR memo |
| 115 | K17 | Readiness waivers: author self-checks and the FW-B0 design-unit row | (a) No waiver: done, the self-checks exist (package item R7). (b) Waive INSP-016 R3 for FW-B0 only, recorded in the SRR memo. | (a) Before the readiness declaration; (b) SRR memo |
| 118 | K17 | Software assurance coverage of the CM plan 05 (07 section 22 row 'Assurance routing of 05 and TS-002') | (a), done; no coverage ruling is needed. | Before the readiness declaration |

### 8.0.1 Consent agenda (package section 13.1.2; adopted with the approval "I approve of this and the SRR.")

Each row is "adopted with the consent agenda" (decisions-for-owner.md part 6). No item was excepted.

| Decision | Theme | Title | Ruling (Recommendation cell, verbatim) | Needed by |
|---|---|---|---|---|
| 1 | A | Approve the plans for the functional baseline | Adopted with the consent agenda: Approve each plan when its `INSP-NNN` record is APPROVED with no open Major finding (05 Table 4-2): the SEMP (INSP-005), 03 (INSP-009 with INSP-017), 06 (INSP-007), 05 (INSP-006, paired with INSP-030), 07 (INSP-010 with INSP-018), 01 (INSP-019), 02 (INSP-020), 04 (INSP-021) and 08 (INSP-022) are APPROVED with liens after the re-issues of 2026-09-26 (package revision 6); the 05 assurance record INSP-030 has assurance verdict APPROVED and its record verdict APPROVED since its re-issue at `99ecccb` (package item R19 (b)). The charter is approved by name and commit (05 Table 4-2 row 1). | SRR memo |
| 2 | A | HSI documented as a SEMP section | Adopted with the consent agenda: Confirm; add the section 7.3.1 rationale to the charter row. | SRR memo |
| 4 | A | Deviation for reviews not held and scope relief | Adopted with the consent agenda: Approve. | SRR memo |
| 10 | A | Charter wording issues carried from the process documents | Adopted with the consent agenda: Approve (a) to (c). | Before the SRR readiness declaration |
| 13 | A | Technology assessment method and finding | Adopted with the consent agenda: Accept; rename the column DML-n as SEMP F-07 asks. | SRR memo |
| 15 | A | Repository protection and signing | Adopted with the consent agenda: Protection before baseline/srr; signing before baseline/pdr. | SRR (protection); PDR (signing) |
| 16 | A | Configuration management choices due later | Adopted with the consent agenda: Path dependency with the commit recorded in the lock; commit binaries directly; owner's choice of archive. | PDR, CDR, SAR as listed |
| 21 | B | Automatic identification, message memories and WinKeyer interface | Adopted with the consent agenda: Not in revision A; keep the identification reminder only. | SRR memo |
| 22 | B | Power steps | Adopted with the consent agenda: Adopt. | SRR memo |
| 23 | B | Default step and deliberate 5 W selection | Adopted with the consent agenda: 1 W default with a confirmation press for 5 W. | SRR memo |
| 24 | B | Maximum output and tolerance | Adopted with the consent agenda: 5.0 W nominal, +/-1 dB requirement, ALC target +/-0.5 dB; the 97.307(e) evaluation is made at the ceiling. | SRR memo; ALC confirmed at PDR (TS-006) |
| 26 | B | Transmit range policy and presets | Adopted with the consent agenda: Full band without a lock; presets 144.050 and 144.100 MHz with the CW-only segment highlighted. | SRR memo |
| 27 | B | Declared necessary bandwidth | Adopted with the consent agenda: 208HA1A, with the measured 26 dB bandwidth of at most 350 Hz binding. | SRR memo |
| 28 | B | Keying envelope convention | Adopted with the consent agenda: REQ-SYS-014 as written (5 ms 10-to-90 percent, 3 to 8 ms), because the 26 dB bandwidth limit binds either way and the slower ramp adds margin. | SRR memo |
| 31 | B | Exposure posture | Adopted with the consent agenda: Adopt. | SRR memo |
| 34 | B | Enclosure legend | Adopted with the consent agenda: Engrave. | SRR memo |
| 35 | B | Regulatory corpus gaps | Adopted with the consent agenda: Do all three before PDR. | PDR |
| 43 | D | Keyer modes and default | Adopted with the consent agenda: All five, Iambic A default. | SRR memo |
| 44 | D | Key-type selection and mono plugs | Adopted with the consent agenda: Menu only in revision A. | SRR memo |
| 45 | D | Speed default and speed control | Adopted with the consent agenda: 15 WPM; press-and-turn with the WPM on the display; no Morse announcement. | SRR memo |
| 46 | D | Sidetone default | Adopted with the consent agenda: 600 Hz, locked, relative level. | SRR memo |
| 48 | D | Timing tunables in the menu | Adopted with the consent agenda: Expose the switchpoint and the debounce only; keep the others as build-time defaults (fewer knobs under Class A rigor). | SRR memo |
| 49 | D | Key input abuse and ESD targets | Adopted with the consent agenda: Adopt; no +24 V line. | SRR memo |
| 50 | D | Keyer timing, thresholds and latencies | Adopted with the consent agenda: Ratify; the debounce closes by the bench capture before PDR. | SRR memo |
| 51 | D | Physical disambiguation of the two jacks | Adopted with the consent agenda: Separate positions plus engraved marking. | PDR (ICD-CTL-ME) |
| 52 | D | Input sampling mechanism | Adopted with the consent agenda: 1 kHz TIMER0 polling; edge interrupts only if the bench shows more than 1 ms latency. | SRR memo |
| 56 | E | Synthesizer trade parameters and allocation | Adopted with the consent agenda: Confirm all three. | SRR memo |
| 57 | E | Receive range and receiver overload survival | Adopted with the consent agenda: As written: 144.010 MHz start and +27 dBm with a limiter. | SRR memo |
| 59 | F | ALC and envelope topology | Adopted with the consent agenda: Gate-bias loop from the pack; cutoff node a TS-006 criterion (R-KN5). | PDR (TS-006) |
| 60 | F | SWR fold-back | Adopted with the consent agenda: Decide at PDR once the device and its ruggedness figure are known. | PDR |
| 61 | F | T/R element, LPF position and receiver protection | Adopted with the consent agenda: Relay, LPF after the T/R node, second protection stage per the fault analysis. | SRR memo; part choice at PDR |
| 62 | F | Transmit fault responses, mismatch bounds and test access | Adopted with the consent agenda: Ratify. | SRR memo |
| 65 | G | Audio source | Adopted with the consent agenda: PWM with the DNP footprint. | SRR memo |
| 66 | G | No-headphones behaviour and mono plugs | Adopted with the consent agenda: Shutdown with indicator, keyer live; accept TS plugs under protection pending the short-circuit analysis (RSK-039 S1). | SRR memo |
| 67 | G | Dose accumulator | Adopted with the consent agenda: Cap and unlock only in revision A. | SRR memo |
| 68 | G | Headphone amplifier family | Adopted with the consent agenda: TPA6132A2 unless the charge-pump comb fails the receiver noise test (RSK-040). | PDR |
| 69 | G | Audio mute, restore and lead pickup values | Adopted with the consent agenda: Ratify. | SRR memo |
| 71 | H | USB input policy | Adopted with the consent agenda: 500 mA default; DCP detection only after TS-005 qualifies the VBUS path; accept the deviation with a handbook note. | SRR memo; TS-005 at PDR |
| 77 | I | Display and light | Adopted with the consent agenda: LS013B7DH03, no light in build 1. | SRR memo |
| 78 | I | Encoders, buttons, knobs and jacks | Adopted with the consent agenda: Adopt all. | SRR memo |
| 79 | I | Operator interface values | Adopted with the consent agenda: Ratify. | SRR memo |
| 80 | J | Antenna connector | Adopted with the consent agenda: SMA jack. | SRR memo |
| 81 | J | Reference antennas and radiated screen | Adopted with the consent agenda: Adopt; correct docs/design/concept.md section 7.1, which calls the Signal Stick a half-wave. | SRR memo |
| 82 | J | Terrain modelling for the range MOEs | Adopted with the consent agenda: Install before PDR. | PDR |
| 83 | J | Enclosure alloy and finish | Adopted with the consent agenda: Adopt. | SRR memo |
| 84 | J | CAD tool build and fit-check prints | Adopted with the consent agenda: Stay on 2021.01; H2C prints; SLA print only if needed. | PDR |
| 87 | K | Board thickness, laminate, via fill and panelization | Adopted with the consent agenda: 1.0 mm if the enclosure gives four bosses, else 1.6 mm with 35 um plating; FR-4; Type VII; decide panelization with the enclosure at PDR; KiCad names. | PDR (TS-004) |
| 88 | K | Sourcing mode and single-side placement | Adopted with the consent agenda: Full turnkey; single-side placement as an L2 requirement at PDR. | SRR memo |
| 89 | K | Functional test at PCBWay | Adopted with the consent agenda: Owner's bench at TRR (receipt inspection and staged bring-up). | CDR |
| 91 | K | Early buys | Adopted with the consent agenda: Approve at PDR by ADR once the trades select the parts. | PDR |
| 92 | L | Emulator selection and accreditation | Adopted with the consent agenda: Adopt all, recorded by the PDR emulator ADR. | PDR (ADR) |
| 93 | L | Firmware design rules | Adopted with the consent agenda: Adopt the rules by ADR; register-access trait decided at PDR. | SRR memo (rules); PDR (trait) |
| 94 | L | Analysis and quality tools | Adopted with the consent agenda: Adopt and approve the installs. | PDR |
| 95 | L | Secure boot | Adopted with the consent agenda: Decide at PDR with RSK-015 and RSK-022. | PDR |
| 96 | M | Pocket-carry MOE | Adopted with the consent agenda: Add and re-parent. | SRR memo |
| 97 | M | Mass and envelope allocations | Adopted with the consent agenda: Adopt as TBR; bottom-up estimates by PDR. | SRR memo (or PDR at the latest) |
| 98 | M | Power allocation and TPM set | Adopted with the consent agenda: Approve with the PDR TPM definitions (SE-40). | PDR |
| 99 | N | Instruments and fixtures | Adopted with the consent agenda: Confirm or buy before PDR; tinySA and attenuator before TRR. | PDR; TRR |
| 100 | N | Hand-assembly bench equipment | Adopted with the consent agenda: Station with auto-sleep and stand, extractor, alloy of the owner's choice recorded in the handbook. | CDR |
| 101 | N | Vendor and supplier correspondence | Adopted with the consent agenda: Do all before PDR (answers due in the CDR package). | PDR |
| 102 | N | Owner bench experiments and stock checks | Adopted with the consent agenda: Do before PDR. | PDR |
| 103 | O | Stakeholder identifier scheme (CI-10) | Adopted with the consent agenda: Keep the name keys. | Before the SRR readiness declaration |
| 116 | P | Re-dating SRR hazard questions whose remaining step is an author edit | Adopted with the consent agenda: Do not re-date: the hazard analysis author closes OQ-SAF-017 and 020 in the file now; the ConOps author edits OPS-013 after the rulings; re-date OQ-SAF-006 to PDR only if that edit misses the declaration. **Status 2026-09-26:** done for OQ-SAF-017 and OQ-SAF-020, both Closed in `hazards.json` 0.4.1-pha without re-dating (the edits were in the products before the readiness declaration); only OQ-SAF-006 remains subject to the re-dating fallback. | Before the readiness declaration |
| 117 | P | Checklist for tool validation records | Adopted with the consent agenda: Accept INSP-015's item set for SRR; Claude writes `docs/templates/peer-review-checklist-tool-validation.md` before the PDR TV set. | SRR memo (method); PDR (template) |

Decisions that need no ruling: 5 (withdrawn) and 12 (done), per decisions-for-owner.md part 3.

### 8.1 Decision 30: the 06 section 14.1 item (g) record for the ten regulatory requirements

This subsection is the class 1 decision record that `docs/process/06-risk-and-decision-analysis.md` section 14.1 item (g) requires for a verification approach that substitutes another method for Test on a regulatory requirement (02 section 4.4), for every non-retired `regulatory` requirement whose method is not Test. Owner ruling 2026-09-26 (key decision K12, as recommended): "Accept for all ten; REQ-SYS-015 moves to Test by CR if the tinySA TV record shows an adequate RBW; REQ-SYS-122 moves to Inspection if decision 113 is approved."

| Requirement | Method accepted | Basis |
|---|---|---|
| REQ-SYS-001 | Inspection | No credited instrument of 04 section 6.1 resolves it (04 section 6.2) |
| REQ-SYS-125 | Inspection | Same |
| REQ-TX-001 | Inspection | Same |
| REQ-SYS-014 | Analysis | Same |
| REQ-SYS-015 | Analysis; moves to Test by CR if the tinySA Ultra TV record shows an adequate resolution bandwidth (ACTION-9, before PDR) | Same; RSK-011 records the residual if Analysis stands |
| REQ-SYS-121 | Analysis | Same; SAR by analogy accepted by decision 32 |
| REQ-SYS-122 | Analysis; moves to Inspection because decision 113 is approved (the CR to 04 rule 7.3.6) | Same |
| REQ-SYS-177 | Analysis | Same |
| REQ-TX-005 | Analysis | Same |
| REQ-TX-006 | Analysis | Same |

Consequences: INSP-003 finding-6 (Major) closes on this record when the INSP-003 reviewer verifies it (R16); each of the ten rationales drops its "owner decision pending at SRR" wording in the baseline change (decisions-for-owner.md part 6).

### 8.2 Decision 115 (b): readiness waiver for the FW-B0 record

Owner ruling 2026-09-26 (key decision K17, as recommended): "(b) Waive INSP-016 R3 for FW-B0 only, recorded in the SRR memo." The waiver: INSP-016 readiness condition R3 ("the design unit is Active and named in `// @design`") is waived for the FW-B0 product only, because it cannot be met before the CDR software design (07 section 3.1). The waiver does not extend to any later build (FW-B1 onward) or to any other record. INSP-016 can reach APPROVED once F-01 and F-02 close (R16 (a) and decision 108). Part (a) grants no waiver: the 16 author self-checks exist (package item R7). Decision 118 needs no ruling: route (a) is done (INSP-030).

### 8.3 TBRs closed by this memo

The 14 L1 TBRs with close_by SRR close with their values as written, each ratified by the decision named (package section 13): REQ-SYS-042, 043 and 047 (decision 50); REQ-SYS-045 (decision 46); REQ-SYS-050 (decision 49); REQ-SYS-057 (decision 79); REQ-SYS-090 (decision 71); REQ-SYS-104 (decision 80); REQ-SYS-157 and 173 (decision 69); REQ-SYS-171 (decision 33); REQ-SYS-180, 150 s to 180 s (decision 38); REQ-SYS-181, 95 C +/-3 C and 100 ms (decision 39); REQ-SYS-182, 10 kHz and 100 ms (decision 40). The requirements authors remove each `tbr` object and the "pending" rationale wording in the baseline change (R16). TPM-014 closes at USD 610 per unit (decision 90).

### 8.4 Records the rulings create or change (charter section 11 rule 6)

| Decision | Record | Constrains |
|---|---|---|
| 17 (accept ADR-015), 29 (accept ADR-022 with the HZ-008 link; V-5 options a and c), 25 (option (a): accept ADR-023 with section 2 item (2) revised to the 1.2 kHz guard), 47 (accept ADR-026) | ADR-015, ADR-022, ADR-023, ADR-026 move from Proposed to Accepted; ADR-010 Status reads "Superseded by ADR-026" | Operator model, harmonic target, band-edge guard, semi break-in hang (L1, L2, PDR) |
| 25 (option (a)) | REQ-SYS-008, REQ-SYS-009, REQ-TX-002 to 144.0012 to 147.9988 MHz (TBR); guard wording of the REQ-SYS-008, REQ-SYS-010, REQ-TX-006 rationales (R16) | Transmit range; TS-006 and the error budget confirm at PDR |
| 105, 106, 111 | ADR correction route (A) confirmed; the 06 section 14.1 customization (i) and (ii) recorded in the SEMP; the ADR-024 clause recorded in the ADR correction | ADR register; INSP-011 F-01, F-02, F-03 |
| 107 | ADR-027 records the firmware runtime and HAL choice A0 with the TS-002 section 8 revisit triggers (SWE-033) | Firmware platform (PDR) |
| 108 | CR-001 approved: its disposition block is filled from this ruling | `firmware/cwht-app/src/main.rs`; INSP-016 finding-2 |
| 109, 110 | Four toolchain installs approved; rustos licence MIT and the manifest work item approved | R16 (a): lock sanity checks, `tools/sw_gate.sh`, the TC-SW-TOOL-001 close-out run (run 4 in the minutes), INSP-016 iteration 4 |
| 113 | CR-002 to 04 rule 7.3.6 (Inspection for documentary requirements; `docs/cm/cr/CR-002-inspection-for-documentary-requirements.md`) and the method changes of REQ-SYS-122, 124, 137, 138, written by Claude | V&V methods |
| 114 | TV-001 to TV-010 accredited as proposed; each record's section 9 accreditation decision is recorded (OA-7) | Credited standing of the tool runs behind rows S4, 8, 24 |
| 36, 37, 41, 42, 38 | New ADR for the stuck-key control set; REQ-SYS-054 edit (RID-SRR-003); ConOps section 3.4 and appendix C aligned to the 120 s bench-test limit (decision 42 (a)) | Keying safety (HZ-001, HZ-004, HZ-006) |
| 64, 70, 72 to 76, 93 | New ADRs for the audio level policy, the power-tree baseline, operation while charging, and the firmware design rules | Audio, power, firmware (PDR) |
| 14 | `mitigation.plan_approval` of the 32 Red risks names this memo and date | Risk register; `tools/render_risk.py --gate PDR` |
| 1 | The plans for the functional baseline approved (SEMP, 01 to 08, the charter by name and commit; 05 Table 4-2) | Functional baseline content |
| 15 | Repository protection configured before `baseline/srr`; tag signing before `baseline/pdr` | Baseline procedure |

Residual risks accepted by the owner: RSK-008 (hardware TRL 3 at the CDR procurement release, decision 11; reconfirmed in the CDR memo), RSK-030 (SAR evidence by analogy, no FDTD estimate in revision A, decision 32), RSK-010 (SWE-219 residual, decisions 6 and 8), the residual that independent assessment is by reviewer agents only (SEMP section 4.1, decision 3), and the 32 Red risks under their approved mitigation plans (decision 14; RSK-009 closes on its own criteria, target PDR).

## 9. Disposition

**Approved with liens**

Liens: L-1 to L-7 of package section 20.1, logged and listed in section 6.

Conditions attached (the owner's sequencing, minutes "Disposition"):

1. The post-ruling work R16 (package section 2.1) is performed next: (a) after decisions 109 and 110, the toolchain installs, the lock sanity checks, the rustos SAFETY-comment work item, `tools/sw_gate.sh` exit 0, the TC-SW-TOOL-001 close-out run (run 4 in the minutes, with the OA-1 and OA-2 outputs) and INSP-016 iteration 4; (b) after the other rulings, the requirement edits, ConOps edits, ADR status edits and rationale edits the rulings require (sections 8.1 to 8.4).
2. The reviewers verify R16. The five open Major findings (INSP-003 finding-6; INSP-011 F-01 and F-04; INSP-016 F-01 and F-02) are closed and the Hard entrance rows of section 3 are Met before the tag. None of them is a lien.
3. `baseline/srr` is created only after that verification, so that the functional baseline carries the rulings (section 10). Decision 15 applies: repository protection is in place before the tag.
4. OA-1 and OA-2 (the FW-B0 flash and observe on the bare Pico 2, and the picotool verify known answer), first recorded as deferred to PDR, were performed in the same session after the owner reversed the deferral, all Pass (section 3). The TC-SW-TOOL-001 run 4 report files the raw outputs and INSP-016 re-verifies them in R16; no deferral or tailoring of row 20 stands.
5. The traceability approach presented at the session is approved, including the requirement field on the safety-critical hardware parts (the hardware transmit timer, the cell protection ICs and the headphone limiter), added at PDR (minutes, "Traceability approach" and "Disposition").

## 10. Baseline

| Field | Value |
|---|---|
| Baseline | Functional |
| Tag | `baseline/srr`. It is created on the baseline-record commit R that follows the R16 verification and this memo's commit (`docs/process/05-configuration-and-data-management.md` section 4.4 steps 3 and 5), so this memo does not carry the tagged commit hash. The tagged commit, the tag object and the pushed hash are recorded in `docs/reviews/SRR/baseline-record.md`. The front-matter key `baseline_tag` is set by amendment (section 13) when the tag exists |
| Baseline record | `docs/reviews/SRR/baseline-record.md` (template `docs/templates/baseline-record.md`), not yet written |
| Items now under change control | From the tag: the functional baseline of charter section 3 (`docs/requirements/l0-stakeholder/expectations.json` NGOs and MOEs, `docs/conops/conops.md`, `docs/requirements/sys/requirements.json`, `docs/plan/semp.md` with the charter as its core) and the plans approved by decision 1 as 05 Table 4-2 lists them; the complete CI list with hashes is the baseline record's. After the tag, changes go through `CR-NNN` (charter section 7) |

## 11. Dissent (§5.2.3.1 f)

None.

## 12. Approval (§5.2.3.1 i)

Owner statements, transcribed verbatim from the conversation (minutes, 2026-09-26):

> "I concur with your recommendations for the key decisions." - Robin, 2026-09-26 (the minutes record the date, not the time).

> "I approve of this and the SRR." - Robin, 2026-09-26 (the minutes record the date, not the time).

The commit that fills this section sets the front-matter keys `signed` (2026-09-26) and `disposition` (*Approved with liens*). The signature of the Decision Authority is this transcription plus that commit; no other signature exists.

This file cannot state its own commit hash. For SRR the memo commit is recorded in the section 1 "Decision memo" row of `docs/reviews/SRR/baseline-record.md` (`memo commit <hash>`) and in the tag message (`cwht functional baseline; decision memo docs/reviews/SRR/decision-memo.md at <memo commit>`), per `docs/process/05-configuration-and-data-management.md` section 4.4 steps 2 and 5.

Review complete per §5.2.3.1 items a to i: items a to h yes; item i yes for the signature, with the baseline procedure of 05 section 4.4 held until the R16 verification (section 9). Follow-up controls (item h): the open items appear in the PDR package burndown and in the review-trend TPM-003 (`tools/review_trend.py --date 2026-09-26 --package SRR --write`, `docs/reviews/SRR/figures/review-trend.png`).

## 13. Amendments

| Date | Item | Change | Rationale | Owner wording | Commit trailer |
|---|---|---|---|---|---|
| 2026-09-26 | A-1: section 8.2 | <a id="W1"></a>The decision 115 (b) waiver of section 8.2 is numbered **W1** and is cited as `docs/reviews/SRR/decision-memo.md#W1` (07 section 10.2; baseline record section 3; INSP-016 readiness R3 for FW-B0 only). The waiver text is unchanged | A baseline record cites each waiver by a numbered id (template section 3); the cross item of the R16 apply stage asked for the numbering | none: transcription of the existing ruling, SRR decision 115 (b) (owner ruling 2026-09-26) | Refs: SRR |
| 2026-09-26 | A-2: sections 6 and 8.3 | REQ-SYS-180, 181 and 182 keep their `tbr` objects with `close_by: PDR` and a PDR confirmation plan (applied at `cd61450`, APPROVED by INSP-003 at `401b01d`), although section 8.3 lists them as closed by this memo; they are carried as TBR liens to PDR with their ruled values (decisions 38, 39 and 40). R16 also added REQ-SYS-184, 185, 186, 188 and 189 with TBRs `close_by: PDR` (decisions 37, 41 and 42). The L1 TBR lien count of section 6 becomes 109 (101 + 8) and the total 134 (109 L1, 25 L2) | Keeps the lien list equal to the requirement files (baseline record section 5) | none: the values are the ruled ones; only the TBR bookkeeping is stated | Refs: SRR |
| 2026-09-26 | A-3: section 9 conditions 2 and 3; section 10 | R16 verification results recorded in section 13.1. `baseline/srr` is **not** created yet: section 9 condition 2 is not met. `docs/reviews/SRR/baseline-record.md` is written as the prepared record (its section 0 lists the open preconditions P1 to P10); `baseline_tag` stays `null` | Section 9 conditions 2 and 3 (owner sequencing, minutes "Disposition") | none: no new owner ruling; the owner decisions still needed are listed in section 13.1 | Refs: SRR |
| 2026-09-26 | A-4: sections 2, 3 (row 20), 9 condition 4 and 13.1 | OA-1 (FW-B0 flash and observe, TC-SW-TOOL-001 steps 11 and 12) and OA-2 (picotool verify known answer) were performed with the owner during the session on board "1" and passed (minutes commit `0a6f461`, table in minutes section "OA-1 and OA-2 performed (deferral reversed)"). The deferral to PDR, first recorded in the minutes Disposition (`7647516`) and carried as history in this memo at `0bcea39`, is reversed; no deferral or tailoring of row 20 stands. The raw outputs are filed as TC-SW-TOOL-001 run 4, `docs/vv/reports/TC-SW-TOOL-001-r4.md` (test conductor, committed in parallel); this supersedes the section 13.1 statement that the run 4 report does not exist. This closes the owner part of entrance row 20. INSP-016 F-01 (the FW-B0 gate does not exit 0) stays open and still blocks the tag (section 9 condition 2) | Keeps the memo equal to the minutes and names the record that holds the OA-1 and OA-2 raw outputs | "I grabbed the pico so I'm ready to test the flash whenever you are." (minutes, OA-1 and OA-2 performed) | Refs: SRR |
| 2026-09-26 | A-5: sections 7.1 and 13.1 | The lead SE applied SRR decision 7 (owner capacities: Health and Medical TA and CIO/SAISO designee in charter section 2) and SRR decision 10 (a) (charter section 10 safety-critical and mission-critical list per 03 section 6.5 item g) and (b) (charter section 5 rows for status notes and the 07 section 22 artifacts) to `docs/process/00-charter.md` at `6ea6b1d`. This supersedes the section 13.1 statements that these charter edits are not made. Decision 10 (c) (03 section 6.5 item X7) is a 05 change, applied in `docs/process/05-configuration-and-data-management.md`, not in the charter | Records the application of ruled decisions; no new ruling | none: decisions 7 and 10 ruled as recommended ("I approve of this and the SRR.") | Refs: SRR |
| 2026-09-26 | A-6: sections 6, 8, 9 conditions 2 and 3, 13.1 | The owner ruled the twelve close-out items of the minutes section "Close-out decisions (after the first close-out run)" (commit `dd39332`) as recommended; section 13.2 records each item, what it approves and where it is applied. This supersedes the section 13.1 list "Owner decisions needed before the tag" for items (1) to (4) and the ADR-014 route of item (6); item (5), repository protection, becomes the owner action of close-out item 6. RFA-SRR-008 (Routine, due PDR) is raised by close-out item 8; it was raised after signing, so it is an open item with a closure plan in section 13.2, not a section 6 lien. RID-SRR-010 is Answered (section 13.2). No earlier line of this memo is changed | Records the owner rulings given after the first close-out run, before the tag (section 9 conditions 2 and 3) | "I concur with your recommendations" (minutes, "Close-out decisions (after the first close-out run)", `dd39332`) | Refs: SRR |
| 2026-09-27 | A-7: sections 6, 9 condition 3, 13.2 | The owner ruled close-out items A to C of the minutes section "Close-out decisions A to C and repository protection" (commit `786822a`) as recommended and confirmed the repository protection of close-out item 6 (baseline record precondition P8); section 13.3 records each item, the CR classes, the three independent Class I impact reviews (`8b86c16`), TC-SW-TOOL-001 run 6 (gate exit 0) and the new lien of item B (`pico2` host-compilable for Miri, due FW-B1). RFA-SRR-008 moves from Open to Answered on the CR-002 impact review; Verified waits for the owner (01 section 10.3). This supersedes, for close-out item 4, the naming of the two halt loops only (item A widens the allowance to the three CS-19 loops), and for close-out item 8 the INSP-003 reviewer as the CR-002 impact reviewer (item C: a separate reviewer agent, `docs/cm/deviations.md` entry 4). No earlier line of this memo is changed | Records the owner rulings given after the third close-out run, before the tag (section 9 conditions 2 and 3) | "Done and added. I approve the other recommendations" (minutes, "Close-out decisions A to C and repository protection", `786822a`) | Refs: SRR |

### 13.1 R16 verification results (amendment A-3, 2026-09-26)

This subsection is the verification paragraph that section 9 conditions 1 to 3 call for. It records what the reviewers found on the post-ruling work R16 at `f6e167c` (the last record commit) and what the integrator applied after it (`7d735e5`, `be270f1`).

**Reviewer re-issues after the rulings (14 records).** APPROVED, with liens where noted: INSP-003 L1 requirements, allocation and TC-SYS (`401b01d`; finding-6 Verified on decision 30, finding-17 Verified on decision 113 and CR-002; new Minors finding-27 to 31); INSP-004 REQ-TX and REQ-SW-KEYER (`216098e`); INSP-005 SEMP (`1e56df4`); INSP-007 risk register and 06 (`a50aba8`); INSP-008 hazard analysis 0.5.0-pha (`8fc3402`; new Minors finding-15 to 21; the CR-002 Inspection route checked by hand for REQ-SYS-122, 124, 137 and 138 as 04 section 7.4 row 7.3.6 requires); INSP-010 07 (`6136712`); INSP-011 ADRs (`f058c58`; F-01 and F-04 Closed on decisions 106 and 47); INSP-015 TV-001 to TV-010 (`6ba7e7b`, `5e9506a`); INSP-021 04 and CR-002 (`a8d3166`); INSP-025 TC-SYS (`08e5c9b`); INSP-026 SW-KEYER assurance (`ccf742c`). NEEDS CHANGES: INSP-002 ConOps and concept (`7c7959f`); INSP-009 03 and RMM (`bb28ed6`); INSP-016 FW-B0 toolchain proof (`f6e167c`).

**The five Major findings of section 9 condition 2.** Closed: INSP-003 finding-6 (decision 30), INSP-011 F-01 (decision 106) and F-04 (decision 47), INSP-016 F-02 (decision 108, CR-001 applied to 07 at `4364ebb`). Open: **INSP-016 F-01**, the FW-B0 gate does not exit 0. At the rustos pin `c54d35a` cargo deny and the unsafe audit fail; on the decision 110 branch `cwht/wp-sw-licence-manifest-safety` (`2ec64c0`, not merged) complexity and Miri fail. OA-1 and OA-2 passed with the owner on 2026-09-26; their raw outputs are not yet filed (the TC-SW-TOOL-001 run 4 report does not exist).

**New Major findings raised by the R16 delta reviews (not liens; they close before the tag).**
- INSP-002 finding-23: ConOps section 3.4, T15, section 3.5.2 item 2 and Appendix C apply the decision 41 forced 0.5 W step and 120 s timeout to keyed tests only, from test start, while REQ-SYS-187 and 188 (HZ-004 K13) apply both to the whole bench test mode from entry. Open; ConOps author.
- INSP-002 finding-24: `docs/design/concept.md` was not updated for decisions 25, 37 and 38 to 41 (1 kHz guard and 144.001 to 147.999 MHz; the 10 s paddle cap; 16 "owner decision pending" markers; the section 8 backstops). Open; concept author.
- INSP-009 finding-11: `tools/render_rmm.py --check` failed on RMM row SWE-033. Author fix applied at `7d735e5` (SWE-033 In place, citing decision 107 and ADR-027; the check exits 0); open until the INSP-009 reviewer delta-verifies it.

**Tool results at `be270f1` (2026-09-26).** `tools/validate_docs.py`: exit 1, 45 of 50 pass; the 5 failures are APPROVED records whose reviewed blobs R16 changed (INSP-006 and INSP-017 on `rmm.json`, INSP-018 on 07, INSP-013 and INSP-027 on the TS-002 Status line); each reviewer re-issues on the delta. Unit tests: 400 run, 1 failure (`test_repository_exit_zero`, the same cause). `tools/traceability.py`: 4 violations, `HAZARD_REQ_NOT_TESTED` on REQ-SYS-122, 124, 137 and 138, because CR-002 step 5 (the tool accepts the Inspection route) is scheduled before the PDR readiness declaration; INSP-008 recorded the manual check. `tools/render_risk.py --check --gate SRR`: exit 0. `tools/render_rmm.py --check`: exit 0 (was 1). `tools/render_compliance.py --check`: exit 0. `git fsck --full`: exit 0. AL-4: `tools/requirements.txt` pinned at `be270f1` and equal to the venv.

**Content not yet carrying the rulings.** `docs/requirements/l0-stakeholder/expectations.json` holds 23 "owner decision pending at SRR" phrases, and NGO-021 and the MOE-012 success criterion predate decision 37 (INSP-001 has not re-reviewed after the rulings). The charter edits of decision 7 (owner capacities in section 2) and decision 10 items (a) to (c) are owner-controlled and not made. ADR-014 does not yet cite the OET 65 Supplement B statement of decision 18 (RID-SRR-010); the route for an Accepted ADR is an owner choice.

**Owner decisions needed before the tag.** (1) Route for the four CR-002 traceability violations: a numbered departure in `docs/cm/deviations.md` for 05 section 4.4 step 1, or CR-002 step 5 now with the TV-002 re-validation, the delta re-issues of INSP-015, INSP-017 and INSP-020, and an extension of ACC-TRACE-001. (2) Merge of the rustos branch and approval of the CR that moves the pin (INSP-016 X-1). (3) The 07 cyclomatic-complexity counting convention for CS-17 and CS-38 (INSP-016 X-2). (4) The rust-src and Miri sysroot download, which decision 109 did not cover (INSP-016 X-3), and acceptance or reversal of the rustup 1.29.1 self-update (X-4). (5) Repository protection of decision 15 (OQ-CM-001), not observable from this machine. (6) The ADR-014 route for decision 18 and the charter edits of decisions 7 and 10.

**Sequencing to the tag.** Author fixes for INSP-002 finding-23 and finding-24 and the L0 edits; the reviewer delta re-issues of INSP-001, INSP-002, INSP-006, INSP-009, INSP-013, INSP-017, INSP-018 and INSP-027; the FW-B0 close-out (items 2 to 4 above, the `tools/sw_gate.sh` fix of INSP-016 F-14, CR-001 step 3, a gate run that exits 0 filed as run 4 with the OA-1 and OA-2 raw outputs, INSP-016 iteration 4); the L1 status change from Draft to Active with an INSP-003 status-only delta; then commit R, the independent record check and the tag (05 section 4.4 steps 3 to 6).

### 13.2 Close-out decisions (amendment A-6, 2026-09-26)

Source: `docs/reviews/SRR/minutes.md` section "Close-out decisions (after the first close-out run)", commit `dd39332`. The presenter put twelve items to the owner, each with a recommendation; the owner merged the rustos branch in the owner's own terminal (fast-forward `c54d35a` to `2ec64c0`) and then stated, verbatim: "I concur with your recommendations". Items 1 to 12 are ruled as recommended. Each item's ruling text is its recommendation as the minutes record it.

| Item | Ruling (as recommended) | Record and application |
|---|---|---|
| 1 | CR-004 approved: the rustos lock pin moves from `c54d35a` to `2ec64c0` (rustos `master` after the owner's merge of `cwht/wp-sw-licence-manifest-safety`), and `firmware/unsafe-audit.md` is regenerated in the same commit | `docs/cm/cr/CR-004-*.md` disposition block carries the transcription (charter section 4 item 4); INSP-016 F-01 closes on the gate run at the new pin, verified by the INSP-016 reviewer |
| 2 | Approved: the `rust-src` component on `nightly-2026-08-24` and the Miri sysroot crate download from crates.io, which decision 109 did not cover | Performed by Claude on 2026-09-26 20:49 to 20:50 CDT (`rustup component add rust-src --toolchain nightly-2026-08-24`, `cargo +nightly-2026-08-24 miri setup`, both exit 0) |
| 3 | Accepted: rustup 1.29.1, installed by rustup's own self-update during the approved install 1; `rustup set auto-self-update disable` is run | Performed by Claude on 2026-09-26 (exit 0; `rustup 1.29.1 (d95a37b6a 2026-08-13)`) |
| 4 | CR-005 approved: the CS-17 and CS-38 complexity counting convention. The counts of `rust-code-analysis-cli` are the measure; `tools/complexity_gate.py` adds one for each `let ... else`; the two CS-19 halt loops (the panic handler and `safe_state_halt`) get a +1 CS-38 allowance by the CR-001 mechanism; the limit stays 15 | `docs/cm/cr/CR-005-*.md`; the changed tool is re-validated and its accreditation extended once the independent review of its validation record is complete (minutes, "Recorded") |
| 5 | Route for the four traceability violations on REQ-SYS-122, 124, 137 and 138: update `tools/traceability.py` now (CR-002 step 5), then re-validate and re-accredit it, rather than record a deviation | CR-002 implementation record; the TV-002 re-validation and its independent review; the accreditation is extended after that review (minutes, "Recorded") |
| 6 | GitHub protection (decision 15): a ruleset on `main` blocking force-push and deletion, and a tag ruleset on `baseline/*` and `release/*` blocking update and deletion, with no pull-request requirement | Owner action in the GitHub settings; the tag waits for the owner to confirm it is done (minutes, "Recorded") |
| 7 | CR-002 is Class I | CR-002 front matter `class: I`; `docs/cm/deviations.md` entry 1 |
| 8 | Raise an RFA for the independent impact review of CR-002, which was approved before that review, due before PDR | RFA-SRR-008 in `docs/reviews/SRR/rfa-rid-log.json` (Routine, originator owner, assignee Claude as lead SE, due before the PDR readiness declaration); it links `docs/cm/deviations.md` entry 1, whose closure plan it carries: the INSP-003 reviewer reviews CR-002 section 4 and records the result in CR-002 section 6, and CR-002 returns to Submitted if the review changes the owner's basis. Open item with a closure plan; not a section 6 lien, because it was raised after signing |
| 9 | Decision 48 clarification: the menu exposes the switchpoint only, and the debounce counts stay fixed (REQ-SW-KEYER-017, 020 and 021; HZ-004 K9 and HZ-010 K3); OQ-SAF-027 closes on this | OQ-SAF-027 closes on this ruling; its status change in `docs/safety/hazards.json` is the hazard author's edit. The product wording that still names the debounce as user-exposed (for example `docs/safety/hazard-analysis.md`, paragraph "Rulings at SRR (0.5.0-pha)") follows at PDR as a lien: fixed before the PDR readiness declaration and verified by the owning reviewer |
| 10 | The decision 72 author proposals are confirmed: the 4.35 V upper bound of REQ-SYS-185 and the 10 kohm fault resistance of REQ-SYS-186, both TBR to PDR | TBR liens of section 6 (A-2 count unchanged: both requirements are already counted) |
| 11 | REQ-SYS-189 (the 60 s full-scale tone limit, HZ-005 K9) falls within decision 41 | Confirms the R16 addition of REQ-SYS-189 under decision 41 (A-2) |
| 12 | Claude runs `brew pin python@3.13` (TV-001 limitation 3) | Performed by Claude on 2026-09-26 (exit 0) |

Items 2, 3 and 12 were performed by Claude on 2026-09-26; no other install or download was made. The raw log is `/private/tmp/claude-501/-Users-robinonsay-Library-Application-Support-Claude-scratch-workspaces-01a36421-8888-44e4-aeed-7b3fd3224ce6-dab7d27e-450a-44a4-afdd-c7d36fa082a0-scratch-2026-09-25-020b5c/2a2f8354-4494-41be-9d32-dba9c4d2f3be/scratchpad/closeout-installs-2026-09-26.txt`; it is cited in `tools/toolchain.lock.md` by the lock update of this close-out (rows of rustup, the `nightly-2026-08-24` toolchain and Python 3.13.5).

**Schedule approval.** SI-038 (`docs/requirements/l0-stakeholder/stakeholder-inputs.md`), added by the L0 author at `d4c9366` and reviewed in the INSP-001 post-SRR-ruling delta (`e88823f`, CON-020 row "Correct") and in the INSP-023 delta (`2f619f8`, schedule rebaseline), records the owner's approval of the schedule rebaseline, verbatim: "But in general, I agree with the schedule. I'm fine with, you know, slipping the schedule I'd rather do it right." (minutes, "Schedule and enclosure inputs").

**RID-SRR-010.** The ADR-014 erratum line at `5122a6b` applies SRR decision 18; the INSP-011 post-SRR-ruling delta 2 (`877ffac`) checked it and raised no finding. The log records the item as Answered with that evidence. The Answered to Verified transition waits, because `tools/validate_docs.py` accepts as `verification.record` only a record whose `product` equals the item's `product` (`tools/README.md`), and INSP-011 reviews the ADR set `docs/decisions/adr/`, not the ADR-014 file. The item is a Minor lien due PDR (section 6) and does not block the tag. The section 6 "Status at signing" column is unchanged.

### 13.3 Close-out decisions A to C and repository protection (amendment A-7, 2026-09-27)

Source: `docs/reviews/SRR/minutes.md` section "Close-out decisions A to C and repository protection", commit `786822a`. After the third close-out run three records held an open Major finding, all waiting on the owner (INSP-010 finding-21, INSP-018 finding-10, INSP-016 F-01), and the independent baseline check (`docs/reviews/SRR/baseline-check.md`, `a048fdb`) returned NOT READY FOR TAG. The presenter put items A to C to the owner, each with a recommendation, and explained the repository protection of close-out item 6. The owner stated, verbatim: "Done and added. I approve the other recommendations". Items A to C are ruled as recommended. Each item's ruling text is its recommendation as the minutes record it.

| Item | Ruling (as recommended) | Record and application |
|---|---|---|
| A | Amend CR-005 so that the +1 CS-38 allowance covers all three unbounded loops that CS-19 names: the main loop in `cwht-app::main` as well as the panic handler and `safe_state_halt`. The presenter's close-out item 4 recommendation had named only the two halt loops | CR-005 amendment 1 at `106bc3a` (07 A.7); TV-012 run 3 at `0da559a` re-validates `tools/complexity_gate.py` (blob `ddf10798`), gate G5 complexity passes on the firmware and rustos `2ec64c0`; INSP-015 re-issue 4 (`0359409`, APPROVED with liens; ACC-COMPLEXITY-001 extended from 2026-09-27); INSP-010 CR-005 amendment delta (`c8a5143`, finding-21 closed by `106bc3a`); INSP-018 delta 2 (`738da03`, APPROVED with liens) |
| B | Narrow the gate G5 Miri command to the host-compilable crates, as 07 section 8.1 states (today `api`). Making `pico2` host-compilable, with its target-only `link_section` attributes under `cfg_attr`, is a lien due at FW-B1 | `tools/sw_gate.sh` at `495a0c3` (G5 Miri `-p api`); INSP-016 F-15 closed; the new lien is listed below |
| C | Confirm CR-004 and CR-005 as Class I. Log the three CRs that were dispositioned before their independent impact review (CR-002, CR-004, CR-005) in `docs/cm/deviations.md`, and perform all three impact reviews before the tag. This closes RFA-SRR-008 early | Classes: CR-004 Class I confirmed at `31272e0`; CR-005 Class I at `106bc3a`; CR-002 Class I since close-out item 7. Departures: `docs/cm/deviations.md` entries 2 to 4 at `31272e0` (entry 1, CR-002, predates them). Impact reviews: see below. RFA-SRR-008: see below |

**Repository protection (close-out item 6, precondition P8).** The owner confirms that the protection of close-out item 6 is in place (minutes, "Recorded"). The presenter's anonymous check (GitHub REST API, 2026-09-27) shows branch `main` reported as `protected: true`; rulesets are not visible without authentication, so the tag rule rests on the owner's confirmation. The owner later kept the protection as set (minutes, "Run 4 acceptance and repository protection detail": "I think the github settings are fine and yes I approve the results").

**Independent Class I impact reviews (item C).** Commit `8b86c16` (2026-09-27, checked at HEAD `0da559a`) fills section 6 of each CR. The reviewer is a separate independent reviewer agent that authored none of the three CRs and none of their implementing commits; for CR-002 it acts in place of the INSP-003 reviewer that close-out item 8 named, as item C and `docs/cm/deviations.md` entry 4 provide.

| CR | Result | Findings (all Minor, liens due PDR under charter section 4 item 3) |
|---|---|---|
| CR-002 | Impact review complete; Class I concurred; concurrence "Concur with comments" | finding-1 hazard-analysis scope wider than section 8.1 (INSP-008 finding-17); finding-2 tool-validation consequences and `affected_cis` rows 30 and 40 not named; finding-3 04 section 7.4 row 7.3.6 stale since `c774851` |
| CR-004 | Impact review complete; Class I concurred; rustos `c54d35a..2ec64c0` comment-only diff confirmed; unsafe audit regenerated byte-identical (blob `18ef484b`) | finding-1 `firmware/deny.toml` comment stale; finding-2 gate G0 cannot read a git archive export (run 5 deviation D20) |
| CR-005 (as amended under item A) | Impact review complete; Class I concurred; G5 complexity re-run on clean exports of `0da559a` and rustos `2ec64c0`: PASS | finding-1 `affected_cis` omits rows 27, 30 and 40; finding-2 CR-001 step 3 not listed |

No finding changes the owner's basis, so no CR returns to Submitted. `docs/cm/deviations.md` entries 1 to 4 are closed at `bb2485e`.

**RFA-SRR-008.** The CR-002 impact review above is the answer the item requested. The log moves the item from Open to Answered (2026-09-27) with evidence CR-002 section 6, `8b86c16` and `bb2485e`. For an RFA the owner verifies the answer (01 section 10.3), so the Answered to Verified transition and the closure wait for the owner's statement, which the review secretary transcribes into the log. The item is not a section 6 lien (A-6) and does not block the tag.

**TC-SW-TOOL-001 run 6 (`68a44ed`, `docs/vv/reports/TC-SW-TOOL-001-r6.md`).** Clean layout of cwht `bb2485e` and rustos `2ec64c0` (git archive export, with the run 5 D20 clone for G0), no download: `tools/sw_gate.sh` exits 0 in both modes (26 gate-step PASS, 0 FAIL, 0 MISSING, 1 SKIP for the emulation stub). B9 is closed by item A and B11 by item B. Result Pass, `credit: false` (Bench on the development board, charter section 3); steps 11 and 12 stand on run 4, whose UF2 files are byte-identical. New deviation D22 (ELF comparison script). INSP-016 delta 2 (`6a969b9`, APPROVED with liens) closes F-01 (Major, Verified) on run 6; its new Minor F-17 (run 6 owner authorization pending) is a lien due PDR.

**New lien (item B).** `pico2` made host-compilable for gate G5 Miri: its two target-only `link_section` attributes placed under `cfg_attr` for the target, a CR moving the lock's rustos pin, then `-p pico2` returned to the G5 Miri step with a known-answer run. Owners: Robin (rustos maintainer), then the `tools/sw_gate.sh` maintainer (Claude). Due: FW-B1. Recorded in the INSP-016 record (`docs/reviews/SRR/checklists/fw-b0-toolchain-proof.md`, `6a969b9`) as lien L-016-6. The section 6 "Status at signing" column is unchanged; this lien is added by this amendment after signing, in the same way as RFA-SRR-008 (A-6).

**What still blocks the tag.** This amendment does not change the tag preconditions; `docs/reviews/SRR/baseline-record.md` section 0.2 and the next independent baseline check state them.
