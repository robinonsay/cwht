# RP2350 emulation options for cwht firmware (headless, macOS)

Research note, assignment key `emulation`. Date of research: 2026-09-25. All web sources were read on that date; project activity dates come from the GitHub, crates.io and GitLab APIs on that date.

## Question

Which emulators can run a bare-metal Rust ELF/UF2 for the RP2350 (Pico 2, Cortex-M33 path, target `thumbv8m.main-none-eabihf`) headlessly on this Mac so cwht firmware can be proven before hardware (charter section 9, evidence class *Emulation*)? Evaluate Wokwi, Renode, QEMU and the rp2040js lineage; deliver a recommendation, install steps for this Mac, and the user actions (accounts, tokens) each option needs.

## Method

1. Read charter sections 1, 9 and 11 (`docs/process/00-charter.md`) and the owner's `rustos` workspace (`/Users/robinonsay/rust/rustos`, crate `firmware/pico2`, alias `cargo pico2 = build -p pico2 --target thumbv8m.main-none-eabihf`, prebuilt `blinky.elf` / `blinky.uf2`).
2. Inventoried this Mac: `sw_vers` = macOS 26.6.2 (Darwin 25.6.0), `uname -m` = arm64 (Apple Silicon), Homebrew 6.0.20, node v25.9.0, npm 11.12.1, rustc 1.98.0 with `thumbv8m.main-none-eabihf` installed, `picotool` present. Not installed: `qemu-system-arm`, `renode`, `wokwi-cli`, `dotnet`, `probe-rs`.
3. Web research (WebSearch/WebFetch) on vendor docs and repositories, plus GitHub / crates.io / GitLab REST and GraphQL APIs via `curl` for dates, trees, release assets and issue comments.
4. Local trial: cloned `c1570/rp2350js` into a scratch dir (`/private/tmp/cwht-emu-scratch/rp2350js`, commit `af0114cbee8e`, 2026-09-10), ran `npm ci` (428 packages), wrote a 30-line headless harness and executed (a) the owner's own `rustos/blinky.uf2` and (b) the emulator's bundled pico-sdk `blink_simple` M33 build. Commands and outputs are quoted in the findings.

## Findings

### A. Wokwi

**F1. Wokwi does not simulate the Pico 2 / RP2350 (as of 2026-09-25).** The supported-hardware page lists only "RP2040 (Raspberry Pi Pico), a dual-core ARM Cortex-M0+ microcontroller" under Pi Pico; the `wokwi-pi-pico` part reference does not mention RP2350; wokwi.com/pi-pico offers Pico and Pico W templates only. Community projects titled "Pico 2" use the RP2040 part. Sources: https://docs.wokwi.com/getting-started/supported-hardware , https://docs.wokwi.com/parts/wokwi-pi-pico , https://wokwi.com/pi-pico , https://wokwi.com/projects/386617826630264833 . Confidence: High.

**F2. Wokwi's RP2040 core is rp2040js; RP2350 support was requested in wokwi/rp2040js#142 (opened 2025-01-31) and the maintainer (Uri Shaked, 2025-03-23) said "I'm not actively working on that. If anyone is up to sponsoring the development I'm happy to discuss."** c1570 posted on 2026-08-02 that rp2350js now has ARM M33 support and a transpiled-C build that "might also be interesting for Wokwi", untested. Source: https://github.com/wokwi/rp2040js/issues/142 (comments fetched via `curl https://api.github.com/repos/wokwi/rp2040js/issues/142/comments`). Confidence: High.

