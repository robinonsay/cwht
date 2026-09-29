---
# Peer-review record front matter (charter sections 2 and 5; docs/process/01-lifecycle-and-reviews.md
# section 13 is the single field list; docs/process/07-software-engineering-plan.md sections 2.1.1, 10.2
# and 15). This is the paired software assurance record (07 section 10.2 Record row) of the independent
# review INSP-130 of ADR-056 to ADR-059 (PDR work plan revision 7, WP-PDR-54: "independent reviewer for
# the ADR with SA (it constrains safety-critical components)"). Dispatch: 07 section 2.1.1 row "Trade
# studies and ADRs whose decision constrains a safety-critical or mission-critical component of section
# 14.1", safety-critical column Yes; rules C4 and C7 of the PDR work plan.
# Checklist applied: docs/templates/peer-review-checklist-software-assurance.md revision A AS ON ITS CR-012
# BRANCH (cr/CR-012-pdr-checklist-templates at 7784672, blob 5b13528504868b2add0f0b1e329c63aa2b54cdf4; not
# merged: git merge-base --is-ancestor 7784672 main is false on 2026-09-29). tools/validate_docs.py fails a
# record whose `checklist` names a template absent from main, so the `checklist` field names
# peer-review-checklist-design revision B, the checklist 08 section 3.5 and 07 section 2.1.1 row 3 give ADRs
# (the INSP-066 form), and `assurance_checklist` names the template actually applied.
# id: INSP-131, pre-assigned by the lead SE brief; not used on main at HEAD ac9cd1a (highest INSP-118) or on
# any cr/ branch (git grep "^id: INSP-131", checked 2026-09-29).
# Record text returned to the lead SE for filing (the harness does not let subagents create new record files).
id: INSP-131
checklist: peer-review-checklist-design
checklist_revision: B
assurance_checklist: "docs/templates/peer-review-checklist-software-assurance.md@5b13528504868b2add0f0b1e329c63aa2b54cdf4 (revision A, branch cr/CR-012-pdr-checklist-templates at 7784672)"
checklist_file: docs/reviews/PDR/checklists/adr-056-to-059-software-assurance.md
# product: the four ADRs as one product set in docs/decisions/adr/ (the INSP-066 form for a set of ADRs);
# INSP-130 sets the product path of the pair and this record follows it at iteration 2 (cross item X-1)
product: docs/decisions/adr/
# product_commit and product_files (iteration 3): the second fix round commit 82f1df8 (main, not pushed) edits
# ADR-056, ADR-058 and ADR-059 in place; ADR-057 is unchanged since 03e3aea. Every blob equals git rev-parse
# 82f1df8:<path>, git rev-parse HEAD:<path> and git hash-object <path> at HEAD 82f1df8 (checked 2026-09-29, 4 of 4);
# 82f1df8 touches the three edited files only. The iteration 1 and 2 pins are kept below
product_commit: "82f1df85de881a7d7fd1a8d87af40b2cd76c432c"
product_files: ["docs/decisions/adr/ADR-056-a5-hand-built-design.md@c66b4c63a9bcf45bfbdb095e1902e08730149405", "docs/decisions/adr/ADR-057-2m-only-rev-a-70cm-ready-a5.md@5d9b8fc230e000debe725f933e47273795057936", "docs/decisions/adr/ADR-058-pico2-module-micro-usb-firmware-only.md@9a2302de4dc74c08b636bcd5b2443473df33b61d", "docs/decisions/adr/ADR-059-2s-18650-holders-external-charging.md@f988ffde42724fb651056b459da84a8fe0bf5fd6"]
# iteration 2 pin: the first fix round commit 03e3aea edited the four ADRs in place
product_commit_iteration_2: "03e3aeade507a716bf874ac82f82cee244f59cb8"
product_files_iteration_2: ["docs/decisions/adr/ADR-056-a5-hand-built-design.md@b7cbd40c8fffa5cf168260896c7ad373344ecf9c", "docs/decisions/adr/ADR-057-2m-only-rev-a-70cm-ready-a5.md@5d9b8fc230e000debe725f933e47273795057936", "docs/decisions/adr/ADR-058-pico2-module-micro-usb-firmware-only.md@308500562c6fd5b2ee99a777ccca46b2c3706296", "docs/decisions/adr/ADR-059-2s-18650-holders-external-charging.md@713cccc014ed40a6f15ac93b7bded6d7680aa4f1"]
# iteration 1 pin: ADR-057 to ADR-059 filed at 8a24bc6; ADR-056 last changed at abe5706 and unchanged at 8a24bc6
product_commit_iteration_1: "8a24bc65a9f14337a0dbb5e34257f940619a76c2"
product_files_iteration_1: ["docs/decisions/adr/ADR-056-a5-hand-built-design.md@5636f4774ad54fbc9ea20261c36c5272d86b04a9", "docs/decisions/adr/ADR-057-2m-only-rev-a-70cm-ready-a5.md@c4ba923ade7f06a27fa75fd97f89afa7b13ba463", "docs/decisions/adr/ADR-058-pico2-module-micro-usb-firmware-only.md@3b8bbd79e25423c70a3e420145ed07ab01060a5e", "docs/decisions/adr/ADR-059-2s-18650-holders-external-charging.md@9961bd9edd0a482d91d1a3fc8cab4205a82c1384"]
# inputs read (not reviewed), blobs at HEAD ac9cd1a
input_files: ["docs/decisions/trade-studies/TS-012-design-to-cost-hand-built.md@b9333386 (revision 8 at bb5dee7: sections 8.1, 8.3 rows 12, 19, 21 to 27, 8.7, 8.10, 8.14 D-6, D-18)", "docs/reviews/PDR/checklists/ts-012-design-to-cost-software-assurance.md@cd571469 (INSP-118 iteration 3: finding-4 to finding-11, X-14)", "docs/reviews/PDR/checklists/ts-012-design-to-cost.md@eda9a782 (INSP-110: finding-24, 25, 27)", "docs/safety/hazards.json@81cacde4 (0.5.0-pha: HZ-002, 003, 004, 005, 007, 008, 009, 011, 014, 015)", "docs/process/07-software-engineering-plan.md@bfe05f43 (sections 2.1.1, 14.1, 14.2)", "docs/requirements/sys/requirements.json@f128235e (REQ-SYS-067, 071, 076, 077, 083, 084, 086 to 088, 090, 092, 093, 097 to 101, 130, 149, 166, 186)", "docs/decisions/adr/ADR-002@b1852fd5, ADR-004@cee1bfef, ADR-005@082da0f9, ADR-009@efa2d0c0, ADR-013@3e036ff9, ADR-015@d165dfda, ADR-020@2e877185, ADR-026@68b998a9 (section 2 and consequences)", "docs/decisions/adr/README.md@f88ff242 (rules 1 to 6)", "docs/templates/adr.md@d5f1b485", "docs/plan/pdr-work-plan.md@fd521750 (WP-PDR-54, rules C1, C2, C4, C7, C10)", "docs/plan/status/status-2026-09-29.md@cdcf2597 (sections 4 and 5, owner's words)", "docs/cm/cr/CR-003-solution-neutral-enclosure.md@fb540367 (revision 4 section 1.1a)", "docs/design/analysis/pa-permit-gate-d18.md@a6bcc2b1 (revision 1 at c397ab1: summary and section 2 only; not reviewed here)", "git log -1 --format=%B for 66f6123, abe5706, 8a24bc6, c397ab1"]
input_files_iteration_2: ["git diff 8a24bc6 03e3aea -- docs/decisions/adr (194 insertions, 82 deletions)", "git log -1 --format=%B 03e3aea", "docs/decisions/trade-studies/TS-012-design-to-cost-hand-built.md@b9333386 (section 8.3 row 12; section 8.10 power rows)", "docs/safety/hazards.json@81cacde4 (HZ-003 K2 and K6, HZ-004 K1, HZ-005 K5 and K6, HZ-007 K3 and K4, HZ-011 K4; every control that names the LCD or display)", "docs/process/07-software-engineering-plan.md@bfe05f43 (section 14.1 frequency verification unit row; section 14.2 rows h, i, j)", "docs/plan/pdr-work-plan.md@fd521750 (rule C1; WP-PDR-24 at S2; OD-40 at S1)", "docs/research/power-tree-and-charging.md (F18, F22)", "scratchpad draft of INSP-130 iteration 1 (front matter and findings list)"]
input_files_iteration_3: ["git diff 03e3aea 82f1df8 -- docs/decisions/adr (61 insertions, 38 deletions in 3 files)", "git log -1 --format=%B 82f1df8", "docs/safety/hazards.json@81cacde4 (control_req_ids of every requirement named in ADR-056 section 4.1; texts of HZ-001 K4 and K8, HZ-003 K2 and K6, HZ-004 K1, K3, K7 and K11, HZ-006 K4, HZ-009 K6, HZ-011 K6, HZ-012 K1, K4, K5 and K6, HZ-013 K2, HZ-014 K2 and K3)", "docs/process/07-software-engineering-plan.md@bfe05f43 (section 14.1 frequency verification unit row; section 14.2 rows b, d, e, h, i, j and the SW-PWR and frequency verification module rows)", "docs/design/analysis/frequency-budget.md@28c29b8a (section 3.3, route R3 and T = 5.0 kHz)", "docs/design/analysis/pa-drive-ts012.md@02852058 at HEAD (open-loop output at 8.4 V; the HZ-001 note)", "docs/decisions/trade-studies/TS-012-design-to-cost-hand-built.md@b9333386 (section 8.10 rows REQ-SYS-029 and 031; D-9; D-17)", "docs/requirements/sys/requirements.json@f128235e (REQ-SYS-029, 031)", "docs/plan/pdr-work-plan.md@fd521750 (OD-10 part 2 at S2)", "scratchpad draft of INSP-130 iteration 2 (front matter)"]
paired_record: INSP-130
product_type: trade-study-or-adr
# criticality: safety-critical. The four ADRs fix the hardware and the software scope of 07 section 14.1
# components: SW-PWR (battery supervision: ADR-058 and ADR-059 remove its charging side and restate its
# discharge side), SW-TXSEQ and the SW-SAFE PA-permit flag (the PA_EN permit D-18, ADR-056 item 1 and item 3),
# the SW-SAFE thermal unit (the REQ-SYS-118 inhibit, ADR-056 section 4.1), the frequency verification unit
# (route R3, D-17), SW-AUDIO (the audio chain of ADR-056 item 3) and the Proposed menu override command path
# (ADR-056 section 4.3)
criticality: safety-critical
product_size: "iteration 3: delta of 61 inserted and 38 deleted lines in 3 ADRs (ADR-056 347 lines, ADR-058 142, ADR-059 177; ADR-057 128, unchanged) in one commit (82f1df8), every hunk read. Iteration 2: 4 ADRs, 771 lines (ADR-056 326, ADR-057 128, ADR-058 141, ADR-059 176); delta of 194 inserted and 82 deleted lines in one commit (03e3aea), every hunk read. Iteration 1: 4 ADRs, 659 lines (ADR-056 232, ADR-057 125, ADR-058 139, ADR-059 163); 3 product commits; assurance lens on 7 component groups of 07 section 14.1, 10 hazards of hazards.json 0.5.0-pha (HZ-002, 003, 004, 005, 007, 008, 009, 011, 014, 015), 27 requirement rows of the section 4.1 tables, the 3 lead SE rulings of ADR-056 section 7, 5 author-flagged items and INSP-118 finding-4 to finding-11"
sprint: PDR-prep
author_agent: "author:WP-PDR-54 (Claude as technical data manager, invocations of 2026-09-29: ADR-056 at 66f6123 and abe5706; ADR-057 to ADR-059 at 8a24bc6; the fix round of all four at 03e3aea; the second fix round of ADR-056, 058 and 059 at 82f1df8)"
reviewer_agent: "sa-reviewer:WP-PDR-54-adrs"
assurance_required: true
assurance_reviewer_agent: "sa-reviewer:WP-PDR-54-adrs (software assurance function; paired file review INSP-130 by its independent reviewer invocation of WP-PDR-54)"
iteration: 3
# readiness_met: R1 to R4 hold at iteration 3 (R1: 4 blobs frozen at 82f1df8 and equal at HEAD; R3: validate_docs.py
# 117 passed, 0 failed at HEAD; traceability.py 0 violations; R4: INSP-130 in progress under its own invocation)
readiness_met: true
# reviewer_verdict and assurance_verdict: APPROVED since iteration 2 (finding-1, the one Major, verified). At
# iteration 3 finding-5, finding-9 and finding-10 are verified; finding-4 stays open in part (one item, the
# REQ-SYS-087 transmit-arm prerequisite of 07 section 14.2 rows e and h), a Minor lien under rule C1
reviewer_verdict: APPROVED
assurance_verdict: APPROVED
# verdict: set by Claude as software lead (07 section 10.2); held at NEEDS CHANGES while INSP-130 has no APPROVED
# verdict (its iteration 2 draft is NEEDS CHANGES; its finding-2 waits on the lead SE ruling on ADR-056 item 4)
# and while CR-012 is not merged (lead SE convention of 2026-09-27)
verdict: NEEDS CHANGES
findings_major: 1
findings_minor: 9
findings_open: 1
findings_fixed: 0
findings_verified: 9
findings_deferred: 0
assurance_findings_major: 1
assurance_findings_minor: 9
assurance_tasks_applied: ["swe-134 7.1 task 5", "swe-022 7.1 task 1", "swe-033 7.1 task 1", "swe-033 7.1 task 2", "swe-033 7.1 task 3", "swe-039 7.1 task 4", "swe-057 7.1 task 2", "swe-134 7.1 task 4", "swe-134 7.1 task 6", "swe-205 7.1 task 1", "swe-205 7.1 task 3", "swe-080 7.1 task 1", "swe-080 7.1 task 2", "swe-081 7.1 task 2", "swe-086 7.1 task 1", "swe-087 7.1 task 2", "swe-089 7.1 task 1"]
swe134_items_checked: [a, b, c, d, e, f, g, h, i, j, k, l]
deferred_rids: []
items_no: ["swe-205 7.1 task 3", SA-D2]
items_no_iteration_2: ["swe-039 7.1 task 4", "swe-134 7.1 task 6", "swe-205 7.1 task 3", SA-D2, SA-D6]
items_no_iteration_1: ["swe-039 7.1 task 4", "swe-057 7.1 task 2", "swe-134 7.1 task 4", "swe-134 7.1 task 6", "swe-205 7.1 task 1", "swe-205 7.1 task 3", "swe-080 7.1 task 1", "swe-087 7.1 task 2", SA-C-a, SA-C-d, SA-C-f, SA-C-g, SA-C-i, SA-C-j, SA-D1, SA-D2, SA-E1]
effort_turns: 106
effort_minutes: 190
record_status: Open
date: 2026-09-29
date_closed: null
---

# Peer review record INSP-131: software assurance pair of INSP-130, ADR-056 to ADR-059 (the A5 decision and the restatements of ADR-002, ADR-004 and ADR-005)

**Product (iteration 1 pin; the iteration 2 pin at `03e3aea` and the iteration 3 pin at `82f1df8` are in their own sections).** Four Proposed ADRs in `docs/decisions/adr/`:

| ADR | Blob | Last commit | Lines | Decision |
|---|---|---|---|---|
| ADR-056 | `5636f477` | `abe5706` (created `66f6123`) | 232 | The owner's A5 decision (item 1) and the S1 items 2 to 4: TS-001 and TS-007 superseded, five studies not written, SWR fold-back closed on ruggedness; section 7 lead SE rulings on the contradicted ADRs |
| ADR-057 | `c4ba923a` | `8a24bc6` | 125 | Restates ADR-002 (2 m only, 70 cm-ready) with the brass-class SMA jack and no 70 cm LO criterion |
| ADR-058 | `3b8bbd79` | `8a24bc6` | 139 | Restates ADR-004 (Pico 2, its micro-USB) with the charge path removed |
| ADR-059 | `9961bd9e` | `8a24bc6` | 163 | Restates ADR-005 (2S 18650 in holders) with the A5 power tree and charging outside the radio |

