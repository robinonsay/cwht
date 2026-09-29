# D-18 PA-permit gate: level interface, unpowered states and the A5 key-up case (WP-PDR-22)

| Field | Value |
|---|---|
| Product | `docs/design/analysis/pa-permit-gate-d18.md` (analysis note, `analysis_kind`: simulation and worst-case datasheet arithmetic; logic interface, power sequencing, single faults, key-up RF level), **revision 0**, 2026-09-29 |
| Work package | WP-PDR-22 (`docs/plan/pdr-work-plan.md` section 3.0 row 22 and the WP-PDR-22 section): "the key-up case with the D-18 gate and the fix of the D-18 lien (gate supply rail, level interface to the 5 V P-FET, unpowered state), which CR-018 needs before it carries the REQ-TX-014 restatement". The rest of WP-PDR-22 (the closed VGG loop with D-9 and D-10 at circuit values, the late-contact and open-loop faults, the simulated power-on of the loop, G3 values) is not in this record |
| Author | Claude, analysis author invocation, 2026-09-29 |
| Status | Draft, for freeze (rule C2) and independent review with its software assurance pair (plan WP-PDR-22: reviewer plus SA; the gate is part of the HZ-004 K8 control) |
| Design basis | TS-012 revision 8 (`bb5dee7`): section 7.3 revision 6 "Hardware gate (D-18)" and the key-down sequence; section 8.1 diagram and note 2 (the open lien); section 8.14 D-18; row E5 (g). The owner chose A5 (TS-012 section 10; status note 2026-09-29 section 5) |
| Findings answered | INSP-118 finding-9 (a), (b) and (c) (`docs/reviews/PDR/checklists/ts-012-design-to-cost-software-assurance.md`); INSP-110 finding-24 (`docs/reviews/PDR/checklists/ts-012-design-to-cost.md`). One fix closes both, as both records say |
| Decks, scripts and results | `hardware/sim/tx-pa-permit/` (README.md there). Runs `2026-09-29-d18-keyup`, `2026-09-29-d18-asis`, `2026-09-29-d18-seq` and `2026-09-29-d18-summary` in `hardware/sim/tx-pa-permit/results/`. After the LTspice runs, the plot labels were edited and each run was re-analysed with the final script (`replot`). The generated decks are byte-identical to the decks that ran, and every run folder holds the same `d18_run.py` |
| Tool | LTspice 26.0.2 through `tools/ltspice-batch.sh` only (ACC-LTSPICE-001); `.raw` read with spicelib 1.6.3 in the repo venv; checker `d18_run.py` |
| Evidence status | **Developer evidence** (05 section 9.1): the checker has no TV record. The logic, transistor and MOSFET limits are datasheet values; the GVA-84+ unpowered isolation, the module's VGG-off isolation, the GVA-84+ current against supply, the regulator and bead models and the hot leakage multipliers are estimates (section 4). Every stage exits 3 when a criterion the design must pass fails or an expected state differs, 0 otherwise |
| Serves | REQ-TX-014 (the key-up case and the CR-018 restatement), REQ-SYS-120 (hardware half of the two conditions), HZ-004 K5 and K8 (WP-PDR-16b wording), 07 section 14.2 row i; TS-012 D-18 and row E5 (g); the TC-TX-014 method |

## Summary

- **The lien is real.** As TS-012 draws it, a 3.3 V NAND output on the gate of the DMP3099L leaves the driver supply at 4.1 to 5.2 V with TX_KEY low in 25 of 36 corner cases. The key-up level then fails REQ-TX-014 in 21 of 36 (up to -14.7 dBm against -30 dBm), and in those cases the driver is powered whenever the 5 V bus is up (section 5.1). INSP-118 finding-9 (a) and INSP-110 finding-24 are reproduced.
- **Fix (design D18-2B, section 2).** The gate becomes a 74LVC1G11 three-input AND on the Pico 2 3V3 rail. Its output drives two 2N3904 open-collector level shifters to the 5 V bus:
  - branch P holds the GVA-84+ supply P-FET's gate at its source through 10 kohm unless permitted;
  - branch C holds the 2N7002 VGG clamp's gate at the 5 V bus (full drive) unless permitted.
  The monostable Q is pulled up to the 5 V bus, and the P-FET feeds only a 100 nF node with a 2.2 kohm bleed.
- **Every criterion passes in all 52 key-up corners** (section 5.3). The corners cover: 5 V bus 4.75 and 5.25 V; 3V3 3.0 and 3.6 V; GPIO high 2.62 and 3.6 V; P-FET threshold -0.73 (hot), -1.0 and -2.1 V; 2N3904 beta 70 and 416; the error amplifier nominal or wound to the rail; the TS-012 sequence and the interval-13 fallback. Results:
  - Not permitted, the P-FET VGS is 0.0 V, against a smallest threshold magnitude of 0.73 V.
  - The driver supply is 0.4 mV in the key-up window, and below 0.1 V within 0.78 ms of TX_KEY falling.
  - The clamp gate is at 4.75 V or more. VGG is at most 7.9 mV with the error amplifier at its rail.
  - Permitted, VGS is -4.26 V or beyond, the P-FET drop is at most 11 mV, and the driver is powered within 1.2 us.
- **REQ-TX-014 on A5 with the gate (the key-up rerun, section 5.4).** Condition: TX_KEY low, PA_EN asserted, CLK1 running.
  - Level: **-58.3 dBm** on the estimates (28.3 dB margin). **-38.8 dBm** with the unpowered GVA-84+ at its passive bound of 0 dB. **-34.0 dBm** at the drive bound (smallest pad, highest pre-pad level) with the passive bound (4.0 dB margin).
  - REQ-TX-014 now needs only 21.2 dB (design drive) or 26.0 dB (drive bound) of combined off-state isolation: GVA-84+ unpowered plus module at VGG = 0. The keying note's check asked for 43 dB from the module alone, which the datasheet does not guarantee.
  - The restatement TS-012 proposes for CR-018 is supported (section 6.1).
