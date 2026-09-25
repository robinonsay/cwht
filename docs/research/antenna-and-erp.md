# Antennas, connector and ERP for cwht: 2 m handheld whips, exposure ERP and the simplex link budget

**Assignment key:** antenna-erp
**Author:** Claude (research subagent), 2026-09-25
**Status:** research input for SRR; not a baseline. Candidate requirements, MOEs and risks are proposals for the requirements owner.
**Relation to prior reports:** extends `part97-regulatory-basis.md` F6 to F8 (the exposure tables there assume a 0 dBd whip; this report supplies measured handheld antenna gains and the resulting ERP per power step), uses the receiver noise-figure and MDS candidates of `2m-cw-transceiver-reference-designs.md` F14 as link-budget inputs, and hands `enclosure-cnc-and-openscad-pipeline.md` the connector mounting constraints. Nothing in those reports is repeated except the few numbers needed to make the tables here self-contained.

Conventions used throughout: dBd is gain relative to a half-wave dipole in free space; dBi = dBd + 2.15 dB. ERP = transmitter power at the connector x antenna gain (dBd, linear); EIRP = ERP x 1.64. A manufacturer's "2.15 dBi" claim is therefore a claim of 0 dBd, i.e. dipole-equivalent radiation. Frequency for all derived numbers is 146.0 MHz (wavelength 2.053 m; quarter wave 51.3 cm; half wave 102.7 cm; 5/8 wave 128.3 cm) unless stated.

## 1. Question

For a 5 W, 144 to 148 MHz, A1A handheld in a CNC-machined aluminum enclosure with the antenna on one end (SI-001, SI-003, SI-008):

1. Which 2 m handheld antennas are realistic candidates (Nagoya NA-771, Diamond SRH77CA, Diamond RH-771, Signal Stick, Smiley, a quarter-wave telescopic, a rubber duck) and what are their published and, where they exist, measured gain, efficiency and SWR on a handheld with and without a counterpoise? Which published gains are marketing rather than measurement?
2. Which connector convention (SMA jack on the radio, SMA plug on the radio, or BNC) do the major radios follow and which antennas ship with which connector?
3. What mechanical load does a whip put on the connector of a machined enclosure and how should it be strain-relieved?
4. How do chassis-as-counterpoise practice and the operator's hand and body change radiated power?
5. What ERP range results for 5 W and for each lower power step, for the RF-exposure evaluation (RFX-01 of the regulatory report)?
6. What are the simplex link-budget inputs for two HTs at 1.5 m over open ground and for a hilltop case, to inform the range MOE?
7. Which connector and which reference antenna should the SRR package carry?

## 2. Method

**Web fetches (2026-09-25).** Primary and measurement sources fetched and read in full or in the cited part:

- hamradio.me (John Huggins, KX4O): "HT Antenna Comparisons" (updated 2018-10-21, republished 2021-01-01) and "EFHW HT Antenna Functions Without Additional Counterpoise" (2018-09-14): chamber EIRP measurements of a Yaesu FT1D with a laboratory reference dipole.
- G4ILO's Blog (Julian Moss), "2m HT antenna shootout", 2011-04-23 (also mirrored at amateurradio.com): relative field-strength readings for twelve 2 m HT antennas.
- K0NR blog (Bob Witte), "K0DK: High-Efficiency HT Antennas", 2006-07-01, summarizing Dick Kiefer K0DK's measurements.
- WD8RIF (William McFadden), "Improving 2-Meter HT Performance in Pedestrian-Mobile Applications" (PDF, sources updated 2018-06-16); KE4SKY (C. Edward Harris), "Getting the Most from Your Hand-Held Transceiver" (qsl.net/n7fan mirror, 1998/1999, updated 2009-05-09), the origin of the often-quoted NBS "rubber duck is 5 dB down" figure.
- SoftWright LLC, "Measured Building and Body Losses: Fourth Annual User's Engineering Seminar" (1999): field measurements of a handheld at 146.52 MHz by body position.
- ECC Report 286, "Body effect of handheld and body worn audio PMSE equipment", 2018-09-28 (docdb.cept.org/download/1361), for the effect of the hand.
- IEEE Xplore abstracts 6178645 and 6565753 (push-to-talk transceiver antenna near the head, VHF/UHF) via search snippets only; the abstract pages returned HTTP 418.
- Manufacturer pages: Diamond Antenna Japan RH series and SRH series specification tables (diamond-ant.co.jp); BTECH/Baofeng Tech NA-771 page; Signal Stuff Signal Stick SMA-M and BNC pages and "Choosing the correct antenna connector for your radio" (2016-08); Smiley Antenna 5/8 Slim Duck 2 Meter page; MFJ MFJ-1714 and MFJ-1714S pages; retailer listings for MFJ-1712 and Nagoya NA-773; Yaesu FT-60R brochure PDF; Ham Radio School (K0NR), "What's That Connector on My HT?" (2021-10-02).
- Connector data: Amphenol RF Europe brass SMA catalog (2006, via RS Components PDF; its text is font-garbled and was decoded with a verified character mapping, see below); AEP SMA catalog hosted at radiall.com (MIL-PRF-39012 class stainless SMA); TEJTE "SMA Connector Dimensions" guide (secondary). amphenolrf.com, digikey.com, mouser.com, newark.com, jameco.com, tti.com, molex.com and te.com all returned HTTP 403 or no response to both WebFetch and curl with a browser user agent, so the Amphenol torque FAQ and the BNC 31-221 datasheet could not be read (Open item 1).
- Standards: ITU-R P.372-13 (09/2016) Table 1 and Table 2 (man-made noise; the P.372-17 URL returned 404); ITU-R F.339-8 (02/2013) Table 1 (required S/N for A1A aural reception); TIA TSB-88.2-E (2016) was scanned for portable body-loss guidance and contains none; Wikipedia articles for the two-ray ground-reflection model and the Egli model (formula check only); Mardeni and Kwan, PIER C vol. 13, 2010, for the Egli equations with the below-10 m mobile-height term; repeater-builder.com "A Quick Overview of the Radio Horizon" (WA6ILQ) for the 4.124 sqrt(h) horizon formula.
- Counterfeits: KB6NU "How to tell if you have a fake Nagoya antenna" (2018-06-06, with 2025 comments); RadioReference threads.

