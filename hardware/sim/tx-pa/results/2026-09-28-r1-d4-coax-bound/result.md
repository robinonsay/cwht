# 2026-09-28-r1-d4-coax-bound: coax-length bound and time-step check (revision 1, finding-1)

Every electrical length of the 50 ohm coax (0.5 to 70 cm at VF 0.66; the line repeats every half wavelength, 69 cm at 144 MHz) for the part corners that set the extremes (max, 25 ohm; max, 50 ohm; nominal; min, 25 ohm; min, 50 ohm), 144, 146 and 148 MHz; 25 C.

| Finalist | Max over any length (mW) | Min over any length (mW) | Max, 5 to 15 cm (mW) | Min, 5 to 15 cm (mW) | Overdrive margin, any length (dB) | Same with the 0.1 dB temperature allowance (dB) |
|---|---|---|---|---|---|---|
| A5 | 48.6 | 5.4 | 35.5 | 5.4 | -2.10 | -2.20 |
| A4 | 195.9 | 45.8 | 180.0 | 45.8 | +0.09 | -0.01 |

Overdrive limit: 30 mW for A5 (module maximum rating); 200 mW for A4 (ruggedness-test drive, not a rating). A negative margin means that some length and part corner exceed the limit with the fixed pad.

- A5 highest step: source 25 ohm, GVA gain 25.3 dB, P1dB set high, 144 MHz, Si5351 case high (VDDO 3.4 V, edge 0.5 ns, duty 0.50), coax 32.5 cm.
- A5 lowest step: source 50 ohm, GVA gain 22.5 dB, P1dB set min, 148 MHz, Si5351 case low (VDDO 3.2 V, edge 1.5 ns, duty 0.45), coax 12.5 cm.
- A5 equivalent shunt capacitance at the CLK1 pin over every length: -16.4 to 30.4 pF (informative; the lumped load is 7 pF).
- A4 highest step: source 25 ohm, GVA gain 25.3 dB, P1dB set high, 144 MHz, Si5351 case high (VDDO 3.4 V, edge 0.5 ns, duty 0.50), coax 32.5 cm.
- A4 lowest step: source 50 ohm, GVA gain 22.5 dB, P1dB set min, 148 MHz, Si5351 case low (VDDO 3.2 V, edge 1.5 ns, duty 0.45), coax 12.5 cm.
- A4 equivalent shunt capacitance at the CLK1 pin over every length: -16.2 to 30.2 pF (informative; the lumped load is 7 pF).

Time-step check (the d2 and d3 decks use a 20 ps maximum step; the same 15 corners at 10 cm rerun with 10 ps):

- A5: largest difference 0.0004 dB in PA input power and 0.013 dB in 3f (criteria 0.02 dB and 0.5 dB): **PASS**.
- A4: largest difference 0.0005 dB in PA input power and 0.013 dB in 3f (criteria 0.02 dB and 0.5 dB): **PASS**.

Plot: `coax_length_bound.png`. Steps: `coax_a5_steps.json`, `coax_a4_steps.json`. Decks `coax_a5.cir`, `coax_a4.cir`, `tstep_a5.cir`, `tstep_a4.cir`; LTspice logs and raws beside them.