- **Unpowered and sequencing states (finding-9 (b), section 5.5).** The gate is safe in either power-up order and with U1 unpowered, open or removed. It is also safe through a 3V3 or 5 V brown-out, with a single stuck line (TX_KEY or PA_EN), and when the monostable expires. The error amplifier is wound to the rail in all of these cases.
- **Interval-13 fallback (finding-9 (c), section 5.6):** the driver is powered 1.2 us after PA_EN, against the 0.5 ms lead before the ramp.
- **Single faults (section 5.7).** A single open or short in one branch defeats that output only, and the other still acts. The AND gate is the common element, as the NAND was in TS-012. The monostable's own wired-OR clamp and the firmware reference clamp stay independent of it.
- **Cost (section 6.3).** The fix adds two 2N3904 at the row 12 price and seven small passives: USD 0.63 to 0.91 before contingency, against the "cents" that E5 (g) carries. A5's ordering gate had USD 0.17 of margin after guards G1 and G2, so this goes to the TS-012 author and the ordering-gate recompute.

## 1. Purpose and scope

The question: with the D-18 gate made to work at the logic levels that exist, does TX_KEY low (with PA_EN asserted and CLK1 running) leave the GVA-84+ unpowered and the VGG clamped? At what RF level? And is the gate safe unpowered, in either power-up order and under single faults?

The lien has three parts, as INSP-118 finding-9 states them:
- (a) **Level interface.** A 3.3 V NAND output leaves the 5 V P-FET at VGS about -1.7 V when it should be off. A 5 V-supplied 74LVC part would not accept a 3.3 V GPIO high.
- (b) **Unpowered state and power-up order.** With the NAND rail down or at brown-out and the 5 V rail up, the clamp and P-FET gates are left undefined.
- (c) **Fallback timing.** In the interval-13 fallback the driver powers up 0.5 ms before the ramp, against 2 ms nominally, and this was not assessed.

INSP-110 finding-24 is the same defect as (a) and asks for the key-up case with the realised gate.

In scope:
- the gate circuit;
- its interface to the RP2350 GPIOs, the LM393 monostable, the DMP3099L and the 2N7002;
- power sequencing and single faults of the gate;
- the A5 key-up RF level (REQ-TX-014) with the gate.

Not in scope:
- the envelope loop and keying spectrum (`keying-ts012.md`; the WP-PDR-22 loop reruns);
- the monostable's timing (WP-PDR-26);
- the firmware writer of PA_EN (WP-PDR-35);
- the pin map (WP-PDR-36a);
- A4, which is not the chosen design.

| Requirement or case | Limit | How it is checked here |
|---|---|---|
| REQ-TX-014 | At most 1 uW (-30 dBm, TBR) at the antenna port with TX_KEY deasserted, PA_EN asserted and the exciter driven | Antenna level in the key-up window (TX_KEY fall + 2 ms to PA_EN fall at 60 ms, CLK1 running), from the simulated driver supply and VGG, for four isolation cases (section 3.3) |
| REQ-SYS-120 (hardware half) | RF only with key-down and the permit both asserted | Driver unpowered and VGG clamped whenever TX_KEY, PA_EN or Q is low, a rail is down, or U1 is unpowered or open (sections 5.3 and 5.5) |
| INSP-118 finding-9 (a), INSP-110 finding-24 | P-FET gate taken to its source rail; clamp gate at full drive | P-FET VGS not permitted at most 0.3 V in magnitude (smallest threshold 0.73 V); clamp gate at least 4.0 V (2N7002 RDS(on) specified at 4.5 V); static datasheet checks (section 5.2) |
| INSP-118 finding-9 (b) | Unpowered or floating gate output leaves the clamp on and the P-FET off; power-up order stated | Sequencing and fault deck, 13 cases (section 5.5) |
| INSP-118 finding-9 (c) | Driver power-up time in the interval-13 fallback | Turn-on time at most 0.25 ms (half the 0.5 ms lead) in the fallback cases (section 5.6) |
| HZ-004 K8, 07 section 14.2 row i | No single line or flag produces RF | Single-line cases L3 and L4 (TX_KEY stuck, PA_EN stuck) and the pre-permit window of every key-up case |

## 2. The design (D18-2B)

```
 Pico 2 3V3 ----------------------------+ VCC
 TX_KEY  (GPIO, 4.7 k to GND) ----------| A
 PA_EN   (GPIO, 4.7 k to GND) ----------| B   U1 74LVC1G11 (3-input AND; Y high only with all three high)
 Q (LM393 #2 open collector) --+--------| C
                               |        +--- Y ---+---------------------------+
             10 k to 5 V bus --+                  |                           |
                                                10 k                         10 k
                                                  |                           |
                                  100 k to GND ---+-- B  Q2 2N3904            +-- B  Q3 2N3904  --- 100 k to GND
                                                     E to GND                    E to GND
                                                     C --- 1 k ---+              C --+-- 10 k -- 5 V bus
                                                                  |                  |
 5 V bus -- bead -- F3 node (22 uF) --+-- 10 k --+-- gate         |                  +-- gate  Q4 2N7002
                                      |          +----------------+                     drain on the VGG node
                                      +-- source Q1 DMP3099L                            source to GND
                                              drain -- TX5 node: 100 nF, 2.2 k to GND -- choke -- GVA-84+ pin 3
```

**Why each part:**
- **74LVC1G11 at 3.3 V.**
  - TX_KEY and PA_EN are 3.3 V GPIOs, so the gate that combines them runs on the rail they come from. VIH is 2.0 V and VIL 0.8 V at VCC 2.7 to 3.6 V.
  - The inputs take up to 5.5 V at any VCC, and IOFF (at most 2 uA) makes it safe unpowered. So Q can come from the 5 V bus.
  - An AND (output high = permit), not a NAND, is used, so that both level shifters conduct only when permitted. A NAND would need the opposite sense in one branch.
  - Same part class and price as the 74LVC1G10 of E5 (g).
- **Two 2N3904 open-collector stages with pull-ups to the 5 V bus.**
  - A bipolar stage switches with the 2.3 V minimum output of the gate: VBE(sat) is at most 0.85 V, and the forced beta is 3.5 to 3.8 against an hFE minimum of 40.
  - The 2N7002 cannot be the level shifter. Its VGS(th) is up to 2.5 V (2.75 V at -55 C), against 2.3 to 2.9 V of drive.
  - The AO3400A would switch (RDS(on) is specified at 2.5 V), but it costs USD 0.52 against 0.28, and its IDSS is 5 uA at 55 C.
  - Each output gets its own stage, so that one open or short defeats one output only (section 5.7).
