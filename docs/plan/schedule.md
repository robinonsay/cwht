# cwht Schedule Baseline (expedited)

**Approved by owner:** 2026-09-25 (Friday). Goal: procurement release (CDR approval) by Sunday 2026-09-27 evening; vendor orders placed Sunday night. Reviews are event-based (NPR 7123.1D §5.1.5); the dates below are targets, and a gate is held only when its entrance criteria in `docs/process/01-lifecycle-and-reviews.md` are met.

| Target | Phase work | Gate / product |
|---|---|---|
| Fri 2026-09-25 evening to Sat morning | ConOps, NGOs/MOEs, L1 requirements, hazard analysis, RMM, risk register, SEMP, V&V approach, research findings, toolchain proof | **SRR** package ready Sat morning; owner review about 1 h |
| Sat 2026-09-26 day | Architecture trade studies (receiver topology, synthesizer, PA, T/R), L2 requirements, ICDs, block-level LTspice with pass/fail checks, V&V plan, integration plan, enclosure envelope | **PDR** package Sat evening; owner review 1 to 2 h; liens permitted where CDR completes the product |
| Sat night to Sun 2026-09-27 afternoon | Full schematic, 4-layer layout, enclosure CAD and STEP, complete analysis package, BOM with live stock checks, fabrication and assembly package, firmware architecture and emulation plan, first-power-on procedure | **CDR** package Sun evening; owner review about 2 h |
| Sun 2026-09-27 night | PCBWay fabrication, assembly and CNC orders; DigiKey order for items PCBWay does not source | **Procurement release** |
| Vendor lead time, 2 to 4 weeks | Firmware implementation, host tests, emulation scenarios, fit-check prints, receipt inspection | **TRR** on board arrival, then V&V execution and **SAR** |

## Schedule risks and levers

1. RID volume at each gate drives re-review cycles (hours each); Claude pre-briefs the top open questions with each package.
2. Layout is the longest single task (Sat night); visual-closure iterations and DRC are planned into it.
3. Live stock checks at CDR may force substitutions; long-lead parts trigger an immediate decision request to the owner.
4. Firmware proof (emulation) continues during vendor lead time and does not gate the hardware order.

Liens policy: a PDR product may be baselined "with liens" when the lien has an owner, a closure plan and a closure gate (CDR). No liens are carried past CDR into procurement without an explicit owner decision recorded in the CDR decision memo.
