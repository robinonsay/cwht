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
| `cascade.py` | NF, gain and MDS cascade with the simulated filter losses; half-IF referral to the antenna; verdicts; plots |

Reproduce: `.venv/bin/python hardware/sim/rx-frontend/make_decks.py`, then `run_sims.py`, then
`check_bpf.py results/<run-id>` for r01 to r04, `check_halfif.py results/2026-09-28-r05-halfif-mixers`,
and `cascade.py` (writes r06).

## Runs

| Run | Content | Result (details in each `result.md`) |
|---|---|---|
| `results/2026-09-28-r01-bpf-ts012-baseline/` | TS-012 BPF1 2 + BPF2 3 resonators, 5 and 6 MHz design, coil Q 100/120/150/200; Monte Carlo 200 runs mode A (TS-012: 20 % capacitors) and mode B (proposed part spec) | **FAIL** REQ-SYS-033 at IF 8 MHz: 51 to 61 dB nominal at every Q, 39 dB (mode A) and 46 dB (mode B) Monte Carlo minimum. At IF 10 MHz 65 to 74 dB nominal, mode B minimum 60 dB: FAIL |
| `results/2026-09-28-r02-bpf-three-section/` | 2 + 3 + 2 and 2 + 3 + 3 resonators (BPF3 between the second J310 and the ring), 6 MHz, Q sweep | 2+3+3: **PASS** 86.0 dB at Q 100 (89.8 at Q 200), IF 8. 2+3+2: FAIL at IF 8 (67.8 dB at Q 100), PASS at IF 10 (86.7 dB) |
| `results/2026-09-28-r03-bpf-three-section-mc/` | Monte Carlo 200 runs, modes A and B, of 2+3+2 and 2+3+3 | 2+3+3 at IF 8: **PASS**, minimum 70.6 dB (mode A) and 78.1 dB (mode B, 97.5 % of runs at 80 dB or more). 2+3+2 at IF 10: PASS, 70.6 dB (A) and 80.5 dB (B) |
| `results/2026-09-28-r04-bpf-leakage/` | 2+3+3 at Q 100 with a stray input-to-output capacitance of 0.003 to 0.1 pF across each section, both leakage phases | Worst case 78.2 dB at 0.1 pF per section (PASS 70 dB); a whole-chain leak is not in this model (see the record) |
| `results/2026-09-28-r05-halfif-mixers/` | Transient: diode ring (4 x 1N5711, Si5351 square LO +10 dBm, duty 45/50/55 %, diode and winding mismatch) and a representative single-J310 mixer (A4, one deck per case, 16 cases) with wanted (144 MHz) and half-IF (140 MHz) tones | Ring: Gc -5.14 dB, half-IF IIP2 51.8 to 63.6 dBm mismatched (matched: at the -77.8 dBc time-step floor, IIP2 67.8 dBm or more). JFET: IIP2 30.1 to 30.4 dBm; 8 of 16 cases did not converge (logs gzip-compressed) |
| `results/2026-09-28-r06-cascade/` | Python cascade (NF, gain, MDS in 500 Hz) with the r01 to r03 losses and r05 mixer data; half-IF referral; isolation needed | 2+3+3 with the ring: NF 5.81 dB, MDS -141.2 dBm nominal (PASS), -139.1 dBm at the filter corner (FAIL by 0.9 dB, at risk). Half-IF at -70 dBm: -177 dBm equivalent (ring), -156 dBm (JFET): PASS. Isolation needed antenna to mixer at the image: 84 dB |

Superseded attempts are not kept: the first r01 to r05 outputs of 2026-09-28 used a capacitive leakage model with one
phase only, 50 kHz Monte Carlo steps and a 20 ps ring step; they were deleted before the commit and regenerated.
Failed JFET cases keep their LTspice log gzip-compressed (`*.log.gz`, the logs are 7 to 10 MB of convergence warnings).

## Limits of the models (short list; the record has the full one)

- Ideal isolation between sections (the J310 stages are not simulated; their tuned-drain selectivity is not credited).
- No PCB layout, no radiation, no ground-return coupling beyond 5 nH per resonator; leakage only as a per-section
  stray capacitance sweep.
- Coil Q is a fixed series resistance set at 146 MHz; capacitor Q 500 is an estimate.
- The mixer decks idealize the diplexer as 50 ohm and model the BN-43-202 transformers as coupled inductors
  (4 uH, k 0.99, estimate); the transient has a time-step floor near -78 dBc that the checker detects and excludes.
- The JFET mixer is representative (no A4 schematic exists); its floor cases did not converge.
