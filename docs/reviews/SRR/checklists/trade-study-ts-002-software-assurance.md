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
# Post-SRR-ruling delta (2026-09-26, package item R16): review baseline HEAD ff0a610 after delta verification of
# 2362183 (TS-002 Status row, SRR decision 107) and of the charter edit 6ea6b1d (SRR decisions 7, 10 (a), 10 (b));
# iteration 1 baseline adcfe09 with TS-002 blob 574cee3d. See "Post-SRR-ruling delta".
# Delta iteration 2 (2026-09-29, lien L-6 verification; section "Delta iteration 2"): product_commit is the WP-PDR-14
# errata commit 443b2a3, the only commit that touches TS-002 after 2362183; post-SRR-ruling value
# "ff0a6105eef743564af60acaae47d9ffdc7e4ded"
product_commit: "443b2a384e515de5257517ebce58c37bec23a4a3"
# delta iteration 2: product_blob 6c385dfc (post-SRR-ruling delta) replaced by 6b18cee8
product_blob: "6b18cee831a67dc9550e6082c595023d77bcd704"
# post-SRR-ruling delta: TS-002 blob 574cee3d (iteration 1) replaced by 6c385dfc (2362183); equal to git rev-parse
# HEAD:<path> and git hash-object at ff0a610
# delta iteration 2: 6c385dfc replaced by 6b18cee8 (443b2a3); equal to git rev-parse HEAD:<path> and git hash-object
# at main c9f611d
product_files: ["docs/decisions/trade-studies/TS-002-firmware-runtime-make-buy.md@6b18cee831a67dc9550e6082c595023d77bcd704"]
# inputs read (not reviewed), committed blobs at adcfe09
input_files: ["docs/process/07-software-engineering-plan.md@d0f8baf614b49e9c99d8fe2169093d02626ac50d", "docs/process/00-charter.md@131608b78e178432e34f8eb9fc385dae07020c6d", "docs/process/06-risk-and-decision-analysis.md@7a92d21f24a1733d70ae083576e708274bfd1a6d", "docs/research/rustos-toolchain-proof.md@74e5363ffbc71d3ec2a09698a1ef3ecbeb95d6f5", "docs/vv/reports/TC-SW-TOOL-001-r2.md@de5c9403578703099d71fe31f28a730d7a61f2dc", "firmware/unsafe-audit.md@b232d77a76b2cddc854d03984edee09092047667", "docs/process/00-charter.md@41575d218c2228825704ce0b080a967c890fe43f (post-SRR-ruling delta, 6ea6b1d)", "docs/process/07-software-engineering-plan.md@37d472b501578504b7fa23422c4f74193647e458 (post-SRR-ruling delta)", "docs/decisions/adr/ADR-027-firmware-runtime-rustos-a0.md@3352ae6084f9d59899343b781f7fc4e4723932f5 (post-SRR-ruling delta)", "docs/reviews/SRR/decisions-for-owner.md@a8931d91253462b687aefd2de715e1adaf0fee45 (post-SRR-ruling delta)", "docs/process/03-software-classification-and-rmm.md@ed270f443e2ab648480017df8ad3d0221400cf4c (post-SRR-ruling delta, section 6.5 item g)", "docs/process/06-risk-and-decision-analysis.md (post-SRR-ruling delta, sections 14.5, 14.6, HEAD)", "docs/process/07-software-engineering-plan.md@bfe05f4327e79fa15c24d2cf8c14249804f946a8 (delta iteration 2)", "docs/decisions/adr/ADR-027-firmware-runtime-rustos-a0.md@a319c789f620f6fda26eeb392796fe2f4ba6c63e (delta iteration 2, at 443b2a3)", "docs/reviews/SRR/minutes.md@5a5f4ed611f3aeb86d47a610a65ee6d4e9384518 (delta iteration 2)", "docs/reviews/SRR/decision-memo.md@110102bf003f1c4c28cc9365c9af7dee39e79abd (delta iteration 2)", "docs/reviews/SRR/decisions-for-owner.md@e1c499851c862b99b664c674e2970dde61005040 (delta iteration 2)", "docs/vv/reports/TC-SW-TOOL-001-r6.md@8d12b38333b4ae863dc8689eed39658dcc276e68 (delta iteration 2)", "docs/risk/register.json@6685aa0eadc9e8bd806f1920e20d2209e8ae130e (delta iteration 2)", "docs/reviews/PDR/checklists/trade-studies-ts-001-ts-002.md@7798e6ce8d1ec3c4e95513726f73d993e74668d8 (delta iteration 2, INSP-054, read after this reviewer's own checks)"]
# product_size: iteration 1 value "1 trade study, 11 sections and appendix A, 361 lines; ..."; delta iteration 2 at 6b18cee8
product_size: 1 trade study, 11 sections, appendix A and an appended errata section of 6 entries, 376 lines; 4 mandatory and 7 enhancing criteria, 4 scored alternatives
sprint: SRR-prep
author_agent: "author:trades (Claude trade study author invocation, 2026-09-25, named as Recommender in the TS-002 header)"
reviewer_agent: "reviewer:INSP-027"
criticality: safety-critical
assurance_required: true
# assurance_reviewer_agent: this record IS the software assurance review; its reviewer is distinct from the
# author (author:trades) and from the file reviewer of the paired record INSP-013 (reviewer:trades)
assurance_reviewer_agent: "reviewer:INSP-027 (software assurance function; paired file review INSP-013 by reviewer:trades)"
paired_record: INSP-013
# iteration 2: the lien L-6 delta on the WP-PDR-14 errata (443b2a3), section "Delta iteration 2" at the end; the
# file-review delta of the same blob is INSP-054 (docs/reviews/PDR/checklists/trade-studies-ts-001-ts-002.md)
iteration: 2
# readiness_met: R1 (no figures in TS-002), R2 and R3 (no REQ-SW design allocation in a trade study) are N/A;
# R4 holds through the author's revision 1 change log and the INSP-013 closure of findings F-08 to F-10
readiness_met: true
reviewer_verdict: APPROVED
assurance_verdict: APPROVED
# verdict: APPROVED (with liens) under the convergence rule of 2026-09-26: 0 Major, 5 Minor, every Minor a lien
# post-SRR-ruling delta: APPROVED (with liens finding-1 to finding-6); 2362183 and 6ea6b1d apply their rulings
# correctly; new Minor finding-6 (TS-002 still reads "pending" in section 1 and the header after Status Decided) is a lien
# delta iteration 2: APPROVED; finding-1 to finding-6 Verified on 6b18cee8; no new finding
verdict: APPROVED
findings_major: 0
findings_minor: 6
findings_open: 0
findings_fixed: 0
# findings_verified and findings_deferred: iteration 1 and the post-SRR-ruling delta had 0 and 6 (six liens);
# delta iteration 2 verifies all six, so no lien remains
findings_verified: 6
findings_deferred: 0
assurance_findings_major: 0
assurance_findings_minor: 6
assurance_tasks_applied: [swe-033 7.1 task 1, swe-033 7.1 task 2, swe-033 7.1 task 3, swe-027 7.1 task 1, swe-211 7.1]
# deferred_rids: the five liens are carried by the package as Routine items (convergence rule), not as RIDs
deferred_rids: []
# items_no: iteration 1 and post-SRR-ruling value [CK-DES-A7, CK-DES-B2, CK-DES-H1, SA-033-2, SA-033-3, SA-211-1];
# delta iteration 2 answers each of them Yes on 6b18cee8
items_no: []
# effort: iteration 1 (32 turns, 45 min), post-SRR-ruling delta (package item R16) (12, 25), delta iteration 2 (20, 35)
effort_turns: 64
effort_minutes: 105
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
| <a id="finding-6"></a>finding-6 (post-SRR-ruling delta) | assurance | Minor | CK-DES-H1, SA-033-1 | TS-002 section 1 line 22 ("**Owner's decision (section 10):** pending. The owner rules it in the SRR decision memo (section 8)."); header rows "Resulting ADR" (line 14: "ADR-NNN, the next free number at decision time (ADR-027 or later ...)") and "Dates" (line 15: "decided: at SRR") | Found at the post-SRR-ruling delta (2026-09-26). Commit `2362183` set the Status row to "Decided 2026-09-26 ... resulting ADR: ADR-027" (SRR decision 107), but three other statements of the same make/buy record still say the decision is pending and the ADR unnumbered, and section 10 is empty (INSP-013 finding-13, concurred). The SWE-033 record therefore states both "Decided" and "pending". Minor, not Major: the Status row, ADR-027, the SRR memo and the minutes record the same decision without ambiguity, so no reader can take a different decision from the baseline, and no score, criterion or trigger is affected. Fix, in the same change as the section 10 transcription and on the same reading (06 section 14.5 recording of the decision, not a post-decision revision under 06 section 14.6 and 05 Table 4-1 row 12): section 1 "Owner's decision: A0 on 2026-09-26 (SRR decision 107)"; "Resulting ADR: ADR-027"; "Dates: decided 2026-09-26". | Lien | | Lien: fix before PDR |