**F3. Wokwi CLI is cloud-hosted and metered.** "The simulation runs in the cloud, and you can stream the serial output back to your CI system". Monthly CI minutes: Free 50, Hobby/Hobby+ 200, Pro 2000. Token: `WOKWI_CLI_TOKEN` from https://wokwi.com/dashboard/ci (account required); "A valid Wokwi CLI token starts with `wok_` and is exactly 44 characters long". Install on macOS: `curl -L https://wokwi.com/ci/install.sh | sh` or the `wokwi-cli-macos-arm64` binary from GitHub releases (latest v0.27.1, 2026-09-16). CLI features: `--timeout`, `--expect-text`, `--fail-text`, `--scenario <yaml>`, `--screenshot-file`, `--serial-log-file`, `--gdb-server-port`; `wokwi.toml` accepts `.hex/.uf2/.elf` for the Pico. Sources: https://docs.wokwi.com/wokwi-ci/getting-started , https://docs.wokwi.com/wokwi-ci/cli-usage , https://docs.wokwi.com/wokwi-ci/cli-installation , https://github.com/wokwi/wokwi-cli , https://docs.wokwi.com/vscode/project-config . Pricing (EUR, 2026 page): Community free, Hobby 5.6/mo, Hobby+ 8.1/mo (includes Wokwi for VS Code), Pro 20/seat/mo (2000 CI min). Source: https://wokwi.com/pricing . Confidence: High.

**F4. Wokwi Custom Chips API (beta) would be adequate for an Si5351 and an SPI LCD model if the MCU were supported.** Chips compile to WASM from C or "any language that compiles to WebAssembly (e.g. Rust ...)". I2C: `i2c_init(i2c_config_t{address, sda, scl, connect, read, write, disconnect})`, connect/write return ACK booleans. SPI: `spi_init(spi_config_t{sck, mosi, miso, mode, done})`, CS handled by `pin_watch` + `spi_start()/spi_stop()`. Framebuffer API: RGBA 32 bpp buffer sized from `.chip.json`. `wokwi-cli chip compile my-chip.c` builds chips; `[[chip]] name/binary` in `wokwi.toml`. Scenario YAML supports `set-control`, `expect-pin`, `wait-serial`, `delay`. Sources: https://docs.wokwi.com/chips-api/getting-started , https://docs.wokwi.com/chips-api/i2c , https://docs.wokwi.com/chips-api/spi , https://docs.wokwi.com/chips-api/framebuffer , https://docs.wokwi.com/wokwi-ci/automation-scenarios . Confidence: High (API), Low (relevance, because of F1).

### B. Renode

**F5. Upstream Renode has no RP2040 or RP2350 platform.** `curl https://api.github.com/repos/renode/renode/contents/platforms/cpus` and `.../boards` contain no `rp2*`/`pico` files (only `picosoc.repl`, `litex_picorv32.repl`); the CHANGELOG has no RP2040/RP2350 entry; the supported-boards page lists none. Renode does support the Cortex-M33 CPU model (`platforms/cpus/stm32l552.repl`: `cpu: CPU.CortexM ... cpuType: "cortex-m33"`). Latest release v1.17.0 (2026-09-07) ships `renode-1.17.0.osx-arm64-portable.dmg`. Sources: https://github.com/renode/renode/tree/master/platforms/cpus , https://raw.githubusercontent.com/renode/renode/master/platforms/cpus/stm32l552.repl , https://github.com/renode/renode/releases/latest , https://renode.readthedocs.io/en/latest/introduction/supported-boards.html . Confidence: High.

**F6. A third-party RP2040 platform for Renode exists (matgla/Renode_RP2040, MIT, created 2024-02-19, last push 2026-09-18, 6 forks) but is frozen and RP2040-only.** README (2025-10-11): "WIP and Frozen (lack of time)". Coverage table: GPIO full (with interrupts), I2C full (master, IRQ, DMA), SPI partial (master only, one mode, no clock config), ADC partial, Timers partial (alarms), DMA full, UART full, Watchdog full, PIO partial (external C++ `piosim` modelled as a second CPU, manual resync; "IRQ and DMA not yet supported"), **PWM not supported**, USB/RTC/SysInfo/SysConfig not implemented. Pinned to Renode 1.16.1; peripherals are C# compiled to `Peripherals.dll` (`dotnet build emulation/Peripherals.csproj -c Release`) and loaded by `cores/load_peripherals.py`; `piosim` ships prebuilt `libpiosim.dylib/.so/.dll`. Run: `path add @repos/Renode_RP2040`, `include @boards/initialize_raspberry_pico.resc`, `sysbus LoadELF @fw.elf`, `start`. Source: https://github.com/matgla/Renode_RP2040 (README raw). Confidence: High.

