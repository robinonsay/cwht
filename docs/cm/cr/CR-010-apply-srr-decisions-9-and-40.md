---
id: CR-010
title: Apply SRR decisions 9 and 40 to the classification record, the software plan and the RMM
status: Submitted
class: II
originator: Claude
date_opened: 2026-09-27
phase: B
configuration_at_origination: baseline/srr (tag on 779f93f); change set prepared on branch base ab2af2d (main); branch head 5cd87cf
baseline_affected: baseline/srr
affected_cis: [2, 3]
affected_paths: [docs/process/03-software-classification-and-rmm.md, docs/process/07-software-engineering-plan.md, docs/process/rmm.json, docs/process/rmm.md]
affected_ids: [SWE-023, SWE-134, SWE-205, SWE-219, SWE-220, WP-SW-14, HZ-008, REQ-SYS-182]
related: [INSP-009, INSP-017, INSP-010, INSP-018, OQ-SAF-014, ADR-027, CR-003, CR-006, RSK-013, RSK-046]
target_release: none
branch: cr/CR-010-apply-srr-decisions-9-and-40
disposition: null
disposition_date: null
relook_trigger: null
relook_by: null
merge_sha: null
date_closed: null
---

# CR-010: Apply SRR decisions 9 and 40 to the classification record, the software plan and the RMM

Template: `docs/templates/change-request.md`. Process: `docs/process/05-configuration-and-data-management.md` §5.1 to §5.3. File location: this file, committed on `main` with `Refs: CR-010`. Status: **Submitted**. Work package: WP-PDR-17 of `docs/plan/pdr-work-plan.md` (revision 2), wave 0 part, "decision 9/40 change set first". The PDR work plan rule C6 requires the section 6 independent review before the owner's disposition, although the template does not require it for a Class II change that touches no requirement, ICD, hazard or test case.

**Where the change is.** The full product change is prepared on the branch `cr/CR-010-apply-srr-decisions-9-and-40`, commit `5cd87cf` on base `ab2af2d`, as the Submitted state of 05 §5.2 allows ("Branch `cr/CR-NNN-<slug>` may be opened for prototyping; nothing merges"). The exact before and after text is `git diff ab2af2d 5cd87cf`. Nothing is merged to `main` before the owner's disposition and the section 9 verification.

| File (Table 4-1 row) | Blob at `baseline/srr` and on `main` | Blob on the branch (`5cd87cf`) |
|---|---|---|
| `docs/process/03-software-classification-and-rmm.md` (row 3, CR part) | `ed270f443e2ab648480017df8ad3d0221400cf4c` | `1e03b873b404deeaa86ba2393806cda74996187d` |
| `docs/process/07-software-engineering-plan.md` (row 2) | `bfe05f4327e79fa15c24d2cf8c14249804f946a8` | `3ae7d73b01810e47fd10251d798e0a047aaa72dd` |
| `docs/process/rmm.json` (row 3, CR part: `implementation` fields) | `e326ddd1b7296d7d7fe172be6f33535cee3192d7` | `a907a087f1302e275ea56bdb7bba89638777a319` |
| `docs/process/rmm.md` (row 3, rendered by `tools/render_rmm.py`) | `54e351f4df231d1a1e74e6eef4bd07db9a408fa0` | `17ea4733a4d41b54424619f8682db815b05d4ebf` |

## 1. Description of the change

The owner ruled at SRR, 2026-09-26 (`docs/reviews/SRR/decision-memo.md` section 8, key decision K2; section 7.1 classification line):

- **Decision 9:** "Concur, with frequency control safety-critical (it removes single point failure row 4) and the override command path safety-critical as 03 proposes."
- **Decision 40:** "Adopt with the 10 kHz window and 100 ms." (REQ-SYS-182, HZ-008 K7, and with it the frequency verification unit.)

The baselined 03, 07 and RMM text still marks the three components these decisions settle as proposed, keeps the decline paths, and keeps WP-SW-14 conditional. This change states the rulings in each place. It changes no component's class beyond what the owner ruled, no criteria union, no SWE-134 allocation, no disposition, no tailoring rationale, no residual risk and no status.

### 1.1 `docs/process/03-software-classification-and-rmm.md` (fifth revision)

