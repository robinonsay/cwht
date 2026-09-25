# rp2350js accreditation: timing error, timer IRQ proof, peripheral coverage and the SWE-136 case

Research note, assignment key `emulator-accredit`. Date of work: 2026-09-25. Extends `rp2350-emulation-options.md` (assignment `emulation`, same date); it does not repeat that report's survey. All emulator behaviour below was measured hands-on on this Mac against the pinned commit named there. Test sources (Rust firmware, TypeScript harness, register probes) are preserved under `docs/research/emulator-accreditation-assets/` so the results can be reproduced after `/private/tmp` is cleared.

## Question

For c1570/rp2350js at commit `af0114cbee8e9e91574204b66f10aa2961cbf28c` running in ARM (Cortex-M33) mode:

1. What is the emulator's timing error for three known sequences (a spin loop, a TIMER0 counter delta across 10 ms, a PWM period), as an error band against the hardware reference?
2. Do TIMER0 alarm interrupts work on the ARM path for a minimal rustos-style `thumbv8m` firmware (IRQ handler toggling a GPIO), and does the polled fallback work? If not, what is the minimal reproduction and the upstream issue text?
3. Which peripherals of the rustos driver work packages (clocks, TIMER0, PWM slices 0 to 11, ADC, I2C0, SPI0, watchdog, flash API, GPIO IRQ, USB) does the model cover, with a one-line test and pass/fail per row?
4. What is the accreditation case (NPR 7150.2D SWE-136, "validate and accredit the software tool(s) required to develop or maintain software", `docs/references/md/npr-7150-2d/04-chapter4.md` 4.4.8): pinned identity, environment, lockfile hash, known answers (blinky toggle count, UART echo), and where the vendored copy lives?

## Method

