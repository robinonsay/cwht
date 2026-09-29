---
# Peer-review record front matter (charter sections 2 and 5; docs/process/01-lifecycle-and-reviews.md
# section 13 is the single field list; docs/process/07-software-engineering-plan.md sections 2.1.1, 10.2
# and 15). This is the paired software assurance record (07 section 10.2 Record row) of the trade-study
# review INSP-055 (docs/reviews/PDR/checklists/ts-007-synthesizer-and-reference.md, reviewer
# reviewer:WP-PDR-20-ts-007-iter1, committed 8fea433), at the path INSP-055, TS-007 header row
# "Independent reviewer" and PDR work plan WP-PDR-20 "Records" name. Dispatch: 07 section 2.1.1 row
# "Trade studies and ADRs whose decision constrains a safety-critical or mission-critical component";
# rules C4 and C9 of the plan.
# Checklist applied: docs/templates/peer-review-checklist-software-assurance.md revision A AS ON ITS CR-012
# BRANCH (cr/CR-012-pdr-checklist-templates at 7784672, blob 5b13528504868b2add0f0b1e329c63aa2b54cdf4; not
# merged, absent from main). tools/validate_docs.py fails a record whose `checklist` names a template absent
# from main, and the lead SE convention of 2026-09-27 does not change the validator, so the `checklist` field
# names peer-review-checklist-risk revision A, the checklist INSP-055 applied (section B, trade studies,
# 08 section 3.5), and `assurance_checklist` names the template actually applied (the INSP-048, INSP-049 and
# INSP-051 form). The product blobs are all on main; only the template is branch-only.
# id: the brief assigned no id. INSP-074 is above every id on main, on every cr/ branch and in the working
# tree at 80d07f0 (highest INSP-072; the untracked ts-011-enclosure.md also carries INSP-071, cross item X-5),
# leaving INSP-073 free for that renumbering.
id: INSP-074
checklist: peer-review-checklist-risk
checklist_revision: A
assurance_checklist: "docs/templates/peer-review-checklist-software-assurance.md@5b13528504868b2add0f0b1e329c63aa2b54cdf4 (revision A, branch cr/CR-012-pdr-checklist-templates at 7784672)"
checklist_file: docs/reviews/PDR/checklists/ts-007-synthesizer-and-reference-software-assurance.md
product: docs/decisions/trade-studies/TS-007-synthesizer-and-reference.md
# product_commit and product_files: equal to INSP-055 iteration 1 (readiness R1; rule C2). Each blob equals
# git rev-parse 9ac2c42:<path>, git rev-parse HEAD:<path> and git hash-object <path> at HEAD 8fea433
# (checked 2026-09-27): the products are not branch-only
# Delta iteration 2 (2026-09-29, supersession): product_commit, product_blob and the TS-007 entry of product_files
# name cfc9111 and blob 3d1e4e59 (the Status row only, 06 section 14.6), equal to INSP-055 delta iteration 2 (081efb9).
# Each blob equals git rev-parse HEAD:<path> and git hash-object <path> at HEAD 081efb9; the checker and the figure are
# unchanged since 9ac2c42 (git log 9ac2c42..HEAD over the three files lists cfc9111 only). The iteration 1 values are
# kept in product_commit_iteration_1 and product_files_iteration_1
product_commit: "cfc9111d6cc0ede052f254bececf09d89d0699f3"
product_blob: 3d1e4e59f1109199a378e31da99289f01f3f7e21
product_files: ["docs/decisions/trade-studies/TS-007-synthesizer-and-reference.md@3d1e4e59f1109199a378e31da99289f01f3f7e21", "hardware/sim/freq/ts007_matrix.py@64c8aad44c9c9da777e6be544cb9553478236481", "docs/reviews/PDR/figures/ts-007-sensitivity.png@e0fb0048a8d6c9ba98016ddb892df33677d5b013"]
product_commit_iteration_1: "9ac2c42d1ff7b82e3734506aba14dec8eadc3923"
product_files_iteration_1: ["docs/decisions/trade-studies/TS-007-synthesizer-and-reference.md@72c47383cbaec09b6d1cc8d9ac8f7912b61c72fb", "hardware/sim/freq/ts007_matrix.py@64c8aad44c9c9da777e6be544cb9553478236481", "docs/reviews/PDR/figures/ts-007-sensitivity.png@e0fb0048a8d6c9ba98016ddb892df33677d5b013"]
# inputs read (not reviewed)
input_files: ["docs/reviews/PDR/checklists/ts-007-synthesizer-and-reference.md (INSP-055, committed 8fea433)", "docs/reviews/PDR/checklists/analysis-frequency-budget-and-clock-plan.md (INSP-056, committed 8fea433)", "docs/design/analysis/frequency-budget.md@1a7be266d1a309391aea99b51dd4a2a82e892d4c", "docs/process/07-software-engineering-plan.md", "docs/safety/hazards.json", "docs/process/05-configuration-and-data-management.md", "docs/risk/register.json", "docs/research/power-tree-and-charging.md", "docs/research/rustos-toolchain-proof.md", "docs/plan/pdr-work-plan.md", "docs/references/md/swehb/ (swe-022, 027, 033, 039, 057, 070, 134, 136, 205 section 7.1; 8-10 section 6)"]
# inputs read at delta iteration 2 (not reviewed), at HEAD 081efb9
input_files_iteration_2: ["docs/reviews/PDR/checklists/ts-007-synthesizer-and-reference.md (INSP-055 delta iteration 2, 081efb9)", "docs/decisions/adr/ADR-056-a5-hand-built-design.md (sections 2 item 2, 4.3, 7 'Other records')", "docs/decisions/trade-studies/TS-012-design-to-cost-hand-built.md@b93333867dbe21ed6243a8f85df1f7ff16d23c00 (sections 7.3, 8.1, 8.12)", "docs/reviews/PDR/checklists/ts-012-design-to-cost-software-assurance.md (INSP-118 iteration 3, 75b8304)", "docs/design/analysis/frequency-budget.md (revision 4, d030ce2: section 1 note on TS-007, section 5 requests)", "docs/design/analysis/sequencer-timing.md (revision 0, 95adefc: key-up and fault-path order)", "docs/safety/hazards.json (HZ-008 swe134_items and cause C7 at HEAD)", "docs/process/07-software-engineering-plan.md (sections 10.2, 14.1 drivers row, 19 rows WP-SW-05, 11, 14 at HEAD)", "docs/plan/pdr-work-plan.md revision 7 (section 3.0a, WP-PDR-20 row, rules C1, C2, C9)", "tools/check_commit_msg.py on cfc9111 and 9ac2c42"]
paired_record: INSP-055
product_type: trade-study-or-adr
# criticality: safety-critical. TS-007 header row "Decision class trigger" names the SW-SYNTH transmit
# frequency-word path and the SW-SAFE frequency verification unit; 07 section 14.1 lists both (rows
# "Frequency control, transmit frequency-word path" and "Frequency verification unit", marked Proposed there;
# a Proposed row counts as its proposed criticality, template R2), and hazards.json HZ-008
# firmware_role.safety_critical is true with the owner concurrence of package decisions 9 and 40
criticality: safety-critical
product_size: 1 trade study (362 lines; 2 scored alternatives, 8 mandatory and 7 enhancing criteria, Part B 4 rules), 1 checker, 1 figure
sprint: PDR-prep
author_agent: "author:WP-PDR-20 wave 1a (Claude as RF designer TX)"
reviewer_agent: "sa-reviewer:WP-PDR-20-ts-007"
assurance_required: true
assurance_reviewer_agent: "sa-reviewer:WP-PDR-20-ts-007 (software assurance function; paired file review INSP-055 by reviewer:WP-PDR-20-ts-007-iter1)"
# iteration: 2 is a delta (rule C1): the supersession of TS-007 by TS-012, no new full review
iteration: 2
readiness_met: true
# reviewer_verdict and assurance_verdict: APPROVED at iteration 1 (rule C1): zero Major findings; four Minor
# findings of this record, which ride with APPROVED and are fixed with the INSP-055 Minor fixes or become liens
# due at the CDR readiness declaration
reviewer_verdict: APPROVED
assurance_verdict: APPROVED
# verdict: set by Claude as software lead (07 section 10.2). Held at NEEDS CHANGES: the product blobs are on
# main, but the checklist applied exists only on cr/CR-012-pdr-checklist-templates (lead SE convention of
# 2026-09-27), and INSP-055 does not yet name this record (paired_record, assurance_reviewer_agent,
# assurance_verdict; each reviewer updates only its own record, cross item X-1). The software lead sets
# APPROVED on both records when INSP-055 carries the pairing and CR-012 merges with the template blob unchanged.
# Delta iteration 2: hold (b) is resolved (INSP-055 names this record at 081efb9: paired_record, assurance_reviewer_agent,
# assurance_verdict APPROVED); hold (a) stands (7784672 is not an ancestor of main at 081efb9). The reviewer does not set
# the record verdict (cross item X-4 of the delta)
verdict: NEEDS CHANGES
findings_major: 0
findings_minor: 4
# findings_open: delta iteration 2 closes all four by supersession, none fixed or verified in TS-007: finding-3 moot;
# finding-1 and finding-2 carried to TS-012 in part, with a residual transferred to INSP-118 (cross item X-2);
# finding-4 product part verified at cfc9111, lead SE part transferred to the INSP-118 finding-8 list (cross item X-3)
findings_open: 0
findings_fixed: 0
findings_verified: 0
findings_deferred: 0
assurance_findings_major: 0
assurance_findings_minor: 4
assurance_tasks_applied: ["swe-134 7.1 task 5", "swe-022 7.1 task 1", "swe-033 7.1 task 1", "swe-033 7.1 task 2", "swe-033 7.1 task 3", "swe-039 7.1 task 4", "swe-057 7.1 task 2", "swe-134 7.1 task 4", "swe-134 7.1 task 6", "swe-205 7.1 task 1", "swe-205 7.1 task 3", "swe-219 7.1 task 1", "swe-220 7.1 task 1", "swe-086 7.1 task 1", "swe-087 7.1 task 2", "swe-089 7.1 task 1", "swe-080 7.1 task 2", "swe-081 7.1 task 2"]
swe134_items_checked: [a, b, c, e, f, g, h, i, j, k, l]
deferred_rids: []
items_no: ["swe-033 7.1 task 2", "swe-134 7.1 task 4", "swe-134 7.1 task 6", "swe-205 7.1 task 1", "swe-205 7.1 task 3", "swe-057 7.1 task 2", SA-C-e, SA-C-g, SA-D1, SA-D2, SA-E3]
# effort: cumulative (iteration 1: 38 turns, 60 minutes; delta iteration 2: 32 turns, 50 minutes)
effort_turns: 70
effort_minutes: 110
# record_status: Closed by supersession at delta iteration 2 (06 section 14.6; ADR-056 section 7 "Other records", lead
# SE disposition; plan section 3.0a row TS-007 "Superseded outright"), as INSP-055 at 081efb9. 07 section 10.2 names no
# supersession route (cross item X-1). Reopens if the owner does not confirm the TS-007 row at PDR session S1 (OD-10
# part 1). Iteration 1 value: Open
record_status: Closed
date: 2026-09-27
date_closed: 2026-09-29
---

