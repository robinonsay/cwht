---
# Peer-review record front matter (charter section 5; docs/process/01-lifecycle-and-reviews.md section 13
# is the single field list; docs/process/08-agent-briefing.md section 3.2; template
# docs/templates/peer-review-checklist-design.md revision B, sections A, B, G and H as 07 section 2.1.1
# row "Trade studies and ADRs" names for a decision that constrains a section 14.1 component).
# This is the separate software assurance record of trade study TS-002, the make/buy record of
# NPR 7150.2D section 6.1 item t (07 section 2.1.1 row "Software plans": Yes in every column; 07
# section 22 open item "Assurance routing of 05 and TS-002"; SRR package item H1 (c), H14).
# The paired file review of the same committed blob is INSP-013,
# docs/reviews/SRR/checklists/trade-studies-ts-001-ts-002.md (reviewer:trades).
id: INSP-027
checklist: peer-review-checklist-design
checklist_revision: B
checklist_file: docs/reviews/SRR/checklists/trade-study-ts-002-software-assurance.md
product: docs/decisions/trade-studies/TS-002-firmware-runtime-make-buy.md
# product_commit: review baseline HEAD; the product blob is git rev-parse HEAD:<path> at that commit
# (first committed at e597e49, unchanged since; the same blob INSP-013 iteration 3 delta verified)
product_commit: "adcfe0946d2f1b5cd8f41a8f91eb4219a7fb99a1"
product_blob: "574cee3dda830327b0aa17af361f863da2bc546c"
product_files: ["docs/decisions/trade-studies/TS-002-firmware-runtime-make-buy.md@574cee3dda830327b0aa17af361f863da2bc546c"]
# inputs read (not reviewed), committed blobs at adcfe09
input_files: ["docs/process/07-software-engineering-plan.md@d0f8baf614b49e9c99d8fe2169093d02626ac50d", "docs/process/00-charter.md@131608b78e178432e34f8eb9fc385dae07020c6d", "docs/process/06-risk-and-decision-analysis.md@7a92d21f24a1733d70ae083576e708274bfd1a6d", "docs/research/rustos-toolchain-proof.md@74e5363ffbc71d3ec2a09698a1ef3ecbeb95d6f5", "docs/vv/reports/TC-SW-TOOL-001-r2.md@de5c9403578703099d71fe31f28a730d7a61f2dc", "firmware/unsafe-audit.md@b232d77a76b2cddc854d03984edee09092047667"]
product_size: 1 trade study, 11 sections and appendix A, 361 lines; 4 mandatory and 7 enhancing criteria, 4 scored alternatives
sprint: SRR-prep
author_agent: "author:trades (Claude trade study author invocation, 2026-09-25, named as Recommender in the TS-002 header)"
reviewer_agent: "reviewer:INSP-027"
criticality: safety-critical
assurance_required: true
# assurance_reviewer_agent: this record IS the software assurance review; its reviewer is distinct from the
# author (author:trades) and from the file reviewer of the paired record INSP-013 (reviewer:trades)
assurance_reviewer_agent: "reviewer:INSP-027 (software assurance function; paired file review INSP-013 by reviewer:trades)"
paired_record: INSP-013
iteration: 1
# readiness_met: R1 (no figures in TS-002), R2 and R3 (no REQ-SW design allocation in a trade study) are N/A;
# R4 holds through the author's revision 1 change log and the INSP-013 closure of findings F-08 to F-10
readiness_met: true
reviewer_verdict: APPROVED
assurance_verdict: APPROVED
# verdict: APPROVED (with liens) under the convergence rule of 2026-09-26: 0 Major, 5 Minor, every Minor a lien
verdict: APPROVED
findings_major: 0
findings_minor: 5
findings_open: 0
findings_fixed: 0
findings_verified: 0
findings_deferred: 5
assurance_findings_major: 0
assurance_findings_minor: 5
assurance_tasks_applied: [swe-033 7.1 task 1, swe-033 7.1 task 2, swe-033 7.1 task 3, swe-027 7.1 task 1, swe-211 7.1]
# deferred_rids: the five liens are carried by the package as Routine items (convergence rule), not as RIDs
deferred_rids: []
items_no: [CK-DES-A7, CK-DES-B2, CK-DES-H1, SA-033-2, SA-033-3, SA-211-1]
effort_turns: 32
effort_minutes: 45
record_status: Open
date: 2026-09-26
date_closed: null
---