1. Read `rp2350-emulation-options.md` in full, charter section 11, the rustos `pico2` crate (`firmware/pico2/link.ld`, `src/lib.rs`, `src/gpio/gpio.rs`, `templates/pico2/.cargo/config.toml`, read-only) and the RP2350 datasheet extract at `/Users/robinonsay/rust/rustos/docs/extracted/rp2350-datasheet.md` (register offsets and bit fields cited below by section or register name; that file is a text extraction of the Raspberry Pi RP2350 datasheet, build 2025, kept in the owner's rustos repository).
2. Fresh clone into a scratch directory and reproduction of the prior blinky run:

```
mkdir -p /private/tmp/cwht-emu-accredit && cd /private/tmp/cwht-emu-accredit
git clone -q https://github.com/c1570/rp2350js.git
cd rp2350js && git checkout -q af0114cbee8e9e91574204b66f10aa2961cbf28c
git log -1 --format='%H %ci'        # af0114cbee8e9e91574204b66f10aa2961cbf28c 2026-09-10 18:07:31 +0200
npm ci --no-audit --no-fund          # "added 428 packages in 2s"; husky hook install; nothing global
shasum -a 256 package-lock.json package.json
#   dd88d3100bd97acdcaa3daa3c2c931590938cd5a42d72e2daf7978d684f24e05  package-lock.json
#   db353ce35c433683da45d70a02d07b6655d073f26ce79c1df8e132ae53b6fdbe  package.json
node --version && npm --version && npx tsc --version && npx ts-node --version
#   v25.9.0 / 11.12.1 / Version 5.9.3 / v10.9.2
cp <assets>/harness/cwht-accredit.ts demo/            # harness (source in this report's assets folder)
npx ts-node demo/cwht-accredit.ts /Users/robinonsay/rust/rustos/blinky.uf2 100000000 none
```

3. Wrote a standalone `no_std` Rust crate (`emutest`, 14 binaries) for `thumbv8m.main-none-eabihf` in `/private/tmp/cwht-emu-accredit/fw`. `link.ld` is a byte-identical copy of rustos `firmware/pico2/link.ld` (sha256 `4be4e6e0e5bf4e6f852e605df72af0af5533f81b20de4f1447a63d52f6c169d4` for both files); `src/rt.rs` reproduces rustos's approach (five-word `IMAGE_DEF` in `.boot_info`, 68-entry `Vector` union table in `.vector_table`, `OnReset` doing CPACR, VTOR, `.data`, `.bss`) and adds handler slots for IRQ 0 (TIMER0_IRQ_0), 8 (PWM_IRQ_WRAP_0), 21 (IO_IRQ_BANK0) and 33 (UART0_IRQ), register helpers, UART0 text output, TIMER0/TICKS setup, SysTick, NVIC and a `subs r0,#1; bne` spin loop in inline asm. rustos itself was not modified (only read) and its `blinky.uf2` was used unchanged as the known-answer image. Build and convert:

```
cd /private/tmp/cwht-emu-accredit/fw
cargo build --release                       # rustc 1.98.0 (88d9e12ae 2026-08-18), cargo 1.98.0, target from .cargo/config.toml
for b in spin timer10ms pwm alarm_irq alarm_poll uart_echo gpio_irq i2c0 spi0 adc watchdog flash_qmi usb clocks; do
  picotool uf2 convert -t elf target/thumbv8m.main-none-eabihf/release/$b out/$b.uf2 --family rp2350-arm-s
done                                        # picotool v2.3.0; every image: family rp2350-arm-s, IMAGE_DEF at 0x10000110
rust-objdump -d --triple=thumbv8m.main-none-eabihf target/thumbv8m.main-none-eabihf/release/spin | grep -A5 'rt4spin>:'
#   10000c04: 3801  subs r0, #0x1
#   10000c06: d1fd  bne  0x10000c04        (Thumb-16, the intended two-instruction loop)
```

4. Ran each image through the harness (`demo/cwht-accredit.ts`: records UART0 bytes with cycle stamps, Low/High transitions on GPIO 25/24/23 with `mcu.cycles` and `mcu.clock.nanos`, per-phase interval statistics, scenario stimuli and hooks, stop on the firmware's `DONE` line):

```
cd /private/tmp/cwht-emu-accredit/rp2350js
npx ts-node demo/cwht-accredit.ts ../fw/out/spin.uf2       60000000 none
npx ts-node demo/cwht-accredit.ts ../fw/out/timer10ms.uf2  30000000 none
npx ts-node demo/cwht-accredit.ts ../fw/out/pwm.uf2        30000000 none
npx ts-node demo/cwht-accredit.ts ../fw/out/alarm_irq.uf2  30000000 none
npx ts-node demo/cwht-accredit.ts ../fw/out/alarm_poll.uf2 30000000 none
npx ts-node demo/cwht-accredit.ts ../fw/out/uart_echo.uf2   8000000 uart-echo
npx ts-node demo/cwht-accredit.ts ../fw/out/gpio_irq.uf2   70000000 gpio-irq
npx ts-node demo/cwht-accredit.ts ../fw/out/i2c0.uf2        8000000 i2c
npx ts-node demo/cwht-accredit.ts ../fw/out/spi0.uf2        8000000 spi
npx ts-node demo/cwht-accredit.ts ../fw/out/adc.uf2         8000000 adc
npx ts-node demo/cwht-accredit.ts ../fw/out/watchdog.uf2   12000000 watchdog
npx ts-node demo/cwht-accredit.ts ../fw/out/flash_qmi.uf2   8000000 none
npx ts-node demo/cwht-accredit.ts ../fw/out/usb.uf2         8000000 usb
npx ts-node demo/cwht-accredit.ts ../fw/out/clocks.uf2     30000000 none
npx ts-node demo/cwht-accredit.ts demo/m33_blink/blink_simple.uf2 300000000 stall-diag   # the F14 image
npx ts-node demo/cwht-accredit.ts demo/m33_blink/blink_simple.uf2 300000000 allpins
npx ts-node demo/cwht-regprobe.ts                                                        # register-level defect repros
npx ts-node demo/cwht-gpioc-probe.ts                                                     # GPIO coprocessor repro
```

5. Cross-checked every anomaly against the emulator source (`src/peripherals/*.ts`, `src/cortex-m33/*.ts`, `src/clock/simulation-clock.ts`, `src/utils/timer32.ts`) and against the datasheet register tables, and checked the upstream tracker (`curl https://api.github.com/repos/c1570/rp2350js/issues?state=all`: one closed PR, zero issues; repository 7 stars, 2 forks, last push 2026-09-10).

Everything ran headless from the command line; no packages were installed globally; nothing outside `/private/tmp` and `docs/research/` was written.

## Findings

### F1. Reproduction of the prior run, and a correction to its timing remark

The fresh clone at the pinned commit reproduces the earlier blinky result exactly. `rustos/blinky.uf2` (sha256 `7e03c238649a1a038f988c58c0e716e6e46207acb3ca63ee2d4d90eb1d4332d9`, `picotool info`: family `rp2350-arm-s`, IMAGE_DEF at `0x10000110`) produces its first GPIO25 Low to High transition at cycle 35132 and then alternates every 5,234,377 (high) and 5,234,378 (low) cycles: 20 transitions in 100,000,000 cycles (800.000 ms of emulated time), wall 1.47 to 1.52 s, 65.8 to 68.0 Mcycles/s. The only emulator warnings are the bootrom's writes to `IO_QSPI_BASE` and `XIP_QMI_BASE`, which are non-fatal.

`rust-objdump -d` of `blinky.elf` shows why the earlier report's "1.05 cycles per iteration is not credible" remark was wrong: rustc unrolled `for _ in 0..5_000_000 { spin_loop() }` into 78,125 iterations of 64 `yield` hints plus `subs r3,#0x40` and `bne`. At the emulator's costs (hint 1, `subs` 1, taken branch 2) that is 67 cycles per iteration, 78,125 x 67 = 5,234,375 cycles, matching the measured half period to within the two store instructions. The emulated cycle count is therefore internally consistent with a plausible Cortex-M33 model; what is not trustworthy is the conversion from cycles to seconds (F5). Sources: `rust-objdump -d --triple=thumbv8m.main-none-eabihf /Users/robinonsay/rust/rustos/blinky.elf`; `src/cortex-m33/execute-thumb16.ts` (`deltaCycles = 1` base, `deltaCycles++` on taken B). Confidence: High.

### F2. Timing test 1: spin loop `subs r0,#1; bne` (image `spin.uf2`)

GPIO25 edges bracket each run; TIMER0 `TIMERAWL` is read before and after.

| n iterations | emulated cycles between edges | cycles per iteration | TIMER0 delta |
|---|---|---|---|
| 1,000 | 3,031 | 3.000 (+31 fixed overhead) | (not printed) |
| 10,000 | 30,031 | 3.000 | (not printed) |
| 100,000 | 300,031 | 3.000 | 2,400 us |
| 1,000,000 | 3,000,031 | 3.000 | 24,000 us |

The emulator charges exactly 3 cycles per iteration (1 for `subs`, 1 + 1 for the taken `bne`), with zero variance, and TIMER0 advances 1 us per 125 cycles exactly. Hardware reference: Arm publishes no per-instruction cycle table for the Cortex-M33 (checked `arm_cortex_m33_trm_100230_08_en.md` and `arm_cortex_m33_dgug_100235_06_en.md` in the rustos extract; neither has one). The Cortex-M3/M4 TRM figure for a taken branch is 1 + P with P = 1 to 3 pipeline-refill cycles, giving 3 to 5 cycles per iteration on a 3-stage core; XIP fetch stalls add to that when the loop is not in the QMI cache. Error band for tight loops: emulator is at the fast edge, 0 % to about -40 % (Low confidence until a bench measurement on the Pico 2; see Open item 1). Confidence: High (emulator side), Low (hardware side).

The SysTick part of this test returned 0 because the RP2350 model's SysTick is unreachable at the architected addresses (F9); all cycle figures above come from the harness's `mcu.cycles` stamps instead.

### F3. Timing test 2: TIMER0 counter delta across 10 ms (image `timer10ms.uf2`)

Five consecutive busy-polls of `TIMERAWL` until 10,000 us elapsed: each reported `us=10000`; GPIO25 edge intervals were 1,250,623 to 1,250,629 cycles (10,000 us plus about 620 cycles of UART printing), and the polling loop ran 166,656 to 166,664 iterations per 10 ms, i.e. 7.50 cycles per `ldr` (APB read +3) / `subs` / `cmp` / `blo` iteration. 10,000 us corresponds to exactly 1,250,000 cycles, so the emulator's effective `clk_sys` is 125.000 MHz (F5). RP2350-only TIMER registers `LOCKED` (0x34) and `SOURCE` (0x38) are unimplemented (reads return 0xffffffff with a warning), and the TICKS block is unimplemented (`TIMER0_CTRL` at TICKS 0x18 and `TIMER0_CYCLES` at 0x1c are logged as unimplemented writes), yet TIMER0 counts anyway. On silicon TIMER0 only counts once `TICKS.TIMER0_CTRL.ENABLE` is set (reset value 0x0) with `TIMER0_CYCLES` chosen for clk_ref (datasheet 8.5 and 12.8.1.1: "the tick source for each timer comes from the system-level tick generators"). Firmware that forgets the tick generator passes in the emulator and has a dead timer on hardware. Confidence: High.

### F4. Timing test 3: PWM period on GPIO25, slice 4 channel B (image `pwm.uf2`)

| Phase | Configuration | Edges | Period (cycles) | High / low (cycles) |
|---|---|---|---|---|
| 1 | DIV 1.0, TOP 999, CC_B 500, CSR.EN=1 | 4,998 intervals | 1000.00 mean | 500.00 / 500.00 (each 497 to 501) |
| 2 | DIV 10.5 (INT 10, FRAC 8), TOP 149, CC_B 75 | 3,174 | 1575.00 mean | 788.00 / 787.00 (784 to 791) |
| 3 | RP2350 `EN` register 0x0f0 written to enable slice 4 | 2,500 | 1000.00 | see F10 (the slice was running for the wrong reason) |
| 4 | Wrap IRQ via RP2350 `IRQ0_INTE` 0x0f8 + NVIC IRQ 8 | 2,499 | 1000.00 | handler count 0 (F10) |

The period equals (TOP + 1) x DIV exactly on average, and the fractional divider is applied as a uniform 10.5 prescale (the `Timer32` model divides nanoseconds), not as the silicon's first-order sigma-delta that alternates 10 and 11 cycle steps (datasheet CHn_DIV description). The +/-3 cycle spread on individual edges is a measurement artefact: alarms fire inside `clock.tick()` after an instruction completes, so edge stamps are quantized to instruction boundaries. In seconds the period is 8.000 us at the emulator's 125 MHz where 150 MHz silicon gives 6.667 us (F5). Confidence: High.

### F5. Clock model: cycles are consistent, seconds are not (all images)

- `RP2350.clkSys = 125 * MHz` and `clkPeri = 125 * MHz` are constants (`src/rp2350.ts` line 156 to 157); `stepThings()` advances the simulation clock by `1e9 / clkSys` ns per cycle (8.000 ns). Every peripheral time base (TIMER, PWM, SysTick, ADC sample time, watchdog) derives from that clock.
- The PLL model computes `foutpostdiv` (logged `150000000` for REFDIV 1, FBDIV 125, POSTDIV 5 and 2) but nothing reads it: after the `clocks.uf2` image "switched" clk_sys to the PLL (`CLK_SYS_SELECTED` read back 2), 10 ms of TIMER0 still took 1,250,198 cycles. `PLL PWR` writes are unimplemented; `CS.LOCK` always reads 1.
- XOSC is an `UnimplementedPeripheral`: `STATUS` reads 0xffffffff, so `STABLE` appears set after zero polls (`XOSC stable=1 polls=0 status=4294967295`). Firmware waiting for the crystal never waits.
- Silicon boots on the ROSC at a nominal 11 MHz (datasheet 8.1 and 8.3 text: "During boot, the ROSC runs at a nominal 11MHz, but varies with PVT"; XOSC "is disabled on chip startup") and reaches 150 MHz only after firmware programs XOSC, PLL_SYS and CLOCKS.

Error band for cycle-to-time conversion, ARM mode, this commit:

| Quantity | Emulator | Hardware reference | Error | Confidence |
|---|---|---|---|---|
| clk_sys before clock setup | 125.000 MHz fixed | ROSC about 11 MHz nominal, PVT dependent | emulator about 11x fast | High |
| clk_sys after PLL to 150 MHz | 125.000 MHz fixed | 150 MHz | -16.7 % cycles per us; cycle-counted delays read 20 % long in emulated microseconds | High |
| TIMER0 tick | 1 us per 125 cycles, exact, independent of TICKS | 1 us only after TICKS.TIMER0 enabled from clk_ref | exact where hardware is configured; counts where hardware would not | High |
| TIMER alarm fire time | in (target - 1 us, target] | at the target microsecond boundary | -1 us to 0 per alarm; measured -0.5 to -0.9 us mean over 30 alarms (F6) | High |
| Exception entry | 12 cycles fixed (`core.ts`) | Cortex-M33: 12 cycles, zero wait state (Arm product data) | about 0 | Medium |
| APB register access | +3 read, +4 write (`cyclesIO`) | not verified on RP2350 | unverified | Low |
| PWM period | (TOP+1) x DIV exact on average | same | 0 % on average; sigma-delta jitter pattern absent | High |
| I2C / SPI transfer time | about 0 (2 I2C bytes: start at cycle 35361, stop at 35365) | 2 bytes at 400 kHz about 50 us; 8 SPI bits at 75 MHz 0.1 us | -100 % | High |
| Watchdog LOAD units | 2 MHz tick (RP2040-E1 constant kept for RP2350) | 1 us tick | fires 2x early: LOAD 10000 fired at 5285 us | High |

Rule for cwht (already stated in the prior report, now quantified): use the emulator for event ordering and register-level logic, never for durations; where a scenario must reason about time, express it in TIMER0 microseconds (exact in the model) and never in instruction counts.

### F6. TIMER0 ALARM0 interrupts work on the ARM path; the polled fallback works too

`alarm_irq.uf2`: `INTE` bit 0 set, NVIC ISER0 bit 0 set, `ALARM0 = TIMERAWL + 1000`; the handler clears `INTR` bit 0, toggles GPIO25, increments a counter and re-arms +1000 us. Main waited three ways: busy loop for alarms 1 to 10 (`A count=10 us=9995`), `wfi` for 11 to 20 (`B count=20 us=19987`), `wfe` for 21 to 30 (`C count=30 us=29980`), then `DONE`. Thirty GPIO25 transitions at 124,904 to 124,917 cycles apart (mean 124,907.73 cycles = 999.26 us at 125 MHz). `ARMED` read 1 (re-armed) and `INTS` 0 at the end. Exception entry, `EXC_RETURN` via `bx lr`, WFI and WFE wake-up all behaved.

`alarm_poll.uf2` (no NVIC): 30 alarms, `ARMED` bit 0 seen set before each fire and clear after each fire (`armed_seen=30 cleared_seen=30`), `INTR` write-1-to-clear worked, 29,974 us total.

Two details matter for accreditation:

- The alarm fires early by up to 1 us. `src/peripherals/timer.ts` computes `deltaMicros = (value - nanos/1000) >>> 0`, truncating the fractional microsecond of "now" before scheduling; the probe confirms that `ALARM0 = 1000` armed at 0.7 us fires at 999,700 ns. Silicon fires when the 1 MHz counter equals the target, i.e. at or after 1,000,000 ns. Hence 10 alarms of 1000 us summed to 9,995 us, 30 to 29,980 us.
- NVIC priority writes did not take: `IPR0` written at 0xE000E400 read back 0xff (unimplemented, F9), so every external IRQ runs at priority 0 in the model. Preemption ordering between cwht IRQs (keyer timer above display SPI, for example) cannot be verified in this emulator until that is fixed.

The README's "Missing: Timer and System Interrupts" line is stale for the ARM path; `src/cortex-m33/exceptions.spec.ts` in the same commit tests NVIC entry and return. Confidence: High.

### F7. Root cause of the prior F14 (pico-sdk `blink_simple` "stalls in `sleep_ms`"): the GPIO coprocessor, not timers

The `stall-diag` run of `demo/m33_blink/blink_simple.uf2` (sha256 `85b02f979beeecf3b46938fcd4e255362004bd3217c21d9f72448fd3be1fc3f9`) after 300,000,000 cycles shows `pc=0x10000aa4 waiting=true primask=0 ipsr=0 nvicEnabled=0x8` and `TIMER0 rawl=2400000 alarm3=2500324 armed=8 inte=8`: the core is legitimately parked in `wfe` inside `sleep_ms`, the alarm-pool alarm (TIMER0 alarm 3, IRQ 3) is armed 100 ms ahead, and its target has advanced through nine 250 ms sleeps, so the SDK's timer interrupt and wake-up path is working. The `allpins` run shows GPIO25 never leaves `InputPullDown`.

The disassembly explains it: pico-sdk builds for RP2350 default to `PICO_USE_GPIO_COPROCESSOR 1` (`raspberry-pi-pico-c-sdk.md` extract, build-configuration table) so `gpio_put()` compiles to `gpioc_bit_out_put`, and `main` contains `ec45 3044 gpioc_bit_oe_put r3, r5` and `ec45 4040 gpioc_bit_out_put r4, r5`. These are MCRR encodings (datasheet 3.6.1.3: `gpioc_bit_out_put = mcrr p0, #4, Rt, Rt2, c0`). In `src/cortex-m33/coprocessor.ts`, `isMrcMcr()` requires `hw0[15:12] == 0xE/0xF` and `hw1[4] == 1`; the MCRR halfwords (`0xEC45`, `0x3044`) fail that test and the instruction is treated as CDP, a NOP. Executing the exact halfwords in SRAM with CP0 enabled in CPACR (`cwht-gpioc-probe.ts`) leaves `GPIO_OE` and `GPIO_OUT` at 0, while plain SIO stores set them.

The single-register forms are also decoded differently from the datasheet: 3.6.1 uses opc1 as the operation (0 put, 1 xor, 2 set, 3 clr, 5/6/7 bit xor/set/clr) and CRm as the bank (c0 lo out, c1 hi out, c4 lo oe, c5 hi oe); the emulator uses opc1 as the bank and opc2 as the operation. Probe results with datasheet encodings: `gpioc_lo_out_put` (opc1 0, c0) works by coincidence; `gpioc_lo_out_set`, `gpioc_lo_oe_set` and `gpioc_bit_out_xor` are silent NOPs. Any RP2350 firmware that drives pins through GPIOC (all pico-sdk GPIO writes by default; possibly future Rust HALs) shows no pin activity in this emulator while everything else runs normally. rustos drives pins by SIO stores (`Rp2350GpioOut::write` writes `gpio_out_set`/`gpio_out_clr`) and is unaffected. The prior report's F14 attribution ("SDK-style alarm-IRQ sleeps ... not yet usable on the ARM path") is withdrawn. Confidence: High.

### F8. GPIO edge interrupts do not fire: the RP2350 IO_BANK0 interrupt registers are mis-decoded

`gpio_irq.uf2` configured GPIO2 as an input with pull-up, wrote `PROC0_INTE0` (IO_BANK0 + 0x248) = 0x400 (GPIO2 `EDGE_LOW`, nibble bits per datasheet Table for PROC0_INTE0), enabled NVIC IRQ 21, and the harness drove GPIO2 high then low five times. Result: `gpio-irq FAIL: 0 handler toggles for 5 falling edges`. The register probe shows the cause: after writing 0x400 to 0x40028248 the read-back is 0 and `gpio[2].irqEnableMask` stays 0; after a falling edge `gpio[2].irqStatus` is 0x5 (edge-low and level-low latched inside the pin object) but `INTR0` and `PROC0_INTS0` read 0 and no NVIC bit pends.

`src/peripherals/io_rp2350.ts` computes `register = (offset % 0x18) * 0x18` and compares it with the absolute constants `INTR0 = 0x230`, `PROC0_INTE0 = 0x248`, `PROC0_INTF0 = 0x260`, `PROC0_INTS0 = 0x278`. For every one of those offsets `offset % 0x18` is 8, so `register` is always 192 and matches no case; reads fall through to 0 and writes are dropped. (The offsets themselves match the datasheet IO_BANK0 register list: INTR0 0x230, PROC0_INTE0 0x248, PROC0_INTF0 0x260, PROC0_INTS0 0x278.) Because cwht's straight key and paddle inputs are the obvious GPIO IRQ users, this is the single most important defect for the project. Reading the pin level by polling `SIO.GPIO_IN` works (`gpio2_in=1` after the harness drove it high). Confidence: High.

### F9. Cortex-M33 private peripheral bus: SysTick and NVIC priority registers are at the wrong offsets

`src/peripherals/ppb_rp2350.ts` defines `SYSTICK_BASE = 0xe010` and then `SYST_CSR = 0x010`, `SYST_RVR = 0x014`, `SYST_CVR = 0x018`, comparing against `SYSTICK_BASE + SYST_CSR` = 0xE020 and so on; the architected addresses are 0xE000E010/14/18/1C (Armv8-M ARM, datasheet 3.7.5 register list). The probe writes to 0xE000E010 log "Unimplemented peripheral write via 0" and read back 0xffffffff, while the same writes at 0xE000E020 succeed (`CSR` reads 0x5). Likewise `NVIC_IPR0 = 0x400` is added to `NVIC_BASE = 0xE100`, giving 0xE500 instead of 0xE400 (datasheet 3.7.5: `0x0e400 NVIC_IPR0`): a write to 0xE000E400 is dropped (`nvicPriority[0]` stays 0), a write to 0xE000E500 sets it to 8. The SDK's `irq_set_priority` writes seen in the F14 image (`0xe414 .. 0xe430`) were hitting this. Consequences: no SysTick-based timing in ARM mode, and no IRQ priority model at all (all IRQs effectively priority 0, no preemption ordering). The SysTick model also always counts `clkSys` regardless of `CLKSOURCE`, whereas silicon's external reference is the 1 us tick (datasheet 8.5.1). Confidence: High.

### F10. PWM: eight slices with the RP2040 register map; slices 8 to 11 alias onto control registers; a DIV write restarts a disabled slice

`src/peripherals/pwm.ts` (inherited from rp2040js) instantiates 8 `PWMChannel`s and places `EN` at 0x0a0, `INTR` 0x0a4, `INTE` 0x0a8, `INTF` 0x0ac, `INTS` 0x0b0. On RP2350 those offsets are `CH8_CSR`, `CH8_DIV`, `CH8_CTR`, `CH8_CC` and `CH8_TOP`; the real `EN` is at 0x0f0, `INTR` 0x0f4, `IRQ0_INTE` 0x0f8, `IRQ0_INTF` 0x0fc, `IRQ0_INTS` 0x100, `IRQ1_*` 0x104 to 0x10c (datasheet PWM register list). Measured: `EN` (0x0f0) and `IRQ0_INTE` (0x0f8) writes are unimplemented and read 0xffffffff; the wrap IRQ never reached the handler (`PWM4 wraps=0`); `CH8_DIV` written 0x10 read back 0 (it cleared the model's raw interrupt bits instead) and `CH8_TOP` written 0x1234 read back 0. Worse, a write to `CH8_CSR` with EN set would be interpreted as the mass-enable register and start slice 0.

A second defect showed in phase 3: slice 4 kept toggling at the new period after `CSR.EN = 0` because `Timer32`'s `prescaler` setter (`src/utils/timer32.ts`) executes `this.enabled = this.prescalerValue !== 0` and re-enables the counter on any DIV write. Probe: `timer.enable` false after disable, true after a DIV write. On silicon a disabled slice stays disabled. Per-slice CSR/DIV/CTR/CC/TOP behaviour and output waveforms for slices 0 to 7 are otherwise correct (F4). Confidence: High.

### F11. Remaining peripheral results

- UART0 (`uart_echo.uf2`, scenario `uart-echo`): PASS. Banner `uart_echo: ready` at cycle 35391; 16 bytes `CQ CQ DE W1AW K\n` fed via `mcu.uart[0].feedByte()` from cycle 5,000,000 at 2,000-cycle spacing were echoed byte-exact and the newline produced exactly one GPIO25 transition (cycle 5,030,024). The model ignores baud and has no TX FIFO timing (`TXFF` is never set), so UART throughput is infinite; RX FIFO, `RXFE`, and `UARTEN/TXE/RXE` behave.
- I2C0 (`i2c0.uf2`, scenario `i2c`, Si5351-style target 0x60): PASS. Hooks saw start, connect addr 0x60 write, bytes 0x03 and 0xff, stop; then start, connect, write 0x00, read with NACK, stop; firmware read back the injected 0x42 and `IC_TX_ABRT_SOURCE` stayed 0. `IC_FS_SPKLEN` (0xa0) is unimplemented (harmless warning). Zero bus time (F5).
- SPI0 (`spi0.uf2`, scenario `spi`, 8-bit Motorola mode 0, manual CS on GPIO17): PASS. `onTransmit` saw 0xa5 then 0x5a with CS low; the injected complements 0x5a and 0xa5 came back through `SSPDR`; `SSPSR` read 0x7 (TFE, TNF, RNE). Zero bus time.
- ADC (`adc.uf2`, scenario `adc`): PASS. `CS.EN`, `READY`, `AINSEL`, `START_ONCE` behave; channel 0 read 0x123 and channel 1 read 0x456 as injected through `mcu.adc.channelValues`; a conversion took 3 us (silicon: 2 us at 48 MHz ADC clock).
- Watchdog (`watchdog.uf2`, scenario `watchdog`): PARTIAL. `LOAD = 10000` with `CTRL.ENABLE` triggered at cycle 660,667 = 5285.3 us; silicon with a 1 us tick would fire at 10,000 us (datasheet 12.9: "the watchdog instead takes a tick input from the system-level ticks block"; `TICK_FREQUENCY = 2_000_000` in `watchdog.ts` is the RP2040-E1 constant). `SCRATCH0..7` and `REASON` behave; `CTRL.TIME` read back 16,777,213 instead of the remaining count; the TICKS.WATCHDOG registers are unimplemented.
- Flash API (`flash_qmi.uf2`, QMI direct mode JEDEC-ID read, emulator-only because on silicon it must run from SRAM): FAIL. `DIRECT_TX` bytes are accepted and discarded, `DIRECT_CSR.RXEMPTY` stays 1 and `DIRECT_RX` reads 0 where a W25Q32 answers 0xEF 0x40 0x16 (the Pico 2 flash per rustos `link.ld` comment). The bootrom flash functions (`flash_range_erase`, `flash_range_program`) are built on the same direct mode, so erase/program of settings (VFO memory, keyer speed) cannot be tested in this emulator; XIP reads of the flash array work (`xip_word0` read 0x20082000, the linked stack top).
- USB (`usb.uf2`, scenario `usb`): PARTIAL. `USB_MUXING` and `MAIN_CTRL.CONTROLLER_EN` drive the `onUSBEnabled` hook (PASS); `USB_PWR` (0x78) and `SIE_CTRL` (0x4c, `PULLUP_EN`) are unimplemented. Device enumeration would have to be scripted from the harness with `sendSetupPacket`; the README claims `hello_usb.c` runs. Not exercised further because SI-022's USB role is firmware loading through the bootrom (BOOTSEL), which is outside the firmware.
- GPIO input pull-ups: an undriven input with `PUE` set reads 0 in `SIO.GPIO_IN` (silicon reads 1); the harness must drive the idle level explicitly (`gpio[n].setInputValue(true)`), as the `gpio-irq` scenario does.
- Emulator throughput on this Mac (Apple Silicon, node v25.9.0, ts-node): 47 to 121 Mcycles/s depending on peripheral activity, i.e. 0.4 to 1.0 x real time at 125 MHz.

### F12. Peripheral coverage matrix: rp2350js ARM model versus the rustos driver work packages

Status: PASS = behaviour matched the datasheet in the test; PARTIAL = usable with the stated limits; FAIL = not usable for evidence at this commit. "Credit" is the recommended `tools/toolchain.lock.md` accreditation scope (`docs/process/04-verification-and-validation.md` section 4 and 5.2).

| Work package | One-line test (image, scenario) | Result | Credit recommendation |
|---|---|---|---|
| Clocks (XOSC, PLL_SYS, CLOCKS, TICKS) | `clocks.uf2`: start XOSC, poll STABLE; PLL to 150 MHz; select clk_sys; measure cycles per 10 ms | PARTIAL: register sequence executes, XOSC STABLE lies (0xffffffff), PLL lock always 1, TICKS unimplemented, clk_sys stays 125 MHz | No credit for clock correctness or any duration; Bench only |
| TIMER0 (counter, 4 alarms, IRQ 0..3) | `alarm_irq.uf2` (30 alarms via NVIC, busy/wfi/wfe) and `alarm_poll.uf2` | PASS with limits: alarm up to 1 us early; LOCKED/SOURCE absent; counts without TICKS | Credit for alarm/IRQ logic and microsecond-ordered event sequences; no credit for sub-microsecond timing |
| PWM slices 0..7 | `pwm.uf2` phases 1, 2 (per-slice CSR/DIV/TOP/CC) | PASS for waveform period and duty in cycles; DIV write re-enables a disabled slice; EN/INTR/IRQ0_INTE at RP2350 offsets unimplemented | Credit for duty/period configuration through CHn registers only; no credit for enable/disable sequencing or wrap IRQs |
| PWM slices 8..11 | `pwm.uf2` phase 5 (CH8_DIV/CH8_TOP readback) | FAIL: aliases onto the model's EN/INTR registers | None; keep cwht's sidetone and backlight on slices 0..7 |
| ADC | `adc.uf2` (channels 0 and 1, injected 0x123/0x456) | PASS | Credit for conversion logic and value plumbing (battery monitor); not for sample timing |
| I2C0 (Si5351) | `i2c0.uf2` (write 2 bytes, pointer write + read, ack/nack hooks) | PASS, zero bus time, IC_FS_SPKLEN unimplemented | Credit for register-write sequences into a host-side Si5351 model; no credit for bus timing or clock stretching |
| SPI0 (LCD) | `spi0.uf2` (8-bit mode 0, manual CS, loopback complement) | PASS, zero bus time | Credit for byte streams and CS/DC ordering into a host-side LCD model; no credit for timing |
| Watchdog | `watchdog.uf2` (LOAD 10000, ENABLE, scratch) | PARTIAL: fires at 0.53 x the RP2350 timeout; TIME readback wrong | Credit for scratch registers and "does it fire" only, with the 2x factor documented; timeout values Bench |
| Flash API (QMI direct mode, bootrom flash functions) | `flash_qmi.uf2` (JEDEC ID 0x9F) | FAIL: no flash device behind QMI direct mode | None; settings persistence is HostUnit (mock) plus Bench |
| GPIO IRQ (key, paddle, encoder) | `gpio_irq.uf2`, scenario `gpio-irq` (EDGE_LOW on GPIO2, NVIC 21) | FAIL: IO_BANK0 INTR/INTE/INTF/INTS mis-decoded | None until fixed upstream or patched in the vendored copy; polling `GPIO_IN` works |
| USB | `usb.uf2`, scenario `usb` | PARTIAL: controller enable hook only; USB_PWR and SIE_CTRL unimplemented | None for cwht (USB is bootrom-side per SI-022) |
| GPIO output/input via SIO (rustos path) | every image (GPIO25 toggles), `gpio_irq.uf2` (GPIO_IN read) | PASS; pull-ups not reflected on undriven inputs | Credit, with the rule that the harness drives every input's idle level |
| GPIO via GPIOC coprocessor (pico-sdk default) | `cwht-gpioc-probe.ts` | FAIL: MCRR bit forms and most MCR forms are NOPs | None; cwht must not adopt GPIOC-based GPIO code |
| UART0 (trace channel) | `uart_echo.uf2`, scenario `uart-echo` | PASS, infinite throughput | Credit for text assertions (expect-text) |
| NVIC entry/return, WFI, WFE | `alarm_irq.uf2` phases A/B/C | PASS | Credit |
| NVIC priorities (IPR), SysTick | `cwht-regprobe.ts`, `spin.uf2` | FAIL: mislocated by +0x100 and +0x10 | None until fixed |

### F13. Accreditation case for the emulator (SWE-136)

Proposed record for `tools/toolchain.lock.md` (owner approval at PDR per `docs/process/07-software-engineering-plan.md` section 8.3), identifier `ACC-EMU-001`.

Tool identity:
- c1570/rp2350js, git commit `af0114cbee8e9e91574204b66f10aa2961cbf28c` (2026-09-10 18:07:31 +0200, "support USB CDC in the C build"), `package.json` version 2.0.1, MIT.
- `package-lock.json` sha256 `dd88d3100bd97acdcaa3daa3c2c931590938cd5a42d72e2daf7978d684f24e05`; `package.json` sha256 `db353ce35c433683da45d70a02d07b6655d073f26ce79c1df8e132ae53b6fdbe`; `npm ci` result "added 428 packages"; embedded bootrom RP2350 A2 (`src/bootroms`).
- Invocation contract: `new RP2350({ coreArch: 'arm', loadFirmware })` (the default `coreArch` is `riscv` and must never be relied upon); harness `cwht-accredit.ts` sha256 `57f703639945aea669d472b4f474e35733ac60661dde387599394f2bc1c0bb4f`; probes `cwht-regprobe.ts` `4ec5d160679bfec4e6cae93a6f25ae6a7428d852e6c6eb4b1b0111560674aa54`, `cwht-gpioc-probe.ts` `a60559f5df5927388226a6f05a7bbe8a47d13dc1f660a58b48666a30d252a204`.

Environment (recorded at accreditation, re-checked at each TRR): macOS 26.6.2 (Darwin 25.6.0) arm64; node v25.9.0; npm 11.12.1; TypeScript 5.9.3; ts-node 10.9.2; rustc 1.98.0 (88d9e12ae 2026-08-18) with `thumbv8m.main-none-eabihf`; cargo 1.98.0; picotool v2.3.0. Node upgrades are a CR because the lockfile is pinned to `engines.node >= 18` only.

Known answers (all three must reproduce bit-exactly before any Emulation evidence is credited):
- KA-1 blinky toggle count: `rustos/blinky.uf2` sha256 `7e03c238649a1a038f988c58c0e716e6e46207acb3ca63ee2d4d90eb1d4332d9`; run 100,000,000 cycles; expect exactly 20 GPIO25 Low/High transitions, the first (Low to High) at cycle 35132, then intervals alternating 5,234,377 and 5,234,378 cycles; no UART output; no GPIO23 (HardFault marker) activity. Reference command: `npx ts-node demo/cwht-accredit.ts <blinky.uf2> 100000000 none`.
- KA-2 UART echo: `uart_echo.uf2` sha256 `c144ce8122c2147c97268d9fc480ce947fb7af763bd20e4f6f5fa0853029eea5` (built from `fw/src/bin/uart_echo.rs` in the assets folder); scenario `uart-echo`, 8,000,000 cycles; expect banner `uart_echo: ready`, the echoed string `"CQ CQ DE W1AW K\n"` byte-exact, and exactly one GPIO25 transition; harness prints `uart-echo PASS`.
- KA-3 timer IRQ: `alarm_irq.uf2` sha256 `d5764035efc8175b4d421af40241268473a8186953abbcf15f9e161806dfdd4d`; 30,000,000 cycles; expect lines `A count=10`, `B count=20`, `C count=30`, `DONE`, and 30 GPIO25 transitions with every interval in 124,880 to 124,940 cycles.

Acceptance criteria: KA-1 to KA-3 reproduce; `npx vitest run` in the vendored tree passes (not run in this study, see Open item 6); the probe scripts report the same PASS/FAIL pattern as this report (so a silent upstream change is noticed); the coverage matrix (F12) is copied into the lock file as the credit scope. A firmware release's Emulation report cites `ACC-EMU-001` and the commit hash of the vendored tree.

Scope of credit (what the tool is accredited for): boot through the A2 bootrom of an `rp2350-arm-s` UF2 or ELF; Cortex-M33 instruction execution including FPU; TIMER0 alarms and NVIC IRQ entry/return, WFI/WFE; SIO GPIO output/input; UART0 text; I2C0/SPI0 byte streams into host-side device models; ADC value plumbing; PWM slices 0 to 7 waveform configuration; microsecond-ordered event sequencing. Explicitly not credited: any duration or frequency in seconds; clock tree; GPIO edge interrupts; NVIC priorities and preemption; SysTick; PWM enable sequencing, wrap IRQs and slices 8 to 11; watchdog timeout values; flash erase/program; USB; GPIOC instructions; TICKS.

Re-accreditation triggers: any change of the emulator commit, lockfile hash, node major version, or a patch to the vendored copy (each patch gets a probe demonstrating the fix, and the credit scope is widened only by CR).

Where the vendored copy lives (recommendation, consistent with the paths the V&V plan already names): `tools/emu/rp2350js/` as a git submodule pinned at `af0114cb`, with a mirror fork under the owner's GitHub account so the commit cannot disappear (the upstream has one maintainer and 7 stars); `tools/emu/harness/` for `cwht-accredit.ts` and the probes; `firmware/emu/` for cwht scenarios and the `emutest` known-answer crate (`docs/process/04-verification-and-validation.md` section 4 names `firmware/emu/`); `docs/vv/reports/ACC-EMU-001/` for the captured known-answer outputs and hashes; the accreditation entry itself in `tools/toolchain.lock.md`. `node_modules` is never committed; `npm ci` from the committed lockfile is the reproducible install.

### F14. Upstream issue drafts (c1570/rp2350js; tracker had zero open issues on 2026-09-25)

Issue A, title "RP2350 ARM: GPIO coprocessor (CP0) decode does not match datasheet 3.6.1; pico-sdk gpio_put() is a NOP":

> In ARM mode at af0114cb, `gpioc_bit_out_put` / `gpioc_bit_oe_put` (MCRR, `mcrr p0, #4, Rt, Rt2, c0/c4`) are treated as CDP and skipped because `isMrcMcr()` in `src/cortex-m33/coprocessor.ts` only accepts hw1[4]=1 encodings. The single-register forms are decoded with opc1 as bank and opc2 as operation, whereas RP2350 datasheet 3.6.1 uses opc1 as the operation (0 put, 1 xor, 2 set, 3 clr, 5 bit_xor, 6 bit_set, 7 bit_clr) and CRm as the bank (c0 lo out, c1 hi out, c4 lo oe, c5 hi oe). Consequence: pico-sdk builds (PICO_USE_GPIO_COPROCESSOR=1 by default) never move a pin; `demo/m33_blink/blink_simple.uf2` sleeps and wakes correctly but GPIO25 stays InputPullDown for 2.4 s of emulated time. Minimal repro (no firmware): enable CP0 in CPACR (write 0x3 to 0xE000ED88), place halfwords `0xec45 0x3044` at SRAM, set r3=25, r5=1, execute one instruction, read SIO GPIO_OE (0xd0000030): expected bit 25 set, observed 0. With `0xee40 0x0010` (gpioc_lo_out_set, r0=1<<24) GPIO_OUT stays 0. Script attached (cwht-gpioc-probe.ts).

Issue B, title "RP2350: IO_BANK0 INTR/PROC0_INTE/INTF/INTS decode always misses (GPIO interrupts never fire)":

> `src/peripherals/io_rp2350.ts` computes `register = (offset % 0x18) * 0x18` and compares it to the absolute offsets INTR0=0x230, PROC0_INTE0=0x248, PROC0_INTF0=0x260, PROC0_INTS0=0x278; `offset % 0x18` is 8 for all four, so `register` is 192 and no case matches. Writes to PROC0_INTE0 are dropped and reads of INTR/INTS return 0. Repro: `chip.writeUint32(0x40028248, 0x400); chip.readUint32(0x40028248)` returns 0 and `chip.gpio[2].irqEnableMask` stays 0; a falling edge on GPIO2 then never pends IO_IRQ_BANK0 (IRQ 21). Suggested fix: derive the register group from `Math.floor((offset - 0x230) / 0x18)` and the GPIO octet from `((offset - 0x230) % 0x18) / 4`.

Issue C, title "RP2350 PPB: SysTick and NVIC_IPR registers are off by 0x10 and 0x100":

> In `src/peripherals/ppb_rp2350.ts`, `SYSTICK_BASE = 0xe010` is combined with `SYST_CSR = 0x010` etc., so SysTick answers at 0xE000E020..2C instead of 0xE000E010..1C; `NVIC_IPR0 = 0x400` is added to `NVIC_BASE = 0xe100`, so priorities live at 0xE000E500 instead of 0xE000E400 (RP2350 datasheet 3.7.5: 0x0e400 NVIC_IPR0). Writes to the architected addresses log "Unimplemented peripheral write via 0" and reads return 0xffffffff; pico-sdk `irq_set_priority` and any SysTick user are affected.

Issue D (shorter notes for one issue or a PR series): (1) PWM uses the RP2040 map: EN/INTR/INTE/INTF/INTS at 0x0a0..0x0b0 collide with CH8..CH11 on RP2350, whose EN is 0x0f0, INTR 0x0f4, IRQ0_INTE 0x0f8, IRQ0_INTS 0x100, IRQ1_* 0x104..0x10c; slices 8..11 missing (README already lists this). (2) `Timer32.prescaler` setter sets `enabled = prescalerValue !== 0`, restarting a slice disabled through CSR.EN=0 when DIV is written. (3) `RPTimer` alarm scheduling truncates the current fractional microsecond (`(value - nanos/1000) >>> 0`), firing up to 1 us early; use `Math.ceil` of the remaining nanoseconds to the target boundary. (4) `RPWatchdog` keeps `TICK_FREQUENCY = 2_000_000` (RP2040-E1) for RP2350, halving timeouts. (5) `RP2350.clkSys` is 125 MHz and never follows PLL_SYS/CLOCKS; README could state this. (6) README "Missing: Timer and System Interrupts" is stale for the ARM core (exceptions.spec.ts covers it; a 30-alarm TIMER0 IRQ firmware runs).

## Implications for cwht

- **DECISION-needed:** Adopt `ACC-EMU-001` (F13) as the SWE-136 accreditation record for the Emulation evidence class, with the credit scope of F12 copied into `tools/toolchain.lock.md`; the ADR due at PDR (`docs/process/04-verification-and-validation.md` section 4) selects c1570/rp2350js ARM mode at `af0114cb` and records Renode as fallback.
- **DECISION-needed:** Vendoring form: git submodule at `tools/emu/rp2350js` pinned to `af0114cb` plus a mirror fork under the owner's account (recommended), versus a plain copied tree. Submodule keeps upstream provenance and makes the future rebase to a fixed upstream cheap; the mirror protects against a single-maintainer repository disappearing.
- **DECISION-needed:** Whether cwht patches the vendored emulator for the GPIO-IRQ decode (F8), PPB offsets (F9) and PWM map (F10) while upstream issues are open. Recommendation: yes, as small patches with probe-backed evidence, because the key/paddle GPIO IRQ path is on the critical firmware path, and the patched tree becomes `ACC-EMU-002` by CR.
- **ACTION:** File Issues A, B, C (and D) upstream with the probe scripts attached; offer the fixes as PRs. The tracker is empty, so response time is unknown.
- **ACTION:** Bench cross-check of F2 and F5 on the owner's Pico 2 to close the hardware side of the timing band: flash `spin.uf2` and `timer10ms.uf2` after adding XOSC+PLL setup; read results either over UART0 with a USB-serial adapter (none is in the bench inventory) or by having the firmware send the measured numbers in Morse on the LED, which the owner can read without instruments.
- **ACTION:** Add a rule to the firmware coding standard: GPIO through SIO stores only (as rustos does), never GPIOC coprocessor instructions, until Issue A is fixed; otherwise emulation shows dead pins.
- **REQ-candidate (firmware):** The clock driver shall enable `TICKS.TIMER0` (and `TICKS.WATCHDOG`) explicitly from clk_ref with `CYCLES` matching the reference frequency before any TIMER0 use, and the HostUnit/Inspection evidence shall check for it, because the emulator counts without it and silicon does not (F3).
- **REQ-candidate (firmware):** The clock driver shall bound its XOSC `STABLE` and PLL `LOCK` waits with a TIMER0-independent timeout and report a fault, because the emulator answers "stable" instantly and silicon may not; the fault path is the only thing emulation can exercise here (F5).
- **REQ-candidate (V&V plan):** Emulation scenarios shall express time only in TIMER0 microseconds and shall assert event ordering, not durations; keyer element timing (dit length at a given WPM, weighting, iambic B release) is verified on the bench with the Pico-based logic capture named in charter section 9.
- **REQ-candidate (V&V plan):** Every emulation scenario shall drive the idle level of each modelled input (key, paddles, encoder A/B, buttons) explicitly, since pull-ups are not reflected (F11).
- **REQ-candidate (firmware design):** Sidetone and backlight PWM shall use slices 0 to 7 and per-slice CSR enable, not the mass EN register or wrap IRQs, so the sidetone path stays inside the emulator's credited scope (F10); this also keeps GPIO25 (slice 4B, the on-board LED) available as the visible emulator marker.
- **RISK-candidate:** GPIO edge interrupts are not modelled at this commit (F8). If unpatched, the key and paddle input paths (SI-018) get no Emulation evidence and rely on HostUnit plus Bench; mitigation: patch or upstream fix before the first firmware sprint, or design the keyer to poll inputs from the TIMER0 alarm handler (which is modelled) so the same code path is testable.
- **RISK-candidate:** No NVIC priority model (F9). Priority inversions between the keyer alarm, Si5351 I2C driver and LCD SPI driver cannot be caught in emulation; mitigation: keep all cwht IRQs at one priority level by design (single-level, run-to-completion handlers with a main-loop queue), which also simplifies the safety argument for TX sequencing.
- **RISK-candidate:** Watchdog timeouts are 2x short in the model (F11); a watchdog-based TX fail-safe tuned in emulation would be tuned wrong. Mitigation: timeout values are Bench-verified; emulation checks only that the feed path exists.
- **RISK-candidate:** The RP2350 A2 bootrom is embedded; owner boards may be A3/A4 (prior report, Open item 1). Unchanged.
- **ACTION (CM):** Record the sha256 of every UF2 used as a known answer (listed above and in the assets folder) and of `link.ld` so the accreditation record can detect drift when rustos changes its linker script.

## Confidence

| Finding | Confidence |
|---|---|
| F1 Reproduction; 67-cycle unrolled loop explains the earlier number | High |
| F2 Spin loop: emulator 3.000 cycles/iteration | High (emulator) / Low (hardware reference) |
| F3 TIMER0 10 ms = 1,250,000 cycles; counts without TICKS | High |
| F4 PWM period exact on average; fractional divider averaged | High |
| F5 clk_sys fixed at 125 MHz, PLL/XOSC/TICKS not applied; error table | High (except APB and IRQ latency rows, Low/Medium) |
| F6 TIMER0 ALARM0 IRQ and polling work; alarm up to 1 us early | High |
| F7 F14 root cause is GPIOC decode, not timers | High |
| F8 GPIO IRQ register decode defect | High |
| F9 SysTick and NVIC_IPR offsets | High |
| F10 PWM RP2350 map, slices 8 to 11, DIV re-enable | High |
| F11 UART/I2C/SPI/ADC PASS; watchdog 2x; QMI FAIL; USB partial; pull-ups | High |
| F12 Coverage matrix | High for tested rows; USB row Medium |
| F13 Accreditation case | High (facts); the credit scope is a recommendation |
| F14 Issue drafts | High (each backed by a probe) |

## Open items

1. Hardware reference for the timing band (F2, F5): run `spin.uf2`/`timer10ms.uf2` variants with XOSC+PLL and TICKS setup on the owner's Pico 2 and compare cycles per iteration and cycles per 10 ms; needs either a USB-serial adapter for UART0 or the Morse-on-LED output method. Until then the hardware side of the spin-loop band is Low confidence.
2. Arm's Cortex-M33 per-instruction timing is not published; the 3 to 5 cycle range for `subs; bne` is inferred from the Cortex-M4 TRM. If the owner wants a documented figure, Arm's Cortex-M33 "Cycle timing" data would have to be requested or measured.
3. Upstream response to Issues A to D is unknown (empty tracker, single maintainer); decide at PDR whether the vendored tree carries local patches.
4. The pico-sdk version and board target of `demo/m33_blink/blink_simple.uf2` were not recorded by upstream; irrelevant to cwht evidence but relevant to Issue A's reproduction text.
5. RP2350 bootrom stepping on the owner's boards (A2 in the emulator) remains unverified (carried from the prior report).
6. `npx vitest run` (the emulator's own 400-plus tests, including `exceptions.spec.ts`) was not executed in this study; it should be part of the acceptance criteria in `ACC-EMU-001` and its runtime measured.
7. USB device enumeration through the harness (`sendSetupPacket`) was not attempted; only relevant if cwht later adds a USB CDC trace port.
8. The `cts2c` transpiled-C build was not accredited; if it is adopted for speed, it needs its own known-answer run (KA-1 to KA-3) because it is a different executable.
9. Whether an emulator-side patch for the TIMER alarm truncation (F6) is worth carrying: at 1 us it is below any cwht requirement, but it makes "sum of N alarms" checks drift by up to N microseconds.
