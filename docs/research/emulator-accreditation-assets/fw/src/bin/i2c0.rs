//! I2C0 master test (Si5351-style access at 7-bit address 0x60):
//! write [0x03, 0xFF], then write register pointer 0x00 and read one byte.
#![no_std]
#![no_main]
#[macro_use]
#[path = "../rt.rs"]
mod rt;
use rt::*;

default_irqs!(TIMER0_IRQ_0, PWM_IRQ_WRAP_0, IO_IRQ_BANK0, UART0_IRQ);

const IC_CON: usize = 0x00;
const IC_TAR: usize = 0x04;
const IC_DATA_CMD: usize = 0x10;
const IC_FS_SCL_HCNT: usize = 0x1c;
const IC_FS_SCL_LCNT: usize = 0x20;
const IC_RAW_INTR_STAT: usize = 0x34;
const IC_CLR_TX_ABRT: usize = 0x54;
const IC_ENABLE: usize = 0x6c;
const IC_STATUS: usize = 0x70;
const IC_RXFLR: usize = 0x78;
const IC_TX_ABRT_SOURCE: usize = 0x80;
const IC_FS_SPKLEN: usize = 0xa0;
const CMD_READ: u32 = 1 << 8;
const STOP: u32 = 1 << 9;

fn wait_idle() -> u32 {
    let mut n = 0u32;
    while rd(I2C0 + IC_STATUS) & (1 << 5) != 0 {
        // MST_ACTIVITY
        n += 1;
        if n > 1_000_000 {
            break;
        }
    }
    n
}

pub fn app_main() -> ! {
    unreset(RST_IO_BANK0 | RST_PADS_BANK0 | RST_I2C0);
    uart_init();
    timer0_init();
    gpio_func(4, 3); // I2C0_SDA
    gpio_func(5, 3); // I2C0_SCL
    uart_puts("i2c0: start\n");
    wr(I2C0 + IC_ENABLE, 0);
    // MASTER_MODE | SPEED=fast(2) | IC_RESTART_EN | IC_SLAVE_DISABLE | TX_EMPTY_CTRL
    wr(I2C0 + IC_CON, 1 | (2 << 1) | (1 << 5) | (1 << 6) | (1 << 8));
    wr(I2C0 + IC_TAR, 0x60);
    // 400 kHz at 150 MHz clk_sys: period 375 cycles (SDK split 60/40)
    wr(I2C0 + IC_FS_SCL_HCNT, 150 - 8);
    wr(I2C0 + IC_FS_SCL_LCNT, 225 - 1);
    wr(I2C0 + IC_FS_SPKLEN, 16);
    wr(I2C0 + IC_ENABLE, 1);
    // Write transaction
    wr(I2C0 + IC_DATA_CMD, 0x03);
    wr(I2C0 + IC_DATA_CMD, 0xff | STOP);
    let spins = wait_idle();
    let abrt = rd(I2C0 + IC_TX_ABRT_SOURCE);
    uart_puts("I2CW");
    kv("spins", spins);
    kv("abrt", abrt);
    kv("raw", rd(I2C0 + IC_RAW_INTR_STAT));
    uart_putc(b'\n');
    let _ = rd(I2C0 + IC_CLR_TX_ABRT);
    // Read transaction: pointer write then read with STOP
    wr(I2C0 + IC_DATA_CMD, 0x00);
    wr(I2C0 + IC_DATA_CMD, CMD_READ | STOP);
    let mut n = 0u32;
    while rd(I2C0 + IC_RXFLR) == 0 {
        n += 1;
        if n > 1_000_000 {
            break;
        }
    }
    let rx = rd(I2C0 + IC_DATA_CMD) & 0xff;
    wait_idle();
    uart_puts("I2CR");
    kv("rx", rx);
    kv("spins", n);
    kv("abrt", rd(I2C0 + IC_TX_ABRT_SOURCE));
    uart_putc(b'\n');
    uart_puts("DONE\n");
    loop {
        wfi();
    }
}