# Peer review record INSP-027: software assurance review of TS-002, firmware runtime and HAL make/buy

**Product.** `docs/decisions/trade-studies/TS-002-firmware-runtime-make-buy.md`, committed blob `574cee3d` at review baseline HEAD `adcfe09` (`git rev-parse HEAD:docs/decisions/trade-studies/TS-002-firmware-runtime-make-buy.md` = `574cee3dda830327b0aa17af361f863da2bc546c`; `git status` shows the file clean). It is the blob INSP-013 delta verified at its iteration 3.

**Why an assurance record.** The committed 07 (blob `d0f8baf6`), section 2.1.1 line 117, routes "the make/buy record `docs/decisions/trade-studies/TS-002-firmware-runtime-make-buy.md` (§6.1 item t, section 17.2)" to the software assurance reviewer with Yes in every column, and line 118 does the same for a trade study "whose decision constrains a safety-critical or mission-critical component of section 14.1 ... for example a runtime, driver, scheduler". 07 section 22 (line 856) lists the dispatch as open before the SRR readiness declaration; SRR package item H1 (c) and H14 carry it. INSP-013 was filed with `assurance_required: false` before that routing existed.

**Lens.** Software assurance: SWE-033 (NPR 7150.2D §3.1.2) with the three SWEHB `swe-033` section 7.1 tasks, SWE-027 (§3.1.14, items a to f), SWE-211 (§4.5.14), and the Class A evidence standard (charter section 1, section 11 rule 2). **Checklist:** `docs/templates/peer-review-checklist-design.md` revision B, sections A, B, G and H as 07 section 2.1.1 line 118 names, with the design checklist's Participants rule (SWEHB section 7.1 tasks written into the record). `docs/templates/peer-review-checklist-software-assurance.md` does not exist (08 section 3.5: due before PDR), so, as INSP-018 did, the SWEHB section 7.1 tasks are applied directly as items SA-NNN-n. **Answer legend:** Yes = Pass, No = Fail, N/A = not applicable; every answer carries evidence.

**Search-first compliance.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (queries: "SWE-033 acquisition versus development assessment make buy software"; "NPR 7150.2D SWE-027 ... SWE-211 test levels of non-custom developed software"; "rustos toolchain proof finding unsafe count api pico2 clippy warnings rustfmt hunks blinky flash RAM size"; "risk score band thresholds Green Yellow Red ... 06 section 8"). The tool was available. `grep -n`, `sed -n` and `awk` were used afterwards only to pin lines the hits pointed to; known paths were read directly.

**Independence.** This reviewer did not author TS-002, 07, the research reports or the FW-B0 reports, is a different invocation from reviewer:trades (INSP-013), and edited no product file. INSP-013 was read after this reviewer's own recomputation and citation checks.

**Convergence rule (lead SE direction 2026-09-26, applying charter section 4 item 3).** Only Major findings change products in this round. Every Minor finding is dispositioned "Lien: fix before PDR" in the lien table below and carried by the package as a Routine item.

## Findings

Ids follow the `finding-<n>` anchor rule of 01 section 13. Severity: Major blocks the baseline; Minor is fixed before the next review. No Major finding was raised: none of the five changes the ranking, the robustness verdict or the recommendation, and none misquotes a requirement.

