# cwht — pocket 2 m true-CW handheld transceiver

A 5 W, true-CW (A1A) handheld for the 144 MHz amateur band, controlled by a
Raspberry Pi Pico 2 running firmware built on [rustos](../rustos). Rev A is
2 m only; the architecture reserves a path to 70 cm in a later revision.

Goal: a PCBWay-assembled board plus a PCBWay-machined aluminum enclosure that
work on first power-on, proven beforehand by SPICE analysis, host-side tests,
and whole-firmware emulation.

## Layout

```
docs/requirements/   requirements.json per module (authoritative) + rendered .md
docs/test_cases/     verification cases traced to requirement IDs
docs/decisions/      architecture decision records (ADR-NNN)
docs/plan/           phase plan, gates, status
docs/research/       research reports that ground the decisions
docs/icd/            interface control: pin maps, connectors, register maps
hardware/sim/        LTspice models and automated pass/fail checks
hardware/kicad/      schematic and PCB
hardware/enclosure/  OpenSCAD sources and exports for CNC
hardware/bom/        DigiKey / PCBWay bills of materials
firmware/            Rust application crate (depends on ../rustos by path)
tools/               scripts: traceability, sim runners, export pipelines
```

## License and status

Open source under the MIT License (see `LICENSE`). Engineered under the NASA systems and software engineering processes at Class A rigor; see `docs/process/00-charter.md` for the process charter and `docs/plan/schedule.md` for the gate schedule. Reference corpus conversions of NASA documents under `docs/references/md/` are US Government works.