| Location | Before | After |
|---|---|---|
| Header status (line 3) | "Draft for SRR (fourth revision ...)" | "Baselined at SRR (`baseline/srr`, blob `ed270f44`)"; a fifth-revision note names this CR and the sections changed; the section 4.2 table stays the 0.4.0-pha transcription until the PDR re-run |
| Lead paragraph (line 5) | The HZ-008 change "is a proposal the owner decides at SRR"; the menu finding and the selection path are "proposals the owner decides as SMA TA at SRR (item X20)" | Concurred by the owner at SRR (decision 9, with decision 40 adopting REQ-SYS-182); the selection path approved with the section 4 determination (memo section 7.1) |
| Section 4.2 closing paragraph | "section 4.3 carries it as the proposal the owner decides as SMA TA at SRR" | The owner concurred; `hazards.json` 0.5.0-pha (`bfea9c7`) removes the word proposed from the HZ-008 component strings; section 4.3 records the decided determination |
| Section 4.3 lead paragraph | "Rows and hazards marked **proposed** carry the HZ-008 determination that the owner decides ..."; "closed by changing 07 section 14.1 in the same pre-SRR change set" | Quotes decisions 9 and 40; the formerly proposed rows are determined and the decline paths no longer apply; 07 section 14.1 changes in this CR; 0.5.0-pha changes only the HZ-008 component strings and no criteria, `safety_critical` or `swe134_items` (verified against 0.4.3-pha), so every criteria cell holds; re-transcription from the committed file is the PDR re-run |
| Section 4.3 rows | `SW-TXSEQ` "frequency-verified PA_EN prerequisite (proposed)", "HZ-008 (proposed)"; safe-state manager and scheduler "HZ-008 by type (ii) finding (proposed, below)"; frequency-word path "**proposed** (package decision 9)"; verification unit "**proposed** (package decisions 9 and 40 ...)"; menu override "**proposed** (...; item X20)"; drivers row "if decision 40 adopts K7, the PIO or timer capture ...", "the conditional WP-SW-14", "if decision 9 makes the frequency-word path safety-critical" | The same rows without the proposed markers, citing SRR decisions 9 and 40; the counter capture is WP-SW-14, required since decision 40 (ADR-027); the synthesizer bus joins the drivers row at the PDR re-run "because SRR decision 9 makes the frequency-word path safety-critical" |
| Frequency control paragraph | Proposal text with the concur and decline branches | The ruling: decision 9 concurred, decision 40 adopted REQ-SYS-182; SWE-219 and SWE-220 apply to the word path and the verification unit; the `SW-SYNTH` unit split is fixed in `docs/design/software-design.md` at PDR and presented to the owner at the PDR re-run; the decline paths and the `hazard-analysis.md` section 8.3 declined-decision-40 residual are not in force |
| Type (ii) findings for HZ-008 | "(proposed with decisions 9 and 40)" | "(in force with SRR decisions 9 and 40)"; text unchanged (item X14 stays open for `hazards.json`) |
| Menu override type (ii) finding | "(proposed, item X20)"; "Alternative the owner may rule instead, or the PDR architecture may adopt"; "If the owner rules the alternative at SRR, or the PDR architecture adopts it ..., the re-run ... returns the path" | "(concurred by SRR decision 9, item X20)"; "Alternative the PDR architecture may still adopt"; if the architecture adopts it, the re-run proposes the return for the owner's concurrence as SMA TA |
| Fault annunciation paragraph | "for HZ-008 if K7 is adopted" | "for HZ-008 with K7, adopted by SRR decision 40" |
| Mission-critical paragraph | "or all of frequency control if the owner declines decision 9 (...)"; "if decision 40 adopts K7, checked by the verification unit" | Decline clause removed; "checked by the frequency verification unit (K7, SRR decision 40)" |
| Section 4.4 SWE-219 and SWE-220 scope | "the menu override command path (proposed, item X20) and, if the owner concurs at SRR (package decision 9 ...), the transmit frequency-word path ... and the frequency verification unit" | The same components without condition, citing SRR decisions 9 and 40 |
| Section 5 paragraph under the lead | Entries "are **proposed**"; decline branches for decisions 9 and 40; menu entries removed "if the owner rules the partitioning alternative" | Entries carry the section 4.3 determination; decline paths no longer apply; menu entries removed only if the PDR architecture adopts the alternative and the owner concurs at the PDR re-run |
| Section 5 table rows a, b, d, e, f, g, h, i | 12 cell entries end "; proposed)" | The same entries end ")" |
| Section 6.5 item g (charter section 10) | Pre-SRR alternatives; status Open | Records that charter section 10 carries the decision 9 reading since `6ea6b1d` (SRR decision 10 (a)); proposes the closing parenthesis "(SRR decisions 9, 10 (a) and 40; the determination record is `docs/process/03-software-classification-and-rmm.md` §4.3 and the single authoritative component list is `docs/process/07-software-engineering-plan.md` §14.1, both re-run from the hazard analysis at PDR and CDR)" for the owner's approval; the component list is unchanged. This record does not edit the charter |
| Section 6.5 items X13, X14, X16, X20 | X13 "Remaining: ... the owner's ruling on decision 9"; X14 "both proposed with decisions 9 and 40"; X16 "Menu override command path (proposed)" and "if the owner rules the partitioning alternative"; X20 Open | X13 decision 9 part Resolved, remaining the PDR re-transcription; X14 "both in force with SRR decisions 9 and 40" (still Open for `hazards.json`); X16 without "(proposed)", alternative only by the PDR architecture with the owner's concurrence (still Open); X20 Resolved by decision 9, with the note that the PDR re-run presents the selection path's class again (INSP-026 finding-4) |
| Section 9 decision record | Safety-critical row names "the proposed type (ii) finding"; frequency control row "if declined ..." and authority "owner as SMA TA at SRR (package decision 9; decision 40 ...)"; menu row "Alternative ..." and "(item X20)"; RMM approval "Draft for SRR" | Rows state the concurrence with quotes and cite memo sections 7.1 and 8; the partitioning alternative stays open to the PDR architecture subject to the owner's concurrence; RMM approval "Approved at SRR (SRR decision 6 ...; `rmm.json` `meta.approval`)" |

