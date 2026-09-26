# What SRR baselines, in plain language

Reading aid for the owner at the SRR session, 2026-09-26. It is not a controlled product: the requirement files and the ConOps are the controlling text, and this summary cites them by number so any line can be checked.

- System requirements: `docs/requirements/sys/requirements.json` (181 live, 2 retired)
- Transmitter requirements: `docs/requirements/tx/requirements.json` (16)
- Keyer software requirements: `docs/requirements/sw/sw-keyer/requirements.json` (39)
- Concept of operations: `docs/conops/conops.md`

About half the numbers below are provisional. The requirement exists and is baselined, but the exact value is marked "to be confirmed" and must be settled by PDR. That applies to 115 of the 181 system requirements, 14 of the 16 transmitter requirements and 11 of the 39 keyer requirements.

## Part 1. The requirements

### The system as a whole (181 requirements)

**Basics and safety habits (SYS-001 to 007).** The radio sends plain on-off Morse only, no voice or data. It runs a self-test at every switch-on and will not transmit until the self-test passes. Any fault stops the transmitter within 20 ms. After a serious (latched) fault the radio will not transmit again until the cause has cleared and you acknowledge it, or you switch it off and on. Either way it re-runs its self-test first. It shows your call sign at power-on. Only the key jack can make it transmit, apart from a deliberately confirmed bench-test mode.

**Transmitter (SYS-008 to 020).**
- Transmits anywhere in the 2 m band except a small guard at each edge, and refuses to transmit outside that range.
- Frequency stays accurate to within about 370 Hz across -10 to +45 °C for a year after calibration.
- Four power levels: 0.5, 1, 2 and 5 W, each held within about 25 percent.
- Survives a missing, shorted or badly mismatched antenna for a minute of heavy keying.
- Soft keying edges with a 3 to 8 ms rise and fall, so no key clicks, and a narrow signal of at most 350 Hz wide at 50 WPM.
- Unwanted emissions stay under the legal limit at every power level. The radio must also keep them at least 60 dB below the carrier at 5 W, a deliberate margin over the legal floor of about 53 dB.
- The antenna-check carrier ("tune") uses 0.5 W unless you confirm a higher power, and it ends by itself within about 5 seconds.

**Receiver (SYS-021 to 037).**
- Covers the whole band, 144.000 to 148.000 MHz.
- Hears very weak signals, around the level a good 2 m CW receiver hears.
- Uses a narrow listening filter about 500 Hz wide that steeply rejects stations 2 kHz or more away.
- A strong nearby station does not deafen the radio or pump its volume up and down.
- Audio level stays roughly steady from very weak to very strong signals.
- Hears again within 50 ms of switching back from transmit.
- Survives a very strong signal at the antenna while receiving.
- Does not hear false stations or its own internal whistles across the band. Its own oscillator noise does not let a strong signal 10 kHz away cover a weak one, and the filter's response is flat across the passband.
- A stored calibration trim centres the filter on each unit, with no knobs to tweak.

**Keys and keyer (SYS-038 to 056, 159 to 163, 174).**
- Works with a straight key and an iambic paddle on a standard 3.5 mm stereo plug. Tip is dit or straight key, ring is dah, and sleeve is common.
- Keyer modes: Straight, Iambic A, Iambic B, Ultimatic and Bug.
- Keyer speed runs from 5 to 50 WPM in 1 WPM steps, with accurate timing.
- The sidetone and keyer respond within a few milliseconds. The transmitted signal follows within about 15 ms, with the same short delay on every element.
- Semi break-in: the radio goes back to receive after a pause you set, 3 to 30 dits long. There is no full QSK.
- Sidetone pitch is settable from 300 to 1000 Hz. A station on your frequency sounds at the same pitch as your sidetone, so matching pitch means you are zero-beat.
- Contact bounce is filtered, and your own transmit signal does not false-key the inputs.
- The key jack survives wrong voltages. The key jack, headphone jack and antenna socket all survive strong static shocks.
- Stuck-key protection comes in layers:
  - it won't transmit after power-on until the key reads open;
  - a straight-key closure longer than 5 seconds stops transmitting;
  - a runaway paddle stream is stopped;
  - a hardware timer independent of the software cuts the carrier after about 10 seconds of continuous key-down.
