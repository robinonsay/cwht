# RF exposure evaluation shape for cwht: worked OET 65 B analysis and the SAR situation for a 2 m CW handheld

**Assignment key:** rf-exposure
**Author:** Claude (research subagent), 2026-09-25
**Status:** research input for SRR; not a baseline. Candidate requirements are proposals for the requirements owner. This report extends `part97-regulatory-basis.md` (Findings F6 to F8, RISK-candidates REG-1 and REG-2, DECISION-1, RFX-01, RFX-02); it does not repeat the rule-text derivations there except where a number is recomputed.
**Rule text currency:** CFR quotations were pulled from the eCFR versioner API for issue date 2026-09-23 (`https://www.ecfr.gov/api/versioner/v1/full/2026-09-23/title-47.xml?part=1&section=1.1310` and likewise for 1.1307, 2.1091, 2.1093 and part 97 section 97.13). 1.1310 carries the citation [85 FR 18145, Apr. 1, 2020]; 2.1093 [... 85 FR 18147, Apr. 1, 2020; 85 FR 38739, June 26, 2020]; 97.13 [... 85 FR 18151, Apr. 1, 2020].

## 1. Question

For cwht (pocket 2 m true-CW handheld, 5 W nominal, US General-class owner, friends who hold at least a Technician license per SI-030, radios handed around per SI-019):

1. For output steps 0.5, 1, 2 and 5 W, the OET 65 Supplement B CW duty factor of 40 %, and on-air fractions of 50 % and 100 % in the 6 minute (occupational/controlled, licensee) and 30 minute (general population/uncontrolled) averaging windows, compute the time-averaged power.
2. With a 0 dBd handheld whip assumption (and a stated range of realistic HT whip gains from the literature), compute the maximum permissible exposure (MPE) compliance distances per 47 CFR 1.1310 for both tiers, and the 1.1307(b)(3)(i)(C) exemption distances.
3. Summarize the specific absorption rate (SAR) situation for portable use within 20 cm at 144 MHz (1.1307(b), 1.1310(d), 2.1093, FCC 19-126 footnote 143, the analogy data the earlier report cited) and give the best available estimate of SAR versus power for a handheld at the head or in the hand, with confidence.
4. Derive candidate L1 requirements: selectable power steps, a default power for scenarios in which a non-licensee holds the radio, duty limiting, on-screen exposure posture, labeling and user documentation, and what evidence the SRR package can present (analysis per OET 65 B) versus what cannot be closed (SAR measurement).

## 2. Method

**Primary texts fetched 2026-09-25** (all kept in the session scratch directory `.../scratchpad/rfx/`; nothing written to the repo except this report):

