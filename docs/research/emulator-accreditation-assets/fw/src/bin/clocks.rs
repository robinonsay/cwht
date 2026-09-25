//! Clock tree test: XOSC start, PLL_SYS to 150 MHz, clk_sys switch, then
//! measure processor cycles per 10 ms of TIMER0 time.
#![no_std]
#![no_main]
#[macro_use]
#[path = "../rt.rs"]
mod rt;
use rt::*;

default_irqs!(TIMER0_IRQ_0, PWM_IRQ_WRAP_0, IO_IRQ_BANK0, UART0_IRQ);

fn measure(tag: &str) {
    let t0 = timer_rawl();
    let s0 = systick();
    while timer_rawl().wrapping_sub(t0) < 10_000 {}
    let s1 = systick();
    uart_puts(tag);
    kv("cyc_per_10ms", systick_elapsed(s0, s1));
    uart_putc(b'\n');
}

pub fn app_main() -> ! {
    unreset(RST_IO_BANK0 | RST_PADS_BANK0);
    uart_init();
    timer0_init();
    systick_start();
    uart_puts("clocks: start\n");
    measure("ROSC");
    // XOSC: STARTUP delay 0xc4, CTRL = ENABLE(0xfab) | FREQ_RANGE 1_15MHZ(0xaa0)
    wr(XOSC + 0x0c, 0xc4);
    wr(XOSC + 0x00, (0xfab << 12) | 0xaa0);
    let mut polls = 0u32;
    while rd(XOSC + 0x04) & (1 << 31) == 0 {
        polls += 1;
        if polls > 1_000_000 {
            break;
        }
    }
    uart_puts("XOSC");
    kv("stable", (rd(XOSC + 0x04) >> 31) & 1);
    kv("polls", polls);
    kv("status", rd(XOSC + 0x04));
    uart_putc(b'\n');
    // clk_ref <- xosc (SRC=2), tick generators at 12 cycles
    wr(CLOCKS + 0x30, 2);
    // PLL_SYS: REFDIV=1, FBDIV=125 (VCO 1500 MHz), POSTDIV1=5, POSTDIV2=2 -> 150 MHz
    unreset(RST_PLL_SYS);
    wr(PLL_SYS + 0x00, 1);
    wr(PLL_SYS + 0x08, 125);
    wr(PLL_SYS + 0x04, 0); // PWR: power on PD/VCOPD/POSTDIVPD
    let mut polls = 0u32;
    while rd(PLL_SYS + 0x00) & (1 << 31) == 0 {
        polls += 1;
        if polls > 1_000_000 {
            break;
        }
    }
    wr(PLL_SYS + 0x0c, (5 << 16) | (2 << 12));
    uart_puts("PLL");
    kv("lock", (rd(PLL_SYS + 0x00) >> 31) & 1);
    kv("polls", polls);
    uart_putc(b'\n');
    // clk_sys: SRC=1 (aux), AUXSRC=0 (pll_sys)
    wr(CLOCKS + 0x3c, 1);
    uart_puts("CLKSYS");
    kv("selected", rd(CLOCKS + 0x44));
    uart_putc(b'\n');
    measure("PLL150");
    uart_puts("DONE\n");
    loop {
        wfi();
    }
}