## Lien table

| Finding | Severity | Disposition | Owner | Due |
|---|---|---|---|---|
| finding-1 | Minor | Lien: fix before PDR | Trade study author (Claude, software lead) | PDR readiness declaration |
| finding-2 | Minor | Lien: fix before PDR | Trade study author (Claude, software lead) | PDR readiness declaration |
| finding-3 | Minor | Lien: fix before PDR | Trade study author (Claude, software lead) | PDR readiness declaration |
| finding-4 | Minor | Lien: fix before PDR | Trade study author (Claude, software lead) | PDR readiness declaration |
| finding-5 | Minor | Lien: fix before PDR | Trade study author (Claude, software lead) | PDR readiness declaration |
| finding-6 (post-SRR-ruling delta) | Minor | Lien: fix before PDR | Trade study author (Claude, software lead), with the section 10 decision record (INSP-013 finding-13) | PDR readiness declaration |

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

## Post-SRR-ruling delta (2026-09-26, SRR package item R16; software assurance reviewer, new invocation)

**Scope and independence.** Written by a new invocation in the software assurance reviewer role (`reviewer:INSP-027`) after the owner approved the SRR on 2026-09-26 (disposition Approved with liens; `docs/reviews/SRR/minutes.md`: "I concur with your recommendations for the key decisions." and "I approve of this and the SRR."; every decision ruled as recommended, the ruling text being the "Recommendation" cell of `docs/reviews/SRR/decisions-for-owner.md` Part 1). It did not author TS-002, ADR-027, the charter edit, INSP-013 or any ruling, and it edited no product file. Everything above this section is the iteration 1 record, kept as history; the only additions above are the finding-6 rows of the findings and lien tables and the front matter values, whose comments name the superseded ones. The convergence rule (charter section 4 item 3) applies: only open Major findings and the ruled post-ruling work change products; a new Minor finding is a lien due PDR.

