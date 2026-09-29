# PDR owner action pack

**Work package:** WP-PDR-04 of `docs/plan/pdr-work-plan.md` (revision 6, `a02d84b`), section 3.0 row 04 (governs) and section 3.2. **Author:** Claude (lead SE). **Revision:** 2, 2026-09-29 (revision 1: 2026-09-27, `1fe9c1a`). **Configuration read:** `main` at `908d21a`.
**Status:** Informational working product of the PDR phase (a request list, not a baselined item). No review record is required (plan WP-PDR-04 "Reviewer"); the equipment list of section 6 is reviewed inside WP-PDR-43. It is an input to `docs/reviews/PDR/package.md` §2 (owner actions) and to the open-decisions slide.
**Nothing is bought or sent by Claude.** Claude never places an order, checks out, creates an account, sends a message or downloads a file for you. Everything below is a list of things to look at in your own browser and write down, or facts only you have. Your replies are transcribed verbatim into the dated status note (SEMP §7.4; charter §4 item 4), never into this file.

**Revision 2 in one paragraph.** On 2026-09-29 you chose design A5 (TS-012 revision 7 section 10: the Mitsubishi RA07M1317M-501 module, the Epson TCXO, the diode-ring mixer, two JLCPCB bare boards that you solder, the printed case, cells charged outside the radio). That removed most of revision 1: no quote is requested from anyone (TS-012 §8.12), so the PCBWay email and instant quotes (OD-04), the Inrad, KVG and Guerrilla RF requests (OD-34), the st.com downloads (OD-18) and the stock checks of the PD54008L-E design (OD-39 part) are withdrawn (sections 2 to 4). In their place: the **price-check list** (section 5, OD-42), which is the TS-012 §8.11 list and the ordering-gate reads of §8.4, and the **equipment list for A5** (section 6), rebuilt from what you told us you own (status notes 2026-09-27 §5, §11; 2026-09-28 §1, §2) and kept inside your USD 300 cap on new equipment. Also on 2026-09-29 you directed that work start as soon as it can (status note 2026-09-29 §8). Nothing in sections 5 and 6 waits for a session: you can do them today.

## 0. What to do, in order

| Step | When | Action | Section | Your time |
|---|---|---|---|---|
| 1 | **Any time now** | The browser price check: Mouser cart, RF Parts cart, JLCPCB quote, 18650BatteryStore cart. Look and write down; no checkout (OD-42) | 5 | About 45 min |
| 2 | **Any time now** | Five equipment facts (dummy load rating, calipers, scale, Pico 2 board, key and paddle names) | 6.2 | 5 min |
| 3 | When you like | Buy equipment in the priority order of section 6.3, keeping the running total at or below USD 300. Tell Claude each price so the tally stays current | 6.3 | Your choice |
| 4 | Session S1, called when its decision sheet is ready (plan date about Sat 10-03) | The A5 baseline decisions and permissions | 8 | About 60 min |
| 5 | Bench session, then S2 and S3 | As section 8 | 8 | As section 8 |

Steps 1 and 2 feed WP-PDR-38 (the BOM and the recomputed ordering-gate figure) and WP-PDR-43 (the V&V plan). The sooner they come in, the sooner those can start.

## 1. CR disposition brief (written by WP-PDR-01)

Reserved for WP-PDR-01 (plan §3.0 row 01 and §3.2): the disposition brief for OD-40 at session S1, covering CR-003 revision 4, CR-006 revision 3 and the A5 re-baseline CR-018, with their section 12 questions and recommendations. It is written after each CR's section 6 impact reviews (rule C6).

## 2. Withdrawn: PCBWay email and instant quotes (revision 1 output a; OD-04)

Withdrawn by the A5 decision: the boards are JLCPCB 2-layer bare boards that you solder, and TS-012 §8.12 records that no quote is requested from anyone (plan §6.0, OD-04 "Dropped"). Revision 1 of this section (the Part A and Part B emails and the section 2.4 instant-quote rows Q-01 to Q-08 and A-01 to A-04 that TS-004 revision 1 cites) is kept in history at `1fe9c1a`. The JLCPCB price read that replaces it is section 5.3; TS-004 is re-scored for JLCPCB in WP-PDR-27. **Do not send the PCBWay emails.**

## 3. Withdrawn: vendor quote requests (revision 1 output b; OA-5, OD-34)

Withdrawn: A5 uses the hand-matched 8 MHz crystal ladder (TS-012 §8.3 row 11) and the RA07M1317M module, so the Inrad #111, KVG and Guerrilla RF GRF5604 requests are not needed (plan §6.0, OD-34 "Dropped"; OD-06 and OD-07 dropped or replaced). Revision 1 text at `1fe9c1a`. **Do not send them.**

