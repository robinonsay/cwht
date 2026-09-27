# TS-012: Design-to-cost architecture for a hand-built first radio under USD 200

| Field | Value |
|---|---|
| ID | TS-012 |
| Status | **Proposed; owner's decision pending.** Revision 0 (2026-09-27). Opened on the owner's direction of 2026-09-27 (`docs/plan/status/status-2026-09-27.md` sections 6 and 8; section 8 governs where they differ). Independent review (06 section 14.3 step 6) not yet run |
| Decision class trigger | 06 section 14.1 class 1 items (a) architecture choice (receiver topology, PA topology, LO scheme, power architecture, enclosure concept), (b) selection of critical parts (RF power device, synthesizer, TCXO, CW filter, battery charger, display), (c) choices touching HZ-002, HZ-003, HZ-004, HZ-005, HZ-007, HZ-008 and HZ-015, (d) the owner asked for it (status note section 6, "A design-to-cost trade study (TS-012)"), (f) changes to KDR requirements (REQ-SYS-010, 102, 103, 137, 140) |
| Decision maker | Robin (owner, Decision Authority) |
| Recommender | Claude (trade-study author invocation, 2026-09-27), from three independent architectures and three judges (section 4.3) |
| Independent reviewer | INSP-NNN in `docs/reviews/PDR/checklists/ts-012-design-to-cost-hand-built.md`, filled from `docs/templates/peer-review-checklist-risk.md` section B (06 section 14.2); not yet run |
| Decide by | Before the PDR trades that depend on it are scored: proposed B1a (Tue 2026-09-29), no later than B1b (Thu 2026-10-01). Every one of WP-PDR-19 to 28, 33, 37 to 40 and 46 changes with this decision (section 8.12) |
| Related risks | RSK-004 (turnkey defects, retired if selected), RSK-006 (PA junction temperature), RSK-008 (first power-on), RSK-025 (antenna port retention), RSK-037 (RP2350 ADC audio; not used for audio here), RSK-038 (stock and end of life), RSK-052 (cost above the model) |
| Related requirements and hazards | Section 8.10 lists every REQ delta. Hazards HZ-002, HZ-003, HZ-004, HZ-005, HZ-007, HZ-008, HZ-015. Stakeholder inputs SI-013, SI-022, SI-028, SI-031, SI-034; the owner inputs of status note sections 6 and 8 take the next free SI id when the re-baseline CR appends them |
| Resulting ADR | The next free ADR number when the owner decides (ADR-056 or later; highest at writing is ADR-055) |
| Dates | opened 2026-09-27; recommended 2026-09-27 (this revision, before independent review); decided: pending |

Price evidence convention used in every table: **L** = listed price read on the seller's own page on 2026-09-27; **A** = distributor price and stock read on 2026-09-27 through the OEMsTrade aggregator page for the part, because Mouser, DigiKey and Newark block automated reads (the owner verifies it in a browser); **E** = estimate with its basis, never a listed price. No page was logged into, no form was filled, nothing was added to a cart and no file was downloaded by the author.

## 1. Executive summary

- **Recommendation (one sentence):** adopt **A4, "min-cost with grafts"**: the NXP AFT05MS004NT1 SOT-89 LDMOS final with a Mini-Circuits GVA-84+ driver on a small PA board bolted to an aluminum heat-sink end wall (fins outside the PETG case), a JFET single-conversion superhet with a hand-matched 6-pole 500 Hz crystal ladder and an analog audio chain, an Adafruit Si5351A module, a Morse-code audio user interface with no display, cells charged outside the radio, one Mouser order plus two JLCPCB 2-layer bare boards soldered by the owner, and six grafts from the other architectures and the judges (catalog Coilcraft LPF inductors, the G5V-2 DPDT relay, the restored 10 s hardware key-down cutoff, the restored independent frequency counter, a plated thermal slot under the PA, and a pre-agreed ordering gate).
- **Cost (section 8.4):** capped total including 15 % contingency **USD 167.95 low, 190.29 planning, 212.64 high**. The planning case fits the USD 200 cap with USD 9.71 of margin. The high case, which stacks every high estimate and a Mouser tariff pass-through that no architect had counted, does **not** fit by itself: it is held under the cap by the ordering gate and its pre-agreed guard ladder, first by the owner's own copper wire (USD 197.47 capped). This is stated plainly because cost is the owner's one firm constraint.
- **What the owner gets:** 5 W CW (estimated 4.4 W at 6.4 V, marginal against the 3.97 W floor of REQ-SYS-012), a 500 Hz crystal-ladder receiver with MDS about -140 dBm (Low confidence), about 8 to 15 h battery life at 1:9, a case of about 142 x 70 x 42 mm (149 mm with the SMA) and 277 to 347 g, and only hand-solderable parts: no BGA, no leadless part, no pitch under 0.65 mm, no hidden thermal pad.
- **What it gives up (section 8.8):** the display (Morse menu instead), in-radio charging, the TCXO in the first build (carrier accuracy relaxed from 2.5 ppm to 30 ppm after calibration, TBR), the conductive case coating, the tuning encoder, the on-board transmit monitor port (an add-back), and the stainless SMA jack.
- **Problem requiring a decision (one sentence):** which radio architecture, parts list and requirement set let the owner build the first complete cwht at his home bench for under USD 200 all in, with listed-price parts only.
- **Robustness verdict (section 6):** Robust for the enhancing matrix (no single weight or Low-confidence score perturbation changes the top rank; A4 leads by 85 points). **Not robust** for the mandatory cost screen: A4's high case and the M1 failures of A2 and A3 turn on shipping and tariff lines that are estimates.
- **Three findings for the owner before deciding:**
  1. **No through-hole 5 W final exists at 144 MHz in catalog stock.** The through-hole choices are new-old-stock TO-220 and TO-39 parts that reach 0.5 to 4.5 W at 7.2 V, and the IRF510 has almost no gain at 144 MHz (section 7.3). Surface-mount SOT-89 and SOT-23 devices are the least-exception path; A4 uses them and nothing harder.
  2. **Two safety controls were missing from the cheapest architecture as submitted** (the REQ-SYS-055 10 s hardware cutoff and the REQ-SYS-182 independent frequency counter). A4 restores both for about USD 1 of parts.
  3. **Mouser passes a share of US tariffs on China-origin parts through as an order line.** No architecture counted it. It is carried here as USD 4 to 12 (estimate) and must be read at the Mouser cart before ordering.
- **Owner's decision (section 10):** pending.

## 2. Problem and decision context

- **Mission and system context:** the whole radio. The cost cap, the hand-assembly rule and the display removal touch every block of `docs/design/concept.md` sections 5 and 7, the L0 constraints CON-010, CON-015 and CON-026, NGO-027, NGO-028, MOE-007 and MOE-013, and about 80 L1 requirements (section 8.10).
- **Decision needed and intended outcome:** after the decision, the preliminary design has one architecture, one bill of materials with listed prices and sellers, one cost roll-up with an ordering gate, one user-interface concept (Morse audio menu) and one list of requirement deltas for a re-baseline CR. The PDR trades of WP-PDR-19 to 28 then close on this basis instead of the PCBWay turnkey basis.
- **Owner direction (verbatim extracts; the full statements are in the status note).** Section 6: "I think the first radio can't be more than $200 um, all in. Uh, you do not have to account for filament cost." "if I have to go ask a website for a quote for a part, that's a bad sign." "if we need to, you know, design our own amplifiers using MOSFETs, then so be it." "I've used JLCPCB before. So I'm down to get a bare PCB and then solder the through hole components myself." "I would be open to dropping the LCD screen and instead having a Morse code audio only interface." "you would press a button to enter the menu, and then you would hear the options in Morse code, and then you would pick like a letter to go to a different option, and then you can change numbers, and it will read it back to you to confirm that it was correct. And then you would say like Roger for like you know setting it, or um, N for no." Section 8 (governs): "Yeah, I'm flexible on the size. Cost is firm. I think it needs to be less than 200 dollars. Uh, that that is a firm constraint. Um, the size and through hole are negotiable. I think ideally it's a through hole part, but if it needs to be a surface mount part, that's fine. I think the the uh, ones that get trickier are ball arrays. or other uh, chips that really require like flow soldering to do them accurately. But I can I can do surface mount parts." "I need to be able to solder it at my home bench you know and I don't have like a very sophisticated soldering setup. I have a heat gun um, I have solder I have flux".
- **Lead SE reading applied here (status note section 8, items 1 to 6, with section 6 where section 8 is silent):**
  1. FIRM: the first complete radio costs under USD 200 all in (boards, parts, shipping, import duty); filament excluded. Committed instruments (tinySA Ultra, SI-034) are outside the cap (to be confirmed by the owner).
  2. Every part has a published price and stock at a catalog distributor or maker shop; nothing sold only on quote.
  3. Through-hole is preferred. Surface-mount parts are acceptable where the owner can hand-solder them with an iron, a heat gun, solder and flux (SOIC, SOT-23, SOT-89, SOT-223, TO-252, 1206 and 0805 passives, QFP and TSSOP of 0.65 mm pitch or more, PowerSO-class devices with a heat gun). Excluded: BGA and any part that in practice needs reflow or a stencil (fine-pitch leadless packages). Every part with a hidden exposed thermal pad is flagged. A pre-built module with pin headers and a listed price counts as through-hole compatible (to be confirmed).
  4. Discrete op-amp and MOSFET circuits, including a discrete PA, are welcome.
  5. Board: a bare JLCPCB board soldered by the owner; perfboard or Manhattan for prototypes and non-RF sections. The owner has perfboard and some potentiometers.
  6. One radio first, in the owner-printed PETG case.
  7. Size is negotiable: the REQ-SYS-102 (350 g) and REQ-SYS-103 (140 x 70 x 40 mm) envelope is the ideal, traded against cost and buildability; the envelope and mass are estimated and any delta reported.
  8. No display: the Morse-code audio menu replaces it.
- **Constraints:** Part 97 (97.307(e) spurious limit of 25 uW for a 5 W transmitter, REQ-SYS-017; 60 dBc design target, REQ-SYS-018). The owner's bench (SI-013: NanoVNA, 50 ohm dummy load, bench supply; plus the tinySA Ultra of SI-034, a heat gun, solder, flux). The owner's rule that LTspice simulations of the amplifiers and filters must run and count as evidence (status note section 9).
- **Prior related decisions:** ADR-007 and SI-031 (PCBWay turnkey, owner through-hole only) and SI-028 (PA from DigiKey, Mouser or PCBWay distributors) are superseded if this study is adopted. TS-001 (PD54008L-E PA, Inrad or tolerance-designed ladder, SRR decision 54), TS-007 (Si5351A plus TCXO), TS-004 (4-layer 1.0 mm board), TS-011 (option C printed case with coating and CNC fallback; its M8 finding that PETG fails near a 4 W PA). CR-003 revision 3 and CR-006 revision 2 are Submitted and held for revision (status note section 6).
- **Research consulted (all 2026-09-27):** the seven block research reports of this study (transmitter and PA, receiver, frequency generation, power and charging, UI and audio, fabrication and shipping, enclosure), quoted in section 11; `docs/research/pa-device-candidates.md`; `docs/research/cw-selectivity-options.md`; `docs/research/tr-switch-candidates.md`; the three architectures and three judge reports of section 4.3; the author's own web reads marked "read today" in section 8.3.

## 3. Decision matrix setup and rationale

### 3.1 Criteria and operational definitions

Mandatory criteria are pass or fail; an alternative that fails one is dropped before scoring (SE HB section 6.8.1.2.1). Because the M1 screen of A2 and A3 turns on Low-confidence estimates (section 6 item 4), all four candidate architectures are still scored in section 5, for information and for the sensitivity run.

