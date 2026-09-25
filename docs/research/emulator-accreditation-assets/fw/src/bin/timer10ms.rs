//! Timing test 2: TIMER0 counter delta across 10 ms of simulated time,
//! with SysTick processor-cycle count over the same interval. The ratio
//! cyc / us is the emulator's effective clk_sys.
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
    uart_puts("timer10ms: start\n");
    for _ in 0..5 {
        let t0 = timer_rawl();
        let s0 = systick();
        let mut iters = 0u32;
        while timer_rawl().wrapping_sub(t0) < 10_000 {
            iters += 1;
        }
        let s1 = systick();
        let t1 = timer_rawl();
        gpio_xor(25);
        uart_puts("T10");
        kv("us", t1.wrapping_sub(t0));
        kv("cyc", systick_elapsed(s0, s1));
        kv("iters", iters);
        uart_putc(b'\n');
    }
    // TIMER LOCKED / SOURCE readback (RP2350-only registers 0x34 / 0x38).
    uart_puts("TIMERREG");
    kv("locked", rd(TIMER0 + 0x34));
    kv("source", rd(TIMER0 + 0x38));
    kv("ticks_ctrl", rd(TICKS + 0x18));
    uart_putc(b'\n');
    uart_puts("DONE\n");
    loop {
        wfi();
    }
}
