---
id: CR-013
title: Fix the SRR peer review liens of 04, 07 and the SEMP
status: Dispositioned
class: II
originator: Claude
date_opened: 2026-09-27
phase: B
configuration_at_origination: baseline/srr (tag on 779f93f); HEAD 13a4f66 on main; branch base 5cd87cf (the CR-010 change set on ab2af2d); branch head 41c588c
baseline_affected: baseline/srr
affected_cis: [2]
affected_paths: [docs/process/04-verification-and-validation.md, docs/process/07-software-engineering-plan.md, docs/plan/semp.md]
affected_ids: [INSP-021, INSP-010, INSP-018, INSP-005, RFA-SRR-006, OQ-SE-001, OQ-SE-003, OQ-SE-005, OQ-SE-006, OQ-SW-001, RSK-059, TPM-019]
related: [CR-001, CR-002, CR-004, CR-005, CR-010, CR-011, CR-003, CR-006, INSP-024, INSP-030, INSP-027]
target_release: none
branch: cr/CR-013-process-04-07-semp-srr-liens
disposition: Approved
disposition_date: 2026-09-28
relook_trigger: null
relook_by: null
merge_sha: null
date_closed: null
---

# CR-013: Fix the SRR peer review liens of 04, 07 and the SEMP

Template: `docs/templates/change-request.md`. Process: `docs/process/05-configuration-and-data-management.md` (05 below) §5.1 to §5.3. File location: this file, committed on `main` with `Refs: CR-013`. The product changes are prototyped on the branch `cr/CR-013-process-04-07-semp-srr-liens` at commit `41c588c` (05 §5.2, Submitted: "Branch `cr/CR-NNN-<slug>` may be opened for prototyping; nothing merges"). Status: **Submitted**. The independent review of section 6 comes before the owner's disposition (PDR work plan rule C6, lesson L4). Originating work package: WP-PDR-13 of `docs/plan/pdr-work-plan.md` (revision 2), which closes carried items C-066, C-067, C-068 (text part), C-100 to C-110 and prepares C-113, and software reader items R-07, T-15, G-12 and G-13.

**Where the change is.** 04, 07 and the SEMP are Table 4-1 row 2 ("Process and planning documents", class CR from SRR) and are in `baseline/srr` unchanged on `main` at `13a4f66`. The branch is built on the CR-010 change set (`5cd87cf`), not on `main`, because the plan section 5.3 writer order for 07 is WP-PDR-17 (CR-010) then WP-PDR-13; 04 and the SEMP are not touched by CR-010, so their diff against `baseline/srr` is this CR alone. The exact text is `git diff 5cd87cf 41c588c`.

| File (Table 4-1 row 2) | Blob at `baseline/srr` and on `main` | Blob after CR-010 (`5cd87cf`) | Blob on this branch (`41c588c`) |
|---|---|---|---|
| `docs/process/04-verification-and-validation.md` | `0b197bba692237ed9860ba49c4422f12fa8512dc` | unchanged | `7617007ec517f76c286a15f469dfcd01c5d2cbde` |
| `docs/process/07-software-engineering-plan.md` | `bfe05f4327e79fa15c24d2cf8c14249804f946a8` | `3ae7d73b01810e47fd10251d798e0a047aaa72dd` | `0ad37a43a9d365408b78488f6c2b02933af56837` |
| `docs/plan/semp.md` | `ccfdecf98a6e2dc1371eb057e6aa37903b672de1` | unchanged | `2076eb0acfdfc283483eb2340bcbbf985df00c72` |

## 1. Description of the change

Every change below fixes a Minor finding that an SRR peer review record carries as "Lien: fix before PDR", or states in the three plans a fact that another approved or submitted change has already made true of the tree. No requirement, test case, hazard, control, risk score, ICD, RMM disposition, compliance-matrix disposition, gate criterion or process rule changes, with one exception named in section 1.2 item 12, where a rule gap is recorded as an open item and not changed. The before and after texts are abridged here; the prototype commit holds the full text.

### 1.1 `docs/process/04-verification-and-validation.md` (record INSP-021, `docs/reviews/SRR/checklists/process-04-verification-and-validation.md`)

