---
# Peer-review record front matter (charter sections 2 and 5; docs/process/01-lifecycle-and-reviews.md
# section 13; docs/process/07-software-engineering-plan.md sections 2.1.1, 10.2 and 15). This is the
# paired software assurance record of INSP-053 (docs/reviews/PDR/checklists/adrs-001-to-027.md, the
# file review of the WP-PDR-14 ADR errata), at the path INSP-053 names in assurance_reviewer_agent and
# cross item 4, dispatched by the lead SE under 07 section 2.1.1 row "Trade studies and ADRs whose
# decision constrains a safety-critical or mission-critical component".
# Checklist applied: docs/templates/peer-review-checklist-software-assurance.md revision A AS ON ITS
# CR-012 BRANCH (cr/CR-012-pdr-checklist-templates at 7784672, blob 5b135285; CR-012 not merged).
# tools/validate_docs.py fails a record whose checklist field names a template absent from main, and the
# lead SE convention of 2026-09-27 does not change the validator, so the checklist field names
# peer-review-checklist-design revision B (the checklist 08 section 3.5 and 07 section 2.1.1 row 3 give
# ADRs, the one INSP-053 applied) and checklist_software_assurance records the template actually applied
# (the INSP-037 and INSP-047 form). The product blobs are all on main; only the template is branch-only.
id: INSP-066
checklist: peer-review-checklist-design
checklist_revision: B
checklist_software_assurance: "docs/templates/peer-review-checklist-software-assurance.md@5b13528504868b2add0f0b1e329c63aa2b54cdf4 (revision A, CR-012 branch head 7784672)"
checklist_file: docs/reviews/PDR/checklists/adrs-001-to-027-software-assurance.md
product: docs/decisions/adr/
# product_commit and product_files: equal to INSP-053; every blob equals git rev-parse HEAD:<path> and
# git hash-object <path> at HEAD e6d87a1 (28 of 28; the only ADR-directory commit after 0f4a7ad is
# 9ac2c42, which adds ADR-031, outside the product)
product_commit: "0f4a7add8fd6aa2098a2cabc16758ec86b624365"
product_files: ["docs/decisions/adr/ADR-001-class-a-rigor-and-review-gates.md@876ee6b6ecdcf4afdf5769c68e32547dcf33db3a", "docs/decisions/adr/ADR-002-2m-only-rev-a-70cm-ready.md@0482a9ce436ca8620d1111d0ba89490ca179e3df", "docs/decisions/adr/ADR-003-true-cw-a1a-5w.md@6b1bae000df907f944a73279e2cdc2a2b20305e8", "docs/decisions/adr/ADR-004-pico2-module-micro-usb.md@a9ddddf3eefa793bdf2cd30188a9d0ee9e4d6738", "docs/decisions/adr/ADR-005-2s-18650-holders.md@ae70b0ab96cedae4c8d94f2956c4c3d510ab7cab", "docs/decisions/adr/ADR-006-rotary-encoder-tuning.md@9bc18133e045ffeeb7340174f0cd12a5bb86d7a7", "docs/decisions/adr/ADR-007-pcbway-turnkey-smt-kit-model.md@64d02a0d15a64f0c59b61ca51acfcb17b98e1479", "docs/decisions/adr/ADR-008-openscad-freecad-step-pcbway-cnc.md@9fa98f3eebb5085765600905a4e3ccbdabec3f34", "docs/decisions/adr/ADR-009-straight-key-and-paddle-trs.md@87d42347a01d9e4e6feeca3511189a8cb4a8843f", "docs/decisions/adr/ADR-010-semi-break-in-only.md@adfa22f86c02eb56fca42883f3d83d86abba6964", "docs/decisions/adr/ADR-011-host-first-software-verification.md@e5e3e022c8611fb39111e4078d7d65c4ef7dcb2a", "docs/decisions/adr/ADR-012-pa-device-sourcing-constraint.md@5c858107d2a3e6a282ef9e7db36f45467491dfaf", "docs/decisions/adr/ADR-013-synthesizer-by-cost-performance-trade.md@972d5a70d340b1d5eea3a8cf4d29614ca80a6e4d", "docs/decisions/adr/ADR-014-licensed-operators-only.md@7887e06419c676f9cc6488482f9dc23a5d198531", "docs/decisions/adr/ADR-015-operator-model-ops-a-guest-lock.md@20a8668716af0e7f096dcfb97bd680dab17717a9", "docs/decisions/adr/ADR-016-full-2m-band-coverage.md@a9a668c26a2377611486e609a9bf730e66558f0d", "docs/decisions/adr/ADR-017-open-source-mit.md@2e3ca2ff77e918559b4c5c84d5a1992dba2ae06b", "docs/decisions/adr/ADR-018-ltspice-telemetry-opt-out.md@1d8b6132e5e947fcd0c34f51d81ed469058217a7", "docs/decisions/adr/ADR-019-rustos-upstream-drivers.md@8c6cf447c3aa799f57ea7dfff759f634200dddd9", "docs/decisions/adr/ADR-020-battery-life-target.md@1d42721f6e5a61e7d74e96139c54d14c7374df8c", "docs/decisions/adr/ADR-021-tinysa-ultra-purchase.md@b68357d913003138baf83f2d5c7593f2b52a9adf", "docs/decisions/adr/ADR-022-harmonic-suppression-target.md@049df7d74cea4e454a29e4e5e3f1bf71775b5adb", "docs/decisions/adr/ADR-023-tcxo-and-band-edge-guard.md@b10388a30a47079c0f635a8c857e9e0febd96020", "docs/decisions/adr/ADR-024-keyer-speed-range.md@a15430ea20b7680cecaaf76a698701a7636a0a62", "docs/decisions/adr/ADR-025-build-quantity-cap.md@32783853ef60b0e1e12b30133e4cbf1ab7cfccb8", "docs/decisions/adr/ADR-026-semi-break-in-hang-and-lead-in.md@0234cb5093a2b0cca6a8c433c1529f453748fa32", "docs/decisions/adr/ADR-027-firmware-runtime-rustos-a0.md@a319c789f620f6fda26eeb392796fe2f4ba6c63e", "docs/decisions/adr/README.md@5f119ab4d7d2af35b9c1cd1274fdea9e02b8aae1"]
# inputs read (not reviewed), blobs at HEAD e6d87a1
input_files: ["docs/reviews/PDR/checklists/adrs-001-to-027.md (INSP-053, committed e515649)", "docs/process/07-software-engineering-plan.md@bfe05f4327e79fa15c24d2cf8c14249804f946a8", "docs/safety/hazards.json (version 0.5.0-pha)", "docs/requirements/sys/requirements.json", "docs/requirements/sw/sw-keyer/requirements.json", "docs/process/rmm.json", "docs/decisions/trade-studies/TS-002-firmware-runtime-make-buy.md", "docs/reviews/SRR/package.md", "docs/plan/pdr-work-plan.md"]
paired_record: INSP-053
product_type: trade-study-or-adr
# criticality: safety-critical, as INSP-053 states: the set constrains SW-TXSEQ (ADR-015, ADR-026),
# SW-KEYER (ADR-009, ADR-024), SW-SCHED and the pico2 drivers (ADR-019, ADR-027), SW-SYNTH word path
# (ADR-013, ADR-016, ADR-023; Proposed rows of 07 section 14.1 count as their proposed criticality)
criticality: safety-critical
product_size: "27 ADRs (2728 lines) and the index README (84 lines); errata delta 5122a6b..0f4a7ad, 28 files, 114 lines added and 85 removed; 12 ADRs constrain a 07 section 14.1 component"
sprint: PDR-prep
author_agent: "author:WP-PDR-14 (Claude as technical data manager, ADR author invocation of 2026-09-27)"
reviewer_agent: "sa-reviewer:WP-PDR-14-adrs"
assurance_required: true
assurance_reviewer_agent: "sa-reviewer:WP-PDR-14-adrs (software assurance function; paired file review INSP-053 by reviewer:WP-PDR-14-adrs)"
iteration: 1
readiness_met: true
# reviewer_verdict and assurance_verdict: NEEDS CHANGES. This record raises one Minor finding of its own.
# The blocking item is INSP-053 finding-1 (in-place edits of Record-class ADRs after baseline/srr with no
# plan-deviation record), which the assurance lens confirms at Major under swe-080 7.1 task 3 and SA-E3;
# per the template finding rules it is cited, not raised again, so findings_major counts 0 here while the
# completion criteria are not met until that Major is fixed and verified
reviewer_verdict: NEEDS CHANGES
assurance_verdict: NEEDS CHANGES
# verdict: held at NEEDS CHANGES (07 section 10.2; the paired record is NEEDS CHANGES; the template applied
# is branch-only, lead SE convention of 2026-09-27)
verdict: NEEDS CHANGES
findings_major: 0
findings_minor: 1
findings_open: 1
findings_fixed: 0
findings_verified: 0
findings_deferred: 0
assurance_findings_major: 0
assurance_findings_minor: 1
assurance_tasks_applied: ["swe-134 7.1 task 5", "swe-022 7.1 task 1", "swe-033 7.1 task 1", "swe-033 7.1 task 2", "swe-033 7.1 task 3", "swe-039 7.1 task 4", "swe-057 7.1 task 2", "swe-134 7.1 task 4", "swe-134 7.1 task 6", "swe-027 7.1 task 1", "swe-136 7.1 task 1", "swe-070 7.1 task 1", "swe-205 7.1 task 3", "swe-073 7.1 task 1", "swe-020 7.1 task 1", "swe-139 7.1 task 1", "swe-211 7.1 task 1", "swe-146 7.1 task 1", "swe-080 7.1 task 1", "swe-080 7.1 task 3", "swe-081 7.1 task 2"]
swe134_items_checked: [d]
deferred_rids: []
items_no: ["swe-134 7.1 task 6", "swe-080 7.1 task 3", SA-E3]
effort_turns: 40
effort_minutes: 65
record_status: Open
date: 2026-09-27
date_closed: null
---

