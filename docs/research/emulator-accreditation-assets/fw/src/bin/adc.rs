//! ADC single conversions on channel 0 and 1 (battery-voltage style read).
#![no_std]
#![no_main]
#[macro_use]
#[path = "../rt.rs"]
mod rt;
use rt::*;

default_irqs!(TIMER0_IRQ_0, PWM_IRQ_WRAP_0, IO_IRQ_BANK0, UART0_IRQ);

const CS: usize = 0x00;
const RESULT: usize = 0x04;

fn convert(ch: u32) -> (u32, u32) {
    wr(ADC + CS, 1 | (ch << 12) | (1 << 2)); // EN | AINSEL | START_ONCE
    let mut spins = 0u32;
    while rd(ADC + CS) & (1 << 8) == 0 {
        spins += 1;
        if spins > 1_000_000 {
            break;
        }
    }
    (rd(ADC + RESULT), spins)
}

pub fn app_main() -> ! {
    unreset(RST_IO_BANK0 | RST_PADS_BANK0 | RST_ADC);
    uart_init();
    timer0_init();
    // ADC pads: input enable off, output disable on (datasheet 12.4.3).
    for pin in [26usize, 27] {
        let pad = PADS_BANK0 + 0x04 + 4 * pin;
        wr(pad, (rd(pad) & !(1 << 6)) | (1 << 7));
    }
    uart_puts("adc: start\n");
    wr(ADC + CS, 1);
    let mut spins = 0u32;
    while rd(ADC + CS) & (1 << 8) == 0 {
        spins += 1;
        if spins > 1_000_000 {
            break;
        }
    }
    uart_puts("ADCEN");
    kv("spins", spins);
    uart_putc(b'\n');
    let t0 = timer_rawl();
    let (r0, s0) = convert(0);
    let t1 = timer_rawl();
    let (r1, s1) = convert(1);
    uart_puts("ADC");
    kv("ch0", r0);
    kv("ch1", r1);
    kv("spins0", s0);
    kv("spins1", s1);
    kv("conv_us", t1.wrapping_sub(t0));
    kv("cs", rd(ADC + CS));
    uart_putc(b'\n');
    uart_puts("DONE\n");
    loop {
        wfi();
    }
}
