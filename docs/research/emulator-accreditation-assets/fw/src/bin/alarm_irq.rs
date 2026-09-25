//! TIMER0 ALARM0 interrupt test. The handler toggles GPIO25 every 1000 us
//! and re-arms. Phase A: main busy-waits; B: main sleeps in WFI; C: WFE.
#![no_std]
#![no_main]
#[macro_use]
#[path = "../rt.rs"]
mod rt;
use core::sync::atomic::{AtomicU32, Ordering};
use rt::*;

default_irqs!(PWM_IRQ_WRAP_0, IO_IRQ_BANK0, UART0_IRQ);

static COUNT: AtomicU32 = AtomicU32::new(0);
const PERIOD_US: u32 = 1000;

#[unsafe(no_mangle)]
pub extern "C" fn TIMER0_IRQ_0() {
    wr(TIMER0 + TIMER_INTR, 1); // clear ALARM_0 (write 1)
    gpio_xor(25);
    COUNT.fetch_add(1, Ordering::Relaxed);
    wr(TIMER0 + TIMER_ALARM0, timer_rawl().wrapping_add(PERIOD_US));
}

fn report(tag: &str, t0: u32) {
    uart_puts(tag);
    kv("count", COUNT.load(Ordering::Relaxed));
    kv("us", timer_rawl().wrapping_sub(t0));
    uart_putc(b'\n');
}

pub fn app_main() -> ! {
    unreset(RST_IO_BANK0 | RST_PADS_BANK0);
    gpio_out(25);
    uart_init();
    timer0_init();
    uart_puts("alarm_irq: start\n");
    // Exercise the NVIC priority register path too (IPR0 byte 0 = IRQ 0).
    nvic_set_priority(0, 0x8);
    uart_puts("IPR0");
    kv("rb", nvic_get_priority(0));
    uart_putc(b'\n');
    wr(TIMER0 + TIMER_INTE, 1);
    nvic_enable(0);
    let t0 = timer_rawl();
    wr(TIMER0 + TIMER_ALARM0, t0.wrapping_add(PERIOD_US));
    // Phase A: busy wait
    while COUNT.load(Ordering::Relaxed) < 10 {}
    report("A", t0);
    // Phase B: WFI
    while COUNT.load(Ordering::Relaxed) < 20 {
        wfi();
    }
    report("B", t0);
    // Phase C: WFE
    while COUNT.load(Ordering::Relaxed) < 30 {
        wfe();
    }
    report("C", t0);
    uart_puts("ARMED");
    kv("armed", rd(TIMER0 + TIMER_ARMED));
    kv("ints", rd(TIMER0 + TIMER_INTS));
    uart_putc(b'\n');
    uart_puts("DONE\n");
    loop {
        wfi();
    }
}
