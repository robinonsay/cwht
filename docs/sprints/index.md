# Software sprints

Index of the software sprints of 07 section 3.4 (Phases 0 to 5). One record per sprint in `docs/sprints/SW-NN-<module>.md`; a sprint delivers one `cwht-core` module or one rustos work package (07 section 19). Charter section 5 row "Software sprint records and measurements (SWE-090)".

| Sprint | Module | Work package | Increment | Design record | Product | Status |
|---|---|---|---|---|---|---|
| [SW-01](SW-01-wp-sw-11-clocks.md) | Clocks and PLL: crystal, PLL_SYS 150 MHz, clk_ref, clk_sys, clk_peri, TIMER0 and watchdog ticks | WP-SW-11 (WP-PDR-41) | FW-B1 | ADR-051 | rustos `cwht/wp-sw-11` at `4a8e825` (revision 2; revision 1 `213c536`) | Open (phase 1 done 2026-09-27; revision 2 for the iteration 1 Majors) |
| [SW-02](SW-02-wp-sw-09-interrupts.md) | Critical section and NVIC helpers: overridable IRQ vectors, one-priority NVIC, `CsCell` | WP-SW-09 (WP-PDR-41) | FW-B1 | ADR-052 | rustos `cwht/wp-sw-09` at `c6e5100` (revision 2; revision 1 `9305f59`) | Open (phase 1 done 2026-09-27; revision 2 for the iteration 1 Majors) |
| [SW-03](SW-03-wp-sw-01-timer0.md) | Time base and alarms: `api::time`, TIMER0 clock and four alarms, timer register ICD | WP-SW-01 (WP-PDR-41) | FW-B1 | ADR-053 | rustos `cwht/wp-sw-01` at `58fe739` (revision 2; revision 1 `a1cd160`) | Open (phase 1 done 2026-09-27; revision 2 for the iteration 1 Majors) |
| [SW-04](SW-04-wp-sw-02-sio-snapshot.md) | GPIO input sampling through SIO: `InputSnapshot`, one `GPIO_IN` read per group | WP-SW-02 (WP-PDR-41) | FW-B1 | ADR-054 | rustos `cwht/wp-sw-02` at `38434b2` (revision 2; revision 1 `f85a190`) | Open (phase 1 done 2026-09-27; revision 2 for the iteration 1 Majors) |
| [SW-05](SW-05-wp-sw-03-pwm.md) | PWM: `api::pwm`, one output per slice on slices 0 to 7, PWM register ICD | WP-SW-03 (WP-PDR-41) | FW-B1 | ADR-055 | rustos `cwht/wp-sw-03` at `48e07ec` (revision 2; revision 1 `6df18af`) | Open (phase 1 done 2026-09-27; revision 2 for the iteration 1 Majors) |

The five rustos branches are stacked in merge order: `cwht/l-016-6` (`5b39e8e`, SRR lien L-016-6) under `cwht/wp-sw-11`, then `cwht/wp-sw-09`, `cwht/wp-sw-01`, `cwht/wp-sw-02`, `cwht/wp-sw-03`. Each branch builds and passes its tests on its own.
