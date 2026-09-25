//! GPIO IRQ test (key / paddle input path): GPIO2 input with pull-up, falling
//! edge interrupt through IO_BANK0 PROC0_INTE0 and NVIC IRQ 21; handler
//! toggles GPIO25.
#![no_std]
#![no_main]
#[macro_use]
#[path = "../rt.rs"]
mod rt;
use core::sync::atomic::{AtomicU32, Ordering};
use rt::*;

default_irqs!(TIMER0_IRQ_0, PWM_IRQ_WRAP_0, UART0_IRQ);

static COUNT: AtomicU32 = AtomicU32::new(0);
static LAST_INTR: AtomicU32 = AtomicU32::new(0);
const INTR0: usize = IO_BANK0 + 0x230;
const PROC0_INTE0: usize = IO_BANK0 + 0x248;
const PROC0_INTS0: usize = IO_BANK0 + 0x278;

#[unsafe(no_mangle)]
pub extern "C" fn IO_IRQ_BANK0() {
    let intr = rd(INTR0);
    LAST_INTR.store(intr, Ordering::Relaxed);
    wr(INTR0, 0xf << 8); // clear GPIO2 edge bits (write-1-to-clear)
    gpio_xor(25);
    COUNT.fetch_add(1, Ordering::Relaxed);
}

pub fn app_main() -> ! {
    unreset(RST_IO_BANK0 | RST_PADS_BANK0);
    gpio_out(25);
    uart_init();
    timer0_init();
    gpio_in(2, true, false);
    uart_puts("gpio_irq: start");
    kv("gpio2_in", gpio_read(2) as u32);
    uart_putc(b'\n');
    wr(INTR0, 0xf << 8); // clear stale edges
    wr(PROC0_INTE0, 0x4 << 8); // GPIO2 EDGE_LOW
    nvic_enable(21);
    let mut last = 0;
    let t0 = timer_rawl();
    loop {
        let c = COUNT.load(Ordering::Relaxed);
        if c != last {
            last = c;
            uart_puts("G");
            kv("count", c);
            kv("us", timer_rawl().wrapping_sub(t0));
            kv("intr", LAST_INTR.load(Ordering::Relaxed));
            kv("ints_now", rd(PROC0_INTS0));
            kv("gpio2_in", gpio_read(2) as u32);
            uart_putc(b'\n');
            if c >= 5 {
                uart_puts("DONE\n");
                loop {
                    wfi();
                }
            }
        }
    }
}