**Search first.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (queries: post-SRR-ruling delta section in a peer review record; trade study decision section filled by the owner and immutable after the decision, 06 sections 14.5 and 14.6). `grep -n`, `sed -n`, `git log`, `git show` and read-only Python were used afterwards only to pin lines.

**Commits examined.** `git log adcfe09..HEAD -- docs/decisions/trade-studies/TS-002-firmware-runtime-make-buy.md docs/process/00-charter.md` lists two commits:
- `2362183` "ADRs: apply SRR owner rulings (R16)": one hunk in TS-002 (the Status row; blob `574cee3d` to `6c385dfc`); the other 19 files of the commit are ADRs and the ADR README, read only where they bear on TS-002 (ADR-027).
- `6ea6b1d` "Charter: apply SRR decisions 7 and 10 (owner ruling 2026-09-26)": four hunks in `docs/process/00-charter.md` (blob `131608b7` to `41575d21`), an input of this record.

The TS-002 blob `6c385dfc` equals `git rev-parse HEAD:<path>` and `git hash-object <path>` at the review baseline (1 of 1).

**Delta verification, hunk by hunk.**

| Hunk | Ruling applied | Assurance check | Result |
|---|---|---|---|
| TS-002 Status row (`2362183`, line 6) | SRR decision 107 (key decision K9): "Approve A0 with the four revisit triggers of TS-002 section 8." | Status reads "Decided 2026-09-26: option A0 approved with the four revisit triggers of section 8 (SRR decision 107 ...); resulting ADR: ADR-027", and names INSP-013 and INSP-027 as the reviews on blob `574cee3d`, which is true. The four triggers in section 8 (lines 308 to 312) are those ADR-027 section 6 (line 100) adopts. The Status row is the one edit 06 section 14.6 allows after the decision. No score, criterion, alternative or risk changed | Correct; the rest of the decision record was not updated (finding-6; INSP-013 finding-13) |
| Charter section 2, Owner bullet (`6ea6b1d`, line 24) | SRR decision 7 ("Approve both."): add the Health and Medical TA and CIO/SAISO designee capacities to the owner's roles in charter section 2 | Adds "Health and Medical Technical Authority, and CIO/SAISO designee for the software cybersecurity requirements (SRR decision 7)"; matches 03 status line owner roles. No role or independence rule removed; the software assurance function bullet is unchanged | Correct |
| Charter section 5, compliance matrix, test reports, design and sprint rows plus two new rows (`6ea6b1d`) | SRR decision 10 (b): "charter section 5 rows for status notes and the artifacts 07 section 22 lists" | Every artifact of 07 section 22 row "Artifacts beyond charter section 5" (line 868: `docs/sprints/index.md`, `docs/design/sw/<module>.md`, `firmware/devcheck/`, `firmware/emu/`, `firmware/THIRD-PARTY-NOTICES.md`, `docs/vv/reports/TC-SW-COV-001-r<N>/`, `docs/process/se-compliance-matrix.schema.json`) is now in section 5, and the SEMP F-09 status-notes path `docs/plan/status/status-YYYY-MM-DD.md` is added. Nothing removed | Correct |
| Charter section 10 (`6ea6b1d`, line 139) | SRR decision 10 (a): section 10 wording per 03 section 6.5 item g, in the decision 9 reading ("frequency control safety-critical ... and the override command path safety-critical") | The list reads the 03 item g decision 9 wording and adds the menu override command path (X20) to the safety-critical list and the key-input and keyer-mode selection path to the mission-critical list (INSP-009 finding-1); 07 section 14.1 stays the single authoritative list; the MC/DC, complexity and nightly-coverage text is unchanged | Correct |