| Finding | Origin | Severity | Item | Location | Description | State | Deferred to | Disposition |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | assurance | Minor | SA-033-2, SA-211-1 | Section 3.1 C1 definition and anchors; section 4 C1 row A0; section 6 item 4 first bullet; section 7 "Task 2" bullet | C1 ("Class A V&V burden of non-project image code", weight 20) scores A0 5, "0 external crates", and section 6 item 4 argues that buying "moves the same effort into verification". But rustos `api` and `pico2` are reused, owner-developed code outside the cwht process: 07 section 17.1 lists both in the third-party register with SWE-027 items a to f, column e "V&V to developed-code level" (HostUnit, dev-board, Bench, datasheet Inspection, unsafe audit); 07 section 9.9 (SWE-211) requires every rustos feature used to be covered by contract tests; charter section 12 row SWE-211 says "rustos `api` and `pico2` are tested to the custom-code level in full". The existing rustos code (boot, vector table, reset handler, GPIO driver; 37 unsafe sites in `firmware/unsafe-audit.md`) therefore carries the same SWE-211 obligation the study charges to A1 to A3, and is counted in neither C1 nor C3. The Task 2 evidence for A0 cites only "07 sections 3.4, 19" (the new work packages), not 07 sections 17.1 and 9.9 that flow SWE-027 and SWE-211 down to the existing code. Recomputed: A0 C1 = 4 (two crates, interpolated between the 5 and 3 anchors) gives A0 380 against A1 265, lead 115; no rank change. Fix: state A0's reused-code V&V obligation in C1 or its evidence, cite 07 sections 17.1 and 9.9 in the Task 2 bullet, and rescore C1 or say why the owner's code counts as project code. | Lien | | Lien: fix before PDR |
| <a id="finding-2"></a>finding-2 | assurance | Minor | SA-033-3, SA-EVD-1 | Section 6 item 6 second bullet; section 7 A0 row 3 (hygiene risk); section 4 C4 row A0; section 4 M3 row A0 | The Class A evidence statements are superseded by committed FW-B0 evidence. (a) Section 6 item 6 says the A0 evidence came from "tools without TV records (package H12), and the FW-B0 toolchain proof (`TC-SW-TOOL-001-r1`) is not yet filed"; TV-001 to TV-013 exist (Validated, not accredited, decision 114) and `docs/vv/reports/TC-SW-TOOL-001-r1.md` (`93d019b`) and `-r2.md` (blob `de5c9403`) are committed. (b) Run 2 (r2 lines 92, 108, 140, 141) measured 37 unsafe sites in rustos `api` and `pico2`, 36 without the CS-06 `// SAFETY:` comment, and a G5 `cargo deny` FAIL because the rustos manifests carry no `license`; both block the FW-B0 exit criterion (SRR entrance row 20) and wait on a rustos work item (decision 110). The section 7 A0 hygiene risk (L5, C1 schedule, "the `-D warnings` gate failing at FW-B0") has materialized in a different, larger form, and the consequence (a blocked SRR entrance row) is above C1. (c) C4 A0 cites "53 lines mention `unsafe`" (F6, a `grep -c`); the controlled audit list now gives 37 sites, which leaves the score 4. (d) M3 A0 "pass, with an owner action ... by PDR" is now also a gate blocker before SRR. Fix: restate section 6 item 6, the A0 hygiene risk row (with the r2 evidence and the RSK it is entered as) and the C4 and M3 evidence against TC-SW-TOOL-001-r2 and `firmware/unsafe-audit.md`. No score changes. | Lien | | Lien: fix before PDR |
| <a id="finding-3"></a>finding-3 | assurance | Minor | CK-DES-H1 | Header row "Independent reviewer"; section 7 paragraph "Evidence offered for the software assurance tasks"; section 9 dissent row, last sentence | The header says the software assurance review is "not dispatched ... because the dispatch table of 07 section 2.1.1 has no trade-study row", and section 9 says "No software assurance review has run". The committed 07 (`d0f8baf6`) section 2.1.1 lines 117 and 118 now route TS-002 to the assurance reviewer (Yes in every column), and this record is that review. Both sentences contradict the plan they cite. Fix: name INSP-027 as the software assurance record in the header and the section 7 paragraph, and update the section 9 sentence. This is separate from INSP-013 finding-11 (the Status line), which remains a lien of its own. | Lien | | Lien: fix before PDR |
| <a id="finding-4"></a>finding-4 | assurance | Minor | CK-DES-A7, CK-DES-B2 | Header row "Related requirements and hazards"; section 4 C3 row A0; section 3.1 C3 definition | The hazard list names HZ-001, 002, 003, 004, 005, 007 and 014 as reached through the 07 section 14.1 components, but omits HZ-008: 07 section 14.1 has two Proposed safety-critical rows on HZ-008 (the `SW-SYNTH` frequency-word path and the frequency verification unit) whose drivers are rustos work packages (I2C or SPI, WP-SW-05 and 06; the conditional WP-SW-14 frequency counter, safety-critical, "only if package decision 40 adopts REQ-SYS-182", 07 section 19). The C3 count for A0 ("12 work packages (WP-SW-01 to WP-SW-12; WP-SW-13 optional)") does not mention WP-SW-14 either. No score effect: A0 C3 stays 1 (>= 11 anchor), and PIO support would favor A1 on the same criterion by at most the existing anchor. Fix: add HZ-008 (Proposed) to the header and name WP-SW-14 as conditional in the C3 row. | Lien | | Lien: fix before PDR |
| <a id="finding-5"></a>finding-5 | assurance | Minor | SA-EVD-1 | Section 3.1 paragraph "Intermediate scores are interpolated between anchors"; section 4 C3 rows A1 to A3 | The C3 anchors are 3 at 6 work packages and 5 at 2 or fewer; "about 3" interpolates to 4.5, and the study records 4 without a rounding rule. Rounded up, A1 would total 285 (275 at 4.5); A0 still leads by 115 or more. TS-001 rounds both ways (INSP-013 lists P1 C3 3.5 rounded to 4 and B-C2 4.5 rounded to 4), so the convention is not stated anywhere. Fix: state the rounding rule (for example, round half against the recommended alternative) and apply it to the A1 to A3 C3 cells. | Lien | | Lien: fix before PDR |