**F7. A 2-day RP2350 port of that platform exists (vighnesh-sawant/Renode_RP2350, commits 2026-03-08/09: "port as much RP2040 peripherals to RP2350").** `cores/rp2350.repl` declares two `CPU.CortexM cpuType: "cortex-m33"` cores with NVICs at 150 MHz SysTick, RP2350 memory map (32 KB bootrom, 4 MB flash, 2x256 KB striped SRAM, SRAM8/9), `UART.RP2040Uart` x2, 3x `CPU.RP2040PIOCPU`, `Timers.RP2040Timer` x2, `SPI.PL022` x2, `I2C.RP2040I2C` x2, `Analog.RP2040ADC`, `DMA.RPDMA`, `GPIOPort.RP2040GPIO`, watchdog, clocks/PLL/XOSC/ROSC, and **plain `Memory.MappedMemory` stubs** for ACCESSCTRL, OTP, POWMAN, HSTX, TRNG, TICKS, BOOTRAM; comment "pio interrupts are not implemented". README is the frozen matgla text; no tests of the RP2350 board are documented; 0 stars, no activity since 2026-03-09. Sources: https://github.com/vighnesh-sawant/Renode_RP2350 , https://raw.githubusercontent.com/vighnesh-sawant/Renode_RP2350/main/cores/rp2350.repl . Confidence: High (content), Low (fitness; untested).

**F8. Renode on this Mac: official Homebrew tap.** README: "brew install renode/tap/renode" (stable) or `renode-nightly`; the formula (renode/homebrew-tap, updated 2026-09-25) has a bottle for `arm64_tahoe` and depends on `dotnet@10`, `gtk+3`, `mono-libgdiplus`, `python@3.12`, `libyaml`, `dialog`, plus build deps. Alternative: the `osx-arm64-portable.dmg` (requires dotnet >= 6.0 on host). Headless flags: `--console`, `--disable-gui`, `--hide-monitor`; `renode-test` runs Robot Framework suites (`pip install -r tests/requirements.txt`). Custom peripherals can be written inline in Python (`Python.PythonPeripheral`) or as C#. Sources: https://raw.githubusercontent.com/renode/renode/master/README.md , https://raw.githubusercontent.com/renode/homebrew-tap/main/Formula/renode.rb , https://renode.readthedocs.io/en/latest/basic/using-python.html . Confidence: High.

### C. QEMU

**F9. No upstream QEMU machine exists for RP2040 or RP2350.** QEMU 11.1 docs list Cortex-M33 boards `mps2-an505`, `mps3-an547`, `musca-a/b1` and only the `raspi0..raspi4b` SBCs; `hw/arm` on master has `raspi.c`/`raspi4b.c` and nothing for `rp2*`. Homebrew has `qemu` 11.1.1 but it would not help. Sources: https://www.qemu.org/docs/master/system/target-arm.html , `curl https://api.github.com/repos/qemu/qemu/contents/hw/arm`. Confidence: High.

**F10. The RP2350 request is an open GitLab task with a discouraging maintainer response.** Task #3125 "Support for RPi RP2350, RPi Pico 2W, and SparkFun Thing Plus - RP2350", opened 2025-09-21 by `eschaton`, state OPEN, label "Kind::Feature Request". Arm maintainer `pm215` (2025-09-22): "There's not a lot of point in posting this unless you're proposing to actually do the work. Our existing raspberry pi board models are already undermaintained and only in the 'odd fixes' state..." (fetched via the GitLab GraphQL API). Source: https://gitlab.com/qemu-project/qemu/-/work_items/3125 . Confidence: High.