# Peer review record INSP-074: software assurance pair of INSP-055, TS-007 synthesizer and frequency reference (WP-PDR-20)

**Delta iteration 2 (2026-09-29, supersession; HEAD `081efb9`, product commit `cfc9111`): record CLOSED by supersession.** TS-012 supersedes TS-007 (ADR-056). The only product change since iteration 1 is `cfc9111`, which edits the TS-007 Status line only, as 06 section 14.6 allows, and keeps the prior status verbatim. No new finding. The four Minor findings close without a fix in TS-007: finding-3 is moot; finding-1 and finding-2 are carried to TS-012 in part, and their residual (the HZ-008 and 07 rows for the A5 changeover retune, the I2C driver and the FC0 counter) is transferred to INSP-118; finding-4's product part is verified at `cfc9111`, and its lead SE part joins the INSP-118 finding-8 commit list. See the section "Delta iteration 2" at the end. Everything between here and that section is the iteration 1 text.

**Product.** `docs/decisions/trade-studies/TS-007-synthesizer-and-reference.md` blob `72c47383` at freeze commit `9ac2c42` (freeze F0, rule C2), with the checker `hardware/sim/freq/ts007_matrix.py` (`64c8aad4`) and the figure `docs/reviews/PDR/figures/ts-007-sensitivity.png` (`e0fb0048`): the three `product_files` of INSP-055, each equal at `9ac2c42`, at `HEAD` (`8fea433`) and in the working tree. **Paired record:** INSP-055 (`ts-007-synthesizer-and-reference.md`), reviewer verdict APPROVED at iteration 1 with five Minor findings, record verdict held for this pair.

**Checklist.** `docs/templates/peer-review-checklist-software-assurance.md` revision A as on its CR-012 branch (`7784672`, blob `5b135285`), sections R, A to F and the section B row `trade-study-or-adr` plus the row "Every product type". It is branch-only; see the front matter for the `checklist` field.

**Acceptance criteria (rule C7).**
- Every task of the section B rows `trade-study-or-adr` and "Every product type" is in the task table.
- Every other SWE the product implements is added. TS-007 cites SWE-219 and SWE-220 (section 3.3, C5), and it is the risk-driven decision of RSK-002 and RSK-046, which are software-tagged (SWE-086).
- Every SWE-134 item that 07 section 14.2 allocates to the two components the study constrains is checked at trade-study maturity: the `SW-SYNTH` frequency-word path (a, b, f, g, h, i, k, l) and the frequency verification unit (a, b, f, g, h, i, k, l). Item c, and item e (which neither row allocates), are also checked because the recommendation changes their applicability (finding-1).
- The HZ-008 software contributions of each alternative are checked by action, inaction and incorrect action (SWEHB `swe-205` 7.1 task 1).

**Independence (rule C4).** This invocation authored no part of WP-PDR-20 (TS-007, the frequency budget, the clock plan, ADR-031, the checkers) and is not the file reviewer of INSP-055 or INSP-056. It edited no product file.

**Search first.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search. Queries: the software assurance template and trade-study SA pairs; SWE-033 SA tasking; commit trailer rules of 05; the BQ25887 and TPA6130A2 I2C bus. `grep` and `awk` were used afterwards only to pin lines and extract the SWEHB section 7.1 task lists. The rustos repository was not read.