Not changed in 03 by this CR (they are the PDR re-run of WP-PDR-17, after WP-PDR-16b and WP-PDR-32): the section 4.2 table and its 0.4.0-pha hash and "not yet committed" statements (INSP-009 finding-8 and finding-9; INSP-017 finding-7 and finding-8), the section 6.4 item 7 and item X7 vehicle (INSP-009 finding-12; INSP-017 finding-9), the section 1 placement rule (INSP-009 finding-7), criterion a on nine hazards (X15), the band-edge figures of SRR decision 25 (1.2 kHz guard, 144.0012 to 147.9988 MHz; carried item C-056), and the drivers that join the safety-critical row at the re-run.

### 1.2 `docs/process/07-software-engineering-plan.md` (revision A.8)

| Location | Before | After |
|---|---|---|
| Section 3.1, PDR row | "WP-SW-01 to WP-SW-07, WP-SW-09 and WP-SW-11, and WP-SW-14 if package decision 40 adopts REQ-SYS-182" | "WP-SW-01 to WP-SW-07, WP-SW-09, WP-SW-11 and WP-SW-14 (required since SRR decision 40 adopted REQ-SYS-182)" |
| Section 5 item 5 | "set frequency when package decision 9 concurs" | "set frequency (SRR decision 9)" |
| Section 12, S1 row | "the two Proposed frequency rows once package decision 9 is recorded as concurred, and the Proposed menu override command path once the owner concurs with 03 item X20" | "the frequency-word path and frequency verification unit rows and the menu override command path, all three concurred by SRR decision 9 with decision 40" |
| Section 14.1 lead | "... the menu override command path), each marked proposed." | "..., which the owner concurred in at SRR (package decision 9, with decision 40 adopting REQ-SYS-182; owner ruling 2026-09-26)." |
| Section 14.1 owner-decision paragraph | "concurs ... Three rows below are marked **Proposed** ... If the owner concurs, the word Proposed is removed. If not, ..."; decline branch for decision 40; the menu alternative as an owner ruling | Quotes decision 9; decision 40 makes the verification unit and WP-SW-14 required (section 19; ADR-027); the three rows are determined and the decline paths no longer apply (CR-010); the partitioning alternative stays open to the PDR architecture, with the return to the not-safety-critical set proposed at the PDR re-run for the owner's concurrence; row d and CS-39 apply in both outcomes (unchanged) |
| Section 14.1 table | `SW-SAFE` and `SW-SCHED` "(proposed with package decisions 9 and 40; ...)"; scheduler "frequency verification if adopted"; word path "(**Proposed**)", basis "package decision 9"; verification unit "(**Proposed**; exists only with REQ-SYS-182, package decision 40)"; menu "(**Proposed**; ...)", "apply to its code units if the owner concurs"; drivers "frequency counter ... if REQ-SYS-182 is adopted", "WP-SW-14 conditional", "conditional counter" | The same rows citing SRR decisions 9 and 40 without condition; drivers row "WP-SW-01, 02, 03, 04, 07, 09, 11 and 14" |
| Paragraph under the table | "`SW-SYNTH` units outside the frequency-word path are mission-critical if package decision 9 concurs" | "... are mission-critical (SRR decision 9)" |
| Mission-critical paragraph | ", and, if package decision 9 does not concur, `SW-SYNTH` as a whole (...)"; "part of the Proposed menu override command path"; "the two Proposed rows above" | Decline clause removed; "part of the menu override command path"; "the frequency-word path and frequency verification unit rows above" |
| Neither paragraph | "the Proposed menu override command path" | "the menu override command path" |
| Section 14.2 row d | "whether or not the owner concurs with the Proposed menu override command path ..., which, if concurred, adds the generating side" | "whatever the PDR architecture decides for the menu override command path ... (safety-critical by SRR decision 9), which adds the generating side" |
| Section 14.2 row h | "when REQ-SYS-182 is adopted (package decision 40)"; "(182 pending package decision 40)" | "(REQ-SYS-182, SRR decision 40)"; "(182 adopted by SRR decision 40)" |
| Section 14.2 row i | "If the owner declines package decision 38, 39 or 40, ... section 8.3 records the branch ..."; "(180 and 182 pending package decisions 38 and 40)"; "(HZ-003 K9, pending package decision 39 ...)" | "The owner adopted package decisions 38, 39 and 40 at SRR (owner ruling 2026-09-26), so the decline branches of `hazard-analysis.md` section 8.3 do not apply"; "adopted by SRR decisions 38 and 40"; "adopted by SRR decision 39". Decisions 38 and 39 appear because the sentences state the three jointly; both were adopted in the same ruling (memo section 8, K2) |
| Section 14.2 module rows | `SW-SYNTH` word path "(**Proposed** safety-critical; HZ-008)", "when REQ-SYS-182 is adopted, verified", and the sentence "If package decision 9 does not concur ..."; menu "(**Proposed** safety-critical ...)", "If the owner rules the partitioning alternative"; verification unit "(**Proposed**; `SW-SAFE`; only with REQ-SYS-182)"; mission-critical `SW-SYNTH` row "all of `SW-SYNTH` with the word path if package decision 9 does not concur" | Markers and decline sentences removed; "read back and verified (a; REQ-SYS-182)"; menu row withdrawn only if the PDR architecture adopts the alternative and the owner concurs at the PDR re-run; items per row unchanged |
| Section 19, WP-SW-14 row | "(conditional: only if package decision 40 adopts REQ-SYS-182; ...)", needed by "FW-B1, if adopted" | "(required: SRR decision 40 adopted REQ-SYS-182; ...)", needed by "FW-B1" |
| Section 21, RSK-013 row | "Thirteen work packages, plus WP-SW-14 if package decision 40 adopts REQ-SYS-182" | "Thirteen work packages plus WP-SW-14, required since SRR decision 40 adopted REQ-SYS-182" |
| Section 22 rows | Menu override ruling, frequency-control determination and tool constants rows due "SRR decision memo" or "With the decision 9 change set" | Done for 07, 03 and the RMM by CR-010; remaining items named (charter section 10 decision 40 citation; SEMP section 7.1; OQ-SAF-014 at the re-run; the `tools/validate_docs.py` constants after merge) |
| Section 23 | Last row A.7 | Row A.8 "pending CR-010 disposition" |