The KX4O page was fetched twice: the first read produced a summary that paraphrased the hand effect and read the MFJ-1714 plot; the second read, prompted for verbatim sentences, returned the quotations used in F2 and F4 and corrected the paraphrase (the hand reduced the stock antenna's EIRP by 3 to 4 dB; it did not "improve" it).

**Local commands.** `curl` and `pdftotext -layout` (Homebrew) in the session scratch directory for the PDFs above; `python3` for every derived number (script `calc.py`, kept in scratch; its output tables are reproduced in F9 to F11 and E of F8). The Amphenol RF Europe PDF text came out as a symbol-font substitution; the mapping `ASCII = 0x120 - code` was verified on the strings "SMA Coaxial Connectors", "RG-58" and "0-12.4 GHz" before use. Nothing was written to the repository except this report.

**Limits.** The session's web-search budget ran out after the connector and range searches; the last confirmations (Signal Stick mass from the maker, Diamond SRH77CA mass, distributor stock and price observations) could not be made and are listed as Open items. No antenna was measured by this agent; all gain numbers are other people's measurements or manufacturers' claims, tagged as such.

## 3. Findings

### F1. The candidate antennas: published physical and electrical data

| Antenna | Electrical type on 2 m | Length | Mass | Connector(s) as sold | Rated power | Manufacturer gain claim | Manufacturer SWR claim | Source |
|---|---|---|---|---|---|---|---|---|
| Nagoya NA-771 (REUEX Industrial, Taiwan; US importer BTECH) | dual-band loaded whip ("precision-engineered loading coil"), 144/430 MHz | 39.6 cm (15.6 in) | 1.41 oz (40 g) | SMA-F standard; SMA-M version sold "for Yaesu, Vertex, Kenwood, Icom"; BNC versions appear on eBay (unverified) | 10 W | "2.15 dBi" (BTECH page: "2.15-3 dBi", "up to 3 dBi") | VSWR <= 1.5 | baofengtech.com/product/nagoya-na-771/ ; batteriesamerica.com NA-771 SMA-male listing |
| Diamond SRH771 (Japan) / SRH77CA (US catalog, RF Parts) | 1/4 wave (144 MHz), 1/2 wave (430 MHz) | 40 cm (US listings: 15 in or 15.6 in) | 38 g (SRH771, Diamond JP) ; SRH77CA mass not published | SMA-P (male) | 10 W FM | "2.15 dBi (430 MHz)" (Diamond JP gives no 144 MHz gain) ; US listings add "+6 dB relative gain" with no stated reference (marketing) | none | diamond-ant.co.jp SRH table ; theantennafarm.com SRH77CA ($29.95 listed) |
| Diamond RH771 (Japan) / RH77CA (US) | 1/4 wave (144 MHz), 1/2 wave radialless (430 MHz) | 40 cm | 42 g | BNC-P (male) | 10 W FM | "2.15 dBi (430 MHz)" | none | diamond-ant.co.jp RH table |
| Diamond RH770 / SRH770 | 1/2 wave radialless (144 MHz), 2 x 5/8 wave radialless (430 MHz), telescopic | 93 cm extended, 22.3 cm retracted, 10 stages (SRH770: 91 cm) | 85 g | RH770 BNC-P ; SRH770 SMA-P | 20 W FM | "3.0 dB (144 MHz), 5.5 dB (430 MHz)", reference not stated | none | diamond-ant.co.jp RH and SRH tables |
| Diamond RH205 | 5/8 wave at full length, 1/4 wave retracted, telescopic, 2 m only | 134 cm extended, 23 cm retracted, 10 stages | 90 g | BNC-P | not stated on JP page | none on JP page; a US retailer listing claims "9.0 dB" (implausible, unverified) | none | diamond-ant.co.jp RH table ; gigaparts.com RH205 |
| Signal Stuff Super-Elastic Signal Stick | 1/4 wave (144 to 148 MHz), 3/4 wave (420 to 450 MHz); Nitinol (NiTi) wire | "approximately 19 in" (48 cm) | not stated by maker; a retailer lists 18 g and a 2019 review says "half the weight of the NA-771" (about 18 to 20 g, Low) | SMA-M, SMA-F, BNC (three products) | 50 W at 100 % duty, 100 W at 50 % duty | none ("gain should be similar on any antenna with a similar length") | "as low as 1.3:1 at 146 MHz, 1.5:1 at 440 MHz" | signalstuff.com/products/st-sma-m/ and st-bnc/ ; stackunderflow.com review 2019-01-10 |
| Smiley Antenna 5/8 Slim Duck 2 Meter (USA) | helical, "5/8 wave" electrical, base-loaded, tuned 146.25 MHz, +/-5 MHz | 10.5 in (26.7 cm) incl. 0.5 in base | not stated | SMA-M, SMA-F, BNC, TNC, MX, RP-SMA, NMO, others | 50 W | "6 dBd gain" (physically implausible for a 0.13 wavelength radiator; marketing) | "low SWR at band center" | smileyantenna.com 5/8 Slim Duck page |
| MFJ-1714 / MFJ-1714S "Long Ranger" | end-fed 1/2 wave, telescopic, 2 m only | 40 in (102 cm) extended; about 10.5 in collapsed (Low: listings disagree) | not stated | 1714 BNC ; 1714S SMA-M | 5 W (retailer listing; Low) | "outperforms a 5/8 wave on an HT" (unquantified) | none | mfjenterprises.com/products/mfj-1714s ($19.95, out of stock 2026-09-25) ; moonrakeronline.com MFJ-1714 |
| MFJ-1712 / 1712S / 1712SF | telescopic 1/4 wave (2 m), 5/8 wave (440 MHz) | 19 in (48 cm) extended, 7.25 in collapsed | not stated | 1712 BNC ; 1712S SMA-M ; 1712SF SMA-F | not stated | none | none | dxengineering.com and gigaparts.com listings |
| Nagoya NA-773 | telescopic dual-band | 12.5 cm to 42 cm | not stated | BNC (and SMA variants) | not stated | "2.15 dB" | none | hobbywireless.com listing |
| Stock rubber duck (e.g. Yaesu FT1D supplied antenna) | normal-mode helix, "4 % to 15 % of a wavelength long" (8 to 31 cm at 2 m) | radio-specific | radio-specific | matches the radio | radio-specific | none | none | Fujimoto, Mobile Antenna Systems Handbook 2nd ed. p. 419 via Wikipedia "Rubber ducky antenna" |

Reading the table: every "2.15 dBi" or "2.15 dB" entry is a claim of dipole-equivalent gain; none of the manufacturers states a measurement condition (chassis, hand, counterpoise, distance) and F2 shows the measured values on a handheld are 6 to 17 dB lower. The Smiley "6 dBd" for a 27 cm antenna and the retailer's "9.0 dB" for the RH205 are not physically attainable for a single monopole over a handheld and are recorded here only so the SRR package can mark them as excluded. Confidence in the physical data (lengths, masses, connectors, power ratings): High for Diamond JP, Signal Stuff and BTECH pages; Medium for retailer-sourced MFJ figures.

### F2. Measured gain on a handheld is 6 to 17 dB below the dipole claims; the counterpoise, not the whip, sets it

**KX4O chamber EIRP measurements (the only absolute numbers found).** Yaesu FT1D transmitting its packet beacon at 135 mW (21.3 dBm) in an antenna chamber "with no other conductors involved"; a laboratory-grade 146 MHz reference dipole (independently measured 2.15 dBi) gave 23.4 dBm average EIRP against the 23.5 dBm expected, which validates the setup. With the radio free-standing (no hand):

| Antenna on the FT1D | Measured EIRP | Gain relative to the dipole | Notes quoted from the article |
|---|---|---|---|
| Reference dipole | 23.4 dBm | 0 dBd (2.15 dBi) | "practically perfect" |
| FT1D stock antenna | about 14.4 dBm | about -9 dBd ("almost 9 dB below the reference dipole") | return loss "varies significantly with handling"; standalone versus held: "Holding it reduced the 146 MHz EIRP by 3-4 dB" (the only hand effect KX4O measured); "surprisingly" robust; author recommends it for routine use |
| Diamond SRH77CA (1/4 wave) | about 6.4 dBm | -17 dBd | "poor" return loss, "high mismatch loss" |
| Diamond SRH77CA + 1/4 wave tiger tail | about 16.4 dBm | about -7 dBd | "+10 dB improvement"; "stunning and advantageous difference" |
| MFJ-1714 1/2 wave end-fed | not printed as a number ("Well well the 1/2 wave antenna finally beats the stock antenna"); plot reading about 17 to 19.5 dBm | about -4 to -6.4 dBd (this report's plot reading is -6.4 dBd; the parallel `rf-exposure-evaluation.md` reads the same plot as about -4 dBd) | return loss 8 to 10 dB ("only about 1/2 dB mismatch loss"); "a few dB short of the ... reference dipole at the broadside 0 degrees", "on par with the reference dipole at elevated angles ... 30+ degrees"; holding the radio "provides no change to hearing the local repeater" (subjective, receive side); adding a counterpoise "makes little difference" |

Source: https://www.hamradio.me/antennas/ht-antenna-comparisons.html ; https://www.hamradio.me/antennas/efhw-ht-antenna-functions-without-counterpoise.html . Confidence: High that these are the published numbers; Medium as generalizations, because they are one radio (a small dual-band FT1D chassis) and free-standing, i.e. the worst counterpoise case; the author reports the hand "noticeably improves" the 1/4 wave antennas (F4) but gives no number.

**G4ILO relative field-strength shootout (hand-held, 2011-04-23).** Yaesu VX-8GR at 5 W into each antenna, Yaege FC-1 frequency counter's relative dBm scale "a couple of metres away"; on-air signal reports from local amateurs agreed with the readings. Relative to the stock VX-8GR antenna and the Nagoya NA-701 (both 0 dB): 2 in 144 MHz stubby -5 dB; A-137 dual-band stubby -3 dB; Smiley 2 m Stubby Duck -2 dB; 6 in 2 m helical -1 dB; 8 in 2 m helical 0 dB; Yaesu FT-817ND whip +1 dB; quarter-wave telescopic whip +3 dB; Nagoya NA-767 about +6 dB; Sharman RH-770 (1/2 wave) +10 dB; 45.5 in black whip +11 dB. Source: http://blog.g4ilo.com/2011/04/2m-ht-antenna-shootout.html (mirror https://www.amateurradio.com/2m-ht-antenna-shootout/). Confidence: Medium (relative readings at a few metres are in the near field of the operator and reflect one geometry; no dBd anchor).

**K0DK via K0NR (2006-07-01).** "A 1/2-wave antenna performs ~5 to 8 dB better than a rubber duck" on 2 m and "~3 to 7 dB" on 70 cm. Source: http://www.k0nr.com/blog/2006/07/k0dk-high-efficiency-ht-antennas.html . Confidence: Medium-Low (method not given in the summary).

**The NBS figure.** KE4SKY (1998/1999): "National Bureau of Standards tests of Public Safety high band and amateur 2-meter antennas indicate that a 'rubber duck' has -5db, 'negative gain' compared to a quarter wave held at face level"; also "HT on belt: -20db attenuation" and "quarter wave with counterpoise: 5 db improvement over a typical rubber duck", "ground plane addition to half-wave: about 2 db gain". WD8RIF repeats the -5 dB figure with the same attribution. The primary NBS report was not located. Source: https://www.qsl.net/n7fan/comm/amateur/ht_ops.htm ; https://wd8rif.com/pdf/ht_antennas.pdf . Confidence: Low (secondary, undated primary).

**Consistency check across the three data sets.** KX4O free-standing: the 1/4 wave is 8 dB below the stock duck and the 1/2 wave is 3 to 5 dB above it (plot reading). G4ILO hand-held: the 1/4 wave telescopic is 3 dB above the stock duck and the 1/2 wave is 10 dB above it. The 11 dB swing of the 1/4 wave between the two conditions is the same size as KX4O's +10 dB tiger-tail effect, which is consistent with the hand and body acting as the counterpoise a small chassis cannot provide (F4, F5). KX4O's one measured hand effect, on the short stock helical, went the other way (3 to 4 dB reduction), so the inference is that a hand completes the dipole for a 1/4 wave but mainly absorbs for a short helical; this is an inference across two data sets, Low-Medium confidence, to be replaced by the ACTION-3 measurement. The 1/2 wave's larger advantage in G4ILO's test is plausibly the VX-8GR's poorer stock duck versus the "surprisingly" good FT1D duck.

**Gain values carried into the analysis (F9 to F11).**

| Case | Gain used | Basis | Confidence |
|---|---|---|---|
| Regulatory bound (part97 report F8 assumption) | 0 dBd | dipole; conservative for exposure | n/a (bound) |
| 1/2 wave end-fed on a small HT | -6.4 dBd (range -4 to -6.4 dBd) | KX4O MFJ-1714, free-standing, "a few dB short" of the dipole broadside; -6.4 dBd is the conservative plot reading and is used in the tables, with the -4 dBd values (the parallel exposure report's reading) added where they change a conclusion | Medium |
| 1/4 wave with 48 cm counterpoise, or hand-held (proxy) | -7 dBd | KX4O SRH77CA + tail; G4ILO hand-held cross-check | Medium-Low |
| Stock short duck | -9 dBd | KX4O FT1D stock, free-standing | Medium |
| 1/4 wave alone on a small chassis, no hand, no tail (table-top worst case) | -17 dBd | KX4O SRH77CA free-standing | Medium (one radio) |

### F3. A quarter-wave counterpoise ("tiger tail") adds about 10 dB to a 1/4 wave whip and about nothing to a 1/2 wave

- KX4O: +10 dB on the SRH77CA; "little difference" on the MFJ-1714 (F2).
- WD8RIF: the 1/4 wave whip "relies on capacitive coupling to the operator's body for the second half of the dipole"; a 19 in (48 cm) wire on the connector shell or a grounded case screw "transforms the 1/4 wave whip into a full-size center-fed 1/2 wave dipole"; a 1/2 wave end-fed without counterpoise "performs much like a 1/4 wave whip with counterpoise"; a wire counterpoise also makes the antenna directional toward the wire (asserted, not measured). Source: https://wd8rif.com/pdf/ht_antennas.pdf .
- Signal Stuff: "Adding a counterpoise to the shield or ensuring a solid ground on the shield can also improve readings." Source: https://signalstuff.com/products/st-sma-m/ .
- Dimension: a free-space quarter wave at 146 MHz is 51.3 cm; the customary 19 in (48 cm) wire is 6 % short, consistent with end effect and insulation. Confidence: High that the effect exists and is about 10 dB for a 1/4 wave on a small chassis (one absolute measurement plus consistent relative evidence); the exact figure for cwht's chassis must be measured (ACTION-3).

### F4. The hand and body are part of the antenna: 5 to 28 dB by posture at 146 MHz, and the hand alone changes a 1/4 wave by about 10 dB

- KX4O (verbatim): stock helical, standalone versus held: "Holding it reduced the 146 MHz EIRP by 3-4 dB"; MFJ-1714 1/2 wave: "holding the body of the FT1D provides no change to hearing the local repeater" (subjective, receive side); no hand measurement was made with the SRH77CA 1/4 wave, whose +10 dB with a tail (F3) is the proxy for what a hand supplies; radiation patterns become asymmetric when held. Source: hamradio.me articles above.
- SoftWright / TAP User's Engineering Seminar (1999): John DeHart K1VBM operated a handheld from a parking lot about 250 ft from a receiving antenna on a 5 ft wooden mast; spectrum analyzer readings at 146.52 MHz, 446.00 MHz and 1294.50 MHz, inside and outside a hotel. The published table gives "the range of maximum attenuation in each particular situation due to location of the user's body on the path between the transmitter and the receiver":

| Position, 146.52 MHz | Inside | Outside |
|---|---|---|
| HT above head | 13 dB | 8 dB |
| At arm's length | 28 dB | 18 dB |
| Vertical at mouth | 18 dB | 10 dB |
| 45 degrees cross-polarized at mouth | 18 dB | 8 dB |
| At waist | 5 dB | 12 dB |

Source: https://www.softwright.com/faq/engineering/Building%20and%20Body%20Losses%20Measured%20at%204th%20Annual%20TAP%20Seminar.html . Confidence: Medium-Low; the reference level and the meaning of the two columns are only as clear as the summary page, and the "arm's length" being worst is counter-intuitive (it puts the body squarely on the path). The robust reading is that posture moves the radiated signal toward the far station by well over 10 dB.
- ECC Report 286 (CEPT, 2018-09-28): for hand-held audio PMSE at 470 to 1800 MHz the mean body effect, to be used as the antenna gain in dBd, is 0.0025 dB/MHz x F - 13.622 dB (sigma 2.1 dB), the maximum (path) body effect 0.0028 dB/MHz x F - 37.63 dB (sigma 6.63 dB); "for hand-held microphones, the position of the hand is critical. A 550 MHz test scenario shows that the body effect is increased by 10 dB by the hand" when the antenna is enclosed by the hand. The report's measurements do not extend down to 146 MHz (simulations start at 235 MHz), so it is used here only to size the hand effect. Source: https://docdb.cept.org/download/1361 . Confidence: High for the quoted statements; Low as a 146 MHz number.
- IEEE conference abstracts (helical antenna on a metal-cased PTT transceiver in front of a numerical head model, VHF and UHF): antenna gain, radiation pattern and SAR were computed versus distance to the face and the papers "recommend" use "at a distance more than 100 mm from the viewpoint of antenna gain and SAR". Sources: https://ieeexplore.ieee.org/document/6178645/ ; https://ieeexplore.ieee.org/document/6565753 (abstract snippets only; Low).
- Belt-worn: -20 dB relative to face level (KE4SKY/NBS lore, Low), repeated by WD8RIF.

Implication for cwht: for a CW handheld the operating posture is not "at the mouth"; it is either in one hand while the other hand keys, or on a table or lap with headphones and a paddle (the posture the regulatory report's DECISION-1 calls (b)). Posture (b) removes the body as counterpoise, which is exactly the -17 dBd case unless a tail or a 1/2 wave whip is used (F5).

### F5. Chassis as counterpoise: a handheld's chassis is too small; the hand, a wire or a 1/2 wave whip must supply the other half

- Electrical size: the FT1D chassis is on the order of 0.05 wavelength at 146 MHz and, free-standing, gave -17 dBd with a 1/4 wave whip (F2). cwht's enclosure is set by two 18650 cells (65 mm long each, 18.5 mm diameter; SI-023) plus the module and battery holder, so an overall length of about 120 to 140 mm is likely: 0.06 to 0.07 wavelength, the same regime. Derived; Medium.
- Practice in commercial HTs: the SMA jack shell is bonded to a die-cast chassis, and the antenna works against chassis plus hand plus body; KX4O's measurements are exactly this configuration minus the hand. Accessory "tiger tails" that clamp under the SMA nut or clip to the shell are sold for this reason (BTECH "rat tail" article, W3ATB, Paratus Radio; commercial products exist).
- For cwht the machined enclosure is the RF ground. Everything bonded to it radiates or loads the antenna: the operator's hand, and the headphone and key cables. A 1.2 m headphone lead is about 0.6 wavelength at 146 MHz and a 1 m paddle lead is about 0.5 wavelength; both will carry antenna current, which (a) detunes the antenna with cable position, (b) couples RF into the audio and keyer inputs, and (c) makes the cables part of the exposure geometry. This is a design consequence, not a measurement; see RISK-candidate ANT-R4 and REQ-candidate ANT-06.

### F6. SWR at the connector is a weak indicator of radiated performance for HT antennas

- KX4O's best radiator, the MFJ-1714, showed 8 to 10 dB return loss (SWR about 1.9 to 2.3), only 0.5 to 1 dB mismatch loss, while the SRH77CA without tail showed "high mismatch loss" and the stock antenna's return loss "varies significantly with handling" (F2).
- Manufacturers quote SWR without conditions (NA-771 VSWR <= 1.5; Signal Stick 1.3:1 at 146 MHz). KB6NU's readers report genuine NA-771 SWR "about 1.2 to 1.3" and fakes "from about 3 to 10" (comment dated August 2025; anecdotal). Source: https://www.kb6nu.com/fake-nagoya-antenna/ .
- Consequence for cwht: the owner's NanoVNA (SI-013) can screen antennas for damage and fakes and can characterize the load the PA sees when the radio is held, on a table, or in a pocket, which is a PA robustness input (REQ-candidate ANT-04); it cannot measure gain. Relative EIRP needs a receiver at a distance, which is what a tinySA Ultra with a reference dipole would provide (DECISION-3; ties to SI-021).

### F7. Connector conventions and what ships with which connector

- Icom, Yaesu (Vertex), Kenwood and Alinco handhelds: SMA jack (female, threaded outside, socket contact) on the radio; the antenna carries an SMA plug (male). Signal Stuff (2016-08): "Icom handhelds (nearly all models)" and "Yaesu handhelds (nearly all models)" take SMA-Male antennas. K0NR (Ham Radio School, 2021-10-02): "the Yaesu FT-60 uses a female SMA connector for the antenna connection ... Yaesu, Icom and Kenwood all use this connector." The FT-60R brochure lists a "CN-3 BNC-to-SMA Adapter" as an option and "Antenna Impedance 50 ohm". Sources: https://signalstuff.com/2016/08/choosing-the-correct-antenna-connector-for-your-radio/ ; https://www.hamradioschool.com/post/what-s-that-connector-on-my-ht ; http://www.yaesu.com/jp/en/products/pdf/AMR/FT-60R.pdf .
- Baofeng, Wouxun, TYT and most Chinese handhelds from about 2014, plus some Motorola and Kenwood commercial radios: SMA plug (male) on the radio; antennas are SMA-F. Signal Stuff notes "off the shelf SMA connectors won't work with Chinese handhelds" in the sense that adapters made for Yaesu/Icom do not fit.
- BNC: "used to be the standard connector for HTs" and "largely replaced with the much smaller SMA" (K0NR); still on older radios and the Icom IC-V80 (Signal Stuff); quarter-turn bayonet, quick on/off, physically larger. Many hams standardize on BNC through adapters "so that all their radios can use BNC" (Signal Stuff). K0NR warns that a plain SMA-to-BNC cable adapter is "arguably mechanically weak for adapting HT antennas" and recommends adapters that "fit snugly on the top of the HT, providing mechanical support".
- RP-SMA (Wi-Fi) has reversed pin and socket and "will not fit your radio" (Signal Stuff).

Antenna availability by connector (from F1): Signal Stick in all three (SMA-M, SMA-F, BNC); Smiley in SMA-M, SMA-F, BNC and others; Nagoya NA-771 primarily SMA-F with an SMA-M version; Diamond SRH-series SMA-M only and RH-series BNC only (same antennas, different catalog letter); MFJ-1714 BNC and 1714S SMA-M; MFJ-1712 in BNC, SMA-M and SMA-F. An SMA-jack radio therefore accepts, without adapters, every quality 2 m handheld antenna named in the assignment except the standard SMA-F NA-771, for which the SMA-M NA-771 exists. Confidence: High.

### F8. Connector mechanical data and the antenna's bending load on a machined enclosure

**SMA.**
- Thread: .250-36 (1/4-36 UNS-2A), major diameter 6.35 mm (Amphenol RF Europe catalog: "Mating .250-36 threaded coupling"; TEJTE guide: "1/4-36 UNS-2A"). Recommended panel hole 6.5 to 6.6 mm ("a safe calculation is 6.55 mm (6.35 mm thread + 0.20 mm clearance)"); nut "HEX 8", about 7.9 mm across flats (TEJTE, secondary). Knurl-mount (nut-retained) SMA receptacles "should be used in panels at least .100 in thick" (2.54 mm) (AEP catalog).
- Coupling torque: Amphenol RF Europe brass SMA specification: "Mating Torque Recommended: 4 inch pounds (45 N.cm), Maximum: 5.2 inch pounds (60 N.cm)"; TEJTE: 0.45 to 0.56 N.m (4 to 5 in-lb); AEP stainless SMA: torque wrench TA-0436 "8 inch-pounds"; a TTI/Amphenol summary seen only in a search snippet says "Recommended 7 to 10 inch pounds (80-110 N.cm)" (unverified). The spread reflects brass versus stainless bodies; for a brass jack in a handheld use 4 to 5 in-lb (0.45 to 0.56 N.m), i.e. finger-tight plus a small fraction of a turn, never a wrench.
- Durability: Amphenol RF Europe brass SMA: "Connector Durability 100 matings"; AEP stainless (MIL-PRF-39012 class): "Durability: 500 mating cycles." A brass SMA jack, the type in consumer radios, is rated for a tenth of the mating cycles usually quoted for SMA.
- Electrical: 50 ohm; flexible-cable SMA 0 to 12.4 GHz; voltage rating 500 V peak (RG-58 type), dielectric withstanding 1000 VRMS; at 5 W into 50 ohm the peak RF voltage is 22.4 V (regulatory report F27 arithmetic), so voltage is not a constraint. Sources: Amphenol RF Europe SMA catalog (2006) via https://docs.rs-online.com/d592/A700000007129863.pdf (decoded text) ; AEP SMA catalog via https://www.radiall.com/media/AEP%20SMA%20127-1.pdf ; https://tejte.com/blog/sma-connector-dimensions-cutouts-thread/ .

**BNC.** Bulkhead jacks such as Amphenol 31-221 (RG-58/59/179/316 solder, straight bulkhead jack, "silver-plated beryllium copper contact", 4 GHz) mount through a 3/8-32 threaded body with a hex nut (standard for the family; the datasheet itself could not be retrieved, see Method) and are commonly rated 500 mating cycles (Low; not read from a datasheet). The bayonet gives quick disconnect with positive locking. Confidence: Medium on the mounting thread, Low on durability.

**Bending load (Analysis, python3; Medium confidence, material properties assumed).**

| Load case | Moment at the connector |
|---|---|
| NA-771 (0.396 m, 40 g), radio lying horizontal, gravity only | 0.078 N.m |
| Signal Stick (0.48 m, 18 g), horizontal | 0.042 N.m |
| RH770 class 1/2 wave (1.02 m, 85 g), horizontal | 0.43 N.m |
| Side load 5 / 10 / 20 N at the tip of a 0.40 m whip (a finger push, a pocket snag, a fall onto the antenna) | 2.0 / 4.0 / 7.9 N.m |
| Same at the tip of a 1.02 m whip | 5.1 / 10.2 / 20.4 N.m |

Yield moment of the connector neck (hollow cylinder, section modulus pi (D^4 - d^4) / (32 D)): SMA neck at the thread minor diameter (5.6 mm) with a 4.13 mm bore, section modulus 1.2 x 10^-8 m^3, yield moment 2.4 N.m at 200 MPa and 3.6 N.m at 300 MPa (free-machining brass range); BNC neck (about 8.7 mm minor, 6.4 mm bore), 4.6 x 10^-8 m^3, 9.1 to 13.7 N.m. Reading: a 5 to 10 N sideways push on the tip of a 40 cm whip reaches the yield moment of a brass SMA neck, and a PCB-only mounted SMA jack transfers that moment into solder joints and copper, which fail long before the brass does. Field evidence is consistent: RadioReference repair threads describe SMA failure as "common wear and tear ... pressed up against at the belt line on VHF antennas" and a Motorola XTS2500 whose SMA "broke off rf board". Sources: https://forums.radioreference.com/threads/replacing-the-sma-connector.362917/ ; https://forums.radioreference.com/threads/xts2500-sma-question-broke-off-rf-board.332933/ .

Strain-relief practice that follows: (1) the enclosure, not the PCB, carries the moment: a bulkhead (nut-retained) jack through a machined boss at least 2.5 mm thick, with a D-flat or anti-rotation feature so coupling torque cannot spin the jack; (2) the PCB connection is compliant: either a short RG-316 pigtail from the bulkhead jack to a board connector, or a PCB-mount bulkhead jack whose threaded body passes through the lid and is nutted (the PCB legs then carry only their own solder and the boss carries the antenna), which requires a tolerance analysis between the PCB outline (PCBWay +/-0.2 mm) and the machined hole (PCBWay ISO 2768 class m, +/-0.1 mm on 3 to 6 mm features); (3) a flexible whip (Signal Stick's Nitinol "can be tied in a knot without any permanent bending") sheds the load by bending; stiff coil-loaded whips and 1 m telescopics transmit it; (4) BNC has 4 to 5 times the neck strength and quick release but needs a hole of about 9.7 mm and a larger nut, and pushes the connector family away from the Icom/Yaesu antenna ecosystem (F7).

### F9. ERP at each power step, time-averaged ERP, and what it does to the exposure distances

Power steps are the RF-06 candidate (0.5 / 1 / 2 / 5 W) plus the RF-05 maximum tolerance (6.0 W). Key-down ERP = P x 10^(G/10):

| Antenna gain case (F2) | 0.5 W | 1.0 W | 2.0 W | 5.0 W | 6.0 W max |
|---|---|---|---|---|---|
| 0 dBd (regulatory bound) | 0.500 W | 1.000 W | 2.000 W | 5.000 W | 6.000 W |
| -4 dBd (1/2 wave end-fed, parallel exposure report's reading) | 0.199 W | 0.398 W | 0.796 W | 1.991 W | 2.389 W |
| -6.4 dBd (1/2 wave end-fed, this report's conservative reading) | 0.115 W | 0.229 W | 0.458 W | 1.145 W | 1.375 W |
| -7 dBd (1/4 wave + tail, or hand-held) | 0.100 W | 0.200 W | 0.399 W | 0.998 W | 1.197 W |
| -9 dBd (stock duck) | 0.063 W | 0.126 W | 0.252 W | 0.629 W | 0.755 W |
| -17 dBd (1/4 wave alone, table-top, no tail) | 0.010 W | 0.020 W | 0.040 W | 0.100 W | 0.120 W |

EIRP is 1.64 x these values. Time-averaged ERP for OET 65 B "conversational CW" (duty factor 0.40) is 0.40 x key-down ERP for continuous operation and 0.20 x for keying half of the averaging window: at 5 W, 0.80 / 0.40 W (1/2 wave at -4 dBd) or 0.46 / 0.23 W (1/2 wave at -6.4 dBd), 0.40 / 0.20 W (1/4 wave + tail), 0.25 / 0.13 W (duck), 0.040 / 0.020 W (bare 1/4 wave), versus 2.0 / 1.0 W at the 0 dBd bound.

Effect on the regulatory report's F8 tables (same formulas: exemption ERP 3.83 R^2 with R >= 0.331 m; far-field S = 2.56 EIRP / (4 pi R^2)):

| Case, 5 W | Time-averaged ERP | MPE-exemption distance (1.1307(b)(3)(i)(C)) | Far-field distance to 0.2 mW/cm2 (general population) | to 1.0 mW/cm2 (operator) |
|---|---|---|---|---|
| 0 dBd, 40 % duty (bound) | 2.00 W | 0.72 m | 0.58 m | 0.26 m |
| -4 dBd, 40 % duty | 0.80 W | 0.46 m | 0.36 m | 0.16 m |
| -4 dBd, carrier (tune-up) | 1.99 W | 0.72 m | 0.58 m | 0.26 m |
| -6.4 dBd, 40 % duty | 0.46 W | 0.35 m | 0.28 m | 0.12 m |
| -6.4 dBd, carrier (tune-up) | 1.15 W | 0.55 m | 0.44 m | 0.20 m |
| -7 dBd, 40 % duty | 0.40 W | 0.331 m (floor) | 0.26 m | 0.12 m |
| -9 dBd, 40 % duty | 0.25 W | 0.331 m (floor) | 0.21 m | 0.09 m |
| -9 dBd, carrier | 0.63 W | 0.41 m | 0.32 m | 0.15 m |

Reading: with any real handheld whip and CW duty, the MPE-based exemption is available between the lambda/2 pi floor (0.33 m) and 0.46 m, and the far-field general-population distance is under 0.4 m; a 1/2 wave whip keyed as a tune-up carrier reproduces the 0 dBd, 40 % duty bound (0.72 m). Two cautions that must travel with these numbers into RFX-01:

1. They apply only to the mobile posture (antenna at least 20 cm from everyone). For the handheld posture the SAR regime applies and **low ERP does not mean low SAR**: the 6 to 17 dB "loss" of an HT antenna is not lost in the whip, it is power dissipated in mismatch, in the chassis, and above all absorbed in the hand and body. The KX4O free-standing numbers were taken with no body present, so the missing power there is mismatch and pattern; with a hand present the absorbed fraction rises. The SAR-by-analogy figures of the regulatory report F8(c) (0.35 W/kg per W at 1 g, 50 % duty) remain the handheld-posture basis and are unchanged by this report.
2. The 0 dBd bound remains the right worst case for a documented evaluation, because an operator can attach a 1/2 wave whip with a tail, or an external dipole, and because the antenna gain of a handheld is not a controlled quantity.

### F10. External noise at 146 MHz and the signal an A1A operator needs

**External noise (ITU-R P.372-13, Table 1).** Fam = c - d log10(f), f in MHz, "valid in the range 0.3 to 250 MHz for all the environmental categories except those of curves D and E": City c = 76.8, d = 27.7; Residential 72.5, 27.7; Rural 67.2, 27.7; Quiet rural 53.6, 28.6; Galactic 52.0, 23.0. At 146 MHz: City 16.8 dB, Residential 12.5 dB, Rural 7.2 dB, Galactic 2.2 dB (the quiet-rural line falls below galactic here, so galactic is the floor). Decile variation with time (Table 2): residential upper 10.6 dB, lower 5.3 dB; rural 9.2 / 4.6 dB; with location 5.8 dB (residential) and 6.8 dB (rural). The values "were measured in the 1970s and may change with time". Source: https://www.itu.int/dms_pubrec/itu-r/rec/p/R-REC-P.372-13-201609-S!!PDF-E.pdf . Confidence: High (verbatim constants), Medium for their currency.

**Required signal for aural Morse (ITU-R F.339-8, Table 1).** "A1A Telegraphy 8 Bd, aural reception: pre-detection bandwidth 3000 Hz, post-detection 1500 Hz, audio SNR -4 dB, average RF SNR 31 dB(Hz) stable condition, 38 dB(Hz) fading condition, non-diversity", the last "for protection 90 % of the time" and defined as "the ratio of signal peak envelope power to the average noise power in a 1 Hz bandwidth". Expressed in a 500 Hz CW filter these are +4 dB and +11 dB SNR. Source: https://www.itu.int/dms_pubrec/itu-r/rec/f/R-REC-F.339-8-201302-I!!PDF-E.pdf . Confidence: High.

**System noise density with an inefficient antenna (derived).** With antenna efficiency eta taken equal to the dBd gain (dipole-like directivity), receiver noise figure NF, and external noise figure Fa, the noise density referred to the receiver input is N0 = -174 dBm/Hz + 10 log10(Fa_lin x eta + (1 - eta) + NF_lin - 1). For NF = 7 dB (the reference-designs report's MDS candidate of -140 dBm in 500 Hz):

| Environment | G = 0 dBd (external dipole) | G = -6.4 dBd | G = -9 dBd | G = -17 dBd |
|---|---|---|---|---|
| Galactic floor | N0 -166.5 ; S_req -135.5 / -128.5 dBm | -166.9 ; -135.9 / -128.9 | -166.9 ; -135.9 / -128.9 | -167.0 ; -136.0 / -129.0 |
| Rural | -164.3 ; -133.3 / -126.3 | -166.2 ; -135.2 / -128.2 | -166.6 ; -135.6 / -128.6 | -166.9 ; -135.9 / -128.9 |
| Residential | -160.6 ; -129.6 / -122.6 | -164.5 ; -133.5 / -126.5 | -165.5 ; -134.5 / -127.5 | -166.7 ; -135.7 / -128.7 |
| City | -156.8 ; -125.8 / -118.8 | -162.0 ; -131.0 / -124.0 | -163.6 ; -132.6 / -125.6 | -166.2 ; -135.2 / -128.2 |

(S_req = N0 + 31 dB stable / N0 + 38 dB fading.) Reading: with a whip on the radio, external noise raises the floor by only 0.8 dB (rural) to 5 dB (city) because the whip attenuates the noise as much as the signal; the receiver's own noise dominates. Consequences: (a) the NF 7 dB / MDS -140 dBm candidate is adequate for a handheld whip; the -144 dBm stretch buys about 3 dB only at a quiet site with a good external antenna and about 1 dB in residential noise with a whip; (b) an external antenna (0 dBd) in a residential location moves the floor up 6.4 dB, so the receiver's blocking and IMD, not sensitivity, are what the external-antenna case stresses (consistent with the reference-designs report's strong-signal findings).

### F11. Simplex link budget for two HTs at 1.5 m and for a hilltop

**Models (all at 146 MHz).** Free space: 32.45 + 20 log10 f(MHz) + 20 log10 d(km) dB. Two-ray flat earth, far field (valid for d much greater than 4 pi h1 h2 / lambda = 13.8 m here): PL = 40 log10 d(m) - 20 log10(h1 h2) = 40 log10 d(km) + 112.96 dB for h1 = h2 = 1.5 m (Wikipedia, citing Jakes 1974 and Rappaport 2002). Egli median for rolling terrain (hm <= 10 m): 20 log10 f + 40 log10 d(km) - 20 log10 hb + 76.3 - 10 log10 hm (Mardeni and Kwan 2010 eq. 9, after Egli, Proc. IRE Oct 1957); with both heights 1.5 m this is 40 log10 d(km) + 114.3 dB, 1.4 dB above two-ray, but Egli was fitted with a base station well above 10 m and 40 mile paths, so it is a rough check only (Low). Radio horizon over a 4/3 earth: d = 4.124 (sqrt h1 + sqrt h2) km, h in m (repeater-builder.com): 10.1 km for 1.5 m + 1.5 m.

| d (km) | Free space | Two-ray, 1.5 m / 1.5 m | Egli, 1.5 m / 1.5 m |
|---|---|---|---|
| 0.5 | 69.7 dB | 100.9 dB | 102.3 dB |
| 1 | 75.7 | 113.0 | 114.3 |
| 2 | 81.8 | 125.0 | 126.3 |
| 3 | 85.3 | 132.0 | 133.4 |
| 5 | 89.7 | 140.9 | 142.3 |
| 10 (horizon) | 95.7 | 153.0 | 154.3 |

**Two HTs at 1.5 m over open, flat ground, 5 W (37 dBm), both radios with the same antenna, NF 7 dB, two-ray model, capped by the 10.1 km horizon.** "c0 / c10 / c20" is an added clutter and fading allowance of 0, 10 or 20 dB (open field, light trees or scattered houses, suburban streets; values chosen, not measured):

| Noise environment | Antenna (both ends) | Allowed path loss, stable, c0 | Range (km), A1A stable, c0 / c10 / c20 | Range (km), A1A fading 90 %, c0 / c10 / c20 |
|---|---|---|---|---|
| Rural | -4 dBd (1/2 wave end-fed, -4 dBd reading) | 168.0 dB | 10.1 (horizon; model 23.8) / 10.1 (13.4) / 7.5 | 10.1 (15.9) / 8.9 / 5.0 |
| Rural | -6.4 dBd (1/2 wave end-fed, conservative reading) | 163.7 dB | 10.1 (horizon; model 18.6) / 10.1 (10.4) / 5.9 | 10.1 (12.4) / 7.0 / 3.9 |
| Rural | -9 dBd (stock duck) | 158.9 dB | 10.1 (14.0) / 7.9 / 4.4 | 9.4 / 5.3 / 3.0 |
| Rural | -17 dBd (bare 1/4 wave, table-top) | 143.2 dB | 5.7 / 3.2 / 1.8 | 3.8 / 2.1 / 1.2 |
| Residential | -4 dBd | 165.6 dB | 10.1 (20.7) / 10.1 (11.6) / 6.5 | 10.1 (13.8) / 7.8 / 4.4 |
| Residential | -6.4 dBd | 162.0 dB | 10.1 (16.8) / 9.5 / 5.3 | 10.1 (11.3) / 6.3 / 3.6 |
| Residential | -9 dBd | 157.8 dB | 10.1 (13.2) / 7.4 / 4.2 | 8.8 / 5.0 / 2.8 |
| Residential | -17 dBd | 143.0 dB | 5.6 / 3.2 / 1.8 | 3.8 / 2.1 / 1.2 |

Reading: over open flat ground at 5 W the CW link is horizon-limited (10 km) for every antenna except the bare table-top 1/4 wave; the antenna and the clutter, not the power, set the range. Power steps scale range by 10^(dB/40) in this regime: 2 W gives 0.79 x, 1 W 0.67 x, 0.5 W 0.56 x the 5 W range.

**FM comparison (the "propagation advantage" of SI-004 in numbers).** A conventional 2 m FM handheld specifies 0.16 uV for 12 dB SINAD (Yaesu FT-60R brochure, 140 to 150 MHz), i.e. -122.9 dBm; the A1A stable requirement with a -9 dBd whip in rural noise is -135.6 dBm, 12.7 dB less. In the 40 dB/decade regime that is 2.1 x the range (10^(12.7/40)); in free space 4.3 x. The same two-ray model for two 5 W FM HTs with stock ducks gives 6.8 / 3.8 / 2.1 km for c0 / c10 / c20, which brackets the "2.5 miles suburban, 3.9 miles flat open ground" figures that ham range calculators quote for FM HTs (radioranked.com, Low), a weak validation that the clutter allowances are in the right range.

**Hilltop case (free space, line of sight, both antennas -6.4 dBd, rural noise, NF 7 dB, far HT at 1.5 m).**

| Hill height above the far station's terrain | Radio horizon | Free-space loss at the horizon | Received power | Margin over A1A stable | over A1A fading 90 % |
|---|---|---|---|---|---|
| 30 m | 27.6 km | 104.6 dB | -76.1 dBm | 59.2 dB | 52.2 dB |
| 100 m | 46.3 km | 109.0 dB | -80.5 dBm | 54.7 dB | 47.7 dB |
| 300 m | 76.5 km | 113.4 dB | -84.9 dBm | 50.3 dB | 43.3 dB |
| 1000 m | 135.5 km | 118.4 dB | -89.9 dBm | 45.3 dB | 38.3 dB |

Reading: a line-of-sight hilltop path has 38 to 59 dB of margin at 5 W (43 to 64 dB with -4 dBd antennas at both ends); even 0.5 W (-10 dB) or a bare 1/4 wave at one end (-10.6 dB) leaves over 20 dB. The hilltop MOE is therefore a test of the horizon and of receiver behaviour with strong signals, not of transmitter power; beyond the horizon, diffraction loss climbs at tens of dB per few kilometres and the CW margin translates into a modest distance extension that only a terrain model (ITM / Longley-Rice, e.g. the open-source SPLAT! CLI) can quantify for real sites (ACTION-4).

### F12. Counterfeit NA-771s are common enough to matter for a reference antenna

Genuine Nagoya antennas are made by REUEX Industrial Co., Ltd. (Taiwan), sold in a yellow slip case with a rectangular holographic trademark label; Nagoya changed the design "to combat the problem with counterfeit products" (Buy Two Way Radios blog, 2014). KB6NU (2018) lists the tells (bag construction, lettering, presence of a spacer); a 2025 commenter measured genuine units at SWR 1.2 to 1.3 and fakes at 3 to 10. RadioReference threads track the fakes. Sources: https://www.kb6nu.com/fake-nagoya-antenna/ ; https://www.buytwowayradios.com/blog/2014/03/updated_design_for_the_nagoya_na-701_and_na-771_antennas.html ; https://forums.radioreference.com/threads/nagoya-na-771-counterfeits.420200/ . Confidence: Medium. Consequence: a reference antenna for a V&V package should be one whose supply chain is unambiguous (Signal Stuff direct; Diamond through its US distributor; MFJ direct), and the SRR package should require an SWR screen of every unit against the maker's figure before it is used as a reference (ACTION-3).

## 4. Implications for cwht

### Candidate requirements (numbers are proposals; owner to confirm at SRR)

- **REQ-candidate ANT-01 (antenna port, F7, F8).** The antenna port shall be a 50 ohm SMA jack (female body, 1/4-36 UNS-2A external thread, socket centre contact) so that the radio accepts SMA-plug antennas per the Icom/Yaesu/Kenwood/Alinco convention. The user documentation shall state that Baofeng-style SMA-F antennas need an SMA-M NA-771 or an adapter and that RP-SMA does not fit. Verify: Inspection.
- **REQ-candidate ANT-02 (connector load path, F8).** The antenna port shall withstand a static bending moment of 4.0 N.m (10 N applied at 0.40 m from the port) in any direction and 1000 mating cycles of an SMA plug at 0.45 to 0.56 N.m coupling torque without loss of RF continuity, damage to the PCB, or rotation of the jack. Design constraint: the jack is retained to the machined enclosure (boss thickness >= 2.5 mm, hole 6.55 mm +0.05/-0.00 mm, anti-rotation flat) and the PCB connection carries no antenna moment (pigtail or PCB-mount bulkhead jack with a documented tolerance stack, see ME). Verify: Analysis (hand calculation or FEA of boss and jack neck), Test (static load on the printed fit-check part and on the first machined enclosure), Inspection (nut torque and thread engagement).
- **REQ-candidate ANT-03 (counterpoise attachment, F3, F5).** A bonded attachment point for a 48 cm (19 in) counterpoise wire shall exist within 20 mm of the antenna port (ring terminal captured under the SMA nut, or an M3 threaded hole in the boss), with DC resistance to the connector shell <= 10 milliohm. Verify: Inspection, Test (milliohm meter).
- **REQ-candidate ANT-04 (PA load tolerance, F6).** The transmitter shall deliver rated power with SWR <= 2:1 and shall survive continuous key-down for at least 60 s into any load of SWR up to 10:1 at any phase, and into open and short circuits, without damage (hand-detuned whips show return loss of 8 dB; counterfeit antennas show SWR 3 to 10). Verify: Analysis (SPICE at load extremes with the LPF), Bench (NanoVNA-characterized mismatch fixtures, thermal check).
- **REQ-candidate ANT-05 (reference antenna configurations, F2, F7, F12).** The V&V baseline shall name two reference configurations: (a) pocket reference: Signal Stuff Signal Stick SMA-M (1/4 wave, 48 cm, Nitinol) with the 48 cm counterpoise of ANT-03 attached; (b) range reference: an end-fed 1/2 wave telescopic with SMA plug (MFJ-1714S or Diamond SRH770). Each reference unit shall be SWR-screened on the radio body before use (accept <= 2:1 at 146 MHz for (a), <= 2.5:1 for (b), from F2 and F6 figures) and its serial or lot recorded. Verify: Inspection.
- **REQ-candidate ANT-06 (RF on cables, F5).** The headphone and key/paddle inputs shall include common-mode suppression (ferrite or choke plus bypass) sized for 144 to 148 MHz so that keying with 5 W into any ANT-05 configuration produces no audible change or false keyer input with 1.0 to 1.5 m unshielded leads. Verify: Analysis (choke impedance >= 500 ohm at 146 MHz), Bench.
- **REQ-candidate RX (input to the receiver requirement of the reference-designs report, F10).** Keep MDS -140 dBm in 500 Hz (NF 7 dB) as the requirement; record the -144 dBm stretch as low value with a handheld whip (about 1 dB in residential noise) and prioritize blocking/IMD for the external-antenna case instead.
- **REQ-candidate RFX (input to RFX-01 of the regulatory report, F9).** The RF Exposure Evaluation shall use ERP = 0 dBd x P as the bound and shall record the measured-gain ERP range of F9 (0.10 to 1.15 W key-down at 5 W; 0.04 to 0.46 W time-averaged at 40 % duty) as the expected values; it shall state explicitly that reduced ERP does not reduce SAR in the handheld posture.
- **MOE-candidates (F11).** MOE-RANGE-1 (open ground): two cwht units, each with the ANT-05(b) reference antenna at 1.5 m over open, flat, unobstructed ground, complete a two-way CW exchange at 5.0 km at 5 W (design margin 6 to 10 dB against the fading case with a 10 dB clutter allowance, for -6.4 to -4 dBd antennas; horizon 10.1 km). MOE-RANGE-2 (hilltop): the same at 30 km with one station at least 100 m above the intervening terrain and line of sight (margin > 40 dB; tests horizon and strong-signal behaviour). MOE-RANGE-3 (pocket): ANT-05(a) with counterpoise, 2.0 km over open ground at 2 W. Validation is by the owner and friends (SI-019); a log of positions, power step, antenna and copy quality is the evidence.

### Constraints

- An SMA jack on the radio accepts every quality 2 m handheld antenna named in the assignment without adapters except the SMA-F NA-771 (an SMA-M version exists) (F7).
- Brass SMA is rated for 100 matings by Amphenol RF Europe; a radio whose antenna is swapped daily will exceed that in a few months. Either specify a stainless-body jack (500 cycles, MIL-PRF-39012 class) or accept the jack as a wear part (F8).
- The enclosure boss around the antenna port is a structural feature of the CNC part: >= 2.5 mm wall at the hole, 6.55 mm hole, a flat for anti-rotation, and clearance for a 7.9 mm hex nut; this must go into the OpenSCAD model and the PCBWay drawing (feeds the enclosure report) (F8).
- The whip's electrical size relative to the enclosure means the operator and the cables are part of the antenna in every posture; the ConOps must describe the postures the exposure evaluation covers (regulatory report DECISION-1) (F4, F5).

### Risks

- **RISK-candidate ANT-R1 (connector or PCB damage from antenna moment, F8).** Likelihood Medium (pocket carry, SI-001), consequence High (radio inoperative; no hand soldering, SI-009). Mitigation: ANT-02, flexible reference whip (ANT-05a), printed fit-check test.
- **RISK-candidate ANT-R2 (PA damage into a detuned or counterfeit antenna, F6, F12).** Likelihood Medium, consequence High. Mitigation: ANT-04, SWR screen in ANT-05, and (design option) a forward/reverse power detector that folds back power at SWR > 3:1.
- **RISK-candidate ANT-R3 (table-top posture loses 10 dB, F2, F5).** A CW operator with a paddle will often set the radio down; without a tail or a 1/2 wave whip the 1/4 wave drops to about -17 dBd, halving the open-ground range and quartering it in clutter. Mitigation: ANT-03, ANT-05, user documentation.
- **RISK-candidate ANT-R4 (RF on headphone and key leads, F5).** Likelihood High if unmitigated, consequence Medium (audio thump, false keyer input, detuning with cable position). Mitigation: ANT-06; keep the keyer input debounce and pull-up robust to RF (feeds the keyer report).
- **RISK-candidate ANT-R5 (exposure evaluation over-credits antenna loss, F9).** Using measured ERP instead of the 0 dBd bound in the SAR posture would understate exposure. Mitigation: RFX input above; keep the regulatory report's F8(c) analogy as the handheld basis.
- **RISK-candidate ANT-R6 (tolerance stack of a PCB-mount bulkhead jack, F8).** A jack soldered to the board and nutted through the lid needs the PCB outline, standoff height and lid hole to agree within about 0.3 mm; a miss either pre-loads the solder joints or leaves the nut unable to seat. Mitigation: pigtail alternative; tolerance analysis at PDR; printed fit-check with the real PCB before the CNC order.

### Decisions needed

- **DECISION-1 (connector).** SMA jack (recommended; compact, the Icom/Yaesu/Kenwood ecosystem, antennas in F1 available as SMA-M, adapters to BNC trivial) versus BNC bulkhead (4 to 5 x neck strength, quick release, larger hole and nut, older antenna ecosystem). Recommendation: SMA jack with the ANT-02 load path; revisit only if the owner prefers BNC for bench convenience (the BNC dummy load of SI-013 needs one SMA-M to BNC adapter either way).
- **DECISION-2 (reference antenna).** Recommendation: Signal Stick SMA-M plus 48 cm tail as the pocket reference, MFJ-1714S (or Diamond SRH770 if MFJ stock stays out) as the range reference; the NA-771 is not recommended as a reference because of the counterfeit problem and its SMA-F default; the Smiley 5/8 Slim Duck is not recommended for reference use because its gain claim cannot be reconciled with physics and no independent measurement was found.
- **DECISION-3 (tinySA Ultra, SI-021).** Beyond spurious verification, a tinySA Ultra with a home-built 146 MHz reference dipole enables the G4ILO/KX4O style relative-EIRP test of the actual cwht enclosure with each antenna, hand, tail and posture; the NanoVNA cannot do this. Recommendation: buy, and add "antenna radiated-performance screen" to the V&V plan.
- **DECISION-4 (terrain modelling for the range MOE).** SPLAT! (ITM / Longley-Rice) is an open-source command-line tool suited to computing real-site paths for the owner and friends, but installing it needs Homebrew (outside this agent's write scope). Recommendation: owner installs; the analysis then becomes an Analysis-class verification of MOE-RANGE-1/2 for the actual sites.
- **DECISION-5 (power fold-back).** Whether to add a directional coupler and SWR fold-back (adds parts and an ADC channel on the RP2350) or to rely on PA ruggedness (ANT-04) alone. Recommendation: decide at PDR after the PA device is chosen and its SWR ruggedness datasheet figure is known.

### Actions

- **ACTION-1.** Obtain and file the datasheets this agent could not fetch (Amphenol 132421 PCB-mount bulkhead SMA jack or equivalent; Amphenol 31-221 BNC bulkhead jack; Amphenol torque FAQ) and record DigiKey/Mouser stock and price with date and time for the parts list; the sites returned HTTP 403 to this tool.
- **ACTION-2.** Put the antenna boss (>= 2.5 mm wall, 6.55 mm hole, flat, nut clearance) and the counterpoise attachment into the OpenSCAD enclosure model and the PCB outline drawing; add the tolerance analysis of ANT-R6 to the PDR package.
- **ACTION-3.** Write the V&V procedure "antenna screen and relative EIRP": NanoVNA SWR of each reference antenna on the radio body (hand-held, table-top, with tail); relative EIRP with tinySA Ultra and reference dipole at >= 3 m (if DECISION-3 is yes); record the +tail delta for the actual enclosure to replace the KX4O proxy in F2.
- **ACTION-4.** If DECISION-4 is yes, run SPLAT! for the owner's and friends' locations at 146 MHz with the F11 antenna gains and produce path-loss and margin tables for MOE-RANGE-1/2.
- **ACTION-5.** Add to the ConOps the operating postures (hand-held, table-top with paddle, pocket/belt) with the F4 losses, so that both the range MOEs and RFX-01 evaluate the same postures.
- **ACTION-6.** Copy the plain-text extracts of ECC Report 286, ITU-R P.372-13 Table 1 and Table 2, and ITU-R F.339-8 Table 1 from the scratch directory into `docs/references/md/` (owner's or parent agent's write scope), and add the KX4O and G4ILO pages to the reference list as the measurement basis of F2.

## 5. Confidence

| Finding | Confidence | Basis |
|---|---|---|
| F1 physical data (lengths, masses, connectors, ratings) | High for Diamond JP, Signal Stuff, BTECH; Medium for MFJ | Manufacturer pages read directly; MFJ from maker page plus retailer listings that disagree on collapsed length and power |
| F1 gain claims are unverified marketing | High | No manufacturer states a measurement condition; F2 measurements contradict them by 6 to 17 dB |
| F2 measured gains | Medium | One absolute chamber data set (KX4O, one radio, free-standing), one relative hand-held set (G4ILO), one summary (K0DK); mutually consistent to within a few dB; the MFJ-1714 value is a plot reading (-4 to -6.4 dBd), not a number printed in the article; the stock (-9 dBd) and SRH77CA (-17 dBd, +10 dB with tail) values are printed |
| F3 counterpoise +10 dB on a 1/4 wave | High that the effect is of this order; Medium on the number for cwht | KX4O measurement plus G4ILO cross-check |
| F4 hand and body | Medium-Low as numbers at 146 MHz | KX4O's 3 to 4 dB hand reduction is measured but for one short helical; SoftWright 1999 table has an ambiguous reference; ECC 286 is 470 to 1800 MHz; NBS figure is secondary |
| F5 chassis as counterpoise | Medium | Derived from F2 and electrical size; no cwht measurement yet |
| F6 SWR as indicator | High | KX4O return-loss versus EIRP data |
| F7 connector conventions | High | Two independent ham sources plus the FT-60R brochure accessory list |
| F8 SMA specifications | High for Amphenol RF Europe and AEP figures (decoded and read); Medium for TEJTE hole and nut figures | The decoding mapping was verified on known strings |
| F8 BNC specifications | Low | No datasheet retrievable; thread and cycles from general knowledge |
| F8 bending analysis | Medium | Geometry from the thread standard and typical bore; brass yield assumed 200 to 300 MPa |
| F9 ERP tables | High as arithmetic; Medium as predictions | Inherit F2's confidence |
| F10 noise and A1A SNR | High | Verbatim ITU constants; the system-noise model is a first-order derivation |
| F11 link budget | Medium | Standard models; clutter allowances are chosen, not measured; horizon cap is robust |
| F12 counterfeits | Medium | Multiple community sources, no manufacturer statement read directly |

## 6. Open items

1. Amphenol torque FAQ, Amphenol 132421 and 31-221 datasheets, and distributor stock/price were not retrievable (HTTP 403 to WebFetch and curl); the SMA torque values in F8 come from the Amphenol RF Europe 2006 catalog and AEP, and the BNC figures are unverified. ACTION-1.
2. Signal Stick mass is not published by the maker (retailer 18 g; review "half the NA-771"); Diamond SRH77CA (US) mass is not published (SRH771 38 g used as proxy). Weigh the purchased units.
3. No measurement of a 1/4 wave whip hand-held with an absolute dBd anchor was found; the -7 dBd hand-held proxy is inferred from the tail measurement and G4ILO's relative data, while KX4O's only measured hand effect (stock helical, 3 to 4 dB reduction) shows the hand can also subtract. ACTION-3 closes this for the actual cwht enclosure.
10. Coordination with `rf-exposure-evaluation.md` (written in parallel by another agent from the same KX4O source): it adopts -9 to -4 dBd for handheld whips with +2 dBd as the largest plausible user antenna, and reads the MFJ-1714 at about -4 dBd; this report uses -6.4 dBd as the conservative half-wave reading and gives the -4 dBd values alongside. The requirements owner should fix one gain set for RFX-01 and the MOEs. Recommendation: the higher ERP (-4 dBd, or the 0 dBd bound) for exposure and the lower gain (-6.4 dBd) for range, since each is the conservative choice for its purpose.
4. The SoftWright 1999 body-position table's reference level is not fully defined on the summary page; the primary seminar material was not found.
5. The NBS report behind the "-5 dB rubber duck" and "-20 dB on the belt" figures was not located; the figures remain Low confidence.
6. ITU-R P.372-17 (2024) could not be downloaded (404 at the search-result URL); P.372-13 constants were used and are unchanged in later editions to this agent's knowledge (unverified).
7. Egli is applied outside its fitted domain (both antennas at 1.5 m); an ITM/Longley-Rice run (DECISION-4) should replace it for the MOE.
8. The web-search budget of the session ran out before Elecraft/QRP Labs BNC practice, the ETSI/TIA radiated-power test-fixture methods for portables, and a second independent chamber measurement of HT whips could be checked; none of these changes the recommendations but each would raise F2 and F7 confidence.
9. Whether the RP2350 module's USB connector (SI-022) and the LCD cable form additional counterpoise or radiating paths depends on the layout and belongs to the RF-08 analysis of the regulatory report.