## Lien table

| Finding | Severity | Disposition | Owner | Due |
|---|---|---|---|---|
| finding-1 | Minor | Lien: fix before PDR | Trade study author (Claude, software lead) | PDR readiness declaration |
| finding-2 | Minor | Lien: fix before PDR | Trade study author (Claude, software lead) | PDR readiness declaration |
| finding-3 | Minor | Lien: fix before PDR | Trade study author (Claude, software lead) | PDR readiness declaration |
| finding-4 | Minor | Lien: fix before PDR | Trade study author (Claude, software lead) | PDR readiness declaration |
| finding-5 | Minor | Lien: fix before PDR | Trade study author (Claude, software lead) | PDR readiness declaration |

Because TS-002 is edited only before the owner's decision (TS-002 change log, 06 section 14.6), the author applies the five liens as revision 2 before the owner signs decision 107, or, if the owner decides first, records them in the resulting ADR and the next 07 revision.

## Numbers verified against their sources

**Recomputation (independent of INSP-013).** The section 5 weights and scores were re-entered in a scratch script run with `.venv/bin/python` and the 06 section 14.4 rules applied as written (weights moved by plus and minus 10, clamped at 0, the others rescaled proportionally; each Low cell moved by plus and minus 1 within 1 to 5):

| Quantity | TS-002 states | Recomputed |
|---|---|---|
| Totals A0, A1, A2, A3 | 400, 265, 220, 220 | 400, 265, 220, 220 |
| Smallest lead under weight perturbation | 80.6 at C3 +10 | 80.625 at C3 +10 |
| Smallest lead under Low-cell perturbation | 115 | 115 (A1 C1 +1) |
| All Low cells in favor of the alternatives | A0 400, A1 355, A2 310, A3 295 | A0 400, A1 355, A2 310, A3 295 |
| finding-1 case, A0 C1 = 4 | not stated | A0 380, lead 115 |
| finding-5 case, A1 C3 = 4.5 | not stated | A1 275 |

The Low-cell lists match the Low tags of section 4 (A1 and A2: C1, C3, C4, C5, C6, C7; A3: C1, C3, C4, C5, C7; A3 C6 is Medium). Risk scores and bands of section 7 match 06 section 8 (Red at 12 or more; Yellow 5 to 11): 3x3 = 9 Yellow, 4x2 = 8 Yellow, 5x1 = 5 Yellow, 4x3 = 12 Red, 2x3 = 6 Yellow. RSK-013 (L3, C3) and RSK-023 (L4, C2) agree with the register matrix (`docs/risk/register.md` lines 32 to 46).