## 4. Downloads that need your browser or permission (output c)

### 4.1 Withdrawn: st.com items (OD-18)

Withdrawn: no PD54008L-E model is built (plan §6.0, OD-18 "Dropped").

### 4.2 Downloads and permissions still asked (session S1)

| Id | Item | Asked at | Plan row |
|---|---|---|---|
| D-1 | KDB 447498 D01 and KDB 643646 D01 (apps.fcc.gov) and the two VHF portable SAR reports named in `docs/research/rf-exposure-evaluation.md` (FCC IDs AZ489FT4948 and AZ489FT7098) | S1 | OD-39 |
| D-2 | NASA-STD-8739.8, the SWEHB PAT-006 and PAT-007 checklists and the SWEHB PAT-071 PDR checklist (MS Word downloads) | S1 | OD-21 |
| D-3 | Permission for the emulator downloads (npm, git) and the rp2350js mirror fork | S1 (permission); S2 (decision) | OD-25 |
| D-4 | SPLAT! install for the site link budget (optional; the Egli model is the fallback) | S1 | OD-39 |

The revision 1 row D-5 (PCM1808 breakout) is dropped (plan §6.0, OD-39).

## 5. Price-check list and ordering-gate reads (OD-42; TS-012 §8.11 and §8.4)

**Why.** Mouser blocks automated reads, so every Mouser price in TS-012 comes from an aggregator (TS-012 EX-12). The design's cost test is: worst case, with 15 % contingency on every line, at or below USD 300 (TS-012 §8.4). Revision 6 of TS-012 puts the stacked worst case USD 16.51 over that line before guards G1 and G2, and USD 0.17 inside after them. Real cart numbers from your browser replace the estimates, and WP-PDR-38 recomputes the figure. **Nothing is ordered at PDR.** The order comes after CDR, and only if the recomputed worst case is at most USD 300 (plan §6.0, OD-20 replaced by the ordering gate).

**Rules for the reads.**
- Use your own browser. Adding items to a cart is fine. **Do not check out, do not enter payment details, do not create an account.** If a site will only show a price or shipping after sign-in, stop there and write "needs sign-in".
- A ZIP code for a shipping estimate is fine to enter on the site itself. Do not send Claude your address; the shipping amount is all Claude needs.
- Write the date and time (with time zone) once per site. Prices change daily; the date makes the number usable as evidence.
- A saved PDF or a screenshot of each cart page is welcome but not required. A pasted table in chat is enough.
- Prices without sales tax (you excluded it, status note 2026-09-27 §10).

### 5.1 Mouser (one cart)

Search each part number on mouser.com, add the quantity shown to one cart, and write down the four things in the last columns. "Flags" means any lifecycle words on the part page: "End of Life", "Obsolete", "Not Recommended for New Designs", "Non-Stocked", "Factory lead time", or a minimum order above the quantity.

