//! Minimal RP2350 (Pico 2, Cortex-M33) bare-metal runtime for cwht emulator
//! accreditation tests. The IMAGE_DEF block, vector-table union and reset
//! sequence follow rustos `firmware/pico2/src/lib.rs` (MIT, Robin Onsay);
//! `link.ld` is a verbatim copy of rustos `firmware/pico2/link.ld`.
//! Register offsets: RP2350 datasheet (build 2025, rustos docs/extracted copy).
#![allow(dead_code)]

use core::panic::PanicInfo;
use core::ptr::{copy_nonoverlapping, read_volatile, write_volatile};

// ---------------------------------------------------------------- boot block
/// Minimum valid Arm IMAGE_DEF (datasheet 5.9.5.1): EXE, secure, Arm, RP2350.
#[used]
#[unsafe(link_section = ".boot_info")]
static BOOT_INFO: [u32; 5] = [0xffffded3, 0x10210142, 0x000001ff, 0x00000000, 0xab123579];

unsafe extern "C" {
    static _stack_top: u32;
    static __sidata: u32;
    static __sdata: u32;
    static __edata: u32;
    static __sbss: u32;
    static __ebss: u32;
    // IRQ handlers supplied by each test binary (see `default_irqs!`).
    fn TIMER0_IRQ_0();
    fn PWM_IRQ_WRAP_0();
    fn IO_IRQ_BANK0();
    fn UART0_IRQ();
}

#[repr(C)]
#[derive(Clone, Copy)]
union Vector {
    handler: unsafe extern "C" fn(),
    reset: unsafe extern "C" fn() -> !,
    stack_top: *const u32,
    reserved: u32,
}
unsafe impl Sync for Vector {}

/// 16 system slots + 52 external IRQs (datasheet 3.2). IRQ numbers used here:
/// TIMER0_IRQ_0 = 0, PWM_IRQ_WRAP_0 = 8, IO_IRQ_BANK0 = 21, UART0_IRQ = 33.
#[used]
#[unsafe(link_section = ".vector_table")]
static VECTOR_TABLE: [Vector; 68] = {
    let mut t = [Vector { handler: DefaultHandler }; 68];
    t[0] = Vector { stack_top: &raw const _stack_top };
    t[1] = Vector { reset: OnReset };
    t[3] = Vector { handler: OnHardFault };
    t[8] = Vector { reserved: 0 };
    t[9] = Vector { reserved: 0 };
    t[10] = Vector { reserved: 0 };
    t[13] = Vector { reserved: 0 };
    t[16 + 0] = Vector { handler: TIMER0_IRQ_0 };
    t[16 + 8] = Vector { handler: PWM_IRQ_WRAP_0 };
    t[16 + 21] = Vector { handler: IO_IRQ_BANK0 };
    t[16 + 33] = Vector { handler: UART0_IRQ };
    t
};

pub const PPB_BASE: usize = 0xE000_0000;
const CPACR: usize = PPB_BASE + 0xED88;
const VTOR: usize = PPB_BASE + 0xED08;

#[unsafe(no_mangle)]
pub extern "C" fn OnReset() -> ! {
    unsafe {
        // FPU on (CP10/CP11 full access), then VTOR, .data copy, .bss zero.
        wr(CPACR, rd(CPACR) | (0b11 << 20) | (0b11 << 22));
        core::arch::asm!("dsb", "isb", options(nostack, preserves_flags));
        wr(VTOR, &raw const VECTOR_TABLE as u32);
        core::arch::asm!("dsb", "isb", options(nostack, preserves_flags));
        let src = &raw const __sidata;
        let dst = &raw const __sdata as *mut u32;
        let end = &raw const __edata as *const u32;
        copy_nonoverlapping(src, dst, (end as usize - dst as usize) / 4);
        let p = &raw const __sbss as *mut u32;
        let end = &raw const __ebss as *const u32;
        p.write_bytes(0, (end as usize - p as usize) / 4);
    }
    crate::app_main()
}

