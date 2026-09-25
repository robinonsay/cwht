# 144 MHz CW transceiver reference designs and component options (assignment: rf-reference)

**Status:** research report for PDR trade studies. **Date:** 2026-09-25. **Author:** Claude (research subagent). **Owner:** Robin.

Scope note from the owner (relayed 2026-09-25): the rig must support **both a straight key and iambic paddles** through the built-in keyer. Findings 22 to 27 (T/R switching and envelope shaping) are written with that as a core requirement: element timing at paddle speeds drives the T/R switch speed, the break-in mode and the shaping overhang.

## Question

Survey published 144 MHz CW/SSB transceiver and transverter designs and component options to ground the PDR trade studies: known homebrew/kit designs and commercial portables with their receiver topologies (superhet IF choices, crystal ladder filters, direct conversion) and typical MDS/IMD figures; synthesizer options at 144 MHz with phase-noise and stability data (Si5351A limits and reports, TCXO references, ADF4351, MAX2871, LMX2571, cost signals); 5 W-class PA devices for 144 MHz at 7.4 V (NXP AFT05MS006N/004N, Mitsubishi RD series status, alternatives) with vendor reference circuits and stock signals; T/R switching (PIN vs relay) and keying envelope shaping practice; crystal filter approaches for 500 Hz CW bandwidth. Deliver a comparison table and the list of decisions the PDR trade studies must resolve.

## Method

1. Web search (WebSearch) for each topic, then WebFetch of primary pages (NXP, Mitsubishi Electric US, TI, Analog Devices, Skyworks datasheet, Kuhne/DB6NT, G4DDK, Elecraft, Q5 Signal, QRP Labs, Omron, NXP PIN diode datasheet, Cornell LII mirror of 47 CFR because ecfr.gov redirected to a bot-check page).
2. Datasheets and manuals that WebFetch could not parse were downloaded with `curl` into the session scratchpad and converted with `pdftotext -layout`, then searched with `grep`. Files: AFT05MS006N datasheet, Si5351A/B/C-B datasheet Rev 1.3, LMX2571 datasheet, ADF4351 datasheet (mirror), Anglian 144 v1.1 and Anglian 3L technical descriptions, Kuhne MKU 144 G2 manual, Q5 Signal L144-28 manual, Elecraft XV owner's manual Rev F1, G4JNT 144 MHz DC receiver note, BAP64-02 datasheet, Omron G6K-2F-RF datasheet, QRP Labs AN005, RD07MUS2B / RD12MVS1 / RD06LUS2 datasheets, KVG 9 MHz standard filter sheet, PGA-103+ datasheet, ARRL QST IC-705 review (Feb 2021 reprint), VA7OJ IC-705 test report, G3OTK key-click paper, QCX and QMX operating manuals.
3. Distributor stock and price signals were taken from findchips.com aggregations (DigiKey, Newark, Avnet, Richardson, Win Source) because digikey.com and octopart.com return HTTP 403 to automated fetches. Prices are qty-1 web prices seen on 2026-09-25 and are signals, not quotes.
4. Derived numbers (MDS from noise figure, harmonic suppression from 97.307(e), phase-noise scaling by output divider, RF voltage/current at 5 W) are computed in this report and labelled "derived".

Local command used for PDF text extraction (example):

```
pdftotext -layout AFT05MS006N.pdf AFT05MS006N.txt && grep -n "136–174" AFT05MS006N.txt
# -> "136–174   0.19   15.5   60.0   6.0"  (Pin W, Gps dB, efficiency %, Pout W at 7.5 V)
```

## Findings

### A. Reference designs: commercial portables

**F1. Icom IC-202 (1976 lineage).** 2 m SSB/CW portable, 3 W PEP, 144 to 146 MHz in four 200 kHz VXO segments. The VXO runs 14.8 MHz crystals multiplied 9x to 133.3 MHz for low-side LO injection with single conversion to a 10.7 MHz IF. Nine C cells or 13.8 V; RX 90 to 250 mA, TX 750 mA, 2.0 kg. Reputation: "a very clean rig with an excellent receiver and transmitter". Sources: G3XBM page https://sites.google.com/view/g3xbm4/home/vhfuhfmicrowaves/vhfuhf-commercial-rigs/icom-ic-202 ; RigReference https://rigreference.com/rigs/2976-ICOM_IC_202 . Lesson for cwht: a fixed crystal-derived LO (multiplied overtone or VXO) gave the IC-202 its clean receiver; the tuning range was the price.

**F2. Yaesu FT-290R (1981).** 2 m all-mode portable, 0.5/2.5 W. Receiver: 1st IF 10.81 MHz, 2nd IF 455 kHz (FM only). SSB/CW sensitivity 0.5 uV for 20 dB S/N; selectivity 2.4 kHz at -6 dB and 4.1 kHz at -60 dB (no dedicated CW filter). Supply 8.5 to 15.2 V; RX 60 to 70 mA, TX 800 mA; 1.3 kg; 8 C cells. Sources: https://www.radiomasterlist.com/en/yaesu-ft-290r.html ; https://rigreference.com/rigs/4278-yaesu-ft-290r . Derived: 0.5 uV = -113 dBm for 20 dB S/N in about 2.4 kHz gives a noise floor near -133 dBm (2.4 kHz), about -140 dBm in 500 Hz, i.e. NF roughly 7 dB. This is the class of performance a 1980s portable superhet delivered.

**F3. Mizuho MX-2.** True 2 m SSB/CW handheld, 200 mW, VXO with up to 2 crystals (50 kHz per crystal), 9.5 V, 142 x 66 x 39 mm. Source: https://rigreference.com/rigs/3591-mizuho-mx-2 ; https://www.radiomuseum.org/r/mizuhotsus_2m_ssbcw_transceiver_mx_2.html . The closest historical precedent to a pocket 2 m CW handheld; it shows the form factor is feasible and that VXO coverage was the compromise.

**F4. Yaesu FT-817/818.** Double conversion, 1st IF 68.33 MHz, 2nd IF 455 kHz; 2 m preamp is an electrically tuned network. KA7OEI reports CW MDS about 0.03 uV (about -137 dBm). Source: http://www.ka7oei.com/ft817_rcv.html ; https://en.wikipedia.org/wiki/Yaesu_FT-817 (states PIN-diode T/R switching; not verified in the service manual).

**F5. Icom IC-705, ARRL Lab (QST Feb 2021).** 144 MHz, 500 Hz bandwidth: noise floor (MDS) -133 dBm preamp off, -144 dBm preamp on; 20 kHz two-tone IMD dynamic range 83 dB (off) and 81 dB (on); blocking gain compression 122/114 dB at 20 kHz (preamp off/on) and 122/122 dB at 5/2 kHz; receiver IP3 +27/+16 dBm (off/on); spurious and harmonic suppression 68 dB at 144 MHz ("Meets FCC requirements"); TX IMD 3rd/5th/7th/9th -33/-44/-57/-64 dB at 144 MHz; keyer 6 to 48 WPM iambic B; CW keying waveform photographed at 60 WPM in QSK. The radio uses a transmit/receive relay. Source (ARRL reprint hosted by DX Engineering): https://static.dxengineering.com/global/images/technicalarticles/ico-ic-705_ng.pdf . Independent report with 144 MHz DR2/IP2 and blocking appendix: https://www.qsl.net/ab4oj/icom/ic705/705notes.pdf . These are the "modern portable" targets to compare cwht against.

### B. Reference designs: transverters and homebrew (DL / G / W / other)

**F6. G4DDK Anglian 144 MHz transverter (G, kit).** Architecture: ADE-1H level-17 mixer used bilaterally; two-stage Butler overtone crystal LO at 116 MHz followed by a PHEMT amplifier to +20 dBm; receive LNA SPF5043 (later PSA4-5043) with about 22 dB gain and 0.8 dB NF including the noise-matching filter, OIP3 +30 dBm at 144 MHz; three-pole BPF (2.5 dB IL, 1 dB BW just over 4 MHz); post-mixer MGA30689 (OIP3 +40 dBm at 28 MHz, NF < 3 dB); BAP64 PIN diodes for low-level path switching "chosen because of their good IMD performance"; TX chain to +22 dBm saturated / +20 dBm P1dB. Measured: NF 1.6 to 1.8 dB, gain 24 to 26 dB, IIP3 +0.5 to +1.5 dBm (3L: better than 0 dBm), image rejection > 70 dB, harmonics -40/-50/< -60 dBc, LO and image suppression > 70 dBc. Anglian 3L: LO composite noise better than -150 dBc/Hz at 20 kHz, TX sideband noise better than -140 dBc/Hz at 20 kHz, 200 ms transmit sequencing, external relay for the antenna, drives a Mitsubishi RA-series module from about +10 dBm. Removing the LO diplexer improved receiver IIP3. Sources: http://www.g4ddk.com/Anglian144v1_1.pdf ; http://www.g4ddk.com/Anglian3Ltechdes.pdf ; https://archive.org/details/eme2014_anglian-144v-1-1 .