| # | Location | Finding | Before (abridged) | After (abridged) |
|---|---|---|---|---|
| 1 | Header, Status | Record of the change | "draft for SRR; baselined with the charter" | "baselined at SRR with the charter (`baseline/srr`, blob `0b197bba`)" |
| 2 | Header, "Changes after the SRR approval" | finding-9 (CR-002 change note) | CR-002 sentence only | Adds that CR-002 step 5 (`c774851`) made the tool accept the Inspection route, and a CR-013 paragraph listing this CR's changes |
| 3 | Section 4, Emulation row | finding-2 (a), C1 | "`ACC-EMU-001`, a research proposal name and not a charter section 6 identifier; charter issue C1" | "the accreditation scope statement `ACC-EMU-001`, an `ACC-<TOOL>-NNN` identifier of charter section 6 held inside that TV record ... charter issue C1 ..., resolved" |
| 4 | Section 4, Emulation row | finding-2 (b) | "`firmware/emu/` (`cwht-emu`, 07 section 9.4)" | "`firmware/emu/` (harness, vendoring form and file format fixed by the PDR emulator ADR, 07 sections 1.2 and 9.4)" |
| 5 | Section 4, Tool accreditation paragraph | finding-4 (c) | "the LTspice batch wrapper `tools/run_sim.py` (written by Claude before the first Simulation case is `Active`, PDR)" | "`tools/ltspice-batch.sh` (ADR-018; committed at `41d150e` with `tools/tests/test_ltspice_batch.py`; TV-014, not accredited on 2026-09-27), accredited before the first Simulation case becomes `Active` (PDR)" |
| 6 | Section 6 lead paragraph | finding-3 (a), A13 | "`sigrok-cli` is not installed and has no `tools/toolchain.lock.md` row at this date, alignment item A13" | "`sigrok-cli` and the sigrok-pico capture firmware are not installed, and `tools/toolchain.lock.md` section 1 carries a row for each with its TV record due TRR, alignment item A13, resolved" |
| 7 | Section 7.4 observation paragraph and command table | finding-4 (b) | Observed 2026-09-25 at `b8214ca` with untracked tools; 258 tests | Re-observed 2026-09-27 at `main` `7bb994f` (tool blob `12de3545`) in a clean worktree: `--help` options unchanged, 461 tests with 16 skipped and 1 repository-content failure (`test_repository_exit_zero`, from the record drift of `tool-validation-tv-001-to-tv-010.md`), fixtures exit 0 and 1; names CR-011 as the pending tool change |
| 8 | Section 7.4 rows 7.3.2 and 7.3.5 | finding-4 (a) | Due "before SRR" | Due PDR, as 02 section 8.5 row T-19 dates the retired list; each states CR-011 implements it; the facts that no `TC-VAL` case exists and that the SRR report gave the retired count (2) without the list |
| 9 | Section 7.4 row 7.3.6 | finding-9 | Inspection route under the open task, "CR-002 implementation step 3", "until the tool accepts it" | Inspection route "Implemented, no longer open", accepted since `c774851` (CR-002 step 5; `InspectionRouteTests`); the `HAZARD_INVERSE` promotion stays open and names CR-011 |
| 10 | Section 7.4 rows 7.3.4, 7.3.11, 7.3.12 and the option sentence | CR-011 section 4 Documentation row (04 §7.4 rows sent to the 04 writer) | Planned codes and options without an implementing change | Each planned code and option names CR-011 (Submitted) as its implementation; the "Implemented today" column stays as observed on `main`, so the rows read "yes" only from the CR-011 merge |
| 11 | Section 10.6 last paragraph | finding-3 (b), A12 | "`docs/plan/tpm.json` carries no NCR entry at this revision; whether to register one as a TPM is decided by the owner at SRR" | "`docs/plan/tpm.json` registers them as TPM-019 (`ncr-trend`), preliminary at SRR; the owner approves or removes it with the TPM definitions at PDR (SE-40; SEMP Appendix F item F-14; alignment item A12, resolved)" |
| 12 | Section 12, Targets bullet | 07 section 22 row "Coverage disposition for target-only code" (software reader G-12, G-13) | The four SWE-189 categories only | Adds the `target-only: verified by <TC-ID>` entry for code that does not compile for the host, as the SWE-190 complementary test and inspection, and the `target-only: Inspection` MC/DC entry for the CS-11 failure arms (07 section 9.5 items 2 and 3) |
| 13 | Section 14, row 4.2 | finding-3 (c), A10 | "a new risk ... (RSK-019 if no other risk is added first, before PDR; alignment item A10)" | "RSK-059 "No qualification testing at the environmental extremes" ... (opened 2026-09-25 from alignment item A10, resolved)" |
| 14 | Section 17, first bullet | finding-3 (d), A14 | "whose table labels these rows NA (wording alignment item A14)" | "whose table labels these rows Customized (NA), its term for a customization with the institutional reason (alignment item A14, resolved)" |
| 15 | Section 18 rows A3, A4, A10, C1 and the Status header | finding-3 (c), finding-2 (a) | A3, A4 "Open: RMM author, before SRR"; A10 Open; C1 Open | A3, A4 re-dated to the PDR readiness declaration with the RMM writer WP-PDR-17 and the re-checked state; A10 Resolved (RSK-059); C1 Resolved against charter `4e3f891` |

### 1.2 `docs/process/07-software-engineering-plan.md` (records INSP-010 `software-plan-07.md` and INSP-018 `software-plan-07-software-assurance.md`)

