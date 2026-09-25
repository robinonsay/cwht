// Minimal register-level reproductions of rp2350js ARM-path model defects found
// during cwht accreditation. No firmware: pokes the bus model directly.
// Usage: npx ts-node demo/cwht-regprobe.ts
import { RP2350 } from '../src';
import { LogLevel } from '../src/utils/logging';

const mcu = new RP2350({ coreArch: 'arm' });
(mcu.logger as any).currentLogLevel = LogLevel.Error; // silence the expected warnings
const hex = (v: number) => '0x' + (v >>> 0).toString(16);
const check = (name: string, got: number, want: number, note = '') =>
  console.log(`${got === want ? 'PASS' : 'FAIL'} ${name}: got ${hex(got)} want ${hex(want)} ${note}`);

// 1. SysTick registers (Arm: SYST_CSR 0xE000E010, RVR 0xE000E014, CVR 0xE000E018)
mcu.writeUint32(0xe000e014, 0xffffff);
mcu.writeUint32(0xe000e010, 0x5);
check('SysTick CSR readback at 0xE000E010', mcu.readUint32(0xe000e010), 0x5, '(emulator maps SysTick at +0x10: 0xE000E020..2C)');
mcu.writeUint32(0xe000e024, 0xffffff);
mcu.writeUint32(0xe000e020, 0x5);
console.log(`info SysTick CSR readback at 0xE000E020 (mislocated): ${hex(mcu.readUint32(0xe000e020))}`);

// 2. NVIC IPR0 (Arm: 0xE000E400 + 4n)
mcu.writeUint32(0xe000e400, 0x80);
check('NVIC IPR0 readback at 0xE000E400', mcu.readUint32(0xe000e400), 0x80, `nvicPriority[0]=${mcu.ppb!.coreState[0].nvicPriority[0]} (emulator decodes IPR at 0xE000E500)`);
mcu.writeUint32(0xe000e500, 0x80);
console.log(`info after write to 0xE000E500: nvicPriority[0]=${mcu.ppb!.coreState[0].nvicPriority[0]} readback ${hex(mcu.readUint32(0xe000e500))}`);

// 3. IO_BANK0 interrupt registers (RP2350: INTR0 0x230, PROC0_INTE0 0x248, PROC0_INTS0 0x278)
mcu.writeUint32(0x40028248, 0x400); // GPIO2 EDGE_LOW enable
check('IO_BANK0 PROC0_INTE0 readback', mcu.readUint32(0x40028248), 0x400, `gpio[2].irqEnableMask=${mcu.gpio[2].irqEnableMask}`);
mcu.gpio[2].setInputValue(true);
mcu.gpio[2].setInputValue(false);
console.log(`info after GPIO2 falling edge: INTR0=${hex(mcu.readUint32(0x40028230))} gpio[2].irqStatus=${hex(mcu.gpio[2].irqStatus)} PROC0_INTS0=${hex(mcu.readUint32(0x40028278))} nvicPending0=${hex(mcu.ppb!.coreState[0].nvicPending[0])}`);

// 4. PWM RP2350 register map (EN 0x0f0, INTR 0x0f4, IRQ0_INTE 0x0f8; CH8..CH11 at 0x0a0..0x0ec)
mcu.writeUint32(0x400a80f0, 0x10);
check('PWM EN (0x0f0) readback', mcu.readUint32(0x400a80f0), 0x10);
mcu.writeUint32(0x400a80a4, 0x10); // CH8_DIV
check('PWM CH8_DIV (0x0a4) readback', mcu.readUint32(0x400a80a4), 0x10, '(emulator treats 0x0a4 as RP2040 INTR)');
mcu.writeUint32(0x400a80f8, 0x10); // IRQ0_INTE slice 4
check('PWM IRQ0_INTE (0x0f8) readback', mcu.readUint32(0x400a80f8), 0x10);

// 5. PWM slice keeps running after CSR.EN=0 if DIV is written afterwards (Timer32.prescaler setter)
const ch4 = 0x400a8000 + 0x14 * 4;
mcu.writeUint32(ch4 + 0x10, 999);
mcu.writeUint32(ch4 + 0x04, 1 << 4);
mcu.writeUint32(ch4 + 0x00, 1); // EN
mcu.writeUint32(ch4 + 0x00, 0); // disable
const enA = (mcu.pwm.channels[4] as any).timer.enable;
mcu.writeUint32(ch4 + 0x04, 1 << 4); // DIV write while disabled
const enB = (mcu.pwm.channels[4] as any).timer.enable;
console.log(`${enB === false ? 'PASS' : 'FAIL'} PWM slice 4 timer.enable after CSR.EN=0 then DIV write: before=${enA} after=${enB} (want false)`);

// 6. TIMER0 alarm scheduled from a fractional microsecond fires early (truncation)
const m2 = new RP2350({ coreArch: 'arm' });
(m2.logger as any).currentLogLevel = LogLevel.Error;
m2.clock.tick(700); // now = 0.7 us
m2.writeUint32(0x400b0010, 1000); // ALARM0 = 1000 us
const fireAt = m2.clock.nanos + m2.clock.nanosToNextAlarm;
console.log(`${fireAt >= 1_000_000 ? 'PASS' : 'FAIL'} TIMER0 ALARM0=1000us armed at 0.7us fires at ${fireAt} ns (hardware: >= 1000000 ns)`);

// 7. Pull-up not reflected on an undriven input
const m3 = new RP2350({ coreArch: 'arm' });
(m3.logger as any).currentLogLevel = LogLevel.Error;
m3.writeUint32(0x40038000 + 0x04 + 4 * 2, 0b0100_1000 | 0b0100_0000 | 0b1000_0000); // GPIO2 pad: PUE|IE|OD
m3.writeUint32(0x40028000 + 0x04 + 8 * 2, 5); // FUNCSEL SIO
console.log(`${(m3.readUint32(0xd0000004) >>> 2) & 1 ? 'PASS' : 'FAIL'} SIO GPIO_IN bit2 with pull-up and nothing driving: ${hex(m3.readUint32(0xd0000004))} (hardware reads 1)`);

// 8. Watchdog tick model constant and clk_sys
console.log(`info emulator clkSys=${mcu.clkSys} Hz clkPeri=${mcu.clkPeri} Hz; simulation clock ns per cycle = ${1e9 / mcu.clkSys}`);
console.log(`info XOSC STATUS read (unimplemented peripheral) = ${hex(mcu.readUint32(0x40048004))}; TICKS TIMER0_CTRL read = ${hex(mcu.readUint32(0x40108018))}`);