**F7. Kuhne / DB6NT MKU 144 G2 transverter module (DL, commercial).** 116 MHz temperature-compensated low-noise Butler oscillator with a 40 C crystal heater, phase noise -156 dBc/Hz at 10 kHz, > 100 mW LO. Receiver: one LNA stage (NF typ 0.5 dB, OIP3 typ +30 dBm), 3-pole helical BPF, +17 dBm Schottky ring mixer. Specs: NF typ 0.9 dB at 18 C, RX gain typ 25 dB, RX output IP3 typ +23 dBm (derived IIP3 about -2 dBm), spurious rejection min 60 dB, harmonic rejection typ 40 dB, output min 100 mW, IM3 max -40 dBc at 200 mW PEP, 12 to 14 V at 370 mA. The manual requires a coax relay with at least 50 dB isolation, at most 1 mW into the RX input, and strongly recommends a sequencer. Source: https://db6nt.de/wp-content/uploads/2024/12/MKU-144-G2-Handbuch.pdf . Current Kuhne shop lists 144 MHz transverters at 815 EUR (search snippet, not verified on the shop page): https://shop.kuhne-electronic.com/kuhne/en/shop/konverter-transverte/transverter/ .

**F8. Elecraft XV144 (W, kit/assembled) and K144XV.** 28 to 30 MHz IF, LO 116 MHz, NF < 1 dB (0.8 dB typ), conversion gain 25 dB typ, image rejection > 60 dB, 3rd-order intercept +20 dBm typ, 20 W out, 13.8 V, RX 250 mA. Design choice stated in the manual: "Relays are used for transmit/receive switching to avoid receive performance degradation by diode switches in the signal path"; T/R switching time 3 ms typical. Sources: https://ftp.elecraft.com/XV/Manuals%20Downloads/E740096%20XV%20Transverter%20Owner's%20Manual%20Rev%20F1.pdf ; K144XV 10 W internal module https://elecraft.com/products/k144xv-144-148-mhz-10-w-internal-module .

**F9. Down East Microwave / Q5 Signal L144-28 (W).** NF < 1.0 dB max at 17 dB conversion gain min, 25 W or 50 W linear, 11.5 to 15.5 V, relay T/R with optional 3-step sequencer and an IF-drive-sense protection circuit for the RX IF and mixer. Source: http://q5signal.com/image/catalog/L144-28r1A.pdf .

**F10. Funkamateur / DC8RI 144 MHz transverter kit (DL).** 28 to 30 MHz IF, up to 10 W out, drive either up to 10 mW or up to 10 W, introductory price 320 EUR (2016), positioned as a lower-cost alternative to DB6NT and SSB-Elektronik. Architecture details were not published on the page fetched. Sources: https://dm5hf-chris.blogspot.com/2016/08/144-mhz-transverter-der-fachzeitschrift.html ; https://dm5hf-chris.blogspot.com/2017/01/144-mhz-transverter-vom-funkamateur.html .

**F11. UR3LMZ 144/28 transverter (eBay module) with VK3HN SP-8 IF rig.** Mini-Circuits ADE mixer, BF-series MOSFETs, 116 MHz overtone LO, solid-state T/R switching, 50 mW drive, 10 W capability throttled to 3 to 5 W "for better spectral purity"; builder notes RF feedback in the enclosure needing gain adjustment, and chose a transverter because designing 144 MHz stages "would require special care". Source: https://vk3hn.wordpress.com/2021/01/18/sp-8-a-homebrew-28mhz-ssb-transceiver-for-a-ur3lmz-144mhz-transverter/ .

**F12. G4JNT 144 MHz direct-conversion I/Q receiver (G).** MAR-6 and MAR-3 RF amplifiers with a two-stage 10 MHz BPF, two SRA-1 mixers fed through a PSCQ-2-160 quadrature hybrid (< 3 degrees error 100 to 160 MHz), LO = AD9851 DDS at 16 to 16.67 MHz followed by a x9 multiplier to +10 dBm, NE5532 baseband with voltage gain about 300 and RF-leakage low-pass filtering; target 20 to 25 dB opposite-sideband rejection (3 degrees phase error gives 25 dB). Built as a linear beacon-measurement receiver, not a CW rig. Source: http://g4jnt.com/144MHzDCReceiver.pdf . Direct conversion at 144 MHz is workable but the LO quadrature generation and baseband gain are the hard parts.

**F13. Si5351-based homebrew practice (ZL2CTM, QRP Labs).** ZL2CTM's SSB transceiver drives ADE-1 mixers from Si5351 outputs via 50 ohm pads (2 mA drive strength for homebrew mixers). Source: https://soldersmoke.blogspot.com/2017/08/zl2ctms-homebrew-transciever-project.html . QRP Labs QCX/QMX (5 W HF CW) use a solid-state microcontroller-operated T/R switch, full QSK after the envelope-shaping delay or semi-QSK with a hang time in dits, and a "Normal 5 ms shape" envelope. Sources: QCX manual https://qrp-labs.com/qcx.html (operating instructions, sections on Full/Semi QSK) and QMX manual https://qrp-labs.com/qmx.html .

### C. Receiver performance benchmarks (derived where marked)

**F14. Noise-floor arithmetic.** Thermal noise in 500 Hz is -174 + 27 = -147 dBm. MDS = -147 dBm + NF (derived). NF 1.7 dB (Anglian class) gives -145 dBm; NF 3 dB gives -144 dBm (the IC-705 preamp-on figure); NF 7 dB gives -140 dBm (FT-290R class); NF 14 dB gives -133 dBm (IC-705 preamp off). Given rubber-duck antenna losses and band noise, a system NF of 3 to 5 dB is sufficient for a handheld; the transverter designs above spend their NF budget on EME/contest use.

**F15. Strong-signal benchmarks.** IIP3 around 0 dBm (Anglian, Kuhne derived, XV144 stated +20 dBm without input/output qualifier) versus IC-705 +27 dBm preamp off / +16 dBm on. Reciprocal mixing dynamic range in 500 Hz equals -(LO phase noise) - 27 dB (VA7OJ report formula, page on RMDR). With an LO at -112 dBc/Hz (10 kHz) RMDR is 85 dB; at -127 dBc/Hz it is 100 dB; at -150 dBc/Hz (Anglian 3L at 20 kHz) it is 123 dB; at -156 dBc/Hz (Kuhne) it is 129 dB (derived).

### D. Synthesizers at 144 MHz

**F16. Si5351A-B (Skyworks, datasheet Rev 1.3, 3/2020).** Output 2.5 kHz to 200 MHz; VCO 600 to 900 MHz; crystal 25 or 27 MHz; core IDD 24 mA typ with 4 outputs; CMOS output VOH >= VDD - 0.6 V, rise/fall 1 ns; period jitter 70 ps pk-pk typ (155 max) for the 10-MSOP with all outputs running, with the note "Jitter is highly dependent on device frequency configuration"; "Only two unique frequencies above 112.5 MHz can be simultaneously output." Source: https://download.mikroe.com/documents/datasheets/Si5351-datasheet.pdf (also https://www.skyworksinc.com/-/media/Skyworks/SL/documents/public/data-sheets/Si5351-B.pdf ). Community findings: even-integer output dividers recommended for lowest jitter; I/Q phase offset register is 7 bits (max 127, even divider means max 126), which limits quadrature output to roughly 110 MHz; VCO can be overclocked and outputs measured to about 292 MHz on some devices with degraded SNR beyond 200 MHz. Sources: https://rfzero.net/tutorials/si5351a/ ; http://nic.vajn.icu/PDF/SiliconLabs/Si5351_facts.txt (QRP Labs "facts and myths"); https://groups.io/g/BITX20/topic/si5351_ms5351_quadrature/109985186 . Implication for 144 MHz: 144 MHz needs divider 6 (VCO 864 MHz) or the out-of-spec divider 4; a 133.3 MHz low-side LO for 10.7 MHz IF uses divider 6 (VCO 800 MHz); a 116 MHz transverter LO uses divider 6 (VCO 696 MHz). All are even integers, so the "even divider" rule can be met, but the small divider gives little phase-noise improvement over the VCO.

**F17. Si5351A phase noise reports.** KE5FX (TimePod) at 19.99 MHz: -127 dBc/Hz at 10 kHz; measurements up to 100 MHz published by NT7S. QRP Labs QCX transmitter at HF: -135.6 dBc/Hz at 10 kHz and -135.9 at 50 kHz (Advantest R3361C), matching the ARRL "better than -135 dBc" figure; other Si5351 rigs measured by ARRL: KX2 about -127 dBc/Hz at 10 kHz, uBITX -132 dBc/Hz. A secondary report attributes a Silicon Labs measurement of -112 dBc/Hz at 10 kHz at 156.2 MHz; the primary page could not be fetched (groups.io returned HTTP 402) and this figure is unverified. Sources: https://nt7s.com/2014/11/si5351a-investigations-part-7/ ; https://qrp-labs.com/qcx/phasenoise ; https://soldersmoke.blogspot.com/2015/09/si5351-and-spectral-purity-mask.html (secondary for the 156.2 MHz figure). Derived: HF results benefit from dividers of 20 to 100 (26 to 40 dB below VCO noise); at 144 MHz the divider is 6 (15.6 dB), so expect roughly 15 to 25 dB worse phase noise than the QCX HF number, consistent with the -112 dBc/Hz report. Also, the Si5351 output is a square wave rich in odd harmonics and needs a band-pass or low-pass filter before a mixer (all community sources agree; e.g. https://la3pna.com/2016/12/31/si5351-spurius-preformance/ ).

