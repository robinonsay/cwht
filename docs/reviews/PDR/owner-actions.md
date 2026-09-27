# PDR owner action pack

**Work package:** WP-PDR-04 of `docs/plan/pdr-work-plan.md` (revision 2, `ab2af2d`), section 3.2. **Author:** Claude (lead SE). **Date:** 2026-09-27. **Configuration read:** `main` at `3d4a74d` (status note 2026-09-27 section 4 records the owner's approval of the plan and the new dates).
**Status:** Informational working product of the PDR phase (a request list, not a baselined item). No review record is required (plan WP-PDR-04 "Reviewer"); the equipment list of section 6 is reviewed inside WP-PDR-43. It becomes an input to `docs/reviews/PDR/package.md` §2 (owner actions) and to the open-decisions slide.
**Drafts only.** Claude never sends an email, submits a quote form, places an order, downloads a file or creates an account. Every message below is a draft for the owner to send from the owner's own mail client. Owner replies are transcribed verbatim into `docs/plan/status/status-2026-09-28.md` and later dated status notes (SEMP §7.4; charter §4 item 4), never into this file.
**AT RISK.** Items marked **AT RISK (CR-003)** or **AT RISK (CR-006)** are drafted on the text of those CRs as proposed (CR-003 revision 3, CR-006 revision 2), which await the owner's disposition (OD-02, OD-03). They are asked now because the PCBWay closure of 2026-10-01 to 10-04 does not wait for the disposition (plan rule C8; status note 2026-09-27 §3 row 9). If a disposition changes them, section 9 says what is re-sent.

## 0. What to do, in order

| Step | When | Action | Section | Owner time |
|---|---|---|---|---|
| 1 | Mon 09-28 morning | Download the three st.com items (OD-18) and tell Claude where they are | 4.1 | 15 min |
| 2 | Mon 09-28 | Send the Inrad and KVG quote requests (OA-5, OD-34) and the Guerrilla RF request (section 3.3 explains the conflict to resolve first) | 3 | 15 min |
| 3 | Mon 09-28, session B0 | Answer the B0 rows of section 8 (dispositions, instrument answers, key and paddle, permissions); reply in the format of section 9 | 6, 7, 8 | 30 min |
| 4 | Mon 09-28 to Tue 09-29 (B1a) | Run the dated stock checks of section 5 where the distributor pages need your browser or login | 5 | 30 min |
| 5 | **Tue 09-29 morning, hard deadline** | Send the PCBWay email and run the instant quotes (OA-4, OD-04); answers are due 09-30, before the factory closes 10-01 to 10-04 (`docs/plan/schedule.md` §3) | 2 | 30 min |
| 6 | Tue 09-29, session B1a | Answer the B1a rows of section 8 | 8 | 20 min |

Section 1 is the CR disposition brief of WP-PDR-01. Sections 2 to 7 are the WP-PDR-04 outputs (a) to (f); section 8 is output (g).

## 1. CR disposition brief (written by WP-PDR-01)

Reserved for WP-PDR-01 (plan §3.2, "The disposition brief for the owner in `docs/reviews/PDR/owner-actions.md` §1"): CR-003 §12 Q1 to Q3 and CR-006 §12 Q1 to Q8 with recommendations, and the cross-CR order rule (CR-006 §5 "Order with CR-003"). Both verification re-checks are recorded with no Major finding (CR-003 §6.4 at `908cc8b`; CR-006 §6.3 at `6d8e624`), so OD-02 and OD-03 can be asked at B0. Until WP-PDR-01 writes this section, the recommendations are those of plan §6.1 OD-02 and OD-03, repeated in section 8 below. CR-006 Q5 and Q6 need facts only you have; section 6 rows E-06 and E-09 ask them in equipment terms.

## 2. PCBWay: email and instant quotes (output a; OA-4, OD-04)

Basis: `docs/research/pcbway-export-and-vendor-questions.md` Part 3 F20 (the SRR draft), updated for the decisions taken since: the PA device is PD54008L-E (SRR decision 58, `docs/research/pa-turnkey-candidates-followup.md` ACTION 17), the build is 5 fabricated with 1 assembled and 2 priced (CR-006 §12 Q2, Q8), the enclosure is a printed case first with the CNC enclosure held as the fallback (CR-003 revision 3), and the case is printed by you with the markings in relief, so no PCBWay print quote is requested (OD-38 preliminary, concurred 2026-09-27, status note §4). Research items closed by the answers: A-PCB-01, A-PCB-06, A-PCB-09 (`docs/research/pcbway-fabrication-and-assembly.md`, `pcbway-export-and-vendor-questions.md`), A-UI-06 (`docs/research/display-and-ui-parts.md`), pa-turnkey ACTION 17. Risks informed: RSK-004, RSK-043, RSK-052 S1, RSK-053.

### 2.1 How to send

- **To:** service@pcbway.com (Part A). Part B goes to 3dcnc@pcbway.com; send it as a separate message with the same subject plus "(CNC)", or send one message to both addresses.
- **Attach:** Raspberry Pi Pico 2 datasheet (RP-008299-DS-3) section 3.2 "Surface-mount footprint" (a page extract or the whole PDF). No design files exist yet; the email says so.
- **When:** Tue 09-29 by 10:00 your time at the latest (Tue evening in China, GMT+8), so the reply lands 09-30.
- **Part B:** **AT RISK (CR-003).** Send it now. It costs nothing, and the answers shape the held CNC fallback package that CR-003 revision 3 pre-approves; after 09-30 the next answer is 10-05.

### 2.2 Draft email, Part A (fabrication and assembly)

```
Subject: Pre-order engineering questions: 4-layer RF board, 5 pcs fabricated, 1 or 2 with turnkey assembly

Hello PCBWay engineering team,

I am preparing an order for a 4-layer, 50 ohm, 144 MHz amateur-radio transceiver board:
5 bare boards fabricated, of which 1 (possibly 2) receive turnkey SMT assembly on the top
side only. Through-hole parts (battery holders, jacks, encoders, buttons, a crystal filter)
will be soldered by me, so please treat them as not placed. The design files are not final
yet; I would like written answers to the points below so the design matches your process
the first time. Where I state an assumption, a simple "confirmed" is enough. I know your
factory closes 1 to 4 October; answers before then would be very helpful.

1. Castellated module. One part is a Raspberry Pi Pico 2 module (SC1631, 51 x 21 mm, 40
   castellated pads on 2.54 mm pitch plus the USB-shell and test-point pads), to be placed
   and reflowed as an SMD part on the top side, footprint and 163 % paste apertures per
   section 3.2 of the attached datasheet. (a) Will you place and reflow it in the same pass
   as the other SMD parts? (b) Will you buy SC1631 from an authorized reseller, or must I
   consign it? (c) The datasheet gives no MSL rating: what baking or handling do you apply,
   and how many extra units do you need? (d) If you prefer that I hand-solder it, please say
   so and whether that changes the quote.

2. PowerFLAT RF transistor with via-in-pad. The RF power transistor is ST PD54008L-E
   (PowerFLAT 5 x 5 mm, MSL 3), bought turnkey from DigiKey or Mouser. Its exposed source
   pad carries about 25 to 30 thermal vias of 0.30 mm finished hole on 0.65 mm pitch; QFN
   exposed pads carry similar vias. (a) Do you require these vias resin filled and capped
   (IPC-4761 Type VII) for assembly, or will you reflow over open vias? (b) What are the
   surcharge and added lead time for "Via in pad" plus "All vias filled with resin and
   capped" on 5 pieces, at 1.0 mm and at 1.6 mm board thickness? (c) Do you offer
   copper-paste filled vias as an alternative? (d) Please confirm you can procure
   PD54008L-E turnkey and apply MSL 3 handling.

3. Board thickness, stackup and plating. I will choose 1.0 mm or 1.6 mm, 4 layers, FR-4
   TG150, 1 oz on all layers, ENIG, green mask. (a) For your standard 4-layer 1.0 mm build,
   what are the L1 to L2 prepreg thickness and its Dk? (b) Your stackup library lists 7628
   prepreg RC46 % Dk 4.74 and core Dk 4.6 for 1.6 mm: at what test frequency, and which
   laminate brand and grade? (c) What finished hole-wall copper thickness do you plate as
   standard, and can I request 35 um average? (d) Is the microsection report available on
   a 5-piece order?

4. Impedance control on a 5-piece order. 50 ohm microstrip on L1 over L2, standard stackup,
   target 50 ohm +/-5 ohm. (a) Do you add a coupon and run TDR, or only a random check?
   (b) Is the impedance test report available for this order size, and is it measured with
   or without solder mask? (c) What is the surcharge?

5. Quantities and later assembly. (a) Please quote assembly of 1 board and of 2 boards from
   a lot of 5 fabricated. (b) If I assemble 1 now, can I order assembly of 1 or 2 more boards
   from the same lot later? Do you keep the remaining bare boards and the stencil, and for
   how long, or must I send the boards back? (c) Please ship all unused turnkey components
   (attrition extras and minimum-order leftovers) with the boards; is there a fee for this?

6. Display FPC. The display is a Sharp LS013B7DH03 panel whose 10-pin 0.5 mm FPC plugs into a
   bottom-contact ZIF connector on the board (the ZIF is an SMD part you place). My
   assumption: I insert the FPC and fix the panel myself after delivery. If I consign the
   panel, would you insert the FPC and fix the panel with double-sided adhesive at final
   assembly, and at what cost?

7. Centroid file. KiCad 10 CSV, header "Ref,Val,Package,PosX,PosY,Rot,Side", units mm,
   origin at the board's lower-left corner, top side only, rotation counter-clockwise
   positive. (a) What is your zero-degree reference (pin 1 position or tape orientation)?
   (b) Do you accept negative angles, or should I normalize to 0 to 360? (c) Will your
   engineers send a placement preview or first-article photo of polarized parts and the
   module for approval before reflow?

8. Gerber and drill files. KiCad 10 RS-274X with X2 attributes off (attributes only as
   G04 #@! comments), aperture macros on, KiCad file names (F_Cu.gbr, In1_Cu.gbr, In2_Cu.gbr,
   B_Cu.gbr, F_Mask.gbr, B_Mask.gbr, F_Silkscreen.gbr, B_Silkscreen.gbr, F_Paste.gbr,
   B_Paste.gbr, Edge_Cuts.gbr) plus a .gbrjob job file; Excellon metric decimal drill with
   full header, separate PTH.drl and NPTH.drl, slots as G85 routes, PDF drill map. Please
   confirm this is accepted without renaming, in particular In1_Cu and In2_Cu.

9. BOM. CSV with columns Item #, Designator, Qty, Manufacturer, Mfg Part #,
   Description / Value, Package/Footprint, Type (SMD, THT, or DNS for do-not-place),
   Your Instructions / Notes. Please confirm, and confirm that LCSC part numbers may be
   given in the Notes column for passives.

Thank you. I will attach your answers to my design review package.

Best regards,
Robin Onsay
```

### 2.3 Draft email, Part B (CNC fallback enclosure) **AT RISK (CR-003)**

```
Subject: Pre-order engineering questions: CNC 6061 aluminum enclosure (1 pc), anodize and engraving

Hello PCBWay CNC team,

I may order one CNC-machined 6061 aluminum enclosure for a handheld radio later this
year (a fallback to a printed case). Before I finish the drawing I would like written
answers to the points below. A simple "confirmed" is enough where I state an assumption.

1. Tapped holes and anodize. The part has M3x0.5 tapped holes and will be bead-blasted and
   Type II anodized. Do you mask the tapped holes during anodizing or tap after anodizing?
   Which is your default, and how do I request the other?

2. Conductive faces. Several faces (a pedestal under the RF transistor, the RF connector
   seat, the PCB mounting bosses and ground contact points) must stay electrically
   conductive. Can you mask them from anodize, and do you offer chromate conversion
   (chem film) on the masked faces? How should I mark them on the drawing?

3. Inserts. Do you install stainless M3 helicoil inserts in 6061, before or after
   anodizing, and what pilot hole should I model?

4. Flatness. For a 15 x 15 mm pedestal face I will call out flatness 0.05 mm and Ra 3.2 um.
   Is this within your standard process, and what does it add to the price?

5. Engraving. The enclosure carries a permanent RF-exposure legend (about three lines of
   text) and markings next to two 3.5 mm jacks. Can you laser-engrave text on the anodized
   face as part of the same job? What are the minimum character height and line width,
   and the cost?

6. Lead time. What is the current lead time for one part of about 140 x 70 x 40 mm, and
   does the 1 to 4 October closure move it?

Thank you.

Best regards,
Robin Onsay
```

### 2.4 Instant-quote set (TS-004; A-PCB-09) **AT RISK (CR-006)**

Run these on pcbway.com (PCB instant quote, then the PCBA estimator), save each result page as a PDF, and send Claude the prices, build times and the date and time with time zone. PCBWay prices "Via in pad" and "All vias filled with resin and capped" only after engineer review (`pcbway-export-and-vendor-questions.md` F15); for those rows, record "after review" and the email answer to item 2(b) supplies the figure.

Common parameters for every fabrication row: 4 layers; FR-4 TG150; board 130 x 62 mm, single board, no panel (planning outline, derived from the 140 x 70 mm MOP-002 envelope less the walls; it is at least 50 x 100 mm, so no panel is required, `pcbway-fabrication-and-assembly.md` F19; the quote is repeated at CDR on the real outline); quantity 5; 1 oz outer and inner copper; minimum track and space 6/6 mil; minimum hole 0.3 mm; ENIG; green mask, white silkscreen; no castellated holes; standard shipping to you.

| Row | Thickness | Via in pad plus resin fill and cap | Impedance control | Price (USD) | Build time | Date, time, zone |
|---|---|---|---|---|---|---|
| Q-01 | 1.6 mm | No | No | | | |
| Q-02 | 1.6 mm | Yes | No | | | |
| Q-03 | 1.6 mm | No | Yes | | | |
| Q-04 | 1.6 mm | Yes | Yes | | | |
| Q-05 | 1.0 mm | No | No | | | |
| Q-06 | 1.0 mm | Yes | No | | | |
| Q-07 | 1.0 mm | No | Yes | | | |
| Q-08 | 1.0 mm | Yes | Yes | | | |

Rows Q-01, Q-04, Q-05 and Q-08 are the minimum set (the four prices of A-PCB-09); the other four split the two surcharges and take a minute each.

Assembly estimate (PCBA estimator), turnkey, top side only, through-hole count 0, for 1 board and for 2 boards. No BOM exists yet, so run it at two planning points and record both; WP-PDR-38 replaces them with the preliminary BOM counts, and the CDR quote uses the released BOM.

| Row | Boards assembled | Unique SMD part numbers | SMD placements | QFN, DFN and leadless packages | Estimate (USD) | Date, time, zone |
|---|---|---|---|---|---|---|
| A-01 | 1 | 50 | 160 | 8 | | |
| A-02 | 1 | 90 | 300 | 14 | | |
| A-03 | 2 | 50 | 160 | 8 | | |
| A-04 | 2 | 90 | 300 | 14 | | |

These counts are the lead SE's planning bracket, not design data. The results feed TPM-014 and MOP-016 (WP-PDR-29), the cost estimate (WP-PDR-46), TS-004 (WP-PDR-26) and CR-006 §12 Q2 and Q3.

### 2.5 Deferred: fixture Gerber upload (A-PCB-08)

A-PCB-08 asks you to upload the known-answer fixture zip (`ka-gerbers-kicad.zip`) to see whether PCBWay's CAM accepts KiCad 10 files with the In1_Cu and In2_Cu names without a ticket. That zip and its generator were made in a research session scratch directory and are not in the repository; the only committed KiCad fixtures (`tools/tests/fixtures/kicad/`) are 2-layer boards, which cannot test inner-layer names. The question is therefore asked in the email (Part A item 8) instead, and the upload waits for the 4-layer fixture of the kicad-cli export wrapper (plan WP-PDR-07 TV-016, `tools/normalize_fab.py`). Nothing is needed from you now.

## 3. Vendor quote requests (output b; OA-5, OD-34)

Basis: TS-001 §6 item 5 (value of information: the Inrad -6 dB bandwidth tolerance decides whether candidate A passes M1 against REQ-SYS-024; a KVG 400 to 600 Hz type would raise A-C8), `docs/research/cw-selectivity-options.md` F2, F3 and ACTION 15, `docs/research/pa-turnkey-candidates-followup.md` ACTION 15. OD-06 (B1b Thu 10-01) chooses B if the Inrad tolerance is not in by Wed 09-30, so send these on Mon 09-28. Quantities are stated for the first build of one unit (CR-006) with the early buy of plan OD-20 and decision 91 in view. **AT RISK (CR-006)** for the quantities only.

### 3.1 Inrad (International Radio), crystal filter #111

Send through the contact route on inrad.net (the research found no published email address; use the site's contact form or the address the site shows).

```
Subject: Quote request: #111 400 Hz 8-pole CW filter, 9010.6 kHz, technical data

Hello,

I am designing a 2 m CW handheld transceiver and would like to use your #111 crystal filter
(400 Hz, 9010.6 kHz, 8 poles) as the IF filter. Before I commit the design, could you
please send:

1. Price and availability for 1, 3 and 5 pieces, and the lead time if not in stock.
2. The -6 dB bandwidth tolerance: the guaranteed minimum and maximum, or the spread you
   see across production. My requirement is a -6 dB bandwidth of at least 400 Hz, so I
   need to know whether a unit can measure below 400 Hz.
3. The -60 dB bandwidth (or the guaranteed shape factor) and the ultimate attenuation.
4. The termination impedance at input and output (resistance and any parallel
   capacitance) that gives the specified passband and ripple.
5. Insertion loss and passband ripple at that termination.
6. A case drawing: outline, height, pin positions and pin functions, and mounting.
7. The operating temperature range.
8. Whether a measured response is supplied with each filter.

Thank you.

Best regards,
Robin Onsay
```

### 3.2 KVG Quartz Crystal Technology (info@kvg-gmbh.de)

```
Subject: Quote request: 9 MHz CW crystal filters XF-90S52-LF and a 400 to 600 Hz type, small quantity

Dear KVG team,

I am designing a 2 m CW handheld transceiver with a 9 MHz IF and would like a quotation
for small quantities of crystal filters:

1. XF-90S52-LF (9.000 MHz, 1.0 kHz at -6 dB, 500 ohm // 30 pF, case BF-01): price for 1, 3
   and 5 pieces, minimum order quantity and lead time.
2. A narrower CW type with a -6 dB bandwidth between 400 and 600 Hz at or near 9 MHz (for
   example a current equivalent of the former XF-9NB, 500 Hz, 8 poles): does one exist,
   and if so its type number, price for 1, 3 and 5 pieces, minimum order quantity and lead
   time; if only as a custom design, the engineering charge and minimum quantity.
3. For each type: the -6 dB bandwidth tolerance (minimum and maximum), the -60 dB
   bandwidth, insertion loss, ripple, termination impedance and the case drawing with pin
   positions.

Thank you for your help.

Kind regards,
Robin Onsay
```

### 3.3 Guerrilla RF (applications@guerrilla-rf.com), GRF5604 at 144 MHz

**Conflict to resolve before sending.** The SRR decision memo records the owner ruling on decision 58: "send the Guerrilla RF request anyway (decision 101)" (`docs/reviews/SRR/decision-memo.md` line 239). The PDR work plan limits the request to the case where P2 is revived (WP-PDR-04 output (b); OD-34), and OD-07 recommends closing the PA branch on P1 without Guerrilla RF. A plan cannot override an owner ruling. Recommendation: send it on Mon 09-28 as the ruling says. It is one email, its answer is the only route by which GRF5604 could return without a REQ-SYS-112 CR (TS-001 §8.3), and it does not delay OD-07. If you prefer the plan's text, say "withdraw the Guerrilla RF request" at B0 and it is recorded as your change to decision 58.

```
Subject: GRF5604 application question: tune for 144 to 148 MHz at 5 W

Hello Guerrilla RF applications team,

I am evaluating the GRF5604 as the power amplifier of a 5 W, 144 to 148 MHz (amateur
2 m band) CW handheld transceiver running from a 5 V rail. Your datasheet and selection
guide do not show a VHF tune. Could you please tell me:

1. Whether you have, or could share, a 144 to 148 MHz application tune (schematic and BOM).
2. Measured output power, gain and PAE at 5 W output in that band.
3. Measured harmonics at 2fo and 3fo at 5 W output, before any external low-pass filter.
4. The stage-2 dissipation at 5 W output, and the junction-to-base thermal resistance of
   stage 2; my design needs stage-2 dissipation at or below about 3.25 W.
5. The VCC transient tolerance (maximum VCC during turn-on and load changes).
6. Ruggedness into a mismatch of 10:1 VSWR at 5 W.

Thank you.

Best regards,
Robin Onsay
```

### 3.4 Recording

Forward each reply to Claude (paste it into the chat). Claude transcribes it into the dated status note and cites it in TS-001 (WP-PDR-19), the PA branch (WP-PDR-21) and the early-buy ADR (WP-PDR-38). If no reply by Wed 09-30, the OD-06 rule of plan §6.1 applies.

## 4. Downloads that need your browser or login (output c, and the related permissions)

Claude cannot reach these pages (bot walls or login). Nothing here is downloaded by Claude.

### 4.1 st.com items for the PA model (OD-18; pa-turnkey ACTION 14)

| Item | Page | Why |
|---|---|---|
| PD54008L-E ADS model (v1.0, 01 Aug 2015, ZIP; login required) | st.com product page for PD54008L-E | Fitting the behavioural LTspice PA model (WP-PDR-21; RSK-001) |
| STEVAL-TDR003V1 board schematics, bill of materials and Gerber files (v1.0, 01 Aug 2015) | st.com page for STEVAL-TDR003V1 | ST's own 5 W, 135 to 175 MHz reference with PD54008L-E as the final (followup F5) |
| DS6782 (STEVAL-TDR003V1 datasheet, v1.0, 31 Mar 2010) | same page | Measured system data at 5, 6 and 7.2 V |

**Where to put them.** The repository is public (github.com/robinonsay/cwht, MIT). Before placing the files in `docs/research/vendor/` (OD-18), check the licence terms shown on the st.com download page. If they permit redistribution, place them there and tell Claude; Claude records their SHA-256 values. If they do not (likely for the ADS model and the Gerbers), keep them outside the repository (for example `~/cwht-vendor/`), tell Claude the path, and Claude records them as owner-held items with SHA-256 values and uses them without committing them.

### 4.2 Other downloads and permissions asked at B0 or B1b

| Id | Item | Needed by | Plan row |
|---|---|---|---|
| D-1 | KDB 447498 D01 and KDB 643646 D01 (apps.fcc.gov) and the two VHF portable SAR reports named in `docs/research/rf-exposure-evaluation.md` (FCC IDs AZ489FT4948 and AZ489FT7098) | B0 Mon 09-28 | OD-39 (decision 35, RFX-A2) |
| D-2 | NASA-STD-8739.8, the SWEHB PAT-006 and PAT-007 checklists and the SWEHB PAT-071 PDR checklist (MS Word downloads) | B1b Thu 10-01 | OD-21 |
| D-3 | Permission for the emulator downloads (npm, git) and the rp2350js mirror fork | Permission at B0 Mon 09-28 | OD-25 |
| D-4 | SPLAT! install for the site link budget (optional; the Egli model is the fallback) | B0 Mon 09-28 | OD-39 (decision 82) |
| D-5 | PCM1808 breakout purchase, only if TS-001 keeps candidate B | B1b Thu 10-01 | OD-39 (decision 102) |

## 5. Dated stock checks for critical parts (output d; OD-39; RSK-038 S1)

Why: RSK-038 (Red) records zero DigiKey and Mouser stock for three rail parts on 2026-09-25 and machine access to several distributor pages refused (`power-tree-and-charging.md` F7, F19, F20; `display-and-ui-parts.md` F22; `tr-switch-candidates.md` Method 4). RSK-038 S1 asks for a dated check of every line against at least three times the build quantity. Check quantity: 9 (three times the three baselined units, ADR-025); **AT RISK (CR-006)**: 3 if CR-006 is approved (one unit). PD54008L-E is also checked against the 20-piece reserve plus 10 bench samples of decision 91.

For each row, open the DigiKey and the Mouser page and record: date, time and zone; stock; minimum order quantity; unit price at 1 and 10; lifecycle or status text (Active, NRND, Obsolete, Last time buy); factory lead time if stock is zero. A pasted table in chat is enough; a saved page PDF is better. Claude transcribes the figures into the status note and WP-PDR-38 puts them in the stock column of `hardware/bom/cwht-bom-prelim.csv`.

| Row | Part (MPN or family) | Maker | Function | Source of the candidate | Research observation (dated) |
|---|---|---|---|---|---|
| S-01 | PD54008L-E | ST | PA final (P1) | TS-001; SRR decision 58 | Mouser 3,430 and DigiKey 1,988 on 2026-09-25 (followup F8) |
| S-02 | PD55015-E and PD55008-E | ST | PA fallback candidates P3, P4 | TS-001 §8.3 | not checked |
| S-03 | GRF5604 | Guerrilla RF | P2, only if revived; bench samples of decision 91 | followup F14 | Mouser 7,409 on 2026-09-25 (followup F14) |
| S-04 | GVA-84+ and PGA-103+ | Mini-Circuits | PA driver candidates | followup F20 | not checked |
| S-05 | Si5351A-B-GT | Skyworks | synthesizer candidate | ADR-013; concept §7.4 | DigiKey stock recorded 2026-09-25 (technology assessment §3.1) |
| S-06 | LMX2571 | TI | synthesizer candidate | ADR-013; concept §7.4 | DigiKey stock recorded 2026-09-25 (technology assessment §3.1) |
| S-07 | BQ25887 | TI | 2S charger | SRR decision 70 | DigiKey 10,972 (power-tree F5) |
| S-08 | S-8252 series (variant chosen in WP-PDR-24) | ABLIC | cell protector | SRR decision 72 | not checked |
| S-09 | BQ29209 | TI | secondary over-voltage protector | SRR decision 72 | not checked |
| S-10 | TPS62913 | TI | buck regulator | power-tree F19 | zero DigiKey and Mouser stock 2026-09-25 |
| S-11 | TPS7A2033 | TI | LDO | power-tree F20 | zero DigiKey and Mouser stock 2026-09-25 |
| S-12 | 1043P | Keystone | 18650 holder (2 per unit; you solder it) | SRR decision 73 | Mouser 10,041 on 2026-09-25 (power-tree F13) |
| S-13 | HF3 54, 1-1462051-7 | TE Connectivity | T/R relay, 6 V coil | ADR-026 scope; tr-switch F7 | TE store "not currently available", distributors unknown |
| S-14 | ARS14A4H | Panasonic | alternate T/R relay | tr-switch F8 | not checked |
| S-15 | 74LVC1G123 | several | hardware PA-enable cutoff monostable | technology assessment §3.6 | not checked |
| S-16 | LS013B7DH03 | Sharp | display panel | display F22 | DigiKey 5300387 listed; stock not readable |
| S-17 | 505110-1092 (Molex) or FH12-10S-0.5SH(55) (Hirose) | Molex, Hirose | display ZIF | display baseline table | listed; stock not readable |
| S-18 | PEC11R-4215F-S0024 | Bourns | encoders (2 per unit) | display baseline table | DigiKey 3,229 (undated snippet, Low) |
| S-19 | SJ1-3535N | Same Sky | key and headphone jacks (2 per unit) | display F17 | not readable |
| S-20 | B3F-1052 | Omron | push buttons (2 per unit) | display baseline table | not checked |
| S-21 | SC1631 (Pico 2, no headers) | Raspberry Pi | controller module | ADR-004; pcbway-fab F16 | not checked |
| S-22 | TPA6132A2 (TPA6130A2 alternate) | TI | headphone amplifier | audio and display trade (ADR-006 scope) | not checked |
| S-23 | PCM1808 | TI | I2S ADC, only if TS-001 keeps B | cw-selectivity implication 9 | TI store out of stock 2026-09-25 |

The Inrad and KVG filters are quote-only and are covered by section 3. The TCXO, LNA, SMA jack and remaining passives are not yet chosen; WP-PDR-38 adds them to the CDR check.

## 6. PDR equipment list, draft (output e; OD-26, OD-19, OD-22, OD-32)

This list is reviewed inside WP-PDR-43 (V&V plan). Answers are needed at B0 Mon 09-28 (OD-26); purchases are needed only by the dates in the last column. For each row, answer **own** (make and model), **borrow** (from whom), **buy** or **decline**. Instruments whose readings are cited as evidence need a tool validation (TV) record before their first credited use (05 §9; charter §8).

| Row | Item | Purpose (case, requirement) | Minimum specification | Recommendation | Needed by | TV record |
|---|---|---|---|---|---|---|
| E-01 | **Near-field H-field probe set for the tinySA Ultra** | Option C shielding measurement (bare board against board in the coated case), leak location at seams and openings, near-field survey of the buck, charger and Pico 2 clock harmonics (CR-003 §5 step 19; status note §3 row 8; REQ-SYS-177, TC-SYS-107 supporting data) | Shielded magnetic loop probes, at least two loop sizes (about 3 to 10 mm and about 20 to 30 mm), SMA male output, usable from about 1 MHz to at least 1.5 GHz; a short SMA cable. No preamplifier is bought until the TV record shows the tinySA noise floor is too high. Keep the probe away from the antenna port and PA while keying; start with the tinySA's internal attenuation at maximum | **Buy.** Owner purchase recommended in CR-003 §5 step 19; you have used the method before (status note §2). Choose from the low-cost multi-probe sets sold for tinySA and NanoVNA users or an instrument-grade set; Claude compares specific sets on request, and the price goes into the WP-PDR-46 instrument line | Before the option C shielding measurement (before TRR) | Yes: relative-measurement TV (repeatability of a fixed probe position on a known emitter), planned by WP-PDR-43 |
| E-02 | Thermocouple and reader | Surface temperature of REQ-SYS-113 (48 C, your limit) and the PA heatsink for HZ-003 K1 and K7 (OQ-VV-003; CR-003 §5 step 19) | K-type bead thermocouple with polyimide tape; a multimeter with a thermocouple input, or a stand-alone K-type thermometer whose datasheet states its accuracy from 20 to 80 C. An infrared thermometer is not a substitute on coated or metal surfaces (emissivity) | **Buy** unless your multimeter has a thermocouple input (answer E-03 first) | Before the option C thermal acceptance (before TRR) | Yes (makes the thermal case credit-bearing, 04 §6.3 OQ-VV-003) |
| E-03 | Multimeter: make, model, ranges, datasheet | Every DC, AC and current reading in the Bench cases; OQ-VV-003 | True-RMS AC range; DC current range down to tens of microamps (TC-SYS-070 off-state current at most 50 uA) | **Answer** make and model; Claude reads the datasheet | Answer at B0 | Yes |
| E-04 | Calipers | Dimension cases (OQ-VV-002; MOP-002 envelope, TPM-016) | 150 mm digital, 0.01 mm resolution | **Answer** own or buy | Answer at B0; before TRR | No (04 §6.1 calipers row) |
| E-05 | Scale | Mass case TC-SYS-071 (REQ-SYS-102, 350 g) | Kitchen or postal scale, 1 g resolution, 500 g capacity or more | **Answer** own or buy | Answer at B0; before TRR | No |
| E-06 | **2 m source of 5 W or more for TC-SYS-025** **AT RISK (CR-006)** | +27 dBm receiver survival at the antenna port (REQ-SYS-037), CR-006 §12 Q6 | A 2 m transmitter whose lowest setting of 5 W or more is at most 10 W, sending a steady carrier (CW, or FM with no audio); its own antenna removed; never over the air | **Answer** Q6: own or borrow; make, model and the setting. An ordinary FM handheld at 5 W is enough | Answer at B0 (with OD-03); in hand before the stress group after TRR | No (it is a characterized fixture, measured with the diode probe each run) |
| E-07 | **Pads for TC-SYS-025** **AT RISK (CR-006)** | Deliver +27 to +28 dBm from E-06 into the antenna port | Attenuation 9 dB or more, rated 10 W or more and at least the source's set power; for a 5 W source a 10 dB pad; for an 8 W source add a 2 dB pad rated to the same rule (11 to 12 dB total); SMA or BNC with adapters; characterized on the NanoVNA | **Buy** (unless owned) | Before the stress group after TRR | No (fixture, NanoVNA-characterized in the run) |
| E-08 | Dummy load power rating | Termination for every transmit test and the E-06 power check | Rated at least the source's set power (E-06) and at least 5 W continuous for the unit | **Answer** the rating of your BNC dummy load (SI-013) | Answer at B0 | No |
| E-09 | **Second 2 m CW station for MOE-001 and MOE-002** **AT RISK (CR-006)** | On-air range validation with a matched second station (CR-006 §12 Q5; MOE-001 as proposed) | A licensed friend's 2 m transceiver that sends and receives CW and can be set within 1 dB of the unit's 5 W, 2 W and 0.5 W steps (directly or through a pad of measured loss) | **Answer** Q5: whose station and which rig; if none can be matched, MOE-001 and MOE-002 stay open at SAR as a lien | Answer at B0 (with OD-03); used after the on-air TRR-Dn | No (its power is measured on your bench by the MOP-004 method) |
| E-10 | Reference antennas, two specimens each **AT RISK (CR-006)** | Range MOEs (SRR decision 81), with the second specimen for the matched station | Signal Stick quarter-wave with a 48 cm counterpoise (pocket), and MFJ-1714S or Diamond SRH770 (range); two of each. None is purchased yet (concept §13) | **Buy** before the on-air series | Before the first on-air TRR-Dn | No |
| E-11 | Weak-signal source for MOE-010 | The bench part of MOE-010 (-137 dBm and -130 dBm with a -60 dBm signal at +/-2 kHz); RID-SRR-011 | A calibrated level source is not in the bench; the tinySA generator is not a level reference under ADR-021 | **Accept Analysis** for the bench part (MOP-006, MOP-007), with the on-air part standing. Alternatives: borrow a calibrated signal generator, or the tinySA generator through a measured step attenuator in a shielded setup, which needs a superseding ADR and a TV record | Decision at B0 (closes the OQ-VV question of RID-SRR-011 before PDR readiness) | Only for the alternatives |
| E-12 | Second Pico 2, sigrok-cli and sigrok-pico firmware (D-VER-2) | Bench keyer timing and sequencing cases (TC-SW-KEYER Bench cases; ADR-009) | One Pico 2; `sigrok-cli` installed on the Mac by you (it is not installed, `tools/toolchain.lock.md`); sigrok-pico `pico2_*.uf2` | For the PDR bounce capture, the development-board GPIO route (OD-19, credit false) is recommended; the logic capture is still needed before TRR. **Buy** the Pico 2 (about USD 5, SC1631); decide the sigrok-cli install by CDR | Pico 2 before CDR; install decision by CDR | Yes (due TRR, with sigrok-cli) |
| E-13 | 3.3 V USB-to-UART adapter, or a second Pico 2 as a UART bridge | UART trace on the unit's test pads (04 §6 row; TC-SYS-005, 082, 108 to 110) | 3.3 V logic levels; model recorded | **Use the E-12 Pico 2 as the bridge** (no purchase) unless you own an adapter | Before TRR | Yes |
| E-14 | tinySA Ultra with a calibrated 30 to 40 dB attenuator rated 10 W or more | All emission cases (SI-034, ADR-021; OQ-VV-001) | As ADR-021; the attenuator is not in the bench inventory (concept §13) | **Confirm** whether the tinySA is ordered or in hand, and buy the attenuator | Before the emission TRR | Yes (receipt inspection plus TV, OQ-VV-001) |
| E-15 | Hand-assembly bench: temperature-controlled station with stand and auto-sleep, fume extractor, eye protection | Your through-hole assembly (OQ-SAF-019; HZ-015 K1, K2, K4, K5; REQ-SYS-138) | As listed | **Confirm** (OD-32) | Answer by B1b Thu 10-01 | No |
| E-16 | Your straight key and paddle: make and model | Bounce capture for the debounce TBRs of REQ-SYS-048 and REQ-SYS-162; ICD-CTL-KEY (OA-6, C-209) | Standard 3.5 mm TRS plugs (SI-034) | **Name them** (OD-22) | B0 Mon 09-28 | No |
| E-17 | PCM1808 breakout | PIO I2S loopback, only if TS-001 keeps candidate B (decision 102) | As the research | Only if B | B1b Thu 10-01 | No (credit false) |

Fixtures Claude designs and you build from parts later (no decision now): the diode RF probe on the dummy load, the Pico keying fixture, the audio load fixture and the 2:1 mismatch fixtures (04 §6; `docs/vv/fixtures/`, planned). Their parts lists come with WP-PDR-43.

## 7. Regulatory corpus additions (output f; OD-24a; OQ-SAF-024, C-062)

The corpus (`docs/references/md/regulatory/`, eCFR issue 2026-09-23) lacks the items below. The CFR text rows are fetched by Claude from the eCFR versioner API with the README command pattern once you approve them (OD-24a, B1b Thu 10-01); the table-image rows need your browser, because the 2.106 table body is published as images (README "Known limitation").

| Row | Item | Why | Who does what | Needed by |
|---|---|---|---|---|
| R-1 | 47 CFR 2.106 Table of Frequency Allocations rows covering 150.8 to 174 MHz, with their footnotes | OQ-SAF-024 (HZ-008 C7): the VHF public-safety and maritime services that an out-of-band fundamental would hit, cited verbatim | **You:** open the eCFR reader page for 47 CFR 2.106, find the page images covering 150.8 to 174 MHz, and send Claude screenshots. **Claude:** transcribes them into `47cfr-2.106-150-174mhz.md` with the footnotes fetched as text | B1b Thu 10-01 (final call B3 Sun 10-04) |
| R-2 | The Part 80 rule that designates 156.800 MHz for distress, safety and calling | OQ-SAF-024 | **Claude**, after OD-24a: finds the section by an eCFR search for "156.800" and fetches it as text; you approve | same |
| R-3 | 47 CFR 2.803 (marketing), with the amendment published at 91 FR 57800 (2026-09-11), which the 2026-09-23 issue text did not yet carry | The 15.23 five-unit reading behind ADR-025 and CR-006, and the build-quantity ADR (`pcbway-export-and-vendor-questions.md` F21, open item 8; plan C-149) | **Claude**, after OD-24a: fetches the current 2.803 text and the Federal Register document | same |
| R-4 | Browser check of the five harmonic rows of `47cfr-2.106-harmonic-bands.md` (DECISION-10) | Those rows are Medium confidence until checked against the current page images (RSK-029) | **You:** view the five rows on the eCFR page images and send screenshots; **Claude** compares and records | B0 Mon 09-28 (OD-39) |
| R-5 | Any clause the WP-PDR-34 citation-resolution table (`docs/requirements/tx/regulatory-citations.md`) finds unresolved | E-12 second clause of the PDR entrance criteria | **Claude** lists them; you approve each | B3 Sun 10-04 |

## 8. Owner decisions and actions with needed-by dates (output g; plan §6.1)

The recommendation and source of each row are those of plan §6.1; this table only orders them by session. "Given" marks what you already answered on 2026-09-27 (status note §2 and §4); those are not asked again.

### 8.1 Already given on 2026-09-27

| Id | Subject | Your answer (status note) |
|---|---|---|
| OD-01 | PDR moved to about Thu 10-08; readiness Tue 10-06; CDR about 10-14 to 10-15 | Approved (§4, "That sounds good to me. I think this is a good plan.") |
| OD-33 | Environment set for the PETG case: 1.0 m drop, IPX2, +60 C storage (48 C is your own limit) | Concurred (§4) |
| OD-38 (preliminary) | You print option C on the H2C in PETG with the legend and jack markings in relief; PCBWay engraving only on the CNC fallback | Concurred (§4); so no PCBWay print quote is in section 2. Final at B1b with TS-011 |

### 8.2 B0, Mon 09-28

| Id | Ask | Recommendation | Material |
|---|---|---|---|
| OD-02 | Disposition CR-003 revision 3 (Class I), answering §12 Q1 to Q3 | Approve as Class I; Q1 yes (12 mm test finger TBR, guarded heatsink); Q2 accept the §5 Effectivity item 3 acceptance set, CNC ordered when a failed item cannot be fixed by one reprint or one coating change; Q3 yes | Section 1; CR-003 §6.4, §12 |
| OD-03 | Disposition CR-006 revision 2 (Class I), answering §12 Q1 to Q8 | Q1 approve; Q2 1 assembled, 2 priced; Q3 option (a), tested by the PDR quotes; Q4 at SAR by ADR; Q5 and Q6 your facts (E-09, E-06); Q7 accept; Q8 yes | Section 1; CR-006 §6.3, §12 |
| OD-18 | st.com downloads | Download; placement per the licence | 4.1 |
| OD-19 | Bounce capture route | Development-board GPIO sampling (credit false) | 6 (E-12) |
| OD-22 | Name the straight key and paddle (OA-6) | Name them now; HSI verdict at B3 | 6 (E-16) |
| OD-24b | Accredit TV-014 (LTspice batch wrapper) on its record | Accredit on the record's recommendation | WP-PDR-07 record |
| OD-25 | Permit the emulator downloads (npm, git) | Permit; the emulator decision follows at B2 | 4.2 (D-3) |
| OD-26 | Instrument answers: calipers, scale, multimeter, thermocouple, weak-signal source, near-field probe, 2 m source, second station | Answer; buy the probe; accept Analysis for MOE-010 | 6 |
| OD-34 | Send the Inrad and KVG quote requests (and Guerrilla RF, section 3.3) | Send Mon 09-28 | 3 |
| OD-39 | KDB and SAR downloads, the 2.106 browser check, SPLAT! (optional) | Permit the downloads; SPLAT! optional | 4.2, 7 (R-4) |

### 8.3 Tue 09-29 (PCBWay deadline) and B1a

| Id | Ask | Recommendation | Material |
|---|---|---|---|
| OD-04 | Send the PCBWay email and run the instant quotes | Send by Tue 09-29 10:00 your time | 2 |
| OD-39 | Dated stock checks where the pages need your browser or login | Run the section 5 list | 5 |
| OD-02, OD-03 | CR dispositions, if not given at B0 | As 8.2 | Section 1 |
| OD-10 (first five) | TS-007 synthesizer, TS-008 T/R relay, TS-009 battery and charger, TS-005 USB, TS-010 audio and display | Decide each on its study's recommendation, only on an APPROVED section B record and SA pair (rule C9) | The trade studies |
| OD-12 | Measure the Pico 2 VBUS path at 0.5, 1.0 and 1.5 A (optional) | Optional; 500 mA stands if unmeasured | WP-PDR-24 |
| OD-17 | Dated record of the OPS-B controlled-environment basis | Give it in chat | WP-PDR-30 |
| OD-36 | Disposition CR-007 (05 Table 4-2 admission rows and 05 SRR liens), after its §6 review | Approve | CR-007 |

### 8.4 B1b, Thu 10-01

| Id | Ask | Recommendation |
|---|---|---|
| OD-06 | TS-001 selectivity A (Inrad #111) or B; confirm P1 and the P3, P4 order | If the Inrad tolerance is not in by Wed 09-30, choose B, or accept A with the REQ-SYS-024 CR risk named (PCR-9) |
| OD-07 | Close the PA branch on P1 without Guerrilla RF, or keep GRF5604 open (REQ-SYS-112 CR to at least 125 C) | Close on P1 |
| OD-10 (rest) | TS-003 PA, TS-006 ALC and cutoff node, SWR fold-back, TS-011 enclosure, TS-004 board | Each on its study's recommendation (rule C9) |
| OD-13 | Secure boot | Off (irreversible) |
| OD-14 | rustos pinning method | Path dependency plus recorded commit |
| OD-15 | Host channel for Rev A | CR to the UART pads (PCR-7) for Rev A, USB CDC at Rev B; PCR-7 disposition at B2 |
| OD-16 | Kani; register-access trait for `pico2` | Kani for the SW-KEYER and SW-TXSEQ invariants (non-credit); trait for safety-critical drivers only |
| OD-21 | NASA-STD-8739.8, PAT-006, PAT-007, PAT-071 downloads | Permit |
| OD-23 | As rustos maintainer, merge WP-SW-11, 01, 09, 02, 03 by Thu 10-01 and the WP-SW-08 ICD page by Fri 10-02; commit L-016-6 | As stated |
| OD-24a | Corpus additions R-1 to R-3 | Approve |
| OD-32 | Hand-assembly bench equipment (E-15) | Confirm |
| OD-38 (final) | Option C maker and markings, with TS-011 | (a), as given preliminarily |
| OD-39 | PCM1808 breakout, only if B | Only if B |

### 8.5 B2 Fri 10-02 to PDR Thu 10-08

| Id | Ask | Session |
|---|---|---|
| OD-09 | Rule every TBR value (batch 1), on APPROVED analysis records (rule C10) | B2 Fri 10-02 |
| OD-25 | Emulator decision: ACC-EMU-001 candidate, Renode or the RSK-003 fallback | B2 Fri 10-02 |
| OD-37 | Dispositions of PCR-2, PCR-3, PCR-7, PCR-8 and any PCR-9 | B2 Fri 10-02 |
| OD-05 | As SMA TA, the HZ-002 and HZ-007 residual with a PETG case | B3 Sun 10-04 |
| OD-08 | TPM definitions (SE-40) | B3 Sun 10-04 |
| OD-09 | TBR values batch 2 | B3 Sun 10-04 |
| OD-22 | Keyer HSI verdict and mockup evaluation (bench session Sat 10-03) | B3 Sun 10-04 |
| OD-24b | TV records cited by F1 products | B3 Sun 10-04 |
| OD-31 | Charter edits drafted by WP-PDR-13 and WP-PDR-17 | B3 Sun 10-04 |
| OD-35 | As SMA TA, concurrence in the re-run safety-critical determination | B3 Sun 10-04 |
| OD-37 | Dispositions of PCR-5, PCR-6 and the remaining PCR-9 | B3 Sun 10-04 |
| OD-11 | Close the Verified SRR log items; verify RFA-SRR-008 | B4 Tue 10-06 |
| OD-27 | Merge approvals closing CR-001, 002, 004, 005; TC-SW-TOOL-001 run 6; ACC-COMPLEXITY-001 and ACC-TREND-001 | B4 Tue 10-06 |
| OD-28 | Configure the SSH tag-signing key (C-092); review the GitHub bypass report of the `baseline/srr` push (C-091) | B4 Tue 10-06 |
| OD-29 | PDR readiness; Soft-row liens; any Red review-trend zone | B4 Tue 10-06 |
| OD-09 | Any re-ruling after a later Major | B4 Tue 10-06 at the latest |
| OD-20 | Early buy of the PD54008L-E reserve and bench samples, Inrad if A, zero-stock rail parts, heatsink, by the early-buy ADR | PDR session Thu 10-08 |
| OD-30 | At the review: RFAs and RIDs, tailoring, re-approvals, Red-risk plans, residual risks, waivers, allocated-baseline content, disposition | PDR session Thu 10-08 |

## 9. Reply format and what changes if a CR disposition changes

**Reply format.** Answer in chat, one line per id, in any order, for example: "OD-19: dev board. OD-22: straight key <make model>, paddle <make model>. E-03: <multimeter make model>. E-06: own <rig>, lowest setting 5 W. Stock S-10: DigiKey 0, Mouser 12, 2026-09-28 09:40 CDT." Claude transcribes the words verbatim into `docs/plan/status/status-2026-09-28.md` §2, writes its reading in §3 for you to correct, and routes each answer to the WP that consumes it.

**If a disposition differs from the proposed text.**

| Change | Effect on this pack |
|---|---|
| CR-006 rejected (three units stay baselined) | PCBWay: a follow-up asking for 3 assembled is sent (section 2.2 item 5); stock check quantity stays 9; E-06, E-07 and E-09 revert to the second-unit setups of the baseline, and TC-SYS-025 stays Blocked until a second unit exists |
| CR-006 Q2 answered "2 assembled" | No re-send: row A-03 and A-04 already price it |
| CR-003 rejected (CNC enclosure stays the delivered route) | Part B becomes the primary enclosure request; E-01 is still recommended (the owner's shielding method applies to any enclosure) |
| OD-38 final is (b) or (c) | A PCBWay 3D-print or engraving quote for the printed case is drafted after B1b; it misses the closure and is answered from 10-05 |

## 10. Traceability

| WP-PDR-04 output | Section | Closes or enables |
|---|---|---|
| (a) PCBWay email and instant-quote set | 2 | C-207 (OA-4, owner performs); OD-04; A-PCB-01, 06, 09; A-UI-06; pa-turnkey ACTION 17; CR-006 §12 Q2, Q8 quote items; RSK-052 S1 input |
| (b) Inrad, KVG and Guerrilla RF requests | 3 | C-208 (OA-5, owner performs); OD-34; TS-001 §6 item 5; cw-selectivity ACTION 15; pa-turnkey ACTION 15 |
| (c) st.com download list | 4.1 | OD-18; pa-turnkey ACTION 14 |
| (d) dated stock-check list | 5 | OD-39 stock checks; RSK-038 S1 input; WP-PDR-38 stock column |
| (e) PDR equipment list draft | 6 | C-209 (OA-6) and C-210 (OQ-VV-002) prompts; C-061 equipment confirmation (OQ-SAF-019); OD-26, OD-19, OD-22, OD-32; CR-003 §5 step 19; CR-006 §12 Q5, Q6 and its §4 equipment list items; OQ-VV-003; RID-SRR-011 source question |
| (f) regulatory corpus additions | 7 | C-062 (OQ-SAF-024 corpus rows); OD-24a; DECISION-10 check (OD-39) |
| (g) owner decision list | 8 | Plan §6.1 OD-01 to OD-39 ordered by session; C-091 and C-092 prompts (OD-28) |
