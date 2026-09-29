---
# Peer-review record front matter (charter section 5; docs/process/01-lifecycle-and-reviews.md section 13;
# docs/process/07-software-engineering-plan.md section 10.2). Independent review of the WP-PDR-41 "FW-B1 PDR point
# for WP-SW-08, 10 and 12": the DML-3 note with its checker and results file, and the WP-SW-08 flash ICD pages on
# rustos branch cwht/wp-sw-08, at the record path the PDR work plan WP-PDR-41 "Reviewer" paragraph names.
# Checklist: docs/templates/peer-review-checklist-design.md revision B, the checklist WP-PDR-41 names ("the
# independent code reviewer with the design checklist"). Its blob 45957f60 is the same on main and on
# cr/CR-012-pdr-checklist-templates (7784672). The record verdict is held while CR-012 is unmerged (lead SE
# convention of 2026-09-27) and until the software assurance pair is APPROVED.
# Freeze (rule C2): the three cwht files are drafts the harness keeps out of the repository; the lead SE files them
# unchanged. The cwht blobs below are git hash-object of the revision 1 drafts (fix round 1); filing them
# byte-identical keeps this record valid, and any change needs a further delta iteration. product_commit
# (iteration 2) is the cwht HEAD on which the drafts were exported, checked and validated (82f1df8; the note's
# section 2 inputs have the same blobs there as at be49be6). The rustos blobs equal git rev-parse 00d5383:<path>,
# the branch head of cwht/wp-sw-08 (fix commit on top of 03b1997, no amend). product_files_iteration_1 keeps the
# iteration 1 set (cwht HEAD f4f6922, rustos 03b1997).
id: INSP-132
checklist: peer-review-checklist-design
checklist_revision: B
checklist_file: docs/reviews/PDR/checklists/analysis-fw-b1-dml3-wp-sw-08-10-12.md
product: docs/design/analysis/fw-b1-dml3-wp-sw-08-10-12.md
product_commit: "82f1df85de881a7d7fd1a8d87af40b2cd76c432c"
product_files: ["docs/design/analysis/fw-b1-dml3-wp-sw-08-10-12.md@8a403ddba8b1d785fdb3c8caf226e5677509c947", "docs/design/analysis/fw-b1-dml3/check_fw_b1_dml3.py@03c960dc66ba6fd607ed866b5802e184e8ef0c49", "docs/design/analysis/fw-b1-dml3/fw-b1-dml3-results.json@225e23c45f597c270c8a3081049759006f525120", "rustos:docs/icd/rp2350/flash/index.md@56d3a73ed78a81e2a4f8f71f066f774256709e22", "rustos:docs/icd/rp2350/flash/01_bootrom_api.md@f8ca1a2eb46daed1e753816ba7f3dae80e306eca", "rustos:docs/icd/rp2350/flash/02_programming.md@8f803cc99d07c88364119cdf9c2770b5a8223d63", "rustos:docs/icd/rp2350/flash/03_xip_qmi.md@f66298c75b8db26ee58eb46ad6f1b2cb979f04d1", "rustos:docs/icd/rp2350/index.md@b6fe67962cb946c63d70e7ff13ce43241edad18d"]
product_files_iteration_1: ["docs/design/analysis/fw-b1-dml3-wp-sw-08-10-12.md@4757a6b6a65c5c6ed975bb5051ee2dc7a3a010dc", "docs/design/analysis/fw-b1-dml3/check_fw_b1_dml3.py@5a070bb0ee07f2a65e382cd090cb28f4910d62da", "docs/design/analysis/fw-b1-dml3/fw-b1-dml3-results.json@79c9547298785daa8f7eb93573d4f59094399b7f", "rustos:docs/icd/rp2350/flash/index.md@b42c5ab5ea12a886bcd5cd19f7dc16f7ebc75a25", "rustos:docs/icd/rp2350/flash/01_bootrom_api.md@f8ca1a2eb46daed1e753816ba7f3dae80e306eca", "rustos:docs/icd/rp2350/flash/02_programming.md@bebbadc26708d14fd1c309f5cadc9ba4c054c60a", "rustos:docs/icd/rp2350/flash/03_xip_qmi.md@f66298c75b8db26ee58eb46ad6f1b2cb979f04d1", "rustos:docs/icd/rp2350/index.md@b6fe67962cb946c63d70e7ff13ce43241edad18d"]
rustos_commit: "00d53834dfe315aafd09a11ec1d76e6ffbc45835"
rustos_commit_iteration_1: "03b1997d45b9cfa267133a389cebe87a346a6e50"
product_size: "iteration 1: 1 note (352 lines, 10 sections, 30 datasheet citations D1 to D30), 1 checker (380 lines, 54 assertions), 1 results file (230 lines); rustos commit 03b1997 with 4 ICD pages (322 lines) and 1 index row. Iteration 2 delta: note revision 1 (440 lines; 132 insertions and 44 deletions against revision 0), checker 467 lines (83 assertions), results 281 lines; rustos 03b1997..00d5383 47 insertions and 22 deletions in 02_programming.md (119 lines) and flash/index.md (76 lines)"
sprint: PDR-prep
author_agent: "author:WP-PDR-41 FW-B1 DML-3 note and WP-SW-08 ICD (Claude, firmware developer role)"
reviewer_agent: "reviewer:WP-PDR-41-dml3-iter1 and reviewer:WP-PDR-41-dml3-iter2 (independent code reviewer; authored no part of WP-SW-08, 10 or 12, of the note, its checker, its fix round or the ICD pages)"
# criticality: WP-SW-08 and WP-SW-12 serve the safety-critical configuration guard (SW-SAFE cfg_guard) and the
# boot image check (SW-BOOT), HZ-014, 07 section 14.1; WP-SW-10 serves verification
criticality: safety-critical
assurance_required: true
assurance_reviewer_agent: "sa-reviewer:WP-PDR-41-dml3 (separate invocation, record docs/reviews/PDR/checklists/analysis-fw-b1-dml3-wp-sw-08-10-12-software-assurance.md, for WP-SW-08 and WP-SW-12; iteration 1 NEEDS CHANGES on its findings 1 to 3, Major; its iteration 2 delta pending)"
iteration: 2
readiness_met: true
# reviewer_verdict: APPROVED at iteration 2 (rule C1): finding-1 and finding-2 (Major) Verified at note 8a403ddb and
# rustos 00d5383; finding-3 and finding-5 (Minor) Verified, overtaken by the Major fix text. The delta raises four
# new Minor findings (14 to 17) on the fix text. The 13 open findings are all Minor and become liens under rule C1
# (owner the firmware developer; due at the CDR readiness declaration)
reviewer_verdict: APPROVED
# assurance_verdict: the paired SA record was NEEDS CHANGES at iteration 1 (its findings 1 to 3, Major); its
# iteration 2 delta has not run
assurance_verdict: pending
# verdict: held at NEEDS CHANGES: CR-012 is unmerged (lead SE convention of 2026-09-27) and the SA pair is not
# APPROVED. The ICD blobs are on an unmerged rustos branch (OD-23; PCR-4 at the owner's merge)
verdict: NEEDS CHANGES
findings_major: 2
findings_minor: 15
# findings_open: 13, all Minor (findings 4, 6 to 17), liens under rule C1
findings_open: 13
findings_fixed: 0
findings_verified: 4
findings_deferred: 0
assurance_findings_major: 0
assurance_findings_minor: 0
assurance_tasks_applied: []
deferred_rids: []
# items_no: none at iteration 2 (iteration 1: CK-DES-A6, CK-DES-C10, CK-DES-D13, CK-DES-H1, all on finding-1 and
# finding-2, now Yes or Yes with Minor exceptions)
items_no: []
renders_inspected: 0
# effort: totals of iterations 1 and 2 (iteration 1: 70 turns, 95 minutes; iteration 2: about 32 turns, 45 minutes)
effort_turns: 102
effort_minutes: 140
record_status: Open
date: 2026-09-29
date_closed: null
---

# Peer review record INSP-132: FW-B1 DML-3 note (WP-SW-08, 10, 12) and the WP-SW-08 flash ICD, iterations 1 and 2

**Product.** The WP-PDR-41 DML-3 note `docs/design/analysis/fw-b1-dml3-wp-sw-08-10-12.md` (draft blob `4757a6b6`), its checker `docs/design/analysis/fw-b1-dml3/check_fw_b1_dml3.py` (`5a070bb0`) and its results file `fw-b1-dml3-results.json` (`79c95472`), all drafts not yet in the repository. Also the WP-SW-08 register ICD on rustos branch `cwht/wp-sw-08` at `03b1997` (parent `cwht/wp-sw-03` `48e07ec`): `docs/icd/rp2350/flash/index.md`, `01_bootrom_api.md`, `02_programming.md`, `03_xip_qmi.md`, and one row in `docs/icd/rp2350/index.md`. `git diff --stat 48e07ec 03b1997` shows these 5 files only (323 insertions). The branch is not pushed and is not merged.