**F18. ADF4351 (Analog Devices).** 35 MHz to 4400 MHz using a 2200 to 4400 MHz VCO and divide-by-1/2/4/8/16/32/64; open-loop VCO phase noise -89 dBc/Hz at 10 kHz, -114 at 100 kHz, -134 at 1 MHz from a 2.2 GHz carrier; in-band -100 dBc/Hz at 3 kHz from 2111.28 MHz; normalized floor -220/-221 dBc/Hz, normalized 1/f -116/-118 dBc/Hz; output -4 to +5 dBm; supply 3.0 to 3.6 V; current DIDD+AIDD 21 to 27 mA, VCO 70 to 80 mA, RF output 21 to 26 mA, dividers 6 mA per divide-by-2 (about 120 to 170 mA total). Source: datasheet mirror https://www.physics.utoronto.ca/~astummer/Archives/2016%20Nyquie%20Plus/Docs/ADF4351%20AnaDev,%20PLL%20&%20VCO,%2035-4400MHz%20module.pdf (Analog Devices original https://www.analog.com/media/en/technical-documentation/data-sheets/adf4351.pdf ). Derived at 137.5 MHz (2.2 GHz divided by 16, 24 dB): about -113 dBc/Hz at 10 kHz and -124 at 3 kHz in-band, i.e. similar to the Si5351 at VHF but at 5x the current and 15x the price. Price signal (findchips, DigiKey qty 1): $16.08 to $25.16, 9,793 in stock. https://www.findchips.com/search/ADF4351BCPZ .

**F19. MAX2871 (Analog Devices, ex-Maxim).** 23.5 MHz to 6.0 GHz integer-N/fractional-N with integrated VCOs; the datasheet feature list quotes in-band phase noise of -102 dBc/Hz (conditions not captured); the datasheet PDF could not be downloaded during this session (analog.com timeouts). Sources: https://www.analog.com/en/products/max2871.html ; datasheet https://www.analog.com/media/en/technical-documentation/data-sheets/max2871.pdf . Price signal (findchips, DigiKey qty 1): $14.06 to $19.98, 5,248 to 8,522 in stock. https://www.findchips.com/search/MAX2871ETJ%2B . Treat as an ADF4351-class alternative with better close-in noise until the datasheet is read.

**F20. LMX2571 (Texas Instruments, Active).** 10 MHz to 1344 MHz from three VCO cores with output dividers; -123 dBc/Hz at 12.5 kHz and -145 dBc/Hz at 1 MHz at 480 MHz; normalized PLL floor -231 dBc/Hz, normalized 1/f -124 dBc/Hz; spurs better than -75 dBc; 39 mA in synthesizer mode (9 mA PLL-only with external VCO); FastLock < 1.5 ms; FSK/direct modulation; 36-pin WQFN 6 x 6 mm; OSCin 10 to 150 MHz; the datasheet shows about 5 dB worse phase noise with a clipped-sine 26 MHz reference than with a square wave. TI positions it for battery-powered PMR radios. Sources: https://www.ti.com/product/LMX2571 ; https://www.ti.com/lit/ds/symlink/lmx2571.pdf . Derived at 144 MHz (480 MHz divided by 3.33, 10.5 dB): about -133 dBc/Hz at 12.5 kHz if the divider noise floor allows. Price signal (findchips, DigiKey qty 1): $8.75 to $14.46, 1,309 in stock. https://www.findchips.com/search/LMX2571NJKR . On paper this is the best fit for a tunable 144 MHz LO in a battery rig: lowest current of the PLL+VCO options, 20 dB better phase noise than Si5351-at-VHF reports, mid price.

