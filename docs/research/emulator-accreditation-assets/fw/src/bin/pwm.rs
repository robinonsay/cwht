//! Timing test 3: PWM period on GPIO25 (slice 4, channel B). GPIO24 toggles
//! mark phase boundaries for the harness.
//! Phase 1: DIV=1.0, TOP=999, CC_B=500  -> period 1000 cycles, 50 % high.
//! Phase 2: DIV=10.5, TOP=149, CC_B=75  -> period 1575 cycles average.
//! Phase 3: RP2350 EN register (0x0f0) used to enable slice 4.
//! Phase 4: wrap IRQ via RP2350 IRQ0_INTE (0x0f8) + NVIC IRQ 8.
//! Phase 5: slice 8 register readback (CH8_DIV 0x0a4, CH8_TOP 0x0b0).
#![no_std]
#![no_main]
#[macro_use]
#[path = "../rt.rs"]
mod rt;
use core::sync::atomic::{AtomicU32, Ordering};
use rt::*;

default_irqs!(TIMER0_IRQ_0, IO_IRQ_BANK0, UART0_IRQ);

static WRAPS: AtomicU32 = AtomicU32::new(0);

const CH4: usize = PWM + 0x14 * 4;
const CSR: usize = 0x00;
const DIV: usize = 0x04;
const CC: usize = 0x0c;
const TOP: usize = 0x10;
const EN: usize = 0x0f0;
const INTR: usize = 0x0f4;
const IRQ0_INTE: usize = 0x0f8;
const IRQ0_INTS: usize = 0x100;

#[unsafe(no_mangle)]
pub extern "C" fn PWM_IRQ_WRAP_0() {
    wr(PWM + INTR, 1 << 4);
    WRAPS.fetch_add(1, Ordering::Relaxed);
}

fn phase_mark() {
    gpio_xor(24);
}

pub fn app_main() -> ! {
    unreset(RST_IO_BANK0 | RST_PADS_BANK0 | RST_PWM);
    gpio_out(24);
    uart_init();
    timer0_init();
    gpio_func(25, 4); // PWM_B_4
    uart_puts("pwm: start\n");

    // Phase 1
    wr(CH4 + CSR, 0);
    wr(CH4 + DIV, 1 << 4);
    wr(CH4 + TOP, 999);
    wr(CH4 + CC, 500 << 16);
    phase_mark();
    wr(CH4 + CSR, 1);
    delay_us(20_000);
    wr(CH4 + CSR, 0);
    uart_puts("PWM1 ctr=");
    uart_dec(rd(CH4 + 0x08));
    uart_putc(b'\n');

    // Phase 2
    wr(CH4 + DIV, (10 << 4) | 8);
    wr(CH4 + TOP, 149);
    wr(CH4 + CC, 75 << 16);
    phase_mark();
    wr(CH4 + CSR, 1);
    delay_us(20_000);
    wr(CH4 + CSR, 0);
    uart_puts("PWM2\n");

    // Phase 3: enable via RP2350 EN register
    wr(CH4 + DIV, 1 << 4);
    wr(CH4 + TOP, 999);
    wr(CH4 + CC, 500 << 16);
    phase_mark();
    wr(PWM + EN, 1 << 4);
    delay_us(10_000);
    uart_puts("PWM3");
    kv("en_rb", rd(PWM + EN));
    kv("csr_rb", rd(CH4 + CSR));
    uart_putc(b'\n');
    wr(PWM + EN, 0);
    wr(CH4 + CSR, 0);

    // Phase 4: wrap IRQ through the RP2350 register map
    phase_mark();
    wr(PWM + INTR, 0xfff);
    wr(PWM + IRQ0_INTE, 1 << 4);
    nvic_enable(8);
    wr(CH4 + CSR, 1);
    delay_us(10_000); // expect ~1250 wraps at 125 MHz, ~1500 at 150 MHz
    wr(CH4 + CSR, 0);
    uart_puts("PWM4");
    kv("wraps", WRAPS.load(Ordering::Relaxed));
    kv("intr", rd(PWM + INTR));
    kv("ints", rd(PWM + IRQ0_INTS));
    uart_putc(b'\n');
    wr(PWM + IRQ0_INTE, 0);

    // Phase 5: slice 8 registers (RP2350 has 12 slices)
    phase_mark();
    wr(PWM + 0x0a4, 0x10); // CH8_DIV
    wr(PWM + 0x0b0, 0x1234); // CH8_TOP
    uart_puts("PWM5");
    kv("ch8_div_rb", rd(PWM + 0x0a4));
    kv("ch8_top_rb", rd(PWM + 0x0b0));
    kv("en_rb", rd(PWM + EN));
    uart_putc(b'\n');
    uart_puts("DONE\n");
    loop {
        wfi();
    }
}
