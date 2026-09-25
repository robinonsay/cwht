# Regulatory basis for cwht: 47 CFR Part 97, RF exposure, and homebrew status

**Assignment key:** regulatory
**Author:** Claude (research subagent), 2026-09-25
**Status:** research input for SRR; not a baseline. Candidate requirements are proposals for the requirements owner, not requirements.
**Rule text currency:** all CFR quotations below were pulled from the eCFR versioner API for issue date 2026-09-23 (the latest eCFR issue date available on 2026-09-25). Part 97 subpart D was last amended by 91 FR 1431 (Jan 14, 2026, effective Feb 13, 2026); that rule touched only 60 m entries and 97.313(f)/(i), so nothing quoted here about 2 m changed in 2026.

## 1. Question

For a US General-class licensee building a 5 W, 144 MHz, true-CW (A1A) handheld transceiver, establish from primary sources:

1. 47 CFR 97.305: which emission types are permitted on 2 m, and whether CW is allowed across the whole band.
2. 47 CFR 97.307(e): spurious-emission limits for 30-225 MHz transmitters of 25 W or less, and the resulting harmonic suppression in dB for a 5 W (37 dBm) transmitter.
3. 47 CFR 97.313: power limits.
4. 47 CFR 97.301 and 97.303: frequency privileges and sharing on 2 m.
5. The ARRL 2 m band plan: CW segments and calling frequencies.
6. The RF-exposure evaluation obligation (47 CFR 1.1307(b) as amended, effective 2021; 97.13(c)), the exemption thresholds for a handheld used within 20 cm of the body at 144 MHz, and what a compliant evaluation looks like for CW duty cycle.
7. Homebrew equipment status: whether licensee-built transceivers need certification, and where 97.315 (external amplifiers) applies.

Deliver candidate requirements with numbers.

## 2. Method

**Web fetches (2026-09-25):**

- ecfr.gov HTML pages redirect automated fetchers to a bot-protection page, so the CFR text was pulled from the public eCFR versioner API with compression negotiated:
  `curl -sL --compressed "https://www.ecfr.gov/api/versioner/v1/full/2026-09-23/title-47.xml?part=97&section=97.307"` (and likewise for 97.3, 97.13, 97.101, 97.119, 97.301, 97.303, 97.305, 97.313, 97.315, 97.317; part 1 sections 1.1307, 1.1310; part 2 sections 2.201, 2.815, 2.1057, 2.1091, 2.1093; part 15 section 15.23). Version histories from `.../versions/title-47.json?part=97&section=NN`. The XML was stripped to text with a short Python script. A first read of 97.305/97.307/97.13/97.315/1.1307 was taken from the Cornell LII mirror (law.cornell.edu/cfr/text/47/...) and then confirmed against the eCFR API text.
- FCC 19-126 (Second Report and Order, RF exposure, adopted 2019-11-27) PDF from docs.fcc.gov, converted with `pdftotext -layout`, grepped for "amateur", "300 MHz", "λ/2π", "transition".
- OET Bulletin 65 Supplement B (Edition 97-01) PDF from transition.fcc.gov, converted with `pdftotext -layout`.
- FCC Enforcement Advisory DA 18-581 PDF (primary FCC statement on amateur equipment authorization) from docs.fcc.gov.
- Federal Register API queries for Part 97 rules published 2025-2026 and for the 2020-2021 RF-exposure effective-date documents.
- ARRL pages: band plan, RF exposure, RF exposure calculator, "the Station Evaluation", two news items; the Richard Tell QEX July/August 2021 handheld SAR paper (PDF via ARRL).
- fcc.gov HTML pages (Amateur Radio Service, OET RF device page) returned HTTP 403 to both WebFetch and curl; web.archive.org is not reachable from this tool. The FCC page statement is therefore cited via a search-engine snippet and backed by the DA 18-581 primary text.

**Local commands:** `pdftotext` (Homebrew), `python3` for text extraction and the dB / distance arithmetic shown in Findings 2 and 8. All downloads were kept in the session scratch directory (`.../scratchpad/ecfr/`, files `sec-*.txt`, `fcc-19-126.txt`, `oet65b.txt`, `qex-tell-2021.txt`, `da-18-581.txt`, `fr-2026-00587.txt`). Nothing was written to the repository except this report.

Formatting note: em and en dashes inside quoted rule text were replaced by hyphens per the report style; no words were changed.

## 3. Findings

### F1. 97.305: CW (A1A) is permitted on the entire 2 m band; everything else starts at 144.1 MHz

47 CFR 97.305 (eCFR, issue 2026-09-23; last amended 91 FR 1431, Jan 14, 2026):

> (a) Except as specified elsewhere in this part, an amateur station may transmit a CW emission on any frequency authorized to the control operator.
> (b) A station may transmit a test emission on any frequency authorized to the control operator for brief periods for experimental purposes, except that no pulse modulation emission may be transmitted on any frequency where pulse is not specifically authorized and no SS modulation emission may be transmitted on any frequency where SS is not specifically authorized.
> (c) A station may transmit the following emission types on the frequencies indicated, as authorized to the control operator, subject to the standards specified in § 97.307(f):
> ... (4) VHF: ... (iii) 2 m | 144.1-148.0 MHz | MCW, phone, image, RTTY, data, test | (f)(2), (5), (8).

Consequences:

- CW is authorized 144.000-148.000 MHz for any control operator who holds 2 m privileges (see F4). 144.000-144.100 MHz is CW-only by omission from the (c) table.
- "CW" is defined in 97.3(c)(1): "International Morse code telegraphy emissions having designators with A, C, H, J or R as the first symbol; 1 as the second symbol; A or B as the third symbol; and emissions J2A and J2B." A1A (on-off keyed carrier, Morse for aural reception) is therefore CW. The designator symbols themselves are defined in 47 CFR 2.201(c)-(e).
- "MCW" (97.3(c)(4)) is tone-modulated Morse (A2A, F2A, etc.). It is a different emission type and is not authorized in 144.0-144.1 MHz. A "true CW" design must not modulate a tone onto the carrier; a sidetone is audio-only.
- The 97.307(f)(2), (5), (8) standards referenced for 2 m constrain non-CW modes (bandwidth of non-phone emissions, digital symbol rate 19.6 kbaud, 20 kHz authorized bandwidth). They do not constrain A1A.
- Version history (eCFR API): 97.305 amended 2016-12-15, 2017 (x3), 2020-10-09, 2020-11-09, 2023-12-07, 2024-01-08, 2026-01-14, 2026-02-13. The Federal Register text of 2026-00587 (91 FR 1405-1431) shows the Jan 2026 change revised only the "60 m" row of 97.305(c); the 2 m row is unchanged.

Sources: https://www.ecfr.gov/current/title-47/section-97.305 ; API https://www.ecfr.gov/api/versioner/v1/full/2026-09-23/title-47.xml?part=97&section=97.305 ; https://www.ecfr.gov/current/title-47/section-97.3 ; https://www.ecfr.gov/current/title-47/section-2.201 ; https://www.federalregister.gov/documents/2026/01/14/2026-00587/implementation-of-the-final-acts-of-the-world-radiocommunication-conference-geneva-2015-wrc-15-other