#[unsafe(no_mangle)]
pub extern "C" fn DefaultHandler() {
    loop {}
}

#[unsafe(no_mangle)]
pub extern "C" fn OnHardFault() {
    // Visible failure signature for the harness: GPIO 23 high, then park.
    gpio_out(23);
    gpio_set(23);
    loop {}
}

#[panic_handler]
fn panic(_info: &PanicInfo) -> ! {
    loop {}
}

/// Define spinning default handlers for the IRQ symbols a binary does not use.
#[macro_export]
macro_rules! default_irqs {
    ($($name:ident),* $(,)?) => {
        $(
            #[unsafe(no_mangle)]
            pub extern "C" fn $name() { loop {} }
        )*
    };
}

// ---------------------------------------------------------------- registers
#[inline(always)]
pub fn rd(addr: usize) -> u32 {
    unsafe { read_volatile(addr as *const u32) }
}
#[inline(always)]
pub fn wr(addr: usize, v: u32) {
    unsafe { write_volatile(addr as *mut u32, v) }
}

pub const ATOMIC_XOR: usize = 0x1000;
pub const ATOMIC_SET: usize = 0x2000;
pub const ATOMIC_CLR: usize = 0x3000;

// Base addresses: RP2350 datasheet section 2.2 address map.
pub const CLOCKS: usize = 0x4001_0000;
pub const RESETS: usize = 0x4002_0000;
pub const IO_BANK0: usize = 0x4002_8000;
pub const PADS_BANK0: usize = 0x4003_8000;
pub const XOSC: usize = 0x4004_8000;
pub const PLL_SYS: usize = 0x4005_0000;
pub const UART0: usize = 0x4007_0000;
pub const SPI0: usize = 0x4008_0000;
pub const I2C0: usize = 0x4009_0000;
pub const ADC: usize = 0x400a_0000;
pub const PWM: usize = 0x400a_8000;
pub const TIMER0: usize = 0x400b_0000;
pub const QMI: usize = 0x400d_0000;
pub const WATCHDOG: usize = 0x400d_8000;
pub const TICKS: usize = 0x4010_8000;
pub const USB: usize = 0x5011_0000;
pub const SIO: usize = 0xd000_0000;

// RESETS.RESET bits (datasheet 7.5, RESET register).
pub const RST_ADC: u32 = 1 << 0;
pub const RST_I2C0: u32 = 1 << 4;
pub const RST_IO_BANK0: u32 = 1 << 6;
pub const RST_PADS_BANK0: u32 = 1 << 9;
pub const RST_PLL_SYS: u32 = 1 << 14;
pub const RST_PWM: u32 = 1 << 16;
pub const RST_SPI0: u32 = 1 << 18;
pub const RST_TIMER0: u32 = 1 << 23;
pub const RST_UART0: u32 = 1 << 26;
pub const RST_USBCTRL: u32 = 1 << 28;

/// Take blocks out of reset and wait for RESET_DONE (offset 0x8).
pub fn unreset(mask: u32) {
    wr(RESETS + ATOMIC_CLR, mask);
    while rd(RESETS + 0x8) & mask != mask {}
}

// ---------------------------------------------------------------- GPIO
/// Pad: IE=1, OD=0, then FUNCSEL, then clear ISO last (datasheet 9.4, PADS).
pub fn gpio_func(pin: usize, funcsel: u32) {
    let pad = PADS_BANK0 + 0x04 + 4 * pin;
    let mut v = rd(pad);
    v &= !(1 << 7); // OD
    v |= 1 << 6; // IE
    wr(pad, v);
    wr(IO_BANK0 + 0x04 + 8 * pin, funcsel & 0x1f);
    wr(pad, rd(pad) & !(1 << 8)); // ISO
}

/// SIO push-pull output, initially low.
pub fn gpio_out(pin: usize) {
    wr(SIO + 0x20, 1 << pin); // GPIO_OUT_CLR
    wr(SIO + 0x38, 1 << pin); // GPIO_OE_SET
    gpio_func(pin, 5);
}

