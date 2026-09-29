# FW-B1 DML-3 note: WP-SW-08 flash write, WP-SW-10 UART0 telemetry and WP-SW-12 CRC-32

| Field | Value |
|---|---|
| Product | DML-3 note of WP-PDR-41, "FW-B1 PDR point for WP-SW-08, 10 and 12" (`docs/plan/pdr-work-plan.md` revision 7, blob `fd521750`, WP-PDR-41; `docs/plan/technology-assessment.md` blob `d46abde0` sections 1 and 3.18) |
| Status | Draft, revision 1, fix round 1 of review iteration 1: the two Major findings of the review record and the three Major findings of its SA pair are fixed; the Minor findings are held under plan rule C1. It proposes designs and values; it changes no requirement, hazard, risk or interface file (plan section 5.3) |
| Author | Claude, firmware developer role, WP-PDR-41 author invocation, 2026-09-29 |
| Review records (plan WP-PDR-41) | `docs/reviews/PDR/checklists/analysis-fw-b1-dml3-wp-sw-08-10-12.md` (independent code reviewer, design checklist) and `analysis-fw-b1-dml3-wp-sw-08-10-12-software-assurance.md` (SA, for WP-SW-08 and WP-SW-12) |
| Analysis kind | timing and worst-case budget, algorithm reference model, interface analysis; criticality: WP-SW-08 and WP-SW-12 serve the safety-critical configuration guard and image check (`SW-SAFE` `cfg_guard`, `SW-BOOT`, HZ-014; 07 section 14.1), WP-SW-10 serves verification |
| ICD pages | WP-SW-08: rustos branch `cwht/wp-sw-08` at `00d5383` (section 4.9; `docs/icd/rp2350/flash/`, not pushed, for the owner's merge, OD-23). WP-SW-10: the committed rustos `docs/icd/rp2350/uart/` at `2ec64c0` (section 5.2). WP-SW-12: section 6 of this note (cwht-local; there is no register ICD) |
| Checker | `docs/design/analysis/fw-b1-dml3/check_fw_b1_dml3.py` (asserts every computed number below) |
| Outputs | `docs/design/analysis/fw-b1-dml3/fw-b1-dml3-results.json` |
| Reproduce | `cd /Users/robinonsay/rust/cwht && .venv/bin/python docs/design/analysis/fw-b1-dml3/check_fw_b1_dml3.py` (exit 0, 83 assertions, about 2 s; needs `numpy` from the venv) |
| Credit | Developer evidence (`docs/process/05-configuration-and-data-management.md` section 9.1): the checker has no TV record. DML-3 only; the move to DML-5 is FW-B2 work before CDR (section 9) |

## 1. Question and scope

The technology assessment (section 3.18, "Plan to PDR") puts WP-SW-08, WP-SW-10 and WP-SW-12 at DML-3 at PDR "with their ICD pages extracted". Its DML-3 row (section 1.1) reads, for firmware: "Reference model or golden vectors exist; datasheet ICD extracted for the driver", and, for the analytical part: "Analytical proof of the critical function: budget or hand analysis against the requirement". For each package this note names the critical function, proves it against its requirement by budget or hand analysis, and points to the ICD page:

| Package | Critical function | Requirement it serves | Proof here | ICD page |
|---|---|---|---|---|
| WP-SW-08 flash write (`FlashStore`, 07 section 19) | Erase a sector and program a page through the bootrom with no flash fetch while XIP is off, in bounded time, leaving at least one valid configuration copy at every instant, for the configuration store and the event log, without a false scheduler fault or watchdog reset and with every row j budget accounted for | REQ-SYS-134, REQ-SYS-135, REQ-SYS-131 (the stall and the kick), REQ-SYS-155 (section 4.6), 07 section 14.2 rows e, f, g, k for `cfg_guard` and `SW-CFG`, the `SW-SCHED` row (j, k, l) and row j; 07 section 16.5 (`SW-DIAG` log); RSK-021 | Section 4 | rustos `docs/icd/rp2350/flash/` (new, section 4.9) |
| WP-SW-10 UART0 | Emit the telemetry and trace lines on the 3.3 V UART pads with USB absent, decodable by the bench logic capture, without delaying any safety task | REQ-SYS-150 (with REQ-SYS-142 pads, REQ-SYS-002 mode trace, TC-SYS-095); the UART0 trace channel of ICD-SW-HOST (written by WP-PDR-36a) | Section 5 | rustos `docs/icd/rp2350/uart/` at `2ec64c0` (committed) |
| WP-SW-12 CRC-32 (`cwht-core`) | Detect corruption of the image and of each configuration copy | REQ-SYS-132; 07 section 14.2 row f (two CRC-32 copies with a sequence number; RAM copy checked every 100 ms; image trailer at boot); REQ-SYS-134; CS-32 | Section 6 | Section 6 (algorithm page) |

Out of scope: the driver code, contract tests and dev-board checks (FW-B2, section 9); the event-log record format and ring sizing (FW-B2; this note reserves its flash, section 4.4, and bounds its writes and wear, sections 4.6 and 4.7); the choice between UART and USB for the host channel (OD-15; PCR-7 if the CR route is taken).

## 2. Sources and page convention

**Datasheet.** RP2350 datasheet, build 2025-02-20, 1369 pages: rustos `docs/rp2350-datasheet.pdf` at `2ec64c0` (git blob `1b26078d`, read by `git show`), the copy the FW-B1 ADRs cite (ADR-051 "Research consulted"). Page numbers below are the **printed page numbers** of the page footer; in this build the PDF page index is the printed number plus 1. A later build (2025-07-29, 1380 pages) exists in the session scratchpad; it was not used for citations.

| # | Figure or statement used | Section | Printed page |
|---|---|---|---|
| D1 | ROM words at 0x10 to 0x19: magic, version, table and lookup pointers | 5.4.1, Table 452 | 376 |
| D2 | Lookup by two-character code, `RT_FLAG_FUNC_ARM_SEC` | 5.4.1 | 377 |
| D3 | Return codes, including -4, -10, -11, -19 | 5.4.3 | 378 |
| D4 | Boot locks; `LOCK_ENABLE` off by default; XIP returns bus faults during direct-mode programming | 5.4.4 | 379 |
| D5 | Low-level flash functions are Arm-S and RISC-V only | 5.4.6.1 | 380 |
| D6 | `connect_internal_flash` restores QSPI pads and connects QMI | 5.4.8.3 | 384 |
| D7 | `FLASH_DEVINFO` default: 16 MB on CS0 | 5.4.8.5 | 385 |
| D8 | `flash_exit_xip`: direct mode, basic 03h XIP at CLKDIV 12 | 5.4.8.7 | 385 |
| D9 | `flash_flush_cache` invalidates every line, unpins pinned lines | 5.4.8.8 | 386 |
| D10 | `flash_op` checks alignment, bounds, partitions; sequence connect, exit XIP, op, flush, XIP setup; XIP bus error during the operation | 5.4.8.9 | 386 to 387 |
| D11 | `flash_range_erase`: 4096-byte alignment and multiple; no argument validation; XIP from DMA, debugger or the other core faults | 5.4.8.10 | 387 |
| D12 | `flash_range_program`: 256-byte alignment and multiple; no validation | 5.4.8.11 | 387 |
| D13 | `flash_select_xip_read_mode` modes 0 to 3; 8-bit command prefix in every bootrom XIP mode; default XIP setup function in boot RAM | 5.4.8.14 | 388 |
| D14 | `xip_setup_func_ptr`, code `'X','F'` | 5.4.8.30 | 398 |
| D15 | Boot read modes: EBh quad at divisor 3 tried first, then down to 03h at 24 | 5.2.7, Table 451 | 372 to 373 |
| D16 | UF2 downloads erase whole 4 kB sectors | 5.5.2 | 400 |
| D17 | RP2350-E10: absolute block at the end of flash, written first; A2 silicon | Appendix E | 1350 to 1351 |
| D18 | XIP windows 0x10, 0x14, 0x18, 0x1c; 16 kB cache; coherence only a concern around programming | 4.4, 4.4.1 | 341 |
| D19 | Direct mode: XIP window disconnected, access faults | 12.14.5 | 1232 |
| D20 | QMI base 0x400d0000; `DIRECT_CSR`, `M0_TIMING` offsets | 12.14.6, Table 1292 | 1233 to 1234 |
| D21 | `M0_TIMING.CLKDIV` bits 7:0, reset 4, SCK period in `clk_sys` cycles, may change on the fly | 12.14.6 | 1239 |
| D22 | NMI ignores PRIMASK; NMI sources: `NMI_MASK0/1` and a failed RCP check | 3.2.1 | 83 |
| D23 | `NMI_MASK0` reset 0x00000000 | 3.7, Table 362 | 232 |
| D24 | UART0 IRQ 33 | 3.2, Table 94 | 82 |
| D25 | UART0 base 0x40070000 | 2.2 | 32 |
| D26 | UART block: PL011, 32 x 8 TX FIFO, UARTCLK = `clk_peri` | 12.1.1 | 958 |
| D27 | Baud divisor: `UARTCLK / (16 x baud)`, 16-bit integer and 6-bit fraction; clock limits | 12.1.3.2.1 | 961 to 962 |
| D28 | UART0 `RESETS` bit 26 | 7.5, Table 534 | 503 |
| D29 | IO levels at IOVDD 3.3 V: VOH at least 2.62 V, VOL at most 0.5 V, VIH at least 2 V, VIL at most 0.8 V | 14.9.4, Table 1435 | 1335 to 1336 |
| D30 | DMA sniffer computes CRC-32 (IEEE 802.3 polynomial), MSB-first and LSB-first | 12.6.8.2; SNIFF_CTRL | 1104; 1133 |

**Other sources.** Pico 2 datasheet (rustos `docs/pico-2-datasheet.pdf` at `2ec64c0`) chapter 1, printed page 4: the flash is a Winbond W25Q32RV (4 MB), and the IO voltage is fixed at 3.3 V. Repository inputs at `main` `be49be6`: `docs/requirements/sys/requirements.json` (blob `f128235e`), `docs/process/07-software-engineering-plan.md` (`bfe05f43`), `docs/design/analysis/keyer-host-study.md` (`32f4a139`; section 6.5, A-7, A-8, R-1, R-2), `docs/research/rustos-toolchain-proof.md` (`74e5363f`; F5, F8, F15), `docs/design/analysis/spurs-ts012.md` (`9b426bf1`; C1, C3, C4), ADR-051 (`7085cf5a`), ADR-052 (`58c06b4f`), `docs/icd/ICD-CTL-USB.md` (`0c254196`), `docs/risk/register.json` (`6685aa0e`; RSK-021), `docs/test_cases/sys/test_cases.md` (`45e7ca51`; TC-SYS-002, 095), `docs/research/emulator-accreditation-and-timer-irq.md` (`ede033aa`; F12, KA-2).

## 3. Assumptions

| Id | Assumption | Effect | Closed by |
|---|---|---|---|
| A-7 (inherited) | W25Q32RV 4 KB sector erase at most 400 ms, page program at most 3 ms, read-back at most 1 ms (Winbond W25Q-family values; the part datasheet is not in the repository) | Sets the masked windows, the longest time without a watchdog kick and the row j latencies (sections 4.5, 4.6) | The part datasheet into the corpus (owner download permission, request R-9) and the DML-5 dev-board measurement. Section 4.6 gives the largest erase time the design tolerates (449 ms, the declared erase bound less the overhead) |
| A-8 (inherited) | Bootrom plus runtime to Self-test at most 100 ms | Boot-time share of REQ-SYS-131 | Section 6.5 bounds the image check inside it; dev-board boot measurement |
| A-F1 | The Pico 2 flash answers EBh quad reads, so the boot XIP mode is EBh at divisor 3 (D15) | Image-check and read-back time (sections 4.5, 6.5) | DML-5: read `M0_RCMD` and `M0_TIMING` after boot |
| A-F2 | Window overhead (connect, exit XIP, flush, XIP setup) at most 1 ms | Masked window (section 4.5) | DML-5 measurement with the logic capture on a GPIO marker |
| A-F3 | The 4 MB W25Q32RV decodes 22 address bits, so offset 0xFFFF00 aliases to 0x3FFF00 | The RP2350-E10 finding (section 4.4) | Part datasheet (R-9); DML-5 check of section 9 item 3 either way, since the layout avoids the last sector |
| A-F4 | 100 000 erase cycles per sector | Wear budget (section 4.7) | Part datasheet (R-9) |
| A-F5 | Service life 10 years for the wear budget | Wear budget | Owner ruling if a different life is wanted |
| A-F6 | Bootrom, runtime and clock bring-up, without the image check, at most 30 ms | Section 6.5 | Dev-board boot measurement |
| A-F7 | Table-driven CRC-32 at most 12 `clk_sys` cycles per byte on the Cortex-M33 with the table in SRAM | Sections 6.5 and 5.3 | DML-5 cycle count (SysTick or TIMER0 around a 4 KiB buffer) |
| A-F8 | One main-loop pass with every task due (every monitor, the kick decision, the store preparation) takes at most 1 ms, one tick: the MSR-26 target of no overrun outside a declared window implies it | Longest time without a kick and the row j latencies (section 4.6) | MSR-26 HostUnit and dev-board loop time (GPIO marker); DML-5 check 7 (section 9) |
| A-F9 | The event log writes at most 100 pages a day on average (one page per flush; FW-B2 sets the flush rule) | Log wear and the number of erase windows (section 4.7) | FW-B2 log design; the log's own page counter read at Bench |

## 4. WP-SW-08 flash write

### 4.1 Critical function and requirements

The configuration store (`SW-CFG`, 07 section 14.2, mission-critical, HZ-014 through the guard) keeps its records, each with a CRC-32 and a sequence number, in two sectors A and B, so that at least two copies are present (row f; section 4.7). A commit follows the `cfg_guard` sequence of row e: validate the new record, write the inactive copy, read it back and CRC-check it, then advance the sequence number; erase and program errors are retried a bounded number of times and then the previous copy is kept and the event logged (row k). REQ-SYS-134 replaces a corrupt or out-of-range setting by its default at load, REQ-SYS-135 keeps every setting across power cycles and cell removal, and the ICD-CTL-USB "Initialization and status" row says settings survive a firmware load. RSK-021 is the risk that a write "hangs or corrupts configuration while XIP is disabled". The second `FlashStore` user is the `SW-DIAG` event log, a CRC-protected ring in flash (07 sections 16.5 and 19). The critical function of WP-SW-08 is therefore: program one 256-byte page into a blank page of the store, and erase one 4 KiB sector only to reclaim it (section 4.7), with no fetch from flash while XIP is off, in a bounded time, without touching the newest record, and, for both users, only where the scheduler and the row j budgets allow the stall (section 4.6).

### 4.2 The bootrom interface (ICD `01_bootrom_api.md`)

The driver calls six ROM entries (D5, D6 to D14), found through the ROM table (D1, D2): `connect_internal_flash` (`'I','F'`), `flash_exit_xip` (`'E','X'`), `flash_range_erase` (`'R','E'`), `flash_range_program` (`'R','P'`), `flash_flush_cache` (`'F','C'`) and the boot-RAM XIP setup function (`'X','F'`). The range functions take flash offsets, are `void` and validate nothing (D11, D12); `flash_op` validates, but only against the 16 MB default size (D7, D10), which is wider than the store. The driver therefore checks every request itself in a host-tested pure function (CS-38): an erase must be exactly one store sector (configuration A or B, or one event-log sector), a program exactly one page of such a sector, and the mode and output conditions of section 4.6.1 must hold; anything else is rejected before any register or ROM call (07 section 14.2 row e: an erase or program request outside the guard sequence is rejected). Boot-lock checking is off by default and rustos does not enable it (D4), so no lock is taken.

### 4.3 Proof that nothing fetches from flash while XIP is off

From `flash_exit_xip` until the range function returns, QMI is in direct mode and any XIP access is a bus fault (D10, D11, D19). Every possible source of an XIP access in that window is listed and closed:

| Source | Closed by | Evidence at DML-3 | Evidence at DML-5 |
|---|---|---|---|
| Core 0 instruction fetch of the driver | The window function is linked in `.data.ramfunc` (SRAM, copied by `reset_data()`; research F8 item 5) and calls only ROM addresses resolved before the window | rustos `link.ld` places `.data.*` in RAM (F8) | Disassembly of the linked ELF: every branch target inside the window lies in SRAM (0x2000_0000 to 0x2008_1FFF) or ROM (below 0x0000_8000); no call to `memcpy`, panic or formatting code |
| Core 0 data access | Arguments, the page buffer, the ROM pointers and the XIP-setup copy are in SRAM; no `const` table, literal pool or `.rodata` read in the window | Design rule of the ICD page `02_programming.md` | Same disassembly: every load address in the window is SRAM, ROM or a peripheral |
| Interrupts, SysTick, PendSV | PRIMASK set for the whole window (the WP-SW-09 critical section, ADR-052); it masks every exception of configurable priority | ADR-052 | Dev-board check with TIMER0 alarms armed during an erase: none serviced until PRIMASK clears (the missed match is then reported `Due`, ADR-053) |
| NMI | `NMI_MASK0/1` stay at their reset value 0 (D22, D23); the only other NMI source is a failed RCP integrity check (D22) | No rustos or cwht code writes `NMI_MASK` (inspection) | Same |
| HardFault or other fault inside the window | Its handler address is in the flash vector table, so the core locks up; the watchdog, last kicked by the main loop just before the window (section 4.6.2) and still counting, resets the chip within its load (1.0 s) of that kick | This is the bounded outcome of RSK-021: a reset, not a hang | Fault-injection build: a deliberate XIP read inside the window ends in a watchdog reset |
| Core 1 | Stays in the bootrom wait state (CS-23; ADR-052 decision item 1) | CS-23 | Inspection: no core 1 launch |
| DMA | No DMA channel reads or writes an XIP window (cwht uses no DMA in Rev A) | 07 section 19 (WP-SW-12 "no DMA sniffer dependency") | Inspection: no DMA channel configured |
| Debugger | A debugger read of XIP in the window faults (D11); this affects bench sessions only | ICD note | Not credited |

With every source closed, the first XIP access after `flash_exit_xip` is the one made after the range function has returned, when XIP is basic 03h at CLKDIV 12 and accessible (D8, D10). The flush (D9) and the XIP setup (D13, D14) then restore the cached boot mode. If the application sets its own QMI divisor (spurs-ts012 C4: divisor 2 at 96 MHz), it rewrites `M0_TIMING.CLKDIV` after the XIP setup, before PRIMASK clears (D21).

### 4.4 Store layout and the RP2350-E10 finding

Research F15 proposed the store in "the top two sectors (0x103FE000 and 0x103FF000)". The last of these is the RP2350-E10 target:

- picotool `--abs-block` adds the E10 block "targeting 0x10ffff00" (research F5, recorded output), and release images carry it (ICD-CTL-USB section 3.2.6, row "Message or command set").
- Offset 0xFFFF00 lies inside the 16 MB default CS0 size (D7), so the bootrom writes it, first (D17).
- If the 4 MB device ignores address bits above 21 (A-F3), the block lands at 0x3FFF00, and because a UF2 download erases whole 4 kB sectors (D16), the whole sector 0x3FF000 is erased on every firmware load.
- With copy B at 0x3FF000, every firmware load would lose copy B. When B holds the newer record, the unit comes up on the older copy A: settings silently roll back one commit, against REQ-SYS-135 and the ICD-CTL-USB statement that settings survive the load. The two-copy scheme hides the loss from the CRC check, so no fault is reported.

**Proposed layout (for WP-PDR-32 and ICD-SW-HOST, request R-3):** the `SW-DIAG` event log in an 8-sector (32 KiB) reserve at offsets 0x3F5000 to 0x3FCFFF (XIP 0x103F5000), configuration sector A at 0x3FD000 (0x103FD000), sector B at 0x3FE000 (0x103FE000), and sector 0x3FF000 left unused for the E10 block; the application `FLASH` region ends at 0x3F5000, 44 KiB below the device end. The log reserve is an upper bound for the FW-B2 ring sizing; if that sizing needs more, R-3 is revised before the linker script is fixed. The checker confirms the alignment and that no store or log sector is the E10 sector (the `flash` entries of the results file). The layout is correct whether or not A-F3 holds.

### 4.5 Time budget

| Item | Value | Source |
|---|---|---|
| Sector erase, maximum | 400 ms | A-7 |
| Page program, maximum | 3 ms | A-7 |
| Window overhead | 1 ms | A-F2 |
| Record | one 256-byte page (section 6.4 gives the reason), appended to a blank page (section 4.7) | this note |
| Program window (15 of every 16 writes) | 4 ms | checker |
| Erase window (only to reclaim a sector, section 4.7) | 401 ms | checker |
| Declared window bounds (section 4.6.2) | 10 ms program, 450 ms erase | this note (proposal) |
| Longest time without a watchdog kick: store preparation after the kick, erase window, catch-up pass | 403 ms (452 ms at the erase bound) | checker; A-F8 |
| Keyer host study bound (erase, two pages, read-back) | 407 ms | keyer host study section 6.5 |
| Watchdog load (keyer host study R-1) | 1.0 s | keyer host study section 6.5 |
| Ratio of the load to the longest time without a kick | 2.48 (2.21 at the erase bound); at least 2 required by the keyer study check | checker |
| Largest erase bound that keeps the ratio of 2 | 498 ms | 1.0 s / 2 - 2 x 1 ms |
| Largest sector erase the design tolerates before the bound declares an overrun | 449 ms | 450 ms - 1 ms |
| Read-back of 256 bytes after the flush, worst mode 03h / CLKDIV 12 at 96 MHz | 0.38 ms (under the 1 ms of A-7) | 256 x 144 cycles; ICD `03_xip_qmi.md` |

Result: the longest time without a kick stays inside the 0.407 s interval the keyer host study used to set the watchdog load, so the REQ-SYS-131 proposal of that study (2 s, design load 1.0 s) stands unchanged. Against A-7 there are 49 ms of erase time before the erase bound; a slower part then shows as a logged overrun fault (section 4.6.2), not as a watchdog reset.

### 4.6 The store window, the scheduler and the row j budgets

While PRIMASK is set, no 1 kHz sample, monitor or alarm runs: for up to 4 ms in a program window and up to 401 ms in an erase window. Three sets of rules meet this stall. The first is the 07 section 14.2 `SW-SCHED` row: "every monitor task dispatched within its period, and the watchdog (2 s, REQ-SYS-131) kicked only when all ran", and "a tick overrun or a missed monitor deadline is an error with response class safe state". The second is keyer host study R-1: the watchdog is "fed from the main loop only after every safety monitor has run". The third is the row j response budgets. Revision 0 did not reconcile the window with the first (review finding-1, SA finding-2), fed the watchdog from the driver against the second (SA finding-1), and left REQ-SYS-155 out of the third (review finding-2). This section gives the design that meets all three.

#### 4.6.1 Where a flash write may start (every `FlashStore` user)

The rule covers every write through `FlashStore`: the configuration store and the `SW-DIAG` event log (07 sections 16.5 and 19), not only settings saves (SA finding-3). A program or erase window starts only when all of these hold:

1. The mode is Receive, or Fault-safe, whose outputs are already the `safe_state()` set of row l. Never Transmit-keyed, Tune, Bench-test, Self-test, Charging or firmware update.
2. PA_EN and `TX_KEY` read low, and every key input the key mode uses reads open (keyer host study R-2).
3. In this pass the kick decision found every monitor on time and kicked, and the pass took a PA temperature sample (section 4.6.3).
4. At least 1 s of normal dispatch has passed since the last window ended (proposed as an 07 allocation), so two windows never run back to back.

Log events raised while a write may not start (in Transmit-keyed, for example) wait in the log's RAM ring and are written at the next allowed point. The ring's size and its overflow rule (counted, never blocking) are FW-B2 log design. A reset before that point loses the queued events except the reset cause, which the watchdog `REASON` and scratch registers carry into the next boot's log (07 section 16.5). The `plan` decision function of section 4.2 (R-2) takes the mode and these conditions as inputs and rejects a request that fails any of them. The rule is therefore enforced in one host-tested place for both users (request R-10).

#### 4.6.2 The window as a declared scheduler state

The store step is one task of the `SW-SCHED` task table (the flash `const` of row f). It serves both users and runs at most one window per pass. The dispatcher declares the window; it does not discover a stall afterwards:

| Step | What happens | Who |
|---|---|---|
| 1 | The pass dispatches every due task; the kick decision finds every monitor on time and kicks | `SW-SCHED` main loop, the only holder of the `Watchdog` handle |
| 2 | In the same pass, after the kick, the dispatcher enters `StoreWindow { start, bound }` (start read from TIMER0; bound from the task table: 10 ms for a program window, 450 ms for an erase window) and calls the store step | `SW-SCHED` |
| 3 | The store step runs the RAM-resident window of ICD `02_programming.md`: PRIMASK set, bootrom sequence, PRIMASK cleared. It never touches the watchdog | WP-SW-08 driver |
| 4 | The dispatcher leaves `StoreWindow` and reads TIMER0, which counts through PRIMASK (the missed ALARM1 match is reported `Due`, ADR-053). Elapsed time over the bound is a tick overrun: `safe_state()`, the event logged, response class safe state (07 rows c, k, l). Within the bound the missed ticks go to a store-stall count, and the longest window since boot is kept; they are not MSR-26 overruns | `SW-SCHED` |
| 5 | A catch-up pass runs every monitor task once on fresh samples (key inputs, PA temperature, cells, VBUS, the RAM-copy CRC of row f), then the kick decision. The deadline check counts a monitor as on time when its period was covered by a declared window within its bound followed by this pass | `SW-SCHED` |
| 6 | The read-back and CRC check after a program window, and the blank check after an erase window, run later as ordinary store steps, outside any window | store task |

Against revision 0, the driver no longer feeds the watchdog before the window (SA finding-1). The only kick is the main loop's, given only after every monitor ran (keyer host study R-1). A hang anywhere, inside a window included, resets the chip 1.0 s after the last main-loop kick and reaches Self-test by 1.1 s (A-8), as in the keyer study. With a driver-side feed, a runaway task that kept calling the store could add a second load after the last main-loop kick: up to 2.1 s to Self-test (about 2.09 s in the SA finding), over the 2 s of REQ-SYS-131. The `FlashStore` implementation holds no `Watchdog` handle, so the rule is enforced by construction (request R-1).

Longest time without a kick: the store preparation after the kick, the window, and the catch-up pass. That is 1 ms + 401 ms + 1 ms = 403 ms with A-7 and A-F8, and 452 ms at the erase bound. The watchdog load is 2.48 times the first and 2.21 times the second, both above the factor 2 of the keyer study; any erase bound up to 498 ms keeps the factor. Step 4 ends a window that runs past its bound as an overrun fault well before the watchdog load, so a slow part shows as a logged fault, not a reset.

MSR-26 keeps its target of zero overruns. It counts overruns outside declared windows and every window over its bound. The declared windows are reported separately (count and longest) through the event log (request R-1, to WP-PDR-32 and to the writer of 07 for the `SW-SCHED` row and MSR-26).

#### 4.6.3 Row j budgets during a window

Every item of 07 section 14.2 row j, in Receive:

| Row j item | Active during a window in Receive | Reason, and what the design does |
|---|---|---|
| Manual-closure timeout 5 s (REQ-SYS-053) | No | Runs only in Transmit-keyed. A window starts only with the key inputs open (4.6.1 item 2) and transmit disarmed for the window, so no key-down is forwarded |
| Tune carrier end within 5.5 s (REQ-SYS-020) | No | Tune only |
| Paddle no-gap watchdog and squeeze limit (REQ-SYS-054) | No | Keyed sending only |
| Test-mode timeout 120 s | No | Bench-test only |
| Key-up response (open debounce, envelope fall, then PA_EN low) | No | `TX_KEY` is low and no key-down is forwarded |
| Carrier end on an inhibit, flag or latched fault within 20 ms (REQ-SYS-004) | No | No carrier: PA_EN is low |
| PA over-temperature to PA_EN low within 100 ms (REQ-SYS-118) | No | PA_EN is already low |
| PA over-current or reflected-power fault to PA_EN low within 10 ms (HZ-003 K5, if sensed) | No | PA_EN is low; the PA is not driven |
| PA temperature reading out of range to Fault-safe within 100 ms (REQ-SYS-155) | Yes | Met in a program window; exceeded in an erase window (section 4.6.4) |
| VBUS detection to transmit disarm within one sample (HZ-011 K6) | Yes | Transmit disarmed before the window; re-armed only through the Arm condition |
| Charge disable within one supervision period of a fault | Yes, if USB is present | Charge enable de-asserted before the window; restored after the charge prerequisites re-check |
| Audio limiter attack at most 1 ms | Yes | Receive audio muted before the window; unmuted after the catch-up pass |
| Receive mute within 2 ms of key-down (REQ-SYS-075) | Yes, if a key closes during the window | Audio is already muted, and the closure starts no transmission before the catch-up pass |
| Battery under-voltage to power-down within 1 s (07 allocation) | Yes | No output to set. The longest gap between battery samples is the supervision period plus 452 ms, so the budget holds for a supervision period up to 547 ms (proposed to WP-PDR-35 with the period, R-4) |
| CPU watchdog 2 s (REQ-SYS-131) | Yes | Section 4.6.2 |

In Fault-safe the same table holds, with REQ-SYS-155 already met (the unit is in Fault-safe) and the outputs already set by `safe_state()`.

A program window (4 ms, bound 10 ms) meets every row j budget as it stands. Because it starts in the pass that took a PA temperature sample, the longest gap between PA samples stays the 50 ms of the 20 Hz path: 51 ms to Fault-safe entry (checker), within 100 ms. Only erase windows exceed REQ-SYS-155.

#### 4.6.4 REQ-SYS-155 during an erase window

REQ-SYS-155 reads "enter Fault-safe within 100 ms (TBR) of its PA temperature reading leaving -20 C to +150 C (TBR)" and has no mode qualifier. In an erase window the first PA sample after the window is the one the catch-up pass takes. An out-of-range reading that appears just after masking therefore reaches Fault-safe 404 ms later (design) or 453 ms later (at the erase bound). The window cannot meet 100 ms, and the response (entry to Fault-safe with its annunciation) is a mode change that cannot be made ahead of the window.

Argument. REQ-SYS-155 protects against HZ-003: a failed thermistor that reads cold would silently defeat the REQ-SYS-118 inhibit. During the window PA_EN is low and transmit is disarmed, so the PA carries no RF drive and the hazard has no energy source. After the window, the thermal prerequisite of row h blocks PA_EN until a valid in-range reading has been taken. Only the Fault-safe entry and its annunciation are late, and the fault screen still appears inside the 1 s of REQ-SYS-067. The hardware PA over-temperature cut-off (REQ-SYS-181, package decision 39) does not depend on the firmware.

Route (request R-11, to the REQ-SYS-155 TBR closure: the PA thermal analysis WP-PDR-28, TBR group G5, and the WP-PDR-45 TBR sheet for the owner's ruling). Either (a) a mode-qualified statement, "within 100 ms (TBR) while PA_EN is high, and within 500 ms (TBR) while PA_EN is held low", which this design meets with 453 ms at the bound, or (b) 100 ms in every state and no erase window at run time, which forces option C of section 4.6.5 with the costs stated there. The note proposes (a). The stall also goes to WP-PDR-16 as the candidate cause "configuration or log write stalls the monitors" (request R-4). This does not close the keyer study SA finding-4, which belongs to that record.

#### 4.6.5 Alternatives weighed

| Option | Longest window at run time | REQ-SYS-155 | Hang to Self-test (REQ-SYS-131) | Cost | Verdict |
|---|---|---|---|---|---|
| A. Revision 0: erase and program the inactive copy on every commit | 401 ms on every commit and every log write | exceeded on every write | 1.1 s | about 55 commits a day of endurance | Replaced |
| B. Page-append records; erase only to reclaim a sector (the design) | 4 ms on 15 of 16 writes; 401 ms on the 16th | met in program windows; erase windows routed (R-11), about 7.5 a day | 1.1 s | the load scans 32 pages (2.2 ms at boot) | Adopted |
| C. B, with every erase done in the boot path before dispatch starts, and none at run time | 4 ms | met in every state | boot path longer by 401 ms per sector: 1.0 s + 30 ms + 557 ms (2 MiB image) + 401 ms = 1.99 s for one sector, over 2 s for two; A-8 no longer holds | after about 16 commits, or 16 log pages, in one power cycle there is no blank page: the write waits in RAM for the next boot and is lost on cell removal (REQ-SYS-135) | Not adopted; it is the fallback if the owner rules (b) at R-11 |
| D. Vector table, monitors and their drivers in SRAM; the erase issued in QMI direct mode with interrupts enabled, polling the device status | microseconds per poll | met | 1.1 s | every monitor path resident in SRAM and audited for flash access; the bootrom range functions not used | Not adopted for Rev A: the effort and the audit surface are much larger than the problem |

Option B takes the 401 ms stall out of 15 of every 16 writes and meets REQ-SYS-155 in those. Option C takes it out entirely, but it uses up the REQ-SYS-131 boot margin (12 ms at the red line for one sector) and trades the stall for lost settings in a long session. Which of (a) and (b) holds is the owner's ruling at R-11.

### 4.7 Power loss and wear

Records are appended. Each 4 KiB sector holds 16 record pages. A write programs the next blank page. When the last page of the active sector has been written, the other sector, which then holds only older records, is erased as a later and separate step (a reclaim). The page holding the newest record is never erased or programmed. This is how the store meets row e ("write the inactive copy, read it back and CRC-check it, then advance the sequence number"): the inactive copy is the next blank page. At load (REQ-SYS-134) `cfg_guard` scans the 32 pages and takes the valid record (CRC holds, fields in range) with the highest sequence number; the scan takes 2.2 ms at 96 MHz. From the second commit on, at least the newest and the previous record are present at every instant (row f, two CRC-32 copies with a sequence number).

Power loss at any point of a write leaves the newest valid record in place:

| Store state (07 row b: idle, erasing, programming, verifying) | Newest valid record | What is being written | Load result (REQ-SYS-134) |
|---|---|---|---|
| Idle | sequence n | nothing | n |
| Programming the next blank page | n, untouched | a partly programmed page | n (a partial page fails its CRC except with probability below 2^-32, section 6.4) |
| Verifying | n, untouched | the new record, n+1 | n+1 if its CRC holds, else n |
| Erasing the other sector (reclaim) | n, in the full active sector, untouched | a partly erased sector that held only older records | n (what is left there is older or fails its CRC) |

The event log uses the same page-append scheme as a ring over its own 8-sector reserve (section 4.4); a power loss loses at most the page being written.

Sequence numbers are `u32`. Even at the endurance rate below (877 commits a day for 10 years) a unit makes about 3.2 million commits, far below 2^32, so the comparison never meets a wrap.

Wear, at 100 000 cycles (A-F4) over 10 years (A-F5). Each sector is erased once per turn of its ring:

| User | Sectors (record pages) | Writes per day | Erases per sector in 10 years | Margin |
|---|---|---|---|---|
| Configuration | 2 (32) | 20 commits (expected; rule R-5) | 2281 | factor 44; the endurance allows 877 commits a day |
| Event log | 8 (128) | 100 pages (A-F9) | 2852 | factor 35 |

Erase windows, both users together: 7.5 a day (1.25 configuration, 6.25 log). The commit rule of request R-5 is unchanged: commit only when a persisted setting changed and the operator leaves the menu, at most once per 60 s.

### 4.8 Emulation

The accredited emulator cannot test flash erase or program (research `emulator-accreditation-and-timer-irq.md`: QMI direct mode FAIL; "flash erase/program" is explicitly not credited). Evidence for WP-SW-08 is HostUnit (the `plan` decision function and the store state machine against `cwht-hal-mock`) and the dev-board check.

### 4.9 ICD page (rustos pull request)

The extraction is on rustos branch `cwht/wp-sw-08`, stacked on `cwht/wp-sw-03` at `48e07ec` like the earlier FW-B1 branches, not pushed, for the owner's merge as rustos maintainer (OD-23): `docs/icd/rp2350/flash/index.md`, `01_bootrom_api.md`, `02_programming.md` (the sequence, the constraint table of section 4.3, the declared window of section 4.6.2, the UF2 and E10 rule and layout of section 4.4, the time budget of section 4.5) and `03_xip_qmi.md` (XIP windows, cache, boot read modes and the per-byte miss cost, direct-mode registers), and one row in `docs/icd/rp2350/index.md`, Revision 0 was one commit, `03b1997` (`03b1997d45b9cfa267133a389cebe87a346a6e50`), parent `48e07ec`. Fix round 1 adds one commit on top (no amend): branch head `00d5383` (`00d53834dfe315aafd09a11ec1d76e6ffbc45835`), parent `03b1997`. It changes `02_programming.md` (the watchdog constraint, the fault paragraph, the window design table now with the declared scheduler state and the catch-up pass, the page-append records, the write conditions, the event-log reserve and the time budget) and the "cwht Driver Notes" of `index.md` (the event log, the write conditions and the watchdog rule).

## 5. WP-SW-10 UART0 telemetry and trace

### 5.1 Requirement

REQ-SYS-150: "The transceiver shall emit its serial telemetry on 3.3 V UART test pads while USB VBUS is absent." The pads are in the REQ-SYS-142 test-point list. The telemetry is how several Bench cases read the unit: TC-SYS-002 records "Time, mode, transition id, cause and PA_EN state" from the telemetry mode sequence; the battery cases log cell voltages and events; TC-SYS-095 closes REQ-SYS-150 by decoding "3.3 V telemetry in receive and during keying with both key types" through the logic capture. The same channel is the Emulation trace (ACC-EMU-001 credits "UART0 text" for expect-text assertions, KA-2). ICD-SW-HOST, which WP-PDR-36a writes, holds the "UART0 trace format"; section 5.4 is the proposal for it.

### 5.2 ICD page: the committed rustos UART extraction

rustos `docs/icd/rp2350/uart/` at `2ec64c0` (confirmed by `git show 2ec64c0:docs/icd/rp2350/uart/<file>`): `index.md` (blob `0dfc6cd4`), `01_overview.md` (`a40e5647`), `02_operation.md` (`60e02033`), `03_interrupts.md` (`36b995b3`), `04_registers.md` (`0c6d6f9c`). It covers the PL011 block, 32 x 8 TX FIFO, framing, the fractional divisor with its worked example, the SDK init order, the interrupt sources and the register map. It cites datasheet sections, not pages; the pages are D24 to D28 above. Its "FT1 Driver Notes" describe the Juno GPS link (9600 baud) and do not apply to cwht; the cwht use is stated here and goes into WP-SW-10's own driver notes in FW-B2. No new rustos extraction is needed for WP-SW-10 at DML-3.

### 5.3 Proof against REQ-SYS-150

| Property | Analysis | Result |
|---|---|---|
| Independent of USB and VBUS | UARTCLK is `clk_peri` (D26), which ADR-051 sources from `clk_sys` on `PLL_SYS`; nothing in the UART path uses `PLL_USB`, the USB controller or VBUS. spurs-ts012 C3 powers `PLL_USB` down whenever USB is not enumerated; the UART is unaffected | Telemetry runs with VBUS absent and `PLL_USB` off |
| 3.3 V levels at the pads | The pads are GPIO; the Pico 2 IO voltage is fixed at 3.3 V (Pico 2 datasheet p. 4). At IOVDD 3.3 V: VOH at least 2.62 V, VOL at most 0.5 V (D29) | Against a 3.3 V LVTTL receiver (VIH 2.0 V, VIL 0.8 V; the adapter's own figures go in `docs/vv/fixtures/uart-adapter.md`): 0.62 V high and 0.3 V low margin |
| Divisor at 115 200 baud | `UARTCLK / (16 x baud)`, fraction rounded to 1/64 (D27). 96 MHz: IBRD 52, FBRD 5, error +0.0100 %. 150 MHz: IBRD 81, FBRD 24, error +0.0064 %. Both inside 16 x baud to 16 x 65535 x baud | Either `clk_sys` choice (C1 or ADR-051) works |
| Bench decode | The Pico-based logic capture samples at 1 MS/s: 8.68 samples per bit. With the start edge found to one sample and the stop bit sampled 9.5 bits later, the decode tolerates a rate mismatch of 4.05 % | More than 10 times the divisor error; 230 400 baud (4.3 samples per bit) is not proposed |
| Line capacity and load | 8N1 at 115 200 baud carries 11 520 B/s. Peak load: one STAT line per second (120 B), TX_KEY edge events at 50 WPM continuous dits (41.7 per s x 40 B = 1667 B/s), and 10 mode or other events per second (800 B/s): 2587 B/s | 22 % of the line (at most 50 % proposed) |
| No blocking of safety tasks | The driver never waits on the FIFO. Each 1 ms tick copies at most the free FIFO space (32 bytes, D26) from a 1 KiB RAM ring. The line drains 11.52 B per ms, so one refill per tick keeps it busy, and a full FIFO covers 2.78 ms, two ticks. A full ring drops the whole new line and counts it (`drop=` in STAT, gaps in `seq`) | No UART interrupt is needed (CS-34 keeps one priority anyway); cost is a few register writes per tick |
| Store window | During an erase window at its 450 ms bound (section 4.6: no keying, R-2) only STAT lines queue: 66 B | Fits the 1 KiB ring; nothing is lost |

### 5.4 Trace and telemetry format (proposal for ICD-SW-HOST, request R-6)

One ASCII line per record, 8N1 at 115 200 baud:

```
line   = "$" type "," seq "," t_us *( "," key "=" value ) "*" crc32 CR LF
type   = "BOOT" / "MODE" / "STAT" / "EVT" / "FLT"
seq    = decimal 0..65535, +1 per line, wraps; a gap shows a dropped line
t_us   = TIMER0 microseconds since boot, decimal (u64): an order key only (07 section 9.4 item 2)
key    = lower-case letters and digits
value  = decimal integer (optionally signed), hex digits, a dotted version, or an upper-case token;
         never "," "*" "=" or space
crc32  = 8 upper-case hex digits: WP-SW-12 CRC-32 of every byte after "$" and before "*"
```

Record set (the field list is the ICD-SW-HOST author's to finalise with the test authors):

| Type | Fields | Used by |
|---|---|---|
| BOOT | `fw` version, `img` image CRC-32, `st` self-test result | REQ-SYS-143 banner content (also sent on USB serial), TC-SYS-095 |
| MODE | `from`, `to` (OFF, CHARGING, SELFTEST, RECEIVE, TXKEYED, TUNE, BENCHTEST, FWUPDATE, FAULTSAFE), `tr` transition id T01 to T25, `cause`, `pa` PA_EN level | TC-SYS-002, TC-SYS-003 (`tools/analyze_mode_trace.py`) |
| STAT (1 Hz) | `mode`, `flags` hex bitmask (bit 0 GUEST, 1 PRACTICE, 2 USB, 3 LOWBATT), `c1` and `c2` cell voltages in mV, `tpa` PA temperature in 0.1 C, `drop` lines dropped since boot | battery and charge cases, cell-sense cases |
| EVT | `ev` event token, `v` value | emulation expect-text, key and TX_KEY order |
| FLT | `code` fault code, `cause` | Fault-safe cases |

Golden lines (the CRC is computed by the checker and becomes a test vector of the formatter HostUnit case):

```
$BOOT,0,81234,fw=0.1.0,img=1A2B3C4D,st=PASS*C5EFA6E4
$MODE,1,1500000,from=SELFTEST,to=RECEIVE,tr=T08,cause=PASS,pa=0*7EFF33FF
$STAT,2,2000000,mode=RECEIVE,flags=00,c1=3912,c2=3905,tpa=251,drop=0*9D525546
$EVT,3,2100417,ev=TXKEY,v=1*B473D807
$STAT,65535,18446744073709551615,mode=FAULTSAFE,flags=0F,c1=4200,c2=4200,tpa=-200,drop=65535*12F4B686
```

The last line is the longest STAT (largest `seq`, `t_us`, mode token and field values): 103 bytes with CR LF, under the 120-byte maximum the load budget uses. A first draft with the flags as names ran to 134 bytes and failed the checker; the bitmask form is the fix.

**Receive side and security.** ICD-SW-HOST also defines the UART receive command set. CS-33 allows no state-changing command on the diagnostic serial interface other than `reboot`, while TC-SYS-002 step 8 injects a latched cause by command and the UART adapter fixture of TC-SYS-002 and other Bench cases exists "so that injection commands reach the unit with its USB port disconnected". The ICD-SW-HOST author has to reconcile the two (for example, injection commands only in a fault-injection build that a release cannot contain). This is recorded as open item L-3; it does not change the transmit analysis.

## 6. WP-SW-12 CRC-32 (`cwht-core`)

### 6.1 Requirements

REQ-SYS-132: Fault-safe with no RF output when the image fails the boot integrity check. 07 section 14.2 row f: "the configuration RAM copy is CRC-32 checked every 100 ms ...; the image CRC-32 trailer is checked at boot; the stored configuration is two CRC-32 copies with a sequence number". CS-32 names the same checks. REQ-SYS-134 relies on the CRC to find a corrupt copy.

### 6.2 Algorithm page

| Parameter | Value |
|---|---|
| Name | CRC-32/ISO-HDLC (the IEEE 802.3 / zlib CRC-32) |
| Width | 32 |
| Polynomial | 0x04C11DB7 (normal form); 0xEDB88320 in the reflected form the code uses |
| Initial value | 0xFFFFFFFF |
| Input reflected | yes (bytes processed least-significant bit first) |
| Output reflected | yes |
| Final XOR | 0xFFFFFFFF |
| Check value, ASCII "123456789" | 0xCBF43926 |
| Residue (CRC over data followed by its CRC, little-endian) | 0x2144DF1C |
| Stored form | 4 bytes, little-endian, immediately after the covered bytes |

Why this variant: the host side (the release script `tools/image_trailer.py`, not yet written, `tools/toolchain.lock.md`) can use Python's `zlib.crc32`, which is this variant, so the trailer writer and the firmware checker share one definition with no custom host code; and the RP2350 DMA sniffer computes the same polynomial (D30), which the dev-board check may use as an independent cross-check even though WP-SW-12 does not depend on it (07 section 19).

Reference form for `cwht-core` (pure function, no `unsafe`, no allocation; `const` table of 256 `u32` built at compile time):

```
table[n] = n; repeat 8 times: table[n] = (table[n] >> 1) ^ (0xEDB88320 if table[n] & 1 else 0)
crc = 0xFFFFFFFF
for each byte b: crc = (crc >> 8) ^ table[(crc ^ b) & 0xFF]
return crc ^ 0xFFFFFFFF
```

A streaming form carries `crc` between calls without the final XOR and applies it once at the end; the checker shows that 16 chunks of 256 bytes give the one-shot value. The table is 1 KiB. A-F7 assumes it in SRAM (a `static` placed in `.data`); left in flash it is served from the XIP cache after first use. The CRC is never called inside the WP-SW-08 window (section 4.3): the read-back check runs after XIP is restored.

### 6.3 Golden vectors (reference model)

Four independent implementations agree on every vector: bit-serial reflected, bit-serial MSB-first on bit-reversed input with the normal polynomial, table-driven, and Python `zlib.crc32`. V2 equals the published check value of CRC-32/ISO-HDLC; the corpus holds no CRC catalogue, so the reference model rests on the agreement of the four implementations, one of which (`zlib`) is independent of this note.

| Id | Input | Length | CRC-32 |
|---|---|---|---|
| V1 | empty | 0 | 0x00000000 |
| V2 | ASCII "123456789" | 9 | 0xCBF43926 |
| V3 | 0x00 | 1 | 0xD202EF8D |
| V4 | 0xFF | 1 | 0xFF000000 |
| V5 | 32 x 0x00 | 32 | 0x190A55AD |
| V6 | 32 x 0xFF | 32 | 0xFF6CAB0B |
| V7 | 0x00, 0x01, ..., 0xFF | 256 | 0x29058C73 |
| V8 | ASCII "The quick brown fox jumps over the lazy dog" | 43 | 0x414FA339 |
| V9 | 252 x 0xFF (the covered part of an erased record) | 252 | 0xA7340E2F |
| V10 | 252 x 0x00 | 252 | 0xA66359F1 |
| V11 | 4096 x 0xFF (an erased sector) | 4096 | 0xF154670A |

These are the vectors of the `cwht-core` HostUnit case for WP-SW-12 in FW-B2 (the TC-SW id is the test author's).

### 6.4 Error-detection proof

- **Single-bit, double-bit and burst errors.** The polynomial has 15 terms and x has order 2^32 - 1 modulo it (the checker computes x^(2^32-1) mod P = 1 and x^((2^32-1)/q) mod P != 1 for each prime factor q of 2^32 - 1: 3, 5, 17, 257, 65537), so it is primitive. A primitive degree-32 polynomial detects every single-bit error, every two-bit error in a codeword shorter than 2^32 - 1 bits (any image or record cwht can have), and every burst of 32 bits or fewer (an error polynomial x^i E(x) with degree of E below 32 and E(0) = 1 is not a multiple of P).
- **Odd-weight errors.** With 15 terms the polynomial is not a multiple of x + 1, so odd-weight errors are not detected by construction; they are covered by the exhaustive test below for the record length.
- **Configuration record, 256 bytes (252 covered, 4 CRC).** The checker tests every error pattern of 1 to 4 bits over the 2048-bit codeword (2 096 128 pairs of positions, all triples and quadruples through the pair syndromes): none is undetected. The Hamming distance is at least 5.
- **512-byte record, for comparison.** Weight 3 is still always detected, but some 4-bit patterns are not: Hamming distance 4. That is the reason the record is kept to one 256-byte page (section 4.5).
- **Other corruption.** Of all 2^n - 1 non-zero error patterns on an n-bit codeword, 2^(n-32) - 1 are codewords, so a random corruption beyond these weights escapes with probability below 2^-32.
- **Erased and zeroed copies.** An all-0xFF record (erased sector, V9) and an all-zero record (V10) both fail the check, so a blank or cleared copy is never taken as valid.

### 6.5 Time cost

| Check | Size | Time at 96 MHz | Time at 150 MHz | Budget |
|---|---|---|---|---|
| RAM copy every 100 ms (row f) | 256 B | 32 us (0.03 % of the CPU) | 20.5 us | under 0.1 % |
| Record read-back after a commit | 256 B | under 0.4 ms (section 4.5) | less | inside A-7's 1 ms |
| Image check at boot, EBh at divisor 3 (A-F1), 64 KiB | 64 KiB | 17 ms | 11 ms | A-8: 100 ms including A-F6 (30 ms) |
| Same, 256 KiB | 256 KiB | 70 ms | 45 ms | A-8 holds up to about 257 KiB at 96 MHz |
| Same, 1 MiB (TPM-010 yellow line) | 1 MiB | 279 ms | 178 ms | REQ-SYS-131 only |
| Same, 2 MiB (TPM-010 red line) | 2 MiB | 557 ms | 357 ms | REQ-SYS-131: 1.0 s + 30 ms + 557 ms = 1.59 s, under 2 s |
| Same, 2 MiB, in the 03h / CLKDIV 12 mode | 2 MiB | 3.41 s | 2.18 s | fails REQ-SYS-131 |

Per-byte cost: the XIP miss cost of ICD `03_xip_qmi.md` (13.5 `clk_sys` cycles per byte in EBh at divisor 3; 144 in 03h at 12) plus 12 cycles per byte for the CRC (A-F7). Results: REQ-SYS-131 holds for any image up to the TPM-010 red line, provided the check runs after the WP-SW-11 clock bring-up and in the boot XIP mode, never after a `flash_exit_xip` without the XIP setup (request R-7). The A-8 figure of 100 ms holds only while the image stays under about 256 KiB at 96 MHz; the release image size is watched against that value (MSR-18 already records it), and A-8 is revisited above it.

## 7. Results against the requirements

| Package | Critical function | Requirement | Number | Target | Margin | DML-3 content |
|---|---|---|---|---|---|---|
| WP-SW-08 | No flash fetch while XIP is off | RSK-021; REQ-SYS-134, 135 | every fetch source closed (section 4.3) | none open | - | ICD page (rustos branch), sequence, constraint table |
| WP-SW-08 | Bounded masked window and longest time without a kick | REQ-SYS-131 via the watchdog load; 07 `SW-SCHED` row | windows 4 ms and 401 ms; 403 ms without a kick (452 ms at the erase bound) | at most half the 1.0 s load (500 ms) | ratio 2.48 (2.21 at the bound); 49 ms of erase time before the bound | Time budget (section 4.5), declared window (4.6.2) |
| WP-SW-08 | No false overrun fault or watchdog reset; hang recovery unchanged | 07 `SW-SCHED` rows j, k, l; MSR-26; REQ-SYS-131 | declared window within its bound is no overrun; kick only from the main loop; hang to Self-test 1.1 s | 2 s | 0.9 s | Section 4.6.2 |
| WP-SW-08 | Row j budgets during a window | 07 section 14.2 row j; REQ-SYS-155 | every item accounted for; REQ-SYS-155: 51 ms in a program window, 404 ms (453 ms at the bound) in an erase window | 100 ms (TBR); 500 ms proposed while PA_EN is held low (R-11) | met in program windows; erase windows routed | Sections 4.6.3, 4.6.4 |
| WP-SW-08 | Newest valid record kept at every instant, and after a firmware load | REQ-SYS-134, 135; ICD-CTL-USB | every write state keeps the newest valid record; E10 sector avoided | no roll-back | - | Store layout (section 4.4), state table (4.7) |
| WP-SW-08 | Wear, configuration and event log | REQ-SYS-135 over life; 07 section 16.5 | 2281 and 2852 erases per sector in 10 years | 100 000 (A-F4) | factor 44 and 35 | Section 4.7 |
| WP-SW-10 | Telemetry with USB absent at 3.3 V | REQ-SYS-150 | UART clock off `PLL_SYS`; VOH 2.62 V, VOL 0.5 V | LVTTL 2.0 V / 0.8 V | 0.62 V / 0.3 V | Committed ICD cited; format and load (sections 5.3, 5.4) |
| WP-SW-10 | Decodable by the bench capture | TC-SYS-095 | divisor error 0.010 %; tolerance 4.05 % | - | factor 405 | Section 5.3 |
| WP-SW-10 | No delay to safety tasks | 07 section 14.2 row j | 22 % line load; no blocking write | at most 50 % | - | Section 5.3 |
| WP-SW-12 | Detects image and record corruption | REQ-SYS-132; 07 section 14.2 row f | HD at least 5 on the 256-byte record; primitive polynomial | - | - | Algorithm page and golden vectors (section 6) |
| WP-SW-12 | Fits the boot and 100 ms budgets | REQ-SYS-131; row f | 1.59 s at the 2 MiB red line; 0.03 % CPU | 2 s; - | 0.41 s | Section 6.5 |

Each package meets the DML-3 definition: WP-SW-08 has its ICD extracted and its time budget proven against the requirements, with the REQ-SYS-155 erase-window case routed to its TBR closure (R-11); WP-SW-10 has its committed ICD cited and its format and budget proven against REQ-SYS-150; WP-SW-12 has its reference model and golden vectors.

## 8. Requests to other work packages

1. **R-1 (WP-PDR-32, firmware architecture, `SW-SCHED`; and the writer of 07 for the section 14.2 `SW-SCHED` row and MSR-26, plan section 5.3):** the WP-SW-08 window design of ICD `02_programming.md` (RAM-resident window function, PRIMASK, one window per store step, 256-byte page-append records); the store window as a declared `SW-SCHED` state with bounds of 10 ms (program) and 450 ms (erase) in the task table, a window over its bound treated as a tick overrun with response class safe state, the catch-up pass of every monitor before the next kick decision, and the deadline rule of section 4.6.2 step 5; the watchdog kicked only by the main loop after every monitor ran, with no `Watchdog` handle in `FlashStore`; the longest time without a kick bounded at 452 ms against the 1.0 s load; MSR-26 counting overruns outside declared windows and windows over their bound, with the declared windows reported separately.
2. **R-2 (WP-PDR-32):** the `FlashStore` request checker as a host-tested decision function that accepts only whole sectors and pages of the configuration and event-log sectors and only under the conditions of section 4.6.1 (section 4.2).
3. **R-3 (WP-PDR-32 and ICD-SW-HOST, WP-PDR-36a):** the store layout of section 4.4 (event-log reserve 0x3F5000 to 0x3FCFFF, A at 0x3FD000, B at 0x3FE000, 0x3FF000 unused, application `FLASH` ending at 0x3F5000), replacing research F15's top-two-sector layout; the FW-B2 log sizing stays inside the reserve or revises this request.
4. **R-4 (WP-PDR-35 and WP-PDR-16):** the pre-window output states and the row j table of section 4.6.3 as a `SW-SAFE` / `SW-CFG` / `SW-SCHED` constraint, including the battery supervision period of at most 547 ms, and the stall as a candidate software cause for the hazard data ("configuration or log write stalls the monitors").
5. **R-5 (WP-PDR-35, `SW-CFG`):** the commit rule of section 4.7 (on menu exit after a change, at most once per 60 s).
6. **R-6 (WP-PDR-36a, ICD-SW-HOST):** the line format, record set, 120-byte maximum and golden lines of section 5.4, and 115 200 baud 8N1 on UART0.
7. **R-7 (WP-PDR-32, `SW-BOOT`):** the image check after the clock bring-up and in the boot XIP mode; the image-size watch against about 256 KiB for A-8 (section 6.5).
8. **R-8 (release script, `tools/image_trailer.py`):** CRC-32/ISO-HDLC as in section 6.2 (`zlib.crc32`), stored little-endian, with golden vectors V1 to V11 as its known answers.
9. **R-9 (owner, as for OD-39):** permission to download the Winbond W25Q32RV datasheet into the reference corpus, to replace A-7, A-F3 and A-F4 with the part's figures.
10. **R-10 (WP-PDR-35, `SW-CFG` and `SW-DIAG`; WP-PDR-32):** the write rule of section 4.6.1 as a requirement on every `FlashStore` write, configuration and event log alike: only in Receive or Fault-safe, PA_EN and `TX_KEY` low, key inputs open, right after a kick in a pass that took a PA temperature sample, and at least 1 s after the last window; log events raised elsewhere wait in a RAM ring (size and overflow rule in FW-B2) and are written at the next allowed point.
11. **R-11 (REQ-SYS-155 TBR closure: WP-PDR-28, TBR group G5, and the WP-PDR-45 TBR sheet for the owner's ruling):** the erase-window case of section 4.6.4. Proposed: (a) "within 100 ms (TBR) while PA_EN is high, and within 500 ms (TBR) while PA_EN is held low"; the alternative (b) keeps 100 ms in every state and moves every erase to the boot path (option C of section 4.6.5, with its REQ-SYS-131 and REQ-SYS-135 costs).

## 9. Limits, open items and the DML-5 plan

- **L-1.** Part timing, address decoding and endurance are assumptions (A-7, A-F3, A-F4) until R-9. The layout of section 4.4 does not depend on A-F3; the budget depends on A-7 with 49 ms of erase time before the declared erase bound, and on A-F8 for the pass time.
- **L-5.** REQ-SYS-155 is exceeded in erase windows (section 4.6.4) until R-11 is ruled; the design proposal holds only under ruling (a).
- **L-2.** The XIP miss cost excludes chip-select and turnaround cycles (ICD `03_xip_qmi.md`); the image-check times are estimates to about 25 %, measured at DML-5.
- **L-3.** The UART receive command set against CS-33 (section 5.4) is for ICD-SW-HOST.
- **L-4.** Observation for the rustos ICD reviewer, outside this product: the WP-SW-01 and WP-SW-03 pages cite "§7.5 Table 534 (p504)", which is the PDF page index (printed page 503), and "§3.2 Table 94 (p82)", which is the printed page; the timer page cites §12.8.5 at "p1184", where the list of registers starts on printed page 1185. The new flash pages use printed pages throughout.

DML-5 (FW-B2, before CDR) for these packages: (1) WP-SW-08 dev-board check: 1000 page writes (about 62 sector reclaims) over the configuration and log sectors with the logic capture on a GPIO marker around each window, recording the longest program and erase windows against their 10 ms and 450 ms bounds; (2) the disassembly check of section 4.3; (3) a firmware load with the E10 block over a stored configuration and log, then a read of every configuration and log sector; (4) the fault-injection build of section 4.3 (XIP read in the window ends in a watchdog reset); (5) WP-SW-10 dev-board check: 60 s of telemetry decoded by the logic capture at 1 MS/s with USB unplugged, zero CRC failures; (6) WP-SW-12 HostUnit with V1 to V11 and the residue, and the CRC cycle count of A-F7 on the dev board, with an optional DMA-sniffer cross-check; (7) `SW-SCHED` with the store: HostUnit of the declared-window logic on the mock clock (a window within its bound gives no overrun and the kick after the catch-up pass; a window over its bound gives `safe_state()` and no kick; a missed monitor outside a window withholds the kick), and a dev-board run of (1) with every monitor task running and the watchdog at 1.0 s, with a GPIO marker on each kick: zero overrun faults, zero watchdog resets, and the longest time between kicks at most 452 ms; a fault-injection build that stretches one window past 450 ms ends in the overrun safe state, not in a watchdog reset.

## 10. Change log

| Revision | Date | Change | Driver |
|---|---|---|---|
| 0 | 2026-09-29 | First issue: DML-3 proofs for WP-SW-08, 10 and 12; rustos flash ICD on branch `cwht/wp-sw-08` | WP-PDR-41 (plan revision 7), technology assessment section 3.18 |
| 1 | 2026-09-29 | Fix round 1, Major findings only (plan rule C1). Review finding-1 and SA finding-2: the store window becomes a declared `SW-SCHED` state with bounds, a catch-up pass and the kick rule; the longest time without a kick is bounded (sections 4.5, 4.6.2); DML-5 check 7. SA finding-1: the driver no longer feeds the watchdog (4.6.2). Review finding-2: every row j item listed, REQ-SYS-155 argued and routed (4.6.3, 4.6.4; R-11). SA finding-2: alternatives weighed, page-append records adopted (4.6.5, 4.7). SA finding-3: the write rule covers the event log (4.6.1, R-10), the log gets its flash reserve (4.4, R-3) and its wear (4.7). A-F8, A-F9 added; checker 83 assertions. rustos ICD fix commit on `cwht/wp-sw-08`. Minor findings 3 to 13 held under rule C1 | `analysis-fw-b1-dml3-wp-sw-08-10-12.md` iteration 1 finding-1 and finding-2; its SA pair, finding-1 to finding-3 |