### F2. 97.307(e): at 5 W the binding spurious limit is the absolute 25 µW cap, which requires 53.0 dB of suppression

47 CFR 97.307 (eCFR, issue 2026-09-23):

> (a) No amateur station transmission shall occupy more bandwidth than necessary for the information rate and emission type being transmitted, in accordance with good amateur practice.
> (b) Emissions resulting from modulation must be confined to the band or segment available to the control operator. Emissions outside the necessary bandwidth must not cause splatter or keyclick interference to operations on adjacent frequencies.
> (c) All spurious emissions from a station transmitter must be reduced to the greatest extent practicable. If any spurious emission, including chassis or power line radiation, causes harmful interference to the reception of another radio station, the licensee of the interfering amateur station is required to take steps to eliminate the interference, in accordance with good engineering practice.
> (e) The mean power of any spurious emission from a station transmitter or external RF power amplifier transmitting on a frequency between 30-225 MHz must be at least 60 dB below the mean power of the fundamental. For a transmitter having a mean power of 25 W or less, the mean power of any spurious emission supplied to the antenna transmission line must not exceed 25 µW and must be at least 40 dB below the mean power of the fundamental emission, but need not be reduced below the power of 10 µW. A transmitter built before April 15, 1977, or first marketed before January 1, 1978, is exempt from this requirement.

"Spurious emission" (97.3(a)(43)): "An emission, or frequencies outside the necessary bandwidth of a transmission, the level of which may be reduced without affecting the information being transmitted." Harmonics are spurious emissions.

Arithmetic (python3, shown in Method):

| Fundamental mean power | dBm | 40 dB below fundamental | Absolute cap 25 µW | Required suppression |
|---|---|---|---|---|
| 5.0 W | 36.99 | -3.0 dBm (500 µW), not binding | -16.02 dBm | **53.0 dB** |
| 6.0 W | 37.78 | -2.2 dBm, not binding | -16.02 dBm | 53.8 dB |
| 7.0 W | 38.45 | -1.5 dBm, not binding | -16.02 dBm | 54.5 dB |
| 25 W (tier edge) | 43.98 | 4.0 dBm, not binding | -16.02 dBm | 60.0 dB |
| > 25 W | | 60 dB relative rule applies | | 60 dB |

Notes:

- For CW, "mean power" during key-down equals carrier power, so the 5 W rating is the number to use.
- The limit is on power "supplied to the antenna transmission line": a conducted measurement at the antenna connector into 50 ohms is the compliance point. Chassis and cable radiation fall under (c) (harmful-interference basis, no numeric limit).
- The rule has no upper frequency bound for "any spurious emission". The FCC's equipment-measurement rule 47 CFR 2.1057(a)(1), which does not bind amateurs but is the natural analog, investigates "from the lowest radio frequency signal generated in the equipment, without going below 9 kHz, up to at least ... the tenth harmonic of the highest fundamental frequency or to 40 GHz, whichever is lower", i.e. to 1.48 GHz for a 148 MHz fundamental, and adds "(b) Particular attention should be paid to harmonics and subharmonics of the carrier frequency as well as to those frequencies removed from the carrier by multiples of the oscillator frequency."
- Where the 2 m harmonics fall (from the fundamental only; allocation table not fetched, see Open items): 2f = 288-296 MHz (federal 225-400 MHz aeronautical mobile), 3f = 432-444 MHz (70 cm amateur band, shared with federal radiolocation per 97.303(b)), 4f = 576-592 MHz (UHF TV), 5f = 720-740 MHz (700 MHz commercial and public-safety LTE), 7f = 1008-1036 MHz (960-1215 MHz aeronautical radionavigation). The 97.307(c) harmful-interference clause makes these consequential beyond the numeric limit.

Sources: https://www.ecfr.gov/current/title-47/section-97.307 ; API https://www.ecfr.gov/api/versioner/v1/full/2026-09-23/title-47.xml?part=97&section=97.307 ; https://www.law.cornell.edu/cfr/text/47/97.307 ; https://www.ecfr.gov/current/title-47/section-2.1057

### F3. 97.313: 1.5 kW PEP ceiling and a "minimum power necessary" duty; no 2 m-specific limit

47 CFR 97.313 (eCFR, issue 2026-09-23):

> (a) An amateur station must use the minimum transmitter power necessary to carry out the desired communications.
> (b) No station may transmit with a transmitter power exceeding 1.5 kW PEP.

Paragraphs (c) through (m) give band-specific limits (200 W on 30 m, 25 W on 1.25 m and 5 W on 23 cm for Novices, 50 W on 70 cm near certain military areas, 60 m ERP limits, 10 W PEP for spread spectrum, etc.). None applies to 2 m. PEP is defined in 97.3(b)(9): "The average power supplied to the antenna transmission line by a transmitter during one RF cycle at the crest of the modulation envelope taken under normal operating conditions." For A1A, PEP equals key-down carrier power.

A 5 W handheld is 25 dB below the ceiling; the operative constraint is 97.313(a), which motivates selectable power levels and is also the primary RF-exposure mitigation (F8).

Source: https://www.ecfr.gov/current/title-47/section-97.313 ; API https://www.ecfr.gov/api/versioner/v1/full/2026-09-23/title-47.xml?part=97&section=97.313

### F4. 97.301 and 97.303: General class has 144-148 MHz in ITU Region 2 with no 2 m sharing constraint in the US

47 CFR 97.301 (eCFR, issue 2026-09-23):

> The following transmitting frequency bands are available to an amateur station located within 50 km of the Earth's surface, within the specified ITU Region, and outside any area where the amateur service is regulated by any authority other than the FCC.
> (a) For a station having a control operator who has been granted a Technician, General, Advanced, or Amateur Extra Class operator license or who holds a CEPT radio-amateur license or IARP of any class:
> ... VHF ... 2 m | ITU Region 1: 144-146 MHz | ITU Region 2: 144-148 MHz | ITU Region 3: 144-148 MHz | Sharing requirements see § 97.303 (paragraph): (a), (k).

The continental US is in ITU Region 2, so 144.000-148.000 MHz applies. A General-class control operator is covered by paragraph (a) exactly as a Technician is; the higher-class tables (b)-(d) only add LF/MF/HF privileges.

47 CFR 97.303 paragraphs cited for 2 m:

> (a) Where, in adjacent ITU Regions or sub-Regions, a band of frequencies is allocated to different services of the same category (i.e., primary or secondary services), the basic principle is the equality of right to operate. Accordingly, stations of each service in one Region or sub-Region must operate so as not to cause harmful interference to any service of the same or higher category in the other Regions or sub-Regions.
> (k) For amateur stations located in ITU Regions 1 and 3: Amateur stations transmitting in the 146-148 MHz segment or the 10.00-10.45 GHz segment must not cause harmful interference to, and must accept interference from, stations of other nations in the fixed and mobile services.

