// cwht emulator accreditation harness for c1570/rp2350js (ARM / Cortex-M33 path).
// Usage: npx ts-node demo/cwht-accredit.ts <fw.uf2|.hex> <maxCycles> [scenario]
// Scenarios: none | uart-echo | gpio-irq | i2c | spi | adc | watchdog | usb | stall-diag
// Output: UART0 lines with cycle stamps, GPIO edge log and interval statistics,
// scenario PASS/FAIL lines, and the emulator's own warnings (unimplemented
// register accesses) on stderr.
import { RP2350 } from '../src';
import { GPIOPinState } from '../src/gpio-pin';

const file = process.argv[2];
const maxCycles = Number(process.argv[3] ?? 100_000_000);
const scenario = process.argv[4] ?? 'none';

const mcu = new RP2350({ coreArch: 'arm', loadFirmware: file });
const CLK_SYS = mcu.clkSys; // emulator's own notion of clk_sys

let uartLine = '';
let uartAll = '';
let doneAtCycle = -1;
mcu.uart[0].onByte = (v: number) => {
  const ch = String.fromCharCode(v);
  uartAll += ch;
  if (ch === '\n') {
    console.log(`[uart @${mcu.cycles}] ${uartLine}`);
    if (uartLine === 'DONE' && doneAtCycle < 0) doneAtCycle = mcu.cycles;
    uartLine = '';
  } else {
    uartLine += ch;
  }
};

interface Edge { pin: number; state: GPIOPinState; cycle: number; nanos: number }
const edges: Edge[] = [];
for (const pin of [25, 24, 23]) {
  mcu.gpio[pin].addListener((state: GPIOPinState, oldState: GPIOPinState) => {
    // Only real output transitions (Low<->High); ignore Input<->driven changes at pad setup.
    const isLevel = (s: GPIOPinState) => s === GPIOPinState.Low || s === GPIOPinState.High;
    if (isLevel(state) && isLevel(oldState)) {
      edges.push({ pin, state, cycle: mcu.cycles, nanos: mcu.clock.nanos });
    }
  });
}

const scenarioLog: string[] = [];
const feedQueue: { atCycle: number; fn: () => void }[] = [];
const ECHO_MSG = 'CQ CQ DE W1AW K\n';
let wdTriggerCycle = -1;
let usbEnabledCycle = -1;