**Source facts checked.**

| TS-002 statement | Source | Result |
|---|---|---|
| SWE-033 at §3.1.2, options a to f in the note | `npr-7150-2d/03-chapter3.md` line 13; SWEHB `swe-033-*.md` section 1.1 | Agrees |
| SWE-027 at §3.1.14, items a to f; item e "verified and validated to the same level ..." | `03-chapter3.md` lines 77 to 89 | Agrees |
| SWE-146 at §3.8.1; SWE-211 at §4.5.14 | `03-chapter3.md` line 225; `04-chapter4.md` line 149 | Agrees |
| NPR 7150.2D §6.1 item t, make/buy record | `06-chapter6.md` line 51 ("Record of Software Engineering Trade-off Criteria & Assessments (make/buy decision)") | Agrees |
| SWEHB `swe-033` section 7.1 tasks 1 to 3 | `swe-033-*.md` lines 477 to 483 | Agrees |
| SE HB §6.8.1.2.1 to §6.8.1.2.7 | `nasa-se-handbook/22-6-8-decision-analysis.md` (6.8.1.2.5 at line 349) | Agrees |
| 06 section 14.1 class 1 items (c) and (h) | `06-risk-and-decision-analysis.md` line 310 | Agrees |
| Charter section 12: SWE-027 tailored in the IP-counsel item only; SWE-211 relief for Rust `core` only; SE-24 to SE-31 not applicable | `00-charter.md` section 12 rows 6, 9, 10 | Agrees; the SWE-211 row also says rustos is tested "to the custom-code level in full" (finding-1) |
| CS-02: zero external crates in the image | `firmware/Cargo.lock`: packages `api`, `cwht-app`, `cwht-core`, `cwht-hal-mock`, `pico2`, none with a `source` line | Agrees |
| rustos README lines 44 to 47 ("No external embedded crates ... are used") | `/Users/robinonsay/rust/rustos/README.md` lines 44 to 47, rustos HEAD `c54d35a` | Agrees |
| F2 zero `api` unit tests; F6 13 clippy warnings, 71 rustfmt hunks, `unsafe` lines `api` 11, `pico2` 42; F4 2,008 B flash and 8,200 B RAM | `docs/research/rustos-toolchain-proof.md` F2, F4, F6 | Agrees; superseded for the unsafe count by the audit list (finding-2) |
| 07 section 19: WP-SW-01 to 12, WP-SW-13 optional; 9 needed by FW-B1 | 07 lines 768 to 791 (FW-B1: WP-SW-01 to 07, 09, 11) | Agrees; WP-SW-14 conditional not mentioned (finding-4) |
| 07 section 2.1.1 has no trade-study row | 07 lines 117, 118 | Contradicted (finding-3) |

## Readiness criteria

| # | Criterion | Answer | Evidence |
|---|---|---|---|
| R1 | Every figure rendered and inspected | N/A | TS-002 contains no figure |
| R2 | `REQ-SW-*` allocated to design units | N/A | A trade study allocates no requirement; `tools/traceability.py --report-only` exit 0 at review time |
| R3 | Requirements the design implements are Active or a CR is named | N/A | REQ-SYS-128 and REQ-SYS-129 are cited as constraints, not implemented |
| R4 | Author's return lists the acceptance criteria and self-check | Yes | TS-002 change log revision 1 maps each change to INSP-013 F-08 to F-10; INSP-013 iteration 2 and 3 verified them on blob `574cee3d` |

## A. Architecture content