**F11. An RP2040-only machine is under review on qemu-devel (RFC v3, Gilles Grimaud, 2026-09-06, 36 patches, machine `raspi-pico`).** Implements dual M0+, SRAM, XIP flash, ELF/UF2 loading, UART0/1, SIO, clocks/PLL, GPIO banks, DMA, synthetic bootrom. Not implemented: **PIO, ADC, I2C, PWM, SPI**, RTC, USB. Not merged. Continues Alex Bennee's 2022 RFC; GitHub mirrors `2xs/qemu-rp2040-pico`, `n9wxu/qemu-rp2040-pico`. No RP2350 content. Sources: https://ratatoskr.run/qemu-devel/2026/09/17521624/t , https://www.mail-archive.com/qemu-devel@nongnu.org/msg860944.html , https://github.com/2xs/qemu-rp2040-pico . Confidence: High.

### D. rp2040js lineage and other native emulators

**F12. c1570/rp2350js (TypeScript, MIT, fork of wokwi/rp2040js; last push 2026-09-10; v2.0.1) is the only found emulator that both (a) runs the Cortex-M33 path and (b) carries the full rp2040js peripheral set with host-side device hooks.** README status: "RISC-V/Hazard3 machine mode", "basic ARM/Cortex M33 support (no secure/insecure mode)", "runs from bootrom" (embedded RP2350 **A2** bootrom generated from `pico-bootrom-rp2350` releases), RAM and flash images, MicroPython on both arches, GDB server, MCP server, ~70M cycles/s on Node, transpiled C variant ~3x faster. `src/peripherals` includes `adc.ts, i2c.ts, spi.ts, uart.ts, pwm.ts, timer.ts, dma*.ts, pio.ts, io_rp2350.ts, pads_rp2350.ts, watchdog.ts, usb.ts, powman_rp2350.ts, xip_rp2350.ts` etc. `RP2350Options.coreArch: 'riscv' | 'arm'` (default `riscv`; real silicon default is `arm`); `loadFirmware` accepts `.hex` or `.uf2` and, for SRAM images, sets up the bootrom's vectored-boot watchdog-scratch handshake. Listed as **missing**: "Timer and System Interrupts (Xh3irq is there though)", "Exceptions", PWM 8->12 slices, TIMER LOCK/SOURCE, timers when changing sys_clk/PLL, QMI address translation, SIO NONSEC, doorbells, RTC, XOSC, PLL_USB, ACCESSCTRL, BUSCTRL, HSTX, TRNG, SHA256, POWMAN (*), OTP, cycle penalties; "somewhat correct instruction cycle counts *". Sources: https://github.com/c1570/rp2350js (README, `src/rp2350.ts`, `src/utils/load-firmware.ts`), https://github.com/raspberrypi/pico-bootrom-rp2350/releases (A2 2024-08-13, A3/A4 2025-07-29). Confidence: High.

**F13. Local trial: the owner's own bare-metal Rust firmware boots and runs in rp2350js on this Mac with no account, token or network.** `picotool info -a /Users/robinonsay/rust/rustos/blinky.uf2` reports `family ID 'rp2350-arm-s'`, `target chip: RP2350`, `image type: ARM Secure`, IMAGE_DEF block at `0x10000110`. Harness (`demo/cwht-run.ts`, below) run:

```
$ cd /private/tmp/cwht-emu-scratch/rp2350js
$ npx ts-node demo/cwht-run.ts /Users/robinonsay/rust/rustos/blinky.uf2 900000000
[XIP_QMI_BASE] Unimplemented peripheral write to 0xc: 1610641923   (bootrom QMI setup, non-fatal; 6 such lines)
GPIO25 -> 0 at cycle 35119
GPIO25 -> 1 at cycle 35132
GPIO25 -> 0 at cycle 5269509 (~0.035 s of simulated time at 150 MHz)
GPIO25 -> 1 at cycle 10503887 (~0.070 s)
GPIO25 -> 0 at cycle 15738264 (~0.105 s)
OK: 6 toggles observed; wall 240 ms
```