**Bearing of the rulings on TS-002 (assurance lens).** The charter now names "the scheduler and runtime" safety-critical, which is the TS-002 decision class item (c) premise (line 7: runtime drivers in the safety-critical call path); consistent. Decision 9 makes the `SW-SYNTH` frequency-word path and the frequency verification unit safety-critical for HZ-008, so the omission of HZ-008 from the TS-002 hazard list (finding-4) now concerns a safety-critical rather than a Proposed component. Severity stays Minor: A0 C3 stays 1 at the >= 11 anchor and no score moves; the finding-4 fix should read "HZ-008 (safety-critical, SRR decision 9)". Decision 107 took the decision while finding-1 to finding-5 were open liens: the owner ruled with them on the record (decision 107 sources cite INSP-027 "APPROVED with liens"), so they do not reopen the decision.

**Fix path of the liens after the decision.** The iteration 1 lien paragraph gave two routes: revision 2 of TS-002 before the decision, or, if the owner decided first, the resulting ADR and the next 07 revision. The owner decided first, and 06 section 14.6 now allows only Status edits to TS-002. ADR-027 (blob `3352ae60`) names INSP-027 in its header but does not record finding-1 to finding-5; that is cross item X-1. finding-6 and INSP-013 finding-13 are different: they complete the recording of the decision (06 section 14.5 bullet 4), not a revision of the analysis. INSP-013 finding-13 states the same reading for the fix.

**New finding.** finding-6 (Minor, CK-DES-H1 and SA-033-1; rows added to the findings and lien tables above): TS-002 section 1 "Owner's decision: pending" (line 22) and the header rows "Resulting ADR: ADR-NNN" (line 14) and "Dates ... decided: at SRR" (line 15) contradict the Status row "Decided 2026-09-26". Lien: fix before PDR. No new Major defect: the make/buy decision, its alternative, its triggers and its ADR are stated identically in the Status row, ADR-027, the SRR memo and the minutes.

**Open Major findings resolved by the rulings.** None: this record had no Major finding.

**Earlier liens.** finding-1 to finding-5 are unchanged by `2362183` (TS-002 sections 3.1, 4, 6, 7 and the header row "Independent reviewer", lines 10, 13, 22 to 329, re-read at `6c385dfc`; the new Status row names INSP-027 but the header "Independent reviewer" row and section 9 still say the assurance review was not dispatched, so finding-3 stands). All stay "Lien: fix before PDR".