## Findings (iteration 1)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | assurance | Minor | `swe-205 7.1 task 1`, `swe-134 7.1 task 6`, SA-D1, SA-C-e | TS-007 section 3.2 row A2 ("retuned between the RX LO and the TX carrier at each changeover"); section 4 M8 cells; section 7 line "Safety (M8)" ("The HZ-008 C7 and C8 causes are controlled identically") | In A2, one VCO carries the receive LO (133.300 to 139.000 MHz, M1) and the transmit carrier. The safety-critical frequency-word path therefore runs at every RX-to-TX changeover, which is every key-down in semi break-in (ADR-026). A skipped or stale retune (inaction), or a receive word written while transmitting (incorrect action, including a TX-to-RX retune before `PA_EN` falls), leaves the carrier at the receive LO, outside 144 to 148 MHz. The harmonic low-pass filter passes that frequency (HZ-008 description). HZ-008 C7 names only "a wrong divider or register computation, a corrupted frequency word, a calibration value out of range". Its `swe134_items` omit e (out-of-sequence commands), so the A2 sequencing is not a stated cause. The A1 counterpart is a wrong PLL or output assignment (CLK1 sourced from PLL A), and A1 writes the word path only on a tuning change. The M8 conclusion holds: K7 checks the carrier before `PA_EN` at every changeover (`frequency-budget.md` C-12.iv12, C-14.A2), and no Red risk results. The statement that the controls apply "identically" is not correct for this cause, though, and the study raises no hazard-data request for it. **Fix:** in the section 7 safety line and the A2 M8 cell, name the per-changeover safety-critical retune and its order: TX word, lock, K7 agreement, then `PA_EN`; and `PA_EN` low before the receive word. State that K7 before `PA_EN` bounds this cause. Add a section 8 impact that sends three requests. To WP-PDR-16b: the cause wording for HZ-008 C7 and item e in `swe134_items`. To the 07 writer: item e for the `SW-SYNTH` word-path row of 07 section 14.2. To the test author, through the lead SE: a key-down injection with the VCO left at the receive LO, which TC-SYS-110 lacks (its before-transmit runs use 150.000 MHz and plus or minus 12 kHz) | Open | Pending | |
| <a id="finding-2"></a>finding-2 | assurance | Minor | `swe-033 7.1 task 2`, `swe-205 7.1 task 3`, SA-D2 | TS-007 section 2 ("rustos knows which bus drivers carry safety-critical traffic (07 WP-SW-05, WP-SW-06, WP-SW-14)"); section 3.1 C5; section 8 "Impacts" (L2 SW requirements: "FC0 frequency verification"; Interfaces: "two GPIN pins") | The decision adds components to the safety-critical set, and the study does not route the flow-down of the safety requirements to them. (a) The bus driver of the word path joins the safety-critical drivers: WP-SW-06 SPI for A2, WP-SW-05 I2C for A1 (C5 evidence). 07 section 14.1 "Drivers these depend on" lists neither driver today, and says such drivers "join at the PDR re-run". So SWE-219, SWE-220, CS-16, CS-38 and the SA second review then apply to that driver, and section 8 does not name this input to the 03 section 4 PDR re-run or the WP-SW-06 row. (b) Section 8 selects FC0 on two GPIN pins, the TCXO-corrected route R3 of `frequency-budget.md` section 3.3. That is the CLOCKS block (the WP-SW-11 driver), not the "PIO state machine or TIMER capture" of 07 section 19 row WP-SW-14. Section 2 still names WP-SW-14. Route R3 also departs from the 07 section 14.1 row and the WP-SW-14 phrase "RP2350 crystal timebase, not the synthesizer reference". The frequency budget sends the K7 wording to WP-PDR-16b (its section 5), but neither note routes the matching 07 rows. **Fix:** state these changes in the section 8 impacts, each with its writer. For the 07 section 14.1 driver row and section 19 rows WP-SW-06, WP-SW-11 and WP-SW-14, the writer order is WP-PDR-17, then 13, then 47 (plan section 5.3), or a CR once 07 is under change control. For the 03 re-run input, the writer is WP-PDR-17. Correct section 2 to the driver set the recommendation uses. The TCXO common-cause bound of route R3 is INSP-056 finding-7 and is not raised again here | Open | Pending | |
| <a id="finding-3"></a>finding-3 | assurance | Minor | `swe-134 7.1 task 4`, `swe-057 7.1 task 2`, SA-C-g | TS-007 section 4 row C5-A2 ("SPI driver (WP-SW-06, also used by the display)"); section 3.2 row A1 (I2C control); section 6 item 5.4; section 7 A2 risk "LMX2571 properties not in the corpus" | The study does not assess isolation of the safety-critical word path from other traffic on its bus. For A2, the LMX2571 shares SPI with the display: `SW-DISPLAY` is mission-critical, and its fault could corrupt or block a synthesizer write through a shared data line or a chip-select fault. For A1, the Si5351A shares I2C with the BQ25887 ADC reads and the TPA6130A2 volume (`docs/research/power-tree-and-charging.md` "Baseline topology"), which serve `SW-PWR` and `SW-AUDIO`. The RP2350 has two instances of each controller (SPI0/SPI1, I2C0/I2C1; `docs/research/rustos-toolchain-proof.md` F9, High; 07 section 19 rows WP-SW-05, WP-SW-06), so a dedicated bus is available. Separately, 07 section 14.2 (`SW-SYNTH` word-path row, item g) requires the registers to be read back after every write. Whether the LMX2571 supports SPI read-back is not in the corpus, and value-of-information item 4 omits it (it lists supply range, SPI ceiling and retune behaviour). If the part does not read back, A2's word path rests on K7 alone for item g. (The Si5351A register map, AN619, is not in the corpus either, TS-007 M3 A1 cell; A1 is not recommended.) Lock detect is INSP-055 finding-4 and is not raised again. **Fix:** (a) add a design constraint for WP-PDR-31, 32 and 36a: the word-path device on its own bus instance, or an isolation argument against the shared bus; (b) add SPI register read-back to value-of-information item 4 and to the A2 risk statement; (c) state the item g consequence if read-back is absent | Open | Pending | |
| <a id="finding-4"></a>finding-4 | assurance | Minor | `swe-080 7.1 task 2`, SA-E3 | Freeze commit `9ac2c42`, trailers | The commit that creates TS-007, its checker and its figure touches 05 Table 4-1 rows 12 (trade studies, Record), 13, 24, 33 and 49, and carries no `Refs:` trailer. Its only trailer is `Co-Authored-By` (`git log -1 --format='%(trailers)' 9ac2c42`). 05 section 4.5 requires `Refs:` on every commit that touches a Table 4-1 row file. `tools/check_commit_msg.py --range 9ac2c42^..9ac2c42` reports "FAIL REFS_MISSING". That tool is not yet accredited (TV-019 is in the working tree only), so the trailer read above is the evidence. No class-CR row is past its CR-from event, so no `CR:` trailer was needed. **Fix:** history is not rewritten. The lead SE lists `9ac2c42` in the CSA change log as a RID candidate for the PDR (the `configuration-status.md` practice for commits without mandatory trailers), and the TS-007 revision commit carries `Refs: TS-007` (or `Refs: WP-PDR-20`) | Open | Pending | |