Paragraph (k) applies only to stations located in Regions 1 and 3; (a) is a general principle. There is no US-specific sharing constraint on 2 m; the band is primary for the amateur service. Version history: 97.301 last substantively amended 2026-01-14 (60 m row only, per the FR amendatory text "18. Amend § 97.301 by revising the entry for the '60 m' wavelength band").

Sources: https://www.ecfr.gov/current/title-47/section-97.301 ; https://www.ecfr.gov/current/title-47/section-97.303 ; API URLs as in Method.

### F5. ARRL 2 m band plan: CW lives in 144.00-144.10 MHz; 144.200 is the national (weak-signal) calling frequency; the plan is voluntary and undated

From https://www.arrl.org/band-plan (fetched 2026-09-25; the page carries no revision date and states the plan was "proposed by the ARRL VHF-UHF Advisory Committee" and that "A band plan refers to a voluntary division of a band to avoid interference"):

| Segment (MHz) | Use |
|---|---|
| 144.00-144.05 | EME (CW) |
| 144.05-144.10 | General CW and weak signals |
| 144.10-144.20 | EME and weak-signal SSB |
| 144.200 | National calling frequency |
| 144.200-144.275 | General SSB operation |
| 144.275-144.300 | Propagation beacons |
| 144.30-144.50 | New OSCAR subband |
| 144.50-144.60 | Linear translator inputs |
| 144.60-144.90 | FM repeater inputs |
| 144.90-145.10 | Weak signal and FM simplex |
| 145.10-145.20 | Linear translator outputs |
| 145.20-145.50 | FM repeater outputs |
| 145.50-145.80 | Miscellaneous and experimental modes |
| 145.80-146.00 | OSCAR subband |
| 146.01-146.37 | Repeater inputs |
| 146.40-146.58 | Simplex |
| 146.52 | National Simplex Calling Frequency (FM) |
| 146.61-146.97 | Repeater outputs |
| 147.00-147.39 | Repeater outputs |
| 147.42-147.57 | Simplex |
| 147.60-147.99 | Repeater inputs |

Observations:

- The ARRL plan designates no CW-specific calling frequency. 144.200 MHz is the weak-signal calling frequency (SSB and CW) and 144.100 MHz is the top of the CW-only segment; several regional plans and operating guides treat 144.100 as a de facto CW meeting frequency, but neither ARRL page fetched (band plan; hamradioschool.com and k0nr.com secondary pages) states this, so it is recorded here at Low confidence.
- Secondary sources agree on the practical rule that non-FM weak-signal work belongs below 144.300 MHz and FM belongs above 145.100 MHz (k0nr.com: "FM voice simplex and repeater operation should occur only above 145.100 MHz").
- Legally, CW is permitted anywhere in 144-148 MHz (F1); the band plan is the "good amateur practice" overlay that 97.101(a) and 97.307(a) invoke.

Sources: https://www.arrl.org/band-plan ; https://www.hamradioschool.com/post/what-frequency-do-i-use-on-2-meters (updated 2026-05-06) ; https://www.k0nr.com/wordpress/my-articles/2m-frequency/

### F6. RF exposure: no routine-evaluation exemption exists for a 5 W handheld at 144 MHz used within 20 cm of the body; an evaluation is mandatory

Chain of rules:

47 CFR 97.13(c) (eCFR; amended 85 FR 18151, Apr 1, 2020, effective June 1, 2020):

> (c) Before causing or allowing an amateur station to transmit from any place where the operation of the station could cause human exposure to RF electromagnetic field levels in excess of those allowed under § 1.1310 of this chapter, the licensee is required to take certain actions.
> (1) The licensee shall ensure compliance with the Commission's radio frequency exposure requirements in §§ 1.1307(b), 2.1091, and 2.1093 of this chapter, where applicable. In lieu of evaluation with the general population/uncontrolled exposure limits, amateur licensees may evaluate their operation with respect to members of his or her immediate household using the occupational/controlled exposure limits in § 1.1310, provided appropriate training and information has been accessed by the amateur licensee and members of his/her household. RF exposure of other nearby persons who are not members of the amateur licensee's household must be evaluated with respect to the general population/uncontrolled exposure limits. Appropriate methodologies and guidance for evaluating amateur radio service operation is described in the Office of Engineering and Technology (OET) Bulletin 65, Supplement B.
> (2) If the routine environmental evaluation indicates that the RF electromagnetic fields could exceed the limits contained in § 1.1310 of this chapter in accessible areas, the licensee must take action to prevent human exposure to such RF electromagnetic fields. ...

47 CFR 1.1307(b)(1)(i): applicants and licensees "must either: (A) Determine that they qualify for an exemption pursuant to § 1.1307(b)(3); (B) Prepare an evaluation of the human exposure to RF radiation pursuant to § 1.1310 and include in the application a statement confirming compliance with the limits in § 1.1310; or (C) Prepare an Environmental Assessment ..."

47 CFR 1.1307(b)(3)(i), single-source exemptions (verbatim, table flattened):

> (A) The available maximum time-averaged power is no more than 1 mW, regardless of separation distance. ...
> (B) Or the available maximum time-averaged power or effective radiated power (ERP), whichever is greater, is less than or equal to the threshold Pth (mW) described in the following formula. This method shall only be used at separation distances (cm) from 0.5 centimeters to 40 centimeters and at frequencies from 0.3 GHz to 6 GHz (inclusive). ...
> (C) Or using Table 1 and the minimum separation distance (R in meters) from the body of a nearby person for the frequency (f in MHz) at which the source operates, the ERP (watts) is no more than the calculated value prescribed for that frequency. For the exemption in Table 1 to apply, R must be at least λ/2π, where λ is the free-space operating wavelength in meters. If the ERP of a single RF source is not easily obtained, then the available maximum time-averaged power may be used in lieu of ERP if the physical dimensions of the radiating structure(s) do not exceed the electrical length of λ/4 or if the antenna gain is less than that of a half-wave dipole (1.64 linear value).
> Table 1 to § 1.1307(b)(3)(i)(C) - Single RF Sources Subject to Routine Environmental Evaluation: 0.3-1.34 MHz: 1,920 R^2 ; 1.34-30 MHz: 3,450 R^2/f^2 ; 30-300 MHz: 3.83 R^2 ; 300-1,500 MHz: 0.0128 R^2 f ; 1,500-100,000 MHz: 19.2 R^2 (Threshold ERP in watts).

The FCC's own gloss on how these fit together for VHF portables, FCC 19-126 footnote 143 (adopted 2019-11-27):

> In Table 2, if R < λ/2π, evaluation is required. Since λ/2π is > 20 cm at frequencies below 239 MHz, these exemption criteria do not apply to portable devices that are operated both at less than 20 cm from the body and at frequencies below 239 MHz. In general, less restrictive SAR-based exemption criteria may be used in accordance with the formulas specified in Table 2, but these SAR-based exemptions are not valid below 300 MHz. Thus, there are no exemption criteria below 239 MHz for portable devices (or for any antenna at less than 20 cm) other than the 1 mW blanket exemption. The λ/2π distance in meters may be conveniently calculated using the formula: 47.7/f where f is the operating frequency in megahertz.