The firmware's delay is `for _ in 0..5_000_000 { spin_loop() }` (`rustos/templates/pico2/src/main.rs`), so a half period of 5.23 M emulated cycles is about 1.05 cycles per loop iteration, which is not credible for a `subs/yield/bne` loop on a Cortex-M33 (expect roughly 3 or more). Functional behaviour is right; **cycle timing is not trustworthy** (consistent with the README's own asterisk). Confidence: High (functional), Medium (timing interpretation).

Harness source (TypeScript, placed in the clone's `demo/`):

```ts
import { RP2350 } from '../src';
import { GPIOPinState } from '../src/gpio-pin';
const mcu = new RP2350({ coreArch: 'arm', loadFirmware: process.argv[2] });
mcu.uart[0].onByte = (v: number) => process.stdout.write(String.fromCharCode(v));
let toggles = 0;
mcu.gpio[25].addListener((s: GPIOPinState) => { toggles++; console.log(`GPIO25 -> ${s} at cycle ${mcu.cycles}`); if (toggles >= 6) process.exit(0); });
while (mcu.cycles < Number(process.argv[3] ?? 6e8)) mcu.step();
process.exit(toggles > 0 ? 0 : 1);
```

**F14. Local trial: the bundled pico-sdk `blink_simple` (M33 build) does NOT blink in rp2350js's ARM mode; it spins inside `sleep_ms`.** Same harness on `demo/m33_blink/blink_simple.hex`: 900 M cycles (6 s simulated) in 7.4 s wall (about 120 M cycles/s on this M-series Mac), `toggles=1`, many `[PPB] Unimplemented peripheral write ... 0xe408..0xe430` (NVIC IPR priority registers). A PC histogram after 200 M cycles shows `0x10000aa4 x99995945`, which the shipped disassembly resolves to `b.n 10000a56 <sleep_ms+0x8e>`. This matches the README gap "Timer and System Interrupts" and means SDK-style alarm-IRQ sleeps, and probably any NVIC-driven ISR, are not yet usable on the ARM path. Confidence: High (observed), Medium (root-cause attribution).

**F15. GhostRoboticsLab/GhLabs_RP2350_emulator (TypeScript, MIT, last push 2026-09-10, 0 stars) is RISC-V only.** "exclusively emulates Hazard3 RISC-V cores", "UF2 loader ... rejects Arm images loudly", boots A2 bootrom, 409 tests, headless CLI `npm run start:rp2350`. Not usable for a `thumbv8m` build. Source: https://github.com/GhostRoboticsLab/GhLabs_RP2350_emulator . Confidence: High.

**F16. 0x4D44/picoem (Rust, MIT OR Apache-2.0; crate `rp2350-emu` 0.2.6 published 2026-06-27; repo created 2026-04-12, last push 2026-06-27, 23 stars) has the best-validated Cortex-M33 core but stub peripherals.** Feature table: M33 ISA "QEMU-tested", FPU, coprocessors (GPIO/CP0, DCP, RCP) working, dual-core + SIO working, clock tree, NVIC/exceptions working, PIO working; **UART / SPI / I2C / DMA / timers: Stubs**; GDB: stub. Boots the real `bootrom-combined.bin` checked into `roms/`. Validation: differential vs QEMU Cortex-M33 (R0-R15 + xPSR) and vs real RP2354 silicon over SWD. Delivery is a TUI (`cargo run -p rp2350-emu-tui --release -- fw.bin`, raw `.bin` only, no ELF/UF2 loader documented) plus a library crate with `EmulatorBuilder`; threaded runtime is x86_64 Linux/Windows only (serial model works on macOS). Author: "A personal research project ... No promises". c1570 credits it as the "M33 reference". Sources: https://github.com/0x4D44/picoem , https://crates.io/api/v1/crates/rp2350-emu . Confidence: High.

**F17. danish9661/picoemu ("Bramble", C, MIT) claims full RP2350 ARM/RISC-V/RP2040 emulation with I2C/SPI device callbacks, ELF/UF2 auto-detect, GDB and 426 tests, but the repository was created 2026-09-08 (17 days old), has 1 star, 111 commits, and an `include/rp2350_arm/m33_cpu.h` described as "Cortex-M33 placeholder"; the Boot row lists only a RISC-V bootrom for RP2350.** Treat as unverified. Source: https://github.com/danish9661/picoemu . Confidence: Medium (facts), Low (fitness).

**F18. PIO-only tools exist for PIO program verification independent of the MCU emulator:** NathanY3G/rp2040-pio-emulator (Python, Apache-2.0, `pip install rp2040-pio-emulator`, RP2040/RP2350) and a browser PIO simulator (ice458). Sources: https://github.com/NathanY3G/rp2040-pio-emulator , https://ice458.github.io/tools/pio_sim/index.html . Confidence: High.

## Recommendation

1. **Adopt c1570/rp2350js (ARM mode) as the cwht *Emulation* evidence tool, vendored at a pinned commit.** It is the only option that today runs the owner's `rp2350-arm-s` UF2 through the real bootrom, headlessly, offline, with no account, on this Mac (F12, F13), and it exposes exactly the hooks cwht needs to model external parts in TypeScript: I2C `onStart/onConnect/onWriteByte/onReadByte/onStop` with `completeConnect(ack)/completeWrite(ack)/completeRead(byte)` for an Si5351 register model, SPI `onTransmit(value)` + `completeTransmit(rx)` plus a GPIO listener for CS/DC for the LCD, `gpio[n].setInputValue()` for straight-key and iambic-paddle stimulus (a scripted dit/dah timing profile is just a table of cycle stamps fed in the step loop), `uart[0].onByte` for expect-text assertions, and a GDB server. Sources for the hook API: https://raw.githubusercontent.com/wokwi/rp2040js/main/src/peripherals/i2c.ts , https://raw.githubusercontent.com/wokwi/rp2040js/main/src/peripherals/spi.ts (inherited by the fork).
2. **Budget engineering effort to close the ARM timer/NVIC interrupt gap (F14) or design around it early.** cwht's keyer, sidetone PWM and TX sequencing will use timer alarms and GPIO IRQs; verify on day one of firmware work whether rustos's timer/IRQ path runs in the emulator, and if not, fix the emulator (upstream to c1570) rather than reshape the firmware. Do not use emulated cycle counts as timing evidence (F13); timing requirements get Bench verification.
3. **Keep picoem as an ISA/oracle cross-check, not a platform** (F16): its M33 core is differential-tested against QEMU and silicon; if an rp2350js instruction bug is suspected, reproduce the instruction sequence there.
4. **Renode is a viable second-line option only with investment** (F5-F8): a Cortex-M33 RP2350 `.repl` can be assembled from matgla's RP2040 C# peripherals (the vighnesh port shows the shape), giving Robot Framework test reports and `LoadELF`, but PWM is absent, PIO needs an external C++ co-simulator with manual resync, the platform is pinned to Renode 1.16.1 while Homebrew ships 1.17.0, and the toolchain is heavy (dotnet@10, gtk+3, mono-libgdiplus). Revisit at PDR if Robot-style reporting is required for the V&V plan.
5. **Do not plan on Wokwi or QEMU.** Wokwi has no RP2350 target and its CLI runs in the cloud under a monthly-minute quota (F1-F3). QEMU has no RP2040/RP2350 machine upstream, the RP2350 request drew an explicit "do the work yourself" from the Arm maintainer, and the pending RP2040 RFC omits I2C, SPI, PWM, ADC and PIO (F9-F11).

### Exact install steps for this Mac (rp2350js path)

Prerequisites already present: git, node v25.9.0, npm 11.12.1, picotool, rustc 1.98.0 with `thumbv8m.main-none-eabihf`. No accounts, tokens or system packages required.

```
# 1. Vendor the emulator at a pinned commit (suggested location: tools/emu/rp2350js as a git submodule)
git -C /Users/robinonsay/rust/cwht submodule add https://github.com/c1570/rp2350js.git tools/emu/rp2350js
git -C /Users/robinonsay/rust/cwht/tools/emu/rp2350js checkout af0114cbee8e9e91574204b66f10aa2961cbf28c
# 2. Install JS deps (offline afterwards)
(cd /Users/robinonsay/rust/cwht/tools/emu/rp2350js && npm ci)
# 3. Build cwht firmware as an RP2350 ARM-S UF2 (rustos already produces one; picotool confirms the family)
picotool uf2 convert firmware.elf firmware.uf2 --family rp2350-arm-s   # or use rustos's existing UF2 output
# 4. Run a scenario headlessly (harness like demo/cwht-run.ts above; coreArch: 'arm')
(cd /Users/robinonsay/rust/cwht/tools/emu/rp2350js && npx ts-node demo/cwht-run.ts /path/to/firmware.uf2)
# 5. Optional: GDB attach (src/gdb/gdb-tcp-server.ts) and the transpiled C build for 3x speed (cts2c/README.md)
```

### Install steps for the alternatives (for the record)

- Renode: `brew install renode/tap/renode` (pulls dotnet@10, gtk+3, mono-libgdiplus, python@3.12; user approval needed because it installs system-level packages), then `git clone https://github.com/matgla/Renode_RP2040`, `dotnet build emulation/Peripherals.csproj -c Release`, author `rp2350.repl`, run `renode --console --disable-gui script.resc`; tests via `renode-test`. Note the 1.16.1 pin in matgla's README vs 1.17.0 in the tap.
- Wokwi: create an account, obtain `WOKWI_CLI_TOKEN` at https://wokwi.com/dashboard/ci , `curl -L https://wokwi.com/ci/install.sh | sh`. Only RP2040 targets; 50 cloud minutes/month free.
- QEMU: `brew install qemu` gives no RP2350 machine; building the RFC v3 tree gives RP2040 only.

## Implications for cwht

- **DECISION-needed (ADR):** Select c1570/rp2350js (ARM mode, pinned commit, vendored under `tools/emu/`) as the *Emulation* evidence-class tool named in charter section 9; record Renode as the fallback and Wokwi/QEMU as rejected with the reasons above.
- **REQ-candidate (build/CM):** Every firmware release shall be produced as an `rp2350-arm-s` UF2 with a picobin IMAGE_DEF block (as rustos already does) so the same image boots through the stock bootrom in emulation and on hardware; the version description (SWE-063) shall record the emulator commit hash and the bootrom revision emulated (A2) versus the revision on the delivered silicon (A2/A3/A4).
- **REQ-candidate (firmware interface):** The firmware shall expose a UART0 text trace channel usable by emulation scenarios for pass/fail assertions (equivalent of Wokwi `--expect-text`), and the trace format shall be specified in the ICD.
- **REQ-candidate (V&V plan):** Emulation scenarios shall inject straight-key and iambic-paddle GPIO stimulus from a timed table (dit/dah/space profiles at several WPM, squeeze and iambic-B release cases) and shall check keyed-output GPIO timing at the instruction level, per the owner's stated requirement that both straight keys and iambic paddles are supported. rp2350js supports this via `gpio[n].setInputValue()` inside the step loop.
- **REQ-candidate (V&V plan):** Timing requirements (keying element timing, PA sequencing delays, sidetone frequency) shall be verified by Bench test, not Emulation; emulation closes only functional/logic behaviour, because emulated cycle counts are not validated (F13).
- **RISK-candidate:** rp2350js ARM mode lacks timer/system interrupts and exceptions (F12, F14); cwht's keyer and sequencer depend on them. Mitigation: prove rustos's timer-alarm and GPIO-IRQ paths in the emulator during the first firmware sprint; fix or extend the emulator and upstream the change; escalate to Renode if the gap is structural.
- **RISK-candidate:** Single-maintainer dependency (c1570; 7 stars) with an unstable API (`coreArch` default is `riscv`, not silicon's `arm`). Mitigation: pin the commit, vendor, and keep the cwht harness thin.
- **RISK-candidate:** Device models for the Si5351 (I2C) and SPI LCD are written by us and become part of the evidence chain; a wrong model can pass wrong firmware. Mitigation: derive the Si5351 register model from the Skyworks datasheet/AN619 and review it independently (charter section 11 rule 4); cross-check register writes against a bench-captured I2C trace once hardware exists.
- **RISK-candidate:** Two CPU flavours: rustos targets `thumbv8m.main-none-eabihf`; several RP2350 emulators are RISC-V-only (GhLabs, early c1570). Keep the ARM decision explicit in the ADR and in the emulator invocation.
- **ACTION:** Create `tools/emu/` with the pinned submodule, a `package.json` scenario runner, and the first three scenarios: boot-to-idle with UART banner, straight-key press to keyed-output GPIO, and Si5351 initialisation sequence captured from the I2C hook.
- **ACTION:** Write the Si5351 I2C model (register map, PLL/MultiSynth readback) and an ST77xx-class SPI LCD model that renders a PNG per frame (mirror of Wokwi's framebuffer idea) for visual-closure review (charter rule 3).
- **ACTION:** Open a tracking issue against c1570/rp2350js for ARM timer/NVIC interrupts once the failing case from F14 is reduced to a minimal repro; consider funding or contributing.
- **ACTION (optional, later):** Evaluate the transpiled-C build (`cts2c`) for CI speed once scenarios exceed a few seconds of simulated time.

## Confidence

| Finding | Confidence |
|---|---|
| F1 Wokwi has no RP2350 | High |
| F2 rp2040js#142 status and maintainer stance | High |
| F3 Wokwi CLI is cloud, metered, token required | High |
| F4 Wokwi chips API adequate in principle | High (API) / Low (relevance) |
| F5 Upstream Renode has no RP2xxx, has Cortex-M33 | High |
| F6 matgla Renode_RP2040 coverage, frozen | High |
| F7 Renode_RP2350 port exists, untested | High (content) / Low (fitness) |
| F8 Renode macOS install via brew tap | High |
| F9 No upstream QEMU RP2040/RP2350 | High |
| F10 QEMU task #3125 open, maintainer discouraging | High |
| F11 RP2040-only RFC v3, missing I2C/SPI/PWM/ADC/PIO | High |
| F12 rp2350js capabilities and gaps | High |
| F13 Owner's Rust UF2 runs; timing not credible | High / Medium |
| F14 SDK blink stalls in sleep_ms on ARM path | High (observed) / Medium (cause) |
| F15 GhLabs is RISC-V only | High |
| F16 picoem: validated M33 core, stub peripherals | High |
| F17 picoemu: unverified, very new | Medium / Low |
| F18 PIO-only simulators | High |

## Open items

1. Confirm on the real Pico 2 which bootrom stepping (A2/A3/A4) the owner's boards carry (`picotool info` over USB); rp2350js embeds A2 only.
2. Reduce F14 to a minimal repro and determine whether the failure is the timer alarm IRQ, NVIC priority handling, or `wfe`; check whether rustos's own timer/IRQ code (not the pico-sdk) hits the same gap.
3. Determine whether PWM slices 8-11 (RP2350 has 12) are needed by cwht's sidetone/backlight design; rp2350js models 8.
4. Wokwi for VS Code licence terms for personal use were not readable from the docs (licence is requested through the extension; pricing lists it under Hobby+). Irrelevant unless Wokwi gains RP2350.
5. Renode 1.17.0 compatibility with matgla's 1.16.1-pinned C# peripherals is untested on macOS; the `libpiosim.dylib` architecture (arm64 vs x86_64) was not checked.
6. picoem's roadmap for real (non-stub) UART/SPI/I2C/timer models is unknown; if those land, a Rust-native, QEMU-validated platform would fit the owner's toolchain better than Node.
7. The GitLab task #3125 shows 3 comments; the full text beyond the first 500 characters of each was not captured.