- The key-input mode changes only by a deliberate menu choice.

**Controls and display (SYS-057 to 070, 164, 165, 171).**
- Two knobs with push action and two buttons, plus a power switch.
- Tuning speeds up as you spin faster, from 10 Hz up to 10 kHz per click, and crosses the band in under 30 seconds.
- Volume has at least 32 steps.
- The screen always shows frequency, power, key mode, speed, battery and transmit state.
- Frequency digits are at least 4 mm tall and readable at arm's length in room light with no backlight.
- Every setting is at most two menu levels deep.
- 5 W needs a second confirming press. A new or reset radio starts at 1 W; after that it remembers the power level you last chose.
- A guest lock makes the radio receive-only, including across power cycles.
- Faults are shown in plain words within a second.
- A reminder to identify appears every 9 minutes.
- A bystander-distance reminder is shown for each power level.
- Charging status shows whenever USB is plugged in.
- A running tally shows how long you have been keyed over the last 6 and 30 minutes.

**Hearing protection (SYS-071 to 079, 157, 158, 169, 170, 173).**
- Hardware caps the headphone level. Software cannot exceed it, and even a single failed part keeps it within a safe bound.
- The everyday level is capped lower still until you acknowledge a warning. The unlock ends after 20 hours of use. It also resets at each power-on, unless you deliberately chose to keep it across power-ons.
- Receive audio mutes while you transmit and fades back smoothly.
- No clicks or pops at key-down, key-up, the switch back to receive, plugging in or switching on. A shorted headphone plug does no damage, however long it lasts.
- The headphone amplifier is off when no headphones are plugged in.
- With long key and headphone cables, you hear only the sidetone while keying.

**Battery and charging (SYS-080 to 101, 149, 153, 166 to 168).**
- Two replaceable 18650 cells in holders, no soldering.
- Charging stops at the right voltage and charges only between 0 and 45 °C.
- Independent hardware guards against overcharge, over-discharge, short circuit and a reversed cell.
- Charging refuses mismatched or damaged cells, cross-checks cell voltages two ways, and has a 15-hour safety timer.
- Draws at most 500 mA from USB and fully charges in 12 hours with the radio off.
- **No transmitting while USB is plugged in,** enforced by hardware. Receiving is fine, and charging pauses while the radio is on.
- Battery life is at least 8 hours at 1 minute of transmit per 9 of receive, and 6 hours at 1 per 4.
- A low-battery warning comes at least 15 minutes ahead. The radio then stops transmitting, and finally shuts down to protect the cells.
- Hot cells shut the radio down.
- The radio won't power up with a cell outside its safe voltage range, won't transmit if the pack voltage is too high, and stops charging if the charge doesn't taper off normally.
- Draws almost nothing when switched off, and the power switch is a real mechanical switch.
- The cell cover cannot pinch fingers.

**Physical and environment (SYS-102 to 117, 175).**
- At most 350 g with cells fitted, not counting the antenna. Fits within 140 x 70 x 40 mm, not counting antenna and knobs.
- SMA antenna connector on one end, mounted strongly enough that a bumped whip doesn't twist it loose. Rated for 500 connections, with a counterpoise attachment point beside it.
- All jacks reachable with plugs fully seated.
- Machined, anodized aluminum case with no sharp edges.
- Stays cool enough to hold, with the transmitter protected, during long key-downs.
- Works from -10 to +45 °C and survives storage at -20 to +60 °C.
- Survives a 1 m drop and light rain while upright.

**Legal and safety backstops (SYS-118 to 124, 130 to 132, 154 to 156, 180 to 183).**
- The transmitter shuts down if its amplifier overheats. There is a software shutdown and a separate hardware one that works even if the software doesn't.
- No transmission while the radio is resetting, starting up or loading firmware.
- Transmitting needs two independent "go" signals.
- A hardware backstop ends any single transmission longer than about 150 to 180 seconds.
- An independent check confirms the frequency before and during transmit.
- A sensor fault puts the radio in a safe state.
- A crash resets the radio within 2 seconds, and corrupted firmware is refused.
- Before first on-air use, an RF exposure evaluation is on file, the handbook carries every safety instruction, and the case is marked with: amateur transmitter, 144-148 MHz, 5 W nominal, licensed operators only, and a pointer to the handbook's RF exposure section.