Numbers at 144 MHz (python3): λ = 2.082 m; λ/2π = 47.7/144 = 0.331 m (0.322 m at 148 MHz). The MPE-based exemption ERP at the minimum permitted distance is 3.83 x 0.331^2 = 0.42 W. A 5 W CW transmitter is 5000 times the 1 mW blanket exemption. Conclusion: **if cwht is used as a handheld (antenna within 20 cm of anyone), no exemption is available and 97.13(c)(1) requires an evaluation before transmitting.** If the ConOps keeps the antenna at least 0.331 m from everyone, the MPE-based exemption becomes available at ERP-dependent distances (F8).

"Portable device" and "mobile device" are defined by distance, not by form factor: 2.1093(b) "A portable device is defined as a transmitting device designed to be used in other than fixed locations and to generally be used in such a way that the RF source's radiating structure(s) is/are within 20 centimeters of the body of the user." 2.1091(b): a mobile device normally maintains "a separation distance of at least 20 centimeters".

Effective dates: the rules were adopted in FCC 19-126 (adopted 2019-11-27, released 2019-12-04), published at 85 FR 18131 (2020-04-01) with an effective date of 2020-06-01 for most amendments; 85 FR 33578 (2020-06-02) delayed the information-collection-dependent amendments; 86 FR 20456 (2021-04-20) announced their effective date as **2021-05-03**. FCC 19-126 para. 116: "We will allow two years from the effective date of the new rules for licensees to determine if evaluations are required, to perform them where necessary, and to comply with the more specific mitigation requirements", i.e. the transition ended 2023-05-03; the ARRL RF exposure page confirms "all transmitters operating in the US are expected to comply with the exposure rules" as of that date. The 1.1307(b) definitions clause is explicit that exemption "is not exemption from general obligations of compliance with the RF exposure limits in § 1.1310".

Sources: https://www.ecfr.gov/current/title-47/section-97.13 ; https://www.ecfr.gov/current/title-47/section-1.1307 ; https://www.ecfr.gov/current/title-47/section-2.1093 ; https://www.ecfr.gov/current/title-47/section-2.1091 ; https://docs.fcc.gov/public/attachments/FCC-19-126A1.pdf ; https://www.federalregister.gov/documents/2020/04/01/2020-02745/human-exposure-to-radiofrequency-electromagnetic-fields-and-reassessment-of-fcc-radiofrequency ; https://www.federalregister.gov/documents/2021/04/20/2021-07720/human-exposure-to-radiofrequency-electromagnetic-fields-and-reassessment-of-fcc-radiofrequency ; https://www.arrl.org/rf-exposure

### F7. The limits the evaluation must meet (47 CFR 1.1310), and which regime applies to a handheld

47 CFR 1.1310 (85 FR 18145, Apr 1, 2020):

> (a) Specific absorption rate (SAR) shall be used to evaluate the environmental impact of human exposure to radiofrequency (RF) radiation as specified in § 1.1307(b) of this part within the frequency range of 100 kHz to 6 GHz (inclusive).
> (b) The SAR limits for occupational/controlled exposure are 0.4 W/kg, as averaged over the whole body, and a peak spatial-average SAR of 8 W/kg, averaged over any 1 gram of tissue ... extremities, such as hands, wrists, feet, ankles, and pinnae, where the peak spatial-average SAR limit for occupational/controlled exposure is 20 W/kg, averaged over any 10 grams of tissue ... Exposure may be averaged over a time period not to exceed 6 minutes ...
> (c) The SAR limits for general population/uncontrolled exposure are 0.08 W/kg, as averaged over the whole body, and a peak spatial-average SAR of 1.6 W/kg, averaged over any 1 gram of tissue ... extremities ... 4 W/kg, averaged over any 10 grams of tissue ... Exposure may be averaged over a time period not to exceed 30 minutes ...
> (d)(2) For operations within the frequency range of 300 kHz and 6 GHz (inclusive), the limits for maximum permissible exposure (MPE), derived from whole-body SAR limits and listed in Table 1 in paragraph (e)(1) of this section, may be used instead of whole-body SAR limits ... except for portable devices as defined in § 2.1093 of this chapter as these evaluations shall be performed according to the SAR provisions in § 2.1093.
> (d)(4) Both the MPE limits ... and the SAR limits ... are for continuous exposure, that is, for indefinite time periods. Exposure levels higher than the limits are permitted for shorter exposure times, as long as the average exposure over a period not more than the specified averaging time in Table 1 ... is less than (or equal to) the exposure limits.
> Table 1, 30-300 MHz: Occupational/Controlled: E = 61.4 V/m, H = 0.163 A/m, S = 1.0 mW/cm2, averaging time 6 minutes. General Population/Uncontrolled: E = 27.5 V/m, H = 0.073 A/m, S = 0.2 mW/cm2, averaging time 30 minutes.

Time averaging for portables, 47 CFR 2.1093(d)(3)-(4): occupational SAR criteria may use "time averaging provisions of the limits ... in conjunction with the maximum duty factor"; for general-population devices "the time averaging provisions ... based on maximum duty factor, may not be used ... However, 'source-based' time averaging based on an inherent property of the RF source is allowed over a time period not to exceed 30 minutes."

Regime for cwht:

- Antenna within 20 cm of the user (handheld in hand, belt clip): portable device, SAR limits apply (1.1310(d)(2)); the licensee and trained household members may be assessed against occupational limits (8 W/kg per 1 g; 20 W/kg per 10 g in the hand) per 97.13(c)(1); anyone else against 1.6 W/kg (4 W/kg hand).
- Antenna 20 cm or more from everyone: mobile device; MPE limits (0.2 mW/cm2 general population, 1.0 mW/cm2 operator) and the OET 65 Supplement B methods apply directly; the MPE-based exemption is also available beyond 0.331 m (F6).

Sources: https://www.ecfr.gov/current/title-47/section-1.1310 ; https://www.ecfr.gov/current/title-47/section-2.1093

### F8. What a compliant evaluation would look like for CW duty cycle: OET 65 Supplement B methods, plus the SAR-by-analogy data that exist for 2 m handhelds

**FCC-endorsed method.** FCC 19-126 footnote 100: "When evaluation is required, additional guidance is available in tabulated generic analyses of compliance for broad classes of antennas and installations from the Commission and third parties. See FCC Office of Engineering at Technology, Additional Information for Amateur Radio Stations, OET Bulletin 65, Supplement B, (1997); Ed Hare, RF Exposure and You, The Amateur Radio Relay League (1998). This guidance has been available for years and is an acceptable method to determine compliance." Para. 32 adds that where "antenna performance characteristics may not be well understood for a particular amateur radio installation, the most feasible option of demonstrating compliance remains to be evaluated".

