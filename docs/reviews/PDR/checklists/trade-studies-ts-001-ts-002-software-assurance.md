---
# Peer-review record front matter (charter sections 2 and 5; docs/process/01-lifecycle-and-reviews.md section 13
# is the single field list; docs/process/07-software-engineering-plan.md sections 2.1.1, 10.2 and 15).
# This is the paired software assurance record (07 section 10.2) of INSP-054
# (docs/reviews/PDR/checklists/trade-studies-ts-001-ts-002.md, reviewer:WP-PDR-14-trades), at the record path INSP-054
# names in assurance_reviewer_agent and cross item 2: the PDR delta of the SRR software assurance record INSP-027
# (docs/reviews/SRR/checklists/trade-study-ts-002-software-assurance.md) that PDR work plan WP-PDR-14 names
# ("INSP-027 delta iterations (SA for TS-002)"). It verifies the WP-PDR-14 errata commit 443b2a3 against the six
# INSP-027 liens and re-applies the SWEHB section 7.1 tasks to TS-002 as corrected.
# Checklist applied: docs/templates/peer-review-checklist-software-assurance.md revision A AS ON ITS CR-012 BRANCH
# (cr/CR-012-pdr-checklist-templates at 7784672, blob 5b13528504868b2add0f0b1e329c63aa2b54cdf4; CR-012 not merged,
# git merge-base --is-ancestor 7784672 main false on 2026-09-27). The `checklist` field names
# peer-review-checklist-design revision B, the checklist INSP-054 and INSP-027 name, because tools/validate_docs.py
# fails a record whose `checklist` names a template absent from main, and the lead SE convention of 2026-09-27 does
# not change the validator. `assurance_checklist` names the template actually applied (the form of INSP-048,
# INSP-049 and INSP-051).
id: INSP-062
checklist: peer-review-checklist-design
checklist_revision: B
assurance_checklist: "docs/templates/peer-review-checklist-software-assurance.md@5b13528504868b2add0f0b1e329c63aa2b54cdf4 (revision A, branch cr/CR-012-pdr-checklist-templates at 7784672)"
checklist_file: docs/reviews/PDR/checklists/trade-studies-ts-001-ts-002-software-assurance.md
product: docs/decisions/trade-studies/
# product_commit and product_files: equal to INSP-054 (readiness R1; rule C2). Both blobs equal git rev-parse
# HEAD:<path> and git hash-object <path> at HEAD 70a3a33 (2026-09-27); both are on main, so the lead SE branch-only
# convention concerns only the checklist template. The assurance lens applies to TS-002 (07 section 2.1.1); TS-001
# is carried so that both records name the same blobs (SA-A3) and is checked only for its routing (SA-A1)
product_commit: "443b2a384e515de5257517ebce58c37bec23a4a3"
product_files: ["docs/decisions/trade-studies/TS-001-receiver-and-pa-concept.md@c53414d980e7cd83367764e47a9ce7464b873d37", "docs/decisions/trade-studies/TS-002-firmware-runtime-make-buy.md@6b18cee831a67dc9550e6082c595023d77bcd704"]
# inputs read (not reviewed), blobs at HEAD 70a3a33
input_files: ["docs/reviews/PDR/checklists/trade-studies-ts-001-ts-002.md@7798e6ce8d1ec3c4e95513726f73d993e74668d8 (INSP-054)", "docs/reviews/SRR/checklists/trade-study-ts-002-software-assurance.md@7a73cc64adc78e1736621041e7eb1d5ca646a469 (INSP-027)", "docs/process/07-software-engineering-plan.md@bfe05f4327e79fa15c24d2cf8c14249804f946a8", "docs/process/rmm.json@e326ddd1b7296d7d7fe172be6f33535cee3192d7", "docs/safety/hazards.json@81cacde47d4f2066ecac3947f3acf65e646b1ad0", "docs/risk/register.json@6685aa0eadc9e8bd806f1920e20d2209e8ae130e", "docs/vv/reports/TC-SW-TOOL-001-r6.md@8d12b38333b4ae863dc8689eed39658dcc276e68", "docs/reviews/SRR/decisions-for-owner.md@e1c499851c862b99b664c674e2970dde61005040", "docs/reviews/SRR/minutes.md@5a5f4ed611f3aeb86d47a610a65ee6d4e9384518", "docs/reviews/SRR/decision-memo.md@110102bf003f1c4c28cc9365c9af7dee39e79abd", "docs/decisions/adr/ADR-027-firmware-runtime-rustos-a0.md@a319c789f620f6fda26eeb392796fe2f4ba6c63e", "rustos 2ec64c0 (git ls-tree and git show of committed objects only: LICENSE, api/Cargo.toml, firmware/pico2/Cargo.toml)"]
paired_record: INSP-054
# product_type: 07 section 2.1.1 row "Software plans" (the make/buy record TS-002, NPR 7150.2D section 6.1 item t;
# Yes in every column). TS-002 is also a trade study whose decision constrains the 07 section 14.1 drivers row
# (runtime, clocks, watchdog, critical section), so the section B row trade-study-or-adr is applied as well
product_type: plans
# criticality: TS-002 constrains the 07 section 14.1 row "Drivers these depend on" (pico2 WP-SW-01, 02, 03, 04,
# 07, 09, 11, conditional WP-SW-14), criticality inherited safety-critical, as INSP-027 recorded. INSP-054 records
# neither for the two-study record; the plans row is Yes in every column, so the dispatch is the same (cross item X-3)
criticality: safety-critical
product_size: "2 trade studies (TS-001 687 lines, Draft revision 2; TS-002 376 lines, decided); assurance lens on TS-002: delta 6c385dfc..6b18cee8 (10 lines rewritten or filled, 15 lines added: section 10 record, 4 lessons, errata section of 6 entries)"
sprint: PDR-prep
author_agent: "author:WP-PDR-14 (Claude as trade study author, invocation of 2026-09-27)"
reviewer_agent: "sa-reviewer:WP-PDR-14-ts-002"
assurance_required: true
assurance_reviewer_agent: "sa-reviewer:WP-PDR-14-ts-002 (software assurance function; paired file review INSP-054 by reviewer:WP-PDR-14-trades)"
iteration: 1
readiness_met: true
# reviewer_verdict and assurance_verdict: APPROVED at iteration 1 (no Major). Two Minor findings; TS-002 is past its
# first APPROVED assurance verdict (INSP-027, SRR), so under PDR work plan rule C1 they are liens due the CDR
# readiness declaration unless the author appends the corrections before the PDR readiness declaration
reviewer_verdict: APPROVED
assurance_verdict: APPROVED
# verdict: set by Claude as software lead (07 section 10.2). Held at NEEDS CHANGES here, as INSP-048, INSP-049 and
# INSP-051 hold theirs: the product blobs are on main, but the checklist applied exists only on
# cr/CR-012-pdr-checklist-templates (lead SE convention of 2026-09-27, INSP-031 practice), and INSP-054 does not yet
# name this record (paired_record, assurance_reviewer_agent, assurance_verdict; each reviewer updates only its own
# record; cross item X-1). Both reviews of the product are now APPROVED; the software lead sets APPROVED on both
# records when INSP-054 carries the pairing and CR-012 merges with the template blob unchanged
verdict: NEEDS CHANGES
findings_major: 0
findings_minor: 2
findings_open: 2
findings_fixed: 0
findings_verified: 0
findings_deferred: 0
assurance_findings_major: 0
assurance_findings_minor: 2
assurance_tasks_applied: ["swe-134 7.1 task 5", "swe-022 7.1 task 1", "swe-013 7.1 task 1", "swe-024 7.1 task 1", "swe-024 7.1 task 2", "swe-024 7.1 task 3", "swe-039 7.1 task 4", "swe-039 7.1 task 7", "swe-039 7.1 task 8", "swe-121 7.1 task 1", "swe-125 7.1 task 1", "swe-139 7.1 task 1", "swe-090 7.1 task 1", "swe-033 7.1 task 1", "swe-033 7.1 task 2", "swe-033 7.1 task 3", "swe-027 7.1 task 1", "swe-211 7.1 task 1", "swe-057 7.1 task 2", "swe-134 7.1 task 4", "swe-134 7.1 task 6", "swe-205 7.1 task 1", "swe-205 7.1 task 3", "swe-205 7.1 task 4", "swe-087 7.1 task 2", "swe-088 7.1 task 1", "swe-088 7.1 task 2", "swe-089 7.1 task 1", "swe-080 7.1 task 2", "swe-081 7.1 task 2"]
# swe134_items_checked: empty; a make/buy record carries no SWE-134 provision (section C N/A with the reason)
swe134_items_checked: []
deferred_rids: []
items_no: ["swe-033 7.1 task 3"]
effort_turns: 34
effort_minutes: 50
record_status: Open
date: 2026-09-27
date_closed: null
---