**Firmware (SYS-126 to 129, 133 to 136, 143, 150).**
- Pico 2 controller running Rust firmware on rustos.
- The application runs unmodified on a Mac or Linux computer, so it can be tested there.
- Firmware updates go over USB with the cells removed.
- A corrupt setting falls back to its default, and settings survive power-off and cell removal.
- Factory defaults: Iambic A, 15 WPM, 600 Hz sidetone, 8-dit hang, 5 ms keying edges.
- At boot the radio reports its firmware version and self-test results over USB, with a serial test port as well.

**Building, testing and cost (SYS-125, 137 to 144, 147, 148, 151, 152, 172, 176 to 179).**
- PCBWay places every surface-mount part. You solder only the through-hole parts and the exposed-pad modules named on the hand-assembly list.
- 4-layer board built to PCBWay's standard rules. Every part PCBWay places, plus the power amplifier device, is stocked at DigiKey, Mouser or PCBWay. Parts you buy yourself have a named source and a dated quote.
- A built-in monitor output 40 dB down lets you safely connect test gear. Labeled test points are provided.
- No adjustments after assembly, only stored calibration.
- Still clean and at least 4 W into a moderately mismatched antenna.
- Quiet while receiving: no leakage out of the antenna, and the case shields its digital noise.
- Reference antennas of modest gain are supplied.
- At most five units, none sold. At most USD 610 per unit, spread over three units.
- Published open source under MIT on GitHub.

**Ready for 70 cm later (SYS-145, 146).** The band-specific parts are kept in separate blocks that a 70 cm revision can swap. There is a reserved spot for a band switch.

### The transmitter in more detail (16 requirements)

- The keying shape is the only thing that modulates the carrier.
- Same frequency range and guard as the system level.
- Two separate off-switches, amplifier enable and key, each alone hold leakage at the antenna below one millionth of a watt.
- The 0.5, 1 and 2 W settings are accurate to within about 25 percent; the 5 W accuracy is set at system level. The soft keying edge is reproduced within 10 percent.
- The keying sidebands are 60 dB down beyond 750 Hz from the carrier.
- The output filter knocks down the second harmonic by at least 40 dB, the third by at least 35 dB, and higher ones by at least 40 dB. The legal limit is met at every power level, and at 5 W into an antenna with up to a 2:1 mismatch. As a design margin, every unwanted signal is at least 60 dB below the carrier at 5 W, beyond the legal requirement.
- A frequency sample feeds the independent frequency check.
- Output never exceeds 6.3 W. That ceiling is what the RF exposure evaluation assumes.
- Carrier leakage while receiving is negligible.

### The keyer software in more detail (39 requirements)

- **Straight key:** follows your contact exactly. You choose whether tip, ring or either contact keys it.
- **Paddle:**
  - elements always finish once started, and spaces are never cut short;
  - dot and dash memory, and squeeze alternation;
  - Iambic A and B differ only in what happens when you release a squeeze, with B's switch point adjustable;
  - Ultimatic repeats the last paddle pressed;
  - Bug mode gives automatic dits and manual dahs.
- **Timing:** within half a percent even while the display and knobs are busy. Speed changes take effect at the next element. The keyer starts within 2 ms of a paddle touch and reads the key every millisecond.
- **Debounce:** a closure must hold for 2 ms and an opening for 5 ms before it counts.
- **Safety behaviour:**
  - no keying at power-on until the key reads open for half a second, with the sidetone silent during that wait;
  - a straight-key closure held 5 seconds stops transmitting, but the sidetone keeps sounding so you notice;
  - no keying if an input reads closed but no plug is present;
  - mode changes and bench tests need two separate deliberate actions;
  - key presses can never change settings, and out-of-range settings are rejected;
  - the keyer checks its own state for corruption and forces key-up within 1 ms if anything looks wrong.
- **Break-in and sidetone:** hang time is 3 to 30 dits. The sidetone starts within 1 ms of key-down.

### What your key-decision rulings change

These values move when the rulings are applied, which is item R16 after the session. The changes go through the normal review.

