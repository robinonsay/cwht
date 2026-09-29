# hardware/sim/tx-pa-permit: the D-18 PA-permit gate and the A5 key-up case (WP-PDR-22)

LTspice transients of the D-18 PA-permit gate of TS-012 revision 7 (the hardware AND of TX_KEY, PA_EN and the
cutoff monostable Q that powers the GVA-84+ driver and releases the VGG clamp), for the chosen design A5
(RA07M1317M module). They close, as analysis, the D-18 lien (INSP-118 finding-9, INSP-110 finding-24): the
gate's supply rail, its level interface to the 5 V P-FET and its unpowered state, and they rerun the key-up case
of REQ-TX-014 with the gate. Analysis record: `docs/design/analysis/pa-permit-gate-d18.md`.

| File | What it is |
|---|---|
| `d18_run.py` | Generator, runner and checker: writes the decks, runs them through `tools/ltspice-batch.sh`, reads the `.raw` with spicelib, computes every criterion per case, the antenna level for four isolation cases from the simulated driver supply and VGG, writes `result.json` and `result.csv`, draws the plots |
| `d18_keyup.cir` | The gate as fixed (design D18-2B): one element and the key-up window with PA_EN asserted and CLK1 running, 52 corner cases (generated) |
| `d18_asis.cir` | The gate as TS-012 revision 7 draws it (3.3 V NAND output straight to the P-FET gate and the clamp gate), 36 cases (generated) |
| `d18_seq.cir` | D18-2B power-up orders, brown-outs, single-line and single-component faults, 13 cases (generated) |
| `results/<run-id>/` | One folder per run: deck, LTspice `.log`, `.raw` (or `raw.sha256` for a `.raw` over 5,000,000 bytes, CR-017 C2), wrapper output, `result.json`, `result.csv`, plots, the script as run |

Run (LTspice only through the accredited wrapper, ACC-LTSPICE-001):

```
.venv/bin/python hardware/sim/tx-pa-permit/d18_run.py keyup
.venv/bin/python hardware/sim/tx-pa-permit/d18_run.py asis
.venv/bin/python hardware/sim/tx-pa-permit/d18_run.py seq
.venv/bin/python hardware/sim/tx-pa-permit/d18_run.py summary
.venv/bin/python hardware/sim/tx-pa-permit/d18_run.py replot keyup     # re-analyse an existing run, no LTspice
```

Exit status: 0 when every criterion the design must pass passes and every expected state (the as-drawn defect,
the component-fault cases) is as the record states; 3 otherwise (printed and in `result.json`); 2 on a tool
error.

## Runs

See the record, section 5, for the numbers; each run's `result.json` holds every case and criterion.

| Run | What | Result |
|---|---|---|
| `2026-09-29-d18-keyup` | D18-2B, 52 cases (bus 4.75 / 5.25 V, 3V3 and GPIO high 3.0 / 2.62 and 3.6 / 3.6 V, P-FET threshold -0.73 / -1.0 / -2.1 V, 2N3904 beta 70 / 416, error amplifier nominal or wound to the rail, 4 interval-13 fallback cases) | Every criterion PASS in every case: driver powered 0.5 to 1.2 us after the permit; VGS permitted -4.26 to -4.71 V, drop at most 11 mV; key-up VGS 0.0 V, driver supply 0.4 mV, under 0.1 V 0.78 ms after TX_KEY falls; clamp gate at least 4.75 V, VGG at most 7.9 mV with the amplifier at its rail. REQ-TX-014 key-up level L1 -58.3, L2 -38.8, L3 -88.3, L4 -34.0 dBm against -30 dBm. `keyup_timeline.png`, `keyup_edges.png`, `keyup_metrics.png`, `level_cases.png`. `.raw` over 5,000,000 bytes: kept, `raw.sha256` |
| `2026-09-29-d18-asis` | As drawn in TS-012 revisions 7 and 8 (3.3 V NAND output on the P-FET gate), 36 cases | Expected defect reproduced: driver powered (4.08 to 5.20 V) at key-up in 25 of 36; REQ-TX-014 fails (L1) in 21 of 36, up to -14.7 dBm. `asis_keyup.png`, `asis_timeline.png`. `.raw` over 5,000,000 bytes: kept, `raw.sha256` |
| `2026-09-29-d18-seq` | D18-2B sequencing and faults, 13 cases, error amplifier wound to the rail | Every design case PASS (either power-up order, 3V3 and 5 V brown-outs, monostable expiry, PA_EN cleared with TX_KEY stuck, each line stuck alone, U1 output open); the four component faults as expected (one output lost, the other acting). `seq_cases.png` |
| `2026-09-29-d18-summary` | Isolation cases, break-even isolation, static datasheet checks | `summary.json`: break-even combined off-state isolation 21.2 dB (design drive) and 26.0 dB (drive bound); 15 static interface checks PASS; exit 0 |