No Major finding. Every Yes and No below carries evidence. None of the four findings changes the ranking, the robustness verdict or the M8 pass, because the stated controls (K4 and K7 before `PA_EN`) bound each cause for both alternatives. The findings do change what the recommendation must carry into the hazard data, 07 and the architecture.

### Task table

| Task | Safety-critical designation (SWEHB 8.10 section 6) | Applied | Result and evidence | Relief (N/A only) | Finding ids |
|---|---|---|---|---|---|
| swe-134 7.1 task 5 | SC | Yes | This record is the assurance participation in the review of a product that 07 section 2.1.1 routes (row "Trade studies and ADRs", safety-critical column Yes) | | none |
| swe-022 7.1 task 1 | SC | Yes | Performed against the project software assurance plan, 07 section 15, with this template. The NASA-STD-8739.8 part is relieved (next column) | NASA-STD-8739.8 part: `rmm.json` SWE-022 T (standard not in the corpus) | none |
| swe-033 7.1 task 1 | | Yes | The acquisition versus development option for the frequency-control software is TS-002's decision (A0: rustos drivers developed, SI-033), carried by 07 sections 17.2 and 19. TS-007 selects hardware. Its software consequence is two developed bus drivers (C5) and the `SW-SYNTH` word-path units in `cwht-core`. No vendor software or generated register data is proposed. The options stand as evaluated | | none |
| swe-033 7.1 task 2 | SC | No | The study names the safety-critical path of each alternative (C5), and it cites SWE-219 and SWE-220 for the word path (section 3.3). It does not flow the safety-critical designation and its obligations to the new driver work. Nor does it route the counter move from WP-SW-14 to FC0 and WP-SW-11 | | finding-2 |
| swe-033 7.1 task 3 | | Yes | Section 7 assesses seven risks in the four-part format with scores (checked in INSP-055 CK-RSK-B8). The software-side consequence of the missing LMX2571 data (M3 by HostUnit, M6) is INSP-055 finding-1, not raised again. The assurance concern about the missing datasheet goes to SA-F1 | | none |
| swe-039 7.1 task 4 | | Yes | Trade study and source data assessed: every A2 value traces to `docs/research/2m-cw-transceiver-reference-designs.md` F16 to F21, with the confidence tags the study copies. The checker was re-run on an export of `9ac2c42`: exit 0, "VERDICT: Robust (top A2; rank changes: none)", 14 weight runs, 12 cell runs, the combined case (360.0 to 360.0) and the cost variant (A1 325.8, A2 338.0), all as the study states | | none |
| swe-057 7.1 task 2 | | No | The decision fixes part of the architecture: synthesizer bus, counter block, GPIN pins (section 8 "Interfaces"). It does not state the isolation that the safety requirements of 07 section 14.2 rows g and i need from shared buses | | finding-3 |
| swe-134 7.1 task 4 | SC | No | Partitioning: 07 section 5 item 5 and section 14.2 row d require untrusted input handling between components of different criticality, and a shared bus is such a path. The study does not assess it for either alternative (see finding-3). The logical separation of the word path from the verification unit is kept: the study keeps K7 independent in code (section 7 safety line), and the timebase question is INSP-056 finding-7 | | finding-3 |
| swe-134 7.1 task 6 | SC | No | The SWE-134 implementation must stay consistent with the hazard analysis. For A2, item e becomes relevant to HZ-008 through the changeover retune, and HZ-008 `swe134_items` omit it | | finding-1 |
| swe-027 7.1 task 1 | | N/A | Condition not met: the decision acquires no COTS, GOTS, MOTS, OSS or reused software. The parts are hardware. Drivers are developed in rustos (07 section 17.1 register unchanged) | Conditional task of the section B row ("reused or OSS component chosen"); 07 section 17.1 | none |
| swe-136 7.1 task 1 | | N/A | Condition not met: the decision selects no tool, emulator or model. The study's checkers are stated as developer evidence without a TV record (section 6 item 6; 05 section 9.1), and their arithmetic is hand-checkable (INSP-055 independent checks) | Conditional task of the section B row ("when the decision selects a tool"); 07 section 17.3 | none |
| swe-070 7.1 task 1 | | N/A | As swe-136: no model or simulation is used to qualify flight software or equipment. The checker results are decision support, not qualification evidence | Conditional task of the section B row; 07 section 17.3 | none |
| swe-205 7.1 task 1 | SC | No | Software contributions by action, inaction and incorrect action, walked per alternative. **Action:** a wrong word computation or calibration (C7, both alternatives). **Incorrect action:** a corrupted word (C7), a wrong PLL or output assignment (A1), a receive word written while transmitting (A2). **Inaction:** a skipped changeover retune (A2) and an unreported loss of lock (C8 with lock detect, INSP-055 finding-4). The A2 sequencing causes are not in HZ-008 | | finding-1 |
| swe-205 7.1 task 3 | SC | No | The decision adds a bus driver to the safety-critical driver set of 07 section 14.1, and it moves the counter to the CLOCKS block. The study does not state either as an input to the hazard-analysis component list or to the 03 PDR re-run | | finding-2 |
| swe-219 7.1 task 1 | SC | Yes | Implemented SWE cited by the study (C5 rationale, section 3.3): SWE-219 applies to the word path in both alternatives, and C5 scores the driver count against it. No coverage claim is made at trade maturity, and none is due (07 section 9.6) | | none |
| swe-220 7.1 task 1 | SC | Yes | As swe-219: the study cites SWE-220 for the word path. There is no code at trade maturity to measure, and the obligation is carried to the drivers by finding-2 | | none |
| swe-086 7.1 task 1 | | Yes | The study serves RSK-002 and RSK-046 (both software-tagged, `docs/risk/register.json`). It sends its risk entries to the register writer WP-PDR-18 as requests: a RSK-035 re-score, RSK-040 and RSK-041 members, and two new entries (section 7 "Would be entered as"). This follows plan section 5.3, which makes WP-PDR-18 the only writer | | none |
| swe-087 7.1 task 2 | | Yes | The five Minor findings of INSP-055 are Open with fixes named. No finding is closed without evidence (iteration 1) | | none |
| swe-089 7.1 task 1 | | Yes | INSP-055 carries the SWE-089 measurements (front matter `effort_turns` 44, `effort_minutes` 70, finding counts, `items_no`). This record carries its own | | none |
| swe-080 7.1 task 2 | | No | Change route of the product files: TS-007 is a new Record-class item (05 Table 4-1 row 12), created at the F0 freeze without the `Refs:` trailer 05 section 4.5 requires | | finding-4 |
| swe-081 7.1 task 2 | | Yes | The safety-critical product and its hazard data are under configuration management: TS-007, the checker and the figure are committed at `9ac2c42`. `docs/safety/hazards.json` is under row control with the single writer WP-PDR-16b (plan section 5.3) | | none |

## Readiness criteria