| # | Qty | Part number (search this) | What it is | TS-012 unit price | Your price each | In stock | Flags |
|---|---|---|---|---|---|---|---|
| 1 | 2 | GVA-84+ | PA driver and spare | 2.99 | | | |
| 2 | 1 | G5V-2-DC5 | T/R relay | 3.33 | | | |
| 3 | 1 | 530002B02500G | Boyd heat sink (end wall) | 3.39 | | | |
| 4 | 2 | C1206C220J1GACTU | 22 pF LPF capacitor | 0.29 | | | |
| 5a | 2 | 1812SMS-68NJLC | 68 nH LPF coil | 1.90 | | | |
| 5b | 2 | 1812SMS-82NJLC | 82 nH LPF and drive coil (TS-012 read 79 in stock) | 1.90 | | | |
| 6 | 3 | 2643000101 | Fair-Rite supply chokes | 0.10 | | | |
| 7 | 2 | MCP6002-I/P | Op amps | 0.44 | | | |
| 8 | 1 | SC1631 | Raspberry Pi Pico 2 | 5.00 | | | |
| 9 | 1 | 485-2045 | Adafruit 2045 Si5351A board | 7.95 | | | |
| 10 | 4 | MMBFJ310LT1G | J310 FETs | 0.23 | | | |
| 11 | 10 | ECS-80-20-4X | 8.000 MHz crystals (price at 10) | 0.532 | | | |
| 12 | 7 | 2N3904BU | Transistors | 0.28 | | | |
| 13 | 1 | NE5532P | Audio op amp | 0.81 | | | |
| 14 | 8 | 1N5711W-7-F | Schottky diodes | 0.307 | | | |
| 15 | 2 | B3F-1052 | Push buttons | 0.39 | | | |
| 16 | 2 | SJ1-3535NG | 3.5 mm jacks | 1.62 | | | |
| 17 | 1 | CONSMA003.062-G | Antenna SMA, edge mount | 4.47 | | | |
| 18 | 1 | CONSMA001-C-G | Monitor-port SMA | 2.80 | | | |
| 19 | 1 | EG1218 | Power switch | 0.72 | | | |
| 20 | 2 | 1043P | 18650 holders | 2.95 | | | |
| 21 | 1 | S-8252AAO-M6T1U | Cell protector IC | 1.66 | | | |
| 22 | 2 | AO3400A | Protector FETs | 0.52 | | | |
| 23 | 3 | DMP3099L-7 | P-channel FETs | 0.40 | | | |
| 24 | 1 | MF-R300 | Pack PTC fuse | 0.50 | | | |
| 25 | 1 | LM2940CT-5.0/NOPB | 5 V regulator (TS-012 read 141 in stock) | 2.04 | | | |
| 26 | 2 | 103AT-2 | NTC thermistors | 0.58 | | | |
| 27 | 2 | LM393P | Comparators | 0.53 | | | |
| 28 | 3 | 74LVC1G80GV,125 | Divider flip-flops | 0.15 | | | |
| 29 | 1 | TG2520SMN 25.000M-MCGNNM3 | TCXO (TS-012 read 1,810 in stock) | 3.61 | | | |
| 30 | 2 | 2843000202 | BN-43-202 cores | 0.88 | | | |
| 31 | 1 | 120-SA | Thermal compound | 5.44 | | | |
| E1 | 2 | C1206C390J1GACTU | 39 pF LPF capacitor (never read; estimated 0.29) | est. 0.29 | | | |

**Look-ups only (do not add to the cart).** For each, write "stocked" or "not stocked" and the price at the quantity shown. These are options the analyses may still call for (TS-012 §8.11 item 1; D-13, D-14).

| # | Qty | Search | Why |
|---|---|---|---|
| L-1 | 2 | 1812SMS-68NG (the 2 % "G" grade of row 5a) | D-14 recommends 2 % LPF coils |
| L-2 | 2 | 1812SMS-82NG (the 2 % grade of row 5b) | D-14 |
| L-3 | 1 | 1812SMS-47NJ | Only if the drive bandpass D-13 is adopted |
| L-4 | 2 | C1206C220G1GACTU and C1206C390G1GACTU (2 % "G" tolerance of rows 4 and E1) | D-14 |

**Cart totals (the ordering-gate read, TS-012 §8.4 item 1).** With rows 1 to 31 and E1 in the cart, write down:

| Item | Value |
|---|---|
| Merchandise total | |
| Shipping charge shown (cheapest ground) | |
| The free-shipping threshold Mouser states (TS-012 assumes USD 100) | |
| Any tariff or duty line in the cart, and its amount | |
| Date, time, zone | |

Not yet in the cart: the surface-mount resistor and capacitor list (TS-012 row E2 and E5), because the schematic values do not exist yet. Claude sends that short list when WP-PDR-37 has the values, as one more small read. Screws, standoffs and knobs (E3, E4): skip them if you have them (guard G2).

### 5.2 RF Parts (the PA module; TS-012 §8.4 item 2)

1. Open https://www.rfparts.com/ra07m1317m.html (the RA07M1317M-501 page).
2. Write down: the price for 1, the stock words on the page ("In Stock", "New", or anything about end of life or last-time buy).
3. Add one to the cart and read the shipping charge to your address (enter your ZIP if asked; the USD 15 minimum order is met by the module). Stop before payment.

| Item | Value |
|---|---|
| Price for 1 (TS-012: 28.91) | |
| Stock words | |
| Cheapest shipping shown | |
| Date, time, zone | |

### 5.3 JLCPCB (the two bare boards; TS-012 §8.4 item 3)

On jlcpcb.com, use the instant quote (no files needed for a price; enter the size by hand). Run it twice, once per design:

| Setting | Main board | RF board |
|---|---|---|
| Layers | 2 | 2 |
| Size | 64 x 100 mm | 40 x 35 mm |
| Quantity | 5 | 5 |
| Thickness | 1.6 mm | 1.6 mm |
| Surface finish | HASL (with lead or lead-free: note both prices if they differ) | same |
| Everything else | the default | the default |

