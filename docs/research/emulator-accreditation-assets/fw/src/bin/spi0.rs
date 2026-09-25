//! SPI0 master test (LCD-style): 8-bit frames, mode 0, manual CS on GPIO17.
//! Sends 0xA5, 0x5A and prints what came back.
#![no_std]
#![no_main]
#[macro_use]
#[path = "../rt.rs"]
mod rt;
use rt::*;

default_irqs!(TIMER0_IRQ_0, PWM_IRQ_WRAP_0, IO_IRQ_BANK0, UART0_IRQ);

const SSPCR0: usize = 0x00;
const SSPCR1: usize = 0x04;
const SSPDR: usize = 0x08;
const SSPSR: usize = 0x0c;
const SSPCPSR: usize = 0x10;

pub fn app_main() -> ! {
    unreset(RST_IO_BANK0 | RST_PADS_BANK0 | RST_SPI0);
    uart_init();
    timer0_init();
    gpio_func(16, 1); // SPI0_RX
    gpio_func(18, 1); // SPI0_SCK
    gpio_func(19, 1); // SPI0_TX
    gpio_out(17); // CS, manual
    gpio_set(17);
    uart_puts("spi0: start\n");
    wr(SPI0 + SSPCR1, 0);
    wr(SPI0 + SSPCR0, 7); // DSS=8 bit, FRF=Motorola, SPO=0, SPH=0, SCR=0
    wr(SPI0 + SSPCPSR, 2); // 150 MHz / (2 * (1+0)) = 75 MHz (emulator ignores)
    wr(SPI0 + SSPCR1, 1 << 1); // SSE
    gpio_clr(17);
    wr(SPI0 + SSPDR, 0xa5);
    wr(SPI0 + SSPDR, 0x5a);
    let mut spins = 0u32;
    while rd(SPI0 + SSPSR) & (1 << 4) != 0 {
        spins += 1;
        if spins > 1_000_000 {
            break;
        }
    }
    gpio_set(17);
    uart_puts("SPI");
    kv("spins", spins);
    kv("sr", rd(SPI0 + SSPSR));
    let mut n = 0;
    while rd(SPI0 + SSPSR) & (1 << 2) != 0 && n < 8 {
        kv("rx", rd(SPI0 + SSPDR) & 0xff);
        n += 1;
    }
    uart_putc(b'\n');
    uart_puts("DONE\n");
    loop {
        wfi();
    }
}
