# Stakeholder inputs log (raw, dated, verbatim intent)

Source record for the Stakeholder Expectations Definition process (SE HB §4.1). Each entry is
the owner's stated expectation as received; NGOs, MOEs and requirements trace back to these
entries by `SI-NNN`. Entries are never edited after the fact; clarifications get new entries.

| ID | Date | Input (owner, Robin) |
|---|---|---|
| SI-001 | 2026-09-25 | Pocket-sized handheld true-CW (A1A) amateur transceiver; "handy-talkie" form factor. |
| SI-002 | 2026-09-25 | 2 m band for the first iteration; 70 cm deferred to a later revision but keep the path open. |
| SI-003 | 2026-09-25 | 5 W transmit power, chosen for useful simplex range. |
| SI-004 | 2026-09-25 | Narrow-bandwidth true CW (not tone-modulated FM) for propagation advantage. |
| SI-005 | 2026-09-25 | Operate with headphones plugged in and a key plugged in; tune to a frequency and chat with friends. |
| SI-006 | 2026-09-25 | Controls kept minimal: band (future), volume, tuning; a small LCD; tuning via a knob (rotary encoder accepted in place of a potentiometer). |
| SI-007 | 2026-09-25 | Raspberry Pi Pico 2 as the controller; firmware in Rust built on the owner's `rustos`. |
| SI-008 | 2026-09-25 | Fits an aluminum enclosure with the antenna on one end; enclosure designed in OpenSCAD and CNC-machined by PCBWay. |
| SI-009 | 2026-09-25 | Fully assembled PCB from PCBWay turnkey (no hand soldering); parts from DigiKey or equivalent. |
| SI-010 | 2026-09-25 | Must work at first power-on: all SPICE analysis, host tests and firmware emulation done beforehand to prove it. |
| SI-011 | 2026-09-25 | Owner does no coding and no PCB layout; Claude produces everything, owner reviews. |
| SI-012 | 2026-09-25 | Owner has a Bambu Lab H2C printer with AMS: printed facade, knobs, fit-check parts are welcome. |
| SI-013 | 2026-09-25 | Bench gear available: NanoVNA, 50 Ω dummy load (BNC), adjustable bench supply; no oscilloscope or spectrum analyzer. |
| SI-014 | 2026-09-25 | Owner holds a US General-class license; operate under 47 CFR Part 97. |
| SI-015 | 2026-09-25 | Process: NASA SE Handbook + NPR 7150.2D at Class A / Crit-1 rigor; gates SRR, PDR, CDR (procurement release), V&V plan/TRR, acceptance review; owner dispositions with RFAs/RIDs. |
| SI-016 | 2026-09-25 | Visual products must be rendered to images and inspected by Claude before iteration. |
| SI-017 | 2026-09-25 | Use vectorized search (Claude Context) across the repo and reference corpus to conserve tokens. |
| SI-018 | 2026-09-25 | **Core requirement:** the radio shall support both a straight key and iambic paddles (built-in electronic keyer). |
| SI-019 | 2026-09-25 | Hand the finished radios to friends so several people can operate together ("play radio"). |
| SI-020 | 2026-09-25 | Owner approved the expedited schedule and plan: SRR Sat morning, PDR Sat evening, CDR Sun evening with procurement release Sunday night; liens on PDR products acceptable when CDR closes them; three owner review windows accepted. |
| SI-021 | 2026-09-25 | Open owner decision: purchase of a tinySA Ultra spectrum analyzer for spurious-emission verification (otherwise spurious compliance rests on analysis or a borrowed instrument). |
| SI-022 | 2026-09-25 | USB strategy: use the Pico 2 module's micro-USB connector for both firmware loading and battery charging (single connector, simplest). |
| SI-023 | 2026-09-25 | Battery: two 18650 Li-ion cells (2S) in a holder so cells are user-replaceable. |
| SI-024 | 2026-09-25 | Frequency coverage: the full US 2 m band, 144.000 to 148.000 MHz. |
| SI-025 | 2026-09-25 | The project is open source under the MIT license at https://github.com/robinonsay/cwht; anyone may use it. |
| SI-026 | 2026-09-25 | Software verification approach: layer the software with dependency injection on the rustos api traits so the same application code runs on a macOS/Linux host implementation and on the Cortex-M33; test application logic on the host; test hardware integration on real hardware. Drivers are traced to the RP2350 datasheet and Cortex-M33 documentation as the hardware ICD. Emulation is optional, not the primary evidence. |
| SI-027 | 2026-09-25 | LTspice telemetry opt-out (CaptureAnalytics=false in the LTspice settings) ratified by the owner. |
| SI-028 | 2026-09-25 | Power amplifier device must be readily sourced from DigiKey, Mouser or PCBWay's turnkey distributors; no bespoke or consignment-only parts. |
| SI-029 | 2026-09-25 | Synthesizer choice: perform a cost and performance trade; if costs are similar, choose the best-performing synthesizer for this application. |
| SI-030 | 2026-09-25 | All operators (owner and friends) hold at least a Technician license; controlled/occupational RF exposure limits apply to operators; bystander (general population) limits still apply to non-operators nearby. |
| SI-031 | 2026-09-25 | Kit assembly model accepted: PCBWay assembles all surface-mount parts; the owner is willing to hand-solder through-hole components and simple pads (no BGA/QFN or other hidden-pad packages). |
| SI-032 | 2026-09-25 | FreeCAD installation via Homebrew approved for headless OpenSCAD-to-STEP export. |
| SI-033 | 2026-09-25 | Keyer speed range 5 to 50 WPM accepted. New peripheral drivers are developed upstream in rustos (the owner's OS), not in a cwht-local crate. |
| SI-034 | 2026-09-25 | Owner's straight key and paddle both use standard 3.5 mm TRS (aux) plugs; brands unknown. Battery-life target accepted: 8 h at a 1:9 transmit-to-receive ratio. Owner will purchase a tinySA Ultra spectrum analyzer. |
| SI-035 | 2026-09-25 | Open: full QSK versus semi break-in awaits the owner's understanding of the trade (explained 2026-09-25); build quantity recommendation (5 bare boards, 3 assembled, at most 5 complete units) stands unless the owner objects. |
| SI-036 | 2026-09-25 | Break-in: semi break-in only. The operator hears their own sidetone while sending and the radio returns to receive after an adjustable hang time; full QSK (hearing between elements) is explicitly not wanted. Closes the open item in SI-035. |