**Duty factor.** OET 65 Supplement B (Edition 97-01), Table 2 "Duty Factor of Modes Commonly Used by Amateurs": Conversational SSB 20% (no processing) / 50% (heavy processing); Voice FM 100%; FSK or RTTY 100%; AFSK SSB 100%; **Conversational CW 40%**; Carrier 100% ("A full carrier is commonly used for tune-up purposes"). The bulletin's recipe: "To obtain an easy estimate of average power, multiply the transmitter peak envelope power by the duty factor, then multiply that result by the worst-case percentage of time the station would be on the air in, e.g., a 6-minute period (the averaging time for controlled exposure) or a 30-minute period (the averaging time for uncontrolled exposure). This is an example of 'source-based' time averaging." Its worked CW example: "500 W X 0.4 (40% from Table 2) X 0.125 (45 of 360 seconds) = 25 W". Table 32 gives distance multipliers (50% duty factor: 0.71). The ARRL RF Exposure Calculator uses the same values ("Conversational CW (duty cycle=40%)") but warns twice: "This calculator should not be used for antennas that are less than 20 cm (8 in) from a person."

Note that the same 1997 bulletin (p. 3 and footnote 7) describes the pre-2021 regime in which "stations using mobile and portable (hand-held) transmitters ... are not required to be routinely evaluated"; that categorical exemption was removed by FCC 19-126 and Supplement B has not been reissued, so its handheld guidance is now advisory only.

**Worked numbers for cwht (Analysis, python3; to be redone with the real antenna gain and ConOps):**

Time-averaged power for 5 W CW: continuous keying 5 x 0.40 = 2.0 W; keying 50% of the averaging window 5 x 0.40 x 0.5 = 1.0 W; tune-up carrier 5 W.

(a) Mobile posture (antenna at least 20 cm from everyone), MPE-based exemption 1.1307(b)(3)(i)(C), ERP threshold 3.83 R^2 W, R at least 0.331 m. Assuming a whip with 0 dBd gain (ERP = time-averaged power; real HT whips are worse than a dipole, so this is conservative):

| Time-averaged ERP | Exempt separation R |
|---|---|
| 0.42 W | 0.331 m (the λ/2π floor) |
| 1.0 W (50% keying) | 0.51 m |
| 2.0 W (continuous keying) | 0.72 m |
| 5.0 W (carrier) | 1.14 m |

(b) Mobile posture, MPE evaluation by the OET 65 far-field formula S = 2.56 x EIRP / (4 pi R^2) (2.56 = worst-case ground reflection; EIRP = 1.64 x ERP for 0 dBd). Distance to reach the limit:

| Time-averaged power, 0 dBd | General population 0.2 mW/cm2 (30 min) | Operator/household 1.0 mW/cm2 (6 min) |
|---|---|---|
| 1.0 W (50% keying) | 0.41 m (0.26 m without reflection) | 0.18 m (0.11 m) |
| 2.0 W (continuous keying) | 0.58 m (0.36 m) | 0.26 m (0.16 m) |
| 5.0 W (carrier, tune-up) | 0.91 m (0.57 m) | 0.41 m (0.26 m) |

(c) Handheld posture (within 20 cm): SAR regime, and the FCC has published no amateur-specific method. The only quantitative data found is Richard Tell K5UJU, "Amateur Portable Radios (Handheld Transceivers): Exposure Considerations Based on SAR", QEX July/August 2021, which mined FCC equipment-authorization SAR reports for commercial VHF/UHF handhelds "that operate in frequency bands that are extremely close to - or, in some cases, actually within - those authorized for the amateur service". Values are "normalized to 1 W and are relative to a duty cycle of 50% based on the push-to-talk (PTT) operation of the handheld. For compliance determination purposes, the FCC applies a presumed duty cycle of 50% for PTT operation of the handheld." Result for 2 m: "in the 2 m band, it might be presumed that an handheld operating with a power of up to 22.9 W (not realistic for an handheld) could be used before exceeding the amateur radio operator SAR limit (8 W/kg divided by 0.35 W/kg/W)." Applying 0.35 W/kg per W (1 g SAR, 50% duty) to cwht:

| Case | Estimated peak 1 g SAR | Limit | Fraction |
|---|---|---|---|
| 5 W, 50% duty (FCC PTT presumption), licensee | 1.75 W/kg | 8 W/kg | 22% |
| 5 W, 40% CW duty factor, licensee | 1.4 W/kg | 8 W/kg | 18% |
| 5 W, 50% duty, non-licensee holding the radio | 1.75 W/kg | 1.6 W/kg | **109%** |
| 5 W, 40% CW duty factor, non-licensee | 1.4 W/kg | 1.6 W/kg | 88% |
| 2 W, 50% duty, non-licensee | 0.70 W/kg | 1.6 W/kg | 44% |

Tell's own caveat: this is a "tentative conclusion" from "a careful but limited examination", the amateur radios "have not necessarily been directly measured for SAR", and the ARRL RF Safety Committee's guidance was "work in progress" in 2021. The ARRL had asked the FCC in May 2020 for permission to use "near-field regression rates using the MPE table as an alternative to SAR for handheld portable devices, noting that SAR data isn't available for amateur equipment"; no FCC response was found in this research. The regulatory position for an amateur-built VHF handheld is therefore: evaluation required, method not prescribed, SAR nominally the metric, OET 65 B accepted by the FCC as "an acceptable method" for amateurs generally. See RISK-1 and DECISION-1.

Sources: https://transition.fcc.gov/Bureaus/Engineering_Technology/Documents/bulletins/oet65/oet65b.pdf ; https://docs.fcc.gov/public/attachments/FCC-19-126A1.pdf ; https://www.arrl.org/rf-exposure-calculator ; http://www.arrl.org/fcc-rf-exposure-regulations-the-station-evaluation ; https://www.arrl.org/files/file/QEX_Next_Issue/2021/07%20Jul-August%202021/07%20JulAug21%20QEX%20Tell.pdf ; http://www.arrl.org/news/view/arrl-seeks-clarification-of-amended-amateur-service-rf-safety-rules (2020-05-13)

### F9. Homebrew status: no FCC equipment authorization for an amateur-built transceiver; 97.315 reaches only external amplifiers; 15.23 covers the digital section