### 1.3 `docs/process/rmm.json` and `docs/process/rmm.md`

Only the `implementation` field of five rows changes (checked by script: no other field of any row and no `meta` field differs):

| Row | Before | After |
|---|---|---|
| SWE-205 | "the proposed determination that the transmit frequency-word path ... (...; owner decision at SRR, package decision 9)"; "the proposed type (ii) finding that the menu override command path ... (...; owner decision at SRR)" | "the determination ... (...; concurred by the owner as SMA TA at SRR, package decision 9, with decision 40 adopting REQ-SYS-182; owner ruling 2026-09-26)"; "the type (ii) finding ... (...; concurred at SRR, package decision 9)" |
| SWE-023, SWE-134 | "the menu override command path (proposed, ..., owner decision at SRR, 03 item X20); and, proposed for the owner's decision at SRR (package decision 9, with decision 40 for the verification unit), the transmit frequency-word path ... and the frequency verification unit"; SWE-134 also "or all of it if decision 9 is declined" | "the menu override command path (03 section 4.3 type (ii) finding, concurred at SRR by package decision 9, 03 item X20); and the transmit frequency-word path ... and the frequency verification unit (SRR decisions 9 and 40, owner ruling 2026-09-26)"; decline clause removed |
| SWE-219 | "three required elements for every safety-critical component of 03 section 4.3:" | adds "(including the transmit frequency-word path of frequency control, the frequency verification unit and the menu override command path, SRR decisions 9 and 40)" |
| SWE-220 | "every function in safety-critical components is measured" | "every function in the safety-critical components of 03 section 4.3 (including ..., SRR decisions 9 and 40) is measured" |

