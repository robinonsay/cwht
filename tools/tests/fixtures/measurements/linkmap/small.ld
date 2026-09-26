/* Fixture linker script: 1 KiB flash, 1 KiB RAM (tools/tests/test_measurements.py). */
MEMORY
{
  FLASH (rx)  : ORIGIN = 0x10000000, LENGTH = 1K
  RAM   (rwx) : ORIGIN = 0x20000000, LENGTH = 1K
}