- FCC Enforcement Advisory DA 18-581 (2018-06-05), footnote 5, quoting the Commission's Pilot Travel Centers NAL: "[R]adio transmitting equipment that transmits solely on Amateur Radio Service ('ARS') frequencies is not subject to equipment authorization requirements prior to manufacture or marketing." Footnote 8, quoting the New Generation Hobbies citation: "[W]hile amateur radio service equipment is exempt from the FCC's equipment certification requirement, it is a violation of the Commission's regulations to market in the United States a transmitter that is designed or intended to operate on frequencies outside of the authorized amateur radio service bands if such equipment has not been issued a grant of equipment certification." The FCC Amateur Radio Service web page states the same ("The FCC equipment authorization program does not generally apply to amateur station transmitters"), seen only as a search snippet because fcc.gov returned HTTP 403 to this tool.
- 47 CFR 97.315 (as amended 90 FR 57712, Dec 12, 2025): "(a) Any external RF power amplifier (see § 2.815 of the FCC Rules) manufactured or imported for use at an amateur radio station must be certificated for use in the amateur service in accordance with subpart J of part 2 of the FCC Rules. No amplifier capable of operation below 144 MHz may be constructed or modified by a non-amateur service licensee without a grant of certification from the FCC. (b) The requirement of paragraph (a) does not apply if one or more of the following conditions are met: (1) The amplifier is constructed or modified by an amateur radio operator for use at an amateur station. (2) [Reserved] (3) ..." 97.3(a)(18) defines an external RF power amplifier as "A device capable of increasing power output when used in conjunction with, but not an integral part of, a transmitter." cwht's PA is integral, so 97.315 does not apply at all; even a separate amateur-built amplifier is exempt under (b)(1). 97.317 (certification standards: 97.307(d)/(e) spurious limits, 15 dB gain cap, no 26-28 MHz gain) applies only to amplifiers seeking certification.
- 47 CFR 2.815(b) restates the marketing prohibition for uncertified external amplifiers "capable of operation on any frequency or frequencies below 144 MHz"; irrelevant to a non-marketed integral PA.
- The RP2350, LCD and DC-DC converters are unintentional radiators. 47 CFR 15.23: "(a) Equipment authorization is not required for devices that are not marketed, are not constructed from a kit, and are built in quantities of five or less for personal use. (b) It is recognized that the individual builder of home-built equipment may not possess the means to perform the measurements for determining compliance with the regulations. In this case, the builder is expected to employ good engineering practices to meet the specified technical standards to the greatest extent practicable. The provisions of § 15.5 apply to this equipment." A PCBWay-assembled board built to the owner's own design is not "constructed from a kit".
- Caveat: the exemption is for equipment that "transmits solely on ARS frequencies" and for equipment that is not marketed. A synthesizer that can physically tune outside 144-148 MHz is fine in a non-marketed personal build, but firmware-locking transmit to the amateur band is both good practice and required anyway by 97.307(b) ("Emissions resulting from modulation must be confined to the band or segment available to the control operator").

Sources: https://docs.fcc.gov/public/attachments/DA-18-581A1.pdf ; https://www.ecfr.gov/current/title-47/section-97.315 ; https://www.ecfr.gov/current/title-47/section-97.317 ; https://www.ecfr.gov/current/title-47/section-2.815 ; https://www.ecfr.gov/current/title-47/section-15.23 ; https://www.federalregister.gov/documents/2025/12/12/2025-22633/delete-delete-delete-removal-of-obsolete-regulations ; https://www.fcc.gov/wireless/bureau-divisions/mobility-division/amateur-radio-service (403; snippet)

### F10. Station identification (97.119) constrains an automatic CW identifier to 20 WPM

47 CFR 97.119: "(a) Each amateur station ... must transmit its assigned call sign on its transmitting channel at the end of each communication, and at least every 10 minutes during a communication ... (b) The call sign must be transmitted with an emission authorized for the transmitting channel in one of the following ways: (1) By a CW emission. When keyed by an automatic device used only for identification, the speed must not exceed 20 words per minute; ..." This bears on any keyer memory or beacon-style auto-ID feature. The keyer type (straight key vs iambic paddle) has no regulatory significance: both produce A1A.

Source: https://www.ecfr.gov/current/title-47/section-97.119

### F11. Keying bandwidth and band edges (97.307(a)-(b), 97.3(a)(8))

97.3(a)(8): "Bandwidth. The width of a frequency band outside of which the mean power of the transmitted signal is attenuated at least 26 dB below the mean power of the transmitted signal within the band." 97.307(b) requires emissions to be confined to the band and prohibits "keyclick interference". No numeric CW bandwidth or rise-time is stated in Part 97; the accepted engineering basis is ITU-R SM.1138 (necessary bandwidth for A1A, Bn = B x K with K = 3 to 5, so about 100-150 Hz at 25 WPM) and the ARRL Handbook's customary 5 ms keying rise/fall. Neither was fetched in this session (Open items), so this finding is Medium confidence for the numbers and High for the rule text. Practical consequence: the transmit carrier must stay far enough inside 144.000 and 148.000 MHz that the 26 dB bandwidth is inside the band; 1 kHz of guard is ample for A1A.

Sources: https://www.ecfr.gov/current/title-47/section-97.307 ; https://www.ecfr.gov/current/title-47/section-97.3 ; ITU-R SM.1138 https://www.itu.int/rec/R-REC-SM.1138 (not fetched)

### F12. Rule currency: 2025-2026 changes to the cited sections do not affect 2 m CW

Federal Register API results for 47 CFR Part 97 rules published since 2025-01-01: 90 FR 57698 "Delete, Delete, Delete; Removal of Obsolete Regulations" (2025-12-12, effective 2026-02-10; revised 97.315, now shows (b)(2) [Reserved]); 91 FR 1405 "Implementation of the Final Acts of ... WRC-15 ..." (2026-01-14, effective 2026-02-13; amendatory instructions 18-22 revise only the 60 m rows of 97.301/97.305, 97.303(h), 97.307(f)(14) and 97.313(f)/(i)). The Dec 2023 / Jan 2024 amendments replaced HF symbol-rate limits with a 2.8 kHz bandwidth in 97.307(f)(3) and did not touch (e). 97.13(c) is unchanged since 2020-06-01; 1.1307 since 2021-06-29 (eCFR version history).

Sources: eCFR version API (`.../versions/title-47.json?part=97&section=97.307`, `...section=97.305`, `...section=97.313`, `...section=97.301`, `...section=97.13`; `...part=1&section=1.1307`) ; Federal Register API `https://www.federalregister.gov/api/v1/documents.json?conditions[cfr][title]=47&conditions[cfr][part]=97&conditions[publication_date][gte]=2025-01-01`

## 4. Implications for cwht

Tags: REQ-candidate (proposed requirement, with verification method per charter §9), RISK-candidate, DECISION-needed, ACTION.

### Candidate requirements (numbers are proposals; owner to confirm at SRR)

