---
# Peer-review record front matter (charter sections 2 and 5; docs/process/01-lifecycle-and-reviews.md section 13
# is the single field list; docs/process/07-software-engineering-plan.md sections 2.1.1, 10.2 and 15).
# This is the software assurance pair that PDR work plan WP-PDR-41 names for the FW-B1 DML-3 note ("Reviewer: the
# independent code reviewer with the design checklist, and SA for WP-SW-08 and 12 (safety-critical configuration
# and image integrity). Record: docs/reviews/PDR/checklists/analysis-fw-b1-dml3-wp-sw-08-10-12.md and its SA pair").
# Scope: WP-SW-08 (configuration store flash write: interrupt masking, code in RAM, power-loss behaviour) and
# WP-SW-12 (image and configuration integrity). WP-SW-10 (UART0 telemetry) is read only where it touches them.
# Checklist applied: docs/templates/peer-review-checklist-software-assurance.md revision A AS ON ITS CR-012 BRANCH
# (cr/CR-012-pdr-checklist-templates at 7784672, blob 5b13528504868b2add0f0b1e329c63aa2b54cdf4; not merged:
# git merge-base --is-ancestor 7784672 HEAD is false at HEAD b2bcba0 on 2026-09-29). The `checklist` field names
# peer-review-checklist-design revision B, the checklist WP-PDR-41 assigns to the file review, because
# tools/validate_docs.py fails a record whose `checklist` names a template absent from main (lead SE convention
# of 2026-09-27). `assurance_checklist` names the template actually applied (the INSP-075 and INSP-111 form).
# id: INSP-133, assigned by the lead SE brief.
id: INSP-133
checklist: peer-review-checklist-design
checklist_revision: B
assurance_checklist: "docs/templates/peer-review-checklist-software-assurance.md@5b13528504868b2add0f0b1e329c63aa2b54cdf4 (revision A, branch cr/CR-012-pdr-checklist-templates at 7784672)"
checklist_file: docs/reviews/PDR/checklists/analysis-fw-b1-dml3-wp-sw-08-10-12-software-assurance.md
product: docs/design/analysis/fw-b1-dml3-wp-sw-08-10-12.md
# product_commit and product_files (iteration 2, the delta of 2026-09-29): the three cwht files are the revision 1
# author drafts of fix round 1, which the lead SE files unchanged (the harness lets no agent create a cwht file), so
# they have no cwht commit yet. Their blobs are git hash-object of the returned drafts in the scratchpad wp41/draft/
# tree. The rustos part is committed: product_commit is the rustos branch cwht/wp-sw-08 head 00d5383 (parent
# 03b1997, the iteration 1 head; one commit on top, no amend). Each rustos blob is git -C ~/rust/rustos rev-parse
# 00d5383:<path> (committed objects only; the rustos working tree was not read). git diff --stat 03b1997 00d5383:
# 2 files (02_programming.md, flash/index.md), 47 insertions, 22 deletions; 01_bootrom_api.md, 03_xip_qmi.md and
# the rp2350 index row are unchanged. product_files_iteration_1 keeps the iteration 1 list (drafts of revision 0,
# rustos 03b1997)
product_commit: "00d53834dfe315aafd09a11ec1d76e6ffbc45835"
product_files: ["docs/design/analysis/fw-b1-dml3-wp-sw-08-10-12.md@8a403ddba8b1d785fdb3c8caf226e5677509c947", "docs/design/analysis/fw-b1-dml3/check_fw_b1_dml3.py@03c960dc66ba6fd607ed866b5802e184e8ef0c49", "docs/design/analysis/fw-b1-dml3/fw-b1-dml3-results.json@225e23c45f597c270c8a3081049759006f525120", "rustos:docs/icd/rp2350/flash/index.md@56d3a73ed78a81e2a4f8f71f066f774256709e22", "rustos:docs/icd/rp2350/flash/01_bootrom_api.md@f8ca1a2eb46daed1e753816ba7f3dae80e306eca", "rustos:docs/icd/rp2350/flash/02_programming.md@8f803cc99d07c88364119cdf9c2770b5a8223d63", "rustos:docs/icd/rp2350/flash/03_xip_qmi.md@f66298c75b8db26ee58eb46ad6f1b2cb979f04d1", "rustos:docs/icd/rp2350/index.md@b6fe67962cb946c63d70e7ff13ce43241edad18d"]
product_files_iteration_1: ["docs/design/analysis/fw-b1-dml3-wp-sw-08-10-12.md@4757a6b6a65c5c6ed975bb5051ee2dc7a3a010dc", "docs/design/analysis/fw-b1-dml3/check_fw_b1_dml3.py@5a070bb0ee07f2a65e382cd090cb28f4910d62da", "docs/design/analysis/fw-b1-dml3/fw-b1-dml3-results.json@79c9547298785daa8f7eb93573d4f59094399b7f", "rustos:docs/icd/rp2350/flash/index.md@b42c5ab5ea12a886bcd5cd19f7dc16f7ebc75a25", "rustos:docs/icd/rp2350/flash/01_bootrom_api.md@f8ca1a2eb46daed1e753816ba7f3dae80e306eca", "rustos:docs/icd/rp2350/flash/02_programming.md@bebbadc26708d14fd1c309f5cadc9ba4c054c60a", "rustos:docs/icd/rp2350/flash/03_xip_qmi.md@f66298c75b8db26ee58eb46ad6f1b2cb979f04d1", "rustos:docs/icd/rp2350/index.md@b6fe67962cb946c63d70e7ff13ce43241edad18d"]
input_files: ["docs/plan/pdr-work-plan.md (revision 7; WP-PDR-41, section 6.2 row PCR-4, section 6.1 rows OD-23 and OD-37, rules C1 to C12)", "docs/plan/technology-assessment.md (sections 1 and 3.18)", "docs/process/07-software-engineering-plan.md (sections 2.1.1, 14.1, 14.2 rows a, f, j and the SW-CFG, SW-SAFE, SW-SCHED module rows, 16.5, 19)", "docs/design/analysis/keyer-host-study.md (section 6.5, A-7, A-8, R-1, R-2)", "docs/reviews/PDR/checklists/analysis-keyer-host-study-software-assurance.md (INSP-075 finding-4)", "docs/requirements/sys/requirements.json (REQ-SYS-004, 131, 132, 134, 135)", "docs/research/rustos-toolchain-proof.md (F5, F8, F15)", "docs/icd/ICD-CTL-USB.md (section 3.2.6 rows)", "docs/decisions/adr/ADR-059-2s-18650-holders-external-charging.md (Status: Proposed)", "rustos 48e07ec:firmware/pico2/link.ld and firmware/pico2/src/lib.rs (git show; FLASH 4M, RAM rwx, .data.* in RAM, IMAGE_DEF EXE secure Arm)", "docs/reviews/PDR/checklists/analysis-fw-b1-dml3-wp-sw-08-10-12.md@83c326bf248b8073790a2c0aa3c856add47fc098 (INSP-132 iteration 1 draft, scratchpad wp41/insp132/; not filed at HEAD 220bb8b)", "docs/conops/conops.md (Table 3.4-4 row 1, KEY inhibit; section 3.4 item 1)", "docs/requirements/sys/requirements.json (iteration 2: REQ-SYS-052, 067, 135, 155, 163, 181)", "rustos 2ec64c0:docs/rp2350-datasheet.pdf (blob 1b26078d, build 2025-02-20; equal by content hash to the scratchpad copy ds-0220.pdf; printed pages 83, 232, 357 to 358, 372 to 373, 376, 379, 385 to 388, 400, 1350 to 1351 read with pdftotext)"]
# paired_record (iteration 2): INSP-132, the independent code review record docs/reviews/PDR/checklists/
# analysis-fw-b1-dml3-wp-sw-08-10-12.md. Its iteration 1 draft (blob 83c326bf, reviewer:WP-PDR-41-dml3-iter1) pins
# the same eight iteration 1 blobs as this record; it is not filed at HEAD 220bb8b, and its iteration 2 delta is
# not yet written (cross item X-6)
paired_record: INSP-132
product_type: design
# criticality: safety-critical. WP-SW-08 and WP-SW-12 serve the configuration guard (SW-SAFE cfg_guard, HZ-014) and
# the boot image check (SW-BOOT, REQ-SYS-132), both safety-critical in 07 section 14.1, and the SW-CFG store
# (mission-critical); the note's own header row "Analysis kind" says so. 07 section 2.1.1 has no row for a
# stand-alone analysis note; WP-PDR-41 routes it, as WP-PDR-33 routed the keyer note (INSP-075 cross item X-1),
# and product_type design is the INSP-075 precedent
criticality: safety-critical
# product_size: iteration 2 figures; iteration 1 was note revision 0 (352 lines, 9 assumptions, 9 requests), checker
# 380 lines with 54 assertions, ICD 323 lines
product_size: "1 DML-3 note revision 1 (440 lines, 10 sections, 30 datasheet citations D1 to D30, 11 assumptions, 11 requests R-1 to R-11, 5 limits); 1 checker (467 lines, 83 assertions); 1 results file; 4 rustos ICD pages and 1 index row (348 lines at 00d5383; the delta 03b1997..00d5383 is 2 files, 47 insertions, 22 deletions)"
sprint: PDR-prep
author_agent: "author:WP-PDR-41 DML-3 note and WP-SW-08 ICD (Claude, firmware developer role, 2026-09-29)"
reviewer_agent: "sa-reviewer:WP-PDR-41-insp-133-dml3-iter1 (iteration 1); iteration 2 by sa-reviewer:WP-PDR-41-insp-133-dml3-iter2 (independent; authored no part of WP-SW-08, 10 or 12, of the note revisions 0 and 1, the checker, the ICD commits 03b1997 and 00d5383, or INSP-132)"
assurance_required: true
assurance_reviewer_agent: "sa-reviewer:WP-PDR-41-insp-133-dml3-iter1 and -iter2 (software assurance function; paired file review INSP-132, docs/reviews/PDR/checklists/analysis-fw-b1-dml3-wp-sw-08-10-12.md, by reviewer:WP-PDR-41-dml3-iter1)"
iteration: 2
# readiness_met: false (iteration 2). R1 is still not met as the checklist states it: the three cwht files are
# uncommitted revision 1 drafts, frozen here by blob, and the lead SE files them unchanged (X-1). R4 is met for
# iteration 1 (INSP-132 iteration 1 is a separate invocation on the same blobs) and pending for iteration 2 (X-6)
readiness_met: false
# reviewer_verdict and assurance_verdict (iteration 2): finding-1, finding-2 and finding-3 (Major) Verified; no
# new Major. The six iteration 1 Minors and the three new Minors (finding-10 to finding-12) are liens under plan
# rule C1, due at the CDR readiness declaration
reviewer_verdict: APPROVED
assurance_verdict: APPROVED
# verdict: set by Claude as software lead (07 section 10.2). Held at NEEDS CHANGES: the cwht drafts are not filed
# (R1, X-1), INSP-132 has no iteration 2 verdict (X-6), the rustos branch cwht/wp-sw-08 is not merged by the owner
# (OD-23; PCR-4 pin move, X-4), and CR-012 is not merged (git merge-base --is-ancestor 7784672 220bb8b is false)
verdict: NEEDS CHANGES
# counts (iteration 2): 12 findings; 3 Major Verified; 9 Minor liens (finding-4 to finding-12). A lien is not Open
# and not a Deferred RID (INSP-073 iteration 2 convention)
findings_major: 3
findings_minor: 9
findings_open: 0
findings_fixed: 0
findings_verified: 3
findings_deferred: 0
assurance_findings_major: 3
assurance_findings_minor: 9
assurance_tasks_applied: ["swe-134 7.1 task 5", "swe-022 7.1 task 1", "swe-057 7.1 task 2", "swe-058 7.1 task 1", "swe-058 7.1 task 2", "swe-058 7.1 task 3", "swe-058 7.1 task 4", "swe-058 7.1 task 5", "swe-134 7.1 task 1", "swe-134 7.1 task 4", "swe-134 7.1 task 6", "swe-205 7.1 task 3", "swe-052 7.1 task 1", "swe-205 7.1 task 1", "swe-205 7.1 task 4", "swe-205 7.1 task 5", "swe-052 7.1 task 2", "swe-192 7.1 task 1", "swe-070 7.1 task 1", "swe-087 7.1 task 1", "swe-089 7.1 task 1", "swe-087 7.1 task 2", "swe-088 7.1 task 1", "swe-088 7.1 task 2"]
swe134_items_checked: [b, c, e, f, g, h, i, j, k]
deferred_rids: []
items_no: ["swe-057 7.1 task 2", "swe-058 7.1 task 2", "swe-058 7.1 task 3", "swe-058 7.1 task 4", "swe-134 7.1 task 1", "swe-134 7.1 task 6", "swe-205 7.1 task 1", "swe-205 7.1 task 5", R1, SA-C-f, SA-C-h, SA-C-j, SA-D1, SA-D6]
effort_turns: 75
effort_minutes: 150
record_status: Open
date: 2026-09-29
date_closed: null
---

