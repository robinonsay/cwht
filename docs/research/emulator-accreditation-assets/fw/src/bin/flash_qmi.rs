//! Flash access test through QMI direct mode: JEDEC ID (0x9F) read.
//! EMULATOR-ONLY: on hardware this must run from SRAM (XIP is unavailable
//! while direct mode is enabled); here it demonstrates whether the emulator
//! models the flash device behind the QMI (W25Q32: 0xEF 0x40 0x16).
#![no_std]
#![no_main]
#[macro_use]
#[path = "../rt.rs"]
mod rt;
use rt::*;

default_irqs!(TIMER0_IRQ_0, PWM_IRQ_WRAP_0, IO_IRQ_BANK0, UART0_IRQ);

const DIRECT_CSR: usize = 0x00;
const DIRECT_TX: usize = 0x04;
const DIRECT_RX: usize = 0x08;

pub fn app_main() -> ! {
    unreset(RST_IO_BANK0 | RST_PADS_BANK0);
    uart_init();
    timer0_init();
    uart_puts("flash_qmi: start");
    kv("csr", rd(QMI + DIRECT_CSR));
    kv("xip_word0", rd(0x1000_0000));
    uart_putc(b'\n');
    // CLKDIV=30 (bits 29:22), EN (bit 0), ASSERT_CS0N (bit 2)
    wr(QMI + DIRECT_CSR, (30 << 22) | 1 | (1 << 2));
    wr(QMI + DIRECT_TX, 0x9f);
    wr(QMI + DIRECT_TX, 0x00);
    wr(QMI + DIRECT_TX, 0x00);
    wr(QMI + DIRECT_TX, 0x00);
    let mut spins = 0u32;
    while rd(QMI + DIRECT_CSR) & (1 << 1) != 0 {
        spins += 1;
        if spins > 1_000_000 {
            break;
        }
    }
    uart_puts("QMI");
    kv("spins", spins);
    kv("csr", rd(QMI + DIRECT_CSR));
    for _ in 0..4 {
        let empty = rd(QMI + DIRECT_CSR) & (1 << 16) != 0;
        kv("rxempty", empty as u32);
        kv("rx", rd(QMI + DIRECT_RX) & 0xff);
    }
    uart_putc(b'\n');
    wr(QMI + DIRECT_CSR, 30 << 22); // deassert CS, leave direct mode
    uart_puts("DONE\n");
    loop {
        wfi();
    }
}
