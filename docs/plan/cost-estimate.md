# cwht Cost Estimate (rough order of magnitude)

Tailored replacement for NPR 7150.2D SWE-015/SWE-151 (see `docs/process/rmm.json`): a labor-free model covering fabrication, assembly, enclosure, non-sourced parts and instruments, with contingency, plus the life-cycle reserves for one rework spin and spares. Updated at every gate; vendor quotes replace estimates at PDR (enclosure) and CDR (PCB, assembly, parts).

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
| Life-cycle reserve, outside the unit budget and the total envelope: rework spin (rev B) fabrication plus assembly | 300 | 800 | RSK-014 consequence (second spin USD 300 to 800, 6 to 12 weeks); drawn only if a rev B is ordered; within the ADR-025 cap of five complete units |
| Life-cycle reserve, outside the unit budget and the total envelope: rework spares (extra quantities of hand-soldered and rework-prone parts, connectors, fuses, one spare cell set) | 40 | 120 | Catalog estimate without quotes; replaced by the BOM spares column at CDR. The two unassembled bare boards of ADR-025 are the board spares and are already in the fabrication line |
| **Life-cycle total (SWE-151 basis)** | **1312** | **2756** | Total envelope plus the two reserve lines |

Notes: AI compute is not costed. Fit-check prints on the owner's Bambu H2C use owned filament.

Life-cycle reserves (revised 2026-09-26 for INSP-023 finding-2). The rework spin and spares lines make the model cover the whole life cycle claimed for NPR 7150.2D SWE-151 a and the risk and uncertainty of SWE-151 d: the rework spin is priced from the RSK-014 consequence, which the 20 % unit contingency (USD 138 to 274) does not cover. Both lines sit outside the TPM-014 unit basis and outside the total envelope, so TPM-014 and the totals the SEMP cites are unchanged. The reserves carry no separate contingency: the rework spin is itself a risk reserve priced as a range, and the spares line is the reserve for rework. A draw on either line spends money and is recorded by an ADR decided by the owner (`docs/process/06-risk-and-decision-analysis.md` section 14.1 class 2); a rev B order is re-estimated from its own vendor quotes.