Then, with both in the cart (or on the quote page's shipping estimate), choose the United States and write down:

| Item | Value |
|---|---|
| Board price, main board, 5 pcs (TS-012 floor: 2.00) | |
| Board price, RF board, 5 pcs (TS-012 floor: 2.00) | |
| Any "different design" or engineering fee | |
| Cheapest US shipping that **prepays the duty** (the option name and price) | |
| The duty or tariff amount shown | |
| Is the duty charged on the boards only, or on the whole order including shipping? (the words on the page) | |
| Date, time, zone | |

If the shipping or duty page needs sign-in, write "needs sign-in" and stop; TS-012's estimates then stand (USD 12 to 25 shipping; duty 35 % to 92.5 %).

### 5.4 18650BatteryStore (cells and charger; TS-012 §8.4 item 4 and §8.11 item 6)

1. Add **2 x Molicel P28A** (https://www.18650batterystore.com/products/molicel-p28a) and **1 x XTAR MC1** (https://www.18650batterystore.com/products/xtar-mc1) to the cart.
2. Read the cart shipping to your address (cheapest, TS-012 assumes USPS Ground Advantage).
3. On the MC1 page or its product sheet: the charge termination voltage and its tolerance (for example "4.20 V +/- 1 %"), as printed.
4. Is the two-bay **XTAR MC2** back in stock? (add-back AB-B)

| Item | Value |
|---|---|
| P28A price each (TS-012: 5.99 sale) | |
| MC1 price (TS-012: 4.99 sale) | |
| Shipping | |
| MC1 termination voltage and tolerance, as printed | |
| MC2 in stock? price? | |
| Date, time, zone | |

### 5.5 Datasheet reads Claude does first (TS-012 §8.11 items 7 and 8)

The Boyd 530002B02500G drawing (mass; a flat centre face of at least 30 x 10 mm for the module flange with room for two M2.5 holes; which fins face out), the DMP3099L-7 maximum RDS(on) at VGS -6 V and the Bourns MF-R300 R1max are public datasheet values. Claude reads them in WP-PDR-38 and WP-PDR-24 and asks you only if a page is blocked.

### 5.6 Your own stock (TS-012 §8.11 item 9)

| Question | Why | Your answer |
|---|---|---|
| Are your through-hole resistors 1 % metal film? | The VGG clamp divider needs 1 % parts; otherwise they are bought (E2) | |
| About how much 24 AWG magnet wire do you have? (about 3 m is needed) | BPF coils and ring transformers | |
| Your two potentiometers: values, shaft type, do they have knobs? | Volume and tuning controls; knobs E4 | |
| Your USB power adapter: 5 V and at least 1 A? (read the label) | The MC1 charger needs it | |
| Your 2 m antenna: the plug is SMA male (you said so); is it marked for 144 MHz or dual-band? | EX-9: it is the antenna the radio is tested with on the air | |

The value list to check your resistor and capacitor assortment against comes later, with the schematic (WP-PDR-37).

### 5.7 What happens with your numbers

Claude transcribes them into the dated status note, then WP-PDR-38 puts each price, stock and flag into the BOM with its date and recomputes the TS-012 §8.4 roll-up: low, planning and worst, with 15 % contingency on every line. The planning figure is compared with your USD 200 target and the worst case with the USD 300 maximum. If the worst case is over, guards G1 to G4 are applied in order (free Mouser shipping, your own knobs and hardware, one board instead of two, no spare driver) and the result is shown to you. The figure is reported at S2 for information. If a price read shows a part out of stock or at end of life, WP-PDR-38 records it as a risk and proposes a substitute; nothing changes in the design without your decision. If session S1 changes a BOM row, only that row is re-read.

## 6. Equipment list for A5 (output e; OD-26, OD-19, OD-22, OD-32)

This list is reviewed inside WP-PDR-43 (the V&V plan). The rule you set (status note 2026-09-27 §11): test equipment is outside the radio's USD 300 maximum, but **all new equipment you buy together must stay at or below USD 300**. Every instrument whose reading is cited as evidence gets a tool validation (TV) record with a known-answer check before its first credited use (04 §6.3; charter §8).

### 6.1 What you already have (no action)

| Item | Used for | Note |
|---|---|---|
| NanoVNA with its calibration loads | Filter tuning (BPF, LPF), T/R relay isolation and loss (EX-14), pad and cable measurements | TV record before first credited use |
| Fluke 174 multimeter | DC voltage and current readings | No temperature input (status note 2026-09-28 §2), so a separate thermometer is on the buy list |
| 50 ohm dummy load, BNC | Every transmit test | Its power rating is question Q-1 below |
| Baofeng BF-F8HP | Only as the strong-signal source for the receiver survival test TC-SYS-025, into a pad, never on the air in that test | It is FM-only, so it cannot be the second CW station for MOE-001 and MOE-002 |
| 2 m antenna with SMA-male plug | On-air use (EX-9) | Question in section 5.6 |
| Bench supply, heat gun, solder and flux | Bench tests, assembly | SI-013; heat gun added to the hand-assembly bench (OD-32) |
| Your straight key and paddle (3.5 mm plugs) | Bench session and keyer tests | Names are question Q-5 |

### 6.2 Five facts to send (any time)

| Id | Question | Why |
|---|---|---|
| Q-1 | What power rating is printed on your BNC dummy load (watts, and for how long if stated)? | It must take at least 5 W continuous from the radio and at least 8 W briefly for the BF-F8HP power check (E-08 of revision 1) |
| Q-2 | Do you have digital calipers (150 mm)? | Size checks (MOP-002, OQ-VV-002). If not, buy or borrow (row B-7) |
| Q-3 | Do you have a kitchen or postal scale with 1 g steps up to at least 500 g? | Mass check TC-SYS-071 (OQ-VV-002). If not, buy or borrow (row B-8) |
| Q-4 | Do you have a Pico 2 development board free for the bench session (the Morse menu demonstration, WP-PDR-40)? | If not, one Pico 2 with headers, about USD 5 (row B-6) |
| Q-5 | The make and model of your straight key and paddle (OD-22) | ICD-CTL-KEY and the bounce capture |

### 6.3 To buy, inside the USD 300 equipment cap (in priority order)

Prices marked **E** are Claude's estimates, not read from a store; **S** is a web search summary of 2026-09-29, not a store page read. When you look at an item, tell Claude the price you see; Claude keeps the running total in the status note. **Before each purchase, check the running total: if the next item would take it over USD 300, stop and tell Claude**; the lower rows are then deferred, borrowed or re-planned. Claude compares specific models on request.

| Row | Item | Minimum specification | Price basis (USD) | Needed by | TV record |
|---|---|---|---|---|---|
| B-1 | **K-type thermocouple thermometer with bead probes** | Stand-alone meter for K-type probes; two inputs recommended (sink and ambient at the same time; T1 minus T2); 0.1 C resolution; its manual states the accuracy over at least 20 to 120 C (the module case can reach about 106 C, thermal analysis); bead probes with polyimide (Kapton) tape, two in all. An infrared thermometer is not a substitute (emissivity) | E: 20 to 45 for the meter with one bead probe; a second bead probe 9.95 (TS-012 EX-13) | The in-situ sink and NTC-offset measurements (`thermal-ts012.md` §9 item 2), before first on-air use; the ice-point TV check can be done as soon as it arrives | Yes (ice point plus a second reference point; OQ-VV-003) |
| B-2 | **SMA-male to BNC-female adapters, two** | 50 ohm, rated to 3 GHz or more | E: 5 to 15 for two | Connects the radio's SMA antenna port to the BNC dummy load; first power-on into the load | No (measured on the NanoVNA with the load) |
| B-3 | **tinySA Ultra** (you buy it later, status note 2026-09-28 §1) | The tinySA Ultra of SI-034 and ADR-021, from an official or authorized seller | S: about 187 to 209 (maker's store on sale about 186.90; Radioddity 199.99; Lab401 209.00; other sellers higher) | Spurious-emission checks before the first on-air transmission (REQ-SYS-017) | Yes (receipt inspection plus TV, OQ-VV-001) |
| B-4 | **Pad for the BF-F8HP test** | 11 to 12 dB in total (for example 10 dB plus 2 dB), each rated at least 10 W continuous; SMA male on the input side to mate the BF-F8HP's SMA-female port, SMA or BNC on the output with adapters; measured on the NanoVNA before use | E: 20 to 60 | TC-SYS-025 (the receiver survival test), which runs after TRR | No (fixture; measured in each run) |
| B-5 | Near-field H-field probe set | Two or more shielded loop sizes (about 3 to 10 mm and 20 to 30 mm), SMA output, for use with the tinySA | E: 15 to 40 | Only for locating leaks and noise sources. The shielding requirement REQ-SYS-177 is deferred and build 1 has no coating (CR-003 revision 4), so **buy it only after the tinySA and only if the total allows** | Yes if its readings are cited (relative-measurement TV) |
| B-6 | Pico 2 with headers (only if Q-4 is "no"), and later a second Pico 2 as the logic-capture probe | SC1631 or SC1632 | About 5 each (TS-012 row 8) | The first: the bench session. The second: the keyer timing captures before TRR (ADR-009; OD-19) | The capture Pico: yes, due TRR |
| B-7 | Digital calipers, 150 mm (only if Q-2 is "no") | 0.01 mm resolution | E: 15 to 30, or borrow | Size check before TRR | No |
| B-8 | Scale, 1 g steps, 500 g or more (only if Q-3 is "no") | Kitchen or postal | E: 10 to 20, or borrow | Mass check before TRR | No |

**Running total, estimate.** Rows B-1 to B-4 (all needed): about USD 242 to 339. With B-5 to B-8 at their highest (two Pico 2 boards): up to about USD 439. The cap is therefore tight: the tinySA is most of it. To stay inside USD 300: buy B-1, B-2 and B-3 first (about USD 222 to 279); pick a pad for B-4 whose price fits what is left; borrow calipers and a scale if you have none (the radio club, perhaps); leave B-5 unless money is left over. The final tally uses the prices you see.

### 6.4 Not bought (and why)

| Item | Why not |
|---|---|
| 30 to 40 dB power attenuator for the tinySA | The radio has a 40 dB monitor port (REQ-SYS-141, TS-012 row 18), so the tinySA reads the transmitter through it (TS-012 EX-13, decided with the exceptions at S1). If S1 does not accept EX-13, a 10 W attenuator is added to this list. The system and TX test cases still name the attenuator; CR-018 and the WP-PDR-35 test-case work carry the change |
| Reference antennas (Signal Stick, MFJ-1714S or Diamond SRH770) | Your own 2 m antenna is used instead (TS-012 EX-9, at S1) |
| A calibrated weak-signal generator for MOE-010 | Recommended: accept Analysis for the bench part of MOE-010 (asked at S2, OD-09) |
| Second 2 m CW station for MOE-001 and MOE-002 | Not bought: a club member's station, if one can be matched within 1 dB (CR-006 Q5; you said you would ask the club, status note 2026-09-27 §5). If none is found, MOE-001 and MOE-002 stay open at SAR as a lien. Answer at S2 (OD-26) |
| sigrok-cli install | Decision by CDR (OD-19): the development-board route is recommended for the PDR bounce capture |
| PCM1808 breakout, PD54008L-E samples, display parts | Not in A5 |

### 6.5 Hand-assembly bench (OD-32, confirm at S1)

Temperature-controlled soldering station with a stand and auto-sleep, fume extraction, eye protection, and the heat gun (TS-012 §8.12, WP-PDR-16 row). Confirm you have them; they feed the hazard analysis (HZ-015).

## 7. Regulatory corpus additions (output f; OD-24a; OQ-SAF-024, C-062)

The corpus (`docs/references/md/regulatory/`, eCFR issue 2026-09-23) lacks the items below. The CFR text rows are fetched by Claude from the eCFR versioner API with the README command pattern once you approve them (OD-24a, session S1); the table-image rows need your browser, because the 2.106 table body is published as images (README "Known limitation").

| Row | Item | Why | Who does what | Needed by |
|---|---|---|---|---|
| R-1 | 47 CFR 2.106 Table of Frequency Allocations rows covering 150.8 to 174 MHz, with their footnotes | OQ-SAF-024 (HZ-008 C7): the VHF public-safety and maritime services that an out-of-band fundamental would hit, cited verbatim | **You:** open the eCFR reader page for 47 CFR 2.106, find the page images covering 150.8 to 174 MHz, and send Claude screenshots. **Claude:** transcribes them into `47cfr-2.106-150-174mhz.md` with the footnotes fetched as text | Any time; at the latest S1 |
| R-2 | The Part 80 rule that designates 156.800 MHz for distress, safety and calling | OQ-SAF-024 | **Claude**, after OD-24a: finds the section by an eCFR search for "156.800" and fetches it as text; you approve | S1 |
| R-3 | 47 CFR 2.803 (marketing), with the amendment published at 91 FR 57800 (2026-09-11), which the 2026-09-23 issue text did not yet carry | The 15.23 reading behind ADR-025 and CR-006 (`pcbway-export-and-vendor-questions.md` F21, open item 8; plan C-149) | **Claude**, after OD-24a: fetches the current 2.803 text and the Federal Register document | S1 |
| R-4 | Browser check of the five harmonic rows of `47cfr-2.106-harmonic-bands.md` (DECISION-10) | Those rows are Medium confidence until checked against the current page images (RSK-029) | **You:** view the five rows on the eCFR page images and send screenshots; **Claude** compares and records | Any time; at the latest S1 (OD-39) |
| R-5 | Any clause the WP-PDR-34 citation-resolution table (`docs/requirements/tx/regulatory-citations.md`) finds unresolved | E-12 second clause of the PDR entrance criteria | **Claude** lists them; you approve each | S2 |

## 8. Owner decisions by session (output g; plan §6.0 governs)

The sessions of plan §6.0 replace the revision 1 sessions B0 to B4. Following your direction of 2026-09-29 (status note §8), each session is called as soon as its decision sheet is ready, at your convenience; the plan dates are the latest planned. The full wording and recommendations are in plan §6.0 and §6.1; each session gets its own plain-language sheet.

| Session | Plan date (latest) | What you are asked |
|---|---|---|
| (No session) | Any time now | OD-42 price check (section 5); the equipment facts Q-1 to Q-5 (section 6.2; Q-5 is OD-22 naming); R-1 and R-4 screenshots (section 7) |
| S1 A5 baseline | About Sat 10-03 AM, about 60 min | OD-40 (CR-003 revision 4, CR-006 revision 3, CR-018 and their questions, exceptions EX-1 to EX-14); OD-43 batch 1 merges; OD-23 and PCR-4; OD-24b; OD-13 to OD-16; OD-10 part 1; permissions and facts OD-17, OD-19, OD-21, OD-22, OD-24a, OD-25, OD-32, OD-39 (section 4.2) |
| Bench | About Tue 10-06 PM, about 1.5 h | Morse-menu demonstration, bounce capture, keyer HIL (needs Q-4 and Q-5) |
| S2 Values and safety | About Mon 10-12 PM, about 1.5 h | OD-10 part 2; OD-09 TBR values; OD-35; OD-05; OD-08; OD-22 verdict; OD-25 decision; OD-31 charter edits (section 11); OD-37; OD-43 batch 2; OD-24b; OD-26 rest (the club station). The recomputed ordering-gate figure, for information |
| S3 Readiness | About Sat 10-17 AM, about 30 min | OD-29, OD-11, OD-27, OD-28, any OD-09 re-ruling |
| PDR review | About Mon 10-19 PM | OD-30 |

Withdrawn from revision 1 (plan §6.0): OD-04, OD-06, OD-07, OD-12, OD-18, OD-20 (replaced by the ordering gate), OD-34; OD-02 and OD-03 replaced by OD-40; OD-33, OD-36 and OD-38 done. Section 11 below was written for "session B3, Sun 10-04"; OD-31 is now asked at S2.

## 9. Reply format

Answer in chat, in any order, one line per item. For example: "Mouser 2026-09-30 20:10 CDT: row 1 2.99 in stock 2,700 no flags; ... merchandise 97.12, shipping 0, threshold 100, tariff 7.40. RF Parts: 28.91 In Stock, ship 12.35. JLCPCB: ... Q-1: 15 W. Q-2: yes. Q-3: no." A pasted table or a screenshot is just as good. Claude transcribes your words verbatim into the dated status note, writes its reading under them for you to correct, and routes each answer to the WP that uses it (38 for prices, 43 for equipment).

## 10. Traceability

| WP-PDR-04 output | Section | Closes or enables |
|---|---|---|
| (a) PCBWay email and instant quotes | 2 (withdrawn) | OD-04 dropped (TS-012 §8.12); C-207 closed by withdrawal, for the lead SE to record in the carried-item list |
| (b) Inrad, KVG, Guerrilla RF requests | 3 (withdrawn) | OD-34 dropped; C-208 closed by withdrawal, for the lead SE to record |
| (c) Downloads and permissions | 4 | OD-18 dropped; OD-21, OD-25, OD-39 at S1 |
| (d) Price-check list and ordering-gate reads (replaces the stock checks) | 5 | OD-42; TS-012 §8.11 items 1 to 9 and §8.4 items 1 to 4; EX-12; RSK-038 S1 input for the A5 parts; WP-PDR-38 price, stock and lifecycle columns |
| (e) Equipment list for A5 | 6 | OD-26 (the rest at S2), OD-19, OD-22, OD-32; C-209 (OA-6) and C-210 (OQ-VV-002) prompts (Q-5, Q-2, Q-3); C-061 equipment confirmation (OQ-SAF-019); OQ-VV-001, OQ-VV-003; TS-012 EX-13, D-16; CR-006 Q5, Q6 |
| (f) Regulatory corpus additions | 7 | C-062 (OQ-SAF-024 corpus rows); OD-24a; DECISION-10 check (OD-39) |
| (g) Owner decision list | 8 | Plan §6.0 and §6.1, ordered by session |

## 11. Charter edit list for the owner (written by WP-PDR-13; OD-31, C-113)

**Why this list.** The charter changes only by your hand (charter §1; agents never edit `docs/process/00-charter.md`, 08 §1 SCOPE). The SRR records and rulings left three charter wording items due before PDR. Each is drafted below with the exact text to replace, for your decision at session B3, Sun 10-04 (OD-31), before freeze F1. Charter read at blob `41575d21` (last changed at `6ea6b1d`). WP-PDR-17 may add edits to this list for OD-31 (plan section 6.1). If you approve an edit, make it in the charter yourself, or tell Claude "apply CE-n as drafted" and Claude transcribes your words into the status note, and you commit the charter change. Nothing below changes a process, a requirement, a baseline or a tailoring disposition.

| Id | Charter location | Before (verbatim) | After (proposed) | Source | Recommendation |
|---|---|---|---|---|---|
| CE-1 | §12 tailoring register, row "Human Systems Integration (SE-65/66)", Rationale cell | "HSI approach is a section of the SEMP covering controls, display, audio, key/paddle ergonomics and RF-exposure safety." | "HSI approach is SEMP §7.3.1, covering controls, display, audio, key/paddle ergonomics and RF-exposure safety, instead of the stand-alone HSI Plan that NPR 7123.1D §5.2.1.3 strongly recommends for Category 1 and Class A programs and projects (applied to cwht because of the owner's Class A and Criticality-1 election, charter §1); that section leaves the location to the project manager, who chose a SEMP section at SRR (decision 2) because cwht has one operator population with one set of tasks, no crew, habitat, manpower or personnel-selection domains, and HSI content that fits one section on the SE HB App. R outline." | SRR decision 2 ("add the rationale to the charter section 12 HSI row", `docs/reviews/SRR/decisions-for-owner.md`); SEMP Appendix F item F-08 and Appendix E OQ-SE-001; SEMP §7.3.1 rationale paragraph; carried item C-113 | Approve. It records a decision you already made; the disposition stays Customized |
| CE-2 | §10, closing parenthesis of the safety-critical component sentence | "(SRR decisions 9 and 10 (a); the single authoritative component list is `docs/process/07-software-engineering-plan.md` §14.1, updated from the hazard analysis)" | "(SRR decisions 9, 10 (a) and 40; the determination record is `docs/process/03-software-classification-and-rmm.md` §4.3 and the single authoritative component list is `docs/process/07-software-engineering-plan.md` §14.1, both re-run from the hazard analysis at PDR and CDR)" | 03 §6.5 item g (as revised by CR-010); CR-010 §12 Q3; 07 §22 rows "Menu override command path ruling" and "Frequency-control determination"; SRR decision 40 adopted REQ-SYS-182 and so created the frequency verification unit the sentence already names | Approve, with CR-010. If you reject CR-010, CE-2 still holds: decision 40 is your ruling of 2026-09-26 either way |
| CE-3 | §3, paragraph after the life-cycle table, first sentence | "Entrance and success criteria for SRR, PDR, CDR, TRR and SAR are tailored from NPR 7123.1D App. G Tables G-4, G-6, G-7, G-10 and G-11," | "Entrance and success criteria for SRR, PDR, CDR, TRR and SAR are tailored from NPR 7123.1D App. G Tables G-3 and G-4 (SRR), G-5 and G-6 (PDR), G-7 (CDR), G-10 with SIR Table G-9 items (TRR) and G-11 with Table G-12 items (SAR), as `docs/process/01-lifecycle-and-reviews.md` §4.3, §5.3, §6.3, §7.3 and §8.3 name them," (the rest of the sentence unchanged) | INSP-024 finding-3 and cross item X-2 (`docs/reviews/SRR/checklists/compliance-matrix.md`): the compliance matrix row SE-34 copies the short list, while 01 uses Tables G-3, G-5, G-9 items and G-12 items as well; the SE-34 row itself is corrected by the compliance matrix writer (PDR work plan WP-PDR-12) to the same list | Approve. It makes the charter name every table 01 already tailors |

**Items checked and not needed.** The charter §5 artifact rows that 07 §22 carried as a charter issue (`docs/sprints/index.md`, `docs/design/sw/<module>.md`, `firmware/devcheck/`, `firmware/emu/`, `firmware/THIRD-PARTY-NOTICES.md`, the per-run report directories, the compliance matrix schema) and the status-note row of SEMP Appendix F item F-09 are already in charter §5 since `6ea6b1d`; no edit is drafted for them.

**Reply format.** "OD-31: CE-1 approve, CE-2 approve, CE-3 approve" (or reject or amend any one). Claude transcribes the reply verbatim into the dated status note (section 9), and the SEMP Appendix E and F rows, 07 §22 and 03 §6.5 item g record the outcome through their writers.