# Peer review record INSP-066: software assurance pair of INSP-053, ADR-001 to ADR-027 PDR errata (WP-PDR-14)

**Product.** The 27 ADRs and the index README of `docs/decisions/adr/` at the WP-PDR-14 errata commit `0f4a7ad`, the same 28 blobs as INSP-053 `product_files`. Identity checked by script at HEAD `e6d87a1`: `git rev-parse HEAD:<path>` and `git hash-object <path>` equal the listed blob for 28 of 28 files. The one later commit touching the directory (`9ac2c42`) adds `ADR-031-clock-plan.md`, which is outside the product.

**Checklist.** `docs/templates/peer-review-checklist-software-assurance.md` revision A **as on its CR-012 branch** (`cr/CR-012-pdr-checklist-templates` at `7784672`, blob `5b135285`; not merged). All sections are applied: R, A, B (row `trade-study-or-adr` plus "Every product type" plus the SWEs the product implements), C (item d only, see below), D, E and F. `product_type` is `trade-study-or-adr` (07 §2.1.1 row 3, Yes for safety-critical). `criticality` is safety-critical (07 §14.1 rows `SW-TXSEQ`, `SW-KEYER`, `SW-SCHED`, `pico2` drivers, and the Proposed `SW-SYNTH` word path).

**Scope.** This is iteration 1 of the assurance review, so it runs in full (plan rule C1). It covers the whole of each ADR that constrains a 07 §14.1 component: ADR-001, 009, 010, 011, 013, 015, 016, 019, 023, 024, 026 and 027. It also covers the errata delta `5122a6b..0f4a7ad` over all 28 files. The errata are read against the liens they claim to close (INSP-053 case table), under the assurance lens.

