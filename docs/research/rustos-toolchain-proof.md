# rustos toolchain proof and RP2350 driver extension map for cwht

**Assignment key:** rustos. **Date:** 2026-09-25. **Author:** Claude (research agent). **Status:** Draft for SRR toolchain-proof entrance product.

## Question

Hands-on in `/Users/robinonsay/rust/rustos` (read-only apart from `target/`): run `cargo build` (host, default members), `cargo test -p api`, and `cargo pico2` (alias for `build -p pico2 --target thumbv8m.main-none-eabihf`); report results and errors; check the picotool version and how to convert the ELF to UF2 without flashing; inspect the `api` and `pico2` crates and produce a driver extension map for cwht (I2C for an Si5351-class synthesizer, SPI for an LCD, ADC for battery and volume, PWM for sidetone and backlight, TIMER alarms for the keyer and UI ticks, GPIO interrupts or PIO for the rotary encoder and key or paddle inputs, watchdog, flash configuration storage) with RP2350 datasheet chapters and register-block names; say how the existing `api` traits (`Read`, `Write`, `Gpio`, `PinHandle`, `define_board!`) would extend and how host-side testing with mocked drivers fits; deliver a work-package table.

Owner input carried into this report: SI-018 (core requirement) says the radio shall support both a straight key and iambic paddles with a built-in electronic keyer. The driver map treats the key jack as two active-low inputs (tip = dit or straight key, ring = dah) and the keyer as portable logic that must be host-testable.

## Method

Local commands on macOS (Darwin 25.6.0, Apple silicon), all in `/Users/robinonsay/rust/rustos` unless noted. Builds were run from a clean `target/` (`cargo clean` first) so the results are not cache hits. Datasheet text was extracted with `pdftotext -layout` (poppler 26.08.0) from `/Users/robinonsay/rust/rustos/docs/rp2350-datasheet.pdf` (build 2025-02-20) and from a freshly downloaded copy of the current online datasheet (build 2025-07-29) to check for revision drift. Two proof crates were built in the session scratch directory: (a) a copy of the owner's `rustos_demo` application, path-patched to the local checkout, built and converted to UF2; (b) a host `cargo test` crate with a mock GPIO driver implementing the `api` traits. Web checks: Rust platform-support page, picotool GitHub releases, Raspberry Pi documentation pages. The `rustos` repository's own extracted ICDs (`docs/icd/rp2350/{clocks,gpio,i2c,spi,uart}`) were surveyed for reuse.

Toolchain versions observed:

```
$ rustc --version && cargo --version
rustc 1.98.0 (88d9e12ae 2026-08-18)
cargo 1.98.0 (797e8a9bc 2026-08-05)
$ rustup show            (abridged)
installed targets: aarch64-apple-darwin, thumbv8m.main-none-eabihf
$ picotool version
picotool v2.3.0 (Darwin, AppleClang-21.0.0.21000099, Release)
$ cargo clippy --version
clippy 0.1.98 (88d9e12ae1 2026-08-18)
$ which probe-rs elf2uf2-rs   -> not installed (not needed; picotool covers conversion and load)
```

## Findings

### F1. Host build of the default members succeeds from clean (High)

```
$ cargo clean
     Removed 610 files, 22.8MiB total
$ cargo build
   Compiling api v0.1.0 (/Users/robinonsay/rust/rustos/api)
    Finished `dev` profile [unoptimized + debuginfo] target(s) in 0.39s
exit=0
```

`Cargo.toml` sets `default-members = ["api"]`, so the host build covers only the portable crate, by design (the `pico2` crate is a `#![no_std]` library that only makes sense for its own triple).

### F2. `cargo test -p api` passes but exercises nothing (High)

```
$ cargo test -p api
     Running unittests src/lib.rs (target/debug/deps/api-f1ce788862a78ad4)
running 0 tests
test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out
   Doc-tests api
running 3 tests
test api/src/common/mod.rs - common::ErrorType (line 16) ... ignored
test api/src/device/mod.rs - device::define_board (line 177) ... ignored
test api/src/gpio/mod.rs - gpio (line 17) ... ignored
test result: ok. 0 passed; 0 failed; 3 ignored
exit=0
```

The `api` crate has zero unit tests and its three doctests are `ignore`d. The README describes a `cargo xtest` alias for host tests; `.cargo/config.toml` no longer defines it (the only alias is `pico2`). Documentation drift, not a build defect.

### F3. `cargo pico2` cross-build succeeds in dev and release (High)

```
$ cargo pico2
   Compiling pico2 v0.1.0 (/Users/robinonsay/rust/rustos/firmware/pico2)
   Compiling api v0.1.0 (/Users/robinonsay/rust/rustos/api)
    Finished `dev` profile [unoptimized + debuginfo] target(s) in 0.38s
exit=0
$ cargo pico2 --release
    Finished `release` profile [optimized] target(s) in 1.28s
exit=0
$ ls target/thumbv8m.main-none-eabihf/release/
libpico2.rlib (127,974 B)   libpico2.d   deps/  build/  ...
```