| Ruling | Effect on the baseline |
|---|---|
| Decision 25, band-edge guard | The guard widens from 1 kHz to 1.2 kHz. Transmit is allowed from 144.0012 to 147.9988 MHz: SYS-008, SYS-009 and TX-002. |
| Decision 37, stuck paddle | **This one loosens a written limit.** Today the paddle watchdog stops after 128 identical dots or dashes, or after 10 seconds. After the ruling it stops after 128 identical dots or dashes, or after 30 seconds of sending with no pause, where a pause is 7 dots long or half a second. A new requirement is added: if both paddles are held closed for 2 seconds, keying stops. SYS-054 is reworded. The 5-second limit on a key held down by hand is confirmed as written; it already covers the Bug-mode dash lever. |
| Decisions 38 to 40, hardware backstops | Three hardware safety nets are adopted, working even if the software fails. One ends any transmission that runs 150 to 180 seconds. One cuts RF within a tenth of a second if the amplifier heat sink goes above about 95 C. One blocks or stops RF within a tenth of a second if an independent check finds the frequency more than 10 kHz off. SYS-180, 181 and 182; the transmitter's frequency-sample output, TX-013, stays because of the last one. |
| Decisions 41 and 42, bench-test mode | Bench-test mode is limited to 0.5 W and 2 minutes, ends on reset, and is never remembered across power-off (added to SYS-179). The ConOps is updated to match: its 60-second bench-test limit becomes 2 minutes, and its stuck-paddle numbers become the new watchdog values. |
| Decisions 17 to 20, operators and guests | Each licensed friend runs a loaned unit as their own station under their own call sign. Friends run your station under your call only if you record it in writing, and then only at 0.5 or 1 W. A receive-only guest lock is included; it survives power-off and takes two deliberate steps to set or release. Unlicensed guests may key only at 0.5 or 1 W, with the licensed operator of that unit right there. |
| Decisions 36, 47 and 76 | These confirm the values already written: a 0.5 W tune carrier that ends within 5.5 s; a hardware cutoff near 10 s, between 7.5 and 13 s; break-in hang of 8 dots by default, adjustable 3 to 30, with a fixed delay of at most 12 ms before each element; battery life of at least 8 h and 6 h; low-battery limits of 3.20 V and 3.00 V per cell; power-down if the cells pass 60 C. |
| Decisions 53 to 58, receiver and amplifier concept | The plan is a single-conversion receiver. Two filter options stay open: the Inrad crystal filter is the working choice, and a second option is kept in case the Inrad quote falls short. The front end uses less current. The ST PD54008L-E is the main amplifier, with two ST parts as backups. The ruling also accepts the receiver-selectivity values still to be confirmed. The parts are design choices confirmed at PDR, not requirement text. |
| Decisions 29 and 63, 64: harmonics and hearing | Harmonic limits stay as written: the 60 dB target, and filter goals of 40, 35 and 40 dB measured from the amplifier output to the antenna. Headphones only, with a hardware ceiling of 100 mV (150 mV for any sound) and a 30 mV default until you acknowledge a warning. |
| Decisions 72, 75 and 85: battery and environment | Two battery-protection requirements are added: a further independent over-charge guard at 4.30 V per cell, and a wiring rule so the protection circuit measures each cell accurately. No transmitting while charging, enforced in hardware. The radio operates from -10 to +45 C and survives a 1 m drop and dripping water. |
| Decision 112: keyer safety checks | The five keyer requirements the software reviewers derived from the hazard analysis are kept: the plug check, the silent sidetone during the start-up wait, the paddle-memory self-check, key presses never changing settings, and the distinct-action rule. |
| Decisions 86 and 90, quantity and cost | Five boards are fabricated and three assembled, with up to five decided at CDR. The budget is USD 610 per unit. |

## Part 2. The concept of operations

**What it is.** A pocket-sized aluminum radio for Morse on the 2 m band, up to 5 W. It has:
- a whip antenna on one end;
- a small screen that reads well in daylight;
- two knobs and two buttons on the face;
- three jacks on the edges: key or paddle, headphones, and USB.

It runs on two replaceable 18650 cells charged over USB.

**Who uses it.**
- **You and your licensed friends.** A friend who borrows a unit operates it as their own station under their own call sign; your ruling on decision 17 adopted this as the default. Lending a unit under your call sign with a dated written note is the exception. Until you confirm which exposure limits apply to that friend, it runs at 0.5 W or 1 W only.
- **Unlicensed guests** may listen and tune freely. They may key only at 0.5 or 1 W with a licensee right beside them.
- **Guest lock.** A licensee can set a lock that makes the radio receive-only.