`rmm.md` is re-rendered by `tools/render_rmm.py` (exit 0) and `tools/render_rmm.py --check` exits 0 (100 rows; FC 75, T 17, NA 8; In place 40; unchanged).

## 2. Reason

1. The owner's rulings of SRR decisions 9 and 40 are not yet stated in three baselined documents: 03 and the RMM (INSP-009 finding-10, "The rulings are not applied to 03 or to `rmm.json` SWE-134", Minor, Lien: fix before PDR, owner 03 author) and 07 (section 14.1 still marks the three rows Proposed and WP-SW-14 conditional). OQ-SAF-014 in `hazards.json` names 03, 07 section 14, the SEMP, the charter and `rmm.json` rows SWE-134, SWE-205, SWE-219 and SWE-220 as the targets.
2. The PDR work plan (`docs/plan/pdr-work-plan.md` WP-PDR-17, wave 0) puts this change set first, because the SW L2 authors of WP-PDR-35 and the software architecture of WP-PDR-32 start from it (plan section 3.7, WP-PDR-35 "Depends on").
3. After `baseline/srr`, 03 (Table 4-1 row 3, CR part), 07 (row 2) and the `rmm.json` fields other than `status` and the implementation path (row 3) are CR-controlled; removing a proposed marker or a condition is not editorial (05 section 2: a status is never editorial). A CR is therefore the vehicle (05 section 5.1 row 1).

Workaround while the CR is open: WP-PDR-32 and WP-PDR-35 read the branch `cr/CR-010-apply-srr-decisions-9-and-40` together with the SRR decision memo section 8, which governs where the baselined text still says proposed.

## 3. Alternatives considered

| Alternative | Why rejected or deferred |
|---|---|
| Do nothing until the full PDR re-run | The SW L2 files and the architecture would be written against text that contradicts the owner's ruling; INSP-009 finding-10 is due before the PDR readiness declaration; the re-run needs WP-PDR-16b and WP-PDR-32 first (plan section 3.5), which is wave 2b |
| Fold this change into the PDR re-run CR | Same timing problem; also mixes a transcription of a decided ruling with a new determination that goes to the owner as OD-35 |
| Log-class commit with `Refs:` | 05 Table 4-1 row 3 makes only `rmm.json` status moves and implementation-path updates Log class; the 03 record, 07 and the text of `rmm.json` implementation fields are CR-controlled |
| Editorial commit | 05 section 2: a status field is never editorial, and "proposed" versus "determined" is the status of a determination |
| One CR per document | The three documents must agree (charter section 10; 03 section 6.4 item 9 "all in the same change set") |

## 4. Impact assessment (CM plan §5.3)