- 47 CFR 1.1307, 1.1310, 2.1091, 2.1093, 97.13 via the eCFR versioner API (`curl -sL --compressed`), XML stripped to text with a short Python script.
- FCC 19-126 (Second Report and Order, ET Docket 19-226, adopted 2019-11-27), `https://docs.fcc.gov/public/attachments/FCC-19-126A1.pdf`, `pdftotext -layout`, grepped for footnotes 100, 143, 144 and paragraphs 32 to 34 and 116.
- OET Bulletin 65 Edition 97-01 (main bulletin), `https://transition.fcc.gov/Bureaus/Engineering_Technology/Documents/bulletins/oet65/oet65.pdf`: Equations (3) to (7), pages 19 to 21 (far-field power density, ERP to EIRP conversion, ground-reflection factors).
- OET Bulletin 65 Supplement B Edition 97-01 (amateur), `.../oet65b.pdf`: Table 2 duty factors (p. 14), the source-based time-averaging recipe (pp. 13 to 14), exposure tiers (p. 11), footnote 7 (p. 4), Table 32 (p. 44).
- OET Bulletin 65 Supplement C Edition 01-01 (June 2001, SAR evaluation of mobile and portable devices), `.../oet65c.pdf`: push-to-talk (PTT) test position, source-based time averaging, usage-based duty factors.
- FCC OET Laboratory Division TCB Workshop slides, April 27, 2022, "Mobile and Portable Device RF Exposure Policies, KDB Publication 447498 D01", `https://transition.fcc.gov/oet/ea/presentations/files/apr22/43-RF-Exposure-Policies.pdf` (scope of the KDB 447498 v06 SAR exclusion thresholds and the FCC's 2022 draft extension of SAR exemption thresholds below 300 MHz).
- Richard Tell K5UJU, "Amateur Portable Radios (Handheld Transceivers): Exposure Considerations Based on SAR", QEX July/August 2021, pp. 11 to 15 (ARRL PDF).
- Gregory Lapin N9GL, "Understanding the FCC Exposure Rules for Handheld Radios", QST February 2026, pp. 55 to 57, `https://www.arrl.org/files/file/QST/This%20Month%20in%20QST/2026/February/FCC%20Exposure%20Rules%20for%20Handheld%20Radios.pdf`. The article states it was reviewed by Kevin Graf of the FCC Office of Engineering and Technology. Its Table 1 tabulates the per-band SAR reference values from the Tell study; this is the newest source found and post-dates the earlier report's sources.
- ARRL RF Safety Committee Report to the ARRL Board, July 2023, `https://www.arrl.org/files/file/ARRL%20RF%20Safety%20Report%202023-07.pdf`, item 1.4 (FCC engineers' position on SAR by analogy; status of the OET 65 B rewrite).
- Antenna gain literature (WebFetch): John Huggins KX4O, "HT Antenna Comparisons", hamradio.me (chamber EIRP measurements at 146 MHz, article dated 2018-10-21 with page date 2021-01-01); Julian Moss G4ILO, "2m HT antenna shootout", amateurradio.com, 2011-04-23 (relative field-strength readings); L-com LCANRBD1027 product page (vendor gain claim).
- Stakeholder inputs re-read for this report: SI-003 (5 W), SI-019 (radios handed to friends), SI-030 (all operators licensed; occupational limits for operators, general population for bystanders), SI-034 (8 h battery at 1:9 transmit-to-receive), SI-035 (at most 5 complete units), SI-036 (semi break-in).

**Not reachable from this tool:** `apps.fcc.gov` KDB attachments (KDB 447498 D01 v06 and KDB 643646 D01) returned "Access Denied" to curl and HTTP 403 to WebFetch; `fccid.io` and `fcc.report` SAR reports for Motorola VHF portables (FCC IDs AZ489FT4948, AZ489FT7098) returned a bot-check page; `www.fcc.gov` HTML and the October 2023 TCB slides returned HTML/403. Consequences are marked Low confidence in F9 and listed in Open items. The WebSearch budget for this session was exhausted after 11 searches; the last three planned searches (academic VHF SAR data, NIST body-effect data, KDB 447498 revision status) were not performed.

**Local computation:** `python3` script `rfx_calc.py` (reproduced in the Appendix). Formulas are cited to the primary text next to each table. Formatting note: em and en dashes in quoted text were replaced by hyphens; no words were changed.

## 3. Findings

### F1. Which limits and which regime apply to cwht, and to whom (rule text)

The chain established in the earlier report (F6, F7) is confirmed against the 2026-09-23 eCFR text and sharpened with SI-030:

- **Portable device.** 2.1093(b): "A portable device is defined as a transmitting device designed to be used in other than fixed locations and to generally be used in such a way that the RF source's radiating structure(s) is/are within 20 centimeters of the body of the user." A handheld with its whip in the hand or at the face is portable; the same radio on a table with the whip at 20 cm or more from everyone is a mobile device (2.1091(b)).
- **Metric for portables is SAR, not MPE.** 1.1310(d)(2): MPE limits "may be used instead of whole-body SAR limits ... except for portable devices as defined in § 2.1093 of this chapter as these evaluations shall be performed according to the SAR provisions in § 2.1093." 2.1093(d)(1): "The SAR limits specified in § 1.1310(a) through (c) of this chapter shall be used for evaluation of portable devices transmitting in the frequency range from 100 kHz to 6 GHz."
- **Limits.** 1.1310(b) occupational/controlled: 0.4 W/kg whole body; 8 W/kg peak spatial-average over any 1 g; extremities (hands, wrists, feet, ankles, pinnae) 20 W/kg over any 10 g; averaging time not to exceed 6 minutes. 1.1310(c) general population/uncontrolled: 0.08 W/kg whole body; 1.6 W/kg per 1 g; extremities 4 W/kg per 10 g; averaging time not to exceed 30 minutes. 1.1310(e)(1) Table 1, 30 to 300 MHz MPE: occupational 61.4 V/m, 0.163 A/m, 1.0 mW/cm2, 6 min; general population 27.5 V/m, 0.073 A/m, 0.2 mW/cm2, 30 min.
- **Who is in which tier.** 97.13(c)(1): the licensee "may evaluate their operation with respect to members of his or her immediate household using the occupational/controlled exposure limits in § 1.1310, provided appropriate training and information has been accessed by the amateur licensee and members of his/her household. RF exposure of other nearby persons who are not members of the amateur licensee's household must be evaluated with respect to the general population/uncontrolled exposure limits." OET 65 B p. 11: "occupational/controlled exposure limits apply to amateur licensees and members of their immediate household (but not their neighbors)". Under SI-030 every operator is a licensee and, when a friend operates a cwht unit under their own call sign, that friend is the licensee of that transmission and is evaluated at the occupational tier; anyone nearby who is neither the operating licensee nor a trained member of that licensee's household is evaluated at the general population tier. A non-licensee who holds and keys the radio (permitted as third-party participation with a control operator present, 97.115) is general population.
- **Time averaging for portables.** 2.1093(d)(3): for occupational SAR "time averaging provisions of the limits may be used in conjunction with the maximum duty factor". 2.1093(d)(4): for general population portables the duty-factor provisions "may not be used ... However, 'source-based' time averaging based on an inherent property of the RF source is allowed over a time period not to exceed 30 minutes." OET 65 C (2001) pp. 16 to 17 adds: "Duty factors related to device usage, frequency hopping or other similar transmission conditions are normally not acceptable as source-based, time averaging factors for RF evaluations", and p. 47: "for certain devices that are hardware limited by design and are restricted to operate with a maximum RF duty factor, source-based time averaging ... may be considered." Reading for cwht: the 40 % conversational-CW duty factor (an emission property of Morse keying) and any firmware-enforced hardware limit are source-based; the operator's on-air fraction is usage-based and may be used for the licensee tier but not for a general-population evaluation.
- **No exemption within 20 cm.** FCC 19-126 footnote 143: "there are no exemption criteria below 239 MHz for portable devices (or for any antenna at less than 20 cm) other than the 1 mW blanket exemption." cwht's smallest time-averaged power in this report (0.5 W step, 40 % duty, 50 % on-air) is 0.1 W, 100 times the 1 mW exemption.
- **Evaluation is the licensee's record, not a filing.** 1.1307(b)(1)(ii): "Upon request by the Commission, the party seeking or holding such authorization must electronically submit technical information showing the basis for such compliance, either by exemption or evaluation." OET 65 B p. 7: "If an amateur station is evaluated and found to be in compliance with the rules, no paperwork need be filed with the FCC".
- **FCC acceptance of the OET 65 B method.** FCC 19-126 footnote 100: OET 65 Supplement B and the ARRL's "RF Exposure and You" guidance "has been available for years and is an acceptable method to determine compliance." Paragraph 32: where "antenna performance characteristics may not be well understood for a particular amateur radio installation, the most feasible option of demonstrating compliance remains to be evaluated". Paragraph 33: "An exemption determination ... is not an exemption from compliance, only from routine RF exposure evaluation."

Sources: eCFR API texts as in Method; FCC 19-126 fn 100, fn 143, paras 32 to 33; OET 65 B pp. 7, 11; OET 65 C pp. 16 to 17, 47.

### F2. Time-averaged power for the four power steps (OET 65 B recipe)

OET 65 B p. 13: "To obtain an easy estimate of average power, multiply the transmitter peak envelope power by the duty factor, then multiply that result by the worst-case percentage of time the station would be on the air in, e.g., a 6-minute period (the averaging time for controlled exposure) or a 30-minute period (the averaging time for uncontrolled exposure). This is an example of 'source-based' time averaging." Table 2 (p. 14): Conversational CW 40 %; Carrier 100 % ("A full carrier is commonly used for tune-up purposes"). For A1A, PEP equals key-down carrier power (97.3(b)(9)), so the step value is the PEP.

Table 1. Time-averaged power P_avg = P x duty x on-air fraction (W). The same fraction is applied to the 6 min and 30 min windows, as in the OET 65 B example where "the result would be the same for either controlled or uncontrolled exposure".

| Step P (W) | CW 40 %, on-air 50 % | CW 40 %, on-air 100 % | Carrier 100 %, on-air 100 % (tune-up) | Typical SI-034 1:9 ratio (on-air 10 %) |
|---|---|---|---|---|
| 0.5 | 0.10 | 0.20 | 0.50 | 0.02 |
| 1.0 | 0.20 | 0.40 | 1.00 | 0.04 |
| 2.0 | 0.40 | 0.80 | 2.00 | 0.08 |
| 5.0 | 1.00 | 2.00 | 5.00 | 0.20 |

Notes: "on-air 100 %" for CW means the key is worked continuously for the whole window (a long CQ or ragchew); the 40 % factor still applies because Morse elements and spaces are an inherent property of the emission. The tune-up carrier column is the only case in which the transmitter runs at 100 % duty; cwht has no FM or data mode, so 100 % duty only arises from a deliberate tune function or a stuck key. The last column is the owner's battery-life operating point (SI-034) and is representative, not worst case; the evaluation must use a worst-case window.

Sources: OET 65 B pp. 13 to 14 (Table 2); 97.3(b)(9) via the earlier report F3.

### F3. MPE compliance distances for the mobile posture (antenna 20 cm or more from everyone), 0 dBd whip

Formulas (OET 65 main bulletin, pp. 19 to 21): Equation (3) S = P G / (4 pi R^2) with G the numeric gain relative to isotropic; Equation (5) EIRP = 1.64 x ERP; Equation (7) S = 2.56 EIRP / (4 pi R^2) using "the EPA-recommended reflection factor of (1.6)^2 = 2.56" for a conservative ground-reflection case; Equation (6) with 100 % reflection gives a factor of 4. OET 65 p. 19: "These equations are generally accurate in the far-field of an antenna but will over-predict power density in the near field, where they could be used for making a 'worst case' or conservative prediction." At 144 MHz the wavelength is 2.082 m and lambda/2pi is 0.331 m, so every distance below is in the near-to-transition region and the estimates are conservative by construction.

Assumption: 0 dBd whip, so ERP = P_avg and EIRP = 1.64 x P_avg (see F4 for why 0 dBd is a conservative upper bound for a pocket HT). Limits: 0.2 mW/cm2 = 2 W/m2 (general population, 30 min); 1.0 mW/cm2 = 10 W/m2 (occupational, 6 min). R = sqrt(F x EIRP / (4 pi S)), F = 1.00 (free space) or 2.56 (reflection).

Table 2. Distance from the antenna at which the time-averaged power density equals the MPE limit (m), 0 dBd.

| Step (W) | Mode / on-air | P_avg (W) | General population, free space | General population, 2.56 reflection | Occupational, free space | Occupational, 2.56 reflection |
|---|---|---|---|---|---|---|
| 0.5 | CW 50 % | 0.10 | 0.08 | 0.13 | 0.04 | 0.06 |
| 0.5 | CW 100 % | 0.20 | 0.11 | 0.18 | 0.05 | 0.08 |
| 0.5 | carrier | 0.50 | 0.18 | 0.29 | 0.08 | 0.13 |
| 1 | CW 50 % | 0.20 | 0.11 | 0.18 | 0.05 | 0.08 |
| 1 | CW 100 % | 0.40 | 0.16 | 0.26 | 0.07 | 0.12 |
| 1 | carrier | 1.00 | 0.26 | 0.41 | 0.11 | 0.18 |
| 2 | CW 50 % | 0.40 | 0.16 | 0.26 | 0.07 | 0.12 |
| 2 | CW 100 % | 0.80 | 0.23 | 0.37 | 0.10 | 0.16 |
| 2 | carrier | 2.00 | 0.36 | 0.58 | 0.16 | 0.26 |
| 5 | CW 50 % | 1.00 | 0.26 | 0.41 | 0.11 | 0.18 |
| 5 | CW 100 % | 2.00 | 0.36 | 0.58 | 0.16 | 0.26 |
| 5 | carrier | 5.00 | 0.57 | 0.91 | 0.26 | 0.41 |

Reading: with the conservative reflection factor and a dipole-equivalent whip, a bystander (general population) is at or below the MPE limit at 0.58 m or more from the antenna during continuous 5 W CW, at 0.41 m for a 50 % on-air fraction, and at 0.91 m during a 5 W tune-up carrier. For the licensee (occupational tier) the corresponding distances are 0.26 m, 0.18 m and 0.41 m; for the two CW cases the occupational distance is at or inside the 20 cm portable boundary, meaning that whenever the licensee is 20 cm or more from the antenna the MPE tier is met at every power step, and inside 20 cm the SAR regime of F5 governs anyway. All rows for the 0.5 W and 1 W steps put the general-population distance at 0.29 m or less even for a continuous carrier.

Exemption distances (1.1307(b)(3)(i)(C), Table 1, 30 to 300 MHz: ERP not more than 3.83 R^2 W with R at least lambda/2pi; "available maximum time-averaged power may be used in lieu of ERP if the physical dimensions of the radiating structure(s) do not exceed the electrical length of lambda/4 or if the antenna gain is less than that of a half-wave dipole (1.64 linear value)", which a pocket HT whip satisfies). At 144 MHz the floor is 0.331 m (0.322 m at 148 MHz) and the exempt ERP at the floor is 0.42 W. Derivation check: 3.83 R^2 is the general-population MPE (2 W/m2) with 100 % reflection (factor 4, OET 65 Equation 6) converted from EIRP to ERP: 2 x 4 pi / 4 / 1.64 = 3.83; FCC 19-126 fn 144 indeed cites "OET Bulletin 65, Equation 6". The exemption threshold is therefore stricter than the Equation (7) evaluation, which is why exempt distances exceed the evaluated distances.

Table 3. Separation at which the routine-evaluation exemption becomes available (m), 0 dBd, 144 MHz.

| P_avg (W) | Cases | Exempt separation R |
|---|---|---|
| 0.10 to 0.40 | 0.5 W and 1 W CW, 2 W CW 50 % | 0.33 (at the lambda/2pi floor) |
| 0.50 | 0.5 W carrier | 0.36 |
| 0.80 | 2 W CW 100 % | 0.46 |
| 1.00 | 5 W CW 50 %, 1 W carrier | 0.51 |
| 2.00 | 5 W CW 100 %, 2 W carrier | 0.72 |
| 5.00 | 5 W carrier | 1.14 |

Sources: OET 65 pp. 19 to 21 (Equations 3, 5, 6, 7); 1.1310(e)(1) Table 1; 1.1307(b)(3)(i)(C) and its Table 1; FCC 19-126 fn 143 and fn 144; arithmetic in the Appendix script.

### F4. Realistic HT whip gains from the literature, and the sensitivity of Table 2 to gain

The 0 dBd assumption is an upper bound for a pocket handheld; measured data:

- **KX4O chamber EIRP measurements at 146 MHz** (hamradio.me, "HT Antenna Comparisons"): Yaesu FT1D transmitting 135 mW (21.3 dBm) into each antenna; reference half-wave dipole independently measured at 2.15 dBi, giving an expected EIRP of 23.5 dBm and a measured 23.4 dBm. Results, quoted: the stock 7 inch flexible antenna is "almost 9 dB below the reference dipole" (about -9 dBd); a Diamond SRH77CA quarter-wave whip on the isolated radio measured "-17 dBd" without a counterpoise and gained "+10 dB" (to about -7 dBd) with a quarter-wave "tiger tail" counterpoise; an MFJ-1714 half-wave (about 40 inches extended) was the best at about -4 dBd. Holding the radio: "Holding it reduced the 146 MHz EIRP by 3-4 dB" for the stock antenna; the half-wave was insensitive to handling. Setup: "performed in an antenna chamber in an EIRP configuration with the most important point being no other conductors are involved."
- **G4ILO relative readings at 145 MHz** (amateurradio.com, 2011-04-23; field-strength readings at about 2 m, not a calibrated gain measurement): relative to a Yaesu VX-8GR stock whip, a 2 inch stubby -5 dB, a 2 m stubby duck -2 dB, a 19 inch telescopic quarter-wave +3 dB, a 5/8-wave telescopic +11 dB. Consistent in ordering with KX4O: a full quarter-wave on a handheld is a few dB better than a stock duck, and only long (half-wave or 5/8-wave) whips approach or exceed a dipole.
- **Vendor claim:** L-com LCANRBD1027, 136 to 174 MHz, 5.90 inch rubber duck, "1.8 dBi gain" (= -0.35 dBd), VSWR < 1.5:1; the page states no ground plane, reference radio or method, so this number is a catalog figure, not a measurement on a handheld.

Range adopted for cwht: **-9 dBd (stock-length flexible whip, radio in hand) to -4 dBd (half-wave whip), with a quarter-wave whip on a small chassis at about -7 dBd; 0 dBd is a conservative envelope and +2 dBd (5/8-wave telescopic) is the largest gain a user might plausibly screw on.** Confidence Medium: two amateur measurement sets that agree in ordering, one calibrated against a dipole in a chamber; no peer-reviewed or NIST data were retrieved (search budget exhausted, see Open items).

Table 4. Gain sensitivity, 5 W CW at 100 % on-air (P_avg 2.0 W), distances in m.

| Whip gain (dBd) | ERP (W) | General population, 2.56 reflection | General population, free space | Occupational, 2.56 reflection | Exempt separation |
|---|---|---|---|---|---|
| -17 (quarter-wave, no counterpoise, KX4O) | 0.040 | 0.08 | 0.05 | 0.04 | 0.33 (floor) |
| -9 (stock flexible whip, KX4O) | 0.25 | 0.21 | 0.13 | 0.09 | 0.33 (floor) |
| -6 | 0.50 | 0.29 | 0.18 | 0.13 | 0.36 |
| -4 (half-wave, KX4O) | 0.80 | 0.37 | 0.23 | 0.16 | 0.46 |
| 0 (this report's assumption) | 2.00 | 0.58 | 0.36 | 0.26 | 0.72 |
| +2 (5/8-wave telescopic) | 3.17 | 0.73 | 0.46 | 0.33 | 0.91 |

Reading: with any realistic pocket-HT whip the bystander distance at 5 W continuous CW is 0.4 m or less, and with the stock-length whip the routine-evaluation exemption itself becomes available at the 0.33 m floor. Caution (Tell, QEX 2021 p. 15): "for a given power, contrary to how gain is generally proportional to antenna size, smaller antennas result in a higher concentration of energy absorption", so antenna inefficiency helps the MPE (mobile) case and does not help the SAR (portable) case.

Sources: hamradio.me KX4O article; amateurradio.com G4ILO article; L-com product page; Tell QEX 2021 p. 15.

### F5. The SAR situation for use within 20 cm at 144 MHz: no exemption, no measurement path, an FCC-tolerated analogy method

- **Test positions the FCC uses for PTT radios** (OET 65 C, June 2001, p. 38 and p. 42): "Flat phantom models should be used to test handsets and push-to-talk (PTT) devices that can be held in front of the user's face or transmit in body-worn operating configurations using belt-clips, holsters or similar accessories." "Transmitters that are designed to operate in front of a person's face, in push-to-talk configurations, should be tested for SAR compliance with the front of the device positioned at 2.5 cm from a flat phantom." Body-worn devices are tested "with the accessories, including headsets and microphones, attached to the device and positioned against a flat phantom in normal use configurations."
- **Duty factor the FCC applies to PTT radios.** Tell (QEX 2021 p. 13): "For compliance determination purposes, the FCC applies a presumed duty cycle of 50% for PTT operation of the handheld." Lapin (QST Feb 2026 p. 56): "SAR measurements of handheld radios for FCC certification are typically based on a 50% transmit cycle". The Washington Laboratories RF-exposure slide deck lists "KDB 643646 D01: SAR test for PTT Radios v01r03" as the governing procedure; the KDB itself could not be fetched (Open items).
- **No SAR data exist for amateur handhelds.** ARRL RF Safety Committee, July 2023, item 1.4: "Under that condition the FCC requires SAR analysis, which is both complicated and expensive to either measure or model. ... since the FCC does not require most equipment developed for amateur radio to be certified, so they could not compel this testing and the manufacturers chose not to do so." Lapin 2026 p. 55: "Manufacturers whose products require FCC certification spend a lot of money testing SAR, and given the expense and complexity, this testing is not feasible for the radio amateur."
- **The FCC's informal position on SAR by analogy.** ARRL RFSC July 2023, item 1.4: "Communications with the engineers at the FCC have indicated that they are willing to accept this logic as evidence of compliance with the exposure regulations. However, they cautioned that this is not a blanket exemption from performing SAR analysis on handheld radios and there must be a strong similarity between the radio in the FCC equipment database and the amateur handheld radio in question. Wording to this effect has been included in section II.D of OET 65 Supplement B, which has yet to be released." As of 2026-09-25 no released revision of Supplement B was found (the FCC OET bulletins page states Bulletin 65 "is currently under review"); the 1997 edition remains the cited document in 97.13(c)(1).
- **Numerical SAR is permitted in principle but gated.** 1.1310(d)(1): "Numerical computation of SAR must be supported by adequate documentation showing that the numerical method as implemented in the computational software has been fully validated; in addition, the equipment under test and exposure conditions must be modeled according to protocols established by FCC-accepted numerical computation standards or available FCC procedures for the specific computational method." 2.1093(d)(2) repeats this. An open-source FDTD run with a simple phantom would be informative engineering analysis but would not, by itself, meet this validation and protocol bar.
- **Equipment-authorization SAR exclusion thresholds do not rescue the case.** FCC 19-126 fn 143: "these SAR-based exemptions are not valid below 300 MHz." The FCC OET's own equipment-authorization guidance (KDB 447498 D01 v06 section 4.3.1, scope confirmed by the April 2022 TCB slides as "distance <= 50 mm, 100 MHz <= frequency < 6 GHz") is a laboratory test-exclusion criterion, not a rule for licensees; a Low-confidence check against it is given in F9.

Regime conclusion for cwht, unchanged from the earlier report but now with SI-030: for the licensee operating the unit within 20 cm of their own body, the SAR limits of 1.1310(b) (8 W/kg per 1 g, 20 W/kg per 10 g in the hand, 6 min averaging with duty factor permitted) apply; for a non-licensee who holds the unit, 1.1310(c) (1.6 W/kg, 4 W/kg, 30 min, source-based averaging only); for everyone else at 20 cm or more, the MPE distances of F3 and F4.

Sources: OET 65 C pp. 38, 42; Tell QEX 2021 p. 13; Lapin QST 2026 pp. 55 to 56; ARRL RFSC July 2023 item 1.4; 1.1310(d)(1); 2.1093(d)(2); FCC 19-126 fn 143; FCC TCB slides April 2022 p. 17.

### F6. Best available estimate of SAR versus power for a 2 m handheld at the head or in the hand

**Data.** Tell mined FCC equipment-authorization SAR reports for commercial handhelds operating "extremely close to - or, in some cases, actually within" the amateur bands; values are "normalized to 1 W and are relative to a duty cycle of 50% based on the push-to-talk (PTT) operation", and "The results plotted in Figures 2 and 3 encompass the absolute maximum reported local SARs for each handheld, regardless of a particular accessory, in the interest of conservatism" (face and body positions). Lapin (QST Feb 2026 Table 1, "SAR Reference Values") tabulates the 1 g values for the 2 m band: **6 radios; low 0.05, high 0.35, mean 0.19, median 0.17 W/kg per W** (at 50 % duty). For comparison the other bands: 1.25 m one radio at 0.59; 70 cm nine radios, 0.21 to 1.50 (mean 1.02); 33 cm two radios, 0.71 to 1.35. Lapin's rule: "The most common value to use, which may be conservative but ensures that you do not exceed FCC limits, is the high SAR."

**Scaling law used.** Because the database values are at 50 % duty, the instantaneous (key-down, 100 % duty) 1 g SAR per watt is 2 x S_norm, and the window-averaged SAR is

SAR_1g(avg) = 2 x S_norm x P x duty x on-air fraction = 2 x S_norm x P_avg,

which is Lapin's formula ("multiplied by 2 to account for the 50% duty cycle used to obtain that tested SAR value"). Check: Lapin's Table 2 gives 4.6 min and 3.4 min maximum talk time per 6 min on 2 m at 15 W and 20 W; the formula gives 6 x 8 / (2 x 0.35 x 15) = 4.57 min and 3.43 min. This linear scaling in power is a property of SAR measurements (SAR is proportional to |E|^2 in tissue, hence to radiated power) and is how the FCC scales tune-up tolerances.

**Estimate for cwht (1 g, at the head or torso, radio in hand within 20 cm).** Instantaneous key-down SAR per watt: 0.10 (low) to 0.70 (high) W/kg per W, median 0.34 W/kg per W. Window-averaged values:

Table 5. Estimated 1 g SAR averaged over the window (W/kg), and fraction of the applicable limit. "Occ" = licensee or trained household member (8 W/kg, 6 min); "GP" = non-licensee holding the radio (1.6 W/kg, 30 min).

| Step (W) | Mode / on-air | P_avg (W) | SAR low (0.05) | SAR median (0.17) | SAR high (0.35) | % of 8 W/kg (high) | % of 1.6 W/kg (high) | % of 1.6 W/kg (median) |
|---|---|---|---|---|---|---|---|---|
| 0.5 | CW 50 % | 0.10 | 0.010 | 0.034 | 0.070 | 0.9 | 4.4 | 2.1 |
| 0.5 | CW 100 % | 0.20 | 0.020 | 0.068 | 0.140 | 1.7 | 8.7 | 4.2 |
| 0.5 | carrier | 0.50 | 0.050 | 0.170 | 0.350 | 4.4 | 21.9 | 10.6 |
| 1 | CW 50 % | 0.20 | 0.020 | 0.068 | 0.140 | 1.7 | 8.7 | 4.2 |
| 1 | CW 100 % | 0.40 | 0.040 | 0.136 | 0.280 | 3.5 | 17.5 | 8.5 |
| 1 | carrier | 1.00 | 0.100 | 0.340 | 0.700 | 8.8 | 43.8 | 21.2 |
| 2 | CW 50 % | 0.40 | 0.040 | 0.136 | 0.280 | 3.5 | 17.5 | 8.5 |
| 2 | CW 100 % | 0.80 | 0.080 | 0.272 | 0.560 | 7.0 | 35.0 | 17.0 |
| 2 | carrier | 2.00 | 0.200 | 0.680 | 1.400 | 17.5 | 87.5 | 42.5 |
| 5 | CW 50 % | 1.00 | 0.100 | 0.340 | 0.700 | 8.8 | 43.8 | 21.2 |
| 5 | CW 100 % | 2.00 | 0.200 | 0.680 | 1.400 | 17.5 | 87.5 | 42.5 |
| 5 | carrier | 5.00 | 0.500 | 1.700 | 3.500 | 43.8 | 218.8 | 106.3 |
| 5 | CW, SI-034 1:9 (10 %) | 0.20 | 0.020 | 0.068 | 0.140 | 1.7 | 8.7 | 4.2 |

Power at which the limit is reached (high analogy unless stated): general population at continuous CW 5.7 W (median: 11.8 W); general population at continuous carrier 2.3 W (median 4.7 W); licensee at continuous CW 28.6 W; licensee at continuous carrier 11.4 W. Maximum key-down time for a non-licensee holding the radio at the 5 W step with a continuous carrier: 13.7 min of any 30 min (high analogy); with CW at 5 W the 30 min window is unlimited (fraction 1.14) under the high analogy but the margin is only 12.5 %.

**In the hand (extremity, 10 g).** The 1 g values above are maxima across face and body positions; Tell's Figure 3 gives the 10 g values, which "are less than those that would result from the smaller averaging mass of 1 g", but the plotted numbers could not be extracted from the PDF text (Open items). Since SAR_10g is at most SAR_1g for the same exposure and the extremity limits are 2.5 times the head/torso limits (20 versus 8 W/kg; 4 versus 1.6 W/kg), the hand fraction of limit is at most 0.4 times the 1 g fraction in Table 5: at 5 W continuous CW at most 7 % (licensee) and 35 % (non-licensee holder). The hand is never the binding location; the binding case is the antenna near the face or torso.

**Confidence: Medium-Low for the absolute SAR numbers; Medium for the ordering and for the conclusion that the licensee tier has at least 5.7x margin at 5 W continuous CW.** Reasons: (a) six commercial radios of different manufacture, antennas and batteries, not cwht; (b) the FCC's "strong similarity" caveat (F5) is weaker for a homebrew aluminum enclosure with an end-mounted whip than for a manufacturer's amateur derivative of a commercial radio; (c) the 40 % CW duty factor is from a 1997 amateur bulletin and has not been evaluated by the FCC for SAR (their PTT presumption is 50 %); using 50 % instead of 40 % raises every CW figure in Table 5 by a factor of 1.25 (5 W continuous CW: 1.75 W/kg, 109 % of the general-population limit under the high analogy, as the earlier report's REG-2 stated); (d) the QST article was reviewed by FCC OET staff but is not a Commission decision. The low-to-high spread of 7:1 in the database is the honest uncertainty band.

Sources: Tell QEX 2021 pp. 13 to 15 (Figures 2 and 3, normalization statement, 22.9 W example); Lapin QST Feb 2026 pp. 56 to 57 (Tables 1 and 2, formula M = 6 x 8 / (2 S P)); 1.1310(b), (c); arithmetic in the Appendix script.

### F7. Consequences of SI-030 and SI-034 for the evaluation shape

- **SI-030 (all operators licensed).** The person holding and keying a cwht unit is normally the licensee of that transmission and is evaluated at 8 W/kg with duty-factor time averaging permitted (2.1093(d)(3)). Table 5 shows at most 17.5 % of that limit at 5 W continuous CW (high analogy) and 43.8 % for a 5 W continuous carrier for a full 6 min. The occupational tier presupposes awareness: 1.1310(e)(2) requires that the exposed person "has received written and/or verbal information fully explaining the potential for RF exposure" and "appropriate training regarding work practices relating to controlling or mitigating his or her exposure"; 97.13(c)(1) requires that "appropriate training and information has been accessed by the amateur licensee and members of his/her household". For friends operating under their own licenses this is satisfied by their licensing plus the cwht manual's exposure section; for a licensee's household members the manual must be the information source. Each operating licensee is the responsible party under 97.13(c) for their own transmissions and may adopt the cwht evaluation as their station evaluation.
- **Non-licensee holding the radio.** Excluded as an operator by SI-030, but SI-019 ("play radio" with friends) and third-party participation under 97.115 make it a foreseeable scenario. Under the high analogy 5 W continuous CW is 87.5 % of the general-population limit and a 5 W carrier exceeds it (218.8 %); the 2 W step is at 35 % (CW) and 87.5 % (carrier); the 1 W step is at 17.5 % (CW) and 43.8 % (carrier); the 0.5 W step at 8.7 % and 21.9 %. Only the 0.5 W and 1 W steps keep even the continuous-carrier case under the limit with margin. Because usage-based on-air fraction may not be credited for this tier (2.1093(d)(4), F1), the 100 % on-air columns are the ones that count.
- **Bystanders at 20 cm or more.** Table 2 (0 dBd, reflection): 0.58 m at 5 W continuous CW; 0.91 m for a 5 W carrier; 0.37 m at 2 W CW; 0.26 m at 1 W CW; 0.18 m at 0.5 W CW. A single operating rule, "keep people who are not the operator at least 0.6 m (arm's length) from the antenna while keying, and 1.0 m while tuning", covers every power step with a dipole-equivalent whip.
- **SI-034 (8 h at 1:9).** The design operating point is a 10 % on-air fraction, giving 0.2 W time-averaged at 5 W (Table 1, last column) and 8.7 % of the general-population SAR limit even under the high analogy. Worst-case windows (a long CQ) are what the evaluation must assume; the 1:9 figure belongs in the ConOps as the nominal case, not in the compliance argument.
- **Several radios operating together (SI-019).** 1.1307(b)(3)(ii)(B) sums fractional contributions of multiple sources in the same averaging period. In a CW net only one station transmits at a time, so exposures from different cwht units do not add for the same person during the same seconds, but a bystander between two operators sees both stations' on-air fractions in the same 30 min window. The rule of 0.6 m from every antenna covers this at the MPE tier.

Sources: SI-019, SI-030, SI-034; 1.1310(e)(2); 97.13(c)(1); 97.115 (not fetched this session; cited by number only); 2.1093(d)(3), (d)(4); 1.1307(b)(3)(ii)(B); Tables 1, 2 and 5.

### F8. What the SRR package can present, and what cannot be closed before first on-air

Can be presented now (Analysis, method accepted by the FCC for amateurs per FCC 19-126 fn 100):

1. Time-averaged power per step, duty factor and on-air fraction (Table 1, OET 65 B recipe).
2. MPE compliance distances and exemption distances for the mobile posture with a stated gain envelope (Tables 2, 3, 4; OET 65 Equations 3 to 7; 1.1310 Table 1; 1.1307(b)(3)(i)(C)).
3. A SAR-by-analogy estimate for the portable posture using the FCC-database values tabulated in Lapin 2026 Table 1 with the high value 0.35 W/kg per W (Table 5), with the FCC engineers' informal acceptance and "strong similarity" caveat documented (ARRL RFSC July 2023).
4. The design controls that keep the general-population scenario bounded (F9 and section 4).

Cannot be closed by this project:

1. A SAR measurement on cwht (IEEE/IEC 62209-style phantom measurement at a test lab; Lapin: "not feasible for the radio amateur"); no cost quote was sought.
2. A validated numerical SAR computation meeting 1.1310(d)(1) ("fully validated" code, FCC-accepted protocol). An open-source FDTD estimate with a homogeneous phantom could be added as supporting engineering analysis with an explicit statement that it is not an FCC-grade evaluation; the owner should decide whether it is worth the effort (DECISION).
3. The "strong similarity" argument in the form the FCC engineers described: cwht is not a derivative of a database radio.

What can be upgraded from assumption to measurement at TRR with the owner's bench: (a) the delivered power per step into the 50 ohm dummy load (tinySA Ultra with a calibrated attenuator, or a power meter); (b) the relative EIRP of the delivered whip against a reference dipole (KX4O method: transmit at a fixed low power, compare received level on the tinySA Ultra at a fixed distance in the same orientation), which converts the 0 dBd assumption into a measured gain and tightens Tables 2 to 4; (c) key-down duty of the keyer at 5 to 50 WPM (host test) to confirm the 40 % figure is conservative for the iambic keyer's actual element/space ratio at the speeds allowed by SI-033.

### F9. Low-confidence cross-check against the FCC's equipment-authorization SAR test-exclusion criterion

KDB 447498 D01 v06 section 4.3.1(a) (scope confirmed by the FCC April 2022 TCB slides: "distance <= 50 mm, 100 MHz <= frequency < 6 GHz"; numeric form from this author's recollection because the KDB PDF was not retrievable) excludes standalone 1 g SAR testing when [P_avg (mW) / d (mm)] x sqrt(f (GHz)) is 3.0 or less, with P_avg the source-based time-averaged conducted power and d the minimum test separation. At 144 MHz sqrt(f) = 0.379, so the exclusion power is 40 mW at 5 mm, 198 mW at 25 mm and 395 mW at 50 mm. cwht's 0.5 W step at 40 % CW duty (200 mW) meets the criterion only at 50 mm or more (value 1.5); the 1 W step (400 mW) is at the threshold at 50 mm (value 3.0); 2 W and 5 W fail at every distance up to 50 mm (values 6.1 and 15.2 at 50 mm). Two cautions: the criterion is a laboratory test-reduction rule for grantees, not a licensee exemption (FCC 19-126 fn 143 says SAR-based exemptions are "not valid below 300 MHz"); and the FCC's 2022 draft extension of the 1.1307 exemption thresholds below 300 MHz (TCB slides pp. 15, 24 to 26, "v07") was a draft (447498 DR05) whose adoption status was not determined here. Use: only as a plausibility argument that the 0.5 W step is in the regime the FCC itself treats as not needing SAR testing when the antenna is 5 cm or more from the body.

Sources: FCC TCB Workshop slides April 27, 2022 pp. 15 to 26; FCC 19-126 fn 143; arithmetic in the Appendix.

## 4. Implications for cwht

Tags: REQ-candidate (proposed L1 requirement with verification method per charter section 9), RISK-candidate (for `docs/risk/register.json`), DECISION-needed, ACTION. Numbers are proposals for the owner; tolerances are stated where a requirement would carry one.

### Candidate L1 requirements

- **REQ-candidate RFX-10 (selectable power steps; supersedes RF-06 numerically).** The transmitter shall provide operator-selectable output steps of 0.5, 1, 2 and 5 W nominal into 50 ohms at the antenna port, each within +/- 1 dB (0.40 to 0.63, 0.79 to 1.26, 1.6 to 2.5, 4.0 to 6.3 W) across the 2S Li-ion supply range 6.0 to 8.4 V, with the selected step shown on the LCD at all times. Rationale: 97.313(a) minimum-power duty; each step maps to a bystander distance (Table 2) and a SAR fraction (Table 5); 5 W is the owner's range requirement (SI-003). Verify: Bench (power into the dummy load through a calibrated attenuator on the tinySA Ultra, at 6.0, 7.4 and 8.4 V), HostUnit (step selection logic).
- **REQ-candidate RFX-11 (default power).** At first power-on and after any configuration reset the selected step shall be 1 W; the selected step shall persist across power cycles thereafter; selecting 5 W shall require a deliberate action distinct from tuning or volume (for example a menu confirmation). Rationale: under the high analogy 1 W keeps a non-licensee holder at 17.5 % of the general-population SAR limit for continuous CW and 43.8 % for a continuous carrier, and puts the bystander MPE distance at 0.26 m; a fresh or loaned unit therefore starts in a compliant state for every foreseeable holder. Verify: HostUnit, host demonstration (SI-026 host build).
- **REQ-candidate RFX-12 (tune carrier and stuck-key limits; duty limiting).** (a) A continuous-carrier tune function, if provided, shall transmit at the 0.5 W step unless the operator raises it, and shall end automatically after 10 s (+/- 1 s) per activation. (b) A continuous key-down longer than 60 s (TBR, +/- 5 s) from either the straight key or the paddle shall unkey the transmitter and show an alert until the key is released. Rationale: continuous carrier is the only 100 % duty case (Table 1); at 0.5 W it is 21.9 % of the general-population SAR limit and 0.29 m bystander distance; the 60 s limit protects the PA thermally and bounds a stuck straight key; no exposure-driven duty limit is needed for licensed operators (17.5 % of limit at 5 W continuous CW). Verify: HostUnit (timer boundaries), Bench (stopwatch on the dummy load).
- **REQ-candidate RFX-13 (on-screen exposure posture; refines RFX-02(b)).** The status display shall show (a) the selected power step; (b) the cumulative key-down time over sliding 6 min and 30 min windows, resolution 1 s; and (c) a one-line separation reminder derived from the selected step for persons other than the operator: 0.5 W "0.2 m", 1 W "0.3 m", 2 W "0.4 m", 5 W "0.6 m", tune mode "1.0 m" (Table 2, general population, 2.56 reflection, 0 dBd, rounded up to 0.1 m). Rationale: gives the licensee the source-based time-averaging evidence and the bystander rule in the field. Verify: HostUnit (accumulator arithmetic against synthetic keying), Inspection (display content).
- **REQ-candidate RFX-14 (labeling).** The enclosure shall carry a permanent legend (CNC-engraved or laser-marked) stating: amateur radio transmitter, 144 to 148 MHz, 5 W maximum; for use by licensed amateur operators; RF exposure information in the manual section named. Rationale: modeled on 2.1093(d)(5) visual advisories for occupational-only portables and OET 65 B p. 11 ("Warning signs and labels can also be used to establish such awareness"); it supports the occupational tier for the operator and the household. Verify: Inspection (rendered enclosure model and delivered part).
- **REQ-candidate RFX-15 (user documentation; refines RFX-02(c)).** The manual shall contain an RF exposure section with: the two tiers and who is in each (F1); Tables 1, 2 and 5 of this report as updated with measured power and antenna gain; the operating rules (persons other than the operator at 0.6 m or more from the antenna while keying and 1.0 m while tuning; non-licensees may key the radio only at the 0.5 W or 1 W step with the control operator present; no continuous carrier above 1 W within 20 cm of anyone); the antenna gain envelope covered (not more than 0 dBd; higher-gain antennas require re-evaluation); and a one-page station-evaluation form that any operating licensee can complete and keep as their record under 97.13(c) and 1.1307(b)(1)(ii). Verify: Inspection (independent reviewer against this list).
- **REQ-candidate RFX-16 (antenna gain measurement and envelope).** The delivered whip shall have a gain not exceeding 0 dBd at 144 to 148 MHz, and the project shall measure its EIRP relative to a reference half-wave dipole before first on-air (KX4O method with the tinySA Ultra), recording the result in the RF exposure evaluation. Rationale: converts the Table 2 assumption into evidence; guards the distances in RFX-13 and RFX-15. Verify: Bench.
- **REQ-candidate RFX-17 (mobile-posture provision).** The antenna connector shall be placed and the ConOps written so that the nominal operating posture (radio on a surface or in the hand at waist level, operator on headphones and paddle) keeps the antenna base at least 20 cm from the operator's head and torso, and the manual shall describe an optional external-antenna connection (short coax to a whip or mag-mount) that moves the unit into the mobile-device regime where the MPE analysis of Table 2 alone closes compliance. Rationale: DECISION-1 posture (b) of the earlier report; Lapin 2026 p. 57 recommends exactly this ("replace the handheld's antenna with a transmission line to a standalone antenna more than 20 centimeters away"). Verify: Inspection (CAD envelope), Demonstration.
- **REQ-candidate RFX-18 (evaluation deliverable; refines RFX-01).** The RF Exposure Evaluation shall be a controlled document produced at PDR from this report's method, updated at CDR with the chosen antenna and at TRR with measured power and relative gain, and it shall state explicitly which conclusions rest on the SAR analogy and its caveats. Verify: Inspection at PDR, CDR and TRR.

### Risks

- **RISK-candidate RFX-R1 (analogy validity for a homebrew form factor; sharpens REG-1).** The FCC engineers' acceptance of SAR by analogy is conditioned on "a strong similarity" to a database radio (ARRL RFSC 2023); cwht's aluminum enclosure, end-mounted whip and different antenna weaken the similarity, and the database spread is 7:1 (0.05 to 0.35 W/kg per W). Likelihood of challenge for a single licensee: low. Consequence if the true value exceeded the high analogy: the licensee tier still has 5.7x margin at 5 W continuous CW, so the residual exposure to the licensee is bounded; the general-population-holder case is not bounded. Mitigation: RFX-11, RFX-12, RFX-15; the smaller the whip, the higher the local SAR (Tell), so avoid a stubby antenna.
- **RISK-candidate RFX-R2 (continuous carrier within 20 cm of a non-licensee; sharpens REG-2).** A 5 W tune carrier at the face of a non-licensee is 219 % of the general-population limit under the high analogy and 106 % under the median. Mitigation: RFX-12(a) (0.5 W tune default, 10 s timeout) reduces this to 21.9 % and 10.6 %.
- **RISK-candidate RFX-R3 (guidance in flux).** The rewritten OET 65 Supplement B, with an analogy-method section II.D, has been "undergoing the review process" since 2023 and is unreleased; the FCC's 2022 draft extension of SAR exemption thresholds below 300 MHz has unknown status. Either could change the method or open a numeric exemption for the 0.5 W step. Mitigation: re-check both before PDR and before first on-air (ACTION).
- **RISK-candidate RFX-R4 (antenna substitution).** A user-fitted 5/8-wave (+2 dBd) grows the 5 W continuous-CW bystander distance from 0.58 m to 0.73 m and the carrier distance to 1.16 m, beyond the RFX-13 reminder. Mitigation: RFX-15 gain envelope statement; RFX-16.
- **RISK-candidate RFX-R5 (duty factor assumption).** The 40 % conversational-CW factor is a 1997 amateur figure; the FCC's PTT presumption is 50 %; a fast iambic keyer sending long dashes or a straight key held for tuning can exceed 40 % over a 6 min window. Mitigation: confirm the keyer's actual key-down ratio at 5 to 50 WPM in host tests (F8 item c); RFX-12(b) caps any continuous key-down at 60 s; state 50 % as the sensitivity case in the evaluation.

### Decisions needed

- **DECISION RFX-D1.** Adopt the power-step set 0.5 / 1 / 2 / 5 W with +/- 1 dB tolerance (RFX-10)? Recommendation: yes.
- **DECISION RFX-D2.** Default step 1 W at first boot and after reset, with a deliberate action to select 5 W (RFX-11)? Alternative: default 0.5 W (8.7 % of the general-population limit at continuous CW) or default to the last-used step with no floor. Recommendation: 1 W.
- **DECISION RFX-D3.** Tune carrier at 0.5 W by default with a 10 s timeout, and a 60 s stuck-key limit (RFX-12)? Recommendation: yes; the 60 s value is TBR pending PA thermal analysis.
- **DECISION RFX-D4 (closes DECISION-5 of the earlier report).** Classify the 6 min / 30 min key-down accumulator and posture line (RFX-13) as a convenience function, not safety-critical under SWE-134. Recommendation: convenience, because licensee compliance does not depend on it (17.5 % of limit worst case at 5 W continuous CW) and the general-population case is controlled by RFX-11 and RFX-12 instead; unit-test it as ordinary firmware.
- **DECISION RFX-D5 (closes DECISION-1 of the earlier report).** Adopt the mobile-leaning posture in the ConOps (radio on a surface or at waist level, antenna 20 cm or more from head and torso; bystanders at 0.6 m) as the primary scenario, with handheld-at-face as an off-nominal scenario evaluated by SAR analogy? Recommendation: yes.
- **DECISION RFX-D6.** Accept SAR by analogy at the high database value (0.35 W/kg per W, 1 g, 50 % duty; Lapin 2026 Table 1) as the SAR evidence for the portable posture, recording RFX-R1 as an accepted risk with the licensee-tier margin as the rationale? Recommendation: yes; no measurement path exists at project scale.
- **DECISION RFX-D7.** Commission a supporting open-source FDTD SAR estimate (homogeneous phantom, simple whip-and-box model) as engineering analysis, explicitly not an FCC-grade evaluation? Recommendation: no for SRR/PDR (cost without regulatory standing); revisit if the owner wants Analysis-grade insight for the rev B antenna choice.
- **DECISION RFX-D8.** Allow non-licensees to key the radio (third-party participation) at all? Recommendation: yes, restricted by the manual to the 0.5 W and 1 W steps with the control operator present (RFX-15).
- **DECISION RFX-D9.** Enclosure legend content and method (engraving in the PCBWay CNC job versus a printed label) per RFX-14? Recommendation: engrave; it is free with the CNC job and permanent.

### Actions

- **ACTION RFX-A1.** Write the RF Exposure Evaluation (RFX-18) as a PDR product from Tables 1 to 5, with a "basis and caveats" section quoting FCC 19-126 fn 100 and fn 143, ARRL RFSC 2023 item 1.4, and the 7:1 analogy spread.
- **ACTION RFX-A2.** Owner, in a browser: download KDB 447498 D01 (current version) and KDB 643646 D01 from `https://www.fcc.gov/kdb`, and one or two VHF PTT SAR reports from the FCC equipment authorization system (for example FCC IDs AZ489FT4948 and AZ489FT7098, Motorola VHF portables, 136 to 174 MHz) into `docs/references/md/regulatory/`, so that the analogy rests on primary SAR data (1 g and 10 g, power, duty, positions) rather than on the two ARRL articles. This tool could not fetch them.
- **ACTION RFX-A3.** Before PDR and before first on-air: check `https://www.fcc.gov/general/oet-bulletins-line` for a released revision of OET 65 Supplement B, and the eCFR version history of 1.1307, 1.1310, 2.1093 and 97.13 (one-line API query as in the earlier report's Method).
- **ACTION RFX-A4.** Add a host test that measures the keyer's key-down fraction at 5, 25 and 50 WPM for representative text and for continuous dashes, to document the actual CW duty factor against the 40 % assumption (RFX-R5).
- **ACTION RFX-A5.** At TRR: measure power per step at 6.0, 7.4 and 8.4 V and the whip's EIRP relative to a reference dipole (RFX-16); update Tables 2 to 5; place the completed one-page station evaluation in the operations handbook.
- **ACTION RFX-A6.** Copy the scratch texts fetched for this report (CFR sections, OET 65, 65 B, 65 C, FCC 19-126, TCB slides, Tell, Lapin, ARRL RFSC) into `docs/references/md/regulatory/` when the parent agent or owner grants write scope there (ACTION-1 of the earlier report remains open).

## 5. Confidence

| Item | Confidence | Basis |
|---|---|---|
| F1 regime, tiers, time-averaging rules | High | Verbatim eCFR text (issue 2026-09-23), FCC 19-126 fn 143, OET 65 B p. 11, OET 65 C pp. 16 to 17, 47 |
| F2 time-averaged power | High | OET 65 B Table 2 and recipe verbatim; arithmetic reproduced in the Appendix |
| F3 MPE and exemption distances | High for arithmetic and formulas (OET 65 Equations 3 to 7, 1.1310 Table 1, 1.1307 Table 1); Medium for physical applicability, since all distances are inside the near-field/transition region where OET 65 says the equations over-predict (conservative) |
| F4 HT whip gain range | Medium | One chamber EIRP data set calibrated against a dipole (KX4O), one relative field-strength set (G4ILO), one uncharacterized vendor claim; no peer-reviewed or NIST data retrieved |
| F5 SAR regime and FCC position | High for rule text and OET 65 C test positions; Medium for the FCC engineers' informal acceptance (reported second-hand by the ARRL RF Safety Committee) |
| F6 SAR estimate | Medium-Low for absolute numbers (six-radio analogy, 7:1 spread, FCC "strong similarity" caveat, 40 % vs 50 % duty question); Medium for the ordering of scenarios and the licensee-tier margin conclusion; the scaling formula is Lapin's and reproduces his Table 2 |
| F7 SI-030/SI-034 consequences | High for the rule reading; the third-party-participation reference (97.115) was not fetched this session |
| F8 evidence boundary | High | Direct from 1.1310(d)(1), 2.1093(d)(2), FCC 19-126 fn 100, Lapin 2026 |
| F9 KDB 447498 cross-check | Low | Scope from FCC 2022 slides; numeric formula from recollection, primary text not retrievable |

## 6. Open items

1. KDB 447498 D01 v06 and KDB 643646 D01 could not be fetched (apps.fcc.gov "Access Denied" to this tool). The exclusion formula in F9 is unverified against the primary text; ACTION RFX-A2.
2. Primary SAR reports for VHF PTT radios (fccid.io, fcc.report) were blocked by a bot check; the analogy rests on Tell 2021 and Lapin 2026 (which tabulate database values but not the FCC IDs); ACTION RFX-A2.
3. Tell's Figure 3 (10 g extremity SAR, normalized) values could not be extracted from the PDF text; the hand estimate in F6 is an upper bound by inequality, not a number.
4. Status of the rewritten OET 65 Supplement B (in government review since 2023 per ARRL) and of the FCC's 2022 draft extension of SAR exemption thresholds below 300 MHz (KDB 447498 DR05 / "v07"): not determined; ACTION RFX-A3.
5. The WebSearch budget was exhausted before searches for peer-reviewed VHF handheld SAR data, NIST body-effect antenna data, and the KDB revision status could be run.
6. 47 CFR 97.115 (third-party participation) is cited by number from general knowledge and should be pulled from the eCFR API when RFX-15 is written.
7. The actual antenna for cwht (stock-length flexible, quarter-wave whip, or half-wave) is undecided; it moves Table 2 by up to 9 dB (Table 4) and, in the opposite direction, the local SAR (Tell). The evaluation must be re-run at CDR with the choice.
8. Whether any friend will operate a unit as a non-licensee third party (SI-019 versus SI-030) needs an explicit ConOps statement; RFX-11, RFX-12 and RFX-15 are sized for that case regardless.
9. The keyer's real key-down fraction at 5 to 50 WPM (SI-033) versus the 40 % assumption; ACTION RFX-A4.

## Appendix. Calculation script (python3, run 2026-09-25)

```python
import math
DUTY_CW, DUTY_CARRIER = 0.40, 1.00      # OET 65 Supp B Table 2
S_OCC, S_GP = 1.0, 0.2                  # mW/cm2, 47 CFR 1.1310 Table 1, 30-300 MHz
G_DIPOLE, REFL, K_EXEMPT = 1.64, 2.56, 3.83   # OET 65 eq (5), eq (7); 1.1307(b)(3)(i)(C) Table 1
SAR_LOW, SAR_MED, SAR_MEAN, SAR_HIGH = 0.05, 0.17, 0.19, 0.35   # W/kg per W, 1 g, 50 % duty (Lapin QST Feb 2026 Table 1, 2 m)
LIM_OCC_1G, LIM_GP_1G = 8.0, 1.6

def lam(f_mhz): return 299.792458 / f_mhz
def r_mpe(eirp_w, s_mwcm2, refl):        # S[W/m2] = refl*EIRP/(4 pi R^2); 1 mW/cm2 = 10 W/m2
    return math.sqrt(refl * eirp_w / (4 * math.pi * s_mwcm2 * 10.0))
def r_exempt(erp_w, f_mhz):              # ERP <= 3.83 R^2, R >= lambda/2pi
    return max(math.sqrt(erp_w / K_EXEMPT), lam(f_mhz) / (2 * math.pi))

for P in (0.5, 1, 2, 5):
    for duty, name in ((DUTY_CW, "CW40"), (DUTY_CARRIER, "carrier")):
        for a in (0.5, 1.0):
            if name == "carrier" and a == 0.5: continue
            pavg = P * duty * a; eirp = G_DIPOLE * pavg
            sar = [2 * s * pavg for s in (SAR_LOW, SAR_MED, SAR_MEAN, SAR_HIGH)]
            print(P, name, a, round(pavg, 3),
                  "R_gp", round(r_mpe(eirp, S_GP, 1.0), 3), round(r_mpe(eirp, S_GP, REFL), 3),
                  "R_occ", round(r_mpe(eirp, S_OCC, 1.0), 3), round(r_mpe(eirp, S_OCC, REFL), 3),
                  "R_ex", round(r_exempt(pavg, 144), 3),
                  "SAR", [round(x, 3) for x in sar],
                  "%occ_high", round(100 * sar[3] / LIM_OCC_1G, 1), "%gp_high", round(100 * sar[3] / LIM_GP_1G, 1))
# gain sensitivity at 2.0 W average
for gdbd in (-17, -9, -6, -4, -3, 0, 2):
    g = 10 ** (gdbd / 10); erp = 2.0 * g
    print(gdbd, "dBd", round(r_mpe(G_DIPOLE * erp, S_GP, REFL), 3), round(r_exempt(erp, 144), 3))
# check against Lapin QST Feb 2026 Table 2: 15 W and 20 W on 2 m
print(round(6 * 8 / (2 * 0.35 * 15), 2), round(6 * 8 / (2 * 0.35 * 20), 2))   # 4.57, 3.43 min
```

Outputs are the values in Tables 1 to 5 and in F9 (rounded as shown).