**Acceptance criteria (rule C7).** The criteria are:

- every task of the section B row `trade-study-or-adr`;
- the row "Every product type";
- the section 7.1 tasks of every other SWE the product implements. These are SWE-073 (the `rmm.json` row names ADR-011), SWE-033 (the row names ADR-027), SWE-020 and SWE-139 (the ADR-001 Class A election), SWE-211 (ADR-011, ADR-027) and SWE-146 (ADR-019 section 5);
- swe-080 and swe-081, for the change route of Record-class safety items;
- the three INSP-053 findings, re-read under the assurance lens.

**Independence (rule C4).** This invocation authored no ADR, no erratum, no SRR record, no part of the plan and no part of INSP-053. It edited no product file. It is neither the author (`author:WP-PDR-14`) nor the file reviewer (`reviewer:WP-PDR-14-adrs`).

**Search first.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search. Queries:

- "WP-PDR-14 ADR errata software assurance pair adrs-001-to-027-software-assurance";
- "SWEHB 7.1 Tasking for Software Assurance trade study decision alternatives SWE-033 acquisition vs development";
- "software requirement drivers live in rustos pico2 behind api traits no cwht-local register access cargo tree inspection".

After that, `grep -n`, `sed -n` and read-only Python scripts were used only to pin lines and to extract the section 7.1 lists, the 8.10 §6 designations, the `hazards.json` firmware roles and the requirement statements.

## Record

### Findings

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | assurance | Minor | swe-134 7.1 task 6, SA-D1 | ADR-027 line 23 (section 1 "Hazards in play"); the same list in TS-002 line 13 header row "Related requirements and hazards" | The line states its rule: "the hazards reached through the components of 07 section 14.1 whose firmware controls run on the runtime drivers". It then lists HZ-001, HZ-002, HZ-003, HZ-004, HZ-005, HZ-007 and HZ-014, plus HZ-008 through K7. At 0.5.0-pha, `hazards.json` `firmware_role.components` also names "Scheduler and runtime (SW-SCHED)" for HZ-006, HZ-011 and HZ-012, and "Keyer and keying output (debounce, stuck-input detection)" for HZ-010. The scheduler and runtime are the subject of this decision (07 §14.1 row `SW-SCHED`, with the `pico2` reset handler, vector table and NVIC plumbing), and keyer debounce runs on the GPIO and TIMER drivers. ADR-019, which decides the same drivers, lists HZ-001 to HZ-008, HZ-010, HZ-011, HZ-012 and HZ-014. The errata restamped this line to 0.5.0-pha "after re-checking the line against it". That re-check (INSP-053 case row "Hazard content at 0.5.0-pha") tested only hazards that name the ADR and requirements whose `source_ids` cite it, and none of these four does either, so the gap passed. The runtime is a common-cause path for every safety-critical control (SWEHB `swe-205` §7.7.2 item 16). A reader who scopes a runtime change from this line would leave out four hazards. Minor: `hazards.json` and 07 §14.1, which govern, are complete and correct, and no hazard data is missing. **Fix:** add an appended section 8 reading in ADR-027 (Record class, the form INSP-053 accepts for section 2 readings) that the hazards in play at 0.5.0-pha are HZ-001 to HZ-008, HZ-010, HZ-011, HZ-012 and HZ-014, as ADR-019 line 23 has it. TS-002 carries the same list, so see cross item X-3 | Open | Pending | |

