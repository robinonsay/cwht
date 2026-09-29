# rx-frontend: receiver band-pass filter, image, half-IF and cascade (TS-012 pre-order item, WP-PDR-19)

Owner of the block: Claude (analysis author invocation, 2026-09-28). Analysis record:
`docs/design/analysis/rx-bpf-ts012.md`. Every LTspice run goes through `tools/ltspice-batch.sh`
(ACC-LTSPICE-001); every `.raw` is read with spicelib 1.6.3 in the repo venv.

## Files

| File | What it does |
|---|---|
| `bpf_design.py` | Coupled-resonator synthesis (shunt LC resonators, top-C coupling, series-C end coupling) from Chebyshev 0.1 dB g-values; writes the LTspice lines of one section |
| `explore.py` | Numpy nodal pre-check used only to pick which designs to simulate (not evidence) |
| `make_decks.py` | Writes every deck in `decks/` (filter Q sweeps, Monte Carlo modes A and B with fixed seeds, leakage, ring and JFET half-IF) |
| `run_sims.py` | Runs the decks through the wrapper into `results/<run-id>/` and copies deck, draws or cases and scripts there |
| `check_bpf.py` | Filter checker: passband loss, image rejection (IF 8 and 10 MHz), half-IF filter attenuation, IF feed-through; plots |
| `check_halfif.py` | Mixer checker: conversion gain, half-IF (2RF - 2LO) response vs level, intercept, numerical floor; plot |
| `cascade.py` | NF, gain and MDS cascade (revision 2: TC-SYS-017 corner losses, J310 port case, TPM-005 thresholds); half-IF referral; verdicts; plots. Exit 1 when REQ-SYS-022 fails at the corner for the proposed configuration |
| `bpf_nodal.py` | Numpy nodal AC solver that parses the same netlist lines as the decks (search tool of revision 2; agreement with LTspice checked in r07) |
| `tolerance.py` | Tolerance boxes (modes A and B), alignment models (none, aligned at 50 ohm, aligned in circuit), port model, vertex corner search, binomial bounds; from revision 4 an exact frequency map for the residual, a post-alignment temperature drift range and a capacitor-box widening (options; the defaults keep r08 to r12 unchanged) |
| `worst_case.py` | Revision 2 runs r08 (Monte Carlo 20,000 and worst-case corners), r09 (J310 port impedances, VSWR design input), r10 (leakage at the corners), revision 3 run r12 (alignment residual limit at the design-input corner) and revision 4 run r13 (REQ-SYS-114 temperature after a room-temperature alignment): `prepare` writes the decks, `check` reads the LTspice `.raw`, compares with the numpy prediction (0.01 dB) and plots. Exit 1 when the proposed filter fails its acceptance (2 + 3 + 3 in r08 to r12; the design 2 + 3 + 4 in r13) |
| `validate_nodal.py` | Run r07: numpy solver against every step of r01 to r04 (acceptance 0.01 dB) |

Reproduce (revision 1): `.venv/bin/python hardware/sim/rx-frontend/make_decks.py`, then `run_sims.py`, then
`check_bpf.py results/<run-id>` for r01 to r04, `check_halfif.py results/2026-09-28-r05-halfif-mixers`.
Revision 2: `validate_nodal.py` (r07); `worst_case.py prepare r08`, `run_sims.py 2026-09-28-r08-bpf-tolerance-corners`,
`worst_case.py check r08`, and the same for r09 and r10; then `cascade.py` (writes r11; r06 keeps the revision 1 script).
Revision 3: `worst_case.py prepare r12` (about 17 minutes on 12 processes), `run_sims.py 2026-09-28-r12-bpf-residual-design-input`, `worst_case.py check r12`.
Revision 4: `worst_case.py prepare r13` (about 19 minutes on 13 processes), `run_sims.py 2026-09-29-r13-bpf-temperature`, `worst_case.py check r13`.

