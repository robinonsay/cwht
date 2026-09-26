# cwht Cost Estimate (rough order of magnitude)

Tailored replacement for NPR 7150.2D SWE-015/SWE-151 (see `docs/process/rmm.json`): a labor-free model covering fabrication, assembly, enclosure, non-sourced parts and instruments, with contingency. Updated at every gate; vendor quotes replace estimates at PDR (enclosure) and CDR (PCB, assembly, parts).

Basis: three radios (owner plus friends), 5 bare boards minimum order, USD, 2026-09-25 estimate without quotes; revised 2026-09-26 (SEMP Appendix F item F-13): the tinySA Ultra line is committed and sits outside the unit budget, and each contingency is exactly 20 %.

| Item | Low | High | Basis |
|---|---|---|---|
| PCBWay 4-layer fabrication, 5 boards | 60 | 120 | Typical small-run 4-layer pricing incl. shipping |
| PCBWay turnkey assembly, 3 boards incl. parts, stencil, setup | 300 | 500 | ~80 to 120 USD parts per board plus assembly labor and setup |
| PCBWay CNC aluminum enclosure, 3 sets, anodized | 250 | 600 | Small 6061 machined parts with finishing |
| DigiKey and other items not sourced by PCBWay (Li-ion cells, antennas, knobs, cables, pack hardware) | 80 | 150 | Catalog prices |
| **Unit subtotal (three complete units, ADR-025)** | **690** | **1370** | Sum of the four lines above |
| Contingency 20 % on the unit subtotal | 138 | 274 | Exactly 20 % |
| **Unit budget total (TPM-014 basis)** | **828** | **1644** | Unit subtotal plus contingency; SEMP section 7 resources paragraph |
| Instrument, outside the unit budget: tinySA Ultra spectrum analyzer with attenuator for spurious verification | 120 | 160 | Committed by the owner (SI-034, ADR-021); not an option any more |
| Contingency 20 % on the instrument line | 24 | 32 | Exactly 20 % |
| **Total envelope** | **972** | **1836** | Unit budget total plus the instrument line and its contingency |

Notes: AI compute is not costed. Fit-check prints on the owner's Bambu H2C use owned filament. A second board spin (rev B), if needed, would repeat the fabrication and assembly lines.