| # | Criterion | Result | Evidence |
|---|---|---|---|
| R1 | Product committed and frozen; `product_files` equal to the paired record's | Yes | `git rev-parse 9ac2c42:<path>` and `HEAD:<path>` for the three files: `72c47383`, `64c8aad4`, `e0fb0048`, equal to INSP-055 `product_files` |
| R2 | Product type and criticality identified | Yes | 07 section 2.1.1 row "Trade studies and ADRs whose decision constrains a safety-critical ... component" (`trade-study-or-adr`). Criticality safety-critical by the 07 section 14.1 rows "Frequency control, transmit frequency-word path" and "Frequency verification unit" (Proposed there, concurred by package decisions 9 and 40 per `hazards.json` HZ-008 `firmware_role.statement`) |
| R3 | `validate_docs.py` on the product files; `traceability.py --report-only --output <scratch>` clean for the ids the product touches | Yes | `traceability.py --report-only --output` to the scratchpad: exit 0, "245 requirements, 173 test cases, 0 violation(s), 2 warning(s)" (REQ-SYS-125 and REQ-SYS-148, not touched by TS-007); `docs/vv/` unchanged. `validate_docs.py`: see the Commands section |
| R4 | Paired file review filed under its own invocation; this reviewer is neither author nor file reviewer | Yes | INSP-055 `author_agent` "author:WP-PDR-20 wave 1a", `reviewer_agent` "reviewer:WP-PDR-20-ts-007-iter1"; this record `reviewer_agent` "sa-reviewer:WP-PDR-20-ts-007" |

## A. Dispatch, independence and record integrity

| Id | Answer | Evidence |
|---|---|---|
| SA-A1 | Yes | 07 section 2.1.1 row 3, safety-critical column Yes. The study constrains `SW-SYNTH` (word path) and `SW-SAFE` (frequency verification unit), 07 section 14.1 |
| SA-A2 | Yes | Three invocations: author "author:WP-PDR-20 wave 1a", file reviewer "reviewer:WP-PDR-20-ts-007-iter1", assurance reviewer "sa-reviewer:WP-PDR-20-ts-007". INSP-055 names this pair as a separate invocation (its `assurance_reviewer_agent` "pending (separate invocation ...)") |
| SA-A3 | Yes | Same product, same three blobs, same commit `9ac2c42`. No product change after either review (TS-007 log: only `9ac2c42`) |
| SA-A4 | Yes | INSP-055 applied `peer-review-checklist-risk.md` section B, the checklist 08 section 3.5 assigns to trade studies. Items B1 to B10 are answered with evidence and B5 is answered No with five findings. `swe-088` 7.1 task 1, criteria a to d: checklist used, readiness recorded (R1 to R4), findings tracked with state, measurements recorded |

## B. SWE-to-task table

| Id | Answer | Evidence |
|---|---|---|
| SA-B1 | Yes | The task table holds every task of the rows `trade-study-or-adr` and "Every product type", plus swe-205 task 1, swe-219, swe-220, swe-086, swe-087 task 2, swe-089, swe-080 task 2 and swe-081 task 2 for the SWEs the product implements or touches. `assurance_tasks_applied` lists every Yes and No row |
| SA-B2 | Yes | The three N/A rows (swe-027, swe-136, swe-070) are conditional tasks whose condition is not met, each with the 07 section named. No SC task is N/A |
| SA-B3 | Yes | Each No row cites a finding (finding-1 to finding-4) |

## C. SWE-134 items a to l (trade-study maturity: the recommendation neither precludes nor weakens the 07 section 14.2 provision)

| Id | Answer | Evidence |
|---|---|---|
| SA-C-a | Yes | Both alternatives allow the `SW-SYNTH` row a provision, "starts unprogrammed with the `PA_EN` frequency prerequisite false until the first write is read back and ... verified", and the verification-unit row a provision (`PA_EN` refused until the first verification passes). The A2 read-back part is conditional (SA-C-g) |
| SA-C-b | Yes | Row b states "unprogrammed, programming, locked, fault" as states. A2 adds a receive or transmit tuning dimension at each changeover, which the design can state. Nothing is precluded, and the sequencing consequence is carried by finding-1 |
| SA-C-c | Yes | `safe_state()` drives `PA_EN` low first (07 section 14.2 row c). A VCO left at either word after termination radiates nothing with `PA_EN` low, for both alternatives |
| SA-C-d | N/A | The study creates no operator override. Frequency selection is not an override in 07 section 14.2 row d |
| SA-C-e | No | Not allocated to the word path by 07 section 14.2 or HZ-008 `swe134_items`. A2 makes the retune order safety-relevant at every changeover (finding-1). The mission-critical `SW-SYNTH` row e ("a retune request is rejected while a transmit sequence is in progress") covers operator retunes, not the changeover retune the sequence itself performs |
| SA-C-f | Yes | The complement-held set frequency (rows f of both units) does not depend on the part |
| SA-C-g | No | Register read-back after every write (word-path row g) is not evidenced for either part: the LMX2571 read-back is not in the corpus, and neither is the Si5351A register map (AN619, TS-007 M3 A1 cell). The study assesses it for neither, and it matters for the recommended A2. Lock detect is INSP-055 finding-4. See finding-3 |
| SA-C-h | Yes | The band-edge check before every write (row h; REQ-SYS-009) holds for both. For A2 it runs at every changeover, inside the lead-in budget (`frequency-budget.md` C-14.A2, 7.5 ms, or 7.6 ms on the INSP-056 finding-5 basis, against 12 ms) |
| SA-C-i | Yes | The word path and K7 stay separate in code for both alternatives (TS-007 section 7 safety line; 07 section 14.1 verification-unit row). The shared-TCXO timebase of route R3 is common to A1 and A2 and is INSP-056 finding-7 |
| SA-C-j | Yes | Changeover to verified carrier within the 12 ms lead-in for A2 (FastLock below 1.5 ms plus an interval-12 count, C-14.A2), and the transmit-time detection budget of REQ-SYS-182 (C-15, 46.0 ms against 100 ms). Carried from the frequency budget, whose record INSP-056 is NEEDS CHANGES on other grounds (cross item X-2) |
| SA-C-k | Yes | Bus errors are handled with the prerequisite false (word-path row k) for either bus. Not precluded |
| SA-C-l | Yes | Unlocked or off-frequency on key-down leads to Fault-safe (row l; REQ-SYS-154) for both. The unlock trigger's mechanism is INSP-055 finding-4 and INSP-056 finding-2 |

## D. Software safety analysis and hazard traceability

| Id | Answer | Evidence |
|---|---|---|
| SA-D1 | No | HZ-008 causes C7 and C8, walked with SWEHB `swe-205` section 7.7.2 in mind (control of safety-critical hardware: the synthesizer output feeds the PA; interlocks: the `PA_EN` frequency-verified prerequisite; common-cause faults: the shared TCXO and the shared buses). The A2 changeover-sequencing contribution is missing (finding-1). The shared-bus common cause is finding-3, and the TCXO common cause is INSP-056 finding-7 |
| SA-D2 | No | The components the study names are in 07 section 14.1 with criteria a, c, e, the union of HZ-008 `firmware_role.criteria`. The bus driver and counter-block changes the recommendation brings are not stated as inputs to the PDR re-run (finding-2) |
| SA-D3 | N/A | No software requirement is written at trade maturity. The REQ-SW-SAFE and `SW-SYNTH` rows come from WP-PDR-35. The system-level ids the study touches (REQ-SYS-154, 182) report no traceability violation (R3) |
| SA-D4 | N/A | No safety-tagged software requirement is written by this product |
| SA-D5 | N/A | No hazard-tracing software requirement is written by this product. The TC-SYS-110 gap for the A2 case is carried in finding-1 as a request to the test author |
| SA-D6 | No | The HZ-008 fault tree of 07 section 14.2 row i changes with A2 (per-changeover word writes). The study sends no update request (finding-1) |

