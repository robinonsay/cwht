//! USB device controller bring-up to the point of CONTROLLER_EN and PULLUP_EN.
#![no_std]
#![no_main]
#[macro_use]
#[path = "../rt.rs"]
mod rt;
use rt::*;

default_irqs!(TIMER0_IRQ_0, PWM_IRQ_WRAP_0, IO_IRQ_BANK0, UART0_IRQ);

const MAIN_CTRL: usize = 0x40;
const SIE_CTRL: usize = 0x4c;
const SIE_STATUS: usize = 0x50;
const USB_MUXING: usize = 0x74;
const USB_PWR: usize = 0x78;

pub fn app_main() -> ! {
    unreset(RST_IO_BANK0 | RST_PADS_BANK0 | RST_USBCTRL);
    uart_init();
    timer0_init();
    uart_puts("usb: start\n");
    wr(USB + USB_MUXING, 1 | (1 << 3)); // TO_PHY | SOFTCON
    wr(USB + USB_PWR, (1 << 2) | (1 << 3)); // VBUS_DETECT | VBUS_DETECT_OVERRIDE_EN
    wr(USB + MAIN_CTRL, 1); // CONTROLLER_EN (device)
    wr(USB + SIE_CTRL, 1 << 16); // PULLUP_EN
    delay_us(2000);
    uart_puts("USB");
    kv("main_ctrl", rd(USB + MAIN_CTRL));
    kv("sie_status", rd(USB + SIE_STATUS));
    uart_putc(b'\n');
    uart_puts("DONE\n");
    loop {
        wfi();
    }
}
