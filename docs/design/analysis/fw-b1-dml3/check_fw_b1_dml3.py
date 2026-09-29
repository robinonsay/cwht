"""Checker for the WP-PDR-41 FW-B1 DML-3 note (docs/design/analysis/fw-b1-dml3-wp-sw-08-10-12.md).

Run from the repository root:
    .venv/bin/python docs/design/analysis/fw-b1-dml3/check_fw_b1_dml3.py

It recomputes every number the note states for WP-SW-08 (flash write time budget, the scheduler and
watchdog reconciliation of the store window, the row j budgets during the window, layout and wear), WP-SW-10
(UART0 divisor, capture margin and telemetry load) and WP-SW-12 (CRC-32 reference model,
golden vectors and error-detection properties), asserts each acceptance value, writes
fw-b1-dml3-results.json beside this file and exits 1 on any failed assertion.
Pass --out <path> to write the results file elsewhere.

Datasheet figures are cited by printed page of the RP2350 datasheet, build 2025-02-20
(rustos docs/rp2350-datasheet.pdf at 2ec64c0, git blob 1b26078d); the note's section 2 lists them.
Values marked ASSUMPTION are not in the repository corpus (note section 3).
"""

from __future__ import annotations

import json
import sys
import zlib
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
FAILS: list[str] = []
NCHECK = 0


def check(cond: bool, msg: str) -> None:
    global NCHECK
    NCHECK += 1
    print(("PASS " if cond else "FAIL ") + msg)
    if not cond:
        FAILS.append(msg)


# ---------------------------------------------------------------------------------------------
# Inputs (note section 2 and section 3)
# ---------------------------------------------------------------------------------------------
SECTOR = 4096                 # flash_range_erase: addr 4096-aligned, count a multiple of 4096 (p. 387)
PAGE = 256                    # flash_range_program: addr 256-aligned, count a multiple of 256 (p. 387)
FLASH_BYTES = 4 * 1024 * 1024  # Pico 2 W25Q32RV, 4 MB (Pico 2 datasheet chapter 1, p. 4; research F15)
XIP_BASE = 0x10000000         # cached XIP window 0x10... (p. 341)
ABS_BLOCK_TARGET = 0x10FFFF00  # RP2350-E10 absolute block address printed by picotool (research F5)
DEVINFO_CS0_DEFAULT = 16 * 1024 * 1024  # FLASH_DEVINFO default CS0 size 16 MB (p. 385)

T_SE_MAX = 0.400              # ASSUMPTION A-7 (keyer host study): 4 KB sector erase maximum
T_PP_MAX = 0.003              # ASSUMPTION A-7: 256-byte page program maximum
T_READBACK = 0.001            # ASSUMPTION A-7: read-back of up to 512 bytes
T_API_OVERHEAD = 0.001        # ASSUMPTION A-F2: connect, exit XIP, flush, XIP setup, per window
ENDURANCE = 100_000           # ASSUMPTION A-F4: erase cycles per sector, W25Q family
LIFE_YEARS = 10               # ASSUMPTION A-F5: service life used for the wear budget

T_WD = 1.0                    # keyer host study section 6.5, request R-1: watchdog load 1.0 s
WD_RATIO_MIN = 2.0            # keyer host study check: load at least twice the longest unkicked interval
REQ_SYS_131_S = 2.0           # REQ-SYS-131: reset re-entering Self-test within 2 s (TBR)
BOOT_OTHER_S = 0.030          # ASSUMPTION A-F6: bootrom, runtime and clock bring-up without the image check
A8_BOOT_S = 0.100             # keyer host study A-8: bootrom plus runtime to Self-test at most 100 ms

F_SYS = (96e6, 150e6)         # spurs-ts012 C1 (96 MHz) and ADR-051 (150 MHz)
CRC_CYCLES_PER_BYTE = 12      # ASSUMPTION A-F7: table-driven byte loop on the Cortex-M33, SRAM table
TPM010_YELLOW = 0.25          # 07 MSR-18: flash usage yellow above 25 percent
TPM010_RED = 0.50             # 07 MSR-18: red above 50 percent