| Id | Answer | Evidence |
|---|---|---|
| CK-DES-A1 | N/A | Trade study, not an architecture; the components named (`api`, `pico2`, `cwht-core`) match 07 section 1.2 |
| CK-DES-A2 | N/A | No quality attributes are allocated by a make/buy study |
| CK-DES-A3 | N/A | No hardware interface is defined |
| CK-DES-A4 | N/A | No internal interface is defined; the `api` trait boundary is cited from ADR-019 |
| CK-DES-A5 | N/A | No state machine |
| CK-DES-A6 | Yes | C6 compares each alternative with CS-34 (one NVIC priority), CS-35 (SIO only, no IO_BANK0 edge interrupts) and the `ACC-EMU-001` exclusions; A0's cell matches 07 section 7.7; A2 and A3 cells cite `emulator-accreditation-and-timer-irq.md` F8 and F9 |
| CK-DES-A7 | No | The safety-critical reach of the decision omits the two Proposed HZ-008 rows of 07 section 14.1 (finding-4) |
| CK-DES-A8 | N/A | Band constants are not in scope |

## B. Traceability

| Id | Answer | Evidence |
|---|---|---|
| CK-DES-B1 | N/A | No `REQ-SW-*` is allocated |
| CK-DES-B2 | No | Header hazard list omits HZ-008 (finding-4); the others trace to 07 section 14.1 rows |
| CK-DES-B3 | N/A | No design units |
| CK-DES-B4 | N/A | No `design_refs` |
| CK-DES-B5 | N/A | Not a CR |

## C to F. Safety provisions, detailed design, interfaces, cybersecurity

ITEMS N/A: CK-DES-C1 to C15, D1 to D13, E1 to E4, F1 to F3. A make/buy trade study carries no SWE-134 design provision, unit design or interface table. The cybersecurity effect is stated in TS-002 section 3.1 (supply-chain exposure through C1; attack surfaces of 07 section 16.2 unchanged) and is consistent with RSK-062 (zero runtime crates, CS-02).

## G. Reuse and dependencies (SWE-211, SWE-027)

| Id | Answer | Evidence |
|---|---|---|
| CK-DES-G1 | Yes | Every rustos feature A0 relies on is either in the 07 section 17.1 register (`api`, `pico2` rows) or delivered by a 07 section 19 work package, and TS-002 section 3.2 row A0 cites both |
| CK-DES-G2 | Yes | A0 introduces no external runtime crate: `firmware/Cargo.lock` lists only the five local packages; A1 to A3, which would, are not recommended, and 07 section 17.1 makes any addition a CR with a trade study |

## H. Consistency and presentation

| Id | Answer | Evidence |
|---|---|---|
| CK-DES-H1 | No | Header and section 9 contradict the committed 07 section 2.1.1 (finding-3); C1 treatment of rustos differs from 07 section 17.1 and charter section 12 row SWE-211 (finding-1) |
| CK-DES-H2 | N/A | No figures |
| CK-DES-H3 | Yes | `wc -l` 361 lines, below 500 |
| CK-DES-H4 | Yes | Every SE HB, SWE-NNN and 06 section citation checked in the table above; no 47 CFR citation in TS-002 |

## Software assurance tasks applied (SWEHB section 7.1 tabs)