**Assurance task answers at the delta.** SA-033-1 Yes (options evaluated; the decision is taken on them); SA-033-2 No (finding-1); SA-033-3 No (finding-2); SA-027-1 Yes (decision 110 now rules the rustos licence as MIT, which answers the item c gap the iteration 1 evidence noted; the 07 section 17.1 update belongs to the 07 author); SA-211-1 No (finding-1); SA-EVD-1 Yes with liens. CK-DES-H1 stays No (finding-3, finding-6). Readiness R1 to R5 as iteration 1 (`readiness_met: true`).

**Pairing (07 section 10.2).** INSP-013 (`trade-studies-ts-001-ts-002.md`, `paired_record: INSP-027`), post-SRR-ruling delta committed at `ab38255`, names TS-002 blob `6c385dfc`, equal to this record, and reads `reviewer_verdict: APPROVED`, `verdict: APPROVED` (with liens finding-11 to finding-13). This record concurs with INSP-013 finding-13 (section 10 empty) at Minor.

**Completion criteria (SWE-088; 07 section 10.2) at the delta: met.** Assurance verdict APPROVED; the paired file review APPROVED on the same blob; readiness met; zero open Major findings; every Minor finding a lien; named blob equals HEAD. `verdict: APPROVED` (with liens finding-1 to finding-6).