**A normal session.**
1. Plug in headphones and a key or paddle, then switch on. A short self-test runs.
2. Tune with the big knob and listen through the narrow filter.
3. Touch the paddle. The radio switches to transmit on the first dit, you hear your sidetone, and a short pause after you stop it returns to receive.
4. The screen always shows frequency, power, speed and battery.
5. Every 9 minutes it reminds you to identify.

**Power.** At a relaxed pace of about 1 minute sending per 9 listening, a charge lasts at least 8 hours. You charge with the radio off, which takes about 10 hours from empty. You can listen with USB plugged in, but charging pauses while the radio is on, and you cannot transmit. A low-battery warning comes 15 minutes before transmit stops.

**How to hold it.** The recommended way is on a table or in your lap, with the antenna at least 20 cm from your body. Holding it at chest height is fine, but keep the antenna away from your face. Keep other people at least 0.6 m from the antenna while you transmit, and 1 m during the antenna-check carrier. Holding the radio at your face is within the exposure limits for a licensed operator at any power. That rests on comparison with similar commercial radios, which is an approximate method. A guest is within limits there only at 0.5 W or 1 W, so never let a guest key above 1 W or run the antenna check at the face. The handbook tells everyone to keep the antenna away from the face.

**The radio's modes.** It is always in exactly one of these:

| Mode | What it does |
|---|---|
| Off | Nothing runs; settings are kept. |
| Charging | Radio switched off with USB plugged in. |
| Self-test | Runs at every switch-on. |
| Receive | Normal listening. |
| Transmit | Keying. |
| Tune | A short 0.5 W carrier for checking an antenna; stops by itself after about 5 seconds. |
| Bench test | Measurements into a dummy load, entered only with confirmation. |
| Firmware update | Loading new firmware over USB. |
| Fault-safe | Transmitting and charging stop, and the screen shows the cause and what to do. It stays locked until you acknowledge it after the cause is fixed, or switch off. Listening may continue if the fault allows. A second reset in a row also puts the radio here. |

Seven conditions block transmitting even in Receive. Four are settings or states: guest lock, practice mode, USB plugged in and low battery. Three are automatic: a key found closed or stuck, overheating, and a frequency too close to a band edge. The screen always names which one is active. The radio also never transmits until the self-test has passed.

**When things go wrong (scenarios OPS-013 to 022).**
- **Mono plug or stuck key:** the radio will not transmit while a key reads as closed. With a mono plug you pick the straight-key setting from the menu to clear it. A key held down is cut off after about 5 seconds for a straight key, the paddle watchdog stops a runaway paddle, and nothing can hold the transmitter on for more than 13 seconds.
- **Overheating:** transmit stops until the radio cools.
- **Missing or bad antenna:** the radio survives.
- **Charging fault:** charging stops and the fault is shown.
- **RF getting into the cables:** the radio still keys correctly.
- **Bystander too close:** the radio cannot detect people. You stop sending or turn the power down and ask them to step back. At the default 1 W, someone standing right next to you is still within the limits.
- **Unlicensed guest:** they are supervised, or the guest lock is set.
- **Near a band edge:** the radio won't transmit past the guard.
- **Reset in the middle of transmitting:** the carrier stops at once and the radio restarts safely.
- **Radio held at the face:** within limits for a licensed operator, and for a guest only at 0.5 or 1 W; discouraged in the handbook.

**Where it lives.**
- Pocket or pack, from -10 to +45 °C.
- Survives a 1 m drop and light rain while upright, but it is not waterproof.
- The screen needs light, because there is no backlight.

**Its life.**
- You order the boards. PCBWay assembles the surface-mount parts and you solder the through-hole parts.
- Each unit passes an acceptance test before it goes to a friend. At most five units exist, and none is sold.
- Firmware updates go over USB.

**Deferred to a later revision:** 70 cm, a speaker, a backlight, full QSK, message memories, beacons, automatic identification (you always send your call sign yourself), a computer keyer interface, faster 1.5 A charging, automatic mono-plug detection, a hearing-exposure tracker and an external-antenna accessory. Whether the radio turns its power down when the antenna is bad is decided at PDR.