**Checklist.** `docs/templates/peer-review-checklist-design.md` revision B (blob `45957f60`, the same on `main` and on `cr/CR-012-pdr-checklist-templates`). Sections A to H apply to the note, and section I applies to the ICD pages. The rustos pages are a register ICD extraction, not an `ICD-<A>-<B>` document, so only the content item I3 applies to them. Section J (hardware) is N/A.

**Independence (rule C4).** This invocation wrote no part of WP-SW-08, 10 or 12: not the note, the checker, the results or the rustos pages.

**Search first (rule C3).** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` came before every `grep`. It was used for the WP-PDR-41 text, RP2350-E10 and `--abs-block`, and the configuration store layout. `grep` only pinned lines in the files the search returned or in known paths.

**rustos access.** Committed objects only, through `git -C ~/rust/rustos show` and `ls-tree` of `03b1997`, `48e07ec` and `2ec64c0` (WP-PDR-41 "read by `git show` only"). The rustos working tree was not read or changed. The datasheet used is the committed `docs/rp2350-datasheet.pdf` (blob `1b26078d`, the same at `2ec64c0` and `03b1997`), written to the reviewer scratchpad. `pdfinfo` gives creation date 2025-02-20 and 1369 pages. `git worktree list` shows no scratch worktree left behind by the author.

**Acceptance criteria (rule C7).** These come from WP-PDR-41 "FW-B1 PDR point" and technology assessment section 1 (the DML-3 row) and section 3.18.
- For each of WP-SW-08, 10 and 12: an analytical proof of the critical function against its requirement, and its ICD page extracted or cited.
- WP-SW-08: the bootrom `flash_range_erase` and `flash_range_program` API; the QMI and XIP constraints (XIP disabled, interrupts masked, code in RAM; RSK-021); an erase and program time budget against the configuration-store requirements; the extraction prepared as a rustos pull request for the owner's merge (OD-23).
- WP-SW-10: the committed rustos `uart/` extraction at `2ec64c0`, confirmed by `git show`; the telemetry and trace format against REQ-SYS-150 and ICD-SW-HOST.
- WP-SW-12: the algorithm page (polynomial, initial value, reflection, final XOR) with golden vectors, against REQ-SYS-132 and 07 section 14.2 row f.
- Every datasheet citation checked against the printed page. Every figure recomputed.
- The keyer study SA finding-4 cases that the note takes on: the row j budgets that are active when a write is allowed.

## Commands run by the reviewer (evidence)

| # | Command | Result |
|---|---|---|
| C1 | `git archive 9fda694` into the scratchpad, drafts copied in; `.venv/bin/python docs/design/analysis/fw-b1-dml3/check_fw_b1_dml3.py --out <scratch>` | exit 0; "54 assertions, 0 failed"; 1.4 s. The regenerated results file is byte-identical to the draft (`cmp`) |
| C2 | the same export: `.venv/bin/python tools/validate_docs.py` | 117 passed, 0 failed |
| C3 | the same export: `.venv/bin/python tools/traceability.py` | 245 requirements, 173 test cases, 0 violations, 2 warnings (REQ-SYS-125 and 148 `SYS_UNALLOCATED`, which exist before this product). Run in the export only, so the repository `docs/vv/traceability-report.md` and `traceability.json` were not touched |
| C4 | reviewer script `reviewer_check.py`, written without the author's code: CRC-32 as MSB-first long division on bit-reversed bytes (Rocksoft definition), GF(2) order of x, syndromes and a concrete weight-4 search, telemetry line CRCs and lengths, UART divisors | every result below; output kept in the reviewer scratchpad as `reviewer_check.txt` |
| C5 | `pdftotext -layout` of each cited PDF page (printed page + 1) of the rustos datasheet at `1b26078d`, and of the Pico 2 datasheet at `9f84bce2` | each page footer equals the printed page the note cites (37 pages checked) |
| C6 | `git rev-parse be49be6:<path>` and `HEAD:<path>` for each repository input of note section 2 | all 11 blobs, plus ADR-051 `7085cf5a` and ADR-052 `58c06b4f`, equal the note and HEAD |
| C7 | `git -C ~/rust/rustos ls-tree 2ec64c0 docs/icd/rp2350/uart/` | the five blobs of note section 5.2 (`0dfc6cd4`, `a40e5647`, `60e02033`, `36b995b3`, `0c6d6f9c`) are the same |

`test_ltspice_batch` was not run: no LTspice tool is in scope for this product.

## Findings (iteration 1, states as filed then)

| Finding | Origin | Severity | Item | Location | Description | State | Deferred to |
|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | reviewer | Major | CK-DES-A6, CK-DES-D13, CK-DES-H1 | Note sections 4.5, 4.6 and section 7 row "Bounded masked window"; ICD `02_programming.md` "cwht window design" steps 2 to 4 | The note does not say how the scheduler treats the planned 401 ms window. 07 section 14.2, `SW-SCHED` row, requires "every monitor task dispatched within its period, and the watchdog (2 s, REQ-SYS-131) kicked only when all ran". It also treats "a tick overrun or a missed monitor deadline" as an error with response class safe state. A 401 ms window with PRIMASK set misses about 400 ticks of the 1 ms tick. It also misses the deadline of every monitor with a shorter period: the 1 kHz key sampler, the 20 Hz PA temperature sample (REQ-SYS-118) and the 100 ms RAM-copy CRC (row f). As 07 is written, every commit is then an overrun that drives `safe_state()`. If the kick decision holds back the kick after missed deadlines, the watchdog (fed only before the window) expires 1.0 s later, and every settings commit becomes a reset. The ratio of 2 also compares the load with the window alone, not with the whole time from the feed before the window to the first kick after it. **Fix:** make the store window a state the dispatcher declares. The overrun and deadline checks leave it out up to a stated bound (for example 496 ms, section 4.5) and treat a longer window as an overrun. The watchdog is fed right after the window, and the monitors run before the next kick decision. Bound the longest time without a kick and compare that with the load. Add this to requests R-1 and R-4 (WP-PDR-32 `SW-SCHED`, WP-PDR-35), and add a DML-5 check: a commit with the monitors running gives no overrun fault and no watchdog reset | Open | |
| <a id="finding-2"></a>finding-2 | reviewer | Major | CK-DES-C10 | Note section 4.6, the sentence "the active row j items are ..." and its table | The list of row j budgets active in Receive leaves out REQ-SYS-155 (Active; 100 ms and range TBR): enter Fault-safe within 100 ms of the PA temperature reading leaving -20 C to +150 C. The requirement has no mode qualifier, so it applies in Receive, where the note allows writes. 07 row j lists it ("PA temperature reading out of range to Fault-safe within 100 ms"). A 401 ms window plus one 50 ms sample at 20 Hz gives about 451 ms. That exceeds the budget, and the response is entry to Fault-safe with its annunciation, a mode change that cannot be set before the window. The keyer study SA finding-4, which this section answers, named "thermal 100 ms" among the budgets to compare. **Fix:** add the row. Give the argument: PA_EN is already low in Receive, so the hazard response state holds during the window, and only the Fault-safe entry and its annunciation are late. Send it as a request to the REQ-SYS-155 TBR closure (a value that allows the window, or a mode-qualified wording), or shorten the window below 100 ms. Also list the other row j items with the reason each one is inactive in Receive (REQ-SYS-004, 075, 118, key-up, over-current), so that the table is complete | Open | |
| <a id="finding-3"></a>finding-3 | reviewer | Minor | CK-DES-A2 | Note section 4.5, row "Ratio of the load to the longest window" | The ratio 2.48 is 1.0 s / 404 ms, the one-window form. For the design window of 401 ms it is 2.49 (1.0 / 0.401 = 2.494). In the table and in the author's summary, 2.48 sits next to 401 ms. The ICD page `02_programming.md` states it correctly ("2.48 times the 404 ms window"). **Fix:** label the row as the one-window form, or give both ratios | Open | |
| <a id="finding-4"></a>finding-4 | reviewer | Minor | CK-DES-D9 | Note section 4.7 "Wear"; request R-5 | The rate rule (at most one commit per 60 s) allows up to 1440 commits a day. That is 26 times the 54.8 a day that the 100 000-cycle endurance (A-F4) allows over 10 years. At the rule's maximum, a sector wears out in 139 days (2 x 100 000 / 1440, reviewer C4). The "expected 20 per day" that gives the factor 2.7 is not a numbered assumption. **Fix:** make the expected rate an assumption with its invalidation. Then either add a wear bound the design enforces (for example a commit counter in the record with a stated response at a budget), or state why wear-out is acceptable: an erase failure keeps the previous copy (row k), at the cost of REQ-SYS-135 | Open | |
| <a id="finding-5"></a>finding-5 | reviewer | Minor | CK-DES-D9, CK-DES-D10 | Note section 4.4 and request R-3; ICD `02_programming.md` "UF2 downloads"; ICD `index.md` "cwht Driver Notes" | The proposed layout places copy A, copy B and the unused E10 sector, and ends the application `FLASH` region at 0x3FD000. The `SW-DIAG` event log is not placed. It is also a flash ring (07 section 16.5), the ICD index names it among the WP-SW-08 users, and RSK-021 names it in its condition. Its sectors need the same last-sector rule. **Fix:** state that the log sectors lie below 0x3FD000 (the `FLASH` end moves down by their size) and that they avoid the last sector. Otherwise, name this as a FW-B2 constraint in R-3 | Open | |
| <a id="finding-6"></a>finding-6 | reviewer | Minor | CK-DES-E2, CK-DES-I3 | Note section 4.3, first sentence; ICD `02_programming.md`, sentence after the datasheet sequence | Both texts say QMI is in direct mode from `flash_exit_xip` until the range function returns. The datasheet says otherwise. `flash_exit_xip` also sets up a basic 03h XIP mode, and the device should be readable by XIP afterwards (5.4.8.7, printed p385). The bus-fault interval is the duration of the erase or program operation (5.4.8.10, p387). The bootrom leaves flash in basic XIP between operations (5.4.8.9, p387). The ICD's own next sentence says reads work between operations. The stated interval is wider than the datasheet's. That is on the safe side, because the design keeps the whole window in SRAM, so no value changes. **Fix:** state the datasheet interval, and keep the SRAM-only window as a design choice | Open | |
| <a id="finding-7"></a>finding-7 | reviewer | Minor | CK-DES-H4 | Note section 4.3, DMA row; ICD `index.md` "cwht Driver Notes", second bullet | The DMA row cites 07 section 19, WP-SW-12 "no DMA sniffer dependency". That row only says the CRC does not use the sniffer; it says nothing about other DMA use. The real basis is that the 07 section 19 table has no DMA work package. Separately, the ICD index says that masking interrupts on core 0 "stops every flash fetch except the debugger's". That leaves out DMA, which the `02_programming.md` constraint table does list. **Fix:** cite the work-package table, make "no DMA channel configured" a design rule for WP-PDR-32 (R-1), and correct the index sentence | Open | |
| <a id="finding-8"></a>finding-8 | reviewer | Minor | CK-DES-F3 | Note section 5.3 row "Line capacity and load"; section 5.4 | The load uses 40 B per TX_KEY event line. With the note's own format, the EVT TXKEY line is 45 B at `seq` 65535 after one hour of uptime and 46 B after 10 hours. At the u64 `t_us` maximum used for the longest STAT line, it is 55 B (reviewer C4). At 46 B the peak is 2837 B/s, 24.6 % of the line, still under the 50 % limit. The 120-byte maximum is shown for STAT only. MODE (`cause`), FLT (`code`, `cause`) and BOOT (`fw`) have tokens with no length limit. **Fix:** size each record type at its longest fields, as done for STAT, and give ICD-SW-HOST a token length limit (R-6) | Open | |
| <a id="finding-9"></a>finding-9 | reviewer | Minor | CK-DES-C4, CK-DES-C5 | Note section 4.6, row "VBUS to transmit disarm" | "transmit disarmed for the window ... re-armed only through the Arm condition" does not say what happens to the operator's TX-armed state after a commit. That state is set by a distinct operator action once per power cycle (07 section 14.2 row d). If each commit clears it, the operator has to re-arm after every menu exit, and that effect on the operator needs to be stated. If it comes back by itself, the "Arm condition" needs a definition that cannot bypass the key-closed interlock or the VBUS inhibit. **Fix:** say which, and add it to R-4 for WP-PDR-35 | Open | |
| <a id="finding-10"></a>finding-10 | reviewer | Minor | CK-DES-A2 | Note section 6.4, "512-byte record"; checker lines 243 to 246 | The 512-byte result is the stated reason for the one-page record, but the checker only prints it as INFO; it does not assert it. The reviewer confirmed it separately (C4): on a 512-byte record, flipping codeword bits 791, 931, 1582 and 3797 passes the CRC check. **Fix:** assert it in the checker and give the example in the note | Open | |
| <a id="finding-11"></a>finding-11 | reviewer | Minor | CK-DES-E2, CK-DES-I3 | ICD `01_bootrom_api.md` "5.4.1 Locating the functions" and its table row `'X','F'`; note section 4.2 and D2 | `xip_setup_func_ptr` (`'X','F'`) is ROM data, not a function. 5.4.6 (p380) says that entries without parentheses are data pointers, and 5.4.6.5 (p381) lists it that way. The SDK looks data up through `rom_data_lookup` with `RT_FLAG_DATA` (p377). The ICD and the note give only `RT_FLAG_FUNC_ARM_SEC`, so a driver written from the text would not find the XIP setup pointer. **Fix:** give the data lookup flag for `'X','F'` (and for `'F','D'` if it is used) | Open | |
| <a id="finding-12"></a>finding-12 | reviewer | Minor | CK-DES-A2 | Note section 6.2 (reference form: "`const` table of 256 `u32`"); A-F7; section 6.5 | A-F7 (12 cycles per byte) assumes the table is in SRAM. The reference form makes it a `const`, which is placed in flash by default. The note also allows a flash table served from the XIP cache. During the image check, 2 MiB of image passes through the 16 kB two-way cache (p341), so a table in flash can be evicted and the cost per byte rises. The 557 ms and 1.59 s results depend on this. **Fix:** make SRAM placement (a `static` in `.data`) a design rule in R-7 or R-8, or bound the cost with the table in flash | Open | |
| <a id="finding-13"></a>finding-13 | reviewer | Minor | CK-DES-H1 | Note section 4.9 | The PDR work plan section 7 row "FW-B1 WP-SW-08 (flash write) ... beyond DML-3" says that if the owner has not merged the ICD pull request before F1, the DML-3 note cites the cwht-side extraction and the merge becomes a CDR lien. The note cites only the rustos branch and names no cwht-side extraction. **Fix:** name note sections 2 (table D1 to D30) and 4.2 to 4.5 as the cwht-side extraction for that case, or add one | Open | |

Two Major findings, so `reviewer_verdict` is NEEDS CHANGES (07 section 10.2; plan rule C1). The flash-write proof otherwise stands. That covers the fetch-source closure, the E10 finding and layout, the power-loss table and the time budget against A-7. So do the UART proof and the whole CRC-32 page. Finding-1 and finding-2 are about how the stall fits with the scheduler and with one row j budget. They do not change the window length.

## Readiness criteria

| # | Criterion | Result | Evidence |
|---|---|---|---|
| R1 | Every figure rendered and inspected | N/A | The product has no figure. Every result is a table, and the tables are recomputed by the checker (C1) and by the reviewer (C4) |
| R2 | `tools/traceability.py` | Yes | 0 violations (C3). The note allocates no `REQ-SW-*`. The `design_refs` for `SW-CFG`, `SW-BOOT` and `SW-DIAG` come with WP-PDR-35 |
| R3 | The requirements are Active | Yes | REQ-SYS-131, 132, 134, 135, 150 and 155 are Active at `f128235e`. REQ-SYS-131 and 155 carry TBRs that close at PDR |
| R4 | The author's return lists the criteria and a self-check | Yes | The author's summary gives the checker result, `validate_docs.py` and `traceability.py` results, each package result and the rustos branch state. Each was re-run and holds (C1 to C3) |

## Datasheet citations (CK-DES-E2, CK-DES-H4)

Each citation was checked on the printed page of the rustos datasheet (build 2025-02-20; PDF page = printed page + 1, confirmed on all 37 pages, C5).

| Ids | Section and printed page | Reviewer reading |
|---|---|---|
| D1, D2 | 5.4.1, Table 452, p376; p377 | Magic `'M','u',0x02` at 0x10, version at 0x13, table and lookup pointers at 0x14 to 0x19; the Arm lookup uses `RT_FLAG_FUNC_ARM_SEC` for functions (data items: finding-11) |
| D3 | 5.4.3, p378 | -4 `NOT_PERMITTED`, -10 `INVALID_ADDRESS`, -11 `BAD_ALIGNMENT`, -19 `LOCK_REQUIRED` |
| D4 | 5.4.4, p379 | `LOCK_ENABLE` (lock 7) off by default; direct-mode programming makes XIP return a bus fault |
| D5 | 5.4.6.1, p380 | The six low-level functions are Arm-S and RISC-V only |
| D6 to D8 | 5.4.8.3, p384; 5.4.8.5 and 5.4.8.7, p385 | As cited. The default `FLASH_DEVINFO` is 16 MB on CS0. `flash_exit_xip` also leaves basic 03h XIP at CLKDIV 12 (finding-6) |
| D9 to D12 | 5.4.8.8 to 5.4.8.11, p386 to 387 | As cited: flush unpins lines; `flash_op` checks; the range functions validate nothing; erase is 4096-aligned, program 256-aligned; the XIP fault is for DMA, the debugger or the other core during the operation |
| D13, D14 | 5.4.8.14, p388; 5.4.8.30, p398 | Modes 0 to 3 with an 8-bit command prefix; `'X','F'` is a data item (finding-11) |
| D15 | 5.2.7, Table 451, p372 to 373 | 16 attempts starting with EBh quad at divisor 3 and ending with 03h at 24 |
| D16 | 5.5.2, p400 | UF2 downloads always erase a whole 4 kB sector |
| D17 | Appendix E, RP2350-E10, p1350 to 1351 | A2 silicon; drag and drop fails with a partition table; the workaround block goes at the start of the UF2, targets the end of flash, is written first and does not reboot |
| D18 | 4.4, 4.4.1, p341 (line size also on p342) | Windows 0x10, 0x14, 0x18, 0x1c; 16 kB two-way cache with 8-byte lines; coherence matters only around programming |
| D19 to D21 | 12.14.5, p1232; Table 1292, p1233 to 1234; p1239 | Direct mode disconnects XIP; base 0x400d0000; `DIRECT_CSR` 0x00, `M0_TIMING` 0x0c; `CLKDIV` bits 7:0, reset 0x04, can change on the fly |
| D22, D23 | 3.2.1, p83; Table 362, p232 | NMI ignores PRIMASK; the RCP NMI asserts on a failed integrity check; `NMI_MASK0` resets to 0 |
| D24, D25, D28 | Table 94, p82; 2.2, p32; Table 534, p503 | `UART0_IRQ` 33; `UART0_BASE` 0x40070000; `RESET` bit 26 UART0 |
| D26, D27 | 12.1.1, p958; 12.1.3.2.1, p961 to 962 | PL011; 32 x 8 TX FIFO; UARTCLK is `clk_peri`; 16 x baud to 16 x 65535 x baud; FBRD = frac x 64 + 0.5 |
| D29 | Table 1435, p1335 to 1336 | At IOVDD 3.3 V: VIH 2 V, VIL 0.8 V, VOH 2.62 V, VOL 0.5 V |
| D30 | 12.6.8.2, p1104; `SNIFF_CTRL`, p1133 | CRC-32 (IEEE 802.3), MSB-first and bit-reversed |
| Pico 2 | Pico 2 datasheet (rustos `9f84bce2`) ch. 1, printed p4 | W25Q32RV flash; IO fixed at 3.3 V |

ICD page register details were also checked: `DIRECT_CSR` bits and `CLKDIV` reset 0x06 (Table 1293, p1235 to 1236), `ATRANS0` to `ATRANS7` at 0x34 to 0x50, 4 MiB each (p1234), translation downstream of the cache (12.14.4.2, p1232), and the rp2350 index row page ranges 340 to 351, 372 to 400 and 1223 to 1246. The note's L-4 observation is correct: Table 534 is on printed page 503, so the WP-SW-01 and 03 pages' "p504" is the PDF index. That belongs to those records (cross item X-2).

## Reviewer recomputation (C4)

| Claim | Note | Reviewer |
|---|---|---|
| V1 to V11 | as tabled | all 11 equal the reviewer's own long-division CRC-32; residue 0x2144DF1C |
| Primitive polynomial, 15 terms | yes | x^(2^32-1) = 1 and x^((2^32-1)/q) != 1 for q in 3, 5, 17, 257, 65537; order 2^32-1 means the polynomial is irreducible and primitive |
| 256-byte record, weights 1 to 4 all detected | HD at least 5 | reviewer syndrome test: all detected. This agrees with the published HD 5 limit of this polynomial for about 3000 data bits |
| 512-byte record, some weight 4 missed | HD 4 | a concrete pattern, confirmed by corrupting a record (finding-10) |
| Golden telemetry lines | CRC and length | all 5 CRCs agree; 54, 74, 79, 38 and 103 bytes |
| Divisors | IBRD 52 FBRD 5 (+0.0100 %); IBRD 81 FBRD 24 (+0.0064 %) | same |
| Capture tolerance | 4.05 % | (0.5 - 1/8.68) / 9.5 = 4.05 % |
| Load | 2587 B/s, 22 % | same arithmetic; basis Minor (finding-8) |
| Window, ratio, erase limit | 401 / 404 ms, 2.48, 496 ms | 0.401 and 0.404; 2.49 and 2.48 (finding-3); 0.5 - 0.004 = 0.496 |
| Image check | 17, 70, 279, 557 ms at 96 MHz; 3.41 s in 03h/12 | same (25.5 and 156 cycles per byte); 263 529 B (257 KiB) for A-8 |
| RAM-copy CRC | 32 us, 0.03 % | same |
| Wear | 54.8 a day, factor 2.7 | same; worst case under the rule 139 days (finding-4) |
| E10 alias | 0xFFFF00 to 0x3FFF00, sector 0x3FF000 | same, under A-F3; A and B at 0x3FD000 and 0x3FE000 avoid it whether or not A-F3 holds |

## Checklist answers

### A. Architecture content

| Id | Answer | Evidence |
|---|---|---|
| CK-DES-A1 | N/A | The note is a DML-3 analysis, not the architecture. Component names (`FlashStore`, `SW-CFG`, `cwht-core` CRC) follow 07 section 19 |
| CK-DES-A2 | Yes, except findings 3, 10 and 12 | The masked window, erase limit, UART load, CRC CPU share and image-check times are quantified with their assumptions |
| CK-DES-A3 | Yes | UART0 pads (REQ-SYS-142, 150) at 3.3 V with levels; the flash device and its bootrom interface; the pin numbers belong to ICD-CTL-SW (WP-PDR-36a) |
| CK-DES-A4 | N/A | No trait boundary is defined at DML-3 (FW-B2) |
| CK-DES-A5 | Yes | Commit states idle, erasing, programming and verifying (07 row b) with the load result in each (section 4.7) |
| CK-DES-A6 | No | Concurrency: PRIMASK for up to 401 ms and its effect on the single-priority tick and monitor dispatch are not reconciled with `SW-SCHED` (finding-1) |
| CK-DES-A7 | Yes | Criticality is stated in the header row "Analysis kind" (`SW-SAFE` `cfg_guard`, `SW-BOOT`, HZ-014) |
| CK-DES-A8 | N/A | No band-dependent content |

### B. Traceability

| Id | Answer | Evidence |
|---|---|---|
| CK-DES-B1 | N/A | No `REQ-SW-CFG`, `SW-BOOT` or `SW-DIAG` file exists yet (WP-PDR-35). The system requirements are traced in section 1 and section 7 |
| CK-DES-B2 | Yes | HZ-014 (image and configuration) is named. The stall goes to WP-PDR-16 as a candidate cause (R-4) |
| CK-DES-B3, B4 | N/A | No code or design units yet (FW-B2) |
| CK-DES-B5 | N/A | Not a CR. The layout change is routed as request R-3, and no requirement or ICD file is edited |

### C. Safety design provisions

| Id | Answer | Evidence |
|---|---|---|
| CK-DES-C1 | N/A | Boot order is not in scope. The image check runs after the clock bring-up (R-7) |
| CK-DES-C2 | N/A | No transition table |
| CK-DES-C3 | Yes | A fault in the window locks the core up and the running watchdog resets it (section 4.3). No new termination path is added |
| CK-DES-C4 | Yes, except finding-9 | The write is allowed only in Receive with the key open (keyer study R-2). Re-arm after the window is not stated |
| CK-DES-C5 | Yes | The `plan` decision function accepts only the two store sectors. Other requests are rejected before any ROM call (section 4.2; row e) |
| CK-DES-C6 | Yes | Two CRC-32 copies with a `u32` sequence number, erased and zero records rejected, RAM copy every 100 ms, image trailer at boot (sections 4.7, 6) |
| CK-DES-C7 | Yes | Read-back after each operation (row g), because the range functions return nothing |
| CK-DES-C8 | N/A | Not the PA_EN prerequisite function |
| CK-DES-C9 | N/A | No new hazard argument |
| CK-DES-C10 | No | Row j budgets during the window: REQ-SYS-155 is missing (finding-2), and the scheduler overrun and kick rule is not covered (finding-1) |
| CK-DES-C11 | Yes | Bounded retry, then the previous copy is kept and logged (row k, section 4.1) |
| CK-DES-C12 | N/A | No state machine |
| CK-DES-C13 | N/A | Decision tables for `plan` come in FW-B2 |
| CK-DES-C14 | Yes | Integer CRC and sequence number; no floating point |
| CK-DES-C15 | Yes | `plan` is a host-tested pure function; the window function holds no decision |

### D. Detailed design adequacy

| Id | Answer | Evidence |
|---|---|---|
| CK-DES-D1, D2 | N/A | DML-3; signatures come in FW-B2 |
| CK-DES-D3 | Yes | Record 256 B (252 covered plus 4 CRC, little-endian), `u32` sequence, telemetry field types and ranges |
| CK-DES-D4 | N/A | Not the keyer |
| CK-DES-D5 | Yes | UART uses no interrupt (section 5.3); no other ISR |
| CK-DES-D6 | Yes | 1 KiB ring, 1 KiB table, 12 KiB of flash reserved; placement of the table and the log: findings 12 and 5 |
| CK-DES-D7 | Yes | HostUnit (`plan`, store state machine, CRC vectors) plus six DML-5 dev-board checks. The emulator is not credited for flash (section 4.8) |
| CK-DES-D8 | N/A | No code |
| CK-DES-D9 | Yes, except findings 4 and 5 | Two copies, CRC-32, sequence, write from task context with PRIMASK, XIP handling per WP-SW-08 |
| CK-DES-D10 | N/A | The event log design is FW-B2 (section 1, out of scope). Its placement constraint is finding-5 |
| CK-DES-D11 | Yes | Audio muted before the window (section 4.6) |
| CK-DES-D12 | N/A | Not the synthesizer, envelope or display |
| CK-DES-D13 | No | The `SW-SCHED` overrun and kick decision around the window is missing (finding-1) |

### E. Interfaces and ICD consistency

| Id | Answer | Evidence |
|---|---|---|
| CK-DES-E1 | N/A | Pin numbers belong to ICD-CTL-SW (WP-PDR-36a) |
| CK-DES-E2 | Yes, except findings 6 and 11 | 30 citations checked on their printed pages (table above) |
| CK-DES-E3 | Yes | Part timing is assumption A-7 with its closure (R-9, DML-5); the 496 ms tolerance is stated |
| CK-DES-E4 | N/A | The UART or USB choice is OD-15; the note is stated for UART0 |

### F. Cybersecurity

| Id | Answer | Evidence |
|---|---|---|
| CK-DES-F1 | Yes | Image CRC trailer and configuration integrity (section 6); host writer on `zlib.crc32` (R-8) |
| CK-DES-F2 | Yes | No receive parser is proposed. The CS-33 conflict with the test-case injection commands is raised as L-3 for ICD-SW-HOST |
| CK-DES-F3 | Yes, except finding-8 | Fixed 1 KiB ring; whole-line drop with a counter; 120-byte line maximum |

### G. Reuse and dependencies

| Id | Answer | Evidence |
|---|---|---|
| CK-DES-G1 | Yes | Bootrom functions through WP-SW-08; CRC in `cwht-core` (WP-SW-12) |
| CK-DES-G2 | Yes | No crate introduced |

### H. Consistency and presentation

| Id | Answer | Evidence |
|---|---|---|
| CK-DES-H1 | No | 07 section 14.2 `SW-SCHED` row: "a tick overrun or a missed monitor deadline is an error with response class safe state". Note section 4.6: "While PRIMASK is set, no 1 kHz sample, monitor or alarm runs for up to 401 ms" (finding-1). Also the plan section 7 fallback (finding-13) |
| CK-DES-H2 | N/A | No figures |
| CK-DES-H3 | Yes | Note 352 lines; ICD pages 71 to 99 lines; each index links its pages |
| CK-DES-H4 | Yes, except finding-7 | Every corpus id exists; all blobs are confirmed (C6, C7) |

### I. Interface control documents (applied to the rustos flash register ICD)

| Id | Answer | Evidence |
|---|---|---|
| CK-DES-I1, I2 | N/A | A rustos register ICD in the rustos house layout (`index.md` plus numbered pages under 500 lines, like `uart/` and `pwm/`), not an `ICD-<A>-<B>` document |
| CK-DES-I3 | Yes, except findings 6 and 11 | Functions with codes and signatures, register offsets and fields, every value with units, part-timing values marked (A) with their source, E10 rule and time budget |
| CK-DES-I4 | N/A | No physical interface |
| CK-DES-I5 to I7 | N/A | Pairing, external constraints and verification belong to the cwht ICDs (ICD-SW-HOST, ICD-CTL-SW) |
| CK-DES-I8 | Yes | New pages, one commit, not merged; the owner's merge is OD-23 |

### J. Hardware design products

CK-DES-J1 to J10: N/A (software analysis and register ICD).

## Cross items for the lead SE (not findings on the product)

- **X-1 Freeze.** Plan rule C2 asks for a committed product. The three cwht files are drafts (harness restriction), so this record is tied to their `git hash-object` blobs in `product_files`. Filing them with other bytes needs a delta iteration.
- **X-2 L-4.** The page citation errors the note reports in the rustos WP-SW-01 and WP-SW-03 pages are real (Table 534 is on printed p503; the pages cite p504). They belong to INSP-095 and INSP-099, not to this record.
- **X-3 Credit.** The checker has no TV record, so its results are developer evidence (note header "Credit"). The values go out as requests R-1 to R-9, not as ruled values.
- **X-4 Merge order.** The ICD branch is stacked on `cwht/wp-sw-03`, so its merge waits for the five driver merges. OD-23 (drivers by Thu 10-01, ICD page by Fri 10-02) allows this order. If a driver branch is refused, the plan section 7 fallback applies (finding-13).
- **X-5 SA pair.** finding-1 and finding-2 overlap the open keyer study SA finding-4, which stays with that record (the note says so in section 4.6).

## Measurements (SWE-089)

Size: 1 note (352 lines), 1 checker (380 lines, 54 assertions), 1 results file, 4 ICD pages plus 1 index row; 30 datasheet citations and 37 printed pages checked. Turns 70, minutes 95. Major 2, minor 11.

## Record verdict (first iteration)

```
VERDICT: NEEDS CHANGES
FINDINGS:
- [Major] CK-DES-A6/D13/H1 note 4.5, 4.6; ICD 02: the 401 ms window is not reconciled with the SW-SCHED overrun, deadline and watchdog-kick rules.
- [Major] CK-DES-C10 note 4.6: REQ-SYS-155 (Fault-safe within 100 ms of a PA temperature reading out of range) is active in Receive and exceeded by the window.
- [Minor] findings 3 to 13 (ratio label, wear worst case, event-log placement, direct-mode interval, DMA evidence, EVT line size, re-arm, 512-byte assertion, data lookup flag, CRC table placement, plan fallback).
ITEMS N/A: CK-DES-J1 to J10; the section A to I items marked N/A above
MEASUREMENTS: size=1 note, 1 checker, 1 results, 4 ICD pages; turns=70; minutes=95; major=2; minor=11
```

The record verdict is NEEDS CHANGES. It stays held at NEEDS CHANGES while CR-012 is unmerged and until the software assurance pair is APPROVED, even after the reviewer delta verifies finding-1 and finding-2.

## Iteration 2: delta verification of finding-1 and finding-2 (Major) (2026-09-29, cwht HEAD `82f1df8`)

**Scope (rule C1).** Iteration 2 is a delta that verifies the fixes of the two Major findings. The author fixed only the Major findings of this record and of its SA pair (SA findings 1 to 3) and held the eleven Minor findings (note revision 1, change log). Product: the note revision 1 (draft blob `8a403ddb`, 440 lines), its checker (`03c960dc`, 83 assertions) and results file (`225e23c4`), all drafts not yet in the repository; and rustos branch `cwht/wp-sw-08` at `00d5383`, one fix commit on top of `03b1997` with no amend (`git diff --stat 03b1997 00d5383`: `02_programming.md` 56 lines and `flash/index.md` 13 lines changed; `01_bootrom_api.md`, `03_xip_qmi.md` and `docs/icd/rp2350/index.md` keep their iteration 1 blobs). The checklist is `peer-review-checklist-design.md` revision B, as at iteration 1. The whole fix text was read: note sections 1, 3, 4.1 to 4.9, 7, 8, 9 and 10, and both changed ICD pages. New findings are raised only on the fix text.

**Independence (rule C4).** This invocation wrote no part of the note, its checker, its fix round (the author's scratch scripts `sw08fr1/` were not used) or the rustos commits, and edited no product file.

**Search first (rule C3).** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran first (queries: the DML-3 flash window, watchdog and REQ-SYS-155; ADR-053 missed-match `Due`; the review-record state rule). `grep` then only pinned lines in the files it returned or in known paths (07, the plan, the requirement file).

**rustos access.** Committed objects only: `git -C ~/rust/rustos log`, `show 00d5383`, `diff --stat` and `rev-parse 00d5383:<path>`. The rustos working tree was not read or changed. The datasheet is the committed copy used at iteration 1 (blob `1b26078d`), already in the reviewer scratchpad.

### Commands run by the reviewer (evidence)

| # | Command | Result |
|---|---|---|
| D1 | `git hash-object` of the three drafts, copied to the reviewer scratchpad (`rv132d/`) so the reviewed bytes stay fixed | `8a403ddb`, `03c960dc`, `225e23c4`, as in `product_files` |
| D2 | `git archive 82f1df8` into the scratchpad, drafts copied in; `.venv/bin/python docs/design/analysis/fw-b1-dml3/check_fw_b1_dml3.py --out <scratch>` | exit 0; "83 assertions, 0 failed"; 1.3 s. The regenerated results file is byte-identical to the draft (`cmp`) |
| D3 | the same export: `.venv/bin/python tools/validate_docs.py`, without and then with this record draft | 117 passed, 0 failed; with the record, 118 passed, 0 failed (its latest iteration section shows 13 open findings, all Minor, and no open Major) |
| D4 | the same export: `.venv/bin/python tools/traceability.py` | 245 requirements, 173 test cases, 0 violations, 2 warnings (REQ-SYS-125 and 148 `SYS_UNALLOCATED`, as at iteration 1). Run in the export only; the repository `docs/vv/traceability-report.md` and `traceability.json` were not touched |
| D5 | reviewer script `rc2.py`, written without the author's code, for every new number of the fix | results in the recomputation table below; output `rc2.txt` in the reviewer scratchpad |
| D6 | `git rev-parse HEAD:<path>` at `82f1df8` for `requirements.json`, 07 and the keyer host study | `f128235e`, `bfe05f43`, `32f4a139`: the blobs note section 2 cites |
| D7 | Requirement text read from `requirements.json`: REQ-SYS-067, 118, 131, 155, 181 (and the 07 section 14.2 rows c, e, f, h, j and the `SW-SCHED` row, lines 597 to 640) | quoted in the verification tables and findings below |
| D8 | `pdftotext -layout` of printed pages 387, 400 and 1351 (PDF 388, 401, 1352) | 5.4.8.10: "For the duration of the erase operation, QMI is in direct mode"; 5.5.2: "The flash is always erased a 4 kB sector at a time"; E10 workaround block "written to flash first". The fix adds no new datasheet citation; the layout change (log reserve) and the window steps rest on these pages only |

`test_ltspice_batch` was not run: no LTspice tool is in scope for this product.

### Verification of finding-1, case by case (rule C7)

| Case | Required by finding-1 | At note `8a403ddb` and rustos `00d5383` | Result |
|---|---|---|---|
| Window as a declared scheduler state | the store window is a state the dispatcher declares, with a stated bound | Note 4.6.2 steps 2 and 4: `StoreWindow { start, bound }` entered by `SW-SCHED` before the store step, bounds 10 ms (program) and 450 ms (erase) from the task table; ICD `02_programming.md` "cwht window design" steps 2 and 5 say the same | Verified |
| Overrun and deadline checks | a window within its bound is not an overrun; a longer window is an overrun with response class safe state | Note 4.6.2 step 4 (TIMER0 read after the window; over the bound: `safe_state()`, logged, 07 rows c, k, l; within it: a separate store-stall count) and step 5 (deadline rule); MSR-26 keeps "Overruns 0" outside declared windows, and counts every window over its bound | Verified (over-bound case: finding-15) |
| Monitors before the next kick | the watchdog is fed after the window and the monitors run before the next kick decision | Note 4.6.2 step 5: a catch-up pass runs every monitor on fresh samples, then the kick decision. The only kick is the main loop's (step 1, the only holder of the `Watchdog` handle) | Verified |
| Longest time without a kick | bounded, and compared with the load | 1 ms + 401 ms + 1 ms = 403 ms (A-7, A-F2, A-F8); 452 ms at the 450 ms bound; 1.0 s / 0.403 s = 2.48 and 1.0 s / 0.452 s = 2.21, both at least 2; the largest bound that keeps the factor 2 is 498 ms. Checker lines 301 to 323 assert each value (run D2 output lines 30 to 36); reviewer D5 agrees | Verified |
| Requests | R-1 (WP-PDR-32 `SW-SCHED`) and R-4 (WP-PDR-35) carry the rule | R-1 carries the declared state, the bounds, the overrun rule, the catch-up pass, the deadline rule, the main-loop-only kick, the 452 ms bound and the MSR-26 counting, and goes also to the writer of 07 (plan section 5.3). R-4 carries the pre-window outputs, the row j table and the 547 ms battery supervision period | Verified |
| DML-5 check | a commit with the monitors running gives no overrun fault and no watchdog reset | Note section 9 item 7: HostUnit of the declared-window logic on the mock clock, and a dev-board run with every monitor running and the watchdog at 1.0 s: zero overruns, zero resets, longest time between kicks at most 452 ms | Verified (pass criteria: finding-15) |
| Alternatives | not required by finding-1 (SA finding-2) | Note 4.6.5 compares four options; page-append records adopted (4.7). Checked under this lens only for consistency: option B numbers agree with D5 (7.5 erase windows a day; boot scan 2.2 ms); option C 1.988 s, 12 ms margin, 2.389 s with two sectors | Consistent (new design detail: finding-16) |

The kick rule also answers SA finding-1: the driver never touches the watchdog (note 4.6.2 step 3, ICD constraint row), and the checker shows the rejected driver-side feed at 2.1 s to Self-test (2 x 1.0 s + 0.1 s), over the 2 s of REQ-SYS-131. Verification of the SA findings belongs to the SA delta; this record notes only that the reviewer found no conflict with finding-1.

### Verification of finding-2, case by case (rule C7)

| Case | Required by finding-2 | At note `8a403ddb` | Result |
|---|---|---|---|
| REQ-SYS-155 row | the row is added to the row j table | Note 4.6.3: "PA temperature reading out of range to Fault-safe within 100 ms (REQ-SYS-155) - Yes - met in a program window; exceeded in an erase window" | Verified |
| Numbers | the latency during a window | Program window: the window starts in the pass that took a PA sample, so the gap stays the 50 ms of the 20 Hz path: 51 ms. Erase window: 403 ms to the catch-up sample plus 1 ms: 404 ms; 453 ms at the bound. Checker lines 340 to 345 (run D2 output lines 40 to 42); reviewer D5 agrees | Verified |
| Argument | PA_EN is already low, so the hazard response state holds; only the Fault-safe entry and its annunciation are late | Note 4.6.4 "Argument": PA_EN low and transmit disarmed during the window; REQ-SYS-181 hardware cut-off independent of firmware; REQ-SYS-067 display | Verified (two statements overreach: finding-14) |
| Route | a request to the REQ-SYS-155 TBR closure, or a window under 100 ms | R-11 to WP-PDR-28 (TBR group G5) and the WP-PDR-45 TBR sheet for the owner's ruling: (a) a mode-qualified value, or (b) 100 ms everywhere with every erase moved to boot (option C). The REQ-SYS-155 `tbr.plan` ("The PA thermal design at PDR fixes the sensor and its plausible range") is the right closure. L-5 records the open state | Verified (wording scope: finding-14) |
| Completeness | every other row j item with the reason it is active or not in Receive | Note 4.6.3 lists 15 items. Against 07 section 14.2 row j (line 624): manual-closure timeout, tune end, paddle no-gap and squeeze, test-mode timeout, key-up response, REQ-SYS-004, REQ-SYS-118, REQ-SYS-155, VBUS disarm, charge disable, audio limiter attack, receive mute (REQ-SYS-075), CPU watchdog, and the two 07 allocations (over-current, battery under-voltage). None is missing. Fault-safe is covered by the sentence after the table | Verified |
| Stall to hazard data | the stall goes to WP-PDR-16 | R-4: "configuration or log write stalls the monitors" as a candidate software cause | Verified |

### Reviewer recomputation, iteration 2 (D5)

| Claim | Note | Reviewer |
|---|---|---|
| Windows | 4 ms program, 401 ms erase | 4.0 and 401.0 ms |
| Longest time without a kick; ratios | 403 ms, 452 ms at the bound; 2.48, 2.21 | 403 and 452 ms; 2.481 and 2.212 |
| Largest bound for the factor 2; largest erase tolerated | 498 ms; 449 ms | 0.5 s - 2 x 1 ms = 498 ms; 450 - 1 = 449 ms |
| REQ-SYS-155 latency | 51, 404, 453 ms | 51, 404, 453 ms |
| Battery supervision period | at most 547 ms | 1000 - 452 - 1 = 547 ms |
| Wear, configuration | 2281 erases per sector in 10 years at 20 a day; 877 a day allowed; factor 44 | 2281.25; 876.7; 43.8 |
| Wear, event log | 2852 at 100 pages a day; factor 35 | 2851.6; 35.1 |
| Erase windows a day | 7.5 | 20/16 + 100/16 = 7.5 |
| Boot scan of 32 pages | 2.2 ms | 8192 B x (13.5 + 12) cycles / 96 MHz = 2.18 ms |
| Option C | 1.99 s (12 ms margin), over 2 s for two sectors | 1.988 s and 2.389 s |
| Rejected driver feed | 2.1 s | 2 x 1.0 + 0.1 = 2.1 s |
| Layout | log 0x3F5000 to 0x3FCFFF; `FLASH` ends 44 KiB below the device end | 0x3FD000 - 8 x 4096 = 0x3F5000; 0x400000 - 0x3F5000 = 44 KiB |
| STAT queue during an erase window at its bound | 66 B | 120 B x (0.452 + 0.1) = 66 B |
| Rate rule R-5 worst case (finding-4, held) | not stated | 1440 commits a day gives 164 250 erases per sector in 10 years, wear-out after about 6.1 years (iteration 1: 139 days under revision 0) |

### Checklist items re-answered for the fix

| Id | Iteration 2 answer | Evidence |
|---|---|---|
| CK-DES-A6 | Yes | Concurrency of PRIMASK with the tick, the monitors and the kick is reconciled by the declared window (finding-1 verification) |
| CK-DES-C10 | Yes, except finding-14 | Every row j item accounted for; REQ-SYS-155 argued and routed |
| CK-DES-D13 | Yes, except finding-15 | `SW-SCHED` overrun, deadline and kick rules around the window are stated |
| CK-DES-H1 | Yes, except findings 13, 14 and 17 | The note now agrees with the 07 `SW-SCHED` row through the declared-window exception it routes to the 07 writer (R-1) |
| CK-DES-A2 | Yes, except findings 10 and 12 | The new numbers are quantified with their assumptions (A-F8, A-F9) and asserted; finding-3 is overtaken (below) |
| CK-DES-D9 | Yes, except findings 4 and 16 | Page-append records with CRC and sequence; the event log placed and bounded |
| CK-DES-C4 | Yes, except findings 9 and 17 | Write conditions of note 4.6.1 |

The other items keep their iteration 1 answers.

### Findings (current state at iteration 2)

| Finding | Origin | Severity | Item | Location | Description | State | Deferred to |
|---|---|---|---|---|---|---|---|
| finding-1 | reviewer | Major | CK-DES-A6, CK-DES-D13, CK-DES-H1 | Note 4.5, 4.6.2, 7, 8 (R-1, R-4), 9 item 7; ICD `02_programming.md` | The planned window was not reconciled with the `SW-SCHED` overrun, deadline and kick rules | Verified (note `8a403ddb`, rustos `00d5383`) | |
| finding-2 | reviewer | Major | CK-DES-C10 | Note 4.6.3, 4.6.4, R-11, L-5 | REQ-SYS-155 was missing from the row j budgets active in Receive | Verified (note `8a403ddb`) | |
| finding-3 | reviewer | Minor | CK-DES-A2 | Note 4.5 | Ratio 2.48 sat next to 401 ms. The rewritten table gives 2.48 against the 403 ms longest time without a kick (1.0 / 0.403 = 2.48), and 2.21 at the bound; the ICD budget matches | Verified (overtaken by the finding-1 fix) | |
| finding-4 | reviewer | Minor | CK-DES-D9 | Note 4.7, R-5 | Page-append records raise the endurance rate from 54.8 to 877 commits a day, but the expected 20 a day is still not a numbered assumption (A-F9 covers the log only), and the R-5 limit of 1440 a day still wears a sector out, now after about 6.1 years (164 250 erases per sector in 10 years) | Open (lien, rule C1) | CDR readiness declaration |
| finding-5 | reviewer | Minor | CK-DES-D9, CK-DES-D10 | Note 4.4, R-3; ICD `02_programming.md` "UF2 downloads", `index.md` | The event log is now placed at 0x3F5000 to 0x3FCFFF, below the configuration sectors and out of the last sector, with the `FLASH` end moved to 0x3F5000; the checker asserts the alignment and the E10 exclusion | Verified (overtaken by the SA finding-3 fix) | |
| finding-6 | reviewer | Minor | CK-DES-E2, CK-DES-I3 | Note 4.3 first sentence; ICD `02_programming.md` line 17 | Direct-mode interval wider than the datasheet's; unchanged | Open (lien, rule C1) | CDR readiness declaration |
| finding-7 | reviewer | Minor | CK-DES-H4 | Note 4.3 DMA row; ICD `index.md` line 64 | DMA evidence and the index sentence; unchanged | Open (lien, rule C1) | CDR readiness declaration |
| finding-8 | reviewer | Minor | CK-DES-F3 | Note 5.3, 5.4 | EVT line size and token length limits; unchanged | Open (lien, rule C1) | CDR readiness declaration |
| finding-9 | reviewer | Minor | CK-DES-C4, CK-DES-C5 | Note 4.6.3 VBUS row | Re-arm of the operator's TX-armed state after a window; unchanged in the note, and the ICD now differs (finding-17) | Open (lien, rule C1) | CDR readiness declaration |
| finding-10 | reviewer | Minor | CK-DES-A2 | Note 6.4; checker (the 512-byte result is still INFO) | 512-byte result not asserted; unchanged | Open (lien, rule C1) | CDR readiness declaration |
| finding-11 | reviewer | Minor | CK-DES-E2, CK-DES-I3 | ICD `01_bootrom_api.md`; note 4.2, D2 | Data lookup flag for `'X','F'`; unchanged | Open (lien, rule C1) | CDR readiness declaration |
| finding-12 | reviewer | Minor | CK-DES-A2 | Note 6.2, A-F7, 6.5 | CRC table placement in SRAM; unchanged | Open (lien, rule C1) | CDR readiness declaration |
| finding-13 | reviewer | Minor | CK-DES-H1 | Note 4.9 | Plan section 7 fallback (cwht-side extraction); unchanged | Open (lien, rule C1) | CDR readiness declaration |
| <a id="finding-14"></a>finding-14 | reviewer | Minor | CK-DES-C10, CK-DES-H1 | Note 4.6.4 "Argument" and "Route"; R-11; checker line 397 | Three statements of the REQ-SYS-155 case go further than their sources. (a) "the thermal prerequisite of row h blocks PA_EN until a valid in-range reading has been taken": 07 row h checks "PA temperature below the inhibit limit (REQ-SYS-118)", which a sensor that fails reading cold passes. What does block PA_EN is that the catch-up pass takes a fresh sample before any key closure is forwarded (4.6.3), so the out-of-range reading is detected first and the "no open Fault" prerequisite of row h holds PA_EN low. The conclusion stands, but on these two grounds, not on the one stated. (b) The proposed wording "within 500 ms (TBR) while PA_EN is held low" covers all of Receive, where PA_EN is always low, so it would relax REQ-SYS-155 for the whole mode, not only for an erase window. The author's summary says "while a write holds PA_EN low", which is the scope the design needs. (c) The checker assertion "the fault screen after an erase window still starts inside the 1 s of REQ-SYS-067" compares the detection latency (453 ms) with 1 s. REQ-SYS-067 runs "within 1 s (TBR) of detection", so the window does not count against it (and condition 4 of 4.6.1 keeps a second window out of that second). **Fix:** state grounds (a) as above; scope the R-11 option (a) to "while a declared store window holds PA_EN low" (or to Receive with PA_EN low, if that wider scope is intended, with the reason); reword the checker message, or drop the assertion | Open (lien, rule C1) | CDR readiness declaration |
| <a id="finding-15"></a>finding-15 | reviewer | Minor | CK-DES-D13, CK-DES-A2 | Note 4.5 "Result", 4.6.2 step 4 and the paragraph after it, section 9 item 7; ICD `02_programming.md` step 5 | The over-bound case is not stated consistently. (a) "Step 4 ends a window that runs past its bound as an overrun fault" and "a slow part shows as a logged fault, not a reset": the dispatcher cannot end a masked window; it sees the overrun only when the ROM call returns. For an erase that ends before about 1.0 s after the pre-window kick the unit reaches the overrun safe state; for a longer one, or a device that never returns ready, the watchdog resets it first. Both end safe, but the claim holds only for the first. (b) DML-5 item 7 asks that "a window over its bound gives `safe_state()` and no kick" and that "a fault-injection build that stretches one window past 450 ms ends in the overrun safe state, not in a watchdog reset". If no kick follows, the watchdog expires 1.0 s after the last kick, so both pass criteria cannot hold. The note does not say whether kicks resume in Fault-safe after an overrun. (c) With a part slower than 449 ms, every reclaim (about 7.5 a day) becomes a Fault-safe entry. The erase does complete, so the store is intact, but the operator effect and the recovery are not stated. **Fix:** state that the overrun is detected on return; state whether the main loop keeps kicking in Fault-safe after a store overrun (as for any other safe-state entry of row c); make the two DML-5 pass criteria agree with that; state the effect of a slow part on each reclaim and its recovery. Route the result with R-1 | Open (lien, rule C1) | CDR readiness declaration |
| <a id="finding-16"></a>finding-16 | reviewer | Minor | CK-DES-D9, CK-DES-C7 | Note 4.7 (page-append records and the power-loss table); R-2; ICD `02_programming.md` "Records are appended" | The page-append design says a write "programs the next blank page", and the power-loss table gives the load result in each state, but not how the next write finds a usable page after a power loss. (a) A partly programmed page fails its CRC but is not blank: programming over it (NOR bits only clear) would corrupt the new record. (b) A reclaim erase cut short leaves a sector whose pages may read 0xFF on cells that are not fully erased, and whose older records may still pass their CRC; the design would then append there. Read-back after programming (row g) catches most such writes, and the newest valid record is never touched, so this is not a loss of the stored configuration. It is a way for a new record to be lost or to decay after its read-back, which rolls settings back one commit (REQ-SYS-135). **Fix:** state the rule: a page is used only if all 256 bytes read 0xFF and every later page of the sector is blank; a sector found at boot in a state that no completed sequence produces (for example blank pages below valid ones, or a mix of old records and blank pages when the other sector is full) is erased again before use. Add a HostUnit case for each state of the power-loss table followed by a new write, and the power-cut case to the DML-5 item 1 run | Open (lien, rule C1) | CDR readiness declaration |
| <a id="finding-17"></a>finding-17 | reviewer | Minor | CK-DES-H1, CK-DES-I3 | ICD `02_programming.md` "Write conditions" and "Records are appended" | Two ICD sentences disagree with the note. (a) The ICD says audio, charge enable and transmit are "restored after step 6". The note says transmit is "re-armed only through the Arm condition" and charge is restored "after the charge prerequisites re-check" (4.6.3). "Restored" reads as an automatic re-arm, which is the open question of finding-9. (b) "A sector is erased only to reclaim it, when the other sector of its ring is full" fits the 2-sector configuration ring but not the 8-sector event-log ring the same paragraph covers, where the sector to reclaim is the next one in ring order, holding the oldest log records. **Fix:** align (a) with the answer to finding-9, and word (b) for both rings ("the next sector of its ring, which holds only its oldest records") | Open (lien, rule C1) | CDR readiness declaration |

Two Major findings Verified; no Major open. Findings 3 and 5 (Minor) are Verified because the Major fix text removes their defects. The other nine iteration 1 Minor findings are unchanged and stay Open. The delta raises four Minor findings (14 to 17) on the fix text. None of them changes a window length, a bound, a ratio or a layout value: they concern how the fix is worded, how the over-bound case is verified and one detail of the new record scheme. Under rule C1, all 13 open findings become liens once this reviewer verdict is APPROVED.

### Readiness criteria, iteration 2

| # | Criterion | Result | Evidence |
|---|---|---|---|
| R1 | Every figure rendered and inspected | N/A | The fix adds no figure |
| R2 | `tools/traceability.py` | Yes | 0 violations (D4) |
| R3 | The requirements are Active | Yes | REQ-SYS-067, 118, 131, 155 and 181 are Active at `f128235e`; 067, 131, 155 and 181 carry TBRs that close at PDR |
| R4 | The author's return lists the criteria and a self-check | Yes | The author's summary gives each fix, the numbers and the new requests; each was re-run and holds (D2 to D5) |

### Cross items for the lead SE, iteration 2 (not findings on the product)

- **X-1 Freeze (updated).** The drafts at `8a403ddb`, `03c960dc` and `225e23c4` are the reviewed bytes; the reviewer's copies are in the scratchpad (`rv132d/`). Filing other bytes needs a further delta iteration of this record and of the SA pair.
- **X-6 SA pair.** SA findings 1 to 3 (Major) were fixed in the same round. This record found no conflict between those fixes and finding-1 or finding-2, but their verification is the SA delta's. The record verdict waits for it.
- **X-7 Proposals to other owners.** The fix routes three rule changes: the declared-window exception to the 07 `SW-SCHED` row and to MSR-26 (R-1, to the writer of 07), the write rule on every `FlashStore` user (R-10), and the REQ-SYS-155 value (R-11, owner ruling at WP-PDR-45). None of them is ruled by this record; under rule C10 the R-11 value goes to the owner only once this record and its SA pair are APPROVED.
- **X-8 rustos commit message.** `00d5383` names "cwht review INSP analysis-fw-b1-dml3-wp-sw-08-10-12" rather than the record id INSP-132. This is rustos house style for the owner's merge and not a finding.

### Measurements (SWE-089), iteration 2

Reviewed: the note revision 1 (132 insertions, 44 deletions against revision 0; 440 lines read), the checker delta (29 new assertions), the results file, and the rustos delta `03b1997..00d5383` (47 insertions, 22 deletions in 2 pages). Datasheet pages re-read: 3. New findings: 4 Minor. Effort of this iteration: about 32 turns and 45 minutes (front matter totals include iteration 1).

### Record verdict, iteration 2

```
VERDICT: NEEDS CHANGES (record verdict held); reviewer_verdict APPROVED
FINDINGS:
- [Major] finding-1: Verified at note 8a403ddb and rustos 00d5383 (declared window, catch-up pass, main-loop-only kick, 403/452 ms against the 1.0 s load, R-1, R-4, DML-5 item 7).
- [Major] finding-2: Verified at note 8a403ddb (REQ-SYS-155 row, 51/404/453 ms, argument, R-11, full row j table).
- [Minor] findings 3 and 5: Verified (overtaken by the Major fixes).
- [Minor] findings 4, 6 to 13: unchanged, liens under rule C1.
- [Minor] finding-14: REQ-SYS-155 argument cites row h for a plausibility check it does not make; R-11 wording covers all of Receive; the REQ-SYS-067 check measures the wrong interval.
- [Minor] finding-15: over-bound window: detected only on return; DML-5 item 7 pass criteria disagree on the kick after an overrun; effect of a slow part on each reclaim not stated.
- [Minor] finding-16: page-append records: no rule for finding a usable page after a torn program or an interrupted reclaim.
- [Minor] finding-17: ICD "restored after step 6" and "the other sector of its ring" disagree with the note.
ITEMS N/A: as iteration 1
MEASUREMENTS: size=note 440 lines, checker 83 assertions, 2 ICD pages changed; turns=32 (total 102); minutes=45 (total 140); major=0 new; minor=4 new
```

`reviewer_verdict: APPROVED`: finding-1 and finding-2 are Verified and no Major is open. The 13 open Minor findings become liens under rule C1 (owner the firmware developer, due at the CDR readiness declaration). The record `verdict` stays held at NEEDS CHANGES while CR-012 is unmerged and until the paired software assurance record files its iteration 2 delta APPROVED. The ICD blobs also sit on an unmerged rustos branch (OD-23; the pin moves by PCR-4 at the owner's merge).