## E. Peer review, change and configuration assurance

| Id | Answer | Evidence |
|---|---|---|
| SA-E1 | Yes | Iteration 1: there are no earlier iterations. INSP-055's five Minor findings are Open with named fixes |
| SA-E2 | Yes | Both records carry the SWE-089 fields (front matter) |
| SA-E3 | No | `9ac2c42` has no `Refs:` trailer (finding-4). No `CR:` trailer was required: TS-007 is Record class and rows 24 and 49 are CR class from CDR (05 Table 4-1), not yet reached |
| SA-E4 | N/A | Test and code rows only; there is no test or credit run here |

## F. Assurance risks, metrics and reporting

| Id | Answer | Evidence |
|---|---|---|
| SA-F1 | Yes | One assurance concern that is not a product defect goes to the register writer WP-PDR-18 as a member of RSK-046 with tag `assurance`. It reads: "Given the recommended LMX2571 whose register map, SPI read-back, lock-detect output and supply range are not in the corpus and whose datasheet download awaits owner permission (OD-18 or OD-39), there is a possibility that the safety-critical `SW-SYNTH` word-path design and its HostUnit cases (M3) cannot be written at the PDR software design, adversely impacting the SWE-134 g and l provisions of 07 section 14.2, leading to a late design change of a safety-critical unit." The lead SE forwards it (cross item X-3) |
| SA-F2 | Yes | Front matter: findings by severity and state, `assurance_findings_major` 0, `assurance_findings_minor` 4, `items_no`, effort |
| SA-F3 | Yes | The package "Software assurance findings" section can take from this record: assurance verdict APPROVED; four Minor findings, Open; 18 tasks applied, 3 N/A with their conditions; SWE-022 relief used |

## Cross items for the lead SE (not findings on TS-007)

- **X-1.** INSP-055 still reads `assurance_reviewer_agent: "pending (...)"` and `assurance_verdict: pending`, and it has no `paired_record`. Its reviewer updates it to `paired_record: INSP-074`, names this reviewer, and copies `assurance_verdict: APPROVED` (07 section 10.2 Record row). The record verdicts then follow the lead SE convention for the branch-only template.
- **X-2.** The M8 and C4 evidence rests on `frequency-budget.md` and `clock-plan.md`, whose record INSP-056 is NEEDS CHANGES with four Major findings. Its findings 1 and 2 (the REQ-SYS-154 true-error limit, and unlock detection) bear on K7, the control on which this record's "no Red risk" conclusion relies. They apply to A1 and A2 alike, so the ranking stands. Before B1a (rule C9), the owner decision sheet should state that M8 passes on K7 as INSP-056 closes it. INSP-056 sets `assurance_verdict: not-required`. Its product proposes the REQ-SYS-154 and REQ-SYS-182 values and the K7 route for the safety-critical verification unit, while 07 section 2.1.1 routes analyses to no row. This routing is reported here, not reviewed (template "When it is used").
- **X-3.** The SA-F1 risk request goes to WP-PDR-18 (the register's single writer, plan section 5.3).
- **X-4.** Findings 1 and 2 carry requests to WP-PDR-16b (`hazards.json`) and to the 07 writer (WP-PDR-17, then 13, then 47). The lead SE routes them with the TS-007 revision.
- **X-5.** The untracked `docs/reviews/PDR/checklists/ts-011-enclosure.md` carries `id: INSP-071`, which the committed WP-PDR-33 record already uses (`40e0d5e`). This record took INSP-074 and left INSP-073 free.

## Commands

- `git rev-parse 9ac2c42:<path>`, `git rev-parse HEAD:<path>`, `git hash-object <path>` for the three product files: equal to `product_files`.
- `.venv/bin/python hardware/sim/freq/ts007_matrix.py` on a `git archive 9ac2c42` export in the scratchpad: exit 0, "VERDICT: Robust (top A2; rank changes: none)".
- `.venv/bin/python tools/traceability.py --report-only --output <scratchpad>/traceability-report.md`: exit 0, 0 violations; `docs/vv/` unchanged.
- `.venv/bin/python tools/check_commit_msg.py --range 9ac2c42^..9ac2c42`: "FAIL REFS_MISSING" (tool not accredited, TV-019 pending; the evidence is `git log -1 --format='%(trailers)' 9ac2c42`).
- `.venv/bin/python tools/validate_docs.py`: this record passes (see the return).

## Visual closure

`docs/reviews/PDR/figures/ts-007-sensitivity.png` (blob `e0fb0048`) was opened with the Read tool. It shows 28 bar pairs (14 weight runs, 12 cell runs, the combined case, the cost variant) with dotted baseline lines at 295 and 380. A2 leads in every run except the combined tie at 360, as stated in TS-007 section 6.

## Measurements (SWE-089)

Tasks in the table: 21 (18 applied, 3 N/A). Tasks answered No: 6. Checklist items answered No: 5 (SA-C-e, SA-C-g, SA-D1, SA-D2, SA-E3). SWE-134 items checked: 11 (d N/A). Findings: 0 Major, 4 Minor, all Open. Iteration 1. Renders inspected: 1. Effort: 38 turns, about 60 minutes.

## Delta iteration 2 (2026-09-29, supersession; HEAD `081efb9`, product commit `cfc9111`)

**Scope (rule C1).** A delta, not a new full review. It checks the one product change since iteration 1 under the assurance lens, names the new TS-007 blob, and disposes of the four Minor findings of iteration 1 now that TS-012 supersedes TS-007 (ADR-056 section 2 item 2; plan revision 7 section 3.0a row TS-007 "Superseded outright"; ADR-056 section 7 "Other records": "TS-007's reviews INSP-055 and INSP-074 end with the study superseded (lead SE disposition)"). The task table and checklist sections R and A to F above are the iteration 1 answers on blob `72c47383` and are not re-answered: TS-007 goes to no owner decision sheet (rule C9), so no assurance answer on its recommendation is needed any more.

**Independence (rule C4).** Written by a new invocation of the software assurance reviewer role. It authored nothing in TS-007, TS-012 or ADR-056, and no iteration of INSP-055, INSP-110, INSP-118, INSP-056 or INSP-111. It edited no product file and no record other than this one. Earlier sections of this record are kept as written; the front matter keeps each iteration 1 value in a comment or an `_iteration_1` field.

**Search first (rule C3).** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (queries: "INSP-074 TS-007 synthesizer and reference software assurance supersession"; "peer review record closed by supersession finding moot transferred to another record state"). `grep`, `git log`, `git show` and `sed` were used afterwards only to pin lines, commits and blobs. The rustos repository was not read.

### Product state

`git log --oneline 9ac2c42..HEAD` over the three `product_files` lists `cfc9111` only ("TS-001 and TS-007 status rows superseded by TS-012 (ADR-056)"). TS-007 `72c47383` becomes `3d1e4e59`. `ts007_matrix.py` (`64c8aad4`) and `ts-007-sensitivity.png` (`e0fb0048`) are unchanged. At HEAD `081efb9`, `git rev-parse HEAD:<path>` equals `git hash-object <path>` for all three. These are the same three blobs that INSP-055 names at its delta iteration 2 (`081efb9`).

### Verification of `cfc9111` (TS-007, one hunk)

| # | Check | Evidence | Result |
|---|---|---|---|
| V1 | The Status line is the only edit (06 section 14.6: "the only edit to the old file is its Status line") | `git show cfc9111 -- <TS-007>`: one hunk `@@ -6 +6 @@`; `git diff --numstat 72c4738 3d1e4e5`: `1 1`; `diff <(git show 72c4738 \| sed 6d) <(git show 3d1e4e5 \| sed 6d)`: no output | Yes |
| V2 | The prior status is kept verbatim | The new row ends "Previous status, kept as written: In review", and the iteration 1 row was "In review" | Yes |
| V3 | No safety-relevant content of TS-007 changed: the section 3.3 SWE-219 and SWE-220 citations, the section 7 safety line, the M8 cells, section 8 impacts | Follows from V1: no other line changed | Yes |
| V4 | The row's claims agree with the records they cite | TS-012 section 10 (A5, the owner's decision of 2026-09-29) and section 8.3 BOM rows 9 and 29 (Adafruit 2045 Si5351A, TG2520SMN); D-17 route R3 (TS-012 line 478: FC0 on GPIN0 and GPIN1, timed by the XOSC, "independent of the synthesizer and its driver"); TS-012 line 110 prunes the LMX2571 as reflow-only; ADR-056 section 2 item 2 (line 59) names the same replacement; plan section 3.0a and the WP-PDR-20 row (20a, 20b) carry the analyses the row lists | Yes |
| V5 | The row does not overstate the state or the safety basis | It says ADR-056 records the decision and that the owner's S1 confirmation (OD-10 part 1) is pending; ADR-056 line 6 reads Proposed, with items 2 to 4 for S1. It does not claim that any HZ-008 control is changed or verified | Yes |
| V6 | Change route (05 section 4.5; iteration 1 finding-4 product part) | `tools/check_commit_msg.py --range cfc9111^..cfc9111`: "PASS cfc9111: rows 12; Refs: TS-012, TS-001, TS-007, WP-PDR-54", exit 0 | Yes |