| Id | Task | Answer | Evidence |
|---|---|---|---|
| SA-033-1 | `swe-033` 7.1 task 1: confirm that the options for acquisition versus development have been evaluated | Yes | TS-002 section 2 table maps SWE-033 options a to f to A0 to A3 or to "not applicable" with reasons (a: no qualified RP2350 runtime, Ferrocene is a toolchain; c: no contracts, charter section 12 SE-24 to SE-31 row); the component-level table dispositions every firmware component the RMM SWE-033 row names; 5 alternatives pruned with reasons (section 3.2). Confirmed |
| SA-033-2 | `swe-033` 7.1 task 2: confirm the flow-down of software engineering, assurance and safety requirements on all acquisition activities | No | For A1 to A3 the study names SWE-027 a to f and SWE-211; for A0 it cites only 07 sections 3.4 and 19 (new work packages) and scores A0 as carrying no reused-code V&V, while 07 section 17.1, 07 section 9.9 and charter section 12 flow SWE-027 and SWE-211 to the existing rustos code (finding-1). The flow-down exists in the plan; the study does not show it |
| SA-033-3 | `swe-033` 7.1 task 3: assess any risks with the acquisition versus development decision | No | Section 7 assesses nine risks with correct bands, and A0's schedule and single-maintainer risks are carried by RSK-013 and RSK-023 with TS-002 in `trade_study_ids`. The A0 hygiene risk is out of date against TC-SW-TOOL-001-r2 (finding-2) |
| SA-027-1 | `swe-027` 7.1 task 1: confirm conditions a to f are complete for any reused or OSS software acquired or used | Yes | The recommended A0 uses only owner-developed rustos and Rust `core`; 07 section 17.1 records a to f for `api`, `pico2` and `core`, item c tailored (charter section 12) with the missing rustos license carried as `OQ-SW-001` (due PDR) and decision 110. For A1 to A3, M3 licenses were read for the top-level crates only; transitive crates are recorded as unassessed (section 6 item 3), acceptable because none is selected |
| SA-211-1 | `swe-211` 7.1: confirm embedded reused components are tested to the level of custom code | No | The plan requires it (charter section 12 row SWE-211; 07 section 9.9); the study's C1 does not count the existing rustos code against it (finding-1). No ranking effect |
| SA-EVD-1 | Class A evidence standard: every score carries evidence and confidence, tool status stated, limitations stated (06 section 14.4 item 5; charter section 11 rule 2) | Yes, with liens | Every section 4 cell carries evidence and a confidence tag; Low cells rest on general knowledge and are declared so (section 2, section 6 item 6); robustness holds under every 06 section 14.4 perturbation (recomputed above). Two evidence statements are stale or unstated (finding-2, finding-5) |

## Concurrence with INSP-013

Read after the checks above. This review agrees with INSP-013 on the totals, the sensitivity figures, the robustness verdict and the citations it verified, and on its finding-11 lien (Status line). INSP-013 recorded `criticality: neither` and `assurance_required: false`; under the committed 07 section 2.1.1 the make/buy record is assurance-routed, which this record now supplies. No INSP-013 finding is re-opened.

## Cross items (outside this record's scope, returned to Claude)

1. 07 section 22 line 856 open item "Assurance routing of 05 and TS-002": the TS-002 part is answered by this record; `tools/validate_docs.py` `ASSURANCE_WHOLE_PRODUCTS` should include the TS-002 path so the rule is enforced (tool owner).
2. SRR package item H1 (c) and H14: "the TS-002 software assurance record" is filed as INSP-027, APPROVED with 5 liens.
3. TS-001: the rounding convention of interpolated scores differs within the study (INSP-013 line 98); the finding-5 rule should be stated once in 06 section 14 or `docs/templates/trade-study.md` rather than per study (process owner).
4. The G5 unsafe-audit FAIL (36 rustos sites without SAFETY comments) is a rustos work item under decision 110; it bears on A0's C4 and C7 evidence but is not a TS-002 defect.

```
VERDICT: APPROVED (with liens)
PRODUCT: docs/decisions/trade-studies/TS-002-firmware-runtime-make-buy.md@574cee3dda830327b0aa17af361f863da2bc546c
FINDINGS:
- [Minor] SA-033-2, SA-211-1 TS-002 section 3.1 and section 4 C1 A0: existing rustos code carries SWE-211 V&V not counted (finding-1). Lien: fix before PDR
- [Minor] SA-033-3 TS-002 section 6 item 6, section 7 A0 hygiene row: superseded by TC-SW-TOOL-001-r2 (finding-2). Lien: fix before PDR
- [Minor] CK-DES-H1 TS-002 header and section 9: assurance routing statement contradicts 07 section 2.1.1 (finding-3). Lien: fix before PDR
- [Minor] CK-DES-A7, B2 TS-002 header and C3 A0: HZ-008 and WP-SW-14 omitted (finding-4). Lien: fix before PDR
- [Minor] SA-EVD-1 TS-002 section 3.1 and C3 A1 to A3: rounding rule of interpolated scores unstated (finding-5). Lien: fix before PDR
ITEMS N/A: CK-DES-A1 to A5, A8, B1, B3 to B5, C1 to C15, D1 to D13, E1 to E4, F1 to F3, H2, I1 to I8, J1 to J10
MEASUREMENTS: size=361 lines; turns=32; minutes=45; major=0; minor=5; lien=5; open_major=0; iteration=1
```