**INSP-053 findings under the assurance lens (cited, not raised again; template finding rules).**

- **finding-1 (in-place edits after `baseline/srr`): concur at Major.** Under swe-080 7.1 task 3 and swe-081 7.1 task 2, the edits change the hazard lines of 12 ADRs that constrain safety-critical components, and the section 4.3 verification lines of 22 ADRs. The change route of 05 Table 4-1 row 13 and README rule 2 does not allow either. `docs/cm/deviations.md` holds no record of the departure. The content of each change is correct (INSP-053 case table; re-checked below for ADR-015, ADR-024 and the 27 stamps), so the defect is in the process record, not in safety content. Either fix INSP-053 names closes it for assurance.
- **finding-2 (ADR-001 section 4.3 safety-critical scope stale): concur at Minor.** Under swe-020 and swe-205 task 2, the stale list omits the boot path, the configuration guard, fault annunciation, the menu override command path, the scheduler and runtime, the word path and the frequency verification unit. It also calls all of frequency control mission-critical. The template's Major criterion "a safety-critical component is not listed as such" is not met, because the line defers to 07 §14.1 as "the authoritative list", and 07 §14.1 lists every one of those components. The severity stays Minor.
- **finding-3 (ADR-001 line 77 "no baseline exists"): concur at Minor.** Under swe-139 task 1 the next sentence gives the correct CR route, so no compliance conclusion changes.

### Task table

