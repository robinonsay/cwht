//! Fallback: TIMER0 ALARM0 polled through INTR (raw) with no NVIC involvement.
#![no_std]
#![no_main]
#[macro_use]
#[path = "../rt.rs"]
mod rt;
use rt::*;

default_irqs!(TIMER0_IRQ_0, PWM_IRQ_WRAP_0, IO_IRQ_BANK0, UART0_IRQ);
const PERIOD_US: u32 = 1000;

pub fn app_main() -> ! {
    unreset(RST_IO_BANK0 | RST_PADS_BANK0);
    gpio_out(25);
    uart_init();
    timer0_init();
    uart_puts("alarm_poll: start\n");
    let t0 = timer_rawl();
    let mut armed_seen = 0u32;
    let mut cleared_seen = 0u32;
    wr(TIMER0 + TIMER_ALARM0, t0.wrapping_add(PERIOD_US));
    for i in 1..=30u32 {
        if rd(TIMER0 + TIMER_ARMED) & 1 != 0 {
            armed_seen += 1;
        }
        while rd(TIMER0 + TIMER_INTR) & 1 == 0 {}
        if rd(TIMER0 + TIMER_ARMED) & 1 == 0 {
            cleared_seen += 1;
        }
        wr(TIMER0 + TIMER_INTR, 1);
        gpio_xor(25);
        wr(TIMER0 + TIMER_ALARM0, timer_rawl().wrapping_add(PERIOD_US));
        if i % 10 == 0 {
            uart_puts("P");
            kv("count", i);
            kv("us", timer_rawl().wrapping_sub(t0));
            kv("armed_seen", armed_seen);
            kv("cleared_seen", cleared_seen);
            uart_putc(b'\n');
        }
    }
    uart_puts("DONE\n");
    loop {
        wfi();
    }
}