/// SIO input with optional pull-up (PUE bit 3) or pull-down (PDE bit 2).
pub fn gpio_in(pin: usize, pull_up: bool, pull_down: bool) {
    wr(SIO + 0x40, 1 << pin); // GPIO_OE_CLR
    let pad = PADS_BANK0 + 0x04 + 4 * pin;
    let mut v = rd(pad);
    v |= 1 << 7; // OD
    v |= 1 << 6; // IE
    v &= !((1 << 3) | (1 << 2));
    if pull_up {
        v |= 1 << 3;
    }
    if pull_down {
        v |= 1 << 2;
    }
    wr(pad, v);
    wr(IO_BANK0 + 0x04 + 8 * pin, 5);
    wr(pad, rd(pad) & !(1 << 8));
}

#[inline(always)]
pub fn gpio_set(pin: usize) {
    wr(SIO + 0x18, 1 << pin);
}
#[inline(always)]
pub fn gpio_clr(pin: usize) {
    wr(SIO + 0x20, 1 << pin);
}
#[inline(always)]
pub fn gpio_xor(pin: usize) {
    wr(SIO + 0x28, 1 << pin);
}
#[inline(always)]
pub fn gpio_read(pin: usize) -> bool {
    rd(SIO + 0x04) & (1 << pin) != 0
}

// ---------------------------------------------------------------- UART0 (PL011)
const UARTDR: usize = 0x00;
const UARTFR: usize = 0x18;
const UARTIBRD: usize = 0x24;
const UARTFBRD: usize = 0x28;
const UARTLCR_H: usize = 0x2c;
const UARTCR: usize = 0x30;

/// UART0 on GPIO0 (TX) / GPIO1 (RX), FUNCSEL 2. Divisor set for 115200 baud
/// at clk_peri = 150 MHz (IBRD 81, FBRD 24); the emulator ignores baud.
pub fn uart_init() {
    unreset(RST_UART0 | RST_IO_BANK0 | RST_PADS_BANK0);
    gpio_func(0, 2);
    gpio_func(1, 2);
    wr(UART0 + UARTIBRD, 81);
    wr(UART0 + UARTFBRD, 24);
    wr(UART0 + UARTLCR_H, (0b11 << 5) | (1 << 4)); // WLEN=8, FEN
    wr(UART0 + UARTCR, (1 << 9) | (1 << 8) | 1); // RXE | TXE | UARTEN
}

pub fn uart_putc(b: u8) {
    while rd(UART0 + UARTFR) & (1 << 5) != 0 {} // TXFF
    wr(UART0 + UARTDR, b as u32);
}

pub fn uart_puts(s: &str) {
    for b in s.bytes() {
        uart_putc(b);
    }
}

pub fn uart_getc(_: ()) -> Option<u8> {
    if rd(UART0 + UARTFR) & (1 << 4) == 0 {
        Some((rd(UART0 + UARTDR) & 0xff) as u8)
    } else {
        None
    }
}

pub fn uart_hex(v: u32) {
    uart_puts("0x");
    for i in (0..8).rev() {
        let n = ((v >> (i * 4)) & 0xf) as u8;
        uart_putc(if n < 10 { b'0' + n } else { b'a' + n - 10 });
    }
}

pub fn uart_dec(mut v: u32) {
    let mut buf = [0u8; 10];
    let mut i = buf.len();
    if v == 0 {
        uart_putc(b'0');
        return;
    }
    while v > 0 {
        i -= 1;
        buf[i] = b'0' + (v % 10) as u8;
        v /= 10;
    }
    for &b in &buf[i..] {
        uart_putc(b);
    }
}

/// key=value helper: prints " key=value" in decimal.
pub fn kv(key: &str, v: u32) {
    uart_putc(b' ');
    uart_puts(key);
    uart_putc(b'=');
    uart_dec(v);
}