| Task | Safety-critical designation (SWEHB 8.10 section 6) | Applied | Result and evidence | Relief (N/A only) | Finding ids |
|---|---|---|---|---|---|
| swe-134 7.1 task 5 | SC | Yes | This review is the assurance participation in the review of a product 07 §2.1.1 row 3 routes here (Yes for safety-critical) | | none |
| swe-022 7.1 task 1 | SC | Yes | Performed against the project software assurance plan (07 §15) by this record. The NASA-STD-8739.8 part is relieved | `rmm.json` SWE-022 T (the standard is not in the corpus) | none |
| swe-033 7.1 task 1 | | Yes | ADR-027 section 3 records alternatives A0 to A3 and the five alternatives pruned before scoring (line 46; TS-002 §3.2). ADR-019 section 3 records options A to D. The errata change neither table (INSP-053 section map). The SWE-033 options a to f were confirmed in INSP-027 SA-033-1 | | none |
| swe-033 7.1 task 2 | SC | Yes | Flow-down on the acquired and reused parts: ADR-027 line 25 (SWE-027, SWE-211, SWE-146), line 41 (SWE-027 item e and SWE-211 to developed-code level for A1) and line 82 (RMM SWE-033 row). ADR-019 line 77 (SWE-027, SWE-146 and SWE-033 RMM rows). 07 §17.1 and §9.9 carry them for `api`, `pico2` and `core` | | none |
| swe-033 7.1 task 3 | | Yes | ADR-027 lines 27, 28 and 77: RSK-013 (driver effort) and RSK-023 (single maintainer), with the hygiene risk carried as a step of RSK-013. ADR-019 line 27. No new acquisition risk comes from the errata | | none |
| swe-039 7.1 task 4 | | Yes | This record is the assurance assessment of the ADR set. The trade studies behind ADR-027 and ADR-013 are assessed in their own records (INSP-027 delta, TS-007 pair) | | none |
| swe-057 7.1 task 2 | | Yes | The architectural constraints in the ADRs support the safety requirements. ADR-011 section 2 (line 33) puts application logic in the `no_std` `cwht-core`, behind `api` traits, host-testable. ADR-019 section 2 allows no cwht-local HAL or register crate. 07 §1 makes `pico2` the only crate permitted `unsafe` and gives `cwht-core` `forbid(unsafe_code)`. The driver-isolation software requirement named in ADR-027 §4.1 row 3 and ADR-019 §4.1 is not yet written (see X-4); it is due at PDR | | none |
| swe-134 7.1 task 4 | SC | Yes | Partitioning and isolation: the layering of ADR-011 and ADR-019 (above) isolates the decision logic from the register access. The independence of the frequency verification unit from `SW-SYNTH` is a 07 §14.1 provision, and no ADR contradicts it (ADR-013 and ADR-023 lines 23 cite K7). No erratum changes a section 2 | | none |
| swe-134 7.1 task 6 | SC | No | The hazard lines of 26 of 27 ADRs are consistent with `hazards.json` 0.5.0-pha (script: `firmware_role.components` of each hazard against the stated scope of each line). ADR-027 is not (finding-1). The ADR-015 reading agrees with HZ-006 K3 ("released by a deliberate two-step action") and REQ-SYS-066 (two-step set and release), which is SWE-134 item d. The ADR-024 E-10 reading quotes REQ-SYS-042 and REQ-SW-KEYER-013 exactly | | finding-1 |
| swe-027 7.1 task 1 | | Yes | ADR-017 section 5 (F-06) now states SWE-214 to SWE-217 as Center Director requirements outside the RMM, and keeps SWE-147 and SWE-148 as the NA rows. ADR-019 and ADR-027 name 07 §17.1 as the register that holds items a to f for `api`, `pico2` and `core` (INSP-027 SA-027-1, carried unchanged) | | none |
| swe-136 7.1 task 1 | | Yes | The tool-selecting ADRs (ADR-008 CAD chain, ADR-018 LTspice, ADR-021 tinySA) each send accreditation to SWE-136 and a TV record. ADR-018 section 4.2 (line 55) names `TV-014-ltspice-batch.md` as the record and claims no accreditation, which is consistent with TV-014 not being accredited (owner action OA-TV014-1). ADR-021 gates the instrument at TRR | | none |
| swe-070 7.1 task 1 | | Yes | ADR-011 takes no qualification credit from an unaccredited emulator. Emulation cases exist "only where `tools/toolchain.lock.md` accredits the peripheral" (line 67), and emulation asserts ordering only (line 54). The emulator choice is left to the PDR emulator ADR (line 79, ACC-EMU-001) | | none |
| swe-205 7.1 task 3 | SC | Yes | No erratum adds, moves or renames a component. The ADR-019 and ADR-027 §4.2 lines "New `SW-<SUB>` modules created by this ADR: none" are unchanged, and INSP-053 found no section 2 hunk. The stale ADR-001 list is INSP-053 finding-2 (concurred above) | | none |
| swe-073 7.1 task 1 | | Yes | ADR-011 (`rmm.json` SWE-073 FC names it) keeps target validation through dev-board checks and Bench cases. It limits high-fidelity simulation to accredited scope (line 25 guidance, line 83 RMM rows). The errata change only its reviewer row, hazard stamp and section 8 | | none |
| swe-020 7.1 task 1 | SC | Yes | Concurrence with the Class A election of ADR-001 section 2, which is unchanged by the errata. The classification record is 03, reviewed in its own SA pair (INSP-037 pair) | | none |
| swe-139 7.1 task 1 | SC | Yes | ADR-001 section 5 now cites the generated `rmm.md` for the dispositions instead of restating counts (F-05 part 1). The stale "no baseline exists" clause is INSP-053 finding-3 (concurred) | | none |
| swe-211 7.1 task 1 | | Yes | ADR-011 line 25 and ADR-027 line 25 cite SWE-211. 07 §9.9 tests the reused rustos code to the developed-code level. The ADRs make no contrary claim | | none |
| swe-146 7.1 task 1 | | Yes | ADR-019 line 25 ("none; registers hand-written with citations") and line 77 (the RMM SWE-146 row limited to `build.rs` constant tables). ADR-027 prunes the `svd2rust` PAC (line 46). Conditions a to g apply at the code review of any `build.rs` table | | none |
| swe-080 7.1 task 1 | SC | Yes | Impact analysis of the errata: no section 2, Status or decided value is changed (INSP-053 section map). The ADR-015 reading narrows an overclaim ("no risk of unlicensed transmission" to "cannot transmit by accident"), which lowers the risk of misuse. The ADR-024 reading keeps the tolerance and names the requirement reference point. The hazard stamps move to the current version. No safety or security impact | | none |
| swe-080 7.1 task 3 | | No | The errata did not follow the change-control process for Record-class items (05 Table 4-1 row 13, 05 §4.2, README rule 2), and no deviation is recorded. This is INSP-053 finding-1, concurred at Major | | INSP-053 finding-1 |
| swe-081 7.1 task 2 | SC | Yes | The safety-related ADRs and `hazards.json` are configuration items under git, in `baseline/srr` (an ancestor of `0f4a7ad`), and the errata commit carries `Refs: INSP-011, RID-SRR-005, RFA-SRR-006, RFA-SRR-007, WP-PDR-14`. The route defect is carried under swe-080 task 3 | | none |

## Readiness criteria

