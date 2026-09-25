//! UART0 echo scenario (accreditation known answer): every received byte is
//! echoed; a newline toggles GPIO25.
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
    uart_puts("uart_echo: ready\n");
    loop {
        if let Some(b) = uart_getc(()) {
            uart_putc(b);
            if b == b'\n' {
                gpio_xor(25);
            }
        }
    }
}
