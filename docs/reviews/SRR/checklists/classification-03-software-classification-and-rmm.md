---
# Peer-review record front matter (charter section 5; docs/process/01-lifecycle-and-reviews.md section 13
# is the single field list; docs/process/08-agent-briefing.md section 3.2; template
# docs/templates/peer-review-checklist-classification.md revision A).
id: INSP-009
checklist: peer-review-checklist-classification
checklist_revision: A
checklist_file: docs/reviews/SRR/checklists/classification-03-software-classification-and-rmm.md
product: docs/process/03-software-classification-and-rmm.md
# product_commit at iteration 3 re-issue 2 (post-SRR-ruling delta 2, 2026-09-26): 7d735e5, the last commit touching the three
# products (SRR decision 107 applied to SWE-033, finding-11); review baseline HEAD 5122a6b; blobs equal git rev-parse HEAD:<path>.
# Earlier: the commit reviewed at iteration 3 re-issue 1, the post-SRR-ruling delta (review baseline HEAD 1e56df4,
# 2026-09-26); iteration 3 reviewed HEAD adcfe09. Iteration 3 text kept below: the commit reviewed at iteration 3 (review baseline HEAD adcfe09, 2026-09-26). The committed blobs
# reviewed are in product_files (git rev-parse HEAD:<path>); the working tree equals HEAD for all three. The iteration 2
# blobs (03 fdc8d076, rmm.json 78c3b236, rmm.md fe374a48) and the iteration 1 blobs named in the body (Product
# paragraph) are not in the object store (SRR package section 2.3).
# product_commit at iteration 3 re-issue 3 (CR-010 delta, 2026-09-29): 5cd87cf, the CR-010 change set on branch
# cr/CR-010-apply-srr-decisions-9-and-40 (base ab2af2d; CR-010 section 5 step 5); the blobs equal git rev-parse 5cd87cf:<path>
# and main holds none of them until the CR-010 merge. The iteration 3 re-issue 2 value was 7d735e5 with 03 ed270f44,
# rmm.json e326ddd1 and rmm.md 54e351f4.
product_commit: "5cd87cff741653c1f3746029d66c7d42c5a0b1d2"
product_files: ["docs/process/03-software-classification-and-rmm.md@1e03b873b404deeaa86ba2393806cda74996187d", "docs/process/rmm.json@a907a087f1302e275ea56bdb7bba89638777a319", "docs/process/rmm.md@17ea4733a4d41b54424619f8682db815b05d4ebf"]
# iteration 3 re-issue 2 product_files named 03 ed270f44, rmm.json e326ddd1 and rmm.md 54e351f4
# iteration 3 re-issue 1 product_files named rmm.json 37c6f24d and rmm.md 5e6dd864 (03 ed270f44 unchanged)
# inputs read at iteration 3 re-issue 3 (not reviewed): hazards.json 81cacde4 (unchanged), 07 at 5cd87cf (3ae7d73b) and the SRR
# decision memo 110102bf (decisions 9 and 40)
# inputs read at iteration 3 re-issue 1 (not reviewed): hazards.json 0.5.0-pha (SHA-256 27228162...fed76de5) and 07 at the HEAD
# blobs below; iteration 3 read hazards.json 0.4.2-pha (blob 37d6cc83) and 07 (blob d0f8baf6)
input_files: ["docs/safety/hazards.json@81cacde47d4f2066ecac3947f3acf65e646b1ad0", "docs/process/07-software-engineering-plan.md@3ae7d73b01810e47fd10251d798e0a047aaa72dd", "docs/reviews/SRR/decision-memo.md@110102bf003f1c4c28cc9365c9af7dee39e79abd"]
# product_size at iteration 3 re-issue 3: the three proposed component rows are determined by SRR decisions 9 and 40 (CR-010)
product_size: 9 inventory items and 13 per-item classification rows; 11 component rows determined plus 5 verification-software items; RMM of 100 rows
sprint: SRR-prep
author_agent: "author:classification-rmm (Claude lead SE and software lead, 03 author; fourth revision 2026-09-26 applying INSP-009 and INSP-017, committed at b301df2 and 1543c9f)"
reviewer_agent: "reviewer:classification"
criticality: safety-critical
assurance_required: true
# assurance_reviewer_agent: the software assurance review of this product is the separate record INSP-017,
# docs/reviews/SRR/checklists/classification-03-software-classification-and-rmm-software-assurance.md (03 section 3.3;
# 03 item X19).
assurance_reviewer_agent: "sa-reviewer:classification (INSP-017)"
# iteration: stays 3 (the schema maximum); the post-SRR-ruling delta is iteration 3 re-issue 1, precedent INSP-005
iteration: 3
# readiness_met: true at iteration 3 re-issue 3 (R2 met: render_rmm.py --check exit 0 at 5cd87cf; R1 met for the product; R3 carried
# as the narrowed lien finding-10). Earlier: true at iteration 3 re-issue 2: R2 met (render_rmm.py --check exit 0 after 7d735e5, finding-11 Verified); R1 met for
# the product; R3 difference carried as lien finding-10 (convergence rule). Earlier: false at iteration 3 re-issue 1: R2 (render_rmm.py --check) exits 1 at HEAD on SWE-033 (finding-11);
# R1 to R3 were met at iteration 3
readiness_met: true
reviewer_verdict: APPROVED
# assurance_verdict at iteration 3 re-issue 3: the INSP-017 verdict as filed on main 908d21a (APPROVED on 03 ed270f44, rmm.json
# e326ddd1, rmm.md 54e351f4); its CR-010 delta by a separate software assurance invocation is observation O-11. Earlier:
# the INSP-017 verdict as filed at HEAD 5122a6b (APPROVED on rmm.json 30fcde24; its delta re-issue is observation O-9)
# at iteration 3 re-issue 2; earlier: the INSP-017 verdict as filed at HEAD 1e56df4 (iteration 3, APPROVED) when iteration 3 re-issue 1 was written
assurance_verdict: APPROVED
# verdict: APPROVED with liens finding-5, 7, 8, 9, 10 (narrowed), 12 at iteration 3 re-issue 3 (CR-010 delta; no Major open;
# no new finding), subject to observation O-11; the same at iteration 3 re-issue 2 (no Major open; convergence rule)
verdict: APPROVED
# finding-12 (Minor) is new at iteration 3 re-issue 2; finding-10 (Minor) and finding-11 (Major) are new at iteration 3 re-issue 1 (post-SRR-ruling delta); finding-7 is new at iteration 2; finding-8 and finding-9 are new at iteration 3 (Minor)
findings_major: 2
findings_minor: 10
# findings_open: none at iteration 3 re-issue 2 (finding-11 Verified at 7d735e5); finding-11 (Major) was open at iteration 3 re-issue 1
findings_open: 0
findings_fixed: 0
# findings_verified: finding-1, 2, 3, 4, 6, and finding-11 at iteration 3 re-issue 2
findings_verified: 6
# findings_deferred: the four Minor findings carried as "Lien: fix before PDR" under the convergence rule of 2026-09-26
# (charter section 4 item 3): finding-5, finding-7, finding-8, finding-9; finding-10 added at iteration 3 re-issue 1;
# finding-12 added at iteration 3 re-issue 2
findings_deferred: 6
assurance_findings_major: 0
assurance_findings_minor: 0
assurance_tasks_applied: []
deferred_rids: []
# iteration 3 re-issue 2: R2 Yes (finding-11 Verified), CL-8 No (finding-12, lien); iteration 3 re-issue 1 answers No: R2 (finding-11), CL-4 (finding-8, finding-10), with the iteration 3 answers that ride as liens;
# iteration 3 answers that ride as liens (iteration 2: R1, CL-3, S1; iteration 1: R1, CL-3, CL-7, CL-8, S1, S5)
items_no: [CL-3, CL-4, CL-8, S1, S5]
# effort: iteration 1 38 turns and 55 minutes; iteration 2 22 turns and 30 minutes; iteration 3 30 turns and 40 minutes;
# iteration 3 re-issue 1 (post-SRR-ruling delta) 22 turns and 35 minutes; iteration 3 re-issue 2 18 turns and 30 minutes;
# iteration 3 re-issue 3 (CR-010 delta, shared with INSP-006 and INSP-010) 14 turns and 30 minutes
effort_turns: 144
effort_minutes: 220
record_status: Open
date: 2026-09-26
date_updated: 2026-09-29
date_closed: null
---

# Peer review record INSP-009: independent software classification assessment (03, rmm.json, rmm.md)

**Product.** `docs/process/03-software-classification-and-rmm.md` (third revision, 2026-09-25, working tree, blob `c87abe5a09985c3f0a3adb74e17386cc61d731b4`, last commit `4e3f891`), sections 3 (classification) and 4 (safety-critical and mission-critical determination) as the checklist scope, with section 5 and the RMM (`docs/process/rmm.json` blob `3645b4f682cba38373f0fca55beb190ded36c032`, rendered `docs/process/rmm.md` blob `070556193080b70d5fdf388550523bade3357007`) checked for the minimum content SWE-020, SWE-125, SWE-139 and SWE-176. **Source of record read:** `docs/safety/hazards.json` 0.3.0-pha, working tree blob `4f9f38fdd5917bf00fdffef270f0c777d53ce142`, SHA-256 `e008671c50a3e034056fa6cce16670dca20ddcf60b75a13c848af42362e3be37` (equal to the hash 03 section 4.2 states). **Authoritative component list read:** `docs/process/07-software-engineering-plan.md` section 14.1, working tree blob `5b6f7b5a947120916dc5cb9e6ab7d9cc17528189`. **Checklist:** `docs/templates/peer-review-checklist-classification.md` revision A (CL-1 to CL-9, copied from 03 section 3.3), plus supplementary items S1 to S5 below for the SWE-020, SWE-125, SWE-139 and SWE-176 minimum content the assignment names. **SRR context:** package `docs/reviews/SRR/package.md` section 2 items H1 and H13, entrance row 22, section 6.9, decisions 9 and 40.

**Search-first compliance.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (queries: App. D Class D and Class E definitions and exclusions; peer-review record front-matter fields and `PEER_REVIEW_RECORD_SCHEMA`; review-figure scripts). `grep -n` was used afterwards only to pin lines the hits pointed at. Files at known paths were read directly.

**Independence.** This reviewer did not author 03, `rmm.json`, `rmm.md`, `hazards.json` or 07. The product was not edited.

## Findings