| # | Criterion | Result | Evidence |
|---|---|---|---|
| R1 | Product committed and frozen; `product_files` equal to the paired record's list | Yes | 28 of 28 blobs equal INSP-053 and HEAD `e6d87a1` (rev-parse and hash-object) |
| R2 | 07 §2.1.1 row and criticality identified | Yes | Row 3 "Trade studies and ADRs whose decision constrains a safety-critical or mission-critical component", Yes for safety-critical; 07 §14.1 rows named in the front matter |
| R3 | `validate_docs.py` exit 0 on the product's files; `traceability.py --report-only` with scratch `--output` reports no violation for the ids touched | Yes | `validate_docs.py` does not schema-check ADR files. Its exit 1 comes from other records, among them INSP-011 on the record drift of the ADR blobs, which INSP-053 cross item 2 names. `traceability.py --report-only --output <scratch>/tr.md`: exit 0, 245 requirements, 173 cases, 0 violations, 2 warnings (REQ-SYS-125, REQ-SYS-148, not touched) |
| R4 | Paired file review filed under its own invocation; this reviewer authored nothing and is not that reviewer | Yes | INSP-053 committed at `e515649`, `author_agent` `author:WP-PDR-14`, `reviewer_agent` `reviewer:WP-PDR-14-adrs`; this invocation is `sa-reviewer:WP-PDR-14-adrs` |

## A. Dispatch, independence and record integrity

| Id | Answer | Evidence |
|---|---|---|
| SA-A1 | Yes | 07 §2.1.1 row 3 applies: the ADRs of the scope paragraph constrain the §14.1 components `SW-TXSEQ`, `SW-KEYER`, `SW-SCHED`, `pico2` drivers and `SW-SYNTH` (Proposed). The plan's WP-PDR-14 names an SA pair for TS-002 only (cross item X-5) |
| SA-A2 | Yes | Three invocations: author, file reviewer and this assurance reviewer. INSP-053 names this record's path as pending (cross item X-1) |
| SA-A3 | Yes | Same product `docs/decisions/adr/`, same `product_commit` `0f4a7ad`, same 28 blobs |
| SA-A4 | Yes | INSP-053 applied `peer-review-checklist-design.md` revision B sections A, B and H (08 §3.5 for ADRs; the checklist of INSP-011) and answered every item with evidence or N/A reasons. SWE-088 criteria a to d are met (checklist, readiness, findings tracked with state, participants named) |

## B. SWE-to-task table

| Id | Answer | Evidence |
|---|---|---|
| SA-B1 | Yes | The task table holds the `trade-study-or-adr` row (swe-033 tasks 1 to 3, swe-039 task 4, swe-057 task 2, swe-134 tasks 4 and 6, swe-027 task 1, swe-136 task 1, swe-070 task 1, swe-205 task 3), the "Every product type" row (swe-134 task 5, swe-022 task 1), and the SWEs the product implements (swe-073, swe-020, swe-139, swe-211, swe-146), plus swe-080 and swe-081 for the change route. `assurance_tasks_applied` lists every Yes and No row |
| SA-B2 | Yes | No task is answered N/A. The one relief used is the NASA-STD-8739.8 part of swe-022 task 1 (`rmm.json` SWE-022 T) |
| SA-B3 | Yes | swe-134 task 6 carries finding-1. swe-080 task 3 carries INSP-053 finding-1 |

## C. SWE-134 items a to l

The product is a set of decision records. It allocates no SWE-134 provision; 07 §14.2 and the requirement and design records carry them. Only item d is touched by the errata, through the ADR-015 guest-lock reading, and it is the only item answered here (`swe134_items_checked: [d]`). The other items are N/A for this product: they are checked at the requirement and design records of the components (07 §14.2 module table).

| Id | Answer | Evidence |
|---|---|---|
| SA-C-d | Yes | The ADR-015 section 8 reading states the release as "a deliberate licensee action", "the two-step release of SRR decision 19 option a". This agrees with REQ-SYS-066 ("set and release guest lock only by a two-step action of a held button combination followed by a confirmation", Active, Test, HZ-006) and HZ-006 K3. `hazards.json` HZ-006 `swe134_items` includes d. The menu override command path of 07 §14.1 (Proposed) names guest-lock set and release |

## D. Software safety analysis and hazard traceability