# Peer review record INSP-062: software assurance pair of INSP-054, TS-002 PDR errata (WP-PDR-14; INSP-027 delta)

**Product.** `docs/decisions/trade-studies/TS-002-firmware-runtime-make-buy.md`, blob `6b18cee8` at the errata commit `443b2a3` (`git rev-parse HEAD:<path>` and `git hash-object <path>` both `6b18cee831a67dc9550e6082c595023d77bcd704` at HEAD `70a3a33`; `git log 443b2a3..HEAD -- docs/decisions/trade-studies/` shows no later change to either file). TS-001 blob `c53414d9` is carried from INSP-054 so that both records name the same blobs. The delta reviewed is `git diff 5122a6b 443b2a3 -- docs/decisions/trade-studies/TS-00[12]*`: for TS-002, header rows "Independent reviewer", "Resulting ADR" and "Dates", the section 1 owner's-decision line, section 10, and the appended section "Errata after the decision (append only)" with entries 1 to 6. **Checklist applied:** `docs/templates/peer-review-checklist-software-assurance.md` revision A as on its CR-012 branch (see the front matter). **Paired record:** INSP-054 (committed `a91ced7`, blob `7798e6ce`), file reviewer `reviewer:WP-PDR-14-trades`, reviewer verdict APPROVED, no finding.

