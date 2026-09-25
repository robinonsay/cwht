# Emulator accreditation assets (research copy)

Sources used by `docs/research/emulator-accreditation-and-timer-irq.md` (2026-09-25). They are kept here so the measurements can be reproduced after the scratch directory `/private/tmp/cwht-emu-accredit` is gone. Intended final homes, subject to the owner's decision: `tools/emu/harness/` for the TypeScript files and `firmware/emu/` for the Rust crate.

- `fw/`: standalone `no_std` crate `emutest` for `thumbv8m.main-none-eabihf`. `link.ld` is a verbatim copy of rustos `firmware/pico2/link.ld`; `src/rt.rs` follows rustos `firmware/pico2/src/lib.rs` (IMAGE_DEF, vector table, reset). Fourteen binaries under `src/bin/`, one per test. Build: `cargo build --release`, then `picotool uf2 convert -t elf target/thumbv8m.main-none-eabihf/release/<bin> <bin>.uf2 --family rp2350-arm-s`.
- `harness/cwht-accredit.ts`: run a UF2/HEX in c1570/rp2350js ARM mode, log UART0 with cycle stamps, GPIO 25/24/23 transitions, interval statistics, scenario stimuli (`uart-echo`, `gpio-irq`, `i2c`, `spi`, `adc`, `watchdog`, `usb`, `stall-diag`, `allpins`). Copy into the emulator's `demo/` directory and run `npx ts-node demo/cwht-accredit.ts <image> <maxCycles> [scenario]`.
- `harness/cwht-regprobe.ts`: register-level reproductions of the model defects (SysTick and NVIC_IPR offsets, IO_BANK0 interrupt decode, PWM RP2350 map, PWM DIV re-enable, TIMER alarm truncation, input pull-ups).
- `harness/cwht-gpioc-probe.ts`: executes pico-sdk GPIO coprocessor instructions in SRAM and shows they do not move pins.

Emulator identity these were run against: commit `af0114cbee8e9e91574204b66f10aa2961cbf28c`, `package-lock.json` sha256 `dd88d3100bd97acdcaa3daa3c2c931590938cd5a42d72e2daf7978d684f24e05`, node v25.9.0, npm 11.12.1.