| Id | Answer | Evidence |
|---|---|---|
| SA-D1 | Yes | `hazards.json` 0.5.0-pha names the software contributions of every component these ADRs constrain (listing above). The walk of the SWEHB `swe-205` §7.7.2 considerations that apply found the following. Item 10 (interlock): the guest lock inhibits every transmit path, ADR-015, HZ-006 K3. Item 21 (operator disabling a control): the release is a deliberate two-step licensee action, ADR-015 reading. Item 16 (common cause): the runtime and drivers of ADR-019 and ADR-027 are shared by every safety-critical control, and ADR-027 understates their hazard reach (finding-1; the hazard data itself is complete). Item 25 (safety-critical commands): the sequencer hang and lead-in of ADR-026 gate `PA_EN`, HZ-004 |
| SA-D2 | Yes | No component is created, moved or renamed by the product (swe-205 task 3 row). The ADR-001 scope text is INSP-053 finding-2 |
| SA-D3 | Yes | `traceability.py --report-only` (scratch output): 0 violations, so there is no `HAZARD_CONTROL_UNTRACED` and no `HAZARD_INVERSE`. The requirement ids cited in the rewritten ADR lines (REQ-SYS-042, 065, 066, REQ-SW-KEYER-013) exist with the quoted text |
| SA-D4 | N/A | No safety-tagged software requirement is created or changed by the product |
| SA-D5 | Yes | The hazard-tracing requirements that the rewritten section 4.3 lines cite close by Test: REQ-SYS-065 and REQ-SYS-066 (HZ-006) by TC-SYS-047, method Test, Bench. ADR-015 states the SW L2 HostUnit guest-lock case as allocated with the SW L2 requirements at PDR, which is within PDR maturity |
| SA-D6 | N/A | The product does not change the hazard analysis. The ADR hazard lines cite it and do not change it (ADR-019 and ADR-027 §4.3 "Hazard analysis update required: no") |

## E. Peer review, change and configuration assurance

| Id | Answer | Evidence |
|---|---|---|
| SA-E1 | Yes | The liens the errata claim to close (INSP-011 F-05 to F-08, F-10, F-12 to F-16, E-10; RID-SRR-005; L-7) are verified in content by INSP-053, which gives evidence for each. This review re-checked three independently: the ADR-015 reading against memo decision 19 and HZ-006 K3; the ADR-024 E-10 reading against REQ-SYS-042 and REQ-SW-KEYER-013; and the 27 hazard stamps (all 0.5.0-pha, the `hazards.json` version). F-05 part 3 is open as INSP-053 finding-2 |
| SA-E2 | Yes | INSP-053 and this record both carry `findings_*`, `items_no`, `effort_turns`, `effort_minutes` and `iteration` (07 §10.3) |
| SA-E3 | No | The trailer is present: `0f4a7ad` carries `Refs:`, as the Record class requires (05 §5.1). The route is not: in-place edits of Record-class items after the CR-from event are neither a CR nor an appended entry, and no deviation is recorded (INSP-053 finding-1, concurred at Major) |
| SA-E4 | N/A | No item under test and no credit run |

## F. Assurance risks, metrics and reporting

| Id | Answer | Evidence |
|---|---|---|
| SA-F1 | Yes | No assurance concern outside a product defect needs a risk entry. The dispatch gap (X-5) and the INSP id collision (X-2) are process administration for the lead SE |
| SA-F2 | Yes | The front matter carries `findings_*`, `assurance_findings_major` 0 and `assurance_findings_minor` 1 (the same finding, counted once, 07 §10.2), `items_no` and effort |
| SA-F3 | Yes | The verdict, the blocking item, the open finding, the tasks applied and the relief used are all stated in this record |

## Completion criteria and verdict

Readiness R1 to R4 were true. Every task SA-B1 requires is in the task table, and every applicable item of sections A, C, D, E and F is answered. This record raises one Minor finding. The completion criteria for `assurance_verdict: APPROVED` are nevertheless not met, because swe-080 task 3 and SA-E3 are answered No on a Major defect: INSP-053 finding-1, concurred and cited rather than raised again. So `assurance_verdict: NEEDS CHANGES`. With INSP-053 at NEEDS CHANGES, the record `verdict` is NEEDS CHANGES (07 §10.2).

Iteration 2 is a delta (plan rule C1). It verifies the INSP-053 finding-1 fix under swe-080 task 3 and SA-E3. It also verifies finding-1 here if the author fixes it in the same change. If the next verdict is APPROVED, an open finding-1 becomes a lien due at the CDR readiness declaration.

## Cross items (returned to Claude)