**Scope and acceptance criteria (rule C7).** The six INSP-027 liens (finding-1 to finding-6; plan section 10.1 rows C-159 to C-165, SRR lien L-6, RFA-SRR-006), each checked case by case against its source, and every SWEHB section 7.1 task that section B of the checklist assigns to the rows "Every product type", `plans` (for TS-002) and `trade-study-or-adr`, plus SWE-211, which the errata now cite as flowed down to A0. Rule C1: this is the first PDR iteration of the TS-002 assurance review; later iterations would verify Major fixes only.

**Independence (rule C4; 07 section 2.1).** This invocation authored no part of TS-001, TS-002, the errata, ADR-027 or the SRR records, is not the file reviewer of INSP-054 or INSP-013, is not the SRR assurance reviewer of INSP-027, and edited no product file. Author, file reviewer and assurance reviewer are three different invocations. INSP-054 was read after this reviewer's own lien checks and recomputation.

**Search first (charter section 11 rule 1).** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (queries: PDR software assurance pair record fields and the CR-012 template form; SWEHB `swe-033` section 7.1 tasking; INSP number assignment). The index returned the new files needed except the untracked records of other agents, which were pinned by path. `grep -n` then pinned lines in TS-002, 07, the plan, SWEHB topic 8.10 section 6, the SRR decision memo, the minutes, ADR-027, `tools/toolchain.lock.md` and the TC-SW-TOOL-001 run 6 artifacts; a Python extraction read the SWEHB section 7.1 lists and the `register.json`, `rmm.json` and `hazards.json` rows. The rustos repository was read only by `git ls-tree` and `git show` of the committed pin `2ec64c0`; its working tree was not touched.

## Record

### Findings

Neither finding changes a criterion, weight, score, total, rank, robustness verdict or the decision, and neither affects a safety conclusion, so both are Minor. TS-002 is decided and immutable (05 Table 4-1 row 12; 06 section 14.6), so the fix for each is a further entry appended to the section "Errata after the decision", in the form entries 1 to 6 use.

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | assurance | Minor | swe-033 7.1 task 3; SA-F1 | TS-002 errata entry 2 (b), last sentence ("The risk is carried by RSK-013, which names TS-002; no separate risk was entered."); section 7, A0 hygiene risk row (register column "new RSK-NNN, or a step of RSK-013 (the research WP-13)") | Entry 2 (b) disposes of the A0 hygiene risk by saying RSK-013 carries it. `docs/risk/register.json` RSK-013 (blob `6685aa0e`) does not: its condition and departure are the driver work packages not being demonstrated on hardware before CDR; its mitigation steps S1 to S4 are the driver gap list, ordering by need, dev-board checks and the register-access trait decision; no step, condition or history entry covers the lint, rustfmt, license-manifest or `// SAFETY:` gate items, and the only "hygiene" text in it is a 2026-09-25 history note saying the research WP-13 hygiene package "has no 07 row". Neither alternative the section 7 row offered (a new RSK or a step of RSK-013) was taken. The SWE-033 risk assessment of the chosen alternative therefore ends on a statement the register does not support. The correct disposition is already in entry 2 (b) itself: the risk materialized at FW-B0, was worked as an issue by SRR decision 110 and CR-004, and was closed by TC-SW-TOOL-001 run 6 (`PASS G5 cargo deny`, unsafe audit 37 sites, 0 without SAFETY); the residual item, 37 unsigned audit entries, is a CDR gate item under CS-07 (07 section 8.2), not a risk. Fix: an appended entry that corrects the sentence to that disposition (no register entry is then needed), or a step added to RSK-013 by the risk register writer and cited. | Open | Pending | |
| <a id="finding-2"></a>finding-2 | assurance | Minor | swe-033 7.1 task 3; CK-DES-H1 | TS-002 section 7, A0 risk row 1 ("Given cwht needs twelve rustos work packages, nine of them before PDR (07 section 19)"); section 8, second bullet ("twelve work packages carried by RSK-013"); errata entry 4 "Places" | Errata entry 4 (INSP-027 finding-4) establishes that A0 needs 13 required rustos work packages: WP-SW-01 to WP-SW-12 plus WP-SW-14, the frequency counter of the frequency verification unit, required because the owner adopted SRR decision 40 (decision memo line 213, key decision K2: "Adopt with the 10 kHz window and 100 ms"; REQ-SYS-182 in `docs/requirements/sys/requirements.json`; 07 section 19 row WP-SW-14, safety-critical, HZ-008 K7). The entry corrects the header and the C3 cell only, the two places INSP-027 finding-4 named. The A0 schedule risk that SWE-033 task 3 assesses (section 7 row 1, 9 / Yellow, carried by RSK-013) and the section 8 cost statement still count twelve, so the risk statement for the decided alternative omits the one added package that is safety-critical and PIO-based, outside the `ACC-EMU-001` scope (ADR-027 section 4). No score change: C3 stays 1 and the likelihood anchor of the row is not moved by one package. Fix: extend entry 4, or append an entry, naming section 7 row 1 and section 8 with the count 13 (WP-SW-14 required after decision 40). The same count gap in the RSK-013 condition is a register item (cross item X-2). | Open | Pending | |