Result: the edit is the one 06 section 14.6 allows. No new finding.

### Where the A5 design leaves each assurance question

A5 is neither TS-007 alternative. `frequency-budget.md` revision 4 (`d030ce2`, line 41) states: "the Si5351A of A1 is used, but its PLL A carries the receive LO and is retuned to the carrier at every changeover, as A2's synthesizer was". TS-012 section 7.3 (line 491) gives the same sequence: at t0, "PLL A is retuned to the carrier with CLK1 enabled (the I2C writes ...)". Its section 8.1 diagram (lines 577 to 599) shows the Si5351A as the only I2C device, cells charged outside the radio, an analog audio chain and no display. So the A2-specific parts of findings 1 to 3 are moot, but the per-changeover retune of finding-1 and the I2C word path of finding-2 apply to the chosen design.

A finding is **moot** when its subject is not in the chosen design and nothing of it remains to be carried. It is **carried** when the same question applies to A5 and a record that stands (TS-012 or an analysis it cites) already holds it. A **residual** is the part that applies to A5 but that no standing record holds yet. The residual is transferred to INSP-118, the software assurance record of the study that now decides the synthesizer (cross item X-2).

### Findings (delta iteration 2)

| Finding | Severity | State | Where it goes |
|---|---|---|---|
| finding-1 | Minor | Closed (carried to TS-012 in part; residual transferred to INSP-118) | **Moot:** the LMX2571 single-VCO cells of TS-007 (A2 is not taken, TS-012 line 110). **Carried:** the transmit-direction order "TX word, lock, count agreement, then `PA_EN`" is in TS-012 section 7.3 (line 491: "SW-SYNTH reads the lock status and SW-SAFE compares the count ... and only then does SW-SAFE set PA_EN") and section 8.12 row WP-PDR-35, 41 (line 999: "PA_EN set only after the counted agreement"), with the lock-gated changeover requested of WP-PDR-23a by `frequency-budget.md` section 5 (revision 2 requests). The return order, `PA_EN` low before the receive word, is in `sequencer-timing.md` revision 0 (`95adefc`, lines 193 and 196, rows KU-04 and FP-01: `PA_EN` low first, then CLK1 off and T/R to receive), which has its own review. **Residual, not held by TS-012 or INSP-118:** HZ-008 cause C7 still names only "a wrong divider or register computation, a corrupted frequency word, a calibration value out of range", and HZ-008 `swe134_items` at HEAD are `[a, b, f, g, h, i, k, l]`, without item e, although A5 retunes the safety-critical word path at every changeover. TS-012 section 8.12 row WP-PDR-16, 17 (line 997) asks only for the K7 wording on route R3. The 07 section 14.2 `SW-SYNTH` word-path row has no item e. TC-SYS-110 has no key-down case with PLL A left at the receive LO |
| finding-2 | Minor | Closed (carried to TS-012 in part; residual transferred to INSP-118) | **Moot:** part (a) for A2 (the WP-SW-06 SPI driver), and the correction of TS-007 section 2 (TS-007 is not edited). **Carried:** the driver-set change is in TS-012 section 8.12 row WP-PDR-35, 41 ("display and encoder drivers removed; decoder, menu, FC0 counter, TX sequencing added"). The counter as FC0 is in TS-012 line 478 and `frequency-budget.md` section 5 row WP-PDR-32 ("FC0 with two GPIN inputs, not a PIO or TIMER capture"). ADR-056 section 4.3 (line 147) sends the safety-critical determination to the WP-PDR-17 re-run (OD-35 at S2). **Residual, not held by TS-012 or INSP-118:** for A5 the word path runs on I2C (`sequencer-timing.md` row KD-06, "I2C0", SW-SYNTH), so WP-SW-05 joins the safety-critical drivers. No record asks the 07 writer to say so. 07 at HEAD (`106bc3a`) line 601 still lists the counter as "PIO or TIMER capture" and no I2C driver. Line 787 (WP-SW-14) still reads "PIO state machine or TIMER capture ... not from the synthesizer reference", which route R3 departs from (the FC0 is in the CLOCKS block, WP-SW-11) |
| finding-3 | Minor | Closed (moot by supersession) | **Moot:** the shared buses it named are not in A5. The display (SPI with the LMX2571) is removed (TS-012 line 999). The BQ25887 and TPA6130A2 that shared the A1 I2C bus are gone: cells are charged outside the radio, the audio chain is analog, and the section 8.1 diagram shows the Si5351A as the only I2C device. The LMX2571 read-back question goes with the part. **What stays is held by standing records:** the dedicated bus instance is requested of WP-PDR-37 and 38 by `frequency-budget.md` section 5 ("The Si5351A I2C bus on its own RP2350 instance (TS-007 SA finding-3)"), under the INSP-056 and INSP-111 reviews. Register read-back after every write is 07 section 14.2 row g itself, which WP-PDR-35 writes from 07. The budget read the Si5351A lock status in AN619 (register 0 bit 5 LOL_A, readable over I2C, `frequency-budget.md` line 284) |
| finding-4 | Minor | Closed (product part Verified at `cfc9111`; lead SE part transferred to the INSP-118 finding-8 list) | **Product part verified:** the TS-007 revision commit carries `Refs:` (V6). **Lead SE part:** supersession does not change the fact that `9ac2c42` has no `Refs:` trailer (`check_commit_msg.py --range 9ac2c42^..9ac2c42`: "FAIL REFS_MISSING ... touches rows 12, 13, 24, 33, 49", exit 1). It is not yet listed: `git grep 9ac2c42 -- docs/cm docs/plan` is empty. It joins the commits of INSP-118 finding-8 and cross item X-9 (the five TS-012 hashes and `dd39a64`) and INSP-111's `802347b` and `4153acf` in one CSA change-log listing of RID candidates (cross item X-3) |