| # | Location | Finding | Change (abridged) |
|---|---|---|---|
| 1 | Section 1.2 paragraph after the table | INSP-010 finding-18 | "no decisions beyond the board `take()` match (CS-38)" becomes "beyond the CS-11 failure arms of `cwht-app::main`, the board `take()` `None` arm and the `Err` arm of each rustos driver constructor that returns `Result` (CS-38; CR-001, SRR decision 108)" |
| 2 | Section 8.1 Miri row | INSP-018 finding-11 | Adds the `api`-only G5 scope at rustos `2ec64c0` (SRR close-out item B, owner ruling 2026-09-27) and the FW-B1 return of the `pico2` decision functions (`cfg_attr` owner change, lock pin CR, plan register PCR-10) |
| 3 | Section 8.1 paragraph after the table | INSP-010 finding-14 | "`tools/toolchain.lock.md` rows 21 to 25" becomes the lock section 1 rows named after each tool, with the rule that lock rows are cited by tool name; "What remains for FW-B0" becomes the record that `miri`, `llvm-tools` and `rust-code-analysis-cli` 0.0.25 were installed on 2026-09-26 (SRR decision 109) |
| 4 | Section 8.3 accreditation schedule | 05 alignment item AL-13 (software reader T-15) | "the Rust toolchain, coverage and static analysis tools and the emulator are accredited by PDR, `picotool` and `cargo-binutils` by CDR" becomes the 05 section 13 schedule: by PDR `rustc`, `cargo`, `clippy`, `cargo-llvm-cov` with `llvm-tools`, `cargo-nextest`, `nightly-2026-08-24` (MSR-14; TV-023 also covers Miri), `tools/measurements.py`, the emulator; by CDR `cargo-audit`, `cargo-deny`, `cargo-geiger`, `rust-code-analysis-cli` with `tools/complexity_gate.py`, `tools/unsafe_audit.py`, `tools/sw_gate.sh`, `picotool`, `cargo-binutils` |
| 5 | Section 8.4 row G5 | INSP-010 finding-22, INSP-018 finding-11 | `miri test -p api -p pico2 --lib` becomes `miri test -p api --lib` with the item B and FW-B1 citation |
| 6 | Section 9.5 item 3 | INSP-010 finding-18 | "the one exception, the board `take()` match of CS-11" becomes the CS-11 failure arms (board `take()` and driver-construction `Err` arms), each in the MC/DC table as `target-only: Inspection`, with CR-001 section 5 as the inspection rule |
| 7 | Section 10.2 Readiness criteria row | INSP-010 finding-20 | "transcribed as a waiver in the SRR decision memo ... when it is written" becomes the memo section 8.2 citation and waiver number W1 (memo amendment A-1, `decision-memo.md#W1`) |
| 8 | Section 11.1, three sentences | INSP-010 finding-16 | "exits 1 until the schema exists" and "`tools/measurements.py` when it exists" and "which does not exist yet" become the committed facts: schema and fixture at `1d423e5`, `tools/measurements.py` and `test_measurements.py` at `3de1e2d`, TV-013 |
| 9 | Section 14.2 row i, L1 column | INSP-010 finding-17, INSP-018 finding-9 | "181 is a 07 addition not named in `hazard-analysis.md` section 7 row i" becomes REQ-SYS-181 listed with 180 and 182 (SRR decisions 38, 39, 40), as `hazard-analysis.md` section 7 row i names them |
| 10 | Section 17.1 rustos `api` row (and by "same" the `pico2` row) | Software reader R-07; 07 section 22 row "rustos license" | Pin `c54d35a` becomes `2ec64c0` (CR-004); the licence cell becomes MIT (`LICENSE` and `license = "MIT"`, `publish = false` in both manifests at `2ec64c0`, read with `git show`), `OQ-SW-001` answered, notices file with WP-PDR-47 |
| 11 | Section 22 lead-in and table | INSP-018 finding-8, INSP-010 finding-16, finding-17 | Six rows closed and removed, each with its evidence in the lead-in ("Paired assurance record fields", "Measurements schema and tool rows", "RMM rows SWE-089, SWE-090 and SWE-094", "Coverage disposition for target-only code", "Toolchain lock rows", "Artifacts beyond charter section 5"); rows re-checked on 2026-09-27 and re-dated with their PDR writers ("03 alignment with section 14", "Hazard analysis follow-ups", "Assurance routing of 05 and TS-002", "Frequency-control determination", "Software risk tags", "rustos license notice"); the "Menu override command path ruling" row points to charter edit CE-2 |
| 12 | Section 22, new row "Evidence preservation of the SRR roll-up" | INSP-010 finding-15 | Records that the fix the finding names (superseding records) does not clear `--check-records` as the tool stands, because `check_records` tests every `Measured` record, superseded or not, against the first commit that contains it; names the two options (tool skips superseded records, or the plan states that the check reports current records) and the owners (tool owner with a TV-013 re-run; the PDR roll-up by WP-PDR-47); due the PDR readiness declaration. No rule of section 11.1 is changed by this CR |
| 13 | Section 23, revision row A.9 | Record of this revision | New row after A.8 |
| 14 | Annex C gate outline, G5 line | INSP-010 finding-22, INSP-018 finding-11 | `-p api -p pico2` becomes `-p api` with the FW-B1 note |

### 1.3 `docs/plan/semp.md` (record INSP-005, `docs/reviews/SRR/checklists/semp.md`)

| # | Location | Finding | Change (abridged) |
|---|---|---|---|
| 1 | Header, Version row | Record of this revision | Version 0.5, 2026-09-27, proposed by CR-013 and not in the baseline until merged; 0.4 kept as the previous version |
| 2 | Section 3.4, DR and DRR paragraph | finding-12 | "the owner approves the deviation ... in the SRR decision memo (OQ-SE-003)" becomes "approved ... at SRR (SRR decision 4 ...; OQ-SE-003 closed)" |
| 3 | Section 4.3 table, Allocation row | CR-011 section 4 Documentation row (SEMP §4.3 sent to the SEMP writer) | "implemented: Warning at SRR, Error from PDR under `--gate`" and "planned before PDR" become the state on `main` (Warning; `--gate` and the T-15 codes implemented by CR-011, Submitted, on `main` from its merge) |
| 4 | Section 4.3 tool status paragraph | finding-10 | Rewritten at `main` `7bb994f`: `tools/measurements.py`, `tools/unsafe_audit.py`, `tools/complexity_gate.py` (all `3de1e2d`) and `tools/ltspice-batch.sh` (`41d150e`) exist, with their gates, rules and TV states; the test list cites the 16 `test_*.py` files |
| 5 | Section 6.0, gate rule for RF hardware | finding-12 | "The owner decides at SRR whether to accept hardware TRL 3 ..." becomes "The owner accepted at SRR ... (SRR decision 11 ...; OQ-SE-006 closed ...) and reconfirms it in the CDR decision memo" |
| 6 | Section 7.1, safety-critical determination sentence | CR-010 cross item (07 section 22 row "Frequency-control determination", SEMP author) | "... the shared safe-state manager, and the mission-critical frequency control and configuration load" becomes the charter section 10 list after SRR decisions 9 and 40: safety-critical adds the boot path, configuration guard, fault annunciation, the menu override command path, the scheduler and runtime, and the transmit frequency-word path with the frequency verification unit; mission-critical is the remainder of frequency control, the configuration store and its non-safety fields, and the key-input and keyer-mode selection path |
| 7 | Section 7.2, Documentation data row | finding-11 | "`tools/measurements.py` (planned)" becomes the four gate scripts and the LTspice wrapper, all existing |
| 8 | Section 7.3.1, decision sentence | finding-12 (same closure fact) | Cites SRR decision 2 and OQ-SE-001 closed |
| 9 | Section 7.4, MOP paragraph | finding-12 | "the owner decides at SRR whether MOE-013 ... is added" becomes the ruling (SRR decision 96, OQ-SE-005 closed), with the fact that `tpm.json` MOP-001 and MOP-002 still read MOE-001 on 2026-09-27 and are re-pointed by WP-PDR-29 |
| 10 | Section 9.0, first paragraph | finding-12 | "for owner approval at SRR (OQ-SE-003)" becomes "approved by the owner at SRR (SRR decision 4; OQ-SE-003 closed)" |
| 11 | Section 9.0, customization row 11 item (ii) | finding-13 | Adds the precondition "where the research analysis leaves one viable option" of §5.17 and ruling R-2 |
| 12 | Appendix E rows OQ-SE-001, 003, 005, 006 | finding-12 | Each gains its closure fact with the decision number (2, 4, 96, 11), in the form OQ-SE-002 already uses |
| 13 | Appendix F items F-06, F-08, F-09, F-12, F-15 | finding-12 (F-12); status of the others | F-12 acceptance part resolved (decision 11); F-06 names CR-011; F-08 names charter edit CE-1; F-09 resolved by charter `6ea6b1d`; F-15 part resolved (`tools/ltspice-batch.sh` committed) |

