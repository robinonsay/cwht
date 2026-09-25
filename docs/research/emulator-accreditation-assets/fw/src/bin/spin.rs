//! Timing test 1: known spin loop (`subs r0,#1; bne`), measured with SysTick
//! (processor cycles) and TIMER0 (microseconds). GPIO25 toggles bracket each run.
#![no_std]
#![no_main]
#[macro_use]
#[path = "../rt.rs"]
mod rt;
use rt::*;

default_irqs!(TIMER0_IRQ_0, PWM_IRQ_WRAP_0, IO_IRQ_BANK0, UART0_IRQ);

pub fn app_main() -> ! {
    unreset(RST_IO_BANK0 | RST_PADS_BANK0);
    gpio_out(25);
    uart_init();
    timer0_init();
    systick_start();
    uart_puts("spin: start\n");
    for &n in &[1_000u32, 10_000, 100_000, 1_000_000] {
        gpio_xor(25);
        let t0 = timer_rawl();
        let s0 = systick();
        spin(n);
        let s1 = systick();
        let t1 = timer_rawl();
        gpio_xor(25);
        uart_puts("SPIN");
        kv("n", n);
        kv("cyc", systick_elapsed(s0, s1));
        kv("us", t1.wrapping_sub(t0));
        uart_putc(b'\n');
    }
    // Reference: 8 back-to-back SysTick reads (the rp2350js cyclecheck demo
    // expects 30 cycles for this on RP2040 hardware).
    let a = systick();
    let mut w = 0u32;
    for _ in 0..8 {
        w = w.wrapping_add(systick());
    }
    let b = systick();
    uart_puts("SYSTICK8");
    kv("cyc", systick_elapsed(a, b));
    kv("w", w & 0xff);
    uart_putc(b'\n');
    // APB read cost: 8 TIMERAWL reads.
    let a = systick();
    let mut w = 0u32;
    for _ in 0..8 {
        w = w.wrapping_add(timer_rawl());
    }
    let b = systick();
    uart_puts("APB8");
    kv("cyc", systick_elapsed(a, b));
    kv("w", w & 0xff);
    uart_putc(b'\n');
    uart_puts("DONE\n");
    loop {
        wfi();
    }
}