switch (scenario) {
  case 'uart-echo': {
    let c = 5_000_000;
    for (const ch of ECHO_MSG) {
      feedQueue.push({ atCycle: c, fn: () => mcu.uart[0].feedByte(ch.charCodeAt(0)) });
      c += 2_000;
    }
    break;
  }
  case 'gpio-irq': {
    mcu.gpio[2].setInputValue(true); // idle high (pull-up on hardware)
    for (let i = 0; i < 5; i++) {
      const t = 10_000_000 + i * 10_000_000;
      feedQueue.push({ atCycle: t, fn: () => mcu.gpio[2].setInputValue(false) });
      feedQueue.push({ atCycle: t + 2_000_000, fn: () => mcu.gpio[2].setInputValue(true) });
    }
    break;
  }
  case 'i2c': {
    const i2c = mcu.i2c[0];
    i2c.onStart = (rs) => { scenarioLog.push(`I2C start restart=${rs} @${mcu.cycles}`); i2c.completeStart(); };
    i2c.onConnect = (addr, mode) => { scenarioLog.push(`I2C connect addr=0x${addr.toString(16)} mode=${mode}`); i2c.completeConnect(addr === 0x60); };
    i2c.onWriteByte = (v) => { scenarioLog.push(`I2C write 0x${v.toString(16)}`); i2c.completeWrite(true); };
    i2c.onReadByte = (ack) => { scenarioLog.push(`I2C read ack=${ack}`); i2c.completeRead(0x42); };
    i2c.onStop = () => { scenarioLog.push(`I2C stop @${mcu.cycles}`); i2c.completeStop(); };
    break;
  }
  case 'spi': {
    const spi = mcu.spi[0];
    spi.onTransmit = (v) => { scenarioLog.push(`SPI tx 0x${v.toString(16)} @${mcu.cycles} cs=${mcu.gpio[17].value}`); spi.completeTransmit(v ^ 0xff); };
    break;
  }
  case 'adc': {
    mcu.adc.channelValues[0] = 0x123;
    mcu.adc.channelValues[1] = 0x456;
    break;
  }
  case 'watchdog': {
    mcu.watchdog.onWatchdogTrigger = () => { wdTriggerCycle = mcu.cycles; scenarioLog.push(`WATCHDOG trigger @${mcu.cycles} (${(mcu.clock.nanos / 1e3).toFixed(1)} us)`); };
    break;
  }
  case 'usb': {
    mcu.usbCtrl.onUSBEnabled = () => { usbEnabledCycle = mcu.cycles; scenarioLog.push(`USB enabled @${mcu.cycles}`); };
    break;
  }
  case 'allpins': {
    // Count Low<->High transitions on every GPIO (which pin does this image drive?).
    const counts = new Map<number, number>();
    const isLevel = (s: GPIOPinState) => s === GPIOPinState.Low || s === GPIOPinState.High;
    mcu.gpio.forEach((g, i) => g.addListener((s: GPIOPinState, o: GPIOPinState) => {
      if (isLevel(s) && isLevel(o)) counts.set(i, (counts.get(i) ?? 0) + 1);
      else scenarioLog.push(`GPIO${i} pad state ${GPIOPinState[o]} -> ${GPIOPinState[s]} @${mcu.cycles}`);
    }));
    process.on('exit', () => console.log(`[allpins] transitions per GPIO: ${JSON.stringify([...counts.entries()])}`));
    break;
  }
}

const t0 = Date.now();
let threw: string | null = null;
try {
  while (mcu.cycles < maxCycles) {
    mcu.step();
    if (feedQueue.length && mcu.cycles >= feedQueue[0].atCycle) {
      feedQueue.shift()!.fn();
    }
    if (doneAtCycle >= 0 && mcu.cycles > doneAtCycle + 200_000) break;
    if (scenario === 'watchdog' && wdTriggerCycle >= 0 && mcu.cycles > wdTriggerCycle + 100_000) break;
  }
} catch (e) {
  threw = String(e);
}
const wall = Date.now() - t0;
if (uartLine) console.log(`[uart @${mcu.cycles}] ${uartLine} (no newline)`);

// GPIO edge report, phases delimited by GPIO24 edges.
const g24 = edges.filter((e) => e.pin === 24).map((e) => e.cycle);
const bounds = [0, ...g24, Number.MAX_SAFE_INTEGER];
const g25 = edges.filter((e) => e.pin === 25);
console.log(`GPIO25 edges: ${g25.length}; GPIO24 phase marks: ${g24.length}; GPIO23 (hardfault) edges: ${edges.filter((e) => e.pin === 23).length}`);
for (let p = 0; p + 1 < bounds.length; p++) {
  const inPhase = g25.filter((e) => e.cycle >= bounds[p] && e.cycle < bounds[p + 1]);
  if (inPhase.length < 2) {
    if (inPhase.length) console.log(`  phase ${p}: ${inPhase.length} edge(s) at ${inPhase.map((e) => e.cycle).join(',')}`);
    continue;
  }
  const dts: number[] = [];
  const highs: number[] = [];
  const lows: number[] = [];
  for (let i = 1; i < inPhase.length; i++) {
    const d = inPhase[i].cycle - inPhase[i - 1].cycle;
    dts.push(d);
    if (inPhase[i - 1].state === GPIOPinState.High) highs.push(d); else lows.push(d);
  }
  const stat = (a: number[]) => a.length ? `n=${a.length} min=${Math.min(...a)} max=${Math.max(...a)} mean=${(a.reduce((x, y) => x + y, 0) / a.length).toFixed(2)}` : 'n=0';
  console.log(`  phase ${p} [${bounds[p]}..${bounds[p + 1] === Number.MAX_SAFE_INTEGER ? 'end' : bounds[p + 1]}): edge intervals (cycles): ${stat(dts)}`);
  console.log(`    high: ${stat(highs)} | low: ${stat(lows)} | period(2 edges) mean=${(2 * dts.reduce((x, y) => x + y, 0) / dts.length).toFixed(2)} cycles = ${(2 * dts.reduce((x, y) => x + y, 0) / dts.length / CLK_SYS * 1e6).toFixed(3)} us at emulator clk_sys ${CLK_SYS / 1e6} MHz`);
  if (inPhase.length <= 12) console.log(`    edges: ${inPhase.map((e) => `${e.cycle}:${e.state === GPIOPinState.High ? 'H' : 'L'}`).join(' ')}`);
  else console.log(`    first edges: ${inPhase.slice(0, 6).map((e) => `${e.cycle}:${e.state === GPIOPinState.High ? 'H' : 'L'}`).join(' ')}`);
}