Each blob equals `git rev-parse 8a24bc6:<path>`, `git rev-parse HEAD:<path>` and `git hash-object <path>` at HEAD `ac9cd1a`. No commit after `8a24bc6` touches `docs/decisions/adr/`. **Paired record:** INSP-130, the independent review of the same four ADRs, in progress under its own invocation. It is not on `main` at `ac9cd1a`, so its blobs and findings could not be compared (cross item X-1).

**Checklist.** `docs/templates/peer-review-checklist-software-assurance.md` revision A as on its CR-012 branch (`7784672`, blob `5b135285`). Applied: readiness R1 to R4, sections A to F, the section B row `trade-study-or-adr` and the row "Every product type", plus the section 7.1 tasks of the other SWEs these decisions touch. The template is branch-only; the front matter explains the `checklist` field.

**Assurance lens (the brief).**
- The decisions these ADRs fix for the components of 07 section 14.1:
  - `SW-PWR`;
  - the `PA_EN` and keying controls (`SW-TXSEQ`, the `SW-SAFE` PA-permit flag, D-18);
  - the thermal inhibit (`SW-SAFE` thermal unit, REQ-SYS-118, with the REQ-SYS-181 backstop);
  - the charge-path removal of ADR-058;
  - the balancing and protector changes of ADR-059.
- The hazard lines against `docs/safety/hazards.json` 0.5.0-pha: HZ-002, HZ-003, HZ-004, HZ-005, HZ-007, HZ-008, HZ-011, HZ-014 and HZ-015, with HZ-009 for ADR-057.
- Whether INSP-118 finding-9 to finding-11 are carried. INSP-118 cross item X-14 asks this review to carry finding-4 to finding-11.
- The five items the author flagged, (a) to (e), assessed under the same lens.

**Acceptance criteria (rule C7).**
- Every task of the section B rows `trade-study-or-adr` and "Every product type" is in the task table. So are the tasks of the other SWEs these decisions touch:
  - hardware changes that feed safety-critical units (swe-080 task 1);
  - Record-class items and hazard data under configuration management (swe-080 task 2, swe-081 task 2);
  - the risk entries the ADRs send (swe-086 task 1);
  - the accepted INSP-118 findings (swe-087 task 2);
  - the measurements (swe-089 task 1);
  - the software contributions by action, inaction and incorrect action (swe-205 task 1).
- Every SWE-134 item that 07 section 14.2 allocates to `SW-PWR`, `SW-TXSEQ`, the `SW-SAFE` units (thermal, safe-state manager with fault annunciation, frequency verification), `SW-AUDIO` and the Proposed menu override command path is checked at ADR maturity. The check: the decision recorded neither precludes the provision nor claims it without support.
- Each firmware function that an ADR says "stays" is checked against the hardware the same ADR fixes (TS-012 section 8.1 and 8.3, as adopted by ADR-056 item 1). The ADR's summary is not taken as the evidence.
- Each hazard line is checked control by control against `hazards.json`. A control is checked as removed, kept or changed, and for a lost object or a lost actuator.

**Independence (rule C4).** This invocation authored no part of ADR-056 to ADR-059, of TS-012 (any revision), of the old ADRs, of INSP-110, INSP-118 or INSP-130, or of `pa-permit-gate-d18.md`. It is neither the author (`author:WP-PDR-54`) nor the file reviewer of INSP-130. It edited no product file and no record in the repository.

**Search first.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (query: software assurance review checklist record ADR INSP validation). `grep`, `sed`, `git` and short Python reads of the JSON files were used afterwards only to pin lines in known files and to read the hazard controls and requirement statements. The brief names `docs/hazards/hazards.json`. That path does not exist; the hazard file is `docs/safety/hazards.json`, which the four ADRs cite correctly (cross item X-9). The rustos repository was not read. LTspice was not run. Nothing was downloaded.

## Findings (iteration 1)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | assurance (the lens raises the severity of author item (e) and extends it from REQ-SYS-099 to REQ-SYS-098 and REQ-SYS-166) | Major | `swe-134 7.1 task 6`, `swe-057 7.1 task 2`, `swe-080 7.1 task 1`, SA-C-a, SA-C-j, SA-D1 | ADR-059 section 2 paragraphs "Rails" and "Power switch"; section 4.1 rows "REQ-SYS-012, REQ-SYS-097, REQ-SYS-098" and "REQ-SYS-086, REQ-SYS-099, REQ-SYS-166"; section 4.3 paragraph "Safety-critical software scope"; ADR-056 section 2 item 1 "Power"; TS-012 section 8.1 "Power" line, section 8.3 rows 12, 19, 23, 25, section 8.10 row REQ-SYS-101 | **The A5 power tree as the ADRs record it gives no commanded path that removes power from the loads. Three HZ-007 controls of `SW-PWR` therefore have no actuator, and ADR-059 tells the owner that they stay.** ADR-059 section 4.3 says the discharge side of `SW-PWR` stays: "rail enable on the cell-voltage window, the transmit-inhibit and power-down thresholds, the cell over-temperature lockout". The hardware the same ADR fixes is as follows. "A mechanical power switch (E-Switch EG1218) drives the gates of the rail P-FETs" (section 2). The LM2940-5 LDO has no enable input, where ADR-005's buck had one (D13). The cell NTC's 60 C trip "clamps the transmitter". TS-012 section 8.10 row REQ-SYS-101 says the EG1218 "drives the rail P-FET gates that remove power". No section of TS-012 or of the ADRs names a controller or comparator output on those gates. BOM row 12 lists one 2N3904 use as "rail-off", but no text says what drives it or which rails it removes. Three L1 requirements need such a path. REQ-SYS-098: "power down its loads when either cell reads below 3.00 V". REQ-SYS-099: "power down its loads when its cell-sensor temperature exceeds 60 C". REQ-SYS-166: "keep its regulated rails off while either cell reads outside 2.5 V to 4.3 V". These are HZ-007 K4 (soft cut-off and 60 C lock-out) and K3 (firmware enables the rails only after both cells read in window). They are also the 07 section 14.2 `SW-PWR` provisions: row a "rail enable on the cell-voltage window" at first start, and row j "battery under-voltage to power-down within 1 s". HZ-007 is Catastrophic. Its `single_point_failures` entry says that for a shorted protector FET pair "nothing in hardware backs over-discharge except the firmware soft cut-off". With no rail-off actuator, the S-8252AAO FET pair becomes an unbacked single point for over-discharge. As drawn, the rails also come up with the switch before any cell is read, which REQ-SYS-166 forbids. ADR-059 section 4.1 crosses only REQ-SYS-099 to WP-PDR-24. It says REQ-SYS-097 and 098 "stay", and it gives REQ-SYS-166 no note. ADR-020's run "to the low-battery cutoff" rests on the same REQ-SYS-098. HZ-007 K4 also reads the cell temperature "through the charger TS input", which A5 does not fit. **Why Major:** SWE-134 items that 07 section 14.2 allocates to `SW-PWR` (a, h, j, l for HZ-007) have no provision in the decided design, and the ADR claims them. The owner would confirm ADR-059 at S1 (OD-10 part 1) on that claim. **Fix (either route, cents or a CR):** (1) In ADR-059 section 2 "Rails" and "Power switch", state a commanded rail-off path. For example: an N-channel FET or the row 12 2N3904, driven by a controller GPIO and by the LM393 #2 cell 60 C output, that pulls the rail P-FET gates to their source, wired-OR with the EG1218, and latched off until the switch is cycled (the controller removes its own supply). State the order at power-on, so that the rails reach the loads other than the controller only after both cells read in window, or record the reading of REQ-SYS-166 that CR-008 proposes. (2) Or propose REQ-SYS-098, 099 and 166 deltas to CR-018, and put the HZ-007 residual (the protector FET pair as the only over-discharge layer; loads left powered at a 60 C cell) to the owner as SMA TA. (3) In either case correct the section 4.3 `SW-PWR` list and the two section 4.1 rows. (4) Route to WP-PDR-24 (pack protection and the TS-005 remnant), WP-PDR-16 (HZ-007 K3, K4 and the single-point entry), WP-PDR-17 and WP-PDR-37 (cross item X-2) | Open | Pending | |
| <a id="finding-2"></a>finding-2 | assurance (INSP-118 X-14) | Minor | `swe-087 7.1 task 2`, SA-E1, SA-C-a, SA-C-d, SA-C-f, SA-C-g, SA-C-i | ADR-056 section 2 item 1 ("D-18 is the PA_EN permit, with its open lien"; "D-1 to D-18 ... at their A5 values"); section 2 item 3 row TS-006; section 4.1 row REQ-SYS-112, REQ-SYS-118; sections 4.2 and 4.3 ("PA_EN written only by the safe-state manager"); ADR-058 section 4.2 ("VBUS reaches only the hardware transmit inhibit on the clamp node"); ADR-059 section 2 ("clamps the transmitter") | **ADR-056 does not carry the open INSP-118 liens. Later work cites the ADR, not TS-012, so the liens drop out of the record chain.** (a) finding-9, the D-18 level interface, unpowered state and fallback timing, appears only as "with its open lien", with no id, no content and no due event. Item 3 decides TS-006 by a "PA_EN permit NAND ... driving the VGG clamp FET and the GVA-84+ supply P-FET". The WP-PDR-22 fix record `pa-permit-gate-d18.md` replaces the NAND with an AND and open-collector stages (`078f2f7`). Its revision 1 (`c397ab1`, commit message; not reviewed here) answers two Major findings of its own review and SA pair. It moves the REQ-SYS-180 backstop, the REQ-SYS-181 95 C trip, the cell 60 C trip and the REQ-SYS-092 VBUS inhibit from the VGG node onto the gate's Q node. The reason given is that on VGG, as TS-012 section 8.1 draws them, these cutoffs leave the driver powered (about -10 to -15 dBm against the -57 dBm RF-off level). ADR-056 item 1, ADR-058 section 4.2 ("the clamp node") and ADR-059 section 2 fix the pre-fix wiring. (b) finding-10 is not carried. TX_KEY and PA_EN are bits of one SIO register, and sections 4.2 and 4.3 repeat "written only by the safe-state manager", which does not answer one wrong register store. The HZ-004 K8 line names "PA_EN and the D-18 NAND" only. (c) finding-11 is not carried. Item 1 adopts D-6 "at its A5 values", and D-6 includes "a firmware duty limit on the sink NTC (79.4 C A5)". The only sink NTC in the BOM is the REQ-SYS-181 backstop's (row 26), and section 4.1 names only the flange NTC. (d) finding-4 (ADC shortfall and channel identity), finding-5 (setpoint and duty-limit wording of REQ-SYS-118), finding-6 (ALT-hold without confirmation), finding-7 (stored keying data not guarded) and finding-8 (lead SE part) are not named either, nor are INSP-110 finding-24, 25 and 27. Hence SA-C-a, d, f, g and i are No at ADR maturity. Each lien is Minor, and the hazard stays controlled by the clamp, so Minor. **Fix:** (1) Add a paragraph to ADR-056 section 4.3, "Open review liens carried by this decision", listing INSP-118 finding-4 to finding-11 and INSP-110 finding-24, 25 and 27, each with its owner WP and due event. (2) In item 1 and in the item 3 TS-006 row, state D-18 and the hardware cutoffs by function ("RF needs TX_KEY and PA_EN; each hardware cutoff ends RF to the REQ-SYS-183 level independently of firmware"), not by gate type or node. Name `pa-permit-gate-d18.md` as the governing record once its review and SA pair are APPROVED (cross item X-6). (3) State in section 4.1 that the duty-limit form of D-6, if chosen, uses its own NTC, separate from the REQ-SYS-181 thermistor. (4) Carry the same wording into ADR-058 section 4.2 and ADR-059 section 2 | Open | Pending | |
| <a id="finding-3"></a>finding-3 | assurance | Minor | `swe-134 7.1 task 6`, `swe-080 7.1 task 1`, SA-D3 | ADR-058 section 1 "Hazards in play" (HZ-011), section 2 (second paragraph), section 1 assumption 1, section 4.1 row REQ-SYS-090, section 4.3 (HZ-011 line); ADR-059 section 2 "Rails" | **The USB power path of the controller is not stated. As a result, one HZ-011 control and one assumption rest on an element that neither ADR names, and the ADR's K4 reading would orphan REQ-SYS-090.** (a) ADR-058 says "VBUS is used on the board only to sense USB presence for the hardware transmit inhibit". The Pico 2 module has its own VBUS-to-VSYS diode (`hazards.json` HZ-011 C4 names "the Pico 2 connector, D1 diode and VBUS copper"). ADR-005 fed VSYS from the 5 V buck. ADR-059 drops the buck and does not say what feeds VSYS. If the LM2940-5 output joins VSYS directly, USB with the cells removed powers the whole 5 V bus: receiver, prescaler, relay drive and the GVA-84+ rail switch. Then REQ-SYS-149 (transmitter supply below 0.5 V from USB alone; HZ-011 K3, HZ-014 K4) and assumption 1 ("the module is the only load on USB") depend on an element that is not recorded. The hazard stays controlled: the module drain comes only from the pack, and the D-18 pull-downs and the VBUS inhibit hold. Hence Minor. (b) ADR-058 section 1 says HZ-011 K4, "the charge input current limit", loses its object, and section 4.3 repeats this. K4's text has a second half: "the Pico 2 VBUS path current bounded by ... the 500 mA design limit" (PWR-USB-01, PWR-USB-02). REQ-SYS-090 is K4's only control requirement, and ADR-058 keeps it. If WP-PDR-16 retires K4 as written, REQ-SYS-090 (hazard_ids HZ-011) loses its control, and the hazard trace becomes one-way. **Fix:** in ADR-059 "Rails" and ADR-058 section 2, state how VSYS is fed: a Schottky or ideal diode from the 5 V bus into VSYS, so that VBUS cannot back-feed the bus. This is the Pico 2 datasheet's external-supply arrangement as the reviewer recalls it, not re-read (Low); WP-PDR-24 confirms it. Name HZ-011 K3 and REQ-SYS-149 in ADR-058 sections 4.1 and 4.3. Restate the K4 line as "K4 keeps its REQ-SYS-090 half; its charge-limit half loses its object". Route to WP-PDR-24 (TS-005 remnant) and WP-PDR-16 (cross item X-3) | Open | Pending | |
| <a id="finding-4"></a>finding-4 | assurance | Minor | `swe-205 7.1 task 3`, SA-D2, SA-C-g | ADR-056 section 4.3 "Safety-critical software scope"; ADR-058 section 4.3 (same row); ADR-059 section 4.3 (same row); section 4.1 of ADR-058 and ADR-059 (no REQ-SYS-130 row) | **The ADRs move component scope but name only the WP-PDR-17 determination re-run. They do not name the 07 section 14 rows and the L1 safe-state requirement that their decisions make stale.** 07 section 14.1 is "the single authoritative component list" and is changed by CR. At the reviewed blob `bfe05f43` it still carries the following. (1) The `SW-PWR` row and module row: charger status, dual dissimilar sensing (REQ-SYS-088, retired), charge disable, charge-state watchdog, the charge pause (HZ-011 K2), and "the GPIO24 VBUS reading against the charger's VBUS status", whose comparison partner A5 removes. (2) Rows a, c and l of 14.2 and REQ-SYS-130 ("... audio muted and charging disabled"); REQ-SYS-130 appears in no section 4.1 table and not in TS-012 section 8.10. (3) Row e: charge enable prerequisites. REQ-SYS-087 becomes "refuse to arm transmit" (ADR-059 section 4.1), a new `PA_EN` or Arm prerequisite that the row h list does not hold. (4) Row g: "cell voltages on two dissimilar paths (REQ-SYS-088)". The firmware discharge monitor becomes single-path, and REQ-SYS-186 is reworded. (5) Row i: "the charger IC and the independent cell over-voltage protector". (6) Row j: "charge disable within one supervision period", and "PA over-current or reflected-power fault, if the PDR design senses it", which lapses with ADR-056 item 4. (7) The `SW-SAFE` thermal unit's "a reading above 85 C". REQ-SYS-118 moves to about 81 C at the flange NTC, or to the duty-limit form. (8) The frequency verification unit's "RP2350 crystal timebase, not the synthesizer reference". Route R3 counts the TCXO, which is the synthesizer's reference, to cancel the XOSC error (D-17). The INSP-118 finding-1 verification accepts R3, but the 07 row text no longer describes it. (9) `SW-DISPLAY`, which ADR-056 section 4.2 removes, is still named as the module of the menu override command path and of the mission-critical selection path. None of these is a new hazard, so Minor. But 03 section 4.1 step 5 and 07 section 14.1 require the list to be re-transcribed in the change set that moves the scope. **Fix:** in ADR-056 section 4.3, and in the matching rows of ADR-058 and ADR-059, name as consequences: the 07 section 14.1 and 14.2 revision by CR (the rows above), carried with the WP-PDR-17 determination; and the REQ-SYS-130 rewording ("charging disabled" removed) in CR-018. Add REQ-SYS-130 to ADR-058 section 4.1, and the REQ-SYS-087 arm prerequisite to the row h list request (cross items X-4, X-5) | Open | Pending | |
| <a id="finding-5"></a>finding-5 | assurance | Minor | `swe-134 7.1 task 4`, `swe-057 7.1 task 2`, SA-C-k | ADR-056 section 4.2 ("The software architecture adds the Morse menu and decoder ..."; "SW-DISPLAY is removed"); section 4.3 (no fault-annunciation line) | **The fault annunciation of the safe-state manager changes medium with A5, and the ADR does not keep it apart from the Morse menu.** 07 section 14.1 places fault annunciation in `SW-SAFE` as "the fixed fault screen and cause messages, REQ-SYS-067, which do not pass through menu or UI rendering (03 section 4.3)". This is the isolation that SWEHB `swe-134` 7.1 task 4 b asks for. With A5, REQ-SYS-067 becomes "announce a distinct cause in Morse within 1 s (headphones) and an LED blink code" (TS-012 section 8.10). The only Morse sender in the design is the menu's (TS-012 section 8.7; section 8.1 "PWM audio (sidetone + Morse menu)"). ADR-056 section 4.2 adds "the Morse menu and decoder" and says nothing about where the cause announcement and the LED code are generated. The same operator indications are display-based in the controls: HZ-004 K1 ("the LCD shows 'KEY CLOSED: check plug'"), HZ-002 K4, HZ-003 K2 ("fault shown on the LCD"), ADR-009 section 2 (the key-closed message) and ADR-015 (lock state on the display). A menu fault that silences or garbles the cause announcement is an incorrect action on a safety-critical path. The hazards stay controlled, because the inhibits act whatever is announced, so Minor. **Fix:** state in ADR-056 section 4.2 that the Morse cause announcement and the LED code are generated by the `SW-SAFE` fault annunciation unit, from its own tone and LED drivers (or a sender unit of that component), and do not pass through the menu units. Route to WP-PDR-32 and WP-PDR-35 (unit placement), WP-PDR-17 (determination) and WP-PDR-16 (the "LCD" wording of HZ-002 K4, HZ-003 K2 and HZ-004 K1) (cross item X-8) | Open | Pending | |
| <a id="finding-6"></a>finding-6 | assurance | Minor | `swe-205 7.1 task 1`, `swe-134 7.1 task 6`, SA-D1 | ADR-056 section 4.3 "Hazard analysis update required" (the HZ-005, HZ-008 and HZ-015 lines); section 4.1 (no REQ-SYS-076 or 077 row); section 2 item 3 row TS-010 | **The hazard lines of ADR-056 section 4.3 miss controls that A5 removes or changes.** (a) HZ-005. The line says only "every menu tone passes through the capped sidetone path". Controls K5 ("amplifier enable pulled down in hardware and asserted by firmware only after the audio source has idled at mid-scale ... de-asserted on brown-out or fault") and K6 ("the amplifier is shut down with no headphones") need an amplifier with an enable or shutdown input. Item 3 decides the audio chain as "NE5532 and MCP6002 on the 5 V bus with a capped attenuator". TS-012 section 8.1 draws "MCP6002 L/R -> 220 uF -> atten -> jack", and the MCP6002 has no shutdown input. REQ-SYS-077 ("disable the headphone amplifier output while no plug is inserted") and REQ-SYS-076 (transients at power-on and plug insertion below 10 mV peak into 32 ohm) are therefore not shown, and neither is in section 4.1 or TS-012 section 8.10. Reviewer estimate (Low): the 220 uF capacitor charging to mid-rail, about 2.5 V, through k of about 0.06 gives a step of about 150 mV at the jack, against 10 mV. K5 is also a `SW-AUDIO` actuator (row a start-up ramp, row j fault mute). The K1 ceiling still bounds the sustained level, so Minor. (b) HZ-008. The line names K7 only. K2 names TS-001's PD54008L-E and ADR-012. K3's "firmware over-voltage lockout above about 8.6 V" is not placed in A5. K6's "5 V buck synchronised to a firmware-set frequency" loses its object with the LDO. (c) HZ-015. K3 limits hand assembly to "through-hole parts and exposed-pad modules ... with every hidden-pad and fine-pitch part placed by PCBWay (SI-031, ADR-007)". ADR-056 retires REQ-SYS-137 and supersedes ADR-007, so K3 loses its basis, not only gains a heat gun. (d) HZ-002. The `firmware_role` (charger supervision, criteria c and e) leaves firmware, which changes the 07 section 14.1 union for `SW-PWR` (finding-4). **Fix:** add these lines to ADR-056 section 4.3 for WP-PDR-16. Add REQ-SYS-076 and REQ-SYS-077 to section 4.1 as "at risk; WP-PDR-25 shows them or proposes a delta by CR-018". Name the HZ-005 K5 and K6 re-design (an amplifier or buffer stage with a shutdown or mute path, or a jack-switched series element) as a WP-PDR-25 item (cross item X-3) | Open | Pending | |
| <a id="finding-7"></a>finding-7 | assurance (author item (d), assessed) | Minor | `swe-080 7.1 task 1`, `swe-134 7.1 task 6` | ADR-056 section 7, "Not contradicted, and they stay: ADR-013 and ADR-023", and the three rulings | **Section 7 lists no Accepted ADR other than ADR-002, 004 to 008, 012 and 025 as contradicted. A5 contradicts the decision text of at least seven more in part, three of them on safety-relevant content.** (1) ADR-013 section 2 sets the synthesizer method: the mandatory criterion "turnkey stock at CDR per ADR-012", the enhancing criterion "70 cm LO coverage (ADR-002)" and the owner's USD 15 cost-band rule. TS-012 applied none of these as its method (section 3.1, C1 to C8). ADR-013 section 4.3 also requires "HZ-008 cause C8 is re-assessed for the chosen part"; ADR-056 section 4.3 does not carry that for the Si5351A. (2) ADR-009 section 2: "otherwise the display shows a key-closed message", the operator indication of HZ-004 K1. (3) ADR-015 section 2: "the lock state is shown on the display", the guest lock of HZ-006. (4) ADR-020: "receiving with the display on", the 3000 mAh basis, and a run that ends at the REQ-SYS-098 cut-off (finding-1). (5) ADR-016 (CW segment "indicated on the display"), ADR-024 ("speed visible on the display") and ADR-026 ("the displayed speed"; the T/R element trade, which ADR-056 item 3 does not write as TS-008): display text only, no safety content. The TS-012 selection keeps the safety content of ADR-013 (HZ-008 K7 on route R3), ADR-009 (the interlock inhibits whatever is shown) and ADR-015 (the lock blocks `PA_EN`). So the assurance lens finds no weakened control, hence Minor. What is missing is the record: the route of each partial contradiction, under README rule 2, which has no partial supersession. That route is the lead SE's ruling, not this record's. **Fix:** extend ADR-056 section 7 with a ruling for each of ADR-009, 013, 015, 016, 020, 024 and 026 (restate as for ruling 2, or a reading note, as the lead SE decides). Carry ADR-013's HZ-008 C8 re-assessment into section 4.3 for WP-PDR-16 (cross item X-7) | Open | Pending | |
| <a id="finding-8"></a>finding-8 | assurance (author item (b); the lens adds the safety rows it sweeps) | Minor | `swe-039 7.1 task 4`, `swe-134 7.1 task 6` | ADR-056 section 4.1 row "REQ-SYS-081 to 093, 167, 185, 186 / retired, reallocated or reworded via CR-018"; next row "REQ-SYS-083, 084" | **The section 4.1 row that CR-018 is told to cite sweeps safety requirements that A5 keeps.** TS-012 section 8.10 keeps REQ-SYS-085 (discharge trip, HZ-007 K1, K2), REQ-SYS-090 (HZ-011 K4) and REQ-SYS-092 (hardware transmit inhibit with USB power: HZ-011 K1, HZ-014 K4, and a firmware-independent bound named in 07 section 14.2 row i), and ADR-058 section 4.1 keeps REQ-SYS-092 and 090. It records REQ-SYS-084 at risk. REQ-SYS-086 (reverse insertion, HZ-007 K3, K6) is not in section 8.10, and ADR-059 treats it as allocated. The ADR-056 row reads all of 081 to 093 as "retired, reallocated or reworded" and lists 083 and 084 again in the next row. A CR-018 author who follows ADR-056 as the cited source could retire REQ-SYS-092. The author flagged the over-breadth. The assurance point is that REQ-SYS-092 is the only firmware-independent USB inhibit. ADR-058 and TS-012 are correct, so Minor. If INSP-130 raises the same defect, this finding cites its id at iteration 2 (cross item X-1). **Fix:** split the row. Retired or reallocated: REQ-SYS-081, 082 (reallocated), 088, 089, 091, 093, 167, 185. Reworded: 083, 087, 186. Kept: 085, 090, 092, and 086 (not in section 8.10). At risk: 084. Mark REQ-SYS-092 "kept; HZ-011 K1, HZ-014 K4" | Open | Pending | |

