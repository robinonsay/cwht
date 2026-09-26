# cwht Cost Estimate (rough order of magnitude)

Tailored replacement for NPR 7150.2D SWE-015/SWE-151 (see `docs/process/rmm.json`): a labor-free model covering fabrication, assembly, enclosure, non-sourced parts and instruments, with contingency. Updated at every gate; vendor quotes replace estimates at PDR (enclosure) and CDR (PCB, assembly, parts).

Basis: three radios (owner plus friends), 5 bare boards minimum order, USD, 2026-09-25 estimate without quotes.

| Item | Low | High | Basis |
|---|---|---|---|
| PCBWay 4-layer fabrication, 5 boards | 60 | 120 | Typical small-run 4-layer pricing incl. shipping |
| PCBWay turnkey assembly, 3 boards incl. parts, stencil, setup | 300 | 500 | ~80 to 120 USD parts per board plus assembly labor and setup |
| PCBWay CNC aluminum enclosure, 3 sets, anodized | 250 | 600 | Small 6061 machined parts with finishing |
| DigiKey and other items not sourced by PCBWay (Li-ion cells, antennas, knobs, cables, pack hardware) | 80 | 150 | Catalog prices |
| Optional: tinySA Ultra spectrum analyzer for spurious verification | 120 | 160 | Owner decision open (see SI-021) |
| Contingency 20 % | 160 | 300 | Applied to the above |
| **Total** | **970** | **1830** | |

Notes: AI compute is not costed. Fit-check prints on the owner's Bambu H2C use owned filament. A second board spin (rev B), if needed, would repeat the fabrication and assembly lines.