- **Branch P.**
  - The P-FET's gate has 10 kohm to its own source. Not permitted, VGS is 0 V whatever the rails do.
  - Permitted, the 1 kohm to the collector gives VGS = -(VF3 - VCE(sat)) x 10/11, which is -4.11 V at the 4.75 V bus minimum.
  - The P-FET source is the F3 node (`spurs-ts012.md` F3: bead and 22 uF), which is placed ahead of the P-FET. The switched node then holds only 100 nF, which keeps the turn-on current pulse to about 1 us.
  - The 2.2 kohm bleed takes the node below 0.1 V within 0.78 ms. The GVA-84+ itself stops drawing current near 3.1 V (E).
- **Branch C.**
  - The clamp's gate is pulled to the 5 V bus, so it is fully driven whenever the permit is absent, including with U1 unpowered.
  - The 2N7002 on the VGG node then holds VGG at about 19 mV even with the error amplifier at 5.25 V and RDS(on) hot.
- **Q pulled up to the 5 V bus.** The LM393 runs on the bus. If the bus is down, Q is low, so no permit can exist without the rail that powers the driver. LM393 VOL is at most 0.7 V (full range, 4 mA), under VIL.
- **Base resistors to ground (100 kohm).** With U1 unpowered (IOFF) or its output open, both stages are off.

Alternatives not taken:
- a 5 V NAND with TTL-threshold inputs: no single three-input part of that kind is in the BOM or was searched;
- one level shifter driving both gates (USD 0.28 cheaper): one component then defeats both outputs (section 5.7);
- AO3400A shifters: cost and hot leakage.

## 3. Method

### 3.1 Decks (LTspice, transient)

`d18_run.py` generates three decks. Every case is one `.step` of one deck.

The netlist:
- **U1** is behavioural. The output is VCC times the product of three logistic input thresholds: 1.4 V, which lies between VIL and VIH, at VCC above 2.7 V, and VCC/2 below. It drives through a switch of 25 ohm that opens (1 Gohm) below VCC 1.2 V, which models IOFF.
- **RP2350 GPIOs:** a driven source of 50 ohm, or high impedance. Every pad has the 4.7 kohm pull-down and a 120 uA E9 leakage current into it.
- **LM393 Q:** a switch to ground with 10 kohm to the 5 V bus.
- **Transistors:**
  - DMP3099L: VDMOS fit to DS36081 (threshold stepped, 99 mohm at -4.5 V, Ciss and Crss from the datasheet, sub-threshold slope 0.04 V, E);
  - 2N7002: VDMOS with the 2.75 V cold-maximum threshold, the worst case for the clamp, and 5.3 ohm at 4.5 V;
  - 2N3904: the published Fairchild/onsemi model, beta stepped.
- **GVA-84+:** a current load I = 0.058 A/V x (V - 3.14 V) (soft-plus below) behind a 1 uH choke. The 0.058 mA/mV slope and the 108 mA at 5 V are datasheet values; the zero-current point is their extrapolation (E).
- **5 V bus:** LM2940 as a 4.75 or 5.25 V source behind 50 mohm and 5 uH, with 22 uF (E). The bead is 0.2 ohm and 1 uH, with 22 uF of F3 (E).
- **VGG node:** the error-amplifier output through the 2.7 k / 5.1 k divider and 10 nF, with the clamp on the node. The amplifier either ramps VGG to 2.75 V (about 5 W, open loop) and returns to 0 V after the ramp ("nominal"), or sits at the 5 V rail from the ramp start onward ("wound", the open-loop and windup fault). The wound case tests the clamp alone.

The decks:
- **`d18_keyup.cir`** follows the TS-012 section 7.3 sequence:
  - PA_EN at t0 + 7 ms and TX_KEY at 8 ms;
  - ramp start 10 ms, 5 ms setting, fall 16 ms after the ramp start;
  - TX_KEY falls 1 ms after the ramp ends (35.5 ms);
  - PA_EN held until 60 ms, the end of the over;
  - in the fallback cases PA_EN comes at 11 ms and the ramp at 11.5 ms.

  52 cases: 2 bus x 2 (3V3, GPIO high) x 3 P-FET thresholds x 2 betas x 2 amplifier states, plus 4 fallback cases.
- **`d18_asis.cir`** is the TS-012 drawing: the NAND output straight to the P-FET gate and the clamp gate through 100 ohm, and no bleed. 36 cases: bus 4.75 / 5.0 / 5.25 V x NAND rail 3.0 / 3.3 / 3.6 V x threshold -0.73 / -1.0 / -1.55 / -2.1 V.
- **`d18_seq.cir`** holds 13 cases with the amplifier wound to the rail throughout (section 5.5).

### 3.2 Criteria

`CRIT` in `d18_run.py` holds each limit with its reason; `result.json` carries the values. They are:
- turn-on at most 0.25 ms;
- clamp release at most 0.25 ms;
- VGS permitted -4.0 V or beyond;
- P-FET drop at most 30 mV;
- P-FET peak current at most 11 A (IDM);
- bus dip at most 100 mV;
- VGS in the key-up window at most 0.3 V in magnitude;
- driver supply in the key-up window at most 50 mV;
- driver supply under 0.1 V within 1 ms of TX_KEY falling;
- clamp gate in the key-up window at least 4.0 V;
- VGG in the key-up window at most 50 mV;
- driver supply at most 50 mV while only one of PA_EN and TX_KEY is high;
- the REQ-TX-014 level at most -30 dBm in each isolation case.