One Major finding is open, so the assurance verdict is NEEDS CHANGES. The fix of finding-1 costs cents (one transistor on the rail gates and its latch) or needs a CR delta with an owner risk decision. Either way the owner must see it before confirming ADR-059 at S1. The other seven findings are record gaps or missing consequences with no weakened control in the decided design. The ADRs are Proposed and are fixed in place (README rule 2; each ADR's Status row), so these Minor findings are fixed now, not liened: this is iteration 1, and no APPROVED verdict has been given yet (rule C1).

### Task table

| Task | Safety-critical designation (SWEHB 8.10 section 6) | Applied | Result and evidence | Relief (N/A only) | Finding ids |
|---|---|---|---|---|---|
| swe-134 7.1 task 5 | SC | Yes | This record is the assurance participation in the review of a product that 07 section 2.1.1 routes (row "Trade studies and ADRs", safety-critical column Yes). WP-PDR-54 names it ("independent reviewer for the ADR with SA") | | none |
| swe-022 7.1 task 1 | SC | Yes | Performed against the project software assurance plan (07 section 15) with this template. The NASA-STD-8739.8 part is relieved (next column) | NASA-STD-8739.8 part: `rmm.json` SWE-022 T (standard not in the corpus) | none |
| swe-033 7.1 task 1 | | Yes | No software make-or-buy option arises. ADR-058 restates ADR-004's runtime unchanged ("Rust on `rustos` with zero external runtime crates (ADR-027)"), and TS-002 and ADR-027 keep the make/buy record. The XTAR MC1 charger is equipment outside the radio | | none |
| swe-033 7.1 task 2 | SC | Yes | No software acquisition activity exists, so no software requirement flows to a supplier | | none |
| swe-033 7.1 task 3 | | Yes | No software acquisition risk exists. The assurance concern of finding-1 goes to SA-F1 | | none |
| swe-039 7.1 task 4 | | No | The ADRs were assessed against their source data: TS-012 revision 8 sections 8.1, 8.3, 8.10 and 8.14, `hazards.json` 0.5.0-pha, the requirement statements, the old ADRs and the owner's words. The owner quotes match status note 2026-09-29 sections 4 and 5 verbatim. The discrepancies: ADR-059 section 4.3's `SW-PWR` claim is not supported by the power tree it fixes (finding-1); the ADR-056 section 4.1 row misreads TS-012 section 8.10 for kept safety rows (finding-8); ADR-058's K4 reading drops K4's REQ-SYS-090 half (finding-3) | | finding-1, finding-3, finding-8 |
| swe-057 7.1 task 2 | | No | The architecture the ADRs fix does not show REQ-SYS-098, 099 and 166 met (finding-1). It also gives the safe-state fault annunciation no place apart from the menu (finding-5) | | finding-1, finding-5 |
| swe-134 7.1 task 4 | SC | No | Isolation: the Morse cause announcement shares the menu's sender (finding-5). The analog-input shortfall of INSP-118 finding-4, which puts safety readings behind a shared selector, is not carried (finding-2 (d)) | | finding-2, finding-5 |
| swe-134 7.1 task 6 | SC | No | Consistency with the hazard analysis: HZ-007 K3 and K4 lose their actuator (finding-1); HZ-011 K4 is read as wholly lost (finding-3); HZ-005 K5 and K6, HZ-008 K2, K3 and K6 and HZ-015 K3 are not in the hazard lines (finding-6); the D-18 and duty-limit liens bearing on HZ-004 K8 and HZ-003 K2 and K9 are not carried (finding-2) | | finding-1, finding-2, finding-3, finding-6, finding-7, finding-8 |
| swe-027 7.1 task 1 | | N/A | Condition not met: no COTS, GOTS, MOTS, OSS or reused software is chosen. The 07 section 17.1 register is unchanged; ADR-058 section 5 restates it | Conditional task of the section B row ("reused or OSS component chosen"); 07 section 17.1 | none |
| swe-136 7.1 task 1 | | N/A | Condition not met: no software tool, emulator or model is selected by these ADRs | Conditional task of the section B row; 07 section 17.3 | none |
| swe-070 7.1 task 1 | | N/A | As swe-136: no model or simulation qualifies flight software or equipment here | Conditional task of the section B row; 07 section 17.3 | none |
| swe-205 7.1 task 1 | SC | No | `hazards.json` names software contributions that A5 changes without a hazard line. HZ-007 C9 and C10: the soft cut-off and the rails enabled outside the window now fail by design, not by firmware, because there is no actuator (finding-1). HZ-005 K5: firmware assertion of an amplifier enable that A5 does not fit (finding-6). The Morse fault announcement as an incorrect-action path (finding-5). The mechanisms that stay are carried: D-18 `PA_EN` (action), the FC0 check (incorrect action, route R3), the duty-limit option (inaction; finding-2 (c)) | | finding-1, finding-5, finding-6 |
| swe-205 7.1 task 3 | SC | No | The decisions move component scope: `SW-PWR` loses its charging side; `SW-DISPLAY` is removed; a Morse menu and decoder module is added; fault annunciation changes medium. The ADRs route the determination to WP-PDR-17 (OD-35 at S2), but not the 07 section 14 revision or REQ-SYS-130 (finding-4) | | finding-4 |
| swe-080 7.1 task 1 | SC | No | Hardware changes that feed safety-critical units were checked for software safety impact: the power switch and LDO (finding-1), the USB power path (finding-3), the audio buffer (finding-6) and the cutoff node (finding-2 (a)). The charge-path removal itself is sound: it removes HZ-002's firmware role and HZ-011 K2's object, and no control that stays depends on it | | finding-1, finding-2, finding-3, finding-6 |
| swe-080 7.1 task 2 | | Yes | Change route of the Record-class ADRs: `66f6123`, `abe5706` and `8a24bc6` each pass `tools/check_commit_msg.py` with a `Refs:` trailer (docs type, 05 section 4.5). Each touches only its ADR files. The ADRs are Proposed, and README rule 2 allows their review fixes in place | | none |
| swe-081 7.1 task 2 | SC | Yes | The four ADRs are on `main`. `hazards.json` stays row-controlled, with WP-PDR-16b as its single writer (plan section 5.3). The ADRs route changes to it and do not edit it | | none |
| swe-086 7.1 task 1 | | Yes | ADR-056 section 4.4 sends its risk rows to the WP-PDR-18 writer. ADR-058 proposes RSK-033 for retirement, which is correct on the charge-path removal. The finding-1 residual belongs with RSK-007 and HZ-007 (SA-F1) | | none |
| swe-087 7.1 task 2 | | No | The accepted INSP-118 findings 4 to 11 (and INSP-110 findings 24, 25 and 27) are liens on the design this ADR records, and ADR-056 does not carry them (finding-2) | | finding-2 |
| swe-089 7.1 task 1 | | Yes | This record carries the SWE-089 measurements (front matter and Measurements). INSP-130 carries its own | | none |

## Readiness criteria

| # | Criterion | Result | Evidence |
|---|---|---|---|
| R1 | Product committed and frozen; `product_files` equal to the paired record's | Yes (own pin) | `git rev-parse 8a24bc6:<path>`, `git rev-parse HEAD:<path>` (HEAD `ac9cd1a`) and `git hash-object <path>` give `5636f477`, `c4ba923a`, `3b8bbd79` and `9961bd9e`, 4 of 4 equal. `git log 8a24bc6..HEAD -- docs/decisions/adr` is empty. INSP-130 is not on `main`, so equality with its `product_files` is checked at iteration 2 (X-1) |
| R2 | Product type and criticality identified | Yes | 07 section 2.1.1 row 3 (`trade-study-or-adr`). Safety-critical by the 07 section 14.1 rows "Battery and charging supervision" (`SW-PWR`), "PA enable and TX sequencer", "Thermal protection", "Safe-state manager", "Audio limiter", "Frequency verification unit" and "Menu override command path" |
| R3 | `validate_docs.py` on the product's files; `traceability.py --report-only --output <scratch>` clean for the ids the product touches | Yes | `validate_docs.py`: "117 passed, 0 failed, 117 checked" at HEAD, and 118 of 118 in an export of HEAD `c16b787` with this record in place (Commands); the ADRs are not validator documents, and no record of them exists yet. `traceability.py --report-only --output <scratchpad>/adr-review/trace-insp131.md`: "245 requirements, 173 test cases, 0 violation(s), 2 warning(s)" (REQ-SYS-125 and 148, not touched by the ADRs); `docs/vv` unchanged. No requirement cites ADR-056 to ADR-059 yet; CR-018 adds them |
| R4 | Paired file review filed or in progress under its own invocation; this reviewer is neither author nor file reviewer | Yes | INSP-130 is dispatched by the lead SE as a separate invocation (brief). This record's `reviewer_agent` "sa-reviewer:WP-PDR-54-adrs" differs from `author:WP-PDR-54` and from the INSP-130 reviewer |

## A. Dispatch, independence and record integrity

| Id | Answer | Evidence |
|---|---|---|
| SA-A1 | Yes | 07 section 2.1.1 row 3, safety-critical column Yes; the components of R2. Each of ADR-056, 058 and 059 names `SW-PWR` or the 07 section 14.1 components in its Decision class row. ADR-057 is reviewed with them because it is filed in the same review (ADR-057 header, "The same review as ADR-056") |
| SA-A2 | Yes | Three distinct invocations: the author (`author:WP-PDR-54`), the INSP-130 reviewer and this assurance invocation. INSP-130 names this pair when it is filed (X-1) |
| SA-A3 | Yes (this record) | This record pins the four blobs of R1 at `8a24bc6`. INSP-130 is to pin the same blobs (X-1) |
| SA-A4 | N/A | INSP-130 is not filed at HEAD `ac9cd1a`, so its checklist use cannot be read. Checked at iteration 2 (X-1) |

## B. SWE-to-task table

| Id | Answer | Evidence |
|---|---|---|
| SA-B1 | Yes | The task table holds every task of the rows `trade-study-or-adr` and "Every product type", plus swe-205 task 1, swe-080 tasks 1 and 2, swe-081 task 2, swe-086 task 1, swe-087 task 2 and swe-089 task 1. `assurance_tasks_applied` lists the 17 Yes and No rows |
| SA-B2 | Yes | The three N/A rows (swe-027, swe-136, swe-070) are conditional tasks whose condition is not met, each with its 07 section. No SC task is N/A |
| SA-B3 | Yes | Each No row cites a finding |

## C. SWE-134 items a to l (ADR maturity: the decision neither precludes nor claims without support the 07 section 14.2 provision)

| Id | Answer | Evidence |
|---|---|---|
| SA-C-a | No | `SW-TXSEQ` and `SW-SAFE`: the TX_KEY and PA_EN pull-downs, the clamps on at reset and the relay's receive default hold RF off before firmware (ADR-056 item 1 via TS-012 section 8.1). The unpowered state of the D-18 gate (INSP-118 finding-9 (b)) is not carried (finding-2). `SW-PWR`: "rail enable on the cell-voltage window" at first start has no actuator; the rails come up with the switch (finding-1). "Charging disabled" at boot lapses (finding-4) |
| SA-C-b | Yes | No state or mode is added to the ConOps set. The Morse menu replaces display pages; the key-down sequence is TS-012 section 7.3's, unchanged |
| SA-C-c | Yes | Every termination path still ends in `safe_state()` with `PA_EN` first. The "charging disabled" step lapses (finding-4) |
| SA-C-d | No | The ALT-hold key-mode change without confirmation (INSP-118 finding-6) is not carried (finding-2 (d)). ADR-056 section 4.3 keeps the override path safety-critical |
| SA-C-e | Yes | No out-of-sequence command path is added. REQ-SYS-087 moves from a charge-enable prerequisite to a transmit-arm prerequisite (finding-4 (3)) |
| SA-C-f | No | The stored keying data of D-10 are not in the configuration guard's field list (INSP-118 finding-7), and this is not carried (finding-2 (d)). Observation O-1 (below) on ADR-057 point (1) |
| SA-C-g | No | Cell voltages become single-path, and the GPIO24 VBUS plausibility partner is removed (finding-4 (1), (4)). The ADC channel identity check of INSP-118 finding-4 is not carried (finding-2 (d)) |
| SA-C-h | Yes | The `PA_EN` prerequisites stay in one function (07 row h). The frequency check before `PA_EN` is carried on route R3 (D-17). The REQ-SYS-087 prerequisite is to be added to the list (finding-4 (3)) |
| SA-C-i | No | One SIO store can raise TX_KEY and PA_EN together (INSP-118 finding-10). The duty-limit option could share the REQ-SYS-181 thermistor (finding-11). Neither is carried (finding-2 (b), (c)) |
| SA-C-j | No | "Battery under-voltage to power-down within 1 s" (07 row j allocation) and the 60 C cell lock-out have no actuator (finding-1). The REQ-SYS-118 response time holds for the inhibit form but not for the duty-limit form (INSP-118 finding-5, not carried; finding-2 (d)) |
| SA-C-k | Yes | No error path is removed. The fault annunciation route is finding-5 |
| SA-C-l | Yes | `safe_state()` stays reachable from every state. The operator's power switch removes the loads (REQ-SYS-101 as interpreted) |

## D. Software safety analysis and hazard traceability

| Id | Answer | Evidence |
|---|---|---|
| SA-D1 | No | Contributions checked by action, inaction and incorrect action, with the SWEHB `swe-205` 7.7.2 considerations for control of hazardous hardware, interlocks, inhibits, cautions and warnings, and common-cause faults. Gaps: HZ-007 C9 and C10 (finding-1); HZ-005 K5 (finding-6); fault annunciation (finding-5); the one-sensor common cause of the duty-limit option (finding-2 (c)) |
| SA-D2 | No | The 07 section 14.1 list and criteria change with the charge-path removal (HZ-002 leaves `SW-PWR`), the display removal and the Morse menu. The ADRs route the determination to WP-PDR-17 but not the list re-transcription (finding-4) |
| SA-D3 | Yes | `traceability.py`: 0 violations at HEAD; no `HAZARD_CONTROL_UNTRACED` or `HAZARD_INVERSE`. The K4 reading of ADR-058 would create a one-way trace if applied as written (finding-3 (b)) |
| SA-D4 | N/A | The product holds no software requirement |
| SA-D5 | N/A | The product holds no hazard-tracing software requirement |
| SA-D6 | Yes | ADR-056 section 4.3 and ADR-058 and ADR-059 section 4.3 route the hazard update to WP-PDR-16 (0.6.0-pha) and the determination to WP-PDR-17. The content gaps of those lines are finding-1, finding-3 and finding-6 |

## E. Peer review, change and configuration assurance

| Id | Answer | Evidence |
|---|---|---|
| SA-E1 | No | The INSP-118 liens finding-4 to finding-11 are not carried by the ADR that records the design (finding-2) |
| SA-E2 | Yes | This record carries the SWE-089 measurements. INSP-130 carries its own |
| SA-E3 | Yes | `66f6123`, `abe5706` and `8a24bc6`: PASS with `Refs:` (Record class, 05 section 4.5). No `CR:` trailer is needed: the ADRs are Proposed records, and their requirement effects are carried by CR-018, CR-003 revision 4 and CR-006 revision 3 |
| SA-E4 | N/A | No test or code product |

## F. Assurance risks, metrics and reporting

| Id | Answer | Evidence |
|---|---|---|
| SA-F1 | Yes | No assurance concern outside the findings. The finding-1 residual, if route (2) is chosen, is an HZ-007 and RSK-007 matter for the owner as SMA TA, and is named there |
| SA-F2 | Yes | Front matter: findings by severity and state, `assurance_findings_major` 1 and `assurance_findings_minor` 7, `items_no`, effort |
| SA-F3 | Yes | Verdict, open findings, tasks applied and reliefs are in this record |

## The author-flagged items (a) to (e), assessed under the assurance lens

| Item | Author's statement | Assurance reading | Where carried |
|---|---|---|---|
| (a) | ADR-056 section 4.1 lists REQ-SYS-104 and 106 under CR-018, but their texts are in CR-003 revision 4 section 1.1a | Confirmed: CR-003 revision 4 section 1.1a (blob `fb540367`) drafts both, and ADR-057 section 4.1 says so. REQ-SYS-106 serves HZ-009 K2, which has no firmware role. No safety effect; this is INSP-130's lens | Not raised here |
| (b) | "REQ-SYS-081 to 093 retired or reworded" is broader than TS-012 section 8.10 | Confirmed. The sweep includes REQ-SYS-092, the only firmware-independent USB inhibit (07 row i), and 085, 086 and 090 | finding-8 |
| (c) | ADR-057 adds ADR-002 item (3), the 70 cm LO criterion, as contradicted (D15); the lead SE confirms it belongs in ADR-057 | Agreed. No safety effect. The Si5351A's 200 MHz ceiling, if anything, narrows the out-of-band range of HZ-008 C7. ADR-057 records the dropped criterion under ADR-002's own revisit condition | No finding |
| (d) | ADR-013's method and the display text of ADR-009 and ADR-020 may also be contradicted in part | Confirmed, and ADR-015, 016, 024 and 026 carry display text too. The safety content of ADR-009, 013 and 015 is kept by the A5 design. ADR-013's HZ-008 C8 re-assessment is not carried. The route is the lead SE's ruling | finding-7 |
| (e) | HZ-011 K2 and K4 lose their object; REQ-SYS-099 is not met by A5 as drawn; cross items to WP-PDR-16 and WP-PDR-24 | K2: agreed (REQ-SYS-093 retired). K4: only its charge-limit half lapses; its REQ-SYS-090 half stays (finding-3 (b)). REQ-SYS-099: agreed, and the same missing actuator defeats REQ-SYS-098 and REQ-SYS-166. Under the lens this is Major, because `SW-PWR` provisions have no actuator and ADR-059 section 4.3 claims them | finding-1, finding-3 |

## Observation (no finding)

- **O-1 (ADR-057 point (1), restated unchanged from ADR-002).** "Frequency plan, band edges, guard, power steps and tuning limits are data, not code paths", and the reserved band control becomes "a Morse-menu entry". The band edges, the guard and the power-step values are HZ-008 and HZ-001 safety values (07 section 14.2 `SW-SYNTH` row h; REQ-SYS-009). The configuration guard's field list holds "power step" and "frequency calibration", not the band edges or the step values. If WP-PDR-32 keeps these as constant image data, not operator-settable and not persisted, and the reserved menu entry has no effect in rev A, the provision holds. Request to WP-PDR-32 and WP-PDR-35 to state it (cross item X-8).

## Cross items (returned to Claude as lead SE)

- **X-1 (INSP-130 reviewer; lead SE).** INSP-130 pins the same four blobs at `8a24bc6` and names this record (`paired_record: INSP-131`, `assurance_reviewer_agent`, `assurance_verdict` copied from here). If INSP-130 sets a different `product` path or raises author item (b) as its own finding, this record follows its product path and cites its finding id in finding-8 at iteration 2. SA-A3 and SA-A4 are checked then.
- **X-2 (WP-PDR-24, WP-PDR-16, WP-PDR-17, WP-PDR-37).** finding-1: the commanded rail-off path (controller and cell 60 C comparator on the rail P-FET gates, latched), the power-up order for REQ-SYS-166, and the HZ-007 K3 and K4 and single-point text. Alternatively, the CR-018 deltas with the residual put to the owner.
- **X-3 (WP-PDR-16 hazard writer; WP-PDR-25).** finding-3: HZ-011 K3 (VSYS feed, REQ-SYS-149) and K4 (its REQ-SYS-090 half stays). finding-6: HZ-005 K5 and K6 with REQ-SYS-076 and 077 (WP-PDR-25 audio analysis), HZ-008 K2, K3 and K6, HZ-015 K3, and the HZ-002 `firmware_role`. Author item (e): HZ-011 K2 loses its object.
- **X-4 (07 author by CR; WP-PDR-17).** finding-4: the 07 section 14.1 and 14.2 rows listed there, re-transcribed with the PDR determination.
- **X-5 (CR-018 author, WP-PDR-53).** REQ-SYS-130 ("charging disabled" removed); REQ-SYS-098, 099 and 166 (finding-1 route (2) only); REQ-SYS-076 and 077 at risk (finding-6); REQ-SYS-092 kept (finding-8). ADR-056 to ADR-059 in `source_ids` as each ADR's section 4.1 asks.
- **X-6 (WP-PDR-22 and the D-18 review pair).** `pa-permit-gate-d18.md` revision 1 (`c397ab1`) moves the hardware cutoffs to the gate's Q node. An ADR-056 revision adopts that wiring only after the D-18 record's review and SA pair are APPROVED. Until then ADR-056, 058 and 059 state the cutoffs by function (finding-2 (2)).
- **X-7 (lead SE).** finding-7: a ruling on ADR-009, 013, 015, 016, 020, 024 and 026 under README rule 2, recorded in ADR-056 section 7.
- **X-8 (WP-PDR-32, WP-PDR-35).** finding-5: the fault annunciation unit and its sender apart from the menu. O-1: band data as constant image data, and the reserved menu entry inert in rev A.
- **X-9 (brief).** The brief names `docs/hazards/hazards.json`. The file is `docs/safety/hazards.json` (0.5.0-pha, blob `81cacde4`), which this record and the ADRs use.

## Commands

- `git rev-parse HEAD:<path>`, `git rev-parse 8a24bc6:<path>` and `git hash-object <path>` for the four ADRs: equal. `git log --oneline 8a24bc6..HEAD -- docs/decisions/adr`: empty. `git show --stat` of `66f6123`, `abe5706` and `8a24bc6`: ADR files only.
- `.venv/bin/python tools/check_commit_msg.py --range <c>^..<c>` for `66f6123`, `abe5706` and `8a24bc6`: PASS each.
- `.venv/bin/python -c` reads of `docs/safety/hazards.json` (causes, controls, `firmware_role`, `single_point_failures` of HZ-002, 003, 004, 005, 007, 008, 009, 011, 014, 015) and of `docs/requirements/sys/requirements.json` (the statements listed in `input_files`).
- `sed` and `grep` on TS-012 sections 8.1, 8.3, 8.10 and 8.14; 07 sections 14.1 and 14.2; ADR-002, 004, 005, 009, 013, 015, 016, 020, 024 and 026, section 2; `git grep -l pa-permit-gate-d18 HEAD -- docs/reviews` (only INSP-118); `git show --stat c397ab1` (message only).
- `git merge-base --is-ancestor 7784672 main`: false. `git rev-parse cr/CR-012-pdr-checklist-templates:docs/templates/peer-review-checklist-software-assurance.md`: `5b135285`.
- `.venv/bin/python tools/traceability.py --report-only --output <scratchpad>/adr-review/trace-insp131.md`: 0 violations; `docs/vv` unchanged. `.venv/bin/python tools/validate_docs.py`: 117 passed, 0 failed.
- Filing check: `git archive HEAD docs tools` (HEAD `c16b787`) extracted to `<scratchpad>/adr-review/export`, this record copied to `docs/reviews/PDR/checklists/adr-056-to-059-software-assurance.md` there, and `.venv/bin/python tools/validate_docs.py --root <export>` run: "PASS docs/reviews/PDR/checklists/adr-056-to-059-software-assurance.md"; "118 passed, 0 failed, 118 checked". The three commits between `ac9cd1a` and `c16b787` touch `docs/cm` only; `git log 8a24bc6..c16b787 -- docs/decisions/adr` is empty, and INSP-130 is still not on `main`.

## Visual closure

No figure is part of the product, and none that this lens relies on changed. The ADRs carry no diagrams. TS-012 section 8.1 is a text block diagram and was read as text. The `c397ab1` plots were not opened, because that run is not reviewed here.

## Measurements (iteration 1)

Size: 4 ADRs, 659 lines. Checked: 7 component groups; 10 hazards, control by control; 27 requirement rows; 3 section 7 rulings; 5 author items; 8 INSP-118 liens. Findings: 1 Major, 7 Minor, all Open. Tasks: 20 rows (17 applied, 8 of them No; 3 N/A with relief). Checklist items answered No: 9 (SA-C-a, d, f, g, i, j; SA-D1, D2; SA-E1). Effort: 48 turns, about 95 minutes.

## Verdict (iteration 1)

```
ASSURANCE VERDICT: NEEDS CHANGES
PRODUCT: docs/decisions/adr/ADR-056-a5-hand-built-design.md@5636f477, ADR-057-2m-only-rev-a-70cm-ready-a5.md@c4ba923a, ADR-058-pico2-module-micro-usb-firmware-only.md@3b8bbd79, ADR-059-2s-18650-holders-external-charging.md@9961bd9e at 8a24bc6; PAIRED RECORD: INSP-130
PRODUCT TYPE: trade-study-or-adr; CRITICALITY: safety-critical
FINDINGS:
- [Major] finding-1 (swe-134 t6, SA-C-a, SA-C-j): the A5 power tree has no commanded rail-off path (EG1218 on the P-FET gates, LDO without enable, cell 60 C trip on the transmitter clamp only); REQ-SYS-098, 099 and 166 (HZ-007 K3, K4) have no actuator, while ADR-059 section 4.3 says those SW-PWR functions stay.
- [Minor] finding-2 (swe-087 t2, SA-E1): INSP-118 finding-9 to 11 (and 4 to 8) are not carried by ADR-056; the D-18 gate type and the VGG cutoff node are fixed although the D-18 fix record (c397ab1) changes both.
- [Minor] finding-3: VSYS feed not stated (HZ-011 K3, REQ-SYS-149); HZ-011 K4 keeps its REQ-SYS-090 half.
- [Minor] finding-4 (SA-D2): 07 section 14.1 and 14.2 rows and REQ-SYS-130 made stale are not named as consequences.
- [Minor] finding-5 (swe-134 t4): Morse fault announcement not kept apart from the menu sender.
- [Minor] finding-6 (SA-D1): hazard lines miss HZ-005 K5 and K6 (REQ-SYS-076, 077), HZ-008 K2, K3 and K6, HZ-015 K3.
- [Minor] finding-7: ADR-009, 013, 015, 016, 020, 024 and 026 contradicted in part and not ruled in ADR-056 section 7 (author item d).
- [Minor] finding-8: the ADR-056 section 4.1 row sweeps kept safety rows, REQ-SYS-092 among them (author item b).
TASKS APPLIED: swe-134 t5, swe-022 t1, swe-033 t1 to t3, swe-039 t4, swe-057 t2, swe-134 t4, t6, swe-205 t1, t3, swe-080 t1, t2, swe-081 t2, swe-086 t1, swe-087 t2, swe-089 t1
TASKS N/A (relief): swe-027 t1, swe-136 t1, swe-070 t1 (conditions not met; 07 sections 17.1 and 17.3)
SWE-134 ITEMS CHECKED: a, b, c, d, e, f, g, h, i, j, k, l
MEASUREMENTS: size=4 ADRs, 659 lines; tasks=20; tasks_no=8; turns=48; minutes=95; major=1; minor=7
```

## Iteration 2: delta verification of the fix round `03e3aea` (2026-09-29, HEAD `03e3aea`)

**Scope (rule C1).** Iteration 2 is a delta. Its purpose is to verify the fix of finding-1, the one Major finding. The author also answered the seven Minor findings in the same commit, so each of those fixes is checked too, under the same assurance lens. Every hunk of `git diff 8a24bc6 03e3aea -- docs/decisions/adr` was read: 194 inserted and 82 deleted lines in the four files. The acceptance criteria of iteration 1 still apply. In particular, a firmware function that an ADR says "stays" is checked against the hardware that the same ADR fixes, and the ADR's own summary is not taken as the evidence.

**Product.** The fix round commit `03e3aea` (on `main`, not pushed) edits the four ADRs in place. The ADRs are Proposed, so README rule 2 allows this. The commit touches only these four files, and it creates no file.

| ADR | Blob at `03e3aea` | Lines | Iteration 1 blob |
|---|---|---|---|
| ADR-056 | `b7cbd40c` | 326 | `5636f477` |
| ADR-057 | `5d9b8fc2` | 128 | `c4ba923a` |
| ADR-058 | `30850056` | 141 | `3b8bbd79` |
| ADR-059 | `713cccc0` | 176 | `9961bd9e` |

Each blob equals `git rev-parse HEAD:<path>` and `git hash-object <path>` at HEAD `03e3aea`. Each ADR gains one change-log row for the fix round. The decision content is unchanged: ADR-056 item 1 is still the owner's A5 decision as recorded, and items 2 to 4 of ADR-056 and ADR-057 to ADR-059 are still proposals for S1.

**Independence (rule C4).** As at iteration 1: this invocation authored no part of the four ADRs, of `03e3aea`, of TS-012 or of INSP-130. It edited no product file. It changed only this record, in the scratchpad.

**Search first.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (query: ADR-059 rail-off 2N3904 REQ-SYS-098 099 166 not met as drawn). After that, `git diff`, `sed`, `grep` and short Python reads of `hazards.json` were used only to pin lines in known files. The rustos repository was not read. LTspice was not run. Nothing was downloaded.

### Verification of the Major finding

**finding-1 (Major): Verified.** Each part of the iteration 1 fix was checked against the ADR text at `03e3aea`:

| Part of the fix asked for | Where the fix is | Check | Result |
|---|---|---|---|
| Stop claiming that the three `SW-PWR` functions work on the A5 power tree | ADR-059 section 4.3, last bullet | The section now says: "Only the transmit inhibit has an actuator in A5 as drawn (the PA_EN prerequisite). Rail enable, power-down and the lockout need the rail-off path of section 4.2 as their actuator: until WP-PDR-24 shows it, `SW-PWR` can decide those actions but cannot carry them out." This matches the hardware of section 2: the EG1218 alone drives the rail P-FET gates, and the LM2940-5 has no enable input | Verified |
| Correct the section 4.1 rows | ADR-059 section 4.1, rows REQ-SYS-012/097/098 and REQ-SYS-086/099/166 | REQ-SYS-098: "not met by A5 as drawn: nothing powers the loads down". REQ-SYS-099 and 166: "not met by A5 as drawn", with the reason (the LM393 #2 trip acts only on the transmitter; nothing holds the rails off). REQ-SYS-097 is met by the `PA_EN` prerequisite. That is right: 07 section 14.2 row h lists "each cell at or above 3.20 V in receive (REQ-SYS-097)" as a `PA_EN` prerequisite. REQ-SYS-086 is placed on the reverse-polarity DMP3099L (K6) and the protector window (K3), which matches HZ-007 K3's text "the protector FETs stay off unless both cells are within window" | Verified |
| State the gap in the decision section and state the rail-off path | ADR-059 section 2, new paragraph "Loads powered down by the radio (open design item, not decided here)"; section 4.2, new bullet "Rail-off path" | Section 2 names the three requirements and the reason there is no actuator. Section 4.2 sets five properties the path must have: (1) the controller commands it for REQ-SYS-098 and 166, and the LM393 #2 comparator commands it for REQ-SYS-099 independently of firmware; (2) it turns the rail P-FETs off and latches, so the rails stay off after the controller and the comparator lose their supply; (3) only an off-on cycle of the EG1218 releases it; (4) it says how REQ-SYS-166 is met at switch-on, before the cells have been read, with the S-8252AAO window as part of the answer; (5) it keeps the off current within REQ-SYS-100 (50 uA), and the latch itself does not run the pack down to the protector's 2.50 V cutoff. These are the properties that iteration 1 asked for, and they come with the firmware-independent 60 C path. The BOM row 12 2N3904 "rail-off" use is named (TS-012 section 8.3 row 12 reads "... relay driver, rail-off", quantity 7). WP-PDR-24 designs and simulates the path and states its single faults | Verified |
| Route (2) as the fallback, with the residual risk put to the owner | ADR-059 section 4.2, last paragraph; section 7, new revisit condition | If WP-PDR-24 cannot show the path at a cost within the ordering-gate margin, CR-018 carries deltas to REQ-SYS-098, 099 and 166, and the HZ-007 residual risk goes to the owner. The timing of this route is finding-9 (new, Minor) | Verified, with finding-9 |
| Carry the fix to the hazard lines and to ADR-056 | ADR-059 section 1 "Hazards in play", assumption 2 and section 4.3 HZ-007 line; ADR-056 section 4.1 row "REQ-SYS-097, 098, 099, 166" and section 4.3 HZ-007 line | K3 and K4 are "not met as drawn". K4's reading of the cell temperature "through the charger TS input" becomes the cell NTC on the ADC and the LM393 #2 comparator. K4's LCD gauge becomes the Morse and LED low-battery announcement (REQ-SYS-096). These readings match the `hazards.json` 0.5.0-pha texts of K3 and K4. WP-PDR-24 is to state the path's single faults, and that is where HZ-007's `single_point_failures` entry (the protector FET pair as the only layer against over-discharge) is answered. The HZ-007 hazard writer receives it with the WP-PDR-24 result (cross item X-2) | Verified |
| Name the work packages | ADR-059 sections 1, 4.1, 4.2, 4.3 and 7 | WP-PDR-24 designs the path, WP-PDR-16 re-reads the hazard, and WP-PDR-17 re-runs the safety-critical determination (section 4.3). WP-PDR-37 (layout) is named for the VSYS feed but not for the rail-off path. The layout follows the WP-PDR-24 schematic in any case, so this is not a finding (X-2) | Verified |

The assurance reading at ADR maturity is this. The decision no longer claims a `SW-PWR` provision that it cannot support. It does not rule the provision out either: the path costs cents, the part is already in the BOM, and its required properties are stated. The HZ-007 controls K3 and K4 are recorded as open, and each has an owner work package and a fallback that reaches the owner. The 07 section 14.2 `SW-PWR` provisions at rows a, h, j and l therefore have a place in the design. So the Major is closed. One gap remains. The S1 memo wording, which is the text the owner confirms, does not mention the open item, and the fallback names a CR that is dispositioned before the item is due. That gap is new finding-9 (Minor).

### Verification of the Minor findings

| Finding | Fix checked | Result |
|---|---|---|
| finding-2 | (1) ADR-056 section 4.3 has a new bullet "Open review liens that this decision carries". It lists INSP-110 finding-21, 22, 24, 25 and 27 and INSP-118 finding-4 to finding-11, each with its content, and says that each closes in TS-012 or in the work package its record names. The per-lien due event that iteration 1 asked for is left to the source records. Those records carry it, so this is accepted. (2) ADR-056 item 1 no longer fixes the D-18 gate type, its level interface or the cutoff node. The item 3 TS-006 row states both the TS-012 drawing and the D-18 record revision 1 proposal, and says they are fixed only when that record is APPROVED and adopted. (3) The HZ-003 line carries INSP-118 finding-11: the duty-limit form of D-6 needs its own sink NTC. (4) ADR-058 section 4.2 states the proposed move of the VBUS inhibit to the Q node. ADR-059 section 2 says "clamps the transmitter", a statement by function. The HZ-004 line carries INSP-118 finding-10 (one SIO write that raises both TX_KEY and PA_EN) | Verified (observation O-3) |
| finding-3 | ADR-059 section 2 "Rails" states the VSYS feed: from the LM2940-5 5 V bus through an OR-ing element (Schottky, or a P-FET gated by VBUS), so that VBUS cannot back-feed the 5 V bus, the transmit 5 V rail or the module drain. It cites `power-tree-and-charging.md` F18, which gives the Pico 2 datasheet's P-FET OR-ing option. WP-PDR-24 and WP-PDR-37 choose the element. ADR-058 section 4.2 adds an "Open item (VBUS back-feed)" with a test that shows it: USB applied, cells removed, and the 5 V bus, transmit 5 V and module drain all below the REQ-SYS-149 limit. HZ-011 K3 and REQ-SYS-149 are named in ADR-058 sections 1, 2, 4.2 and 4.3 and in ADR-056 section 4.1 (row REQ-SYS-092, 149). ADR-058 section 4.1 has no REQ-SYS-149 row, but ADR-056 section 4.1 carries it, which is enough. K4 keeps its REQ-SYS-090 half, and cause C4 still applies (ADR-058 sections 1 and 4.3, ADR-056 section 4.1 row REQ-SYS-090, 100, and the HZ-011 line). This matches the K4 text in `hazards.json` | Verified (observation O-2) |
| finding-4 | ADR-056 section 4.3 has a new bullet "07 rows made stale". It lists these 07 section 14.1 rows: "Battery and charging supervision", "Thermal protection", "Safe-state manager", "Menu override command path" and "Drivers", plus the "Neither" paragraph. It lists these section 14.2 rows: a, b, c, e, g and l, and the module rows `SW-PWR`, `SW-DISPLAY`, the `SW-SAFE` thermal unit and the safe-state manager. REQ-SYS-130 has a row in ADR-056 section 4.1 ("made stale"), with a cross item to CR-018. **Four of the nine iteration 1 items are still missing:** (3) row h: the Arm condition ("transmit armed under the Arm condition (Self-test passed ...; key-closed interlock passed)") does not yet list REQ-SYS-087, which becomes "refuse to arm transmit" (ADR-056 and ADR-059 section 4.1); (5) row i: "charging: the charger IC and the independent cell over-voltage protector (REQ-SYS-083) limit independently of software"; (6) row j: "charge disable within one supervision period of a fault"; (8) the 14.1 row "Frequency verification unit": "RP2350 crystal timebase, not the synthesizer reference". Route R3 counts the TCXO, which is the synthesizer's reference (D-17). The "Drivers" entry names FC0 but not this row's timebase clause | Open in part (residual Minor; a lien under rule C1) |
| finding-5 | ADR-056 section 4.3 has a new bullet "Fault annunciation". It says the unit stays in `SW-SAFE` and apart from the menu: it does not pass through the menu state machine, and a menu fault cannot block, delay or change a fault announcement. WP-PDR-32 and WP-PDR-35 fix whether it has its own Morse sender or shares one verified at its own level, and the WP-PDR-17 re-run checks it. This answers the isolation point (swe-134 task 4 b). **Still missing:** the hazard lines do not re-read the LCD wording of three controls. HZ-004 K1 says "the LCD shows 'KEY CLOSED: check plug'". HZ-003 K2 says "fault shown on the LCD". HZ-003 K6, the handbook, says "the PA temperature warning on the LCD". The ADR-056 HZ-004 line names K8 only. The HZ-003 line names K2 for its 81 C threshold only, and not K6. The other LCD controls are re-read: HZ-005 K6, HZ-006 K5, HZ-007 K4, HZ-011 K2 and K5; HZ-002 K4 lapses with the charger | Open in part (residual Minor; a lien under rule C1) |
| finding-6 | ADR-056 section 4.3: the HZ-005 line states K5 and K6 with the missing enable, mute and jack-detect path, and routes them to WP-PDR-25 and WP-PDR-16. REQ-SYS-076 and 077 get a section 4.1 row: "not yet shown with the MCP6002 buffer". The HZ-008 line re-reads K2, K3 and K6 and keeps K7 on route R3. The HZ-015 line says K3 loses its object and is rewritten. The HZ-002 line says its firmware role lapses. Each reading matches `hazards.json` 0.5.0-pha | Verified |
| finding-7 | ADR-056 section 7 has a new "Item 4". It assesses ADR-013 (method), ADR-022, ADR-026 and the display clauses of ADR-009, 015, 016, 020 and 024, and gives each a proposed route. ADR-013 is no longer listed as not contradicted. The re-assessment of HZ-008 cause C8 for the Si5351A is carried in the HZ-008 line. The item says that each ADR stays Accepted and in force until the lead SE rules, and that the conflict is an open item for S1. The rulings themselves belong to the lead SE, not to this record. The record gap is closed (cross item X-7) | Verified (observation O-4) |
| finding-8 | The ADR-056 section 4.1 power rows now match TS-012 section 8.10 row by row. Reallocated: 081 and 082. Reworded or changed: 083, 087 and 186. At risk: 084. Kept: 085, 090 and 100, and 092 with 149. Retired: 088, 089, 091, 093, 167, 185 and 070. Row 086 is kept, not in section 8.10. The second listing of 083 and 084 is gone. REQ-SYS-092 is "kept", with HZ-011 K1 and HZ-014 K4. Its row also reads "kept as written" among the REQ-SYS-055 to 183 transmitter rows. Checked against TS-012 lines 917 to 934. INSP-130 raised the same defect as its finding-1 (Major). This record cites that finding, as cross item X-1 asked | Verified |

### New findings (iteration 2)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-9"></a>finding-9 | assurance (introduced by the finding-1 fix) | Minor | `swe-134 7.1 task 6`, SA-D6 | ADR-059 section 6 "Proposed memo wording for S1"; section 1 assumption 2; section 4.2 "Rail-off path", last paragraph; section 7, last revisit condition; ADR-056 section 4.3 HZ-007 line | **The S1 memo that the owner confirms does not mention the open rail-off item, and the fallback names a CR that is dispositioned before the item is due.** (a) The memo reads "Confirm ADR-059. It restates ADR-005 with the A5 power tree ...". It does not say that the radio as drawn cannot power its loads down for a low cell (REQ-SYS-098) or a hot cell (REQ-SYS-099), or keep its rails off for an out-of-window cell (REQ-SYS-166). These are controls of HZ-007, a Catastrophic hazard. Nor does the memo say that confirming the ADR may later bring the owner a residual-risk decision. The body says all this (section 2, section 4.2), but the memo is what the owner reads and confirms. ADR-057's memo, by contrast, now names its open item: the retention of the edge-mount jack is "a PDR design item". (b) Assumption 2 is confirmed "before S2", and the plan puts the WP-PDR-24 values at S2 (plan section 8.12 row WP-PDR-24). The fallback says "CR-018 carries deltas to REQ-SYS-098, 099 and 166". But CR-018 is dispositioned at S1 (OD-40). If WP-PDR-24 cannot show the path after S1, the named route no longer exists as written. **Why Minor:** the ADR body states the gap plainly, and no requirement or residual risk changes without an owner decision. But this text feeds the S1 owner sheet, and the fix is one sentence, so it should be fixed before S1. **Fix:** (1) Add to the memo: "The radio as drawn does not yet switch itself off for a low or hot cell. A small latched switch-off circuit (a few cents, one transistor already in the parts list) is designed at PDR. If it cannot be shown, you will be asked to accept the risk or to change the requirements." (2) In section 4.2, section 7 and the ADR-056 HZ-007 line, state the fallback as "CR-018, if the WP-PDR-24 result comes before CR-018's S1 disposition; otherwise a revision of CR-018 or a new CR, with the owner's risk decision at S2". Or bring the WP-PDR-24 rail-off result before S1 | Open | Pending | |
| <a id="finding-10"></a>finding-10 | assurance (residual of finding-1 in the ADR it did not name) | Minor | `swe-039 7.1 task 4` | ADR-058 section 4.3, "Safety-critical software scope (SWE-134 provisions) changed" | **ADR-058 still says, without a caveat, that the `SW-PWR` discharge-side functions stay.** The text reads: "Its discharge-side functions and the GPIO24 VBUS reading (HZ-011 K6) stay." This is the claim that finding-1 corrected in ADR-059 section 4.3, where it now says "stay as requirements" and that rail enable, power-down and the lockout "cannot" be carried out until the rail-off path is shown. The two ADRs go to the owner together, and they now disagree. **Why Minor:** ADR-059 is the record of the power tree, and it is correct. **Fix:** in ADR-058 section 4.3, write: "Its discharge-side functions stay as requirements; rail enable, power-down and the cell over-temperature lockout have no actuator until the rail-off path of ADR-059 section 4.2 is shown. The GPIO24 VBUS reading (HZ-011 K6) stays." | Open | Pending | |

### Findings (iteration 2; current state of every finding of this record)

| Finding | Severity | State at iteration 2 | Remaining work |
|---|---|---|---|
| finding-1 | Major | Verified | None in the ADRs. X-2 carries the WP-PDR-24 design and the WP-PDR-16 hazard re-read |
| finding-2 | Minor | Verified | The liens close in their source records |
| finding-3 | Minor | Verified | WP-PDR-24 and WP-PDR-37 choose the OR-ing element and run the back-feed check |
| finding-4 | Minor | Open in part | 07 section 14.2 rows h (REQ-SYS-087 in the Arm condition), i (charger IC and protector) and j (charge disable), and the 14.1 frequency verification unit timebase clause, added to the ADR-056 list of stale rows |
| finding-5 | Minor | Open in part | The LCD wording of HZ-004 K1, HZ-003 K2 and HZ-003 K6 added to the ADR-056 hazard lines for WP-PDR-16 |
| finding-6 | Minor | Verified | WP-PDR-25 shows REQ-SYS-076 and 077, or proposes a delta |
| finding-7 | Minor | Verified | The lead SE rules on item 4 (X-7) |
| finding-8 | Minor | Verified | None |
| finding-9 | Minor | Open (new) | S1 memo sentence; fallback route timing |
| finding-10 | Minor | Open (new) | ADR-058 section 4.3 sentence |

There is no open Major finding, so the assurance verdict is APPROVED. Under rule C1, the four open Minor findings become liens once the verdict is APPROVED. They are due at the CDR readiness declaration and are listed in package section 15. Finding-9 and finding-10 each change the text that the owner reads at S1 (the ADR-059 memo, and the ADR-058 section 4.3 claim), and each fix is one or two sentences. So the assurance reviewer recommends that the lead SE fix them before the S1 sheet is built, in one more fix commit, rather than hold them to CDR. Finding-4 and finding-5 are writer inputs for WP-PDR-17 and WP-PDR-16, and they can stay liens.

### Observations (iteration 2; no finding)

- **O-1** (iteration 1) is unchanged: ADR-057 point (1) and the band data. It is still a request to WP-PDR-32 and WP-PDR-35 (X-8).
- **O-2 (ADR-059 section 2, VSYS feed).** The VSYS feed sentence is new text in the Decision section, and TS-012 section 8.1 does not draw it. It carries ADR-005's "feeds VSYS" over to the A5 LDO, and WP-PDR-24 and WP-PDR-37 choose the element. The change log's "No decision content changes" is therefore read as "nothing the owner decided has changed". The OR-ing element is a design constraint that REQ-SYS-149 already requires, so it is not a new decision.
- **O-3 (ADR-059 sections 4.1 and 4.2, "the transmitter clamp node").** Two sentences say the LM393 #2 cell 60 C trip acts "on the transmitter clamp node". That is the node as TS-012 draws it, and the D-18 record revision 1 proposes moving that trip to the Q node. Stating it by function, as section 2 does ("clamps the transmitter"), would avoid a later edit once the D-18 record is adopted. This is editorial, and it is covered by the X-6 rule.
- **O-4 (ADR-056 section 7 item 4, scope of the S1 set).** If the lead SE takes the proposed ruling 2 route for ADR-022, ADR-026 and the five display ADRs, seven more restating ADRs join this review set. Only the ADR-022 draft exists, outside the repository. Each would need its independent review and assurance pair before S1, because each is confirmed at OD-10 part 1 and ADR-015 bears on HZ-006 (the guest lock). This is a planning item for the lead SE (X-7), not a defect of these four ADRs.

### Task table and checklist items changed at iteration 2

| Task or item | Iteration 1 | Iteration 2 | Evidence |
|---|---|---|---|
| swe-039 7.1 task 4 | No | No | finding-1 and finding-8 verified; finding-3 verified; finding-10 (ADR-058 section 4.3 against ADR-059) open |
| swe-057 7.1 task 2 | No | Yes | Actuators for REQ-SYS-098, 099 and 166 required and routed (finding-1); fault annunciation placed apart from the menu (finding-5, isolation part) |
| swe-134 7.1 task 4 | No | Yes | Isolation of fault annunciation stated (finding-5); the INSP-118 finding-4 shortfall carried as a lien (finding-2) |
| swe-134 7.1 task 6 | No | No | finding-1, 3, 6, 7 and 8 verified; the LCD wording of HZ-004 K1 and HZ-003 K2 and K6 (finding-5 residual) and the fallback timing (finding-9) open |
| swe-205 7.1 task 1 | No | Yes | HZ-007 C9 and C10 now stated as "no actuator" with a path to be shown; HZ-005 K5 routed; fault annunciation as an incorrect-action path answered |
| swe-205 7.1 task 3 | No | No | 07 rows listed, apart from rows h, i and j and the frequency verification unit timebase (finding-4 residual) |
| swe-080 7.1 task 1 | No | Yes | Power switch and LDO (finding-1), USB power path (finding-3), audio buffer (finding-6) and cutoff node (finding-2) each carried |
| swe-087 7.1 task 2 | No | Yes | INSP-110 and INSP-118 liens listed in ADR-056 section 4.3 (finding-2) |
| swe-080 7.1 task 2 | Yes | Yes | `03e3aea`: `tools/check_commit_msg.py --range 03e3aea^..03e3aea` PASS, "Refs: ADR-056, ADR-057, ADR-058, ADR-059, INSP-130, INSP-131, WP-PDR-54". The commit touches the four ADR files only |
| SA-C-a | No | Yes | Rail enable at first start is a stated property of the rail-off path (REQ-SYS-166 at switch-on); the D-18 unpowered state is a carried lien; the "charging disabled" item is routed through REQ-SYS-130 |
| SA-C-d, SA-C-f, SA-C-i | No | Yes | INSP-118 finding-6, finding-7, finding-10 and finding-11 carried (finding-2) |
| SA-C-g | No | Yes | Row g and the GPIO24 partner listed as stale (finding-4); the ADC channel-identity lien carried (finding-2) |
| SA-C-j | No | Yes | The power-down and lockout response has a required actuator and an owner (finding-1); the INSP-118 finding-5 lien carried |
| SA-D1 | No | Yes | HZ-007 C9 and C10, HZ-005 K5 and fault annunciation answered (finding-1, 5, 6) |
| SA-D2 | No | No | finding-4 residual |
| SA-D6 | Yes | No | The fallback route of the rail-off item names a CR that is dispositioned before the item is due (finding-9) |
| SA-E1 | No | Yes | finding-2 verified |
| SA-A3, SA-A4 | Yes; N/A | Yes; Yes | INSP-130 iteration 1 (scratchpad draft, not yet on `main`) sets `product: docs/decisions/adr/`, pins the same four `8a24bc6` blobs as this record's iteration 1 pin, names `paired_record: INSP-131`, and applies `peer-review-checklist-design` revision B sections A, B and H. INSP-130 iteration 2 is still to pin the `03e3aea` blobs (X-1) |

### Readiness (iteration 2)

| # | Result | Evidence |
|---|---|---|
| R1 | Yes | Four blobs at `03e3aea` equal `git rev-parse HEAD:<path>` and `git hash-object <path>` at HEAD `03e3aea`. INSP-130 iteration 2 is to pin the same blobs (X-1) |
| R2 | Yes | Unchanged from iteration 1 |
| R3 | Yes | `validate_docs.py`: "117 passed, 0 failed, 117 checked" at HEAD `03e3aea`. `traceability.py --report-only --output <scratchpad>/adr-review/trace-insp131-it2.md`: "245 requirements, 173 test cases, 0 violation(s), 2 warning(s)" (REQ-SYS-125 and 148, SYS_UNALLOCATED, not touched by the ADRs). `git status --short docs/vv` was empty before and after, and `git restore` was run on the report and json as a guard. Filing check with this record in an export of HEAD `03e3aea`: PASS, 118 of 118 (Commands, iteration 2) |
| R4 | Yes | INSP-130 is still under its own invocation. This invocation is neither its reviewer nor the author |

### Cross items (iteration 2, returned to Claude as lead SE)

- **X-1 (INSP-130 reviewer).** INSP-130 iteration 2 pins the `03e3aea` blobs of this record's `product_files`. This record cites INSP-130 finding-1 for the same defect as finding-8, and INSP-130 finding-2 for finding-7. The record verdict stays NEEDS CHANGES until INSP-130 gives an APPROVED verdict and CR-012 is merged.
- **X-2 (WP-PDR-24, WP-PDR-16, WP-PDR-17, WP-PDR-37).** This item stands, reduced to the design work. WP-PDR-24 designs and simulates the latched rail-off path to the five properties of ADR-059 section 4.2 and states its single faults. WP-PDR-16 re-reads HZ-007 K3 and K4 and the `single_point_failures` entry on it. WP-PDR-17 re-runs the `SW-PWR` determination. WP-PDR-37 lays it out.
- **X-7 (lead SE).** Rule on ADR-056 section 7 item 4 before S1, and on the corrected reading of ruling 1. If ruling 2 is taken, the restating ADRs need drafting, filing and a review with an assurance pair before S1 (O-4).
- **X-10 (lead SE; ADR-058 and ADR-059 author).** Fix finding-9 and finding-10 before the S1 sheet is built (recommended). Finding-4 and finding-5 stay liens.
- **X-11 (CR-018 author, WP-PDR-53).** Plan now for the case where the rail-off result arrives after OD-40: a CR-018 revision or a new CR for REQ-SYS-098, 099 and 166 (finding-9 (b)).
- X-3 to X-6, X-8 and X-9 stand as at iteration 1. X-3 now also carries the LCD wording of HZ-004 K1 and HZ-003 K2 and K6 (finding-5 residual).

### Commands (iteration 2)

- `git log --oneline 8a24bc6..HEAD -- docs/decisions/adr` gives `03e3aea` only. `git show --stat 03e3aea`: four ADR files, 194 insertions, 82 deletions, no file created.
- `git rev-parse HEAD:<path>` and `git hash-object <path>` for the four ADRs: equal (`b7cbd40c`, `5d9b8fc2`, `30850056`, `713cccc0`).
- `git diff 8a24bc6 03e3aea -- docs/decisions/adr/<each>`, and full reads of the four ADRs at `03e3aea`.
- `.venv/bin/python tools/check_commit_msg.py --range 03e3aea^..03e3aea`: "PASS 03e3aea: rows 13; Refs: ADR-056, ADR-057, ADR-058, ADR-059, INSP-130, INSP-131, WP-PDR-54".
- `.venv/bin/python -c` reads of `docs/safety/hazards.json`: HZ-005 K5 and K6, HZ-007 K3 and K4, HZ-011 K4, and every control whose text names the LCD or the display.
- `sed -n 905,940p` of TS-012 (section 8.10 power rows) and `grep` of section 8.3 row 12. `grep` of 07 section 14.1 (frequency verification unit row) and section 14.2 rows h, i and j. `grep` of the plan (rule C1, WP-PDR-24, OD-40). `grep` of `power-tree-and-charging.md` F18 and F22.
- `.venv/bin/python tools/validate_docs.py`: 117 passed, 0 failed. `.venv/bin/python tools/traceability.py --report-only --output <scratchpad>/adr-review/trace-insp131-it2.md`: 0 violations and 2 warnings. `git restore docs/vv/traceability-report.md docs/vv/traceability.json`, after which `git status --short docs/vv` is empty.
- Filing check: `git archive HEAD docs tools` (HEAD `03e3aea`) extracted to `<scratchpad>/adr-review/export-it2`. This record was copied to `docs/reviews/PDR/checklists/adr-056-to-059-software-assurance.md` in the export, and `.venv/bin/python tools/validate_docs.py --root <export-it2>` was run: "PASS docs/reviews/PDR/checklists/adr-056-to-059-software-assurance.md"; "118 passed, 0 failed, 118 checked".

### Visual closure (iteration 2)

The product has no figure, and the fix round adds none. Nothing was rendered.

### Measurements (iteration 2)

Delta size: 1 commit, 4 files, 194 inserted and 82 deleted lines, every hunk read. Checked: 1 Major and 7 Minor fixes; 6 fix parts of finding-1; 15 hazard control texts; 3 rows of 07 section 14.2 and 1 row of 14.1; the power rows of TS-012 section 8.10 (lines 917 to 934) and section 8.3 row 12. Findings at iteration 2: 6 verified (1 Major, 5 Minor); 2 open in part (finding-4, finding-5); 2 new Minor (finding-9, finding-10). Task and item rows re-answered: 18. Checklist items answered No: 5 (swe-039 task 4, swe-134 task 6, swe-205 task 3, SA-D2, SA-D6). Effort at iteration 2: 28 turns and about 50 minutes (76 turns and about 145 minutes in total).

### Verdict (iteration 2)

```
ASSURANCE VERDICT: APPROVED
PRODUCT: docs/decisions/adr/ADR-056-a5-hand-built-design.md@b7cbd40c, ADR-057-2m-only-rev-a-70cm-ready-a5.md@5d9b8fc2, ADR-058-pico2-module-micro-usb-firmware-only.md@30850056, ADR-059-2s-18650-holders-external-charging.md@713cccc0 at 03e3aea; PAIRED RECORD: INSP-130
PRODUCT TYPE: trade-study-or-adr; CRITICALITY: safety-critical
RECORD VERDICT: NEEDS CHANGES (held: INSP-130 has no APPROVED verdict yet; CR-012 not merged)
FINDINGS:
- [Major] finding-1: Verified. ADR-059 no longer claims the SW-PWR rail enable, power-down and 60 C lockout; it states that there is no actuator, the latched rail-off path WP-PDR-24 must show, and the fallback to the owner.
- [Minor] finding-2, finding-3, finding-6, finding-7, finding-8: Verified.
- [Minor] finding-4: open in part. 07 section 14.2 rows h, i and j and the 14.1 frequency verification timebase clause are not in the ADR-056 list of stale rows (lien).
- [Minor] finding-5: open in part. The LCD wording of HZ-004 K1 and HZ-003 K2 and K6 is not re-read in the hazard lines (lien).
- [Minor] finding-9 (new): the ADR-059 S1 memo does not mention the open rail-off item, and the fallback names CR-018, which is dispositioned at S1 before the WP-PDR-24 result is due at S2 (fix before S1 recommended).
- [Minor] finding-10 (new): ADR-058 section 4.3 still says the SW-PWR discharge-side functions stay, with no caveat (fix before S1 recommended).
TASKS APPLIED: as iteration 1 (17 rows); No at iteration 2: swe-039 t4, swe-134 t6, swe-205 t3
TASKS N/A (relief): swe-027 t1, swe-136 t1, swe-070 t1 (conditions not met; 07 sections 17.1 and 17.3)
SWE-134 ITEMS CHECKED: a, b, c, d, e, f, g, h, i, j, k, l
MEASUREMENTS: delta=1 commit, 4 files, +194/-82; findings verified=6, open=4 (all Minor); tasks_no=3; items_no=5; turns=76; minutes=145; major=1; minor=9
```

## Iteration 3: delta verification of the second fix round `82f1df8` (2026-09-29, HEAD `82f1df8`)

**Scope (rule C1).** Iteration 3 is a delta. It checks the four Minor findings that iteration 2 left open (finding-4 and finding-5 in part, finding-9 and finding-10). It also checks the other text that `82f1df8` changed under the assurance lens: the section 4.1 hazard-control lists, the new section 4.3 hazard lines, the section 6 memo wording and the section 7 entries on item 4. Every hunk of `git diff 03e3aea 82f1df8 -- docs/decisions/adr` was read: 61 inserted and 38 deleted lines in three files. The acceptance criteria of iteration 1 still apply. The author's summary was not taken as the evidence. Each claim was checked against the ADR text at `82f1df8` and against its source.

**Product.** The second fix round commit `82f1df8` (on `main`, not pushed) edits ADR-056, ADR-058 and ADR-059 in place. The ADRs are Proposed, so README rule 2 allows this. Each of the three gains one change-log row. ADR-057 is not touched. The commit touches only these three files and creates no file.

| ADR | Blob at `82f1df8` | Lines | Iteration 2 blob |
|---|---|---|---|
| ADR-056 | `c66b4c63` | 347 | `b7cbd40c` |
| ADR-057 | `5d9b8fc2` (unchanged) | 128 | `5d9b8fc2` |
| ADR-058 | `9a2302de` | 142 | `30850056` |
| ADR-059 | `f988ffde` | 177 | `713cccc0` |

Each blob equals `git rev-parse 82f1df8:<path>`, `git rev-parse HEAD:<path>` and `git hash-object <path>` at HEAD `82f1df8`. `git log 03e3aea..HEAD -- docs/decisions/adr` gives `82f1df8` only. The decision content is unchanged. ADR-056 item 1 is still the owner's A5 decision as recorded. Items 2 to 4 of ADR-056, and ADR-057 to ADR-059, are still proposals for S1.

**Independence (rule C4).** As at iterations 1 and 2. This invocation authored no part of the four ADRs, of `82f1df8`, of TS-012 or of INSP-130. It edited no product file. It changed only this record, in the scratchpad.

**Search first.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (query: ADR-059 memo wording rail-off open item follow-on CR at S2). After that, `git diff`, `sed`, `grep` and short Python reads of `hazards.json` and `requirements.json` were used only to pin lines in known files. The rustos repository was not read. LTspice was not run. Nothing was downloaded.

### Verification of the open findings

| Finding | Fix checked | Result |
|---|---|---|
| finding-9 (Minor, new at iteration 2) | (a) The ADR-059 section 6 memo wording now adds: "One item is still open and is not decided by this confirmation: A5 as drawn cannot yet switch its own loads off for a low cell, a cell above 60 C or a cell outside its safe voltage window (REQ-SYS-098, 099 and 166)." It then says that a small latched switch-off circuit, expected to cost cents, is to be designed and simulated by WP-PDR-24 before S2. If the circuit cannot be shown within the cost margin, the owner will be asked at S2 to accept changed requirements and the remaining risk of a cell run too low or too hot (HZ-007). This is what iteration 2 asked for: the owner reads the open item and the possible risk decision in the text she confirms. (b) The fallback no longer names CR-018. Section 4.2 now says the WP-PDR-24 result is due at S2 (OD-10 part 2), after CR-018 is dispositioned at S1 (OD-40). It says CR-018 keeps REQ-SYS-098, 099 and 166 as written, and that any delta goes in a follow-on CR put to the owner at S2 with the HZ-007 residual risk as a risk decision. The section 7 revisit condition says the same. The ADR-056 HZ-007 line names no CR and points to ADR-059 section 4.2, so it needs no change. `grep CR-018` of ADR-059 finds no other fallback text. Assumption 2 is still confirmed "before S2", which matches the new timing. `docs/plan/pdr-work-plan.md` (blob `fd521750`) places OD-10 part 2 decisions at S2 | Verified |
| finding-10 (Minor, new at iteration 2) | ADR-058 section 4.3 now reads: "The GPIO24 VBUS reading (HZ-011 K6) stays, with its actuator, the transmit disarm. Its discharge-side functions stay as requirements, but only the transmit inhibit has an actuator in A5 as drawn: rail enable on the cell window, power-down and the cell over-temperature lockout need the rail-off path of ADR-059 section 4.2 ...". This agrees with ADR-059 section 4.3. The HZ-011 K6 text in `hazards.json` gives the actuator as stated ("transmit is disarmed and VBUS absent is a PA_EN prerequisite"). The two ADRs that go to the owner together no longer disagree | Verified |
| finding-5 (Minor, open in part) | The iteration 2 residual was the LCD wording of HZ-004 K1, HZ-003 K2 and HZ-003 K6. Each is now re-read in ADR-056 section 4.3. HZ-004: K1's "the LCD shows 'KEY CLOSED: check plug'" and K3's "shows 'KEY?'" become Morse and LED messages, and the interlock and the timeout are unchanged. HZ-003: K2's "fault shown on the LCD" becomes the Morse and LED cause message of the fault annunciation (REQ-SYS-067). K6, the handbook, keeps its text, with its "PA temperature warning on the LCD" read as the Morse warning. The line also says that the fold-back K6 names is K2's thermal fold-back, not the SWR fold-back that item 4 closes. That reading is correct: K6 sits in HZ-003 (thermal), and item 4 closes only the SWR option. HZ-014 K2's "LCD indication" of a configuration replaced by defaults is re-read the same way. Each quoted phrase matches `hazards.json` 0.5.0-pha. Each new reading sends the indication to the fault annunciation unit, which the iteration 2 fix placed in `SW-SAFE` apart from the menu. So the isolation point of `swe-134` task 4 carries over to these controls | Verified |
| finding-4 (Minor, open in part) | The iteration 2 residual had four items. Three are now in the ADR-056 section 4.3 list "07 rows made stale". (5) Row i: "charging: the charger IC and the independent cell over-voltage protector (REQ-SYS-083) limit independently of software", now the S-8252AAO alone. The list also names the row i audio ceiling. That item is harmless extra coverage, because the ceiling's requirements change via CR-018. (6) Row j: "charge disable within one supervision period of a fault", which has no object. The list also names "PA over-current or reflected-power fault ... (HZ-003 K5)", not sensed after item 4, and "battery under-voltage to power-down within 1 s", which has no actuator as drawn. (8) The 14.1 row "Frequency verification unit": its "RP2350 crystal timebase, not the synthesizer reference" clause. The list states that route R3 keeps the gate on the XOSC but scales the count by the XOSC/TCXO ratio counted in receive. That matches `frequency-budget.md` section 3.3 ("The gate stays on the XOSC, but the scale factor uses the TCXO"). Row h is now listed as well. It names the 10 kHz agreement, now read with the 5.0 kHz measured threshold of route R3 (`frequency-budget.md` section 3.3; TS-012 D-17), and the PA temperature inhibit at about 81 C. **Still missing: item (3), REQ-SYS-087 as a transmit-arm prerequisite.** ADR-056 and ADR-059 section 4.1 change REQ-SYS-087 to "refuse to arm transmit, in place of refusing charging". The 07 section 14.2 row h Arm condition reads "Self-test passed, REQ-SYS-003; key-closed interlock passed", and row e holds REQ-SYS-087 only as a charge-enable prerequisite. The ADR-056 list names row e only as stale "charge enable". Its row h entry does not name the new prerequisite. A 07 author who follows the list could delete the row e clause and never add REQ-SYS-087 to the row h Arm condition, or to the `SW-PWR` module row h entry. The provision would then be lost, not moved. The hazard is still controlled: the S-8252AAO window (HZ-007 K3) and the reverse-polarity FET act without firmware, so this stays Minor. **Fix (one clause):** in the ADR-056 row h entry, add "and the Arm condition gains the REQ-SYS-087 cell insertion check (refuse to arm transmit), which leaves row e". | Open in part (one item; a Minor lien under rule C1) |

### Other text changed at `82f1df8`, checked under the assurance lens

| Text | Check | Result |
|---|---|---|
| ADR-056 section 4.1, hazard controls named in every changed row and full control lists in the kept rows | Every requirement named in section 4.1 was checked against the inverse of `control_req_ids` in `hazards.json` 0.5.0-pha, about 90 requirement ids by a Python read. Every control that a row names is one the requirement serves, and no row omits one. Examples: REQ-SYS-055 gives HZ-001 K9, HZ-003 K8, HZ-004 K5, HZ-006 K9, HZ-012 K5 and HZ-014 K3. REQ-SYS-180 gives six controls, HZ-001 K10 to HZ-014 K8. REQ-SYS-064 gives HZ-001 K1, HZ-006 K1, HZ-012 K1 and HZ-014 K2. REQ-SYS-076 gives HZ-005 K4 and K5, and REQ-SYS-077 gives HZ-005 K6. REQ-SYS-130 gives HZ-002 K4 and K5, HZ-004 K7 and HZ-005 K5. REQ-SYS-160 and 161 are marked as carrying none, which the file confirms. REQ-SYS-092 is kept with HZ-011 K1 and HZ-014 K4, so the finding-8 fix holds | Verified |
| ADR-056 section 4.3, new or extended hazard lines (HZ-001 K4, K7, K8; HZ-003 K1, K4, K7; HZ-004 K7, K11; HZ-006 K4; HZ-009 K6; HZ-012; HZ-014 K2, K3) | Each quoted control text matches `hazards.json`. HZ-001 K4 keeps "the ALC-off 10 W case" as the fault bound, and the line says it still covers the A5 open-loop case of at most 8 W at 8.4 V (D-9). That 8 W figure is a WP-PDR-22 pass criterion that has not yet been shown. The claim still holds without it: `pa-drive-ts012.md` at HEAD gives the unclamped open loop at the -10 C start as 10.68 W at the module and 9.58 W at the SMA, and the note says "The 10 W figure holds at the SMA". HZ-012 K4 now rests on the module's load-ruggedness rating, and its recessed-contact clause holds for the A5 SMA female jack (REQ-SYS-104). HZ-014 K3 keeps "the protector" limit only, which is right with no charger. HZ-004 K7 names REQ-SYS-130's stale "charging disabled" item. HZ-013 K2's encoder bushing becomes the potentiometer bushing (ruling 1) | Verified (observation O-6) |
| ADR-056 section 6 memo wording, parts 1 and 2 | Part 1 now tells the owner that the SWR fold-back closure "covers survival into a bad antenna only, and the spurious and power checks into SWR 2:1 are still to be shown". Under the assurance lens this is the correct limit: item 4 removes a sensed fault (07 row j, "PA over-current or reflected-power fault") and does not show the SWR 2:1 case. Part 1 also names the supersession of ADR-006, 007 and 012 in plain terms. Part 2, the ADR-013 notice, matches TS-012 section 8.10 rows REQ-SYS-029 and 031 (78 dB TBR). Neither of those requirements carries a hazard id. Part 2 is marked as to be put in the form the lead SE rules | Verified |
| ADR-056 section 7, "Lead SE ruling on item 4: pending" and the list of restating ADRs | The ruling is not invented. The entry lists what must be made to agree with the ruling once it is given. Each restating ADR is to be filed before S1 with its own independent review, which must be APPROVED before S1. This answers observation O-4 of iteration 2 as far as the author can. The ruling itself stays with the lead SE (X-7) | Verified (observation O-5) |
| ADR-058 Decision class row | The charge-path change is sourced to TS-012 items (a) and (b). Hand assembly is sourced to the owner's direction, taken as a constraint in TS-012 section 2 (exception EX-2). No safety content changes. This is INSP-130's lens | No assurance effect |

### Findings (iteration 3; current state of every finding of this record)

| Finding | Severity | State at iteration 3 | Remaining work |
|---|---|---|---|
| finding-1 | Major | Verified (iteration 2) | None in the ADRs. X-2 carries the WP-PDR-24 design and the WP-PDR-16 hazard re-read |
| finding-2 | Minor | Verified (iteration 2) | The liens close in their source records |
| finding-3 | Minor | Verified (iteration 2) | WP-PDR-24 and WP-PDR-37 choose the OR-ing element and run the back-feed check |
| finding-4 | Minor | Open in part | One clause: REQ-SYS-087 as a transmit-arm prerequisite, added to the ADR-056 row h entry of "07 rows made stale" (a lien under rule C1; X-4) |
| finding-5 | Minor | Verified (iteration 3) | None |
| finding-6 | Minor | Verified (iteration 2) | WP-PDR-25 shows REQ-SYS-076 and 077, or proposes a delta |
| finding-7 | Minor | Verified (iteration 2) | The lead SE rules on item 4 (X-7) |
| finding-8 | Minor | Verified (iteration 2) | None |
| finding-9 | Minor | Verified (iteration 3) | None in the ADRs. X-11 (plan for the follow-on CR at S2) |
| finding-10 | Minor | Verified (iteration 3) | None |

No Major finding is open, and none was opened at iteration 3. The assurance verdict stays APPROVED. The one open item, the finding-4 clause, is a lien under rule C1, due at the CDR readiness declaration and listed in package section 15. It is a writer input for the 07 revision with the WP-PDR-17 re-run. It does not change the text the owner reads at S1. The author may still fold it into any later fix commit before S1.

### Observations (iteration 3; no finding)

- **O-1** (iteration 1) is unchanged: ADR-057 point (1) and the band data. It is still a request to WP-PDR-32 and WP-PDR-35 (X-8).
- **O-2 and O-3** (iteration 2) are unchanged. ADR-059 sections 4.1 and 4.2 still name "the transmitter clamp node" in two places. This is covered by the X-6 rule.
- **O-4** (iteration 2) is answered in the ADR as far as the author can answer it (section 7 entries). It is replaced by O-5.
- **O-5 (ADR-056 section 7, the restating ADRs).** The entry gives each restating ADR "its own independent review record". It does not say that some of them also need a software assurance pair. Under 07 section 2.1.1 row 3, an ADR whose decision constrains a safety-critical component of 07 section 14.1 is reviewed with an SA pair. At least three restatements do that. The ADR-009 restatement carries the key-closed interlock (HZ-004 K1; `SW-KEYER` and `SW-TXSEQ`). The ADR-015 restatement carries the guest lock that blocks `PA_EN` (HZ-006 K3; `SW-SAFE`). The ADR-020 restatement carries a run that ends at the REQ-SYS-098 power-down, which has no actuator as drawn (`SW-PWR`; finding-1). The 07 dispatch rule applies whether or not the ADR says so, so this is a planning point for the lead SE when the records are assigned (X-7), not a defect.
- **O-6 (ADR-056 HZ-001 line, the D-9 reason).** The line gives D-9's "at most 8 W at 8.4 V" as the reason the 10 W fault bound still holds. That figure is a WP-PDR-22 pass criterion that has not yet been shown. The claim holds on the `pa-drive-ts012.md` figures even without it: 9.58 W at the SMA at the -10 C start. If WP-PDR-16 re-reads HZ-001, citing the analysis figure rather than the design target would avoid a claim that depends on work not yet done. This is editorial.

### Task table and checklist items changed at iteration 3

| Task or item | Iteration 2 | Iteration 3 | Evidence |
|---|---|---|---|
| swe-039 7.1 task 4 | No | Yes | finding-10 verified. ADR-058 and ADR-059 section 4.3 now agree with the power tree they fix |
| swe-134 7.1 task 6 | No | Yes | finding-5 residual verified: the LCD wording of HZ-004 K1 and K3, HZ-003 K2 and K6 and HZ-014 K2 is re-read. finding-9 verified: the fallback reaches the owner at S2 through a CR that exists then. Section 4.1 control lists match `hazards.json` |
| swe-205 7.1 task 3 | No | No | 07 rows h, i and j and the frequency verification timebase clause are now listed. The REQ-SYS-087 move into the row h Arm condition is not (finding-4 residual) |
| swe-080 7.1 task 2 | Yes | Yes | `82f1df8`: `tools/check_commit_msg.py --range 82f1df8^..82f1df8` PASS, "Refs: ADR-056, ADR-058, ADR-059, INSP-130, INSP-131, WP-PDR-54". The commit touches the three edited ADR files only |
| SA-D2 | No | No | finding-4 residual |
| SA-D6 | No | Yes | finding-9 verified: the rail-off fallback is routed to a follow-on CR at S2, after the WP-PDR-24 result is due |
| SA-A3, SA-A4 | Yes; Yes | Yes; Yes | The INSP-130 scratchpad draft is at iteration 2: it pins the `03e3aea` blobs, names `paired_record: INSP-131` and applies `peer-review-checklist-design` revision B. Its `assurance_verdict` still reads NEEDS CHANGES, which is this record's iteration 1 value. INSP-130 iteration 3 is to pin the `82f1df8` blobs and copy APPROVED (X-1) |

The other rows of the task table and checklist keep their iteration 2 answers.

### Readiness (iteration 3)

| # | Result | Evidence |
|---|---|---|
| R1 | Yes | Four blobs at `82f1df8` equal `git rev-parse HEAD:<path>` and `git hash-object <path>` at HEAD `82f1df8`. INSP-130 iteration 3 is to pin the same blobs (X-1) |
| R2 | Yes | Unchanged from iteration 1 |
| R3 | Yes | `validate_docs.py`: "117 passed, 0 failed, 117 checked" at HEAD `82f1df8`. `traceability.py --report-only --output <scratchpad>/adr-review/trace-insp131-it3.md`: "245 requirements, 173 test cases, 0 violation(s), 2 warning(s)" (REQ-SYS-125 and 148, SYS_UNALLOCATED, not touched by the ADRs). `git status --short docs/vv` was empty before and after, and `git restore docs/vv/traceability-report.md docs/vv/traceability.json` was run as a guard. Filing check with this record in an export of HEAD `82f1df8`: PASS, 118 of 118 (Commands, iteration 3) |
| R4 | Yes | INSP-130 is still under its own invocation. This invocation is neither its reviewer nor the author |

### Cross items (iteration 3, returned to Claude as lead SE)

- **X-1 (INSP-130 reviewer).** INSP-130 iteration 3 pins the `82f1df8` blobs of this record's `product_files` and copies `assurance_verdict: APPROVED`, which this record has held since iteration 2. The record verdict stays NEEDS CHANGES until INSP-130 gives an APPROVED verdict and CR-012 is merged (`git merge-base --is-ancestor 7784672 main` is still false).
- **X-4 (07 author by CR; WP-PDR-17).** This item stands with one addition: REQ-SYS-087 moves from the row e charge-enable prerequisites to the row h Arm condition and the `SW-PWR` module row (finding-4 residual). The ADR-056 author may add the clause to the row h entry in any later fix commit.
- **X-7 (lead SE).** Rule on ADR-056 section 7 item 4 before S1, and record the ruling in the "pending" entry. When the review records for the restating ADRs are assigned, give the ADR-009, ADR-015 and ADR-020 restatements an SA pair under 07 section 2.1.1 row 3 (O-5).
- **X-10 (lead SE; ADR-058 and ADR-059 author).** Closed: finding-9 and finding-10 are fixed before the S1 sheet is built.
- **X-11 (CR-018 author, WP-PDR-53).** This item stands, now in the form ADR-059 records: CR-018 keeps REQ-SYS-098, 099 and 166 as written. If WP-PDR-24 cannot show the rail-off path, a follow-on CR goes to the owner at S2 with the HZ-007 risk decision.
- X-2, X-3, X-5, X-6, X-8 and X-9 stand as at iteration 2.

### Commands (iteration 3)

- `git log --oneline 03e3aea..HEAD -- docs/decisions/adr` gives `82f1df8` only. `git show --stat 82f1df8`: three ADR files, 61 insertions, 38 deletions, no file created.
- `git rev-parse HEAD:<path>`, `git rev-parse 82f1df8:<path>` and `git hash-object <path>` for the four ADRs: equal (`c66b4c63`, `5d9b8fc2`, `9a2302de`, `f988ffde`).
- `git diff 03e3aea 82f1df8 -- docs/decisions/adr/ADR-058-... ADR-059-...` (full), and `git diff --word-diff=plain 03e3aea 82f1df8 -- docs/decisions/adr/ADR-056-...` (every changed hunk).
- `.venv/bin/python tools/check_commit_msg.py --range 82f1df8^..82f1df8`: "PASS 82f1df8: rows 13; Refs: ADR-056, ADR-058, ADR-059, INSP-130, INSP-131, WP-PDR-54".
- `.venv/bin/python -` reads of `docs/safety/hazards.json`: the inverse of `control_req_ids` for every requirement named in ADR-056 section 4.1 and for REQ-SYS-081 to 100, 070, 111, 137, 149, 166, 167, 185 and 186; the control texts listed in `input_files_iteration_3`. A read of `docs/requirements/sys/requirements.json` for REQ-SYS-029 and 031 (`hazard_ids` empty).
- `grep` of 07 section 14.1 (frequency verification unit row) and 14.2 rows b, d, e, h, i and j and the `SW-PWR` and frequency verification module rows. `sed` of `frequency-budget.md` section 3.3. `git show HEAD:docs/design/analysis/pa-drive-ts012.md` lines 308 and 457 (the working-tree copy has uncommitted edits by another task, so the committed blob `02852058` was read). `grep` of TS-012 for D-9, D-17 and the section 8.10 rows REQ-SYS-029 and 031. `grep` of the plan for OD-10 part 2.
- `grep -n 087` and `grep CR-018` of ADR-056, 058 and 059.
- `.venv/bin/python tools/validate_docs.py`: 117 passed, 0 failed. `.venv/bin/python tools/traceability.py --report-only --output <scratchpad>/adr-review/trace-insp131-it3.md`: 0 violations and 2 warnings. `git restore docs/vv/traceability-report.md docs/vv/traceability.json`, after which `git status --short docs/vv` is empty.
- `git merge-base --is-ancestor 7784672 main`: false (CR-012 not merged).
- Filing check: `git archive HEAD docs tools` (HEAD `82f1df8`) extracted to `<scratchpad>/adr-review/export-it3`. This record was copied to `docs/reviews/PDR/checklists/adr-056-to-059-software-assurance.md` in the export, and `.venv/bin/python tools/validate_docs.py --root <export-it3>` was run: "PASS docs/reviews/PDR/checklists/adr-056-to-059-software-assurance.md"; "118 passed, 0 failed, 118 checked".

### Visual closure (iteration 3)

The product has no figure, and the second fix round adds none. Nothing was rendered.

### Measurements (iteration 3)

Delta size: 1 commit, 3 files, 61 inserted and 38 deleted lines, every hunk read. Checked: 4 open Minor findings; about 90 requirement-to-control mappings of ADR-056 section 4.1; 18 hazard control texts; 7 rows of 07 section 14.2 and 1 row of 14.1; the section 6 memo wording of ADR-056 and ADR-059; the section 7 entries on item 4. Findings at iteration 3: 3 verified (finding-5, finding-9, finding-10); 1 still open in part (finding-4, one clause); no new finding. In total: 9 verified (1 Major, 8 Minor), 1 open (Minor, a lien). Task and item rows re-answered: 7. Checklist items answered No: 2 (swe-205 task 3, SA-D2). Effort at iteration 3: 30 turns and about 45 minutes (106 turns and about 190 minutes in total).

### Verdict (iteration 3)

```
ASSURANCE VERDICT: APPROVED
PRODUCT: docs/decisions/adr/ADR-056-a5-hand-built-design.md@c66b4c63, ADR-057-2m-only-rev-a-70cm-ready-a5.md@5d9b8fc2, ADR-058-pico2-module-micro-usb-firmware-only.md@9a2302de, ADR-059-2s-18650-holders-external-charging.md@f988ffde at 82f1df8; PAIRED RECORD: INSP-130
PRODUCT TYPE: trade-study-or-adr; CRITICALITY: safety-critical
RECORD VERDICT: NEEDS CHANGES (held: INSP-130 has no APPROVED verdict yet; CR-012 not merged)
FINDINGS:
- [Major] finding-1: Verified (iteration 2).
- [Minor] finding-2, finding-3, finding-6, finding-7, finding-8: Verified (iteration 2).
- [Minor] finding-5: Verified. The LCD wording of HZ-004 K1 and K3, HZ-003 K2 and K6 and HZ-014 K2 is re-read as Morse and LED messages of the fault annunciation.
- [Minor] finding-9: Verified. The ADR-059 S1 memo names the open rail-off item and the possible risk decision at S2; the fallback is a follow-on CR at S2, and CR-018 keeps REQ-SYS-098, 099 and 166 as written.
- [Minor] finding-10: Verified. ADR-058 section 4.3 now agrees with ADR-059 section 4.3.
- [Minor] finding-4: open in part (lien). 07 rows h, i and j and the frequency verification timebase clause are listed; the move of REQ-SYS-087 into the row h Arm condition is not.
TASKS APPLIED: as iteration 1 (17 rows); No at iteration 3: swe-205 t3
TASKS N/A (relief): swe-027 t1, swe-136 t1, swe-070 t1 (conditions not met; 07 sections 17.1 and 17.3)
SWE-134 ITEMS CHECKED: a, b, c, d, e, f, g, h, i, j, k, l
MEASUREMENTS: delta=1 commit, 3 files, +61/-38; findings verified=9, open=1 (Minor); tasks_no=1; items_no=2; turns=106; minutes=190; major=1; minor=9
```
