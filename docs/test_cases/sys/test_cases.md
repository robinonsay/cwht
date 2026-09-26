# SYS verification cases (TC-SYS)

Rendered from `docs/test_cases/sys/test_cases.json` (module `SYS`); the JSON is the controlled record and this file is regenerated from it, never edited by hand. Author: independent test author invocation (charter section 2, IEEE 1012 independence), written from `docs/requirements/sys/requirements.json` and the process documents, before any design or code exists. Status of every case: Draft (written, not yet reviewed under `docs/process/04-verification-and-validation.md` section 8.3). Date: 2026-09-25.

## Summary

- Cases: 110; live SYS requirements covered: 181 of 181 (retired REQ-SYS-016 and REQ-SYS-123 are not cited).
- By method: Analysis 25, Demonstration 6, Inspection 11, Test 68.
- By evidence class: Bench 74, Inspection 11, Simulation 25.
- Credit rows (04 section 5.2): Test requirements close by Bench on the delivered unit (T-HW); Analysis by Simulation (A); Inspection by Inspection (I); Demonstration by owner-operated Bench runs (D). The diode-probe characterization case carries SUPPORT and never closes a requirement.
- The HostUnit and Emulation evidence named in the requirements' verification notes closes the REQ-SW children allocated at PDR and is authored with those modules; Simulation and dev-board runs named as pre-build evidence are supporting cases to be added with the design.
- Planned scripts and fixtures named in `automation_ref`, `setup` and `instruments` (for example `tools/analyze_logic_capture.py`, `tools/tinysa_scan_check.py`, `tools/rf_probe_power.py`, `hardware/sim/checks/*`, `docs/vv/fixtures/*`) do not exist yet; each is a prerequisite of the case becoming Active.

## Case index

| Case | Title | Method | Class | Requirements |
|---|---|---|---|---|
| TC-SYS-001 | A1A-only emission path: transmit-chain schematic and firmware keying-path inspection | Inspection | Inspection | REQ-SYS-001 |
| TC-SYS-002 | Operating modes part 1: every allowed transition T01 to T25 of ConOps Table 3.4-2 on the delivered unit | Test | Bench | REQ-SYS-002 |
| TC-SYS-003 | Operating modes part 2: forbidden transitions and properties F1 to F9 of ConOps section 3.4 | Test | Bench | REQ-SYS-002, REQ-SYS-183 |
| TC-SYS-004 | Transmit armed only after a power-on self-test in which every check has passed | Test | Bench | REQ-SYS-003 |
| TC-SYS-005 | Carrier end within 20 ms on every inhibit, flag and latched fault, a distinct message per fault type, and Fault-safe left only through acknowledgment after clearance or by switch-off or power removal | Test | Bench | REQ-SYS-004, REQ-SYS-005, REQ-SYS-067 |
| TC-SYS-006 | Operator call sign after every power-on and every operator setting retained across power cycles and cell removal | Test | Bench | REQ-SYS-006, REQ-SYS-135 |
| TC-SYS-007 | Transmitted Morse only from key-jack closures, and bench test mode entry only after selection and confirmation | Test | Bench | REQ-SYS-007, REQ-SYS-179 |
| TC-SYS-008 | Transmit carrier placed from 144.001 to 147.999 MHz and inhibited outside that range | Test | Bench | REQ-SYS-008, REQ-SYS-009, REQ-SYS-183 |
| TC-SYS-009 | Carrier frequency error budget over temperature and one-year aging | Analysis | Simulation | REQ-SYS-010 |
| TC-SYS-010 | Diode RF probe characterization on the dummy load (fixture case, supporting) | Test | Bench | REQ-SYS-011, REQ-SYS-012 |
| TC-SYS-011 | Output power at the 0.5, 1, 2 and 5 W steps across the band and pack voltage | Test | Bench | REQ-SYS-011, REQ-SYS-012 |
| TC-SYS-012 | Survival of 60 s of 5 W keying at 80 percent duty into open, short and SWR 10:1 loads at four phases | Test | Bench | REQ-SYS-013 |
| TC-SYS-013 | Keying envelope shape and 26 dB occupied bandwidth by transient simulation and FFT | Analysis | Simulation | REQ-SYS-014, REQ-SYS-015 |
| TC-SYS-014 | Spurious emissions from 9 kHz to 1.5 GHz at every step, three frequencies and the pack voltage extremes | Test | Bench | REQ-SYS-017, REQ-SYS-018 |
| TC-SYS-015 | Tune carrier at 0.5 W unless a higher step is confirmed, ended within 5.5 s | Test | Bench | REQ-SYS-019, REQ-SYS-020 |
| TC-SYS-016 | Reception of A1A signals from 144.000 to 148.000 MHz | Test | Bench | REQ-SYS-021 |
| TC-SYS-017 | Receiver minimum discernible signal from the noise-figure and filter-loss cascade | Analysis | Simulation | REQ-SYS-022, REQ-SYS-023 |
| TC-SYS-018 | End-to-end receive selectivity: -6 dB and -60 dB bandwidths, stopband, ultimate rejection and ripple | Analysis | Simulation | REQ-SYS-024, REQ-SYS-025, REQ-SYS-026, REQ-SYS-027, REQ-SYS-028 |
| TC-SYS-019 | Adjacent-signal desensitization and reciprocal-mixing dynamic range from selectivity and phase noise | Analysis | Simulation | REQ-SYS-029, REQ-SYS-031 |
| TC-SYS-020 | Receive level control: no gain pumping from an adjacent keyed signal and audio level over -120 to -20 dBm | Analysis | Simulation | REQ-SYS-030, REQ-SYS-032 |
| TC-SYS-021 | Image and intermediate-frequency response rejection from the front-end and mixer responses | Analysis | Simulation | REQ-SYS-033 |
| TC-SYS-022 | Internally generated receive responses from 144.010 to 147.999 MHz | Test | Bench | REQ-SYS-034 |
| TC-SYS-023 | Receive filter-centre calibration trim over +/-500 Hz in 10 Hz steps, retained across a power cycle | Demonstration | Bench | REQ-SYS-035 |
| TC-SYS-024 | Receive sensitivity recovery after hang expiry from T/R release and LNA supply settling | Analysis | Simulation | REQ-SYS-036 |
| TC-SYS-025 | Receiver survival of +27 dBm at the antenna port | Test | Bench | REQ-SYS-037 |
| TC-SYS-026 | Keying the transmitter with the owner's straight key and with the iambic paddle | Demonstration | Bench | REQ-SYS-038, REQ-SYS-039 |
| TC-SYS-027 | Keyer modes Straight, Iambic A, Iambic B, Ultimatic and Bug against the reference model | Test | Bench | REQ-SYS-040 |
| TC-SYS-028 | Keyer speed range 5 to 50 WPM in 1 WPM steps and element and space timing accuracy | Test | Bench | REQ-SYS-041, REQ-SYS-042 |
| TC-SYS-029 | Paddle-to-element latency and sidetone onset latency for key and paddle | Test | Bench | REQ-SYS-043, REQ-SYS-159 |
| TC-SYS-030 | Semi break-in hang time of 3 to 30 dits at the displayed speed | Test | Bench | REQ-SYS-044 |
| TC-SYS-031 | Sidetone frequency from 300 Hz to 1000 Hz in 10 Hz steps | Test | Bench | REQ-SYS-045 |
| TC-SYS-032 | CW pitch equals sidetone: frequency-plan analysis of receive LO, BFO and trim against the sidetone setting | Analysis | Simulation | REQ-SYS-046 |
| TC-SYS-033 | Key contact thresholds, then survival of -5 V to +12 V on each key contact, then thresholds re-checked | Test | Bench | REQ-SYS-047, REQ-SYS-049 |
| TC-SYS-034 | Key closure accepted after 2 ms of continuous contact and opening after 5 ms of continuous break | Test | Bench | REQ-SYS-048, REQ-SYS-162 |
| TC-SYS-035 | Electrostatic discharge tolerance at the key jack, headphone jack and antenna port from clamp ratings and return paths | Analysis | Simulation | REQ-SYS-050 |
| TC-SYS-036 | Key-input states unchanged while transmitting 5 W with 1.5 m unshielded leads on the key and headphone jacks | Test | Bench | REQ-SYS-051 |
| TC-SYS-037 | Key-input mode changes only by menu selection, selection accepted with a closed input, and the key-closed interlock | Test | Bench | REQ-SYS-052, REQ-SYS-056, REQ-SYS-163 |
| TC-SYS-038 | Straight-key timeout and paddle watchdog, each holding the transmitter unkeyed until the contacts read open | Test | Bench | REQ-SYS-053, REQ-SYS-054 |
| TC-SYS-039 | Hardware transmit cutoff independent of firmware, 7.5 s to 13 s into a continuous key-down | Test | Bench | REQ-SYS-055 |
| TC-SYS-040 | Enclosure CAD and BOM: operator control set, external envelope and antenna-port face | Inspection | Inspection | REQ-SYS-057, REQ-SYS-103, REQ-SYS-175 |
| TC-SYS-041 | Tuning one step per detent from 10 Hz to 10 kHz with rotation rate, and band crossing time | Test | Bench | REQ-SYS-058, REQ-SYS-164 |
| TC-SYS-042 | Headphone level set in at least 32 steps from mute to the active cap | Test | Bench | REQ-SYS-059 |
| TC-SYS-043 | Status display content in Receive, Transmit-keyed and Tune, and every setting within two menu levels | Demonstration | Bench | REQ-SYS-060, REQ-SYS-062 |
| TC-SYS-044 | Displayed frequency character height from the rendered status frame and the display pixel pitch | Inspection | Inspection | REQ-SYS-061 |
| TC-SYS-045 | 5 W selected only after a step selection followed by a separate confirmation press | Test | Bench | REQ-SYS-063 |
| TC-SYS-046 | Defaults at first power-on and after a configuration reset: 1 W, Iambic A, 15 WPM, 600 Hz, 8-dit hang, 5 ms envelope | Test | Bench | REQ-SYS-064, REQ-SYS-136 |
| TC-SYS-047 | Guest lock: no RF from any source while set, including after power cycles, and two-step set and release | Test | Bench | REQ-SYS-065, REQ-SYS-066, REQ-SYS-183 |
| TC-SYS-048 | Identification reminder 9 min 00 s +/-5 s after the first transmission following the previous reminder | Test | Bench | REQ-SYS-068 |
| TC-SYS-049 | Separation reminder per step and mode, and cumulative key-down time over 6 min and 30 min windows | Test | Bench | REQ-SYS-069, REQ-SYS-171 |
| TC-SYS-050 | USB input current, charge-state indication in every phase, and charging paused while the radio is on | Test | Bench | REQ-SYS-070, REQ-SYS-090, REQ-SYS-093 |
| TC-SYS-051 | Headphone output ceiling for a full-scale sine and for any digital audio pattern | Test | Bench | REQ-SYS-071, REQ-SYS-072 |
| TC-SYS-052 | Headphone output ceiling under every single component failure in the output path | Analysis | Simulation | REQ-SYS-073 |
| TC-SYS-053 | Default 30 mVrms audio cap until acknowledgment, restored at every power-on unless a persistent unlock is selected | Test | Bench | REQ-SYS-074, REQ-SYS-170 |
| TC-SYS-054 | Receive audio mute at key-down, hold through transmit and hang, and restore fade | Analysis | Simulation | REQ-SYS-075, REQ-SYS-157, REQ-SYS-158 |
| TC-SYS-055 | Headphone transients at key-down, key-up, hang expiry, plug insertion and power-on | Analysis | Simulation | REQ-SYS-076 |
| TC-SYS-056 | Headphone amplifier output disabled while no plug is in the headphone jack | Test | Bench | REQ-SYS-077 |
| TC-SYS-057 | Channel balance into 16 to 64 ohm at the active cap, and survival of a headphone contact short to sleeve | Test | Bench | REQ-SYS-078, REQ-SYS-079 |
| TC-SYS-058 | BOM, schematic and ICD inspection: cell holders, antenna connector, controller module and key-jack wiring | Inspection | Inspection | REQ-SYS-080, REQ-SYS-104, REQ-SYS-126, REQ-SYS-174 |
| TC-SYS-059 | Charge termination voltage per cell and charge time of a 3000 mAh pack from low-battery power-down | Test | Bench | REQ-SYS-081, REQ-SYS-091 |
| TC-SYS-060 | Charge temperature window 0 C to 45 C and cell over-temperature power-down at 60 C | Test | Bench | REQ-SYS-082, REQ-SYS-099 |
| TC-SYS-061 | Independent cell over-voltage protection between 4.25 and 4.30 V | Test | Bench | REQ-SYS-083 |
| TC-SYS-062 | Independent cell under-voltage disconnect at 2.50 V and survival of a reversed cell | Test | Bench | REQ-SYS-084, REQ-SYS-086 |
| TC-SYS-063 | Pack over-current and short-circuit trip level from the protector threshold, FET resistance and fuse rating | Analysis | Simulation | REQ-SYS-085 |
| TC-SYS-064 | Cell insertion check, dual-path cell-voltage check and rails held off for out-of-window cells | Test | Bench | REQ-SYS-087, REQ-SYS-088, REQ-SYS-166 |
| TC-SYS-065 | Charge safety timer of 15 h and constant-voltage current-fall supervision | Test | Bench | REQ-SYS-089, REQ-SYS-167 |
| TC-SYS-066 | Hardware transmit inhibit with USB present, and no transmitter supply from USB alone | Test | Bench | REQ-SYS-092, REQ-SYS-149, REQ-SYS-183 |
| TC-SYS-067 | Battery life of at least 8 h at 1:9 and the low-battery warning at least 15 min before transmit inhibit | Test | Bench | REQ-SYS-094, REQ-SYS-096 |
| TC-SYS-068 | Battery life of at least 6 h at 1:4 | Test | Bench | REQ-SYS-095 |
| TC-SYS-069 | Low-battery transmit inhibit at 3.20 V, low-battery power-down at 3.00 V and high pack-voltage transmit lockout at 8.60 V | Test | Bench | REQ-SYS-097, REQ-SYS-098, REQ-SYS-153 |
| TC-SYS-070 | Pack current with the switch off and loads removed by the mechanical power switch | Test | Bench | REQ-SYS-100, REQ-SYS-101 |
| TC-SYS-071 | Unit mass with cells fitted and without the antenna | Test | Bench | REQ-SYS-102 |
| TC-SYS-072 | Antenna-port bending moment of 4.0 N m without jack rotation, and counterpoise attachment position and resistance | Test | Bench | REQ-SYS-105, REQ-SYS-107 |
| TC-SYS-073 | Antenna-port mating life from the jack datasheet rating and the handbook torque | Analysis | Simulation | REQ-SYS-106 |
| TC-SYS-074 | Fully seated plugs at the key jack, headphone jack and micro-USB receptacle through the enclosure openings | Demonstration | Bench | REQ-SYS-108 |
| TC-SYS-075 | Enclosure material, anodize and conductive masking in the STEP, drawing and order notes | Inspection | Inspection | REQ-SYS-109 |
| TC-SYS-076 | Enclosure mechanical safety by scripted CAD checks: edge break, knob clearance and cell-cover pinch gaps | Analysis | Simulation | REQ-SYS-110, REQ-SYS-111, REQ-SYS-168 |
| TC-SYS-077 | PA junction and hand-hold surface temperature from the thermal resistance chain | Analysis | Simulation | REQ-SYS-112, REQ-SYS-113 |
| TC-SYS-078 | Operating and storage temperature ranges from every part rating | Analysis | Simulation | REQ-SYS-114, REQ-SYS-115 |
| TC-SYS-079 | Requirements met after a 1.0 m drop onto a hard floor on each face with the antenna fitted | Test | Bench | REQ-SYS-116 |
| TC-SYS-080 | Requirements met after 10 min of IEC 60529 IPX2 dripping water with plugs inserted | Test | Bench | REQ-SYS-117 |
| TC-SYS-081 | PA over-temperature inhibit and PA temperature-sensor fault response | Test | Bench | REQ-SYS-118, REQ-SYS-155 |
| TC-SYS-082 | Safe state first on reset, panic and latched fault; RF off in reset, bootloader and firmware load; hang recovery within 2 s | Test | Bench | REQ-SYS-119, REQ-SYS-130, REQ-SYS-131, REQ-SYS-183 |
| TC-SYS-083 | RF output only while both the keyer key-down and the separately maintained PA permit are asserted | Test | Bench | REQ-SYS-120, REQ-SYS-183 |
| TC-SYS-084 | RF exposure evaluation on record and reference antenna gain | Analysis | Simulation | REQ-SYS-121, REQ-SYS-172 |
| TC-SYS-085 | Operations handbook safety content checked against every documentation and operator-procedure control | Analysis | Simulation | REQ-SYS-122 |
| TC-SYS-086 | Enclosure legend artwork and engraving callout against the required legend | Analysis | Simulation | REQ-SYS-124 |
| TC-SYS-087 | Build quantity cap in the release package and the unit serial register | Inspection | Inspection | REQ-SYS-125 |
| TC-SYS-088 | Firmware platform, host-testable layering and single interrupt priority | Inspection | Inspection | REQ-SYS-127, REQ-SYS-128, REQ-SYS-129 |
| TC-SYS-089 | Fault-safe on a failed firmware-image integrity check, and defaults for corrupt or out-of-range settings | Test | Bench | REQ-SYS-132, REQ-SYS-134 |
| TC-SYS-090 | Firmware update through the micro-USB receptacle with the cells removed | Demonstration | Bench | REQ-SYS-133 |
| TC-SYS-091 | Assembly split: every surface-mount part placed by PCBWay, only through-hole parts and exposed-pad modules for the owner | Analysis | Simulation | REQ-SYS-137, REQ-SYS-138 |
| TC-SYS-092 | Circuit board stack-up, PCBWay DRC and probe test points | Inspection | Inspection | REQ-SYS-139, REQ-SYS-142 |
| TC-SYS-093 | Parts sourcing: distributor stock for turnkey parts and the PA, dated quotes for owner-procured parts | Inspection | Inspection | REQ-SYS-140, REQ-SYS-178 |
| TC-SYS-094 | Transmit monitor port attenuation of 40 dB +/-1 dB into 50 ohm | Test | Bench | REQ-SYS-141 |
| TC-SYS-095 | Boot banner over USB serial and telemetry on the UART test pads without USB | Test | Bench | REQ-SYS-143, REQ-SYS-150 |
| TC-SYS-096 | Requirements met after assembly with only the stored firmware calibration of pitch centre and reference trim | Test | Bench | REQ-SYS-144 |
| TC-SYS-097 | 70 cm readiness: band-dependent blocks partitioned and a reserved band control | Inspection | Inspection | REQ-SYS-145, REQ-SYS-146 |
| TC-SYS-098 | Unit cost from the labor-free cost model with CDR quotes | Analysis | Simulation | REQ-SYS-147 |
| TC-SYS-099 | MIT license, third-party notices and pushed baseline tags in the public repository | Inspection | Inspection | REQ-SYS-148 |
| TC-SYS-100 | Spurious emissions and rated power into SWR 2:1 loads | Test | Bench | REQ-SYS-151, REQ-SYS-152 |
| TC-SYS-101 | Synthesizer unlock or off-frequency fault and forward-power detector fault responses | Test | Bench | REQ-SYS-154, REQ-SYS-156, REQ-SYS-183 |
| TC-SYS-102 | Straight-key contact to RF rise latency and a constant lead-in across an over | Test | Bench | REQ-SYS-160, REQ-SYS-161 |
| TC-SYS-103 | Display legibility at 0.5 m under 300 lux without a backlight | Analysis | Simulation | REQ-SYS-165 |
| TC-SYS-104 | Default audio cap restored after 20 h of cumulative unlocked operation | Test | Bench | REQ-SYS-169 |
| TC-SYS-105 | Only the sidetone on the headphones while keying 5 W with 1.5 m unshielded leads | Demonstration | Bench | REQ-SYS-173 |
| TC-SYS-106 | Receive-mode emissions at the antenna port from 9 kHz to 1.5 GHz | Test | Bench | REQ-SYS-176 |
| TC-SYS-107 | Enclosure attenuation of digital and switching-converter emissions | Analysis | Simulation | REQ-SYS-177 |
| TC-SYS-108 | Transmission-length hardware backstop: RF ended at 150 s to 180 s of continuous transmit until the return to receive, independent of firmware | Test | Bench | REQ-SYS-180, REQ-SYS-183 |
| TC-SYS-109 | Hardware PA over-temperature cut-off: RF ended while the heat-sink sensor reads above 95 C, independent of firmware | Test | Bench | REQ-SYS-181, REQ-SYS-183 |
| TC-SYS-110 | Independent frequency verification: no transmission unless the measured synthesizer output agrees with the set frequency within 10 kHz, before and during transmit | Test | Bench | REQ-SYS-182, REQ-SYS-183 |

## Requirement coverage

| Requirement | Method | Cases |
|---|---|---|
| REQ-SYS-001 | Inspection | TC-SYS-001 |
| REQ-SYS-002 | Test | TC-SYS-002, TC-SYS-003 |
| REQ-SYS-003 | Test | TC-SYS-004 |
| REQ-SYS-004 | Test | TC-SYS-005 |
| REQ-SYS-005 | Test | TC-SYS-005 |
| REQ-SYS-006 | Test | TC-SYS-006 |
| REQ-SYS-007 | Test | TC-SYS-007 |
| REQ-SYS-008 | Test | TC-SYS-008 |
| REQ-SYS-009 | Test | TC-SYS-008 |
| REQ-SYS-010 | Analysis | TC-SYS-009 |
| REQ-SYS-011 | Test | TC-SYS-010, TC-SYS-011 |
| REQ-SYS-012 | Test | TC-SYS-010, TC-SYS-011 |
| REQ-SYS-013 | Test | TC-SYS-012 |
| REQ-SYS-014 | Analysis | TC-SYS-013 |
| REQ-SYS-015 | Analysis | TC-SYS-013 |
| REQ-SYS-016 | Analysis | retired, no case |
| REQ-SYS-017 | Test | TC-SYS-014 |
| REQ-SYS-018 | Test | TC-SYS-014 |
| REQ-SYS-019 | Test | TC-SYS-015 |
| REQ-SYS-020 | Test | TC-SYS-015 |
| REQ-SYS-021 | Test | TC-SYS-016 |
| REQ-SYS-022 | Analysis | TC-SYS-017 |
| REQ-SYS-023 | Analysis | TC-SYS-017 |
| REQ-SYS-024 | Analysis | TC-SYS-018 |
| REQ-SYS-025 | Analysis | TC-SYS-018 |
| REQ-SYS-026 | Analysis | TC-SYS-018 |
| REQ-SYS-027 | Analysis | TC-SYS-018 |
| REQ-SYS-028 | Analysis | TC-SYS-018 |
| REQ-SYS-029 | Analysis | TC-SYS-019 |
| REQ-SYS-030 | Analysis | TC-SYS-020 |
| REQ-SYS-031 | Analysis | TC-SYS-019 |
| REQ-SYS-032 | Analysis | TC-SYS-020 |
| REQ-SYS-033 | Analysis | TC-SYS-021 |
| REQ-SYS-034 | Test | TC-SYS-022 |
| REQ-SYS-035 | Demonstration | TC-SYS-023 |
| REQ-SYS-036 | Analysis | TC-SYS-024 |
| REQ-SYS-037 | Test | TC-SYS-025 |
| REQ-SYS-038 | Demonstration | TC-SYS-026 |
| REQ-SYS-039 | Demonstration | TC-SYS-026 |
| REQ-SYS-040 | Test | TC-SYS-027 |
| REQ-SYS-041 | Test | TC-SYS-028 |
| REQ-SYS-042 | Test | TC-SYS-028 |
| REQ-SYS-043 | Test | TC-SYS-029 |
| REQ-SYS-044 | Test | TC-SYS-030 |
| REQ-SYS-045 | Test | TC-SYS-031 |
| REQ-SYS-046 | Analysis | TC-SYS-032 |
| REQ-SYS-047 | Test | TC-SYS-033 |
| REQ-SYS-048 | Test | TC-SYS-034 |
| REQ-SYS-049 | Test | TC-SYS-033 |
| REQ-SYS-050 | Analysis | TC-SYS-035 |
| REQ-SYS-051 | Test | TC-SYS-036 |
| REQ-SYS-052 | Test | TC-SYS-037 |
| REQ-SYS-053 | Test | TC-SYS-038 |
| REQ-SYS-054 | Test | TC-SYS-038 |
| REQ-SYS-055 | Test | TC-SYS-039 |
| REQ-SYS-056 | Test | TC-SYS-037 |
| REQ-SYS-057 | Inspection | TC-SYS-040 |
| REQ-SYS-058 | Test | TC-SYS-041 |
| REQ-SYS-059 | Test | TC-SYS-042 |
| REQ-SYS-060 | Demonstration | TC-SYS-043 |
| REQ-SYS-061 | Inspection | TC-SYS-044 |
| REQ-SYS-062 | Demonstration | TC-SYS-043 |
| REQ-SYS-063 | Test | TC-SYS-045 |
| REQ-SYS-064 | Test | TC-SYS-046 |
| REQ-SYS-065 | Test | TC-SYS-047 |
| REQ-SYS-066 | Test | TC-SYS-047 |
| REQ-SYS-067 | Test | TC-SYS-005 |
| REQ-SYS-068 | Test | TC-SYS-048 |
| REQ-SYS-069 | Test | TC-SYS-049 |
| REQ-SYS-070 | Test | TC-SYS-050 |
| REQ-SYS-071 | Test | TC-SYS-051 |
| REQ-SYS-072 | Test | TC-SYS-051 |
| REQ-SYS-073 | Analysis | TC-SYS-052 |
| REQ-SYS-074 | Test | TC-SYS-053 |
| REQ-SYS-075 | Analysis | TC-SYS-054 |
| REQ-SYS-076 | Analysis | TC-SYS-055 |
| REQ-SYS-077 | Test | TC-SYS-056 |
| REQ-SYS-078 | Test | TC-SYS-057 |
| REQ-SYS-079 | Test | TC-SYS-057 |
| REQ-SYS-080 | Inspection | TC-SYS-058 |
| REQ-SYS-081 | Test | TC-SYS-059 |
| REQ-SYS-082 | Test | TC-SYS-060 |
| REQ-SYS-083 | Test | TC-SYS-061 |
| REQ-SYS-084 | Test | TC-SYS-062 |
| REQ-SYS-085 | Analysis | TC-SYS-063 |
| REQ-SYS-086 | Test | TC-SYS-062 |
| REQ-SYS-087 | Test | TC-SYS-064 |
| REQ-SYS-088 | Test | TC-SYS-064 |
| REQ-SYS-089 | Test | TC-SYS-065 |
| REQ-SYS-090 | Test | TC-SYS-050 |
| REQ-SYS-091 | Test | TC-SYS-059 |
| REQ-SYS-092 | Test | TC-SYS-066 |
| REQ-SYS-093 | Test | TC-SYS-050 |
| REQ-SYS-094 | Test | TC-SYS-067 |
| REQ-SYS-095 | Test | TC-SYS-068 |
| REQ-SYS-096 | Test | TC-SYS-067 |
| REQ-SYS-097 | Test | TC-SYS-069 |
| REQ-SYS-098 | Test | TC-SYS-069 |
| REQ-SYS-099 | Test | TC-SYS-060 |
| REQ-SYS-100 | Test | TC-SYS-070 |
| REQ-SYS-101 | Test | TC-SYS-070 |
| REQ-SYS-102 | Test | TC-SYS-071 |
| REQ-SYS-103 | Inspection | TC-SYS-040 |
| REQ-SYS-104 | Inspection | TC-SYS-058 |
| REQ-SYS-105 | Test | TC-SYS-072 |
| REQ-SYS-106 | Analysis | TC-SYS-073 |
| REQ-SYS-107 | Test | TC-SYS-072 |
| REQ-SYS-108 | Demonstration | TC-SYS-074 |
| REQ-SYS-109 | Inspection | TC-SYS-075 |
| REQ-SYS-110 | Analysis | TC-SYS-076 |
| REQ-SYS-111 | Analysis | TC-SYS-076 |
| REQ-SYS-112 | Analysis | TC-SYS-077 |
| REQ-SYS-113 | Analysis | TC-SYS-077 |
| REQ-SYS-114 | Analysis | TC-SYS-078 |
| REQ-SYS-115 | Analysis | TC-SYS-078 |
| REQ-SYS-116 | Test | TC-SYS-079 |
| REQ-SYS-117 | Test | TC-SYS-080 |
| REQ-SYS-118 | Test | TC-SYS-081 |
| REQ-SYS-119 | Test | TC-SYS-082 |
| REQ-SYS-120 | Test | TC-SYS-083 |
| REQ-SYS-121 | Analysis | TC-SYS-084 |
| REQ-SYS-122 | Analysis | TC-SYS-085 |
| REQ-SYS-123 | Test | retired, no case |
| REQ-SYS-124 | Analysis | TC-SYS-086 |
| REQ-SYS-125 | Inspection | TC-SYS-087 |
| REQ-SYS-126 | Inspection | TC-SYS-058 |
| REQ-SYS-127 | Inspection | TC-SYS-088 |
| REQ-SYS-128 | Inspection | TC-SYS-088 |
| REQ-SYS-129 | Inspection | TC-SYS-088 |
| REQ-SYS-130 | Test | TC-SYS-082 |
| REQ-SYS-131 | Test | TC-SYS-082 |
| REQ-SYS-132 | Test | TC-SYS-089 |
| REQ-SYS-133 | Demonstration | TC-SYS-090 |
| REQ-SYS-134 | Test | TC-SYS-089 |
| REQ-SYS-135 | Test | TC-SYS-006 |
| REQ-SYS-136 | Test | TC-SYS-046 |
| REQ-SYS-137 | Analysis | TC-SYS-091 |
| REQ-SYS-138 | Analysis | TC-SYS-091 |
| REQ-SYS-139 | Inspection | TC-SYS-092 |
| REQ-SYS-140 | Inspection | TC-SYS-093 |
| REQ-SYS-141 | Test | TC-SYS-094 |
| REQ-SYS-142 | Inspection | TC-SYS-092 |
| REQ-SYS-143 | Test | TC-SYS-095 |
| REQ-SYS-144 | Test | TC-SYS-096 |
| REQ-SYS-145 | Inspection | TC-SYS-097 |
| REQ-SYS-146 | Inspection | TC-SYS-097 |
| REQ-SYS-147 | Analysis | TC-SYS-098 |
| REQ-SYS-148 | Inspection | TC-SYS-099 |
| REQ-SYS-149 | Test | TC-SYS-066 |
| REQ-SYS-150 | Test | TC-SYS-095 |
| REQ-SYS-151 | Test | TC-SYS-100 |
| REQ-SYS-152 | Test | TC-SYS-100 |
| REQ-SYS-153 | Test | TC-SYS-069 |
| REQ-SYS-154 | Test | TC-SYS-101 |
| REQ-SYS-155 | Test | TC-SYS-081 |
| REQ-SYS-156 | Test | TC-SYS-101 |
| REQ-SYS-157 | Analysis | TC-SYS-054 |
| REQ-SYS-158 | Analysis | TC-SYS-054 |
| REQ-SYS-159 | Test | TC-SYS-029 |
| REQ-SYS-160 | Test | TC-SYS-102 |
| REQ-SYS-161 | Test | TC-SYS-102 |
| REQ-SYS-162 | Test | TC-SYS-034 |
| REQ-SYS-163 | Test | TC-SYS-037 |
| REQ-SYS-164 | Test | TC-SYS-041 |
| REQ-SYS-165 | Analysis | TC-SYS-103 |
| REQ-SYS-166 | Test | TC-SYS-064 |
| REQ-SYS-167 | Test | TC-SYS-065 |
| REQ-SYS-168 | Analysis | TC-SYS-076 |
| REQ-SYS-169 | Test | TC-SYS-104 |
| REQ-SYS-170 | Test | TC-SYS-053 |
| REQ-SYS-171 | Test | TC-SYS-049 |
| REQ-SYS-172 | Analysis | TC-SYS-084 |
| REQ-SYS-173 | Demonstration | TC-SYS-105 |
| REQ-SYS-174 | Inspection | TC-SYS-058 |
| REQ-SYS-175 | Inspection | TC-SYS-040 |
| REQ-SYS-176 | Test | TC-SYS-106 |
| REQ-SYS-177 | Analysis | TC-SYS-107 |
| REQ-SYS-178 | Inspection | TC-SYS-093 |
| REQ-SYS-179 | Test | TC-SYS-007 |
| REQ-SYS-180 | Test | TC-SYS-108 |
| REQ-SYS-181 | Test | TC-SYS-109 |
| REQ-SYS-182 | Test | TC-SYS-110 |
| REQ-SYS-183 | Test | TC-SYS-003, TC-SYS-008, TC-SYS-047, TC-SYS-066, TC-SYS-082, TC-SYS-083, TC-SYS-101, TC-SYS-108, TC-SYS-109, TC-SYS-110 |

## Cases

### TC-SYS-001: A1A-only emission path: transmit-chain schematic and firmware keying-path inspection

| Field | Value |
|---|---|
| Requirements | REQ-SYS-001 |
| Method / class | Inspection / Inspection |
| Status | Draft |
| Automation | `tools/check_tx_modulation_paths.py` |

**Setup.** Article: design data at tag baseline/cdr: transmit-chain schematic sheets, the netlist exported from them, and the firmware source of the keyer, transmit sequencer, envelope driver and synthesizer driver at the same tag. Configuration: tools/check_tx_modulation_paths.py (planned) walks the netlist from every audio, sidetone, audio-DAC footprint and headphone net to the synthesizer, PA drive, PA bias, ALC and envelope nets through any number of passive parts; the firmware writers of the envelope drive, PA enable and synthesizer frequency registers are listed from the compiler call graph. Credit row: I. Inspection of design data, closed at CDR on the product baseline (docs/process/04-verification-and-validation.md sections 5.1 item 4 and 5.2); the receipt inspection named in the verification_note, where there is one, is recorded as data in the same report. Tools: kicad-cli at its lock path /Applications/KiCad/KiCad.app/Contents/MacOS/kicad-cli and Python per tools/toolchain.lock.md; rustc and cargo per the lock Safety: not applicable (design data only). Environment: not applicable.

**Procedure.**

1. Export the schematic netlist at tag baseline/cdr with kicad-cli sch export netlist.
2. Run tools/check_tx_modulation_paths.py on the netlist and save the list of every path from an audio or tone net to an RF-chain control net.
3. Classify each listed path on the rendered schematic as a DC supply or ground return with decoupling (acceptable) or a signal coupling (finding).
4. Confirm on the schematic that the keying envelope drive is the only time-varying control of carrier amplitude and that the synthesizer has no modulation input other than its frequency-setting interface.
5. List every firmware function that writes the envelope drive output, the PA enable output or the synthesizer frequency registers, and save the list.
6. Confirm that the envelope drive is written only by the keying-envelope sequencer in the key-down and key-up ramps and that no audio, sidetone or tone-generation function writes the envelope drive or the synthesizer registers.
7. Record the inspected file paths, their commit and tool versions in the report.
8. On any finding against the criteria, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if no signal-coupling path exists from any audio, sidetone or tone net to the synthesizer, PA drive, PA bias, ALC or envelope nets (DC supply and ground returns with decoupling excepted), the keying envelope is the only time-varying amplitude control of the carrier, and the only firmware writers of the envelope drive, PA enable and synthesizer frequency are the keying-envelope sequencer and the frequency-setting code; otherwise Fail.

**Expected artifacts.**

- `tx-netlist.net` (other): Netlist exported at baseline/cdr
- `tx-modulation-paths.txt` (report): Checker list of audio-to-RF-control paths with the classification of each
- `fw-rf-writers.txt` (report): Firmware functions that write the envelope drive, PA enable and synthesizer registers

### TC-SYS-002: Operating modes part 1: every allowed transition T01 to T25 of ConOps Table 3.4-2 on the delivered unit

| Field | Value |
|---|---|
| Requirements | REQ-SYS-002 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | `tools/analyze_mode_trace.py` |

**Setup.** Article: CWHT-A-001, enclosure lid off for test-point access, running the fault-injection test build of release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (a build flavour of the release commit whose injection commands arrive over the UART test pads from the host serial terminal through the 3.3 V serial adapter, or over USB serial only in steps that expect no carrier, because USB VBUS sets the USB flag and the hardware transmit inhibit of REQ-SYS-092, and which toggles the injection-marker test pad at the instant of each injection); the release image is restored and checked with picotool verify at the end of the case. Configuration: pack from the two-cell simulator fixture at 3.70 V per cell; USB through the USB breakout fixture when a step applies it; dummy load on the antenna port; logic capture on PA_EN, TX_KEY, the key tip and ring inputs and the UART telemetry pad; mode names read from the telemetry mode field and the display; faults injected with the fault-injection commands; 0.5 W step. Credit row: T-HW. Test of a system requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the campaign (section 13) and witnessed by the owner; the pre-build Simulation, HostUnit and Emulation evidence named in each requirement's verification_note is supporting only and is not part of this case. Hazard controls exercised: HZ-004, HZ-011 (from the cited requirements; docs/safety/hazards.json). Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: every transmission goes into the 50 ohm dummy load or the calibrated power attenuator, connected before power-on, never into an open antenna port; key-down duty kept within the load rating recorded in the report; anyone other than the operator stays 0.6 m or more from the unit and load while keying and 1.0 m or more during a tune carrier (NGO-019); the bench supply current limit is set before each power-on; antistatic wrist strap while the lid is off; the PA area is not touched after key-down runs. Safety: cells and cell simulators are handled per the operations handbook battery section: current limit set before connection, cell terminals never shorted, cells on a non-flammable surface and attended during every charge or discharge run; a cell warm to the touch above about 45 C ends the run. Environment: room temperature 18 to 28 C; the cells or cell simulators named in Configuration; dummy load on the antenna port.

**Procedure.**

1. Run the logic-capture reference pulse-train check of this session and record the result (docs/process/04-verification-and-validation.md section 4).
2. Wire the UART telemetry test pad to a logic-capture channel and confirm that the sigrok-cli UART decoder prints the telemetry lines (REQ-SYS-150).
3. Start a continuous capture. With the switch off and no USB, turn the switch on: expect Off to Self-test to Receive (T01, T08).
4. Close the straight key for 1 s, then wait for hang expiry: expect Receive to Transmit-keyed to Receive (T10, T11). Repeat with the paddle dit lever held for 1 s in Iambic A.
5. Select Tune with its confirmation and let it time out; repeat and end it with a button press: expect Receive to Tune to Receive twice (T12, T13).
6. Select the test menu with its confirmation, then exit: expect Receive to Bench-test to Receive (T14, T15).
7. Apply USB, send the bootloader host command, copy the release UF2 and let the unit reset with the switch on: expect Receive to Firmware-update to Self-test (T16, T21).
8. Inject a latched cause (cutoff-seen command), clear it and acknowledge: expect Receive to Fault-safe to Self-test to Receive (T17, T24).
9. Inject a watchdog hang: expect Receive to Self-test to Receive (T18).
10. Remove USB and turn the switch off: expect Receive to Off (T19). Apply USB with the switch off: expect Off to Charging (T02). Remove USB: expect Charging to Off (T04).
11. Apply USB with the switch off, then turn the switch on: expect Charging to Self-test (T05); turn it off again: expect Charging (T19 with USB).
12. In Charging send the bootloader host command, copy the UF2 and let it reset with the switch off: expect Charging to Firmware-update to Charging (T07, T22); send the command again and unplug USB: expect Firmware-update to Off (T23).
13. With the switch off, hold BOOTSEL and apply USB: expect Off to Firmware-update (T03); unplug USB.
14. In Charging set the simulated cells 600 mV apart (3.40 V and 4.00 V): expect Charging to Fault-safe (T06); restore them and remove USB with the switch off: expect Fault-safe to Off (T25).
15. Arm the display-check failure injection and turn the switch on: expect Self-test to Fault-safe (T09); turn the switch off (T25) and clear the injection.
16. Turn on, then lower the simulated pack to 5.9 V in Receive: expect Receive to Off (T20); repeat with USB present: expect Receive to Charging (T20 with USB).
17. Stop the capture, export it and run tools/analyze_mode_trace.py to list every mode change with its time, cause and the PA_EN state in each mode.
18. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
19. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if each of the transitions T01 to T25 of docs/conops/conops.md Table 3.4-2 is observed from its From mode to its To mode on its event and guard in the telemetry mode sequence and on the display, no other mode change occurs, and PA_EN is high only in Transmit-keyed, Tune and a Bench-test keyed test; otherwise Fail.

**Instruments and fixtures.**

- Pico-based logic capture (second Pico 2 with sigrok-pico firmware read by sigrok-cli; planned, ADR-009), 3.3 V inputs, 1 MS/s unless a step states otherwise
- Two-cell simulator fixture: the bench supply across the pack terminals with an adjustable, buffered mid-point tap for the cell junction and a parallel sink resistor so that the fixture absorbs charger current (docs/vv/fixtures/cell-simulator.md, planned; characterized before TRR)
- USB power breakout fixture with VBUS routed through the multimeter current range (docs/vv/fixtures/usb-breakout.md, planned)
- Host computer with picotool and a serial terminal per tools/toolchain.lock.md, micro-USB cable
- 3.3 V USB-to-UART serial adapter between the host computer and the UART test pads, so that injection commands reach the unit with its USB port disconnected (docs/vv/fixtures/uart-adapter.md, planned)
- 50 ohm BNC dummy load with SMA adapter, power rating recorded in the report
- Owner's straight key and iambic paddle, 3.5 mm TRS plugs (SI-034)
- Multimeter, DC voltage and DC current ranges, accuracy per datasheet copied into the report (OQ-VV-003)

**Expected artifacts.**

- `mode-trace.csv` (csv): Time, mode, transition id, cause and PA_EN state
- `mode-capture.sr` (other): Raw logic capture of the session
- `modes-setup.jpg` (photo): Photograph of the setup

### TC-SYS-003: Operating modes part 2: forbidden transitions and properties F1 to F9 of ConOps section 3.4

| Field | Value |
|---|---|
| Requirements | REQ-SYS-002, REQ-SYS-183 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | `tools/analyze_mode_trace.py` |

**Setup.** Article: CWHT-A-001, enclosure lid off for test-point access, running the fault-injection test build of release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (a build flavour of the release commit whose injection commands arrive over the UART test pads from the host serial terminal through the 3.3 V serial adapter, or over USB serial only in steps that expect no carrier, because USB VBUS sets the USB flag and the hardware transmit inhibit of REQ-SYS-092, and which toggles the injection-marker test pad at the instant of each injection); the release image is restored and checked with picotool verify at the end of the case. Configuration: as part 1 (TC-SYS-002); every forbidden attempt is made with the straight key and then with the paddle where it involves keying (SI-018). Credit row: T-HW. Test of a system requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the campaign (section 13) and witnessed by the owner; the pre-build Simulation, HostUnit and Emulation evidence named in each requirement's verification_note is supporting only and is not part of this case. RF-off level: the acceptance criteria use -57 dBm, the value of REQ-SYS-183 marked TBR (close by PDR); a change returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2). Hazard controls exercised: HZ-004, HZ-011 (from the cited requirements; docs/safety/hazards.json). Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: every transmission goes into the 50 ohm dummy load or the calibrated power attenuator, connected before power-on, never into an open antenna port; key-down duty kept within the load rating recorded in the report; anyone other than the operator stays 0.6 m or more from the unit and load while keying and 1.0 m or more during a tune carrier (NGO-019); the bench supply current limit is set before each power-on; antistatic wrist strap while the lid is off; the PA area is not touched after key-down runs. Safety: cells and cell simulators are handled per the operations handbook battery section: current limit set before connection, cell terminals never shorted, cells on a non-flammable surface and attended during every charge or discharge run; a cell warm to the touch above about 45 C ends the run. Environment: room temperature 18 to 28 C; the cells or cell simulators named in Configuration; dummy load on the antenna port.

**Procedure.**

1. Run the logic-capture reference pulse-train check of this session and record the result (docs/process/04-verification-and-validation.md section 4).
2. Wire the UART telemetry test pad to a logic-capture channel and confirm that the sigrok-cli UART decoder prints the telemetry lines (REQ-SYS-150).
3. F1: hold the straight key closed during Self-test, then the paddle dit lever; after a forced Self-test failure (display-check injection) key both again in Fault-safe.
4. F2 flags: with GUEST, then PRACTICE, then USB present, then LOWBATT (pack at 6.3 V) set in turn, key with the straight key and the paddle and select Tune.
5. F2 inhibits: with KEY (plug closed at switch-on), HOT (PA sensor substituted at its 90 C equivalent) and GUARD (tuned to 147.9995 MHz) active in turn, key with both keys and select Tune.
6. F2 USB power alone: remove the cells, apply USB, key with both keys and select Tune.
7. F3: attempt a key closure, a Tune selection and a test-menu entry from Charging, Firmware-update, Fault-safe and Self-test.
8. F4: tune to 144.0005 MHz and key with both keys.
9. F5: in Fault-safe with the cause still present, pulse RUN (controller reset); confirm the unit re-enters Fault-safe and does not reach Receive.
10. F6: set GUEST, perform a configuration reset, then load the release UF2; confirm GUEST remains set after each.
11. F7: start one Tune and read its carrier duration from TX_KEY; with the fault build holding TX_KEY high, read the longest carrier duration.
12. F8: insert and remove a TS plug and a TRS plug in each key-input mode; confirm the mode never changes without a menu selection.
13. F9: hold the straight key closed and send the bootloader host command; confirm Firmware-update is not entered while PA_EN is high.
14. Export the capture and run tools/analyze_mode_trace.py.
15. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
16. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if PA_EN stays low and no carrier at the set frequency above -57 dBm at the antenna port on the tinySA Ultra (the RF-off level of REQ-SYS-183) for every attempt of F1 to F4 and F3's forbidden entries do not occur; the Fault-safe latch survives the reset (F5); GUEST survives the configuration reset and the firmware load (F6); the Tune carrier lasts at most 5.5 s and no carrier lasts more than 13 s (F7); the key-input mode never changes without a menu selection (F8); and Firmware-update is never entered while PA_EN is high (F9); otherwise Fail.

**Instruments and fixtures.**

- Pico-based logic capture (second Pico 2 with sigrok-pico firmware read by sigrok-cli; planned, ADR-009), 3.3 V inputs, 1 MS/s unless a step states otherwise
- tinySA Ultra spectrum analyzer (ADR-021) through the calibrated 30 to 40 dB attenuator rated 10 W or more, attenuator S21 measured on the NanoVNA in the same session; level accuracy per its TV record
- Two-cell simulator fixture: the bench supply across the pack terminals with an adjustable, buffered mid-point tap for the cell junction and a parallel sink resistor so that the fixture absorbs charger current (docs/vv/fixtures/cell-simulator.md, planned; characterized before TRR)
- USB power breakout fixture with VBUS routed through the multimeter current range (docs/vv/fixtures/usb-breakout.md, planned)
- Host computer with picotool and a serial terminal per tools/toolchain.lock.md, micro-USB cable
- 3.3 V USB-to-UART serial adapter between the host computer and the UART test pads, so that injection commands reach the unit with its USB port disconnected (docs/vv/fixtures/uart-adapter.md, planned)
- 50 ohm BNC dummy load with SMA adapter, power rating recorded in the report
- Owner's straight key and iambic paddle, 3.5 mm TRS plugs (SI-034)
- NTC substitution fixture: fixed resistors at the temperature equivalents named in the steps, switched in place of the cell or PA sensor at its test pad, the switch's second pole wired to a logic-capture channel as the event marker (docs/vv/fixtures/ntc-substitution.md, planned)
- NanoVNA, SOL calibration at the cable end used, checked on the dummy load

**Expected artifacts.**

- `forbidden-attempts.csv` (csv): Attempt, mode, keying source, PA_EN, RF reading and result
- `forbidden-capture.sr` (other): Raw logic capture

### TC-SYS-004: Transmit armed only after a power-on self-test in which every check has passed

| Field | Value |
|---|---|
| Requirements | REQ-SYS-003 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | `tools/analyze_logic_capture.py` |

**Setup.** Article: CWHT-A-001, enclosure lid off for test-point access, running the fault-injection test build of release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (a build flavour of the release commit whose injection commands arrive over the UART test pads from the host serial terminal through the 3.3 V serial adapter, or over USB serial only in steps that expect no carrier, because USB VBUS sets the USB flag and the hardware transmit inhibit of REQ-SYS-092, and which toggles the injection-marker test pad at the instant of each injection); the release image is restored and checked with picotool verify at the end of the case. Configuration: pack from the two-cell simulator fixture; cell NTC through the NTC substitution fixture; dummy load; logic capture on PA_EN, TX_KEY, the key tip and ring inputs and the UART telemetry pad; each self-test check forced by a fixture setting or an injection command; the firmware-image check is exercised by TC-SYS-089. Credit row: T-HW. Test of a system requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the campaign (section 13) and witnessed by the owner; the pre-build Simulation, HostUnit and Emulation evidence named in each requirement's verification_note is supporting only and is not part of this case. Hazard controls exercised: HZ-004, HZ-014 (from the cited requirements; docs/safety/hazards.json). Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: every transmission goes into the 50 ohm dummy load or the calibrated power attenuator, connected before power-on, never into an open antenna port; key-down duty kept within the load rating recorded in the report; anyone other than the operator stays 0.6 m or more from the unit and load while keying and 1.0 m or more during a tune carrier (NGO-019); the bench supply current limit is set before each power-on; antistatic wrist strap while the lid is off; the PA area is not touched after key-down runs. Safety: cells and cell simulators are handled per the operations handbook battery section: current limit set before connection, cell terminals never shorted, cells on a non-flammable surface and attended during every charge or discharge run; a cell warm to the touch above about 45 C ends the run. Environment: room temperature 18 to 28 C; the cells or cell simulators named in Configuration; dummy load on the antenna port.

**Procedure.**

1. Run the logic-capture reference pulse-train check of this session and record the result (docs/process/04-verification-and-validation.md section 4).
2. Wire the UART telemetry test pad to a logic-capture channel and confirm that the sigrok-cli UART decoder prints the telemetry lines (REQ-SYS-150).
3. Baseline: all conditions nominal; switch on, read the self-test result lines, close the straight key for 1 s and the paddle dit lever for 1 s after Self-test ends; expect PA_EN to follow the keying.
4. Force the cell-voltage check with simulated cells 600 mV apart but both inside 2.5 V to 4.3 V (3.40 V and 4.00 V) and switch on.
5. Force the cell-temperature check (NTC fixture at its 65 C equivalent) and switch on.
6. Force the dual-path cell-voltage check (injection command: 150 mV disagreement) and switch on.
7. Force the rail check (injection command: 3.3 V rail out of tolerance) and switch on.
8. Force the amplifier-enable check (injection command: enable readback high) and switch on.
9. Force the display check (injection command: display not responding) and switch on.
10. For each forced check above: read the telemetry self-test line and the display message, close the straight key and then the paddle for 1 s each at 10 s after Self-test ends, record PA_EN, restore the condition and switch off.
11. Write a corrupt configuration through the test interface and switch on: read the substituted defaults and key with both keys.
12. Hold the straight key closed through switch-on and release it 2 s after Self-test ends; key again after 1 s.
13. Export the capture and run tools/analyze_logic_capture.py to list PA_EN edges against the self-test end and key closures.
14. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
15. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if for every forced check the telemetry names the failed item, the unit is in Fault-safe with the item shown and PA_EN stays low for every straight-key and paddle closure; the corrupt configuration is replaced by defaults, shown, Self-test passes and PA_EN follows the key; with the key closed at switch-on PA_EN stays low until the key has read open for 500 ms; and in the baseline PA_EN follows both keys; otherwise Fail.

**Instruments and fixtures.**

- Pico-based logic capture (second Pico 2 with sigrok-pico firmware read by sigrok-cli; planned, ADR-009), 3.3 V inputs, 1 MS/s unless a step states otherwise
- Two-cell simulator fixture: the bench supply across the pack terminals with an adjustable, buffered mid-point tap for the cell junction and a parallel sink resistor so that the fixture absorbs charger current (docs/vv/fixtures/cell-simulator.md, planned; characterized before TRR)
- NTC substitution fixture: fixed resistors at the temperature equivalents named in the steps, switched in place of the cell or PA sensor at its test pad, the switch's second pole wired to a logic-capture channel as the event marker (docs/vv/fixtures/ntc-substitution.md, planned)
- Host computer with picotool and a serial terminal per tools/toolchain.lock.md, micro-USB cable
- 3.3 V USB-to-UART serial adapter between the host computer and the UART test pads, so that injection commands reach the unit with its USB port disconnected (docs/vv/fixtures/uart-adapter.md, planned)
- 50 ohm BNC dummy load with SMA adapter, power rating recorded in the report
- Owner's straight key and iambic paddle, 3.5 mm TRS plugs (SI-034)

**Expected artifacts.**

- `selftest-results.csv` (csv): Forced check, telemetry result, display message, PA_EN per closure
- `selftest-capture.sr` (other): Raw logic capture

### TC-SYS-005: Carrier end within 20 ms on every inhibit, flag and latched fault, a distinct message per fault type, and Fault-safe left only through acknowledgment after clearance or by switch-off or power removal

| Field | Value |
|---|---|
| Requirements | REQ-SYS-004, REQ-SYS-005, REQ-SYS-067 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | `tools/analyze_logic_capture.py` |

**Setup.** Article: CWHT-A-001, enclosure lid off for test-point access, running the fault-injection test build of release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (a build flavour of the release commit whose injection commands arrive over the UART test pads from the host serial terminal through the 3.3 V serial adapter, or over USB serial only in steps that expect no carrier, because USB VBUS sets the USB flag and the hardware transmit inhibit of REQ-SYS-092, and which toggles the injection-marker test pad at the instant of each injection); the release image is restored and checked with picotool verify at the end of the case. Configuration: dummy load; 5 W step at 146.00 MHz; USB disconnected except in the charger-fault step; logic capture on the injection-marker pad, PA_EN, the display chip-select and the UART telemetry pad at 1 MS/s; the RF fall after PA_EN release is bounded by the envelope Analysis (TC-SYS-013) because PA_EN is released only after the completed shaped fall (REQ-SYS-004 verification_note), and RF with PA_EN low is at the RF-off level of REQ-SYS-183, measured by the cases that cite REQ-SYS-183. The causes are those the REQ-SYS-004 rationale takes from docs/conops/conops.md Tables 3.4-3 and 3.4-4: the inhibits KEY, HOT and GUARD, the flags GUEST, PRACTICE, USB and LOWBATT, and the latched causes; the ConOps table states the same 20 ms as REQ-SYS-004 (ConOps appendix D item D3, closed). The exit rules of REQ-SYS-005 are exercised with the two latched causes its verification_note names, a cell-sense disagreement and a repeated watchdog reset. Credit row: T-HW. Test of a system requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the campaign (section 13) and witnessed by the owner; the pre-build Simulation, HostUnit and Emulation evidence named in each requirement's verification_note is supporting only and is not part of this case. TBR values: the acceptance criteria use the values of REQ-SYS-004, REQ-SYS-067 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Hazard controls exercised: HZ-004 (from the cited requirements; docs/safety/hazards.json). Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: every transmission goes into the 50 ohm dummy load or the calibrated power attenuator, connected before power-on, never into an open antenna port; key-down duty kept within the load rating recorded in the report; anyone other than the operator stays 0.6 m or more from the unit and load while keying and 1.0 m or more during a tune carrier (NGO-019); the bench supply current limit is set before each power-on; antistatic wrist strap while the lid is off; the PA area is not touched after key-down runs. Environment: room temperature 18 to 28 C; the pack is supplied by the bench supply at 7.4 V +/-0.05 V through the battery terminals unless a step sets another value; dummy load on the antenna port.

**Procedure.**

1. Run the logic-capture reference pulse-train check of this session and record the result (docs/process/04-verification-and-validation.md section 4).
2. Wire the UART telemetry test pad to a logic-capture channel and confirm that the sigrok-cli UART decoder prints the telemetry lines (REQ-SYS-150), and confirm that the host serial terminal reaches the injection commands through the serial adapter with USB disconnected.
3. List the injectable causes of the build and record the list: inhibits KEY, HOT and GUARD; flags GUEST, PRACTICE, USB and LOWBATT; latched causes second watchdog reset, Self-test check failed, independent cutoff seen, cell-sense disagreement, cell reversed or mismatched, charger fault, synthesizer unlocked, synthesizer off frequency, PA sensor out of range and forward-power detector implausible.
4. Inhibits and flags: for each of KEY, HOT, GUARD, GUEST, PRACTICE, USB and LOWBATT, key down with the straight key held, inject the cause 1 s after key-down, hold the key for a further 2 s, release, clear the cause by command and wait 5 s; record the mode shown before and after the clearance.
5. Repeat the previous step for each of the seven causes keyed with the paddle dah lever held at 15 WPM.
6. Latched causes during a carrier: for each of cell-sense disagreement, synthesizer unlocked, synthesizer off frequency, PA sensor out of range and forward-power detector implausible, key down (straight key held for the first, third and fifth, paddle dah lever held for the second and fourth), inject the cause 1 s after key-down and hold the key for a further 2 s; photograph the displayed message; clear the cause, acknowledge and confirm Self-test then Receive before the next cause.
7. Latched causes that do not arise during a carrier: inject each in the mode where it arises and photograph the displayed message: Self-test check failed and cell reversed or mismatched (each injection armed, then switch off and on), independent cutoff seen (fault build holding TX_KEY high until the hardware cutoff of REQ-SYS-055 acts, as in TC-SYS-039), second watchdog reset (two watchdog-expiry injections in Receive without a switch-off) and charger fault (switch off, USB applied through the USB breakout with the two-cell simulator charging, injection over USB serial); clear each cause and acknowledge, except the charger fault, which is left by removing USB with the switch off (T25).
8. Exit rules, cell-sense disagreement: inject it in Receive and keep it present; press acknowledge; confirm the unit stays in Fault-safe; close the straight key and then the paddle dah lever for 2 s each.
9. With the cause still present, pulse RUN (controller reset); confirm the unit returns through Self-test to Fault-safe without reaching Receive; repeat the two key closures.
10. Clear the cause without acknowledging and wait 60 s; confirm the unit stays in Fault-safe; repeat the two key closures.
11. With the cause cleared and not acknowledged, pulse RUN; confirm the unit returns through Self-test to Fault-safe; repeat the two key closures.
12. Acknowledge; confirm Self-test then Receive, and close the straight key for 1 s.
13. Exit rules, repeated watchdog reset: inject two watchdog expiries in Receive without a switch-off so that the second reset latches Fault-safe; pulse RUN and confirm the unit returns through Self-test to Fault-safe; repeat the two key closures; acknowledge and confirm Self-test then Receive; close the paddle dit lever for 1 s.
14. Switch-off exit: latch a cell-sense disagreement again, clear it by command and, without acknowledging, turn the power switch off; confirm Off (display dark, no telemetry on the UART pad); turn the switch on and confirm Self-test then Receive.
15. Power-removal exit: latch a cell-sense disagreement again, clear it by command and, without acknowledging and with the switch on, disconnect the bench supply for 5 s; reconnect it and confirm Self-test then Receive.
16. Export the capture and run tools/analyze_logic_capture.py to measure, per injection, marker-to-PA_EN-fall and marker-to-first-display-frame-write latencies, and to list every PA_EN rise and every mode change in the exit-rule steps.
17. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
18. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if, for every inhibit, flag and latched cause injected during a carrier (steps 4 to 6) with either key type, PA_EN falls at most 20 ms after the injection marker (REQ-SYS-004); for every latched cause (steps 6 and 7) the display write that shows the cause begins at most 1 s after the marker and each cause shows a message distinct from every other (REQ-SYS-067); and Fault-safe is left only through Self-test after the cause has cleared and the operator has acknowledged (steps 12 and 13) or by switch-off or power removal (steps 14 and 15), while acknowledgment with the cause present, clearance without acknowledgment and a controller reset with or without the cause present each leave the unit in Fault-safe with no PA_EN rise on any key closure (steps 8 to 11 and 13) (REQ-SYS-005); otherwise Fail.

**Instruments and fixtures.**

- Pico-based logic capture (second Pico 2 with sigrok-pico firmware read by sigrok-cli; planned, ADR-009), 3.3 V inputs, 1 MS/s unless a step states otherwise
- Host computer with picotool and a serial terminal per tools/toolchain.lock.md, micro-USB cable
- 3.3 V USB-to-UART serial adapter between the host computer and the UART test pads, so that injection commands reach the unit with its USB port disconnected (docs/vv/fixtures/uart-adapter.md, planned)
- 50 ohm BNC dummy load with SMA adapter, power rating recorded in the report
- Owner's straight key and iambic paddle, 3.5 mm TRS plugs (SI-034)
- Adjustable bench supply, 0 to 30 V, current limit set per step
- USB power breakout fixture with VBUS routed through the multimeter current range (docs/vv/fixtures/usb-breakout.md, planned)
- Two-cell simulator fixture: the bench supply across the pack terminals with an adjustable, buffered mid-point tap for the cell junction and a parallel sink resistor so that the fixture absorbs charger current (docs/vv/fixtures/cell-simulator.md, planned; characterized before TRR)

**Expected artifacts.**

- `faultsafe-latency.csv` (csv): Cause, class, keying source, marker-to-PA_EN and marker-to-display latencies
- `faultsafe-exit.csv` (csv): Exit-rule step, event, mode before and after, PA_EN rises on the key closures
- `faultsafe-messages.jpg` (photo): Photographs of each displayed cause message
- `faultsafe-capture.sr` (other): Raw logic capture

### TC-SYS-006: Operator call sign after every power-on and every operator setting retained across power cycles and cell removal

| Field | Value |
|---|---|
| Requirements | REQ-SYS-006, REQ-SYS-135 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | none (manual) |

**Setup.** Article: CWHT-A-001 in its enclosure, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: unit on the owner's cells; settings read from the menus and the status screen and photographed. Credit row: T-HW. Test of a system requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the campaign (section 13) and witnessed by the owner; the pre-build Simulation, HostUnit and Emulation evidence named in each requirement's verification_note is supporting only and is not part of this case. Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: cells and cell simulators are handled per the operations handbook battery section: current limit set before connection, cell terminals never shorted, cells on a non-flammable surface and attended during every charge or discharge run; a cell warm to the touch above about 45 C ends the run. Environment: room temperature 18 to 28 C; the cells or cell simulators named in Configuration; dummy load on the antenna port.

**Procedure.**

1. Enter the one-character call sign K; power-cycle; read the call sign shown after power-on.
2. Enter the ten-character call sign KC1ABC/QRP; power-cycle; read it.
3. Set every operator setting to a non-default value and record the list (frequency, step, key-input mode, keyer mode, speed, sidetone, hang, envelope time, volume, PRACTICE, filter trim, reference trim, call sign).
4. Switch off, remove both cells for 1 min, reinsert them and switch on.
5. Read every setting and the call sign; photograph the menus.
6. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
7. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if the last-entered call sign of 1 and of 10 characters is displayed after each power-on (REQ-SYS-006), and every listed setting reads its set value after the cell removal (REQ-SYS-135); otherwise Fail. The audio-cap unlock is excluded because REQ-SYS-170 restores the cap at power-on unless a persistent unlock is selected.

**Instruments and fixtures.**

- Owner's 3000 mAh 18650 cells, a matched pair

**Expected artifacts.**

- `persistence.csv` (csv): Setting, value set, value read
- `persistence-menus.jpg` (photo): Photographs of the menus

### TC-SYS-007: Transmitted Morse only from key-jack closures, and bench test mode entry only after selection and confirmation

| Field | Value |
|---|---|
| Requirements | REQ-SYS-007, REQ-SYS-179 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | `tools/analyze_logic_capture.py` |

**Setup.** Article: CWHT-A-001, enclosure lid off for test-point access, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: dummy load; 0.5 W step at 146.00 MHz; logic capture on TX_KEY, PA_EN and the keyer test point at 100 kS/s for the long captures; mode read from the display. Credit row: T-HW. Test of a system requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the campaign (section 13) and witnessed by the owner; the pre-build Simulation, HostUnit and Emulation evidence named in each requirement's verification_note is supporting only and is not part of this case. Hazard controls exercised: HZ-004, HZ-005 (from the cited requirements; docs/safety/hazards.json). Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: every transmission goes into the 50 ohm dummy load or the calibrated power attenuator, connected before power-on, never into an open antenna port; key-down duty kept within the load rating recorded in the report; anyone other than the operator stays 0.6 m or more from the unit and load while keying and 1.0 m or more during a tune carrier (NGO-019); the bench supply current limit is set before each power-on; antistatic wrist strap while the lid is off; the PA area is not touched after key-down runs. Environment: room temperature 18 to 28 C; the pack is supplied by the bench supply at 7.4 V +/-0.05 V through the battery terminals unless a step sets another value; dummy load on the antenna port.

**Procedure.**

1. Run the logic-capture reference pulse-train check of this session and record the result (docs/process/04-verification-and-validation.md section 4).
2. With the key jack empty, capture TX_KEY for 10 min in Receive.
3. Set PRACTICE and capture TX_KEY for 10 min; clear PRACTICE.
4. Enter the test menu with its confirmation but start no test; capture TX_KEY for 10 min; exit.
5. Insert the straight key, leave it untouched and capture 1 min; repeat with the paddle.
6. Apply each test-mode control sequence without its confirmation: test-menu selection then back; selection then 30 s timeout; confirmation press without a selection; every other single button and knob action; read the mode on the display after each.
7. Select the test menu and confirm; select the PARIS keyed test into the dummy load; record the time of the start confirmation press on a spare capture channel wired to the button.
8. Let the PARIS test run 20 s, then exit.
9. Export the captures and run tools/analyze_logic_capture.py to count TX_KEY edges per interval.
10. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
11. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if TX_KEY shows zero edges in the three 10 min jack-open captures and the two idle-key captures, every non-confirmed sequence leaves the mode unchanged with zero TX_KEY edges, and the test-mode generator's first TX_KEY edge follows the start confirmation press; otherwise Fail.

**Instruments and fixtures.**

- Pico-based logic capture (second Pico 2 with sigrok-pico firmware read by sigrok-cli; planned, ADR-009), 3.3 V inputs, 1 MS/s unless a step states otherwise
- 50 ohm BNC dummy load with SMA adapter, power rating recorded in the report
- Owner's straight key and iambic paddle, 3.5 mm TRS plugs (SI-034)
- Adjustable bench supply, 0 to 30 V, current limit set per step

**Expected artifacts.**

- `keysource-edges.csv` (csv): Interval, mode, TX_KEY edge count
- `keysource-capture.sr` (other): Raw logic captures

### TC-SYS-008: Transmit carrier placed from 144.001 to 147.999 MHz and inhibited outside that range

| Field | Value |
|---|---|
| Requirements | REQ-SYS-008, REQ-SYS-009, REQ-SYS-183 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | none (manual) |

**Setup.** Article: CWHT-A-001, enclosure lid off for test-point access, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: antenna port to the calibrated power attenuator and the tinySA Ultra; 0.5 W step; logic capture on PA_EN; the tinySA reference accuracy from its TV record is the frequency uncertainty of each marker reading. Credit row: T-HW. Test of a system requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the campaign (section 13) and witnessed by the owner; the pre-build Simulation, HostUnit and Emulation evidence named in each requirement's verification_note is supporting only and is not part of this case. TBR values: the acceptance criteria use the values of REQ-SYS-008, REQ-SYS-009 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). RF-off level: the acceptance criteria use -57 dBm, the value of REQ-SYS-183 marked TBR (close by PDR); a change returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2). Hazard controls exercised: HZ-008 (from the cited requirements; docs/safety/hazards.json). Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: every transmission goes into the 50 ohm dummy load or the calibrated power attenuator, connected before power-on, never into an open antenna port; key-down duty kept within the load rating recorded in the report; anyone other than the operator stays 0.6 m or more from the unit and load while keying and 1.0 m or more during a tune carrier (NGO-019); the bench supply current limit is set before each power-on; antistatic wrist strap while the lid is off; the PA area is not touched after key-down runs. Environment: room temperature 18 to 28 C; the pack is supplied by the bench supply at 7.4 V +/-0.05 V through the battery terminals unless a step sets another value; dummy load on the antenna port.

**Procedure.**

1. Run the logic-capture reference pulse-train check of this session and record the result (docs/process/04-verification-and-validation.md section 4).
2. Measure the attenuator and cable S21 on the NanoVNA from 9 kHz (or the NanoVNA lower limit) to 1.5 GHz and save the Touchstone file; run the tinySA Ultra internal calibration-output check; record both.
3. Tune to 144.001 MHz, close the straight key for 3 s and read the tinySA marker at the carrier peak (span 20 kHz, narrowest RBW).
4. Repeat at 146.000 and 147.999 MHz, and at 144.001 MHz keyed by the paddle dah lever for 3 s.
5. Tune to 144.0005 MHz, then 147.9995 MHz, and, if the tuning allows them, 143.999 and 148.000 MHz; at each close the straight key for 3 s and then the paddle dah lever for 3 s, and read the display transmit-state field.
6. Export the capture and the tinySA traces.
7. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
8. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if at each set frequency from 144.001 to 147.999 MHz the unit keys and the carrier marker lies within the set frequency +/-(2.5 ppm plus the tinySA reference accuracy) (REQ-SYS-008), and at every set frequency outside 144.001 to 147.999 MHz PA_EN stays low, no carrier at the set frequency above -57 dBm at the antenna port on the tinySA Ultra (the RF-off level of REQ-SYS-183) and the display shows the guard inhibit (REQ-SYS-009); otherwise Fail.

**Instruments and fixtures.**

- tinySA Ultra spectrum analyzer (ADR-021) through the calibrated 30 to 40 dB attenuator rated 10 W or more, attenuator S21 measured on the NanoVNA in the same session; level accuracy per its TV record
- NanoVNA, SOL calibration at the cable end used, checked on the dummy load
- Pico-based logic capture (second Pico 2 with sigrok-pico firmware read by sigrok-cli; planned, ADR-009), 3.3 V inputs, 1 MS/s unless a step states otherwise
- Owner's straight key and iambic paddle, 3.5 mm TRS plugs (SI-034)
- Adjustable bench supply, 0 to 30 V, current limit set per step

**Expected artifacts.**

- `guard-markers.csv` (csv): Set frequency, keying source, marker frequency, PA_EN and RF level
- `guard-traces.png` (plot): tinySA traces at each set frequency

### TC-SYS-009: Carrier frequency error budget over temperature and one-year aging

| Field | Value |
|---|---|
| Requirements | REQ-SYS-010 |
| Method / class | Analysis / Simulation |
| Status | Draft |
| Automation | `tools/budgets/frequency_error_budget.py` |

**Setup.** Article: design data at tag baseline/cdr: frequency-reference and synthesizer part numbers and datasheets from the CDR BOM, the synthesizer register table and the reference-trim resolution. Configuration: tools/budgets/frequency_error_budget.py (planned) sums, as a worst case, the reference initial tolerance after calibration, its stability from -10 C to +45 C, one-year aging, the trim resolution and the synthesizer fractional-N rounding error at 144.001, 146.000 and 147.999 MHz. Credit row: A. Analysis closed by Simulation on the CDR design data and confirmed at SAR by the physical configuration audit of every analyzed value (docs/process/04-verification-and-validation.md sections 5.1 item 5 and 5.2); the post-build readings named in the verification_note are supporting data only. TBR values: the acceptance criteria use the values of REQ-SYS-010 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Hazard controls exercised: HZ-008 (from the cited requirements; docs/safety/hazards.json). Risk acceptance: the verification_note of REQ-SYS-010 (RSK-002) begins 'Analysis accepted per RSK-NNN'; that risk carries the hazard control not closed by Test (docs/process/04-verification-and-validation.md section 3, rule 7.3.6). Tools: Python per tools/toolchain.lock.md Safety: not applicable (design data only). Environment: not applicable.

**Procedure.**

1. Confirm that the budget inputs equal the CDR BOM part numbers and the datasheet values cited in the script header (script prints the diff; an empty diff is required).
2. Run tools/budgets/frequency_error_budget.py and save its table of each term in ppm and the total at the three frequencies.
3. Confirm that the displayed-frequency computation in the firmware design uses the same reference frequency constant as the budget.
4. Record tool versions, the design-data tag and the commit of every deck, model, script and checker in the report.
5. On any assertion or checker failure, or any difference between the analyzed values and the design data, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if the worst-case sum of initial tolerance after calibration, -10 C to +45 C stability, one-year aging, trim resolution and synthesizer rounding is at most 2.5 ppm at 144.001, 146.000 and 147.999 MHz; otherwise Fail.

**Expected artifacts.**

- `frequency-error-budget.csv` (csv): Budget terms in ppm and totals per frequency
- `frequency-error-budget.log.txt` (log): Script output with the input diff

### TC-SYS-010: Diode RF probe characterization on the dummy load (fixture case, supporting)

| Field | Value |
|---|---|
| Requirements | REQ-SYS-011, REQ-SYS-012 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | `tools/rf_probe_power.py` |

**Setup.** Article: the diode RF probe fixture (1N5711 or equivalent in its printed housing, docs/vv/fixtures/rf-probe.md, planned) with the BNC T and the dummy load it is used on; no cwht unit. Configuration: NanoVNA on the dummy load with and without the probe on the T; the probe's diode forward-drop curve measured at DC with the bench supply through a series resistor and the multimeter; uncertainty budget computed by tools/rf_probe_power.py --characterize. Credit row: SUPPORT. Fixture characterization that every diode-probe power case depends on (docs/process/04-verification-and-validation.md section 6.2 output-power row); it never closes a requirement and must be Passed before the TRR that opens the power cases. It also underpins the probe readings of TC-SYS-015, TC-SYS-045, TC-SYS-046, TC-SYS-100 and TC-SYS-012; it cites only REQ-SYS-011 and REQ-SYS-012 so that, until the CLOSING_CLASS check of 04 section 7.4 exists, the matrix lists it against the fewest requirements. Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: no cwht unit is connected and no RF above the NanoVNA output level is applied; the DC characterization uses the bench supply with a 10 mA current limit. Environment: room temperature 18 to 28 C.

**Procedure.**

1. Calibrate the NanoVNA (SOL) at the cable end and measure the dummy load return loss from 144 to 148 MHz without the probe.
2. Fit the probe on the T at the load and repeat the return-loss measurement.
3. Measure the dummy load DC resistance with the multimeter and its |Z| at 146 MHz from the NanoVNA sweep.
4. Measure the probe's forward drop at DC: apply known DC voltages from 2 V to 25 V through the probe input and record the multimeter output reading at each, giving the correction curve Vpk = f(Vout).
5. Run tools/rf_probe_power.py --characterize: it combines the correction curve, the multimeter accuracy, the load impedance and the probe loading into a power uncertainty at 0.4, 0.5, 1, 2, 5 and 6.3 W.
6. Record instrument calibration state, the fixture serial and tool versions in the report.
7. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if the probe changes the dummy-load return loss by at most 0.5 dB from 144 to 148 MHz, the load |Z| at 146 MHz is 50 ohm +/-2 ohm, the correction curve covers 2 V to 25 V, and the combined power uncertainty is at most 15 percent at every listed power; otherwise Fail. The resulting uncertainty is copied into every power case that uses the probe.

**Instruments and fixtures.**

- NanoVNA, SOL calibration at the cable end used, checked on the dummy load
- Multimeter, DC voltage and DC current ranges, accuracy per datasheet copied into the report (OQ-VV-003)
- Adjustable bench supply, 0 to 30 V, current limit set per step
- 50 ohm BNC dummy load with SMA adapter, power rating recorded in the report

**Expected artifacts.**

- `probe-characterization.csv` (csv): Correction curve, loading and uncertainty per power
- `probe-return-loss.s1p` (other): Dummy load S11 with and without the probe
- `probe-fixture.jpg` (photo): Photograph of the probe on the T at the load

### TC-SYS-011: Output power at the 0.5, 1, 2 and 5 W steps across the band and pack voltage

| Field | Value |
|---|---|
| Requirements | REQ-SYS-011, REQ-SYS-012 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | `tools/rf_probe_power.py` |

**Setup.** Article: CWHT-A-001 in its enclosure, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: bench supply through the pack-resistance fixture into the battery terminals; dummy load with the diode RF probe on its T; multimeter on the probe output; for the secondary reading the dummy load is replaced by the calibrated power attenuator and the tinySA Ultra; key-downs of 3 s with at least 10 s between them. Credit row: T-HW. Test of a system requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the campaign (section 13) and witnessed by the owner; the pre-build Simulation, HostUnit and Emulation evidence named in each requirement's verification_note is supporting only and is not part of this case. TBR values: the acceptance criteria use the values of REQ-SYS-011, REQ-SYS-012 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Hazard controls exercised: HZ-001, HZ-003, HZ-006, HZ-008 (from the cited requirements; docs/safety/hazards.json). Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: every transmission goes into the 50 ohm dummy load or the calibrated power attenuator, connected before power-on, never into an open antenna port; key-down duty kept within the load rating recorded in the report; anyone other than the operator stays 0.6 m or more from the unit and load while keying and 1.0 m or more during a tune carrier (NGO-019); the bench supply current limit is set before each power-on; antistatic wrist strap while the lid is off; the PA area is not touched after key-down runs. Environment: room temperature 18 to 28 C; the pack is supplied by the bench supply at 7.4 V +/-0.05 V through the battery terminals unless a step sets another value; dummy load on the antenna port.

**Procedure.**

1. Confirm that TC-SYS-010 is Passed and copy its power uncertainty into the report.
2. Set the supply to 6.4 V at the battery terminals under load.
3. At 144.05 MHz select the 0.5 W step, close the straight key for 3 s and read the probe output; repeat for the 1 W, 2 W and 5 W steps.
4. Repeat the previous step at 146.00 and 147.95 MHz.
5. Repeat the three previous frequency runs at 8.4 V, and the 5 W step at 7.4 V.
6. At 146.00 MHz, 7.4 V and the 5 W step, hold the paddle dah lever at 15 WPM for 3 s and read the probe; compare with the straight-key reading.
7. Replace the dummy load by the attenuator and tinySA; at 146.00 MHz and 7.4 V read the carrier power at each step (secondary reading).
8. Run tools/rf_probe_power.py on the readings to compute power with its uncertainty band.
9. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
10. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if at every frequency and pack voltage the probe power with its characterized uncertainty band lies entirely inside 0.397 to 0.629 W at 0.5 W, 0.794 to 1.259 W at 1 W and 1.589 to 2.518 W at 2 W (REQ-SYS-011, +/-1 dB) and inside 3.972 to 6.295 W at 5 W (REQ-SYS-012, +/-1 dB); otherwise Fail. A probe and tinySA disagreement beyond their combined uncertainty is a Procedure-correction NCR (04 section 6.2), not a requirement result.

**Instruments and fixtures.**

- Diode RF probe (1N5711 or equivalent, printed housing) on a BNC T at the dummy load, characterized by TC-SYS-010, read on the multimeter DC voltage range
- Multimeter, DC voltage and DC current ranges, accuracy per datasheet copied into the report (OQ-VV-003)
- Adjustable bench supply, 0 to 30 V, current limit set per step
- Pack-resistance fixture: series resistor equal to the datasheet internal resistance of two cells plus two holders, in the bench-supply lead (docs/vv/fixtures/pack-resistance.md, planned)
- 50 ohm BNC dummy load with SMA adapter, power rating recorded in the report
- tinySA Ultra spectrum analyzer (ADR-021) through the calibrated 30 to 40 dB attenuator rated 10 W or more, attenuator S21 measured on the NanoVNA in the same session; level accuracy per its TV record
- NanoVNA, SOL calibration at the cable end used, checked on the dummy load
- Owner's straight key and iambic paddle, 3.5 mm TRS plugs (SI-034)

**Expected artifacts.**

- `power-steps.csv` (csv): Frequency, pack voltage, step, keying source, probe reading, power and band
- `power-secondary.csv` (csv): tinySA secondary readings with attenuator correction
- `power-setup.jpg` (photo): Photograph of the setup

### TC-SYS-012: Survival of 60 s of 5 W keying at 80 percent duty into open, short and SWR 10:1 loads at four phases

| Field | Value |
|---|---|
| Requirements | REQ-SYS-013 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | none (manual) |

**Setup.** Article: CWHT-A-001 in its enclosure, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: mismatch fixture set (SMA open and short standards and a 5 ohm load rated 5 W, each behind 0, 1/8, 1/4 and 3/8 wavelength line sections at 146 MHz; docs/vv/fixtures/mismatch-set.md, planned), each characterized on the NanoVNA this session; 146.00 MHz, 7.4 V, 5 W step; PA temperature read from the UART telemetry; after the stress the power and spurious readings use the methods of TC-SYS-011 and TC-SYS-014. Credit row: T-HW. Test of a system requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the campaign (section 13) and witnessed by the owner; the pre-build Simulation, HostUnit and Emulation evidence named in each requirement's verification_note is supporting only and is not part of this case. Hazard controls exercised: HZ-003, HZ-009, HZ-012 (from the cited requirements; docs/safety/hazards.json). Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: every transmission goes into the 50 ohm dummy load or the calibrated power attenuator, connected before power-on, never into an open antenna port except the SMA open standard of this case; key-down duty kept within the load rating recorded in the report; anyone other than the operator stays 0.6 m or more from the unit and load while keying and 1.0 m or more during a tune carrier (NGO-019); the bench supply current limit is set before each power-on; antistatic wrist strap while the lid is off; the PA area is not touched after key-down runs. The PA is allowed to cool to 40 C (telemetry) between fixtures. Environment: room temperature 18 to 28 C; the pack is supplied by the bench supply at 7.4 V +/-0.05 V through the battery terminals unless a step sets another value; dummy load on the antenna port.

**Procedure.**

1. Wire the UART telemetry test pad to a logic-capture channel and confirm that the sigrok-cli UART decoder prints the telemetry lines (REQ-SYS-150).
2. Measure each of the 12 fixture conditions (open, short and 5 ohm at four line sections) on the NanoVNA and record reflection magnitude and phase at 146 MHz.
3. Fit the first fixture; key with the straight key held until the 5 s timeout, release, re-key within 1 s, for 60 s.
4. Repeat for each of the 12 fixture conditions, logging PA temperature and any inhibit or Fault-safe message.
5. On the open fixture at the 0 section, squeeze both paddle levers (alternating elements) at 50 WPM for 60 s.
6. Refit the dummy load and measure the 5 W step power at 146.00 MHz and 7.4 V with the diode probe.
7. Replace the dummy load by the attenuator and tinySA and scan 9 kHz to 1.5 GHz at the 5 W step at 146.00 MHz.
8. Inspect the board around the PA and the filter for discoloration and photograph it.
9. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
10. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if after all 12 fixture conditions and the paddle run the 5 W step power lies inside 3.972 to 6.295 W with the probe uncertainty band, every spurious emission is at most 25 uW (-16.0 dBm) at the antenna port, the unit operates normally, and no part shows damage; otherwise Fail. Protective power reduction or inhibits during the stress are recorded and do not fail the case.

**Instruments and fixtures.**

- NanoVNA, SOL calibration at the cable end used, checked on the dummy load
- Diode RF probe (1N5711 or equivalent, printed housing) on a BNC T at the dummy load, characterized by TC-SYS-010, read on the multimeter DC voltage range
- Multimeter, DC voltage and DC current ranges, accuracy per datasheet copied into the report (OQ-VV-003)
- tinySA Ultra spectrum analyzer (ADR-021) through the calibrated 30 to 40 dB attenuator rated 10 W or more, attenuator S21 measured on the NanoVNA in the same session; level accuracy per its TV record
- 50 ohm BNC dummy load with SMA adapter, power rating recorded in the report
- Owner's straight key and iambic paddle, 3.5 mm TRS plugs (SI-034)
- Pico-based logic capture (second Pico 2 with sigrok-pico firmware read by sigrok-cli; planned, ADR-009), 3.3 V inputs, 1 MS/s unless a step states otherwise
- Adjustable bench supply, 0 to 30 V, current limit set per step

**Expected artifacts.**

- `mismatch-fixtures.csv` (csv): Fixture, line section, reflection magnitude and phase
- `mismatch-stress-log.csv` (csv): Fixture, keying source, PA temperature, messages
- `mismatch-post-power-spurious.csv` (csv): Post-stress power and spurious readings
- `mismatch-board.jpg` (photo): Photograph of the PA and filter area after the stress

### TC-SYS-013: Keying envelope shape and 26 dB occupied bandwidth by transient simulation and FFT

| Field | Value |
|---|---|
| Requirements | REQ-SYS-014, REQ-SYS-015 |
| Method / class | Analysis / Simulation |
| Status | Draft |
| Automation | `hardware/sim/checks/keying_envelope_check.py` |

**Setup.** Article: design data at tag baseline/cdr: hardware/sim/tx/keying_envelope.asc with the CDR shaping network, PA and ALC models, driven by the firmware ramp tables for the 3, 5 and 8 ms settings exported from the release at CDR. Configuration: LTspice .tran of a continuous-dit sequence at 50 WPM for each setting; hardware/sim/checks/keying_envelope_check.py (planned) measures the 10-to-90 percent rise and fall times, the deviation from an ideal raised cosine, and the 26 dB bandwidth of the load-voltage spectrum by the 47 CFR 97.3(a)(8) power-containment definition (docs/research/regulatory-corpus-and-operators.md ACTION-8). Credit row: A. Analysis closed by Simulation on the CDR design data and confirmed at SAR by the physical configuration audit of every analyzed value (docs/process/04-verification-and-validation.md sections 5.1 item 5 and 5.2); the post-build readings named in the verification_note are supporting data only. TBR values: the acceptance criteria use the values of REQ-SYS-014, REQ-SYS-015 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Hazard controls exercised: HZ-008 (from the cited requirements; docs/safety/hazards.json). Risk acceptance: the verification_note of REQ-SYS-014 (RSK-011), REQ-SYS-015 (RSK-011) begins 'Analysis accepted per RSK-NNN'; that risk carries the hazard control not closed by Test (docs/process/04-verification-and-validation.md section 3, rule 7.3.6). Tools: LTspice through the batch wrapper tools/run_sim.py and Python per tools/toolchain.lock.md Safety: not applicable (design data only). Environment: not applicable.

**Procedure.**

1. Confirm that the deck part values and ramp tables equal the CDR schematic and the release ramp tables (script prints the diff; an empty diff is required).
2. Run the transient for the 3 ms setting through tools/run_sim.py and export the load voltage.
3. Run hardware/sim/checks/keying_envelope_check.py: 10-to-90 percent rise and fall times, maximum deviation of the normalized envelope from the ideal raised cosine of the same 10-to-90 time, and the 26 dB bandwidth.
4. Repeat the two previous steps for the 5 ms and the 8 ms settings.
5. Repeat the computation with every toleranced input at its worst-case corner (checker option --corners) and record the worst case.
6. Record tool versions, the design-data tag and the commit of every deck, model, script and checker in the report.
7. On any assertion or checker failure, or any difference between the analyzed values and the design data, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if at each of the 3, 5 and 8 ms settings the simulated rise and fall are raised cosines (normalized envelope within 5 percent of full scale of the ideal raised cosine at every sample), the 10-to-90 percent times equal the setting within +/-0.5 ms, and the 26 dB bandwidth of continuous dits at 50 WPM is at most 350 Hz, nominal and at every tolerance corner; otherwise Fail. The 5 percent and 0.5 ms shape tolerances are the test author's, because REQ-SYS-014 states none.

**Expected artifacts.**

- `keying-envelope-3-5-8ms.csv` (csv): Envelope samples per setting, nominal and corners
- `keying-spectrum.png` (plot): Spectrum per setting with the 26 dB bandwidth marked
- `keying-envelope-check.log.txt` (log): Checker output with the deck diff and pass/fail per value

### TC-SYS-014: Spurious emissions from 9 kHz to 1.5 GHz at every step, three frequencies and the pack voltage extremes

| Field | Value |
|---|---|
| Requirements | REQ-SYS-017, REQ-SYS-018 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | `tools/tinysa_scan_check.py` |

**Setup.** Article: CWHT-A-001 in its enclosure, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: antenna port to the calibrated power attenuator and the tinySA Ultra; bench supply through the pack-resistance fixture; keyed by the Bench-test continuous-dit generator at 25 WPM (at most 60 s per activation) with max-hold over the keyed dits; spurious means any discrete signal outside the carrier +/-10 kHz (inside that window the close-in keying spectrum is the Analysis of TC-SYS-013, 04 section 6.1); span segmented so that the noise floor referred to the antenna port is at least 6 dB below -23 dBm; readings corrected by the attenuator S21 of this session. Blocked until OQ-VV-001 closes and the tinySA TV record exists (04 section 6.3). Credit row: T-HW. Test of a system requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the campaign (section 13) and witnessed by the owner; the pre-build Simulation, HostUnit and Emulation evidence named in each requirement's verification_note is supporting only and is not part of this case. TBR values: the acceptance criteria use the values of REQ-SYS-018 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Hazard controls exercised: HZ-008 (from the cited requirements; docs/safety/hazards.json). Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: every transmission goes into the 50 ohm dummy load or the calibrated power attenuator, connected before power-on, never into an open antenna port; key-down duty kept within the load rating recorded in the report; anyone other than the operator stays 0.6 m or more from the unit and load while keying and 1.0 m or more during a tune carrier (NGO-019); the bench supply current limit is set before each power-on; antistatic wrist strap while the lid is off; the PA area is not touched after key-down runs. Environment: room temperature 18 to 28 C; the pack is supplied by the bench supply at 7.4 V +/-0.05 V through the battery terminals unless a step sets another value; dummy load on the antenna port.

**Procedure.**

1. Measure the attenuator and cable S21 on the NanoVNA from 9 kHz (or the NanoVNA lower limit) to 1.5 GHz and save the Touchstone file; run the tinySA Ultra internal calibration-output check; record both.
2. At 146.00 MHz, 7.4 V and the 5 W step, read the key-down carrier level (max-hold, 10 kHz span) and compute the carrier power at the antenna port.
3. Scan 9 kHz to 1.5 GHz in segments with max-hold for at least 20 s of dits per segment; record 2f, 3f and 7f individually and every other signal more than 6 dB above the noise floor.
4. For every recorded signal within 10 dB of -16.0 dBm or of 60 dB below the carrier, add 10 dB of attenuation and re-read: a true emission drops by 10 dB +/-1 dB; a signal that drops by more is analyzer-generated, excluded and recorded.
5. Repeat the carrier and scan steps at 144.05 and 147.95 MHz for the 5 W step at 7.4 V.
6. Repeat the scan at 144.05, 146.00 and 147.95 MHz for the 0.5, 1, 2 and 5 W steps at 6.4 V and at 8.4 V (24 combinations).
7. At 146.00 MHz, 5 W and 7.4 V, re-read 2f and 3f keyed by the straight key (3 s holds) and by the paddle (squeeze at 25 WPM); compare with the generator readings.
8. Run tools/tinysa_scan_check.py on the exported traces: corrects for attenuator S21, adds the tinySA level accuracy, and reports each emission in dBm at the antenna port and in dB below the carrier.
9. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
10. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if every spurious emission at the antenna port, corrected for the attenuator and increased by the tinySA level accuracy, is at most -16.0 dBm (25 uW) in all 24 step, frequency and pack-voltage combinations (REQ-SYS-017), and at the 5 W step at 144.05, 146.00 and 147.95 MHz every spurious emission is at least 60 dB below the mean carrier power (REQ-SYS-018), with 2f, 3f and 7f reported individually; otherwise Fail. Straight-key and paddle readings within 1 dB of the generator readings confirm the keying source does not change the result; a larger difference is a Procedure-correction NCR.

**Instruments and fixtures.**

- tinySA Ultra spectrum analyzer (ADR-021) through the calibrated 30 to 40 dB attenuator rated 10 W or more, attenuator S21 measured on the NanoVNA in the same session; level accuracy per its TV record
- NanoVNA, SOL calibration at the cable end used, checked on the dummy load
- Adjustable bench supply, 0 to 30 V, current limit set per step
- Pack-resistance fixture: series resistor equal to the datasheet internal resistance of two cells plus two holders, in the bench-supply lead (docs/vv/fixtures/pack-resistance.md, planned)
- Owner's straight key and iambic paddle, 3.5 mm TRS plugs (SI-034)

**Expected artifacts.**

- `spurious-scans.csv` (csv): Combination, frequency, corrected level in dBm and dBc for every recorded emission
- `spurious-traces.png` (plot): tinySA traces per segment and combination
- `attenuator-s21.s2p` (other): Attenuator and cable S21 of the session
- `spurious-check.log.txt` (log): tools/tinysa_scan_check.py output with pass/fail

### TC-SYS-015: Tune carrier at 0.5 W unless a higher step is confirmed, ended within 5.5 s

| Field | Value |
|---|---|
| Requirements | REQ-SYS-019, REQ-SYS-020 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | `tools/analyze_logic_capture.py` |

**Setup.** Article: CWHT-A-001, enclosure lid off for test-point access, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: dummy load with the diode probe on its T; logic capture on TX_KEY and PA_EN; operating step set to 5 W before each tune activation to show the tune step is independent of it. Credit row: T-HW. Test of a system requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the campaign (section 13) and witnessed by the owner; the pre-build Simulation, HostUnit and Emulation evidence named in each requirement's verification_note is supporting only and is not part of this case. TBR values: the acceptance criteria use the values of REQ-SYS-019, REQ-SYS-020 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Hazard controls exercised: HZ-001, HZ-006, HZ-012 (from the cited requirements; docs/safety/hazards.json). Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: every transmission goes into the 50 ohm dummy load or the calibrated power attenuator, connected before power-on, never into an open antenna port; key-down duty kept within the load rating recorded in the report; anyone other than the operator stays 0.6 m or more from the unit and load while keying and 1.0 m or more during a tune carrier (NGO-019); the bench supply current limit is set before each power-on; antistatic wrist strap while the lid is off; the PA area is not touched after key-down runs. Environment: room temperature 18 to 28 C; the pack is supplied by the bench supply at 7.4 V +/-0.05 V through the battery terminals unless a step sets another value; dummy load on the antenna port.

**Procedure.**

1. Run the logic-capture reference pulse-train check of this session and record the result (docs/process/04-verification-and-validation.md section 4).
2. Confirm that TC-SYS-010 is Passed and copy its uncertainty into the report.
3. With the operating step at 5 W, activate Tune without confirming a higher step; read the probe during the carrier.
4. Repeat with the operating step at 1 W and at 0.5 W.
5. Activate Tune and confirm the 5 W step for this activation; read the probe.
6. Activate Tune three times at 0.5 W and three times at the confirmed 5 W, never pressing any control, and capture TX_KEY and PA_EN.
7. Close the straight key once and the paddle once during a tune carrier and confirm the carrier ends (ConOps T13).
8. Export the capture and run tools/analyze_logic_capture.py to measure each carrier duration from PA_EN rise to fall.
9. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
10. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if the tune carrier without a confirmed higher step lies inside 0.397 to 0.629 W with the probe uncertainty band whatever the operating step, 5 W is reached only after the confirmation (REQ-SYS-019), and every tune carrier ends at most 5.5 s after it starts (REQ-SYS-020); otherwise Fail.

**Instruments and fixtures.**

- Diode RF probe (1N5711 or equivalent, printed housing) on a BNC T at the dummy load, characterized by TC-SYS-010, read on the multimeter DC voltage range
- Multimeter, DC voltage and DC current ranges, accuracy per datasheet copied into the report (OQ-VV-003)
- Pico-based logic capture (second Pico 2 with sigrok-pico firmware read by sigrok-cli; planned, ADR-009), 3.3 V inputs, 1 MS/s unless a step states otherwise
- 50 ohm BNC dummy load with SMA adapter, power rating recorded in the report
- Owner's straight key and iambic paddle, 3.5 mm TRS plugs (SI-034)
- Adjustable bench supply, 0 to 30 V, current limit set per step

**Expected artifacts.**

- `tune-power.csv` (csv): Operating step, confirmation, probe reading and power
- `tune-durations.csv` (csv): Activation, step and carrier duration

### TC-SYS-016: Reception of A1A signals from 144.000 to 148.000 MHz

| Field | Value |
|---|---|
| Requirements | REQ-SYS-021 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | none (manual) |

**Setup.** Article: CWHT-A-001 in its enclosure, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: tinySA Ultra generator output through a fixed attenuation of at least 60 dB (NanoVNA-characterized pads) into the antenna port, used as an unmodulated carrier source; headphone output into the 32 ohm audio load read on the multimeter; guest lock set so that no transmission can reach the generator. Credit row: T-HW. Test of a system requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the campaign (section 13) and witnessed by the owner; the pre-build Simulation, HostUnit and Emulation evidence named in each requirement's verification_note is supporting only and is not part of this case. Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: guest lock is set and the key jack is empty while the generator is on the antenna port; bench supply current limit set before power-on. Environment: room temperature 18 to 28 C; the pack is supplied by the bench supply at 7.4 V +/-0.05 V through the battery terminals unless a step sets another value; dummy load on the antenna port.

**Procedure.**

1. Characterize the pad chain S21 at 146 MHz on the NanoVNA and record it.
2. Set the generator to 144.000 MHz plus the sidetone offset so that the carrier falls in the passband when the unit is tuned to 144.000 MHz; set the generator level so that the level at the antenna port is about -100 dBm.
3. Tune the unit to 144.000 MHz, set volume to the cap step, and read the audio RMS with the generator on and then off.
4. Repeat at 146.000 and 148.000 MHz.
5. Keying the generator output on and off at about 1 Hz (generator output toggle), confirm by ear on the audio load through a monitoring amplifier or by the multimeter that the tone follows (A1A).
6. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
7. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if at 144.000, 146.000 and 148.000 MHz the audio RMS with the carrier present is at least 10 dB above the reading with it absent and follows the on-off keying of the source; otherwise Fail.

**Instruments and fixtures.**

- tinySA Ultra signal generator output used as a frequency source and relative level source only, never as a level reference (docs/process/04-verification-and-validation.md section 6.2)
- NanoVNA, SOL calibration at the cable end used, checked on the dummy load
- Multimeter, true-RMS AC voltage range, accuracy at 700 Hz per datasheet copied into the report (OQ-VV-003)
- Audio load fixture: 16, 32 and 64 ohm resistors, 0.25 W, selectable on a 3.5 mm TRS breakout per channel (docs/vv/fixtures/audio-load.md, planned)
- Adjustable bench supply, 0 to 30 V, current limit set per step

**Expected artifacts.**

- `rx-range.csv` (csv): Frequency, audio RMS with and without carrier

### TC-SYS-017: Receiver minimum discernible signal from the noise-figure and filter-loss cascade

| Field | Value |
|---|---|
| Requirements | REQ-SYS-022, REQ-SYS-023 |
| Method / class | Analysis / Simulation |
| Status | Draft |
| Automation | `tools/budgets/rx_noise_cascade.py` |

**Setup.** Article: design data at tag baseline/cdr: the receive line-up of the TS-001 architecture selected at PDR, with CDR part values, filter insertion losses (NanoVNA-measured where a supporting L2 Test exists, datasheet otherwise) and device noise figures. Configuration: tools/budgets/rx_noise_cascade.py (planned) computes the Friis cascade from the antenna port to the detector at 144.05, 146.00 and 147.95 MHz and MDS = -174 dBm/Hz + 10 log10(500 Hz) + NF (TPM-005). Credit row: A. Analysis closed by Simulation on the CDR design data and confirmed at SAR by the physical configuration audit of every analyzed value (docs/process/04-verification-and-validation.md sections 5.1 item 5 and 5.2); the post-build readings named in the verification_note are supporting data only. TBR values: the acceptance criteria use the values of REQ-SYS-022, REQ-SYS-023 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Tools: Python per tools/toolchain.lock.md Safety: not applicable (design data only). Environment: not applicable.

**Procedure.**

1. Confirm that the cascade stages and values equal the CDR line-up (script prints the diff; an empty diff is required).
2. Run tools/budgets/rx_noise_cascade.py and save the per-stage gain, noise figure and cumulative noise figure at the three frequencies.
3. Compute MDS in 500 Hz at each frequency.
4. Repeat the computation with every toleranced input at its worst-case corner (checker option --corners) and record the worst case.
5. Record tool versions, the design-data tag and the commit of every deck, model, script and checker in the report.
6. On any assertion or checker failure, or any difference between the analyzed values and the design data, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if the worst-case MDS in 500 Hz over the three frequencies and all tolerance corners is at most -140 dBm (REQ-SYS-022, noise figure 7 dB or less) and at most -142 dBm (REQ-SYS-023, noise figure 5 dB or less); otherwise Fail, reported separately for each requirement.

**Expected artifacts.**

- `rx-noise-cascade.csv` (csv): Stage gains, noise figures and MDS per frequency and corner
- `rx-noise-cascade.log.txt` (log): Script output with the line-up diff

### TC-SYS-018: End-to-end receive selectivity: -6 dB and -60 dB bandwidths, stopband, ultimate rejection and ripple

| Field | Value |
|---|---|
| Requirements | REQ-SYS-024, REQ-SYS-025, REQ-SYS-026, REQ-SYS-027, REQ-SYS-028 |
| Method / class | Analysis / Simulation |
| Status | Draft |
| Automation | `hardware/sim/checks/rx_selectivity_check.py` |

**Setup.** Article: design data at tag baseline/cdr: the passive filter path response (NanoVNA S21 through test connectors from the supporting L2 Test where it exists, otherwise the CDR LTspice model with the vendor or tolerance-designed crystal models) and, for architecture B, the DSP filter response from the HostUnit case of the REQ-SW child; simulation data under docs/research/sim/cw-selectivity/. Configuration: hardware/sim/checks/rx_selectivity_check.py (planned) cascades the passive and DSP responses on one frequency grid relative to the passband centre and measures each quantity (04 section 6.2 receiver and audio frequency response row). Credit row: A. Analysis closed by Simulation on the CDR design data and confirmed at SAR by the physical configuration audit of every analyzed value (docs/process/04-verification-and-validation.md sections 5.1 item 5 and 5.2); the post-build readings named in the verification_note are supporting data only. TBR values: the acceptance criteria use the values of REQ-SYS-024, REQ-SYS-025, REQ-SYS-026, REQ-SYS-027, REQ-SYS-028 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Tools: LTspice through the batch wrapper tools/run_sim.py and Python per tools/toolchain.lock.md Safety: not applicable (design data only). Environment: not applicable.

**Procedure.**

1. Confirm that the input responses are the CDR data sets (checker prints their paths and hashes).
2. Run hardware/sim/checks/rx_selectivity_check.py and save the combined response from -10 kHz to +10 kHz about the passband centre.
3. Read the -6 dB bandwidth, the -60 dB bandwidth, the minimum attenuation from 2 kHz to 5 kHz either side of centre, the minimum attenuation beyond 5 kHz, and the peak-to-peak ripple inside the -6 dB points.
4. Repeat the computation with every toleranced input at its worst-case corner (checker option --corners) and record the worst case.
5. Record tool versions, the design-data tag and the commit of every deck, model, script and checker in the report.
6. On any assertion or checker failure, or any difference between the analyzed values and the design data, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if, nominal and at every tolerance corner, the -6 dB bandwidth is from 400 Hz to 600 Hz, the -60 dB bandwidth is at most 2.5 kHz, attenuation from 2 kHz to 5 kHz either side of centre is at least 60 dB, attenuation beyond 5 kHz is at least 80 dB, and passband ripple is at most 2 dB; otherwise Fail, reported per requirement.

**Expected artifacts.**

- `rx-selectivity.csv` (csv): Combined response in dB versus offset, nominal and corners
- `rx-selectivity.png` (plot): Combined response with the five limit masks drawn
- `rx-selectivity-check.log.txt` (log): Checker output with per-quantity pass/fail

### TC-SYS-019: Adjacent-signal desensitization and reciprocal-mixing dynamic range from selectivity and phase noise

| Field | Value |
|---|---|
| Requirements | REQ-SYS-029, REQ-SYS-031 |
| Method / class | Analysis / Simulation |
| Status | Draft |
| Automation | `tools/budgets/rx_reciprocal_mixing.py` |

**Setup.** Article: design data at tag baseline/cdr: the combined selectivity response of the selectivity case, the local-oscillator phase-noise data of the synthesizer and reference selected by TS-002 (measured or primary-source), and the receive gain distribution. Configuration: tools/budgets/rx_reciprocal_mixing.py (planned) integrates the phase noise over the passband at 2 kHz and 10 kHz offsets and adds the selectivity leakage of the interferer. Credit row: A. Analysis closed by Simulation on the CDR design data and confirmed at SAR by the physical configuration audit of every analyzed value (docs/process/04-verification-and-validation.md sections 5.1 item 5 and 5.2); the post-build readings named in the verification_note are supporting data only. TBR values: the acceptance criteria use the values of REQ-SYS-029, REQ-SYS-031 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Tools: Python per tools/toolchain.lock.md Safety: not applicable (design data only). Environment: not applicable.

**Procedure.**

1. Confirm that the phase-noise data set and the selectivity response are the CDR data (script prints their paths and hashes).
2. Compute the (S+N)/N loss of a -130 dBm wanted signal with a -60 dBm unmodulated interferer 2 kHz away, from reciprocal mixing plus filter leakage plus any compression of the gain stages.
3. Compute the reciprocal-mixing dynamic range at 10 kHz offset in 500 Hz as RMDR = -L(10 kHz) - 10 log10(500 Hz).
4. Repeat the computation with every toleranced input at its worst-case corner (checker option --corners) and record the worst case.
5. Record tool versions, the design-data tag and the commit of every deck, model, script and checker in the report.
6. On any assertion or checker failure, or any difference between the analyzed values and the design data, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if the (S+N)/N loss of the -130 dBm signal with the -60 dBm signal 2 kHz away is at most 3 dB and the reciprocal-mixing dynamic range at 10 kHz offset in 500 Hz is at least 85 dB (phase noise -112 dBc/Hz or lower at 10 kHz), nominal and at the corners; otherwise Fail, reported per requirement.

**Expected artifacts.**

- `reciprocal-mixing.csv` (csv): Offset, phase noise, integrated noise and results
- `reciprocal-mixing.log.txt` (log): Script output with input hashes

### TC-SYS-020: Receive level control: no gain pumping from an adjacent keyed signal and audio level over -120 to -20 dBm

| Field | Value |
|---|---|
| Requirements | REQ-SYS-030, REQ-SYS-032 |
| Method / class | Analysis / Simulation |
| Status | Draft |
| Automation | `hardware/sim/checks/agc_loop_check.py` |

**Setup.** Article: design data at tag baseline/cdr: the AGC or digital level-control model of the TS-001 architecture with the detector placement, the combined selectivity response and the CDR gain distribution. Configuration: hardware/sim/checks/agc_loop_check.py (planned) runs the level-control loop in the time domain with a 20 WPM keyed interferer and sweeps a steady wanted signal from -120 to -20 dBm. Credit row: A. Analysis closed by Simulation on the CDR design data and confirmed at SAR by the physical configuration audit of every analyzed value (docs/process/04-verification-and-validation.md sections 5.1 item 5 and 5.2); the post-build readings named in the verification_note are supporting data only. TBR values: the acceptance criteria use the values of REQ-SYS-030, REQ-SYS-032 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Tools: LTspice through the batch wrapper tools/run_sim.py and Python per tools/toolchain.lock.md Safety: not applicable (design data only). Environment: not applicable.

**Procedure.**

1. Confirm that the model parameters equal the CDR design (checker prints the diff; an empty diff is required).
2. Simulate a -130 dBm steady wanted signal with a -60 dBm interferer 2 kHz away keyed at 20 WPM for 10 s, and record the wanted-signal audio level envelope.
3. Simulate a steady CW signal stepped from -120 dBm to -20 dBm in 10 dB steps, and record the settled audio level at each step.
4. Repeat the computation with every toleranced input at its worst-case corner (checker option --corners) and record the worst case.
5. Record tool versions, the design-data tag and the commit of every deck, model, script and checker in the report.
6. On any assertion or checker failure, or any difference between the analyzed values and the design data, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if the -130 dBm signal's audio level stays within 1 dB of its level without the interferer throughout the keyed interferer run, and the audio level of the CW signal stays within a 6 dB window from -120 dBm to -20 dBm, nominal and at the corners; otherwise Fail, reported per requirement.

**Expected artifacts.**

- `agc-pumping.csv` (csv): Audio level of the wanted signal versus time with the keyed interferer
- `agc-range.csv` (csv): Settled audio level versus input level
- `agc-loop-check.log.txt` (log): Checker output

### TC-SYS-021: Image and intermediate-frequency response rejection from the front-end and mixer responses

| Field | Value |
|---|---|
| Requirements | REQ-SYS-033 |
| Method / class | Analysis / Simulation |
| Status | Draft |
| Automation | `tools/budgets/rx_spurious_response.py` |

**Setup.** Article: design data at tag baseline/cdr: front-end filter models (CDR values) and the frequency plan (LO and IF) of the selected architecture. Configuration: tools/budgets/rx_spurious_response.py (planned) computes the image and IF frequencies for tuned frequencies across 144.000 to 148.000 MHz and the front-end attenuation at each (04 section 6.2 image rejection row). Credit row: A. Analysis closed by Simulation on the CDR design data and confirmed at SAR by the physical configuration audit of every analyzed value (docs/process/04-verification-and-validation.md sections 5.1 item 5 and 5.2); the post-build readings named in the verification_note are supporting data only. TBR values: the acceptance criteria use the values of REQ-SYS-033 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Tools: LTspice through the batch wrapper tools/run_sim.py and Python per tools/toolchain.lock.md Safety: not applicable (design data only). Environment: not applicable.

**Procedure.**

1. Confirm that the filter models and frequency plan equal the CDR design (script prints the diff; an empty diff is required).
2. Compute the image and IF response frequencies for tuned frequencies at 100 kHz spacing across the band.
3. Compute the attenuation of each response relative to the in-band response from the simulated front-end S21 and the mixer port isolation.
4. Repeat the computation with every toleranced input at its worst-case corner (checker option --corners) and record the worst case.
5. Record tool versions, the design-data tag and the commit of every deck, model, script and checker in the report.
6. On any assertion or checker failure, or any difference between the analyzed values and the design data, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if every image and IF response is at least 70 dB below the in-band response at every tuned frequency, nominal and at the corners; otherwise Fail.

**Expected artifacts.**

- `rx-spurious-responses.csv` (csv): Tuned frequency, response frequency and rejection

### TC-SYS-022: Internally generated receive responses from 144.010 to 147.999 MHz

| Field | Value |
|---|---|
| Requirements | REQ-SYS-034 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | `tools/analyze_birdie_survey.py` |

**Setup.** Article: CWHT-A-001, enclosure lid off for test-point access, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: antenna port terminated in the dummy load; guest lock set; audio into the 32 ohm load read by the multimeter (true RMS) or, if the software design provides it, by the audio-level field of the telemetry; level control held fixed if the Bench-test mode offers it; predicted birdie list from the clock-harmonic table of the clock plan; tinySA Ultra with a near-field probe for the predicted sources. Credit row: T-HW. Test of a system requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the campaign (section 13) and witnessed by the owner; the pre-build Simulation, HostUnit and Emulation evidence named in each requirement's verification_note is supporting only and is not part of this case. TBR values: the acceptance criteria use the values of REQ-SYS-034 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Hazard controls exercised: HZ-008 (from the cited requirements; docs/safety/hazards.json). Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: guest lock is set and the key jack is empty; bench supply current limit set before power-on; antistatic wrist strap while the lid is off. Environment: room temperature 18 to 28 C; the pack is supplied by the bench supply at 7.4 V +/-0.05 V through the battery terminals unless a step sets another value; dummy load on the antenna port.

**Procedure.**

1. Wire the UART telemetry test pad to a logic-capture channel and confirm that the sigrok-cli UART decoder prints the telemetry lines (REQ-SYS-150).
2. Record the noise-floor audio RMS at 146.000 MHz and at five other frequencies spread across the band; take the median as the noise reference.
3. For each predicted birdie frequency, tune from 2 kHz below to 2 kHz above in 250 Hz steps and record the audio RMS at each step.
4. Sweep 144.010 to 147.999 MHz in 250 Hz steps with the Bench-test sweep function if the software design provides one, logging the audio level; otherwise the owner sweeps at 1 kHz steps by ear and every audible tone is measured as in the previous step.
5. For every response found, probe the board with the near-field probe on the tinySA Ultra and record the probable source.
6. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
7. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if the audio RMS at every tuned frequency from 144.010 to 147.999 MHz is at most 1.41 times the noise reference (at most 3 dB above the MDS noise level); otherwise Fail. If neither the Bench-test sweep nor a 250 Hz manual sweep of the full range is available, the case result is Blocked for the unswept frequencies and the owner decides at TRR.

**Instruments and fixtures.**

- Multimeter, true-RMS AC voltage range, accuracy at 700 Hz per datasheet copied into the report (OQ-VV-003)
- Audio load fixture: 16, 32 and 64 ohm resistors, 0.25 W, selectable on a 3.5 mm TRS breakout per channel (docs/vv/fixtures/audio-load.md, planned)
- tinySA Ultra spectrum analyzer (ADR-021) through the calibrated 30 to 40 dB attenuator rated 10 W or more, attenuator S21 measured on the NanoVNA in the same session; level accuracy per its TV record
- 50 ohm BNC dummy load with SMA adapter, power rating recorded in the report
- Pico-based logic capture (second Pico 2 with sigrok-pico firmware read by sigrok-cli; planned, ADR-009), 3.3 V inputs, 1 MS/s unless a step states otherwise
- Adjustable bench supply, 0 to 30 V, current limit set per step

**Expected artifacts.**

- `birdie-survey.csv` (csv): Tuned frequency and audio RMS
- `birdie-sources.csv` (csv): Response frequency, level and probable source

### TC-SYS-023: Receive filter-centre calibration trim over +/-500 Hz in 10 Hz steps, retained across a power cycle

| Field | Value |
|---|---|
| Requirements | REQ-SYS-035 |
| Method / class | Demonstration / Bench |
| Status | Draft |
| Automation | none (manual) |

**Setup.** Article: CWHT-A-001 in its enclosure, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: calibration menu; values read from the display and photographed. Credit row: D. Demonstration by the owner on the delivered unit (docs/process/04-verification-and-validation.md section 5.2): pass or fail is observed without detailed data gathering and each observation is photographed or logged. TBR values: the acceptance criteria use the values of REQ-SYS-035 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: no transmission is intended; the dummy load stays on the antenna port throughout so that an unintended key-down is absorbed; bench supply current limit set before power-on; antistatic wrist strap while the lid is off. Environment: room temperature 18 to 28 C; the pack is supplied by the bench supply at 7.4 V +/-0.05 V through the battery terminals unless a step sets another value; dummy load on the antenna port.

**Procedure.**

1. Open the calibration menu and set the trim to -500 Hz; photograph.
2. Step up one 10 Hz step and back; photograph each value.
3. Set 0 Hz, then +500 Hz; photograph.
4. Attempt one step beyond +500 Hz and beyond -500 Hz; photograph the value shown.
5. Set +370 Hz, power-cycle, and read the stored value.
6. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
7. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if the trim takes -500, 0 and +500 Hz, moves in single 10 Hz steps, does not go beyond +/-500 Hz, and the stored value is shown unchanged after the power cycle; otherwise Fail.

**Instruments and fixtures.**

- Host computer with picotool and a serial terminal per tools/toolchain.lock.md, micro-USB cable
- Adjustable bench supply, 0 to 30 V, current limit set per step

**Expected artifacts.**

- `trim-demo.jpg` (photo): Photographs of each displayed trim value

### TC-SYS-024: Receive sensitivity recovery after hang expiry from T/R release and LNA supply settling

| Field | Value |
|---|---|
| Requirements | REQ-SYS-036 |
| Method / class | Analysis / Simulation |
| Status | Draft |
| Automation | `hardware/sim/checks/rx_recovery_check.py` |

**Setup.** Article: design data at tag baseline/cdr: the relay datasheet release and bounce times, the LNA supply switch and its decoupling, and the receive-chain model including the level-control state at hang expiry. Configuration: hardware/sim/checks/rx_recovery_check.py (planned) simulates the LNA supply settling and the receive-chain gain recovery from the T/R release command and adds the relay release plus bounce time from the datasheet. Credit row: A. Analysis closed by Simulation on the CDR design data and confirmed at SAR by the physical configuration audit of every analyzed value (docs/process/04-verification-and-validation.md sections 5.1 item 5 and 5.2); the post-build readings named in the verification_note are supporting data only. TBR values: the acceptance criteria use the values of REQ-SYS-036 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Tools: LTspice through the batch wrapper tools/run_sim.py and Python per tools/toolchain.lock.md Safety: not applicable (design data only). Environment: not applicable.

**Procedure.**

1. Confirm that the model values equal the CDR design (checker prints the diff; an empty diff is required).
2. Simulate from the hang-expiry command: relay release and bounce (datasheet maximum), LNA supply rise and settling, and chain gain recovery.
3. Find the time after hang expiry at which the modelled noise figure returns to within 3 dB of its steady value (MDS within 3 dB).
4. Repeat the computation with every toleranced input at its worst-case corner (checker option --corners) and record the worst case.
5. Record tool versions, the design-data tag and the commit of every deck, model, script and checker in the report.
6. On any assertion or checker failure, or any difference between the analyzed values and the design data, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if the receive chain is within 3 dB of its steady MDS at most 50 ms after hang expiry, nominal and at the corners; otherwise Fail.

**Expected artifacts.**

- `rx-recovery.csv` (csv): Time versus modelled noise figure after hang expiry
- `rx-recovery-check.log.txt` (log): Checker output

### TC-SYS-025: Receiver survival of +27 dBm at the antenna port

| Field | Value |
|---|---|
| Requirements | REQ-SYS-037 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | none (manual) |

**Setup.** Article: CWHT-A-001 in its enclosure, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: a second cwht unit (CWHT-A-002) at its 5 W step as the source, its power measured with the diode probe first, through a 10 dB pad rated 10 W or more (NanoVNA-characterized) into the unit under test's antenna port; the unit under test in Receive with guest lock set; noise floor and a weak tone from the tinySA Ultra generator (relative source) read as audio RMS on the multimeter before and after. If no second unit is available the case is Blocked (04 section 8.3 item 5). Credit row: T-HW. Test of a system requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the campaign (section 13) and witnessed by the owner; the pre-build Simulation, HostUnit and Emulation evidence named in each requirement's verification_note is supporting only and is not part of this case. TBR values: the acceptance criteria use the values of REQ-SYS-037 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: the second unit transmits only into the 10 dB pad and the unit under test's antenna port, or into the dummy load for its power check, never into an open port; the unit under test has guest lock set and no key; the tinySA generator is disconnected before the second unit keys; bystanders 0.6 m or more; bench supply current limits set before power-on. Environment: room temperature 18 to 28 C; the pack is supplied by the bench supply at 7.4 V +/-0.05 V through the battery terminals unless a step sets another value; dummy load on the antenna port.

**Procedure.**

1. Characterize the 10 dB pad at 146 MHz on the NanoVNA.
2. Measure the second unit's 5 W step power into the dummy load with the diode probe; compute the level delivered through the pad.
3. On the unit under test, record the audio RMS of the noise floor and of a tinySA generator tone at a fixed low level at 146.00 MHz.
4. Connect the second unit through the pad to the unit under test; key the second unit with its straight key for 5 s on and 1.25 s off for 60 s (80 percent duty).
5. Repeat the 60 s run keyed with the second unit's paddle squeezed at 50 WPM.
6. Reconnect the tinySA generator at the same setting and repeat the noise-floor and tone readings.
7. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
8. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if the level delivered to the antenna port is at least +27 dBm during both runs and, afterwards, the noise-floor and tone audio readings are within 1 dB of their values before the runs; otherwise Fail.

**Instruments and fixtures.**

- Diode RF probe (1N5711 or equivalent, printed housing) on a BNC T at the dummy load, characterized by TC-SYS-010, read on the multimeter DC voltage range
- Multimeter, DC voltage and DC current ranges, accuracy per datasheet copied into the report (OQ-VV-003)
- Multimeter, true-RMS AC voltage range, accuracy at 700 Hz per datasheet copied into the report (OQ-VV-003)
- NanoVNA, SOL calibration at the cable end used, checked on the dummy load
- tinySA Ultra signal generator output used as a frequency source and relative level source only, never as a level reference (docs/process/04-verification-and-validation.md section 6.2)
- Audio load fixture: 16, 32 and 64 ohm resistors, 0.25 W, selectable on a 3.5 mm TRS breakout per channel (docs/vv/fixtures/audio-load.md, planned)
- Owner's straight key and iambic paddle, 3.5 mm TRS plugs (SI-034)
- Second cwht unit CWHT-A-002 as a characterized 5 W source (fixture), with a 10 dB pad rated 10 W or more
- Adjustable bench supply, 0 to 30 V, current limit set per step

**Expected artifacts.**

- `overload.csv` (csv): Source power, delivered level, readings before and after

### TC-SYS-026: Keying the transmitter with the owner's straight key and with the iambic paddle

| Field | Value |
|---|---|
| Requirements | REQ-SYS-038, REQ-SYS-039 |
| Method / class | Demonstration / Bench |
| Status | Draft |
| Automation | none (manual) |

**Setup.** Article: CWHT-A-001, enclosure lid off for test-point access, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: the owner's straight key and paddle one at a time on the key jack; dummy load; 0.5 W step; logic capture of the key contacts and TX_KEY recorded as the demonstration log; the confirming OnAir runs are TC-VAL cases for OPS-004 and OPS-005. Credit row: D. Demonstration by the owner on the delivered unit (docs/process/04-verification-and-validation.md section 5.2): pass or fail is observed without detailed data gathering and each observation is photographed or logged. Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: every transmission goes into the 50 ohm dummy load or the calibrated power attenuator, connected before power-on, never into an open antenna port; key-down duty kept within the load rating recorded in the report; anyone other than the operator stays 0.6 m or more from the unit and load while keying and 1.0 m or more during a tune carrier (NGO-019); the bench supply current limit is set before each power-on; antistatic wrist strap while the lid is off; the PA area is not touched after key-down runs. Environment: room temperature 18 to 28 C; the pack is supplied by the bench supply at 7.4 V +/-0.05 V through the battery terminals unless a step sets another value; dummy load on the antenna port.

**Procedure.**

1. Run the logic-capture reference pulse-train check of this session and record the result (docs/process/04-verification-and-validation.md section 4).
2. Select Straight; send the owner's call sign and a CQ with the straight key, including one long closure of 3 s.
3. Select Iambic A; send the same text with the paddle at 15 WPM, then at 25 WPM.
4. The owner observes the TX indicator and sidetone and compares the capture of TX_KEY with the contacts.
5. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
6. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if every straight-key closure keys the transmitter for the duration of the closure (REQ-SYS-038) and the paddle closures key the transmitter with the Morse elements of the text sent (REQ-SYS-039), as observed by the owner and shown in the capture; otherwise Fail.

**Instruments and fixtures.**

- Pico-based logic capture (second Pico 2 with sigrok-pico firmware read by sigrok-cli; planned, ADR-009), 3.3 V inputs, 1 MS/s unless a step states otherwise
- 50 ohm BNC dummy load with SMA adapter, power rating recorded in the report
- Owner's straight key and iambic paddle, 3.5 mm TRS plugs (SI-034)
- Adjustable bench supply, 0 to 30 V, current limit set per step

**Expected artifacts.**

- `keying-demo.sr` (other): Capture of the contacts and TX_KEY
- `keying-demo.jpg` (photo): Photograph of the setup

### TC-SYS-027: Keyer modes Straight, Iambic A, Iambic B, Ultimatic and Bug against the reference model

| Field | Value |
|---|---|
| Requirements | REQ-SYS-040 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | `tools/keyer_ref.py` |

**Setup.** Article: CWHT-A-001, enclosure lid off for test-point access, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: logic capture at 1 MS/s on the key tip and ring contacts at the jack, the keyer test point, TX_KEY, the T/R drive, the envelope drive and the sidetone PWM line as the steps name them; dummy load; 0.5 W step; the captured paddle-contact edges of each run are replayed through tools/keyer_ref.py and its output is compared with the captured keyer test point. Credit row: T-HW. Test of a system requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the campaign (section 13) and witnessed by the owner; the pre-build Simulation, HostUnit and Emulation evidence named in each requirement's verification_note is supporting only and is not part of this case. Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: every transmission goes into the 50 ohm dummy load or the calibrated power attenuator, connected before power-on, never into an open antenna port; key-down duty kept within the load rating recorded in the report; anyone other than the operator stays 0.6 m or more from the unit and load while keying and 1.0 m or more during a tune carrier (NGO-019); the bench supply current limit is set before each power-on; antistatic wrist strap while the lid is off; the PA area is not touched after key-down runs. Environment: room temperature 18 to 28 C; the pack is supplied by the bench supply at 7.4 V +/-0.05 V through the battery terminals unless a step sets another value; dummy load on the antenna port.

**Procedure.**

1. Run the logic-capture reference pulse-train check of this session and record the result (docs/process/04-verification-and-validation.md section 4).
2. Select Straight and send ten closures with the straight key; capture.
3. Select Iambic A at 20 WPM; with the paddle send single dits, single dahs, a squeeze released during a dah, a squeeze released during a dit and the letters C, K and R; capture.
4. Repeat the previous step in Iambic B.
5. Select Ultimatic and send the same patterns (squeezes held and released); capture.
6. Select Bug and send dits on the dit lever (automatic) and dahs on the dah lever (manual) including one long dah; capture.
7. Run tools/keyer_ref.py on each capture's contact edges and compare the model output with the captured keyer test point element by element.
8. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
9. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if in each of the five modes every captured element and space matches the reference model output in sequence, and each element edge is within +/-1 percent or +/-0.5 ms (whichever is larger) of the model's timing; otherwise Fail.

**Instruments and fixtures.**

- Pico-based logic capture (second Pico 2 with sigrok-pico firmware read by sigrok-cli; planned, ADR-009), 3.3 V inputs, 1 MS/s unless a step states otherwise
- 50 ohm BNC dummy load with SMA adapter, power rating recorded in the report
- Owner's straight key and iambic paddle, 3.5 mm TRS plugs (SI-034)
- Adjustable bench supply, 0 to 30 V, current limit set per step

**Expected artifacts.**

- `keyer-modes-compare.csv` (csv): Mode, pattern, element index, model and captured edges, difference
- `keyer-modes-capture.sr` (other): Raw captures per mode

### TC-SYS-028: Keyer speed range 5 to 50 WPM in 1 WPM steps and element and space timing accuracy

| Field | Value |
|---|---|
| Requirements | REQ-SYS-041, REQ-SYS-042 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | `tools/analyze_keyer_capture.py` |

**Setup.** Article: CWHT-A-001, enclosure lid off for test-point access, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: logic capture at 1 MS/s on the key tip and ring contacts at the jack, the keyer test point, TX_KEY, the T/R drive, the envelope drive and the sidetone PWM line as the steps name them; dummy load; 0.5 W step; Iambic A; PARIS sent by holding and squeezing the paddle as each step states. Credit row: T-HW. Test of a system requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the campaign (section 13) and witnessed by the owner; the pre-build Simulation, HostUnit and Emulation evidence named in each requirement's verification_note is supporting only and is not part of this case. Key types (SI-018, 04 section 8.2): both requirements concern keyer-generated paddle elements only; the straight-key variant of keying timing is covered by TC-SYS-102, TC-SYS-030 and TC-SYS-026. Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: every transmission goes into the 50 ohm dummy load or the calibrated power attenuator, connected before power-on, never into an open antenna port; key-down duty kept within the load rating recorded in the report; anyone other than the operator stays 0.6 m or more from the unit and load while keying and 1.0 m or more during a tune carrier (NGO-019); the bench supply current limit is set before each power-on; antistatic wrist strap while the lid is off; the PA area is not touched after key-down runs. Environment: room temperature 18 to 28 C; the pack is supplied by the bench supply at 7.4 V +/-0.05 V through the battery terminals unless a step sets another value; dummy load on the antenna port.

**Procedure.**

1. Run the logic-capture reference pulse-train check of this session and record the result (docs/process/04-verification-and-validation.md section 4).
2. At 5 WPM hold the dit lever for 10 elements, the dah lever for 10 elements and squeeze for 10 elements; capture the keyer test point.
3. Repeat at 15, 25 and 50 WPM.
4. Repeat the dit-lever run at 6, 14, 16, 24, 26 and 49 WPM.
5. Confirm on the menu that the speed setting moves in 1 WPM steps from 5 to 50 and cannot be set outside that range.
6. Run tools/analyze_keyer_capture.py on each capture: dit, dah, inter-element space and the implied WPM.
7. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
8. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if the menu offers every integer speed from 5 to 50 WPM and no other, each captured run's dit equals 1200/WPM ms at its setting (REQ-SYS-041), and every element and space at 5, 25 and 50 WPM (and the other captured speeds) is within +/-1 percent or +/-0.5 ms, whichever is larger, of its nominal (dit 1200/WPM ms, dah three dits, space one dit) (REQ-SYS-042), each tolerance widened by one capture sample; otherwise Fail.

**Instruments and fixtures.**

- Pico-based logic capture (second Pico 2 with sigrok-pico firmware read by sigrok-cli; planned, ADR-009), 3.3 V inputs, 1 MS/s unless a step states otherwise
- 50 ohm BNC dummy load with SMA adapter, power rating recorded in the report
- Owner's straight key and iambic paddle, 3.5 mm TRS plugs (SI-034)
- Adjustable bench supply, 0 to 30 V, current limit set per step

**Expected artifacts.**

- `keyer-speed.csv` (csv): WPM, element type, nominal, measured and error

### TC-SYS-029: Paddle-to-element latency and sidetone onset latency for key and paddle

| Field | Value |
|---|---|
| Requirements | REQ-SYS-043, REQ-SYS-159 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | `tools/analyze_logic_capture.py` |

**Setup.** Article: CWHT-A-001, enclosure lid off for test-point access, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: logic capture at 1 MS/s on the key tip and ring contacts at the jack, the keyer test point, TX_KEY, the T/R drive, the envelope drive and the sidetone PWM line as the steps name them; dummy load; 0.5 W step. Credit row: T-HW. Test of a system requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the campaign (section 13) and witnessed by the owner; the pre-build Simulation, HostUnit and Emulation evidence named in each requirement's verification_note is supporting only and is not part of this case. TBR values: the acceptance criteria use the values of REQ-SYS-159 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Hazard controls exercised: HZ-005 (from the cited requirements; docs/safety/hazards.json). Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: every transmission goes into the 50 ohm dummy load or the calibrated power attenuator, connected before power-on, never into an open antenna port; key-down duty kept within the load rating recorded in the report; anyone other than the operator stays 0.6 m or more from the unit and load while keying and 1.0 m or more during a tune carrier (NGO-019); the bench supply current limit is set before each power-on; antistatic wrist strap while the lid is off; the PA area is not touched after key-down runs. Environment: room temperature 18 to 28 C; the pack is supplied by the bench supply at 7.4 V +/-0.05 V through the battery terminals unless a step sets another value; dummy load on the antenna port.

**Procedure.**

1. Run the logic-capture reference pulse-train check of this session and record the result (docs/process/04-verification-and-validation.md section 4).
2. At 15 WPM, from idle (no element in progress, at least 1 s since the last), make 50 single dit-lever closures and capture the dit contact, the keyer test point and the sidetone PWM line.
3. Repeat at 50 WPM.
4. Select Straight and make 50 straight-key closures; capture the contact and the sidetone PWM line.
5. Run tools/analyze_logic_capture.py: contact-closure edge (first make) to keyer-test-point rise, and to the first sidetone PWM edge.
6. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
7. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if every paddle-initiated element from idle starts at the keyer test point at most 3 ms after the contact closure at 15 and 50 WPM (REQ-SYS-043), and the sidetone starts at most 4 ms after the contact closure for all 50 paddle and 50 straight-key closures (REQ-SYS-159); otherwise Fail.

**Instruments and fixtures.**

- Pico-based logic capture (second Pico 2 with sigrok-pico firmware read by sigrok-cli; planned, ADR-009), 3.3 V inputs, 1 MS/s unless a step states otherwise
- 50 ohm BNC dummy load with SMA adapter, power rating recorded in the report
- Owner's straight key and iambic paddle, 3.5 mm TRS plugs (SI-034)
- Adjustable bench supply, 0 to 30 V, current limit set per step

**Expected artifacts.**

- `latency-paddle.csv` (csv): Closure, speed, key type, element and sidetone latencies

### TC-SYS-030: Semi break-in hang time of 3 to 30 dits at the displayed speed

| Field | Value |
|---|---|
| Requirements | REQ-SYS-044 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | `tools/analyze_logic_capture.py` |

**Setup.** Article: CWHT-A-001, enclosure lid off for test-point access, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: logic capture at 1 MS/s on the key tip and ring contacts at the jack, the keyer test point, TX_KEY, the T/R drive, the envelope drive and the sidetone PWM line as the steps name them; dummy load; 0.5 W step. Credit row: T-HW. Test of a system requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the campaign (section 13) and witnessed by the owner; the pre-build Simulation, HostUnit and Emulation evidence named in each requirement's verification_note is supporting only and is not part of this case. TBR values: the acceptance criteria use the values of REQ-SYS-044 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: every transmission goes into the 50 ohm dummy load or the calibrated power attenuator, connected before power-on, never into an open antenna port; key-down duty kept within the load rating recorded in the report; anyone other than the operator stays 0.6 m or more from the unit and load while keying and 1.0 m or more during a tune carrier (NGO-019); the bench supply current limit is set before each power-on; antistatic wrist strap while the lid is off; the PA area is not touched after key-down runs. Environment: room temperature 18 to 28 C; the pack is supplied by the bench supply at 7.4 V +/-0.05 V through the battery terminals unless a step sets another value; dummy load on the antenna port.

**Procedure.**

1. Run the logic-capture reference pulse-train check of this session and record the result (docs/process/04-verification-and-validation.md section 4).
2. Confirm that the hang setting offers 3 to 30 dits and no other value.
3. At 5 WPM with the 3-dit setting, send a single dit with the paddle and wait; capture the keyer test point and the T/R drive. Repeat with the straight key in Straight mode.
4. Repeat for 8 and 30 dits, and all three settings at 15 and 50 WPM.
5. Run tools/analyze_logic_capture.py: last key-up at the keyer test point to T/R drive release.
6. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
7. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if for every speed and setting the time from the last key-up to the return to receive equals the setting times 1200/WPM ms within +/-1 percent or +/-0.5 ms, whichever is larger, for both key types; otherwise Fail. The tolerance is the test author's, taken from REQ-SYS-042, because REQ-SYS-044 states none.

**Instruments and fixtures.**

- Pico-based logic capture (second Pico 2 with sigrok-pico firmware read by sigrok-cli; planned, ADR-009), 3.3 V inputs, 1 MS/s unless a step states otherwise
- 50 ohm BNC dummy load with SMA adapter, power rating recorded in the report
- Owner's straight key and iambic paddle, 3.5 mm TRS plugs (SI-034)
- Adjustable bench supply, 0 to 30 V, current limit set per step

**Expected artifacts.**

- `hang.csv` (csv): WPM, setting, key type, nominal and measured hang

### TC-SYS-031: Sidetone frequency from 300 Hz to 1000 Hz in 10 Hz steps

| Field | Value |
|---|---|
| Requirements | REQ-SYS-045 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | `tools/analyze_logic_capture.py` |

**Setup.** Article: CWHT-A-001, enclosure lid off for test-point access, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: logic capture of the sidetone PWM line at 1 MS/s; tone frequency computed from the PWM duty sequence by tools/analyze_logic_capture.py --tone; PRACTICE set so that no transmission occurs. Credit row: T-HW. Test of a system requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the campaign (section 13) and witnessed by the owner; the pre-build Simulation, HostUnit and Emulation evidence named in each requirement's verification_note is supporting only and is not part of this case. Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: no transmission is intended; the dummy load stays on the antenna port throughout so that an unintended key-down is absorbed; bench supply current limit set before power-on; antistatic wrist strap while the lid is off. Environment: room temperature 18 to 28 C; the pack is supplied by the bench supply at 7.4 V +/-0.05 V through the battery terminals unless a step sets another value; dummy load on the antenna port.

**Procedure.**

1. Run the logic-capture reference pulse-train check of this session and record the result (docs/process/04-verification-and-validation.md section 4).
2. Set 300 Hz, hold the straight key for 2 s and capture; repeat holding the paddle dah lever.
3. Repeat at 310, 600, 610, 990 and 1000 Hz.
4. Confirm on the menu that the setting moves in 10 Hz steps from 300 to 1000 Hz.
5. Run the tone analysis on each capture.
6. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
7. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if the menu offers 300 to 1000 Hz in 10 Hz steps and each measured tone is within +/-5 Hz of its setting for both key types; otherwise Fail. The +/-5 Hz tolerance (half a step) is the test author's, because REQ-SYS-045 states none.

**Instruments and fixtures.**

- Pico-based logic capture (second Pico 2 with sigrok-pico firmware read by sigrok-cli; planned, ADR-009), 3.3 V inputs, 1 MS/s unless a step states otherwise
- Owner's straight key and iambic paddle, 3.5 mm TRS plugs (SI-034)
- Adjustable bench supply, 0 to 30 V, current limit set per step

**Expected artifacts.**

- `sidetone.csv` (csv): Setting, key type, measured frequency

### TC-SYS-032: CW pitch equals sidetone: frequency-plan analysis of receive LO, BFO and trim against the sidetone setting

| Field | Value |
|---|---|
| Requirements | REQ-SYS-046 |
| Method / class | Analysis / Simulation |
| Status | Draft |
| Automation | `tools/budgets/frequency_plan_check.py` |

**Setup.** Article: design data at tag baseline/cdr: the frequency plan, the synthesizer and BFO (or DSP offset) resolution, the sidetone generator resolution and the filter-centre trim range of REQ-SYS-035. Configuration: tools/budgets/frequency_plan_check.py (planned) computes, for each sidetone setting from 300 to 1000 Hz in 10 Hz steps and trim values -500, 0 and +500 Hz, the audio pitch of a carrier at the transmit frequency. Credit row: A. Analysis closed by Simulation on the CDR design data and confirmed at SAR by the physical configuration audit of every analyzed value (docs/process/04-verification-and-validation.md sections 5.1 item 5 and 5.2); the post-build readings named in the verification_note are supporting data only. Tools: Python per tools/toolchain.lock.md Safety: not applicable (design data only). Environment: not applicable.

**Procedure.**

1. Confirm that the plan constants equal the CDR design and firmware constants (script prints the diff; an empty diff is required).
2. Compute for every sidetone setting and the three trim values the pitch of a received carrier at the unit's own transmit frequency.
3. Compute the difference between that pitch and the generated sidetone frequency including both quantization errors.
4. Record tool versions, the design-data tag and the commit of every deck, model, script and checker in the report.
5. On any assertion or checker failure, or any difference between the analyzed values and the design data, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if the received pitch equals the sidetone frequency within 10 Hz at every sidetone setting from 300 to 1000 Hz and every trim value; otherwise Fail.

**Expected artifacts.**

- `pitch-vs-sidetone.csv` (csv): Sidetone setting, trim, received pitch and difference

### TC-SYS-033: Key contact thresholds, then survival of -5 V to +12 V on each key contact, then thresholds re-checked

| Field | Value |
|---|---|
| Requirements | REQ-SYS-047, REQ-SYS-049 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | none (manual) |

**Setup.** Article: CWHT-A-001, enclosure lid off for test-point access, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: a TRS breakout with a resistor substitution box (0, 100, 500 ohm; 100 kohm, 1 Mohm, open) across tip-sleeve and ring-sleeve; keyer test point on the logic capture; Straight mode for the tip, Iambic A for the ring; dummy load; 0.5 W step; for the abuse step the bench supply, current limit 50 mA, applied to tip and to ring. Credit row: T-HW. Test of a system requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the campaign (section 13) and witnessed by the owner; the pre-build Simulation, HostUnit and Emulation evidence named in each requirement's verification_note is supporting only and is not part of this case. TBR values: the acceptance criteria use the values of REQ-SYS-049 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Hazard controls exercised: HZ-010 (from the cited requirements; docs/safety/hazards.json). Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: every transmission goes into the 50 ohm dummy load or the calibrated power attenuator, connected before power-on, never into an open antenna port; key-down duty kept within the load rating recorded in the report; anyone other than the operator stays 0.6 m or more from the unit and load while keying and 1.0 m or more during a tune carrier (NGO-019); the bench supply current limit is set before each power-on; antistatic wrist strap while the lid is off; the PA area is not touched after key-down runs. Environment: room temperature 18 to 28 C; the pack is supplied by the bench supply at 7.4 V +/-0.05 V through the battery terminals unless a step sets another value; dummy load on the antenna port.

**Procedure.**

1. Run the logic-capture reference pulse-train check of this session and record the result (docs/process/04-verification-and-validation.md section 4).
2. Tip: apply 0, 100 and 500 ohm for 2 s each and read the key state at the keyer test point; apply 100 kohm, 1 Mohm and open.
3. Ring: repeat the previous step in Iambic A (dah elements appear while closed).
4. Abuse: with the unit on, apply +12 V to tip for 10 min, then -5 V for 10 min, recording the supply current; repeat on ring.
5. Repeat the tip and ring threshold steps.
6. Key the straight key and the paddle once each and confirm normal keying.
7. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
8. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if, before and after the abuse, each contact reads closed at 0, 100 and 500 ohm and open at 100 kohm, 1 Mohm and open (REQ-SYS-047), and after 10 min at +12 V and at -5 V on each contact the thresholds still pass and both keys key normally with no damage (REQ-SYS-049); otherwise Fail.

**Instruments and fixtures.**

- Pico-based logic capture (second Pico 2 with sigrok-pico firmware read by sigrok-cli; planned, ADR-009), 3.3 V inputs, 1 MS/s unless a step states otherwise
- Adjustable bench supply, 0 to 30 V, current limit set per step
- Multimeter, DC voltage and DC current ranges, accuracy per datasheet copied into the report (OQ-VV-003)
- 50 ohm BNC dummy load with SMA adapter, power rating recorded in the report
- Owner's straight key and iambic paddle, 3.5 mm TRS plugs (SI-034)
- TRS breakout with resistor substitution box (docs/vv/fixtures/key-resistors.md, planned)

**Expected artifacts.**

- `key-thresholds.csv` (csv): Contact, resistance, state before and after abuse
- `key-abuse.csv` (csv): Contact, voltage, duration, supply current

### TC-SYS-034: Key closure accepted after 2 ms of continuous contact and opening after 5 ms of continuous break

| Field | Value |
|---|---|
| Requirements | REQ-SYS-048, REQ-SYS-162 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | `tools/analyze_logic_capture.py` |

**Setup.** Article: CWHT-A-001, enclosure lid off for test-point access, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: logic capture at 1 MS/s of the owner's straight key contact and paddle contacts at the jack and of the keyer test point; Straight mode for the key, Iambic A for the paddle; PRACTICE set (no transmission). Credit row: T-HW. Test of a system requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the campaign (section 13) and witnessed by the owner; the pre-build Simulation, HostUnit and Emulation evidence named in each requirement's verification_note is supporting only and is not part of this case. TBR values: the acceptance criteria use the values of REQ-SYS-048, REQ-SYS-162 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Hazard controls exercised: HZ-004, HZ-010 (from the cited requirements; docs/safety/hazards.json). Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: no transmission is intended; the dummy load stays on the antenna port throughout so that an unintended key-down is absorbed; bench supply current limit set before power-on; antistatic wrist strap while the lid is off. Environment: room temperature 18 to 28 C; the pack is supplied by the bench supply at 7.4 V +/-0.05 V through the battery terminals unless a step sets another value; dummy load on the antenna port.

**Procedure.**

1. Run the logic-capture reference pulse-train check of this session and record the result (docs/process/04-verification-and-validation.md section 4).
2. Make 50 closures and 50 openings with the straight key at varied force and speed; capture.
3. Make 50 dit-lever and 50 dah-lever closures and openings with the paddle; capture.
4. Run tools/analyze_logic_capture.py --debounce: for each accepted edge find the start of the continuous contact or break that precedes it; count accepted versus physical operations.
5. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
6. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if the number of accepted closures and openings equals the number of physical operations, every accepted closure follows at least 2 ms of continuous contact and occurs within 2 ms +0.25 ms of its start (REQ-SYS-048), and every accepted opening follows at least 5 ms of continuous break and occurs within 5 ms +0.25 ms of its start (REQ-SYS-162), for both key types; otherwise Fail. The +0.25 ms acceptance window is the test author's, because the requirements state none.

**Instruments and fixtures.**

- Pico-based logic capture (second Pico 2 with sigrok-pico firmware read by sigrok-cli; planned, ADR-009), 3.3 V inputs, 1 MS/s unless a step states otherwise
- Owner's straight key and iambic paddle, 3.5 mm TRS plugs (SI-034)
- Adjustable bench supply, 0 to 30 V, current limit set per step

**Expected artifacts.**

- `debounce.csv` (csv): Operation, key type, bounce duration, continuous interval, acceptance delay

### TC-SYS-035: Electrostatic discharge tolerance at the key jack, headphone jack and antenna port from clamp ratings and return paths

| Field | Value |
|---|---|
| Requirements | REQ-SYS-050 |
| Method / class | Analysis / Simulation |
| Status | Draft |
| Automation | `tools/budgets/esd_clamp_check.py` |

**Setup.** Article: design data at tag baseline/cdr: the protection parts at each jack and at the antenna port with their datasheets, the series impedances and the layout ground-return path from each clamp to the chassis. Configuration: tools/budgets/esd_clamp_check.py (planned) tabulates per exposed conductor the clamp part, its IEC 61000-4-2 rating, the clamping voltage at the rated pulse against the protected pin's absolute maximum, and the return path; no ESD generator is on the bench (CON-016). Credit row: A. Analysis closed by Simulation on the CDR design data and confirmed at SAR by the physical configuration audit of every analyzed value (docs/process/04-verification-and-validation.md sections 5.1 item 5 and 5.2); the post-build readings named in the verification_note are supporting data only. Hazard controls exercised: HZ-010 (from the cited requirements; docs/safety/hazards.json). Risk acceptance: the verification_note of REQ-SYS-050 (RSK-012) begins 'Analysis accepted per RSK-NNN'; that risk carries the hazard control not closed by Test (docs/process/04-verification-and-validation.md section 3, rule 7.3.6). Tools: Python per tools/toolchain.lock.md Safety: not applicable (design data only). Environment: not applicable.

**Procedure.**

1. List every conductor exposed at the key jack (tip, ring, sleeve), the headphone jack (tip, ring, sleeve) and the antenna port (centre, shell).
2. For each, record the clamp part and its datasheet IEC 61000-4-2 contact and air rating.
3. Compute the residual voltage at the protected pin from the clamping voltage and the series impedance, and compare with the pin's absolute maximum.
4. Confirm on the layout that each clamp returns to chassis ground through a path with no series trace to the protected part's ground.
5. Record tool versions, the design-data tag and the commit of every deck, model, script and checker in the report.
6. On any assertion or checker failure, or any difference between the analyzed values and the design data, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if every exposed conductor at the key jack, headphone jack and antenna port has a clamp rated for IEC 61000-4-2 level 4 (8 kV contact, 15 kV air) or is chassis ground, every residual pin voltage is below the protected part's absolute maximum, and every clamp has a direct chassis return; otherwise Fail.

**Expected artifacts.**

- `esd-clamp-table.csv` (csv): Conductor, clamp, rating, residual voltage, pin maximum and return path

### TC-SYS-036: Key-input states unchanged while transmitting 5 W with 1.5 m unshielded leads on the key and headphone jacks

| Field | Value |
|---|---|
| Requirements | REQ-SYS-051 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | `tools/analyze_logic_capture.py` |

**Setup.** Article: CWHT-A-001 in its enclosure, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: 1.5 m unshielded leads on the key jack (open at the far end for the first run, then with the paddle attached) and on the headphone jack into the 32 ohm load; logic capture on both key inputs at the test pads through short shielded probe leads; the Bench-test PARIS generator at 5 W. The reference-antenna block runs only after the OnAir authorization in docs/reviews/TRR-Dn/decision-memo.md (04 section 6.3). Credit row: T-HW. Test of a system requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the campaign (section 13) and witnessed by the owner; the pre-build Simulation, HostUnit and Emulation evidence named in each requirement's verification_note is supporting only and is not part of this case. Hazard controls exercised: HZ-004, HZ-010 (from the cited requirements; docs/safety/hazards.json). Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: every transmission goes into the 50 ohm dummy load or the calibrated power attenuator, connected before power-on, never into an open antenna port; key-down duty kept within the load rating recorded in the report; anyone other than the operator stays 0.6 m or more from the unit and load while keying and 1.0 m or more during a tune carrier (NGO-019); the bench supply current limit is set before each power-on; antistatic wrist strap while the lid is off; the PA area is not touched after key-down runs. Antenna block: operator 0.6 m or more from the antenna of any bystander, identification per 47 CFR 97.119 at least every 10 min and at the end, a clear frequency in 144.000 to 144.100 MHz after listening for 60 s. Environment: room temperature 18 to 28 C; pack at 7.4 V +/-0.05 V from the bench supply; dummy load, then the reference antenna.

**Procedure.**

1. Run the logic-capture reference pulse-train check of this session and record the result (docs/process/04-verification-and-validation.md section 4).
2. Into the dummy load, run the PARIS generator at 5 W as five consecutive 60 s activations (the Bench-test limit per activation) with the key-jack lead open at its far end; capture both key inputs.
3. Repeat with the paddle at the far end of the lead, untouched.
4. Connect the reference antenna (Signal Stick half-wave with its counterpoise), confirm the OnAir authorization, and repeat both runs.
5. Straight-key check: with the straight key on the lead, key it by hand for 1 min into the dummy load and confirm the key inputs follow only the contact.
6. Run tools/analyze_logic_capture.py to count key-input edges during each run.
7. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
8. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if neither key input changes state during any generator run into the dummy load or the reference antenna, and during the hand-keyed minute the inputs change only with the contact; otherwise Fail.

**Instruments and fixtures.**

- Pico-based logic capture (second Pico 2 with sigrok-pico firmware read by sigrok-cli; planned, ADR-009), 3.3 V inputs, 1 MS/s unless a step states otherwise
- 50 ohm BNC dummy load with SMA adapter, power rating recorded in the report
- Audio load fixture: 16, 32 and 64 ohm resistors, 0.25 W, selectable on a 3.5 mm TRS breakout per channel (docs/vv/fixtures/audio-load.md, planned)
- Owner's straight key and iambic paddle, 3.5 mm TRS plugs (SI-034)
- Reference antenna: Signal Stick half-wave with 48 cm counterpoise tail
- 1.5 m unshielded two-conductor leads with 3.5 mm TRS plugs (docs/vv/fixtures/, planned)
- Adjustable bench supply, 0 to 30 V, current limit set per step

**Expected artifacts.**

- `rf-immunity.csv` (csv): Run, load, lead termination, key-input edge count

### TC-SYS-037: Key-input mode changes only by menu selection, selection accepted with a closed input, and the key-closed interlock

| Field | Value |
|---|---|
| Requirements | REQ-SYS-052, REQ-SYS-056, REQ-SYS-163 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | `tools/analyze_logic_capture.py` |

**Setup.** Article: CWHT-A-001, enclosure lid off for test-point access, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: logic capture on the key tip and ring contacts and PA_EN; dummy load; 0.5 W step; mode read from the display. Credit row: T-HW. Test of a system requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the campaign (section 13) and witnessed by the owner; the pre-build Simulation, HostUnit and Emulation evidence named in each requirement's verification_note is supporting only and is not part of this case. TBR values: the acceptance criteria use the values of REQ-SYS-052 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Hazard controls exercised: HZ-004, HZ-014 (from the cited requirements; docs/safety/hazards.json). Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: every transmission goes into the 50 ohm dummy load or the calibrated power attenuator, connected before power-on, never into an open antenna port; key-down duty kept within the load rating recorded in the report; anyone other than the operator stays 0.6 m or more from the unit and load while keying and 1.0 m or more during a tune carrier (NGO-019); the bench supply current limit is set before each power-on; antistatic wrist strap while the lid is off; the PA area is not touched after key-down runs. Environment: room temperature 18 to 28 C; the pack is supplied by the bench supply at 7.4 V +/-0.05 V through the battery terminals unless a step sets another value; dummy load on the antenna port.

**Procedure.**

1. Run the logic-capture reference pulse-train check of this session and record the result (docs/process/04-verification-and-validation.md section 4).
2. In each key-input mode, insert and remove a TS (mono) plug and a TRS plug three times; read the mode after each.
3. In paddle mode power on with a mono plug inserted (ring closed); record PA_EN; select Straight-on-tip from the menu with the ring still closed.
4. After the selection, key the straight key once 200 ms after the tip reads open, and again 700 ms after; record PA_EN.
5. In paddle mode power on with the dit lever held; release it; key after 200 ms and after 700 ms of open.
6. Pulse RUN (reset) with the dah lever held; release it; key after 200 ms and after 700 ms.
7. Change the key-input mode with the dit lever held; release it; key after 200 ms and after 700 ms.
8. Run tools/analyze_logic_capture.py to measure open time before each key-down and PA_EN response.
9. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
10. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if the key-input mode never changes on plug insertion or removal (REQ-SYS-056), the Straight-on-tip selection is accepted with the ring closed (REQ-SYS-163), and after each power-on, reset and mode change PA_EN stays low for key closures until each input the mode uses has read open for 500 ms and follows the key after that (REQ-SYS-052); otherwise Fail.

**Instruments and fixtures.**

- Pico-based logic capture (second Pico 2 with sigrok-pico firmware read by sigrok-cli; planned, ADR-009), 3.3 V inputs, 1 MS/s unless a step states otherwise
- 50 ohm BNC dummy load with SMA adapter, power rating recorded in the report
- Owner's straight key and iambic paddle, 3.5 mm TRS plugs (SI-034)
- 3.5 mm TS (mono) plug
- Adjustable bench supply, 0 to 30 V, current limit set per step

**Expected artifacts.**

- `keymode.csv` (csv): Condition, input, open time, PA_EN response, mode

### TC-SYS-038: Straight-key timeout and paddle watchdog, each holding the transmitter unkeyed until the contacts read open

| Field | Value |
|---|---|
| Requirements | REQ-SYS-053, REQ-SYS-054 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | `tools/analyze_logic_capture.py` |

**Setup.** Article: CWHT-A-001, enclosure lid off for test-point access, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: logic capture on the key tip and ring contacts at the jack, the keyer test point and PA_EN; dummy load; 1 W step; the 10 s of REQ-SYS-054 governs, not the 30 s of docs/conops/conops.md Table 3.4-4 row 3 (decision D-KN3); the checks after each release test the end of the stop that each requirement's 'until' clause bounds and the self-clearing Inhibit class (KEY) that both rationales assign (Table 3.4-4 rows 2 and 3, ConOps appendix D item D5). Credit row: T-HW. Test of a system requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the campaign (section 13) and witnessed by the owner; the pre-build Simulation, HostUnit and Emulation evidence named in each requirement's verification_note is supporting only and is not part of this case. TBR values: the acceptance criteria use the values of REQ-SYS-053, REQ-SYS-054 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Hazard controls exercised: HZ-001, HZ-003, HZ-004, HZ-006, HZ-012 (from the cited requirements; docs/safety/hazards.json). Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: every transmission goes into the 50 ohm dummy load or the calibrated power attenuator, connected before power-on, never into an open antenna port; key-down duty kept within the load rating recorded in the report; anyone other than the operator stays 0.6 m or more from the unit and load while keying and 1.0 m or more during a tune carrier (NGO-019); the bench supply current limit is set before each power-on; antistatic wrist strap while the lid is off; the PA area is not touched after key-down runs. Environment: room temperature 18 to 28 C; the pack is supplied by the bench supply at 7.4 V +/-0.05 V through the battery terminals unless a step sets another value; dummy load on the antenna port.

**Procedure.**

1. Run the logic-capture reference pulse-train check of this session and record the result (docs/process/04-verification-and-validation.md section 4).
2. Straight mode: hold the straight key closed for 10 s, release, and 1 s after the release close it for 0.5 s; repeat three times.
3. Bug mode: hold the dah contact closed for 10 s, release, and 1 s after the release close it for 0.5 s.
4. Iambic A at 5 WPM: hold the dit lever until keying stops and for a further 5 s; close the dah lever as well and hold both for 3 s; release the dit lever and hold the dah lever alone for 3 s; release it; 1 s after both contacts read open, send one dit.
5. Repeat the previous step starting with the dah lever, adding the dit lever and then releasing the dah lever first.
6. Repeat the two previous steps at 25 WPM and at 50 WPM.
7. Run tools/analyze_logic_capture.py: for the straight and Bug holds, time from accepted closure to PA_EN fall, PA_EN activity until the contact opens and the keying of the closure that follows; for the paddle holds, element count and duration of identical elements before keying stops, every PA_EN rise from the stop until both contacts read open, and the keying of the dit that follows.
8. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
9. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if for every manually timed hold the transmitter is unkeyed from 5.0 s +0.1 s after the accepted closure until the contact opens and the closure made 1 s after the release keys the transmitter (REQ-SYS-053), and for every paddle hold keying stops at the first of 128 consecutive identical elements or 10 s of identical elements, with no more than 128 elements and no keying beyond 10 s +0.1 s, PA_EN does not rise from the stop until both paddle contacts read open (through the squeeze and the single-lever hold), and the dit sent 1 s after both contacts read open keys the transmitter (REQ-SYS-054); otherwise Fail. The +0.1 s windows are the test author's, because the requirements state none.

**Instruments and fixtures.**

- Pico-based logic capture (second Pico 2 with sigrok-pico firmware read by sigrok-cli; planned, ADR-009), 3.3 V inputs, 1 MS/s unless a step states otherwise
- 50 ohm BNC dummy load with SMA adapter, power rating recorded in the report
- Owner's straight key and iambic paddle, 3.5 mm TRS plugs (SI-034)
- Adjustable bench supply, 0 to 30 V, current limit set per step

**Expected artifacts.**

- `stuckkey.csv` (csv): Hold, mode, speed, element count, time to unkey, PA_EN rises before both contacts read open, keying after the release
- `stuckkey-capture.sr` (other): Raw logic capture of the contacts, keyer test point and PA_EN

### TC-SYS-039: Hardware transmit cutoff independent of firmware, 7.5 s to 13 s into a continuous key-down

| Field | Value |
|---|---|
| Requirements | REQ-SYS-055 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | none (manual) |

**Setup.** Article: CWHT-A-001, enclosure lid off for test-point access, running the fault-injection test build of release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (a build flavour of the release commit whose injection commands arrive over the UART test pads from the host serial terminal through the 3.3 V serial adapter, or over USB serial only in steps that expect no carrier, because USB VBUS sets the USB flag and the hardware transmit inhibit of REQ-SYS-092, and which toggles the injection-marker test pad at the instant of each injection); the release image is restored and checked with picotool verify at the end of the case. Configuration: fault-injection build with the firmware key-down timeouts disabled and a command that holds TX_KEY high; antenna port to the calibrated power attenuator and the tinySA Ultra in zero span at the carrier (sweep time 20 s) for the RF duration; logic capture on TX_KEY and PA_EN; 1 W step at 146.00 MHz. Credit row: T-HW. Test of a system requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the campaign (section 13) and witnessed by the owner; the pre-build Simulation, HostUnit and Emulation evidence named in each requirement's verification_note is supporting only and is not part of this case. TBR values: the acceptance criteria use the values of REQ-SYS-055 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Hazard controls exercised: HZ-001, HZ-003, HZ-004, HZ-006, HZ-012, HZ-014 (from the cited requirements; docs/safety/hazards.json). Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: every transmission goes into the 50 ohm dummy load or the calibrated power attenuator, connected before power-on, never into an open antenna port; key-down duty kept within the load rating recorded in the report; anyone other than the operator stays 0.6 m or more from the unit and load while keying and 1.0 m or more during a tune carrier (NGO-019); the bench supply current limit is set before each power-on; antistatic wrist strap while the lid is off; the PA area is not touched after key-down runs. Environment: room temperature 18 to 28 C; the pack is supplied by the bench supply at 7.4 V +/-0.05 V through the battery terminals unless a step sets another value; dummy load on the antenna port.

**Procedure.**

1. Run the logic-capture reference pulse-train check of this session and record the result (docs/process/04-verification-and-validation.md section 4).
2. Measure the attenuator and cable S21 on the NanoVNA from 9 kHz (or the NanoVNA lower limit) to 1.5 GHz and save the Touchstone file; run the tinySA Ultra internal calibration-output check; record both.
3. At 7.4 V, command TX_KEY high for 20 s and record the RF duration on the tinySA zero-span trace and PA_EN on the capture.
4. Repeat at 6.4 V and at 8.4 V.
5. At 7.4 V, hold the straight key closed for 20 s in the build, then hold the paddle dah lever for 20 s, and record both.
6. Confirm that after each cutoff the unit shows the TX CUTOFF latched message (ConOps Table 3.4-4 row 12) and acknowledge it.
7. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
8. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if in every run antenna-port RF ends between 7.5 s and 13 s after the start of the continuous key-down while TX_KEY is still commanded high; otherwise Fail.

**Instruments and fixtures.**

- Pico-based logic capture (second Pico 2 with sigrok-pico firmware read by sigrok-cli; planned, ADR-009), 3.3 V inputs, 1 MS/s unless a step states otherwise
- Host computer with picotool and a serial terminal per tools/toolchain.lock.md, micro-USB cable
- 3.3 V USB-to-UART serial adapter between the host computer and the UART test pads, so that injection commands reach the unit with its USB port disconnected (docs/vv/fixtures/uart-adapter.md, planned)
- tinySA Ultra spectrum analyzer (ADR-021) through the calibrated 30 to 40 dB attenuator rated 10 W or more, attenuator S21 measured on the NanoVNA in the same session; level accuracy per its TV record
- NanoVNA, SOL calibration at the cable end used, checked on the dummy load
- Adjustable bench supply, 0 to 30 V, current limit set per step
- Owner's straight key and iambic paddle, 3.5 mm TRS plugs (SI-034)

**Expected artifacts.**

- `cutoff-durations.csv` (csv): Run, supply, keying source, RF duration and PA_EN duration
- `cutoff-zero-span.png` (plot): tinySA zero-span traces

### TC-SYS-040: Enclosure CAD and BOM: operator control set, external envelope and antenna-port face

| Field | Value |
|---|---|
| Requirements | REQ-SYS-057, REQ-SYS-103, REQ-SYS-175 |
| Method / class | Inspection / Inspection |
| Status | Draft |
| Automation | `hardware/enclosure/checks/enclosure_inspect.py` |

**Setup.** Article: design data at tag baseline/cdr: enclosure STEP exported from OpenSCAD through FreeCAD, its rendered views, the BOM and the front-panel drawing. Configuration: hardware/enclosure/checks/enclosure_inspect.py (planned) loads the STEP headlessly with the FreeCAD command-line interpreter, reports the axis-aligned bounding box of the enclosure body with knobs and antenna excluded, and lists every panel cutout with the face it lies on. Credit row: I. Inspection of design data, closed at CDR on the product baseline (docs/process/04-verification-and-validation.md sections 5.1 item 4 and 5.2); the receipt inspection named in the verification_note, where there is one, is recorded as data in the same report. TBR values: the acceptance criteria use the values of REQ-SYS-103 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Tools: FreeCAD 1.1.3 command-line interpreter, OpenSCAD 2021.01 and Python per tools/toolchain.lock.md Safety: not applicable (design data only). Environment: not applicable.

**Procedure.**

1. Render the enclosure STEP to front, rear, both side, top and end views and save the PNG files.
2. Run hardware/enclosure/checks/enclosure_inspect.py on the STEP and save the bounding box and cutout list.
3. Count on the renders and the BOM the rotary encoders with push action and the momentary push buttons that are operator controls, and identify the power switch.
4. Confirm that no other operator control (switch, knob, button, touch area) exists on the renders or in the BOM.
5. Read the bounding box of the enclosure with knobs and antenna excluded.
6. Identify the face that carries the antenna-port cutout and confirm that it is an end face and that no other face carries an antenna port.
7. Record the inspected file paths, their commit and tool versions in the report.
8. On any finding against the criteria, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if the renders and BOM show exactly two rotary knobs with push action and exactly two push buttons as operator controls besides the power switch, the bounding box excluding antenna and knobs is at most 140 mm x 70 mm x 40 mm, and the antenna port lies on one end face only; otherwise Fail.

**Expected artifacts.**

- `enclosure-views.png` (plot): Rendered views of the enclosure STEP (one file per view)
- `enclosure-inspect.txt` (report): Bounding box and cutout-to-face list from the checker

### TC-SYS-041: Tuning one step per detent from 10 Hz to 10 kHz with rotation rate, and band crossing time

| Field | Value |
|---|---|
| Requirements | REQ-SYS-058, REQ-SYS-164 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | `tools/analyze_logic_capture.py` |

**Setup.** Article: CWHT-A-001, enclosure lid off for test-point access, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: logic capture on the tuning encoder A and B lines and the UART telemetry pad (frequency field); guest lock set (no transmission needed). Credit row: T-HW. Test of a system requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the campaign (section 13) and witnessed by the owner; the pre-build Simulation, HostUnit and Emulation evidence named in each requirement's verification_note is supporting only and is not part of this case. TBR values: the acceptance criteria use the values of REQ-SYS-058, REQ-SYS-164 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: no transmission is intended; the dummy load stays on the antenna port throughout so that an unintended key-down is absorbed; bench supply current limit set before power-on; antistatic wrist strap while the lid is off. Environment: room temperature 18 to 28 C; the pack is supplied by the bench supply at 7.4 V +/-0.05 V through the battery terminals unless a step sets another value; dummy load on the antenna port.

**Procedure.**

1. Run the logic-capture reference pulse-train check of this session and record the result (docs/process/04-verification-and-validation.md section 4).
2. Wire the UART telemetry test pad to a logic-capture channel and confirm that the sigrok-cli UART decoder prints the telemetry lines (REQ-SYS-150).
3. Turn the tuning knob one detent at a time, at least 0.5 s apart, for 20 detents each way; capture.
4. Turn at a steady medium rate for 5 s, then as fast as possible for 5 s; capture.
5. Tune to 144.000 MHz; turn the knob steadily at about 2 revolutions per second until the display reaches 148.000 MHz; capture.
6. Run tools/analyze_logic_capture.py --encoder: detent count, detent rate, frequency step per detent and crossing time.
7. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
8. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if every detent produces exactly one frequency change, every step lies between 10 Hz and 10 kHz, slow single detents step 10 Hz, and the step never decreases as the detent rate increases (REQ-SYS-058), and at a measured mean rate of 2.0 +/-0.2 revolutions per second the tuning from 144.000 to 148.000 MHz takes at most 30 s (REQ-SYS-164); otherwise Fail.

**Instruments and fixtures.**

- Pico-based logic capture (second Pico 2 with sigrok-pico firmware read by sigrok-cli; planned, ADR-009), 3.3 V inputs, 1 MS/s unless a step states otherwise
- Adjustable bench supply, 0 to 30 V, current limit set per step

**Expected artifacts.**

- `tuning.csv` (csv): Detent time, rate, frequency before and after, step

### TC-SYS-042: Headphone level set in at least 32 steps from mute to the active cap

| Field | Value |
|---|---|
| Requirements | REQ-SYS-059 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | none (manual) |

**Setup.** Article: CWHT-A-001 in its enclosure, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: headphone output into the 32 ohm audio load; the steady 700 Hz Bench-test tone; multimeter true-RMS AC on the tip channel; default cap active. Credit row: T-HW. Test of a system requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the campaign (section 13) and witnessed by the owner; the pre-build Simulation, HostUnit and Emulation evidence named in each requirement's verification_note is supporting only and is not part of this case. TBR values: the acceptance criteria use the values of REQ-SYS-059 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: headphones are never worn during this case; a 32 ohm load resistor on a 3.5 mm TRS breakout replaces them; the full-scale test tone is selected only after the warning screen and the second confirmation of the Bench-test mode (docs/conops/conops.md Table 3.4-1). Environment: room temperature 18 to 28 C; the pack is supplied by the bench supply at 7.4 V +/-0.05 V through the battery terminals unless a step sets another value; dummy load on the antenna port.

**Procedure.**

1. Select the 700 Hz test tone (not the full-scale tone).
2. From mute, turn the volume knob one detent at a time to the maximum and read the RMS at each detent.
3. Count the distinct increasing levels from mute to the cap.
4. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
5. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if at least 32 detent positions give levels that increase strictly from mute to the active cap and the last level equals the active cap within the meter accuracy; otherwise Fail.

**Instruments and fixtures.**

- Multimeter, true-RMS AC voltage range, accuracy at 700 Hz per datasheet copied into the report (OQ-VV-003)
- Audio load fixture: 16, 32 and 64 ohm resistors, 0.25 W, selectable on a 3.5 mm TRS breakout per channel (docs/vv/fixtures/audio-load.md, planned)
- Adjustable bench supply, 0 to 30 V, current limit set per step

**Expected artifacts.**

- `volume-steps.csv` (csv): Detent and RMS level

### TC-SYS-043: Status display content in Receive, Transmit-keyed and Tune, and every setting within two menu levels

| Field | Value |
|---|---|
| Requirements | REQ-SYS-060, REQ-SYS-062 |
| Method / class | Demonstration / Bench |
| Status | Draft |
| Automation | none (manual) |

**Setup.** Article: CWHT-A-001 in its enclosure, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: dummy load; 0.5 W step; the list of operator settings from the software design; displays photographed. Credit row: D. Demonstration by the owner on the delivered unit (docs/process/04-verification-and-validation.md section 5.2): pass or fail is observed without detailed data gathering and each observation is photographed or logged. TBR values: the acceptance criteria use the values of REQ-SYS-062 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: every transmission goes into the 50 ohm dummy load or the calibrated power attenuator, connected before power-on, never into an open antenna port; key-down duty kept within the load rating recorded in the report; anyone other than the operator stays 0.6 m or more from the unit and load while keying and 1.0 m or more during a tune carrier (NGO-019); the bench supply current limit is set before each power-on; antistatic wrist strap while the lid is off; the PA area is not touched after key-down runs. Environment: room temperature 18 to 28 C; the pack is supplied by the bench supply at 7.4 V +/-0.05 V through the battery terminals unless a step sets another value; dummy load on the antenna port.

**Procedure.**

1. In Receive, photograph the status screen and identify frequency, power step, key mode, keyer speed, battery state and transmit state.
2. Key with the straight key for 2 s, then the paddle, and photograph the status screen during Transmit-keyed.
3. Activate Tune and photograph the status screen.
4. For each operator setting in the list, navigate from the status screen and count the menu levels to reach it.
5. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
6. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if all six items are shown in Receive, Transmit-keyed and Tune (REQ-SYS-060) and every operator setting is reached within two menu levels from the status screen (REQ-SYS-062); otherwise Fail.

**Instruments and fixtures.**

- 50 ohm BNC dummy load with SMA adapter, power rating recorded in the report
- Owner's straight key and iambic paddle, 3.5 mm TRS plugs (SI-034)
- Adjustable bench supply, 0 to 30 V, current limit set per step

**Expected artifacts.**

- `status-screens.jpg` (photo): Photographs of the status screen in each mode
- `menu-depth.csv` (csv): Setting and menu level

### TC-SYS-044: Displayed frequency character height from the rendered status frame and the display pixel pitch

| Field | Value |
|---|---|
| Requirements | REQ-SYS-061 |
| Method / class | Inspection / Inspection |
| Status | Draft |
| Automation | `tools/check_display_glyph.py` |

**Setup.** Article: design data at tag baseline/cdr: the status frame rendered to a PNG by the HostUnit renderer of the release at CDR and the selected display datasheet (D-UI-01). Configuration: The frequency glyph height in pixels is read from the PNG and multiplied by the datasheet pixel pitch. Credit row: I. Inspection of design data, closed at CDR on the product baseline (docs/process/04-verification-and-validation.md sections 5.1 item 4 and 5.2); the receipt inspection named in the verification_note, where there is one, is recorded as data in the same report. TBR values: the acceptance criteria use the values of REQ-SYS-061 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Tools: Python per tools/toolchain.lock.md Safety: not applicable (design data only). Environment: not applicable.

**Procedure.**

1. Render the Receive status frame showing the frequency string with the most characters the display format allows (for example 147.999 MHz with 10 Hz digits) to a PNG at native resolution.
2. Measure the cap height of the frequency digits in pixels on the PNG.
3. Read the pixel pitch from the selected display datasheet and compute the character height in mm.
4. At receipt, measure the displayed digit height with calipers if OQ-VV-002 confirms them, and record it as data.
5. Record the inspected file paths, their commit and tool versions in the report.
6. On any finding against the criteria, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if the frequency digit height, computed as pixels times the datasheet pixel pitch, is at least 4.0 mm; otherwise Fail.

**Expected artifacts.**

- `status-frame.png` (plot): Rendered Receive status frame at native resolution
- `char-height.txt` (report): Pixel count, pixel pitch and computed height

### TC-SYS-045: 5 W selected only after a step selection followed by a separate confirmation press

| Field | Value |
|---|---|
| Requirements | REQ-SYS-063 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | none (manual) |

**Setup.** Article: CWHT-A-001 in its enclosure, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: dummy load with the diode probe; step read from the display; 146.00 MHz. Credit row: T-HW. Test of a system requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the campaign (section 13) and witnessed by the owner; the pre-build Simulation, HostUnit and Emulation evidence named in each requirement's verification_note is supporting only and is not part of this case. Hazard controls exercised: HZ-001, HZ-006 (from the cited requirements; docs/safety/hazards.json). Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: every transmission goes into the 50 ohm dummy load or the calibrated power attenuator, connected before power-on, never into an open antenna port; key-down duty kept within the load rating recorded in the report; anyone other than the operator stays 0.6 m or more from the unit and load while keying and 1.0 m or more during a tune carrier (NGO-019); the bench supply current limit is set before each power-on; antistatic wrist strap while the lid is off; the PA area is not touched after key-down runs. Environment: room temperature 18 to 28 C; the pack is supplied by the bench supply at 7.4 V +/-0.05 V through the battery terminals unless a step sets another value; dummy load on the antenna port.

**Procedure.**

1. From the 2 W step, turn the step selection to 5 W and leave the menu without the confirmation press; read the display and key the straight key for 3 s reading the probe.
2. From the 2 W step, select 5 W and let the selection time out; read and key as before.
3. Press the confirmation button without a preceding 5 W selection; read and key as before.
4. Apply every other knob and button action of the menu (tuning, volume, push actions) with the step selector at 5 W and no confirmation; read and key as before.
5. Select 5 W and press the confirmation; read the display and key the straight key for 3 s, then the paddle dah lever for 3 s, reading the probe.
6. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
7. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if every sequence without the confirmation press leaves the displayed step below 5 W with probe power (with uncertainty) at most 2.518 W, and the sequence with the confirmation shows 5 W with probe power inside 3.972 to 6.295 W; otherwise Fail.

**Instruments and fixtures.**

- Diode RF probe (1N5711 or equivalent, printed housing) on a BNC T at the dummy load, characterized by TC-SYS-010, read on the multimeter DC voltage range
- Multimeter, DC voltage and DC current ranges, accuracy per datasheet copied into the report (OQ-VV-003)
- 50 ohm BNC dummy load with SMA adapter, power rating recorded in the report
- Owner's straight key and iambic paddle, 3.5 mm TRS plugs (SI-034)
- Adjustable bench supply, 0 to 30 V, current limit set per step

**Expected artifacts.**

- `fivewatt-sequences.csv` (csv): Sequence, displayed step, probe reading and power

### TC-SYS-046: Defaults at first power-on and after a configuration reset: 1 W, Iambic A, 15 WPM, 600 Hz, 8-dit hang, 5 ms envelope

| Field | Value |
|---|---|
| Requirements | REQ-SYS-064, REQ-SYS-136 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | `tools/analyze_logic_capture.py` |

**Setup.** Article: CWHT-A-001, enclosure lid off for test-point access, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: dummy load with the diode probe; logic capture on the keyer test point, the sidetone PWM line and the envelope drive; first power-on state produced by erasing the configuration sector with picotool; every setting changed from its default before each reset. Credit row: T-HW. Test of a system requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the campaign (section 13) and witnessed by the owner; the pre-build Simulation, HostUnit and Emulation evidence named in each requirement's verification_note is supporting only and is not part of this case. TBR values: the acceptance criteria use the values of REQ-SYS-064, REQ-SYS-136 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Hazard controls exercised: HZ-001, HZ-006, HZ-012, HZ-014 (from the cited requirements; docs/safety/hazards.json). Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: every transmission goes into the 50 ohm dummy load or the calibrated power attenuator, connected before power-on, never into an open antenna port; key-down duty kept within the load rating recorded in the report; anyone other than the operator stays 0.6 m or more from the unit and load while keying and 1.0 m or more during a tune carrier (NGO-019); the bench supply current limit is set before each power-on; antistatic wrist strap while the lid is off; the PA area is not touched after key-down runs. Environment: room temperature 18 to 28 C; the pack is supplied by the bench supply at 7.4 V +/-0.05 V through the battery terminals unless a step sets another value; dummy load on the antenna port.

**Procedure.**

1. Run the logic-capture reference pulse-train check of this session and record the result (docs/process/04-verification-and-validation.md section 4).
2. Set every operator setting to a non-default value (5 W, Iambic B, 30 WPM, 800 Hz, 20 dits, 8 ms).
3. Perform a configuration reset from the menu.
4. Read every setting from the menus and the status screen and photograph them.
5. Close the straight key for 3 s and read the probe; hold the paddle dit lever for 2 s and capture the keyer test point, sidetone PWM and envelope drive.
6. Erase the configuration sector with picotool (first-boot state), power on and repeat the two previous steps.
7. Run tools/analyze_logic_capture.py to compute the dit length (speed), the sidetone frequency and the hang from last key-up to T/R release; the envelope setting is read from the menu only.
8. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
9. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if after the configuration reset and after the first power-on the step is 1 W with probe power inside 0.794 to 1.259 W (REQ-SYS-064), and the menus show Iambic A, 15 WPM, 600 Hz sidetone, 8-dit hang and 5 ms envelope, corroborated by a captured dit of 80 ms +/-1 percent, a sidetone of 600 Hz +/-5 Hz and a hang of 640 ms +/-1 percent (REQ-SYS-136); otherwise Fail.

**Instruments and fixtures.**

- Diode RF probe (1N5711 or equivalent, printed housing) on a BNC T at the dummy load, characterized by TC-SYS-010, read on the multimeter DC voltage range
- Multimeter, DC voltage and DC current ranges, accuracy per datasheet copied into the report (OQ-VV-003)
- Pico-based logic capture (second Pico 2 with sigrok-pico firmware read by sigrok-cli; planned, ADR-009), 3.3 V inputs, 1 MS/s unless a step states otherwise
- Host computer with picotool and a serial terminal per tools/toolchain.lock.md, micro-USB cable
- 50 ohm BNC dummy load with SMA adapter, power rating recorded in the report
- Owner's straight key and iambic paddle, 3.5 mm TRS plugs (SI-034)
- Adjustable bench supply, 0 to 30 V, current limit set per step

**Expected artifacts.**

- `defaults-menus.jpg` (photo): Photographs of the menus after each reset
- `defaults-readings.csv` (csv): Setting, displayed value, measured value

### TC-SYS-047: Guest lock: no RF from any source while set, including after power cycles, and two-step set and release

| Field | Value |
|---|---|
| Requirements | REQ-SYS-065, REQ-SYS-066, REQ-SYS-183 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | none (manual) |

**Setup.** Article: CWHT-A-001, enclosure lid off for test-point access, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: antenna port to the calibrated power attenuator and the tinySA Ultra; logic capture on PA_EN; lock state read from the display. Credit row: T-HW. Test of a system requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the campaign (section 13) and witnessed by the owner; the pre-build Simulation, HostUnit and Emulation evidence named in each requirement's verification_note is supporting only and is not part of this case. RF-off level: the acceptance criteria use -57 dBm, the value of REQ-SYS-183 marked TBR (close by PDR); a change returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2). Hazard controls exercised: HZ-006 (from the cited requirements; docs/safety/hazards.json). Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: every transmission goes into the 50 ohm dummy load or the calibrated power attenuator, connected before power-on, never into an open antenna port; key-down duty kept within the load rating recorded in the report; anyone other than the operator stays 0.6 m or more from the unit and load while keying and 1.0 m or more during a tune carrier (NGO-019); the bench supply current limit is set before each power-on; antistatic wrist strap while the lid is off; the PA area is not touched after key-down runs. Environment: room temperature 18 to 28 C; the pack is supplied by the bench supply at 7.4 V +/-0.05 V through the battery terminals unless a step sets another value; dummy load on the antenna port.

**Procedure.**

1. Run the logic-capture reference pulse-train check of this session and record the result (docs/process/04-verification-and-validation.md section 4).
2. Measure the attenuator and cable S21 on the NanoVNA from 9 kHz (or the NanoVNA lower limit) to 1.5 GHz and save the Touchstone file; run the tinySA Ultra internal calibration-output check; record both.
3. On an unlocked unit apply every single-button action, every button pair without the hold, every knob action and the held combination without the confirmation; read the lock state after each.
4. Set the lock with the held combination followed by the confirmation.
5. On the locked unit apply the same sequences as for the unlocked unit; read the lock state after each.
6. On the locked unit close the straight key for 3 s, hold the paddle dit lever for 3 s, attempt Tune and attempt the test menu.
7. Power-cycle and repeat the keying attempts; perform a configuration reset and repeat them.
8. Release the lock with the two-step action and confirm that the straight key keys the carrier.
9. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
10. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if every sequence other than the held combination followed by the confirmation leaves the lock state unchanged on both a locked and an unlocked unit (REQ-SYS-066), and while locked, before and after the power cycle and the configuration reset, PA_EN stays low and no carrier at the set frequency above -57 dBm at the antenna port on the tinySA Ultra (the RF-off level of REQ-SYS-183) for every keying, tune and test-mode attempt (REQ-SYS-065); otherwise Fail.

**Instruments and fixtures.**

- Pico-based logic capture (second Pico 2 with sigrok-pico firmware read by sigrok-cli; planned, ADR-009), 3.3 V inputs, 1 MS/s unless a step states otherwise
- tinySA Ultra spectrum analyzer (ADR-021) through the calibrated 30 to 40 dB attenuator rated 10 W or more, attenuator S21 measured on the NanoVNA in the same session; level accuracy per its TV record
- NanoVNA, SOL calibration at the cable end used, checked on the dummy load
- Owner's straight key and iambic paddle, 3.5 mm TRS plugs (SI-034)
- Adjustable bench supply, 0 to 30 V, current limit set per step

**Expected artifacts.**

- `guestlock-sequences.csv` (csv): Sequence, starting state, resulting state
- `guestlock-rf.csv` (csv): Attempt, PA_EN and RF level while locked

### TC-SYS-048: Identification reminder 9 min 00 s +/-5 s after the first transmission following the previous reminder

| Field | Value |
|---|---|
| Requirements | REQ-SYS-068 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | `tools/analyze_logic_capture.py` |

**Setup.** Article: CWHT-A-001, enclosure lid off for test-point access, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: logic capture at 100 kS/s on TX_KEY and the UART telemetry pad (reminder event); dummy load; 0.5 W step. Credit row: T-HW. Test of a system requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the campaign (section 13) and witnessed by the owner; the pre-build Simulation, HostUnit and Emulation evidence named in each requirement's verification_note is supporting only and is not part of this case. TBR values: the acceptance criteria use the values of REQ-SYS-068 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: every transmission goes into the 50 ohm dummy load or the calibrated power attenuator, connected before power-on, never into an open antenna port; key-down duty kept within the load rating recorded in the report; anyone other than the operator stays 0.6 m or more from the unit and load while keying and 1.0 m or more during a tune carrier (NGO-019); the bench supply current limit is set before each power-on; antistatic wrist strap while the lid is off; the PA area is not touched after key-down runs. Environment: room temperature 18 to 28 C; the pack is supplied by the bench supply at 7.4 V +/-0.05 V through the battery terminals unless a step sets another value; dummy load on the antenna port.

**Procedure.**

1. Run the logic-capture reference pulse-train check of this session and record the result (docs/process/04-verification-and-validation.md section 4).
2. Wire the UART telemetry test pad to a logic-capture channel and confirm that the sigrok-cli UART decoder prints the telemetry lines (REQ-SYS-150).
3. After power-on, send one character with the straight key; keep sending a character every 60 s; capture until the reminder event and 1 min beyond.
4. Acknowledge the reminder, wait 2 min without keying, then send with the paddle and repeat the run.
5. Run tools/analyze_logic_capture.py: first key-down after the previous reminder (or power-on) to the reminder event.
6. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
7. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if in both runs the reminder is shown 540 s +/-5 s after the first transmission following the previous reminder; otherwise Fail.

**Instruments and fixtures.**

- Pico-based logic capture (second Pico 2 with sigrok-pico firmware read by sigrok-cli; planned, ADR-009), 3.3 V inputs, 1 MS/s unless a step states otherwise
- 50 ohm BNC dummy load with SMA adapter, power rating recorded in the report
- Owner's straight key and iambic paddle, 3.5 mm TRS plugs (SI-034)
- Adjustable bench supply, 0 to 30 V, current limit set per step

**Expected artifacts.**

- `id-reminder.csv` (csv): Run, first key-down time, reminder time, interval

### TC-SYS-049: Separation reminder per step and mode, and cumulative key-down time over 6 min and 30 min windows

| Field | Value |
|---|---|
| Requirements | REQ-SYS-069, REQ-SYS-171 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | `tools/analyze_logic_capture.py` |

**Setup.** Article: CWHT-A-001, enclosure lid off for test-point access, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: logic capture at 100 kS/s on TX_KEY; dummy load; the displayed values compared with docs/design/analysis/rf-exposure-evaluation.md at its current revision. Credit row: T-HW. Test of a system requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the campaign (section 13) and witnessed by the owner; the pre-build Simulation, HostUnit and Emulation evidence named in each requirement's verification_note is supporting only and is not part of this case. TBR values: the acceptance criteria use the values of REQ-SYS-069 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Hazard controls exercised: HZ-006 (from the cited requirements; docs/safety/hazards.json). Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: every transmission goes into the 50 ohm dummy load or the calibrated power attenuator, connected before power-on, never into an open antenna port; key-down duty kept within the load rating recorded in the report; anyone other than the operator stays 0.6 m or more from the unit and load while keying and 1.0 m or more during a tune carrier (NGO-019); the bench supply current limit is set before each power-on; antistatic wrist strap while the lid is off; the PA area is not touched after key-down runs. Environment: room temperature 18 to 28 C; the pack is supplied by the bench supply at 7.4 V +/-0.05 V through the battery terminals unless a step sets another value; dummy load on the antenna port.

**Procedure.**

1. Run the logic-capture reference pulse-train check of this session and record the result (docs/process/04-verification-and-validation.md section 4).
2. Select each power step in Receive and read the separation reminder; select Tune and read it.
3. Compare each value with the evaluation's bystander separation at that step's maximum permitted power and mode.
4. Reset the key-down totals if the design provides it (otherwise power-cycle); run the Bench-test PARIS generator at 1 W as seven consecutive 60 s activations (the Bench-test limit per activation), capturing TX_KEY; read and photograph the 6 min and 30 min totals at the end.
5. Send by hand for 1 min with the straight key and for 1 min with the paddle; read and photograph the totals again.
6. Run tools/analyze_logic_capture.py to sum key-down time over the last 360 s and over the whole run.
7. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
8. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if the displayed separation for every step and for Tune equals the evaluation's value (REQ-SYS-069), and the displayed 6 min and 30 min totals equal the captured key-down sums over the last 360 s and over the run within +/-1 s at 1 s resolution at both readings (REQ-SYS-171); otherwise Fail.

**Instruments and fixtures.**

- Pico-based logic capture (second Pico 2 with sigrok-pico firmware read by sigrok-cli; planned, ADR-009), 3.3 V inputs, 1 MS/s unless a step states otherwise
- 50 ohm BNC dummy load with SMA adapter, power rating recorded in the report
- Owner's straight key and iambic paddle, 3.5 mm TRS plugs (SI-034)
- Adjustable bench supply, 0 to 30 V, current limit set per step

**Expected artifacts.**

- `separation-display.csv` (csv): Step or mode, displayed value, evaluation value
- `keydown-totals.csv` (csv): Reading, displayed totals, captured sums
- `exposure-display.jpg` (photo): Photographs of the displays

### TC-SYS-050: USB input current, charge-state indication in every phase, and charging paused while the radio is on

| Field | Value |
|---|---|
| Requirements | REQ-SYS-070, REQ-SYS-090, REQ-SYS-093 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | none (manual) |

**Setup.** Article: CWHT-A-001 in its enclosure, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: cells replaced by the two-cell simulator fixture unless a step names the owner's cells; USB through the USB breakout fixture; charge current read on the multimeter in series with the pack lead; charge state and events read from the display and the UART telemetry. The simulator starts at 3.0 V per cell (discharged). Credit row: T-HW. Test of a system requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the campaign (section 13) and witnessed by the owner; the pre-build Simulation, HostUnit and Emulation evidence named in each requirement's verification_note is supporting only and is not part of this case. Hazard controls exercised: HZ-002, HZ-011 (from the cited requirements; docs/safety/hazards.json). Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: cells and cell simulators are handled per the operations handbook battery section: current limit set before connection, cell terminals never shorted, cells on a non-flammable surface and attended during every charge or discharge run; a cell warm to the touch above about 45 C ends the run. Environment: room temperature 18 to 28 C; the cells or cell simulators named in Configuration; dummy load on the antenna port.

**Procedure.**

1. Wire the UART telemetry test pad to a logic-capture channel and confirm that the sigrok-cli UART decoder prints the telemetry lines (REQ-SYS-150).
2. With the switch off, apply USB; read the VBUS current and the charge current at the start of charge; read the charge indication.
3. Turn the switch on; read VBUS current, charge current and the indication.
4. Turn the switch off; raise the simulator in steps through pre-charge, constant current and constant voltage (as the charger enters each), reading the indication and VBUS current in each phase; hold at termination and read.
5. Repeat the indication check with the switch on at each phase.
6. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
7. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if VBUS current, with the meter accuracy added, is at most 500 mA in every state (REQ-SYS-090); the charge state is indicated in every charge phase with the switch off and with it on (REQ-SYS-070); and with the switch on and USB present the charge current into the pack is at most 5 mA (REQ-SYS-093); otherwise Fail. The 5 mA paused-charge threshold is the test author's, because REQ-SYS-093 states none.

**Instruments and fixtures.**

- USB power breakout fixture with VBUS routed through the multimeter current range (docs/vv/fixtures/usb-breakout.md, planned)
- Two-cell simulator fixture: the bench supply across the pack terminals with an adjustable, buffered mid-point tap for the cell junction and a parallel sink resistor so that the fixture absorbs charger current (docs/vv/fixtures/cell-simulator.md, planned; characterized before TRR)
- Multimeter, DC voltage and DC current ranges, accuracy per datasheet copied into the report (OQ-VV-003)
- Pico-based logic capture (second Pico 2 with sigrok-pico firmware read by sigrok-cli; planned, ADR-009), 3.3 V inputs, 1 MS/s unless a step states otherwise

**Expected artifacts.**

- `charge-usb.csv` (csv): State, phase, VBUS current, charge current, indication
- `charge-indication.jpg` (photo): Photographs of the indication in each phase

### TC-SYS-051: Headphone output ceiling for a full-scale sine and for any digital audio pattern

| Field | Value |
|---|---|
| Requirements | REQ-SYS-071, REQ-SYS-072 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | none (manual) |

**Setup.** Article: CWHT-A-001 in its enclosure, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: headphone output into the audio load fixture (32 ohm per channel unless a step says otherwise); multimeter true-RMS AC across the load; Bench-test tones: the steady 700 Hz tone and, after the warning screen and second confirmation, the full-scale 700 Hz sine and the full-scale test patterns; PRACTICE set so that no transmission occurs. The cap is unlocked with its acknowledgment and volume set to maximum. Credit row: T-HW. Test of a system requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the campaign (section 13) and witnessed by the owner; the pre-build Simulation, HostUnit and Emulation evidence named in each requirement's verification_note is supporting only and is not part of this case. TBR values: the acceptance criteria use the values of REQ-SYS-071, REQ-SYS-072 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Hazard controls exercised: HZ-005 (from the cited requirements; docs/safety/hazards.json). Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: headphones are never worn during this case; a 32 ohm load resistor on a 3.5 mm TRS breakout replaces them; the full-scale test tone is selected only after the warning screen and the second confirmation of the Bench-test mode (docs/conops/conops.md Table 3.4-1). Environment: room temperature 18 to 28 C; the pack is supplied by the bench supply at 7.4 V +/-0.05 V through the battery terminals unless a step sets another value; dummy load on the antenna port.

**Procedure.**

1. Unlock the audio cap with its acknowledgment and set the volume to maximum.
2. Select the full-scale 700 Hz sine; read the RMS on tip and on ring.
3. Select each full-scale test pattern (full-scale square, alternating-code and every other pattern the Bench-test mode offers); read the RMS on tip and on ring for each.
4. Record the meter's true-RMS crest-factor limit and bandwidth from its datasheet.
5. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
6. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if the full-scale 700 Hz sine gives 90 to 110 mVrms (100 mVrms +/-10 percent) into 32 ohm on each channel, reading and meter accuracy combined (REQ-SYS-071), and every test pattern gives at most 150 mVrms into 32 ohm on each channel with the meter accuracy added (REQ-SYS-072); otherwise Fail.

**Instruments and fixtures.**

- Multimeter, true-RMS AC voltage range, accuracy at 700 Hz per datasheet copied into the report (OQ-VV-003)
- Audio load fixture: 16, 32 and 64 ohm resistors, 0.25 W, selectable on a 3.5 mm TRS breakout per channel (docs/vv/fixtures/audio-load.md, planned)
- Adjustable bench supply, 0 to 30 V, current limit set per step

**Expected artifacts.**

- `audio-ceiling.csv` (csv): Pattern, channel, RMS reading

### TC-SYS-052: Headphone output ceiling under every single component failure in the output path

| Field | Value |
|---|---|
| Requirements | REQ-SYS-073 |
| Method / class | Analysis / Simulation |
| Status | Draft |
| Automation | `hardware/sim/checks/audio_single_fault_check.py` |

**Setup.** Article: design data at tag baseline/cdr: hardware/sim/audio/output_path.asc with the CDR amplifier gain setting, passive network and the full-scale digital audio source. Configuration: hardware/sim/checks/audio_single_fault_check.py (planned) opens and shorts each part of the output path in turn and simulates full-scale square and sine patterns into 32 ohm on each channel. Credit row: A. Analysis closed by Simulation on the CDR design data and confirmed at SAR by the physical configuration audit of every analyzed value (docs/process/04-verification-and-validation.md sections 5.1 item 5 and 5.2); the post-build readings named in the verification_note are supporting data only. TBR values: the acceptance criteria use the values of REQ-SYS-073 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Hazard controls exercised: HZ-005 (from the cited requirements; docs/safety/hazards.json). Risk acceptance: the verification_note of REQ-SYS-073 (RSK-017) begins 'Analysis accepted per RSK-NNN'; that risk carries the hazard control not closed by Test (docs/process/04-verification-and-validation.md section 3, rule 7.3.6). Tools: LTspice through the batch wrapper tools/run_sim.py and Python per tools/toolchain.lock.md Safety: not applicable (design data only). Environment: not applicable.

**Procedure.**

1. Confirm that the deck part values equal the CDR schematic (checker prints the diff; an empty diff is required).
2. Run the nominal case with full-scale sine and square patterns into 32 ohm and record the RMS output of each channel.
3. Run every single-failure case (each part open, then shorted) and record the RMS output of each channel.
4. Repeat the computation with every toleranced input at its worst-case corner (checker option --corners) and record the worst case.
5. Record tool versions, the design-data tag and the commit of every deck, model, script and checker in the report.
6. On any assertion or checker failure, or any difference between the analyzed values and the design data, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if the RMS output into 32 ohm is at most 150 mVrms on each channel for the nominal case and for every single open or short failure of each part in the output path; otherwise Fail.

**Expected artifacts.**

- `audio-single-fault.csv` (csv): Failure case, pattern, channel and RMS output
- `audio-single-fault-check.log.txt` (log): Checker output

### TC-SYS-053: Default 30 mVrms audio cap until acknowledgment, restored at every power-on unless a persistent unlock is selected

| Field | Value |
|---|---|
| Requirements | REQ-SYS-074, REQ-SYS-170 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | none (manual) |

**Setup.** Article: CWHT-A-001 in its enclosure, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: headphone output into the audio load fixture (32 ohm per channel unless a step says otherwise); multimeter true-RMS AC across the load; Bench-test tones: the steady 700 Hz tone and, after the warning screen and second confirmation, the full-scale 700 Hz sine and the full-scale test patterns; PRACTICE set so that no transmission occurs. Volume at maximum throughout. Credit row: T-HW. Test of a system requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the campaign (section 13) and witnessed by the owner; the pre-build Simulation, HostUnit and Emulation evidence named in each requirement's verification_note is supporting only and is not part of this case. TBR values: the acceptance criteria use the values of REQ-SYS-074 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Hazard controls exercised: HZ-005 (from the cited requirements; docs/safety/hazards.json). Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: headphones are never worn during this case; a 32 ohm load resistor on a 3.5 mm TRS breakout replaces them; the full-scale test tone is selected only after the warning screen and the second confirmation of the Bench-test mode (docs/conops/conops.md Table 3.4-1). Environment: room temperature 18 to 28 C; the pack is supplied by the bench supply at 7.4 V +/-0.05 V through the battery terminals unless a step sets another value; dummy load on the antenna port.

**Procedure.**

1. With the cap in its default state, select the full-scale 700 Hz tone at maximum volume; read the RMS on each channel.
2. Unlock the cap with its acknowledgment; read again.
3. Power-cycle without selecting a persistent unlock; read again at maximum volume.
4. Unlock the cap selecting the persistent unlock; power-cycle; read again.
5. Restore the non-persistent state; power-cycle; read again.
6. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
7. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if before acknowledgment, and after each power-on without a persistent unlock, the output is at most 30 mVrms into 32 ohm on each channel with the meter accuracy added (REQ-SYS-074, REQ-SYS-170), and after acknowledgment and after a power-on with the persistent unlock the output exceeds 30 mVrms; otherwise Fail.

**Instruments and fixtures.**

- Multimeter, true-RMS AC voltage range, accuracy at 700 Hz per datasheet copied into the report (OQ-VV-003)
- Audio load fixture: 16, 32 and 64 ohm resistors, 0.25 W, selectable on a 3.5 mm TRS breakout per channel (docs/vv/fixtures/audio-load.md, planned)
- Adjustable bench supply, 0 to 30 V, current limit set per step

**Expected artifacts.**

- `audio-cap.csv` (csv): State, power cycle, channel, RMS

### TC-SYS-054: Receive audio mute at key-down, hold through transmit and hang, and restore fade

| Field | Value |
|---|---|
| Requirements | REQ-SYS-075, REQ-SYS-157, REQ-SYS-158 |
| Method / class | Analysis / Simulation |
| Status | Draft |
| Automation | `hardware/sim/checks/audio_mute_fade_check.py` |

**Setup.** Article: design data at tag baseline/cdr: the audio-chain state machine and fade tables of the release at CDR (the REQ-SW child results of its HostUnit case) combined with hardware/sim/audio/output_path.asc for the analog path. Configuration: hardware/sim/checks/audio_mute_fade_check.py (planned) drives the analog model with the digital fade sequence for a key-down, a 20 s over at 5, 15 and 50 WPM and a hang expiry, with a steady received tone at the unmuted level. Credit row: A. Analysis closed by Simulation on the CDR design data and confirmed at SAR by the physical configuration audit of every analyzed value (docs/process/04-verification-and-validation.md sections 5.1 item 5 and 5.2); the post-build readings named in the verification_note are supporting data only. TBR values: the acceptance criteria use the values of REQ-SYS-158 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Hazard controls exercised: HZ-005 (from the cited requirements; docs/safety/hazards.json). Risk acceptance: the verification_note of REQ-SYS-075 (RSK-017), REQ-SYS-157 (RSK-017), REQ-SYS-158 (RSK-017) begins 'Analysis accepted per RSK-NNN'; that risk carries the hazard control not closed by Test (docs/process/04-verification-and-validation.md section 3, rule 7.3.6). Tools: LTspice through the batch wrapper tools/run_sim.py and Python per tools/toolchain.lock.md Safety: not applicable (design data only). Environment: not applicable.

**Procedure.**

1. Confirm that the fade tables and deck equal the release at CDR and the CDR schematic (checker prints the diff; an empty diff is required).
2. Simulate key-down and measure the time from key-down to 60 dB attenuation of the received tone and the fade shape.
3. Simulate overs at 5, 15 and 50 WPM and record the minimum attenuation of the received tone from the first key-down to hang expiry.
4. Simulate hang expiry and measure the restore fade duration (from start to full level) and its shape.
5. Repeat the computation with every toleranced input at its worst-case corner (checker option --corners) and record the worst case.
6. Record tool versions, the design-data tag and the commit of every deck, model, script and checker in the report.
7. On any assertion or checker failure, or any difference between the analyzed values and the design data, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if receive audio is attenuated by at least 60 dB within 2 ms of key-down through a raised-cosine fade (REQ-SYS-075), stays at least 60 dB below its unmuted level from the first key-down to hang expiry at every speed (REQ-SYS-157), and is restored at hang expiry by a raised-cosine fade lasting 5 ms to 20 ms (REQ-SYS-158), with the fade shapes within 5 percent of full scale of the ideal raised cosine; otherwise Fail, reported per requirement.

**Expected artifacts.**

- `audio-mute-fade.csv` (csv): Time versus received-tone level for each scenario
- `audio-mute-fade.png` (plot): Fade envelopes with the limits drawn

### TC-SYS-055: Headphone transients at key-down, key-up, hang expiry, plug insertion and power-on

| Field | Value |
|---|---|
| Requirements | REQ-SYS-076 |
| Method / class | Analysis / Simulation |
| Status | Draft |
| Automation | `hardware/sim/checks/audio_transient_check.py` |

**Setup.** Article: design data at tag baseline/cdr: hardware/sim/audio/output_path.asc with the amplifier enable, ramp and coupling-capacitor network and the jack-detect path. Configuration: hardware/sim/checks/audio_transient_check.py (planned) simulates each event with no audio signal and reports the peak voltage across 32 ohm on each channel. Credit row: A. Analysis closed by Simulation on the CDR design data and confirmed at SAR by the physical configuration audit of every analyzed value (docs/process/04-verification-and-validation.md sections 5.1 item 5 and 5.2); the post-build readings named in the verification_note are supporting data only. TBR values: the acceptance criteria use the values of REQ-SYS-076 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Hazard controls exercised: HZ-005 (from the cited requirements; docs/safety/hazards.json). Risk acceptance: the verification_note of REQ-SYS-076 (RSK-017) begins 'Analysis accepted per RSK-NNN'; that risk carries the hazard control not closed by Test (docs/process/04-verification-and-validation.md section 3, rule 7.3.6). Tools: LTspice through the batch wrapper tools/run_sim.py and Python per tools/toolchain.lock.md Safety: not applicable (design data only). Environment: not applicable.

**Procedure.**

1. Confirm that the deck part values equal the CDR schematic (checker prints the diff; an empty diff is required).
2. Simulate each event (key-down, key-up, hang expiry, plug insertion with the amplifier enabling, power-on of the audio rail) and record the peak voltage across 32 ohm on each channel.
3. Repeat the computation with every toleranced input at its worst-case corner (checker option --corners) and record the worst case.
4. Record tool versions, the design-data tag and the commit of every deck, model, script and checker in the report.
5. On any assertion or checker failure, or any difference between the analyzed values and the design data, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if the peak transient across 32 ohm is below 10 mV on each channel for every event, nominal and at the corners; otherwise Fail.

**Expected artifacts.**

- `audio-transients.csv` (csv): Event, channel and peak transient voltage

### TC-SYS-056: Headphone amplifier output disabled while no plug is in the headphone jack

| Field | Value |
|---|---|
| Requirements | REQ-SYS-077 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | `tools/analyze_logic_capture.py` |

**Setup.** Article: CWHT-A-001, enclosure lid off for test-point access, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: logic capture on the amplifier enable line and the jack-detect contact; PRACTICE set. Credit row: T-HW. Test of a system requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the campaign (section 13) and witnessed by the owner; the pre-build Simulation, HostUnit and Emulation evidence named in each requirement's verification_note is supporting only and is not part of this case. Hazard controls exercised: HZ-005 (from the cited requirements; docs/safety/hazards.json). Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: no transmission is intended; the dummy load stays on the antenna port throughout so that an unintended key-down is absorbed; bench supply current limit set before power-on; antistatic wrist strap while the lid is off. Environment: room temperature 18 to 28 C; the pack is supplied by the bench supply at 7.4 V +/-0.05 V through the battery terminals unless a step sets another value; dummy load on the antenna port.

**Procedure.**

1. Run the logic-capture reference pulse-train check of this session and record the result (docs/process/04-verification-and-validation.md section 4).
2. With no plug inserted, capture the amplifier enable for 60 s in Receive and during PRACTICE keying with the straight key and the paddle.
3. Insert and remove a TRS plug ten times at about 2 s intervals; capture.
4. Power on with no plug inserted; capture from power-on.
5. Run tools/analyze_logic_capture.py: amplifier enable state while the detect contact reads no plug.
6. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
7. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if the amplifier enable is low whenever the jack reads no plug, allowing at most 20 ms after each removal edge, and is never high at power-on without a plug; otherwise Fail. The 20 ms allowance is the test author's, because REQ-SYS-077 states none.

**Instruments and fixtures.**

- Pico-based logic capture (second Pico 2 with sigrok-pico firmware read by sigrok-cli; planned, ADR-009), 3.3 V inputs, 1 MS/s unless a step states otherwise
- Owner's straight key and iambic paddle, 3.5 mm TRS plugs (SI-034)
- 3.5 mm TRS plug
- Adjustable bench supply, 0 to 30 V, current limit set per step

**Expected artifacts.**

- `amp-off.csv` (csv): Event, detect state, enable state, delay

### TC-SYS-057: Channel balance into 16 to 64 ohm at the active cap, and survival of a headphone contact short to sleeve

| Field | Value |
|---|---|
| Requirements | REQ-SYS-078, REQ-SYS-079 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | none (manual) |

**Setup.** Article: CWHT-A-001 in its enclosure, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: headphone output into the audio load fixture (32 ohm per channel unless a step says otherwise); multimeter true-RMS AC across the load; Bench-test tones: the steady 700 Hz tone and, after the warning screen and second confirmation, the full-scale 700 Hz sine and the full-scale test patterns; PRACTICE set so that no transmission occurs. Default cap active for the balance runs. Credit row: T-HW. Test of a system requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the campaign (section 13) and witnessed by the owner; the pre-build Simulation, HostUnit and Emulation evidence named in each requirement's verification_note is supporting only and is not part of this case. TBR values: the acceptance criteria use the values of REQ-SYS-078 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Hazard controls exercised: HZ-010 (from the cited requirements; docs/safety/hazards.json). Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: headphones are never worn during this case; a 32 ohm load resistor on a 3.5 mm TRS breakout replaces them; the full-scale test tone is selected only after the warning screen and the second confirmation of the Bench-test mode (docs/conops/conops.md Table 3.4-1). Environment: room temperature 18 to 28 C; the pack is supplied by the bench supply at 7.4 V +/-0.05 V through the battery terminals unless a step sets another value; dummy load on the antenna port.

**Procedure.**

1. With the steady 700 Hz tone at the default cap, read the RMS on tip and on ring into 16, 32 and 64 ohm.
2. Unlock the cap, set maximum volume, record the 32 ohm RMS on each channel.
3. Insert a TS plug (tip and ring both shorted to sleeve) for 10 min at maximum volume with the full-scale tone.
4. Remove the TS plug, refit the 32 ohm load and repeat the 32 ohm reading at maximum volume.
5. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
6. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if tip and ring RMS differ by at most 1 dB at the active cap into each of 16, 32 and 64 ohm (REQ-SYS-078), and after the 10 min short each channel's 32 ohm RMS is within 1 dB of its value before the short with no damage (REQ-SYS-079); otherwise Fail.

**Instruments and fixtures.**

- Multimeter, true-RMS AC voltage range, accuracy at 700 Hz per datasheet copied into the report (OQ-VV-003)
- Audio load fixture: 16, 32 and 64 ohm resistors, 0.25 W, selectable on a 3.5 mm TRS breakout per channel (docs/vv/fixtures/audio-load.md, planned)
- 3.5 mm TS plug
- Adjustable bench supply, 0 to 30 V, current limit set per step

**Expected artifacts.**

- `audio-load.csv` (csv): Load, channel, RMS, before and after short

### TC-SYS-058: BOM, schematic and ICD inspection: cell holders, antenna connector, controller module and key-jack wiring

| Field | Value |
|---|---|
| Requirements | REQ-SYS-080, REQ-SYS-104, REQ-SYS-126, REQ-SYS-174 |
| Method / class | Inspection / Inspection |
| Status | Draft |
| Automation | `tools/check_bom.py` |

**Setup.** Article: design data at tag baseline/cdr: BOM, schematic, holder and connector datasheets, enclosure STEP and docs/icd/ICD-CTL-KEY.md. Configuration: tools/check_bom.py (planned) prints the BOM lines selected by reference designator and the datasheet fields named in the steps; the reviewer compares them with the schematic and the ICD pin table. Credit row: I. Inspection of design data, closed at CDR on the product baseline (docs/process/04-verification-and-validation.md sections 5.1 item 4 and 5.2); the receipt inspection named in the verification_note, where there is one, is recorded as data in the same report. Tools: kicad-cli at its lock path /Applications/KiCad/KiCad.app/Contents/MacOS/kicad-cli and Python per tools/toolchain.lock.md Safety: not applicable (design data only). Environment: not applicable.

**Procedure.**

1. Confirm that the BOM carries two 18650 holders, that the schematic wires the two cells in series, and that the holders hold the cells by spring contact with no soldered cell tab.
2. Confirm on the enclosure STEP renders that both cells can be removed and inserted with the cell cover opened and no tool other than the cover fastener.
3. Read the antenna connector BOM line and datasheet: SMA jack (female body), stainless-steel body, 50 ohm impedance.
4. Confirm that the controller is the Raspberry Pi Pico 2 module in the BOM and the schematic symbol, and that no other microcontroller exists on the board.
5. Trace the key jack in the schematic: tip to the dit and straight-key input, ring to the dah input, sleeve to common; compare with the ICD-CTL-KEY pin table and the BOM connector (3.5 mm TRS).
6. Record the inspected file paths, their commit and tool versions in the report.
7. On any finding against the criteria, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if the BOM and schematic show two series 18650 cells in holders removable without soldering, a 50 ohm stainless-steel SMA jack with female body as the antenna port, the Raspberry Pi Pico 2 module as the only controller, and a 3.5 mm TRS key jack wired tip dit or straight key, ring dah and sleeve common in agreement with ICD-CTL-KEY; otherwise Fail.

**Expected artifacts.**

- `bom-selected-lines.csv` (csv): BOM lines of the holders, antenna jack, controller module and key jack with datasheet fields
- `key-jack-trace.png` (plot): Schematic excerpt of the key jack with the ICD pin table beside it

### TC-SYS-059: Charge termination voltage per cell and charge time of a 3000 mAh pack from low-battery power-down

| Field | Value |
|---|---|
| Requirements | REQ-SYS-081, REQ-SYS-091 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | none (manual) |

**Setup.** Article: CWHT-A-001 in its enclosure, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: the owner's 3000 mAh cells, discharged in the unit to the low-battery power-down; switch off; USB through the USB breakout fixture from a 500 mA port; each cell voltage read with the multimeter at the holder terminals; the meter's DC voltage accuracy must be 0.1 percent or better, otherwise the termination reading is Blocked (04 section 8.3 item 3). Credit row: T-HW. Test of a system requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the campaign (section 13) and witnessed by the owner; the pre-build Simulation, HostUnit and Emulation evidence named in each requirement's verification_note is supporting only and is not part of this case. TBR values: the acceptance criteria use the values of REQ-SYS-081 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Hazard controls exercised: HZ-002 (from the cited requirements; docs/safety/hazards.json). Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: cells and cell simulators are handled per the operations handbook battery section: current limit set before connection, cell terminals never shorted, cells on a non-flammable surface and attended during every charge or discharge run; a cell warm to the touch above about 45 C ends the run. Environment: room temperature 18 to 28 C; the cells or cell simulators named in Configuration; dummy load on the antenna port.

**Procedure.**

1. Wire the UART telemetry test pad to a logic-capture channel and confirm that the sigrok-cli UART decoder prints the telemetry lines (REQ-SYS-150).
2. Discharge the cells in the unit (Receive at maximum volume) until the low-battery power-down; record the time.
3. Apply USB with the switch off; record the start time and the VBUS current.
4. Every hour read VBUS current and the cell voltages; log the telemetry.
5. At charge termination record the time and read each cell voltage within 60 s.
6. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
7. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if each cell voltage at termination is 4.179 to 4.221 V (4.20 V +/-0.5 percent) with the meter accuracy included (REQ-SYS-081), and the pack reaches termination at most 12 h after USB is applied (REQ-SYS-091); otherwise Fail.

**Instruments and fixtures.**

- USB power breakout fixture with VBUS routed through the multimeter current range (docs/vv/fixtures/usb-breakout.md, planned)
- Multimeter, DC voltage and DC current ranges, accuracy per datasheet copied into the report (OQ-VV-003)
- Pico-based logic capture (second Pico 2 with sigrok-pico firmware read by sigrok-cli; planned, ADR-009), 3.3 V inputs, 1 MS/s unless a step states otherwise
- Owner's 3000 mAh 18650 cells, a matched pair

**Expected artifacts.**

- `charge-full.csv` (csv): Time, VBUS current, cell voltages

### TC-SYS-060: Charge temperature window 0 C to 45 C and cell over-temperature power-down at 60 C

| Field | Value |
|---|---|
| Requirements | REQ-SYS-082, REQ-SYS-099 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | none (manual) |

**Setup.** Article: CWHT-A-001, enclosure lid off for test-point access, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: cells replaced by the two-cell simulator fixture unless a step names the owner's cells; USB through the USB breakout fixture; charge current read on the multimeter in series with the pack lead; charge state and events read from the display and the UART telemetry. The cell NTC is replaced by the NTC substitution fixture at -3, -1, +1, +3, 43, 45, 47, 58 and 62 C equivalents. Credit row: T-HW. Test of a system requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the campaign (section 13) and witnessed by the owner; the pre-build Simulation, HostUnit and Emulation evidence named in each requirement's verification_note is supporting only and is not part of this case. TBR values: the acceptance criteria use the values of REQ-SYS-082, REQ-SYS-099 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Hazard controls exercised: HZ-002, HZ-007 (from the cited requirements; docs/safety/hazards.json). Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: cells and cell simulators are handled per the operations handbook battery section: current limit set before connection, cell terminals never shorted, cells on a non-flammable surface and attended during every charge or discharge run; a cell warm to the touch above about 45 C ends the run. Environment: room temperature 18 to 28 C; the cells or cell simulators named in Configuration; dummy load on the antenna port.

**Procedure.**

1. With the switch off and USB applied, step the NTC fixture through -3, -1, +1 and +3 C; read the charge current at each after 30 s.
2. Step through 43, 45 and 47 C; read the charge current at each.
3. With the switch on (no USB) in Receive, set 58 C and read the pack current; then set 62 C and read it.
4. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
5. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if charging runs at +1, +3 and 43 C and is stopped at -3 and 47 C (thresholds within 0 C +/-2 C and 45 C +/-2 C) (REQ-SYS-082), and the loads are powered at 58 C and powered down at 62 C (REQ-SYS-099); otherwise Fail.

**Instruments and fixtures.**

- NTC substitution fixture: fixed resistors at the temperature equivalents named in the steps, switched in place of the cell or PA sensor at its test pad, the switch's second pole wired to a logic-capture channel as the event marker (docs/vv/fixtures/ntc-substitution.md, planned)
- Two-cell simulator fixture: the bench supply across the pack terminals with an adjustable, buffered mid-point tap for the cell junction and a parallel sink resistor so that the fixture absorbs charger current (docs/vv/fixtures/cell-simulator.md, planned; characterized before TRR)
- USB power breakout fixture with VBUS routed through the multimeter current range (docs/vv/fixtures/usb-breakout.md, planned)
- Multimeter, DC voltage and DC current ranges, accuracy per datasheet copied into the report (OQ-VV-003)

**Expected artifacts.**

- `cell-temp.csv` (csv): Equivalent temperature, state, charge or pack current

### TC-SYS-061: Independent cell over-voltage protection between 4.25 and 4.30 V

| Field | Value |
|---|---|
| Requirements | REQ-SYS-083 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | none (manual) |

**Setup.** Article: CWHT-A-001, enclosure lid off for test-point access, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: cells replaced by the two-cell simulator fixture unless a step names the owner's cells; USB through the USB breakout fixture; charge current read on the multimeter in series with the pack lead; charge state and events read from the display and the UART telemetry. The charger is held off (fault build command, or charger enable held inactive at its test pad) so that only the protector acts; the protector FET state read as the voltage across it with the multimeter. Credit row: T-HW. Test of a system requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the campaign (section 13) and witnessed by the owner; the pre-build Simulation, HostUnit and Emulation evidence named in each requirement's verification_note is supporting only and is not part of this case. TBR values: the acceptance criteria use the values of REQ-SYS-083 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Hazard controls exercised: HZ-002 (from the cited requirements; docs/safety/hazards.json). Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: cells and cell simulators are handled per the operations handbook battery section: current limit set before connection, cell terminals never shorted, cells on a non-flammable surface and attended during every charge or discharge run; a cell warm to the touch above about 45 C ends the run. Environment: room temperature 18 to 28 C; the cells or cell simulators named in Configuration; dummy load on the antenna port.

**Procedure.**

1. Set both simulated cells to 4.20 V; read the protector FET state.
2. Raise one simulated cell in 5 mV steps from 4.20 V to 4.35 V, reading the FET state at each step; record the trip voltage.
3. Lower it back and record the release voltage; repeat for the other cell.
4. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
5. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if for each cell the protector stops the charge path at a cell voltage from 4.25 V to 4.30 V at room temperature with the meter accuracy included, with the charger and firmware not acting; otherwise Fail. The 0 C to 45 C span of the requirement is covered by the supporting threshold analysis named in its verification_note.

**Instruments and fixtures.**

- Two-cell simulator fixture: the bench supply across the pack terminals with an adjustable, buffered mid-point tap for the cell junction and a parallel sink resistor so that the fixture absorbs charger current (docs/vv/fixtures/cell-simulator.md, planned; characterized before TRR)
- Multimeter, DC voltage and DC current ranges, accuracy per datasheet copied into the report (OQ-VV-003)
- Adjustable bench supply, 0 to 30 V, current limit set per step

**Expected artifacts.**

- `cell-ov.csv` (csv): Cell, voltage step, FET state

### TC-SYS-062: Independent cell under-voltage disconnect at 2.50 V and survival of a reversed cell

| Field | Value |
|---|---|
| Requirements | REQ-SYS-084, REQ-SYS-086 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | none (manual) |

**Setup.** Article: CWHT-A-001, enclosure lid off for test-point access, running the fault-injection test build of release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (a build flavour of the release commit whose injection commands arrive over the UART test pads from the host serial terminal through the 3.3 V serial adapter, or over USB serial only in steps that expect no carrier, because USB VBUS sets the USB flag and the hardware transmit inhibit of REQ-SYS-092, and which toggles the injection-marker test pad at the instant of each injection); the release image is restored and checked with picotool verify at the end of the case. Configuration: cells replaced by the two-cell simulator fixture unless a step names the owner's cells; USB through the USB breakout fixture; charge current read on the multimeter in series with the pack lead; charge state and events read from the display and the UART telemetry. The fault build has the firmware power-down disabled; for the reversal a bench-supply channel current-limited to 100 mA emulates one reversed cell. Credit row: T-HW. Test of a system requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the campaign (section 13) and witnessed by the owner; the pre-build Simulation, HostUnit and Emulation evidence named in each requirement's verification_note is supporting only and is not part of this case. TBR values: the acceptance criteria use the values of REQ-SYS-084, REQ-SYS-086 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Hazard controls exercised: HZ-007 (from the cited requirements; docs/safety/hazards.json). Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: cells and cell simulators are handled per the operations handbook battery section: current limit set before connection, cell terminals never shorted, cells on a non-flammable surface and attended during every charge or discharge run; a cell warm to the touch above about 45 C ends the run. Environment: room temperature 18 to 28 C; the cells or cell simulators named in Configuration; dummy load on the antenna port.

**Procedure.**

1. Set both simulated cells to 3.00 V with the unit on; lower one in 10 mV steps from 2.60 V to 2.40 V, reading the pack current and the voltage across the protector FETs at each step.
2. Record the cell voltage at which the protector FETs open and the pack current falls below 50 uA; restore and repeat for the other cell.
3. Switch off; connect the reversed-cell emulation in place of one cell; read the current drawn for 60 s with the switch off and then on.
4. Remove the reversal, fit correct cells (simulator at 3.70 V), disconnect USB, switch on and confirm normal Receive and 1 s transmissions into the dummy load with the straight key and with the paddle.
5. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
6. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if the pack is disconnected from its loads (current below 50 uA) at a cell voltage of 2.45 to 2.55 V with firmware power-down disabled (REQ-SYS-084), and with one cell reversed the current drawn is at most 10 mA and the unit then operates normally (REQ-SYS-086); otherwise Fail.

**Instruments and fixtures.**

- Two-cell simulator fixture: the bench supply across the pack terminals with an adjustable, buffered mid-point tap for the cell junction and a parallel sink resistor so that the fixture absorbs charger current (docs/vv/fixtures/cell-simulator.md, planned; characterized before TRR)
- Host computer with picotool and a serial terminal per tools/toolchain.lock.md, micro-USB cable
- 3.3 V USB-to-UART serial adapter between the host computer and the UART test pads, so that injection commands reach the unit with its USB port disconnected (docs/vv/fixtures/uart-adapter.md, planned)
- Adjustable bench supply, 0 to 30 V, current limit set per step
- Multimeter, DC voltage and DC current ranges, accuracy per datasheet copied into the report (OQ-VV-003)
- 50 ohm BNC dummy load with SMA adapter, power rating recorded in the report
- Owner's straight key and iambic paddle, 3.5 mm TRS plugs (SI-034)

**Expected artifacts.**

- `cell-uv.csv` (csv): Cell, voltage, pack current
- `cell-reverse.csv` (csv): Switch state, current

### TC-SYS-063: Pack over-current and short-circuit trip level from the protector threshold, FET resistance and fuse rating

| Field | Value |
|---|---|
| Requirements | REQ-SYS-085 |
| Method / class | Analysis / Simulation |
| Status | Draft |
| Automation | `tools/budgets/pack_protection_check.py` |

**Setup.** Article: design data at tag baseline/cdr: the protector part (ABLIC S-8252 class) over-current detection voltages, the dual N-FET on-resistance over gate drive and temperature, and the fuse part. Configuration: tools/budgets/pack_protection_check.py (planned) computes the trip current I = V_detect / R_ds(on) over the datasheet tolerance and the -10 C to +60 C cell temperature range, and compares the fuse time-current curve with the 2.1 A key-down pulses. Credit row: A. Analysis closed by Simulation on the CDR design data and confirmed at SAR by the physical configuration audit of every analyzed value (docs/process/04-verification-and-validation.md sections 5.1 item 5 and 5.2); the post-build readings named in the verification_note are supporting data only. TBR values: the acceptance criteria use the values of REQ-SYS-085 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Hazard controls exercised: HZ-007 (from the cited requirements; docs/safety/hazards.json). Risk acceptance: the verification_note of REQ-SYS-085 (RSK-007) begins 'Analysis accepted per RSK-NNN'; that risk carries the hazard control not closed by Test (docs/process/04-verification-and-validation.md section 3, rule 7.3.6). Tools: Python per tools/toolchain.lock.md Safety: not applicable (design data only). Environment: not applicable.

**Procedure.**

1. Confirm that the part numbers and datasheet values equal the CDR BOM (script prints the diff; an empty diff is required).
2. Compute the minimum and maximum trip current over detection-voltage tolerance, FET on-resistance tolerance and temperature.
3. Confirm from the fuse curve that the 2.1 A key-down pulses of the ConOps duty cycle do not open or age the fuse and that the fuse opens at a pack short.
4. Record tool versions, the design-data tag and the commit of every deck, model, script and checker in the report.
5. On any assertion or checker failure, or any difference between the analyzed values and the design data, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if the computed discharge-interrupt trip current lies between 3 A and 10 A at every corner and the fuse neither opens nor ages at the 2.1 A key-down pulses; otherwise Fail.

**Expected artifacts.**

- `pack-protection.csv` (csv): Corner, detection voltage, on-resistance and trip current

### TC-SYS-064: Cell insertion check, dual-path cell-voltage check and rails held off for out-of-window cells

| Field | Value |
|---|---|
| Requirements | REQ-SYS-087, REQ-SYS-088, REQ-SYS-166 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | none (manual) |

**Setup.** Article: CWHT-A-001, enclosure lid off for test-point access, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: cells replaced by the two-cell simulator fixture unless a step names the owner's cells; USB through the USB breakout fixture; charge current read on the multimeter in series with the pack lead; charge state and events read from the display and the UART telemetry. For the dual-path check a divider resistor of one measurement path is substituted to offset that path by 150 mV (docs/vv/fixtures/, planned). Credit row: T-HW. Test of a system requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the campaign (section 13) and witnessed by the owner; the pre-build Simulation, HostUnit and Emulation evidence named in each requirement's verification_note is supporting only and is not part of this case. TBR values: the acceptance criteria use the values of REQ-SYS-087, REQ-SYS-088, REQ-SYS-166 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Hazard controls exercised: HZ-002, HZ-007 (from the cited requirements; docs/safety/hazards.json). Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: cells and cell simulators are handled per the operations handbook battery section: current limit set before connection, cell terminals never shorted, cells on a non-flammable surface and attended during every charge or discharge run; a cell warm to the touch above about 45 C ends the run. Environment: room temperature 18 to 28 C; the cells or cell simulators named in Configuration; dummy load on the antenna port.

**Procedure.**

1. Set the cells to 3.70 V and 4.10 V (400 mV apart), switch off, apply USB; read the charge current after 30 s.
2. Set 2.40 V and 3.70 V; apply USB; read. Set 4.40 V and 3.70 V; apply USB; read.
3. Set both at 3.70 V; start a charge; substitute the divider resistor during the charge; read the charge current and the displayed cause.
4. Remove USB; set one cell to 2.40 V; switch on; read the 5 V and 3.3 V rails with the multimeter. Repeat with one cell at 4.40 V.
5. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
6. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if no charge current flows (at most 5 mA) with cells 400 mV apart or with either cell outside 2.5 V to 4.3 V (REQ-SYS-087), charging stops with the cell-sense cause shown when the two measurements differ by 150 mV (REQ-SYS-088), and the regulated rails stay below 0.5 V at switch-on with either cell at 2.40 V or 4.40 V (REQ-SYS-166); otherwise Fail. The 5 mA and 0.5 V thresholds are the test author's (0.5 V follows REQ-SYS-149).

**Instruments and fixtures.**

- Two-cell simulator fixture: the bench supply across the pack terminals with an adjustable, buffered mid-point tap for the cell junction and a parallel sink resistor so that the fixture absorbs charger current (docs/vv/fixtures/cell-simulator.md, planned; characterized before TRR)
- USB power breakout fixture with VBUS routed through the multimeter current range (docs/vv/fixtures/usb-breakout.md, planned)
- Multimeter, DC voltage and DC current ranges, accuracy per datasheet copied into the report (OQ-VV-003)

**Expected artifacts.**

- `cell-supervision.csv` (csv): Condition, charge current, rails, displayed cause

### TC-SYS-065: Charge safety timer of 15 h and constant-voltage current-fall supervision

| Field | Value |
|---|---|
| Requirements | REQ-SYS-089, REQ-SYS-167 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | none (manual) |

**Setup.** Article: CWHT-A-001, enclosure lid off for test-point access, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: cells replaced by the two-cell simulator fixture unless a step names the owner's cells; USB through the USB breakout fixture; charge current read on the multimeter in series with the pack lead; charge state and events read from the display and the UART telemetry. For the timer run the simulator is held below the constant-voltage threshold by its sink resistor so the charger stays in constant current; for the current-fall run it is held at the constant-voltage point with a fixed load so the charge current stays flat. Credit row: T-HW. Test of a system requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the campaign (section 13) and witnessed by the owner; the pre-build Simulation, HostUnit and Emulation evidence named in each requirement's verification_note is supporting only and is not part of this case. TBR values: the acceptance criteria use the values of REQ-SYS-089, REQ-SYS-167 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Hazard controls exercised: HZ-002 (from the cited requirements; docs/safety/hazards.json). Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: cells and cell simulators are handled per the operations handbook battery section: current limit set before connection, cell terminals never shorted, cells on a non-flammable surface and attended during every charge or discharge run; a cell warm to the touch above about 45 C ends the run. Environment: room temperature 18 to 28 C; the cells or cell simulators named in Configuration; dummy load on the antenna port.

**Procedure.**

1. Wire the UART telemetry test pad to a logic-capture channel and confirm that the sigrok-cli UART decoder prints the telemetry lines (REQ-SYS-150).
2. Timer run: set both simulated cells to 3.90 V with the sink resistor absorbing the charge current; apply USB with the switch off; log charge current and telemetry until the charge stops or 15 h 30 min elapse.
3. Current-fall run: set the simulator at the constant-voltage point with a fixed load; apply USB; log until the charge stops or 90 min after constant-voltage entry.
4. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
5. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if the timer run stops charging at most 15 h after the charge start (REQ-SYS-089), and the current-fall run stops charging 60 min +/-2 min after constant-voltage entry with the charge current having fallen by less than 20 mA (REQ-SYS-167); otherwise Fail. The +/-2 min window is the test author's, because REQ-SYS-167 states none.

**Instruments and fixtures.**

- Two-cell simulator fixture: the bench supply across the pack terminals with an adjustable, buffered mid-point tap for the cell junction and a parallel sink resistor so that the fixture absorbs charger current (docs/vv/fixtures/cell-simulator.md, planned; characterized before TRR)
- USB power breakout fixture with VBUS routed through the multimeter current range (docs/vv/fixtures/usb-breakout.md, planned)
- Multimeter, DC voltage and DC current ranges, accuracy per datasheet copied into the report (OQ-VV-003)
- Pico-based logic capture (second Pico 2 with sigrok-pico firmware read by sigrok-cli; planned, ADR-009), 3.3 V inputs, 1 MS/s unless a step states otherwise

**Expected artifacts.**

- `charge-timers.csv` (csv): Run, time, charge current, events

### TC-SYS-066: Hardware transmit inhibit with USB present, and no transmitter supply from USB alone

| Field | Value |
|---|---|
| Requirements | REQ-SYS-092, REQ-SYS-149, REQ-SYS-183 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | none (manual) |

**Setup.** Article: CWHT-A-001, enclosure lid off for test-point access, running the fault-injection test build of release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (a build flavour of the release commit whose injection commands arrive over the UART test pads from the host serial terminal through the 3.3 V serial adapter, or over USB serial only in steps that expect no carrier, because USB VBUS sets the USB flag and the hardware transmit inhibit of REQ-SYS-092, and which toggles the injection-marker test pad at the instant of each injection); the release image is restored and checked with picotool verify at the end of the case. Configuration: fault build asserting TX_KEY on command; antenna port to the calibrated power attenuator and the tinySA Ultra; logic capture on TX_KEY and PA_EN; transmitter rail read with the multimeter at its test pad; 1 W step. Credit row: T-HW. Test of a system requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the campaign (section 13) and witnessed by the owner; the pre-build Simulation, HostUnit and Emulation evidence named in each requirement's verification_note is supporting only and is not part of this case. TBR values: the acceptance criteria use the values of REQ-SYS-149 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). RF-off level: the acceptance criteria use -57 dBm, the value of REQ-SYS-183 marked TBR (close by PDR); a change returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2). Hazard controls exercised: HZ-011, HZ-014 (from the cited requirements; docs/safety/hazards.json). Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: every transmission goes into the 50 ohm dummy load or the calibrated power attenuator, connected before power-on, never into an open antenna port; key-down duty kept within the load rating recorded in the report; anyone other than the operator stays 0.6 m or more from the unit and load while keying and 1.0 m or more during a tune carrier (NGO-019); the bench supply current limit is set before each power-on; antistatic wrist strap while the lid is off; the PA area is not touched after key-down runs. Environment: room temperature 18 to 28 C; the pack is supplied by the bench supply at 7.4 V +/-0.05 V through the battery terminals unless a step sets another value; dummy load on the antenna port.

**Procedure.**

1. Run the logic-capture reference pulse-train check of this session and record the result (docs/process/04-verification-and-validation.md section 4).
2. Measure the attenuator and cable S21 on the NanoVNA from 9 kHz (or the NanoVNA lower limit) to 1.5 GHz and save the Touchstone file; run the tinySA Ultra internal calibration-output check; record both.
3. With the cells (bench supply) fitted and USB applied, command TX_KEY high for 3 s, then close the straight key and the paddle for 3 s each; record PA_EN and RF.
4. Remove the cells; apply USB with the unit in the bootloader state; read the transmitter rail while pressing the straight key.
5. With the cells removed and the application running from USB, command TX_KEY high; read the transmitter rail and RF.
6. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
7. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if with USB present no carrier at the set frequency above -57 dBm at the antenna port (the RF-off level of REQ-SYS-183) appears for the commanded TX_KEY or either key (REQ-SYS-092), and with the cells removed the transmitter rail stays below 0.5 V in the bootloader and application states while TX_KEY is asserted (REQ-SYS-149); otherwise Fail.

**Instruments and fixtures.**

- Pico-based logic capture (second Pico 2 with sigrok-pico firmware read by sigrok-cli; planned, ADR-009), 3.3 V inputs, 1 MS/s unless a step states otherwise
- Host computer with picotool and a serial terminal per tools/toolchain.lock.md, micro-USB cable
- 3.3 V USB-to-UART serial adapter between the host computer and the UART test pads, so that injection commands reach the unit with its USB port disconnected (docs/vv/fixtures/uart-adapter.md, planned)
- tinySA Ultra spectrum analyzer (ADR-021) through the calibrated 30 to 40 dB attenuator rated 10 W or more, attenuator S21 measured on the NanoVNA in the same session; level accuracy per its TV record
- NanoVNA, SOL calibration at the cable end used, checked on the dummy load
- Multimeter, DC voltage and DC current ranges, accuracy per datasheet copied into the report (OQ-VV-003)
- USB power breakout fixture with VBUS routed through the multimeter current range (docs/vv/fixtures/usb-breakout.md, planned)
- Owner's straight key and iambic paddle, 3.5 mm TRS plugs (SI-034)
- Adjustable bench supply, 0 to 30 V, current limit set per step

**Expected artifacts.**

- `usb-inhibit.csv` (csv): State, stimulus, PA_EN, RF level, transmitter rail

### TC-SYS-067: Battery life of at least 8 h at 1:9 and the low-battery warning at least 15 min before transmit inhibit

| Field | Value |
|---|---|
| Requirements | REQ-SYS-094, REQ-SYS-096 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | none (manual) |

**Setup.** Article: CWHT-A-001 in its enclosure, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: fresh, fully charged owner's 3000 mAh cells; USB disconnected; keyed pattern at 1:9 transmit-to-receive with 45 percent key-down in transmit at the 5 W step into the dummy load, from a Bench-test duty-cycle pattern if the software design provides one, otherwise from a keying fixture that closes the key-jack tip contact through an optocoupler driven by a Pico 2 running the pattern with every closure shorter than the straight-key timeout (docs/vv/fixtures/keying-fixture.md, planned); display and audio on at the default cap; elapsed time and the warning and inhibit events from the UART telemetry recorded on the logic capture (a second Pico 2 USB-UART bridge image is the alternative for this long run). Credit row: T-HW. Test of a system requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the campaign (section 13) and witnessed by the owner; the pre-build Simulation, HostUnit and Emulation evidence named in each requirement's verification_note is supporting only and is not part of this case. Hazard controls exercised: HZ-007 (from the cited requirements; docs/safety/hazards.json). Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: every transmission goes into the 50 ohm dummy load or the calibrated power attenuator, connected before power-on, never into an open antenna port; key-down duty kept within the load rating recorded in the report; anyone other than the operator stays 0.6 m or more from the unit and load while keying and 1.0 m or more during a tune carrier (NGO-019); the bench supply current limit is set before each power-on; antistatic wrist strap while the lid is off; the PA area is not touched after key-down runs. Safety: cells and cell simulators are handled per the operations handbook battery section: current limit set before connection, cell terminals never shorted, cells on a non-flammable surface and attended during every charge or discharge run; a cell warm to the touch above about 45 C ends the run. Environment: room temperature 18 to 28 C; the cells or cell simulators named in Configuration; dummy load on the antenna port.

**Procedure.**

1. Wire the UART telemetry test pad to a logic-capture channel and confirm that the sigrok-cli UART decoder prints the telemetry lines (REQ-SYS-150).
2. Record the cell voltages and start the 1:9 pattern; start the telemetry recording.
3. Check the unit and the dummy load temperature every 30 min.
4. Record the time of the low-battery warning and of the low-battery transmit inhibit from the telemetry.
5. Every hour, key by hand for 30 s with the straight key and for 30 s with the paddle in place of the pattern, keeping the ratio.
6. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
7. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if the elapsed time from start to the low-battery transmit inhibit is at least 8 h (REQ-SYS-094), and the low-battery warning appears at least 15 min before the inhibit (REQ-SYS-096); otherwise Fail.

**Instruments and fixtures.**

- Pico-based logic capture (second Pico 2 with sigrok-pico firmware read by sigrok-cli; planned, ADR-009), 3.3 V inputs, 1 MS/s unless a step states otherwise
- 50 ohm BNC dummy load with SMA adapter, power rating recorded in the report
- Multimeter, DC voltage and DC current ranges, accuracy per datasheet copied into the report (OQ-VV-003)
- Owner's straight key and iambic paddle, 3.5 mm TRS plugs (SI-034)
- Owner's 3000 mAh 18650 cells, a matched fresh pair, fully charged

**Expected artifacts.**

- `battery-19.csv` (csv): Time, cell voltages, events
- `battery-19-telemetry.log.txt` (serial_output): Telemetry of the run

### TC-SYS-068: Battery life of at least 6 h at 1:4

| Field | Value |
|---|---|
| Requirements | REQ-SYS-095 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | none (manual) |

**Setup.** Article: CWHT-A-001 in its enclosure, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: as TC-SYS-067 with a 1:4 transmit-to-receive pattern at 45 percent key-down at 5 W. Credit row: T-HW. Test of a system requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the campaign (section 13) and witnessed by the owner; the pre-build Simulation, HostUnit and Emulation evidence named in each requirement's verification_note is supporting only and is not part of this case. TBR values: the acceptance criteria use the values of REQ-SYS-095 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: every transmission goes into the 50 ohm dummy load or the calibrated power attenuator, connected before power-on, never into an open antenna port; key-down duty kept within the load rating recorded in the report; anyone other than the operator stays 0.6 m or more from the unit and load while keying and 1.0 m or more during a tune carrier (NGO-019); the bench supply current limit is set before each power-on; antistatic wrist strap while the lid is off; the PA area is not touched after key-down runs. Safety: cells and cell simulators are handled per the operations handbook battery section: current limit set before connection, cell terminals never shorted, cells on a non-flammable surface and attended during every charge or discharge run; a cell warm to the touch above about 45 C ends the run. Environment: room temperature 18 to 28 C; the cells or cell simulators named in Configuration; dummy load on the antenna port.

**Procedure.**

1. Wire the UART telemetry test pad to a logic-capture channel and confirm that the sigrok-cli UART decoder prints the telemetry lines (REQ-SYS-150).
2. Record the cell voltages and start the 1:4 pattern and the telemetry recording.
3. Check the unit and the dummy load temperature every 30 min.
4. Every hour, key by hand for 30 s with the straight key and for 30 s with the paddle in place of the pattern, keeping the ratio.
5. Record the time of the low-battery transmit inhibit.
6. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
7. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if the elapsed time from start to the low-battery transmit inhibit is at least 6 h; otherwise Fail.

**Instruments and fixtures.**

- Pico-based logic capture (second Pico 2 with sigrok-pico firmware read by sigrok-cli; planned, ADR-009), 3.3 V inputs, 1 MS/s unless a step states otherwise
- 50 ohm BNC dummy load with SMA adapter, power rating recorded in the report
- Multimeter, DC voltage and DC current ranges, accuracy per datasheet copied into the report (OQ-VV-003)
- Owner's straight key and iambic paddle, 3.5 mm TRS plugs (SI-034)
- Owner's 3000 mAh 18650 cells, a matched fresh pair, fully charged

**Expected artifacts.**

- `battery-14.csv` (csv): Time, cell voltages, events

### TC-SYS-069: Low-battery transmit inhibit at 3.20 V, low-battery power-down at 3.00 V and high pack-voltage transmit lockout at 8.60 V

| Field | Value |
|---|---|
| Requirements | REQ-SYS-097, REQ-SYS-098, REQ-SYS-153 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | none (manual) |

**Setup.** Article: CWHT-A-001, enclosure lid off for test-point access, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: the two-cell simulator fixture; logic capture on PA_EN; multimeter on the pack current; dummy load; 1 W step; each voltage stepped in 10 mV steps (20 mV for the pack) and held 10 s before keying. Credit row: T-HW. Test of a system requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the campaign (section 13) and witnessed by the owner; the pre-build Simulation, HostUnit and Emulation evidence named in each requirement's verification_note is supporting only and is not part of this case. TBR values: the acceptance criteria use the values of REQ-SYS-097, REQ-SYS-098, REQ-SYS-153 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Hazard controls exercised: HZ-007, HZ-008 (from the cited requirements; docs/safety/hazards.json). Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: every transmission goes into the 50 ohm dummy load or the calibrated power attenuator, connected before power-on, never into an open antenna port; key-down duty kept within the load rating recorded in the report; anyone other than the operator stays 0.6 m or more from the unit and load while keying and 1.0 m or more during a tune carrier (NGO-019); the bench supply current limit is set before each power-on; antistatic wrist strap while the lid is off; the PA area is not touched after key-down runs. Safety: cells and cell simulators are handled per the operations handbook battery section: current limit set before connection, cell terminals never shorted, cells on a non-flammable surface and attended during every charge or discharge run; a cell warm to the touch above about 45 C ends the run. Environment: room temperature 18 to 28 C; the cells or cell simulators named in Configuration; dummy load on the antenna port.

**Procedure.**

1. Run the logic-capture reference pulse-train check of this session and record the result (docs/process/04-verification-and-validation.md section 4).
2. Set both cells to 3.70 V; lower one from 3.30 V to 3.10 V in 10 mV steps; at each, in receive, close the straight key for 1 s; record PA_EN.
3. Repeat with the other cell and the paddle.
4. Lower one cell from 3.10 V to 2.90 V in 10 mV steps; read the pack current at each.
5. Set both cells equal and raise the pack from 8.50 V to 8.70 V in 20 mV steps; at each close the straight key for 1 s; record PA_EN. Repeat with the paddle.
6. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
7. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if transmission is refused (PA_EN low) at every step at or below 3.15 V and allowed at or above 3.25 V, for either cell and both keys (REQ-SYS-097); the loads power down at a cell voltage from 2.95 V to 3.05 V (REQ-SYS-098); and transmission is refused at every pack step at or above 8.65 V and allowed at or below 8.55 V (REQ-SYS-153); otherwise Fail.

**Instruments and fixtures.**

- Two-cell simulator fixture: the bench supply across the pack terminals with an adjustable, buffered mid-point tap for the cell junction and a parallel sink resistor so that the fixture absorbs charger current (docs/vv/fixtures/cell-simulator.md, planned; characterized before TRR)
- Pico-based logic capture (second Pico 2 with sigrok-pico firmware read by sigrok-cli; planned, ADR-009), 3.3 V inputs, 1 MS/s unless a step states otherwise
- Multimeter, DC voltage and DC current ranges, accuracy per datasheet copied into the report (OQ-VV-003)
- 50 ohm BNC dummy load with SMA adapter, power rating recorded in the report
- Owner's straight key and iambic paddle, 3.5 mm TRS plugs (SI-034)

**Expected artifacts.**

- `pack-thresholds.csv` (csv): Cell or pack voltage, key type, PA_EN, pack current

### TC-SYS-070: Pack current with the switch off and loads removed by the mechanical power switch

| Field | Value |
|---|---|
| Requirements | REQ-SYS-100, REQ-SYS-101 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | none (manual) |

**Setup.** Article: CWHT-A-001, enclosure lid off for test-point access, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: bench supply at 7.4 V as the pack; multimeter in the microamp range in the pack lead; rails read at their test pads; USB disconnected. Credit row: T-HW. Test of a system requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the campaign (section 13) and witnessed by the owner; the pre-build Simulation, HostUnit and Emulation evidence named in each requirement's verification_note is supporting only and is not part of this case. TBR values: the acceptance criteria use the values of REQ-SYS-100 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Hazard controls exercised: HZ-004, HZ-007 (from the cited requirements; docs/safety/hazards.json). Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: no transmission is intended; the dummy load stays on the antenna port throughout so that an unintended key-down is absorbed; bench supply current limit set before power-on; antistatic wrist strap while the lid is off. Environment: room temperature 18 to 28 C; the pack is supplied by the bench supply at 7.4 V +/-0.05 V through the battery terminals unless a step sets another value; dummy load on the antenna port.

**Procedure.**

1. Switch off; wait 60 s; read the pack current on the microamp range.
2. With the switch off, read the PA rail and VSYS with the multimeter.
3. Switch on and off five times, repeating both readings after the last.
4. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
5. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if the pack current with the switch off is at most 50 uA with the meter accuracy added (REQ-SYS-100), and the PA rail and VSYS are below 0.5 V with the switch off (REQ-SYS-101); otherwise Fail. The 0.5 V threshold follows REQ-SYS-149.

**Instruments and fixtures.**

- Adjustable bench supply, 0 to 30 V, current limit set per step
- Multimeter, DC voltage and DC current ranges, accuracy per datasheet copied into the report (OQ-VV-003)

**Expected artifacts.**

- `off-state.csv` (csv): Reading, value, range accuracy

### TC-SYS-071: Unit mass with cells fitted and without the antenna

| Field | Value |
|---|---|
| Requirements | REQ-SYS-102 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | none (manual) |

**Setup.** Article: CWHT-A-001 in its enclosure, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: the owner's cells fitted, antenna removed, knobs fitted; a kitchen or postal scale with at least 1 g resolution. Blocked until OQ-VV-002 confirms a scale (04 section 6.3). Credit row: T-HW. Test of a system requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the campaign (section 13) and witnessed by the owner; the pre-build Simulation, HostUnit and Emulation evidence named in each requirement's verification_note is supporting only and is not part of this case. TBR values: the acceptance criteria use the values of REQ-SYS-102 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: not applicable beyond normal handling. Environment: room temperature 18 to 28 C.

**Procedure.**

1. Check the scale with a known mass (for example 500 mL of water weighed in a tared container) and record the reading.
2. Weigh the unit three times and record each reading.
3. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
4. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if the mean of three readings plus the scale check error is at most 350 g; otherwise Fail.

**Instruments and fixtures.**

- Kitchen or postal scale, 1 g resolution (OQ-VV-002)

**Expected artifacts.**

- `mass.csv` (csv): Reading number and mass

### TC-SYS-072: Antenna-port bending moment of 4.0 N m without jack rotation, and counterpoise attachment position and resistance

| Field | Value |
|---|---|
| Requirements | REQ-SYS-105, REQ-SYS-107 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | none (manual) |

**Setup.** Article: CWHT-A-001 in its enclosure, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: a 0.40 m lever clamped on the SMA jack in place of an antenna and a 1.02 kg mass (10 N) hung at its end in four directions, made up by water volume if no scale exists (OQ-VV-002); a witness mark across the jack nut and the enclosure; NanoVNA return loss at the antenna port before and after; run on the printed fit-check enclosure and on the first machined enclosure; for the counterpoise, 1 A from the bench supply between the lug and the connector shell with the voltage sensed at the lug and shell (four-wire). Credit row: T-HW. Test of a system requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the campaign (section 13) and witnessed by the owner; the pre-build Simulation, HostUnit and Emulation evidence named in each requirement's verification_note is supporting only and is not part of this case. TBR values: the acceptance criteria use the values of REQ-SYS-105, REQ-SYS-107 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Hazard controls exercised: HZ-009 (from the cited requirements; docs/safety/hazards.json). Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: unit switched off with the cells removed; the hung mass is secured against falling onto the unit or a foot. Environment: room temperature 18 to 28 C; unit unpowered.

**Procedure.**

1. Calibrate the NanoVNA and measure the antenna-port return loss from 144 to 148 MHz with the dummy load fitted.
2. Draw the witness mark; fit the lever; hang the 10 N mass at 0.40 m for 60 s in each of the four directions (up, down, left, right).
3. Inspect the witness mark with a loupe and photograph it; remeasure the return loss with the dummy load.
4. Repeat the two previous steps on the machined enclosure if the first run was on the printed part.
5. Measure the distance from the counterpoise attachment to the antenna port centre with calipers or a steel rule.
6. Pass 1 A from the bench supply between the lug and the shell and read the millivolt drop between them.
7. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
8. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if the witness mark shows no rotation and the return loss changes by at most 1 dB from 144 to 148 MHz after the moment in all four directions (REQ-SYS-105), and the counterpoise attachment is within 20 mm of the antenna port with at most 10 mohm to the shell (at most 10 mV at 1 A, meter accuracy added) (REQ-SYS-107); otherwise Fail.

**Instruments and fixtures.**

- NanoVNA, SOL calibration at the cable end used, checked on the dummy load
- 50 ohm BNC dummy load with SMA adapter, power rating recorded in the report
- Adjustable bench supply, 0 to 30 V, current limit set per step
- Multimeter, DC voltage and DC current ranges, accuracy per datasheet copied into the report (OQ-VV-003)
- 0.40 m lever with SMA plug and a 1.02 kg mass (docs/vv/fixtures/, planned)

**Expected artifacts.**

- `antenna-moment.csv` (csv): Direction, return loss before and after, rotation observed
- `witness-mark.jpg` (photo): Photographs of the witness mark after each direction
- `counterpoise.csv` (csv): Distance, current, voltage drop, resistance

### TC-SYS-073: Antenna-port mating life from the jack datasheet rating and the handbook torque

| Field | Value |
|---|---|
| Requirements | REQ-SYS-106 |
| Method / class | Analysis / Simulation |
| Status | Draft |
| Automation | none (manual) |

**Setup.** Article: design data at tag baseline/cdr: the SMA jack datasheet (mating durability, recommended torque, return-loss specification) and the torque stated in docs/ops/operations-handbook.md. Configuration: Reviewer computation recorded in docs/design/analysis/; NanoVNA return loss at receipt and at SAR is supporting data. Credit row: A. Analysis closed by Simulation on the CDR design data and confirmed at SAR by the physical configuration audit of every analyzed value (docs/process/04-verification-and-validation.md sections 5.1 item 5 and 5.2); the post-build readings named in the verification_note are supporting data only. TBR values: the acceptance criteria use the values of REQ-SYS-106 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Hazard controls exercised: HZ-009 (from the cited requirements; docs/safety/hazards.json). Risk acceptance: the verification_note of REQ-SYS-106 (RSK-018) begins 'Analysis accepted per RSK-NNN'; that risk carries the hazard control not closed by Test (docs/process/04-verification-and-validation.md section 3, rule 7.3.6). Tools: Python per tools/toolchain.lock.md Safety: not applicable (design data only). Environment: not applicable.

**Procedure.**

1. Read the jack datasheet mating-cycle rating and the condition under which its return-loss specification holds after that rating.
2. Read the handbook mating torque and compare it with 0.45 to 0.56 N m and with the datasheet recommended torque.
3. Compute the change of return loss at 144 to 148 MHz from the datasheet return-loss specification before and after the rated cycles.
4. Record tool versions, the design-data tag and the commit of every deck, model, script and checker in the report.
5. On any assertion or checker failure, or any difference between the analyzed values and the design data, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if the jack is rated for at least 500 mating cycles at a torque range that contains 0.45 to 0.56 N m, the handbook states a torque inside 0.45 to 0.56 N m, and the datasheet return-loss specification after the rated cycles implies a change of at most 1 dB at 144 to 148 MHz; otherwise Fail.

**Expected artifacts.**

- `mating-life-analysis.md` (report): Datasheet values, handbook torque and the computation

### TC-SYS-074: Fully seated plugs at the key jack, headphone jack and micro-USB receptacle through the enclosure openings

| Field | Value |
|---|---|
| Requirements | REQ-SYS-108 |
| Method / class | Demonstration / Bench |
| Status | Draft |
| Automation | none (manual) |

**Setup.** Article: CWHT-A-001 in its enclosure, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: receipt demonstration with the owner's straight key and paddle plugs, headphones and a micro-USB cable. Credit row: D. Demonstration by the owner on the delivered unit (docs/process/04-verification-and-validation.md section 5.2): pass or fail is observed without detailed data gathering and each observation is photographed or logged. Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: not applicable beyond normal handling. Environment: room temperature 18 to 28 C.

**Procedure.**

1. Insert the key plug fully and confirm that it seats (tip, ring and sleeve contact: the key state follows the key).
2. Insert the headphone plug fully and confirm stereo audio at the default cap.
3. Insert the micro-USB cable fully and confirm the charge indication.
4. Photograph each seated plug against the enclosure face.
5. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
6. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if each plug seats fully through its enclosure opening and its function is observed; otherwise Fail.

**Instruments and fixtures.**

- Owner's straight key and iambic paddle, 3.5 mm TRS plugs (SI-034)
- Owner's headphones
- Micro-USB cable

**Expected artifacts.**

- `connector-demo.jpg` (photo): Photographs of the seated plugs

### TC-SYS-075: Enclosure material, anodize and conductive masking in the STEP, drawing and order notes

| Field | Value |
|---|---|
| Requirements | REQ-SYS-109 |
| Method / class | Inspection / Inspection |
| Status | Draft |
| Automation | none (manual) |

**Setup.** Article: design data at tag baseline/cdr: enclosure STEP, 2D drawing with masking callouts and the PCBWay CNC order notes in the CDR release package under hardware/releases/. Configuration: Reviewer reads the drawing title block, finish notes and masking callouts and compares them with the order notes. Credit row: I. Inspection of design data, closed at CDR on the product baseline (docs/process/04-verification-and-validation.md sections 5.1 item 4 and 5.2); the receipt inspection named in the verification_note, where there is one, is recorded as data in the same report. Tools: FreeCAD 1.1.3 per tools/toolchain.lock.md Safety: not applicable (design data only). Environment: not applicable.

**Procedure.**

1. Read the material callout on the drawing and in the order notes and confirm an aluminum alloy machined by CNC.
2. Read the finish callout and confirm anodizing.
3. Confirm masking callouts on the drawing for every chassis-ground contact area and every connector contact area (antenna jack boss and counterpoise attachment, key and headphone jack bosses, PCB ground-contact standoffs).
4. Confirm that the order notes repeat the material, the anodize and every masking callout.
5. At receipt, check continuity with the multimeter from each masked area to the antenna-jack shell and record it as data.
6. Record the inspected file paths, their commit and tool versions in the report.
7. On any finding against the criteria, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if the drawing and order notes specify a CNC-machined aluminum enclosure, anodized, with every chassis-ground and connector contact area called out as masked (left conductive); otherwise Fail. The receipt continuity readings are recorded as data.

**Expected artifacts.**

- `enclosure-drawing-callouts.png` (plot): Drawing excerpt with material, finish and masking callouts
- `cnc-order-notes.txt` (other): Order notes of the CNC release package

### TC-SYS-076: Enclosure mechanical safety by scripted CAD checks: edge break, knob clearance and cell-cover pinch gaps

| Field | Value |
|---|---|
| Requirements | REQ-SYS-110, REQ-SYS-111, REQ-SYS-168 |
| Method / class | Analysis / Simulation |
| Status | Draft |
| Automation | `hardware/enclosure/checks/enclosure_safety_check.py` |

**Setup.** Article: design data at tag baseline/cdr: enclosure and knob STEP models and the cell-cover mechanism model. Configuration: hardware/enclosure/checks/enclosure_safety_check.py (planned) runs headlessly in the FreeCAD command-line interpreter: it measures the chamfer or fillet size on every external and cutout edge, the radial clearance between each knob and the panel, and the gap between the cell cover and the body at 1 degree steps through the cover travel. Credit row: A. Analysis closed by Simulation on the CDR design data and confirmed at SAR by the physical configuration audit of every analyzed value (docs/process/04-verification-and-validation.md sections 5.1 item 5 and 5.2); the post-build readings named in the verification_note are supporting data only. TBR values: the acceptance criteria use the values of REQ-SYS-168 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Hazard controls exercised: HZ-013 (from the cited requirements; docs/safety/hazards.json). Risk acceptance: the verification_note of REQ-SYS-110 (RSK-018), REQ-SYS-111 (RSK-018), REQ-SYS-168 (RSK-018) begins 'Analysis accepted per RSK-NNN'; that risk carries the hazard control not closed by Test (docs/process/04-verification-and-validation.md section 3, rule 7.3.6). Tools: FreeCAD 1.1.3 command-line interpreter and Python per tools/toolchain.lock.md Safety: not applicable (design data only). Environment: not applicable.

**Procedure.**

1. Confirm that the STEP files are those of the CDR release package (checker prints their hashes).
2. Run the edge-break check and save the list of every external and cutout edge with its break size.
3. Run the knob clearance check and save the minimum radial clearance per knob.
4. Run the cover sweep and save the gap versus travel at every closing gap.
5. Record tool versions, the design-data tag and the commit of every deck, model, script and checker in the report.
6. On any assertion or checker failure, or any difference between the analyzed values and the design data, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if every external and cutout edge has a chamfer or fillet of at least 0.5 mm (REQ-SYS-110), every knob has at least 1.0 mm radial clearance to the panel (REQ-SYS-111), and every closing gap of the cell cover stays below 4 mm or above 25 mm throughout its travel (REQ-SYS-168); otherwise Fail, reported per requirement.

**Expected artifacts.**

- `edge-break.csv` (csv): Edge id, location and break size
- `knob-clearance.csv` (csv): Knob and minimum radial clearance
- `cover-gap-sweep.csv` (csv): Cover angle and gap per closing gap

### TC-SYS-077: PA junction and hand-hold surface temperature from the thermal resistance chain

| Field | Value |
|---|---|
| Requirements | REQ-SYS-112, REQ-SYS-113 |
| Method / class | Analysis / Simulation |
| Status | Draft |
| Automation | `tools/budgets/thermal_budget.py` |

**Setup.** Article: design data at tag baseline/cdr: docs/design/analysis/thermal-budget.md inputs: PA device junction-to-case resistance (TS-003), dissipation at the 5 W step from the PA simulation, the PCB via field and thermal pad, the enclosure boss and the enclosure-to-ambient path. Configuration: tools/budgets/thermal_budget.py (planned) computes the steady-state junction temperature at 45 C ambient for continuous key-down at 5 W and the transient surface temperature of the hand-hold areas after 5 min of continuous key-down at 25 C ambient. Credit row: A. Analysis closed by Simulation on the CDR design data and confirmed at SAR by the physical configuration audit of every analyzed value (docs/process/04-verification-and-validation.md sections 5.1 item 5 and 5.2); the post-build readings named in the verification_note are supporting data only. TBR values: the acceptance criteria use the values of REQ-SYS-112, REQ-SYS-113 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Hazard controls exercised: HZ-003 (from the cited requirements; docs/safety/hazards.json). Risk acceptance: the verification_note of REQ-SYS-112 (RSK-006), REQ-SYS-113 (RSK-006) begins 'Analysis accepted per RSK-NNN'; that risk carries the hazard control not closed by Test (docs/process/04-verification-and-validation.md section 3, rule 7.3.6). Tools: Python per tools/toolchain.lock.md Safety: not applicable (design data only). Environment: not applicable.

**Procedure.**

1. Confirm that the budget inputs equal the CDR data (script prints the diff; an empty diff is required).
2. Compute the steady-state PA junction temperature at 45 C ambient, continuous key-down at the 5 W step, worst-case pack voltage.
3. Compute the hand-hold surface temperature after 5 min of continuous key-down at 5 W in 25 C ambient from the enclosure thermal capacity and resistances.
4. Repeat the computation with every toleranced input at its worst-case corner (checker option --corners) and record the worst case.
5. Record tool versions, the design-data tag and the commit of every deck, model, script and checker in the report.
6. On any assertion or checker failure, or any difference between the analyzed values and the design data, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if the PA junction is at or below 110 C (REQ-SYS-112) and the hand-hold surfaces are at most 48 C (REQ-SYS-113) at the worst-case corner; otherwise Fail, reported per requirement.

**Expected artifacts.**

- `thermal-budget.csv` (csv): Thermal chain terms and results per corner

### TC-SYS-078: Operating and storage temperature ranges from every part rating

| Field | Value |
|---|---|
| Requirements | REQ-SYS-114, REQ-SYS-115 |
| Method / class | Analysis / Simulation |
| Status | Draft |
| Automation | `tools/budgets/part_rating_check.py` |

**Setup.** Article: design data at tag baseline/cdr: the CDR BOM with the operating and storage temperature rating of every part, the frequency error budget and the cell datasheet. Configuration: tools/budgets/part_rating_check.py (planned) compares each part's rated operating range with -10 C to +45 C (plus the part's own rise where the thermal budget gives one) and its storage range with -20 C to +60 C. Credit row: A. Analysis closed by Simulation on the CDR design data and confirmed at SAR by the physical configuration audit of every analyzed value (docs/process/04-verification-and-validation.md sections 5.1 item 5 and 5.2); the post-build readings named in the verification_note are supporting data only. TBR values: the acceptance criteria use the values of REQ-SYS-114, REQ-SYS-115 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Tools: Python per tools/toolchain.lock.md Safety: not applicable (design data only). Environment: not applicable.

**Procedure.**

1. Confirm that the BOM is the CDR BOM (script prints its hash).
2. Run tools/budgets/part_rating_check.py and save the table of every part with its ratings and margins.
3. Confirm that the frequency error budget case covers -10 C to +45 C and that the display, encoder and battery-holder ratings cover the range.
4. Confirm that the storage check excludes the cells (removed in storage) and includes every other part.
5. Record tool versions, the design-data tag and the commit of every deck, model, script and checker in the report.
6. On any assertion or checker failure, or any difference between the analyzed values and the design data, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if every part's operating rating covers -10 C to +45 C ambient plus its own rise (REQ-SYS-114) and every part except the removed cells has a storage rating covering -20 C to +60 C (REQ-SYS-115); otherwise Fail, reported per requirement.

**Expected artifacts.**

- `part-ratings.csv` (csv): Part, operating range, storage range and margins

### TC-SYS-079: Requirements met after a 1.0 m drop onto a hard floor on each face with the antenna fitted

| Field | Value |
|---|---|
| Requirements | REQ-SYS-116 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | none (manual) |

**Setup.** Article: CWHT-A-001 in its enclosure, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: one unit with cells and the reference antenna fitted, switched off; a hard floor (concrete or tile over concrete); drop height measured from the lowest point of the unit; after the drops the acceptance test set of docs/process/04-verification-and-validation.md section 11 (TC-ATP cases) is run. Credit row: T-HW. Test of a system requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the campaign (section 13) and witnessed by the owner; the pre-build Simulation, HostUnit and Emulation evidence named in each requirement's verification_note is supporting only and is not part of this case. TBR values: the acceptance criteria use the values of REQ-SYS-116 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: unit switched off; drop zone clear of people; cells inspected for dents or leakage after each drop and a damaged cell ends the case and is disposed of per the handbook. Environment: room temperature 18 to 28 C; hard floor.

**Procedure.**

1. Run the acceptance test set on the unit before the drops and file its reports.
2. Drop the unit from 1.0 m onto each of its six faces, one drop per face.
3. After each drop inspect the enclosure, antenna, jacks, knobs and cells and photograph any damage.
4. Run the acceptance test set again.
5. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
6. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if after the six 1.0 m drops the unit passes every case of the acceptance test set it passed before the drops and no cell is damaged; otherwise Fail.

**Instruments and fixtures.**

- tinySA Ultra spectrum analyzer (ADR-021) through the calibrated 30 to 40 dB attenuator rated 10 W or more, attenuator S21 measured on the NanoVNA in the same session; level accuracy per its TV record
- Diode RF probe (1N5711 or equivalent, printed housing) on a BNC T at the dummy load, characterized by TC-SYS-010, read on the multimeter DC voltage range
- Multimeter, DC voltage and DC current ranges, accuracy per datasheet copied into the report (OQ-VV-003)
- Pico-based logic capture (second Pico 2 with sigrok-pico firmware read by sigrok-cli; planned, ADR-009), 3.3 V inputs, 1 MS/s unless a step states otherwise
- 50 ohm BNC dummy load with SMA adapter, power rating recorded in the report
- Owner's straight key and iambic paddle, 3.5 mm TRS plugs (SI-034)
- Steel rule or tape for the 1.0 m height

**Expected artifacts.**

- `drop-inspection.jpg` (photo): Photographs after each drop
- `drop-atp-comparison.csv` (csv): ATP case, result before, result after

### TC-SYS-080: Requirements met after 10 min of IEC 60529 IPX2 dripping water with plugs inserted

| Field | Value |
|---|---|
| Requirements | REQ-SYS-117 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | none (manual) |

**Setup.** Article: CWHT-A-001 in its enclosure, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: one unit upright with key and headphone plugs inserted and the antenna fitted, switched off; a drip tray with a calibrated drip rate of 3 mm/min (docs/vv/fixtures/drip-tray.md, planned); the unit tilted 15 degrees in each of four directions for 2.5 min each (IPX2); then dried and the acceptance test set run. Credit row: T-HW. Test of a system requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the campaign (section 13) and witnessed by the owner; the pre-build Simulation, HostUnit and Emulation evidence named in each requirement's verification_note is supporting only and is not part of this case. TBR values: the acceptance criteria use the values of REQ-SYS-117 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: unit switched off with the cells fitted but no charging; water kept away from the bench supply and instruments. Environment: room temperature 18 to 28 C.

**Procedure.**

1. Run the acceptance test set before the exposure.
2. Measure the drip rate by collecting water for 1 min in a container of known area.
3. Expose the unit for 2.5 min at each of the four 15 degree tilts.
4. Wipe the exterior, open the enclosure, photograph any water inside, and dry for 24 h.
5. Run the acceptance test set again.
6. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
7. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if the drip rate is 3 mm/min +/-0.5 mm/min, the exposure lasts 10 min, and afterwards the unit passes every acceptance case it passed before; otherwise Fail. Water found inside is recorded for the design and is not by itself a failure.

**Instruments and fixtures.**

- tinySA Ultra spectrum analyzer (ADR-021) through the calibrated 30 to 40 dB attenuator rated 10 W or more, attenuator S21 measured on the NanoVNA in the same session; level accuracy per its TV record
- Diode RF probe (1N5711 or equivalent, printed housing) on a BNC T at the dummy load, characterized by TC-SYS-010, read on the multimeter DC voltage range
- Multimeter, DC voltage and DC current ranges, accuracy per datasheet copied into the report (OQ-VV-003)
- Pico-based logic capture (second Pico 2 with sigrok-pico firmware read by sigrok-cli; planned, ADR-009), 3.3 V inputs, 1 MS/s unless a step states otherwise
- 50 ohm BNC dummy load with SMA adapter, power rating recorded in the report
- Owner's straight key and iambic paddle, 3.5 mm TRS plugs (SI-034)
- Drip tray fixture (planned)

**Expected artifacts.**

- `rain-exposure.jpg` (photo): Photographs of the setup and the interior after exposure
- `rain-atp-comparison.csv` (csv): ATP case, result before, result after

### TC-SYS-081: PA over-temperature inhibit and PA temperature-sensor fault response

| Field | Value |
|---|---|
| Requirements | REQ-SYS-118, REQ-SYS-155 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | `tools/analyze_logic_capture.py` |

**Setup.** Article: CWHT-A-001, enclosure lid off for test-point access, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: PA sensor at its test pad driven by the NTC substitution fixture (80, 82, 84, 86, 88 and 90 C equivalents, open and short); fixture marker, PA_EN and UART telemetry on the logic capture; dummy load; 1 W step. Credit row: T-HW. Test of a system requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the campaign (section 13) and witnessed by the owner; the pre-build Simulation, HostUnit and Emulation evidence named in each requirement's verification_note is supporting only and is not part of this case. TBR values: the acceptance criteria use the values of REQ-SYS-118, REQ-SYS-155 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Hazard controls exercised: HZ-003 (from the cited requirements; docs/safety/hazards.json). Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: every transmission goes into the 50 ohm dummy load or the calibrated power attenuator, connected before power-on, never into an open antenna port; key-down duty kept within the load rating recorded in the report; anyone other than the operator stays 0.6 m or more from the unit and load while keying and 1.0 m or more during a tune carrier (NGO-019); the bench supply current limit is set before each power-on; antistatic wrist strap while the lid is off; the PA area is not touched after key-down runs. Environment: room temperature 18 to 28 C; the pack is supplied by the bench supply at 7.4 V +/-0.05 V through the battery terminals unless a step sets another value; dummy load on the antenna port.

**Procedure.**

1. Run the logic-capture reference pulse-train check of this session and record the result (docs/process/04-verification-and-validation.md section 4).
2. Wire the UART telemetry test pad to a logic-capture channel and confirm that the sigrok-cli UART decoder prints the telemetry lines (REQ-SYS-150).
3. With the straight key held, switch the fixture from 80 C to 82 C, then to 84, 86, 88 and 90 C equivalents at 1 s intervals; record PA_EN.
4. Repeat with the paddle dah lever held.
5. Set the 80 C equivalent, key with the straight key, switch directly to the 90 C equivalent; repeat three times.
6. Switch the sensor to open, in Receive and while keyed with the straight key; then to short, in Receive and while keyed with the paddle.
7. Run tools/analyze_logic_capture.py: marker-to-PA_EN-fall and marker-to-Fault-safe telemetry latencies.
8. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
9. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if RF output ceases (PA_EN low) at most 100 ms after the sensor reading crosses 85 C and the trip lies between the 82 C and 88 C equivalents (REQ-SYS-118), and the unit enters Fault-safe at most 100 ms after the sensor is opened or shorted, in Receive and while keyed (REQ-SYS-155); otherwise Fail.

**Instruments and fixtures.**

- Pico-based logic capture (second Pico 2 with sigrok-pico firmware read by sigrok-cli; planned, ADR-009), 3.3 V inputs, 1 MS/s unless a step states otherwise
- NTC substitution fixture: fixed resistors at the temperature equivalents named in the steps, switched in place of the cell or PA sensor at its test pad, the switch's second pole wired to a logic-capture channel as the event marker (docs/vv/fixtures/ntc-substitution.md, planned)
- 50 ohm BNC dummy load with SMA adapter, power rating recorded in the report
- Owner's straight key and iambic paddle, 3.5 mm TRS plugs (SI-034)
- Adjustable bench supply, 0 to 30 V, current limit set per step

**Expected artifacts.**

- `pa-temp-trip.csv` (csv): Equivalent temperature, keying source, PA_EN and latency
- `pa-sensor-fault.csv` (csv): Fault, state, latency to Fault-safe

### TC-SYS-082: Safe state first on reset, panic and latched fault; RF off in reset, bootloader and firmware load; hang recovery within 2 s

| Field | Value |
|---|---|
| Requirements | REQ-SYS-119, REQ-SYS-130, REQ-SYS-131, REQ-SYS-183 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | `tools/analyze_logic_capture.py` |

**Setup.** Article: CWHT-A-001, enclosure lid off for test-point access, running the fault-injection test build of release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (a build flavour of the release commit whose injection commands arrive over the UART test pads from the host serial terminal through the 3.3 V serial adapter, or over USB serial only in steps that expect no carrier, because USB VBUS sets the USB flag and the hardware transmit inhibit of REQ-SYS-092, and which toggles the injection-marker test pad at the instant of each injection); the release image is restored and checked with picotool verify at the end of the case. Configuration: antenna port to the calibrated power attenuator and the tinySA Ultra in zero span; logic capture on the injection-marker pad, the RUN line (the marker of every reset), PA_EN, TX_KEY, the T/R drive, the amplifier enable, the charger enable, the display chip-select, the sidetone PWM line and the UART pad; fault build commands for panic, deliberate hang and latched faults; 1 W step. The keyed steps run with USB disconnected, because USB VBUS inhibits transmit (REQ-SYS-092), and the charging steps run with the switch off, USB applied through the USB breakout and the two-cell simulator absorbing the charge current, because charging is paused while the switch is on (REQ-SYS-093); the keyed steps expose PA off, key up, antenna to receive and audio muted, and the charging steps expose charging disabled, the five safe-state actions of REQ-SYS-130. Credit row: T-HW. Test of a system requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the campaign (section 13) and witnessed by the owner; the pre-build Simulation, HostUnit and Emulation evidence named in each requirement's verification_note is supporting only and is not part of this case. TBR values: the acceptance criteria use the values of REQ-SYS-131 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). RF-off level: the acceptance criteria use -57 dBm, the value of REQ-SYS-183 marked TBR (close by PDR); a change returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2). Hazard controls exercised: HZ-002, HZ-004, HZ-005, HZ-014 (from the cited requirements; docs/safety/hazards.json). Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: every transmission goes into the 50 ohm dummy load or the calibrated power attenuator, connected before power-on, never into an open antenna port; key-down duty kept within the load rating recorded in the report; anyone other than the operator stays 0.6 m or more from the unit and load while keying and 1.0 m or more during a tune carrier (NGO-019); the bench supply current limit is set before each power-on; antistatic wrist strap while the lid is off; the PA area is not touched after key-down runs. Environment: room temperature 18 to 28 C; the pack is supplied by the bench supply at 7.4 V +/-0.05 V through the battery terminals unless a step sets another value; dummy load on the antenna port.

**Procedure.**

1. Run the logic-capture reference pulse-train check of this session and record the result (docs/process/04-verification-and-validation.md section 4).
2. Measure the attenuator and cable S21 on the NanoVNA from 9 kHz (or the NanoVNA lower limit) to 1.5 GHz and save the Touchstone file; run the tinySA Ultra internal calibration-output check; record both.
3. While keyed with the straight key held, pulse RUN low; then while keyed with the paddle dah lever held, pulse RUN again.
4. While keyed with the straight key held, inject a panic; then, keyed with the paddle dah lever held, inject a latched fault (cell-sense disagreement); clear it and acknowledge.
5. Turn the switch off, apply USB through the USB breakout with the two-cell simulator at 3.70 V per cell and confirm charge current on the multimeter; pulse RUN.
6. In Charging, confirm charge current again; inject a panic over USB serial; after recovery inject a latched fault (charger fault); record the charge current after each event; clear the cause and remove USB with the switch off (T25).
7. Hold BOOTSEL and pulse RUN with the straight key closed; hold the bootloader state for 30 s.
8. Copy the release UF2 while the straight key is held closed and capture the whole load.
9. Inject a deliberate hang in Receive; repeat while keyed with the straight key held and while keyed with the paddle.
10. Export the capture and run tools/analyze_logic_capture.py: order of the first edges after each marker, and marker-to-reset times.
11. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
12. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if PA_EN is low, TX_KEY low and no carrier at the set frequency above -57 dBm at the antenna port on the tinySA Ultra (the RF-off level of REQ-SYS-183) throughout the reset, bootloader and firmware-load states (REQ-SYS-119); after every reset, panic and latched fault PA_EN is low, TX_KEY low (key up), the T/R drive at receive, the amplifier enable low (audio muted) and the charger enable low (charging disabled) before the first edge on any other captured output, in the keyed and in the charging steps (REQ-SYS-130); and every hang ends in a reset into SafeState at most 2 s after the hang marker (REQ-SYS-131); otherwise Fail.

**Instruments and fixtures.**

- Pico-based logic capture (second Pico 2 with sigrok-pico firmware read by sigrok-cli; planned, ADR-009), 3.3 V inputs, 1 MS/s unless a step states otherwise
- tinySA Ultra spectrum analyzer (ADR-021) through the calibrated 30 to 40 dB attenuator rated 10 W or more, attenuator S21 measured on the NanoVNA in the same session; level accuracy per its TV record
- NanoVNA, SOL calibration at the cable end used, checked on the dummy load
- Host computer with picotool and a serial terminal per tools/toolchain.lock.md, micro-USB cable
- 3.3 V USB-to-UART serial adapter between the host computer and the UART test pads, so that injection commands reach the unit with its USB port disconnected (docs/vv/fixtures/uart-adapter.md, planned)
- Owner's straight key and iambic paddle, 3.5 mm TRS plugs (SI-034)
- USB power breakout fixture with VBUS routed through the multimeter current range (docs/vv/fixtures/usb-breakout.md, planned)
- Two-cell simulator fixture: the bench supply across the pack terminals with an adjustable, buffered mid-point tap for the cell junction and a parallel sink resistor so that the fixture absorbs charger current (docs/vv/fixtures/cell-simulator.md, planned; characterized before TRR)
- Multimeter, DC voltage and DC current ranges, accuracy per datasheet copied into the report (OQ-VV-003)
- Adjustable bench supply, 0 to 30 V, current limit set per step

**Expected artifacts.**

- `reset-safe-order.csv` (csv): Event, configuration (keyed or charging), first edges in order, marker-to-reset time
- `reset-charge-current.csv` (csv): Charging step, charge current before and after each event
- `reset-safe-capture.sr` (other): Raw logic capture

### TC-SYS-083: RF output only while both the keyer key-down and the separately maintained PA permit are asserted

| Field | Value |
|---|---|
| Requirements | REQ-SYS-120, REQ-SYS-183 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | none (manual) |

**Setup.** Article: CWHT-A-001, enclosure lid off for test-point access, running the fault-injection test build of release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (a build flavour of the release commit whose injection commands arrive over the UART test pads from the host serial terminal through the 3.3 V serial adapter, or over USB serial only in steps that expect no carrier, because USB VBUS sets the USB flag and the hardware transmit inhibit of REQ-SYS-092, and which toggles the injection-marker test pad at the instant of each injection); the release image is restored and checked with picotool verify at the end of the case. Configuration: fault-injection build able to force the keyer key-down alone and the PA permit alone; antenna port to the calibrated power attenuator and the tinySA Ultra in zero span; logic capture on TX_KEY, the PA permit line and PA_EN; 1 W step. Credit row: T-HW. Test of a system requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the campaign (section 13) and witnessed by the owner; the pre-build Simulation, HostUnit and Emulation evidence named in each requirement's verification_note is supporting only and is not part of this case. RF-off level: the acceptance criteria use -57 dBm, the value of REQ-SYS-183 marked TBR (close by PDR); a change returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2). Hazard controls exercised: HZ-004 (from the cited requirements; docs/safety/hazards.json). Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: every transmission goes into the 50 ohm dummy load or the calibrated power attenuator, connected before power-on, never into an open antenna port; key-down duty kept within the load rating recorded in the report; anyone other than the operator stays 0.6 m or more from the unit and load while keying and 1.0 m or more during a tune carrier (NGO-019); the bench supply current limit is set before each power-on; antistatic wrist strap while the lid is off; the PA area is not touched after key-down runs. Environment: room temperature 18 to 28 C; the pack is supplied by the bench supply at 7.4 V +/-0.05 V through the battery terminals unless a step sets another value; dummy load on the antenna port.

**Procedure.**

1. Run the logic-capture reference pulse-train check of this session and record the result (docs/process/04-verification-and-validation.md section 4).
2. Measure the attenuator and cable S21 on the NanoVNA from 9 kHz (or the NanoVNA lower limit) to 1.5 GHz and save the Touchstone file; run the tinySA Ultra internal calibration-output check; record both.
3. Force the keyer key-down alone (permit withheld) for 3 s; record RF and PA_EN.
4. Force the PA permit alone (key up) for 3 s; record RF and PA_EN.
5. Close the straight key normally for 3 s (both asserted), then the paddle dit lever for 3 s; record RF and PA_EN.
6. Repeat each forced condition five times.
7. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
8. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if with either condition forced alone PA_EN stays low and no carrier at the set frequency above -57 dBm at the antenna port on the tinySA Ultra (the RF-off level of REQ-SYS-183) in every repetition, and RF is present only while both conditions are asserted; otherwise Fail.

**Instruments and fixtures.**

- Pico-based logic capture (second Pico 2 with sigrok-pico firmware read by sigrok-cli; planned, ADR-009), 3.3 V inputs, 1 MS/s unless a step states otherwise
- Host computer with picotool and a serial terminal per tools/toolchain.lock.md, micro-USB cable
- 3.3 V USB-to-UART serial adapter between the host computer and the UART test pads, so that injection commands reach the unit with its USB port disconnected (docs/vv/fixtures/uart-adapter.md, planned)
- tinySA Ultra spectrum analyzer (ADR-021) through the calibrated 30 to 40 dB attenuator rated 10 W or more, attenuator S21 measured on the NanoVNA in the same session; level accuracy per its TV record
- NanoVNA, SOL calibration at the cable end used, checked on the dummy load
- Owner's straight key and iambic paddle, 3.5 mm TRS plugs (SI-034)
- Adjustable bench supply, 0 to 30 V, current limit set per step

**Expected artifacts.**

- `two-conditions.csv` (csv): Condition, repetition, PA_EN and RF level

### TC-SYS-084: RF exposure evaluation on record and reference antenna gain

| Field | Value |
|---|---|
| Requirements | REQ-SYS-121, REQ-SYS-172 |
| Method / class | Analysis / Simulation |
| Status | Draft |
| Automation | `tools/budgets/rf_exposure.py` |

**Setup.** Article: design data at tag baseline/cdr: docs/design/analysis/rf-exposure-evaluation.md (controlled document), the reference antenna datasheets and the literature data of docs/research/rf-exposure-evaluation.md F4, updated at TRR with the Bench power per step. Configuration: tools/budgets/rf_exposure.py (planned) recomputes the MPE distances per step and mode and the SAR analogy from the evaluation's inputs; the reviewer checks the evaluation against 47 CFR 1.1307(b), 2.1091 and 2.1093 (eCFR 2026-09-23). Credit row: A. Analysis closed by Simulation on the CDR design data and confirmed at SAR by the physical configuration audit of every analyzed value (docs/process/04-verification-and-validation.md sections 5.1 item 5 and 5.2); the post-build readings named in the verification_note are supporting data only. TBR values: the acceptance criteria use the values of REQ-SYS-172 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Hazard controls exercised: HZ-001, HZ-006 (from the cited requirements; docs/safety/hazards.json). Risk acceptance: the verification_note of REQ-SYS-121 (RSK-016), REQ-SYS-172 (RSK-016) begins 'Analysis accepted per RSK-NNN'; that risk carries the hazard control not closed by Test (docs/process/04-verification-and-validation.md section 3, rule 7.3.6). Tools: Python per tools/toolchain.lock.md Safety: not applicable (design data only). Environment: not applicable.

**Procedure.**

1. Confirm that the evaluation exists as a controlled document with a revision recorded before the first on-air transmission.
2. Run tools/budgets/rf_exposure.py with the evaluation inputs and confirm that it reproduces every distance and SAR fraction in the evaluation tables.
3. Confirm that the evaluation addresses 1.1307(b), 2.1091 and 2.1093 with the occupational tier for operators and the general-population tier for everyone else (SI-030), each power step, tune, time averaging and the reference antennas.
4. Read the gain of each reference antenna from its published data and the literature data, from 144 MHz to 148 MHz.
5. At TRR, replace the nominal step powers with the Bench measured powers and re-run the script.
6. Record tool versions, the design-data tag and the commit of every deck, model, script and checker in the report.
7. On any assertion or checker failure, or any difference between the analyzed values and the design data, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if the RF exposure evaluation per 47 CFR 1.1307(b), 2.1091 and 2.1093 is on record before the first on-air transmission, the script reproduces its values, and every reference antenna has a published or literature gain of at most 0 dBd from 144 MHz to 148 MHz; otherwise Fail, reported per requirement.

**Expected artifacts.**

- `rf-exposure-recompute.csv` (csv): Step, mode, distance and SAR fraction recomputed
- `antenna-gain-table.csv` (csv): Antenna, frequency and gain in dBd with source

### TC-SYS-085: Operations handbook safety content checked against every documentation and operator-procedure control

| Field | Value |
|---|---|
| Requirements | REQ-SYS-122 |
| Method / class | Analysis / Simulation |
| Status | Draft |
| Automation | `tools/check_handbook_controls.py` |

**Setup.** Article: design data at tag baseline/cdr: docs/ops/operations-handbook.md and docs/safety/hazards.json at the same tag. Configuration: tools/check_handbook_controls.py (planned) lists every hazard control whose type is Documentation or Operator procedure; an independent reviewer agent maps each to the handbook section that carries it. Credit row: A. Analysis closed by Simulation on the CDR design data and confirmed at SAR by the physical configuration audit of every analyzed value (docs/process/04-verification-and-validation.md sections 5.1 item 5 and 5.2); the post-build readings named in the verification_note are supporting data only. Hazard controls exercised: HZ-001, HZ-002, HZ-003, HZ-004, HZ-005, HZ-006, HZ-007, HZ-009, HZ-011, HZ-012, HZ-013 (from the cited requirements; docs/safety/hazards.json). Risk acceptance: the verification_note of REQ-SYS-122 (RSK-016) begins 'Analysis accepted per RSK-NNN'; that risk carries the hazard control not closed by Test (docs/process/04-verification-and-validation.md section 3, rule 7.3.6). Tools: Python per tools/toolchain.lock.md Safety: not applicable (design data only). Environment: not applicable.

**Procedure.**

1. Run tools/check_handbook_controls.py and save the list of Documentation and Operator procedure controls with their hazard ids.
2. For each control, the independent reviewer records the handbook section and quotes the instruction that implements it.
3. Confirm that each quoted instruction states the control completely (distances, times, steps and warnings as the control states them).
4. Confirm that a printed copy is in the ship list of each unit's as-built record.
5. Record tool versions, the design-data tag and the commit of every deck, model, script and checker in the report.
6. On any assertion or checker failure, or any difference between the analyzed values and the design data, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if every Documentation and Operator procedure control of docs/safety/hazards.json is carried completely by a named handbook section and the printed handbook is in each unit's ship list; otherwise Fail.

**Expected artifacts.**

- `handbook-control-map.csv` (csv): Hazard, control, handbook section and quoted instruction

### TC-SYS-086: Enclosure legend artwork and engraving callout against the required legend

| Field | Value |
|---|---|
| Requirements | REQ-SYS-124 |
| Method / class | Analysis / Simulation |
| Status | Draft |
| Automation | none (manual) |

**Setup.** Article: design data at tag baseline/cdr: the engraving artwork and the drawing callout in the CNC release package. Configuration: Reviewer compares the artwork text with the required legend word for word and reads the process and depth callout. Credit row: A. Analysis closed by Simulation on the CDR design data and confirmed at SAR by the physical configuration audit of every analyzed value (docs/process/04-verification-and-validation.md sections 5.1 item 5 and 5.2); the post-build readings named in the verification_note are supporting data only. Hazard controls exercised: HZ-001, HZ-006 (from the cited requirements; docs/safety/hazards.json). Risk acceptance: the verification_note of REQ-SYS-124 (RSK-016) begins 'Analysis accepted per RSK-NNN'; that risk carries the hazard control not closed by Test (docs/process/04-verification-and-validation.md section 3, rule 7.3.6). Tools: FreeCAD 1.1.3 per tools/toolchain.lock.md Safety: not applicable (design data only). Environment: not applicable.

**Procedure.**

1. Extract the artwork text and compare it with the legend: amateur transmitter, 144-148 MHz, 5 W nominal, licensed operators only, handbook exposure section.
2. Confirm that the callout specifies engraving or machining into the enclosure metal (not a label, print or ink) with a stated depth.
3. Confirm that the legend location is not covered by a knob, jack, cover or the antenna when assembled.
4. Record tool versions, the design-data tag and the commit of every deck, model, script and checker in the report.
5. On any assertion or checker failure, or any difference between the analyzed values and the design data, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if the artwork carries every element of the legend, the callout marks it into the enclosure metal with a stated depth, and it is visible on the assembled unit; otherwise Fail.

**Expected artifacts.**

- `legend-artwork.png` (plot): Artwork render with the callout

### TC-SYS-087: Build quantity cap in the release package and the unit serial register

| Field | Value |
|---|---|
| Requirements | REQ-SYS-125 |
| Method / class | Inspection / Inspection |
| Status | Draft |
| Automation | none (manual) |

**Setup.** Article: design data at tag baseline/cdr: CDR release package under hardware/releases/ (PCBWay fabrication, assembly and CNC order quantities) and the unit serial register of docs/vv/adp/. Configuration: Reviewer reads the ordered quantities and the serial register; at SAR the configuration audit repeats the serial count. Credit row: I. Inspection of design data, closed at CDR on the product baseline (docs/process/04-verification-and-validation.md sections 5.1 item 4 and 5.2); the receipt inspection named in the verification_note, where there is one, is recorded as data in the same report. Tools: none beyond a text viewer Safety: not applicable (design data only). Environment: not applicable.

**Procedure.**

1. Read the assembly and CNC enclosure order quantities in the release package.
2. Read the unit serial register and count the CWHT-A-NNN serials issued.
3. Confirm that no sale listing, price list or marketing text for the unit exists in the repository.
4. Record the inspected file paths, their commit and tool versions in the report.
5. On any finding against the criteria, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if the release package orders parts for at most five complete units, the serial register issues at most five serials CWHT-A-001 to CWHT-A-005, and no marketing material for the unit exists; otherwise Fail.

**Expected artifacts.**

- `quantity-inspection.txt` (report): Order quantities, serial list and search result for marketing material

### TC-SYS-088: Firmware platform, host-testable layering and single interrupt priority

| Field | Value |
|---|---|
| Requirements | REQ-SYS-127, REQ-SYS-128, REQ-SYS-129 |
| Method / class | Inspection / Inspection |
| Status | Draft |
| Automation | `tools/check_nvic_priority.py` |

**Setup.** Article: design data at tag baseline/cdr: the firmware workspace in firmware/ at the release tag named in the VDD, its Cargo.lock, the rustos revision recorded in the VDD and the CI host build log of that tag. Configuration: tools/check_nvic_priority.py (planned) lists every NVIC priority write in cwht-app and the rustos board crate with the value written; cargo tree lists the dependencies of cwht-core. Credit row: I. Inspection of design data, closed at CDR on the product baseline (docs/process/04-verification-and-validation.md sections 5.1 item 4 and 5.2); the receipt inspection named in the verification_note, where there is one, is recorded as data in the same report. Tools: Rust toolchain, cargo and Python per tools/toolchain.lock.md Safety: not applicable (design data only). Environment: not applicable.

**Procedure.**

1. Confirm that every firmware crate in the workspace manifests is Rust and that the target binary depends on the rustos crates at the revision named in the VDD and Cargo.lock.
2. Confirm that cwht-core carries #![no_std] and #![forbid(unsafe_code)] at its crate root.
3. Run cargo tree -p cwht-core and confirm that its only non-dev dependencies are the rustos api crate and crates that are themselves no_std without hardware access.
4. Confirm from the CI host build log of the tag that cwht-core built and its tests ran unmodified on a macOS or Linux host against the rustos api traits.
5. Run tools/check_nvic_priority.py on cwht-app and the rustos board crate and confirm that every enabled interrupt is assigned the same NVIC priority value and that no code changes a priority at run time.
6. Record the inspected file paths, their commit and tool versions in the report.
7. On any finding against the criteria, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if the firmware is Rust on the rustos revision named in the VDD, cwht-core is no_std with forbid(unsafe_code) and depends only on the rustos api traits, the host build and test run of the tag succeeded unmodified on macOS or Linux, and every interrupt handler runs at one NVIC priority level; otherwise Fail.

**Expected artifacts.**

- `cargo-tree-cwht-core.txt` (log): cargo tree output for cwht-core
- `nvic-priority-writes.txt` (report): Checker list of NVIC priority writes with values
- `ci-host-build.log.txt` (log): CI host build and test log of the tag

### TC-SYS-089: Fault-safe on a failed firmware-image integrity check, and defaults for corrupt or out-of-range settings

| Field | Value |
|---|---|
| Requirements | REQ-SYS-132, REQ-SYS-134 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | none (manual) |

**Setup.** Article: CWHT-A-001, enclosure lid off for test-point access, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: images prepared from the release: one with a flipped byte, one truncated and one for the wrong target, each loaded with picotool; configuration images with copy A corrupt, copy B corrupt, both corrupt and each field out of range, written through the test interface; dummy load; logic capture on PA_EN. Run at each unit's ATP. Credit row: T-HW. Test of a system requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the campaign (section 13) and witnessed by the owner; the pre-build Simulation, HostUnit and Emulation evidence named in each requirement's verification_note is supporting only and is not part of this case. Hazard controls exercised: HZ-014 (from the cited requirements; docs/safety/hazards.json). Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: every transmission goes into the 50 ohm dummy load or the calibrated power attenuator, connected before power-on, never into an open antenna port; key-down duty kept within the load rating recorded in the report; anyone other than the operator stays 0.6 m or more from the unit and load while keying and 1.0 m or more during a tune carrier (NGO-019); the bench supply current limit is set before each power-on; antistatic wrist strap while the lid is off; the PA area is not touched after key-down runs. Environment: room temperature 18 to 28 C; the pack is supplied by the bench supply at 7.4 V +/-0.05 V through the battery terminals unless a step sets another value; dummy load on the antenna port.

**Procedure.**

1. Run the logic-capture reference pulse-train check of this session and record the result (docs/process/04-verification-and-validation.md section 4).
2. Load the flipped-byte image; power on; read the display; close the straight key and the paddle for 1 s each; record PA_EN.
3. Repeat with the truncated and the wrong-target images.
4. Restore the release image and check it with picotool verify.
5. Write the configuration with copy A corrupt; power on; read every setting.
6. Repeat with copy B corrupt, both corrupt, and each field out of range in turn.
7. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
8. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if with each bad image the unit is in Fault-safe with the image fault shown and PA_EN stays low for every closure (REQ-SYS-132), and with each corrupt or out-of-range configuration every affected setting loads as its default while the valid settings keep their values (REQ-SYS-134); otherwise Fail.

**Instruments and fixtures.**

- Pico-based logic capture (second Pico 2 with sigrok-pico firmware read by sigrok-cli; planned, ADR-009), 3.3 V inputs, 1 MS/s unless a step states otherwise
- Host computer with picotool and a serial terminal per tools/toolchain.lock.md, micro-USB cable
- 50 ohm BNC dummy load with SMA adapter, power rating recorded in the report
- Owner's straight key and iambic paddle, 3.5 mm TRS plugs (SI-034)
- Adjustable bench supply, 0 to 30 V, current limit set per step

**Expected artifacts.**

- `integrity.csv` (csv): Image or configuration case, result, PA_EN, settings read

### TC-SYS-090: Firmware update through the micro-USB receptacle with the cells removed

| Field | Value |
|---|---|
| Requirements | REQ-SYS-133 |
| Method / class | Demonstration / Bench |
| Status | Draft |
| Automation | none (manual) |

**Setup.** Article: CWHT-A-001 in its enclosure, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: cells removed; micro-USB to the host computer; release UF2 from the release package. Credit row: D. Demonstration by the owner on the delivered unit (docs/process/04-verification-and-validation.md section 5.2): pass or fail is observed without detailed data gathering and each observation is photographed or logged. Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: cells removed; no transmission possible. Environment: room temperature 18 to 28 C.

**Procedure.**

1. Remove the cells; hold BOOTSEL and connect USB; confirm the bootloader drive appears.
2. Copy the release UF2; wait for the reset.
3. Run picotool verify against the release image and record the result.
4. Refit the cells, power on and read the boot banner version.
5. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
6. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if the image loads with the cells removed, picotool verify reports a match, and the boot banner shows the released version; otherwise Fail.

**Instruments and fixtures.**

- Host computer with picotool and a serial terminal per tools/toolchain.lock.md, micro-USB cable

**Expected artifacts.**

- `fwupdate.log.txt` (serial_output): picotool verify output and boot banner

### TC-SYS-091: Assembly split: every surface-mount part placed by PCBWay, only through-hole parts and exposed-pad modules for the owner

| Field | Value |
|---|---|
| Requirements | REQ-SYS-137, REQ-SYS-138 |
| Method / class | Analysis / Simulation |
| Status | Draft |
| Automation | `tools/check_assembly_split.py` |

**Setup.** Article: design data at tag baseline/cdr: BOM with the package column, the CPL exported by kicad-cli with the PCBWay flags of tools/toolchain.lock.md, and hardware/releases/HW-MB-revA-n/cwht-MB-revA-hand-assembly.csv. Configuration: tools/check_assembly_split.py (planned) classifies each BOM line by package and checks it against the CPL and the hand-assembly file. Credit row: A. Analysis closed by Simulation on the CDR design data and confirmed at SAR by the physical configuration audit of every analyzed value (docs/process/04-verification-and-validation.md sections 5.1 item 5 and 5.2); the post-build readings named in the verification_note are supporting data only. Hazard controls exercised: HZ-015 (from the cited requirements; docs/safety/hazards.json). Risk acceptance: the verification_note of REQ-SYS-137 (RSK-004), REQ-SYS-138 (RSK-004) begins 'Analysis accepted per RSK-NNN'; that risk carries the hazard control not closed by Test (docs/process/04-verification-and-validation.md section 3, rule 7.3.6). Tools: kicad-cli at its lock path and Python per tools/toolchain.lock.md Safety: not applicable (design data only). Environment: not applicable.

**Procedure.**

1. Export the CPL with kicad-cli and the PCBWay flags.
2. Run tools/check_assembly_split.py and save the classification of every BOM line.
3. Confirm that every surface-mount line appears in the CPL for PCBWay placement and not in the hand-assembly file.
4. Confirm that every hand-assembly line is a through-hole part or an exposed-pad module (Pico 2 castellations, holders, jacks, encoders).
5. Record tool versions, the design-data tag and the commit of every deck, model, script and checker in the report.
6. On any assertion or checker failure, or any difference between the analyzed values and the design data, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if every surface-mount part is in the PCBWay CPL (REQ-SYS-137) and the hand-assembly file holds only through-hole parts and exposed-pad modules (REQ-SYS-138); otherwise Fail, reported per requirement.

**Expected artifacts.**

- `assembly-split.csv` (csv): BOM line, package, CPL presence and hand-assembly presence

### TC-SYS-092: Circuit board stack-up, PCBWay DRC and probe test points

| Field | Value |
|---|---|
| Requirements | REQ-SYS-139, REQ-SYS-142 |
| Method / class | Inspection / Inspection |
| Status | Draft |
| Automation | `hardware/kicad/checks/run_drc.py` |

**Setup.** Article: design data at tag baseline/cdr: KiCad PCB file, board setup (stack-up), fabrication notes and the PCBWay standard-service rule set used for DRC. Configuration: kicad-cli pcb drc with the PCBWay rule set, severity all, JSON report; the schematic and layout are searched for the test-point footprints of the listed signals. Credit row: I. Inspection of design data, closed at CDR on the product baseline (docs/process/04-verification-and-validation.md sections 5.1 item 4 and 5.2); the receipt inspection named in the verification_note, where there is one, is recorded as data in the same report. TBR values: the acceptance criteria use the values of REQ-SYS-139 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Tools: kicad-cli at its lock path /Applications/KiCad/KiCad.app/Contents/MacOS/kicad-cli and Python per tools/toolchain.lock.md Safety: not applicable (design data only). Environment: not applicable.

**Procedure.**

1. Confirm in the board setup and the fabrication notes a 4-layer stack-up and a finished thickness of 1.0 mm.
2. Run kicad-cli pcb drc with the PCBWay standard-service rule set and save the JSON report.
3. Confirm that the DRC report lists zero errors and zero unwaived warnings; list any waiver with its rationale.
4. Confirm in the schematic and layout a probe test point on each of: key tip input, key ring input, keyer output, TX_KEY, T/R drive, PA_EN, envelope drive and UART telemetry transmit.
5. Confirm that each test point is on an outer layer and reachable with the enclosure lid off.
6. Record the inspected file paths, their commit and tool versions in the report.
7. On any finding against the criteria, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if the board is 4 layers of 1.0 mm finished thickness, DRC against the PCBWay standard-service rule set reports zero errors and zero unwaived warnings, and each of the eight listed signals has a reachable probe test point; otherwise Fail.

**Expected artifacts.**

- `drc-report.json` (report): kicad-cli DRC report with the PCBWay rule set
- `test-point-list.csv` (csv): Signal, test-point reference, layer and position

### TC-SYS-093: Parts sourcing: distributor stock for turnkey parts and the PA, dated quotes for owner-procured parts

| Field | Value |
|---|---|
| Requirements | REQ-SYS-140, REQ-SYS-178 |
| Method / class | Inspection / Inspection |
| Status | Draft |
| Automation | `tools/check_bom.py` |

**Setup.** Article: design data at tag baseline/cdr: BOM with distributor columns, the hand-assembly file cwht-MB-revA-hand-assembly.csv and the stock and quote snapshots saved in the CDR release package. Configuration: tools/check_bom.py --sourcing (planned) joins the BOM with the saved stock snapshots and flags any line without a timestamped stock record or quote. Credit row: I. Inspection of design data, closed at CDR on the product baseline (docs/process/04-verification-and-validation.md sections 5.1 item 4 and 5.2); the receipt inspection named in the verification_note, where there is one, is recorded as data in the same report. Tools: Python per tools/toolchain.lock.md Safety: not applicable (design data only). Environment: not applicable.

**Procedure.**

1. Run tools/check_bom.py --sourcing on the CDR BOM and the saved stock snapshots.
2. Confirm that every turnkey-placed line and the PA device line has a stock record timestamped at CDR at DigiKey, Mouser or a PCBWay turnkey distributor, with stock quantity at least the build quantity, and that none is consignment-only.
3. Confirm that every line of the hand-assembly file names a catalog item, a named source and a dated quote.
4. Record the inspected file paths, their commit and tool versions in the report.
5. On any finding against the criteria, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if every turnkey-placed part and the PA device has a timestamped CDR stock record at DigiKey, Mouser or a PCBWay turnkey distributor covering the build quantity, and every owner-procured hand-soldered part has a catalog item, a named source and a dated quote; otherwise Fail.

**Expected artifacts.**

- `sourcing-check.csv` (csv): BOM line, distributor, stock, timestamp, quote date and pass/fail

### TC-SYS-094: Transmit monitor port attenuation of 40 dB +/-1 dB into 50 ohm

| Field | Value |
|---|---|
| Requirements | REQ-SYS-141 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | none (manual) |

**Setup.** Article: CWHT-A-001 in its enclosure, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: NanoVNA port 1 on the antenna port and port 2 on the monitor port, through-calibrated at the cable ends; the unit switched off, then switched on in Receive with guest lock set so that no transmission can occur. Credit row: T-HW. Test of a system requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the campaign (section 13) and witnessed by the owner; the pre-build Simulation, HostUnit and Emulation evidence named in each requirement's verification_note is supporting only and is not part of this case. TBR values: the acceptance criteria use the values of REQ-SYS-141 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: no transmission is intended; guest lock is set and no key is connected while the NanoVNA is on the antenna port, so that no key-down can reach the NanoVNA; bench supply current limit set before power-on. Environment: room temperature 18 to 28 C; the pack is supplied by the bench supply at 7.4 V +/-0.05 V through the battery terminals unless a step sets another value; dummy load on the antenna port.

**Procedure.**

1. Calibrate the NanoVNA (SOLT) at the two cable ends.
2. With the unit off, measure S21 from the antenna port to the monitor port at 144, 146, 148, 292 and 438 MHz.
3. Set guest lock, switch the unit on in Receive and repeat the measurement.
4. Record the NanoVNA S21 uncertainty at -40 dB from its TV record or datasheet.
5. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
6. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if |S21| from the antenna port to the monitor port, with the NanoVNA uncertainty added, lies between 39 dB and 41 dB of attenuation at 144, 146, 148, 292 and 438 MHz in both unit states; otherwise Fail.

**Instruments and fixtures.**

- NanoVNA, SOL calibration at the cable end used, checked on the dummy load
- Adjustable bench supply, 0 to 30 V, current limit set per step

**Expected artifacts.**

- `monitor-port.s2p` (other): Antenna-to-monitor S-parameters in both states
- `monitor-port.csv` (csv): Frequency, state and attenuation

### TC-SYS-095: Boot banner over USB serial and telemetry on the UART test pads without USB

| Field | Value |
|---|---|
| Requirements | REQ-SYS-143, REQ-SYS-150 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | none (manual) |

**Setup.** Article: CWHT-A-001 in its enclosure, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: host computer serial terminal on USB for the banner; UART telemetry pad on a logic-capture channel decoded by sigrok-cli for the no-USB runs; unit on the bench supply; dummy load; 0.5 W step. Credit row: T-HW. Test of a system requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the campaign (section 13) and witnessed by the owner; the pre-build Simulation, HostUnit and Emulation evidence named in each requirement's verification_note is supporting only and is not part of this case. Hazard controls exercised: HZ-014 (from the cited requirements; docs/safety/hazards.json). Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: every transmission goes into the 50 ohm dummy load or the calibrated power attenuator, connected before power-on, never into an open antenna port; key-down duty kept within the load rating recorded in the report; anyone other than the operator stays 0.6 m or more from the unit and load while keying and 1.0 m or more during a tune carrier (NGO-019); the bench supply current limit is set before each power-on; antistatic wrist strap while the lid is off; the PA area is not touched after key-down runs. Environment: room temperature 18 to 28 C; the pack is supplied by the bench supply at 7.4 V +/-0.05 V through the battery terminals unless a step sets another value; dummy load on the antenna port.

**Procedure.**

1. Run the logic-capture reference pulse-train check of this session and record the result (docs/process/04-verification-and-validation.md section 4).
2. With USB connected to the host, power on and log the USB serial output to the end of Self-test; repeat for three boots.
3. Compare the banner's firmware version and image hash with the VDD of the flashed release, and read the self-test result lines.
4. Disconnect USB; power on from the bench supply and capture the UART pad during receive for 60 s.
5. Close the straight key and then the paddle during the UART capture and confirm telemetry continues during keying.
6. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
7. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if every boot reports over USB serial a firmware version and image hash equal to the VDD and the self-test results (REQ-SYS-143), and with USB absent the UART pads carry decodable 3.3 V telemetry in receive and during keying with both key types (REQ-SYS-150); otherwise Fail.

**Instruments and fixtures.**

- Host computer with picotool and a serial terminal per tools/toolchain.lock.md, micro-USB cable
- Pico-based logic capture (second Pico 2 with sigrok-pico firmware read by sigrok-cli; planned, ADR-009), 3.3 V inputs, 1 MS/s unless a step states otherwise
- 50 ohm BNC dummy load with SMA adapter, power rating recorded in the report
- Owner's straight key and iambic paddle, 3.5 mm TRS plugs (SI-034)
- Adjustable bench supply, 0 to 30 V, current limit set per step

**Expected artifacts.**

- `boot-banner.log.txt` (serial_output): USB serial logs of three boots
- `uart-telemetry.log.txt` (serial_output): Decoded UART telemetry without USB

### TC-SYS-096: Requirements met after assembly with only the stored firmware calibration of pitch centre and reference trim

| Field | Value |
|---|---|
| Requirements | REQ-SYS-144 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | none (manual) |

**Setup.** Article: CWHT-A-001 in its enclosure, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: each delivered unit at its acceptance test; the as-built record of docs/vv/adp/<unit>/as-built.md lists every action performed between receipt and acceptance. Credit row: T-HW. Test of a system requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the campaign (section 13) and witnessed by the owner; the pre-build Simulation, HostUnit and Emulation evidence named in each requirement's verification_note is supporting only and is not part of this case. Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: every transmission goes into the 50 ohm dummy load or the calibrated power attenuator, connected before power-on, never into an open antenna port; key-down duty kept within the load rating recorded in the report; anyone other than the operator stays 0.6 m or more from the unit and load while keying and 1.0 m or more during a tune carrier (NGO-019); the bench supply current limit is set before each power-on; antistatic wrist strap while the lid is off; the PA area is not touched after key-down runs. Environment: room temperature 18 to 28 C; the pack is supplied by the bench supply at 7.4 V +/-0.05 V through the battery terminals unless a step sets another value; dummy load on the antenna port.

**Procedure.**

1. Confirm from the BOM and the as-built record that no adjustable part (trimmer, variable inductor or capacitor) is fitted.
2. Perform only the firmware calibration step for the pitch centre and the reference trim, and record the stored values.
3. Run the acceptance test set of docs/process/04-verification-and-validation.md section 11 (TC-ATP cases) on the unit.
4. Confirm that no hardware adjustment, rework or part change is recorded between receipt and the end of the acceptance tests.
5. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
6. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if each unit passes its acceptance test set with no adjustment other than the stored pitch-centre and reference-trim calibration and no adjustable part fitted; otherwise Fail.

**Instruments and fixtures.**

- tinySA Ultra spectrum analyzer (ADR-021) through the calibrated 30 to 40 dB attenuator rated 10 W or more, attenuator S21 measured on the NanoVNA in the same session; level accuracy per its TV record
- Diode RF probe (1N5711 or equivalent, printed housing) on a BNC T at the dummy load, characterized by TC-SYS-010, read on the multimeter DC voltage range
- Multimeter, DC voltage and DC current ranges, accuracy per datasheet copied into the report (OQ-VV-003)
- Pico-based logic capture (second Pico 2 with sigrok-pico firmware read by sigrok-cli; planned, ADR-009), 3.3 V inputs, 1 MS/s unless a step states otherwise
- 50 ohm BNC dummy load with SMA adapter, power rating recorded in the report
- Owner's straight key and iambic paddle, 3.5 mm TRS plugs (SI-034)
- Adjustable bench supply, 0 to 30 V, current limit set per step

**Expected artifacts.**

- `no-alignment-record.txt` (report): Calibration values stored and the as-built action list

### TC-SYS-097: 70 cm readiness: band-dependent blocks partitioned and a reserved band control

| Field | Value |
|---|---|
| Requirements | REQ-SYS-145, REQ-SYS-146 |
| Method / class | Inspection / Inspection |
| Status | Draft |
| Automation | none (manual) |

**Setup.** Article: design data at tag baseline/cdr: docs/design/architecture.md, the PCB region map, the enclosure STEP, docs/icd/ICD-CTL-SW.md and the display layout; inspected at PDR on the allocated baseline and again at CDR. Configuration: Reviewer compares the architecture block list with the PCB region map and the interfaces between blocks. Credit row: I. Inspection of design data, closed at CDR on the product baseline (docs/process/04-verification-and-validation.md sections 5.1 item 4 and 5.2); the receipt inspection named in the verification_note, where there is one, is recorded as data in the same report. Tools: FreeCAD 1.1.3 and kicad-cli per tools/toolchain.lock.md Safety: not applicable (design data only). Environment: not applicable.

**Procedure.**

1. List from docs/design/architecture.md every function that depends on the band (filters, LO plan, PA match, T/R, antenna match) and the block that holds each.
2. Confirm on the PCB region map that each band-dependent block occupies its own region with interfaces only through the ICD-listed signals.
3. Confirm that no block outside that list changes when the band-dependent blocks are replaced for 70 cm (the architecture document states the replacement set).
4. Confirm a reserved position for a band control on the enclosure STEP, a reserved controller input in the ICD-CTL-SW pin map and a reserved band field in the display layout.
5. Record the inspected file paths, their commit and tool versions in the report.
6. On any finding against the criteria, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if every band-dependent function is confined to identified blocks whose replacement for 70 cm changes no other block, and an enclosure position, a controller input and a display field are reserved for a band control; otherwise Fail.

**Expected artifacts.**

- `band-partition-table.csv` (csv): Band-dependent function, block, PCB region and interface signals
- `reserved-band-control.png` (plot): Renders and excerpts of the reserved position, pin and display field

### TC-SYS-098: Unit cost from the labor-free cost model with CDR quotes

| Field | Value |
|---|---|
| Requirements | REQ-SYS-147 |
| Method / class | Analysis / Simulation |
| Status | Draft |
| Automation | `tools/budgets/cost_model.py` |

**Setup.** Article: design data at tag baseline/cdr: docs/plan/cost-estimate.md and the dated CDR quotes (PCBWay fabrication, assembly and CNC, DigiKey, owner-procured parts, shipping) in the release package. Configuration: tools/budgets/cost_model.py (planned) sums the quotes for the ordered quantity with the stated contingency and divides by three units. Credit row: A. Analysis closed by Simulation on the CDR design data and confirmed at SAR by the physical configuration audit of every analyzed value (docs/process/04-verification-and-validation.md sections 5.1 item 5 and 5.2); the post-build readings named in the verification_note are supporting data only. TBR values: the acceptance criteria use the values of REQ-SYS-147 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Tools: Python per tools/toolchain.lock.md Safety: not applicable (design data only). Environment: not applicable.

**Procedure.**

1. Confirm that every quote in the model has a date and a file in the release package.
2. Run tools/budgets/cost_model.py and save the cost per complete unit amortized over three units, excluding instruments and labor.
3. At SAR, repeat with the invoices in place of the quotes and record the result as supporting data.
4. Record tool versions, the design-data tag and the commit of every deck, model, script and checker in the report.
5. On any assertion or checker failure, or any difference between the analyzed values and the design data, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if the cost per complete unit amortized over three units, excluding instruments and labor, is at most USD 610 with the CDR quotes; otherwise Fail.

**Expected artifacts.**

- `cost-model.csv` (csv): Line items, quotes, contingency and per-unit total

### TC-SYS-099: MIT license, third-party notices and pushed baseline tags in the public repository

| Field | Value |
|---|---|
| Requirements | REQ-SYS-148 |
| Method / class | Inspection / Inspection |
| Status | Draft |
| Automation | none (manual) |

**Setup.** Article: design data at tag baseline/cdr: the repository at the baseline tag and the public remote github.com/robinonsay/cwht. Configuration: git ls-remote lists the tags on the public remote; the LICENSE file and the third-party notice file are read. Credit row: I. Inspection of design data, closed at CDR on the product baseline (docs/process/04-verification-and-validation.md sections 5.1 item 4 and 5.2); the receipt inspection named in the verification_note, where there is one, is recorded as data in the same report. Tools: git per tools/toolchain.lock.md Safety: not applicable (design data only). Environment: not applicable.

**Procedure.**

1. Confirm that LICENSE at the repository root is the MIT license text naming the copyright holder.
2. Confirm that the third-party notice file lists every external crate, library or model in the build with its license.
3. Run git ls-remote --tags on github.com/robinonsay/cwht and confirm that every baseline tag created so far is present on the public remote.
4. Confirm that design data, firmware and process records are all in that repository (no private companion repository is referenced by the build).
5. Record the inspected file paths, their commit and tool versions in the report.
6. On any finding against the criteria, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if the MIT LICENSE, the complete third-party notice file and every baseline tag are present in the public repository github.com/robinonsay/cwht, and the design, firmware and process records are all in it; otherwise Fail.

**Expected artifacts.**

- `ls-remote-tags.txt` (log): git ls-remote --tags output

### TC-SYS-100: Spurious emissions and rated power into SWR 2:1 loads

| Field | Value |
|---|---|
| Requirements | REQ-SYS-151, REQ-SYS-152 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | `tools/tinysa_scan_check.py` |

**Setup.** Article: CWHT-A-001 in its enclosure, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: 2:1 fixtures: for spurious, NanoVNA-characterized 2:1 mismatch networks at four phases ahead of the calibrated attenuator, readings corrected by each fixture's S21; for power, the same four 2:1 fixtures with the delivered power computed from the tinySA carrier reading as P_in = P_meas (1 - |S11|^2) / |S21|^2 with the fixture and attenuator S-parameters at 146 MHz, and the 25 ohm and 100 ohm resistive loads with the diode probe across them, P = Vpk^2 / (2 R) with R from the NanoVNA at 146 MHz (docs/vv/fixtures/mismatch-set.md, planned); 5 W step; bench supply through the pack-resistance fixture. Credit row: T-HW. Test of a system requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the campaign (section 13) and witnessed by the owner; the pre-build Simulation, HostUnit and Emulation evidence named in each requirement's verification_note is supporting only and is not part of this case. TBR values: the acceptance criteria use the values of REQ-SYS-151, REQ-SYS-152 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Hazard controls exercised: HZ-003, HZ-008, HZ-009 (from the cited requirements; docs/safety/hazards.json). Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: every transmission goes into the 50 ohm dummy load or the calibrated power attenuator, connected before power-on, never into an open antenna port; key-down duty kept within the load rating recorded in the report; anyone other than the operator stays 0.6 m or more from the unit and load while keying and 1.0 m or more during a tune carrier (NGO-019); the bench supply current limit is set before each power-on; antistatic wrist strap while the lid is off; the PA area is not touched after key-down runs. Environment: room temperature 18 to 28 C; the pack is supplied by the bench supply at 7.4 V +/-0.05 V through the battery terminals unless a step sets another value; dummy load on the antenna port.

**Procedure.**

1. Measure the attenuator and cable S21 on the NanoVNA from 9 kHz (or the NanoVNA lower limit) to 1.5 GHz and save the Touchstone file; run the tinySA Ultra internal calibration-output check; record both.
2. Characterize the four 2:1 spurious fixtures (S11 and S21 at the carrier and at 2f, 3f and 7f) and the 25 ohm and 100 ohm power loads (|Z| at 146 MHz).
3. With the first 2:1 fixture, 7.4 V, 5 W step, scan 9 kHz to 1.5 GHz at 144.05, 146.00 and 147.95 MHz keyed by the continuous-dit generator, as in TC-SYS-014.
4. Repeat for the other three fixture phases.
5. Correct every level by the fixture and attenuator S21 with tools/tinysa_scan_check.py.
6. With each of the four 2:1 fixtures in turn ahead of the calibrated attenuator, set 6.4 V and at 146.00 MHz close the straight key for 3 s; read the carrier level on the tinySA Ultra and compute the delivered power from the fixture S11 and S21 and the attenuator S21 with tools/tinysa_scan_check.py.
7. Fit the 25 ohm load with the probe, set 6.4 V, and at 146.00 MHz close the straight key for 3 s; read the probe. Repeat with the paddle dah lever held for 3 s.
8. Repeat the previous step with the 100 ohm load.
9. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
10. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if every spurious emission at the antenna port, corrected and increased by the tinySA level accuracy, is at most 25 uW (-16.0 dBm) at the 5 W step into each 2:1 fixture at the three frequencies (REQ-SYS-151), and the delivered power at 6.4 V into each of the four 2:1 fixtures, less the tinySA level uncertainty, and into the 25 ohm and the 100 ohm loads, less the probe uncertainty, is at least 4.0 W (REQ-SYS-152); otherwise Fail.

**Instruments and fixtures.**

- tinySA Ultra spectrum analyzer (ADR-021) through the calibrated 30 to 40 dB attenuator rated 10 W or more, attenuator S21 measured on the NanoVNA in the same session; level accuracy per its TV record
- NanoVNA, SOL calibration at the cable end used, checked on the dummy load
- Diode RF probe (1N5711 or equivalent, printed housing) on a BNC T at the dummy load, characterized by TC-SYS-010, read on the multimeter DC voltage range
- Multimeter, DC voltage and DC current ranges, accuracy per datasheet copied into the report (OQ-VV-003)
- Adjustable bench supply, 0 to 30 V, current limit set per step
- Pack-resistance fixture: series resistor equal to the datasheet internal resistance of two cells plus two holders, in the bench-supply lead (docs/vv/fixtures/pack-resistance.md, planned)
- Owner's straight key and iambic paddle, 3.5 mm TRS plugs (SI-034)

**Expected artifacts.**

- `mismatch-spurious.csv` (csv): Fixture phase, frequency and corrected emission levels
- `mismatch-power.csv` (csv): Load (four 2:1 fixtures and the 25 ohm and 100 ohm loads), keying source, tinySA or probe reading and delivered power

### TC-SYS-101: Synthesizer unlock or off-frequency fault and forward-power detector fault responses

| Field | Value |
|---|---|
| Requirements | REQ-SYS-154, REQ-SYS-156, REQ-SYS-183 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | `tools/analyze_logic_capture.py` |

**Setup.** Article: CWHT-A-001, enclosure lid off for test-point access, running the fault-injection test build of release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (a build flavour of the release commit whose injection commands arrive over the UART test pads from the host serial terminal through the 3.3 V serial adapter, or over USB serial only in steps that expect no carrier, because USB VBUS sets the USB flag and the hardware transmit inhibit of REQ-SYS-092, and which toggles the injection-marker test pad at the instant of each injection); the release image is restored and checked with picotool verify at the end of the case. Configuration: fault build commands for synthesizer loss of lock and a 12 kHz frequency offset; forward-power detector output forced low and high at its test pad through a resistor to ground and to 3.3 V switched by a fixture whose second pole marks the event on the logic capture; antenna port to the calibrated power attenuator and the tinySA Ultra; 1 W step at 146.00 MHz. Credit row: T-HW. Test of a system requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the campaign (section 13) and witnessed by the owner; the pre-build Simulation, HostUnit and Emulation evidence named in each requirement's verification_note is supporting only and is not part of this case. TBR values: the acceptance criteria use the values of REQ-SYS-154, REQ-SYS-156 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). RF-off level: the acceptance criteria use -57 dBm, the value of REQ-SYS-183 marked TBR (close by PDR); a change returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2). Hazard controls exercised: HZ-003, HZ-008 (from the cited requirements; docs/safety/hazards.json). Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: every transmission goes into the 50 ohm dummy load or the calibrated power attenuator, connected before power-on, never into an open antenna port; key-down duty kept within the load rating recorded in the report; anyone other than the operator stays 0.6 m or more from the unit and load while keying and 1.0 m or more during a tune carrier (NGO-019); the bench supply current limit is set before each power-on; antistatic wrist strap while the lid is off; the PA area is not touched after key-down runs. Environment: room temperature 18 to 28 C; the pack is supplied by the bench supply at 7.4 V +/-0.05 V through the battery terminals unless a step sets another value; dummy load on the antenna port.

**Procedure.**

1. Run the logic-capture reference pulse-train check of this session and record the result (docs/process/04-verification-and-validation.md section 4).
2. Measure the attenuator and cable S21 on the NanoVNA from 9 kHz (or the NanoVNA lower limit) to 1.5 GHz and save the Touchstone file; run the tinySA Ultra internal calibration-output check; record both.
3. Inject loss of lock in Receive, then close the straight key: record PA_EN, RF and the mode.
4. Close the straight key, then inject loss of lock during the over: record the same.
5. Repeat the two previous steps with the 12 kHz offset, keyed with the paddle dah lever.
6. While keyed with the straight key, force the detector output low; after acknowledging, force it high while keyed with the paddle.
7. Run tools/analyze_logic_capture.py: marker-to-PA_EN-fall latencies.
8. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
9. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if for loss of lock and for the 12 kHz offset, at key-down and during the over, the unit enters Fault-safe with PA_EN low and no carrier at the set frequency above -57 dBm at the antenna port on the tinySA Ultra (the RF-off level of REQ-SYS-183) (REQ-SYS-154), and it enters Fault-safe at most 100 ms after the detector reading is forced low or high during key-down (REQ-SYS-156); otherwise Fail.

**Instruments and fixtures.**

- Pico-based logic capture (second Pico 2 with sigrok-pico firmware read by sigrok-cli; planned, ADR-009), 3.3 V inputs, 1 MS/s unless a step states otherwise
- tinySA Ultra spectrum analyzer (ADR-021) through the calibrated 30 to 40 dB attenuator rated 10 W or more, attenuator S21 measured on the NanoVNA in the same session; level accuracy per its TV record
- NanoVNA, SOL calibration at the cable end used, checked on the dummy load
- Host computer with picotool and a serial terminal per tools/toolchain.lock.md, micro-USB cable
- 3.3 V USB-to-UART serial adapter between the host computer and the UART test pads, so that injection commands reach the unit with its USB port disconnected (docs/vv/fixtures/uart-adapter.md, planned)
- Owner's straight key and iambic paddle, 3.5 mm TRS plugs (SI-034)
- Adjustable bench supply, 0 to 30 V, current limit set per step

**Expected artifacts.**

- `rf-faults.csv` (csv): Fault, timing, keying source, PA_EN, RF and latency

### TC-SYS-102: Straight-key contact to RF rise latency and a constant lead-in across an over

| Field | Value |
|---|---|
| Requirements | REQ-SYS-160, REQ-SYS-161 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | `tools/analyze_logic_capture.py` |

**Setup.** Article: CWHT-A-001, enclosure lid off for test-point access, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: logic capture at 1 MS/s on the key tip and ring contacts at the jack, the keyer test point, TX_KEY, the T/R drive, the envelope drive and the sidetone PWM line as the steps name them; dummy load; 1 W step; RF rise taken as the first envelope ramp-step edge on the envelope drive (04 section 6.1). Credit row: T-HW. Test of a system requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the campaign (section 13) and witnessed by the owner; the pre-build Simulation, HostUnit and Emulation evidence named in each requirement's verification_note is supporting only and is not part of this case. TBR values: the acceptance criteria use the values of REQ-SYS-160, REQ-SYS-161 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: every transmission goes into the 50 ohm dummy load or the calibrated power attenuator, connected before power-on, never into an open antenna port; key-down duty kept within the load rating recorded in the report; anyone other than the operator stays 0.6 m or more from the unit and load while keying and 1.0 m or more during a tune carrier (NGO-019); the bench supply current limit is set before each power-on; antistatic wrist strap while the lid is off; the PA area is not touched after key-down runs. Environment: room temperature 18 to 28 C; the pack is supplied by the bench supply at 7.4 V +/-0.05 V through the battery terminals unless a step sets another value; dummy load on the antenna port.

**Procedure.**

1. Run the logic-capture reference pulse-train check of this session and record the result (docs/process/04-verification-and-validation.md section 4).
2. Select Straight; from receive, make 20 overs of five closures each; capture the contact, the T/R drive and the envelope drive.
3. Select Iambic A at 15 WPM and send PARIS five times as one over with the paddle; capture the keyer test point, the T/R drive and the envelope drive.
4. Repeat at 50 WPM.
5. Run tools/analyze_logic_capture.py: contact-to-first-ramp-step for each straight-key closure, and keyer-edge-to-ramp-step delay for every element of each paddle over.
6. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
7. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if every straight-key closure, first and later in an over, begins the RF rise at most 15 ms after contact closure (REQ-SYS-160), and within each paddle over every element's delay from the keyer test point to the RF rise is at most 12 ms and all delays in the over differ by at most 0.5 ms (REQ-SYS-161); otherwise Fail. The 0.5 ms equality tolerance is the test author's, taken from REQ-SYS-042, because REQ-SYS-161 states none.

**Instruments and fixtures.**

- Pico-based logic capture (second Pico 2 with sigrok-pico firmware read by sigrok-cli; planned, ADR-009), 3.3 V inputs, 1 MS/s unless a step states otherwise
- 50 ohm BNC dummy load with SMA adapter, power rating recorded in the report
- Owner's straight key and iambic paddle, 3.5 mm TRS plugs (SI-034)
- Adjustable bench supply, 0 to 30 V, current limit set per step

**Expected artifacts.**

- `latency-rf.csv` (csv): Over, element, key type, delay

### TC-SYS-103: Display legibility at 0.5 m under 300 lux without a backlight

| Field | Value |
|---|---|
| Requirements | REQ-SYS-165 |
| Method / class | Analysis / Simulation |
| Status | Draft |
| Automation | `tools/budgets/display_legibility.py` |

**Setup.** Article: design data at tag baseline/cdr: the selected display datasheet (reflectance and contrast ratio under ambient light, D-UI-01) and the character height of the character-size inspection case. Configuration: tools/budgets/display_legibility.py (planned) computes the visual angle of the frequency characters at 0.5 m and the luminance contrast at 300 lux from the datasheet reflectance values. Credit row: A. Analysis closed by Simulation on the CDR design data and confirmed at SAR by the physical configuration audit of every analyzed value (docs/process/04-verification-and-validation.md sections 5.1 item 5 and 5.2); the post-build readings named in the verification_note are supporting data only. TBR values: the acceptance criteria use the values of REQ-SYS-165 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Tools: Python per tools/toolchain.lock.md Safety: not applicable (design data only). Environment: not applicable.

**Procedure.**

1. Read the datasheet reflectance of on and off pixels (or the contrast ratio) at the illuminance closest to 300 lux.
2. Compute the luminance contrast ratio at 300 lux.
3. Compute the visual angle subtended at 0.5 m by the character height of TC-SYS-044.
4. Record tool versions, the design-data tag and the commit of every deck, model, script and checker in the report.
5. On any assertion or checker failure, or any difference between the analyzed values and the design data, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if the luminance contrast ratio at 300 lux is at least 3:1 and the frequency characters subtend at least 16 arcmin at 0.5 m; otherwise Fail. These two legibility criteria are proposed by the test author because REQ-SYS-165 names no metric; the owner confirms or replaces them at PDR (D-UI-01).

**Expected artifacts.**

- `display-legibility.txt` (report): Datasheet values, contrast and visual angle

### TC-SYS-104: Default audio cap restored after 20 h of cumulative unlocked operation

| Field | Value |
|---|---|
| Requirements | REQ-SYS-169 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | none (manual) |

**Setup.** Article: CWHT-A-001 in its enclosure, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: headphone output into the audio load fixture (32 ohm per channel unless a step says otherwise); multimeter true-RMS AC across the load; Bench-test tones: the steady 700 Hz tone and, after the warning screen and second confirmation, the full-scale 700 Hz sine and the full-scale test patterns; PRACTICE set so that no transmission occurs. Unit on the bench supply; the 20 h accumulate in one run or in several runs whose elapsed times are logged from the UART telemetry. Credit row: T-HW. Test of a system requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the campaign (section 13) and witnessed by the owner; the pre-build Simulation, HostUnit and Emulation evidence named in each requirement's verification_note is supporting only and is not part of this case. TBR values: the acceptance criteria use the values of REQ-SYS-169 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Hazard controls exercised: HZ-005 (from the cited requirements; docs/safety/hazards.json). Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: headphones are never worn during this case; a 32 ohm load resistor on a 3.5 mm TRS breakout replaces them; the full-scale test tone is selected only after the warning screen and the second confirmation of the Bench-test mode (docs/conops/conops.md Table 3.4-1). Environment: room temperature 18 to 28 C; the pack is supplied by the bench supply at 7.4 V +/-0.05 V through the battery terminals unless a step sets another value; dummy load on the antenna port.

**Procedure.**

1. Wire the UART telemetry test pad to a logic-capture channel and confirm that the sigrok-cli UART decoder prints the telemetry lines (REQ-SYS-150).
2. Unlock the cap (non-persistent) and read the full-scale tone RMS at maximum volume.
3. Operate unlocked, logging telemetry, for 19 h 50 min of cumulative operation; read the RMS.
4. Continue to 20 h 10 min cumulative; read the RMS and the displayed cap state.
5. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
6. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if the output still exceeds 30 mVrms at 19 h 50 min and is at most 30 mVrms with the default cap shown at 20 h 10 min of cumulative unlocked operation; otherwise Fail.

**Instruments and fixtures.**

- Multimeter, true-RMS AC voltage range, accuracy at 700 Hz per datasheet copied into the report (OQ-VV-003)
- Audio load fixture: 16, 32 and 64 ohm resistors, 0.25 W, selectable on a 3.5 mm TRS breakout per channel (docs/vv/fixtures/audio-load.md, planned)
- Adjustable bench supply, 0 to 30 V, current limit set per step
- Pico-based logic capture (second Pico 2 with sigrok-pico firmware read by sigrok-cli; planned, ADR-009), 3.3 V inputs, 1 MS/s unless a step states otherwise

**Expected artifacts.**

- `audio-expiry.csv` (csv): Cumulative time, cap state, RMS

### TC-SYS-105: Only the sidetone on the headphones while keying 5 W with 1.5 m unshielded leads

| Field | Value |
|---|---|
| Requirements | REQ-SYS-173 |
| Method / class | Demonstration / Bench |
| Status | Draft |
| Automation | none (manual) |

**Setup.** Article: CWHT-A-001 in its enclosure, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: 1.5 m unshielded leads on the key jack and the headphone jack; the owner's headphones at the default cap; the Bench-test PARIS generator at 5 W into the dummy load, then into the reference antenna; the antenna block runs only after the OnAir authorization in docs/reviews/TRR-Dn/decision-memo.md (04 section 6.3). Credit row: D. Demonstration by the owner on the delivered unit (docs/process/04-verification-and-validation.md section 5.2): pass or fail is observed without detailed data gathering and each observation is photographed or logged. Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: every transmission goes into the 50 ohm dummy load or the calibrated power attenuator, connected before power-on, never into an open antenna port; key-down duty kept within the load rating recorded in the report; anyone other than the operator stays 0.6 m or more from the unit and load while keying and 1.0 m or more during a tune carrier (NGO-019); the bench supply current limit is set before each power-on; antistatic wrist strap while the lid is off; the PA area is not touched after key-down runs. Headphones at the default 30 mVrms cap only. Antenna block: identification per 47 CFR 97.119 at least every 10 min and at the end, a clear frequency in 144.000 to 144.100 MHz after listening for 60 s. Environment: room temperature 18 to 28 C; dummy load, then the reference antenna.

**Procedure.**

1. Into the dummy load, run the PARIS generator at 5 W for 1 min while the owner listens.
2. Key by hand with the straight key and then the paddle on the long lead for 30 s each while listening.
3. Confirm the OnAir authorization, connect the reference antenna and repeat both steps.
4. The owner writes on the demonstration sheet whether anything other than the sidetone was heard.
5. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
6. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if the owner hears only the sidetone (no buzz, hum, RF rectification or clicks beyond the sidetone envelope) in every run; otherwise Fail.

**Instruments and fixtures.**

- 50 ohm BNC dummy load with SMA adapter, power rating recorded in the report
- Owner's straight key and iambic paddle, 3.5 mm TRS plugs (SI-034)
- Reference antenna: Signal Stick half-wave with 48 cm counterpoise tail
- Owner's headphones
- 1.5 m unshielded two-conductor leads with 3.5 mm TRS plugs (docs/vv/fixtures/, planned)

**Expected artifacts.**

- `leads-audio-sheet.jpg` (photo): Photograph of the owner's demonstration sheet

### TC-SYS-106: Receive-mode emissions at the antenna port from 9 kHz to 1.5 GHz

| Field | Value |
|---|---|
| Requirements | REQ-SYS-176 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | `tools/tinysa_scan_check.py` |

**Setup.** Article: CWHT-A-001 in its enclosure, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: antenna port to the calibrated power attenuator at its 30 dB setting and the tinySA Ultra; guest lock set and the key jack empty so that no transmission can occur; RBW and span segments chosen so the noise floor referred to the antenna port is at least 6 dB below -57 dBm; readings corrected by the attenuator S21. Credit row: T-HW. Test of a system requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the campaign (section 13) and witnessed by the owner; the pre-build Simulation, HostUnit and Emulation evidence named in each requirement's verification_note is supporting only and is not part of this case. TBR values: the acceptance criteria use the values of REQ-SYS-176 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: no transmission is intended; guest lock is set, the key jack is empty and the power attenuator stays in line so that an unintended key-down cannot reach the analyzer input unattenuated; bench supply current limit set before power-on. Environment: room temperature 18 to 28 C; the pack is supplied by the bench supply at 7.4 V +/-0.05 V through the battery terminals unless a step sets another value; dummy load on the antenna port.

**Procedure.**

1. Measure the attenuator and cable S21 on the NanoVNA from 9 kHz (or the NanoVNA lower limit) to 1.5 GHz and save the Touchstone file; run the tinySA Ultra internal calibration-output check; record both.
2. Tune to 144.05 MHz in Receive and scan 9 kHz to 1.5 GHz in segments with max-hold for 20 s per segment.
3. Repeat at 146.00 MHz and at 147.95 MHz.
4. Run tools/tinysa_scan_check.py for the receive-mode limit.
5. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
6. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if every emission at the antenna port in receive, corrected and increased by the tinySA level accuracy, is at most -57 dBm from 9 kHz to 1.5 GHz at the three tuned frequencies; otherwise Fail.

**Instruments and fixtures.**

- tinySA Ultra spectrum analyzer (ADR-021) through the calibrated 30 to 40 dB attenuator rated 10 W or more, attenuator S21 measured on the NanoVNA in the same session; level accuracy per its TV record
- NanoVNA, SOL calibration at the cable end used, checked on the dummy load
- Adjustable bench supply, 0 to 30 V, current limit set per step

**Expected artifacts.**

- `rx-emissions.csv` (csv): Tuned frequency, emission frequency and corrected level
- `rx-emissions-traces.png` (plot): tinySA traces

### TC-SYS-107: Enclosure attenuation of digital and switching-converter emissions

| Field | Value |
|---|---|
| Requirements | REQ-SYS-177 |
| Method / class | Analysis / Simulation |
| Status | Draft |
| Automation | `tools/budgets/enclosure_shielding.py` |

**Setup.** Article: design data at tag baseline/cdr: the clock plan (every clock and converter frequency with harmonics to 1.5 GHz), the enclosure material, wall thickness, seams and every aperture from the STEP. Configuration: tools/budgets/enclosure_shielding.py (planned) computes the aperture-limited shielding effectiveness of the enclosure at each fundamental and harmonic. Credit row: A. Analysis closed by Simulation on the CDR design data and confirmed at SAR by the physical configuration audit of every analyzed value (docs/process/04-verification-and-validation.md sections 5.1 item 5 and 5.2); the post-build readings named in the verification_note are supporting data only. TBR values: the acceptance criteria use the values of REQ-SYS-177 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Tools: Python per tools/toolchain.lock.md Safety: not applicable (design data only). Environment: not applicable.

**Procedure.**

1. List every clock and switching-converter fundamental and its harmonics to 1.5 GHz from the clock plan.
2. List every aperture and seam with its largest dimension from the STEP.
3. Compute the shielding effectiveness at each listed frequency from the largest aperture dimension and the wall material.
4. Repeat the computation with every toleranced input at its worst-case corner (checker option --corners) and record the worst case.
5. Record tool versions, the design-data tag and the commit of every deck, model, script and checker in the report.
6. On any assertion or checker failure, or any difference between the analyzed values and the design data, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if the computed enclosure attenuation is at least 20 dB at every digital and switching-converter fundamental and harmonic to 1.5 GHz; otherwise Fail.

**Expected artifacts.**

- `shielding.csv` (csv): Frequency, limiting aperture and shielding effectiveness

### TC-SYS-108: Transmission-length hardware backstop: RF ended at 150 s to 180 s of continuous transmit until the return to receive, independent of firmware

| Field | Value |
|---|---|
| Requirements | REQ-SYS-180, REQ-SYS-183 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | `tools/analyze_logic_capture.py` |

**Setup.** Article: CWHT-A-001, enclosure lid off for test-point access, running the fault-injection test build of release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (a build flavour of the release commit whose injection commands arrive over the UART test pads from the host serial terminal through the 3.3 V serial adapter, or over USB serial only in steps that expect no carrier, because USB VBUS sets the USB flag and the hardware transmit inhibit of REQ-SYS-092, and which toggles the injection-marker test pad at the instant of each injection); the release image is restored and checked with picotool verify at the end of the case. Configuration: part A uses the fault-injection build with the firmware straight-key timeout, the paddle watchdog, the bench test-mode timeout, the hang-time return to receive and the independent-cutoff-seen detection (ConOps Table 3.4-4 row 12) disabled, and commands that hold the T/R drive in transmit and toggle TX_KEY in a set pattern, so that firmware keeps commanding transmit through the whole run; part B uses the release build with the operator sending and the hang time set to 30 dits, so that normal sending never returns the unit to receive; antenna port through the BNC T of the RF-present indicator to the calibrated power attenuator and the tinySA Ultra; USB disconnected; tinySA span 1 MHz at the carrier on the live trace until the carrier disappears, then max hold, started within 5 s of the disappearance and kept until the T/R drive returns to receive; logic capture on the T/R drive, TX_KEY, PA_EN and the RF-present indicator; 0.5 W step at 146.00 MHz. Continuous transmit starts at the T/R drive edge into transmit (REQ-SYS-180 rationale); the RF-present indicator falls at or after the end of the RF, so reading the end time from it is conservative. The window of REQ-SYS-180 is 150 s to 180 s (TBR): an end before 150 s or after 180 s fails the case, and every end time is recorded for the closure of the TBR. Credit row: T-HW. Test of a system requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the campaign (section 13) and witnessed by the owner; the pre-build Simulation, HostUnit and Emulation evidence named in each requirement's verification_note is supporting only and is not part of this case. TBR values: the acceptance criteria use the window of REQ-SYS-180 as written, 150 s to 180 s marked TBR (close by SRR, package decision 38; confirmed by the monostable timing Simulation at PDR); a change returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071), and if the owner declines the backstop this case is retired with the requirement (02 section 11.3). RF-off level: the acceptance criteria use -57 dBm, the value of REQ-SYS-183 marked TBR (close by PDR); a change returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2). Hazard controls exercised: HZ-001, HZ-003, HZ-004, HZ-006, HZ-012, HZ-014 (from the cited requirement; HZ-004 K12 in docs/safety/hazards.json). Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: every transmission goes into the 50 ohm dummy load or the calibrated power attenuator, connected before power-on, never into an open antenna port; key-down duty kept within the load rating recorded in the report; anyone other than the operator stays 0.6 m or more from the unit and load while keying and 1.0 m or more during a tune carrier (NGO-019); the bench supply current limit is set before each power-on; antistatic wrist strap while the lid is off; the PA area is not touched after key-down runs. The operator watches every run: if the carrier has not disappeared 190 s after the T/R drive entered transmit, the operator removes bench-supply power (part A) or stops sending (part B) and the stop rule applies; each run keeps a carrier of about 50 percent duty at 0.5 W for up to 210 s, within the attenuator rating recorded in the report. Environment: room temperature 18 to 28 C; the pack is supplied by the bench supply at 7.4 V +/-0.05 V through the battery terminals unless a step sets another value; the calibrated power attenuator on the antenna port through the BNC T of the RF-present indicator.

**Procedure.**

1. Run the logic-capture reference pulse-train check of this session and record the result (docs/process/04-verification-and-validation.md section 4).
2. Measure the attenuator and cable S21 on the NanoVNA from 9 kHz (or the NanoVNA lower limit) to 1.5 GHz and save the Touchstone file; run the tinySA Ultra internal calibration-output check; record both.
3. Close the straight key for 3 s and confirm that the RF-present indicator channel is high with the carrier and low after it.
4. Part A at 7.4 V: command the T/R drive into transmit and TX_KEY toggling 80 ms on and 80 ms off (continuous dits at 15 WPM, 50 percent duty) and keep the command for 210 s after the T/R edge; start the tinySA max hold within 5 s of the carrier disappearing from the live trace; then command the T/R drive to receive.
5. Re-arm: 5 s after the return to receive, command the T/R drive into transmit with the same TX_KEY pattern for 10 s, then to receive; record whether the carrier is present.
6. Repeat the two previous steps at 6.5 V and at 8.4 V.
7. At 7.4 V repeat the part A run with a PARIS loop at 50 WPM (24 ms dit, 7-dit word spaces) as the TX_KEY pattern, followed by the re-arm run.
8. Restore the release image and check it with picotool verify; disconnect USB; set Straight mode, 15 WPM and the 30-dit hang time.
9. Part B, straight key: send plain text continuously with the straight key, with no pause longer than 1 s, for 200 s after the first key-down, starting the tinySA max hold within 5 s of the carrier disappearing; stop sending, then record the displayed message and acknowledge it.
10. Part B, paddle: set Iambic A at 25 WPM with the 30-dit hang time and repeat the previous step with the paddle.
11. Run tools/analyze_logic_capture.py: per run, the time from the T/R drive edge into transmit to the end of the last RF-present high, TX_KEY activity after it, RF-present activity from then until the T/R drive returns to receive, and the carrier in each re-arm run.
12. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
13. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if in every part A and part B run the last RF-present high ends at least 150 s and at most 180 s after the T/R drive entered transmit, the indicator stays low from then until the T/R drive returns to receive, in part A while TX_KEY is still toggling (the evidence of independence from firmware; in part B the firmware ends keying when it sees the cut), and no carrier above -57 dBm at the antenna port on the tinySA Ultra (the RF-off level of REQ-SYS-183) appears on the max-hold trace until that return, and in every re-arm run the carrier is present after the return to receive; otherwise Fail. The end time of every run is recorded for the closure of the window TBR.

**Instruments and fixtures.**

- Pico-based logic capture (second Pico 2 with sigrok-pico firmware read by sigrok-cli; planned, ADR-009), 3.3 V inputs, 1 MS/s unless a step states otherwise
- RF-present indicator: the diode RF probe (1N5711 or equivalent, printed housing, characterized by TC-SYS-010) on a BNC T at the attenuator input, its DC output through a resistive divider with a 3.3 V clamp to a logic-capture channel, sized so that a 0.5 W carrier reads logic high (docs/vv/fixtures/rf-present-indicator.md, planned); a timing indicator whose falling edge comes at or after the end of the RF, never a level measurement
- tinySA Ultra spectrum analyzer (ADR-021) through the calibrated 30 to 40 dB attenuator rated 10 W or more, attenuator S21 measured on the NanoVNA in the same session; level accuracy per its TV record
- NanoVNA, SOL calibration at the cable end used, checked on the dummy load
- Host computer with picotool and a serial terminal per tools/toolchain.lock.md, micro-USB cable
- 3.3 V USB-to-UART serial adapter between the host computer and the UART test pads, so that injection commands reach the unit with its USB port disconnected (docs/vv/fixtures/uart-adapter.md, planned)
- Owner's straight key and iambic paddle, 3.5 mm TRS plugs (SI-034)
- Adjustable bench supply, 0 to 30 V, current limit set per step

**Expected artifacts.**

- `backstop-runs.csv` (csv): Run, part, supply, TX_KEY pattern or key, T/R-into-transmit to RF-end time, RF after the end, re-arm result
- `backstop-maxhold.png` (plot): tinySA max-hold trace after each RF end
- `backstop-capture.sr` (other): Raw logic capture
- `backstop-setup.jpg` (photo): As-run setup: BNC T, RF-present indicator, attenuator and tinySA

### TC-SYS-109: Hardware PA over-temperature cut-off: RF ended while the heat-sink sensor reads above 95 C, independent of firmware

| Field | Value |
|---|---|
| Requirements | REQ-SYS-181, REQ-SYS-183 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | `tools/analyze_logic_capture.py` |

**Setup.** Article: CWHT-A-001, enclosure lid off for test-point access, running the fault-injection test build of release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (a build flavour of the release commit whose injection commands arrive over the UART test pads from the host serial terminal through the 3.3 V serial adapter, or over USB serial only in steps that expect no carrier, because USB VBUS sets the USB flag and the hardware transmit inhibit of REQ-SYS-092, and which toggles the injection-marker test pad at the instant of each injection); the release image is restored and checked with picotool verify at the end of the case. Configuration: fault-injection build with the REQ-SYS-118 over-temperature inhibit, the fold-back and the independent-cutoff-seen detection (ConOps Table 3.4-4 row 12) disabled, so that firmware keeps PA_EN asserted on every key-down whatever the PA temperature and whether or not the cut-off acts; the cut-off sensor replaced at its test pad by the NTC substitution fixture with the equivalents of 25 C, 80 C, 90 C, T_trip and 100 C, where T_trip is 98 C (the upper bound of the 95 C +/-3 C threshold of REQ-SYS-181) minus the cut-off sensor's datasheet tolerance at 98 C minus the fixture resistor tolerance expressed in degrees, computed in the report from the adopted sensor's datasheet curve, so that a threshold anywhere within the stated tolerance, read by a sensor cold within its own tolerance, still demands the cut; 90 C lies below the 92 C lower bound, so the carrier must be present there; before each threshold and full over-temperature run the fixture is set to 25 C for 2 s and then to 90 C, so that the run starts from the released state; fixture marker, PA_EN and the RF-present indicator on the logic capture; antenna port through the BNC T of the RF-present indicator to the calibrated power attenuator and the tinySA Ultra; USB disconnected; tinySA in zero span at the carrier with a 5 s sweep started at each key-down, so that the trace shows the level before and after the cut; 0.5 W step at 146.00 MHz; every key-down at most 3 s long, so that neither the firmware timeouts nor the hardware cutoff of REQ-SYS-055 act. The case applies to the sensor-and-comparator form of the cut-off that the REQ-SYS-181 verification note assumes; if the ADR that adopts the cut-off selects a thermal fuse or a PTC, the case returns to Draft for a heated-heat-sink procedure (thermocouple input per OQ-VV-003). The 100 ms response window is the response time of REQ-SYS-181 (TBR), equal to that of the firmware inhibit REQ-SYS-118. The requirement states no release point: the carrier at 90 C and 80 C on the way down is recorded as data. Credit row: T-HW. Test of a system requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the campaign (section 13) and witnessed by the owner; the pre-build Simulation, HostUnit and Emulation evidence named in each requirement's verification_note is supporting only and is not part of this case. TBR values: the acceptance criteria use the values of REQ-SYS-181 as written, 95 C +/-3 C and 100 ms marked TBR (close by SRR, package decision 39; confirmed by the PDR thermal analysis); a change returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071), and if the owner declines the cut-off this case is retired with the requirement (02 section 11.3). RF-off level: the acceptance criteria use -57 dBm, the value of REQ-SYS-183 marked TBR (close by PDR); a change returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2). Hazard controls exercised: HZ-003 (from the cited requirement; HZ-003 K9 in docs/safety/hazards.json). Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: every transmission goes into the 50 ohm dummy load or the calibrated power attenuator, connected before power-on, never into an open antenna port; key-down duty kept within the load rating recorded in the report; anyone other than the operator stays 0.6 m or more from the unit and load while keying and 1.0 m or more during a tune carrier (NGO-019); the bench supply current limit is set before each power-on; antistatic wrist strap while the lid is off; the PA area is not touched after key-down runs. Environment: room temperature 18 to 28 C; the pack is supplied by the bench supply at 7.4 V +/-0.05 V through the battery terminals unless a step sets another value; the calibrated power attenuator on the antenna port through the BNC T of the RF-present indicator.

**Procedure.**

1. Run the logic-capture reference pulse-train check of this session and record the result (docs/process/04-verification-and-validation.md section 4).
2. Measure the attenuator and cable S21 on the NanoVNA from 9 kHz (or the NanoVNA lower limit) to 1.5 GHz and save the Touchstone file; run the tinySA Ultra internal calibration-output check; record both.
3. Close the straight key for 3 s with the fixture at 90 C and confirm that the RF-present indicator channel is high with the carrier and low after it.
4. Threshold: with the fixture at 90 C, key down with the straight key; 1 s after key-down switch the fixture to T_trip; hold the key for a further 2 s; release.
5. Full over-temperature: with the fixture at 90 C, key down with the straight key; 1 s after key-down switch to 100 C; hold for a further 2 s; release.
6. Key-down while hot: with the fixture at 100 C in Receive, close the straight key for 3 s, then hold the paddle dah lever for 3 s.
7. Way down: with the fixture at 100 C, key down with the straight key, switch to T_trip after 1 s and hold for a further 2 s; release; then set 90 C and close the straight key for 3 s, and set 80 C and close it for 3 s again, recording whether the carrier returns at each.
8. Repeat the threshold and full over-temperature steps keyed with the paddle dah lever held at 15 WPM.
9. Repeat the full over-temperature step at 6.5 V and at 8.4 V.
10. Run tools/analyze_logic_capture.py: fixture-marker-to-RF-present-fall latency, PA_EN state at each fall, and RF-present activity while the fixture is at or above T_trip.
11. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
12. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if every threshold and full over-temperature run starts with the carrier present at the 90 C equivalent; after every switch to T_trip or 100 C during a key-down the RF-present indicator falls at most 100 ms after the fixture marker while PA_EN is still asserted by the firmware; and while the fixture stays at or above T_trip (including the key-downs begun at 100 C and the T_trip reading on the way down) the indicator stays low and no carrier above -57 dBm at the antenna port on the tinySA Ultra (the RF-off level of REQ-SYS-183) appears on the zero-span trace after the cut; otherwise Fail.

**Instruments and fixtures.**

- Pico-based logic capture (second Pico 2 with sigrok-pico firmware read by sigrok-cli; planned, ADR-009), 3.3 V inputs, 1 MS/s unless a step states otherwise
- NTC substitution fixture: fixed resistors at the temperature equivalents named in the steps, switched in place of the cell or PA sensor at its test pad, the switch's second pole wired to a logic-capture channel as the event marker (docs/vv/fixtures/ntc-substitution.md, planned)
- RF-present indicator: the diode RF probe (1N5711 or equivalent, printed housing, characterized by TC-SYS-010) on a BNC T at the attenuator input, its DC output through a resistive divider with a 3.3 V clamp to a logic-capture channel, sized so that a 0.5 W carrier reads logic high (docs/vv/fixtures/rf-present-indicator.md, planned); a timing indicator whose falling edge comes at or after the end of the RF, never a level measurement
- tinySA Ultra spectrum analyzer (ADR-021) through the calibrated 30 to 40 dB attenuator rated 10 W or more, attenuator S21 measured on the NanoVNA in the same session; level accuracy per its TV record
- NanoVNA, SOL calibration at the cable end used, checked on the dummy load
- Host computer with picotool and a serial terminal per tools/toolchain.lock.md, micro-USB cable
- 3.3 V USB-to-UART serial adapter between the host computer and the UART test pads, so that injection commands reach the unit with its USB port disconnected (docs/vv/fixtures/uart-adapter.md, planned)
- Owner's straight key and iambic paddle, 3.5 mm TRS plugs (SI-034)
- Adjustable bench supply, 0 to 30 V, current limit set per step

**Expected artifacts.**

- `hw-thermal-cutoff.csv` (csv): Run, supply, keying source, fixture equivalent, marker-to-RF-end latency, PA_EN at the fall, carrier on the way down
- `hw-thermal-ttrip.txt` (report): T_trip derivation from the sensor datasheet and fixture tolerances
- `hw-thermal-zero-span.png` (plot): tinySA zero-span traces per key-down
- `hw-thermal-capture.sr` (other): Raw logic capture

### TC-SYS-110: Independent frequency verification: no transmission unless the measured synthesizer output agrees with the set frequency within 10 kHz, before and during transmit

| Field | Value |
|---|---|
| Requirements | REQ-SYS-182, REQ-SYS-183 |
| Method / class | Test / Bench |
| Status | Draft |
| Automation | `tools/analyze_logic_capture.py` |

**Setup.** Article: CWHT-A-001, enclosure lid off for test-point access, running the fault-injection test build of release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (a build flavour of the release commit whose injection commands arrive over the UART test pads from the host serial terminal through the 3.3 V serial adapter, or over USB serial only in steps that expect no carrier, because USB VBUS sets the USB flag and the hardware transmit inhibit of REQ-SYS-092, and which toggles the injection-marker test pad at the instant of each injection); the release image is restored and checked with picotool verify at the end of the case. Configuration: fault-injection build with commands that program the synthesizer to 150.000 MHz, or 12 kHz above or below the set frequency, while the frequency-control state and the display keep the set frequency 146.000 MHz (the corrupted frequency word of HZ-008 cause C7), applied in Receive or 1 s into an over, and a command that stops the independent frequency measurement (no valid measurement); the release build for the agreement runs; antenna port through the BNC T of the RF-present indicator to the calibrated power attenuator and the tinySA Ultra; USB disconnected; tinySA in zero span at the frequency the synthesizer is programmed to (150.000 MHz, the offset frequency, or 146.000 MHz for the no-measurement runs), RBW 3 kHz, 5 s sweep started at each key-down or Tune confirmation; logic capture on the injection marker, PA_EN and the RF-present indicator, which responds to a carrier at any frequency; 0.5 W step. Each key closure or Tune attempt is one run: before it, any Fault-safe the previous run caused (REQ-SYS-154, TC-SYS-101) is cleared by removing the injection and acknowledging, and the injection for the run is then applied. The 100 ms window for the during-transmit runs is the time of REQ-SYS-182 (TBR), which covers detection and the REQ-SYS-004 fall. Credit row: T-HW. Test of a system requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the campaign (section 13) and witnessed by the owner; the pre-build Simulation, HostUnit and Emulation evidence named in each requirement's verification_note is supporting only and is not part of this case. TBR values: the acceptance criteria use the values of REQ-SYS-182 as written, 10 kHz and 100 ms marked TBR (close by SRR, package decision 40 with decision 9; confirmed by the PDR prescaler, counter and timebase design, TS-002); a change returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071), and if the owner declines the verification this case is retired with the requirement (02 section 11.3). RF-off level: the acceptance criteria use -57 dBm, the value of REQ-SYS-183 marked TBR (close by PDR); a change returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2). Hazard controls exercised: HZ-008 (from the cited requirement; HZ-008 K7 in docs/safety/hazards.json). Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: every transmission goes into the 50 ohm dummy load or the calibrated power attenuator, connected before power-on, never into an open antenna port; key-down duty kept within the load rating recorded in the report; anyone other than the operator stays 0.6 m or more from the unit and load while keying and 1.0 m or more during a tune carrier (NGO-019); the bench supply current limit is set before each power-on; antistatic wrist strap while the lid is off; the PA area is not touched after key-down runs. A failed inhibit puts a 0.5 W carrier at 150.000 MHz into the attenuator only; the antenna port is never open during this case. Environment: room temperature 18 to 28 C; the pack is supplied by the bench supply at 7.4 V +/-0.05 V through the battery terminals unless a step sets another value; the calibrated power attenuator on the antenna port through the BNC T of the RF-present indicator.

**Procedure.**

1. Run the logic-capture reference pulse-train check of this session and record the result (docs/process/04-verification-and-validation.md section 4).
2. Measure the attenuator and cable S21 on the NanoVNA from 9 kHz (or the NanoVNA lower limit) to 1.5 GHz and save the Touchstone file; run the tinySA Ultra internal calibration-output check; record both.
3. Close the straight key for 3 s at 146.000 MHz and confirm that the RF-present indicator channel is high with the carrier and low after it.
4. Before transmit, gross error: at 146.000 MHz, with the 150.000 MHz command applied in Receive before each run, close the straight key for 3 s, then hold the paddle dah lever for 3 s, then select Tune with its confirmation; record the indicator, PA_EN, the zero-span trace at 150.000 MHz and the display for each.
5. Before transmit, window: repeat the straight-key and paddle runs of the previous step with the synthesizer 12 kHz above, and then 12 kHz below, the set frequency, the zero span at the offset frequency.
6. Before transmit, no measurement: with the synthesizer correct and the frequency measurement stopped in Receive before each run, close the straight key for 3 s, then hold the paddle dah lever for 3 s.
7. During transmit, gross error: key down with the straight key, apply the 150.000 MHz command 1 s into the over and hold the key for a further 3 s; repeat keyed with the paddle dah lever held.
8. During transmit, window and no measurement: repeat the previous step with the 12 kHz above offset (straight key), the 12 kHz below offset (paddle) and the measurement stopped 1 s into an over (straight key).
9. Agreement (positive control): restore the release image and check it with picotool verify; disconnect USB; at 144.001, 146.000 and 147.999 MHz close the straight key for 3 s and hold the paddle dah lever for 3 s; read the carrier marker on a 20 kHz span.
10. Run tools/analyze_logic_capture.py: indicator and PA_EN activity in every before-transmit run, and marker-to-RF-present-fall latency in every during-transmit run.
11. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
12. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if in every before-transmit run (150.000 MHz, 12 kHz above, 12 kHz below and no measurement; straight key, paddle and, for 150.000 MHz, Tune) the RF-present indicator stays low and no carrier at the programmed frequency above -57 dBm at the antenna port on the tinySA Ultra (the RF-off level of REQ-SYS-183) appears on the zero-span trace; in every during-transmit run the indicator falls at most 100 ms after the injection marker and the zero-span trace shows no carrier above -57 dBm at the antenna port (the RF-off level of REQ-SYS-183) from then to the end of the key-down; and in the agreement runs the carrier is present at each of the three frequencies with both key types; otherwise Fail.

**Instruments and fixtures.**

- Pico-based logic capture (second Pico 2 with sigrok-pico firmware read by sigrok-cli; planned, ADR-009), 3.3 V inputs, 1 MS/s unless a step states otherwise
- RF-present indicator: the diode RF probe (1N5711 or equivalent, printed housing, characterized by TC-SYS-010) on a BNC T at the attenuator input, its DC output through a resistive divider with a 3.3 V clamp to a logic-capture channel, sized so that a 0.5 W carrier reads logic high (docs/vv/fixtures/rf-present-indicator.md, planned); a timing indicator whose falling edge comes at or after the end of the RF, never a level measurement
- tinySA Ultra spectrum analyzer (ADR-021) through the calibrated 30 to 40 dB attenuator rated 10 W or more, attenuator S21 measured on the NanoVNA in the same session; level accuracy per its TV record
- NanoVNA, SOL calibration at the cable end used, checked on the dummy load
- Host computer with picotool and a serial terminal per tools/toolchain.lock.md, micro-USB cable
- 3.3 V USB-to-UART serial adapter between the host computer and the UART test pads, so that injection commands reach the unit with its USB port disconnected (docs/vv/fixtures/uart-adapter.md, planned)
- Owner's straight key and iambic paddle, 3.5 mm TRS plugs (SI-034)
- Adjustable bench supply, 0 to 30 V, current limit set per step

**Expected artifacts.**

- `freq-verify-runs.csv` (csv): Run, timing (before or during), injected error, keying source, indicator activity, PA_EN, latency, carrier level
- `freq-verify-zero-span.png` (plot): tinySA zero-span traces per run
- `freq-verify-capture.sr` (other): Raw logic capture