for (const l of scenarioLog) console.log(`[scenario] ${l}`);
switch (scenario) {
  case 'uart-echo': {
    const banner = 'uart_echo: ready\n';
    const echoed = uartAll.slice(banner.length);
    console.log(`[scenario] uart-echo ${echoed === ECHO_MSG ? 'PASS' : 'FAIL'}: echoed=${JSON.stringify(echoed)} toggles=${g25.length}`);
    break;
  }
  case 'gpio-irq':
    console.log(`[scenario] gpio-irq ${g25.length === 5 ? 'PASS' : 'FAIL'}: ${g25.length} handler toggles for 5 falling edges`);
    break;
  case 'watchdog':
    console.log(`[scenario] watchdog ${wdTriggerCycle >= 0 ? `triggered @${wdTriggerCycle} cycles = ${(wdTriggerCycle / CLK_SYS * 1e6).toFixed(1)} us (LOAD=10000 -> expect 10000 us on RP2350)` : 'did not trigger'}`);
    break;
  case 'usb':
    console.log(`[scenario] usb ${usbEnabledCycle >= 0 ? 'PASS' : 'FAIL'}: onUSBEnabled ${usbEnabledCycle >= 0 ? '@' + usbEnabledCycle : 'never called'}`);
    break;
  case 'stall-diag': {
    const c = mcu.armCore0;
    const st = mcu.ppb!.coreState[0];
    console.log(`[diag] pc=0x${c.regs.pc.toString(16)} waiting=${c.waiting} primask=${c.regs.primask} ipsr=${c.regs.ipsr} nvicEnabled=${st.nvicEnabled.map((x) => '0x' + (x >>> 0).toString(16))} nvicPending=${st.nvicPending.map((x) => '0x' + (x >>> 0).toString(16))} vtor=0x${st.vtor.toString(16)}`);
    const T = 0x400b0000;
    console.log(`[diag] TIMER0 rawl=${mcu.readUint32(T + 0x28)} alarm0..3=${[0x10, 0x14, 0x18, 0x1c].map((o) => mcu.readUint32(T + o))} armed=${mcu.readUint32(T + 0x20)} intr=${mcu.readUint32(T + 0x3c)} inte=${mcu.readUint32(T + 0x40)} ints=${mcu.readUint32(T + 0x48)}`);
    break;
  }
}
if (threw) console.log(`EMULATOR THREW at cycle ${mcu.cycles}: ${threw}`);
console.log(`Stopped after ${mcu.cycles} cycles (${(mcu.clock.nanos / 1e6).toFixed(3)} ms simulated at ${CLK_SYS / 1e6} MHz); wall ${wall} ms; ${(mcu.cycles / Math.max(wall, 1) / 1000).toFixed(1)} Mcycles/s; DONE seen: ${doneAtCycle >= 0}`);
process.exit(threw ? 2 : 0);