### 1.4 Not in this CR, and where each goes

- **INSP-021 finding-6, finding-8 and finding-10** are defects of the CR-002 record, owner "CR-002 originator", not of 04. The plan routes CR-002 record corrections to WP-PDR-47 (carried item C-096).
- **INSP-010 finding-15** (80 `--check-records` failures) needs a tool change or a plan rule decision first (section 1.2 item 12); the superseding records are appended at the PDR roll-up by WP-PDR-47. This CR records the gap and does not claim the finding fixed.
- **Charter edits** (carried item C-113: charter §12 HSI row, §10 decision 40 citation, §3 App. G table list for SE-34) are drafted for the owner as CE-1 to CE-3 in `docs/reviews/PDR/owner-actions.md` section 11 (OD-31), an Informational file committed on `main` with this CR file. The charter is the owner's to change.
- **The 07 section 14.1 decision 9 and 40 text** is CR-010's (WP-PDR-17), on which this branch is built.

## 2. Reason

The SRR records INSP-021, INSP-010, INSP-018 and INSP-005 carry these Minor findings as "Lien: fix before PDR", due at the PDR readiness declaration (charter section 4 item 3; lien L-6, RFA-SRR-006). A Minor RID not fixed before the next review breaks charter section 4 item 3 and leaves entrance criterion S2 open. The three files are CR-controlled from SRR (05 Table 4-1 row 2), so a non-editorial fix needs an approved CR (05 §5.1 row 1). The plan assigns them to WP-PDR-13. Workaround while the CR is open: none needed; every defect is a stale statement, a wrong citation or a wording gap, and none sets a conflicting value, rule or disposition in the baseline (every record rates each one Minor).

## 3. Alternatives considered

| Alternative | Why rejected or deferred |
|---|---|
| Do nothing | The liens stay open at the PDR readiness declaration; S2 cannot be met, and 04 and 07 keep stating tool and plan facts that are no longer true of the tree |
| Commit the fixes on `main` with an `Editorial:` trailer | Not permitted: 05 §2 defines an editorial change as one that "alters no technical meaning" and never admits one to a number, an ID or a status field; the section 7.4 due gates and statuses, the section 12 report entry, the 07 G5 command, the 07 §8.3 schedule and the SEMP closure facts all change meaning or status |
| One CR per document | Three CRs, three §6 reviews and three dispositions for one Class II lien set on one Table 4-1 row; one CR costs the owner less. The SRR records are still delta-iterated one per document |
| Build the 07 part on `main` instead of on CR-010 | Rejected: the plan section 5.3 writer order puts WP-PDR-17 before WP-PDR-13 on 07, and CR-010 changes 07 section 14.2 row i, which finding-17 also changes; building on `main` would force a conflicting merge |
| Fix INSP-010 finding-15 by appending superseding records now | Rejected: as the tool stands the check still fails on the superseded records (section 1.2 item 12), so the lien would be reported fixed while `--check-records` exits 1; the decision on the rule comes first |
| Mark the section 7.4 rows "yes" now, since CR-011 implements them | Rejected: the section is "evidence, not assertion" (charter section 11 rule 2); `main` does not carry the code until CR-011 merges |

## 4. Impact assessment (CM plan §5.3)