**F21. Reference oscillators.** Si5351A-B-GT price signal $1.10 to $2.19 (DigiKey qty 1, 5,087 in stock; https://www.findchips.com/search/si5351a-b-gt ). A stock 25 MHz crystal (tens of ppm) puts the 144 MHz LO several kHz off and drifting (derived: 30 ppm = 4.3 kHz at 144 MHz), so a TCXO is mandatory. Options: QRP Labs 25 MHz TCXO module, $8.25, measured within +/-0.25 ppm from 4 to 65 C ( https://shop.qrp-labs.com/tcxo ); Abracon ATX-13 26 MHz clipped sine +/-0.5 ppm; Epson TG2520SMN 10 to 55 MHz +/-0.5 ppm (about $0.44 at 3k); SiTime SiT5356 MEMS Super-TCXO 1 to 60 MHz, +/-0.1/0.2/0.25 ppm, LVCMOS or clipped sine, I2C digital tuning, +/-1 ppb per C slope, in production ( https://www.sitime.com/products/super-tcxo/sit5356 ; https://www.epsondevice.com/crystal/en/products/crystal-oscillator/tg2520smn.html ; https://www.digikey.com/en/products/detail/abracon-llc/ATX-13-F-26-000MHZ-F05-T/14000628 ). Derived stability at 144 MHz: 0.5 ppm = 72 Hz, 0.25 ppm = 36 Hz, 0.1 ppm = 14 Hz, all within a 500 Hz CW filter but 0.5 ppm is marginal for a 250 Hz filter or for holding a zero-beat over a long QSO.

### E. 5 W-class PA devices for 144 MHz at 7.4 V (2S Li-ion, 6.0 to 8.4 V)

**F22. NXP AFT05MS006N is EOL / not recommended for new designs.** NXP product page: "This page contains information on a product that is not recommended for new designs", filed under Legacy RF Power; DigiKey listing text: "Not recommended for new design, minimums may apply". Datasheet (Freescale Rev 0, 2/2014) wideband row 136 to 174 MHz: Pin 0.19 W, gain 15.5 dB, drain efficiency 60 %, Pout 6.0 W at 7.5 V, IDQ 100 mA; VDSS 30 V, VGS -6/+12 V, TJ 150 C, RthJC 1.0 C/W, > 65:1 VSWR ruggedness at 520 MHz with 3 dB overdrive, VGS(th) 1.8 to 2.6 V, package PLD-1.5W (SOT1811-2, 6.6 x 5.84 mm). Reference circuits provided only for 520 MHz narrowband, 440 to 520 MHz and 760 to 870 MHz; no 136 to 174 MHz reference PCB in the datasheet. Stock signal: DigiKey listing showed 1,110 units in a search snippet, while the findchips aggregation on 2026-09-25 showed 0 units at DigiKey, Newark, Avnet and TME at $3.74 to $7.30; treat stock as volatile last-time-buy inventory. Sources: https://www.nxp.com/products/radio-frequency-rf/legacy-rf/legacy-rf-power/136-941-mhz-6-0-w-7-5-v-wideband-rf-power-ldmos-transistor:AFT05MS006N ; https://www.nxp.com/docs/en/data-sheet/AFT05MS006N.pdf ; https://www.digikey.com/en/products/detail/nxp-usa-inc/AFT05MS006NT1/4814338 ; https://www.findchips.com/search/AFT05MS006N .

**F23. The rest of NXP's 7.5 V handheld LDMOS family is also EOL.** AFT05MS004N (4 W, SOT-89A): "End of Life", https://www.nxp.com/products/radio-frequency-rf/legacy-rf/legacy-rf-power/136-941-mhz-4-w-7-5-v-wideband-rf-power-ldmos-transistor:AFT05MS004N . AFT05MS003N (3.2 W at 136 to 174 MHz, 17.1 dB gain, 67.1 % efficiency, SOT-89): "no longer manufactured", https://nxp.com/products/rf/rf-power/rf-mobile-radio/3-w-cw-over-1.8-941-mhz-7.5-v-wideband-rf-power-ldmos-transistor:AFT05MS003N . AFT09MS007N, AFM906N, AFM907N are all under Legacy RF Power. The only Active 7.5 V part found is the **AFIC901N** integrated amplifier: 30 dBm (1 W) over 1.8 to 1000 MHz, 27 to 32 dB gain, 24-pin 4 mm QFN, with downloadable 136 to 174 MHz reference PCB design files. Source: https://www.nxp.com/products/rf/rf-power/rf-mobile-radio/30-dbm-over-1-8-1000-mhz-7-5-v-airfast-wideband-integrated-rf-ldmos-amplifier:AFIC901N . No findchips pricing was returned for AFIC901N.

**F24. Mitsubishi Electric RD series: partly current, partly gone.** Mitsubishi's current silicon RF discrete list (2025/2026) includes RD12MVS1, RD10MMS2, RD08MUS2, RD07MUS2B, RD06LUS2, RD04HMS2, RD04LUS2, RD02LUS2, RD02MUS2, RD01MUS2B, RD01MUS3, RD01MUS2, RD00LUS2 and the 12.5 V high-power HxF1C/HUP2 parts; the classic amateur parts RD06HVF1, RD15HVF1, RD16HHF1 and RD07MVS1 are absent and RF Parts lists them as new-old-stock "no longer available for export". Source: https://www.mitsubishielectric.com/semiconductors/hf/products/sirf/index.html ; https://www.rfparts.com/rftransistors/transistor-rd.html . Candidates for 7.4 V:
- **RD07MUS2B** (7.2 V, 7 W, 175/527/870 MHz): datasheet Pout 7.2 W typ at 175 MHz with Pin 0.3 W, 65 % efficiency, IDQ 250 mA, VDSS 25 V, load VSWR 20:1 all phases without destruction, RthJC 2.5 C/W, SLP package; Mitsubishi Electric US page shows status "Active (mass production)" with distributors Mitsubishi Electric US, Telepro and Diamond Advanced Components; not stocked at DigiKey/Mouser/RFMW; RF Parts sells NOS at $4.91. Sources: https://www.mitsubishielectric.com/semiconductors/hf/products/datasheet/rd07mus2b.pdf ; https://meus-semiconductors.com/products/high-frequency-devices/rd07mus2b ; https://www.rfparts.com/rftransistors/transistor-rd/rd07mus2b.html .
- **RD12MVS1** (7.2 V, 12 W at 175 MHz, Pin 1.0 W, 57 % efficiency, IDQ 1.0 A, VDSS 50 V, RthJC 2.5 C/W): more power than needed and 1 A quiescent is hostile to a battery rig. Source: https://www.mitsubishielectric.com/semiconductors/hf/products/datasheet/rd12mvs1.pdf .
- **RD06LUS2** (new, sampled Feb 2024): 6.5 W at 3.6 V, 65 % efficiency, but VDD operating max 5 V and VDSS 14 V, so it cannot run from a 2S pack directly. Sources: https://www.mitsubishielectric.com/news/2024/0227.html ; https://www.mitsubishielectric.com/semiconductors/hf/products/datasheet/rd06lus2.pdf .
- **RA07M1317M** module (135 to 175 MHz, 6.5 W, 7.2 V, two-stage): RF Parts marks the -101 variant END OF LIFE 2017; NOS only. Source: https://www.rfparts.com/ra07m1317m-501.html .
- RD07MVS1 / RD07MVS1B (7.2 V, 175 to 520 MHz): NOS only at RF Parts. Source: https://www.rfparts.com/rd07mvs1.html .

**F25. Other device families.** Renesas RQA0009 family (UPAK, +38 dBm at 6 V, 520 MHz) exists but its lifecycle status was not confirmed ( https://www.renesas.com/us/en/products/power-power-management/discrete-power-devices/power-mosfets/rqa0009txdqs-n-channel-mosfet ). Ampleon (the NXP RF power spin-off) lists no 7.5 V handheld transistor in the search results. Vintage bipolars (2SC1971 class) are obsolete and a counterfeit risk; not recommended. Practical PA line-up options for 5 W: (a) RD07MUS2B final driven at about +25 dBm by an AFIC901N or a MMIC; (b) last-time-buy AFT05MS006N with a cwht-designed 136 to 174 MHz match (no vendor reference for that band); (c) a 12.5 V-class device behind a boost converter (adds a switcher and its spurs to a receiver-adjacent board). Derived: LDMOS Pout scales roughly with VDD squared, so a design giving 5 W at 7.4 V gives about 3.3 W at 6.0 V (cell cut-off) and about 6.4 W at 8.4 V unless regulated or ALC-limited. At 60 % efficiency 5 W needs about 8.3 W DC, about 1.1 A at 7.4 V.

### F. Regulatory constraints on the transmitter

**F26. 47 CFR 97.307(e) (current as of 2026-01-14, 91 FR 1431).** For transmitters between 30 and 225 MHz spurious emissions must be at least 60 dB below the mean power of the fundamental; for a transmitter of 25 W or less, spurious emissions "must not exceed 25 uW and must be at least 40 dB below the mean power of the fundamental emission, but need not be reduced below the power of 10 uW." 97.307(a) to (c): occupy no more bandwidth than necessary, no splatter or key-click interference, reduce spurious emissions "to the greatest extent practicable". 97.305(a): CW may be transmitted on any frequency authorized to the control operator; the 2 m table row for other emissions starts at 144.1 MHz, so 144.0 to 144.1 MHz is CW-only in effect. Sources: https://www.law.cornell.edu/cfr/text/47/97.307 ; https://www.law.cornell.edu/cfr/text/47/97.305 (ecfr.gov redirected to https://unblock.federalregister.gov/ for automated access; the Cornell mirror carries the same amendment note). Derived for 5 W (+37 dBm): the 25 uW (-16 dBm) cap is tighter than the 40 dB rule (-3 dBm), so every harmonic and spur must be at least 53 dB below carrier; the transverters above show 2nd harmonics of -40 dBc before the low-pass filter, so the output LPF must supply about 15 dB at 288 MHz plus margin. 47 CFR 2.202 gives CW necessary bandwidth Bn = B x K with K = 5 (fading) or 3 (non-fading); example 25 WPM, B = 20 baud, Bn = 100 Hz (100HA1A). Source: https://www.law.cornell.edu/cfr/text/47/2.202 .

### G. T/R switching

**F27. PIN diodes.** NXP BAP64-02 (Rev 11, 2019): VR 175 V, IF max 100 mA, Ptot 715 mW at Tsp 90 C, forward resistance 0.7 ohm at 100 mA and 2.0 ohm at 10 mA (100 MHz), Cd 0.23 pF at 20 V, carrier lifetime 1.55 us. Source: https://www.nxp.com/docs/en/data-sheet/BAP64-02.pdf . Derived at 5 W into 50 ohm: peak RF voltage 22.4 V, peak current 0.45 A, RMS current 0.32 A. A series PIN at the antenna therefore needs a bias current well above 0.1 A or a diode with long carrier lifetime relative to 144 MHz, and a shunt PIN needs reverse bias above 22 V; the BAP64-02 is suitable for the low-level switching where G4DDK uses it, not as the sole 5 W antenna switch. Elecraft explicitly chose relays over diode switches for receive performance (F8); Kuhne requires a coax relay (F7); Icom uses a T/R relay in the IC-705 (F5); the FT-817 is reported to use PIN diodes at 5 W (F4, unverified). Classic HF PIN QSK designs (W8ZR, W6JL, Ameritron QSK-5) use high-voltage, high-current PIN diodes with quarter-wave sections. Sources: https://w8zr.net/QSK/qsk_QST.pdf ; https://www.frostburg.edu/personal/latta/ee/qsk5/trswitch/trswitch.html .

**F28. Signal relays.** Omron G6K-2F-RF (DPDT, 10.3 x 6.9 x 5.4 mm, 100 mW coil): operate time 3 ms max (about 1.4 ms actual), release 3 ms max (about 1.3 ms), rated carry current 1 A, maximum carry power 3 W and maximum switching power 1 W at VSWR 1.2 max, insertion loss 0.2 dB max at 1 GHz. Source: https://omronfs.omron.com/en_US/ecb/products/pdf/en-g6k_2f_rf.pdf . The 3 W carry rating excludes it as a single-element 5 W antenna relay; a larger signal relay or a split path (relay carries RX only, PA output goes straight to the LPF and antenna with the RX port isolated) is needed. Elecraft's relay-based XV achieves 3 ms T/R (F8). Relay timing of 1.3 to 3 ms rules out true QSK at paddle speeds unless the receiver is muted electronically during the transition and the relay only follows the PTT envelope (semi break-in).

**F29. Keyer timing constraints (straight key and iambic paddles).** ARRL keying tests run 20 ms on / 20 ms off (60 WPM PARIS); at 30 WPM an element is 40 ms (G3OTK). QRP Labs AN005 warns "the rise/fall speed must never be more than the symbol rate" and its Key OUT line overhangs key-up by the fall time. Derived: with 5 ms rise and 5 ms fall, a 20 ms element spends half its time in transition; at 40 WPM (30 ms dit) a 3 ms relay plus 5 ms shaping still leaves about 22 ms steady state, so semi break-in with a relay is workable up to 40 WPM but full QSK between elements needs a solid-state (PIN or FET) switch. The IC-705 supports 6 to 48 WPM iambic B with QSK via relay (its ARRL keying photos at 60 WPM show the first two dits intact). Sources: https://www.qrp-labs.com/images/appnotes/AN005_A4.pdf ; F5; F13.

### H. Keying envelope shaping

**F30. Recommended rise/fall and its effect on bandwidth.** ARRL recommends about 5 ms rise and fall (measured 10 to 90 %) for a 30 WPM fading circuit and 10 ms for non-fading; ARRL Lab measures keying at 20 ms on/off. G3OTK (SPICE study): square-wave keying at 12.5 Hz dot rate reaches -60 dBc only at about 12.5 kHz (25 kHz bandwidth); a 5 ms linear ramp is 20 dB better at 500 Hz but the slope discontinuities still spread; a raised cosine with the same maximum slope reaches -60 dBc just under 300 Hz (600 Hz bandwidth); a 4-pole Gaussian-to-6 dB low-pass (F3dB 70 Hz) approximating the raised cosine reaches -60 dBc above 230 Hz (460 Hz bandwidth). Sources: http://www.ivarc.org.uk/uploads/1/2/3/8/12380834/keyclicks_version_1.pdf ; ARRL Test Procedures Manual https://www.arrl.org/files/file/Technology/tis/info/pdf/Procedure%20Manual%202010%20with%20page%20breaks.pdf (5 ms recommendation quoted via search snippet and G3OTK; the PDF text was not extracted in this session).

**F31. Implementation practice.** QRP Labs (5 W PA kit, AN005): an 8-bit R-2R DAC drives a discrete power modulator with foldback current limiting on the PA drain supply; a microcontroller writes a raised-cosine sequence with rise/fall adjustable 2 to 113 ms; "Practically, 5 to 10 ms is most commonly used"; RC1 keyer chip and QCX/QMX firmware do the same in software. Sources: https://www.qrp-labs.com/images/appnotes/AN005_A4.pdf ; https://qrp-labs.com/pa.html ; http://shop.qrp-labs.com/rc1 . For an LDMOS final the same result can come from modulating the driver stage supply or the gate bias (NXP LDMOS bias note: quiescent current is set by DC gate voltage, https://community.nxp.com/pwmxy87654/attachments/pwmxy87654/Power-Management/695/1/Bias%20setting%20instructions%20LDMOS%20RF%20Power%20Amplifiers.pdf ). On the RP2350 this is a PWM or SPI-DAC waveform task with the keyer as the timing master.

### I. Crystal filters for 500 Hz CW

**F32. Homebrew ladder filters.** Rule of thumb from several builders: 4 to 8 identical fundamental crystals (9 or 10 MHz), crystals matched to within 100 Hz (giangrandi) and to better than 50 Hz for a 500 Hz filter (search summary of DJ6EV/Dishal practice), passband asymmetric (slower skirt below the passband). Measured examples: 4-pole 10 MHz filter 520 Hz at -3 dB, 4,360 Hz at -60 dB (shape factor 8.4:1), 34 ohm terminations ( https://www.giangrandi.org/electronics/xtalfilters/xtalfilters.shtml ); 5-pole 9 MHz 500 Hz filter with IQD LFXTAL064523 crystals and a 50:200 ohm transformer, 3-pole 330 Hz design measured 400 Hz at -3 dB and 600 Hz at -6 dB ( http://land-boards.com/blwiki/index.php?title=Crystal_Filter_Design ); 8-pole 9 MHz filter modelled at 700 Hz in Dishal and measured 548 Hz at -6 dB with ECS-90-S-4X crystals matched within 20 Hz (search summary). Design tools: DJ6EV Dishal program ( https://www.bartelsos.de/filter/quarzfilter/quarzfilter-dj6ev ; help file https://warc.org.uk/wp-content/uploads/2014/01/eDishalHelp.pdf ) and QEX Nov/Dec 2009 "Crystal Ladder Filters for All" ( https://www.arrl.org/files/file/QEX_Next_Issue/Nov-Dec_2009/QEX_Nov-Dec_09_Feature.pdf ). Insertion loss is typically several dB and rises as bandwidth narrows; Dishal assumes lossless parts.

**F33. Commercial filters.** KVG XF-9NB (9.0 MHz, CW, 8 poles, 6 dB bandwidth +/-0.25 kHz = 500 Hz, insertion loss max 6.5 dB, ripple 1 dB, shape factor 6:60 = 1:2.2 and 6:80 = 1:4.0, ultimate attenuation > 100 dB, termination 500 ohm // 30 pF, -10 to +60 C, case BF-1) and XF-9P (250 Hz, 7.5 dB IL); price by quotation only. Source: https://www.kn34pc.com/spr/quartz_filters_ge/spr_kvg_9_mhz_standard_filter.pdf ; KVG catalogues via https://pdf.directindustry.com/pdf/kvg-quartz-crystal-technology-gmbh/discrete-crystal-filters-10-mhz-107-mhz/82515-750637.html . Inrad's 455 kHz 400 Hz filter lists at $174.25 as a price signal for boutique CW filters ( http://www.inrad.net/product.php?printable=Y&productid=130 ). Off-the-shelf 10.7 MHz MCFs (Golledge GMCF-10, 7.5 kHz) and 45 MHz MCFs (ECS/YIC, 15 kHz, at DigiKey) are FM/roofing parts, not CW filters ( https://www.golledge.com/products/gmcf-10-10g7c/c-26/p-2490 ; https://www.digikey.com/en/products/detail/yic/MCF45M15A-SM756/21804189 ). Krystaly Hradec Kralove builds custom crystal and monolithic filters to order ( https://www.krystaly.cz/en/products/filters/ ).

**F34. Turnkey-assembly conflict.** Every homebrew ladder-filter source relies on measuring 20 to 40 crystals and hand-selecting matched sets. A PCBWay turnkey build cannot do that; the choices are a commercial filter (KVG/Krystaly), a ladder filter designed to tolerate the catalogue tolerance of a tight-spec crystal (with the response verified by Monte Carlo in SPICE), or moving the 500 Hz selectivity into DSP on the RP2350 with a wider analog filter ahead of it (the QMX approach).

### J. Front-end devices (for the mixer/LNA trades)

**F35.** Mini-Circuits PGA-103+: NF 0.5 dB at 0.05 to 0.5 GHz, 0.6 dB to 1 GHz, OIP3 +45 dBm at 5 V, P1dB +22.5 dBm, operating current 97 mA at 5 V or 60 mA at 3 V, SOT-89. Source: https://www.minicircuits.com/pdfs/PGA-103+.pdf ; G4DDK preamp note http://www.g4ddk.com/PGA103amp.pdf . Qorvo SPF5189Z (NF about 0.5 dB at 145 MHz) reached end of life in March 2021 with QPL9547 as replacement ( https://www.qorvo.com/products/p/SPF5189Z ). G4DDK moved from SPF5043 to PSA4-5043 and MGA30689 for quieter bias regulators (F6). The 97 mA of the PGA-103+ at 5 V is a real battery cost for a handheld; the Anglian/Kuhne front ends spend that current because they chase 0.5 dB NF.

## Comparison tables

### Table 1. Reference designs

| Design | Type / origin | Receiver topology | LO | Selectivity | NF / MDS (500 Hz) | IIP3 or DR | TX | T/R | Notes |
|---|---|---|---|---|---|---|---|---|---|
| Icom IC-202 (1976) | Commercial portable, JA | Single conversion, 10.7 MHz IF | VXO 14.8 MHz x9 = 133.3 MHz | 10.7 MHz crystal filter (SSB) | not published | not published | 3 W PEP | not published | 4 x 200 kHz segments; "excellent receiver" reputation |
| Yaesu FT-290R (1981) | Commercial portable, JA | 10.81 MHz IF (+455 kHz FM) | PLL | 2.4 kHz/-6 dB, 4.1 kHz/-60 dB | 0.5 uV / 20 dB S/N (derived NF about 7 dB) | not published | 2.5 / 0.5 W | not published | 60 mA RX, 800 mA TX |
| Mizuho MX-2 | Commercial handheld, JA | VXO superhet | VXO, 50 kHz per crystal | not published | not published | not published | 0.2 W | not published | Pocket 2 m SSB/CW precedent |
| Yaesu FT-817/818 | Commercial portable, JA | 68.33 MHz / 455 kHz | PLL | 500 Hz option | MDS about -137 dBm | not captured | 5 / 6 W | PIN (reported) | Double conversion |
| Icom IC-705 (2020) | Commercial portable, JA | Heterodyne to direct sampling | DDS/PLL | DSP | -133 / -144 dBm (pre off/on) | 83 / 81 dB IMD DR at 20 kHz; BDR 122 dB; IP3 +27/+16 dBm | 5 W (10 W ext) | Relay | 68 dB spur suppression at 144 MHz; QSK photos at 60 WPM |
| G4DDK Anglian 3L | Kit transverter, G | 144 to 28 MHz, ADE-1H level 17 | 116 MHz 5th-overtone Butler + PHEMT, -150 dBc/Hz at 20 kHz | 3-pole LC BPF (IF rig does the rest) | 1.6 to 1.8 dB / about -145 dBm | IIP3 better than 0 dBm | +20 dBm P1dB | BAP64 PIN (low level), external relay, 200 ms sequencing | Best-documented homebrew 2 m front end |
| Kuhne MKU 144 G2 | Commercial module, DL | 144 to 28 MHz, +17 dBm ring mixer | 116 MHz heated Butler, -156 dBc/Hz at 10 kHz | 3-pole helical | 0.9 dB typ / about -146 dBm | OIP3 +23 dBm at 25 dB gain | 100 mW | Coax relay + sequencer required | 370 mA at 12 V; about 815 EUR class |
| Elecraft XV144 / K144XV | Kit transverter, W | 144 to 28 MHz | 116 MHz | IF rig | < 1 dB (0.8 typ) | IP3 +20 dBm (qualifier not stated) | 20 W (10 W module) | Relays, 3 ms | Relays chosen to avoid diode-switch degradation |
| Q5 Signal L144-28 | Commercial transverter, W | 144 to 28 MHz | crystal | IF rig | < 1.0 dB max | not published | 25 / 50 W | Relays + sequencer | IF-drive protection circuit |
| Funkamateur / DC8RI | Kit transverter, DL | 144 to 28 MHz | not published | IF rig | not published | not published | 10 W | not published | 320 EUR intro (2016) |
| UR3LMZ | eBay module, UR | 144 to 28 MHz, ADE mixer | 116 MHz overtone | IF rig | not published | not published | 3 to 5 W (throttled for purity) | Solid state | RF feedback in enclosure reported |
| G4JNT DC receiver | Homebrew, G | Direct conversion I/Q at 144 MHz | AD9851 DDS x9 (+10 dBm), PSCQ-2-160 hybrid | Audio/SDR | not published | linear, no AGC | RX only | n/a | 20 to 25 dB sideband rejection target |

### Table 2. Synthesizer options for a 144 MHz-class LO

| Device | Range | Phase noise (datasheet or report) | Derived at about 144 MHz, 10 kHz offset | Current | Ref input | Price signal, qty 1 (2026-09-25) | Notes |
|---|---|---|---|---|---|---|---|
| Si5351A-B | 2.5 kHz to 200 MHz (VCO 600 to 900 MHz) | -127 dBc/Hz at 20 MHz (KE5FX); -135 at HF (QCX); -112 at 156 MHz (unverified report) | about -110 to -115 (divider 6) | 24 mA core + 2 mA per output | 25/27 MHz crystal or TCXO | $1.10 to $2.19 (DigiKey) | Square-wave outputs need filtering; I/Q only to about 110 MHz; 2 outputs above 112.5 MHz |
| LMX2571 | 10 to 1344 MHz | -123 dBc/Hz at 12.5 kHz at 480 MHz; floor -231 | about -133 | 39 mA (synth mode) | 10 to 150 MHz; square wave 5 dB better than clipped sine | $8.75 to $14.46 (DigiKey) | Active; PMR/battery oriented; FastLock; FSK |
| ADF4351 | 35 to 4400 MHz | VCO -89 at 10 kHz at 2.2 GHz; in-band -100 at 3 kHz; floor -220/-221 | about -113 | 120 to 170 mA | 10 to 250 MHz | $16.08 to $25.16 (DigiKey) | ADIsimPLL models; high current for a handheld |
| MAX2871 | 23.5 MHz to 6 GHz | in-band -102 dBc/Hz (feature list; conditions not captured) | not derived | not captured | not captured | $14.06 to $19.98 (DigiKey) | Datasheet not read this session |
| Fixed 116 MHz overtone crystal LO (Anglian/Kuhne style) | fixed | -150 (20 kHz) to -156 (10 kHz) dBc/Hz | n/a | 30 to 100 mA incl. amplifier/heater | crystal | crystal about 10 to 30 EUR, custom | Requires a tunable IF stage; tuning range set by the IF |

### Table 3. PA device candidates for 5 W at 7.4 V, 144 MHz

| Device | Vendor status (2026-09) | Rated | 136 to 175 MHz datasheet data | Package / RthJC | Stock and price signal | Vendor reference circuit |
|---|---|---|---|---|---|---|
| AFT05MS006N | EOL, not recommended for new designs (NXP; DigiKey note) | 6 W, 7.5 V, 136 to 941 MHz | Pin 0.19 W, 15.5 dB, 60 %, 6.0 W; IDQ 100 mA; VDSS 30 V; > 65:1 VSWR | PLD-1.5W / 1.0 C/W | 0 to 1,110 units reported by different snapshots; $3.74 to $7.30 | 520 MHz, 440 to 520 MHz, 760 to 870 MHz only |
| AFT05MS004N | EOL | 4 W, 7.5 V | 15.4 to 20.9 dB gain, 49 to 75 % efficiency (band not resolved) | SOT-89A | not captured | not captured |
| AFT05MS003N | No longer manufactured | 3.2 W, 7.5 V | 17.1 dB, 67.1 %, 3.2 W | SOT-89 | none | none listed |
| AFIC901N | Active | 1 W, 7.5 V, 1.8 to 1000 MHz, 27 to 32 dB gain | 136 to 174 MHz reference design files | 4 mm QFN-24 | no findchips result | yes, 136 to 174 MHz |
| RD07MUS2B | Active (mass production) per Mitsubishi Electric US; not at DigiKey/Mouser/RFMW | 7 W, 7.2 V, 175/527/870 MHz | Pin 0.3 W, 7.2 W typ, 65 %; IDQ 250 mA; VDSS 25 V; 20:1 VSWR | SLP / 2.5 C/W | RF Parts NOS $4.91; Mitsubishi US, Telepro, Diamond Advanced Components | test-fixture matching data and S-parameters in datasheet |
| RD12MVS1 | Listed in current lineup | 12 W, 7.2 V, 175 MHz | Pin 1.0 W, 12 W, 57 %; IDQ 1.0 A; VDSS 50 V | 2.5 C/W | not captured | 175 MHz test fixture in datasheet |
| RD06LUS2 | New (samples Feb 2024) | 6.5 W, 3.6 V, 520 MHz | 135 MHz data at 4.4 V; VDD max 5 V | dual-chip pkg / 0.8 C/W | not captured | yes, but 3.6 V only |
| RA07M1317M module | EOL 2017 (RF Parts) | 6.5 W, 7.2 V, 135 to 175 MHz | two-stage module | module | NOS only | module |

### Table 4. T/R switch elements

| Element | Speed | 5 W suitability | RX-path penalty | Sources |
|---|---|---|---|---|
| BAP64-02 PIN | microseconds | Not as sole antenna switch (IF max 100 mA vs 0.45 A peak RF; Ptot 715 mW) | Good IMD when biased (G4DDK) | F27 |
| High-current/high-voltage PIN (QSK-class) | microseconds | Yes with > 22 V reverse bias and adequate forward current | Requires bias supply and quarter-wave or lumped isolation | F27 |
| Omron G6K-2F-RF relay | 1.3 to 3 ms | No as single element (3 W carry, 1 W switching) | Negligible loss (0.2 dB at 1 GHz) | F28 |
| Larger signal relay / coax relay | 3 to 10 ms | Yes | None; Elecraft/Kuhne/Icom choice | F7, F8, F5 |
| FET/solid-state (QCX/QMX style) | microseconds | Proven at 5 W HF; VHF layout care needed | Diode limiter on RX input | F13 |

## Implications for cwht

Tags: REQ-candidate (requirement to write), RISK-candidate (for the risk register), DECISION-needed (PDR trade study or ADR), ACTION (task).

1. **REQ-candidate (spurious):** Every transmitter spurious and harmonic emission at 5 W shall be at least 53 dB below carrier and below 25 uW absolute, per 47 CFR 97.307(e) (derived from F26). Verification: Analysis (LTspice harmonic balance of the LPF) then Bench (spectrum analyzer or tinySA with attenuator).
2. **REQ-candidate (keying bandwidth):** CW envelope rise and fall time shall default to 5 ms (10 to 90 %), be configurable, and follow a raised-cosine or Gaussian-shaped profile such that keying sidebands are at least 60 dB down beyond +/-300 Hz (F30). Verification: Emulation of the DAC sequence, Bench spectrum at 60 WPM per ARRL method.
3. **REQ-candidate (keyer/T-R):** The keyer shall support straight key and iambic paddles (mode A/B) from at least 5 to 40 WPM with per-element T/R sequencing; break-in mode (semi or full) shall be a configuration item; envelope fall shall complete before the T/R switch opens (F29, F31, AN005 rule).
4. **REQ-candidate (stability):** LO frequency error and drift shall be within +/-50 Hz at 144 MHz over 0 to 50 C and 30 minutes, implying a reference of 0.25 ppm or better or a calibration scheme (F21).
5. **REQ-candidate (receiver):** MDS at least -140 dBm in 500 Hz (NF <= 7 dB, FT-290R class) with a stretch of -144 dBm (NF 3 dB, IC-705 preamp-on class); IIP3 at least -10 dBm; reciprocal mixing dynamic range at least 85 dB at 10 kHz (F14, F15). These are proposals to be sized against the ConOps, not ceilings.
6. **RISK-candidate (PA obsolescence, high):** The specified AFT05MS006N and its whole 7.5 V family are EOL at NXP with volatile distributor stock (F22, F23). Mitigation: last-time-buy a project-lifetime quantity now, or baseline RD07MUS2B (Active) with a confirmed authorized-channel quote, and design the PA footprint/match so a second device can be substituted.
7. **RISK-candidate (PA reference circuit gap):** No vendor 136 to 174 MHz reference PCB exists for AFT05MS006N; the RD07MUS2B datasheet gives test-fixture impedances and S-parameters but no PCB. The 144 MHz match must be designed and SPICE/S-parameter verified in-house (F22, F24).
8. **RISK-candidate (battery voltage droop):** Pout falls to about 3.3 W at 6.0 V cell cut-off and rises to about 6.4 W at 8.4 V without regulation (F25). Decide between regulated PA supply, ALC via the envelope DAC, or accepting droop in the requirement.
9. **RISK-candidate (LO phase noise at VHF):** A Si5351 at 144 MHz runs its divider at 6 and reports suggest about -112 dBc/Hz at 10 kHz, some 20 dB worse than its HF reputation; this bounds reciprocal mixing to about 85 dB (F16, F17). Acceptable for a handheld but poor next to transverter-class LOs (F6, F7).
10. **RISK-candidate (turnkey assembly vs matched crystals):** Hand-matched crystal ladder filters are incompatible with PCBWay turnkey assembly (F34).
11. **RISK-candidate (PIN diode ratings at 5 W):** Small-signal PIN diodes such as BAP64-02 cannot carry 5 W as the series element (F27); Elecraft and Kuhne avoided diode antenna switching for performance reasons (F7, F8).
12. **RISK-candidate (RX protection):** Kuhne requires <= 1 mW at the RX input and >= 50 dB isolation during TX; a 5 W transmitter needs >= 37 dB isolation plus a limiter to meet that (F7).
13. **DECISION-needed (receiver architecture), PDR trade study:** (A) single-conversion superhet at 144 MHz with a tunable Si5351 or LMX2571 LO and a 9 or 10.7 MHz crystal filter (FT-290R/IC-202 pattern); (B) internal transverter: fixed low-noise 116 MHz overtone LO into a 28 MHz IF where a Si5351 performs well (divider about 30, quadrature available), followed by a QSD/DSP or a second conversion to a crystal filter (Anglian/Kuhne/XV144 front end plus QCX/QMX back end); (C) direct conversion I/Q at 144 MHz with DSP on the RP2350 (G4JNT pattern; quadrature LO above 110 MHz is the blocker for Si5351, so it needs LMX2571/ADF4351 plus a divider or a hybrid); (D) commercial transverter module plus a 28 MHz CW rig (rejected for size and cost, kept as a fallback).
14. **DECISION-needed (synthesizer and reference):** Si5351A ($1) vs LMX2571 ($9 to $14, 39 mA, about 20 dB better phase noise on paper) vs ADF4351/MAX2871 ($14 to $25, 120+ mA), and TCXO grade 0.5 / 0.25 / 0.1 ppm (Epson TG2520SMN, Abracon ATX-13, QRP Labs module, SiTime SiT5356 with I2C trim). The LMX2571 datasheet penalises clipped-sine references by 5 dB, which couples the two choices.
15. **DECISION-needed (CW selectivity):** commercial 8-pole 9 MHz filter (KVG XF-9NB, quote), tolerance-designed ladder filter with tight-spec catalogue crystals verified by Monte Carlo, or DSP selectivity on the RP2350 behind a wider analog filter.
16. **DECISION-needed (PA device and supply topology):** RD07MUS2B vs last-time-buy AFT05MS006N vs AFIC901N-driven line-up vs 12.5 V device behind a boost converter; direct 2S vs regulated; thermal path through the machined enclosure (RthJC 1.0 vs 2.5 C/W matters at 5 W and 60 % efficiency).
17. **DECISION-needed (T/R architecture and break-in):** relay rated >= 5 W carry (semi break-in, 3 ms) vs PIN/FET solid-state switch (full QSK) vs hybrid (PIN or FET for RX isolation, PA output permanently on the LPF/antenna path). Owner input needed on whether full QSK is a requirement given paddle operation.
18. **DECISION-needed (envelope shaping node):** PA drain supply modulator (QRP Labs proven at 5 W HF), driver-stage supply modulation, or gate-bias modulation of the LDMOS; and who owns the waveform (RP2350 PWM/DAC as keyer master).
19. **DECISION-needed (front-end current budget):** PGA-103+ (0.5 dB NF, 97 mA at 5 V) vs lower-current MMIC or discrete stage with 2 to 3 dB NF; the handheld does not need transverter-class NF.
20. **ACTION:** Pull the MAX2871 datasheet and record its normalized floor and current; pull the LMX2571 closed-loop plots for a 144 MHz output (Figures 2 to 5 are images) to replace the derived estimate.
21. **ACTION:** Request quotes and lifecycle letters: Mitsubishi Electric US or Telepro for RD07MUS2B; KVG (or Krystaly) for an XF-9NB-class 500 Hz filter; SiTime SiT5356 25 MHz LVCMOS pricing.
22. **ACTION:** Find the primary source for the Si5351 -112 dBc/Hz at 156.2 MHz figure or measure a Si5351 at 144 MHz on the bench (owner has a NanoVNA and tinySA-class tools; a phase-noise-capable analyzer would have to be borrowed).
23. **ACTION:** Verify the FT-817 PIN-diode T/R claim in the service manual and capture its diode part numbers as a 5 W PIN precedent.

## Confidence

| Finding | Confidence | Basis |
|---|---|---|
| F1 to F3 (IC-202, FT-290R, MX-2) | Medium | Secondary databases and enthusiast pages; consistent across sources; sensitivity for IC-202 not found |
| F4 (FT-817) | Medium | KA7OEI measured pages; PIN-diode claim from Wikipedia only (Low) |
| F5 (IC-705 ARRL numbers) | High | ARRL Lab table text extracted from the reprint PDF |
| F6 (Anglian) | High | Author's technical descriptions with measured tables |
| F7 (Kuhne MKU 144 G2) | High for specs; Low for price | Manufacturer manual; price from a search snippet |
| F8, F9 (XV144, L144-28) | High | Manufacturer manuals |
| F10, F11 (DC8RI kit, UR3LMZ) | Medium | Builder blogs, no vendor data |
| F12 (G4JNT) | High | Author's note |
| F13 (QCX/QMX, ZL2CTM) | High for QRP Labs; Medium for ZL2CTM | Manuals; blog summary |
| F14, F15 (derived benchmarks) | High for arithmetic; inputs as above | Standard formulas |
| F16 (Si5351 datasheet) | High | Datasheet Rev 1.3 text |
| F17 (Si5351 phase noise) | Medium for HF numbers; Low for 156.2 MHz figure | QRP Labs and NT7S primary; VHF figure secondary and unverified |
| F18 (ADF4351) | High | Datasheet text |
| F19 (MAX2871) | Low | Datasheet not read; feature-list snippet only |
| F20 (LMX2571) | High for specs; Medium for derived 144 MHz value | Datasheet and TI page |
| F21 (references/TCXO) | Medium | Vendor pages and QRP Labs shop; prices partly missing |
| F22, F23 (NXP EOL) | High | NXP product pages state EOL/legacy; DigiKey note |
| F24 (Mitsubishi status) | Medium | Mitsubishi lineup page and MEUS "Active" page; no authorized-distributor stock seen |
| F25 (alternatives, droop) | Medium/derived | Renesas status unverified; scaling is a rule of thumb |
| F26 (CFR) | High | Cornell LII text current to 2026-01-14 |
| F27, F28 (PIN, relay) | High | Datasheets |
| F29 (keyer timing) | High for numbers; Medium for the QSK judgement | AN005, ARRL, G3OTK |
| F30 (shaping) | High for G3OTK; Medium for ARRL 5 ms (text not extracted) | Paper; ARRL via secondary quotes |
| F31 (implementation) | High | QRP Labs AN005 |
| F32 to F34 (filters) | Medium | Multiple builder pages agree; KVG sheet primary; prices missing |
| F35 (front-end devices) | High | Datasheets and vendor EOL notice |

## Open items

1. MAX2871 datasheet (phase noise floor, current, output level) not retrieved; analog.com timed out repeatedly.
2. Primary source for the Si5351 -112 dBc/Hz at 10 kHz at 156.2 MHz measurement (groups.io thread returned HTTP 402).
3. ARRL Test Procedures Manual text (5 ms rise/fall definition, keying sideband method) not extracted; cited via secondary quotes.
4. Authorized-channel stock and price for RD07MUS2B (Mitsubishi Electric US, Telepro, Diamond Advanced Components) and lifecycle letter; RFMW search returned no result.
5. Price and lead time for KVG XF-9NB or a Krystaly custom 500 Hz 9 MHz filter.
6. Icom IC-202 receiver sensitivity and Yaesu FT-818 ARRL 2 m table (the DX Engineering FT-818 review URL returned HTML, not the PDF).
7. Kuhne MKU 144 G3 specification and current price (only G2 manual and a shop snippet found).
8. Candidate high-current PIN diodes and >= 5 W signal relays with datasheet-confirmed RF carry ratings; FT-817 T/R diode part numbers.
9. AFIC901N stock and price (no findchips result).
10. hamspirit.net DL "2m (QRP) CW/SSB Transceiver" thread was unreachable (connection refused); may name additional DL homebrew designs.
11. A directly measured Si5351 phase-noise figure at 144 MHz for the cwht LO plan, or an LMX2571 evaluation, before the synthesizer ADR is closed.

## Sources

- NXP AFT05MS006N product page: https://www.nxp.com/products/radio-frequency-rf/legacy-rf/legacy-rf-power/136-941-mhz-6-0-w-7-5-v-wideband-rf-power-ldmos-transistor:AFT05MS006N
- NXP AFT05MS006N datasheet: https://www.nxp.com/docs/en/data-sheet/AFT05MS006N.pdf
- NXP AFT05MS004N page: https://www.nxp.com/products/radio-frequency-rf/legacy-rf/legacy-rf-power/136-941-mhz-4-w-7-5-v-wideband-rf-power-ldmos-transistor:AFT05MS004N
- NXP AFT05MS003N page: https://nxp.com/products/rf/rf-power/rf-mobile-radio/3-w-cw-over-1.8-941-mhz-7.5-v-wideband-rf-power-ldmos-transistor:AFT05MS003N
- NXP AFIC901N page: https://www.nxp.com/products/rf/rf-power/rf-mobile-radio/30-dbm-over-1-8-1000-mhz-7-5-v-airfast-wideband-integrated-rf-ldmos-amplifier:AFIC901N
- DigiKey AFT05MS006NT1: https://www.digikey.com/en/products/detail/nxp-usa-inc/AFT05MS006NT1/4814338
- Findchips AFT05MS006N: https://www.findchips.com/search/AFT05MS006N
- Mitsubishi silicon RF lineup: https://www.mitsubishielectric.com/semiconductors/hf/products/sirf/index.html
- Mitsubishi RD06LUS2 news: https://www.mitsubishielectric.com/news/2024/0227.html
- Mitsubishi RD07MUS2B datasheet: https://www.mitsubishielectric.com/semiconductors/hf/products/datasheet/rd07mus2b.pdf
- Mitsubishi RD12MVS1 datasheet: https://www.mitsubishielectric.com/semiconductors/hf/products/datasheet/rd12mvs1.pdf
- Mitsubishi RD06LUS2 datasheet: https://www.mitsubishielectric.com/semiconductors/hf/products/datasheet/rd06lus2.pdf
- Mitsubishi Electric US RD07MUS2B: https://meus-semiconductors.com/products/high-frequency-devices/rd07mus2b
- RF Parts RD07MUS2B: https://www.rfparts.com/rftransistors/transistor-rd/rd07mus2b.html
- RF Parts RD series: https://www.rfparts.com/rftransistors/transistor-rd.html
- RF Parts RA07M1317M: https://www.rfparts.com/ra07m1317m-501.html
- Renesas RQA0009: https://www.renesas.com/us/en/products/power-power-management/discrete-power-devices/power-mosfets/rqa0009txdqs-n-channel-mosfet
- Si5351A/B/C-B datasheet Rev 1.3: https://download.mikroe.com/documents/datasheets/Si5351-datasheet.pdf and https://www.skyworksinc.com/-/media/Skyworks/SL/documents/public/data-sheets/Si5351-B.pdf
- RFzero Si5351A tutorial: https://rfzero.net/tutorials/si5351a/
- QRP Labs Si5351 facts: http://nic.vajn.icu/PDF/SiliconLabs/Si5351_facts.txt
- QRP Labs QCX phase noise: https://qrp-labs.com/qcx/phasenoise
- NT7S Si5351A investigations part 7 (KE5FX measurements): https://nt7s.com/2014/11/si5351a-investigations-part-7/
- SolderSmoke spectral purity post: https://soldersmoke.blogspot.com/2015/09/si5351-and-spectral-purity-mask.html
- LA3PNA Si5351 spurious: https://la3pna.com/2016/12/31/si5351-spurius-preformance/
- BITX20 Si5351 quadrature thread: https://groups.io/g/BITX20/topic/si5351_ms5351_quadrature/109985186
- ADF4351 datasheet (ADI): https://www.analog.com/media/en/technical-documentation/data-sheets/adf4351.pdf (mirror used: https://www.physics.utoronto.ca/~astummer/Archives/2016%20Nyquie%20Plus/Docs/ADF4351%20AnaDev,%20PLL%20&%20VCO,%2035-4400MHz%20module.pdf )
- MAX2871 product page: https://www.analog.com/en/products/max2871.html
- LMX2571 product page and datasheet: https://www.ti.com/product/LMX2571 ; https://www.ti.com/lit/ds/symlink/lmx2571.pdf
- Findchips price signals: https://www.findchips.com/search/si5351a-b-gt ; https://www.findchips.com/search/ADF4351BCPZ ; https://www.findchips.com/search/LMX2571NJKR ; https://www.findchips.com/search/MAX2871ETJ%2B
- QRP Labs TCXO: https://shop.qrp-labs.com/tcxo
- SiTime SiT5356: https://www.sitime.com/products/super-tcxo/sit5356
- Epson TG2520SMN: https://www.epsondevice.com/crystal/en/products/crystal-oscillator/tg2520smn.html
- Abracon ATX-13 at DigiKey: https://www.digikey.com/en/products/detail/abracon-llc/ATX-13-F-26-000MHZ-F05-T/14000628
- G4DDK Anglian 144 v1.1: http://www.g4ddk.com/Anglian144v1_1.pdf ; Anglian 3L: http://www.g4ddk.com/Anglian3Ltechdes.pdf ; PGA103 preamp: http://www.g4ddk.com/PGA103amp.pdf
- Kuhne MKU 144 G2 manual: https://db6nt.de/wp-content/uploads/2024/12/MKU-144-G2-Handbuch.pdf ; Kuhne shop: https://shop.kuhne-electronic.com/kuhne/en/shop/konverter-transverte/transverter/
- Elecraft XV manual Rev F1: https://ftp.elecraft.com/XV/Manuals%20Downloads/E740096%20XV%20Transverter%20Owner's%20Manual%20Rev%20F1.pdf ; K144XV: https://elecraft.com/products/k144xv-144-148-mhz-10-w-internal-module
- Q5 Signal L144-28 manual: http://q5signal.com/image/catalog/L144-28r1A.pdf
- Funkamateur/DC8RI transverter (DM5HF): https://dm5hf-chris.blogspot.com/2016/08/144-mhz-transverter-der-fachzeitschrift.html ; https://dm5hf-chris.blogspot.com/2017/01/144-mhz-transverter-vom-funkamateur.html
- VK3HN SP-8 / UR3LMZ: https://vk3hn.wordpress.com/2021/01/18/sp-8-a-homebrew-28mhz-ssb-transceiver-for-a-ur3lmz-144mhz-transverter/
- G4JNT 144 MHz DC receiver: http://g4jnt.com/144MHzDCReceiver.pdf
- ZL2CTM (SolderSmoke): https://soldersmoke.blogspot.com/2017/08/zl2ctms-homebrew-transciever-project.html
- G3XBM IC-202: https://sites.google.com/view/g3xbm4/home/vhfuhfmicrowaves/vhfuhf-commercial-rigs/icom-ic-202 ; RigReference IC-202: https://rigreference.com/rigs/2976-ICOM_IC_202
- FT-290R: https://www.radiomasterlist.com/en/yaesu-ft-290r.html ; https://rigreference.com/rigs/4278-yaesu-ft-290r
- Mizuho MX-2: https://rigreference.com/rigs/3591-mizuho-mx-2 ; https://www.radiomuseum.org/r/mizuhotsus_2m_ssbcw_transceiver_mx_2.html
- KA7OEI FT-817 receiver: http://www.ka7oei.com/ft817_rcv.html
- ARRL QST IC-705 review reprint: https://static.dxengineering.com/global/images/technicalarticles/ico-ic-705_ng.pdf ; VA7OJ IC-705 report: https://www.qsl.net/ab4oj/icom/ic705/705notes.pdf
- 47 CFR 97.307: https://www.law.cornell.edu/cfr/text/47/97.307 ; 97.305: https://www.law.cornell.edu/cfr/text/47/97.305 ; 2.202: https://www.law.cornell.edu/cfr/text/47/2.202 (ecfr.gov: https://www.ecfr.gov/current/title-47/chapter-I/subchapter-D/part-97/subpart-D/section-97.307 redirected for automated access)
- NXP BAP64-02 datasheet: https://www.nxp.com/docs/en/data-sheet/BAP64-02.pdf
- Omron G6K-2F-RF datasheet: https://omronfs.omron.com/en_US/ecb/products/pdf/en-g6k_2f_rf.pdf
- W8ZR QSK article: https://w8zr.net/QSK/qsk_QST.pdf ; QSK-5 PIN switch notes: https://www.frostburg.edu/personal/latta/ee/qsk5/trswitch/trswitch.html
- G3OTK key clicks and CW waveform shaping: http://www.ivarc.org.uk/uploads/1/2/3/8/12380834/keyclicks_version_1.pdf
- ARRL Test Procedures Manual (2010): https://www.arrl.org/files/file/Technology/tis/info/pdf/Procedure%20Manual%202010%20with%20page%20breaks.pdf
- QRP Labs AN005: https://www.qrp-labs.com/images/appnotes/AN005_A4.pdf ; 5 W PA kit: https://qrp-labs.com/pa.html ; RC1: http://shop.qrp-labs.com/rc1 ; QCX: https://qrp-labs.com/qcx.html ; QMX: https://qrp-labs.com/qmx.html
- NXP LDMOS bias note: https://community.nxp.com/pwmxy87654/attachments/pwmxy87654/Power-Management/695/1/Bias%20setting%20instructions%20LDMOS%20RF%20Power%20Amplifiers.pdf
- KVG 9 MHz standard filters: https://www.kn34pc.com/spr/quartz_filters_ge/spr_kvg_9_mhz_standard_filter.pdf ; KVG catalogues: https://pdf.directindustry.com/pdf/kvg-quartz-crystal-technology-gmbh/discrete-crystal-filters-10-mhz-107-mhz/82515-750637.html
- Giangrandi crystal ladder filters: https://www.giangrandi.org/electronics/xtalfilters/xtalfilters.shtml
- Land Boards crystal filter design: http://land-boards.com/blwiki/index.php?title=Crystal_Filter_Design
- DJ6EV Dishal: https://www.bartelsos.de/filter/quarzfilter/quarzfilter-dj6ev ; help: https://warc.org.uk/wp-content/uploads/2014/01/eDishalHelp.pdf
- QEX Crystal Ladder Filters for All: https://www.arrl.org/files/file/QEX_Next_Issue/Nov-Dec_2009/QEX_Nov-Dec_09_Feature.pdf
- Inrad 400 Hz CW filter (price signal): http://www.inrad.net/product.php?printable=Y&productid=130
- Golledge GMCF-10: https://www.golledge.com/products/gmcf-10-10g7c/c-26/p-2490 ; YIC 45 MHz MCF at DigiKey: https://www.digikey.com/en/products/detail/yic/MCF45M15A-SM756/21804189
- Krystaly Hradec Kralove filters: https://www.krystaly.cz/en/products/filters/
- Mini-Circuits PGA-103+: https://www.minicircuits.com/pdfs/PGA-103+.pdf ; Qorvo SPF5189Z EOL: https://www.qorvo.com/products/p/SPF5189Z