# Peer review record INSP-133: software assurance pair for the FW-B1 DML-3 note (WP-SW-08 and WP-SW-12) and the WP-SW-08 flash ICD (WP-PDR-41)

**Product.** `docs/design/analysis/fw-b1-dml3-wp-sw-08-10-12.md` revision 0 (draft blob `4757a6b6`), its checker `fw-b1-dml3/check_fw_b1_dml3.py` (`5a070bb0`) and results file (`79c95472`), and the rustos ICD pages `docs/icd/rp2350/flash/` on branch `cwht/wp-sw-08` at `03b1997` (not pushed, for the owner's merge, OD-23). The note's WP-SW-10 sections were read only where they touch the store window (section 5.3 row "Store window") or the CRC (section 5.4).

**Independence (rule C4; 07 section 2.1).** This invocation authored no part of WP-SW-08, WP-SW-10 or WP-SW-12, the note, the checker or the ICD pages, is not the file reviewer of the paired record, and edited no product file. It wrote only this record (as a draft) and scratch files.

**Search first (charter section 11 rule 1; rule C3).** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (queries: WP-PDR-41 and the DML-3 note, the configuration store and the flash write; the event log in flash and SWE-210). rustos content was read only as committed objects (`git show` and `git rev-parse` of `03b1997`, `48e07ec` and `2ec64c0` in the rustos object store); the rustos working tree was not read or changed.

## Record

### Findings

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | assurance | Major | swe-058 7.1 tasks 2 and 4; swe-134 7.1 task 1; swe-205 7.1 task 1; SA-C-j, SA-D1 | Note section 4.3 row "HardFault or other fault inside the window" (line 101, "the watchdog, fed just before the window"); request R-1 (line 329, "watchdog fed immediately before each window"); ICD `02_programming.md` constraint row (line 36, "The watchdog is fed immediately before masking") and window design step 2 (line 53, "Feed the watchdog; set PRIMASK") | The design adds a second watchdog kick, inside the flash driver. 07 section 14.2 row j and the `SW-SCHED` row (j) say the watchdog is "kicked only when all ran", and keyer host study R-1 says "fed from the main loop only after every safety monitor has run". A kick in the driver does not check that the monitors ran. Failure case: a monitor task stops being dispatched at t0, so the supervised kicks stop. A settings commit starts at t0 + 0.99 s and the driver kicks. The reset then comes at about t0 + 1.99 s, and Self-test starts about 0.1 s later (A-8), at about 2.09 s. That is past the 2 s of REQ-SYS-131. The software watchdog control (K7) is weakened, and the hazard data does not show it. The 2.48 ratio does not need the extra kick: the window can start in the same main-loop pass as a supervised kick. Fix: remove the kick from the driver, in the note (section 4.3, section 4.5, R-1) and in the ICD page (constraint row and step 2). Instead, the store window starts only in the main-loop pass right after a supervised kick. Before masking, a host-tested precondition checks that the time since the last supervised kick plus the longest window is at most half the load, and defers the write if not. Route this rule to WP-PDR-32 and to WP-PDR-35 (`SW-SCHED`, `SW-CFG`) | Open | Pending | |
| <a id="finding-2"></a>finding-2 | assurance | Major | swe-058 7.1 tasks 2, 3 and 4; swe-134 7.1 tasks 1 and 6; swe-205 7.1 task 5; SA-C-j, SA-D6 | Note sections 4.5 and 4.6 (lines 119 to 148), section 7 row "Bounded masked window" (line 316); ICD `02_programming.md` "cwht window design" (lines 44 to 60) | The note does not say how the scheduler treats the window. 07 section 14.2, `SW-SCHED` row (k, l), says "a tick overrun or a missed monitor deadline is an error with response class safe state", and MSR-26 targets "Overruns 0". Each commit masks interrupts for up to 401 ms (erase) plus 4 ms (program). That misses up to 401 of the 1 ms ticks and every monitor period shorter than 401 ms. As designed, then, every settings change either puts the unit in the safe state, or overrun detection is turned off around the window without any analysis, which weakens a safety-critical control. Fix: state the scheduler rule as a design constraint for WP-PDR-32 and WP-PDR-35. For example: the store declares a bounded window before masking; the scheduler counts that window's missed ticks separately; any overrun or missed deadline outside a declared window stays a safe-state error. Tell the MSR-26 owner. Also record, in the note, the trade against designs that shorten the window during operation: erase the inactive sector only at boot, before dispatch starts, or append records page by page in an erased sector (16 records per sector, erase outside operation). Then only 4 ms program windows occur in operation, and there are 16 times fewer erase cycles | Open | Pending | |
| <a id="finding-3"></a>finding-3 | assurance | Major | swe-205 7.1 tasks 1 and 5; swe-134 7.1 tasks 1 and 6; swe-057 7.1 task 2; SA-C-h, SA-C-j, SA-D1, SA-D6 | Note section 4.6 (line 139, "With a write allowed only in Receive, PA_EN low and the key inputs open"); requests R-3, R-4, R-5 (lines 331 to 333); section 4.7 wear (line 163); section 1 "Out of scope" (line 26); ICD `index.md` line 54 ("for the configuration copies A and B and the event log") | The window analysis and its safety constraint cover configuration commits only. WP-SW-08 has a second client: the persistent event log, a "ring buffer in flash" (07 section 16.5; 07 section 19 row WP-SW-08, "configuration copies A/B, event log ring"). Its records include safety rejections (SWE-134 e and h), Fault entries and panic markers, and these arise in Transmit-keyed or Tune. An event-log write there would stall the monitors for up to 401 ms with PA_EN high, against REQ-SYS-004 (20 ms) and the 100 ms thermal budget. Also: no request carries the "Receive only" precondition itself. R-4 carries only the outputs set before the window, and keyer host study R-2 speaks of "configuration-store write" only. R-3 ends the application `FLASH` region at 0x3FD000 and leaves no sector for the event log. The wear budget ignores event-log erases. Fix: make the write-state rule apply to every flash erase or program. For example: the event log keeps records in RAM and writes them to flash only in Receive, after the safe state, or at the next boot. Put the Receive-only precondition, with PA_EN low and the key inputs open, into R-4 for WP-PDR-35 and WP-PDR-16. Either reserve the event-log sectors in the R-3 layout (below copy A, with the application `FLASH` end moved down) or state that R-3 covers the configuration store only and the event-log layout is still open. Add the event-log erases to the wear budget | Open | Pending | |
| <a id="finding-4"></a>finding-4 | assurance | Minor | swe-134 7.1 task 6; SA-C-j; rule C7; rule C8 | Note section 4.6 (lines 139 to 146) | The note lists four row j items as active in Receive but does not give a reason for leaving out the others. The ones left out: the key-up response, the manual-closure timeout, the tune end, the paddle no-gap and squeeze watchdog, the test-mode timeout, PA over-temperature at 100 ms, PA temperature out of range to Fault-safe within 100 ms (REQ-SYS-155, which does not say it is transmit-only), receive mute within 2 ms of key-down, REQ-SYS-004, and PA over-current at 10 ms. This part of the INSP-075 finding-4 fix ("state which row j budgets are active") is therefore incomplete. The battery under-voltage row needs a supervision period of at most 599 ms, but no request carries that limit. The charge-disable row depends on in-radio charging, which ADR-059 (Proposed, A5, charging outside the radio) would remove, so this row is at risk under rule C8. Fix: add a table of every row j item marked active or not active in the states where a write is allowed, each with its reason. Add the 599 ms supervision-period limit to R-4. Mark the charge row "AT RISK (A5 CRs)" | Open | Pending | |
| <a id="finding-5"></a>finding-5 | assurance | Minor | swe-058 7.1 task 3; SA-C-c | Note section 4.3 row "HardFault or other fault inside the window" (line 101, "a reset, not a hang"); ICD `02_programming.md` lines 40 to 42 | The claim that a fault in the window always ends in a reset leaves out one condition: the flash must be idle when the chip restarts. Datasheet section 5.4.8.7 (printed p385) says "resetting RP2350 does not reset attached QSPI devices". The exit-XIP sequence brings the device out of continuous-read or QPI mode, and the datasheet says nothing about a device still busy with an erase. If the chip resets while an erase is still running, the bootrom looks for an image on a busy device. Such a reset can come from the RUN pin, a debugger, or a watchdog expiry if an erase takes longer than the 1.0 s load. If the bootrom finds no image, the chip stays in USB or UART boot. RF stays off (07 section 14.2 row a: external pull-downs on TX_KEY and PA_EN), but Self-test is never reached, so REQ-SYS-131 is not met in that case. The case the note does analyse (lockup, then watchdog) is safe, because the erase ends (400 ms at most, A-7) before the load runs out; the note should say this is why. Fix: state the condition in section 4.3 and in the ICD page. Add a DML-5 item to section 9: assert RUN, or force a watchdog reset, during an erase and record whether the unit reaches Self-test. If it does not, record the residual (a power cycle recovers it) for WP-PDR-16 and RSK-021 | Open | Pending | |
| <a id="finding-6"></a>finding-6 | assurance | Minor | swe-134 7.1 task 4; SA-C-e | ICD `02_programming.md` sequence step 3 (line 12, `flash_range_erase(offset, 4096 * n, block_size, block_cmd)`) and window design step 0 (line 51); ICD `01_bootrom_api.md` line 36; note section 4.2 and R-2 (line 330) | Nothing fixes the values the driver passes for `block_size` and `block_cmd`. The ROM "will use the larger block erase where possible" and "no validation of the arguments is performed" (section 5.4.8.10, printed p387). The request checker `plan` checks only the offset and length. Failure case: if `block_size` is 4096 and `block_cmd` is the D8h 64 KiB block command, a sector erase of copy A erases the whole 64 KiB block from 0x3F0000, which holds both copies and the end of the application. A zero `block_size` has no defined meaning in the datasheet. Fix: set the pair as named constants in the ICD page, for example the plain 4 KiB sector erase with no larger-block command, with its value and datasheet basis. Include them in the `plan` decision, and add a HostUnit case that rejects any other pair | Open | Pending | |
| <a id="finding-7"></a>finding-7 | assurance | Minor | swe-058 7.1 task 1; SA-C-f | Note sections 6.1, 6.2 and 6.5 (lines 236 to 309); requests R-7 and R-8 (lines 335 to 336) | The WP-SW-12 critical function includes "detect corruption of the image", but the note defines only the CRC algorithm. It does not say which bytes of the image are covered (start, end, where the length comes from, where the trailer sits and how it is aligned, whether the IMAGE_DEF block is included, and that the E10 block and the store sectors are excluded). It does not say what happens when the length is out of range. It also does not state a common-mode limit: the check runs from the same image it checks. Datasheet section 5.1.8 (printed p357 to 358) offers an alternative that runs before any image code: a block hash checked by the bootrom ("Hashes guard against corruption of an image"). The note does not consider it. Fix: add the coverage definition to section 6 and to R-7 and R-8, with the length taken from a link-time bound inside the application `FLASH` region rather than from data read from flash at run time. State the common-mode limit, and record the bootrom hash option with the reason for or against it, for WP-PDR-32 (`SW-BOOT`) | Open | Pending | |
| <a id="finding-8"></a>finding-8 | assurance | Minor | swe-058 7.1 task 1; SA-C-k | Note section 4.7 (lines 161 to 163), R-5 (line 333), section 3 assumptions | "An expected 20 commits per day" has no source and no assumption row. R-5's own limit, one commit per 60 s, allows 1440 commits per day: 26 times the endurance budget of 54.8 per day, or about 139 days of such use. The note also does not say what happens at wear-out: row k retries and keeps the previous copy, after which changes are no longer saved, against REQ-SYS-135. Fix: add an assumption row for the expected commit rate with its basis. State the worst-case life at the R-5 limit. State the wear-out behaviour (logged, shown to the operator) as part of R-5 | Open | Pending | |
| <a id="finding-9"></a>finding-9 | assurance | Minor | swe-058 7.1 task 1 (editorial) | Note section 4.5 table (lines 127 and 131) | The row "Ratio of the load to the longest window: 2.48" comes right after the 401 ms design row, but 2.48 is 1.0 s / 0.404 s, the one-window form. For 401 ms the ratio is 2.49. The checker asserts it against 0.404 s (line 290), and ICD `02_programming.md` line 94 labels it correctly. The author's summary repeats "401 ms ... (2.48 times". Fix: label the ratio as taken against the 404 ms one-window form, as the ICD page does | Open | Pending | |

Three Major findings: `assurance_verdict` NEEDS CHANGES (07 section 10.2; rule C1). Checked and found sound: the list of flash-fetch sources during the window, and each way it is closed (section 4.3), against the cited datasheet pages; the RP2350-E10 finding and the proposed layout; the power-loss state table (section 4.7), which holds for one writer; the CRC-32/ISO-HDLC definition, the golden vectors and the error-detection claims, which this reviewer confirmed independently (Commands); and the time budget arithmetic.

### Task table

| Task | Safety-critical designation (SWEHB 8.10 section 6) | Applied | Result and evidence | Relief (N/A only) | Finding ids |
|---|---|---|---|---|---|
| swe-134 7.1 task 5 (every type) | SC | Yes | This record is the assurance participation in the review of a product that sets the design of the store write and the integrity check for `SW-SAFE` `cfg_guard`, `SW-BOOT` and `SW-CFG` (07 section 14.1) | | none |
| swe-022 7.1 task 1 (every type) | SC | Yes | Performed against the software assurance plan, 07 section 15, by this review | NASA-STD-8739.8 part: `rmm.json` SWE-022 T (standard not in the corpus) | none |
| swe-057 7.1 task 1 (design) | | N/A | The note has no architecture content | 07 section 2.1.1 row "Design": architecture is WP-PDR-32, reviewed with SA in plan wave 2a | |
| swe-057 7.1 task 2 (design) | | No | The store window meets its safety purpose only for configuration commits in Receive; the event-log client and the Receive-only precondition are not carried | | finding-3 |
| swe-058 7.1 task 1 (design) | | Yes | Each critical function traces to REQ-SYS-131, 132, 134, 135 and 07 section 14.2 rows e, f, g, k (note section 1 table). Gaps in definition: finding-7, finding-8, finding-9 | | finding-7, finding-8, finding-9 |
| swe-058 7.1 task 2 (design) | | No | The window design contradicts the `SW-SCHED` kick rule (row j) and overrun rule (rows k, l) of 07 section 14.2 | | finding-1, finding-2 |
| swe-058 7.1 task 3 (design) | | No | Undesired behaviours not analysed: safe state on every commit (overrun rule), event-log stall in Transmit-keyed, boot on a busy flash device | | finding-2, finding-3, finding-5 |
| swe-058 7.1 task 4 (design) | SC | No | REQ-SYS-131 (2 s) is not kept for a stopped monitor task when a commit falls near the end of the load; row j budgets are not kept for event-log writes outside Receive | | finding-1, finding-2, finding-3 |
| swe-058 7.1 task 5 (design) | | Yes | This record's own analysis: independent zlib-only Hamming-distance search, checker re-run, datasheet page checks, rustos linker and IMAGE_DEF check (Commands) | | none |
| swe-134 7.1 task 1 (design) | SC | No | Section C: items f, h, j not met as stated | | finding-1, finding-2, finding-3, finding-7 |
| swe-134 7.1 task 4 (design) | SC | Yes | The `plan` request checker keeps the store sectors apart from the image region (note section 4.2, R-2); the erase-argument gap is finding-6 | | finding-6 |
| swe-134 7.1 task 6 (design) | SC | No | The monitor stall is routed to WP-PDR-16 and WP-PDR-35 (R-4), but not the driver kick, the overrun-rule conflict or the event-log writes, and the row j table is incomplete | | finding-1, finding-2, finding-3, finding-4 |
| swe-143 7.1 task 1 (design) | | N/A | No architecture review is held on this product | 07 section 2.1.1 row "Design": the SWE-143 review is plan wave 2a | |
| swe-205 7.1 task 3 (design) | SC | Yes | No component is added or moved; WP-SW-08 and WP-SW-12 are the 07 section 19 rows | | none |
| swe-052 7.1 task 1 (design) | | Yes | Section 1 and section 7 trace each result to its requirement; no code exists at DML-3 | | none |
| swe-205 7.1 task 1 | SC | No | Software contributions found by this review are not in the hazard data or routed to it: the unsupervised kick (weakens K7), the overrun-rule conflict, event-log stalls outside Receive | | finding-1, finding-2, finding-3 |
| swe-205 7.1 task 4 | SC | Yes | Section D, SA-D3 | | none |
| swe-205 7.1 task 5 | SC | No | The software safety analysis update is requested for the configuration-commit stall only | | finding-2, finding-3 |
| swe-052 7.1 task 2 | SC | Yes | Section D, SA-D3 | | none |
| swe-192 7.1 task 1 | SC | Yes | R3 run: 0 violations and no `HAZARD_REQ_NOT_TESTED`; the note claims no closure | | none |
| swe-070 7.1 task 1 (checker) | | Yes | The checker has no TV record and the note labels it developer evidence (05 section 9.1). Its CRC results rest on agreement with `zlib`, and this reviewer confirmed the Hamming-distance result with a zlib-only search | | none |
| swe-136 7.1 task 1 | | N/A | numpy is used for array work only; the venv interpreter is TV-001 | 07 section 17.3 and 05 section 9.1 class C | |
| swe-134 7.1 task 3 | SC | N/A | Safety-critical loaded data (the configuration record, its defaults and limits) is tested with the code and test products | 07 section 9.7 (loaded data, SWE-193 cases) | |
| swe-087 7.1 task 1 | | Yes | The paired file review and this record are the peer review of the product | | none |
| swe-087 7.1 task 2, swe-088 7.1 task 2 | | N/A | Iteration 1: no finding accepted or fixed yet | 07 section 10.2 | |
| swe-088 7.1 task 1 | | N/A | The paired record is not filed (SA-A4) | 07 section 10.2 (checked at the delta iteration) | |
| swe-089 7.1 task 1 | | Yes | Section E, SA-E2 | | none |

## Readiness criteria

| # | Criterion | Result | Evidence |
|---|---|---|---|
| R1 | Frozen, and the same blobs as the paired record | No (X-1) | rustos: the five blobs equal `git rev-parse 03b1997:<path>`; `git diff --stat 48e07ec 03b1997` shows only these files. cwht: the three drafts are not committed; the blobs are `git hash-object` of the returned drafts. The paired record is not filed, so its list cannot be compared |
| R2 | Row and criticality identified | Yes | `product_type` design, `criticality` safety-critical (07 section 14.1 `SW-SAFE`, `SW-BOOT`; `SW-CFG` mission-critical); routed by WP-PDR-41 |
| R3 | validate_docs and traceability clean for the ids touched | Yes | On a scratch `git archive` export of HEAD `b2bcba0` with the three drafts and this record added: `tools/validate_docs.py` exit 0; `tools/traceability.py --report-only --output <scratch>/traceability-report.md` 0 violations. Nothing was written into `docs/vv` of the repository |
| R4 | Paired review filed by its own invocation; this reviewer independent | Pending (X-2) | The paired record is not filed at HEAD `b2bcba0`; this invocation is not the author |

## A. Dispatch, independence and record integrity

| Id | Answer | Evidence |
|---|---|---|
| SA-A1 | Yes | WP-PDR-41: "SA for WP-SW-08 and 12 (safety-critical configuration and image integrity)"; 07 section 14.1 `SW-SAFE` (`cfg_guard`), `SW-BOOT`; no 07 section 2.1.1 row for analysis notes (INSP-075 X-1 precedent) |
| SA-A2 | Yes | Author `author:WP-PDR-41 DML-3 note and WP-SW-08 ICD`; file reviewer the independent code reviewer (pending); this reviewer |
| SA-A3 | N/A | The paired record is not filed; to be checked at the delta (X-2) |
| SA-A4 | N/A | The paired record is not filed (X-2) |

## B. SWE-to-task table

| Id | Answer | Evidence |
|---|---|---|
| SA-B1 | Yes | Task table: row "Every product type", row `design`, and the SWE-205, SWE-052, SWE-192, SWE-070, SWE-136, SWE-134 task 3, SWE-087, SWE-088 and SWE-089 tasks the product or its review implements |
| SA-B2 | Yes | N/A rows cite 07 sections 2.1.1, 9.7, 10.2, 17.3 and 05 section 9.1. The only SC task answered N/A is swe-134 task 3, relieved by 07 section 9.7 |
| SA-B3 | Yes | Every No row cites a finding |

## C. SWE-134 items a to l (07 section 14.2; `SW-CFG` a, b, e, f, g, k; `SW-SAFE` and `SW-SCHED` j; `SW-BOOT` f)

| Id | Answer | Evidence |
|---|---|---|
| SA-C-a | N/A | The note sets no boot or restart behaviour of the store |
| SA-C-b | Yes | Note section 4.7: the four store states (idle, erasing, programming, verifying) of row b, each with the load result; one valid copy in every state, for one writer |
| SA-C-c | Yes, with finding-5 | A fault in the window locks the core; the watchdog resets it. The boot on a busy flash device is not stated (finding-5) |
| SA-C-d | N/A | No override is set by the note |
| SA-C-e | Yes, with finding-6 | `plan` rejects any request outside the two store sectors before any ROM call (section 4.2; ICD step 0), meeting row e. The erase-argument gap is finding-6 |
| SA-C-f | No | Configuration: two copies, CRC-32, sequence number; Hamming distance at least 5 on the 256-byte record, confirmed independently; erased and zeroed copies fail. Image: coverage and common-mode limit not defined (finding-7) |
| SA-C-g | Yes | Every program is read back and every erase checked for 0xFF (ICD step 5; row g); the record length is fixed at one page |
| SA-C-h | No | The prerequisite for any flash write (Receive, PA_EN low, key inputs open) is a premise of section 4.6, not a stated constraint, and does not cover the event log (finding-3) |
| SA-C-i | Yes | The note finds and removes a single-event failure: a firmware load that erases copy B and silently rolls settings back one commit (section 4.4). The E10 text is confirmed on printed p1351 ("This block will be written to flash first"), and the alias arithmetic by the checker |
| SA-C-j | No | Findings 1 to 4 |
| SA-C-k | Yes, with finding-8 | Row k (bounded retry, keep the previous copy, log) is kept (section 4.1). The wear-out case is not stated (finding-8) |
| SA-C-l | N/A | The note does not set how the safe state is entered |

## D. Software safety analysis and hazard traceability

| Id | Answer | Evidence |
|---|---|---|
| SA-D1 | No | SWEHB `swe-205` section 7.7.2 walked: monitoring, the watchdog as an independent control, and common cause (one masked window stops every monitor) apply. The configuration-commit stall is routed (R-4). The driver kick, the overrun-rule conflict and the event-log stall are not (findings 1 to 3) |
| SA-D2 | Yes | No component or criterion changed; 07 section 14.1 and 03 section 4.3 unchanged |
| SA-D3 | Yes | R3: 0 violations, no `HAZARD_CONTROL_UNTRACED` or `HAZARD_INVERSE` |
| SA-D4 | N/A | The product holds no software requirement |
| SA-D5 | N/A | The product holds no hazard-tracing requirement |
| SA-D6 | No | The hazard analysis update is requested for the configuration-commit stall only (findings 2 and 3) |

## E. Peer review, change and configuration assurance

| Id | Answer | Evidence |
|---|---|---|
| SA-E1 | N/A | First review of the product. INSP-075 finding-4 is the keyer host study's own finding: this note answers its routing part (R-4) and part of its row j part (finding-4 here); it does not close it (X-3) |
| SA-E2 | Yes | This record carries the SWE-089 fields of 07 section 10.3 |
| SA-E3 | N/A | The cwht drafts are not yet under CM; the check is made at filing (X-1). The rustos commit `03b1997` adds only the flash pages and one index row, in rustos house style, on an unpushed branch for the owner's merge (OD-23) |
| SA-E4 | N/A | No test is run for credit; the checker is developer evidence |

## F. Assurance risks, metrics and reporting

| Id | Answer | Evidence |
|---|---|---|
| SA-F1 | Yes | RSK-021 covers a hang or corruption during the write; the part-timing assumption A-7 goes to the owner as R-9. The findings are product defects, not new risks |
| SA-F2 | Yes | Front matter: `assurance_findings_major` 3, `assurance_findings_minor` 6, `items_no`, effort |
| SA-F3 | Yes | Verdict, open findings, tasks applied and reliefs are in this record |

## Cross items for the software lead (not findings on the product)

- **X-1 (rule C2).** The three cwht files were reviewed as uncommitted drafts, because the harness lets no agent create them. At filing, the software lead confirms that `git rev-parse HEAD:<path>` equals each cwht blob in `product_files`. If it does, R1 holds from the filing commit. If not, the change needs a delta iteration of both records.
- **X-2.** The paired file review `analysis-fw-b1-dml3-wp-sw-08-10-12.md` is not filed at HEAD `b2bcba0`. When it is, the software lead writes the pairing into both records (`paired_record`, `assurance_reviewer_agent`, `assurance_verdict`); each reviewer updates only its own record.
- **X-3.** INSP-075 finding-4 (keyer host study, Open) stays with INSP-075. This note answers its routing request through R-4. The row j part is complete only after finding-4 here is fixed, and even then it covers only the writes that finding-3 here brings under the rule.
- **X-4.** Findings 1 and 6 also touch the rustos ICD page `02_programming.md` on the unpushed branch `cwht/wp-sw-08`. The fix is a new rustos commit on that branch, before the owner's merge (OD-23), with the pin-move CR (PCR-4) on the new head.

## Commands

- `git -C ~/rust/rustos rev-parse 03b1997:<path>` for the five ICD files, and `git -C ~/rust/rustos diff --stat 48e07ec 03b1997`: 5 files, 323 insertions. `git -C ~/rust/rustos show 03b1997:<path>` to read each page. Only committed objects were read.
- `git hash-object` of the three drafts: `4757a6b6`, `5a070bb0`, `79c95472`.
- Checker re-run from the repository root with the venv: `.venv/bin/python <draft>/check_fw_b1_dml3.py --out <scratch>/results-sa.json`: 54 assertions, 0 failed, exit 0. The regenerated results file equals the draft results file (JSON diff empty).
- Independent Hamming-distance search (`<scratch>/sa/hd_indep.py`). It uses `zlib.crc32` only and none of the author's code: single-bit syndromes over the whole codeword, then collision search for weights 1 to 4. 256-byte record: no undetected pattern of 1 to 4 bits. 512-byte record: 3504 undetected weight-4 pairs. An example, codeword bits 791, 931, 1582 and 3797, flipped in a real record still passes `zlib`. This confirms note section 6.4.
- Datasheet: `git -C ~/rust/rustos rev-parse 2ec64c0:docs/rp2350-datasheet.pdf` = `1b26078d`; the content hash equals that of the scratchpad copy `ds-0220.pdf` (`142c4fe6`). `pdftotext` of printed pages 83 (NMI and PRIMASK, RCP), 232 (`NMI_MASK0/1`), 357 to 358 (hashing), 372 to 373 (flash boot), 379 (boot locks), 385 to 388 (`flash_exit_xip`, `flash_flush_cache`, `flash_op`, `flash_range_erase` and `flash_range_program`), 400 (UF2 erases whole sectors), 1350 to 1351 (RP2350-E10). The cited statements match.
- rustos `48e07ec:firmware/pico2/link.ld` (FLASH 4M, RAM rwx, `.data .data.*` placed in RAM from flash) and `src/lib.rs` (IMAGE_DEF EXE, Secure, Arm; VTOR set to the flash vector table): consistent with note section 4.3 and ICD `01_bootrom_api.md` section 5.4.2.
- `git merge-base --is-ancestor 7784672 HEAD`: false (CR-012 not merged).
- R3: `git archive b2bcba0` exported to the scratchpad, with the three drafts and this record added; then `tools/validate_docs.py` and `tools/traceability.py --report-only --output <scratch>/traceability-report.md` run there. No test with LTspice was run.

## Measurements (SWE-089)

Tasks in the task table: 27 rows (19 applied Yes or No, 8 N/A); 8 answered No. Section items checked: 38 (R1 to R4, SA-A1 to A4, B1 to B3, C-a to C-l, D1 to D6, E1 to E4, F1 to F3), of which 6 answered No (R1, SA-C-f, SA-C-h, SA-C-j, SA-D1, SA-D6). Findings: 3 Major, 6 Minor; 0 fixed; 0 deferred. Iteration 1. Effort: 45 turns, 90 minutes.

## Verdict

```
ASSURANCE VERDICT: NEEDS CHANGES
PRODUCT: docs/design/analysis/fw-b1-dml3-wp-sw-08-10-12.md@4757a6b6, fw-b1-dml3/check_fw_b1_dml3.py@5a070bb0, fw-b1-dml3/fw-b1-dml3-results.json@79c95472 (drafts); rustos docs/icd/rp2350/flash/ (4 pages) and index row at 03b1997; PAIRED RECORD: pending (analysis-fw-b1-dml3-wp-sw-08-10-12.md)
PRODUCT TYPE: design (routed by PDR work plan WP-PDR-41); CRITICALITY: safety-critical
FINDINGS:
- [Major] swe-058 7.1 task 4 (SA-C-j) the flash driver kicks the watchdog before each window without the every-monitor-ran check; REQ-SYS-131 can be exceeded (about 2.09 s).
- [Major] swe-058 7.1 task 2 (SA-C-j) the 401 ms window conflicts with the SW-SCHED rule "tick overrun or missed monitor deadline is an error with response class safe state"; not addressed.
- [Major] swe-205 7.1 task 1 (SA-C-h) the Receive-only write rule covers configuration commits only; event-log flash writes (07 section 16.5) outside Receive and their layout and wear are not covered.
- [Minor] swe-134 7.1 task 6 row j items active or not active not reasoned for every item; 599 ms supervision limit not routed; charge row at risk under ADR-059.
- [Minor] swe-058 7.1 task 3 (SA-C-c) boot after a reset during a busy erase is not stated; DML-5 item missing.
- [Minor] swe-134 7.1 task 4 (SA-C-e) block_size and block_cmd of flash_range_erase not fixed; a wrong pair erases 64 KiB.
- [Minor] swe-058 7.1 task 1 (SA-C-f) image check coverage, length source and common-mode limit undefined; bootrom hash option not considered.
- [Minor] swe-058 7.1 task 1 (SA-C-k) expected commit rate unsourced; worst case at the R-5 limit and wear-out behaviour not stated.
- [Minor] swe-058 7.1 task 1 editorial: the 2.48 ratio is against 404 ms, not the 401 ms design row.
TASKS APPLIED: swe-134 7.1 tasks 1, 4, 5, 6; swe-022 7.1 task 1; swe-057 7.1 task 2; swe-058 7.1 tasks 1 to 5; swe-205 7.1 tasks 1, 3, 4, 5; swe-052 7.1 tasks 1, 2; swe-192 7.1 task 1; swe-070 7.1 task 1; swe-087 7.1 task 1; swe-089 7.1 task 1
TASKS N/A (relief): swe-057 7.1 task 1 and swe-143 7.1 task 1 (07 section 2.1.1 row Design, WP-PDR-32); swe-136 7.1 task 1 (07 section 17.3, 05 section 9.1 class C); swe-134 7.1 task 3 (07 section 9.7); swe-087 7.1 task 2 and swe-088 7.1 task 2 (07 section 10.2); swe-088 7.1 task 1 (paired record not filed)
SWE-134 ITEMS CHECKED: b, c, e, f, g, h, i, j, k
MEASUREMENTS: size=1 note (352 lines), 1 checker (380 lines), 1 results file, 4 ICD pages and 1 index row (323 lines); tasks=27; tasks_no=8; turns=45; minutes=90; major=3; minor=6
```

## Iteration 2: delta verification of finding-1, finding-2 and finding-3 (Major) (2026-09-29, cwht HEAD `220bb8b`)

**Scope (rule C1).** This delta checks only the three Major findings of iteration 1 and the product changes that answer them: note revision 1 (draft blob `8a403ddb`), the checker (`03c960dc`) and the results file (`225e23c4`), and the rustos fix commit `00d5383` on `cwht/wp-sw-08` (parent `03b1997`). It also reads the new design text those fixes brought in (page-append records, the declared window, the write conditions) for defects the fixes introduced. The six iteration 1 Minors (finding-4 to finding-9) were not re-checked. The note's status row and change log say they are held. Under rule C1 they become liens with this APPROVED assurance verdict. The paired reviewer's own Majors (INSP-132 finding-1 and finding-2) belong to INSP-132. They are read here only where they overlap finding-1 to finding-3.

**Independence (rule C4).** This invocation (`sa-reviewer:WP-PDR-41-insp-133-dml3-iter2`) authored no part of WP-SW-08, 10 or 12. It wrote no part of note revision 0 or 1, the checker, either rustos commit, or INSP-132, and it edited no product file. It wrote only this record, as a draft, and scratch files under `wp41/sa4/`.

**Search first.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search. Queries: INSP-133, the DML-3 note and the flash window watchdog; a key input closed at power-on, or a Fault-safe latch. `grep` and `sed` were used afterwards only to pin lines. rustos content was read only as committed objects (`git -C ~/rust/rustos show`, `rev-parse` and `diff` of `03b1997` and `00d5383`). The rustos working tree was not read or changed. LTspice was not run.

**Freeze.** The three cwht files are still uncommitted drafts. Their blobs are the `git hash-object` values in `product_files`. The revision 0 copies kept by the author in `wp41/sw08fr1/rev0/` hash to the iteration 1 blobs `4757a6b6`, `5a070bb0` and `79c95472`, so the delta is measured from the reviewed text. On the rustos side, `git diff --stat 03b1997 00d5383` gives 2 files (`flash/02_programming.md`, `flash/index.md`), 47 insertions and 22 deletions. `01_bootrom_api.md`, `03_xip_qmi.md` and the `rp2350/index.md` row are unchanged. The rustos ref `cwht/wp-sw-08` is at `00d5383`, the head the note names in its header row "ICD pages" and in section 4.9.

### finding-1 (driver-side watchdog feed): Verified

| Fix element asked in iteration 1 | Revision 1 | Reviewer check | Result |
|---|---|---|---|
| Remove the kick from the driver, in the note (section 4.3, section 4.5, R-1) | Section 4.3 row "HardFault" (line 103) now says the watchdog was "last kicked by the main loop just before the window". Section 4.6.2 (line 170) says the driver "never touches the watchdog", and `FlashStore` "holds no `Watchdog` handle". R-1 (line 413) says the watchdog is "kicked only by the main loop after every monitor ran" | Read. No text in the note has the driver feed the watchdog. The only kick is the `SW-SCHED` main loop's (step 1, line 163) | Yes |
| The same in the ICD page (constraint row and step 2) | `02_programming.md` line 36: "The flash driver never touches the watchdog". Old step 2 ("Feed the watchdog; set PRIMASK") replaced by new steps 1 and 2. `index.md` lines 58 to 59: "The flash driver holds no watchdog handle" | `git diff 03b1997 00d5383` read line by line | Yes |
| The window starts only in the main-loop pass right after a supervised kick, checked before masking by a host-tested precondition | Section 4.6.1 item 3 (line 152): "In this pass the kick decision found every monitor on time and kicked". The `plan` decision function takes it as an input (line 155; R-2, R-10) | This is stricter than the iteration 1 example ("time since the last kick plus the longest window at most half the load"). The window cannot start later than the same pass as the kick | Yes |
| The iteration 1 failure case no longer exceeds REQ-SYS-131 | Section 4.6.2 (line 170): 1.1 s from the last main-loop kick to Self-test; checker `hang_to_selftest_design_s` 1.1 and `hang_to_selftest_if_driver_feeds_s` 2.1 | Reviewer timeline (`sa4/sa_iter2.py`): a monitor with period P stops at t0; kicks go on until its deadline t0 + P; reset one load later. From the stop to Self-test: P + 1.1 s with main-loop kicks only (1.10 s at 1 ms, 1.20 s at 100 ms), against P + 2.1 s with a driver feed. REQ-SYS-131 holds for any monitor period up to 0.9 s, the keyer host study basis | Yes |
| Route the rule to WP-PDR-32 and WP-PDR-35 | R-1 goes to WP-PDR-32 and to the writer of 07 (`SW-SCHED` row, MSR-26). R-10 goes to WP-PDR-35 and WP-PDR-32 | Read | Yes |

Observation, not a finding. The note's "1.1 s" (line 170) is measured from the last main-loop kick. From the moment a monitor stops, the figure is the monitor's period plus 1.1 s, as in the keyer host study. The 0.9 s margin of the section 7 row (line 399) is on the same basis. The margin is correct as long as that basis is kept.

### finding-2 (store window against the scheduler overrun rule): Verified

| Fix element asked in iteration 1 | Revision 1 | Reviewer check | Result |
|---|---|---|---|
| The store declares a bounded window before masking | Section 4.6.2 step 2 (line 164): `StoreWindow { start, bound }`, with a bound of 10 ms for a program window and 450 ms for an erase window, entered before the store step. ICD `02_programming.md` steps 2 and 5 (lines 56 onward) | Read. The window is declared before PRIMASK is set, not found after it | Yes |
| The window's missed ticks are counted apart; an overrun or missed deadline outside a declared window stays a safe-state error | Step 4 (line 166): a window over its bound "is a tick overrun: `safe_state()`, the event logged, response class safe state". Within the bound, the missed ticks go to a store-stall count. Step 5 (line 167): a catch-up pass runs every monitor, and the deadline rule applies. Line 174: MSR-26 "counts overruns outside declared windows and every window over its bound" | The relief is narrow. It applies only to the declared store step, only within its bound, and only when the pass that opened the window found every monitor on time (4.6.1 item 3). A monitor that was already late cannot hide behind a window. A monitor that stops during the window is not run by the catch-up pass, so the kick is withheld. The overrun check itself is not weakened | Yes |
| Tell the MSR-26 owner | R-1 (line 413) goes to "the writer of 07 for the section 14.2 `SW-SCHED` row and MSR-26" | Read | Yes |
| Record the trade against designs that shorten the window (boot-only erase; page-append) | Section 4.6.5 (lines 210 to 219) weighs four options, A to D. B (page-append, erase only to reclaim) is adopted. C (erase only at boot) is the fallback if the owner rules (b) at R-11 | Reviewer recomputation: option C is 1.988 s for one boot erase (12 ms margin) and 2.389 s for two. Option A allows 54.8 commits a day. The figures match the note and the checker | Yes |
| The numbers | Section 4.5 and section 4.6.2: 403 ms without a kick (452 ms at the bound); ratios 2.48 and 2.21; largest erase bound 498 ms; largest tolerated erase 449 ms | Checker re-run: 83 assertions, 0 failed, exit 0. The regenerated results equal the draft results file. Reviewer recomputation (`sa4/sa_iter2.py`, no author code): 403 ms and ratio 2.481; 452 ms and ratio 2.212; 498 ms; 449 ms | Yes |
| New DML-5 evidence | Section 9 item 7 (line 433): HostUnit tests of the declared-window logic on the mock clock (within the bound; over the bound; a missed monitor outside a window), a dev-board run with a GPIO marker on each kick, and a fault-injection build that stretches a window past 450 ms | Read. Each branch of the step 4 and step 5 logic has a known-answer case | Yes |

### finding-3 (event-log writes outside Receive): Verified

| Fix element asked in iteration 1 | Revision 1 | Reviewer check | Result |
|---|---|---|---|
| The write-state rule covers every flash erase or program | Section 4.6.1 (line 148): "The rule covers every write through `FlashStore`: the configuration store and the `SW-DIAG` event log". ICD `02_programming.md` line 64 "Write conditions (cwht, every `FlashStore` user ...)"; `index.md` line 55 | Read | Yes |
| Events raised elsewhere wait in RAM | Line 155: they "wait in the log's RAM ring and are written at the next allowed point". The ring size and overflow rule are FW-B2 work. The reset cause is carried in the watchdog `REASON` and scratch registers | Read. Transmit-keyed, Tune and Bench-test can no longer start a window. A new defect in the wait rule is finding-10 | Yes |
| The Receive-only precondition, with PA_EN low and the key inputs open, in a request to WP-PDR-35 (and the stall to WP-PDR-16) | R-10 (line 422), to WP-PDR-35 and WP-PDR-32, holds the full condition list. R-4 (line 416) sends the stall to WP-PDR-16 as "configuration or log write stalls the monitors" | The condition went into R-10 rather than R-4, which iteration 1 named. The receiving packages and the content are the ones asked for | Yes |
| Reserve the event-log sectors in R-3, or say the layout is open | Section 4.4 (line 119) and R-3 (line 415): 8 sectors from 0x3F5000 to 0x3FCFFF, with the application `FLASH` region ending at 0x3F5000. ICD `02_programming.md` line 92 | Checker `layout` entries: every sector is aligned and none is the E10 sector 0x3FF000. 0x400000 - 0x3F5000 = 44 KiB. The reserve is stated as an upper bound for the FW-B2 sizing | Yes |
| Add the event-log erases to the wear budget | Section 4.7 wear table (lines 240 to 243): 2852 erases per sector over 10 years at 100 pages a day (A-F9); 7.5 erase windows a day for both users | Reviewer recomputation: 100 x 3650 / 128 = 2852; 20 x 3650 / 32 = 2281; 20/16 + 100/16 = 7.5 | Yes |

### New findings (iteration 2; defects in the text the fix round added)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-10"></a>finding-10 | assurance | Minor | swe-058 7.1 task 3; SA-C-h, SA-C-k | Note section 4.6.1 item 2 (line 151) and line 155; R-10 (line 422); ICD `02_programming.md` line 64 | While a used key input reads closed, no flash write can start, and nothing bounds or reports how long a write waits. The condition "every key input the key mode uses reads open" applies in Fault-safe as well as Receive. Case 1: ConOps Table 3.4-4 row 1 and section 3.4 item 1 describe a whole Receive session under the KEY inhibit ("headphones read as a closed contact"). Every settings save and every log flush of that session waits in RAM, and all of it is lost when the cells come out, against REQ-SYS-135 and the 07 section 16.5 log. Case 2: in Fault-safe with a key held closed, the Fault entry record is never written to flash before the switch-off exit (T25). Transmit is already disarmed in both cases (REQ-SYS-052; transmit disarmed for the window, line 182), so the key condition adds nothing to safety there. Fix: either drop item 2 when transmit is already disarmed by an inhibit or by Fault-safe (keep PA_EN and `TX_KEY` low), or state the outcome: a counted and shown "settings not saved" state and the log overflow rule. Add the chosen rule to R-10 | Lien (plan rule C1) | | |
| <a id="finding-11"></a>finding-11 | assurance | Minor | swe-058 7.1 task 3; SA-C-b, SA-C-f, SA-C-g | Note section 4.7 (lines 223 to 234), state table row "Erasing the other sector (reclaim)"; section 4.6.2 step 6 (line 168); ICD `02_programming.md` line 71 | The page-append scheme is new in revision 1, and it does not say how the store resumes after a power loss during a reclaim erase or during a page program. The state table gives only the load result. Two cases are left out. (a) An interrupted sector erase can leave cells that read 0xFF but are weakly erased. With no erase-complete marker, the next boot sees a blank sector, programs records into it, and they pass the read-back of step 6. Their retention is then not assured. Once the older full sector is reclaimed, every record present sits in that one weak sector: a common cause for both of the copies row f requires. (b) The scan must treat a page that is neither blank nor valid as used. It must also not program a second time into a page whose program was cut off while it still read blank. Revision 0 re-erased before every write, so it did not have this gap. Fix: state the resume rule. For example, a sector counts as erased only once a completed erase is recorded (a marker page, or a blank check that is re-run as a declared erase window at run time after any boot that finds no marker), and a non-blank invalid page is skipped. Add a DML-5 item: power loss injected during a reclaim erase and during a program, then a check of the next write and load | Lien (plan rule C1) | | |
| <a id="finding-12"></a>finding-12 | assurance | Minor | swe-058 7.1 task 1 (editorial) | Note section 4.5 "Result" (line 140); checker assertion "longest time without a kick ... within the keyer study 0.407 s" | Line 140 says "the longest time without a kick stays inside the 0.407 s interval the keyer host study used". That holds for the 403 ms design value only. The declared erase bound allows 452 ms without an overrun (line 172), which is past 0.407 s, and the checker compares only the design value with 0.407 s. The watchdog load still holds, because 1.0 s / 0.452 s = 2.21, above the factor of 2 the keyer study requires. Fix: base the sentence on the factor of 2 at the bound (as line 172 already does), or also state that 452 ms is past the keyer study interval but still meets its factor | Lien (plan rule C1) | | |

No new Major. The page-append scheme, the declared window and the write conditions were also read for any change to the safety controls. The catch-up pass, the 1 s spacing between windows, and the output states set before the window keep every row j item in the section 4.6.3 table at least as protected as in revision 0. REQ-SYS-155 in an erase window (404 ms by design, 453 ms at the bound) is INSP-132 finding-2's. From the assurance side: PA_EN is held low for the whole window, and the row h thermal prerequisite blocks PA_EN until a valid reading comes in. REQ-SYS-181 is a firmware-independent cut-off (read: "independently of firmware", 100 ms at 95 C). L-5 records the non-compliance until the owner rules R-11. Rule C10 holds that ruling until this pair of records is APPROVED.

### Iteration 1 Minors (not re-checked; liens)

finding-4 to finding-9 stay as written in iteration 1 and become liens under plan rule C1, due at the CDR readiness declaration. Owner: the note author (firmware developer role, WP-PDR-41). Some revision 1 text touches them, and the software lead may use that at the lien pass without a new review. Two examples. The section 4.6.3 table now gives every row j item with a reason, and R-4 carries a battery period limit of 547 ms (the iteration 1 figure was 599 ms, before the 1 ms passes and the bound). This covers most of finding-4, but not its "AT RISK (A5 CRs)" mark on the charge row. The 2.48 ratio is now correctly labelled as 1.0 s / 403 ms (line 135), which answers finding-9. finding-5 to finding-8 are untouched. For finding-8: with page-append, the R-5 limit of 1440 commits a day gives a configuration-sector life of about 6.1 years (reviewer figure), up from the 139 days of revision 0.

| Finding | Severity | Disposition | Owner | Due |
|---|---|---|---|---|
| finding-4 | Minor | Lien (plan rule C1) | note author, WP-PDR-41 | CDR readiness declaration |
| finding-5 | Minor | Lien (plan rule C1) | note author, WP-PDR-41 | CDR readiness declaration |
| finding-6 | Minor | Lien (plan rule C1); the ICD part is a rustos commit on `cwht/wp-sw-08` before the owner's merge (X-4) | note author, WP-PDR-41 | CDR readiness declaration |
| finding-7 | Minor | Lien (plan rule C1) | note author, WP-PDR-41 | CDR readiness declaration |
| finding-8 | Minor | Lien (plan rule C1) | note author, WP-PDR-41 | CDR readiness declaration |
| finding-9 | Minor | Lien (plan rule C1); answered by revision 1 line 135 | note author, WP-PDR-41 | CDR readiness declaration |
| finding-10 | Minor | Lien (plan rule C1) | note author, WP-PDR-41 | CDR readiness declaration |
| finding-11 | Minor | Lien (plan rule C1) | note author, WP-PDR-41 | CDR readiness declaration |
| finding-12 | Minor | Lien (plan rule C1) | note author, WP-PDR-41 | CDR readiness declaration |

Open Major: 0. Open Minor: 0 (nine liens). Verified: 3 (finding-1 to finding-3). Deferred: 0.

### Task and section answers changed by this delta

| Item | Iteration 1 | Iteration 2 | Evidence |
|---|---|---|---|
| swe-057 7.1 task 2 | No (finding-3) | Yes | The window rule now covers both `FlashStore` users (finding-3 Verified) |
| swe-058 7.1 task 2 | No (finding-1, finding-2) | Yes | The kick rule and the overrun rule of the `SW-SCHED` row are met by the declared window (finding-1 and finding-2 Verified) |
| swe-058 7.1 task 3 | No | Yes, with finding-5, finding-10 and finding-11 (Minor) | The iteration 1 undesired behaviours are analysed (safe state on every commit, event-log stall). The busy-flash boot (finding-5), the closed-key wait (finding-10) and the interrupted-reclaim resume (finding-11) are liens |
| swe-058 7.1 task 4 | No | Yes | REQ-SYS-131 holds under the main-loop-only kick (1.1 s from the last kick). Row j is accounted for item by item, and REQ-SYS-155 in an erase window is routed (R-11, L-5) |
| swe-134 7.1 task 1 | No | Yes, with finding-7 (Minor) | Items h and j met (SA-C-h, SA-C-j below); item f keeps the image-coverage lien |
| swe-134 7.1 task 6 | No | Yes | The stall, the window rule and REQ-SYS-155 are routed to WP-PDR-16, 28, 32, 35 and 45 and to the 07 writer (R-1, R-4, R-10, R-11) |
| swe-205 7.1 task 1 | No | Yes | With no driver kick, K7 is no longer weakened. The overrun rule is kept, with a declared relief. The log writes fall under the write rule. The residual stall goes to WP-PDR-16 (R-4) |
| swe-205 7.1 task 5 | No | Yes | The requested update now covers both writers and the REQ-SYS-155 case (R-4, R-11) |
| swe-087 7.1 task 2, swe-088 7.1 task 2 | N/A | Yes | This delta: each iteration 1 Major fix checked element by element, and none closed without evidence |
| swe-088 7.1 task 1 (SA-A4) | N/A | Yes, for INSP-132 iteration 1 | INSP-132 iteration 1 draft (blob `83c326bf`): checklist `peer-review-checklist-design` revision B, which WP-PDR-41 assigns; 57 `CK-` rows answered; the same eight blobs as this record's iteration 1. Its iteration 2 is pending (X-6) |
| SA-A3 | N/A | Yes | INSP-132 author `author:WP-PDR-41 ...`, reviewer `reviewer:WP-PDR-41-dml3-iter1`, and this record's reviewers are three separate invocations |
| SA-C-h | No | Yes, with finding-10 (Minor) | The prerequisites of every flash write are a stated and host-checked constraint (4.6.1, R-2, R-10) |
| SA-C-j | No | Yes | Findings 1 to 3 Verified; the finding-4 remainder is a lien |
| SA-C-b | Yes | Yes, with finding-11 (Minor) | The four row b states hold for page-append; resuming after an interrupted reclaim is not stated |
| SA-D1 | No | Yes | The three contributions of iteration 1 are removed or routed (R-4, R-10, R-11) |
| SA-D6 | No | Yes | Same as swe-205 task 5 |
| SA-E1 | N/A | Yes | This delta verifies the iteration 1 Majors. The iteration 1 Minors are liens with owner and due date (table above) |
| R1 | No (X-1) | No (X-1) | The three cwht files are still uncommitted drafts |
| R3 | Yes | Yes | Re-run for iteration 2 (Commands) |
| R4 | Pending | Yes for iteration 1; pending for iteration 2 (X-6) | Above |

SA-C-f stays "No" only because of finding-7 (Minor, image coverage), now a lien. For the configuration copies, row f is met by page-append: from the second commit on, the newest and the previous record are both present. The weak-erase common cause is finding-11.

### Cross items (iteration 2, for the software lead)

- **X-1 (unchanged).** At filing, the software lead checks that `git rev-parse HEAD:<path>` equals each of the three revision 1 cwht blobs in `product_files`. If so, R1 holds from the filing commit. If not, both records need a delta.
- **X-4 (updated).** The rustos fix is one commit on top, `00d5383` (no amend). The PCR-4 pin-move CR names `00d5383`, or a later head that answers the finding-6 lien, not `03b1997`. The branch is not pushed. The owner merges it as rustos maintainer (OD-23).
- **X-5.** INSP-132 iteration 1 has `assurance_verdict: pending` and `assurance_findings_major: 0`. After this delta the values are APPROVED, 3 Major and 9 Minor. INSP-132 copies them in its own iteration 2. Each reviewer updates only their own record.
- **X-6.** INSP-132 iteration 2, the delta of its finding-1 and finding-2, is not written yet. The record verdict of both records stays held until it is, and until X-1, X-4 and the CR-012 merge are done.
- **X-7.** Observation outside assurance scope, for INSP-132 and the author: a receive-audio mute of about 0.45 s, about 7.5 times a day at arbitrary times in Receive (log reclaims included), is a usability effect of the mute before each window (line 193). The mute itself is a safety control, since the audio limiter cannot run during a window. Whether the dropout is acceptable is a design question, not a safety one.

### Commands (iteration 2)

- `git -C ~/rust/rustos for-each-ref refs/heads/cwht/`: `cwht/wp-sw-08` at `00d5383`. `git -C ~/rust/rustos log -1 --format='%H %P' 00d5383`: parent `03b1997`. `git -C ~/rust/rustos diff --stat 03b1997 00d5383` and `diff 03b1997 00d5383`: 2 files, +47 -22, read in full. `git -C ~/rust/rustos rev-parse 00d5383:<path>` for the five ICD files. Only committed objects were read.
- `git hash-object` of `wp41/sw08fr1/rev0/*` (equal to the iteration 1 blobs) and of the three revision 1 drafts (`8a403ddb`, `03c960dc`, `225e23c4`). `git diff --no-index` of revision 0 against revision 1 (note: 132 insertions, 44 deletions) and of the checker, read in full.
- Checker re-run from the repository root: `.venv/bin/python <draft>/check_fw_b1_dml3.py --out <scratch>/sa4/results-sa.json`: 83 assertions, 0 failed, exit 0, 1.3 s. JSON comparison with the draft results file: equal.
- Reviewer recomputation `wp41/sa4/sa_iter2.py` (arithmetic and a timeline for a stopped monitor; no author code imported): values quoted in the tables above.
- `docs/requirements/sys/requirements.json`: statements of REQ-SYS-052, 067, 135, 155, 163 and 181 read for the finding-10 cases and the REQ-SYS-155 argument. `docs/conops/conops.md` Table 3.4-4 row 1 and section 3.4 item 1 for the KEY inhibit.
- R3: `git archive 220bb8b` exported to `wp41/sa4/exp/`, with the three revision 1 drafts, the INSP-132 iteration 1 draft and this record added. `tools/validate_docs.py` and `tools/traceability.py --report-only --output <scratch>` were run there: `validate_docs` 121 passed, 0 failed, exit 0 (this record and INSP-132 PASS); `traceability` 245 requirements, 0 violations, 2 warnings (`SYS_UNALLOCATED` REQ-SYS-125 and 148, neither touched by this product), exit 0. Nothing was written into `docs/vv` of the repository.
- `git merge-base --is-ancestor 7784672 220bb8b`: false (CR-012 not merged).

### Measurements (SWE-089), iteration 2

Majors re-checked: 3; Verified: 3. Fix elements checked: 16 (finding-1 5, finding-2 6, finding-3 5); all Yes. New findings: 3 Minor, 0 Major. Liens: 9. Task and section answers changed: 20 rows (table above). Reviewer recomputations: 14 values and a stopped-monitor timeline at 4 monitor periods. Effort this iteration: about 30 turns and 60 minutes (the front matter totals include iteration 1).

### Verdict (iteration 2)

```
ASSURANCE VERDICT: APPROVED (liens)
PRODUCT: docs/design/analysis/fw-b1-dml3-wp-sw-08-10-12.md@8a403ddb, fw-b1-dml3/check_fw_b1_dml3.py@03c960dc, fw-b1-dml3/fw-b1-dml3-results.json@225e23c4 (revision 1 drafts); rustos docs/icd/rp2350/flash/ (4 pages) and index row at 00d5383; PAIRED RECORD: INSP-132 (iteration 2 pending)
PRODUCT TYPE: design (routed by PDR work plan WP-PDR-41); CRITICALITY: safety-critical
FINDINGS:
- [Major] finding-1 Verified: the flash driver never touches the watchdog; the window starts only in the pass of a main-loop kick after every monitor ran; hang to Self-test 1.1 s from the last kick.
- [Major] finding-2 Verified: the store window is a declared SW-SCHED state with 10 ms and 450 ms bounds; over the bound is a safe-state overrun; catch-up pass before the next kick; MSR-26 kept; four options weighed, page-append adopted.
- [Major] finding-3 Verified: the write rule covers the configuration store and the event log; log events wait in RAM; 32 KiB log reserve in R-3; log wear 2852 erases per sector over 10 years.
- [Minor] finding-10 (new, lien): writes wait with no bound or report while a used key input reads closed (KEY inhibit session, Fault-safe with a key closed); lost on cell removal.
- [Minor] finding-11 (new, lien): page-append resume after a power loss in a reclaim erase or a program not stated; weak-erase common cause for both records.
- [Minor] finding-12 (new, lien): section 4.5 says the time without a kick stays inside 0.407 s; true for 403 ms, not for the 452 ms bound.
- [Minor] finding-4 to finding-9: liens (plan rule C1), not re-checked.
RECORD VERDICT: NEEDS CHANGES (held: cwht drafts not filed, X-1; INSP-132 iteration 2 pending, X-6; rustos cwht/wp-sw-08 not merged, X-4; CR-012 not merged)
```