Exit statuses (review finding 4): `check_bpf.py` exits 1 on any REQ-SYS-033 FAIL in its run, so r01, r02 and r03 exit 1
by design (the TS-012 2 + 3 filter, and 2 + 3 + 2 at IF 8, fail); r04 exits 0. `worst_case.py check` exits 0 for r08,
r09, r10 and r12 (the then-proposed 2 + 3 + 3 meets each run's acceptance at the alignment temperature, with the margins below; in r12 only up to a residual of +/-0.32 %) and for r13 (the design 2 + 3 + 4 meets REQ-SYS-033 over REQ-SYS-114). `cascade.py` exits 1:
REQ-SYS-022 fails at the TC-SYS-017 corner. `validate_nodal.py` exits 0.

## Runs

| Run | Content | Result (details in each `result.md`) |
|---|---|---|
| `results/2026-09-28-r01-bpf-ts012-baseline/` | TS-012 BPF1 2 + BPF2 3 resonators, 5 and 6 MHz design, coil Q 100/120/150/200; Monte Carlo 200 runs mode A (TS-012: 20 % capacitors) and mode B (proposed part spec) | **FAIL** REQ-SYS-033 at IF 8 MHz: 51 to 61 dB nominal at every Q, 39 dB (mode A) and 46 dB (mode B) Monte Carlo minimum. At IF 10 MHz 65 to 74 dB nominal, mode B minimum 60 dB: FAIL |
| `results/2026-09-28-r02-bpf-three-section/` | 2 + 3 + 2 and 2 + 3 + 3 resonators (BPF3 between the second J310 and the ring), 6 MHz, Q sweep | 2+3+3: **PASS** 86.0 dB at Q 100 (89.8 at Q 200), IF 8. 2+3+2: FAIL at IF 8 (67.8 dB at Q 100), PASS at IF 10 (86.7 dB) |
| `results/2026-09-28-r03-bpf-three-section-mc/` | Monte Carlo 200 runs, modes A and B, of 2+3+2 and 2+3+3 | Sample minima only (revision 2 wording): 2+3+3 at IF 8 no run below 70 dB in 200 (minimum 70.6 dB mode A, 78.1 dB mode B); 2+3+2 at IF 10 minimum 70.6 (A) and 80.5 (B). **The revision 1 "PASS" for mode A is withdrawn**: r08 shows 0.32 % of mode A builds below 70 dB and a 49.1 dB worst-case corner |
| `results/2026-09-28-r04-bpf-leakage/` | 2+3+3 at Q 100 with a stray input-to-output capacitance of 0.003 to 0.1 pF across each section, both leakage phases | Worst case 78.2 dB at 0.1 pF per section (PASS 70 dB); a whole-chain leak is not in this model (see the record) |
| `results/2026-09-28-r05-halfif-mixers/` | Transient: diode ring (4 x 1N5711, Si5351 square LO +10 dBm, duty 45/50/55 %, diode and winding mismatch) and a representative single-J310 mixer (A4, one deck per case, 16 cases) with wanted (144 MHz) and half-IF (140 MHz) tones | Ring: Gc -5.14 dB, half-IF IIP2 51.8 to 63.6 dBm mismatched (matched: at the -77.8 dBc time-step floor, IIP2 67.8 dBm or more). JFET: IIP2 30.1 to 30.4 dBm; 8 of 16 cases did not converge (logs gzip-compressed) |
| `results/2026-09-28-r06-cascade/` | Python cascade (NF, gain, MDS in 500 Hz) with the r01 to r03 losses and r05 mixer data; half-IF referral; isolation needed | Superseded by r11 (kept as the revision 1 record). 2+3+3 with the ring: NF 5.81 dB, MDS -141.2 dBm nominal, -139.1 dBm at the Monte Carlo p95 filter case. Half-IF at -70 dBm: -177 dBm equivalent (ring), -156 dBm (JFET): PASS. Isolation needed antenna to mixer at the image: 84 dB |
| `results/2026-09-28-r07-nodal-validation/` | Numpy nodal solver against LTspice on all 1,224 filter steps of r01 to r04 (acceptance 0.01 dB) | **ACCEPTED**: largest difference 2.5e-3 dB (S21), 1.8e-3 dB (image rejection) |
| `results/2026-09-28-r08-bpf-tolerance-corners/` | Finding 1. Numpy Monte Carlo 20,000 runs and the worst-case corner (vertex search plus interior check) of each tolerance box, for 2+3, 2+3+3, 2+3+4 (IF 8) and 2+3+2 (IF 10); modes A and B; revision 1 model (no re-alignment) and aligned at 50 ohm; every corner re-simulated in LTspice; LTspice Monte Carlo 1,000 runs of 2+3+3 | 2+3+3 at IF 8, worst-case corner: mode A 49.1 dB (**FAIL**; 0.32 % of 20,000 builds below 70 dB) and mode B 67.2 dB (**FAIL**) without re-alignment; aligned at 50 ohm: mode A 70.1 dB, mode B **75.6 dB (PASS)**. 2+3+4: 91.4 dB. 2+3+2 IF 10: 78.9 dB. LTspice agrees with every numpy corner to 0.01 dB |
| `results/2026-09-28-r09-bpf-port-impedance/` | Finding 2. Sections between MMBFJ310 port impedances (input 56 to 125 ohm, 5 pF; drain 50 to 200 ohm, 2.5 pF) and on VSWR circles; LTspice re-simulation of the named cases | 2+3+3 mode B corner with datasheet J310 ports: down to 68.0 dB (aligned at 50) and 61.3 dB (aligned in circuit): **FAIL**. Design input every internal port VSWR 1.2 or better: 72.1 dB (PASS). BPF1 into 125 ohm: +0.63 dB loss at Q 120 |
| `results/2026-09-28-r10-bpf-leakage-corner/` | Finding 5. Stray C per section with a worst-phase bound at nominal, at the mode B corner and at the design-input corner (VSWR 1.2); LTspice at SGN +1 and -1 | 2+3+3 design-input corner with 0.03 pF per section: **70.2 dB, PASS by 0.2 dB**; 0.1 pF gives 66.4 dB (FAIL). 2+3+4: 80.1 dB. 2+3+2 IF 10: 72.5 dB |
| `results/2026-09-28-r12-bpf-residual-design-input/` | Review iteration 2, finding 6. Alignment residual swept +/-0.05 to +/-1.5 % at the 50 ohm, VSWR 1.2 and design-input corners (mode B, aligned at 50 ohm, VSWR 1.2 ports, 0.03 pF per section, worst phase); bisection of the residual that holds 70 dB; LTspice at the limit, +/-0.3 % and +/-0.75 % | 2+3+3 design-input corner: 70.19 dB at +/-0.3 % (estimate), **limit +/-0.32 %** (0.87 dB per 0.1 %), 65.96 dB at +/-0.75 % (**FAIL**; the revision 2 limit of +/-0.75 % is withdrawn). Limits: 2+3+2 IF 10 +/-0.68 % (69.53 dB at +/-0.75 %, FAIL), 2+3+4 +/-0.97 % (73.64 dB at +/-0.75 %). LTspice agrees on 18 cases (3.6e-4 dB) |
| `results/2026-09-29-r13-bpf-temperature/` | Review iteration 3, finding-7 (revision 4). Design-input corner over REQ-SYS-114 after a 20 to 30 C alignment: board -10 C and +70 C (main-bay air of the thermal note), C0G 0 +/- 30 ppm/K (KEMET) plus +/-10 ppm/K stray, coils +5 to +70 ppm/K (Coilcraft 184-1), hot coil Q 92.2; per-resonator drift on the exact frequency map; residual sweep and bisection per case; board temperature sweep; doubled-coefficient sensitivity; LTspice on 22 corner cases | **2+3+4 (design): PASS over temperature, worst case 75.37 dB hot at +/-0.3 % (margin 5.37 dB)**; limit over temperature +/-0.64 %, alignment acceptance +/-0.62 %; room limit +/-0.95 % (exact map; reviewer's values reproduced). 2+3+3: **FAIL** (69.46 cold, 67.00 hot; no residual holds hot). 2+3+2 IF 10: 70.16 dB (+0.16 dB), limit +/-0.32 %. Doubled coefficients, 2+3+4 hot: 70.99 dB. LTspice agrees to 3.6e-4 dB. Parts of the design BPF3: nine 0805 C0G (2 end, 4 shunt, 3 coupling) and four coils from owned wire, against seven and three for 2+3+3, which is the top of TS-012 row E5 (a) (seven to nine C0G, USD 1.00 to 4.50); J310 port-matching parts not counted (record section 5) |
| `results/2026-09-28-r11-cascade-tpm005/` | Findings 2 and 3. Cascade with TC-SYS-017 corner losses (mode B vertices, Q 100, ports VSWR 1.2), a J310 port case, TPM-005 thresholds | 2+3+3 with the ring: MDS -141.2 nominal (TPM-005 Yellow), -140.6 J310 port (Yellow), **-138.0 corner (REQ-SYS-022 FAIL, Yellow)**, -133.7 stack (Red). No configuration meets the TPM-005 PDR margin policy of -142 dBm |

Superseded attempts are not kept: the first r01 to r05 outputs of 2026-09-28 used a capacitive leakage model with one
phase only, 50 kHz Monte Carlo steps and a 20 ps ring step; they were deleted before the commit and regenerated.
Failed JFET cases keep their LTspice log gzip-compressed (`*.log.gz`, the logs are 7 to 10 MB of convergence warnings).

## Limits of the models (short list; the record has the full one)

- Revision 2 alignment model: each resonator re-tuned after assembly (Dishal node resonance, 50 ohm ports) with a
  +/-0.3 % residual (estimate); the review showed that without re-alignment the mode B corner fails (67.2 dB).
  The residual that holds 70 dB at the design-input corner is at most +/-0.32 % for 2 + 3 + 3 (r12; +/-0.68 % for
  2 + 3 + 2 at IF 10, +/-0.97 % for 2 + 3 + 4, first-order map, at the alignment temperature). Over REQ-SYS-114
  (r13, exact map) the limits are +/-0.64 % for the design 2 + 3 + 4 (acceptance +/-0.62 %), +/-0.32 % for 2 + 3 + 2
  at IF 10 and none for 2 + 3 + 3; the achieved residual is not measured.
- Revision 4 temperature model: coefficient classes from the C0G and 1812SMS datasheets (the coil class applied to a
  hand-wound coil is an estimate), a +/-10 ppm/K stray allowance and a +70 C board bound (estimates); ports assumed
  within VSWR 1.2 over temperature; MDS not re-analysed over temperature.
- J310 ports are modelled as a shunt R and C per port from datasheet values; no J310 stage was simulated.

- Ideal isolation between sections (the J310 stages are not simulated; their tuned-drain selectivity is not credited).
- No PCB layout, no radiation, no ground-return coupling beyond 5 nH per resonator; leakage only as a per-section
  stray capacitance sweep.
- Coil Q is a fixed series resistance set at 146 MHz; capacitor Q 500 is an estimate.
- The mixer decks idealize the diplexer as 50 ohm and model the BN-43-202 transformers as coupled inductors
  (4 uH, k 0.99, estimate); the transient has a time-step floor near -78 dBc that the checker detects and excludes.
- The JFET mixer is representative (no A4 schematic exists); its floor cases did not converge.