### Lien verification of INSP-027 (rule C7, every lien)

| INSP-027 lien | Fix at `443b2a3` | Source checked by this reviewer | Result |
|---|---|---|---|
| finding-1 (C1 and Task 2 omit A0's reused-code V&V) | Errata entry 1 names the four places, states the SWE-027 and SWE-211 obligation of the existing rustos code, reads Task 2 as citing 07 sections 17.1 and 9.9, and gives the sensitivity A0 C1 = 4, total 380, lead 115 | 07 section 17.1 rows rustos `api` and `pico2`, column e ("Contract tests, host tests, dev-board checks"; "HostUnit ... dev-board checks per peripheral, Bench, driver-to-datasheet Inspection, unsafe audit"); 07 section 9.9 ("a rustos feature not covered is not used"); `rmm.json` SWE-211 row (T, rustos `api` and `pico2` named); section 5: A0 400 with C1 weight 20, 400 - 20 = 380; A1 265; lead 115 | Verified |
| finding-2 (Class A evidence superseded) | Errata entry 2 (a) to (d) | (a) `docs/cm/tool-validation/` holds TV-001 to TV-013 (and later records); `docs/vv/reports/TC-SW-TOOL-001-r1.md` to `-r6.md` exist; r6 front matter `run: 6`, `credit: false`, `result: Pass`, `date: 2026-09-27`, toolchain lock rustos row `2ec64c0` from CR-004. (b) r6 `sw-gate-full.txt` line 94 `PASS G5 cargo deny (bans, licenses, sources)`; `unsafe-audit.txt`: "total 37; without SAFETY 0; unsigned 37", `exit=0`; CR-004 file present, `status: Dispositioned`; decision 110 row in `decisions-for-owner.md` line 114. (c) 37 sites, C4 score 4 unchanged. (d) rustos at `2ec64c0` has `LICENSE` and `license = "MIT"` in `api/Cargo.toml` and `firmware/pico2/Cargo.toml` (git show) | Verified, except the last sentence of (b): finding-1 of this record |
| finding-3 (assurance review statements superseded) | Header row "Independent reviewer" corrected in place (decision record, 06 section 14.5); entry 3 corrects section 7 and section 9 | 07 section 2.1.1 row "Software plans" names TS-002, Yes in every column; INSP-027 path and pairing | Verified |
| finding-4 (HZ-008 and WP-SW-14 omitted) | Entry 4: HZ-008 through the two Proposed 07 section 14.1 rows; C3 A0 count 13 required, WP-SW-13 optional; score 1 kept | 07 section 14.1 rows "Frequency control, transmit frequency-word path (**Proposed**)" and "Frequency verification unit (**Proposed**)"; `hazards.json` 0.5.0-pha HZ-008 `firmware_role` criteria a, c, e with K7 "adopted at SRR (package decision 40)"; decision memo line 213; C3 anchor 1 is 11 or more | Verified for the two places named; the same count is stale in two further places (finding-2) |
| finding-5 (rounding rule) | Entry 5: half-down rounding disclosed; A1 275 and 285, A2 and A3 230 and 240; lead at least 115; lesson 3 | C3 weight 20: 265 + 10 = 275, 265 + 20 = 285; 220 + 10 = 230, 220 + 20 = 240; 400 - 285 = 115 | Verified |
| finding-6 (decision still "pending") | Section 1 line, "Resulting ADR", "Dates" and section 10 filled | Minutes lines 21 and 47 (both owner statements verbatim, equal to section 10); decision 107 cell (`decisions-for-owner.md` line 113, "Approve A0"); ADR-027 exists (blob `a319c789`) and section 7 line 100 repeats the four section 8 triggers; section 10 triggers equal section 8 lines 309 to 312 | Verified |

**Recomputation (independent of INSP-054).** Section 5 re-read: A0 400, A1 265, A2 220, A3 220 (weights 20, 10, 20, 10, 15, 15, 10; sum 100). Entries 1 and 5 together in the worst direction: A0 380 against A1 285, lead 95, above the 25-point closeness threshold of 06 section 14.5. INSP-027's weight and Low-cell sensitivity results (smallest leads 80.6 and 115) are unaffected, because no cell changed.

### Task table

| Task | Safety-critical designation (SWEHB 8.10 section 6) | Applied | Result and evidence | Relief (N/A only) | Finding ids |
|---|---|---|---|---|---|
| swe-134 7.1 task 5 (every type) | SC | Yes | This record is the assurance participation in the review of a product 07 section 2.1.1 routes; TS-002 constrains the safety-critical drivers row of 07 section 14.1 | | none |
| swe-022 7.1 task 1 (every type) | SC | Yes | Performed against the project's software assurance plan, 07 section 15, by this review | NASA-STD-8739.8 part: `rmm.json` SWE-022 T (standard not in the corpus) | none |
| swe-013 7.1 task 1 (plans) | SC | Yes | TS-002 has the content the NPR 7150.2D section 6.1 item t record needs at its life-cycle event: options, criteria, scores, risks, recommendation, and now the owner's decision (section 10), the ADR (ADR-027) and the revisit conditions; 07 section 1.3 row t names it | | none |
| swe-013 7.1 task 2 (plans) | SC | N/A | Develop and maintain the SA plan | 07 section 15 is the software assurance plan (07 section 2.1.1 row "Software plans"; template section B row `plans`); TS-002 is not it | |
| swe-024 7.1 task 1 (plans) | SC | Yes | The errata change no commitment of the plan: the decision, the triggers and the work-package list of 07 section 19 are unchanged; entry 4 aligns the study with commitments already in 07 section 19 and decision 40 | | none |
| swe-024 7.1 task 2 (plans) | SC | Yes | Closure of the corrective actions (INSP-027 liens) is recorded with rationale per lien in entries 1 to 6 and section 10; verified above | | none |
| swe-024 7.1 task 3 (plans) | SC | Yes | The commitment change (decision recorded, ADR-027, SRR decision 107) is in the decision memo, the minutes, ADR-027 and section 10; the route (record, not revision) is stated in section 10 and the errata preamble with 05 Table 4-1 row 12 and 06 section 14.6 | | none |
| swe-039 7.1 task 4 (trade-study-or-adr) | | Yes | This record assesses the trade study as corrected, with the recomputation above | | finding-1, finding-2 |
| swe-039 7.1 task 7 (plans) | | Yes | This record's findings table and the INSP-027 lien table are the SA discrepancy list for TS-002; cross items returned below | | none |
| swe-039 7.1 task 8 (plans) | SC | Yes | Every INSP-027 finding has a response in the product (entries 1 to 6, section 10) tracked through RFA-SRR-006, lien L-6 and plan rows C-159 to C-165 | | none |
| swe-121 7.1 task 1 (plans) | SC | Yes | The tailoring TS-002 relies on (SWE-027 T, item c by the owner; SWE-211 T, Rust `core` coverage relief) is in `rmm.json` and approved at SRR ("approves the proposed tailoring of section 17", decision memo line 129) | | none |
| swe-121 7.1 task 2 (plans) | SC | N/A | Develop an SA tailoring matrix | `rmm.json` SWE-022 T: NASA-STD-8739.8 not in the corpus (07 section 15 row "5.17 item 13") | |
| swe-125 7.1 task 1 (plans) | SC | Yes | `rmm.json` rows SWE-033 (FC, implementation names the make-or-buy assessment), SWE-027 and SWE-211 exist | | none |
| swe-125 7.1 task 2 (plans) | SC | N/A | Maintain the 8739.8 mapping matrix | `rmm.json` SWE-022 T | |
| swe-139 7.1 task 1 (plans) | SC | Yes | TS-002 meets NPR 7150.2D 3.1.2 as the `rmm.json` SWE-033 row states it, with the decision now recorded | | none |
| swe-087 7.1 task 3 (plans) | | N/A | Peer review of SA and safety plans | TS-002 is not the SA or safety plan; 07 is (07 section 2.1.1 row "Software plans", section 15) | |
| swe-090 7.1 task 1 (plans) | | Yes | This record and INSP-054 carry the SWE-089 measures of 07 section 10.3 (MSR-20, MSR-21 inputs) | | none |
| swe-154 7.1 task 1, swe-156 7.1 task 1, swe-159 7.1 tasks 1 and 2 (plans, cybersecurity section) | swe-156 blank; others blank | N/A | TS-002 has no cybersecurity section | Template row `plans` limits these to the cybersecurity section, which is 07 section 16; the reused-code and dependency risk is RSK-062 there | |
| swe-033 7.1 task 1 | | Yes | Section 2 maps SWE-033 options a to f; four alternatives scored; unchanged by the errata; decision recorded against them | | none |
| swe-033 7.1 task 2 | SC | Yes | Entry 1 now flows SWE-027 a to f and SWE-211 to A0's reused rustos code through 07 sections 17.1 and 9.9, the gap INSP-027 SA-033-2 answered No | | none |
| swe-033 7.1 task 3 | | No | The risks of the decision are assessed and the hygiene risk is restated against run 2 and run 6, but its disposition names a risk that does not carry it, and the driver-effort risk row keeps twelve packages | | finding-1, finding-2 |
| swe-027 7.1 task 1 | | Yes | 07 section 17.1 records a to f for `api`, `pico2` and `core`; item c: rustos at the pin `2ec64c0` is MIT (`LICENSE`, manifest `license` fields), which entry 2 (d) states; 07 section 17.1 at main still names `c54d35a` and "No `LICENSE` file", corrected on the CR-013 branch (07 line 728 there; cross item X-4) | | none |
| swe-211 7.1 task 1 | | Yes | At plan maturity: 07 section 9.9 and 07 section 19 closure rule (contract tests, dev-board check, signed unsafe audit entries) require custom-code level for every rustos feature used; entry 1 now states it for A0. Testing itself is by work package (FW-B1 onward) | | none |
| swe-057 7.1 task 2 (trade-study-or-adr) | | Yes | The errata change no architecture statement; the decided structure (zero external crates, single NVIC priority, SIO-only inputs, REQ-SYS-129, 07 section 7.7) is unchanged, so no safety requirement moves | | none |
| swe-134 7.1 task 4 (trade-study-or-adr) | SC | Yes | Partitioning (07 section 7.8) is not affected by the decision or the errata; A0 keeps the safe-state and monitor units in `cwht-core` over owner-controlled drivers | | none |
| swe-134 7.1 task 6 (trade-study-or-adr) | SC | Yes | Entry 4 makes the study's hazard list consistent with `hazards.json` 0.5.0-pha and 07 section 14.1 (HZ-008 via the Proposed rows) | | none |
| swe-027 7.1 task 1 (trade-study-or-adr) | | Yes | As above (same task, both rows) | | none |
| swe-136 7.1 task 1, swe-070 7.1 task 1 (trade-study-or-adr) | | N/A | The decision selects no tool, emulator or model | Template row `trade-study-or-adr` applies them only "when the decision selects a tool, emulator or model"; the toolchain is TS-002 section 2 "Buy (upstream stable)", accredited under 07 section 17.3 (TV-020) | |
| swe-205 7.1 task 1 | SC | Yes | Section D, SA-D1 | | none |
| swe-205 7.1 task 3 (trade-study-or-adr) | SC | Yes | The decision adds or moves no component; entry 4 names only components already in 07 section 14.1 (the two Proposed HZ-008 rows and the drivers row with WP-SW-14) | | none |
| swe-205 7.1 task 4 | SC | Yes | Section D, SA-D3 | | none |
| swe-087 7.1 task 2 | | Yes | Section E, SA-E1 | | none |
| swe-088 7.1 tasks 1 and 2 | | Yes | Section A, SA-A4; section E, SA-E1 | | none |
| swe-089 7.1 task 1 | | Yes | Section E, SA-E2 | | none |
| swe-080 7.1 task 2, swe-081 7.1 task 2 | swe-081 task 2 SC | Yes | Section E, SA-E3 | | none |

## Readiness criteria

| # | Criterion | Answer | Evidence |
|---|---|---|---|
| R1 | Committed, frozen, same blobs as the paired record | Yes | Both blobs equal INSP-054 `product_files` and HEAD (`git rev-parse`, `git hash-object`); no commit after `443b2a3` touches them |
| R2 | Row and criticality identified | Yes | 07 section 2.1.1 row "Software plans" (line 117) and row "Trade studies and ADRs" (line 118); 07 section 14.1 drivers row, inherited safety-critical |
| R3 | `validate_docs.py` on the product; traceability with `--output` in the scratch directory | Yes | `validate_docs.py` reports no failure on either study (the failures it prints are other records, including INSP-013 and INSP-027 record drift, INSP-054 cross item 1); `traceability.py --report-only --output <scratch>/trace.md`: 245 requirements, 173 test cases, 0 violations, 2 warnings (REQ-SYS-125, REQ-SYS-148, not touched by the product); `docs/vv/` unchanged |
| R4 | Paired review filed under its own invocation; this reviewer independent | Yes | INSP-054 `author_agent` author:WP-PDR-14, `reviewer_agent` reviewer:WP-PDR-14-trades |

## A. Dispatch, independence and record integrity

| Id | Answer | Evidence |
|---|---|---|
| SA-A1 | Yes | TS-002: 07 section 2.1.1 row "Software plans", Yes in every column, and row "Trade studies and ADRs" through the drivers row of 07 section 14.1. TS-001: routed No (row 3; a hardware concept study that constrains no 07 section 14.1 component; its header now says so), consistent with INSP-013 and INSP-054 |
| SA-A2 | Yes | Three invocations: author:WP-PDR-14, reviewer:WP-PDR-14-trades, this reviewer; recorded here; INSP-054 names this record's path as pending (cross item X-1) |
| SA-A3 | Yes | Same product path and the same two blobs as INSP-054 |
| SA-A4 | Yes | INSP-054 used the design checklist A, B, H and CK-RSK-B1 to B10, the set of INSP-013 and 07 section 2.1.1 row 3, and answered every item with evidence; 5.3.3 a to d: readiness met, checklist applied, participants recorded, verdict and measures recorded |

## B. SWE-to-task table

| Id | Answer | Evidence |
|---|---|---|
| SA-B1 | Yes | Task table covers the rows "Every product type", `plans` (common tasks and "for TS-002") and `trade-study-or-adr`, plus swe-211; `assurance_tasks_applied` lists every Yes and No row |
| SA-B2 | Yes | Each N/A row cites `rmm.json` SWE-022 T, 07 section 15, 07 section 16 or the template row condition |
| SA-B3 | Yes | swe-033 task 3 (No) is carried by finding-1 and finding-2 |

## C. SWE-134 items a to l

N/A for this product. TS-002 is the make/buy record; the a to l provisions are carried by the requirements, design and code of the 07 section 14.2 modules and are checked at those products. The decision and the errata change no provision: the drivers keep the inherited criticality, and the section 19 closure rule (contract tests, dev-board check, signed unsafe audit) is unchanged. `swe134_items_checked` is empty for this reason, as in INSP-027.

## D. Software safety analysis and hazard traceability

| Id | Answer | Evidence |
|---|---|---|
| SA-D1 | Yes | The study's hazard list now includes HZ-008 (entry 4), matching `hazards.json` 0.5.0-pha HZ-008 `firmware_role` (criteria a, c, e; frequency-word path and K7). No new software contribution arises from the make/buy decision; SWEHB `swe-205` section 7.7.2 considerations (control of the PA through `PA_EN`, interlocks, watchdog) sit in the drivers the decision keeps owner-controlled |
| SA-D2 | Yes | 07 section 14.1 drivers row "inherited" criticality and the conditional WP-SW-14 row agree with the union rule; the errata do not rename or add a component |
| SA-D3 | Yes | Traceability run (R3): 0 violations, so zero `HAZARD_CONTROL_UNTRACED` and zero `HAZARD_INVERSE` |
| SA-D4, SA-D5 | N/A | TS-002 creates no software requirement (the section D items bind requirement and test products, 07 section 2.1.1 rows 1 and 7) |
| SA-D6 | N/A | No software change for the safety analysis to absorb; `hazard-analysis.md` is WP-PDR-16's product |

## E. Peer review, change and configuration assurance

| Id | Answer | Evidence |
|---|---|---|
| SA-E1 | Yes | INSP-027 finding-1 to finding-6 each verified at the new blob (lien table); INSP-013 finding-11 to finding-13 verified by INSP-054 and re-read here for the TS-002 parts; none closed without evidence |
| SA-E2 | Yes | Both records carry the 07 section 10.3 measures (size, findings by severity and state, turns, minutes) |
| SA-E3 | Yes | TS-002 is Record class (05 Table 4-1 row 12, section 4.2): commit `443b2a3` carries `Refs: INSP-013, INSP-027, RFA-SRR-006, WP-PDR-14` and the Co-Authored-By line; the change is append-only for the analysis and fills the decision record 06 section 14.5 requires; no CR is needed (the plan registers none for WP-PDR-14) |
| SA-E4 | N/A | No item under test; no credit run cited for credit (run 6 is `credit: false` and is cited as a fact) |

## F. Assurance risks, metrics and reporting

| Id | Answer | Evidence |
|---|---|---|
| SA-F1 | Yes | No new risk: finding-1 is a product statement, and the WP-SW-14 count gap in RSK-013 is returned to the risk register writer (WP-PDR-18) as cross item X-2 against the existing RSK-013 |
| SA-F2 | Yes | Front matter: 0 Major, 2 Minor, both Open, items_no, effort |
| SA-F3 | Yes | Verdict block below states verdict, open findings, tasks applied and reliefs |

## Completion criteria and verdict

Readiness R1 to R4 true; every task SA-B1 requires is in the task table; sections A, C, D, E and F answered with N/A reliefs stated; zero Major findings; two Minor findings raised after TS-002's first APPROVED assurance verdict (INSP-027 at SRR), so they are liens due the CDR readiness declaration under rule C1 unless appended before the PDR readiness declaration; `assurance_tasks_applied` filled; measures filled; `validate_docs.py` passes on this record. `assurance_verdict: APPROVED`. The record `verdict` is held at NEEDS CHANGES for the software lead as explained in the front matter.

## Cross items (returned to Claude)

- **X-1.** INSP-054 still reads `assurance_reviewer_agent: "pending: ..."` and `assurance_verdict: pending` and has no `paired_record`. Its reviewer updates it to `paired_record: INSP-062`, names this reviewer and copies `assurance_verdict: APPROVED` (07 section 10.2 Record row). INSP-054's lien table also cites "`register.json` RSK-013 `trade_study_ids: ["TS-002"]`"; the field holds `["TS-001", "TS-002"]` (no effect on its conclusion).
- **X-2.** RSK-013 condition in `docs/risk/register.json` still reads "thirteen rustos driver work packages (WP-SW-01 to WP-SW-13, WP-SW-13 optional ...)"; after SRR decision 40 WP-SW-14 is required, so the count is 13 required plus 1 optional. Risk register writer (WP-PDR-18) at the PDR Track pass.
- **X-3.** INSP-054 records `criticality: neither` for the two-study record; the TS-002 assurance lens uses safety-critical (07 section 14.1 drivers row, as INSP-027). No dispatch effect (row "Software plans" is Yes in every column); the software lead may align the two at the pairing update.
- **X-4.** 07 section 17.1 at main pins rustos `c54d35a` and says no license exists; 07 section 17.2 still says TS-002 is Draft with its assurance review pending. The CR-013 branch corrects 17.1 (line 728 there, pin `2ec64c0`, `OQ-SW-001` answered); the 07 writer (WP-PDR-13) checks that 17.2 is corrected in the same CR.
- **X-5.** INSP-013 and INSP-027 fail `validate_docs.py` on record drift (they name `2a0c40a8` and `6c385dfc`); the re-issue deltas that point to INSP-054 and this record are INSP-054 cross item 1, not repeated here.
- **X-6.** The SA checklist template's "Every product type" row and the `plans` row were applied from the CR-012 branch; after CR-012 merges, the delta iteration of this record switches `checklist` to `peer-review-checklist-software-assurance` revision A and drops `assurance_checklist`.
- **X-7.** Two working-tree records of other agents both carry `id: INSP-060` (`docs/reviews/PDR/checklists/semp.md` and `cr-015-process-01-02-08.md`, untracked at the time of this review); this record took INSP-062, the next number free across main, the CR branches and the working tree.

## Commands

```
git rev-parse HEAD:docs/decisions/trade-studies/TS-002-firmware-runtime-make-buy.md    # 6b18cee8...
git hash-object docs/decisions/trade-studies/TS-002-firmware-runtime-make-buy.md      # 6b18cee8...
git diff 5122a6b 443b2a3 -- docs/decisions/trade-studies/TS-00[12]*
git merge-base --is-ancestor cr/CR-012-pdr-checklist-templates main                   # false
git -C /Users/robinonsay/rust/rustos ls-tree --name-only 2ec64c0                       # LICENSE present
git -C /Users/robinonsay/rust/rustos show 2ec64c0:api/Cargo.toml                       # license = "MIT"
/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/validate_docs.py
/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/traceability.py --report-only --output <scratch>/trace.md
```

## Verdict

```
ASSURANCE VERDICT: APPROVED
PRODUCT: docs/decisions/trade-studies/TS-002-firmware-runtime-make-buy.md@6b18cee8, docs/decisions/trade-studies/TS-001-receiver-and-pa-concept.md@c53414d9 (carried, routed No) at 443b2a3; PAIRED RECORD: INSP-054
PRODUCT TYPE: plans (and trade-study-or-adr); CRITICALITY: safety-critical
FINDINGS:
- [Minor] swe-033 7.1 task 3 (SA-F1) errata entry 2 (b) says RSK-013 carries the A0 hygiene risk; RSK-013 has no such step or condition (finding-1).
- [Minor] swe-033 7.1 task 3 section 7 row 1 and section 8 still count twelve rustos work packages; entry 4 makes it 13 with WP-SW-14 (finding-2).
LIENS VERIFIED: INSP-027 finding-1 to finding-6 (finding-2 (b) last sentence and finding-4 propagation raised as finding-1 and finding-2 here)
TASKS APPLIED: swe-134 5; swe-022 1; swe-013 1; swe-024 1 to 3; swe-039 4, 7, 8; swe-121 1; swe-125 1; swe-139 1; swe-090 1; swe-033 1 to 3; swe-027 1; swe-211 1; swe-057 2; swe-134 4, 6; swe-205 1, 3, 4; swe-087 2; swe-088 1, 2; swe-089 1; swe-080 2; swe-081 2
TASKS N/A (relief): swe-013 2 (07 section 15); swe-121 2, swe-125 2 (rmm.json SWE-022 T); swe-087 3 (07 is the SA plan); swe-154 1, swe-156 1, swe-159 1 and 2 (07 section 16); swe-136 1, swe-070 1 (no tool selected)
SWE-134 ITEMS CHECKED: none (make/buy record; section C N/A)
MEASUREMENTS: size=2 studies (lens on TS-002, 376 lines); tasks=40 (30 applied, 10 N/A); tasks_no=1; turns=34; minutes=50; major=0; minor=2
RECORD VERDICT: NEEDS CHANGES (held for the software lead: template on the CR-012 branch; INSP-054 pairing pending)
```