| Field | Assessment (numbers, IDs, paths) |
|---|---|
| Performance margins | None: no MOP, TPM or budget value changes. SEMP §7.4 now states the decision 96 ruling; the `moe_ids` of MOP-001 and MOP-002 are not changed by this CR (WP-PDR-29, `tpm.json` writer) |
| Safety | None to a hazard, control or `control_req_ids` link. SEMP §7.1 now names the safety-critical and mission-critical components as charter §10 already does after SRR decisions 9 and 40, which is the list of 07 §14.1 (CR-010); the component list does not change. 07 §9.5 item 3 and 04 §12 now name the CS-11 driver-construction failure arms in the MC/DC table, which CR-001 already admitted, so the MC/DC scope is stated completely and not widened. Hazard analysis re-issue: no. RF exposure evaluation: no |
| Risk | None added, closed or re-scored. 04 now cites RSK-059, which exists. 07 §22 re-dates the software-tag row to the register writer (WP-PDR-18) |
| Software classification and tailoring | None: no classification, `rmm.json` disposition or compliance-matrix row changes. 07 §8.3 now states the TV schedule of 05 §13 (05 AL-13); 05 is unchanged. 04 §18 A3 and A4 re-date two RMM text items to the RMM writer (WP-PDR-17) |
| Interfaces | None: no ICD changes; no external interface changes |
| Operations and ConOps | None: no mode, transition, operator procedure, handbook or maintenance instruction changes |
| Cybersecurity | None: no USB firmware-load or key-input path changes (07 §16 unchanged) |
| Verification | No TC invalidated; no method or evidence class changes. 04 §12 adds a report entry for target-only code that 07 §9.5 item 2 already required, so the `TC-SW-COV-001` report content is now stated once in the governing document (07 §1 precedence rule). 04 §7.4 changes no tool rule; it records the observed state and names CR-011. **Review records invalidated as evidence for the changed blobs:** INSP-021 (04 `0b197bba`), INSP-005 (SEMP `ccfdecf9`), and INSP-010 and INSP-018 (07, already invalidated by CR-010 for `bfe05f43`); `tools/validate_docs.py` at `41c588c` fails exactly these four plus the three that CR-010 already fails (INSP-009, INSP-017, INSP-006), 43 of 50 pass. Each clears when its delta iteration names the new blob (section 5 step 4) |
| Cost | None |
| Schedule | None on vendors or gates. Order: CR-010 merges first, then this CR (07 writer order). The §6 review, the four delta iterations and the disposition are requested for session B1b (Thu 10-01) or B2 (Fri 10-02) at the latest, so 04, 07 and the SEMP freeze at F1 (Sun 10-04) on a known basis. If CR-010 is rejected or changed, this branch is rebased onto `main` (or the new CR-010 head) and 07 section 14.2 row i is re-applied to the text that results; the other 07 hunks do not overlap CR-010's. The SEMP hunks share no line with CR-003 (SEMP lines 141, 332, 363, 364, 368) or CR-006 (lines 45, 102, 148, 422) except the Version row, where each CR prepends its own entry; the CR merged second rebases |
| Requirements and traceability | None added, modified, deleted or retired. Volatility contribution 0 (02 §10.4: A = 0, M = 0, R = 0). `tools/traceability.py --report-only` at `41c588c`: exit 0, 245 requirements, 173 test cases, 0 violations, 2 warnings (`SYS_UNALLOCATED` REQ-SYS-125 and REQ-SYS-148, both present on `main`); the generated report and data were restored with `git checkout` |
| Regulatory | None |
| Documentation | With this CR (branch): 04, 07 (revision A.9), SEMP (version 0.5). On `main` with this file: `docs/reviews/PDR/owner-actions.md` section 11 (charter edit list, Informational). After merge: the four SRR records get their delta iterations (section 5), and the SRR log secretary moves the RFA-SRR-006 items (WP-PDR-15). No VDD or package manifest exists |
| Released units | None: no unit exists |
| At risk | The 04 §7.4 rows and SEMP §4.3 and F-06 texts that name CR-011 are drafted on CR-011 as submitted. If CR-011 is rejected or changes a code, those cells are re-stated before F1 (plan rule C8) |

Classification rationale: Class II. The change touches three Table 4-1 row 2 process and planning documents only and changes no requirement, verification method, interface, hazard control, safety-critical component, schedule commitment or cost (05 §5.3). Adapted from the SE HB §6.5.1.2.3 minor change.

## 5. Implementation plan