BAUD = 115200
CAPTURE_SPS = 1e6             # Pico-based logic capture, 1 MS/s (test cases, instruments list)
UART_FIFO = 32                # TX FIFO 32 x 8 (p. 958)
TICK_S = 0.001                # 1 kHz scheduler tick (07 section 19, WP-SW-01 ALARM1)
T_PASS = 0.001                # ASSUMPTION A-F8: one main-loop pass with every task due, at most one tick (MSR-26: no overrun)
W_BOUND_PROG = 0.010          # proposal (note section 4.6): declared bound of a program window
W_BOUND_ERASE = 0.450         # proposal (note section 4.6): declared bound of an erase window
WINDOW_SPACING_S = 1.0        # proposal (note section 4.6): normal dispatch between two declared windows, at least
T_PA_SAMPLE = 0.050           # REQ-SYS-118 and 07 section 14.2 row j: PA temperature sampled at 20 Hz
REQ_SYS_155_S = 0.100         # REQ-SYS-155: Fault-safe within 100 ms (TBR) of a PA reading out of range
REQ_SYS_155_PROPOSED_S = 0.500  # proposal to the REQ-SYS-155 TBR closure (request R-11): while PA_EN is held low by a window
T_BATT_PD = 1.0               # 07 section 14.2 row j (07 allocation): battery under-voltage to power-down within 1 s
PAGES_PER_SECTOR = 4096 // 256  # 16 record pages per sector (page-append store, note section 4.7)
CFG_SECTORS = 2               # configuration sectors A and B
LOG_SECTORS = 8               # proposal (request R-3): event-log reserve, 32 KiB, sized in FW-B2
CFG_COMMITS_PER_DAY = 20      # expected commit rate of note section 4.7
LOG_PAGES_PER_DAY = 100       # ASSUMPTION A-F9: event-log page writes per day, on average
LINE_MAX = 120                # proposed maximum trace line, bytes including CR LF (note section 5.3)


# ---------------------------------------------------------------------------------------------
# WP-SW-12 CRC-32 reference models
# ---------------------------------------------------------------------------------------------
POLY = 0x04C11DB7             # normal form
POLY_R = 0xEDB88320           # reflected form


def reflect(v: int, width: int) -> int:
    r = 0
    for i in range(width):
        if v >> i & 1:
            r |= 1 << (width - 1 - i)
    return r


def crc_bitwise_reflected(data: bytes, init: int = 0xFFFFFFFF, xorout: int = 0xFFFFFFFF) -> int:
    crc = init
    for b in data:
        crc ^= b
        for _ in range(8):
            crc = (crc >> 1) ^ (POLY_R if crc & 1 else 0)
    return crc ^ xorout


def crc_msb_first_on_reflected_input(data: bytes) -> int:
    """Independent formulation: MSB-first register with the normal polynomial, each input byte
    bit-reversed and the result bit-reversed (refin = refout = true)."""
    crc = 0xFFFFFFFF
    for b in data:
        crc ^= reflect(b, 8) << 24
        for _ in range(8):
            crc = ((crc << 1) ^ POLY) & 0xFFFFFFFF if crc & 0x80000000 else (crc << 1) & 0xFFFFFFFF
    return reflect(crc, 32) ^ 0xFFFFFFFF


TABLE = []
for _n in range(256):
    _c = _n
    for _ in range(8):
        _c = (_c >> 1) ^ (POLY_R if _c & 1 else 0)
    TABLE.append(_c)


def crc_table(data: bytes, init: int = 0xFFFFFFFF, xorout: int = 0xFFFFFFFF) -> int:
    """The form the cwht-core implementation takes (note section 6.2): 256-entry table, one byte per step."""
    crc = init
    for b in data:
        crc = (crc >> 8) ^ TABLE[(crc ^ b) & 0xFF]
    return crc ^ xorout


def crc_lin(data: bytes) -> int:
    """Linear part (init 0, xorout 0), used for the error-pattern syndromes."""
    return crc_table(data, 0, 0)


# GF(2) polynomial arithmetic for the order test
FULL = (1 << 32) | POLY


def gf_mulmod(a: int, b: int) -> int:
    r = 0
    while b:
        if b & 1:
            r ^= a
        b >>= 1
        a <<= 1
        if a >> 32 & 1:
            a ^= FULL
    return r


