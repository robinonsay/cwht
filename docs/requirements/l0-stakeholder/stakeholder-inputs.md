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