| Field | Assessment (numbers, IDs, paths) |
|---|---|
| Performance margins | None: no TPM, MOP or budget value changes; text of process documents only |
| Safety | HZ-008 (frequency-word path, frequency verification unit, K7) and HZ-001, HZ-004, HZ-005, HZ-006 (menu override command path) are referenced; no hazard changes. 07 section 14.1 rows that change: `SW-SYNTH` frequency-word path, `SW-SAFE` frequency verification unit, the menu override command path (module fixed at PDR), and the `SW-SAFE`, `SW-SCHED`, `SW-TXSEQ` and `pico2` driver rows (wording only). No module enters or leaves the safety-critical or mission-critical set relative to the owner's SRR ruling; no criteria union and no SWE-134 item changes. Hazard analysis re-issue: no (`hazards.json` 0.5.0-pha already records both rulings). RF exposure evaluation: no |
| Risk | None changed by this CR. RSK-046 (out-of-band transmission; single point failure row 4) and RSK-013 (rustos driver effort, now including WP-SW-14 without condition) are re-assessed in the WP-PDR-18 Track pass, which owns `docs/risk/register.json` |
| Software classification and tailoring | 03 fifth revision (determination text only; the classification is unchanged); `rmm.json` rows SWE-023, SWE-134, SWE-205, SWE-219, SWE-220, `implementation` field only; no disposition, `tailoring_rationale`, `residual_risk`, `status` or `meta` change; no compliance-matrix row. No tailoring change, so no re-acceptance under 03 section 4.4 |
| Interfaces | None: no ICD; no external interface |
| Operations and ConOps | None: no `OPS-` scenario, operator procedure or handbook text changes |
| Cybersecurity | None: the USB firmware-load path and the key-input command path (07 section 16) are unchanged |
| Verification | None invalidated: no `TC-*` exists yet for `SW-SYNTH`, `SW-SAFE` or the menu path. The SWE-219 decision tables and independence-pair tests of 07 section 9.6 cover the three components from their first design (this was already required by the SRR ruling; this CR states it). No evidence class changes |
| Cost | None: no BOM, fabrication or shipping line |
| Schedule | None new: WP-SW-14 was already in the FW-B1 set of 07 section 3.1 under the decision 40 condition, which the SRR ruling met (ADR-027 section 2 already records it as required). Consequential text outside this CR: `docs/plan/schedule.md` FM-3 still reads "(and WP-SW-14 if package decision 40 adopts REQ-SYS-182)" |
| Requirements and traceability | None: no requirement or test case added, changed or retired; volatility contribution 0. `tools/traceability.py --report-only` on the branch: 245 requirements, 173 test cases, 0 violations, 2 warnings (the same as on `main`) |
| Regulatory | None: no 47 CFR Part 97 clause affected |
| Documentation | Changed by this CR: the four files of the table above. Consequential changes by their own writers and vehicles (PDR work plan section 5.3): SEMP section 7.1 ("the mission-critical frequency control and configuration load", WP-PDR-13); `docs/plan/schedule.md` FM-3 (WP-PDR-02, then WP-PDR-46); `tools/validate_docs.py` `SAFETY_CRITICAL_MODULES` (`SW-SYNTH`, WP-PDR-09); `hazards.json` OQ-SAF-014 closure and items X14 and X16 (WP-PDR-16b); charter section 10 decision 40 citation (owner, OD-31; 03 item g carries the wording) |
| Released units | None: no unit and no firmware release exists |

Classification rationale: Class II (05 section 2, adapted from the SE HB section 6.5.1.2.3 minor change). The change records in the configuration documentation rulings the owner already made at SRR (decisions 9 and 40, memo section 8, and the classification approval of memo section 7.1). It has no impact on form, fit, function, interchangeability, interfaces, safety, verification evidence or operator procedures beyond those rulings: the safety-critical set, the criteria unions and the SWE-134, SWE-219 and SWE-220 scope are the ones the owner approved. It touches no requirement, ICD, hazard or test case. The owner confirms or changes the class in section 7.

## 5. Implementation plan

