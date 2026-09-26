/* Fixture layout: 2-word vector table, picotool binary-info header inside the first 256 bytes,
   RP2350 IMAGE_DEF block inside the first 4 kB, then code and read-only data. */
MEMORY
{
  FLASH : ORIGIN = 0x10000000, LENGTH = 64K
  RAM   : ORIGIN = 0x20000000, LENGTH = 16K
}
ENTRY(reset)
SECTIONS
{
  .vector_table ORIGIN(FLASH) : { KEEP(*(.vector_table)) } > FLASH
  .binary_info_header : ALIGN(4) { KEEP(*(.binary_info_header)) } > FLASH
  .image_def : ALIGN(4) { KEEP(*(.image_def)) } > FLASH
  .text : ALIGN(4) { *(.text .text.*) } > FLASH
  .rodata : ALIGN(4) { *(.rodata .rodata.*) } > FLASH
  .binary_info : ALIGN(4) { __binary_info_start = .; KEEP(*(.binary_info.keep*)) __binary_info_end = .; } > FLASH
  /DISCARD/ : { *(.ARM.exidx .ARM.exidx.*) }
}