**Cross items (outside this record's scope).**
- **X-1.** ADR-027 author (lead SE): record the carried INSP-027 liens finding-1 to finding-5 in ADR-027 or the next 07 revision (iteration 1 lien paragraph route (b)); the ADR-027 independent review due before PDR (its header) checks it.
- **X-2.** TS-002 author: fill section 10 (INSP-013 finding-13) and apply finding-6 in one change, stated in the change log as the 06 section 14.5 recording of decision 107; the lead SE may do it as R16 work before the `baseline/srr` tag, with INSP-013 and this record re-verified.
- **X-3.** 07 author: 07 section 17.1 SWE-027 item c row for rustos to cite decision 110 (MIT licence) in place of `OQ-SW-001`, if not already done.

**Tool runs (2026-09-26, `.venv/bin/python`).**

| Command | Exit | Result |
|---|---|---|
| `tools/validate_docs.py` (before this update, HEAD `183aa88`) | 1 | 49 passed, 1 failed: this record on drift (TS-002 `574cee3d` against HEAD `6c385dfc`), as expected before the delta |
| `tools/validate_docs.py` (after this update, HEAD `ff0a610`) | 1 | 48 passed, 2 failed (INSP-002 on its open Major finding-23 and finding-24 and INSP-015 on `toolchain.lock.md` drift, both from concurrent product commits of other agents); this record PASS |
| `tools/traceability.py --report-only` (HEAD `dd3372c`) | 0 | 245 requirements, 173 test cases, 4 violations (`HAZARD_REQ_NOT_TESTED`, REQ-SYS-122, 124, 137, 138; no TS-002 id), 2 warnings; `docs/vv/` outputs restored with `git checkout` |
| `tools/render_risk.py --check --gate SRR --hazards docs/safety/hazards.json` | 0 | 65 risks, register current |
| `tools/render_rmm.py --check` | 0 | 100 rows, rendered file current |
| `tools/render_compliance.py --check` | 0 | validation passed, rendered file current |
| `-m unittest discover -s tools/tests` | 1 | 400 run, 1 failure (`test_repository_exit_zero`, the repository validator failures of other records at the time of the run) |

```
POST-SRR-RULING DELTA (2026-09-26, package item R16): VERDICT: APPROVED (with liens finding-1 to finding-6)
DELTA: 2362183 (TS-002 Status row, SRR decision 107) and 6ea6b1d (charter sections 2, 5, 10; SRR decisions 7, 10 (a), 10 (b)) apply their rulings correctly
CLOSED BY RULINGS: none (no Major finding in this record)
NEW: finding-6 (Minor, TS-002 section 1 and header still read pending after Status Decided), Lien: fix before PDR; concurs with INSP-013 finding-13; open Major 0
PRODUCT: docs/decisions/trade-studies/TS-002-firmware-runtime-make-buy.md@6c385dfc77c61619d31756418c479c5beca7b527 (equal to HEAD, 1/1)
PAIRING: INSP-013 reviewer_verdict APPROVED, verdict APPROVED on the same blob
MEASUREMENTS (delta): turns=12; minutes=25; cumulative turns=44, minutes=70; major=0; minor=6; lien=6
```

## Delta iteration 2 (2026-09-29, lien L-6 verification on the WP-PDR-14 errata; software assurance reviewer, new invocation)

**Scope.** The re-issue delta of this record on TS-002 blob `6b18cee8`, committed at `443b2a3` ("docs(decisions): WP-PDR-14 TS-001 and TS-002 errata for the INSP-013 and INSP-027 liens"). It verifies each lien of this record (finding-1 to finding-6, carried by the SRR decision memo as lien L-6, RFA-SRR-006, due at the PDR readiness declaration) and every changed hunk since the pinned blob `6c385dfc`, and names the new blob in `product_files`. `git log 6c385dfc..HEAD` on the TS-002 path lists one commit, `443b2a3`; `git diff --stat 6c385dfc 6b18cee8` gives 25 insertions and 10 deletions. `git rev-parse HEAD:<path>` and `git hash-object <path>` both give `6b18cee8` at `main` `c9f611d`. This is a delta (not a re-pin): the reviewed content changed. It is the "INSP-027 delta" that INSP-054 (the PDR file-review delta of the same errata, `docs/reviews/PDR/checklists/trade-studies-ts-001-ts-002.md`) names as its software assurance pair.

**Independence (PDR work plan rule C4).** A new invocation of the software assurance reviewer role (07 section 2.1.1). It authored no part of TS-002, its errata, ADR-027, INSP-013, INSP-054 or the earlier sections of this record, and edited no product file. INSP-054 was read only after the checks below.

**Search first (rule C3).** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (queries: the INSP-027 delta and TS-002 errata; the INSP-060 re-pin precedent). `grep -n`, `sed -n`, `git show`, `git diff` and read-only Python were used afterwards only to pin lines at `443b2a3`.

**Hunks examined (`git diff 2362183 443b2a3 -- <TS-002>`).** Header rows "Independent reviewer" (line 10), "Resulting ADR" (line 14) and "Dates" (line 15); the section 1 line "Owner's decision"; the section 10 body (decision, decided by, rationale, records, revisit conditions, lessons 1 to 4); the appended section "Errata after the decision (append only)" with entries 1 to 6. Sections 2 to 9, Appendix A, the section 5 matrix and the change log are byte-identical to `6c385dfc` (no hunk there). The fix route agrees with the post-SRR-ruling delta above: after decision 107 the study is a Record (05 Table 4-1 row 12; 06 section 14.6), so the decision record is filled under 06 section 14.5 and each analysis correction is an appended erratum that names its place, not an edit of sections 2 to 9. Cross item X-1 of the post-SRR-ruling delta (liens into ADR-027) is superseded by that route, and X-2 is done by this commit.

### Findings of the delta

| Finding | Severity | State | Evidence at `6b18cee8` (sources read at `443b2a3`) |
|---|---|---|---|
| finding-1 | Minor | Verified | Erratum 1 names the four places (section 3.1 C1, section 4 C1 row A0, section 6 item 4, section 7 Task 2 bullet), states the SWE-027 item e and SWE-211 obligation of the reused rustos `api` and `pico2` code from 07 section 17.1 (register rows `api` and `pico2`, line 729: V&V to developed-code level) and 07 section 9.9 (line 422), and charter section 12 row SWE-211 ("custom-code level"), and reads the Task 2 evidence as citing 07 sections 17.1 and 9.9. Sensitivity recomputed: A0 C1 = 4 at weight 20 gives 400 - 20 = 380 against A1 265, lead 115. Not rescoring is correct for a decided study (06 section 14.6); the obligation is now stated. SA-033-2 and SA-211-1: Yes |
| finding-2 | Minor | Verified | Erratum 2 (a) to (d). TV-001 to TV-013 exist in `docs/cm/tool-validation/`; TC-SW-TOOL-001 runs 1 to 6 are filed. Run 6 (`TC-SW-TOOL-001-r6.md`, 2026-09-27, `credit: false`) ends `sw_gate: PASS (G0 to G6)` at rustos `2ec64c0` (CR-004 pin, `docs/cm/cr/CR-004-rustos-pin-2ec64c0.md`), with `PASS G5 cargo deny (bans, licenses, sources)` and `PASS G5 unsafe audit`: 37 sites, 0 without SAFETY, 37 unsigned (r6 line 161). The r2 facts (37 sites, 36 without comment, G5 license FAIL, SRR entrance row 20) are those of iteration 1. The C4 count is corrected to 37 sites with the score 4 unchanged; the M3 pass is unchanged. RSK-013 lists TS-002 in `related.trade_study_ids` (`docs/risk/register.json`), the risk the section 7 row pointed to ("or a step of RSK-013"). SA-033-3: Yes. See O-1 |
| finding-3 | Minor | Verified | Header row "Independent reviewer" names INSP-027 as the software assurance record paired with INSP-013 and routed by 07 section 2.1.1 row "Software plans" (07 line 117, Yes in every column), with the verdicts of both records as recorded; erratum 3 corrects the section 7 paragraph and the section 9 dissent sentence ("No software assurance review has run") by an appended entry that quotes both. CK-DES-H1 (this part): Yes |
| finding-4 | Minor | Verified | Erratum 4 adds HZ-008 through the two 07 section 14.1 rows (`SW-SYNTH` frequency-word path, line 598; frequency verification unit, line 599) and counts A0 C3 as 13 required work packages (WP-SW-01 to 12 plus WP-SW-14; WP-SW-13 optional). WP-SW-14 is conditional on decision 40 (07 line 787); decision 40 is in key decision K2 (`decisions-for-owner.md` line 400) with the recommendation "Adopt with the 10 kHz window and 100 ms", ruled as recommended. A0 C3 stays 1 (anchor 1: 11 or more). CK-DES-A7 and CK-DES-B2: Yes. See O-2 |
| finding-5 | Minor | Verified | Erratum 5 states the rounding the study used (half down, toward the recommended alternative) and both other cases. Recomputed with C3 weight 20: interpolation of "about 3" between 6 (score 3) and 2 (score 5) is 4.5; A1 265 + 10 = 275 and + 20 = 285; A2 and A3 220 + 10 = 230 and + 20 = 240; A0 400 leads by at least 115. Lesson 3 of section 10 sets the rule for later studies. SA-EVD-1: Yes. See O-3 |
| finding-6 | Minor | Verified | Section 1 "Owner's decision: A0, decided 2026-09-26 at SRR (SRR decision 107, key decision K9) ... recorded by ADR-027 and `docs/reviews/SRR/decision-memo.md`"; "Resulting ADR: ADR-027"; "Dates: ... decided 2026-09-26 at SRR". Section 10 matches its sources: decision 107 in K9 (`decisions-for-owner.md` line 113, cell "Approve A0 with the four revisit triggers of TS-002 section 8."); the two owner statements are verbatim in `docs/reviews/SRR/minutes.md` lines 21 and 47 (sections "Rulings" and "Disposition"); decision memo section 8.0 row 107 (line 240); ADR-027 Status Accepted, section 6 quotes the ruling (line 88), section 7 repeats the four triggers (line 100) in the words of section 10. The Status row, header, section 1, section 10 and ADR-027 now agree. CK-DES-H1 and SA-033-1: Yes |

New findings: none. No hunk changes a criterion, weight, score, total, rank, robustness verdict, recommendation, alternative, risk row or trigger.

### Observations (no finding)

- **O-1.** Erratum 2 says the materialized hygiene risk "is carried by RSK-013, which names TS-002; no separate risk was entered". RSK-013's statement is the driver work-package risk and its history mentions the rustos hygiene package only as a numbering note, so "carried" means the register link rather than a mitigation step. No open risk is left out: the hygiene event was closed by CR-004 and run 6 (G5 PASS), so no register entry is needed.
- **O-2.** Erratum 4 calls the two HZ-008 rows "Proposed", which is what 07 section 14.1 still reads at `443b2a3` and at `HEAD` (`bfe05f43`). SRR decision 9 concurred with frequency control safety-critical ("Concur, with frequency control safety-critical", `decisions-for-owner.md` line 38), so the word Proposed is due to come out of 07. That is a 07 transcription item (cross item X-5), not a TS-002 defect: the erratum accurately cites the plan as committed, and the class does not change any score.
- **O-3.** Entries 1 and 5 are one-at-a-time sensitivities, as 06 section 14.4 requires. Applied together in the worst direction, A0 380 against A1 285 leads by 95 points; A0 stays first (INSP-054 records the same combined check).

### Assurance task answers at the delta

SA-033-1 Yes; SA-033-2 Yes (finding-1); SA-033-3 Yes (finding-2); SA-027-1 Yes (as the post-SRR-ruling delta); SA-211-1 Yes (finding-1); SA-EVD-1 Yes (finding-2, finding-5). CK-DES-A7 Yes, CK-DES-B2 Yes (finding-4); CK-DES-H1 Yes (finding-3, finding-6). Readiness R1 to R4 as iteration 1 (`readiness_met: true`): the author's return is the `443b2a3` commit message, which maps each change to its finding and states the sensitivity values.

### Pairing and concurrence (07 section 10.2)

INSP-013 (`paired_record` of this record) still names TS-002 `6c385dfc` and TS-001 `2a0c40a8`; its file-review delta on the errata is INSP-054, a PDR record (filed under PDR as the INSP-044 precedent allows), `reviewer_verdict: APPROVED`, no finding, on the same TS-002 blob `6b18cee8`. Read after the checks above, INSP-054 agrees with this delta on every lien, on the arithmetic and on the combined case. This record concurs; no INSP-054 finding is re-opened, and this delta raises none.

### Completion criteria (SWE-088; 07 section 10.2)

Met: readiness met; every applicable item answered; zero open findings (finding-1 to finding-6 Verified); the named blob equals `HEAD`; the file-review delta of the same blob (INSP-054) is reviewer APPROVED. `assurance_verdict: APPROVED`, `verdict: APPROVED`. `record_status` stays Open until the software lead closes the record (07 section 10.2); nothing in this record blocks the closure.

### Cross items (outside this record's scope, returned to Claude)

- **X-4.** INSP-054 reads `assurance_reviewer_agent: "pending: ... trade-studies-ts-001-ts-002-software-assurance.md"` and `assurance_verdict: pending`. This delta is the TS-002 assurance review of blob `6b18cee8` that the INSP-054 comment names ("the INSP-027 delta"); the INSP-054 reviewer may point its assurance fields at this record (INSP-027, delta iteration 2, APPROVED) instead of a new file, and then set its record verdict.
- **X-5.** 07 author: remove "Proposed" from the two HZ-008 rows of 07 section 14.1 (and the SWE-134 module rows at lines 642 and 644) to transcribe SRR decisions 9 and 40, if a CR in progress (CR-010) does not already do so; and, as post-SRR-ruling cross item X-3 still asks, cite decision 110 in the 07 section 17.1 rustos row in place of `OQ-SW-001` (still "due PDR" at `bfe05f43`).
- **X-6.** INSP-013 (`docs/reviews/SRR/checklists/trade-studies-ts-001-ts-002.md`) fails `tools/validate_docs.py` at `main` `c9f611d` on record drift for both studies (TS-001 at `HEAD` is `152c2b90`, later than the `c53414d9` INSP-054 reviewed). Its re-issue belongs to the file-review role.

### Tool runs (2026-09-29, `.venv/bin/python`)

| Command | Exit | Result |
|---|---|---|
| `tools/validate_docs.py` (before this update, `main` `c9f611d`) | 1 | 110 passed, 7 failed; this record failed on drift (`6c385dfc` against `HEAD` `6b18cee8`) |
| `tools/validate_docs.py` (after this update; working tree of `main` with other agents' uncommitted record edits) | 1 | 115 passed, 2 failed; this record PASS; the failures are INSP-047 (`cm-plan-05-software-assurance.md`, CR-007 drift, re-issued separately) and `docs/reviews/SRR/checklists/adrs-001-to-025.md` |

```
DELTA ITERATION 2 (2026-09-29, TS-002 errata 443b2a3): VERDICT: APPROVED
FINDINGS: finding-1 to finding-6 Minor, Verified; new findings 0; open Major 0
PRODUCT: docs/decisions/trade-studies/TS-002-firmware-runtime-make-buy.md@6b18cee831a67dc9550e6082c595023d77bcd704 (equal to HEAD, 1/1)
PAIRING: INSP-054 (file-review delta of the same blob) reviewer APPROVED, no finding; concur
MEASUREMENTS (delta): turns=20; minutes=35; cumulative turns=64, minutes=105; liens verified=6; major=0; minor=0 new
```