Ids follow the `finding-<n>` anchor rule of 01 section 13 and 08 section 3.2 (the assignment's F-nn label is given in brackets).

| Finding | Origin | Severity | Item | Location | Description | State | Deferred to | Disposition |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 (F-01) | reviewer | Major | CL-7 | 03 section 4.3, "Not safety-critical and not mission-critical" paragraph (menu handling); section 9 row Safety-critical software; mirrored in 07 section 14.1 "Neither" paragraph and `rmm.json` SWE-134 | Menu handling is placed outside the mission-critical set, but the key-input mode can change only by a menu selection (REQ-SYS-056, "only by an explicit operator menu selection"; REQ-SYS-163 accepts that selection while a key input reads closed, the mono-plug straight-key case), and the keyer modes Straight, Iambic A, Iambic B, Ultimatic and Bug are operator-selected (REQ-SYS-040). A menu fault that prevents or corrupts that selection contributes to losing the straight-key or paddle capability, which 03 section 4.1 step 4 names as the primary mission objective (SI-018, core requirement). By the App. A definition (`07-appendixa.md` line 71, "cause, contribute to, or mitigate the loss of capabilities") and by 03's own rule ("when its failure can cause or contribute to losing that capability (not only when it defeats it outright)"), the same argument 03 uses to make frequency display rendering and encoder input mission-critical applies to the key-input and keyer-mode selection path of the menu. This changes the mission-critical set. Fix: classify the key-input mode and keyer-mode selection path of menu handling (with the UI input it depends on) as mission-critical in section 4.3 and section 9, carry it into section 5 (SWE-134 allocation, mission-critical column) and raise the matching 07 section 14.1 and `rmm.json` SWE-134 change; or state, with evidence, why no menu fault can prevent selection of either key type (for example a boot-time default or a hardware path that bypasses the menu). | Verified | | Closed (iteration 2). 03 fourth revision section 4.3 mission-critical paragraph (line 182) classifies the key-input and keyer-mode selection path (REQ-SYS-040, 056, 163, speed and weighting, the menu units and the button and encoder input) as mission-critical; the evidence offered for "no path bypasses the menu" holds: REQ-SYS-136 (`requirements.json`, Draft) restores Iambic A at every configuration reset and REQ-SYS-056 permits a mode change only by menu selection. Carried to section 5 rows a, b, g and k (mission-critical column), section 4.3 "Not safety-critical and not mission-critical" paragraph, section 9 (safety-critical row and menu-handling row), and `rmm.json` SWE-134 implementation ("key-input and keyer-mode selection path"). The 07 section 14.1 and 14.2 change is raised as 03 X1 (x) and (xi) and the charter section 10 wording as 03 item g; the owner rules through X20. |
| <a id="finding-2"></a>finding-2 (F-02) | reviewer | Minor | CL-8 | 03 section 6.5 items X1 and X3; section 4.3 scheduler row and drivers row | X1 lists differences (i) to (vii) "re-checked against 07 at 4e3f891", and X3 is Open, but the 07 working tree that forms the same pre-SRR change set (blob `5b6f7b5`) already carries them: `SW-TXSEQ` names HZ-008, the bench test-mode guard and the VBUS-absent and frequency-verified prerequisites; `SW-SAFE` names HZ-001 to HZ-007, HZ-011, HZ-014 with union a, b, c, e and the fault annunciation and no-gap watchdog units; `SW-PWR` names the charge pause and the GPIO24 VBUS reading; `SW-SCHED` has a, b, c, e; the two Proposed frequency rows exist; the "Neither" paragraph cites 03 section 4.3.1; section 19 has WP-SW-14 (07 line 773); 07 section 14.2 row d no longer cites "03 section 5 item d" (07 line 607). Two 03 statements are stale for the same reason: the scheduler row "100 ms in 07 section 14.2 j" (07 row j now reads "CPU watchdog 2 s (REQ-SYS-131) ... This replaces the revision A.2 watchdog of 100 ms") and the drivers row "The frequency-counter capture has no work package in 07 section 19". The differences that do remain are not listed: 07 section 14.1 rows `SW-SAFE` and `SW-SCHED` do not carry the two HZ-008 type (ii) findings of 03 section 4.3 (X14 addresses only `hazards.json`), and the 07 `SW-SCHED` row still says "03 section 4.3 records a, c until its re-transcription". Fix: re-check X1 and X3 against the current 07, mark what is resolved, list the remaining differences (the HZ-008 type (ii) findings in 07, the stale 07 note), and correct the two stale 03 statements. | Verified | | Closed (iteration 2). 03 X1 (line 327) now marks (i) to (vii) resolved and lists (viii) to (xii); each remaining difference was confirmed in 07 blob `1b8864b`: line 571 cites 0.3.0-pha and names the 03 re-transcription as pending; line 587 `SW-SCHED` reads "03 section 4.3 records a, c until its re-transcription" and lists no HZ-008; line 590 drivers row "gains ... at its re-transcription"; line 596 "Neither" places all menu handling outside both sets. X3 (line 329) is Resolved and 07 line 607 row d cites `hazard-analysis.md` section 7 row d. The 03 scheduler row now gives "at most 2 s, REQ-SYS-131" and the drivers row names the conditional WP-SW-14 (07 line 773). |
| <a id="finding-3"></a>finding-3 (F-03) | reviewer | Minor | S1 (SWE-020) | 03 section 1 inventory and section 3.1 per-item table | SWE-020 requires each system and subsystem containing software to be classified. Project software present in the working tree is in neither table: `tools/render_review_figures.py` (review-package and deck figures; 05 section 9.1 class B per INSP-006 finding-8), the figure generators `docs/reviews/SRR/figures/concept-block-diagram.py` and `docs/reviews/SRR/figures/risk-matrix.py`, `docs/icd/figures/render_icd_figures.py`, the tool-validation evidence scripts under `docs/cm/tool-validation/evidence/`, and the known-answer test suite `tools/tests/*.py` (verification software of the Class D tools; section 6.1.1 relies on it but section 3.1 does not classify it). None changes a class (each would be Class D by a.1(b) and example b.1, elected Class A, like the other render tools). Fix: add these items to sections 1 and 3.1, or add a rule that places every script under `tools/`, `docs/**/figures/` and `docs/cm/tool-validation/evidence/` in a named row. | Verified | | Closed (iteration 2). Sections 1 (lines 15 to 17) and 3.1 (lines 56 to 58) classify `tools/render_review_figures.py`, `docs/reviews/<REVIEW>/figures/*.py`, `docs/icd/figures/render_icd_figures.py`, `docs/cm/tool-validation/evidence/*.sh` and `*.py` and `tools/tests/*.py` as Class D, elected Class A; every named file exists. The Class D a.1(c) clause cited for the evidence scripts is verbatim at `10-appendixd.md` line 185. The placement rule (line 21) covers `tools/`, `docs/**/figures/`, `docs/cm/tool-validation/evidence/`, the sim folders and `firmware/`. Two script sets outside those directories remain unplaced; raised as finding-7. |
| <a id="finding-4"></a>finding-4 (F-04) | reviewer | Minor | S5 | 03 section 6.3 "Consistency with charter section 12" paragraph; section 6.5 items c, e and h | The charter at `4e3f891` (unchanged in the working tree) already contains what items c, e and h propose: the reuse line reads "Reuse cataloging and Government rights (SWE-147, 148)" without 214 to 217 (charter line 167); the CMMI, IV&V, Center reporting line names SWE-032, 141, 131, 178, 179, 174 and 143 and not SWE-094 or SWE-045 (line 156); and a "Non-custom software testing (SWE-211) / Tailored, proposed for owner decision at SRR" line exists (line 159). Section 6.3 therefore misstates the charter ("SWE-211 T is not yet on the line", "the line also names SWE-094 and SWE-045", "the line also names SWE-214 to SWE-217") and items c, e and h are Open when resolved. Fix: mark c, e and h Resolved by charter `4e3f891` and rewrite the section 6.3 consistency paragraph to the current charter lines. | Verified | | Closed (iteration 2). 03 X c, e and h (lines 322, 324, 341) are Resolved by charter `4e3f891`, and the charter lines match: line 156 (CMMI line, SWE-032, 141, 131, 178, 179, 174, 143 and the chapter 2 SWE-214 to 217 as institutional), line 159 (SWE-211 "Tailored, proposed for owner decision at SRR"), line 167 (reuse line, SWE-147, 148 only). The section 6.3 consistency paragraph (line 300) now states each line as the charter reads it; the O-3 comma is fixed (line 296). |
| <a id="finding-5"></a>finding-5 (F-05) | reviewer | Minor | CL-3 | `docs/safety/hazards.json` HZ-001, HZ-003, HZ-006 and HZ-012 `firmware_role.criteria`, transcribed in 03 section 4.2 | These four hazards record criteria b and c (HZ-003: b and e) but not criterion a, although their own statements make firmware the actor whose incorrect action causes the hazardous condition: a wrong power step or default (5 W instead of 1 W), a tune carrier not ended by the timeout, or a wrong PA bias. SWEHB `swe-205` section 7.1 task 1 asks for "all known software contributions or events where software, either by its action, inaction, or incorrect action, leads to a hazard", and 07 section 14.1 cites the same task. The component set does not change (the PA enable and TX sequencer and the safe-state manager already carry a), so this is Minor. Fix (hazard analysis author, cross item): add criterion a to the four hazards or state in each `firmware_role.statement` why incorrect firmware action is not a contribution; 03 section 4.2 is then re-transcribed (section 6.4 item 9). | Lien | PDR | Lien: fix before PDR (iteration 3; convergence rule of 2026-09-26, charter section 4 item 3). At HEAD `hazards.json` 0.4.2-pha (blob `37d6cc83`) still records HZ-001 b, c; HZ-003 b, e; HZ-006 b, c; HZ-012 b, c, with no `firmware_role.statement` reason; 03 section 4.3 criterion a paragraph (line 180) and item X15 (line 344) carry it. Owner: hazard analysis author, then 03 re-transcription. Iteration 2 disposition: Open (iteration 2). Not fixed where the finding lies: `hazards.json` 0.4.0-pha (blob `89d0cbc3`) still records HZ-001 b, c; HZ-003 b, e; HZ-006 b, c; HZ-012 b, c, and no `firmware_role.statement` explains why incorrect firmware action is not a contribution. 03 now records its own reading that criterion a is met (section 4.3, criterion a paragraph, widened to nine hazards) and routes the fix as item X15 to the hazard analysis author; that is correct tracking, not closure. Owner of the fix: hazard analysis author, then 03 re-transcription; due before the SRR readiness declaration (03 X15). |
| <a id="finding-6"></a>finding-6 (F-06) | reviewer | Minor | S5 | 03 section 2 (tailoring paragraph), section 4.4 (human safety risk sentence), section 9 signature block risk-taker line | NPR 7150.2D section 2.2.1 (corpus `02-chapter2.md` line 221): "For tailoring involving human safety risk, the actual risk taker(s) (or official spokesperson[s] and appropriate supervisory chain) need to formally agree to assume the risk." 03 section 4.4 names the friends who operate the radios (SI-019) and bystanders as bearers of the SWE-022, SWE-023 and SWE-219 tailoring risk, yet only the owner formally accepts it; other operators are "informed" through the operations handbook. Informing is not formal agreement, and 03 does not claim the owner as official spokesperson for them. Fix: add a formal acceptance step for each operator before hand-over (for example a signed acceptance line in `docs/vv/adp/CWHT-A-NNN/as-built.md`), or record, for the owner's decision at SRR, that the owner acts as the official spokesperson for other operators and bystanders, with the rationale, and add the matching line to the section 9 signature block. | Verified | | Closed (iteration 2). Section 2 (line 28) and the new section 4.4 risk-taker table (lines 204 to 212) give each group a formal agreement: the owner at SRR; each other operator by a signed acceptance line in the unit's `as-built.md` before hand-over; the owner as official spokesperson for bystanders and household members with a stated rationale. The quoted NPR 7150.2D section 2.2.1 sentence is verbatim at `02-chapter2.md` line 221. Section 9 carries the spokesperson signature line (line 392); section 6.4 item 3 lists it; `rmm.json` SWE-022, SWE-023 and SWE-219 `residual_risk` carry the same text. The template and hand-over precondition are 03 item X18 (lead SE, before SAR), which does not block this finding because no hand-over occurs before SAR. |
| <a id="finding-7"></a>finding-7 (F-07, new at iteration 2) | reviewer | Minor | S1 (SWE-020) | 03 section 1 placement rule (line 21) | The placement rule assigns a row only to scripts under `tools/`, `docs/**/figures/`, `docs/cm/tool-validation/evidence/`, `hardware/sim/`, `docs/research/sim/` and `firmware/`. Two sets of project software lie outside those directories and no row names them: (1) `docs/research/emulator-accreditation-assets/` (committed at `2d3c4d8`): Rust probe firmware `fw/src/bin/*.rs`, `fw/src/rt.rs`, `fw/build.rs` and the TypeScript harness `harness/cwht-accredit.ts`, `cwht-regprobe.ts`, `cwht-gpioc-probe.ts`, which produce the emulator accreditation evidence that section 4.3.1 relies on for `cwht-emu` (ACC-EMU-001); this reviewer missed them at iteration 1; (2) `docs/vv/reports/TC-SW-TOOL-001-r1/gate-known-answer.sh` (untracked, written 2026-09-25 22:50), a known-answer script for the gate tooling. Neither changes a class (each is Class D by a.1(b) or a.1(c), elected Class A, like the evidence scripts). Fix: name both in sections 1 and 3.1, or widen the placement rule to "every script or program in the repository", with `docs/research/**` and `docs/vv/reports/**` scripts assigned to the tool-validation evidence row. | Lien | PDR | Lien: fix before PDR (iteration 3; convergence rule). At HEAD the placement rule (03 line 21) is unchanged and both sets are committed and unnamed: `docs/research/emulator-accreditation-assets/fw/` (`build.rs`, `src/bin/*.rs`) and the harness scripts, and `docs/vv/reports/TC-SW-TOOL-001-r1/gate-known-answer.sh`, now joined by `docs/vv/reports/TC-SW-TOOL-001-r2/gate-known-answer.sh` (`git ls-files`). Owner: 03 author. |
| <a id="finding-8"></a>finding-8 (F-08, new at iteration 3) | reviewer | Minor | CL-4 | 03 section 4.2 table (lines 116 to 129), the 0.4.0-pha hash of line 112 and the "Current input" paragraph (line 148) | Section 4.2 does not equal the committed `hazards.json`. The table was transcribed from the uncommitted 0.4.0-pha working file (SHA-256 `f9325b36...`, line 112), and the committed 0.4.0-pha (`08d1496`, SHA-256 `18fbf5ed...`) added content under the same version label that 0.4.2-pha keeps. Reviewer's script over the 15 rows against HEAD 0.4.2-pha: criteria, `safety_critical`, every component string and every Software control id and status are equal, but five `control_req_ids` lists lack a back-link the file carries (HZ-004 K1 REQ-SW-KEYER-035, K7 REQ-SYS-183, K8 REQ-SW-KEYER-034, K9 REQ-SW-KEYER-036; HZ-010 K3 REQ-SW-KEYER-036), and two condensed control texts contradict the file: HZ-010 K3 says debounce "configurable 1 to 20 ms" where the file says "fixed counts ... not operator-configurable", and HZ-007 K4 gives pack thresholds 6.4 V and 6.0 V where the file states per-cell thresholds of 3.20 V and 3.00 V. Line 148 says 0.4.2-pha was "checked field by field against the committed 0.4.0-pha file" and that "every `control_req_ids` list [is] unchanged ... so no re-transcription is needed". Measured from the committed 0.4.0-pha, that is true. It is not true of the table, which predates that commit. The safety-critical set, the criteria unions and section 5 are unaffected, so the finding is Minor. Fix: re-transcribe the Software-control column from 0.4.2-pha (section 6.4 item 9), state the committed hash only, and correct line 148 | Lien | PDR | Lien: fix before PDR (convergence rule). Owner: 03 author. |
| <a id="finding-9"></a>finding-9 (F-09, new at iteration 3) | reviewer | Minor | S5 | 03 header (lines 3 and 5), section 3.3 (line 84), section 4.2 (line 112), section 6.1 (line 246), section 6.3 status rule (line 300); `rmm.json` SWE-020 implementation | Several status statements are stale at HEAD (charter section 11 rule 2): `hazards.json` 0.4.0-pha described as a "working-tree file ..., not yet committed" (lines 5 and 112), although it is committed and superseded by 0.4.2-pha; the command results of section 6.1 ("34 passed, 2 failed"; "331 tests, 1 failure") no longer match (validate_docs exits 0 on the HEAD tree, 37 passed; unittest 392 tests OK); line 300 and `rmm.json` SWE-020 describe INSP-009 and INSP-017 as "at iteration 1 with verdict NEEDS CHANGES"; line 84 says iteration 2 verifies this revision. None changes a class, a determination or a disposition. Fix: refresh these statements when the RMM rows move under section 6.4 item 7 | Lien | PDR | Lien: fix before PDR (convergence rule). Owner: 03 author. |

## Readiness criteria (all true before the review starts)

| # | Criterion | Result | Evidence |
|---|---|---|---|
| R1 | `tools/validate_docs.py` exits 0 (includes `hazards.json` and `rmm.json`) | Not met (outside the product) | Run 2026-09-25 before this record: exit 1, "validate_docs: 27 passed, 1 failed, 28 checked"; `docs/process/rmm.json` and `docs/safety/hazards.json` PASS; the only failure is `docs/design/allocation.json` ("schema not found: docs/design/allocation.schema.json"), which 03 section 6.1 already reports. Recorded as `readiness_met: false`; the review proceeded at the dispatching session's direction. |
| R2 | `tools/render_rmm.py --check` exits 0 | Met | Exit 0: "rmm.json OK: 100 rows; FC=75, T=17, NA=8; In place=37 [...]"; "rmm.md is current". `tools/tests/test_render_rmm.py`: 20 tests OK, as 03 section 6.1 states. |
| R3 | The `hazards.json` version transcribed is stated, and every difference from the current file is an open item of section 6.5 | Met | 03 header and section 4.2 state 0.3.0-pha with SHA-256 `e008671c...e3be37`; `shasum -a 256 docs/safety/hazards.json` gives the same value and the file's `version` field is `0.3.0-pha`, so no difference exists (CL-4). |

## Participants

Author `author:classification-rmm` (not present). Reviewer `reviewer:classification` (this section). Software assurance reviewer: required (03 is a whole-product item of 07 section 2.1.1; `tools/validate_docs.py` `ASSURANCE_WHOLE_PRODUCTS`); a separate invocation, not yet run, adds its verdict, findings and applied SWEHB tasks (for example `swe-020` section 7.1 task 1 and `swe-205` section 7.1 tasks 1 to 4) to this file. Owner: resolves the findings as ETA and SMA TA in the SRR decision memo section 11 (03 section 3.3).

## Checks (copied from 03 section 3.3)

| # | Check | Answer | Evidence |
|---|---|---|---|
| CL-1 | Each App. D factor score of section 3.1 is consistent with D.1 and the App. D class definitions | Concur | D.1 (`10-appendixd.md` line 9) names the five factors 03 scores; D.2 (line 11) "assign the higher of the classes". Classes A to C all presuppose NASA space, aeronautics or facility use (lines 15 to 172), so "Excludes Classes A, B, C" holds. Human dependence row cites Class E a.3 ("Class E software cannot be safety-critical software. If the software is classified as safety-critical software, then it has to be classified as Class D or higher", line 237) and exclusion c.8 ("Software that is safety-critical", line 263), both verbatim in the corpus, and SWEHB 7.02 section 1.2 ("All Safety-critical software has to be classified as Class D or higher"). The section 3.1 conclusion states honestly that App. D does not apply to cwht and that the placements are by analogy (charter section 1). |
| CL-2 | Class of each section 3.1 item follows from the cited App. D clause and D.2 | Concur, per item | `cwht-fw` D: floor fixed by Class E a.3 and c.8 plus D.2; no Class D definition fits a radio literally, which the section 3.1 conclusion discloses. Firmware test tooling D: Class C example b.1 "simulators, emulators, or facilities used to test Class A, B, or C software in development" (line 157) read by analogy; Class E a.4 "does not support ground tests" (line 239) and c.6 "used in technical decisions concerning operational systems, or systems being developed for operation" (line 259). `traceability.py`, `validate_docs.py` D: Class D a.1(b) "Ground software tools that support engineering development" (line 183), example b.1 "project assurance databases (... requirements management databases)" (line 209), Class E c.5 "can adversely affect the integrity of engineering/scientific artifacts" (line 257) and c.6. Render tools D: a.1(b), b.1, c.5. Gate scripts D: c.6. Release tooling D: example b.1 "integrated build management systems", c.5. Simulation decks D: example b.1 "Engineering design and modeling tools (e.g., computer-aided design ..., thermal/structural analysis tools)". `tools/refs/*.py` E: example b "file format converters" (line 243); the c.5 non-applicability argument (third-party reference, cross-checked by `render_rmm.py`) is reasonable. Items missing from the table: finding-3. |
| CL-3 | Each hazard's `firmware_role.criteria` is supported by its narrative and by para 3.2 | Dissent in part (finding-5) | Para 3.2 criteria a to e verified verbatim in `swehb/7-02-classification-and-safety-criticality.md` section 1.2 (lines 58 to 66). Per-hazard table below. |
| CL-4 | Section 4.2 equals `hazards.json` (ids, criteria, components verbatim) | No differences in content | Script over the 15 section 4.2 rows against `hazards.json` 0.3.0-pha (reviewer's own, in the scratch directory): title, severity, likelihood, initial risk, criteria, `safety_critical`, every `firmware_role.components` string, and every Software-type control id, status (P or RP) and `control_req_ids` list equal the file for all 15 hazards; each hazard's `requirement_ids` equals the union of its controls' `control_req_ids`. Only difference: the Exposed column writes the `exposed` values in lower case after the first ("Operator, household member" for `["Operator", "Household member"]`), a typographic variance, not raised. The 0.2.0-pha to 0.3.0-pha diff (`git show 28e49e6:docs/safety/hazards.json` against the working tree) changes no `firmware_role` criteria, flags or `swe134_items`; it changes the HZ-008 verification-unit component string and HZ-008 K7 status, and also adds or re-statuses Hardware interlock and Design controls (HZ-001 K10, HZ-003 K9 and K10, HZ-004 K12, HZ-006 K10, HZ-011 K3, HZ-012 K6, HZ-014 K8) with REQ-SYS-130, 180, 181 and 182 in `requirement_ids`; none is of type Software, so 03's X13 statement "0.3.0-pha changed no `firmware_role` criteria or `swe134_items` from 0.2.0-pha" holds. |
| CL-5 | Each section 4.3 criteria cell equals the union over the hazards naming the component; each type (ii) finding states hazard, criterion and why | Concur, per component | Unions recomputed from `hazards.json`: Keyer HZ-001, 004, 010 gives a, b, c; PA enable and TX sequencer HZ-001, 003, 004, 006, 007, 008, 011, 012 gives a, b, c, e; Battery HZ-002, 007, 011 gives c, e; Thermal HZ-003 gives b, e; Audio HZ-005 gives b, c; Safe-state manager HZ-001 to 007, 011, 014 gives a, b, c, e; Scheduler HZ-001 to 007, 011, 012 gives a, b, c, e (exactly the hazards whose `swe134_items` include j, as 03 says); Frequency control and Frequency verification unit HZ-008 give a, c, e. All ten cells and hazard lists match 03 section 4.3. The two HZ-008 type (ii) findings (safe-state manager c and e; scheduler c) each state the hazard, the criterion and the reason, and neither changes a union. Section 5 Hazards column recomputed from `swe134_items` for items a to l: all twelve lists match. |
| CL-6 | Section 4.3.1 determination for the verification software and its rigor | Concur | The SWEHB 7.02 section 1.2 sentence quoted in 4.3.1 is verbatim (line 70). The "none" basis (host-side, in no hazard's causal chain, failure mode a false pass controlled by rigor and independence) is sound; the rigor column is concrete and checkable: the three `traceability.py` checks `HAZARD_REQ_NOT_TESTED`, `HAZARD_UNRESOLVED` and `VERIFIED_WITHOUT_EVIDENCE` exist in `tools/traceability.py` and are asserted in `tools/tests/test_traceability.py` (5, 1 and 1 occurrences). The `image_trailer.py` argument (a wrong trailer fails safe at boot; a correct trailer over a wrong build is caught by the rebuild check and `picotool verify`) is consistent with 05 section 8.1 as cited. |
| CL-7 | Mission-critical list of section 4.3 against the App. A definition | Dissent (finding-1) | App. A definition verified verbatim (`07-appendixa.md` line 71). Concur with the listed mission-critical items (frequency control outside the word path, ALC and envelope shaper, receive-chain control, configuration store and non-safety fields, frequency display, encoder input) and with their rationale. Dissent: menu handling for key-input and keyer-mode selection meets the same definition (finding-1). |
| CL-8 | Every difference between section 4.3 and 07 section 14.1, and between section 4.3 and `hazards.json`, is an open item of section 6.5 | Differences not listed (finding-2) | 4.3 against `hazards.json`: the only differences are the two HZ-008 type (ii) findings, listed as X14. 4.3 against 07 section 14.1 (working tree): X1 and X3 list differences that no longer exist and omit the remaining ones (finding-2). |
| CL-9 | Overall classification and safety-critical determination | Concur with the classification and the safety-critical set; dissent on the mission-critical set | Class A elected for every item Class D by the letter, Class E for the reference-corpus converters (not elected), recorded in `rmm.json` `meta.software_class_elected` "A" and `meta.software_class_app_d_assessment`, agree with 03 section 3.2. The safety-critical set of section 4.3 follows from `hazards.json` 0.3.0-pha by the section 4.1 step 3 rule, with the HZ-008 rows correctly marked proposed for package decisions 9 and 40 and the decline paths stated. The mission-critical set lacks the key-input and keyer-mode selection path (finding-1, Major). Verdict NEEDS CHANGES. |

### CL-3 per-hazard results

| Hazard | Criteria; flag | Result | Basis |
|---|---|---|---|
| HZ-001 | b, c; true | Concur with b, c; a missing (finding-5) | Statement: firmware controls when RF exists, the power step and default, the tune timeout; an incorrect action of these causes the exposure |
| HZ-002 | c, e; true | Concur | Charger supervision, dissimilar sensing, disable and report; firmware is not in the primary protection path (charger IC hardware limit) |
| HZ-003 | b, e; true | Concur with b, e; a missing (finding-5) | Firmware sets PA bias and power; an incorrect bias causes the over-temperature |
| HZ-004 | a, b, c; true | Concur | Keyer and sequencer faults cause stuck transmission; the SWE-134 note on commanding the hazardous operation applies |
| HZ-005 | b, c; true | Concur | The hardware ceiling (K1, 100 mVrms) bounds any firmware fault, which supports omitting a |
| HZ-006 | b, c; true | Concur with b, c; a missing (finding-5) | Same functions as HZ-001 plus the guest lock |
| HZ-007 | c, e; true | Concur | Discharge-side window, inhibit, lock-out and report; protector IC and fuse act without firmware |
| HZ-008 | a, c, e; true (proposed) | Concur | C7: one fault in the frequency-word path puts 5 W on 150 to 174 MHz, passed by the filter; K7 mitigates, detects and reports |
| HZ-009 | none; false | Concur | Mechanical |
| HZ-010 | c; true | Concur | Debounce, stuck-input detection and range checks mitigate; protection itself is hardware |
| HZ-011 | c, e; true | Concur | VBUS disarm and charge pause mitigate; detection and report on the LCD |
| HZ-012 | b, c; true | Concur with b, c; a missing (finding-5) | Same functions as HZ-001 (tune timeout, power step) |
| HZ-013 | none; false | Concur | Mechanical |
| HZ-014 | a, c, e; true | Concur | A loaded image is a potential cause; boot-path integrity, configuration guard and safe defaults |
| HZ-015 | none; false | Concur | Assembly hazard |

## Supplementary items (SWE-020, SWE-125, SWE-139, SWE-176 minimum content)

| # | Check | Answer | Evidence |
|---|---|---|---|
| S1 | SWE-020 (NPR 7150.2D 3.5.1, verified in `03-chapter3.md`): each system and subsystem containing software is classified at the highest applicable App. D class, and software assurance performs or concurs (the paragraph after the Note, verified verbatim) | No (finding-3) | Section 1 and 3.1 classify the firmware CSCI, its test tooling, auto-generated code, the listed engineering tools and the converters; several project scripts are unclassified (finding-3). The concurrence mechanism (section 3.3, this record, owner resolves dissent in memo section 11) matches the NPR paragraph and SWEHB `swe-020` section 7.1 task 1 ("Perform a software classification or concur with the engineering software classification"). `rmm.json` SWE-020: FC, In place, independent concurrence "Planned for SRR" with placeholder `INSP-NNN` (now INSP-009; cross item). |
| S2 | SWE-125 (3.1.13): an RMM (one or several) against the NPR requirements, including delegated or contracted ones | Yes | `rmm.json` has 100 rows, `render_rmm.py --check` exit 0. Reviewer's own parse of `09-appendixc.md` Table 2: 100 SWE rows, X counts A 100, B 100, C 92, D 64, E 12; no row is X for A without B; every D and E row is also an A row; the 12 Class E rows are SWE-013, 020, 022, 033, 042, 121, 125, 139, 148, 156, 176, 205; the 36 Class A rows without a Class D X include every id 03 section 3.2 item 1 names. All match 03 sections 3.2 and 6.1.1. The row states no delegated or contracted components exist, consistent with charter section 12 (contracted-effort line). |
| S3 | SWE-139 (3.1.11): compliance with every X for the class, and the disposition rules | Yes | Every Class A row addressed: FC 75, T 17, NA 8; the T and NA id lists of 03 section 6.3 equal the renderer's lists (17 and 8 ids, checked one by one). T and NA rows carry `tailoring_rationale` and `residual_risk` (schema-enforced). Tailoring authority text checked against NPR 7150.2D sections 2.2.1, 2.2.5 Note, 2.2.6 and App. C.3 (all verbatim in the corpus). |
| S4 | SWE-176 (3.5.2): records of each classification determination, each RMM and each independent classification assessment kept for the life of the project | Yes | Git retention (03 section 6.4 item 6); this record is the first independent assessment, filed at the path 03 section 3.3 and the RMM rows SWE-020, SWE-176 and SWE-205 name. |
| S5 | 03 statements about other controlled documents and NASA text are true of the repository (charter section 11 rule 2) | No (finding-4, finding-6) | Charter section 12 lines misstated (finding-4); NPR 7150.2D section 2.2.1 risk-taker agreement incompletely applied (finding-6). Other checks passed: SWE-205 text (3.7.1), SWE-223 (2.1.2.7), SWE-150 (2.2.7), SWE-021 (2.2.8), SWE-126 (2.1.8.2), CHMO authority (2.1.4.2) verified at their lines in `02-chapter2.md`; REQ-SW-SAFE-001 to 012 all present in 07; 03 section 6.1's statement of command results (command 1 exit 1 on `allocation.json` only, command 4 "331 tests, 1 failure: `test_repository_exit_zero`") reproduced exactly on 2026-09-25. |

## Observations (not findings)

- **O-1.** `rmm.json` rows SWE-020, SWE-176 and SWE-205 cite the concurrence record with `id INSP-NNN` and "Planned for SRR". The record now exists as INSP-009 with verdict NEEDS CHANGES; the 03 author updates those rows when the record is Closed (03 section 6.4 item 7). Cross item for Claude.
- **O-2.** The author's context note that 0.2.0-pha to 0.3.0-pha changed only the HZ-008 verification-unit string and K7 status is incomplete (CL-4 row lists the Hardware and Design control changes). The product text itself is accurate.
- **O-3.** 03 section 6.3 has a missing comma: "SWE-210 (cybersecurity scope) SWE-219". Editorial.
- **O-4.** The transcribed controls repeat two different bench test-mode timeouts under REQ-SYS-179 (HZ-004 K13 "120 s (TBR)", HZ-005 K9 "60 s (TBR)"), while REQ-SYS-179 itself has `tbr: null` and states entry only. The transcription is faithful to `hazards.json`; the inconsistency belongs to the hazard analysis and the requirements author (cross item).

## Tool runs (2026-09-25, reviewer)

| Command | Exit | Output (summary) |
|---|---|---|
| `.venv/bin/python tools/validate_docs.py` (before the record) | 1 | 27 passed, 1 failed: `docs/design/allocation.json` schema not found (outside product) |
| `.venv/bin/python tools/render_rmm.py --check` | 0 | 100 rows; FC 75, T 17, NA 8; In place 37; rmm.md current |
| `.venv/bin/python tools/traceability.py --report-only` | 0 | 231 requirements, 167 test cases, 0 violations, 42 warnings |
| `.venv/bin/python tools/render_risk.py --check --gate SRR --hazards docs/safety/hazards.json` | 1 | "HZ-008: related_risk_ids does not name RSK-046, which carries it" (outside product; cross item) |
| `.venv/bin/python tools/render_compliance.py --check` | 0 | current |
| `.venv/bin/python -m unittest discover -s tools/tests` | 1 | 331 tests, 1 failure `test_validate_docs.RepositoryTests.test_repository_exit_zero` (the `allocation.json` cause) |

## Verdict

```
VERDICT: NEEDS CHANGES
FINDINGS:
- [Major] CL-7 03 section 4.3: menu handling of key-input and keyer-mode selection (REQ-SYS-056, REQ-SYS-040, REQ-SYS-163; SI-018) meets the App. A mission-critical definition and is classified neither.
- [Minor] CL-8 03 section 6.5 X1, X3 and section 4.3: stale against the current 07; remaining differences unlisted.
- [Minor] S1 SWE-020: project scripts missing from sections 1 and 3.1.
- [Minor] S5 03 section 6.3 and 6.5 c, e, h: charter section 12 misstated; items already resolved.
- [Minor] CL-3 hazards.json HZ-001, HZ-003, HZ-006, HZ-012: criterion a not recorded for incorrect firmware action.
- [Minor] S5 NPR 7150.2D section 2.2.1: formal agreement of the other risk takers not provided.
ITEMS N/A: none
MEASUREMENTS: size=8 classification rows, 10 components, 5 verification items, 100 RMM rows; items checked=17 (R1 to R3, CL-1 to CL-9, S1 to S5); items answered No or Dissent=6; major=1; minor=5; fixed=0; deferred=0; iteration=1; turns=38; minutes=55
```

## Closure (iteration 2, 2026-09-26)

**Re-review scope.** `reviewer:classification`, a new invocation of the same role, independent of the author; the product was not edited. The author reported finding-1 to finding-4 and finding-6 fixed (with INSP-017 finding-1, 2, 4, 5 and 6 applied in the same revision) and disputed none; finding-5 was not reported. Re-read in full: 03 fourth revision (blob `fdc8d0764e7ee513a05215de7dfb580687b721d4`, 395 lines); `rmm.json` rows SWE-020, 022, 023, 134, 176, 205, 219 and `meta.software_class_app_d_assessment` (blob `78c3b236`); inputs `hazards.json` 0.4.0-pha (blob `89d0cbc3`, SHA-256 `f9325b36...51d59d1`, equal to the hash 03 section 4.2 states), 07 (blob `1b8864b0`) lines 571 to 617 and 773, charter section 12 (lines 150 to 167, unchanged since `4e3f891`), `requirements.json` REQ-SYS-040, 056, 136, 163. Search first: `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any `grep` (queries: peer-review record closure block and dispositions; the 07 `SW-SCHED` stale re-transcription note; `PEER_REVIEW_RECORD_SCHEMA` assurance fields). `grep -n` then pinned lines only. The tool was available throughout.

**Dispositions.**

| Disposition | Count | Findings |
|---|---|---|
| Closed (fix verified in the product, state Verified) | 5 (Major 1, Minor 4) | finding-1, finding-2, finding-3, finding-4, finding-6 |
| Disputed accepted | 0 | none disputed |
| Open | 2 (Minor) | finding-5 (`hazards.json` criteria unchanged; tracked as 03 X15, hazard analysis author); finding-7 (new: two script sets outside the placement rule) |

Open Major: 0. Open Minor: 2.

**Iteration 2 answers** (items that changed; all others stand as at iteration 1).

| Item | Answer | Evidence |
|---|---|---|
| R1 | Not met (outside the product) | `validate_docs.py` exit 1: 34 passed, 2 failed, both outside the product (`docs/design/allocation.json` and `docs/plan/measurements.json`, schema not found); `rmm.json`, `hazards.json` and this record PASS |
| R2 | Met | `render_rmm.py --check` exit 0: 100 rows, FC 75, T 17, NA 8, In place 37, `rmm.md` current |
| R3 | Met | 03 header and section 4.2 state 0.4.0-pha with SHA-256 `f9325b36...`, equal to `shasum -a 256`; the 0.3.0-pha to 0.4.0-pha differences are listed in section 4.2 |
| CL-2 | Concur, per item | New rows checked: figure generators Class D a.1(b), b.1, E c.5; evidence scripts Class D a.1(c) (line 185, verbatim) and E a.4, c.6; tool tests Class D by the Class C b.1 analogy; NODIS converters Class D by E c.6 and c.5 (INSP-017 finding-5), guidance-corpus converters Class E with the c.5 and c.6 reasoning stated; `cwht-fw` "no class fits by the letter; Class D is the floor" (INSP-017 finding-4) with exclusion c.1 read strictly. Unplaced scripts: finding-7 |
| CL-3 | Dissent in part (finding-5) | `hazards.json` 0.4.0-pha criteria for HZ-001, 003, 006 and 012 unchanged |
| CL-4 | No differences in content | Reviewer's own script over the 15 section 4.2 rows against 0.4.0-pha: criteria and flag, every component string, and every Software control id, status and `control_req_ids` set equal the file; 0 differences |
| CL-5 | Concur, per component | 0.4.0-pha changes no `firmware_role` or `swe134_items`, so the iteration 1 unions stand. The new menu override command path row (INSP-017 finding-1) is a type (ii) finding that states hazards (HZ-001, 004, 005, 006), criterion a and the reason, and is routed to `hazards.json` as X16 |
| CL-7 | Concur | finding-1 closed; the mission-critical set now includes the key-input and keyer-mode selection path |
| CL-8 | Concur | finding-2 closed; X1 (viii) to (xii) list every difference between section 4.3 and the current 07 section 14.1 and 14.2 that this reviewer found; X14, X15 and X16 list the differences from `hazards.json` |
| CL-9 | Concur, with finding-5 and finding-7 riding as Minor | Classification, safety-critical set (with the proposed rows for package decisions 9 and 40 and item X20) and mission-critical set are consistent with sections 3 and 4 and with `rmm.json` meta, SWE-023, SWE-134 and SWE-205 |
| S1 | No (finding-7) | Iteration 1 items classified (finding-3 closed); two further script sets unplaced |
| S4 | Yes | Section 3.3 names both assessment records, INSP-009 and INSP-017, with paths; `rmm.json` SWE-020, 176 and 205 cite both. Front matter of this record now points `assurance_reviewer_agent` and `assurance_verdict` to INSP-017 (the reviewer's part of 03 X19) |
| S5 | Yes | finding-4 and finding-6 closed; the NPR 7150.2D section 2.2.1 sentence is verbatim at `02-chapter2.md` line 221 |

**Commands run (2026-09-26, iteration 2).**
- `validate_docs.py` exit 1 (R1 above; product files and this record PASS).
- `traceability.py --report-only --output <scratchpad>/tr.md` exit 0: 237 requirements, 170 test cases, 0 violations, 7 warnings.
- `render_risk.py --check --gate SRR --hazards docs/safety/hazards.json` exit 0 (65 risks, 159 candidates, 0 warnings).
- `render_rmm.py --check` exit 0.
- `render_compliance.py --check` exit 0.
- `python -m unittest discover -s tools/tests` exit 1: 331 tests, 1 failure, `test_validate_docs.RepositoryTests.test_repository_exit_zero` (the two missing schemas above).

**Verdict.** Zero unresolved findings of the blocking severity. `readiness_met` stays false only because R1 fails on files outside the product, and the validator ties APPROVED to `readiness_met` true, so the recorded verdict is NEEDS CHANGES. It becomes APPROVED, with finding-5 and finding-7 riding as Minor findings (08 section 3.2), once `validate_docs.py` exits 0 and INSP-017 concurs at its iteration 2. `record_status` stays Open for the lead SE to set Closed with `date_closed` (07 section 10.2) once finding-5 and finding-7 are Verified or deferred by the owner with a decision reference and a gate.

```
ITERATION 2 (2026-09-26): VERDICT: NEEDS CHANGES (readiness R1 outside the product). Closed 5 (finding-1, finding-2, finding-3, finding-4, finding-6; Major 1, Minor 4); Disputed accepted 0; unresolved 2 Minor (finding-5, finding-7); unresolved Major 0.
```

## Iteration 3 (2026-09-26)

**Scope and baseline.** `reviewer:classification`, a new invocation of the same role, independent of the author. The product was not edited. Review baseline HEAD `adcfe0946d2f1b5cd8f41a8f91eb4219a7fb99a1`; the working tree equals HEAD for every product and input file (`git diff --quiet HEAD -- docs/process docs/safety`). Committed blobs reviewed (`git rev-parse HEAD:<path>`): 03 `ed270f443e2ab648480017df8ad3d0221400cf4c` (396 lines, read in full), `rmm.json` `30fcde240eeb6a147359de8c5d8cdd93364dc9c8` (rows SWE-020, 023, 134, 176, 205 and `meta`), `rmm.md` `7337d1bf870e4cd0b82f3435140f0d2edcdfe63c` (currency by `render_rmm.py --check`). Inputs: `hazards.json` 0.4.2-pha, blob `37d6cc83`, SHA-256 `6b69a00f...8cf3c7` (equal to the hash 03 line 148 states); 07 blob `d0f8baf6`, section 14.1 (lines 579 to 607). The iteration 2 blobs (03 `fdc8d076`, `rmm.json` `78c3b236`, `rmm.md` `fe374a48`) are not in the object store (`git cat-file -e` fails), so no diff against them exists. This iteration therefore re-read the whole of 03 at HEAD. It diffed `b301df2..HEAD` for the three products: 03 gains the line 148 "Current input" paragraph, and `rmm.json` changes only in the SWE-200 implementation text. It diffed `hazards.json` field by field from the committed 0.4.0-pha (`1543c9f^`) to HEAD. Search first: `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (query: peer-review record iteration 3 lien table, convergence rule, record drift and `product_files`). `grep -n` was used afterwards only to pin lines. The tool was available throughout. Convergence rule applied: lead SE direction of 2026-09-26 under charter section 4 item 3 (a Minor RID is fixed before the next review and does not block the baseline).

**Disposition of every finding at HEAD.**

| Finding | Severity | Iteration 3 disposition | Evidence at HEAD (03 blob `ed270f44` unless named) |
|---|---|---|---|
| finding-1 | Major | Closed (Verified) | Key-input and keyer-mode selection path mission-critical: section 4.3 line 184; section 5 rows a, b, g (lines 226, 227, 232) and k; section 4.3 "Not safety-critical" paragraph line 186; section 9 lines 375 and 377; `rmm.json` SWE-134 names the "key-input and keyer-mode selection path"; 07 line 605 and the `SW-DISPLAY` row line 648 carry it |
| finding-2 | Minor | Closed (Verified) | Scheduler row "at most 2 s, REQ-SYS-131" line 164; drivers row names conditional WP-SW-14 line 168; X1 line 329 and X3 line 331. 07 at `d0f8baf6` now carries the HZ-008 type (ii) findings on `SW-SAFE` and `SW-SCHED`, and the stale notes are gone (07 lines 581, 594 and 597), consistent with X1's "Resolved 2026-09-26 for 07" |
| finding-3 | Minor | Closed (Verified) | Sections 1 (lines 15 to 17) and 3.1 (lines 56 to 58) |
| finding-4 | Minor | Closed (Verified) | Section 6.3 consistency paragraph line 302; X c, e and h lines 324, 326 and 343 match charter lines 156, 159 and 167 |
| finding-5 | Minor | Lien: fix before PDR | `hazards.json` 0.4.2-pha criteria for HZ-001, 003, 006 and 012 unchanged; tracked as 03 X15 (line 344) |
| finding-6 | Minor | Closed (Verified) | Section 2 line 28; risk-taker table lines 208 to 212; signature block lines 393 and 394 |
| finding-7 | Minor | Lien: fix before PDR | Placement rule line 21 unchanged; the two script sets remain unnamed and a third evidence script (`TC-SW-TOOL-001-r2/gate-known-answer.sh`) joins them |
| finding-8 (new) | Minor | Lien: fix before PDR | Section 4.2 control column differs from the committed file in five `control_req_ids` lists and two condensed texts; line 148's no-re-transcription statement rests on the committed 0.4.0-pha, not on the table |
| finding-9 (new) | Minor | Lien: fix before PDR | Stale status statements at lines 3, 5, 84, 112, 246 and 300 and in `rmm.json` SWE-020 |

Closed 5 (Major 1, Minor 4); Disputed-accepted 0; Lien 4 (all Minor); no Major finding remains unresolved; no finding needs an owner ruling.

**New-defect scan (text changed since the iteration 2 quotes).** Every section was re-read. The changed text (line 148; `rmm.json` SWE-200) and every passage the iteration 2 quotes cited were checked against their sources. No new Major defect was found. The classification (section 3), the safety-critical set, the proposed HZ-008 and menu override command path rows and the mission-critical set (section 4.3) are unchanged in substance. They are consistent with `hazards.json` 0.4.2-pha `firmware_role` and `swe134_items`, which the reviewer's own script recomputed, and with 07 section 14.1 at `d0f8baf6`. The two defects found are Minor (finding-8, finding-9). The committed 0.4.0-pha to 0.4.2-pha diff changes only the HZ-004 K2 text, the HZ-004 history and open questions OQ-SAF-017, 019 and 020 (reviewer's own field walk). This confirms the line 148 statement about that interval.

**Iteration 3 answers** (items that changed; all others stand as at iteration 2).

| Item | Answer | Evidence |
|---|---|---|
| R1 | Met | `validate_docs.py --root <scratchpad>/head` on a `git archive HEAD` export: exit 0, 37 passed, 0 failed. In the working tree the run exits 1 only on `docs/reviews/SRR/checklists/risk-register-06.md`, which another invocation is editing uncommitted (outside this product; cross item 2). This record PASSes, with no drift note |
| R2 | Met | `render_rmm.py --check` exit 0: 100 rows; FC 75, T 17, NA 8; In place 39; `rmm.md` current |
| R3 | Met (with finding-8 as a lien) | 03 line 148 states 0.4.2-pha with SHA-256 `6b69a00f...`, equal to `shasum -a 256 docs/safety/hazards.json`; the unlisted control-column differences are finding-8 |
| CL-3 | Dissent in part (finding-5, lien) | Criteria of HZ-001, 003, 006, 012 unchanged at 0.4.2-pha |
| CL-4 | Differences listed (finding-8, lien) | Reviewer's script over the 15 rows against 0.4.2-pha: criteria, flag, components, Software control ids and statuses equal; five `control_req_ids` back-links missing; HZ-010 K3 and HZ-007 K4 texts differ |
| CL-5 | Concur, per component | `firmware_role` and `swe134_items` unchanged from 0.4.0-pha, so the iteration 1 and 2 unions stand |
| CL-7 | Concur | finding-1 stays closed at HEAD |
| CL-8 | Concur | X1 (viii) to (xii) are applied in 07 at `d0f8baf6` (lines 581, 594, 597, 600, 605, 607, 643, 648); X14, X15 and X16 still list the `hazards.json` differences |
| CL-9 | Concur, with four Minor liens | Classification, safety-critical set with its proposed rows (package decision 9, decision 40, item X20) and mission-critical set as at iteration 2 |
| S1 | No (finding-7, lien) | Placement rule unchanged |
| S5 | No (finding-9, lien) | Stale status statements; the charter section 12 statements (finding-4) and the NPR 7150.2D section 2.2.1 quotation (finding-6) still hold |

**Lien table (convergence rule; carried by the SRR package as Routine items).**

| Lien | Finding | Severity | Product location | Fix | Owner | Due |
|---|---|---|---|---|---|---|
| L-1 | finding-5 | Minor | `hazards.json` HZ-001, 003, 006, 012 `firmware_role` (03 X15) | Add criterion a or state in `firmware_role.statement` why incorrect firmware action is not a contribution; re-transcribe 03 sections 4.2 and 4.3 | Hazard analysis author, then 03 author | Before PDR |
| L-2 | finding-7 | Minor | 03 section 1 placement rule and section 3.1 | Name `docs/research/emulator-accreditation-assets/` (probe firmware and harness) and `docs/vv/reports/**/gate-known-answer.sh`, or widen the rule to every script or program in the repository | 03 author | Before PDR |
| L-3 | finding-8 | Minor | 03 section 4.2 table, line 112 hash, line 148 | Re-transcribe the Software-control column from 0.4.2-pha, cite the committed hash only, correct the line 148 statement | 03 author | Before PDR |
| L-4 | finding-9 | Minor | 03 lines 3, 5, 84, 112, 246, 300; `rmm.json` SWE-020 | Refresh the status statements to the committed state and the current tool results | 03 author | Before PDR |

**Cross items (outside this record's scope; for the lead SE).**
1. Package decision 9 (`package.md` line 745) names the menu override command path. It does not name the mission-critical key-input and keyer-mode selection path (INSP-009 finding-1), nor the partitioning alternative, both of which 03 item X20 (line 349) asks the package to carry. X20 still states that "Neither has a package decision number". Reconcile the two.
2. `docs/reviews/SRR/checklists/risk-register-06.md` (INSP-007, uncommitted edit by another invocation) fails `validate_docs.py` with its open-Major rule: the validator reports that record's finding-9 as unresolved at the blocking severity while its verdict is APPROVED.
3. `validate_docs.py` `open_major_findings` flags any line that contains a `finding-<n>` anchor and the words Major and Open, including summary prose. This iteration reworded two iteration 2 summary lines of this record ("Verdict" paragraph and the ITERATION 2 line) to avoid a false positive; their meaning is unchanged. Tool owner: consider matching the findings table state column only.
4. 03 item X19 (this record's front matter): `assurance_reviewer_agent` and `assurance_verdict` point to INSP-017 (done at iteration 2; `assurance_verdict` updated here to the INSP-017 iteration 3 verdict as filed in the working tree).

**Commands run (2026-09-26, iteration 3).**
- `validate_docs.py`: exit 1 in the working tree (36 passed, 1 failed: `risk-register-06.md`, cross item 2). This record PASSes after the update. The HEAD export gives exit 0 (37 passed).
- `traceability.py --report-only --output <scratchpad>/tr.md`: exit 0; 237 requirements, 170 test cases, 0 violations, 2 warnings.
- `render_risk.py --check --gate SRR --hazards docs/safety/hazards.json`: exit 0; 65 risks, 159 candidates, 0 warnings.
- `render_rmm.py --check`: exit 0.
- `render_compliance.py --check`: exit 0.
- `python -m unittest discover -s tools/tests`: exit 0; 392 tests OK.

No image was produced at this iteration, so no render needed inspection.

```
ITERATION 3 (2026-09-26): VERDICT: APPROVED (with liens). Reviewed HEAD adcfe09: 03 ed270f44, rmm.json 30fcde24, rmm.md 7337d1bf. Closed 5 (finding-1, finding-2, finding-3, finding-4, finding-6); Disputed accepted 0; Lien 4 Minor (finding-5, finding-7, finding-8, finding-9: "Lien: fix before PDR"). Unresolved Major: none.
```

## Post-SRR-ruling delta (iteration 3 re-issue 1, independent reviewer, 2026-09-26)

**Scope and baseline.** `reviewer:classification`, a new invocation of the same role, independent of the author; the product was not edited. Trigger: the owner approved the SRR on 2026-09-26 (disposition Approved with liens L-1 to L-7; `docs/reviews/SRR/minutes.md` lines 21 and 47, "I concur with your recommendations for the key decisions." and "I approve of this and the SRR."), so every decision of `docs/reviews/SRR/decisions-for-owner.md` is ruled as its Recommendation cell states; package item R16 (`package.md` section 2.1) applies the rulings. Review baseline HEAD `1e56df4d3e78c7ca36d10a6834213431bc51993a`; the working tree equals HEAD for the three products and both inputs. Committed blobs reviewed: 03 `ed270f443e2ab648480017df8ad3d0221400cf4c` (unchanged since iteration 3), `rmm.json` `37c6f24df49040c9cdbdf394d9a1370daddc4783`, `rmm.md` `5e6dd864a6fd467c5bba96515e22523dbe06c80c`. Inputs: `hazards.json` 0.5.0-pha, blob `81cacde4`, SHA-256 `2722816228ce865343e9079bfc7341349c57b0268af5adf2f3ce4063fed76de5`; 07 blob `37d472b5` (its only change since `adcfe09` is CR-001 at `4364ebb`, SRR decision 108, which touches no line of section 14.1). Search first: `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (queries: SRR decision RMM approval and SWE-022, SWE-023 tailoring rulings; finding severity definitions for a peer-review record). `grep -n` then pinned lines only. The tool was available throughout.

**Commits since `product_commit` `adcfe09` that touched the products** (`git log adcfe09..HEAD -- <the three product paths>`): one, `9bdf33c` (rmm.json and rmm.md; 03 untouched). One further commit changed a product's check result without touching the product: `0bcea39` (the SRR decision memo), finding-11.

**Delta verification of `9bdf33c` (SRR decisions 6, 7 and 8, owner ruling 2026-09-26).** Reviewer's own field walk of `rmm.json` at `adcfe09` against HEAD: 100 rows both sides, same SWE ids, no change to any `disposition`, `implementation`, `residual_risk`, `authority` or `status`; exactly nine `tailoring_rationale` fields and `meta.approval` changed. Counts at HEAD FC 75, T 17, NA 8, equal to decision 6 ("100 rows: 75 FC, 17 T, 8 NA"). The memo section 7.1 statement that the content approved is that of `ae8abd2` holds: `git rev-parse ae8abd2:docs/process/rmm.json` and `adcfe09:docs/process/rmm.json` both give `30fcde24`, the blob iteration 3 reviewed.

| Change | Ruling cited | Ruling text (Recommendation cell) | Result |
|---|---|---|---|
| `meta.approval`: status "Approved at SRR", `approved_by` the owner as ETA, SMA TA, HMTA and CIO/SAISO designee, `approved_on` 2026-09-26, memo `decision-memo.md` | Decisions 6, 7, 8 | 6 "Approve both reliefs; RSK-010 carries the SWE-219 residual."; 7 "Approve both."; 8 "Accept, with RSK-010 and the hazard analysis as the record." | Correct; the four capacities match the three decisions and the 03 section 9 signature block |
| SWE-211 rationale: approved as ETA and SMA TA (decision 6) | 6 | SWE-211 relief approved | Correct |
| SWE-219 rationale: method approved as ETA and SMA TA (decision 6), RSK-010 carries the residual; risk accepted as HMTA and risk taker (decision 8) | 6, 8 | Both | Correct |
| SWE-022, SWE-023 rationale: HMTA review and risk acceptance, RSK-010 and the hazard analysis as the record | 8 | Accept | Correct |
| SWE-154, 156, 157, 159, 210 rationale: relief approved as CIO/SAISO designee | 7 | Approve | Correct; exactly the five rows decision 7 names |
| `rmm.md` re-rendered | none | none | Current against `rmm.json` (`render_rmm.py` reports "rmm.md is current" at `9bdf33c`) |

No change applies a ruling wrongly and none introduces a Major defect. `9bdf33c` is correct in what it changed. Its omissions at HEAD are finding-10 (decisions 9 and 40 not applied) and finding-11 (SWE-033).

**New findings at iteration 3 re-issue 1.**

| Finding | Origin | Severity | Item | Location | Description | State | Deferred to | Disposition |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-11"></a>finding-11 (F-11, new at iteration 3 re-issue 1) | reviewer | Major | R2; S3 (SWE-139, SWE-125) | `rmm.json` row SWE-033 `status` "Planned" (blob `37c6f24d`) | `tools/render_rmm.py --check` exits 1 at HEAD: "SWE-033: status 'Planned' but every named path exists and no 'Planned for <gate>' names the future artifact or execution (set status In place or add the label)". The row names `docs/decisions/trade-studies/TS-002-firmware-runtime-make-buy.md` and approval "in docs/reviews/SRR/decision-memo.md". The memo was created at `0bcea39`, and SRR decision 107 (K9, "Approve A0 with the four revisit triggers of TS-002 section 8", owner ruling 2026-09-26) approved the trade study, so the row is complete but still reads Planned. Reviewer's bisection on `git archive` exports: `0bcea39^` exit 0, `0bcea39` exit 1, HEAD exit 1. 03 section 6.4 item 7 requires the status move in the same change that creates the artifact. `9bdf33c` is an ancestor of `0bcea39`, so the R16 RMM edit passed the check when it was made. Major: a gate tool of 03 section 6.1 fails on the product, which blocks `baseline/srr` (08 section 3.2, "blocks baseline"), and the RMM misstates the SWE-033 compliance state that the owner approved. Fix (03 author, R16): set SWE-033 `status` to "In place", citing SRR decision 107 (owner ruling 2026-09-26), re-render `rmm.md`, and confirm `render_rmm.py --check` exits 0 (In place 40) | Open | | Open (iteration 3 re-issue 1). Blocks the record verdict |
| <a id="finding-10"></a>finding-10 (F-10, new at iteration 3 re-issue 1) | reviewer | Minor | CL-4, CL-8; S5 | 03 header line 3 ("Draft for SRR"); section 4.2 line 112 and table rows (HZ-004 K4 and K13, HZ-005 K9, HZ-008 components); section 4.3 rows at lines 165 to 167 ("proposed"), paragraphs at lines 170 to 174; section 5 line 220 and rows b and i ("proposed"); section 6.5 X13 and X20 (lines 341, 349); section 9 lines 375 to 380 (RMM approval "Draft for SRR"); `rmm.json` SWE-134 `implementation` ("proposed ... owner decision at SRR, 03 item X20", "hazards.json 0.4.0-pha") | The rulings are not applied to 03 or to `rmm.json` SWE-134. SRR decision 9 ("Concur, with frequency control safety-critical ... and the override command path safety-critical as 03 proposes") and decision 40 ("Adopt with the 10 kHz window and 100 ms") settle the three rows 03 and SWE-134 still mark proposed. Decision 6 approved the RMM, yet 03 section 9 still reads "Draft for SRR" while `rmm.json` `meta.approval` reads "Approved at SRR". The input also moved: `hazards.json` 0.5.0-pha (`bfea9c7`, R16) drops "proposed" from the HZ-008 component strings. It moves the Software controls HZ-004 K4 and K13 and HZ-005 K9 from Requirement pending to Proposed with new `control_req_ids` (reviewer's field walk; REQ-SYS-184 to 190 and REQ-SW-KEYER-039 added to `requirement_ids`). 03 section 4.2 still transcribes 0.4.2-pha (RP for those three controls), and section 6.5 does not list the difference (R3, CL-8). `firmware_role.criteria`, `safety_critical` and `swe134_items` are unchanged for all 15 hazards, so the classification, the safety-critical set (with the three rows now determined), the criteria unions and section 5 hold in substance. Minor: status and transcription text only. Fix (03 author): re-transcribe sections 4.2 and 4.3 from 0.5.0-pha; drop "proposed" and the decline paths, citing SRR decisions 9 and 40 (owner ruling 2026-09-26); mark X20 and X13 resolved; set 03 section 9 RMM approval to the decision 6 state; bring SWE-134 `implementation` to the ruled set; this rides with finding-8 (same re-transcription) and finding-9 | Lien | PDR | Lien: fix before PDR (convergence rule, charter section 4 item 3). Owner: 03 author |

**Disposition of every finding at HEAD `1e56df4`.**

| Finding | Severity | Iteration 3 re-issue 1 disposition | Evidence and ruling |
|---|---|---|---|
| finding-1 | Major | Closed (Verified) | Stays closed: 03 blob unchanged; SRR decision 9 (owner ruling 2026-09-26) concurs with the 03 classification and determination, which carries the mission-critical key-input and keyer-mode selection path (03 line 184); no ruling reverses it |
| finding-2 | Minor | Closed (Verified) | 03 unchanged; 07 section 14.1 unchanged since `adcfe09` |
| finding-3 | Minor | Closed (Verified) | 03 unchanged |
| finding-4 | Minor | Closed (Verified) | 03 unchanged |
| finding-5 | Minor | Lien: fix before PDR | `hazards.json` 0.5.0-pha criteria for HZ-001, 003, 006, 012 unchanged (b, c; b, e; b, c; b, c) |
| finding-6 | Minor | Closed (Verified) | Decision 8 ("Accept, with RSK-010 and the hazard analysis as the record") recorded in `rmm.json` SWE-022, 023, 219 at `9bdf33c`; the spokesperson line is observation O-5 |
| finding-7 | Minor | Lien: fix before PDR | Placement rule unchanged |
| finding-8 | Minor | Lien: fix before PDR | Unchanged; widened in effect by the 0.5.0-pha drift, carried as finding-10 |
| finding-9 | Minor | Lien: fix before PDR | Unchanged; 03 section 9 "Draft for SRR" now joins it (finding-10) |
| finding-10 (new) | Minor | Lien: fix before PDR | See the new-findings table |
| finding-11 (new) | Major | Open | See the new-findings table |

No ruling of 2026-09-26 resolves an open Major finding of this record: none was open at iteration 3. The rulings close no Minor lien either. Decisions 6 to 9 confirm what the liens assume and change no fix.

**Iteration 3 re-issue 1 answers** (items that changed; all others stand as at iteration 3).

| Item | Answer | Evidence |
|---|---|---|
| R1 | Met for this product (the repository run fails outside it) | `validate_docs.py` at HEAD: 35 passed, 15 failed before this record was updated, every failure a record-drift or record-state failure of a peer-review record whose product R16 changed; `rmm.json` and `hazards.json` PASS. This record's own failure was the drift of `rmm.json` and `rmm.md` to `9bdf33c`, cleared by the `product_files` update |
| R2 | Not met (finding-11) | `render_rmm.py --check` exit 1 on SWE-033 |
| R3 | Not met in full (finding-10, lien) | 03 states 0.4.2-pha (SHA-256 `6b69a00f...`); the file is 0.5.0-pha (`27228162...`); the difference is not an open item of section 6.5 |
| CL-4 | Differences not listed (finding-8, finding-10; liens) | HZ-004 K4, K13 and HZ-005 K9 status and `control_req_ids`; HZ-008 component strings |
| CL-5 | Concur, per component | `firmware_role.criteria`, `components` membership and `swe134_items` unchanged from 0.4.2-pha, so the unions stand |
| CL-9 | Concur with the classification and determination, now ruled | SRR decision 9 (owner ruling 2026-09-26) concurs as SMA TA; decision 40 adopts REQ-SYS-182 |
| S2 | Yes | 100 rows; FC 75, T 17, NA 8 unchanged |
| S3 | No (finding-11) | SWE-033 status misstated; T and NA rows now carry their approval notes (decisions 6, 7, 8) |
| S4 | Yes | Decision memo section 7.1 names this record and INSP-017 as the independent concurrence |

**Observations (not findings; cross items for the lead SE).**

- **O-5.** `rmm.json` SWE-022, SWE-023 and SWE-219 `residual_risk`, content approved by decision 6, state "The owner also accepts it as official spokesperson for bystanders and household members". The decision memo section 7.1 records that no separate owner statement for that 03 section 9 line was given and leaves the line empty as an owner action. The two should agree once the owner states it; the RMM text is the 03 section 4.4 plan statement and needs no change if the owner signs the line.
- **O-6.** SRR package item R16 (b) does not name 03 or `rmm.json` SWE-033 and SWE-134. The lead SE should add finding-11 to R16 before `baseline/srr`, since it blocks a gate tool, and route finding-10 with the PDR liens.
- **O-7.** Package decision 9 settles the menu override command path. The cross item 1 of iteration 3 (package decision list against 03 X20) is therefore resolved by the ruling, and X20 itself is part of finding-10.

**Lien table (convergence rule; iteration 3 table L-1 to L-4 stands, one row added).**

| Lien | Finding | Severity | Product location | Fix | Owner | Due |
|---|---|---|---|---|---|---|
| L-5 | finding-10 | Minor | 03 sections 3 header, 4.2, 4.3, 5, 6.5 X13 and X20, 9; `rmm.json` SWE-134 | Apply SRR decisions 6, 9 and 40 and re-transcribe from `hazards.json` 0.5.0-pha | 03 author | Before PDR |

**Commands run (2026-09-26, iteration 3 re-issue 1, repository root, `.venv/bin/python`).**
- `tools/validate_docs.py`: exit 1 before this update (35 passed, 15 failed; this record failed on `rmm.json` and `rmm.md` drift only). After the update this record PASSes; the run exits 1 (41 passed, 9 failed), every remaining failure in another record (drift to R16 products, cross item for the lead SE).
- `tools/traceability.py --report-only --output <scratchpad>/tr.md`: 245 requirements, 173 test cases, 4 violations, 2 warnings (outside this product; `docs/vv/traceability-report.md` and `traceability.json` not written).
- `tools/render_risk.py --check --gate SRR --hazards docs/safety/hazards.json`: exit 0; 65 risks, 159 candidates, 0 warnings.
- `tools/render_rmm.py --check`: exit 1 (finding-11). The same check on `git archive` exports: `0bcea39^` exit 0, `0bcea39` exit 1, `9bdf33c` exit 0.
- `tools/render_compliance.py --check`: exit 0.
- `python -m unittest discover -s tools/tests`: 400 tests, 1 failure, `test_validate_docs.RepositoryTests.test_repository_exit_zero` (the repository `validate_docs.py` failures above).

No image was produced at this iteration, so no render needed inspection.

**Verdict.** One Major finding is open (finding-11), so under the convergence rule the verdict is NEEDS CHANGES, with `readiness_met` false on R2. The record becomes APPROVED (with liens finding-5, 7, 8, 9 and 10) once SWE-033 is set In place and `render_rmm.py --check` exits 0; a delta check of that one row is enough.

```
ITERATION 3 RE-ISSUE 1 (2026-09-26, post-SRR-ruling delta): VERDICT: NEEDS CHANGES. Reviewed HEAD 1e56df4: 03 ed270f44 (unchanged), rmm.json 37c6f24d, rmm.md 5e6dd864; delta commit 9bdf33c applies SRR decisions 6, 7 and 8 correctly. New: finding-11 Major (SWE-033 status, render_rmm.py --check exit 1, since 0bcea39); finding-10 Minor lien (decisions 9 and 40 and hazards.json 0.5.0-pha not applied in 03 and SWE-134). Closed 5; Lien 5 Minor (finding-5, 7, 8, 9, 10). Unresolved Major: finding-11.
```

## Post-SRR-ruling delta 2 (iteration 3 re-issue 2, independent reviewer, 2026-09-26)

**Scope and baseline.** `reviewer:classification`, a new invocation of the same role, independent of the author of 03, `rmm.json`, `rmm.md` and of the commits verified here; no product was edited. Earlier sections of this record are left as written; only the front matter fields and their comments changed, and this section was appended. Trigger: SRR package item R16 applied the fix of finding-11 (Major) at `7d735e5`, and the lead SE applied SRR decision 10 (c) to 05 at `0834da2`, which changes the control class of the `rmm.json` rows this record reviews. The owner approved the SRR on 2026-09-26 (Approved with liens; `docs/reviews/SRR/minutes.md`); every decision is ruled as its Recommendation cell in `docs/reviews/SRR/decisions-for-owner.md` states. Review baseline HEAD `5122a6b` (HEAD `ab38255` at the tool runs; `ab38255` touches only the INSP-013 record). Blobs reviewed, each equal to `git rev-parse HEAD:<path>` and `git hash-object`: 03 `ed270f443e2ab648480017df8ad3d0221400cf4c` (unchanged since iteration 3), `rmm.json` `e326ddd1b7296d7d7fe172be6f33535cee3192d7`, `rmm.md` `54e351f4df231d1a1e74e6eef4bd07db9a408fa0`. Inputs unchanged since re-issue 1: `hazards.json` `81cacde4` (0.5.0-pha), 07 `37d472b5`. The convergence rule (charter section 4 item 3) applies: only open Major findings and ruled R16 work change products; a new Minor finding is a lien due PDR.

**Search first.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (queries: post-SRR-ruling delta re-issue records and `product_commit`; the `validate_docs.py` record state rule and latest-iteration section). `grep -n` then pinned lines only.

**Commits since `product_commit` `1e56df4` that touched the products** (`git log 1e56df4..HEAD` over the three products and both inputs): one, `7d735e5` (`rmm.json` and `rmm.md`; 5 insertions, 5 deletions). 03, `hazards.json` and 07 are untouched.

**Delta verification of `7d735e5` (SRR decision 107; finding-11).** Reviewer's field walk of `rmm.json` from `adcfe09` (blob `30fcde24`, iteration 3) to HEAD: 100 rows both sides, same SWE ids; the changed fields are exactly SWE-033 `implementation` and `status` (this commit), the nine `tailoring_rationale` fields and `meta.approval` already verified at re-issue 1 (`9bdf33c`). No `disposition`, `residual_risk`, `authority` or other row changed.

| Change | Ruling or finding cited | Check | Result |
|---|---|---|---|
| SWE-033 `status` "Planned" to "In place" | finding-11 (Major); SRR decision 107, Recommendation cell "Approve A0 with the four revisit triggers of TS-002 section 8" (owner ruling 2026-09-26) | Every path the row names exists at HEAD: `docs/decisions/trade-studies/TS-002-firmware-runtime-make-buy.md` (status row line 6 "Decided 2026-09-26 ... SRR decision 107"), `docs/reviews/SRR/decision-memo.md`, `docs/decisions/adr/ADR-027-firmware-runtime-rustos-a0.md` (committed at `2362183`). The 03 section 6.3 status rule ("satisfied today by artifacts that exist") holds | Correct; finding-11 fixed |
| SWE-033 `implementation`: adds "(SRR decision 107, owner ruling 2026-09-26: option A0 with the four TS-002 section 8 revisit triggers), and the decision is recorded in ... ADR-027" | Decision 107 | TS-002 section 8 lists exactly four revisit triggers; the decision 107 source cell names ADR-027 as the resulting ADR | Correct; `disposition` FC, `tailoring_rationale` and `residual_risk` null unchanged |
| `rmm.md` re-rendered: status table Planned 60, In place 40 (SWE-033 added); row SWE-033 | none (render) | `render_rmm.py --check` exit 0: "rmm.json OK: 100 rows; FC=75, T=17, NA=8; In place=40 [SWE-033, ...]"; "rmm.md is current" | Correct |

No change applies a ruling wrongly and none introduces a Major defect. The commit trailer is "Refs: SRR", not the artifact id (03 section 6.4 item 7 pre-SRR form "Refs: <artifact id>"); the body names decision 107 and ADR-027, so the trace is complete (observation O-8, not a finding).

**Effect of `0834da2` (05, SRR decision 10 (c)) on this product.** 05 Table 4-1 row 3 (03, `rmm.json`, `rmm.md`, compliance matrix) is now Mixed: after SRR a `status` move and implementation-path update of an `rmm.json` row are Log class with `Refs: <artifact id>`; dispositions, rationale, residual risk, the 03 record and the compliance matrix stay CR. The decision 10 Recommendation cell is "Approve (a) to (c)", and item (c) is "the rmm.json status moves and implementation-path updates as Log class after SRR (03 item X7)", so 05 now applies the ruling (INSP-006 verifies the 05 text). 03 was not updated with it: section 6.4 item 7 (line 312) still states "After SRR the vehicle is a Class II `CR-NNN`" with the X7 relief as "Proposed", and section 6.5 item X7 (line 335) is still "Open". This is finding-12.

**New finding at iteration 3 re-issue 2.**

| Finding | Origin | Severity | Item | Location | Description | State | Deferred to | Disposition |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-12"></a>finding-12 (F-12, new at iteration 3 re-issue 2) | reviewer | Minor | CL-8 | 03 section 6.4 item 7 (line 312); section 6.5 item X7 (line 335) | 03 still names a Class II `CR-NNN` as the post-SRR vehicle for an `rmm.json` status move and marks X7 Open, while 05 Table 4-1 row 3 and the new section 5.1 row (`0834da2`) make it a Log commit under SRR decision 10 (c) (owner ruling 2026-09-26). 03 itself says "The lead SE decides X7 before SRR and this item is updated to the decision", so the text is stale, not a second rule; the ruling and 05 govern, and following 03 would only board a change that needs no board (more conservative, no loss of control). Minor under the convergence rule. Fix (03 author): update item 7 to the decision 10 (c) vehicle citing 05 row 3, mark X7 Resolved (SRR decision 10 (c), `0834da2`); rides with finding-10 (rulings not applied to 03) | Lien | PDR | Lien: fix before PDR (convergence rule, charter section 4 item 3). Owner: 03 author |

**Disposition of every finding at HEAD `5122a6b`.**

| Finding | Severity | Iteration 3 re-issue 2 disposition | Evidence |
|---|---|---|---|
| finding-1 | Major | Closed (Verified) | 03 unchanged; stays closed |
| finding-2, finding-3, finding-4, finding-6 | Minor | Closed (Verified) | 03 unchanged; `rmm.json` SWE-022, 023, 219 rationale unchanged since `9bdf33c` |
| finding-5, finding-7, finding-8, finding-9, finding-10 | Minor | Lien: fix before PDR | Unchanged. finding-9 now also covers 03 section 6.1 line 246 "In place 37" (HEAD 40); finding-10 unchanged |
| finding-11 | Major | Verified (fixed at `7d735e5`) | SWE-033 In place under SRR decision 107; `render_rmm.py --check` exit 0 at HEAD |
| finding-12 (new) | Minor | Lien: fix before PDR | See the new-finding table |

**Answers that changed at iteration 3 re-issue 2** (all others stand as at re-issue 1).

| Item | Answer | Evidence |
|---|---|---|
| R2 | Met | `render_rmm.py --check` exit 0 (In place 40, `rmm.md` current) |
| R3 | Not met in full (lien finding-10) | Unchanged; carried as a lien under the convergence rule, so `readiness_met` is set on R1 and R2 as re-issue 1 stated |
| S3 | Yes | SWE-033 status now matches the approved compliance state (decision 107) |
| CL-8 | No (finding-12, lien) | 03 section 6.4 item 7 and X7 against 05 row 3 |

**Observations (not findings).**
- **O-8.** `7d735e5` carries "Refs: SRR" rather than the artifact id; the body cites decision 107 and ADR-027. From `baseline/srr`, 05 row 3 requires `Refs: <artifact id>` on such a Log commit.
- **O-9 (cross item, INSP-017 reviewer).** INSP-017, the software assurance record of this product, names `rmm.json` `30fcde24` and fails the record drift rule at HEAD (`validate_docs.py`). Its `assurance_verdict` APPROVED is carried here as filed (07 section 10.2). Its reviewer should issue the delta re-issue on `rmm.json` `e326ddd1` and `rmm.md` `54e351f4` (changes `9bdf33c` and `7d735e5`); if that re-issue does not return APPROVED, this record's `verdict` returns to NEEDS CHANGES.
- **O-10 (cross item, lead SE).** Package item R16 and the lien list should add finding-12 with finding-10 (03 author, before PDR).

**Lien table (L-1 to L-5 stand; one row added).**

| Lien | Finding | Severity | Product location | Fix | Owner | Due |
|---|---|---|---|---|---|---|
| L-6 | finding-12 | Minor | 03 section 6.4 item 7, section 6.5 X7 | Apply SRR decision 10 (c) as 05 row 3 states; mark X7 Resolved | 03 author | Before PDR |

**Commands run (2026-09-26, iteration 3 re-issue 2, repository root, `.venv/bin/python`).**
- `tools/validate_docs.py`: before this update exit 1 (43 passed, 7 failed); this record passed then only because its NEEDS CHANGES verdict exempted it from the drift rule. After the update this record PASSes with the HEAD blobs; the remaining failures are other records (drift to R16 products).
- `tools/traceability.py --report-only --output <scratchpad>/tr.md`: exit 0; 245 requirements, 173 test cases, 4 violations, 2 warnings (outside this product); `docs/vv/traceability-report.md` and `traceability.json` restored with `git checkout`.
- `tools/render_risk.py --check --gate SRR --hazards docs/safety/hazards.json`: exit 0; 65 risks, 159 candidates, 0 warnings.
- `tools/render_rmm.py --check`: exit 0; 100 rows, FC 75, T 17, NA 8, In place 40; `rmm.md` current.
- `tools/render_compliance.py --check`: exit 0.
- `python -m unittest discover -s tools/tests`: 400 tests, 1 failure, `test_validate_docs.RepositoryTests.test_repository_exit_zero` (the repository `validate_docs.py` failures in other records).

No image was produced, so no render needed inspection.

**Verdict.** finding-11, the only open Major, is fixed at `7d735e5` and verified; no Major finding is open; the Minor findings finding-5, 7, 8, 9, 10 and 12 are liens due PDR. Under the convergence rule the reviewer verdict is APPROVED with liens, readiness is met, the assurance verdict (INSP-017, as filed) is APPROVED, so the record verdict is APPROVED, subject to observation O-9.

```
ITERATION 3 RE-ISSUE 2 (2026-09-26, post-SRR-ruling delta 2): VERDICT: APPROVED (with liens finding-5, 7, 8, 9, 10, 12). Reviewed HEAD 5122a6b: 03 ed270f44 (unchanged), rmm.json e326ddd1, rmm.md 54e351f4; delta commit 7d735e5 applies SRR decision 107 to SWE-033 correctly and fixes finding-11 (Verified; render_rmm.py --check exit 0). New: finding-12 Minor lien (03 section 6.4 item 7 and X7 not updated to SRR decision 10 (c), applied in 05 at 0834da2). Open Major 0. Cross: INSP-017 delta re-issue (O-9).
```

## CR-010 delta (iteration 3 re-issue 3, independent reviewer, 2026-09-29)

**Scope and independence.** Written by a new invocation in the `reviewer:classification` role, dispatched as the configuration manager of WP-PDR-55 merge batch 1 for CR-010 section 5 step 5 (plan rule C4). This invocation authored no part of CR-010, of its change set `5cd87cf`, of INSP-037 or INSP-050, or of the CR-010 impact reviews, and it edited no product file. Earlier sections of this record are left as written. Only the front matter fields and their comments changed, and this section was appended. Trigger: CR-010 (Class II, Approved by the owner 2026-09-28, `a17af87`) replaces the three product blobs this record names. Its section 5 step 5 requires this record to name the new blobs, and to be committed on the CR branch before the merge, so that `main` never fails the record drift rule (SRR package section 2.3, R13). The owner's disposition conditions (CR-010 section 7) set that placement, which settles CR-010 IR2-F2 for this record.

**Search first.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (queries: CR-010 pre-merge checks and SRR record re-issue; the `validate_docs.py` record drift and record state rules). `git diff`, `git show`, `grep` and read-only Python were used afterwards only to pin lines.

**Configuration reviewed.** Branch `cr/CR-010-apply-srr-decisions-9-and-40` at `5cd87cf` (one commit on base `ab2af2d`; trailer `CR: CR-010`). `git diff --stat ab2af2d 5cd87cf`: the four files of CR-010 section 1 only (03, 07, `rmm.json`, `rmm.md`; 72 insertions, 71 deletions). `main` (`908d21a`) has not changed any of the four files since `ab2af2d`, and none of the five SRR records CR-010 names, so no rebase was needed (step 4) and the four blobs are the ones INSP-037 and INSP-050 froze. Blobs reviewed, each equal to `git rev-parse 5cd87cf:<path>`: 03 `1e03b873b404deeaa86ba2393806cda74996187d`, `rmm.json` `a907a087f1302e275ea56bdb7bba89638777a319`, `rmm.md` `17ea4733a4d41b54424619f8682db815b05d4ebf`.

**Delta verification (reviewer's own checks).**

| Check | Method | Result |
|---|---|---|
| `rmm.json` differs from `e326ddd1` only in the five `implementation` fields | Python field walk of `ab2af2d` against `5cd87cf`: `meta` equal; 100 rows, same `swe` ids in the same order; changed fields exactly SWE-023, SWE-134, SWE-205, SWE-219 and SWE-220 `implementation` | Correct. No `disposition`, `tailoring_rationale`, `residual_risk`, `status` or `authority` changed, so the classification and the tailoring stand |
| `rmm.md` equals the render of the new `rmm.json` | `tools/render_rmm.py --check` in the branch worktree | Exit 0: 100 rows; FC 75, T 17, NA 8; In place 40; "rmm.md is current" |
| No criteria union, component set or SWE-134 allocation changed in 03 | Column-wise comparison of every changed table row of 03 (sections 4.3, 5, 6.5, 9) between `ab2af2d` and `5cd87cf` | Correct. Section 4.3: the criteria column is unchanged in every row; only the hazards and component columns lose "(proposed)" and gain the SRR decision citations. Section 5 rows a, b, d to i: each changed cell equals the old cell with "; proposed)" replaced by ")", 12 entries in all, as CR-010 section 1.1 states |
| Decision quotes equal the memo | `grep -F` of the quoted texts against `docs/reviews/SRR/decision-memo.md` (blob `110102bf`) | Correct. The decision 9 text (memo line 214) and the decision 40 text (memo line 213) are quoted verbatim in 03 section 4.3. `rmm.json` cites the decisions without quoting them |
| Residual conditional wording tied to decisions 9 and 40 | `grep -n -i -E` for "proposed", "if ... concur", "if decision 9 / 40", "is adopted", "if adopted", "conditional", "declin" over 03 at `5cd87cf` | Two "proposed" occurrences remain, both by design. Section 4.2 list item 2 (line 135, "each marked proposed") is the 0.4.0-pha transcription that CR-010 section 1.1 keeps until the PDR re-run. The section 9 configuration guard row (line 379, "Proposed by Claude") concerns HZ-014, not decision 9 or 40. No decline path remains |
| RMM approval state in 03 section 9 | Row read at `5cd87cf` | "Approved at SRR (SRR decision 6 ...; `rmm.json` `meta.approval`)", consistent with `meta.approval` |

**finding-10 (Minor lien) re-checked.** The parts that CR-010 fixes are verified at `5cd87cf`. The 03 header no longer reads "Draft for SRR". The proposed markers and the decline paths of sections 4.3, 4.4, 5 and 9 are gone and cite SRR decisions 9 and 40. X20 is Resolved, and X13 is resolved for its decision 9 part. The section 9 RMM approval matches decision 6, and `rmm.json` SWE-134 names the ruled set. One part remains and is not in CR-010's scope: re-transcribing sections 4.2 and 4.3 from `hazards.json` 0.5.0-pha (the HZ-004 K4 and K13 and HZ-005 K9 control statuses and `control_req_ids`), with the R3 and CL-4 difference listed in section 6.5. CR-010 section 1.1 assigns it to the WP-PDR-17 PDR re-run, together with finding-8. finding-10 stays "Lien: fix before PDR", narrowed to that remainder.

**Findings of the CR-010 product reviews, not raised again.** INSP-037 finding-2 to finding-7 and INSP-050 finding-1 to finding-3 (liens in those records; for example, the 03 section 4.3 lead states the 0.5.0-pha difference too broadly, INSP-037 finding-3) are concurred with at Minor. They are not duplicated here.

**Disposition of every finding (supersedes the earlier tables; record state rule of `tools/validate_docs.py`).**

| Finding | Severity | State | Evidence |
|---|---|---|---|
| finding-1 | Major | Verified | Closed since iteration 2. SRR decision 9 concurs with the determination that finding-1 produced; unchanged by CR-010 |
| finding-2, finding-3, finding-4, finding-6 | Minor | Verified | Closed; untouched by CR-010 |
| finding-5, finding-7, finding-8, finding-9, finding-12 | Minor | Lien: fix before PDR | Untouched by CR-010. The section 6.4 item 7 and X7 text of finding-12 is unchanged at `5cd87cf` |
| finding-10 | Minor | Lien: fix before PDR | Narrowed: the decision 9 and 40 parts are verified at `5cd87cf`; the 0.5.0-pha re-transcription remains (above) |
| finding-11 | Major | Verified | Closed at `7d735e5`; SWE-033 unchanged by CR-010 |

No Major finding is open, and no new finding is raised.

**Answers changed at this delta.** R2 Met (`render_rmm.py --check` exit 0 at `5cd87cf`). R3 is not met in full (the narrowed finding-10 lien), which is unchanged in kind. CL-9 is Yes: the determination now states the owner's rulings. The other answers stand as at re-issue 2.

**Observations (not findings).**
- **O-11 (software assurance reviewer; cross item).** INSP-017, the paired software assurance record, still names 03 `ed270f44`, `rmm.json` `e326ddd1` and `rmm.md` `54e351f4`. On any tree that holds the CR-010 blobs it fails the record drift rule, and CR-010 section 5 step 5 names it. Its delta is a software assurance review, which 07 sections 2.1.1 and 10.2 and plan rule C4 give to a separate invocation, so this invocation did not write it. `assurance_verdict` is copied from INSP-017 as filed. If the INSP-017 delta does not return APPROVED, this record's `verdict` returns to NEEDS CHANGES.
- **O-12 (03 author).** The 03 header fifth-revision note reads "CR-010, Class II, Submitted", the state when it was written. CR-010 has been Dispositioned (Approved) since 2026-09-28. This is not a defect of the reviewed change (a product edit now would restart step 5). The next 03 revision (the WP-PDR-17 re-run) states the merged state.
- **O-13 (lead SE).** The drift interval is confined to the CR branch, as CR-010 section 5 intends. After this delta and the INSP-010 and INSP-006 deltas, the only records on the branch that name a pre-change CR-010 blob are INSP-017 and INSP-018 (O-11).

**Commands run (2026-09-29, branch worktree at `5cd87cf` with the three record edits, `.venv/bin/python`).**
- `tools/validate_docs.py`: exit 1, 48 passed, 2 failed of 50. The two failures are INSP-017 and INSP-018 (O-11). This record, INSP-006 and INSP-010 PASS.
- `tools/traceability.py --report-only --output <scratchpad>/cr010-tr.md`: exit 0; 245 requirements, 173 test cases, 0 violations, 2 warnings (REQ-SYS-125, REQ-SYS-148).
- `tools/render_rmm.py --check`: exit 0 (counts above).
- `python -m unittest discover -s tools/tests`: 424 run, 1 failure (`test_repository_exit_zero`, on the two failures above), 3 skipped.
- The trial merge with `main` and the gate runs on it are recorded in CR-010 section 9 (configuration manager pre-merge check of 2026-09-29).

No image was produced, so no render needed inspection.

```
ITERATION 3 RE-ISSUE 3 (2026-09-29, CR-010 delta): VERDICT: APPROVED (with liens finding-5, 7, 8, 9, 10 narrowed, 12), subject to O-11. Reviewed branch cr/CR-010 at 5cd87cf: 03 1e03b873, rmm.json a907a087, rmm.md 17ea4733; the delta ab2af2d..5cd87cf states SRR decisions 9 and 40 correctly, changes no criteria, component set, SWE-134 allocation or disposition, and fixes the decision 9 and 40 parts of finding-10. New findings 0; open Major 0. Cross: INSP-017 delta by a separate software assurance invocation (O-11).
```
