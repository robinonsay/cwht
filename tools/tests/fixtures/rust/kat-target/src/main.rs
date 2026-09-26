//! Known-answer fixture image (tools/tests/fixtures/rust/known-answers.json).
//!
//! Contents, all fixed: a two-word vector table (initial SP 0x2000_4000, reset vector),
//! a pico-sdk binary-info header with one program-name entry "cwht-kat-fixture" (the
//! value `picotool info` reads back), the five-word RP2350 IMAGE_DEF block for an Arm
//! Secure executable (RP2350 datasheet section 5.9; rustos tutorial 04 section 4.4),
//! and a reset handler that spins. It is never flashed for the record.
#![no_std]
#![no_main]

use core::panic::PanicInfo;

core::arch::global_asm!(
    r#"
    .section .vector_table, "a"
    .p2align 2
    .word 0x20004000
    .word reset

    .section .binary_info_header, "a"
    .p2align 2
    .word 0x7188ebf2
    .word __binary_info_start
    .word __binary_info_end
    .word kat_data_cpy_table
    .word 0xe71aa390

    .section .image_def, "a"
    .p2align 2
    .word 0xffffded3
    .word 0x10210142
    .word 0x000001ff
    .word 0x00000000
    .word 0xab123579

    .section .binary_info.keep.kat, "a"
    .p2align 2
    .word kat_bi_program_name

    .section .rodata.kat_bi, "a"
    .p2align 2
kat_data_cpy_table:
    .word 0
kat_bi_program_name:
    .hword 6
    .hword 0x5052
    .word 0x02031c86
    .word kat_program_name_str
kat_program_name_str:
    .asciz "cwht-kat-fixture"
"#
);

/// Reset handler: spins forever.
#[unsafe(no_mangle)]
pub extern "C" fn reset() -> ! {
    loop {
        core::hint::spin_loop();
    }
}

#[panic_handler]
fn panic(_info: &PanicInfo) -> ! {
    loop {
        core::hint::spin_loop();
    }
}