| ID | Criterion | Type | Operational definition | Scale | Weight |
|---|---|---|---|---|---|
| M1 | Cost cap | Mandatory | Capped planning total (listed prices plus the midpoint of every estimated line, shipping, duty and the Mouser tariff pass-through, times 1.15) is under USD 200; and the high case is brought under USD 200 by a pre-agreed guard ladder that costs no performance requirement | pass / fail | n/a |
| M2 | Listed prices | Mandatory | Every part has a published price and stock at a catalog distributor or maker shop (aggregator reads accepted provisionally, pending the owner's browser check); no part is sold only on quote | pass / fail | n/a |
| M3 | Hand-solderable | Mandatory | No BGA and no part that in practice needs reflow or a stencil (fine-pitch leadless). Leaded parts with pitch under 0.65 mm and leadless parts with large pads are admitted only as flagged exceptions and are scored in C3 | pass / fail | n/a |
| M4 | Safety controls | Mandatory | Every hardware hazard control adopted at SRR (REQ-SYS-055, 083 to 085, 092, 120, 180, 181, 182) is implemented, or its removal is recorded as a requirement delta for the owner; no Red safety risk that no step reduces to Yellow (06 section 13 item 2) | pass / fail | n/a |
| M5 | Emissions path | Mandatory | A design path to 97.307(e): a harmonic filter of at least 45 dB ideal attenuation at 2f plus a stated verification (LTspice and tinySA) | pass / fail | n/a |
| C1 | Cost margin | Enhancing | Capped planning total, USD (the M1 figure) | 1: >= 200 / 3: 190 / 5: <= 170 (linear between) | 25 |
| C2 | Cost robustness | Enhancing | Capped high-case total and what it takes to hold the cap | 1: over 200 after every guard that costs no performance / 3: under 200 after guards that need only owner confirmations (owned stock, a verified shipping line) / 5: under 200 with no guard | 10 |
| C3 | Hand-solderability | Enhancing | Count of flagged exceptions (hidden pad, leadless, pitch under 0.65 mm) | 1: three or more / 3: one / 5: none | 15 |
| C4 | Build and alignment effort | Enhancing | Count of RF networks the owner designs or tunes by hand plus hand-wound filter or match coils, and board-area closure | 1: two or more hand matches, wound LPF and BPF, board does not close / 3: one hand match, wound BPF, catalog LPF / 5: no winding, no match to design | 10 |
| C5 | RF and emissions confidence | Enhancing | Evidence behind the 60 dBc target, 5 W and MDS: vendor harmonic data, LPF construction, reference accuracy, T/R isolation | 1: no harmonic data, wound LPF, unvalidated mixer, clamp overstress / 3: no PA harmonic data but catalog LPF and DPDT / 5: guaranteed harmonics, catalog LPF, TCXO, DPDT, monitor port | 15 |
| C6 | Envelope and mass | Enhancing | Case volume against 140 x 70 x 40 mm and mass against 350 g | 1: over 20 % volume or over 350 g / 3: up to 8 % over, or one axis over / 5: inside on all axes and under 350 g | 10 |
| C7 | Requirement deltas and firmware scope | Enhancing | Number and size of requirement relaxations, unrecorded gaps and firmware added | 1: safety requirements dropped silently / 3: deltas recorded, moderate firmware / 5: wording-only deltas, no firmware added | 5 |
| C8 | Safety margin | Enhancing | PA junction margin to 110 C at 45 C, heat path relative to cells and PETG, Catastrophic hazards kept in the box | 1: junction over 110 C / 3: junction under 110 C with in-radio charger or unanalyzed heat path next to the cells / 5: junction margin over 20 K, heat outside the case, no charger in the box | 10 |
| | | | | **Sum of weights** | **100** |

Criteria considered (06 section 13 item 1): safety used as M4 and C8; first power-on used as C4 (build and alignment effort is the main first-power-on driver); cost used as M1, C1 and C2; performance margin used as M5 and C5; schedule omitted because every alternative uses a JLCPCB bare board and catalog parts with similar lead times (about 1 to 2 weeks), so it does not discriminate; system security omitted because no alternative changes the USB firmware-loading or key-input attack surfaces of 07 section 16.2 (the Morse menu is common to all and its command path is assessed in WP-PDR-17).

Other criteria considered and not used: sourcing breadth (folded into M2 and C2, because shipments and unread lines drive the cost robustness), and the judges' three lenses as separate criteria (their content is carried by C1, C2 for cost and sourcing; C5 and M5 for RF and regulatory; C3, C4, C6 and C8 for buildability, size and safety).

### 3.2 Alternatives

| ID | Alternative | Description | Source |
|---|---|---|---|
| A0 | Current baseline (do nothing) | SRR concept: PCBWay 4-layer board with turnkey SMT, PD54008L-E PA, Inrad #111 or tolerance ladder with 24-bit ADC, LS013B7DH03 display, encoders, in-radio 2S charging, printed case with coating and a PCBWay CNC fallback; unit budget USD 610 over three units | `docs/plan/cost-estimate.md`; TS-001; TS-011; CR-003; CR-006 |
| A1 | min-cost (as submitted) | AFT05MS004NT1 SOT-89 PA with GVA-84+ driver, JFET superhet with hand-matched 500 Hz ladder, Morse-only UI, cells charged in an XTAR VC2, one Mouser order plus two JLCPCB boards; USD 169.15 to 199.17 capped | Architecture report "min-cost" |
| A2 | performance-in-cap PIC-5 | RD01MUS2 plus RD07MUS2B discrete pair (RF Parts), bare Si5351A with HCI TCXO, diode-ring superhet, ADC audio path, in-radio 2S charger (CN3302 chain), four buttons; USD 165.50 to 218.28 capped | Architecture report "performance-in-cap" |
| A3 | buildability B1 | RA07M1317M module PA (RF Parts), no hand-wound parts (Coilcraft LPF, XRMW slug-tuned BPF, TC1-1T+ mixer), bare Si5351A with TCXO, ADC audio, charging outside the radio, 40 dB monitor port; USD 183.05 to 240.02 capped | Architecture report "buildability" |
| A4 | min-cost with grafts (recommended) | A1 plus: Coilcraft 1812SMS LPF (from A3), G5V-2 DPDT relay (from A2 and A3), second LM393 for the REQ-SYS-055 10 s cutoff and a cell 60 C trip (from A3), SN74LVC74ADBR prescaler into a PIO counter for REQ-SYS-182 (from A2 and A3), a solder-filled plated slot and via field under the PA tab (from A2), XTAR MC1 charger in place of the VC2 (author, read today), the ordering gate with guards and add-backs (from A2), board fences cut from spare boards (from A2) | This study, sections 8.1 to 8.4 |

Alternatives pruned before scoring, with reason:
- **All-through-hole radio.** No through-hole VHF final is in active production at a catalog distributor; the NOS RD06HVF1 (TO-220, RF Parts USD 9.91) gives an estimated 3.5 to 4.5 W at 7.2 V and about 2.8 W at 6.0 V, and TO-39 bipolar chains give 0.5 to 1 W (transmitter research, section 7.3). The TO-92 J310 is out of stock at LCSC and unverified at DigiKey and Mouser. Pruned as infeasible at 5 W; kept only as a reduced-power fallback (EX-TX-4 of the transmitter research).
- **Generic MOSFET PA (IRF510, BS170, 2N7000).** 0 to 5 dB of power gain at 144 MHz for the IRF510 (Ciss 135 to 180 pF, 7 nH source lead); the BS170 and 2N7000 are 0.1 to 0.3 W pre-drivers at best (estimate). Pruned on physics.
- **Direct-conversion receiver (receiver research L2).** 0 dB opposite-sideband response 1.4 kHz from the wanted signal and 3 dB double-sideband noise penalty; fails REQ-SYS-022 and 025. Kept only as a perfboard audio-chain prototype.
- **SA612 mixer, commercial CW filters (Inrad #111 USD 118, KVG on quote), LMX2571 synthesizer (WQFN with exposed pad, 0.5 mm).** Discontinued, over the cap, sold on quote, or reflow-only.
- **Perfboard or Manhattan for the RF sections.** Admitted for prototypes and non-RF sections only (status note section 6); a 144 MHz LPF, PA match and front end need controlled ground and short returns that a 2-layer board with a solid pour gives for USD 2.

### 3.3 Weight rationale

Cost carries 35 (C1 25 and C2 10) because it is the owner's only firm constraint ("Cost is firm"); C2 is separate because the owner's cap is breached by the high case, not the planning case, and the margin depends on unread shipping lines. Hand-solderability (C3, 15) and RF and emissions confidence (C5, 15) come next: the first is the owner's stated reason for the SMD boundary, the second is a legal limit (97.307(e)) and the radio's purpose. Build effort (C4, 10), envelope (C6, 10, negotiable per status note section 8 item 2) and safety margin (C8, 10; the mandatory safety floor is M4) follow. Deltas and firmware scope (C7, 5) matter least because the Morse UI adds the same firmware to every alternative. No weight was set by the owner directly.

### 3.4 Evaluation methods

| Criterion | Method | Tool | Evidence artifact |
|---|---|---|---|
| M1, C1, C2 | Cost query (listed pages, aggregator), budget roll-up with contingency | Python roll-up script (author's scratchpad, reproduced in section 8.4) | This report sections 4.3 and 8.4; architecture reports |
| M2 | Cost query | WebFetch of seller and OEMsTrade pages | Section 8.3 URLs |
| M3, C3 | Datasheet and package comparison | Research reports | Section 8.6 |
| M4, C8 | Requirement trace and derived thermal chain | Hand calculation | Sections 4.2, 7.3 |
| M5, C5 | Datasheet comparison and derived LPF response | Transmitter research LPF derivation; LTspice run pending (WP-PDR-21, TV-014) | Section 7.3 |
| C4 | Design inspection | Architecture reports | Section 4.2 |
| C6 | Budget analysis (stack-up, mass roll-up) | Hand calculation | Section 8.5 |
| C7 | Requirement trace | `docs/requirements/sys/requirements.json` | Section 8.10 |

### 3.5 Setup matrix (before scoring)

| Criterion | Weight | A0 | A1 | A2 | A3 | A4 |
|---|---|---|---|---|---|---|
| M1 to M5 | n/a | | | | | |
| C1 | 25 | | | | | |
| C2 | 10 | | | | | |
| C3 | 15 | | | | | |
| C4 | 10 | | | | | |
| C5 | 15 | | | | | |
| C6 | 10 | | | | | |
| C7 | 5 | | | | | |
| C8 | 10 | | | | | |

## 4. Scoring rationale

### 4.1 Mandatory screening

A common Mouser tariff line is added to every alternative for M1 (estimate: 20 to 40 % on the China-origin share of the Mouser goods; basis in section 8.4). A1 as submitted has about USD 76 of Mouser goods, A2 and A3 about USD 34 each.

| Alternative | M1 cost | M2 listed | M3 solderable | M4 safety | M5 emissions | Result |
|---|---|---|---|---|---|---|
| A0 | **fail**: USD 828 to 1644 for three units (cost model); PCBWay turnkey alone is USD 300 to 500 | pass | pass (turnkey places the SMT) but moot | pass | pass | dropped |
| A1 | pass on its figures (199.17 high); planning about USD 193.85 with the AO3400A correction and the tariff midpoint | pass (provisional: all Mouser rows via aggregator) | pass | **fail**: REQ-SYS-055 and REQ-SYS-182 not implemented and no delta recorded (judges 0, 1, 2) | pass (ideal LPF 48 dB at 2f) | dropped; A4 is its repair |
| A2 | **fail (conditional, Low)**: planning 196.92 plus the tariff midpoint (about USD 5.75 capped) is about 202.67; high 218.28 plus tariff; the planning figure also needs an unverified LCSC-into-JLCPCB merge | pass (provisional) | pass with three flagged exceptions (hidden-pad leadless RD07MUS2B, 0.5 mm MSOP Si5351A, leadless TCXO) | pass | pass | kept for information |
| A3 | **fail (conditional, Low)**: expected 199.23 (judge 2 re-sum 199.63) plus the tariff midpoint is about 205; high 240.02; the IMR VC2 at USD 9.99 shows "Notify Me When Available" (judge 1) | pass (provisional) | pass with two flagged exceptions (0.5 mm MSOP, leadless TCXO) | pass | pass | kept for information |
| A4 | **pass**: planning 190.29; high 212.64 held by guard G1 to 197.47 (section 8.4) | pass (provisional) | pass, no exception | pass (both controls restored) | pass | kept |

### 4.2 Enhancing scores

| Criterion | Alt | Measured value | Score | Conf. | Evidence |
|---|---|---|---|---|---|
| C1 | A1 | about USD 193.85 planning (184.16 midpoint + 0.49 AO3400A + 9.20 tariff) | 2 | Low | min-cost report section 2.3; judge 1 AO3400A; section 8.4 tariff |
| C1 | A2 | about USD 202.67 | 1 | Low | PIC-5 section 0; tariff estimate |
| C1 | A3 | about USD 205 | 1 | Low | B1 section 5; judge 2 re-sum |
| C1 | A4 | USD 190.29 | 3 | Low | section 8.4 |
| C2 | A1 | high about 214 with tariff; under 200 only with the owner's wire | 3 | Low | section 8.4 method applied to A1 |
| C2 | A2 | high about 225; needs owner wire and owner cells (G1, G2) | 2 | Low | PIC-5 section 9 |
| C2 | A3 | high about 247; the cuts include a PA change and an unverified JLC shipping cut | 1 | Low | B1 section 6 |
| C2 | A4 | high 212.64; 197.47 with the owner's wire | 3 | Low | section 8.4 |
| C3 | A1 | no exception | 5 | High | min-cost section 6 |
| C3 | A2 | three exceptions | 1 | High | PIC-5 section 6 |
| C3 | A3 | two exceptions | 2 | High | B1 section 8 |
| C3 | A4 | no exception (the prescaler is SSOP-14 at 0.65 mm, inside the owner's list) | 5 | High | section 8.6 |
| C4 | A1 | NXP match rebuilt with wound 12 to 27 nH coils, wound LPF, wound BPF, crystal matching, two boards | 2 | Medium | min-cost sections 1, 8 |
| C4 | A2 | two copied match networks, wound LPF and BPF, charger chain, board does not close (67 cm2 on 60 cm2) | 1 | Medium | judges 0, 1, 2 |
| C4 | A3 | no winding, module PA, slug-tuned BPF, one board | 5 | Medium | B1 section 2 |
| C4 | A4 | one hand match (NXP reference), wound BPF, catalog LPF | 3 | Medium | section 8.1 |
| C5 | A1 | no AFT05 harmonic data, wound LPF, 30 ppm, unvalidated JFET mixer, SPDT relay with about 20 mA peak into 15 mA clamps | 2 | Low | judge 1 |
| C5 | A2 | vendor harmonics (2f -37 to -40 dBc), TCXO, wound LPF, two hand matches | 4 | Medium | transmitter research L2 |
| C5 | A3 | guaranteed module harmonics (2f -25 dBc max), Coilcraft LPF, TCXO, DPDT, monitor port | 5 | Medium | transmitter research L1 |
| C5 | A4 | no AFT05 harmonic data, but catalog LPF with higher self-resonance, DPDT with the RX-grounding pole, frequency counter; 30 ppm; JFET mixer | 3 | Low | sections 7.3, 8.1 |
| C6 | A1 | 142 x 70 x 42 mm (+6.5 % volume; 149 mm with the SMA); 275 to 345 g | 3 | Medium | min-cost section 5; sink 25.4 mm confirmed by judges 1 and 2 |
| C6 | A2 | 138 x 67 x 42 mm including the SMA; about 293 g; fallback board adds 7 mm of width | 4 | Low | PIC-5 section 5 |
| C6 | A3 | 124 x 69 x 46 mm with the 25.4 mm sink (+6 mm height); about 295 g | 3 | Medium | judges 1, 2 |
| C6 | A4 | 142 x 70 x 42 mm (149 with the SMA); 277 to 347 g | 3 | Medium | section 8.5 |
| C7 | A1 | 010 relaxed 12x; 141 and charging retired; 055 and 182 dropped without a delta | 2 | Medium | judges 0, 2 |
| C7 | A2 | 010 and charging kept; ADR audio path needs a TS-001 re-ruling; largest firmware | 3 | Medium | PIC-5 section 8 |
| C7 | A3 | 010 and 141 kept; charging retired; ADR audio re-ruling; DSP firmware | 3 | Medium | B1 section 9 |
| C7 | A4 | 010 relaxed (TBR, restored by the TCXO add-back); charging retired; 141 deferred to an add-back; every delta recorded; analog audio | 3 | Medium | section 8.10 |
| C8 | A1 | Tj about 160 C with 8 vias (judge 1: 8 x 0.3 mm vias are about 24 K/W, not 8) | 1 | Low | judge 1 |
| C8 | A2 | Tj about 92 C; full in-radio 2S charger (Catastrophic hazard HZ-002 kept, with its controls) | 3 | Low | PIC-5 section 4 |
| C8 | A3 | module sink fins-down inside the PETG case beside the cells at 5 to 7 W, unanalyzed | 2 | Low | judges 1, 2 |
| C8 | A4 | Tj about 86 to 97 C at 45 C (derived, section 7.3); heat outside the case; no charger in the box | 4 | Low | section 7.3 |

### 4.3 Independent architects' and judges' results (inputs to this study)

Three architects worked independently, one per angle (minimum cost, performance inside the cap, buildability); three judges then scored all three, each through a different lens. Their numbers are reproduced here as evidence; this study's own matrix is section 5.

**Architect totals (capped, including 15 % contingency, as submitted):**

| Architecture | Low | Planning or expected | High |
|---|---|---|---|
| min-cost (A1) | 169.15 | (midpoint 184.16) | 199.17 |
| PIC-5 (A2) | 165.50 | 196.92 | 218.28 |
| B1 (A3) | 183.05 | 199.23 | 240.02 |

**Judge 0 (cost-and-sourcing lens; 1 to 10; weighted = cost x3, sourcing x2, envelope x2, others x1, maximum 120):**

| Criterion | min-cost | PIC-5 | B1 |
|---|---|---|---|
| Fits USD 200 with contingency | 8 | 6 | 5 |
| Listed-price sourcing verified | 5 | 6 | 6 |
| Envelope and mass | 5 | 7 | 7 |
| Hand-solderability | 9 | 4 | 6 |
| 97.307(e) and RF credibility | 5 | 6 | 8 |
| Safety controls kept | 4 | 7 | 7 |
| Owner buildability | 6 | 4 | 8 |
| Firmware scope | 7 | 5 | 6 |
| Requirement deltas | 4 | 7 | 6 |
| **Unweighted (/90)** | **53** | **52** | **59** |
| **Weighted (/120)** | **79** | **77** | **82** |

Judge 0's ranking put min-cost first, "ONLY IF" REQ-SYS-055 and REQ-SYS-182 are restored, although B1 has the higher weighted total: the judge ranked on the cost cap, not on the total. This study records that inconsistency and resolves it by making the cap mandatory (M1) and scoring cost robustness separately (C2).

**Judge 1 (RF-and-regulatory lens; 1 to 10; unweighted sum):** min-cost 60, B1 57, PIC-5 51. Cost: 8 / 4 / 5 (min-cost / B1 / PIC-5); sourcing 7 / 6 / 6; envelope 6 / 6 / 8; hand-solderable 9 / 6 / 4; emissions and RF 5 / 9 / 8; safety 6 / 6 / 7; buildability 5 / 8 / 4; firmware 8 / 5 / 4; deltas 6 / 7 / 5. Ranking: min-cost, B1, PIC-5.

**Judge 2 (owner buildability, size and safety lens; 1 to 10; weighted out of 10):** min-cost 6.8, PIC-5 5.9, B1 5.6. Cost 8 / 5 / 4 (min-cost / PIC-5 / B1); sourcing 6 / 6 / 6; envelope 6 / 8 / 6; hand-solder 9 / 4 / 6; emissions 6 / 7 / 8; safety 6 / 7 / 5; buildability 7 / 4 / 7; firmware 8 / 5 / 5; deltas 4 / 6 / 6. Ranking: min-cost, PIC-5, B1.

**All three judges ranked min-cost first, each conditionally.** Their arithmetic checks all reproduced the architects' totals, with these corrections: min-cost's own AO3400A flag (+0.86) moves its high case to 200.16 (judge 1); PIC-5's planning total is 196.93, not 196.92 (rounding); B1's itemized expected rows re-sum to about USD 199.63, a margin of about 0.37 (judge 2).

**Findings the judges called fatal or near-fatal, and how A4 treats each:**

| Finding (judge) | Treatment in A4 |
|---|---|
| min-cost drops REQ-SYS-055 (7.5 to 13 s hardware cutoff) and REQ-SYS-182 (independent frequency verification) with no delta (0, 2) | Restored: second LM393P monostable; SN74LVC74ADBR prescaler into an RP2350 PIO counter (section 8.1) |
| min-cost PA thermal path: 8 vias of 0.3 mm are about 24 K/W, so Tj is about 160 C (1) | Solder-filled plated slot plus 30 or more 0.4 mm vias under the tab; Tj estimate 86 to 97 C (section 7.3); ALC power derate as fallback |
| min-cost high case is 200.16 with the AO3400A correction (1) | Carried in the high case (+0.86); the cap is held by the ordering gate (section 8.4) |
| No architecture counts Mouser's tariff pass-through (2) | Carried as USD 4 to 12 (estimate) in every total |
| min-cost has no AFT05 harmonic data and wound LPF coils; SPDT relay overstresses the RX clamps (0, 1, 2) | Coilcraft 1812SMS LPF; G5V-2 DPDT with the RX-grounding pole; LTspice and tinySA verification before first on-air use |
| Sourcing evidence for Mouser is aggregator-only (0) | Owner price-check list (section 8.11) before ordering |
| Boyd sink height disputed (18.3 against 25.4 mm) (0, 1, 2) | Settled at 25.4 mm (Farnell and Newark listings, read by judges 1 and 2); A4 uses it as an end wall, so the case is 42 mm tall |
| PIC-5 and B1 high cases break the cap; PIC-5 board over-full; B1 sink inside PETG beside the cells (0, 1, 2) | Scored in C1, C2, C4, C8 |

**Grafts proposed by the judges and their disposition:**

| Graft | From | Disposition in A4 |
|---|---|---|
| Coilcraft 1812SMS LPF inductors | B1 | **Adopted** (+USD 5.70 listed via aggregator) |
| G5V-2 DPDT relay | PIC-5, B1 | **Adopted** (+0.88) |
| 10 s hardware cutoff and cell 60 C trip on a second LM393 | B1 | **Adopted** (+0.53) |
| 74LVC74 prescaler for REQ-SYS-182 | PIC-5, B1 | **Adopted** (SN74LVC74ADBR, +0.34, read today) |
| Plated slot and dense via field under the PA | PIC-5 | **Adopted** (board feature, no part cost) |
| Ordering gate with pre-agreed guards and add-backs | PIC-5 | **Adopted** (section 8.4) |
| Board-level fences cut from spare boards | PIC-5 | **Adopted** (no cost) |
| Heat sink as an end wall, fins outside | min-cost | **Kept** |
| One US distributor; LCSC only if the JLC merge is verified | min-cost | **Kept** |
| Analog receive audio chain (no ADC audio) | min-cost | **Kept** |
| 40 dB on-board monitor port (REQ-SYS-141) | B1 | **Add-back AB1** (the footprint and tap are on the board; the second SMA is bought when the gate allows) |
| TCXO | PIC-5, B1 | **Add-back AB2** (Epson TG2520SMN, leadless, flagged) |
| IMR bundle of P30B cells with the VC2 at USD 9.99 | B1 | **Not adopted**: the IMR VC2 page shows "Notify Me When Available" (judge 1). The XTAR MC1 at USD 4.99 in stock (read today) saves more |
| XRMW0505 slug-tuned BPF coils from LCSC | B1 | **Conditional guard G5**: only if the owner confirms at checkout that LCSC ships in the JLCPCB parcel |

## 5. Final decision matrix

Weighted score = weight x score; maximum 500. A0 is dropped at M1 and not scored.

| Criterion | Weight | A1 | A1 w | A2 | A2 w | A3 | A3 w | A4 | A4 w |
|---|---|---|---|---|---|---|---|---|---|
| C1 Cost margin | 25 | 2 | 50 | 1 | 25 | 1 | 25 | 3 | 75 |
| C2 Cost robustness | 10 | 3 | 30 | 2 | 20 | 1 | 10 | 3 | 30 |
| C3 Hand-solderability | 15 | 5 | 75 | 1 | 15 | 2 | 30 | 5 | 75 |
| C4 Build effort | 10 | 2 | 20 | 1 | 10 | 5 | 50 | 3 | 30 |
| C5 RF and emissions | 15 | 2 | 30 | 4 | 60 | 5 | 75 | 3 | 45 |
| C6 Envelope and mass | 10 | 3 | 30 | 4 | 40 | 3 | 30 | 3 | 30 |
| C7 Deltas and firmware | 5 | 2 | 10 | 3 | 15 | 3 | 15 | 3 | 15 |
| C8 Safety margin | 10 | 1 | 10 | 3 | 30 | 2 | 20 | 4 | 40 |
| **Total** | **100** | | **255** | | **215** | | **255** | | **340** |
| **Percent of maximum** | | | 51 % | | 43 % | | 51 % | | 68 % |
| **Rank** | | | 2= (fails M4) | | 4 (fails M1, conditional) | | 2= (fails M1, conditional) | | **1** |

## 6. Uncertainty and sensitivity statement

1. **Weight sensitivity.** Every weight moved by +10 and -10 points, the others rescaled to keep 100. A4 stays first in all 16 runs. Its smallest lead is 51.5 points (C5 at +10: A4 335.3, A3 283.8). No run changes the top rank.
2. **Score sensitivity.** Every Low-confidence cell (C1 and C2 for all alternatives, C5 for A1 and A4, C6 for A2, C8 for all) moved by +1 and -1 one at a time: A4 stays first in every case. A joint adverse case (every Low cell of A4 down one and every Low cell of the others up one, beyond the 14.4 rule) gives A1 315, A3 300, A4 280, A2 270; A1 is excluded by M4 and A4 is its repair, so the joint case does not change the recommendation, but it shows that A4's lead over A3 rests on cost cells that are Low.
3. **Assumptions and their evidence:**
   - Mouser prices are the aggregator republication of Mouser's own price and stock (section 8.3); two rows were re-read today (AFT05MS004NT1, AO3400A) and one new row (SN74LVC74ADBR).
   - Mouser free shipping starts at USD 100 in the US (search summary citing the EEVblog thread "MOUSER - FREE Shipping Threshold Increase!"; Low). Below it, standard shipping is estimated at USD 5 to 8.
   - Mouser charges "a percentage of the imposed tariffs" on some China-origin products (search summary of Mouser's tariff page, which timed out when fetched); users reported 20 % line items in January and February 2025 (The Amp Garage forum). The China-origin share of the A4 Mouser order is estimated at USD 20 to 30, because the Pico 2 (UK) and the Adafruit module (US) are not China-origin (Low).
   - JLCPCB shipping to the US is USD 12 to 25 (a forum report of 2026-03-19: about USD 12 shipping and about USD 2 tax on a USD 10 board order by Global Standard Direct Line, 12 days; the fabrication research estimate USD 15 to 25 for DDP express). JLCPCB collects 35 % (its tariff FAQ) to 60 % (Hack Club cost guide) on the board value at order.
   - The AFT05MS004N reference circuit gives 6.0 W at 7.5 V with 17.8 to 20.2 dB gain and 62 to 69 % drain efficiency, 136 to 174 MHz (datasheet Rev. 0, 7/2014, Tables 8 to 10, read by the min-cost architect); output at other voltages scaled by V squared (derived).
   - Receiver MDS about -140 dBm from the receiver research cascade (5.8 dB NF with a diode ring); the JFET mixer substitution is the architect's (Low, +/-2 dB).
4. **Robustness verdict:** **Robust** for the enhancing matrix. **Not robust** for the mandatory cost screen: (a) A4 passes M1 at planning with USD 9.71 of margin, but its high case needs guard G1; (b) A2 fails M1 at planning by about USD 2.67 and would pass if the Mouser tariff on its order is under about USD 2.7 and the LCSC merge is offered; (c) A3 fails by about USD 5.
5. **Value of information.** The measurements that settle the cost screen are the owner's browser reads of section 8.11: Mouser merchandise total, shipping and tariff line at the cart (without checking out), the JLCPCB quote for two designs, and the 18650BatteryStore shipping. About 30 minutes of the owner's time, before any order and before B1a. They were not performed before this recommendation because agents may not use carts. The engineering values that raise the Low scores of C5 and C8 are the LTspice run of the AFT05 match and LPF (WP-PDR-21, needs TV-014 accreditation, status note section 9) and the PA thermal chain (WP-PDR-28), both before the F0 freeze of the TX design.
6. **Limitations of the evaluation methods and tools:** prices are single-day reads, mostly through an aggregator; shipping, tariff and duty lines are estimates or forum reports; no cart was opened. Performance figures are datasheet values, graph reads (about +/-10 %) and hand-derived cascades; no LTspice run exists yet for this architecture, and TV-014 (LTspice) is not yet accredited. The thermal chain is a lumped hand estimate. Envelope and mass are stack-up estimates with an unread sink mass. The judges' scores are expert judgement, not measurement.

## 7. Risks and benefits of the surviving alternatives

### 7.1 Risks (four-part format, 06 sections 4, 6, 7)

| Alt | Risk statement | L | C (driving) | Score / band | Would be entered as |
|---|---|---|---|---|---|
| A4 | Given that the high-case estimate is USD 212.64 and the shipping, tariff and duty lines are unread, there is a possibility that the verified order exceeds USD 200, adversely impacting the owner's firm cost cap, leading to a cut in performance or an owner cap exception | 3 | 4 (performance: stakeholder input not met) | 12 / Red | merged into RSK-052 (steps: ordering gate; guard ladder) |
| A4 | Given that the AFT05MS004N datasheet gives no harmonic data and the match is rebuilt with 0805 parts and wound coils, there is a possibility that a harmonic exceeds 25 uW, adversely impacting 97.307(e) compliance (HZ-008), leading to a filter redesign and a board respin | 4 (no analysis yet) | 4 (regulatory rule) | 16 / Red | new RSK (steps: LTspice match and LPF, trap footprint, tinySA measurement into the dummy load before any on-air use) |
| A4 | Given a SOT-89 source tab cooled through a 1.6 mm board, there is a possibility that the junction exceeds 110 C at continuous key-down in 45 C ambient, adversely impacting REQ-SYS-112 and device life, leading to a power derate or PA board respin | 3 | 4 (performance: KDR) | 12 / Red | merged into RSK-006 |
| A4 | Given a JFET mixer that the research did not validate and Low-confidence NF values, there is a possibility that MDS is worse than -140 dBm or IIP3 too low, adversely impacting REQ-SYS-022 (KDR), leading to the diode-ring fallback | 3 | 4 (performance: KDR) | 12 / Red | new RSK |
| A4 | Given that the SN74LVC74A toggle rating at 3.3 V is recalled near 150 MHz, there is a possibility that the prescaler miscounts at 148 MHz, adversely impacting REQ-SYS-182 (HZ-008 control), leading to a faster divider part | 3 | 4 (regulatory rule) | 12 / Red | new RSK (step: datasheet check at PDR; fallback divider) |
| A4 | Given a 64 x 100 mm board that already carries about 58 cm2 of blocks, there is a possibility that the grafts do not fit, adversely impacting the envelope, leading to a 70 x 100 mm board and a case 6 mm wider | 3 | 2 (performance) | 6 / Yellow | new RSK |
| A4 | Given that a straight key's timing varies, there is a possibility that the Morse menu misreads entries, adversely impacting usability, leading to paddle-only menu entry | 3 | 2 (performance) | 6 / Yellow | new RSK |
| A4 | Given a PETG case whose heat-deflection temperature is about 69 C (TS-011 M8), there is a possibility that bosses near the PA board soften at 45 C ambient key-down, adversely impacting board retention, leading to a PC-class filament (not owned) or standoffs | 3 | 3 (performance) | 9 / Yellow | merged into the TS-011 M8 finding |
| A2 | Given a leadless NOS RD07MUS2B with a hidden source pad soldered with a heat gun, there is a possibility of a bad joint or overheated die, adversely impacting first power-on, leading to rework with the spare | 3 | 3 (first power-on) | 9 / Yellow | new RSK if selected |
| A2 | Given a high case of USD 218.28 plus tariff, there is a possibility the order exceeds the cap, adversely impacting the firm cap | 4 | 4 | 16 / Red | RSK-052 |
| A3 | Given a 5 to 7 W sink inside the PETG case beside the cells, there is a possibility that cell and case temperatures exceed limits, adversely impacting HZ-003 and HZ-007, leading to a case redesign | 3 | 4 (safety: HZ-003 and HZ-007 mapping) | 12 / Red | merged into RSK-006 |
| A3 | Given a high case of USD 240.02, there is a possibility the order exceeds the cap | 4 | 4 | 16 / Red | RSK-052 |

Aggregate risk (maximum score): A2 16, A3 16, A4 16. The A4 Reds are all Research or Mitigate risks with steps due before the F0 freeze of the TX and RX designs; none is a safety-consequence-5 risk.

### 7.2 Benefits beyond the scored criteria

| Alt | Benefits |
|---|---|
| A4 | One distributor order (Mouser) plus the boards and the cells: three paid shipments. The AFT05 is in active production, in stock at Mouser and Newark, rated for 65:1 VSWR (strong for REQ-SYS-013), and covers 136 to 941 MHz, so a later 70 cm revision keeps the device. The TX drain needs no high-side switch (idle leakage at VGS 0 is at most 1 uA). Charging outside the radio removes the Catastrophic HZ-002 charger chain from the box. Analog audio keeps the TS-001 audio decision. |
| A2 | Keeps in-radio charging, the TCXO and the best envelope. |
| A3 | Easiest build: no winding, no PA match; guaranteed harmonics. |

### 7.3 Feasibility: the PA and the receiver at 144 MHz with hand-solderable parts

**Through-hole at 144 MHz, honestly (transmitter and receiver research).**
- No through-hole VHF power device is in active production and stocked by a franchised distributor. DigiKey shows 0 stock (or minimum orders of 500 to 1000) for 2N3866, 2N4427 and 2N5109. RF Parts lists NOS parts with prices (RD06HVF1 USD 9.91, RD15HVF1 USD 14.91, 2N4427 USD 3.91), which meets the listed-price rule but is a finite supply.
- The RD06HVF1 (TO-220, a 12.5 V part) reads 3.8 W at 7 V and 2.8 W at 6 V on the datasheet graph: it cannot hold 5 W across the pack. A TO-39 chain gives 0.5 to 1 W (estimate).
- The IRF510 has roughly 0 to 5 dB of power gain at 144 MHz; the BS170 and 2N7000 are DC switches here.
- The TO-92 J310 is out of stock at LCSC (USD 2.55 listed); the SOT-23 MMBFJ310 is in stock everywhere. The SA612 mixer is discontinued. A 146 MHz tuned circuit has no catalog through-hole coil.
- **Conclusion:** a 5 W 2 m radio from catalog stock needs a handful of SOT-89 and SOT-23 parts and 0805 or 1206 capacitors in the RF sections. Everything else in A4 is through-hole or a module.

**PA (A4).**
- Line-up: Si5351A CLK1 (about +7 to +10 dBm) into a pad, GVA-84+ MMIC (about +19 dBm out), AFT05MS004NT1 with the NXP 136 to 174 MHz broadband reference match (0805 C0G in place of the 0603 ATC parts, wound 12 to 27 nH coils of 1.5 to 3 turns), then the G5V-2 relay and a 7-pole Chebyshev LPF (fc 165 MHz; Coilcraft 1812SMS 68, 82, 68 nH; 1206 C0G 22, 39, 39, 22 pF, re-optimized for the 82 nH part) with a footprint for one series-LC trap.
- Output: about 6.0 W at 7.5 V available (vendor reference), estimated 4.4 W at 6.4 V, 3.8 W at 6.0 V and 7.5 W at 8.4 V (V squared scaling; the ALC and a firmware cap hold 5 W). REQ-SYS-012 is met marginally at 6.4 V (4.4 W against 3.97 W).
- Power steps 0.5, 1 and 2 W come from gate bias (vendor Fig. 12: 0 to 5.5 W over VGS 1.5 to 2.4 V at 155 MHz).
- Harmonics: no vendor data, so the LPF carries the no-data case (ideal 48 dB at 2f, 76 dB at 3f). With a 2f output of, say, -15 dBc before the filter, the filter's 48 dB gives -63 dBc, 10 dB inside the 53 dBc legal limit and 3 dB past the 60 dBc target. This is illustrative until the LTspice run and the tinySA measurement.
- Thermal (derived, Low): dissipation about 3.7 W in the AFT05 at 5 W out (about 60 % drain efficiency) plus 0.5 W in the GVA-84+. Chain: 4.4 K/W junction to case (datasheet), then the board. Judge 1 showed that 8 plain 0.3 mm vias are about 24 K/W, which would put Tj near 160 C. A4 instead uses a solder-filled plated slot of about 1 x 3 mm under the tab (about 7 K/W alone) in parallel with 30 solder-filled 0.4 mm vias (about 3 K/W), about 2 K/W for the barrel paths, and 3 to 6 K/W including spreading in the pads; then 1 K/W interface and 2.6 K/W sink. Total 11 to 14 K/W, rise 41 to 52 K, **Tj about 86 to 97 C at 45 C** against 110 C. The sink face rises about 10 to 11 K, so REQ-SYS-113 (48 C at 25 C) is met. Fallback: an ALC derate to 4 W at high ambient, recorded as a REQ-SYS-112 condition.
- Keying and safety: CLK1 enable and the gate envelope are the two independent conditions of REQ-SYS-120. The hardware 10 s cutoff (REQ-SYS-055), the 150 to 180 s backstop (REQ-SYS-180), the 95 C sink trip (REQ-SYS-181), the cell 60 C trip and the VBUS inhibit (REQ-SYS-092) are open-collector clamps wired-OR on the gate node, on by default at reset.

**Receiver (A4).**
- Chain: G5V-2 pole A, pole B grounding the RX input in transmit, 1N5711 clamp pair, BPF1 (2 wound air-coil resonators), MMBFJ310 grounded gate, BPF2 (3 resonators), MMBFJ310 grounded gate, MMBFJ310 mixer (LO 136 to 140 MHz low side, CLK0), diplexer, 2N3904 post-mixer amplifier, 6-pole 500 Hz ladder of 8.000 MHz crystals matched on the NanoVNA (6 from 10), two 2N3904 IF stages whose gain is a PWM-derived control voltage (AGC and volume), MMBFJ310 product detector (BFO on CLK2), NE5532 preamp and filter, summing with the PWM sidetone and menu tones, MCP6002 headphone buffers on 5 V, 220 uF coupling, attenuator, switched jack.
- Numbers: NF and MDS about -140 dBm (Low, +/-2 dB); -6 dB bandwidth about 470 to 525 Hz and -60 dB about 2.4 kHz (same-lot Monte Carlo); image rejection 83 dB ideal from 5 resonators (Low); RMDR about 83 dB set by Si5351 phase noise; AGC after the crystal filter, so no pumping.
- The receiver research found that one J310 stage fails REQ-SYS-022 (8.4 dB NF); two stages are needed.
- Fallback for the mixer: the research diode ring (four 1N5711 and two BN-43-2402 class cores). The Fair-Rite 2843002402 at Mouser is owner to verify (estimate USD 0.3 to 0.6 each); Kits and Parts lists 25 cores for USD 6.00 plus shipping.
- LO: the JFET mixer is a high-impedance load, which the frequency research asked for; the 18th BFO harmonic lands near 143.96 MHz, 36 kHz below the band.

## 8. Recommendation

- **Recommended alternative:** A4, total 340 of 500 (68 %), the only alternative passing every mandatory criterion, leading the next by 85 points (Robust).
- **Rationale:** it is the only architecture whose planning total fits the firm cap with margin after every common line (tariff, corrections) is added, it has no hand-solder exception, it keeps every SRR hardware safety control, and its RF weaknesses as submitted (wound LPF, SPDT relay, thermal path) are repaired by grafts costing about USD 8.
- **Closely ranked alternatives:** none within 25 points. A3 (B1) is the better-built radio but fails the cap; it is the natural second build if the owner later lifts the cap.
- **Conditions:** the ordering gate of section 8.4 before any purchase; the LTspice runs of the PA match and LPF (WP-PDR-21) and the thermal chain (WP-PDR-28) before the TX F0 freeze.

### 8.1 Recommended architecture (block diagram)

```
                     +------------------ Pico 2 (RP2350, Rust) -------------------+
                     | I2C | PWM gate env | ADC: ALC, pot x2, AGC env, cells, NTC x2 |
                     | PWM audio (sidetone + Morse menu) | key/paddle | 1 button     |
                     | PIO counter <- prescaler | LED (TX, fault blink code)        |
                     +---+----------+-----------------------------------------------+
                         |          |
 Adafruit 2045 Si5351A (stock 25 MHz crystal; TCXO add-back AB2 by module rework)
  CLK1 TX 144-148 --pad--> GVA-84+ --> AFT05MS004NT1 (NXP ref. match) on PA board, slot + vias, on sink
         |                               gate <- MCP6002 <- RC <- PWM (5 ms raised cosine, ALC, steps)
         +--> SN74LVC74ADBR /4 --> PIO   gate clamps (wired-OR, on at reset): LM393 #2 10 s cutoff,
                                         LM393 #1 150-180 s backstop, LM393 #1 95 C sink trip,
                                         LM393 #2 cell 60 C trip, 2N3904 VBUS inhibit
                                                       |
 ANT SMA edge (end face) <-- 7-pole LPF (Coilcraft 1812SMS, 1206 C0G, trap footprint)
                         <-- G5V-2 pole A (TX / RX); pole B grounds the RX input in TX
                             [40 dB tap footprint -> 2nd SMA: add-back AB1]
 RX: 1N5711 clamps -> BPF1 (2) -> J310 GG -> BPF2 (3) -> J310 GG -> J310 mixer (CLK0 136-140 MHz)
     -> diplexer -> 2N3904 -> 6-pole 500 Hz ladder (8.000 MHz, 6 of 10) -> 2N3904 IF x2 (PWM gain)
     -> J310 product det. (CLK2 BFO) -> NE5532 -> sum with PWM tones -> MCP6002 L/R -> 220 uF -> atten -> jack
 Power: 2 x P28A in 1043P holders -> S-8252AAO + 2 x AO3400A (pack negative) -> MF-R300 -> DMP3099L
        reverse/rail switch (EG1218 drives the gate) -> PA drain from the pack; LM2940-5 -> 5 V bus
 Charging: cells out of the radio, XTAR MC1 (1 bay). USB is for firmware only.
```

Boards: two JLCPCB 2-layer 1.6 mm HASL designs, 5 of each, each within 100 x 100 mm. The main board is 64 x 100 mm (cells in holders on the bottom; Pico 2 soldered flat by its castellations beside them). The PA board is about 40 x 35 mm, its via-stitched bottom copper screwed flat to the inside face of the Boyd sink, which forms one end wall with its fins outside. Receiver and synthesizer fences are cut from spare boards. The owner's perfboard is for bench prototypes of the audio chain, the Morse UI and the safety timers.

### 8.2 Differences from A1 as submitted

| Change | Why | Parts cost (pre-contingency) |
|---|---|---|
| G5V-1 SPDT to G5V-2 DPDT | RX-grounding pole; removes about 20 mA peak into the 15 mA 1N5711 clamps (judge 1) | +0.88 |
| Wound LPF coils to Coilcraft 1812SMS 68/82/68 nH | Higher self-resonance for REQ-TX-011 (576 MHz to 1.5 GHz); no winding in the legally critical filter | +5.70 |
| Second LM393P | REQ-SYS-055 10 s cutoff and cell 60 C trip | +0.53 |
| SN74LVC74ADBR prescaler (SSOP-14, 0.65 mm) | REQ-SYS-182 independent frequency check | +0.34 |
| Plated slot and 30 or more vias under the PA tab | REQ-SYS-112 (Tj about 160 C to about 86 to 97 C) | 0 |
| XTAR VC2 (USD 14.99) to XTAR MC1 (USD 4.99, in stock, read today) | Cost; one cell at a time at 0.5 A (about 6 h per cell) | -10.00 |
| AO3400A high-case correction | Aggregator row 0.09 against DigiKey 0.52 | 0 low, +0.86 high |
| Mouser tariff pass-through line | Not counted by any architect (judge 2) | +4 to +12 (E) |
| Ordering gate, guards, add-backs | Firm cap with unread lines | 0 |

### 8.3 Bill of materials

All prices retrieved 2026-09-27. Kind L, A, E as defined under the header. OEMsTrade URLs have the form `https://www.oemstrade.com/search/<PART>`.

**Mouser (one order).**

| # | Qty | Part number | Function | Package | Unit (qty 1) | Line | Stock | Kind | Source URL | Date |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | NXP AFT05MS004NT1 | PA final | SOT-89 | 4.62 | 4.62 | 72 (Newark 4.21, 1,519; DigiKey 4.15, 0) | A (re-read today) | https://www.oemstrade.com/search/AFT05MS004NT1 | 2026-09-27 |
| 2 | 1 | Mini-Circuits GVA-84+ | PA driver MMIC | SOT-89 | 2.99 | 2.99 | 2,754 | A | https://www.oemstrade.com/search/GVA-84+ | 2026-09-27 |
| 3 | 1 | Omron G5V-2-DC5 | T/R relay, DPDT | THT | 3.33 | 3.33 | 2,988 | A | https://www.oemstrade.com/search/G5V-2-DC5 | 2026-09-27 |
| 4 | 1 | Boyd 530002B02500G | Heat sink 2.6 C/W, 63.5 x 41.9 x 25.4 mm, end wall | THT | 3.39 | 3.39 | 3,693 | A | https://www.oemstrade.com/search/530002B02500G | 2026-09-27 |
| 5 | 2 | KEMET C1206C220J1GACTU | LPF 22 pF C0G 100 V | 1206 | 0.29 | 0.58 | 3,978 | A | https://www.oemstrade.com/search/C1206C220J1GACTU | 2026-09-27 |
| 6 | 3 | Coilcraft 1812SMS-68NJLC (2), 1812SMS-82NJLC (1) | LPF inductors | 1812 air core | 1.90 | 5.70 | 784 and 79 (Coilcraft direct 1.01, 2,989) | A | https://www.oemstrade.com/search/1812SMS-68NJLC | 2026-09-27 |
| 7 | 3 | Fair-Rite 2643000101 | Supply chokes | THT bead | 0.10 | 0.30 | 167,261 | A | https://www.oemstrade.com/search/2643000101 | 2026-09-27 |
| 8 | 2 | Microchip MCP6002-I/P | Gate buffer; headphone buffers | DIP-8 | 0.44 | 0.88 | 2,155 | A | https://www.oemstrade.com/search/MCP6002-I%2FP | 2026-09-27 |
| 9 | 1 | Raspberry Pi Pico 2 SC1631 | Controller | Module | 5.00 | 5.00 | 2,078 (PiShop 5.00 in stock, L) | A | https://www.oemstrade.com/search/SC1631 ; https://www.pishop.us/product/raspberry-pi-pico-2/ | 2026-09-27 |
| 10 | 1 | Adafruit 2045 Si5351A breakout | LO, TX carrier, BFO | Module, header | 7.95 | 7.95 | 242 (Adafruit direct 7.95 in stock, L) | A | https://www.oemstrade.com/search/485-2045 ; https://www.adafruit.com/product/2045 | 2026-09-27 |
| 11 | 5 | onsemi MMBFJ310LT1G | 2 LNAs, mixer, product detector, spare | SOT-23 | 0.23 | 1.15 | 184,334 | A | https://www.oemstrade.com/search/MMBFJ310LT1G | 2026-09-27 |
| 12 | 10 | ECS ECS-80-20-4X | 8.000 MHz ladder crystals (match 6) | HC-49/US THT | 0.532 at 10+ (qty-1 price not captured) | 5.32 | 1,990 | A | https://www.oemstrade.com/search/ECS-80-20-4X | 2026-09-27 |
| 13 | 7 | onsemi 2N3904BU | Post-mix amp, IF x2, VBUS inhibit, RX mute, relay driver, rail-off | TO-92 | 0.28 | 1.96 | 200,083 | A | https://www.oemstrade.com/search/2N3904BU | 2026-09-27 |
| 14 | 1 | TI NE5532P | Audio preamp and filter | DIP-8 | 0.81 | 0.81 | 9,869 | A | https://www.oemstrade.com/search/NE5532P | 2026-09-27 |
| 15 | 4 | Diodes 1N5711W-7-F | ALC detector, RX clamps, spare | SOD-123 | 0.24 | 0.96 | 1,839 | A | https://www.oemstrade.com/search/1N5711 | 2026-09-27 |
| 16 | 1 | Omron B3F-1052 | Menu button | THT | 0.39 | 0.39 | 9,504 | A | https://www.oemstrade.com/search/B3F-1052 | 2026-09-27 |
| 17 | 2 | Same Sky SJ1-3535NG | Key jack, phones jack (switched) | THT | 1.62 | 3.24 | 12,431 | A | https://www.oemstrade.com/search/SJ1-3535N | 2026-09-27 |
| 18 | 1 | TE/Linx CONSMA003.062-G | Antenna SMA, edge mount, gold | THT edge | 4.47 | 4.47 | 2,641 | A | https://www.oemstrade.com/search/CONSMA003.062 | 2026-09-27 |
| 19 | 1 | E-Switch EG1218 | Power switch (drives FET gates) | THT | 0.72 | 0.72 | 7,563 | A | https://www.oemstrade.com/search/EG1218 | 2026-09-27 |
| 20 | 2 | Keystone 1043P | 18650 holders | THT | 2.95 | 5.90 | 10,041 | A | https://www.oemstrade.com/search/1043P | 2026-09-27 |
| 21 | 1 | ABLIC S-8252AAO-M6T1U | 2S protector (4.25 V OV, 2.50 V UV, OC) | SOT-23-6 | 1.66 | 1.66 | 3,390 | A | https://www.oemstrade.com/search/S-8252AAO-M6T1U | 2026-09-27 |
| 22 | 2 | AOS AO3400A | Protector FETs | SOT-23 | 0.09 (DigiKey 0.52, 303,947; row looks mis-captured) | 0.18 | 50,678 | A (re-read today) | https://www.oemstrade.com/search/AO3400A | 2026-09-27 |
| 23 | 2 | Diodes DMP3099L-7 | Reverse-polarity FET, rail switch | SOT-23 | 0.40 | 0.80 | 275,851 | A | https://www.oemstrade.com/search/DMP3099L-7 | 2026-09-27 |
| 24 | 1 | Bourns MF-R300 | Pack PTC | THT | 0.50 | 0.50 | 8,019 | A | https://www.oemstrade.com/search/MF-R300 | 2026-09-27 |
| 25 | 1 | TI LM2940CT-5.0/NOPB | 5 V bus LDO | TO-220 laid flat | 2.04 | 2.04 | 141 | A | https://www.oemstrade.com/search/LM2940CT-5.0%2FNOPB | 2026-09-27 |
| 26 | 2 | Semitec 103AT-2 | Cell NTC, sink NTC | THT | 0.58 | 1.16 | 137,636 | A | https://www.oemstrade.com/search/103AT-2 | 2026-09-27 |
| 27 | 2 | TI LM393P | Backstop and 95 C trip; 10 s cutoff and cell 60 C trip | DIP-8 | 0.53 | 1.06 | 6,247 | A | https://www.oemstrade.com/search/LM393P | 2026-09-27 |
| 28 | 1 | TI SN74LVC74ADBR | TX prescaler (divide by 4) | SSOP-14, 0.65 mm | 0.34 | 0.34 | 4,292 (DigiKey 0.44, 1,198; Newark SN74LVC74AD SOIC 1.13, 392) | A (read today) | https://www.oemstrade.com/search/SN74LVC74AD | 2026-09-27 |
| | | | | | **Mouser listed subtotal** | **67.40** | | | | |
| 29 | 2 | KEMET C1206C390J1GACTU | LPF 39 pF C0G | 1206 | est. 0.29 | est. 0.58 | not read | E: same series as row 5 | - | 2026-09-27 |
| 30 | about 175 | Resistors, 0805 and 1206 C0G and X7R (about 14 C0G for the NXP match), 8 electrolytics (2 x 220 uF, 2 x 10 uF 50 V), timer and prescaler passives | Passives | 0805 / 1206 / THT | - | est. 12.50 to 18.50 | - | E: about 55 values in 10-piece lots at USD 0.02 to 0.06, electrolytics about 0.25 (min-cost basis plus about 15 parts for the grafts) | - | 2026-09-27 |
| 31 | - | M3 screws and nuts, counterpoise lug | Hardware | - | - | est. 1.00 to 2.00 | - | E: typical catalog fastener price | - | 2026-09-27 |
| 32 | 1 | SMA-male solder plug for a quarter-wave wire whip | Antenna | - | - | est. 3.00 to 6.00 | - | E: not in the research; 0 if the owner has a 2 m SMA-male whip | - | 2026-09-27 |
| 33 | - | AO3400A price correction | - | - | - | est. 0 to 0.86 | - | E: if Mouser's price is 0.52 | - | 2026-09-27 |

Mouser merchandise: USD 84.48 (low estimates) to 95.34 (high).

**Other sellers.**

| Qty | Item | Seller | Unit (qty 1) | Line | Stock | Kind | URL | Date |
|---|---|---|---|---|---|---|---|---|
| 2 | Molicel P28A 18650, 2.8 Ah (2.6 Ah min), unprotected flat top | 18650BatteryStore | 5.99 (sale; regular 6.99) | 11.98 | In stock | L (read today) | https://www.18650batterystore.com/products/molicel-p28a | 2026-09-27 |
| 1 | XTAR MC1 one-bay USB Li-ion charger, 0.5 A | 18650BatteryStore | 4.99 (sale; regular 9.99) | 4.99 | In stock | L (read today) | https://www.18650batterystore.com/products/xtar-mc1 | 2026-09-27 |
| 1 | Remington Industries 20SNSP.125, 20 AWG magnet wire, 2 oz, 40 ft (BPF and PA-match coils) | Remington Industries | 13.19 (free US shipping) | 13.19 | "Current stock" | L (PA research) | https://www.remingtonindustries.com/magnet-wire/magnet-wire-20-awg-enameled-copper-9-spool-sizes/ | 2026-09-27 |
| 2 designs x 5 | Main board 64 x 100 mm and PA board about 40 x 35 mm, 2-layer, 1.6 mm, HASL | JLCPCB | "From $2.00 / 5 pcs" each | 4.00 | Made to order | L (listed floor; owner to verify in the quote tool) | https://jlcpcb.com/ | 2026-09-27 |
| 2 | Potentiometers (tuning fine window, volume), read by the ADC | Owner's stock | - | 0 | Owned | - | - | 2026-09-27 |

**Shipping, duty and tariff.**

| Line | Low | High | Kind and basis |
|---|---|---|---|
| Mouser standard shipping | 5.00 | 8.00 | E; 0 if the merchandise total reaches the free-shipping threshold (USD 100 per a search summary, Low; owner to verify) |
| 18650BatteryStore, USPS Ground Advantage | 5.00 | 8.00 | E; "from 5.00" (power research) |
| JLCPCB to the US | 12.00 | 25.00 | E; forum report of 2026-03-19 (about USD 12, Global Standard Direct Line); fabrication research USD 15 to 25 for DDP express |
| US duty on the boards, collected by JLCPCB | 1.40 | 2.40 | 35 % (JLCPCB tariff FAQ, listed) to 60 % (Hack Club cost guide) of USD 4.00 |
| Mouser tariff pass-through on China-origin parts | 4.00 | 12.00 | E; USD 20 to 30 China-origin share at 20 to 40 % |

### 8.4 Cost roll-up, ordering gate, guards and add-backs

| Line | Low | Planning (midpoints) | High |
|---|---|---|---|
| Listed parts (Mouser 67.40 + cells 11.98 + charger 4.99 + wire 13.19 + boards 4.00) | 101.56 | 101.56 | 101.56 |
| Estimated parts (rows 29 to 33) | 17.08 | 22.51 | 27.94 |
| Shipping (Mouser, 18650BatteryStore, JLCPCB) | 22.00 | 31.50 | 41.00 |
| Board duty | 1.40 | 1.90 | 2.40 |
| Mouser tariff pass-through | 4.00 | 8.00 | 12.00 |
| **Subtotal** | **146.04** | **165.47** | **184.90** |
| Contingency 15 % | 21.91 | 24.82 | 27.74 |
| **Total, all in, capped** | **167.95** | **190.29** | **212.64** |
| Margin to USD 200 | 32.05 | 9.71 | -12.64 |

**Ordering gate (before anything is ordered).** The owner reads in a browser, without checking out: (1) the Mouser cart with every row of section 8.3: merchandise total, the shipping charge and any tariff line; (2) the JLCPCB quote for the two designs with the cheapest US shipping that prepays duty; (3) the 18650BatteryStore cart (cells and MC1) shipping. Claude then recomputes the total with the verified numbers and 15 % contingency on the remaining estimates.

**Guards, applied in order if the recomputed total is USD 200 or more** (capped values):
- **G1** owner's own copper wire of 18 to 24 AWG (enamelled, bare or stripped solid hookup wire) replaces the magnet wire: -15.17. The high case becomes 197.47.
- **G2** free Mouser shipping: if the verified merchandise is within the shipping charge of the threshold, add the add-backs below until it crosses (they then cost about what the shipping would have): up to -9.20.
- **G3** owner's 2 m SMA-male whip or owner's resistor and capacitor assortment: -3.45 to -6.90 (antenna plug) and -14.38 to -21.28 (passives).
- **G4** owner's Li-ion charger: -5.74.
- **G5** only if the JLCPCB checkout offers LCSC parts in the same parcel: XR XRMW0505-4.5TBRG slug-tuned BPF coils (LCSC C51913014, USD 0.066 each, 1,550 in stock, L via the B1 architect) replace the wound BPF, and the PA match coils are wound from any owned wire, so the magnet wire is not bought.
- **G6 (not recommended)** hand-wind the LPF instead of the Coilcraft parts: -6.55, with the REQ-TX-011 risk back.
- If the total is still over USD 200 after G1 to G5, the owner decides between G6 and a cap exception; nothing is ordered until then.

**Add-backs, in order, if the verified total leaves room** (capped values):
- **AB1** 40 dB monitor port: a second SMA (TE/Linx CONSMA001-C-G, USD 2.80, A) on the tap footprint already on the board: +3.45. Keeps REQ-SYS-141 and removes the need for a 10 W 30 dB pad for tinySA work.
- **AB2** TCXO: Epson TG2520SMN 25.000M-MCGNNM3, USD 3.61 at Mouser (A, 1,810 in stock, +/-0.5 ppm, 3.3 V): +4.15. Needs rework of the Adafruit module (crystal removed, TCXO AC-coupled into XA) and is leadless 2.5 x 2.0 mm (flagged, EX-7). Restores REQ-SYS-010 and the 1.2 kHz guard.
- **AB3** spare AFT05MS004NT1: +5.31.

### 8.5 Envelope and mass (estimates)

- **Plan.** Width: 64 mm board + 2 mm clearance + two 2 mm walls = 70 mm. Length: 25.4 mm sink with fins outside, 13 mm PA-board zone, 100 mm board, 2 mm clearance, 2 mm wall = about 142 mm; the edge SMA adds about 7 mm at the far end face, where the key and phones jacks and the Pico 2 micro-USB also sit.
- **Height.** 2 mm wall, about 21 mm of cells in holders, 1 mm gap, 1.6 mm board, at most 12 mm of parts (G5V-2 about 11.5 mm; Si5351 module on its header about 9 mm; electrolytics 7 mm or less), 1 mm gap, 2 mm wall: about 40.6 mm. The sink end wall is 41.9 mm tall (Farnell and Newark listings), so the case is **about 42 mm**; filing the sink to 40 mm removes the height delta.
- **Envelope: about 142 x 70 x 42 mm (149 mm long with the SMA)** against REQ-SYS-103 (140 x 70 x 40 mm, TBR): +2 mm length, +2 mm height, +6.5 % volume (+11.7 % with the SMA protrusion).
- **Board area.** About 58 cm2 of the 64 cm2 top side used in A1, plus about 3 cm2 for the grafts (G5V-2 larger than G5V-1, a DIP-8, an SSOP-14): about 61 cm2 of 64 cm2, tight. Fallback: a 70 x 100 mm board (still within the JLCPCB 100 x 100 mm price), case 76 mm wide.
- **Mass: about 277 to 347 g** against REQ-SYS-102 (350 g, TBR): cells 92 to 96 g; holders 12 to 16 g; boards 23 g; components and wiring 62 to 77 g; Boyd sink 30 to 60 g (not read; owner to verify on the drawing); PETG shell with 2 mm walls 55 to 70 g; screws 3 to 5 g. Inside the limit, with 3 g of margin at the high end.

### 8.6 Surface-mount parts used (no BGA, no leadless part, no pitch under 0.65 mm, no hidden thermal pad)

| Part | Package | Why SMD | Flag |
|---|---|---|---|
| AFT05MS004NT1 | SOT-89 | Only in-stock listed-price VHF 4 to 6 W device with a vendor 136 to 174 MHz reference circuit | Source tab visible; owner confirms on the drawing |
| GVA-84+ | SOT-89 | 50 ohm MMIC driver; no through-hole equivalent in stock | none |
| MMBFJ310LT1G x4 used | SOT-23 | TO-92 J310 out of stock | none |
| 1N5711W-7-F x3 used | SOD-123 | Mouser stocks the 1N5711 only in SMD in the rows read | none |
| S-8252AAO-M6T1U | SOT-23-6 | No through-hole 2S protector exists | none |
| AO3400A x2, DMP3099L-7 x2 | SOT-23 | Through-hole protector FETs out of stock | none |
| SN74LVC74ADBR | SSOP-14, 0.65 mm | Needs to toggle at 148 MHz | At the 0.65 mm limit of the owner's list; drag-solder with flux |
| Coilcraft 1812SMS x3 | 1812 air-core with solder ends | Catalog LPF coil, high self-resonance | none |
| C0G and resistors in the RF sections, decoupling | 1206 / 0805 | Lead inductance at VHF; the NXP match uses 0603 ATC, substituted by 0805 | none |
| Pico 2 (castellated, soldered flat), Adafruit 2045 (header) | Modules | Read as through-hole compatible (owner to confirm) | none |

Through-hole: relay, jacks, switch, button, holders, crystals, TO-92 transistors, DIP op-amps and comparators, LDO, PTC, NTCs, beads, electrolytics, heat sink.

### 8.7 Morse-code audio user interface (owner direction 8)

**Controls.** One push button (B3F-1052), two owner potentiometers on ADC inputs (pot 1: fine tuning window of +/-5 kHz around the entered centre, about 10 to 20 Hz resolution with hysteresis; pot 2: volume), the key or paddle on the key jack, and the power switch. The Pico 2 on-board LED, behind a light pipe, shows transmit and blinks fault codes.

**Sequence (the owner's words, implemented).**
1. A short press of the button enters the menu. Transmit is disarmed: the key line goes to the decoder, and only the sidetone path sounds.
2. The radio sends the menu letters in Morse through the sidetone path, at the keyer speed, with the tone level held under the headphone ceiling (REQ-SYS-071).
3. The operator sends one letter on the key or paddle to pick an item, for example: F frequency, P power step, S keyer speed, K key mode (straight, iambic A, iambic B), T tone pitch, C call sign, B battery and status read-out, X exit.
4. For a number, the operator sends digits (for F: kHz within the band, for example 144050); the paddle can also step a value (dit down, dah up) with a step size set in the menu.
5. The radio reads the value back in Morse.
6. The operator sends R to confirm or N to reject (the value is not applied on N). No entry for 20 s (TBR) exits without change.

**Rules.**
- Two menu levels at most from menu entry (REQ-SYS-062).
- The 5 W step needs the read-back and an R (REQ-SYS-063); a first entry after power-on starts at a lower step.
- A long press outside the menu sends the status in Morse (frequency, power step, key mode, speed, battery), replacing the status display (REQ-SYS-060).
- The call sign is sent at power-on and when the headphones are plugged in (REQ-SYS-006).
- Faults are announced in Morse within 1 s through the headphones and shown by an LED blink code without them (REQ-SYS-067, 077).
- Low battery, the identification reminder and the separation reminder are announced (REQ-SYS-068, 069, 096).
- The menu override command path stays safety-critical (SRR decision 9); the menu never clears a hardware clamp.
- Straight-key decoding is adaptive (the highest firmware risk); paddle decoding is exact; if the straight-key decoder proves unreliable, menu entry is paddle-only.

**Firmware scope added (WP-PDR-35, 41):** Morse sender on the PWM tone path, adaptive decoder, menu state machine with R/N confirmation and time-out, number entry and read-back, pot reading with hysteresis, status and fault announcements, LED codes, PIO frequency counter, gate envelope and ALC loop, AGC control voltage, Si5351 I2C driver. Removed: display driver and encoder drivers. The audio stays analog, so no ADC audio path or DSP is added.

**Hazard notes.** HZ-004 (stuck transmission): transmit is disarmed in the menu and the hardware cutoffs stay independent. HZ-005 (hearing): every menu tone passes through the same capped path as the sidetone.

### 8.8 Descopes

| # | Descope | What it costs |
|---|---|---|
| D1 | No display; Morse-only audio UI | No UI without headphones except the LED; straight-key menu entry needs the adaptive decoder |
| D2 | No in-radio charging; cells charged one at a time in an XTAR MC1 | Loses SI-022 and CON-010 USB charging; about 6 h per cell at 0.5 A; cells handled at each charge; HZ-002 re-scoped to the COTS charger |
| D3 | No TCXO in the first build (add-back AB2) | 30 ppm after calibration (TBR); carrier guard widened to 5.3 kHz |
| D4 | No conductive coating or case lining | REQ-SYS-177 (Goal) deferred; board fences and ground pour only |
| D5 | No tuning encoder | Tuning by Morse direct entry, pot fine window and paddle steps |
| D6 | No volume encoder | Owner pot, quantized by firmware; pot rated -10 C, zero margin to REQ-SYS-114 |
| D7 | One button | Status by long press, escape by time-out or X |
| D8 | Gold-plated brass-class SMA instead of stainless | About 100 mating cycles against 500 |
| D9 | Non-RF-rated relay (G5V-2) | Isolation verified on the NanoVNA; semi break-in only |
| D10 | JFET mixer instead of a diode ring | Lower IIP3 (Low); diode ring is the fallback |
| D11 | Monitor port not populated (add-back AB1) | tinySA work needs an external 10 W 30 dB pad until AB1 |
| D12 | No spare PA device (add-back AB3) | A blown AFT05 costs about USD 12.60 to reorder |
| D13 | No 3.3 V analog LDO; op-amps on the 5 V bus | Headphone ceiling set by a 2.5 V peak rail; attenuator k about 0.06 (TBR) |
| D14 | In-radio charge protection layers removed (TLV431, LM393 window, MCP3202, HY2213 balancers) | Their requirements move to the COTS charger and the handbook; the S-8252 keeps 4.25 V OV and 2.50 V UV in the pack |
| D15 | 70 cm | Si5351A limit 200 MHz; the AFT05 covers 136 to 941 MHz |
| D16 | Pocket envelope traded slightly | +2 mm length (+9 mm with the SMA), +2 mm height |
| D17 | No metal case, heat-set inserts or PCBWay CNC fallback within the cap | Printed bosses with captive M3 nuts; a CNC case would need its own cap decision |

### 8.9 Exceptions the owner must approve

| Id | Exception | Why | Cheapest way through |
|---|---|---|---|
| EX-1 | Surface-mount parts: SOT-89 (AFT05MS004NT1, GVA-84+), SOT-23 (MMBFJ310 x4, AO3400A x2, DMP3099L x2), SOT-23-6 (S-8252AAO), SOD-123 (1N5711W), SSOP-14 0.65 mm (SN74LVC74ADBR), 1812 (Coilcraft), 0805 and 1206 passives | No through-hole equivalent in stock at 144 MHz (section 7.3) | All on the section 8 hand-solder list; none has a hidden pad (owner confirms the SOT-89 tab) |
| EX-2 | Modules counted as through-hole compatible: Pico 2 soldered flat by its castellations; Adafruit 2045 on its header | Status note section 6 reading (to confirm) | Confirm |
| EX-3 | PA device is the NXP AFT05MS004NT1 run at 5 W against its nominal 4 W rating, on the vendor 6 W reference circuit, with 0805 parts and wound coils | Removes the RF Parts order (about USD 45 capped for the RA07M1317M with shipping) | LTspice, NanoVNA and tinySA work before first on-air use; fallback RA07M1317M (about +USD 45) |
| EX-4 | Charging outside the radio in an XTAR MC1 (USD 4.99), inside the cap; SI-022 and CON-010 charging given up | Removes the LCSC-only CN3302 and HY2213 and the Catastrophic charger chain | USD 0 if the owner has any Li-ion charger |
| EX-5 | TCXO not fitted (REQ-SYS-010 relaxed to 30 ppm, TBR) | Cost | Add-back AB2 |
| EX-6 | JFET mixers instead of the researched diode ring (not research-validated) | Cost and LO loading | LTspice before the RX freeze; diode ring fallback |
| EX-7 | Add-back AB2 only: Epson TG2520SMN is leadless 2.5 x 2.0 mm, 4 pads under the body (no thermal pad), heat-gun soldered, plus module rework | No through-hole TCXO at +/-1 ppm with a catalog listing | Decide only if AB2 is funded |
| EX-8 | Owner-supplied items: two potentiometers; a USB power adapter for the MC1; headphones; key or paddle; optionally wire, whip and passives (guards G1, G3) | Owner stock | Confirm values (5 k to 100 k, any taper) and shafts |
| EX-9 | Antenna: a DIY quarter-wave wire whip on an SMA-male plug (estimate USD 3 to 6), not the REQ-SYS-172 reference antennas | Cost | USD 0 with an owned 2 m SMA-male whip |
| EX-10 | Cap margin: USD 9.71 at planning; the high case needs guard G1 or verified shipping | Unread lines | Ordering gate, section 8.4 |
| EX-11 | Envelope about 142 x 70 x 42 mm (149 with the SMA) | Sink end wall 41.9 x 25.4 mm | Size is negotiable (status note section 8 item 2) |
| EX-12 | Price evidence: every Mouser price via the aggregator; AO3400A row suspect | Mouser blocks automated reads | Owner price-check list, section 8.11 |
| EX-13 | Instruments outside the cap (to confirm): tinySA Ultra (committed), NanoVNA, dummy load (SI-013), a 10 W 30 dB pad (est. USD 15 to 25) unless AB1, a thermocouple (USD 9.95) | Status note section 6 reading | Confirm |
| EX-14 | Non-RF-rated T/R relay (G5V-2) | RF-rated relays are out of stock or about USD 39 | NanoVNA isolation and loss measurement before first transmission |

### 8.10 Requirement deltas (for the re-baseline CR)

Current values from `docs/requirements/sys/requirements.json` at HEAD. "Keep" means the value is unchanged; "at risk" names what the PDR analysis must show.

**User interface (display to Morse, owner direction 8).**

| REQ | Current | Proposed |
|---|---|---|
| REQ-SYS-006 | Display the call sign after every power-on | Announce the call sign in Morse at power-on and at headphone insertion |
| REQ-SYS-044 | Hang time in dits at the displayed speed | At the set speed |
| REQ-SYS-057 | Exactly two rotary knobs with push and two push buttons | One push button, two potentiometer controls (tuning fine window, volume) and the key or paddle for menu entry, besides the power switch |
| REQ-SYS-058 | One step per tuning-knob detent, 10 Hz to 10 kHz with rotation rate | Morse direct frequency entry, a pot fine window of +/-5 kHz at 20 Hz resolution or better, and a paddle step mode of 10 Hz to 10 kHz |
| REQ-SYS-059 | Volume knob, at least 32 steps | Potentiometer read by the ADC, quantized to at least 32 steps from mute to the cap |
| REQ-SYS-060 | Show frequency, power step, key mode, speed, battery and transmit state outside menus | Announce the same items in Morse on demand (long press or menu command); transmit state on the LED |
| REQ-SYS-061 | Frequency characters at least 4.0 mm high | Retired |
| REQ-SYS-062 | Every setting within two menu levels from the status screen | Within two Morse-menu levels from menu entry, with R/N confirmation and a 20 s (TBR) time-out |
| REQ-SYS-063 | 5 W only after a step selection and a separate confirmation press | 5 W only after the Morse read-back and an R |
| REQ-SYS-067 | Display a distinct cause message within 1 s | Announce a distinct cause in Morse within 1 s (headphones) and an LED blink code (no headphones) |
| REQ-SYS-068, 069, 096, 171 | Show or display the ID reminder, separation reminder, low-battery warning, key-down time | Announce in Morse (and LED for low battery); timing values unchanged |
| REQ-SYS-070 | Indicate charge state whenever USB power is present | Retired (no in-radio charging; the MC1 indicates) |
| REQ-SYS-146 | Reserved enclosure position, controller input and display field for band control | Reserved enclosure position, controller input and Morse-menu entry |
| REQ-SYS-164 | Band crossing within 30 s at 2 rev/s of the knob | Any in-band frequency reached by Morse direct entry within 30 s (TBR) |
| REQ-SYS-165 | Displayed frequency legible at 0.5 m under 300 lux | Retired |

**Frequency and receiver.**

| REQ | Current | Proposed |
|---|---|---|
| REQ-SYS-008, 009, REQ-TX-002 | Carrier 144.0012 to 147.9988 MHz (TBR); inhibit outside | 144.0053 to 147.9947 MHz (TBR): 4.44 kHz for 30 ppm at 148 MHz plus the 0.83 kHz sideband allowance already inside the 1.2 kHz guard (derived); back to 1.2 kHz with AB2 |
| REQ-SYS-010 | +/-2.5 ppm (TBR) of the displayed frequency, -10 to +45 C, one year after calibration | +/-30 ppm (TBR) of the set frequency after a room-temperature calibration against the tinySA or a beacon; +/-2.5 ppm when AB2 is fitted |
| REQ-SYS-182 | Withhold or end RF within 100 ms unless an independent measurement agrees within 10 kHz | Keep. At risk: 30 ppm synthesizer error plus the counter timebase error (Pico 2 crystal, about 30 ppm recalled, Low) is up to about 8.9 kHz at 148 MHz, inside 10 kHz with about 1.1 kHz margin; prescaler toggle rate at 148 MHz |
| REQ-SYS-022 | MDS at most -140 dBm (TBR) | Keep; at risk (estimate about -140 dBm, Low); fallback diode ring |
| REQ-SYS-023 (Goal) | MDS -142 dBm | Record as not met (about -140 dBm) |
| REQ-SYS-029 | 3 dB loss with a -60 dBm signal 2 kHz away | -65 dBm (TBR) or an accepted limitation (Si5351 close-in phase noise) |
| REQ-SYS-031 | RMDR at least 85 dB at 10 kHz | 80 dB (TBR); estimate about 83 dB |
| REQ-SYS-032, 033 | Level range -120 to -20 dBm; 70 dB image and IF rejection | Keep; at risk (AGC range; image estimate Low) |

**Transmitter and safety.**

| REQ | Current | Proposed |
|---|---|---|
| REQ-SYS-012 | 5 W +/-1 dB (TBR) at 6.4 to 8.4 V | Keep; at risk (estimate 4.4 W at 6.4 V against the 3.97 W floor) |
| REQ-SYS-013, 017, 018, REQ-TX-009 to 011 | Survival; 25 uW; 60 dBc; harmonic filter values | Keep; 017, 018 and REQ-TX-011 at risk until the LTspice run and the tinySA measurement (no AFT05 harmonic data) |
| REQ-SYS-055, 120, 180, 181, 092 | Hardware cutoff 7.5 to 13 s; two conditions; backstop 150 to 180 s; 95 C trip; USB inhibit | Keep, all implemented on the gate node. REQ-SYS-180 at risk from RC timer tolerance; if +/-9 % cannot hold, widen to 130 to 200 s (TBR) by CR |
| REQ-SYS-112, 113 | Tj at most 110 C at 45 C; hand surfaces at most 48 C | Keep; Tj estimate 86 to 97 C with the plated slot (Low) |
| REQ-SYS-141 | Transmit monitor port, 40 dB +/-1 dB | Deferred to add-back AB1 (tap on the board, SMA bought when funded); retired for the first build if AB1 is not funded |
| REQ-SYS-183 | RF-off at most -57 dBm | Keep; verify relay isolation and CLK1-off leakage |

**Power and charging (charging outside the radio).**

| REQ | Current | Proposed |
|---|---|---|
| REQ-SYS-081 | Charge termination 4.20 V +/-0.5 % | Reallocated to the external charger (XTAR MC1; its termination tolerance owner to verify, recalled 4.2 V +/-1 %, TBR) and the handbook |
| REQ-SYS-082 | Charge temperature window 0 to 45 C | Reallocated to the handbook ("charge at room temperature") and the charger's protection |
| REQ-SYS-083 | Independent cell over-voltage protection 4.25 to 4.30 V | Keep, as the S-8252AAO 4.25 V detection in the pack path; reworded for the absent charger |
| REQ-SYS-087 | Refuse charging on a failed cell insertion check | Refuse to arm transmit |
| REQ-SYS-088, 089, 091, 093, 167, 185 | Dual-path check, 15 h timer, 12 h charge time, charge pause in receive, current-fall supervision, further OV layer | Retired from the radio (no in-radio charging) |
| REQ-SYS-186 | Separate cell-sense paths per protection layer | Reworded for the one remaining in-pack layer plus the firmware monitor |
| REQ-SYS-090, 100 | 500 mA from USB; 50 uA off current | Keep (Pico only on USB; off current about 10 to 20 uA) |
| REQ-SYS-094 | 8 h at 1:9 on fresh 3000 mAh cells | Test with the fitted 2.8 Ah P28A cells, or keep 3.0 Ah as the test cell; estimate 8.4 to 14.7 h |
| REQ-SYS-101 | A mechanical switch removes power from every load | The mechanical switch (EG1218, 0.2 A) drives the rail P-FET gates that remove power (owner interpretation) |
| REQ-SYS-071 to 073, ICD-CTL-PHONES | Headphone ceiling from a 3.3 V ground-referenced amplifier | Capacitor-coupled MCP6002 buffer on the 5 V bus, rail-bounded attenuator k about 0.06 (TBR), confirmed in LTspice |

**Mechanical, enclosure and antenna.**

| REQ | Current | Proposed |
|---|---|---|
| REQ-SYS-102 | 350 g (TBR) | Keep; estimate 277 to 347 g |
| REQ-SYS-103 | 140 x 70 x 40 mm (TBR) | 142 x 70 x 42 mm (TBR), plus about 7 mm of SMA at the end face |
| REQ-SYS-104 | SMA female, stainless steel | SMA female, gold-plated brass class (TE/Linx CONSMA003.062-G) |
| REQ-SYS-106 | 500 mating cycles | 100 cycles (TBR) |
| REQ-SYS-109 | CNC-machined anodized aluminum enclosure | Owner-printed PETG case with one aluminum heat-sink end wall; no conductive coating in the first build (CR-003 carries the solution-neutral wording) |
| REQ-SYS-124 | Legend marked into enclosure metal | Legend in relief in the PETG surface (OD-38 route (a)) |
| REQ-SYS-172 | Reference antennas of 0 dBd or less shipped | A DIY quarter-wave whip with the 48 cm counterpoise tail, or the owner's antenna |
| REQ-SYS-175 | Antenna port on one end face | Keep (edge-mount SMA on the far end face) |
| REQ-SYS-177 (Goal) | Enclosure shielding at least 20 dB | Deferred (board fences and ground pour only) |

**Build, sourcing and cost.**

| REQ | Current | Proposed |
|---|---|---|
| REQ-SYS-137 (KDR) | Every SMT part placed by PCBWay turnkey | Retired (owner hand-assembles everything) |
| REQ-SYS-138 | Owner hand-solders only through-hole parts and listed exposed-pad modules | Owner solders all parts; SMT limited to the section 8 hand-solder list, no BGA, no leadless or reflow-only parts, exceptions named in the hand-assembly file |
| REQ-SYS-139 | 4-layer, 1.0 mm (TBR), PCBWay DRC | 2-layer, 1.6 mm, JLCPCB standard DRC, two designs each within 100 x 100 mm |
| REQ-SYS-140 (KDR) | Turnkey parts and the PA only from DigiKey, Mouser or PCBWay distributors | Every part from a catalog distributor or maker shop with a published price and stock (Mouser primary) |
| REQ-SYS-144 | No adjustment except stored firmware calibration | Admit a one-time build alignment on the NanoVNA and tinySA (BPF coil squeeze, crystal matching, PA match trim, LPF check), then stored calibration only |
| REQ-SYS-145 | Band-dependent functions partitioned | Keep; the synthesizer becomes band-dependent (Si5351A limit 200 MHz) |
| REQ-SYS-147 | USD 610 (TBR) per unit amortized over three units | The first complete unit costs under USD 200 all in (boards, parts, shipping, duty, tariff; filament and instruments excluded), including 15 % contingency |
| REQ-SYS-178 | Owner-procured part with a named source and a dated quote | Named source and dated listed price |

**L0, interfaces and hazards (same CR).** CON-010 (USB for firmware and charging, to firmware only), CON-015 (PCBWay CNC aluminum, to the printed PETG case with a sink end wall; CR-003 carries the enclosure wording), NGO-027 (PCBWay turnkey, to JLCPCB bare boards hand-assembled), NGO-028 and MOE-007 (USD 610 over three units, to under USD 200 for the first unit), SI-022, SI-028 and SI-031 superseded by the new owner inputs (next free SI id), ICD-CTL-USB (charging removed), ICD-PWR-CELL (1043P holders, external charger), ICD-TX-ANT (SMA material), HZ-002 (re-scoped to the COTS charger and the handbook), HZ-015 (heat-gun use added), HSI and ConOps display content replaced by the Morse menu.

### 8.11 Owner price-check list (browser, no checkout)

1. Every Mouser row of section 8.3 (all aggregator reads), especially: AO3400A (0.09 or 0.52), Coilcraft 1812SMS-82NJLC stock (79), AFT05MS004NT1 stock (72; Newark 4.21 as the alternate), LM2940CT-5.0 stock (141), Adafruit 2045 (Mouser part 485-2045).
2. The estimated Mouser rows: KEMET C1206C390J1GACTU; the passives lot; M3 hardware; an SMA-male solder plug; and, for AB1 and AB2, CONSMA001-C-G and TG2520SMN.
3. The Mouser cart: merchandise total, shipping charge, the free-shipping threshold, and the tariff line.
4. JLCPCB: the instant quote for the two designs (2-layer, 1.6 mm, HASL, 5 pcs each), the cheapest US shipping that prepays duty, the duty shown, and whether LCSC parts can ship in the same parcel (guard G5).
5. 18650BatteryStore: cart shipping for 2 P28A and 1 XTAR MC1; the MC1 termination voltage and tolerance on its product sheet.
6. Boyd 530002B02500G drawing: mass and the flat base face dimensions for the PA board (judge 1 asks that the radial-fin sink has a flat face large enough).
7. Owner stock: copper wire of 18 to 24 AWG (G1), a 2 m SMA-male whip, a resistor and capacitor assortment, a Li-ion charger, a USB power adapter, the two potentiometers (values and shafts).

### 8.12 What changes in the PDR work plan, CR-003 and CR-006

**PDR work plan (`docs/plan/pdr-work-plan.md`).**

| WP or item | Change |
|---|---|
| WP-PDR-04, OD-04, OD-34 | The PCBWay email, the PCBWay instant quotes and the Inrad, KVG and Guerrilla RF requests are cancelled. They are replaced by the owner price-check list of section 8.11 and the ordering gate. No quote is requested from anyone |
| WP-PDR-19 (TS-001) | The hand-matched 6-pole 500 Hz ladder is re-admitted (TS-001 pruned it only because turnkey assembly could not match crystals); the Inrad and 24-bit ADC candidates are dropped; analog audio is kept; JFET mixer and diode-ring fallback simulated in LTspice |
| WP-PDR-20 (TS-007, clock plan) | Si5351A module with its stock crystal, TCXO as add-back; REQ-SYS-010 and the guard relaxed (TBR); clock plan re-run for the 8 MHz IF and the display removal |
| WP-PDR-21 (TS-003, LPF) | PA device becomes the AFT05MS004NT1 with a GVA-84+; LTspice of the NXP reference match with 0805 parts and of the Coilcraft LPF with a trap; the harmonic budget closes REQ-SYS-017, 018 and REQ-TX-011 |
| WP-PDR-22 (TS-006) | ALC and envelope on the AFT05 gate; power steps from gate bias |
| WP-PDR-23 | T/R element is the G5V-2 with an RX-grounding pole; NanoVNA isolation plan |
| WP-PDR-24 (power, TS-005) | Charging out of the radio; TS-005 (USB input) narrows to firmware loading and the VBUS inhibit; the in-radio charger analyses are dropped |
| WP-PDR-25 (audio and display) | Display trade removed; audio on the 5 V MCP6002 buffer; the Morse menu tone path shares the ceiling analysis |
| WP-PDR-26 | Two LM393 monostables and trips; the RC timing analysis over tolerance and temperature for REQ-SYS-055 and 180 |
| WP-PDR-27 (TS-011, TS-004) | TS-011 is re-scored: a sink end wall with fins outside, no coating in build 1, the PCBWay CNC fallback and port block outside the cap; the PETG M8 finding is re-run for the A4 heat layout. TS-004 becomes 2-layer 1.6 mm JLCPCB against 4-layer, with the two-design split |
| WP-PDR-28 | Thermal chain of the SOT-89 PA with the plated slot and via field; PETG boss temperatures |
| WP-PDR-16, 17 | HZ-002 re-scoped; HZ-015 adds the heat gun; the Morse menu command path in the safety-critical determination |
| WP-PDR-33, 40 | UI analyses and the HSI evaluation move from a display mockup to a Morse-menu demonstration on the Pico 2 dev board (paddle and straight key) |
| WP-PDR-35, 41 | SW L2 and the driver set follow section 8.7 (display and encoder drivers removed; decoder, menu, PIO counter added) |
| WP-PDR-37, 38, 39 | Schematic and floorplan on two JLCPCB 2-layer boards; this BOM is the preliminary BOM; the enclosure model takes the sink end wall |
| WP-PDR-46 | `docs/plan/cost-estimate.md` rewritten on section 8.4; TPM-014 re-based on USD 200 |
| New owner decision | OD for TS-012 at B1a (proposed), before the trades above are scored; the re-baseline CR at B2 |

**CR-003 (enclosure, Submitted, held).** Needs a revision 4 before disposition: the printed PETG case stays the first and delivered enclosure, but (a) the heat sink forms an end wall with its fins outside, (b) no conductive coating is bought for build 1 and REQ-SYS-177 is deferred, (c) the PCBWay CNC fallback and the 6061 port block are outside the USD 200 cap, so the fallback becomes a second printed iteration (free filament) or an owner cap decision, (d) the legend and jack markings stay in relief (OD-38 route (a)), (e) the TS-011 PC-class filament condition is re-run for the A4 heat layout before it is asked of the owner, and (f) REQ-SYS-104 and 106 follow section 8.10.

**CR-006 (build sequence, Submitted, held).** Its reading (one assembled unit first) stands, but its PCBWay content does not: (a) five bare boards of each of two designs come from JLCPCB and the owner assembles one unit; (b) REQ-SYS-147, NGO-028 and MOE-007 take the under-USD-200 first-unit cap instead of USD 610 amortized over the first build; (c) NGO-027 changes from PCBWay turnkey to JLCPCB bare boards with owner hand assembly; (d) questions Q2 (PCBWay assembled count), Q3 (unit-cost options) and Q8 (unused turnkey parts) become moot; (e) the TC-SYS-025 and MOE-001 and 002 content (the Baofeng source and the matched second station, status note section 5) is unaffected. Recommendation: fold both CR revisions and the section 8.10 deltas into one re-baseline CR (the next free CR number when its file is created), with its section 6 impact review before the owner's disposition.

## 9. Dissent

| Who | Date | Dissent | How it was addressed |
|---|---|---|---|
| Independent reviewer (INSP-NNN) | - | None recorded yet; the review has not run | - |
| Judge 0 (panel input) | 2026-09-27 | Its own weighted total ranked B1 first (82 against 79) while its ranking put min-cost first | Cost cap made mandatory (M1) and cost robustness scored (C2) |
| Judge 1 (panel input) | 2026-09-27 | min-cost's thermal path and cost arithmetic are fatal as submitted | Plated slot and via field; AO3400A correction carried; ordering gate |
| Judge 2 (panel input) | 2026-09-27 | No budget counts Mouser's tariff pass-through; REQ-SYS-182 missing | Tariff line added to every alternative; prescaler added |

## 10. Decision

Left empty until the owner decides.

- **Decision:**
- **Decided by:**
- **Rationale as stated by the owner:**
- **Records produced:**
- **Revisit conditions:** the verified ordering-gate total exceeds USD 200 after guards G1 to G5; the LTspice harmonic run shows less than 53 dBc at any harmonic with the trap fitted; the Tj analysis exceeds 110 C; the AFT05MS004NT1 stock at Mouser and Newark reaches zero before the order.
- **Lessons learned:**

## 11. References

- `docs/plan/status/status-2026-09-27.md` sections 6, 8 and 9 (owner direction, verbatim).
- `docs/process/06-risk-and-decision-analysis.md` sections 6, 7, 8, 13, 14; `docs/templates/trade-study.md`.
- `docs/requirements/sys/requirements.json`, `docs/requirements/tx/requirements.json`; `docs/safety/hazards.json`; `docs/risk/register.json`; `docs/plan/cost-estimate.md`; `docs/plan/pdr-work-plan.md`; `docs/cm/cr/CR-003-solution-neutral-enclosure.md`; `docs/cm/cr/CR-006-build-sequence-one-unit-first.md`; TS-001, TS-004, TS-007, TS-011.
- Block research reports of this study, 2026-09-27: transmitter chain and PA; receiver and CW selectivity; frequency generation; power and charging; UI and audio; fabrication and shipping; enclosure (not committed as files; their findings are quoted here with their sources).
- Architecture reports: min-cost, performance-in-cap (PIC-5), buildability (B1); judge reports 0 (cost and sourcing), 1 (RF and regulatory), 2 (buildability, size, safety); all 2026-09-27.
- NXP AFT05MS004N datasheet Rev. 0, 7/2014 (Tables 8 to 10, Figs. 12, 13), read by the min-cost architect. Mitsubishi RA07M1317M datasheet (June 2019); RD06HVF1 datasheet (July 2017); Mitsubishi AN-VHF-053-A.
- Seller and aggregator pages as listed in section 8.3, read 2026-09-27, including the author's reads: https://www.oemstrade.com/search/AFT05MS004NT1 , https://www.oemstrade.com/search/AO3400A , https://www.oemstrade.com/search/SN74LVC74AD , https://www.18650batterystore.com/products/molicel-p28a , https://www.18650batterystore.com/products/xtar-mc1 .
- Shipping and tariff evidence (author's reads, 2026-09-27): https://forum.allaboutcircuits.com/threads/jlcpcb-global-standard-direct-line-shipping.209788/ (post of 2026-03-19); https://highway.hackclub.com/guides/JLC-cost-optimizing ; https://ampgarage.com/forum/viewtopic.php?t=37728 (posts of 2025-01-17 and 2025-02-03); https://www.mouser.com/en/section-301-tariff-updates/ (timed out; content from a search summary); https://www.eevblog.com/forum/chat/mouser-free-shipping-threshold-increase!/ (HTTP 403; threshold from a search summary); https://jlcpcb.com/help/article/us-tariff-policy-faq ; Boyd sink dimensions https://uk.farnell.com/aavid-thermalloy/530002b02500g/heat-sink-2-6k-w-to-220/dp/2295719 and https://www.newark.com/aavid-thermalloy/530002b02500g/extruded-heat-sink/dp/99K1617 (read by judges 1 and 2).

## Appendix A. Supporting analysis

- **Literature and research search:** claude-context `search_code` on `/Users/robinonsay/rust/cwht` first (charter section 11 rule 1), queries on trade-study format and decision analysis; then reads of known paths. Web: WebSearch and WebFetch of public product, aggregator and forum pages listed in section 11; Mouser, DigiKey and EEVblog pages blocked or timed out.
- **Previous related decisions and dissent:** TS-001 (SRR decision 54 and the ladder pruning), TS-007, TS-011 (M8 PETG finding), ADR-007, SI-028, SI-031.
- **Detailed analysis:** the roll-up and the sensitivity run were computed with short Python scripts in the author's scratchpad (not committed): 16 weight perturbations and every Low-cell perturbation, reproduced in section 6. No LTspice deck exists yet for A4; the PA match, LPF, headphone ceiling and JFET mixer decks are WP-PDR-21, 25 and 19 products.
- **Decision metrics:** opened and recommended the same day; five alternatives (one pruned tree of five more); eight enhancing and five mandatory criteria; no criteria revision yet.

## Change log

| Revision | Date | Change | Reason |
|---|---|---|---|
| 0 | 2026-09-27 | Initial, Proposed | Owner direction of status note sections 6 and 8 |