// ---------------------------------------------------------------- TIMER0 / TICKS / SysTick
pub const TIMER_TIMERAWL: usize = 0x28;
pub const TIMER_ALARM0: usize = 0x10;
pub const TIMER_ARMED: usize = 0x20;
pub const TIMER_INTR: usize = 0x3c;
pub const TIMER_INTE: usize = 0x40;
pub const TIMER_INTS: usize = 0x48;

/// RP2350 TIMER0 counts ticks from TICKS.TIMER0 (datasheet 8.5, 12.8), which
/// is disabled at reset (TIMER0_CTRL.ENABLE reset 0x0). Configure it the way
/// hardware requires: 12 clk_ref cycles per tick for a 12 MHz reference.
pub fn timer0_init() {
    unreset(RST_TIMER0);
    wr(TICKS + 0x1c, 12); // TIMER0_CYCLES
    wr(TICKS + 0x18, 1); // TIMER0_CTRL.ENABLE
}

#[inline(always)]
pub fn timer_rawl() -> u32 {
    rd(TIMER0 + TIMER_TIMERAWL)
}

pub fn delay_us(us: u32) {
    let t0 = timer_rawl();
    while timer_rawl().wrapping_sub(t0) < us {}
}

const SYST_CSR: usize = PPB_BASE + 0xE010;
const SYST_RVR: usize = PPB_BASE + 0xE014;
const SYST_CVR: usize = PPB_BASE + 0xE018;

/// SysTick from the processor clock (CLKSOURCE=1), 24-bit reload 0xFFFFFF.
pub fn systick_start() {
    wr(SYST_RVR, 0x00ff_ffff);
    wr(SYST_CVR, 0);
    wr(SYST_CSR, (1 << 2) | 1);
}
#[inline(always)]
pub fn systick() -> u32 {
    rd(SYST_CVR)
}
/// Elapsed processor cycles between two SysTick reads (down counter, 24-bit).
pub fn systick_elapsed(before: u32, after: u32) -> u32 {
    before.wrapping_sub(after) & 0x00ff_ffff
}

// ---------------------------------------------------------------- NVIC
pub fn nvic_enable(irq: u32) {
    wr(PPB_BASE + 0xE100 + 4 * (irq as usize / 32), 1 << (irq % 32));
}
pub fn nvic_clear_pending(irq: u32) {
    wr(PPB_BASE + 0xE280 + 4 * (irq as usize / 32), 1 << (irq % 32));
}
/// NVIC_IPRn at 0xE000E400 + 4n, one byte per IRQ, priority in bits 7:4.
pub fn nvic_set_priority(irq: u32, prio4: u32) {
    let reg = PPB_BASE + 0xE400 + 4 * (irq as usize / 4);
    let shift = 8 * (irq % 4);
    let v = rd(reg) & !(0xff << shift);
    wr(reg, v | ((prio4 & 0xf) << 4) << shift);
}
pub fn nvic_get_priority(irq: u32) -> u32 {
    let reg = PPB_BASE + 0xE400 + 4 * (irq as usize / 4);
    (rd(reg) >> (8 * (irq % 4))) & 0xff
}

#[inline(always)]
pub fn wfi() {
    unsafe { core::arch::asm!("wfi", options(nomem, nostack, preserves_flags)) }
}
#[inline(always)]
pub fn wfe() {
    unsafe { core::arch::asm!("wfe", options(nomem, nostack, preserves_flags)) }
}
#[inline(always)]
pub fn cpsie() {
    unsafe { core::arch::asm!("cpsie i", options(nomem, nostack, preserves_flags)) }
}

/// Known instruction sequence: `subs r0,#1 ; bne` (two Thumb-16 instructions).
#[inline(never)]
pub fn spin(n: u32) {
    unsafe {
        core::arch::asm!(
            "1:",
            "subs r0, #1",
            "bne 1b",
            inout("r0") n => _,
            options(nomem, nostack)
        );
    }
}
