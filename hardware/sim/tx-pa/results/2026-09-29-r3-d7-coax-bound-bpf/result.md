# 2026-09-29-r3-d7-coax-bound-bpf: coax-length bound of the bandpass chain and the time-step check (revision 3)

- Over every length (0.5 to 70 cm) the fixed-pad drive spans 6.0 to 38.7 mW.
- Highest step: source 25 ohm, GVA gain 25.3 dB, P1dB set high, 146 MHz, Si5351 case high (VDDO 3.4 V, edge 0.5 ns, duty 0.50), coax 30.0 cm, Q 135.
- Lowest step: source 50 ohm, GVA gain 22.5 dB, P1dB set min, 148 MHz, Si5351 case low (VDDO 3.2 V, edge 1.5 ns, duty 0.45), coax 27.5 cm, Q 100.
- Pad loss a unit needs at 146 MHz for 17.3 mW, any length: 13.90 to 21.92 dB.
- Frequency span of the drive within one unit, any length: 0.31 dB.
- CLK1 pin equivalent shunt C over every length: 4.9 to 9.0 pF.
- 3f at the GVA-84+ input, worst over every length: -33.7 dBc.
- Numerical check: 15 corners at 10 ps and 400 ns against d6 at 20 ps and 250 ns: 0.0028 dB power, 0.040 dB 3f (criteria 0.02 and 0.5 dB).

Plot `coax_length_bound_bpf.png`; steps in `coax_a5_bpf_steps.json`; decks `coax_a5_bpf.cir`, `tstep_a5_bpf.cir`.