- **REQ-candidate RF-01 (frequency privileges, F1/F4).** The transmitter shall be capable of emitting only when the carrier frequency is within 144.000-148.000 MHz (ITU Region 2, 97.301(a)); the firmware transmit inhibit shall be enforced independently of the display/tuning logic (safety-critical per SWE-134 scoping). Verify: HostUnit (boundary tests), Emulation (attempt to key at 143.999 and 148.001), Bench (counter).
- **REQ-candidate RF-02 (band-edge guard, F11).** With a 26 dB occupied bandwidth budget of 500 Hz for A1A, the transmit carrier shall be limited to 144.001-147.999 MHz so that the emission stays inside the band per 97.307(b). Verify: Analysis (keying spectrum), Bench (spectrum analyzer, RBW 100 Hz).
- **REQ-candidate RF-03 (emission type, F1).** The transmitter shall produce only A1A (on-off keyed unmodulated carrier). No tone or other modulation shall be applied to the carrier; the sidetone shall be an audio-only path. Rationale: 144.000-144.100 MHz is CW-only; MCW is a different emission type. Verify: Inspection (design), Bench (spectrum analyzer shows a single carrier under key-down).
- **REQ-candidate RF-04 (spurious and harmonic emissions, F2).** At every power setting up to the maximum rated output, and across 144.000-148.000 MHz, each spurious emission delivered to the antenna port shall be (a) not more than 25 µW (-16.0 dBm) and (b) at least 40 dB below the fundamental, per 97.307(e). At 5.0 W this is 53.0 dB; at the proposed 6.0 W upper tolerance it is 53.8 dB. **Design target: at least 60 dB below the fundamental at 5 W (spurious not more than -23 dBm, 5 µW)**, giving about 7 dB margin and meeting the over-25 W tier. Measurement span: 9 kHz to 1.5 GHz (tenth harmonic of 148 MHz, by analogy with 2.1057), with particular attention to 2f-7f. Verify: Analysis (SPICE harmonic content of the PA plus LPF S-parameter simulation with component parasitics and SRF), Bench (spectrum analyzer through a calibrated attenuator into 50 ohms).
- **REQ-candidate RF-05 (power rating, F3).** Nominal output 5.0 W into 50 ohms; maximum output including tolerance not to exceed 6.0 W (DECISION-2) at any supply voltage in the 2S Li-ion range; RF-04 shall hold at the maximum. 97.313(b) (1.5 kW) is trivially met. Verify: Bench (power meter across 6.0-8.4 V supply).
- **REQ-candidate RF-06 (selectable power, F3/F8).** Output power shall be operator-selectable in at least four steps spanning 0.5 W to 5 W (e.g. 0.5 / 1 / 2 / 5 W), with the selected level shown on the LCD, in support of 97.313(a) "minimum transmitter power necessary" and RF-exposure mitigation. Verify: Bench.
- **REQ-candidate RF-07 (keying envelope, F11).** Carrier rise and fall times shall be 3-6 ms (target 5 ms) with no overshoot, at all keyer speeds up to the maximum (e.g. 50 WPM), so that 97.307(b) keyclick and 97.307(a) necessary-bandwidth provisions are met. Verify: Analysis, Bench (oscilloscope envelope; spectrum analyzer).
- **REQ-candidate RF-08 (unintended radiation, F2/F9).** Chassis and cable radiation from the digital section (RP2350, LCD, DC-DC, USB charging) shall be minimized by design (enclosure bonding, filtered feedthroughs, spread-spectrum-free clocks near 144 MHz receive) per 97.307(c) and 15.23(b) good engineering practice; no numeric limit is imposed by rule. Verify: Analysis (clock harmonic map vs 144-148 MHz and vs the IF), Bench (near-field probe, receiver birdie scan).
- **REQ-candidate FW-01 (station ID aid, F10).** The firmware shall provide a transmit-elapsed timer with a 10-minute identification reminder and, if a message memory can send the call sign automatically, shall cap that message speed at 20 WPM (97.119(b)(1)). Verify: HostUnit, Emulation.
- **REQ-candidate FW-02 (keyer, owner core requirement).** The keyer shall support a straight key (direct keying) and an iambic paddle (mode A and mode B) selectable by the operator; both produce identical A1A envelopes per RF-07. (No regulatory difference; recorded here because the owner named it a core requirement.) Verify: HostUnit (timing tests), Bench.
- **REQ-candidate RFX-01 (RF exposure evaluation deliverable, F6-F8).** Before first on-air transmission the project shall produce an RF Exposure Evaluation (Analysis) covering: the operating postures in the ConOps; time-averaged power using the OET 65 B method (5 W x 0.40 CW duty factor x worst-case on-air fraction in 6 and 30 minute windows); MPE compliance distances for non-household persons (0.2 mW/cm2) and for the operator (1.0 mW/cm2); and, for any posture with the antenna within 20 cm of a person, a SAR estimate with documented basis (DECISION-1). The evaluation is filed with station records (no FCC filing is required). Verify: Inspection (review of the document at TRR).
- **REQ-candidate RFX-02 (exposure controls in the product, F7/F8).** The device shall (a) offer the power steps of RF-06, (b) display cumulative key-down time over sliding 6-minute and 30-minute windows (source-based time-averaging evidence for the operator), and (c) carry in its user documentation a statement of the evaluated postures and the minimum separation distances from Finding F8 for persons other than the licensee. Verify: HostUnit, Inspection.
- **REQ-candidate OPS-01 (band plan defaults, F5).** Default tuning presets shall be within the ARRL weak-signal segment 144.050-144.300 MHz (e.g. 144.100 and 144.200 MHz), with the CW-only segment 144.000-144.100 MHz highlighted on the display; operation elsewhere in 144-148 MHz remains available (DECISION-3). Verify: Inspection, Emulation.

### Constraints

- No FCC equipment authorization, filing, or label is required for the transceiver (F9). No FCC filing is required for the RF exposure evaluation either; it is a licensee record (97.13(c), 1.1307(b)(1)(ii) "Upon request by the Commission").
- 97.315/97.317 do not apply to cwht's integral PA. They would apply only if a separate external amplifier were ever marketed; an amateur-built one is exempt under 97.315(b)(1).
- The unit must not be marketed or built in more than five copies without revisiting 15.23 and the DA 18-581 marketing caveats.

### Risks

- **RISK-candidate REG-1 (RF exposure method gap for VHF portables).** For handheld use at 144 MHz there is no exemption (F6), the nominal metric is SAR (F7), and the FCC has published no amateur handheld SAR method; the only quantitative basis found is SAR-by-analogy from certified commercial VHF handhelds (F8, 0.35 W/kg per W at 1 g). Likelihood of a compliance challenge is low for a single licensee, but the project's "proven beforehand" goal requires a defensible evaluation. Mitigations: DECISION-1 posture; RFX-01 documents the analogy and its caveats; RF-06 power steps; consider a numerical SAR estimate (open-source FDTD with a simple phantom) if the owner wants Analysis-grade evidence.
- **RISK-candidate REG-2 (general-population SAR margin at 5 W).** By the F8 analogy, 5 W at 50% duty gives about 1.75 W/kg, above the 1.6 W/kg general-population limit; the licensee's own 8 W/kg limit has more than 4x margin. Anyone who is not the licensee or a trained household member should not hold the radio while it transmits at 5 W; document this and rely on RF-06 (2 W step gives 44% of limit).
- **RISK-candidate RF-1 (harmonic suppression).** 53 dB minimum and 60 dB target from a 5 W PA means the low-pass filter must deliver roughly 40-50 dB at 288 MHz on top of the PA's intrinsic second-harmonic level; SMD inductor self-resonance in the 300-600 MHz region and PCB layout leakage commonly erode simulated attenuation. Mitigation: SPICE with vendor parasitic models, S-parameter check on the NanoVNA of the assembled filter, elliptic or 7th-order topology, shielding between PA and filter.
- **RISK-candidate RF-2 (3rd harmonic in 70 cm).** 432-444 MHz lands in the 70 cm amateur band shared with federal radiolocation (97.303(b), (m)); even a compliant -16 dBm harmonic is a strong signal to a nearby 70 cm receiver. Mitigation: RF-04 target, operating awareness.
- **RISK-candidate RF-3 (band-edge violation).** Tuning to 144.000 MHz exactly would place half of the keying spectrum below the band edge; RF-02 removes this.
- **RISK-candidate REG-3 (rule drift).** 97.305/97.307/97.313 were amended in 2023, 2024 and 2026; 1.1307 in 2021. Mitigation: ACTION-5 re-check before CDR and before first on-air.