- **X-1.** INSP-053 (`adrs-001-to-027.md`) still reads `assurance_reviewer_agent: "pending: ..."` and `assurance_verdict: pending`, and has no `paired_record`. Its reviewer updates it to `paired_record: INSP-066`, names this reviewer and copies `assurance_verdict: NEEDS CHANGES` (07 §10.2 Record row).
- **X-2.** INSP id allocation. Three records carried `id: INSP-055` in the working tree during this review (`cr-015-process-01-02-08.md`, `process-04-verification-and-validation.md`, `ts-007-synthesizer-and-reference.md`; `ts-007` has since been committed as INSP-055 at `8fea433`). This record first took INSP-065, and an uncommitted record of another work package (`code-tools-traceability-software-assurance.md`) took the same id, so this record is INSP-066. The lead SE confirms the numbering of the other two records before the CSA counts them.
- **X-3.** TS-002 line 13 (header row "Related requirements and hazards") has the same hazard list as ADR-027 line 23. INSP-027 finding-4 added only HZ-008. The TS-002 software assurance pair INSP-062 (`trade-studies-ts-001-ts-002-software-assurance.md`, committed `e6d87a1`) does not mention HZ-006 or HZ-011; its next delta, or the TS-002 author with finding-1 here, adds HZ-006, HZ-010, HZ-011 and HZ-012.
- **X-4.** The driver-isolation software requirement is not written yet: drivers only in rustos `pico2` behind `api` traits, no cwht-local register access, Inspection by `cargo tree`. ADR-027 §4.1 row 3, ADR-019 §4.1 and TS-002 section 8 name it as due at PDR with the software architecture. No `docs/requirements/sw/**` file holds it at `e6d87a1`. It belongs to the software requirement authors of WP-PDR-34 and the software architecture of WP-PDR-32.
- **X-5.** Plan WP-PDR-14 names an SA pair only for TS-002. 07 §2.1.1 row 3 also requires one for this ADR set. The lead SE adds this record to the WP-PDR-14 records line, or to the register of SA pairs, so that PDR readiness counts it.
- **X-6.** After CR-012 merges, the delta iteration of this record switches `checklist` to `peer-review-checklist-software-assurance` revision A and drops `checklist_software_assurance`.

## Commands

| Command | Exit | Result |
|---|---|---|
| Script over the 28 `product_files`: `git rev-parse HEAD:<path>` and `git hash-object <path>` at HEAD `e6d87a1` (and at `b308f8c`) | 0 | 28 of 28 equal |
| `git log 0f4a7ad..HEAD -- docs/decisions/adr` | 0 | `9ac2c42` only (adds ADR-031, outside the product) |
| `git merge-base --is-ancestor baseline/srr 0f4a7ad` | 0 | The tag is an ancestor of the errata commit |
| `git show cr/CR-012-pdr-checklist-templates:docs/templates/peer-review-checklist-software-assurance.md` | 0 | Revision A, blob `5b135285` |
| Section 7.1 extraction from `docs/references/md/swehb/swe-NNN-*.md` for SWE-020, 022, 027, 033, 039, 057, 070, 073, 080, 081, 134, 136, 139, 146, 205, 211; the 8.10 §6 table for the SC designations | 0 | Task texts and designations used in the task table |
| Python over `hazards.json` 0.5.0-pha `firmware_role.components` against the 27 ADR line-23 lists | 0 | ADR-027 omits HZ-006, HZ-010, HZ-011, HZ-012 (finding-1); the other 26 lines are consistent with their stated scope |
| Python over `requirements.json` files for REQ-SYS-042, 065, 066, 127 and REQ-SW-KEYER-013 | 0 | Statements as quoted above |
| `.venv/bin/python tools/traceability.py --report-only --output <scratch>/tr.md` | 0 | 0 violations, 2 warnings; no repository report file written |
| `.venv/bin/python tools/validate_docs.py` | 1 | This record PASS; the failures are other records (INSP-011 drift, among others) |

## Verdict format

```
ASSURANCE VERDICT: NEEDS CHANGES
PRODUCT: docs/decisions/adr/ (27 ADRs and README, the 28 INSP-053 product_files blobs) at 0f4a7ad; PAIRED RECORD: INSP-053
PRODUCT TYPE: trade-study-or-adr; CRITICALITY: safety-critical
BLOCKING: INSP-053 finding-1 concurred at Major under swe-080 7.1 task 3 and SA-E3 (in-place edits of Record-class ADRs after baseline/srr, no deviation record); cited, not raised again
FINDINGS:
- [Minor] swe-134 7.1 task 6 (SA-D1) ADR-027 line 23 omits HZ-006, HZ-010, HZ-011 and HZ-012, which its own rule and hazards.json 0.5.0-pha include (finding-1).
CONCURRED: INSP-053 finding-2 (Minor), finding-3 (Minor)
TASKS APPLIED: swe-134 tasks 5, 4, 6; swe-022 task 1; swe-033 tasks 1 to 3; swe-039 task 4; swe-057 task 2; swe-027 task 1; swe-136 task 1; swe-070 task 1; swe-205 task 3; swe-073 task 1; swe-020 task 1; swe-139 task 1; swe-211 task 1; swe-146 task 1; swe-080 tasks 1 and 3; swe-081 task 2
TASKS N/A (relief): none (swe-022 task 1 NASA-STD-8739.8 part: rmm.json SWE-022 T)
SWE-134 ITEMS CHECKED: d
MEASUREMENTS: size=27 ADRs + README, delta 28 files; tasks=21; tasks_no=2; turns=40; minutes=65; major=0 (1 concurred); minor=1
```