| Step | Artifact and path | Responsible | Done (SHA) |
|---|---|---|---|
| 1 | Change set prepared on `cr/CR-010-apply-srr-decisions-9-and-40` (03, 07, `rmm.json`, `rmm.md`); `tools/render_rmm.py` render and `--check`; `tools/validate_docs.py`; `tools/traceability.py --report-only`; unit tests | Claude (software lead, 03 and 07 author; WP-PDR-17) | `5cd87cf` (prototype before disposition) |
| 2 | Section 6 independent impact review against `git diff ab2af2d 5cd87cf` | Independent reviewer (a separate invocation that authored no part of this CR or the change set) | |
| 3 | Owner disposition (section 7) | Owner | |
| 4 | Rebase or merge the branch onto current `main`; resolve any conflict with CR-003, CR-006 or CR-009 hunks in `rmm.json` (those CRs touch other rows) by keeping both; re-render `rmm.md`; re-run the four commands; every commit carries `CR: CR-010` | Claude | |
| 5 | Section 9 verification; delta iterations of INSP-009 and INSP-017 (03 and RMM) and INSP-010 and INSP-018 (07) verify INSP-009 finding-10 for the decision 9 and 40 parts | Independent reviewers | |
| 6 | Owner merge approval; `merge(CR-010): ...` with `--no-ff`; CSA regenerated | Owner, then Claude | |

Verification of the implementation (what the independent reviewer will check): every "proposed", "Proposed", "if ... concurs", "if decision 40 adopts", "if REQ-SYS-182 is adopted" and "conditional" occurrence tied to decisions 9 or 40 in the four files is resolved or intentionally kept (the section 4.2 table of 03 is kept by design); the quotes of decisions 9 and 40 equal the memo text; no criteria union, SWE-134 allocation, module list or class changed; `rmm.json` differs from `e326ddd1` in the five `implementation` fields only; `tools/render_rmm.py --check`, `tools/validate_docs.py`, `tools/traceability.py --report-only` and the unit tests exit 0.

## 6. Independent review of the impact assessment

Required by the PDR work plan rule C6 (every CR raised in the phase is reviewed before the owner is asked; lesson L4, `docs/cm/deviations.md` entries 1 and 2), although the template would mark a Class II change without requirement, ICD, hazard or test impact "Not required".

| Item | Reviewer (agent invocation) | Date | Finding | Resolution |
|---|---|---|---|---|
| | | | | |

Reviewer concurrence: pending.

## 7. CCB disposition (owner)

| Field | Value |
|---|---|
| Decision | |
| Class confirmed | |
| Date | |
| Conditions | |
| Rationale | |
| Waiver scope (if Approved (waiver)) | n/a |
| Re-look trigger and re-look-by review (if Deferred) | |
| Source | |

Disposition history (append only):

| Date | Decision | New target | Source |
|---|---|---|---|
| | | | |

## 8. Implementation record

| Commit | Files | Trailer check (`CR: CR-010` present) |
|---|---|---|
| `5cd87cf` (branch, prototype before disposition) | `docs/process/03-software-classification-and-rmm.md`, `docs/process/07-software-engineering-plan.md`, `docs/process/rmm.json`, `docs/process/rmm.md` | Yes |

Traceability report after implementation: to be generated at merge; renders regenerated: `docs/process/rmm.md` (branch).

## 9. Verification of implementation

| Impact item | Planned closure (from §4/§5) | Evidence (report path, TC id, analysis file) | Result |
|---|---|---|---|
| Safety and classification text | Section 5 verification list | | |
| RMM fields | `rmm.json` diff limited to five `implementation` fields; `render_rmm.py --check` exit 0 | | |
| Tool runs | `validate_docs.py`, `traceability.py --report-only`, unit tests exit 0 after the merge preparation | | |

Independent verifier (agent invocation): pending.

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
| 2026-09-27 | Submitted | Claude (software lead, WP-PDR-17) | this commit | Created with the impact assessment complete; change set prototyped on the branch at `5cd87cf`. Number CR-010 taken because CR-007 (WP-PDR-05), CR-008 and CR-009 were claimed by parallel wave 0 work packages |

## 12. Questions for the owner (answer with the disposition)

| # | Question | Recommendation |
|---|---|---|
| Q1 | Approve CR-010, which states your SRR rulings of decisions 9 and 40 in 03, 07 and the RMM, with no change to the safety-critical set you approved? | Approve, after the section 6 review reports no Major finding |
| Q2 | Confirm Class II | Confirm: it records rulings already made and touches no requirement, ICD, hazard or test case |
| Q3 | Charter section 10 citation (separate from this CR, because the charter is yours to change): adopt the closing parenthesis proposed in 03 section 6.5 item g, which adds SRR decision 40 and names 03 section 4.3 as the determination record | Adopt with the other charter edits of the PDR work plan (OD-31), before freeze F1 |