def gf_powmod(e: int) -> int:
    result, base = 1, 2   # base = x
    while e:
        if e & 1:
            result = gf_mulmod(result, base)
        base = gf_mulmod(base, base)
        e >>= 1
    return result


def min_weight_undetected(record_bytes: int) -> dict:
    """Exhaustive test of every error pattern of weight 1 to 4 over a record of record_bytes bytes,
    the last 4 of which hold the CRC-32 of the rest (little-endian)."""
    data_bits = (record_bytes - 4) * 8
    syn = np.zeros(data_bits + 32, dtype=np.uint32)
    L = record_bytes - 4
    for j in range(data_bits):
        msg = bytearray(L)
        msg[j // 8] = 1 << (j % 8)
        syn[j] = crc_lin(bytes(msg))
    for k in range(32):
        syn[data_bits + k] = 1 << k
    n = len(syn)
    w1 = bool(np.all(syn != 0))
    w2 = len(np.unique(syn)) == n
    iu, ju = np.triu_indices(n, k=1)
    pairs = syn[iu] ^ syn[ju]
    del iu, ju
    w3 = not bool(np.isin(pairs, syn).any())
    ps = np.sort(pairs)
    w4 = not bool((ps[1:] == ps[:-1]).any())
    hd = 5 if (w1 and w2 and w3 and w4) else (4 if (w1 and w2 and w3) else (3 if (w1 and w2) else 2))
    return {"record_bytes": record_bytes, "codeword_bits": n, "pairs_tested": int(len(pairs)),
            "weight1_all_detected": w1, "weight2_all_detected": w2,
            "weight3_all_detected": w3, "weight4_all_detected": w4, "hamming_distance_at_least": hd}


def main(out: Path) -> int:
    res: dict = {"inputs": {k: v for k, v in globals().items() if k.isupper() and k != "NCHECK" and isinstance(v, (int, float, tuple))}}

    # ---- 1. WP-SW-12 CRC-32: algorithm and golden vectors ---------------------------------------
    check(reflect(POLY, 32) == POLY_R, "0xEDB88320 is the bit reversal of 0x04C11DB7")
    vectors = [
        ("V1", b""),
        ("V2", b"123456789"),
        ("V3", b"\x00"),
        ("V4", b"\xff"),
        ("V5", bytes(32)),
        ("V6", b"\xff" * 32),
        ("V7", bytes(range(256))),
        ("V8", b"The quick brown fox jumps over the lazy dog"),
        ("V9", b"\xff" * 252),
        ("V10", bytes(252)),
        ("V11", b"\xff" * SECTOR),
    ]
    gv = []
    for vid, d in vectors:
        a, b, c, z = crc_bitwise_reflected(d), crc_msb_first_on_reflected_input(d), crc_table(d), zlib.crc32(d)
        agree = a == b == c == z
        check(agree, f"CRC-32 golden vector {vid} ({len(d)} bytes): four implementations agree at 0x{c:08X}")
        gv.append({"id": vid, "length": len(d), "hex_prefix": d[:16].hex(), "crc32": f"0x{c:08X}"})
    res["golden_vectors"] = gv
    check(crc_table(b"123456789") == 0xCBF43926, "check value of '123456789' is 0xCBF43926 (CRC-32/ISO-HDLC)")
    # residue: CRC over data followed by its CRC (little-endian) is a constant
    resid = set()
    for _, d in vectors:
        cr = crc_table(d)
        resid.add(crc_table(d + cr.to_bytes(4, "little")))
    check(len(resid) == 1, f"residue over data plus little-endian CRC is one constant for all vectors: 0x{min(resid):08X}")
    res["residue"] = f"0x{min(resid):08X}"
    # incremental form (streaming over pages) equals one-shot
    d = bytes(range(256)) * 16
    inc = 0xFFFFFFFF
    for i in range(0, len(d), 256):
        inc = crc_table(d[i:i + 256], inc, 0)
    check(inc ^ 0xFFFFFFFF == crc_table(d), "streaming over 256-byte chunks with carried state equals the one-shot CRC")
    # erased and zeroed records fail the check
    ff_rec = b"\xff" * 256
    z_rec = bytes(256)
    check(crc_table(ff_rec[:252]) != int.from_bytes(ff_rec[252:], "little"), "an erased 256-byte record (all 0xFF) fails the CRC check")
    check(crc_table(z_rec[:252]) != int.from_bytes(z_rec[252:], "little"), "an all-zero 256-byte record fails the CRC check")

    # polynomial properties
    order_full = gf_powmod(2**32 - 1) == 1
    primes = (3, 5, 17, 257, 65537)
    check(3 * 5 * 17 * 257 * 65537 == 2**32 - 1, "2^32 - 1 = 3 x 5 x 17 x 257 x 65537")
    proper = all(gf_powmod((2**32 - 1) // q) != 1 for q in primes)
    check(order_full and proper, "x has order 2^32 - 1 modulo the CRC-32 polynomial: the polynomial is primitive")
    parity = bin(FULL).count("1") % 2
    res["poly_terms"] = bin(FULL).count("1")
    res["poly_primitive"] = bool(order_full and proper)
    res["poly_divisible_by_x_plus_1"] = parity == 0
    check(parity == 1, f"the polynomial has {bin(FULL).count('1')} terms (odd): x + 1 is not a factor, so odd-weight errors are not all detected by construction")

    hd256 = min_weight_undetected(256)
    check(hd256["hamming_distance_at_least"] >= 5,
          f"256-byte record: every error of 1 to 4 bits is detected ({hd256['pairs_tested']} pairs); Hamming distance at least 5")
    hd512 = min_weight_undetected(512)
    res["hd"] = {"256": hd256, "512": hd512}
    print(f"INFO 512-byte record: weight-3 all detected {hd512['weight3_all_detected']}, "
          f"weight-4 all detected {hd512['weight4_all_detected']}")

    # CPU and boot-time budgets for the CRC (07 section 14.2 row f; REQ-SYS-132)
    crc_budget = {}
    for f in F_SYS:
        ram_copy_s = 256 * CRC_CYCLES_PER_BYTE / f
        crc_budget[f"{f/1e6:.0f}MHz"] = {"ram_copy_256B_us": ram_copy_s * 1e6, "cpu_share_at_100ms": ram_copy_s / 0.1}
        check(ram_copy_s / 0.1 < 0.001, f"RAM-copy CRC of 256 B every 100 ms at {f/1e6:.0f} MHz uses {ram_copy_s*1e6:.1f} us, under 0.1 percent of the CPU")
    res["crc_budget"] = crc_budget

    # ---- 2. Image check time at boot (REQ-SYS-132 with REQ-SYS-131) -----------------------------
    # XIP miss cost per 8-byte cache line (p. 341): 8-bit serial command prefix (p. 388),
    # EBh quad: 24 address bits on 4 lines = 6 clocks, 6 wait clocks including MODE, 64 data bits = 16 clocks;
    # 03h serial: 24 address clocks, 64 data clocks. Boot leaves EBh at divisor 3 when the part answers it (Table 451, p. 372).
    xip = {"EBh_div3": (8 + 6 + 6 + 16) * 3 / 8, "EBh_div2": (8 + 6 + 6 + 16) * 2 / 8, "03h_div12": (8 + 24 + 64) * 12 / 8}
    res["xip_cycles_per_byte"] = xip
    img = {}
    for f in F_SYS:
        for label, frac in (("64KiB", 64 * 1024 / FLASH_BYTES), ("256KiB", 256 * 1024 / FLASH_BYTES),
                            ("yellow_1MiB", TPM010_YELLOW), ("red_2MiB", TPM010_RED)):
            size = frac * FLASH_BYTES
            for mode in ("EBh_div3", "03h_div12"):
                t = size * (xip[mode] + CRC_CYCLES_PER_BYTE) / f
                img[f"{f/1e6:.0f}MHz_{label}_{mode}"] = t
    res["image_check_s"] = img
    t_red = img["96MHz_red_2MiB_EBh_div3"]
    check(T_WD + BOOT_OTHER_S + t_red <= REQ_SYS_131_S,
          f"REQ-SYS-131: hang to Self-test {T_WD + BOOT_OTHER_S + t_red:.3f} s within 2 s with a 2 MiB image (TPM-010 red line) at 96 MHz, EBh/3")
    t_worst = img["96MHz_red_2MiB_03h_div12"]
    print(f"INFO a 2 MiB check in the slow 03h/12 mode would take {t_worst:.2f} s (the check must not run in that mode)")
    check(T_WD + BOOT_OTHER_S + t_worst > REQ_SYS_131_S,
          "the 03h/12 mode fails REQ-SYS-131 at the red line, so the constraint 'check in the boot XIP mode' is needed")
    size_a8 = (A8_BOOT_S - BOOT_OTHER_S) * 96e6 / (xip["EBh_div3"] + CRC_CYCLES_PER_BYTE)
    res["image_max_for_A8_bytes"] = size_a8
    check(size_a8 >= 256 * 1024, f"A-8 (100 ms) holds for images up to {size_a8/1024:.0f} KiB at 96 MHz, EBh/3 (at least 256 KiB)")

    # ---- 3. WP-SW-08 flash write budget ----------------------------------------------------------
    t_prog_win = T_API_OVERHEAD + T_PP_MAX                           # program window (one 256-byte page)
    t_erase_win = T_API_OVERHEAD + T_SE_MAX                          # erase window (one 4 KiB sector)
    t_keyer_bound = T_SE_MAX + 2 * T_PP_MAX + T_READBACK             # keyer host study section 6.5 figure
    check(abs(t_keyer_bound - 0.407) < 1e-9, "keyer host study bound is 0.407 s (erase 400 ms, two pages 6 ms, read-back 1 ms)")
    check(abs(t_prog_win - 0.004) < 1e-9 and abs(t_erase_win - 0.401) < 1e-9,
          f"program window {t_prog_win*1e3:.0f} ms, erase window {t_erase_win*1e3:.0f} ms (A-7, A-F2)")
    check(t_prog_win <= W_BOUND_PROG and t_erase_win <= W_BOUND_ERASE,
          f"each window fits its declared bound ({W_BOUND_PROG*1e3:.0f} ms program, {W_BOUND_ERASE*1e3:.0f} ms erase)")
    # scheduler and watchdog (note section 4.6): kick -> store step in the same pass -> window -> catch-up pass -> kick
    nokick_design = T_PASS + t_erase_win + T_PASS
    nokick_bound = T_PASS + W_BOUND_ERASE + T_PASS
    res["flash"] = {"program_window_s": t_prog_win, "erase_window_s": t_erase_win, "keyer_study_bound_s": t_keyer_bound,
                    "bound_program_s": W_BOUND_PROG, "bound_erase_s": W_BOUND_ERASE,
                    "longest_without_kick_design_s": nokick_design, "longest_without_kick_at_bound_s": nokick_bound,
                    "ratio_T_wd_design": T_WD / nokick_design, "ratio_T_wd_at_bound": T_WD / nokick_bound}
    check(abs(nokick_design - 0.403) < 1e-9 and nokick_design <= t_keyer_bound,
          f"longest time without a kick (kick, window, catch-up pass) is {nokick_design*1e3:.0f} ms, within the keyer study 0.407 s")
    check(T_WD / nokick_design >= WD_RATIO_MIN,
          f"watchdog load 1.0 s is {T_WD / nokick_design:.2f} times the longest time without a kick (at least 2)")
    check(T_WD / nokick_bound >= WD_RATIO_MIN,
          f"at the declared erase bound the longest time without a kick is {nokick_bound*1e3:.0f} ms: ratio {T_WD / nokick_bound:.2f} (at least 2)")
    bound_max = T_WD / WD_RATIO_MIN - 2 * T_PASS
    res["flash"]["erase_bound_max_for_ratio_2_s"] = bound_max
    check(W_BOUND_ERASE <= bound_max, f"the erase bound {W_BOUND_ERASE*1e3:.0f} ms is under the {bound_max*1e3:.0f} ms that keeps the ratio of 2")
    t_se_limit = W_BOUND_ERASE - T_API_OVERHEAD
    res["flash"]["erase_max_tolerated_s"] = t_se_limit
    check(t_se_limit >= T_SE_MAX, f"the design tolerates a sector erase up to {t_se_limit*1e3:.0f} ms before the bound declares an overrun (A-7 uses 400 ms)")
    check(WINDOW_SPACING_S > nokick_bound, "the 1 s spacing between declared windows is longer than one window, so two never run back to back")
    # hang recovery (REQ-SYS-131): the kick is the main loop's only; a driver-side feed would stack a second load
    hang_design = T_WD + A8_BOOT_S
    hang_driver_feed = 2 * T_WD + A8_BOOT_S
    res["flash"]["hang_to_selftest_design_s"] = hang_design
    res["flash"]["hang_to_selftest_if_driver_feeds_s"] = hang_driver_feed
    check(hang_design <= REQ_SYS_131_S, f"hang to Self-test {hang_design:.1f} s with the kick only in the main loop (REQ-SYS-131, 2 s)")
    check(hang_driver_feed > REQ_SYS_131_S,
          f"a driver that fed the watchdog before each window would allow up to {hang_driver_feed:.1f} s: rejected (SA finding-1)")
    # row j during the window (note section 4.6): the window starts in the pass that took a PA temperature sample
    gap_prog = max(T_PA_SAMPLE, T_PASS + W_BOUND_PROG + T_PASS)
    gap_erase_design = max(T_PA_SAMPLE, nokick_design)
    gap_erase_bound = max(T_PA_SAMPLE, nokick_bound)
    l155 = {"program_window_s": gap_prog + T_PASS, "erase_window_design_s": gap_erase_design + T_PASS,
            "erase_window_at_bound_s": gap_erase_bound + T_PASS}
    res["flash"]["req_sys_155_latency"] = l155
    check(l155["program_window_s"] <= REQ_SYS_155_S,
          f"REQ-SYS-155 with a program window: {l155['program_window_s']*1e3:.0f} ms, within 100 ms (the normal 20 Hz path)")
    check(l155["erase_window_design_s"] > REQ_SYS_155_S,
          f"REQ-SYS-155 with an erase window: {l155['erase_window_design_s']*1e3:.0f} ms (design), over 100 ms: routed (R-11)")
    check(l155["erase_window_at_bound_s"] <= REQ_SYS_155_PROPOSED_S,
          f"REQ-SYS-155 with an erase window at its bound: {l155['erase_window_at_bound_s']*1e3:.0f} ms, within the 500 ms proposed for PA_EN held low")
    p_batt_max = T_BATT_PD - nokick_bound - T_PASS
    res["flash"]["battery_supervision_period_max_s"] = p_batt_max
    check(p_batt_max >= 0.5, f"battery under-voltage power-down within 1 s holds for a supervision period up to {p_batt_max*1e3:.0f} ms")
    # alignment of the proposed store (note section 4.4)
    store = {"A": 0x3FD000, "B": 0x3FE000, "reserved_E10": 0x3FF000}
    log_base = 0x3FD000 - LOG_SECTORS * SECTOR
    for i in range(LOG_SECTORS):
        store[f"log{i}"] = log_base + i * SECTOR
    res["flash"]["layout"] = {k: f"0x{v:06X}" for k, v in store.items()}
    res["flash"]["app_flash_end"] = f"0x{log_base:06X}"
    check(log_base == 0x3F5000 and FLASH_BYTES - log_base == 44 * 1024,
          "the event-log reserve (8 sectors) starts at 0x3F5000; the application FLASH region ends 44 KiB below the device end")
    for k, off in store.items():
        check(off % SECTOR == 0 and off + SECTOR <= FLASH_BYTES, f"store sector {k} at offset 0x{off:06X} is sector-aligned inside 4 MB")
    abs_off = (ABS_BLOCK_TARGET - XIP_BASE)
    check(abs_off < DEVINFO_CS0_DEFAULT, "E10 block offset 0xFFFF00 lies inside the 16 MB default CS0 size, so the bootrom accepts it")
    alias = abs_off % FLASH_BYTES
    alias_sector = alias - alias % SECTOR
    res["flash"]["e10_alias_offset"] = f"0x{alias:06X}"
    res["flash"]["e10_alias_sector"] = f"0x{alias_sector:06X}"
    check(alias_sector == 0x3FF000, "with 22 decoded address bits (A-F3) the E10 block lands in the last sector 0x3FF000")
    check(alias_sector not in (store["A"], store["B"]), "the proposed copies A and B avoid the E10 sector")
    check(0x3FF000 == FLASH_BYTES - SECTOR, "research F15 copy B (0x103FF000) is the last sector, the E10 sector")
    check(all(v != 0x3FF000 for k, v in store.items() if k != "reserved_E10"), "no store or log sector is the E10 sector")
    # wear budget (note section 4.7): page-append records, one erase per sector per revolution
    days = LIFE_YEARS * 365
    cfg_per_sector = CFG_COMMITS_PER_DAY * days / (CFG_SECTORS * PAGES_PER_SECTOR)
    cfg_rate_at_endurance = ENDURANCE * CFG_SECTORS * PAGES_PER_SECTOR / days
    log_per_sector = LOG_PAGES_PER_DAY * days / (LOG_SECTORS * PAGES_PER_SECTOR)
    erase_windows_per_day = CFG_COMMITS_PER_DAY / PAGES_PER_SECTOR + LOG_PAGES_PER_DAY / PAGES_PER_SECTOR
    res["flash"]["wear"] = {"cfg_erases_per_sector_life": cfg_per_sector, "cfg_commits_per_day_at_endurance": cfg_rate_at_endurance,
                            "log_erases_per_sector_life": log_per_sector, "erase_windows_per_day": erase_windows_per_day}
    check(cfg_per_sector <= ENDURANCE / 10,
          f"configuration: {cfg_per_sector:.0f} erases per sector in 10 years at 20 commits a day (endurance allows {cfg_rate_at_endurance:.0f} a day)")
    check(log_per_sector <= ENDURANCE / 10,
          f"event log: {log_per_sector:.0f} erases per sector in 10 years at {LOG_PAGES_PER_DAY} pages a day (factor {ENDURANCE/log_per_sector:.0f})")
    check(abs(erase_windows_per_day - 7.5) < 1e-9, f"erase windows per day, configuration and log: {erase_windows_per_day:.2f}")
    t_scan = CFG_SECTORS * SECTOR * (((8 + 6 + 6 + 16) * 3 / 8) + CRC_CYCLES_PER_BYTE) / 96e6
    res["flash"]["boot_scan_32_pages_s"] = t_scan
    check(t_scan < 0.003, f"the boot scan of the 32 configuration pages takes {t_scan*1e3:.1f} ms at 96 MHz, EBh/3")
    seq_life = cfg_rate_at_endurance * days
    check(seq_life < 2**32 / 1000, f"{seq_life/1e6:.1f} million commits in 10 years at the endurance rate: a u32 sequence never wraps")
    rev0_rate = ENDURANCE / days * CFG_SECTORS
    check(abs(rev0_rate - 54.8) < 0.05, f"option A (revision 0, one erase per commit) allows {rev0_rate:.1f} commits a day")
    # option C (note section 4.6.5): every erase in the boot path
    boot_c1 = T_WD + BOOT_OTHER_S + t_red + t_erase_win
    boot_c2 = T_WD + BOOT_OTHER_S + t_red + 2 * t_erase_win
    res["flash"]["option_C_hang_to_selftest_s"] = {"one_sector": boot_c1, "two_sectors": boot_c2}
    check(boot_c1 <= REQ_SYS_131_S and REQ_SYS_131_S - boot_c1 < 0.013,
          f"option C: hang to Self-test {boot_c1:.3f} s with one boot erase (2 MiB image, 96 MHz): {1e3*(REQ_SYS_131_S - boot_c1):.0f} ms margin")
    check(boot_c2 > REQ_SYS_131_S, f"option C: {boot_c2:.3f} s with two boot erases, over 2 s")
    check(l155["erase_window_at_bound_s"] < 1.0, "the fault screen after an erase window still starts inside the 1 s of REQ-SYS-067")
    # program page and record size
    check(256 % PAGE == 0, "the 256-byte record is one program page")

    # ---- 4. WP-SW-10 UART0 ------------------------------------------------------------------------
    uart = {}
    for f in F_SYS:
        div = f / (16 * BAUD)                  # p. 961 to 962: BAUDDIV = UARTCLK / (16 x baud)
        ibrd = int(div)
        fbrd = int((div - ibrd) * 64 + 0.5)
        actual = f / (16 * (ibrd + fbrd / 64))
        err = actual / BAUD - 1
        uart[f"{f/1e6:.0f}MHz"] = {"IBRD": ibrd, "FBRD": fbrd, "baud": actual, "error": err}
        check(abs(err) < 0.001, f"115200 baud at clk_peri {f/1e6:.0f} MHz: IBRD {ibrd}, FBRD {fbrd}, error {err*100:+.4f} percent")
        check(f >= 16 * BAUD and f <= 16 * 65535 * BAUD, f"clock constraint 16 x baud <= UARTCLK <= 16 x 65535 x baud holds at {f/1e6:.0f} MHz")
    spb = CAPTURE_SPS / BAUD
    # decoder: start edge located to within one sample; the stop bit centre lies 9.5 bits after the edge
    tol = (0.5 - 1 / spb) / 9.5
    uart["capture"] = {"samples_per_bit": spb, "baud_mismatch_tolerance": tol}
    check(spb >= 8, f"the 1 MS/s logic capture gives {spb:.2f} samples per bit at 115200 baud (at least 8)")
    worst_err = max(abs(v["error"]) for k, v in uart.items() if k.endswith("MHz"))
    check(tol > 10 * worst_err, f"capture decode tolerance {tol*100:.2f} percent is more than 10 times the divisor error")
    rate = BAUD / 10                            # 8N1: 10 bit times per byte
    dit_50 = 1.2 / 50                           # 1200/WPM ms (keyer host study I-1)
    key_edges_per_s = 2 / (2 * dit_50)          # continuous dits: two edges per dit-space pair
    load = {"STAT_1Hz": 1 * LINE_MAX, "KEY_edges_50WPM": key_edges_per_s * 40, "MODE_EVT_10_per_s": 10 * 80}
    total = sum(load.values())
    uart["load_Bps"] = load
    uart["capacity_Bps"] = rate
    uart["utilisation"] = total / rate
    check(total / rate <= 0.5, f"peak telemetry load {total:.0f} B/s is {total/rate*100:.0f} percent of the {rate:.0f} B/s line (at most 50 percent)")
    per_tick = rate * TICK_S
    check(per_tick < UART_FIFO, f"one 1 ms tick drains {per_tick:.2f} B, under the 32-byte FIFO, so a refill each tick keeps the line busy")
    gap_ok = UART_FIFO / rate
    uart["fifo_gap_s"] = gap_ok
    check(gap_ok >= 2 * TICK_S, f"a full FIFO covers {gap_ok*1e3:.2f} ms, at least two ticks")
    ring = 1024
    stat_only = 1 * LINE_MAX * (nokick_bound + 0.1)
    uart["ring_bytes"] = ring
    check(stat_only < ring, f"during an erase window at its bound (no keying, R-2) the STAT lines queue {stat_only:.0f} B, under a 1 KiB ring")
    # telemetry line format (note section 5.4): golden lines with their CRC-32
    samples = [
        ("BOOT", 0, 81234, "fw=0.1.0,img=1A2B3C4D,st=PASS"),
        ("MODE", 1, 1500000, "from=SELFTEST,to=RECEIVE,tr=T08,cause=PASS,pa=0"),
        ("STAT", 2, 2000000, "mode=RECEIVE,flags=00,c1=3912,c2=3905,tpa=251,drop=0"),
        ("EVT", 3, 2100417, "ev=TXKEY,v=1"),
        ("STAT", 65535, 18446744073709551615,
         "mode=FAULTSAFE,flags=0F,c1=4200,c2=4200,tpa=-200,drop=65535"),
    ]
    lines = []
    for typ, seq, t, fields in samples:
        body = f"{typ},{seq},{t},{fields}"
        c = crc_table(body.encode("ascii"))
        line = f"${body}*{c:08X}\r\n"
        lines.append({"line": line.rstrip(), "bytes": len(line), "crc32": f"{c:08X}"})
        check(len(line) <= LINE_MAX, f"trace line {typ} seq {seq} is {len(line)} bytes, at most {LINE_MAX}")
    uart["golden_lines"] = lines
    res["uart"] = uart

    res["assertions"] = NCHECK
    res["failed"] = FAILS
    out.write_text(json.dumps(res, indent=1, default=str) + "\n")
    print(f"{NCHECK} assertions, {len(FAILS)} failed; results in {out}")
    return 1 if FAILS else 0


if __name__ == "__main__":
    out_path = HERE / "fw-b1-dml3-results.json"
    if "--out" in sys.argv:
        out_path = Path(sys.argv[sys.argv.index("--out") + 1])
    sys.exit(main(out_path))