| Step | Artifact and path | Responsible | Done (SHA) |
|---|---|---|---|
| 1 | 04, 07 and SEMP changes of section 1, prototyped on the branch | Claude (04 author, 07 author, SEMP author; WP-PDR-13) | `41c588c` |
| 2 | Tool runs on the branch: `tools/validate_docs.py`, `tools/traceability.py --report-only` | Claude | Run at `41c588c`: traceability exit 0 (0 violations, 2 warnings); validate_docs 43 of 50, the 7 failures being the record drift rule on INSP-005, INSP-006, INSP-009, INSP-010, INSP-017, INSP-018 and INSP-021 (the last four named in section 4, the other three CR-010's) |
| 3 | Section 6 independent review of this impact assessment | Independent reviewer (a separate invocation that authored nothing in this CR) | |
| 4 | Delta iterations verifying each finding on the frozen blobs below: INSP-021 (`reviewer:INSP-021`), INSP-010 with its software assurance pair INSP-018 (07 §2.1.1 Yes for 07), INSP-005 (`reviewer:semp`). Each record names the frozen blob; while the blob is only on this branch, the record sets `reviewer_verdict` (and `assurance_verdict`) and keeps the record `verdict` held until the merge (lead SE convention of 2026-09-27); the record verdict is set in the merge commit or the commit right after it. INSP-010 and INSP-018 also carry CR-010's delta for 07 `3ae7d73b`; one delta iteration may verify both CRs on `0ad37a43` if both merge together | Independent reviewers (new invocations of each record's reviewer role) | |
| 5 | After approval: rebase onto `main` after CR-010 merges (and onto CR-011's merge if it lands first, re-stating the section 7.4 cells), re-run step 2, merge `--no-ff` with the owner's merge approval | Claude (CM) | |
| 6 | Section 9 verification of the implementation | Independent verifier | |

Frozen products for review (plan rule C2), at branch commit `41c588c`: `docs/process/04-verification-and-validation.md@7617007ec517f76c286a15f469dfcd01c5d2cbde`, `docs/process/07-software-engineering-plan.md@0ad37a43a9d365408b78488f6c2b02933af56837`, `docs/plan/semp.md@2076eb0acfdfc283483eb2340bcbbf985df00c72`.

Verification of the implementation (what the reviewers check, every case named, plan rule C7): each before and after of section 1 against the blob; that no other line of the three files changed (`git diff 5cd87cf 41c588c`); for INSP-021: finding-2 (a) and (b), finding-3 (a) to (d), finding-4 (a) to (c) and finding-9, each at its location, plus charter section 6 for C1 and 02 section 8.5 row T-19 for the re-dated rows; for INSP-010: finding-14, 16, 17, 18, 20 and 22, and the finding-15 open row against `tools/measurements.py` `check_records`; for INSP-018: finding-8, 9 and 11; for INSP-005: finding-10, 11, 12 (every one of the eight locations it names: Appendix E rows OQ-SE-001, 003, 005, 006; §3.4; §9.0; §6.0; §7.4; F-12) and 13; the 07 §8.3 schedule against 05 §13 row by row; the 07 §17.1 licence facts against `git -C /Users/robinonsay/rust/rustos show 2ec64c0:LICENSE` and both manifests; the SEMP §7.1 component list against charter §10 and 07 §14.1 at `5cd87cf`; the 04 §7.4 command results by re-running them on a clean worktree of the observed commit.

## 6. Independent review of the impact assessment

Required before the owner's disposition (plan rule C6). Not yet performed.

| Item | Reviewer (agent invocation) | Date | Finding | Resolution |
|---|---|---|---|---|
| Pending | | | | |

Reviewer concurrence: pending.

### 6.1 Impact review round 1: independent reviewer (2026-09-27)

Reviewer: independent reviewer agent (WP-PDR-13 reviewer invocation), a separate invocation. It authored no part of this CR, of WP-PDR-13, of CR-010 or of either branch commit. It also wrote the product delta records INSP-058 (04), INSP-059 (07) and INSP-064 (SEMP), committed at `ecdfd1f`. The table and the "pending" line above are the template placeholders and are left as written; this round is the first review entry. Configuration reviewed: this file at blob `560fe69a` on `main` (`8470350`, unchanged to `ecdfd1f`); branch `cr/CR-013-process-04-07-semp-srr-liens` at `41c588c` (parent `5cd87cf`). Method: `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` first, then `grep` and `git` only to pin lines and blobs; `git diff --word-diff 5cd87cf 41c588c`; detached scratch worktrees of `41c588c` and `7bb994f` (removed after use), in which the reviewer ran `tools/validate_docs.py`, `tools/traceability.py --report-only`, `unittest discover -s tools/tests` and the section 7.4 fixture commands; `git merge-tree --write-tree main 41c588c`; `git show` of the rustos commits `2ec64c0` and `c54d35a` (the owner's rustos working tree was not read); `git diff` of the other open `cr/` branches for overlap with the three files. LTspice was not run.

| Item | Reviewer (agent invocation) | Date | Finding | Resolution |
|---|---|---|---|---|
| IR-F1 (Minor) The SRR record drift does not clear by the delta records as planned | Independent reviewer agent (CR-013 impact review) | 2026-09-27 | Section 4 (Verification) says the seven `validate_docs.py` failures at `41c588c` clear "when its delta iteration names the new blob (section 5 step 4)", and section 3 says "the SRR records are still delta-iterated one per document". The plan (section 3.1 "Records") and the WP-PDR-13 brief put the delta iterations in new records under `docs/reviews/PDR/checklists/`. They are filed as INSP-058, INSP-059 and INSP-064, plus the INSP-018 assurance pair still to be filed. A new PDR record does not change the `product_files` of the SRR records INSP-021, INSP-010, INSP-018 and INSP-005, which are APPROVED and name blobs `0b197bba`, `bfe05f43` and `ccfdecf9`. So after the merge, `validate_docs.py` on `main` still fails those four records (and INSP-009, INSP-017 and INSP-006 until CR-010's step 5). This breaks readiness R1 for every later record and `test_repository_exit_zero`. No step names who updates the SRR records, or when. CR-010 section 5 step 5 re-issues its SRR records on its branch, and CR-010 round 2 IR2-F2 already asks the two CRs to agree | Author: add to section 5 a step that names, for each of INSP-021, INSP-010, INSP-018 and INSP-005, the record update that makes it name the new blob (for example a dated re-issue appended by that record's reviewer, pointing to INSP-058, INSP-059, the INSP-018 pair and INSP-064, with `product_files` updated), and its place (the merge commit, or the CR branch as CR-010 does). Correct the section 4 sentence. Settle the placement with CR-010 (IR2-F2) before step 5 |
| IR-F2 (Minor) Dated tool-state texts and `related` go stale before the merge; step 5 re-runs tools only | Same | 2026-09-27 | Several texts are dated at `main` `7bb994f`, and `main` has moved since. `86ff3b0` (12:45, after the prototype at 12:34) adds `tools/render_tpm.py`, `tools/scad2step.py`, `tools/csa.py`, `tools/check_commit_msg.py` and `tools/normalize_fab.py`. At the merge, SEMP section 4.3 ("`render_tpm.py` is written by Claude before PDR"), SEMP F-15 ("`tools/scad2step.py` not yet committed") and the 04 section 7.4 observation will be stale. Branch `cr/CR-014-tool-liens-srr` (WP-PDR-09; no CR file on `main` yet) changes `tools/validate_docs.py` (`16cdd3e`: 05, TS-002 and `SW-SYNTH` added to the tool constants) and `tools/measurements.py`. That makes the re-checked 07 section 22 rows "Assurance routing of 05 and TS-002" ("the constant names neither") and "Tool constants" stale when it merges. `related` does not name it. Step 5 re-runs only `validate_docs.py` and `traceability.py`. Rebasing onto a new `main` does not refresh these texts, and a blob change after rebase needs delta iterations (plan rule C2) | Author: in step 5, add a re-observation at the rebase commit of 04 section 7.4, SEMP section 4.3, F-06 and F-15, and 07 section 22 rows "Assurance routing" and "Tool constants". Re-state them if the tree changed, and send the changed blobs to delta iterations of INSP-058, INSP-059 (with the pair) and INSP-064. Add the WP-PDR-09 tool-lien CR to `related` when it is numbered. Section 4 "At risk" should name it beside CR-011 |
| IR-F3 (Minor) A due-gate change is not in section 1.1 or the Schedule field | Same | 2026-09-27 | Item 10 of section 1.1 says the 7.3.4, 7.3.11 and 7.3.12 rows only add the CR-011 citation. The 7.3.4 Due cell also changes, from "CDR" to "CDR (`CLOSED_NOT_INSTALLED`: PDR, with CR-011)". Under the 04 section 7.4 lead ("the gate's readiness declaration is blocked until its unit test passes"), the PDR readiness declaration then waits on the CR-011 merge. 02 section 8.5 row T-11 still dates the code CDR. The change tightens a gate and relaxes nothing, but the owner does not see it in section 1 or in the Schedule field (INSP-058 finding-3) | Author: either restore "CDR" (keeping the CR-011 citation), or list the re-date in section 1.1 item 10 and the PDR dependency on CR-011 in section 4 Schedule, with the 02 T-11 alignment sent to the 02 writer (WP-PDR-12) |

Items checked with no finding:

- **Class II is correct** under 05 section 5.1. The three files are Table 4-1 row 2 (class CR from SRR), and no requirement, verification method, interface, hazard control, safety-critical component, cost or vendor schedule changes. `affected_cis: [2]` is right. `affected_paths` equal the branch change set (`git diff --stat 5cd87cf 41c588c`: exactly the three paths, 67 insertions, 69 deletions). Blobs in the header table and section 5 equal `git ls-tree` of `baseline/srr`, `5cd87cf` and `41c588c`. The prototype commit carries `CR: CR-013`.
- **Tool runs reproduced at `41c588c`:** `validate_docs.py` 43 passed, 7 failed, the seven records named in section 4 and step 2. `traceability.py --report-only`: exit 0, 245 requirements, 173 test cases, 0 violations, 2 warnings (`SYS_UNALLOCATED` REQ-SYS-125, 148). Section 7.4 of 04 re-run on a clean worktree of `7bb994f`: 461 tests, 16 skipped, 1 failure (`test_repository_exit_zero`, from `tool-validation-tv-001-to-tv-010.md`); fixtures exit 0 and 1. The one count error (15 test modules, not 16) is INSP-058 finding-1 and INSP-064 finding-1.
- **Merge:** `git merge-tree --write-tree main 41c588c` completes with no conflict on today's `main`. The stated order (CR-010 first, then this CR) is necessary because the branch contains `5cd87cf`. No other open `cr/` branch (CR-008, 009, 011, 012, 015, 016) changes 04, 07 or the SEMP. CR-014's branch changes tools only (IR-F2).
- **Safety:** SEMP section 7.1 now lists the same safety-critical and mission-critical components as charter section 10 and 07 section 14.1 at `5cd87cf`. 07 section 9.5 item 3 and 04 section 12 name the CS-11 driver-construction arms that CR-001 (Dispositioned, SRR decision 108) admitted. The MC/DC scope is stated completely and is not widened. No hazard, control or `control_req_ids` changes.
- **Software classification and tailoring:** 07 section 8.3 equals 05 section 13 row by row for the software tools. No RMM or compliance-matrix row changes. 04 A3 and A4 re-date RMM text items to the `rmm.json` writer WP-PDR-17 (plan section 5.3). The facts they state hold at `main` and at `5cd87cf`.
- **Verification:** no case is invalidated. INSP-010 finding-15 is correctly left open: at `7bb994f`, `tools/measurements.py` `check_records` tests every `Measured` record whether or not a later record supersedes it. Question 2 of section 12 is the right owner decision. The rustos licence facts of 07 section 17.1 hold (`2ec64c0` `LICENSE` MIT; `license = "MIT"`, `publish = false` in both manifests; neither at `c54d35a`).
- **Requirements, cost, interfaces, operations, cybersecurity, regulatory, released units:** None, as stated. Volatility contribution 0.
- **Charter:** the CR does not edit the charter. The three charter items go to the owner as CE-1 to CE-3 (`docs/reviews/PDR/owner-actions.md` section 11, Informational). Their "before" texts equal charter sections 12, 10 and 3 verbatim.
- **Assurance routing:** 07 is a 07 section 2.1.1 "Software plans" Yes product. Step 4 names the INSP-018 pair, which is still to be filed as `docs/reviews/PDR/checklists/software-plan-07-software-assurance.md`. 04 and the SEMP need none, as INSP-021 and INSP-005 recorded.

Product findings are in the delta records and are not repeated here: INSP-058 finding-1 to finding-3, INSP-059 finding-1 to finding-3, INSP-064 finding-1. All are Minor liens under plan rule C1, and none changes an impact field except INSP-058 finding-3, which is IR-F3 above.

Reviewer concurrence: concur with Class II and with the change as a closure of the named SRR liens. **Impact review complete, with findings: 0 Major, 3 Minor (IR-F1 to IR-F3).** The CR stays Submitted. The author resolves IR-F1 and IR-F3, or states why not, before question 1 of section 12 goes to the owner. IR-F2 is resolved before step 5. None needs a further impact review round unless a product blob changes.

## 7. CCB disposition (owner)

Dispositioned 2026-09-28 (table below); originally requested at owner session B1b (Thu 10-01), or B2 (Fri 10-02) at the latest, after the section 6 review and after CR-010's disposition. Questions for the owner are in section 12.

| Field | Value |
|---|---|
| Decision | Approved |
| Class confirmed | II (proposed II; concurred in section 6) |
| Date | 2026-09-28 |
| Conditions | None stated by the owner. The merge follows section 5 steps 4 to 6, after CR-010 merges |
| Rationale | Fixes the SRR liens of INSP-021, INSP-010, INSP-018 and INSP-005 in 04, 07 and the SEMP. Section 6: 0 Major, IR-F1 to IR-F3 Minor and open |
| Waiver scope (if Approved (waiver)) | n/a |
| Re-look trigger and re-look-by review (if Deferred) | |
| Source | Chat transcription by Claude (configuration manager) on 2026-09-28. The presenter asked the owner to approve CR-007 to CR-016, the SRR lien fixes that passed their impact reviews (recommendation: approve all ten). Owner statement, verbatim: "Um, and then, yeah, I think you're uh, good to continue." The lead SE reads it as approval of item 1 as recommended, with the branches to merge after the section 9 checks (`docs/plan/status/status-2026-09-28.md` section 1, commit `e288add`, which transcribes the full statement); the owner is asked to correct any line |

Disposition history (append only):

| Date | Decision | New target | Source |
|---|---|---|---|
| 2026-09-28 | Approved | none | owner, `status-2026-09-28.md` section 1 (`e288add`), transcribed by Claude (configuration manager) |

## 8. Implementation record

Not yet implemented (the branch holds a prototype only).

| Commit | Files | Trailer check (`CR: CR-013` present) |
|---|---|---|
| `41c588c` (prototype, branch `cr/CR-013-process-04-07-semp-srr-liens`, parent `5cd87cf`) | `04-verification-and-validation.md`, `07-software-engineering-plan.md`, `semp.md` | Present |

Traceability report after implementation: to be regenerated at merge; no render changes (the three files are hand-written Markdown).

## 9. Verification of implementation

| Impact item | Planned closure (from §4/§5) | Evidence (report path, TC id, analysis file) | Result |
|---|---|---|---|
| | | | |

Independent verifier (agent invocation): pending.

Configuration manager pre-merge check (2026-09-28; performed at the disposition, not the independent verification, which stays pending). Method: `git merge-tree --write-tree` of the branch head with `main` (no conflict), then a trial `git merge --no-ff` in a detached scratch worktree of `main` (discarded afterwards, no ref kept), `tools/validate_docs.py` and `tools/traceability.py --report-only` on the trial merge, and the failure set compared with the baseline. Baseline on `main` at `e288add`: `tools/validate_docs.py` 102 passed, 8 failed (all record drift already on `main`: SRR `adrs-001-to-025.md`, `process-02-requirements-and-traceability.md`, `tool-validation-tv-001-to-tv-010.md`, `trade-studies-ts-001-ts-002.md`, `trade-study-ts-002-software-assurance.md`; PDR `cm-plan-05-software-assurance.md`, `configuration-status.md`, `lessons-learned.md`); `python -m unittest discover -s tools/tests` 596 run, 1 failure (`test_repository_exit_zero`, the same drift), 14 skipped; `tools/traceability.py --report-only` 0 violations, 2 warnings. Branch head `41c588c`, stacked on the CR-010 change set `5cd87cf`, so it cannot merge before CR-010. Trial merge of CR-010 then CR-013: `validate_docs.py` 95 passed, 15 failed; seven new failures, CR-010's five plus `docs/reviews/SRR/checklists/process-04-verification-and-validation.md` (INSP-021) and `semp.md` (INSP-005). `traceability.py --report-only`: 0 violations, 2 warnings. Merge held: CR-010 not merged; IR-F1 (the SRR records INSP-021, INSP-010, INSP-018 and INSP-005 keep naming the old blobs after the PDR deltas INSP-058, INSP-059 and INSP-064) is unresolved; INSP-059 carries `assurance_verdict: NEEDS CHANGES`.

## 10. Closure

| Field | Value |
|---|---|
| Owner merge approval | 2026-09-28, with the disposition: "their branches merge after the section 9 checks" (lead SE reading, `docs/plan/status/status-2026-09-28.md` section 1). Merge held at the disposition: see the section 9 configuration manager pre-merge check |
| Merge commit | |
| Waiver entered in CSA item 12 and affected VDDs | n/a |
| CSA regenerated | |
| Date closed | |

## 11. History

| Date | State | By | Commit on main | Note |
|---|---|---|---|---|
| 2026-09-27 | Draft, then Submitted | Claude (WP-PDR-13 author) | this file's commit | Created with the impact assessment complete; product prototype on the branch at `41c588c`, built on the CR-010 change set `5cd87cf` |
| 2026-09-28 | Dispositioned (Approved) | Claude (configuration manager), transcribing the owner | the commit that records this row (`Refs: CR-013`) | Owner approval of CR-007 to CR-016 as recommended (`status-2026-09-28.md` section 1); merge held at the disposition: after CR-010; SRR record re-issues (IR-F1) not done (section 9 pre-merge check) |

## 12. Questions for the owner (answer with the disposition)

1. Approve CR-013 as Class II? Recommendation: approve. Every change fixes a Minor lien of an SRR record or states a fact already true of the tree.
2. INSP-010 finding-15: which rule for superseded measurement records? (a) the tool tests the superseding record and skips the superseded one, or (b) the plan states that the check reports current records only and superseded failures stay as history. Recommendation: (a), because it keeps `--check-records` able to exit 0 without editing history, and the TV-013 re-run shows the change. Either answer goes to the tool owner and WP-PDR-47; it is not part of this CR's product change.
3. Charter edits CE-1 to CE-3 (`docs/reviews/PDR/owner-actions.md` section 11) are asked separately under OD-31 at B3; they do not depend on this CR.

Answers recorded with the disposition (2026-09-28; the lead SE reading of the owner's approval "as recommended", the owner is asked to correct any answer): Q1 approved, Class II. Q2 (a): the tool tests the superseding measurement record and skips the superseded one; the answer goes to the tool owner and WP-PDR-47, outside this CR's product. Q3 (charter edits) stays with OD-31.
