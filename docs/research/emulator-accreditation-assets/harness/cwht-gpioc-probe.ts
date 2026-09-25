// Executes the pico-sdk GPIO coprocessor instructions from blink_simple.dis in SRAM
// and checks whether SIO GPIO_OE / GPIO_OUT change.
//   100001ee: ec45 3044  gpioc_bit_oe_put  r3, r5   (MCRR p0, #4, r3, r5, c4)
//   100001f8: ec45 4040  gpioc_bit_out_put r4, r5   (MCRR p0, #4, r4, r5, c0)
// Usage: npx ts-node demo/cwht-gpioc-probe.ts
import { RP2350 } from '../src';
import { LogLevel } from '../src/utils/logging';

const hex = (v: number) => '0x' + (v >>> 0).toString(16);
const SRAM = 0x20000000;
const chip = new RP2350({ coreArch: 'arm' });
(chip.logger as any).currentLogLevel = LogLevel.Error;
const core = chip.armCore0;
chip.currentCore = 0;
// CPACR: full access to CP0 (GPIOC) and CP10/11, as the SDK runtime does; otherwise NOCP UsageFault.
chip.writeUint32(0xe000ed88, 0x3 | (0xf << 20));
// GPIO25 as SIO function so pad state follows SIO OE/OUT.
chip.writeUint32(0x40028000 + 0x04 + 8 * 25, 5);
chip.writeUint32(0x40038000 + 0x04 + 4 * 25, 0x40); // IE=1, OD=0, ISO=0

function run(words: number[], label: string, regs: Record<number, number>) {
  const MAIN = SRAM + 0x100;
  words.forEach((w, i) => chip.writeUint16(MAIN + 2 * i, w));
  for (const [r, v] of Object.entries(regs)) core.regs.r[Number(r)] = v;
  core.PC = MAIN;
  core.regs.sp = SRAM + 0x1000;
  core.regs.msp = SRAM + 0x1000;
  let err = '';
  try {
    core.executeInstruction();
  } catch (e) {
    err = String(e);
  }
  const oe = chip.readUint32(0xd0000030);
  const out = chip.readUint32(0xd0000010);
  console.log(`${label}: pc_after=${hex(core.PC)} GPIO_OE=${hex(oe)} GPIO_OUT=${hex(out)} gpio25=${chip.gpio[25].value}${err ? ' THREW ' + err : ''}`);
}

// MCRR forms used by pico-sdk when the pin is a runtime value.
run([0xec45, 0x3044], 'MCRR gpioc_bit_oe_put r3=25, r5=1 ', { 3: 25, 5: 1 });
run([0xec45, 0x4040], 'MCRR gpioc_bit_out_put r4=25, r5=1', { 4: 25, 5: 1 });
run([0xec46, 0x4040], 'MCRR gpioc_bit_out_put r4=25, r6=0', { 4: 25, 6: 0 });
// Reference: plain SIO stores do work.
chip.writeUint32(0xd0000038, 1 << 25);
chip.writeUint32(0xd0000018, 1 << 25);
console.log(`SIO store reference: GPIO_OE=${hex(chip.readUint32(0xd0000030))} GPIO_OUT=${hex(chip.readUint32(0xd0000010))} gpio25=${chip.gpio[25].value}`);
// Single-register MCR bulk form: mcr p0, #0, r0, c0, c0, #1  (gpioc_lo_out_set)
// Encoding: hw0 = 0xEE00 | (opc1<<5) | CRn ; hw1 = (Rt<<12) | (coproc<<8) | (opc2<<5) | 0x10 | CRm
run([0xee00 | (0 << 5) | 0, (0 << 12) | (0 << 8) | (1 << 5) | 0x10 | 0], 'MCR  gpioc_lo_out_set r0=1<<24', { 0: 1 << 24 });
// Datasheet 3.6.1 single-register forms (opc1 = operation, CRm = bank, opc2 = 0):
//   gpioc_lo_out_set  = mcr p0, #2, Rt, c0, c0    -> hw0 0xEE40, hw1 (Rt<<12)|0x10
//   gpioc_lo_oe_set   = mcr p0, #2, Rt, c0, c4    -> hw0 0xEE40, hw1 (Rt<<12)|0x14
//   gpioc_bit_out_xor = mcr p0, #5, Rt, c0, c0    -> hw0 0xEEA0, hw1 (Rt<<12)|0x10
chip.writeUint32(0xd0000020, 0xffffffff); // clear OUT
chip.writeUint32(0xd0000040, 0xffffffff); // clear OE
run([0xee40, (0 << 12) | 0x10], 'MCR  gpioc_lo_out_set r0=1<<24 (datasheet enc)', { 0: 1 << 24 });
run([0xee40, (0 << 12) | 0x14], 'MCR  gpioc_lo_oe_set  r0=1<<24 (datasheet enc)', { 0: 1 << 24 });
run([0xeea0, (0 << 12) | 0x10], 'MCR  gpioc_bit_out_xor r0=25   (datasheet enc)', { 0: 25 });
run([0xee00, (0 << 12) | 0x10], 'MCR  gpioc_lo_out_put r0=1<<26 (datasheet enc)', { 0: 1 << 26 });