### Decisions needed

- **DECISION-1 (exposure posture in the ConOps).** Define whether the primary operating posture is (a) handheld/body-worn (antenna within 20 cm: portable device, SAR regime, evaluation by analogy or numerical SAR) or (b) body-separated (radio on a surface or short mast with the antenna at least 0.33 m from everyone: mobile device, MPE regime with an exemption available at 0.51-0.72 m for 1-2 W time-averaged ERP). A CW handheld operated with a paddle and headphones may naturally sit on a surface, which makes (b) realistic and simplifies compliance evidence.
- **DECISION-2 (maximum output and tolerance).** Fix the maximum rated output (proposal: 5.0 W nominal, 6.0 W maximum) because the 25 µW cap is absolute and the required suppression grows with power.
- **DECISION-3 (transmit range policy).** Whole 144-148 MHz CW permitted by rule versus a default lock to 144.000-144.300 MHz with an "expert" unlock to honor the voluntary band plan.
- **DECISION-4 (harmonic design margin).** Adopt the 60 dB target (this report's proposal) or a different margin policy; record as an ADR because it drives filter order, PA topology and enclosure partitioning.
- **DECISION-5 (exposure telemetry scope).** Whether the sliding-window key-down accumulator in RFX-02 is a safety-critical function (SWE-134 scope, MC/DC coverage) or a convenience feature.

### Actions

- **ACTION-1.** Add the primary rule texts to `docs/references/md/regulatory/` (the charter marks this "to be added"): 97.3, 97.13, 97.101, 97.119, 97.301, 97.303, 97.305, 97.307, 97.313, 97.315, 97.317, 1.1307, 1.1310, 2.201, 2.815, 2.1057, 2.1091, 2.1093, 15.23 as of eCFR issue 2026-09-23; plus FCC 19-126, OET 65 B, DA 18-581, the Tell QEX paper. Plain-text extracts of all of these are in this session's scratch directory (`.../scratchpad/ecfr/`); copying them into the repo needs the owner's or parent agent's write scope.
- **ACTION-2.** Write the RF Exposure Evaluation (RFX-01) as a PDR analysis product, updated with the measured antenna gain at CDR and the bench-measured power at TRR.
- **ACTION-3.** Write the 97.307(e) bench procedure (span 9 kHz-1.5 GHz, attenuator calibration, RBW, pass criteria -16 dBm and 40 dBc, plus the -23 dBm target) for TRR.
- **ACTION-4.** Confirm the local frequency coordinator's 2 m plan and whether 144.100 MHz is used as a CW calling frequency in the owner's region before fixing OPS-01 presets.
- **ACTION-5.** Re-check eCFR versions of 97.13, 97.301, 97.305, 97.307, 97.313 and 1.1307 before CDR and before first on-air; the API query in Method makes this a one-line check.

## 5. Confidence

| Finding | Confidence | Basis |
|---|---|---|
| F1 97.305 CW whole band; 144.0-144.1 CW-only | High | Verbatim eCFR text, issue 2026-09-23, cross-checked with LII |
| F2 97.307(e) limits; 53.0 dB at 5 W | High (rule and arithmetic); Medium (harmonic landing spots) | Verbatim text; python arithmetic; allocation table not fetched |
| F3 97.313 | High | Verbatim eCFR text |
| F4 97.301/97.303 | High | Verbatim eCFR text |
| F5 ARRL band plan table | High (content); Low (144.100 as CW calling; plan date) | ARRL page fetched; no revision date on page; calling convention only in secondary sources |
| F6 No exemption for VHF handheld; evaluation required; dates | High | Verbatim 1.1307(b)(3), 97.13(c), FCC 19-126 fn 143 and para 116, FR effective-date notices |
| F7 Limits and regime | High | Verbatim 1.1310, 2.1093 |
| F8 Evaluation method and numbers | Medium | OET 65 B duty factors verbatim (High); FCC acceptance quoted (High); SAR-by-analogy 0.35 W/kg/W from one 2021 QEX paper, author's own caveats (Medium-Low); distances assume 0 dBd whip and worst-case reflection (conservative Analysis) |
| F9 Homebrew status | High (97.315, 2.815, 15.23 verbatim; DA 18-581 quoting Commission decisions); Medium (fcc.gov page seen only as snippet) | |
| F10 97.119 | High | Verbatim |
| F11 Keying bandwidth numbers | Medium | Rule text High; ITU-R SM.1138 and Handbook values from memory, not fetched |
| F12 Rule currency | High | eCFR version API and Federal Register amendatory text |

## 6. Open items

1. FCC guidance on how amateurs should evaluate portable (within 20 cm) devices below 300 MHz remains unpublished as far as this search found; the ARRL's May 2020 clarification request has no located response, and no 2025-2026 ARRL RF Safety Committee handheld guidance was found. Re-search before PDR; if nothing appears, DECISION-1 posture (b) is the low-risk path.
2. fcc.gov HTML pages (Amateur Radio Service page, OET RF-device page) returned HTTP 403 to this tool; the "equipment authorization program does not generally apply to amateur station transmitters" statement is cited from a search snippet, backed by DA 18-581's quotations of Commission decisions. Owner could confirm in a browser.
3. OET 65 Supplement B remains the 1997 edition; its handheld text reflects the pre-2021 categorical exemption. Check for any reissue.
4. ARRL band plan page has no revision date; obtain the dated PDF from ARRL if a citable version is needed.
5. ITU-R SM.1138 (A1A necessary bandwidth) and the ARRL Handbook keying rise-time recommendation were not fetched; RF-02/RF-07 numbers should be confirmed against them.
6. The US Table of Frequency Allocations (47 CFR 2.106) was not fetched; the harmonic landing spots in F2 are from general knowledge and should be confirmed before they are used in an interference-risk argument.
7. Whether the owner intends any operation from a vehicle (mobile installation) or with an external antenna; either changes the RF exposure evaluation inputs (antenna gain, height, separation) and may add a 97.13(a) location consideration.
8. Scratch copies of all fetched primary texts exist only in the session scratch directory; ACTION-1 moves them into `docs/references/md/regulatory/`.