Counts at this delta: 4 Minor, 0 Major; open 0; fixed 0; verified 0 (finding-4 product part only); deferred 0; closed by supersession 4 (moot 1; carried in part with a residual transferred 2; product part verified with the lead SE part transferred 1). No new finding.

### Readiness (delta iteration 2)

| # | Criterion | Result | Evidence |
|---|---|---|---|
| R1 | Product committed; `product_files` equal to the paired record's | Yes | The three blobs above, equal to HEAD and to INSP-055 at `081efb9` |
| R2 | Product type and criticality | Yes | Unchanged from iteration 1 |
| R3 | `validate_docs.py` on the record; `traceability.py` clean for the ids the product touches | Yes | See Commands. `cfc9111` touches no requirement, test case or hazard id |
| R4 | Paired file review filed under its own invocation | Yes | INSP-055 delta iteration 2 (`081efb9`) |

### Request from the frequency budget (TS-007 R-M3)

`frequency-budget.md` revision 4 section 5 asks WP-PDR-20b to record in this delta the TS-007 R-M3 result for RB2, the TG2520SMN on XA. Recorded as the budget states it (section 3.5, RB-0; not re-derived here, because INSP-056 and INSP-111 review that section): **not met**, 2.7 ppm (fo-TC band referred to +25 C) or 3.2 ppm (band read as a 1.0 ppm window), against 1.5 ppm. TS-007 is not revised, so the result changes no TS-007 cell. It matters to assurance because option (c) of `frequency-budget.md` section 3.5 would make part of HZ-008 K4 a `SW-SYNTH` software control (items g and k). That decision is the owner's, on the lead SE's sheet. The records that hold it are the frequency budget, INSP-111 and ADR-056 (D-17). It is not an INSP-074 matter.

### Cross items (outside this record's scope)

- **X-1 (lead SE; 07 writer).** 07 section 10.2 (Action tracking row) allows `record_status: Closed` "only when every finding is Verified or Deferred". It has no route for a record whose product is superseded. This record and INSP-055 (`081efb9`) close on the lead SE disposition of ADR-056 section 7, with finding states "Closed (moot ...)" and "Closed (carried ...)" that 07 section 10.2 does not define. Add the supersession route and its finding states to 07 section 10.2, and to the 01 section 13 field list if needed, through the WP-PDR-12 or WP-PDR-17 change route. Until then this closure rests on ADR-056 section 7.
- **X-2 (lead SE, to the INSP-118 reviewer or the ADR-056 software assurance pair).** Take the finding-1 and finding-2 residuals as Minor liens at the next delta. INSP-118 cross item X-14 already names the ADR-056 pair as the record that carries open liens. The requests to route, for A5:
  - **To WP-PDR-16b.** HZ-008 cause C7 names the per-changeover PLL A retune: a transmit word not written or stale at key-down (carrier left at the receive LO), and a receive word written before `PA_EN` falls. Add item e to HZ-008 `swe134_items`.
  - **To the 07 writer** (WP-PDR-17, then 13, then 47, plan section 5.3; or a CR once 07 is under change control). Item e in the section 14.2 `SW-SYNTH` word-path row. In section 14.1, the drivers row names I2C (WP-SW-05, the Si5351A bus) and the FC0 counter in the CLOCKS block in place of "PIO or TIMER capture". Section 19 rows WP-SW-05, WP-SW-11 and WP-SW-14 are updated to match, and WP-SW-14 drops "not from the synthesizer reference" for route R3.
  - **To the test author.** A TC-SYS-110 key-down injection with PLL A left at the receive LO.
- **X-3 (lead SE).** List `9ac2c42` in the CSA change log as a RID candidate for the PDR, with the INSP-118 finding-8 and X-9 commits and INSP-111's `802347b` and `4153acf`.
- **X-4 (software lead).** Record verdict. Hold (b) of iteration 1 is resolved: INSP-055 names this record at `081efb9`. Hold (a) stands: `git merge-base --is-ancestor 7784672 main` is false at `081efb9`. The `verdict` is left at NEEDS CHANGES for the software lead. Because TS-007 goes to no decision sheet, the held verdict blocks nothing.
- **X-5.** If the owner does not confirm the TS-007 row at S1 (OD-10 part 1), this record reopens, and the four findings return to Open on blob `3d1e4e59`. This is the same condition as INSP-055 cross item X-3.

### Commands (delta iteration 2)

- `git log --oneline 9ac2c42..HEAD -- <three product files>`: `cfc9111` only.
- `git show cfc9111 -- docs/decisions/trade-studies/TS-007-synthesizer-and-reference.md`: one hunk, line 6. `git diff --numstat 72c4738 3d1e4e5`: `1 1`. The line-6-deleted diff: no output.
- `git rev-parse HEAD:<path>` and `git hash-object <path>` at `081efb9`: `3d1e4e59`, `64c8aad4`, `e0fb0048`.
- `.venv/bin/python tools/check_commit_msg.py --range cfc9111^..cfc9111`: PASS, exit 0. `--range 9ac2c42^..9ac2c42`: FAIL REFS_MISSING, exit 1.
- `git merge-base --is-ancestor 7784672 main`: false. `git grep 9ac2c42 -- docs/cm docs/plan`: no match.
- HZ-008 `swe134_items` read from `docs/safety/hazards.json` at HEAD: `[a, b, f, g, h, i, k, l]`.
- `.venv/bin/python tools/validate_docs.py`: this record PASS with no drift note (overall result in the return). `.venv/bin/python tools/traceability.py`: 0 violations; `docs/vv/traceability-report.md` and `traceability.json` restored with `git restore`.

### Measurements (delta iteration 2, SWE-089)

Commits verified: 1 (1 hunk). Checks: 6 (V1 to V6), all Yes. Findings dispositioned: 4 (moot 1, carried in part with residual 2, product part verified with the lead SE part transferred 1). New findings: 0. Renders: 0 (no figure changed). Effort: 32 turns, about 50 minutes (cumulative 70 turns, 110 minutes).

### Verdict (delta iteration 2)

```
DELTA ITERATION 2 (2026-09-29, supersession; HEAD 081efb9, product commit cfc9111): ASSURANCE VERDICT: APPROVED (unchanged); record CLOSED by supersession
PRODUCT: TS-007@3d1e4e59 (Status row only, 06 section 14.6: verified; prior status "In review" kept verbatim); ts007_matrix.py@64c8aad4 and ts-007-sensitivity.png@e0fb0048 unchanged
FINDINGS: finding-3 Closed (moot); finding-1, finding-2 Closed (carried to TS-012 in part; residual transferred to INSP-118, X-2); finding-4 Closed (product part Verified at cfc9111; lead SE part to the CSA listing, X-3); open Major 0; new 0
MEASUREMENTS: checks=6; turns=32; minutes=50; cumulative turns=70, minutes=110
```