In the sequencing deck, the conditions are:
- driver supply at most 0.1 V whenever not permitted;
- VGG at most 0.1 V with the bus at 4 V or more, and at most 2.0 V while a rail ramps (under the module's dead zone to about 2.3 V);
- when permitted, the driver within 50 mV of its source and the clamp gate at most 0.3 V.

The component-fault cases have expected states (section 5.7).

### 3.3 Antenna level and isolation cases

The checker computes the antenna level at every time point as the sum of two paths, less 0.5 dB for the LPF and relay (`keying-ts012.md` section 3.1):
- **the module path:** the module output for the simulated VGG (the A5 digitized table at 7.9 V drain, 100 dB/V below the graph, as the keying note), with the drive scaled 1:1 by the driver's gain;
- **the leakage path:** the drive into the GVA-84+, times the GVA-84+ gain at the simulated supply, less the 3 dB pad and the module's VGG-off isolation.

The GVA-84+ gain against its supply is an estimate: -Iso(unpowered) at or below 3.14 V, 24.1 dB at 4.8 V and above, linear in dB between. The steady key-up level depends only on the unpowered value.

| Case | Drive into the GVA-84+ | GVA-84+ unpowered | Module VGG-off | Basis |
|---|---|---|---|---|
| L1 (estimates) | -5.27 dBm | 19.6 dB | 30 dB | Drive: 26.5 mW in-service maximum at the module (`pa-drive-ts012.md` s1) + 3.00 dB pad - 22.5 dB lowest GVA-84+ gain. Unpowered: a matched shunt-feedback Darlington has Rf about Z0(1 + \|S21\|) = 852 ohm; unpowered, Rf in series between two 50 ohm ports gives 100 / 952, -19.6 dB (E; junction capacitances neglected; TS-012 used 20 dB). Module: TS-012's 30 dB (E) |
| L2 (GVA-84+ passive bound) | -5.27 dBm | 0 dB | 30 dB | An unpowered GVA-84+ is passive, so \|S21\| is at most 1 |
| L3 (module at "up to 60 dB") | -5.27 dBm | 19.6 dB | 60 dB | Datasheet "the RF input signal attenuates up to 60 dB" (not a limit) |
| L4 (drive bound) | -0.49 dBm | 0 dB | 30 dB | The highest pre-pad level of the PA drive runs (48.6 mW at the module with the 18.42 dB fixed pad and 25.3 dB gain, d4, any coax length) less the smallest pad of the select-on-test set (13.48 dB): no unit can put more into the driver |

The break-even combined isolation for REQ-TX-014 (GVA-84+ unpowered plus module VGG-off) is:
- 21.2 dB at the design drive: -5.27 - 3.0 - 0.5 + 30;
- 26.0 dB at the drive bound.

## 4. Inputs and sources

Classes: **D** datasheet value; **DD** derived from a datasheet (graph read, arithmetic); **R** requirement or TS-012 text; **E** estimate.

| Input | Value | Class | Source |
|---|---|---|---|
| DMP3099L | VGS(th) -1.0 to -2.1 V at -250 uA; RDS(on) 99 mohm max at -4.5 V; IDSS 800 nA max at -30 V; Ciss 563 pF, Crss 41 pF, RG 10.3 ohm typ; IDM 11 A (10 us) | D | Diodes DMP3099L DS36081 Rev. 5-2 (May 2025), page 2, read 2026-09-29 through the web-fetch tool (PDF SHA-256 `06f30303...b442c`) |
| DMP3099L threshold hot | Figure 7 (typical, -250 uA): about 1.76 V at 25 C, 1.57 V at 100 C, 1.35 V at 150 C, so about -2.6 mV/K. On the -1.0 V minimum: -0.81 V at 100 C, **-0.73 V at 125 C** (used) | DD, E | Same, page 4, Figure 7 (rendered and read) |
| 74LVC1G11 | VCC 1.65 to 5.5 V; VIH 2.0 V, VIL 0.8 V at VCC 2.7 to 3.6 V; VOH VCC - 0.1 V at -100 uA, 2.3 V min at -24 mA and VCC 3.0 V; VI 0 to 5.5 V at any VCC; IOFF 2 uA max; Schmitt-trigger inputs; tpd 4.9 ns max at 3.0 to 3.6 V | D | Nexperia 74LVC1G11 Rev. 13.1 (15 Aug 2023), Tables 6 to 8, read 2026-09-29 (SHA-256 `9588c447...bae09`) |
| 2N3904 | hFE min 40 at 0.1 mA, 70 at 1 mA; VCE(sat) 0.2 V max and VBE(sat) 0.65 to 0.85 V at 10 mA / 1 mA; ICEX 50 nA max at 30 V; ts 200 ns max | D | onsemi 2N3903/D Rev. 9 (Aug 2021), read 2026-09-29 (SHA-256 `4a32e2ab...77b8d`); SPICE model: the published Fairchild/onsemi 2N3904 model |
| 2N7002 | VGS(th) 1.0 / 2.0 / 2.5 V (25 C), 2.75 V max at -55 C, 0.6 V min at 150 C; RDS(on) 5.3 ohm max at 4.5 V, 5 ohm at 10 V (25 C), 9.25 ohm at 10 V (150 C); IDSS 10 uA max at 150 C; IGSS 100 nA | D | Nexperia 2N7002 Rev. 7 (8 Sep 2011), Table 6, read 2026-09-29 (SHA-256 `cc9c2754...46475`). The web-fetch tool's own summary of this PDF misreported VGS(th) as 0.5 to 1.3 V; the values here are from the extracted text of the table |
| LM393 | VOL 400 mV max at 4 mA (25 C), 700 mV full range; IOH-LKG 20 nA max at 5 V | D | TI SLCS005AH (Apr 2025), read 2026-09-29 (SHA-256 `f28830c2...e9456`) |
| RP2350 GPIO | VOH min 2.62 V, VOL max 0.5 V (IOVDD 3.3 V); erratum E9 pad leakage about 120 uA (typical, A2 stepping) | D (as quoted) | `docs/research/keyer-verification-and-key-input-network.md` (RP2350 datasheet Table 1436 and erratum RP2350-E9) |
| GVA-84+ | Fixed +5 V operation; device 4.8 / 5.0 / 5.2 V, 85 / 108 / 130 mA; 0.058 mA/mV; gain 22.9 / 24.1 / 25.3 dB at 0.1 GHz; input 13 dBm max; Darlington | D | Mini-Circuits GVA-84+ Rev. F, read 2026-09-29 (SHA-256 `49daf1cb...be95`) |
| GVA-84+ current against supply, zero-current point 3.14 V | I = 0.058 A/V x (V - 3.14 V) | E | Extrapolation of the datasheet slope |
| GVA-84+ unpowered isolation | 19.6 dB, bound 0 dB | E; bound by passivity | Section 3.3 |
| Module VGG-off isolation | 30 dB (E); "up to 60 dB" (datasheet, not a limit) | E, D | TS-012 section 7.3; Mitsubishi RA07M1317M datasheet (Jun. 2019) page 1 |
| Drive into the GVA-84+ | -5.27 dBm (design), -0.49 dBm (bound) | DD | `pa-drive-ts012.md` sections 4.2 (d2, d4, s1: 26.5 mW in service; 48.6 mW fixed-pad maximum over any coax length; pad set 13.48 to 22.04 dB) |
| 5 V bus | LM2940-5, 4.75 to 5.25 V; regulator 50 mohm and 5 uH, 22 uF | R (range), E (dynamics) | TS-012 section 8.1 and the finding-14 disposition (TI SNVS769J 6.5) |
| F3 | Bead and 22 uF on the GVA-84+ supply | R (`spurs-ts012.md` F3), E (0.2 ohm, 1 uH) | Placement ahead of the P-FET is this record's choice |
| Hot leakage multipliers | 2N3904 collector leakage x 100 (5 uA); DMP3099L IDSS x 64 (51 uA) at about +60 K | E | Doubling per 10 K, taken on the datasheet maxima |
| Key-down sequence | PA_EN t0 + 7 ms, TX_KEY 8 ms, ramp 10 ms; fallback PA_EN 11 ms, ramp 11.5 ms; TX_KEY falls 1 ms after the ramp end | R | TS-012 section 7.3 revision 6 |

## 5. Results

### 5.1 As drawn in TS-012: the defect (run `2026-09-29-d18-asis`)

![As drawn: driver supply and key-up level against the P-FET threshold](../../../hardware/sim/tx-pa-permit/results/2026-09-29-d18-asis/asis_keyup.png)

The key-up window holds TX_KEY low, PA_EN asserted and CLK1 running. The NAND output is high, at its rail. Across the 36 cases:
- The P-FET sees VGS of -(bus - NAND rail) = -1.15 to -2.25 V. That is beyond its threshold over most of the -0.73 to -2.1 V range.
- The driver supply stays above the GVA-84+ conduction point (3.14 V) in **25 of 36 cases**, at 4.08 to 5.20 V.
- The key-up level on the L1 estimates exceeds -30 dBm in **21 of 36**, at up to **-14.7 dBm**.
- The P-FET turns off (driver under 3.14 V) in 11 cases only, all with a threshold of -1.55 V or beyond. That needs a threshold magnitude near the top of the datasheet range. At the -1.0 V minimum and at the hot estimate, the driver is powered in every case.
- The drawing gives the same NAND output whenever any input is low, so in those 25 cases the driver is also powered before PA_EN and between overs whenever the bus is up. A single line then no longer unpowers it (`asis_timeline.png`: the driver supply is at 4.1 to 5.2 V from t = 0).
- The clamp gate at 3.0 to 3.6 V is only just above the 2N7002's 2.75 V cold threshold. The clamp still holds VGG low with the loop nominal.

This reproduces INSP-118 finding-9 (a) and INSP-110 finding-24, and shows the defect is wider than the key-up case.

![As drawn, time traces at bus 5.25 V, NAND 3.0 V](../../../hardware/sim/tx-pa-permit/results/2026-09-29-d18-asis/asis_timeline.png)

### 5.2 Static interface checks (datasheet limits; `summary.json` key `static_checks`)

| Check | Value | Limit | Margin |
|---|---|---|---|
| GPIO high at U1 (RP2350 VOH min) | 2.62 V | VIH 2.0 V | 0.62 V |
| GPIO driven low (VOL max) | 0.50 V | VIL 0.8 V | 0.30 V |
| GPIO high impedance at reset or boot: 4.7 k x 120 uA (E9) | 0.56 V | 0.8 V | 0.24 V (break-even leakage 170 uA) |
| Q high: 4.75 V - 10 k x (20 nA + 1 uA) | 4.74 V | 2.0 V | 2.74 V |
| Q high at the 5.25 V bus maximum | 5.25 V | VI max 5.5 V | 0.25 V |
| Q low (LM393 VOL, full range, 4 mA; the load is 0.53 mA) | 0.70 V | 0.8 V | 0.10 V |
| 2N3904 base current at U1's 2.3 V minimum | 0.137 mA | 0.1 mA | 0.037 mA |
| Forced beta, branch P / branch C | 3.5 / 3.8 | hFE min 40 at 0.1 mA | saturated |
| P-FET VGS permitted at the 4.75 V bus (magnitude) | 4.11 V | 4.0 V | 0.11 V (the simulation gives 4.26 V) |
| P-FET VGS not permitted: 10 k x 5 uA (hot collector leakage, E) | 0.05 V | 0.73 V | 0.68 V |
| Driver node not permitted: 2.2 k x 51 uA (hot IDSS, E) | 0.11 V | 3.14 V | 3.03 V |
| Clamp gate not permitted: 4.75 V - 10 k x 5.1 uA | 4.70 V | 4.5 V | 0.20 V |
| Clamp gate permitted: VCE(sat) max against 2N7002 VGS(th) min at 150 C | 0.20 V | 0.6 V | 0.40 V |
| VGG clamped with the amplifier at 5.25 V and RDS(on) scaled to 150 C (9.8 ohm) | 19 mV | 50 mV | 31 mV |

The E9 check applies only to the A2 stepping. It holds with the external 4.7 kohm pull-down, which is under the 8.2 kohm the erratum names; the internal pull-down is not relied on.

### 5.3 D18-2B key-up deck (run `2026-09-29-d18-keyup`, 52 cases)

![D18-2B, one element and the key-up window](../../../hardware/sim/tx-pa-permit/results/2026-09-29-d18-keyup/keyup_timeline.png)

![Switching edges over every corner](../../../hardware/sim/tx-pa-permit/results/2026-09-29-d18-keyup/keyup_edges.png)

![Every criterion over the 52 corners](../../../hardware/sim/tx-pa-permit/results/2026-09-29-d18-keyup/keyup_metrics.png)

| Criterion | Range over the 52 cases | Limit | Verdict |
|---|---|---|---|
| Driver powered after the later of PA_EN and TX_KEY | 0.5 to 1.2 us | 0.25 ms | PASS |
| Clamp released | 0.08 to 0.12 us | 0.25 ms | PASS |
| P-FET VGS permitted | -4.26 to -4.71 V | -4.0 V or beyond | PASS |
| P-FET drop at the GVA-84+ current | 6.9 to 11.1 mV | 30 mV | PASS |
| P-FET peak current at turn-on (the 100 nF node, under 1 us) | 1.0 to 2.4 A | 11 A (IDM, 10 us) | PASS |
| 5 V bus dip at turn-on | 30 to 39 mV | 100 mV | PASS |
| P-FET VGS in the key-up window | 0.000 V | at most 0.3 V (magnitude) | PASS |
| Driver supply in the key-up window | 0.34 to 0.38 mV | 50 mV | PASS |
| Driver supply below 0.1 V after TX_KEY falls | 0.77 to 0.78 ms (below 3.1 V within about 20 us) | 1.0 ms | PASS |
| Clamp gate in the key-up window | 4.75 to 5.25 V | 4.0 V | PASS |
| VGG in the key-up window (amplifier nominal / wound to 5 V) | 0.0 / 7.9 mV | 50 mV | PASS |
| Driver supply with only one of PA_EN and TX_KEY high | under 1 uV | 50 mV | PASS |

In the wound cases the clamp alone takes VGG from 3.4 V to under 8 mV when TX_KEY falls, as REQ-SYS-120 asks of the hardware.

The antenna level between PA_EN and the ramp (the backwave) is:
- -14.7 to -16 dBm on L1 and about -10 dBm on L4, with the driver powered and VGG at 0 V;
- then -58 or -34 dBm in the key-up window.

The keying note (section 4.5) treats the 2 ms backwave before each ramp. It is unchanged by this fix.

### 5.4 REQ-TX-014 on A5 with the gate: the key-up rerun

![Steady key-up level per isolation case](../../../hardware/sim/tx-pa-permit/results/2026-09-29-d18-keyup/level_cases.png)

Condition: TX_KEY low, PA_EN asserted, CLK1 running (the exciter drive present at the GVA-84+ input). The worst of the 52 corners, which equals the analytic chain in every case, is:

| Case | Level at the antenna | REQ-TX-014 (-30 dBm) | Information: REQ-SYS-183 (-57 dBm), if a fault left CLK1 on after the over |
|---|---|---|---|
| L1 estimates | -58.3 dBm | PASS, 28.3 dB | 1.3 dB under |
| L2 GVA-84+ passive bound | -38.8 dBm | PASS, 8.8 dB | 18.2 dB over |
| L3 module "up to 60 dB" | -88.3 dBm | PASS, 58.3 dB | 31.3 dB under |
| L4 drive bound with the passive bound | -34.0 dBm | PASS, 4.0 dB | 23.0 dB over |

- **What REQ-TX-014 now rests on.** With the driver unpowered, REQ-TX-014 needs 21.2 dB (design drive) or 26.0 dB (drive bound) from the GVA-84+ unpowered and the module at VGG = 0 together. Without the gate it needed 43 dB from the module alone (`keying-ts012.md` section 8 item 3). Either element alone meets the design-drive figure on its estimate: the module 30 dB, or the unpowered GVA-84+ 19.6 dB plus the module's first 1.6 dB. Neither isolation is a datasheet limit, so the closing evidence stays the bench test TC-TX-014 names.
- **Comparison with TS-012.** TS-012 revision 6 quotes about -61 dBm for A5 (+10.4 dBm CLK1, 18 dB pad, 20 dB, 3 dB, 30 dB). This record gets -58.3 dBm on the same isolations, at the in-service drive maximum of the select-on-test pad in place of the nominal CLK1 level. For REQ-TX-014 the difference is immaterial.
- **REQ-SYS-183 (CLK1 left on after the over by a firmware fault).** TS-012 states about -61 dBm, under -57 dBm. The margin is 1.3 dB on the estimates and not shown on the bounds. This is a finding for TS-012 and the REQ-SYS-183 owner (WP-PDR-23), not for REQ-TX-014 (section 7, F-3). With CLK1 disabled, the keying note's -111 dBm stands.

### 5.5 Power sequencing, brown-outs and single lines (run `2026-09-29-d18-seq`)

![Sequencing and fault cases](../../../hardware/sim/tx-pa-permit/results/2026-09-29-d18-seq/seq_cases.png)

The error amplifier is wound to the 5 V rail in every case, the worst case for the clamp. Every design case passes.

| Case | What | Result |
|---|---|---|
| S1 | 5 V bus first (1 ms), 3V3 at 6 ms; GPIOs high impedance (pull-downs and E9) until 12 ms; permit 20 to 30 ms | Driver at most 36 mV (the bus ramp's coupling through Cgs) and VGG at most 1.05 V while the bus ramps (clamp gate rising with it), under the module's dead zone; off otherwise; on when permitted; PASS |
| S2 | 3V3 first (USB), GPIOs low from 3 ms, bus at 8 ms; permit 20 to 30 ms | Same (36 mV, 1.07 V during the bus ramp); PASS |
| S3 | 3V3 brown-out while permitted (3.3 to 0 V, 20 to 21 ms) | Off once 3V3 falls under about 1.2 V (U1 output high impedance, bases pulled down); PASS |
| S4 | 5 V bus collapse while permitted | Off; Q falls with the bus; PASS |
| L1 | Monostable expires at 20 ms with TX_KEY and PA_EN high | Off; PASS |
| L2 | SW-SAFE clears PA_EN with TX_KEY stuck high | Off; PASS |
| L3 | TX_KEY stuck high, PA_EN never set | Off throughout; PASS |
| L4 | PA_EN stuck high (or a corrupted permit flag), TX_KEY never set | Off throughout; PASS |
| F1 | U1 output open (lifted pin, missing part) with all inputs high | Off throughout; PASS |

**Power-up order.** Neither order matters.
- With U1 unpowered, its output is high impedance, the base resistors hold both stages off, and both pull-ups go to the bus that powers the loads.
- With the bus down, the GVA-84+ has no supply, the error amplifier cannot raise VGG, and Q is low.
- The 5 V bus overshoot of about 5.4 V at the stepped bus ramp is the regulator model's LC ringing (E). It stays under U1's 5.5 V input limit.

### 5.6 Interval-13 fallback (finding-9 (c))

In the four fallback cases:
- PA_EN rises at t0 + 11 ms, with TX_KEY already high since 8 ms.
- The driver supply is within 50 mV of its source 0.55 to 1.2 us later, and the clamp releases within 0.12 us.
- The ramp at 11.5 ms therefore starts on a driver that has been powered for 0.5 ms.

The GVA-84+'s own bias settling is not modelled, but it is set by the 100 nF and the choke, microseconds. So the 0.5 ms lead is enough. The key-down lead-in of REQ-SYS-161 is unchanged (TS-012 section 7.3).

### 5.7 Single faults of the gate

Component-fault cases of the sequencing deck (expected states, all as expected), and single faults that follow from the circuit by inspection (analysis, not simulated):

| Fault | Driver (GVA-84+ supply) | VGG clamp | Consequence at key-up (L1 isolations) | Detected by |
|---|---|---|---|---|
| F2: branch P gate-source 10 k open (simulated) | Stays on after TX_KEY falls (gate charge held) | On | Driver-on leakage about -14 dBm with VGG clamped: REQ-TX-014 fails; no RF at power | TC-TX-014 at build; latent afterwards |
| F3: Q2 collector-emitter short (simulated) | On always | On unless permitted | As F2 | As F2 |
| DMP3099L drain-source short (analysis) | On always | On unless permitted | As F2 | As F2 |
| F4: branch C pull-up open (simulated) | Off unless permitted | Lost | Loop drives VGG to 0; with the loop also wound, VGG 3.3 V into a driver-off leak, a double fault | Build test of the clamp |
| F5: Q3 collector-emitter short, or 2N7002 open (simulated / analysis) | Off unless permitted | Lost | As F4 | As F4 |
| U1 output stuck high, or shorted to 3V3 (analysis) | On | Released | Both D-18 outputs lost. The monostable's own wired-OR clamp still ends RF in 7.5 to 13 s, and the firmware reference clamp still acts. PA_EN can no longer remove RF | TC-TX-014 fault-injection build; latent afterwards |
| U1 output open, or U1 unpowered (simulated F1, S1, S3) | Off | On | Safe | - |
| A base pull-down (100 k) open (analysis) | No effect while U1 is powered; with U1 also unpowered, the base floats (dual fault) | Same | - | - |

So:
- One component in a branch defeats that branch only; the other output still acts.
- U1 is the common element, as the NAND was in TS-012 revision 7. Its failure leaves K5 and the firmware reference clamp, but not K8.
- Full independence would take a second gate IC for branch C: a 74LVC1G11, USD 0.10 to 0.40 (E). That is offered in section 6.4, not adopted here.
- The latent faults of branch P can be made detectable by a TX5 sense line (section 6.4, R-2).

## 6. Proposals and verdicts

### 6.1 D-18 text (to TS-012 and the schematic, WP-PDR-37) and the REQ-TX-014 restatement

- **D-18 (proposed wording of the gate):**
  - A 74LVC1G11 three-input AND on the Pico 2 3V3 rail of TX_KEY (4.7 kohm pull-down), PA_EN (4.7 kohm pull-down) and the cutoff monostable output Q (LM393 open collector, 10 kohm pull-up to the 5 V bus).
  - Its output drives two 2N3904 stages, each with 10 kohm base and 100 kohm base-to-ground.
  - Branch P: the collector through 1 kohm to the gate of the DMP3099L, which has 10 kohm gate to source. The source is on the F3 node (bead and 22 uF from the 5 V bus); the drain feeds 100 nF and a 2.2 kohm bleed, then the GVA-84+ choke.
  - Branch C: the collector with 10 kohm to the 5 V bus, on the gate of the 2N7002 clamp on the VGG node.
  - Unpowered, open or low, the gate leaves the P-FET at VGS = 0 V and the clamp gate at the 5 V bus, in either power-up order.
- **REQ-TX-014.** The key-up case holds with the gate: -58.3 dBm by estimate, -34.0 dBm at the bounds, against -30 dBm. The TS-012 section 8.10 restatement for CR-018 is supported: "... at most 1 uW (TBR) while TX_KEY is deasserted with PA_EN asserted and the synthesizer's transmit output running". So is its HZ-004 note, since TX_KEY removes both the drive supply and the gate bias in hardware at the logic levels that exist.
- **TBR.** The proposal is to keep 1 uW (-30 dBm). The bound case leaves 4.0 dB; the estimate leaves 28.3 dB.

### 6.2 HZ-004 K8 wording (to WP-PDR-16b)

K8 can name:
- the gate (AND of TX_KEY, PA_EN and Q) and its two outputs;
- the safe state: driver unpowered and VGG clamped whenever any input is low, U1 is unpowered or open, or the 3V3 rail is down;
- the common element U1, whose stuck-high failure leaves K5 and the firmware reference clamp.

### 6.3 Cost (row E5 (g))

| Item | Revision 7/8 E5 (g) | D18-2B |
|---|---|---|
| Gate | 74LVC1G10-class NAND, 0.10 to 0.40 (E) | 74LVC1G11, same class, 0.10 to 0.40 (E) |
| Clamp FET | 2N7002-class, 0.10 to 0.30 (E) | Unchanged |
| GVA-84+ supply P-FET | 0 to 0.40 (row 23) | Unchanged |
| Level interface | "cents" | Two 2N3904 at the row 12 price, 0.56 (row 12 goes from 7 to 9); seven resistors and one 100 nF from the E2 lot, 0.07 to 0.35 (E) |
| **Change** | - | **+0.63 to +0.91 before contingency** (+0.72 to +1.05 capped) |

TS-012 section 8.4 gives A5's worst case as USD 299.83 after guards G1 and G2, a margin of 0.17. This change alone would put it at about 300.55 to 300.88. It goes to the TS-012 author and the ordering-gate recompute after the owner's price reads. At the price check, the 2N3904 might cost less at a 10-piece break, or as the SMD MMBT3904 (neither is read; both would be added to the section 8.11 list). If the gate does not hold, the options are:
- the one-stage variant (+0.35 to +0.63): one component in the stage then defeats both outputs;
- to find the cents elsewhere.

### 6.4 Recommendations (not needed to close the lien)

- **R-1 (to WP-PDR-16b and the TS-012 author).** Decide whether U1's stuck-high single fault is acceptable with K5 and the firmware reference clamp remaining. If not, give branch C its own 74LVC1G11 (+0.10 to 0.40, E).
- **R-2 (to WP-PDR-36a and WP-PDR-35).** A TX5 sense line: a 10 k / 10 k divider from the TX5 node to a spare GPIO input. With it SW-SAFE can check, before PA_EN is set at each changeover, that the driver is unpowered, which makes the latent branch-P faults of section 5.7 detectable. It needs one GPIO and two resistors, and only if the pin map has one left.
- **R-3 (to WP-PDR-37).** Place the 10 kohm gate-to-source resistor at the DMP3099L. Place the 2.2 kohm bleed and the 100 nF at the GVA-84+ choke. Keep F3's 22 uF ahead of the P-FET.

## 7. Findings for other records

- **F-1 (TS-012).** The D-18 lien is closed by D18-2B (section 6.1). The section 8.1 diagram should show the AND, the two stages and the pull-up rails. Row E5 (g) changes by +0.63 to +0.91 (section 6.3).
- **F-2 (TS-012, `keying-ts012.md` section 8 item 3).** The on-receipt module isolation check "at least 43 dB" is no longer the REQ-TX-014 criterion. With the gate, the criterion is the key-up level of TC-TX-014 itself: at most -30 dBm with TX_KEY low, PA_EN held high and CLK1 running. The chain then needs only 21.2 to 26.0 dB of combined off-state isolation.
- **F-3 (TS-012 section 7.3; REQ-SYS-183 with WP-PDR-23).** TS-012 says the level is "about -61 dBm even if a firmware fault left CLK1 on, under -57 dBm". At the in-service drive maximum it is -58.3 dBm on the same estimates, 1.3 dB under. With the unpowered GVA-84+ at its passive bound it is over (-38.8 dBm). The statement should carry its basis, or the CLK1-left-on case should be bounded otherwise, for example by SW-SAFE disabling CLK1 as part of `safe_state()`.
- **F-4 (WP-PDR-26).** The monostable output Q is pulled up to the 5 V bus, not the 3V3 rail (section 2), so that no permit exists with the bus down.
- **F-5 (`pa-drive-ts012.md`, information).** The GVA-84+ device voltage is 4.8 V minimum, and the LM2940 bus is 4.75 V minimum before the bead and the P-FET (up to 37 mV here). The PA drive record's "min" P1dB set is taken to cover 4.75 to 5.25 V. This record adds 7 to 11 mV of P-FET drop to that; it does not change the conclusion.

## 8. Limitations

1. **Logic model.** U1 is behavioural: logistic thresholds at 1.4 V (VCC/2 below 2.7 V), a 25 ohm output and IOFF as a switch at 1.2 V. The guaranteed levels are checked separately against the datasheet limits (section 5.2), not taken from the model.
2. **MOSFET models.** VDMOS fits to datasheet points, not vendor models. Hot and cold thresholds are stepped as corners, not by a temperature model. Leakage is added analytically at hot (section 5.2), not simulated.
3. **GVA-84+.** The current against supply and the gain against supply are estimates. Only the unpowered isolation enters the steady key-up level, and it is bounded by passivity (L2, L4).
4. **Module isolation.** The 30 dB of TS-012 is an estimate, and the datasheet's "up to 60 dB" is not a limit. The L2 and L4 cases keep 30 dB. Below the 21.2 to 26.0 dB break-even combined with the GVA-84+, REQ-TX-014 would fail; the bench test closes it.
5. **Regulator and bead.** The LM2940 and bead dynamics are estimates. The bus dip (30 to 39 mV) and the overshoot at the stepped power-up depend on them.
6. **Coupling that bypasses the chain** (CLK1 coax to the output, the prescaler tap) is not in this record. It belongs to WP-PDR-20 and to the TC-TX-014 bench test.
7. **Error amplifier.** Modelled as an ideal source ramping VGG open loop, or at its rail. The loop itself is the WP-PDR-22 loop rerun.
8. **Raw sizes.** `d18_keyup.raw` (10,867,266 bytes) and `d18_asis.raw` (7,072,648 bytes) are over 5,000,000 bytes. They are kept in their run folders on the owner's Mac, with `raw.sha256` committed beside them (CR-017 C2). `d18_seq.raw` is committed.

## 9. What closes on the bench

- **TC-TX-014** (post-build, closing), as REQ-TX-014's verification note states: a fault-injection build holding PA_EN high and TX_KEY low with the exciter running, the tinySA Ultra through the calibrated attenuator into the dummy load, at 144.0012, 146.000 and 147.9988 MHz. Pass: at most -30 dBm.
- **Gate function at first power-on** (supporting; the owner's Fluke multimeter):
  - TX5 at most 0.1 V and the clamp gate at 4.5 V or more, with each of TX_KEY, PA_EN and Q low in turn;
  - the same with the Pico 2 unpowered and the 5 V bus up (USB unplugged, cells in).

## 10. References

- TS-012 revision 8, `docs/decisions/trade-studies/TS-012-design-to-cost-hand-built.md` (`bb5dee7`): sections 7.3 (revision 6 key-down sequence and D-18), 8.1 (diagram, note 2), 8.3 rows 12 and 23, 8.4, 8.10 (REQ-TX-014 restatement), 8.14 D-18, row E5 (g).
- INSP-118 record, `docs/reviews/PDR/checklists/ts-012-design-to-cost-software-assurance.md` (finding-9); INSP-110 record, `docs/reviews/PDR/checklists/ts-012-design-to-cost.md` (finding-24).
- `docs/design/analysis/keying-ts012.md` (sections 3.1, 4.5, 8 items 3 and 4); `docs/design/analysis/pa-drive-ts012.md` (sections 3.1 and 4.2, runs d2, d4, s1); `docs/design/analysis/spurs-ts012.md` (F3).
- `docs/research/keyer-verification-and-key-input-network.md` (RP2350 Table 1436, erratum RP2350-E9).
- Requirements at HEAD: `docs/requirements/tx/requirements.md` (REQ-TX-014), `docs/requirements/sys/requirements.md` (REQ-SYS-120, REQ-SYS-183); `docs/plan/pdr-work-plan.md` (WP-PDR-22; rules C1 to C12).
- Diodes DMP3099L DS36081 Rev. 5-2 (May 2025), https://www.diodes.com/assets/Datasheets/DMP3099L.pdf.
- Nexperia 74LVC1G11 Rev. 13.1 (15 Aug 2023), https://assets.nexperia.com/documents/data-sheet/74LVC1G11.pdf.
- Nexperia 2N7002 Rev. 7 (8 Sep 2011), https://assets.nexperia.com/documents/data-sheet/2N7002.pdf.
- onsemi 2N3903/D Rev. 9 (Aug 2021), https://www.onsemi.com/download/data-sheet/pdf/2n3903-d.pdf.
- TI LM393 SLCS005AH (Apr 2025), https://www.ti.com/lit/ds/symlink/lm393.pdf.
- Mini-Circuits GVA-84+ Rev. F, https://www.minicircuits.com/pdfs/GVA-84+.pdf.
- Alpha and Omega AO3400A Rev. 3.1 (Jul 2023), https://www.aosmd.com/res/datasheets/AO3400A.pdf (alternative considered, section 2).
- All datasheets were read on 2026-09-29 through the web-fetch tool, which cached each PDF (SHA-256 prefixes in section 4). The text was extracted with pdftotext, and the DMP3099L page 4 was rendered for Figure 7.