Output is an `.rlib` only. Since commit `8502402 "Move demo app out"`, the workspace has no binary crate: the flashable application lives in the sibling directory `/Users/robinonsay/rust/rustos_demo` (git deps on `github.com/robinonsay/rustos`, `[patch]`-overridden to `../rustos`). The README still describes a three-crate workspace with `demo/` and says `cargo build --release` produces the image; that is stale. `thumbv8m.main-none-eabihf` is a Tier 3 Rust target, `no_std` only, no host tools (https://doc.rust-lang.org/nightly/rustc/platform-support.html).

### F4. End-to-end application build against the local checkout works offline (High)

A copy of `rustos_demo` was placed in the scratch directory with the `[patch]` paths made absolute and built with `--offline`:

```
$ cargo build --release --offline
   Compiling pico2 v0.1.0 (/Users/robinonsay/rust/rustos/firmware/pico2)
   Compiling api v0.1.0 (/Users/robinonsay/rust/rustos/api)
   Compiling demo v0.1.0 (.../scratchpad/demo_build)
warning: linker stdout: Memory region         Used Size  Region Size  %age Used
                    FLASH:        2008 B         4 MB      0.05%
                      RAM:        8200 B       520 KB      1.54%
  = note: `#[warn(linker_messages)]` on by default
    Finished `release` profile [optimized] target(s) in 1.42s
exit=0
$ file target/thumbv8m.main-none-eabihf/release/demo
ELF 32-bit LSB executable, ARM, EABI5 version 1, statically linked, not stripped   (134,500 B)
```

The single warning is the linker memory report that the template's `rustflags` deliberately requests (`--print-memory-usage`); 8,192 B of the RAM figure is the reserved minimum stack from `link.ld`. The template `.cargo/config.toml` also sets `runner = "picotool load -u -x -t elf"`, so `cargo run --release` flashes a BOOTSEL-mode board; the runner was not executed here.

### F5. ELF to UF2 conversion with picotool needs no device attached (High)

```
$ cp target/thumbv8m.main-none-eabihf/release/demo demo.elf
$ picotool uf2 convert demo.elf demo.uf2 --family rp2350-arm-s
exit=0                      -> demo.uf2, 4096 B
$ picotool info -a demo.uf2
File demo.uf2 family ID 'rp2350-arm-s':
Program Information: target chip RP2350, image type ARM Secure
Metadata Block 1: address 0x10000110, block type image def, target chip RP2350, image type ARM Secure
$ picotool uf2 convert demo.elf demo_abs.uf2 --family rp2350-arm-s --abs-block
RP2350-E10: Adding absolute block to UF2 targeting 0x10ffff00
exit=0                      -> demo_abs.uf2, 4608 B
```

picotool identifies input type by extension, so the ELF must carry a `.elf` name (or pass `-t elf`). The committed `blinky.elf` converts to a UF2 byte-identical to the committed `blinky.uf2` (sha256 `7e03c238...32d9` for both), confirming the README claim. The `--abs-block` flag applies the RP2350-E10 workaround (UF2 drag-and-drop fails when a partition table is present on A2 silicon); it is harmless on an unpartitioned Pico 2 and should be the default for release images. Usage text: `picotool help uf2 convert`. Upstream picotool is at 2.3.1 (GitHub releases page, 2026-09-05 per search results; fixes `uf2 convert` model inference when `--platform` is omitted); the installed 2.3.0 behaved correctly with `--family` given explicitly. Source: https://github.com/raspberrypi/picotool/releases.

### F6. Static-analysis and formatting baseline of rustos (High)

```
$ cargo clippy -p api                                        -> 0 warnings
$ cargo clippy -p pico2 --target thumbv8m.main-none-eabihf   -> 13 warnings:
   7 needless `return`, 2 empty `loop {}` (panic/default handlers), 2 unnecessary pointer casts,
   1 unnecessary parentheses, 1 module inception (gpio::gpio)
$ cargo fmt --check -p api -p pico2 | grep -c '^Diff in'      -> 71 hunks (sources are not rustfmt-formatted)
$ cargo doc -p api --no-deps ; cargo doc -p pico2 --no-deps --target thumbv8m...   -> both clean
$ grep -c unsafe  (lines mentioning unsafe): api 11, pico2 42
```

None of the clippy findings is a correctness defect; they matter because the cwht software plan commits to clippy as static analysis (charter section 10, SWE-061/135) and a `-D warnings` gate would fail today on `pico2`.

### F7. What the `api` crate provides today (High)

Source: `/Users/robinonsay/rust/rustos/api/src/{lib,common/mod,gpio/mod,device/mod}.rs` (87 + 114 + 180 + 322 lines, mostly documentation).

| Item | Definition | Notes |
|---|---|---|
| `common::ErrorType` | `type Error: Debug` supertrait | one error type per peripheral, embedded-hal 1.0 style |
| `common::Write<T>` | `fn write(&mut self, T) -> Result<(), Self::Error>` | doc: "idempotent and non-blocking where the hardware allows"; a UART "would implement `Write<u8>`" |
| `common::Read<T>` | `fn read(&mut self) -> Result<T, Self::Error>` | `&mut self` so FIFO-popping reads are sound |
| `gpio::Pull` | `Up`, `Down`, `None` | required argument, no default |
| `gpio::GpioPinIn<N>` / `GpioPinOut<N>` | marker traits over `Read<bool>` / `Write<bool>` | pin number is a const generic |
| `gpio::Gpio` | GATs `Input<const N>`, `Output<const N>`; `input_from_handle(PinHandle<N>, Pull)`, `output_from_handle(PinHandle<N>)` | consumes the handle, so double configuration is a compile error |
| `device::PinHandle<N>` | zero-sized, `const unsafe fn new()` | "Call it directly only in host-side tests or on hardware not (yet) described by a `define_board!`" |
| `device::DeviceHandle<T>` | zero-sized `PhantomData<T>` claim on one peripheral | driver constructors consume it |
| `define_board!` | generates `Pins` struct, board struct with `DeviceHandle` fields, once-per-boot `take()` via `AtomicBool::compare_exchange` | rough edges documented in-source: needs `use core::sync::atomic::Ordering::Acquire;` in the invoking module; fixed `BOARD_TAKEN` name, one board per module |

Absent from `api`: any notion of time (instant, duration, delay, alarm), bus transactions (I2C, SPI), PWM duty, ADC samples, interrupts or critical sections, non-volatile storage, watchdog. Every one of these is needed by cwht and must be added as new traits in `api` (portable, host-compilable) before the `pico2` drivers exist.

### F8. What the `pico2` crate provides today, and the gaps that block cwht (High)

Source: `/Users/robinonsay/rust/rustos/firmware/pico2/src/{lib,common/{mod,board,reg,reset},gpio/{mod,gpio}}.rs`, `link.ld`, `build.rs`.

Provided: `BOOT_INFO` IMAGE_DEF block; a 68-entry `VECTOR_TABLE` static; `OnReset` (enables FPU via CPACR, sets VTOR, copies `.data`, zeroes `.bss`, calls `__rustos_main`); `entry!` macro; `RegAddr { RESET, IO_BANK0, PADS_BANK0, SIO }`; `clr_reset_reg`, `set_reset_reg`, `wait_for_reset_done` (read-modify-write on `RESETS.RESET`); `Rp2350` board with pins `gpio0..gpio22, smps_ps(23), vbus_sense(24), led(25), gpio26..gpio28, vsys_adc(29)` and one device `gpio: Rp2350Gpio`; `Rp2350Gpio` (releases IO_BANK0 and PADS_BANK0 from reset, SIO function 5 only) producing `Rp2350GpioIn<N>` / `Rp2350GpioOut<N>` with `Error = Infallible`, `const _VALID: () = assert!(N < 30)`.

Gaps that matter for cwht:

1. **No interrupt path.** All 66 non-reset vector entries are `DefaultHandler` (`loop {}`), built as a `const` static inside `pico2`. An application cannot install a handler without editing `pico2`; there is no NVIC enable/priority code and no critical-section primitive. Stable-Rust remedy (the `cortex-m-rt` pattern): declare `unsafe extern "C" { fn TIMER0_IRQ_0(); ... }` for the 52 RP2350 IRQ lines, place them in the table, and add `PROVIDE(TIMER0_IRQ_0 = DefaultHandler);` lines to `link.ld` so an application's `#[unsafe(no_mangle)] extern "C" fn TIMER0_IRQ_0()` overrides the default. NVIC registers (datasheet 3.7.5, extracted md lines 10712 to 10740): `NVIC_ISER0` at PPB+0x0E100, `NVIC_ICER0` +0x0E180, `NVIC_ISPR0` +0x0E200, `NVIC_IPR0` +0x0E400.
2. **No clock bring-up.** After the bootrom the chip runs from the ring oscillator ("During boot, the ROSC runs at a nominal 11 MHz, but varies with PVT", datasheet 8.1.1.2). The demo's `delay()` is "calibrated by eye". Keyer element timing (dit = 1200 ms / WPM) and I2C/SPI bit clocks need the crystal (Pico 2 fits an Abracon ABM8-272-T3 12 MHz crystal, Pico 2 datasheet section 2) and PLL_SYS.
3. **Timer tick not started.** "The timer's tick (see Section 8.5) must be running for the timer to start counting" (12.8.4). The TICKS block (`TICKS_BASE 0x40108000`: `TIMER0_CTRL 0x18`, `TIMER0_CYCLES 0x1c`, `WATCHDOG_CTRL 0x30`, `WATCHDOG_CYCLES 0x34`, `PROC0_CTRL 0x00`) must be programmed with `CYCLES = 12` for a 1 us tick from a 12 MHz `clk_ref` (8.5).
4. **Reset helper granularity.** Each new driver must release its own `RESETS.RESET` bit (table in F9). The helpers use read-modify-write; the atomic set/clear/xor aliases (+0x2000/+0x3000/+0x1000 on every APB block, datasheet 2.1.3) are unused. Not a defect, but interrupt-safe bring-up is simpler with the aliases.
5. **Linker script already supports RAM-resident code.** `.data : { *(.data .data.*) } > RAM AT > FLASH`, so a function tagged `#[unsafe(link_section = ".data.ramfunc")]` is copied to SRAM by `reset_data()`. That is exactly what flash programming needs (F15).

### F9. Address map, reset bits and IRQ numbers for every cwht peripheral (High)

Sources: datasheet 2.2 "Address Map" (pdf pp. 30 to 34), 7.5 "Subsystem Resets" `RESETS.RESET` bit table (pp. 500 to 505), 3.2 "Interrupts" Table (pp. 82 to 84). `RESETS_BASE = 0x40020000` (already `RegAddr::RESET`).

| Block | Base | RESETS.RESET bit | NVIC IRQ | Datasheet section (pdf page) |
|---|---|---|---|---|
| CLOCKS | 0x40010000 | (5, RO in RESET_DONE only) | CLOCKS_IRQ 30 | 8.1 (510) |
| XOSC | 0x40048000 | not in RESETS | | 8.2 (552) |
| PLL_SYS | 0x40050000 | 14 | PLL_SYS_IRQ 42 | 8.6 (572) |
| TICKS | 0x40108000 | not in RESETS | | 8.5 (567) |
| IO_BANK0 | 0x40028000 | 6 | IO_IRQ_BANK0 21 (NS 22) | 9.4, 9.5, 9.11.1 (586, 591, 601) |
| PADS_BANK0 | 0x40038000 | 9 | | 9.6, 9.11.3 (592, 782) |
| SIO | 0xd0000000 | 21 (RO) | SIO_IRQ_FIFO 25 | 3.1, 9.8 (36, 594) |
| TIMER0 | 0x400b0000 | 23 | TIMER0_IRQ_0..3 = 0..3 | 12.8 (1179) |
| TIMER1 | 0x400b8000 | 24 | TIMER1_IRQ_0..3 = 4..7 | 12.8 |
| PWM | 0x400a8000 | 16 | PWM_IRQ_WRAP_0 8, _1 9 | 12.5 (1073) |
| ADC | 0x400a0000 | 0 | ADC_IRQ_FIFO 35 | 12.4 (1063) |
| I2C0 / I2C1 | 0x40090000 / 0x40098000 | 4 / 5 | I2C0_IRQ 36 / I2C1_IRQ 37 | 12.2 (980) |
| SPI0 / SPI1 | 0x40080000 / 0x40088000 | 18 / 19 | SPI0_IRQ 31 / SPI1_IRQ 32 | 12.3 (1043) |
| DMA | 0x50000000 | 2 | DMA_IRQ_0..3 = 10..13 | 12.6 (1091) |
| PIO0 / PIO1 / PIO2 | 0x50200000 / 0x50300000 / 0x50400000 | 11 / 12 / 13 | PIO0_IRQ_0/1 = 15/16, PIO1 17/18, PIO2 19/20 | 11 (873) |
| WATCHDOG | 0x400d8000 | not in RESETS (reset only by chip-level reset, 12.9.1) | | 12.9 (1190) |
| XIP_QMI | 0x400d0000 | (20 XIP, RO) | | 12.14 (1223) |
| POWMAN | 0x40100000 | | POWMAN_IRQ_POW 44, _TIMER 45 | 6.4 (454) |
| PPB (NVIC, SysTick) | 0xe0000000 | | | 3.7 (123) |

Register names extracted from each block's "List of Registers" (offsets relative to base):

- **I2C (DW_apb_i2c), 12.2.17 (p. 1005):** `IC_CON 0x00, IC_TAR 0x04, IC_SAR 0x08, IC_DATA_CMD 0x10, IC_SS_SCL_HCNT 0x14, IC_SS_SCL_LCNT 0x18, IC_FS_SCL_HCNT 0x1c, IC_FS_SCL_LCNT 0x20, IC_INTR_STAT 0x2c, IC_INTR_MASK 0x30, IC_RAW_INTR_STAT 0x34, IC_RX_TL 0x38, IC_TX_TL 0x3c, IC_CLR_INTR 0x40 ... IC_CLR_TX_ABRT 0x54 ... IC_ENABLE 0x6c, IC_STATUS 0x70, IC_TXFLR 0x74, IC_RXFLR 0x78, IC_SDA_HOLD 0x7c, IC_TX_ABRT_SOURCE 0x80, IC_DMA_CR 0x88, IC_ENABLE_STATUS 0x9c, IC_FS_SPKLEN 0xa0`. GPIO function select F3. External pull-ups required (rustos `docs/icd/rp2350/i2c/01_overview.md`, quoting 12.2.1.3). Master init sequence is already captured in `docs/icd/rp2350/i2c/02_modes.md`.
- **SPI (PL022), 12.3.5 (p. 1057):** `SSPCR0 0x000, SSPCR1 0x004, SSPDR 0x008, SSPSR 0x00c, SSPCPSR 0x010, SSPIMSC 0x014, SSPRIS 0x018, SSPMIS 0x01c, SSPICR 0x020, SSPDMACR 0x024`. GPIO function F1. rustos `docs/icd/rp2350/spi/` exists.
- **ADC, 12.4.7 (p. 1070):** `CS 0x00, RESULT 0x04, FCS 0x08, FIFO 0x0c, DIV 0x10, INTR 0x14, INTE 0x18, INTF 0x1c, INTS 0x20`. QFN-60: `CS.AINSEL 0..3` map to GPIO26..GPIO29, 4 = temperature sensor (12.4.2.1). Needs a 48 MHz `clk_adc`, "which could come from the USB PLL" (12.4.3); 96 cycles per sample = 2 us; 12-bit, 9.2 ENOB.
- **PWM, 12.5.3 (p. 1083):** per slice n: `CHn_CSR, CHn_DIV, CHn_CTR, CHn_CC, CHn_TOP` at 0x14*n; global `EN, INTR, IRQ0_INTE/INTF/INTS, IRQ1_*`. 12 slices, 16-bit counter, 8.4 fractional divider, double-buffered TOP and CC. Channel map for GPIO 0..29: GPIO g drives slice (g/2) mod 8, channel A for even g, B for odd g (12.5.2 table); the two channels of a slice share one period. GPIO function F4.
- **TIMER, 12.8.5 (p. 1185):** `TIMEHW 0x00, TIMELW 0x04, TIMEHR 0x08, TIMELR 0x0c, ALARM0..3 0x10..0x1c, ARMED 0x20, TIMERAWH 0x24, TIMERAWL 0x28, DBGPAUSE 0x2c, PAUSE 0x30, LOCKED 0x34, SOURCE 0x38, INTR 0x3c, INTE 0x40, INTF 0x44, INTS 0x48`. 64-bit 1 us counter; 4 alarms on the low 32 bits (max 2^32 us, about 71.6 min); arm by writing ALARMn, clear by writing 1 to INTR. Read TIMELR then TIMEHR (latching), or TIMERAWL for a 32-bit fast path.
- **GPIO interrupts, 9.5 (p. 591) and 9.11.1:** per-pin Level High/Low and Edge High/Low; edge events latch in `INTR0..5 0x230..0x244`; per-destination `PROC0_INTE0..5 0x248, PROC0_INTF0..5 0x260, PROC0_INTS0..5 0x278`, summary `IRQSUMMARY_PROC0_SECURE0/1 0x200/0x204`. All Bank 0 pins share `IO_IRQ_BANK0` (21). Pad controls 9.6: `PADS_BANK0.GPIOn` bits `SCHMITT, PUE, PDE, IE, OD, ISO, DRIVE, SLEWFAST` (the driver already uses IE 6, OD 7, PUE 3, PDE 2, ISO 8).
- **PIO, 11.7 (p. 936):** `CTRL 0x000, FSTAT, FDEBUG, FLEVEL, TXF0..3 0x010, RXF0..3 0x020, IRQ 0x030, IRQ_FORCE, INPUT_SYNC_BYPASS, DBG_*, INSTR_MEM0..31 0x048..0x0c4, SMn_CLKDIV/EXECCTRL/SHIFTCTRL/ADDR/INSTR/PINCTRL from 0x0c8 (0x18 per SM)`, plus RP2350 `GPIOBASE`, `INTR`, `IRQ0_INTE/INTF/INTS`. GPIO functions F6/F7/F8. Datasheet 11.6.7 gives an I2C example and 11.6.8 a PWM example; no quadrature example in the datasheet itself (the pico-examples repo has one).
- **Watchdog, 12.9.7 (p. 1193):** `CTRL 0x00 (ENABLE, PAUSE_*, TRIGGER, TIME 23:0), LOAD 0x04, REASON 0x08, SCRATCH0..7 0x0c..0x28`. Tick from `TICKS.WATCHDOG_*`; reset scope chosen outside the block via `RESETS.WDSEL`, `PSM.WDSEL`, `POWMAN.WATCHDOG` (12.9.4). 24-bit `LOAD` at a 1 us tick gives about 16.7 s maximum. The bootrom checks the scratch registers for a magic value at boot to allow a soft reset into user code (5.2.4).
- **QMI, 12.14.6 (p. 1233):** `DIRECT_CSR 0x00, DIRECT_TX 0x04, DIRECT_RX 0x08, M0_TIMING 0x0c, M0_RFMT, M0_RCMD, M0_WFMT, M0_WCMD, M1_* 0x20.., ATRANS0..7 0x34..0x50`. Direct mode (12.14.5) is the register-level alternative to the bootrom flash API; not recommended for cwht (F15).

### F10. The timebase for the keyer depends on a clock driver that does not exist yet (High)

Datasheet 8.5: "The tick generators use clk_ref as their reference clock ... Ideally, clk_ref will be configured to use the crystal oscillator (XOSC) to provide an accurate reference ... For a 12 MHz reference clock, set the cycle count to 12 to generate a 1 us tick." 12.8.1: TIMER0/TIMER1 are 64-bit microsecond counters with four alarms each. A keyer at 20 WPM has a 60 ms dit; 1 percent timing accuracy is easily met from the crystal and not at all from the ROSC (PVT variation, 8.1.1.2). The July 2025 datasheet changed the documented reset values of `CLK_SYS_CTRL.SRC` and `.AUXSRC` for stepping A3, so the clock driver must write every field explicitly rather than rely on reset defaults. rustos already holds an extracted clocks ICD (`docs/icd/rp2350/clocks/02_programming.md`).

### F11. RP2350-E9 rules out internal pull-downs for key, paddle and encoder inputs on A2 silicon (High)

Datasheet Appendix E, RP2350-E9 (local copy p. 1357; "Affects RP2350 A2"): with the pad input buffer enabled and the pad in the undefined logic region, leakage of about 120 uA holds the pad near 2.2 V; "the pad pull-down (if enabled) is significantly weaker than the leakage current in this state and therefore is not strong enough to pull the pad voltage low"; "The pad pull-up still works"; workaround is an external pull-down of 8.2 kOhm or less, or toggling `IE`. The 2025-07-29 datasheet marks E9 "Fixed by RP2350 A3, Documentation", but Pico 2 modules already in the supply chain may be A2, so cwht must be designed for A2: switches to ground with pull-ups (internal `PUE` plus an external 10 kOhm for RF and ESD robustness), Schmitt trigger enabled, and the keyer logic reading active-low. ADC pins must have `IE` cleared (12.4.3, restated in the E9 workaround).

### F12. Errata and datasheet revision status (High for content, Medium for which stepping cwht will receive)

Local `docs/rp2350-datasheet.pdf`: build-date 2025-02-20, build-version 3184e62-clean, 1369 pages, errata E3..E25. Current online datasheet (https://datasheets.raspberrypi.com/rp2350/rp2350-datasheet.pdf, redirecting to `pip-assets.raspberrypi.com/.../RP-008373-DS-2-rp2350-datasheet.pdf`): build-date 2025-07-29, build-version d126e9e-clean, 1380 pages. Release note for 29 July 2025: "Added hardware revision history (Appendix C), and documented steppings A3 and A4. Added new errata. ... Updated existing errata entries to indicate fix status. Updated register reset values of FREQA.DS0_RANDOM, FREQA.DS1_RANDOM, CLK_SYS_CTRL.SRC, and CLK_SYS_CTRL.AUXSRC to reflect changes in RP2350 A3." New errata E26 (RCP random delays side-channel), E27 (bus priority controls apply to wrong managers), E28 (OTP page 62/63 keys) affect A2, A3 and A4 and are not relevant to cwht functions. E10 (UF2 with partition table) is "Fixed by RP2350 A3 bootrom". E25 (flash segments must be word-sized) is already honoured in `link.ld`.

### F13. Host-side testing with mocked drivers works against `api` as it stands (High)

Proof crate (scratch `mocktest/`, `Cargo.toml` depends on `api = { path = "/Users/robinonsay/rust/rustos/api" }`): a `MockGpio` implementing `api::gpio::Gpio` with `MockIn<N>`/`MockOut<N>` pin types, a `select_element(dit, dah)` function generic over `Read<bool>` (paddle: dit wins, then dah, then none) and a `straight_key(key, tx)` function generic over `Read<bool>` + `Write<bool>`. Handles are created with `unsafe { PinHandle::<10>::new() }`, which the `PinHandle::new` Safety section explicitly permits for host tests.

```
$ cargo test --offline
running 2 tests
test tests::straight_key_follows_key_line ... ok
test tests::paddle_dit_wins_over_dah_and_idle_is_none ... ok
test result: ok. 2 passed; 0 failed
$ cargo build --offline --target thumbv8m.main-none-eabihf     (same crate, #![cfg_attr(not(test), no_std)])
    Finished `dev` profile ... exit=0
```

So the split that cwht needs is available today: portable logic in a `no_std` library crate that depends only on `api`, tested on the host with `std`, and compiled unchanged for the target. What is missing for full keyer testing is a portable time abstraction (an `Instant`/`Clock` trait) so that a simulated clock can drive element timing, mode A/B iambic behaviour and debounce deterministically.

### F14. Pin budget on the Pico 2 fits cwht with margin (Medium)

Pico 2 exposes GPIO0..22 and GPIO26..28 (26 pins) plus on-board 23/24/25/29. Estimated cwht use: I2C SDA/SCL (2, F3), LCD SPI SCK/MOSI/CS/DC/RST (5, F1 + SIO), backlight PWM (1, F4), sidetone PWM (1, F4, on a different slice than the backlight so periods are independent), encoder A/B/push (3, SIO with pull-ups), key jack tip/ring (2, SIO with pull-ups, Schmitt), TX key line (1), TR/PA enable (1), battery ADC (1 of GPIO26..28 via external divider, since 2S Li-ion exceeds VSYS 5.5 V max and ADC 3.3 V), volume ADC (1). Total 19, leaving about 7 spare. GPIO29 (`vsys_adc`, VSYS/3) gives a free regulated-rail reading. ADC_VREF on Pico 2 is a filtered 3V3 rail and is noisy (Pico 2 datasheet 3.5); battery and volume readings should be oversampled and are not precision measurements.

### F15. Configuration storage: bootrom flash API is the right route (High)

Datasheet 5.4.6.1 lists `connect_internal_flash()`, `flash_enter_cmd_xip()`, `flash_exit_xip()`, `flash_flush_cache()`, `flash_range_erase()`, `flash_range_program()` (Arm-S). 5.4.8.10 `flash_range_erase(addr, count, block_size, block_cmd)`: "addr must be aligned to a 4096-byte sector, and count must be a multiple of 4096 bytes ... The QSPI device must be in a serial command state before calling this API, which can be achieved by calling connect_internal_flash() followed by flash_exit_xip(). After the erase, the flash cache should be flushed via flash_flush_cache() ... the original XIP mode should be restored by copying the saved XIP setup function from boot RAM into SRAM, and executing it". 5.4.8.11 `flash_range_program(addr, data, count)`: 256-byte page alignment. Functions are found through `rom_table_lookup` (pointer at ROM 0x16/0x18, codes `'R','E'` and `'R','P'`, 5.4.1). The higher-level `flash_op()` (5.4.6.2) validates alignment and bounds. Because XIP is unavailable between `flash_exit_xip()` and the XIP restore, the calling function must be RAM-resident (`.data.*` section, F8 item 5) and interrupts must be masked (the vector table lives in flash). Pico 2 flash is a Winbond W25Q32RV (4 MB, 4 KiB sectors). Reserve the top two sectors (0x103FE000 and 0x103FF000) by shrinking `FLASH LENGTH` in the application's copy of `link.ld` and use an A/B record scheme with CRC so a power loss during write cannot lose both copies.

### F16. rustos repository hygiene items found in passing (High)

1. README: "three crates" and `demo/` no longer exist in the workspace; `cargo xtest` alias removed; `cargo build --release` at the workspace root no longer produces a flashable image.
2. `api` has no unit tests; `pico2` has 13 clippy warnings and 71 rustfmt hunks.
3. `docs/rp2350-datasheet.pdf` is one revision behind (F12).
4. `docs/icd/rp2350/` covers clocks, GPIO, UART, I2C, SPI only; no ADC, PWM, TIMER, watchdog, PIO or QMI ICD exists yet.
5. The GitHub repository `github.com/robinonsay/rustos` is public (22 commits, default branch master), so the template's git dependencies resolve; cwht should nonetheless depend on rustos by path (per the cwht README) and pin a commit for the baseline.

## Driver extension map for cwht

### How `api` extends

Keep the existing philosophy: one zero-sized `DeviceHandle<T>` per peripheral instance consumed by the driver constructor, one zero-sized `PinHandle<N>` per pad consumed by pin configuration, one `ErrorType` per driver, value-generic `Read<T>`/`Write<T>` for data paths, and new *capability* traits only where `Read`/`Write` cannot express the operation (transactions, time, alarms). Proposed additions, all in `api` (no register facts):

| New `api` item | Shape | Used by |
|---|---|---|
| `time::Instant` (u64 us), `time::Duration`, `time::Clock: ErrorType { fn now(&mut self) -> Result<Instant, _> }` | monotonic microsecond clock | keyer, debounce, UI ticks, timeouts |
| `time::Alarm: ErrorType { fn schedule(&mut self, at: Instant) ; fn cancel() ; fn is_pending() }` | one alarm per value; the driver maps to TIMER0 ALARMn | keyer element timer, UI 100 Hz tick |
| `time::DelayUs` (blocking) | for bring-up sequences (XOSC settle, LCD reset) | drivers |
| `gpio::Gpio::alt_from_handle::<N, F>(handle, PadConfig) -> PinFunc<N, F>` plus `gpio::GpioPinIn` gaining `fn set_schmitt`, and an `EdgeInput<N>: GpioPinIn<N> { fn enable_edge(Edge) ; fn take_event() -> bool }` | function select F1/F3/F4 and pad control; edge-latch reads for encoder | I2C, SPI, PWM pins; encoder, key |
| `bus::I2cMaster: ErrorType { fn write(addr7, &[u8]); fn read(addr7, &mut [u8]); fn write_read(addr7, &[u8], &mut [u8]) }` | blocking with timeout and abort-source decoding in `Error` | Si5351-class synthesizer driver (in cwht-core) |
| `bus::SpiTx: ErrorType { fn write(&[u8]) ; fn flush() }` (optionally `Write<u8>` for single bytes) | TX-only 8-bit mode 0 | LCD driver (in cwht-core), D/C and CS as `GpioPinOut` |
| `pwm::PwmChannel: Write<Duty>` with `fn set_period(Hz)`; `Duty(u16)` | slice/channel derived from `N` at compile time (`const fn slice(N)`) | sidetone, backlight |
| `adc::AdcChannel<const CH: usize>: Read<u16>` | one-shot 12-bit sample; `AdcInput` marker on pins 26..29 | battery, volume |
| `watchdog::Watchdog: ErrorType { fn start(Duration) ; fn feed() ; fn reason() -> ResetReason }` | | SWE-134 provisions for keying and PA enable |
| `nv::NvStore: ErrorType { fn read(&mut [u8]) ; fn write(&[u8]) }` with record CRC handled in cwht-core | | frequency, WPM, keyer mode, sidetone pitch, volume |
| `irq::CriticalSection` (closure-based `with(|cs| ..)`) and `irq::Interrupt` enable/disable tokens | needed by alarm and edge drivers; mock is a no-op on the host | all IRQ users |

`define_board!` extends without change: add `devices { gpio: Rp2350Gpio, clocks: Rp2350Clocks, timer0: Rp2350Timer0, pwm: Rp2350Pwm, adc: Rp2350Adc, i2c0: Rp2350I2c0, spi0: Rp2350Spi0, watchdog: Rp2350Watchdog, flash: Rp2350Flash }`. Two rough edges to fix first: the macro should qualify `core::sync::atomic::Ordering::Acquire` itself, and `BOARD_TAKEN` should be generated per board name.

### Peripheral to driver map

| cwht need | RP2350 block(s) | Datasheet (local pdf page) | Register block names | Preferred mechanism | Fallback |
|---|---|---|---|---|---|
| Synthesizer control (Si5351-class, 7-bit addr, 400 kHz) | I2C0 + IO_BANK0 F3 + PADS (PUE, SCHMITT, SLEWFAST=0) | 12.2 (980), 12.2.10.2 init, 12.2.14 clocking, 12.2.17 regs | `IC_CON, IC_TAR, IC_DATA_CMD, IC_FS_SCL_HCNT/LCNT, IC_FS_SPKLEN, IC_ENABLE, IC_STATUS, IC_TX_ABRT_SOURCE, IC_CLR_TX_ABRT, IC_RAW_INTR_STAT` | polled master with timeout | IRQ-driven (I2C0_IRQ 36) if UI latency demands |
| LCD | SPI0 F1 (SCK, TX), CS/DC/RST as SIO outputs; PWM backlight | 12.3 (1043), 12.3.5 regs; 12.6 DMA optional | `SSPCR0, SSPCR1, SSPCPSR, SSPDR, SSPSR, SSPIMSC, SSPDMACR` | polled TX, 8-bit, mode 0, `SSPSR.BSY` wait | DMA channel for full-frame pushes |
| Battery, volume | ADC ch 0..2 (GPIO26..28), `vsys_adc` ch 3; `clk_adc` 48 MHz from PLL_USB | 12.4 (1063), 12.4.2.1 channels, 12.4.3 SAR, 12.4.7 regs | `CS (EN, AINSEL, START_ONCE, READY), RESULT, FCS, DIV` | one-shot, oversampled x16 | free-running FIFO + DMA |
| Sidetone, backlight | PWM slices (distinct slices) F4 | 12.5 (1073), 12.5.2 model, 12.5.3 regs | `CHn_CSR, CHn_DIV, CHn_TOP, CHn_CC, EN` | sidetone: fixed TOP for 600 to 800 Hz, CC = 50 percent, gate on key; backlight: 1 to 20 kHz, duty from UI | none needed |
| Keyer timing, UI ticks | TIMER0 alarms 0..1 fed by TICKS from XOSC clk_ref; SysTick optional | 12.8 (1179), 8.5 (567), 8.2, 8.6 | `TIMELR/TIMEHR, TIMERAWL, ALARM0..3, ARMED, INTE, INTR`; `TICKS.TIMER0_CTRL/CYCLES` | ALARM0 keyer element timer (IRQ 0), ALARM1 1 kHz sampling tick (IRQ 1) | polling `TIMERAWL` in the main loop |
| Rotary encoder A/B/push; key jack tip/ring (straight key or paddle) | SIO inputs with PUE + SCHMITT (E9); optional IO_BANK0 edge IRQ | 9.5 (591), 9.6 (592), 9.11 regs | `PADS_BANK0.GPIOn`, `IO_BANK0.GPIOn_CTRL`, `INTR0..5`, `PROC0_INTE0..5`, `PROC0_INTS0..5`, `SIO.GPIO_IN` | 1 kHz timer-tick sampling with software debounce and quadrature state machine (deterministic, fully host-testable) | edge IRQ on IO_IRQ_BANK0 (21) for sub-ms key latency; PIO quadrature program deferred (needs a PIO assembler step) |
| Watchdog | WATCHDOG + TICKS.WATCHDOG_* + RESETS.WDSEL/PSM.WDSEL | 12.9 (1190), 7.5 | `CTRL, LOAD, REASON, SCRATCH0..7` | 1 to 2 s timeout fed from the main loop; `REASON` logged at boot | |
| Configuration storage | Bootrom flash API over QMI; RAM-resident caller | 5.4.6.1, 5.4.8.10/11 (376 to 398), 4.4 (340), 12.14 (1223) | ROM table codes `'R','E'` erase, `'R','P'` program, plus `connect_internal_flash`, `flash_exit_xip`, `flash_flush_cache`; XIP restore function from boot RAM | A/B 4 KiB sectors at top of the 4 MB part, CRC32 records | QMI direct mode (12.14.5) only if the bootrom path proves unworkable |
| Interrupt plumbing | NVIC (PPB), vector table in `pico2` | 3.2 (82), 3.7.5 | `NVIC_ISER0, NVIC_ICER0, NVIC_ISPR0, NVIC_IPR0` | `PROVIDE()` overridable handlers in `link.ld`, `cpsid/cpsie` critical section | |
| Clocks | XOSC, PLL_SYS, CLOCKS, TICKS | 8.1 (510), 8.2 (552), 8.6 (572), 8.5 (567) | `XOSC.CTRL/STATUS/STARTUP`, `PLL_SYS.CS/PWR/FBDIV_INT/PRIM`, `CLOCKS.CLK_REF_CTRL, CLK_SYS_CTRL, CLK_PERI_CTRL, CLK_ADC_CTRL`, `TICKS.*` | 12 MHz XOSC, PLL_SYS 150 MHz, clk_ref = XOSC, clk_peri = clk_sys, clk_adc = PLL_USB 48 MHz | run at a lower PLL setting if power budget requires |

### Host-side testing fit

Three crates in `cwht/firmware/`:

1. `cwht-core` (`#![no_std]` library, depends only on `api`): keyer state machine (straight, iambic A, iambic B, WPM, weighting), debounce and quadrature decoder, UI state, frequency plan and band limits (47 CFR 97.301), Si5351 register computation, LCD command sequences, config record codec with CRC, safety interlocks (key-down timeout, PA enable rules). Tested with `cargo test` on the host: mock `Gpio`, mock `Clock`/`Alarm` (simulated time advanced by the test), transaction-recording mock `I2cMaster` and `SpiTx`, in-memory `NvStore`. MC/DC coverage is measured here (SWE-219) and cyclomatic complexity is checked here (SWE-220).
2. `cwht-mock` (host-only library): the mock drivers, a scenario runner, and golden-transaction assertions (for example "tuning to 144.200 MHz emits exactly this Si5351 register sequence").
3. `cwht-fw` (`#![no_std]`, `#![no_main]` binary on `pico2`): board definition via `define_board!`, driver construction, interrupt handlers, main loop. Only integration glue lives here; it is verified by emulation (whole-binary scenarios) and on the bench, not by host unit tests.

`pico2` drivers themselves are register-level and remain untestable on the host unless register access goes through an injectable trait; the cheaper Class A evidence for them is inspection against the datasheet ICD plus emulation, which is the charter's "Emulation" evidence class.

## Work-package table

| WP | Title | Crate(s) | Datasheet | Deliverables | Depends on | Size | Pre-power-on evidence |
|---|---|---|---|---|---|---|---|
| WP-01 | Clock bring-up: XOSC, PLL_SYS 150 MHz, CLOCKS mux, TICKS 1 us, clk_adc 48 MHz | pico2 (`clocks`), api (`time::DelayUs`) | 8.1, 8.2, 8.5, 8.6 | `Rp2350Clocks::new(board.clocks)`; explicit field writes (A3 reset-value change) | none | M | Inspection vs `docs/icd/rp2350/clocks`; emulation clock-tree readback |
| WP-02 | Interrupt plumbing: overridable vectors via `PROVIDE`, NVIC enable/priority, critical section | pico2 (`lib.rs`, `link.ld`, `irq`), api (`irq`) | 3.2, 3.7.5 | 52 named IRQ symbols; `Rp2350Nvic`; `with_cs()` | none | M | Emulation: forced IRQ (`NVIC_ISPR0`) reaches app handler |
| WP-03 | TIMER0 clock and alarms | pico2 (`timer`), api (`time::{Clock,Alarm,Instant}`) | 12.8 | 64-bit `now()`, ALARM0/1 with IRQ 0/1 | WP-01, WP-02 | M | Host: mock clock; emulation: alarm fires at +N us |
| WP-04 | GPIO extension: function select, pad config (SCHMITT, PUE, IE, DRIVE), edge interrupts, E9-safe input policy | pico2 (`gpio`), api (`gpio` additions) | 9.4, 9.5, 9.6, E9 | `alt_from_handle`, `EdgeInput`; `IE` cleared on ADC pins | WP-02 | S/M | Host: mock; inspection of pad bit fields |
| WP-05 | PWM: sidetone and backlight | pico2 (`pwm`), api (`pwm`) | 12.5 | compile-time slice/channel from pin number; period and duty API | WP-01, WP-04 | S | Host: duty math tests; emulation register readback |
| WP-06 | ADC: one-shot channels 0..3, temperature | pico2 (`adc`), api (`adc`) | 12.4 | `Read<u16>` per channel; oversampling helper in core | WP-01, WP-04 | S | Host: scaling math; emulation |
| WP-07 | I2C0 master (DW_apb_i2c) with timeout and abort decoding | pico2 (`i2c`), api (`bus::I2cMaster`) | 12.2 | 100/400 kHz, `write`, `read`, `write_read` | WP-01, WP-04 | M | Host: Si5351 sequence goldens via recorder mock; emulation with a scripted I2C target |
| WP-08 | SPI0 TX master (PL022) for LCD | pico2 (`spi`), api (`bus::SpiTx`) | 12.3 (12.6 optional) | 8-bit mode 0 TX, CS/DC as GPIO | WP-01, WP-04 | M | Host: LCD command goldens; emulation |
| WP-09 | Watchdog | pico2 (`watchdog`), api (`watchdog`) | 12.9, 7.5 | start/feed/reason; boot-reason logging | WP-01 | S | Emulation: starve and observe reset; inspection |
| WP-10 | Non-volatile config via bootrom flash API | pico2 (`flash`, RAM-resident section), api (`nv::NvStore`), core (record codec) | 5.4, 4.4, E25 | A/B sectors reserved in `link.ld`; CRC records | WP-02 | M/L | Host: codec and A/B recovery tests; emulation of erase/program via ROM stubs |
| WP-11 | Input logic: quadrature decoder, debounce, keyer (straight, iambic A/B) | core | none (logic) | pure functions over `Read<bool>` and `Clock` | api time traits (WP-03 shapes) | M | Host: exhaustive state-machine tests, MC/DC 100 percent |
| WP-12 | Test infrastructure: `cwht-mock`, CI gates (`cargo test`, `clippy -D warnings`, `cargo pico2`, `picotool uf2 convert --abs-block`, rustfmt), emulation harness hook | cwht `tools/`, `firmware/` | | scripts and gate definitions | none | M | Inspection |
| WP-13 | rustos hygiene: README drift, clippy 13 warnings, rustfmt, `define_board!` rough edges, datasheet refresh to 2025-07-29, ADC/PWM/TIMER/WDG/QMI ICD extraction | rustos | | PRs to rustos with baseline tag | none | S | Inspection |
| WP-14 | Deferred: PIO quadrature or LCD acceleration; DMA for SPI | pico2 | 11, 12.6 | only if WP-08/WP-11 timing proves insufficient | WP-08, WP-11 | L | |

Suggested order: WP-13 (unblocks a `-D warnings` gate), WP-01, WP-02, WP-03, WP-04, then WP-11 in parallel with WP-05..WP-09, then WP-10, WP-12 continuously.

## Implications for cwht

- **REQ-candidate (SW):** The firmware shall run from the 12 MHz crystal with PLL_SYS and a 1 us TIMER0 tick derived from XOSC before any keyer or bus activity (F10). Verification: Emulation (clock register readback) and Bench (sidetone frequency measured against a known reference).
- **REQ-candidate (SW-KEYER):** Keyer element timing shall be derived from TIMER0 and be accurate to within 1 percent of 1200 ms / WPM over 5 to 40 WPM (F10). Verification: HostUnit with simulated clock; Bench.
- **REQ-candidate (SW-KEYER, from SI-018):** The keyer shall accept a straight key on the tip contact and an iambic paddle on tip (dit) and ring (dah), selectable by a stored mode (straight, iambic A, iambic B), with all timing logic in a host-tested portable crate (F13). Verification: HostUnit, Demonstration.
- **REQ-candidate (CTL/ICD):** Key, paddle and encoder inputs shall be switch-to-ground with internal pull-up enabled, an external pull-up of about 10 kOhm, and Schmitt trigger enabled; no design shall rely on internal pull-downs (F11, RP2350-E9). Verification: Inspection (schematic, pad configuration).
- **REQ-candidate (CTL/ICD):** ADC input pads shall have the digital input buffer disabled (`IE = 0`) whenever sampled (F9 ADC, 12.4.3). Verification: Inspection.
- **REQ-candidate (SW):** Non-volatile configuration shall be stored in two dedicated 4 KiB flash sectors at the top of the 4 MB device using CRC-protected A/B records, written only by RAM-resident code with interrupts masked (F15). Verification: HostUnit (codec, recovery), Emulation.
- **REQ-candidate (SW):** A watchdog of at most 2 s shall be enabled before the transmitter can be keyed, and the reset reason shall be recorded (F9 watchdog; SWE-134). Verification: Emulation, Bench.
- **REQ-candidate (VER):** Release images shall be produced by `picotool uf2 convert <elf> <uf2> --family rp2350-arm-s --abs-block` and the UF2 metadata checked with `picotool info -a` as part of the version description (F5). Verification: Inspection.
- **RISK-candidate:** `pico2` has no interrupt or clock infrastructure; every cwht driver depends on WP-01/WP-02 landing first. Schedule risk, likelihood medium, consequence high (nothing else can be emulated end to end until then).
- **RISK-candidate:** Silicon stepping of procured Pico 2 modules is unknown (A2 vs A3/A4); E9 and E10 behaviours differ. Mitigated by designing for A2 (pull-ups, `--abs-block`); residual risk low.
- **RISK-candidate:** ADC reference on Pico 2 is a filtered 3V3 rail (noisy) and the 2S battery needs an external divider; battery gauge accuracy is limited to roughly 2 percent without calibration. Likelihood high, consequence low (display only).
- **RISK-candidate:** `pico2` register-level drivers cannot be unit-tested on the host without a register-access abstraction; Class A evidence for them rests on inspection plus emulation. Decide early whether an emulator with RP2350 peripheral models is available (separate research assignment).
- **RISK-candidate:** rustos README and tree have drifted (F16); a reviewer following the README will not reproduce the build. Low consequence, fix in WP-13.
- **DECISION-needed:** Encoder and key input mechanism: 1 kHz timer-sampled polling (recommended, fully host-testable, no PIO toolchain) versus IO_BANK0 edge interrupts versus PIO. Recommend polling for rev A with edge IRQ reserved for key-down latency if bench tests show more than 1 ms.
- **DECISION-needed:** Single-core only for cwht firmware (recommended for Class A simplicity; core 1 left in its bootrom wait state) versus using core 1 for UI.
- **DECISION-needed:** Where new drivers live: extend rustos `pico2` upstream (keeps one HAL, benefits Juno) versus a cwht-local `pico2-ext` crate. Recommend upstream via reviewed PRs with a pinned commit in cwht.
- **DECISION-needed:** Whether `pico2` drivers adopt an injectable register-access trait to enable host tests, at the cost of departing from the current raw-pointer style.
- **ACTION:** Refresh `rustos/docs/rp2350-datasheet.pdf` to build 2025-07-29 (RP-008373-DS-2) and extract ADC, PWM, TIMER, TICKS, WATCHDOG, QMI and bootrom-API ICDs in the same style as `docs/icd/rp2350/`.
- **ACTION:** Add the CI gate set from WP-12 to cwht `tools/` and run it against the pinned rustos commit at SRR.
- **ACTION:** Record the toolchain baseline in the SEMP: rustc 1.98.0 stable, target `thumbv8m.main-none-eabihf` (Tier 3), picotool 2.3.0 (upgrade to 2.3.1 optional), poppler pdftotext for ICD extraction.

## Confidence

| Finding | Confidence | Basis |
|---|---|---|
| F1, F2, F3, F4, F5, F6 | High | commands executed in this session, outputs quoted |
| F7, F8 | High | source read in full; gaps are absences, not interpretations |
| F9 | High | extracted from datasheet register lists and address map; offsets quoted verbatim |
| F10 | High | datasheet 8.5 and 12.8 text quoted |
| F11 | High for A2 behaviour; Medium for which stepping cwht will receive | datasheet errata text; stepping of future purchases unknown |
| F12 | High | both PDFs read locally (colophon build dates) |
| F13 | High | proof crate built and tests run |
| F14 | Medium | pin count is an estimate pending the hardware architecture |
| F15 | High for the API contract; Medium for the RAM-resident and A/B implementation details | datasheet 5.4.8 text; implementation pattern from the pico-sdk approach, not yet prototyped in Rust |
| F16 | High | observed directly |

## Open items

1. Which RP2350 stepping (A2, A3, A4) will PCBWay-sourced Pico 2 modules carry in 2026? Affects only E9/E10 margins; design assumes A2.
2. Is an RP2350 emulator with peripheral models (TIMER, I2C, SPI, PWM, ADC, GPIO) available for the "Emulation" evidence class? Out of this assignment's scope; the driver map assumes one exists or will be selected separately.
3. Si5351-class synthesizer choice and its exact I2C timing (100 vs 400 kHz, clock-stretching) come from the synthesizer research assignment; WP-07 sizing assumes a standard 7-bit, 400 kHz, no-stretch device.
4. LCD controller and interface (SPI mode, bit width, D/C line) come from the display research assignment; WP-08 assumes 8-bit mode 0 TX-only.
5. Whether the rustos owner accepts upstream additions to `api` (time, bus, pwm, adc, watchdog, nv, irq traits) and to `pico2` (vector overrides, clocks) or prefers a cwht-local extension crate (DECISION-needed above).
6. The `rustos_demo` runner (`picotool load -u -x -t elf`) and BOOTSEL flashing were not exercised (no board attached, and flashing was out of scope); first bench flash of a cwht image is a TRR item.
7. Proof crates live only in the session scratch directory; if the SRR package needs them as artifacts, copy `mocktest/` and `demo_build/` into `cwht/tools/proofs/` under a follow-up action.

## Sources

- rustos sources: `/Users/robinonsay/rust/rustos/{Cargo.toml,.cargo/config.toml,README.md,api/src/**,firmware/pico2/src/**,firmware/pico2/link.ld,templates/**,docs/icd/rp2350/**}`; demo application `/Users/robinonsay/rust/rustos_demo/`.
- RP2350 datasheet, local copy build 2025-02-20 (`/Users/robinonsay/rust/rustos/docs/rp2350-datasheet.pdf`): sections 2.2, 3.2, 3.7.5, 5.4, 8.1, 8.2, 8.5, 8.6, 9.4 to 9.6, 9.11, 11.7, 12.2 to 12.5, 12.8, 12.9, 12.14, Appendix E (E9, E10, E25).
- RP2350 datasheet, current online build 2025-07-29: https://datasheets.raspberrypi.com/rp2350/rp2350-datasheet.pdf (redirects to https://pip-assets.raspberrypi.com/categories/1214-rp2350/documents/RP-008373-DS-2-rp2350-datasheet.pdf); Raspberry Pi silicon documentation page https://www.raspberrypi.com/documentation/microcontrollers/silicon.html.
- Pico 2 datasheet (`/Users/robinonsay/rust/rustos/docs/pico-2-datasheet.pdf`, extracted md): flash W25Q32RV, crystal ABM8-272-T3, ADC_VREF filtering, GPIO29 = VSYS/3.
- Rust platform support: https://doc.rust-lang.org/nightly/rustc/platform-support.html (thumbv8m.main-none-eabihf, Tier 3).
- picotool: https://github.com/raspberrypi/picotool/releases (2.3.1, 2026-09-05); local `picotool help uf2 convert`.
- rustos on GitHub: https://github.com/robinonsay/rustos (public, master).
- cwht process charter: `/Users/robinonsay/rust/cwht/docs/process/00-charter.md` sections 1, 9, 11; stakeholder inputs `/Users/robinonsay/rust/cwht/docs/requirements/l0-stakeholder/stakeholder-inputs.md` (SI-018).
