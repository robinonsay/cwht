//! Watchdog timeout test: LOAD = 10000 ticks (10 ms at the 1 us tick), then
//! toggle GPIO25 every 1 ms until the watchdog fires.
#![no_std]
#![no_main]
#[macro_use]
#[path = "../rt.rs"]
mod rt;
use rt::*;

default_irqs!(TIMER0_IRQ_0, PWM_IRQ_WRAP_0, IO_IRQ_BANK0, UART0_IRQ);

const CTRL: usize = 0x00;
const LOAD: usize = 0x04;
const REASON: usize = 0x08;
const SCRATCH0: usize = 0x0c;

pub fn app_main() -> ! {
    unreset(RST_IO_BANK0 | RST_PADS_BANK0);
    gpio_out(25);
    uart_init();
    timer0_init();
    uart_puts("watchdog: start");
    kv("reason", rd(WATCHDOG + REASON));
    kv("scratch0", rd(WATCHDOG + SCRATCH0));
    uart_putc(b'\n');
    // Tick generator for the watchdog (TICKS.WATCHDOG at 0x30/0x34).
    wr(TICKS + 0x34, 12);
    wr(TICKS + 0x30, 1);
    wr(WATCHDOG + SCRATCH0, 0xc0ffee);
    wr(WATCHDOG + LOAD, 10_000);
    wr(WATCHDOG + CTRL, 1 << 30); // ENABLE
    let t0 = timer_rawl();
    loop {
        delay_us(1000);
        gpio_xor(25);
        let dt = timer_rawl().wrapping_sub(t0);
        if dt % 5000 < 1000 {
            uart_puts("WD");
            kv("us", dt);
            kv("time", rd(WATCHDOG + CTRL) & 0xff_ffff);
            uart_putc(b'\n');
        }
        if dt > 30_000 {
            uart_puts("WD no reset after 30 ms\nDONE\n");
            loop {
                wfi();
            }
        }
    }
}
