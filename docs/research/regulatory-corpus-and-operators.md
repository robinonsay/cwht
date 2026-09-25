# Regulatory corpus, control operator and third-party rules, A1A bandwidth, and harmonic allocations for cwht

**Assignment key:** reg-corpus
**Author:** Claude (research subagent), 2026-09-25
**Status:** research input for SRR; not a baseline. Candidate requirements are proposals for the requirements owner. Extends `part97-regulatory-basis.md` (assignment key regulatory, same day); section 3.11 reconciles the two.
**Rule text currency:** every CFR quotation is from the eCFR versioner API for issue date 2026-09-23 (latest issue available on 2026-09-25). The Federal Register API lists no Part 97 rule published in 2026 other than 91 FR 1405 (2026-01-14, effective 2026-02-13), which the eCFR text already incorporates.

## 1. Question

**(A) Corpus.** Build `docs/references/md/regulatory/` from primary sources: 47 CFR 97.3, 97.7, 97.13, 97.101, 97.103, 97.105, 97.115, 97.119, 97.203, 97.221, 97.301(a), 97.303, 97.305, 97.307, 97.313, 97.315; 1.1307(b), 1.1310; 2.202, 2.1091, 2.1093; and the 2.106 Table of Frequency Allocations rows covering 288 to 296, 432 to 444, 576 to 592, 720 to 740 and 1008 to 1036 MHz. One file per section with a header stating section, issue date and URL; a README index; the FCC 19-126, OET 65 Supplement B and DA 18-581 extracts if the part97 agent left them in scratch, else fetched.

**(B) Report.** (1) Apply the control operator and third-party rules (97.7, 97.103, 97.105, 97.115) to SI-019 (radios handed to friends): what an unlicensed friend may and may not do, and what the OPS scenario must say for a licensed versus an unlicensed friend. (2) The necessary bandwidth of A1A under 2.202 at 25 and 50 WPM, and the 26 dB bandwidth of a 5 ms raised-cosine keyed carrier at 50 WPM, to set the band-edge guard. (3) The US allocations at each 2 m harmonic. (4) Reconcile with `part97-regulatory-basis.md` and state what is superseded.

## 2. Method

**Scratch search.** `/private/tmp` was searched for the part97 agent's extracts (names containing 19-126, oet, 18-581, fcc, part97, ecfr): none exist (only `cwht-emu-scratch`, `cwht-ltspice` and session scratchpads are present), so everything was fetched afresh from the same primary URLs the prior report cites.

**eCFR (2026-09-25 16:39 UTC).** For each section: `curl -sL --compressed "https://www.ecfr.gov/api/versioner/v1/full/2026-09-23/title-47.xml?part=P&section=S"` and the version history `.../versions/title-47.json?part=P&section=S`. Fetched: the assigned sections plus, at negligible cost, the supplementary set the prior report's ACTION-1 listed (97.5, 97.109, 97.317, 2.1, 2.201, 2.815, 2.1057, 15.23). A Python script converted the XML to markdown (paragraphs, flattened tables, verbatim text) and wrote one file per section with a provenance header; see `docs/references/md/regulatory/README.md`.

**2.106 table body.** The eCFR XML of 2.106 (562 kB) contains the footnotes as text but the Table body as 68 page images (`/graphics/er14ja26.019.gif` and similar; the file names encode the Federal Register issue that last revised each page). The images returned HTTP 406 from ecfr.gov and 403 from images.federalregister.gov; no OCR tool is installed and installing one is out of scope. Fallback, all text-based: (i) the FCC's own "Online Table of Frequency Allocations, Revised on July 1, 2022" PDF from transition.fcc.gov (retrieved 16:42 UTC, `pdftotext -layout`) for the row text; (ii) the Federal Register full-text XML of every final rule amending 47 CFR part 2 since 2022-07-01 (Federal Register API, 33 rules) grepped for the five bands and their footnotes, to establish what changed after the PDF; (iii) the eCFR 2026-09-23 footnote text for every footnote the rows cite. The pending amendment the eCFR flags (91 FR 48739, 2026-07-31) was identified through the Federal Register API as the Upper C-Band rule (3.98 to 4.2 GHz, effective 2026-09-29), irrelevant here.

**FCC documents.** FCC-19-126A1.pdf (159 pp), DA-18-581A1.pdf (3 pp) from docs.fcc.gov and oet65b.pdf (65 pp) from transition.fcc.gov, converted with `pdftotext -layout`; the cited passages were extracted by line range into the corpus files. fcc.gov HTML pages return HTTP 403 to curl and WebFetch (as in the prior report). The session's WebSearch budget was already exhausted (200 of 200) before this assignment, so no search-engine confirmation was possible; nothing below depends on a search result.

**Computation.** numpy is not installed in any local python3 (homebrew 3.13.5, system 3.9.6) and installs are prohibited, so the keying-spectrum analysis uses a pure-Python radix-2 FFT (`bw.py`, `bw2.py` in the session scratchpad; 1.2 s runtime). Model: baseband envelope of "PARIS PARIS" (the 50-unit standard word) at 25 and 50 WPM, dit = 1.2/WPM s, sampled at 20 kHz, with each on/off transition replaced by a raised-cosine (Hann) edge of full 0 to 100 percent duration tr; the A1A RF spectrum is this envelope spectrum translated to the carrier, so bandwidths are 2x the one-sided baseband figure. A continuous dit stream (the highest keying rate) was run as the worst case. Bandwidth definitions computed: 2.202(a) occupied bandwidth (0.5 percent of mean power beyond each edge); the 97.3(a)(8) 26 dB bandwidth read as power containment (power outside the band at least 26 dB below power inside, i.e. 99.75 percent containment); and the offset beyond which every 10 Hz cell of the spectrum is below -40, -50 and -60 dB relative to the total mean power.

**Not done.** No GUI, no screen capture, no macOS permission requests; nothing written outside `docs/research/`, `docs/references/md/regulatory/` and the session scratchpad.

## 3. Findings

### F1. Corpus delivered: 33 files plus README in `docs/references/md/regulatory/`, 364 kB

- 21 assigned CFR sections (97.3, 97.7, 97.13, 97.101, 97.103, 97.105, 97.115, 97.119, 97.203, 97.221, 97.301 in full including (a), 97.303, 97.305, 97.307, 97.313, 97.315, 1.1307, 1.1310, 2.202, 2.1091, 2.1093), each as `47cfr-S.md` with a header table (citation, source, eCFR issue date 2026-09-23, retrieval time, API URL, reader URL, amendment dates from the versions API, scope, fidelity statement) and the verbatim text.
- 8 supplementary sections from the prior report's ACTION-1 (97.5, 97.109, 97.317, 2.1, 2.201, 2.815, 2.1057, 15.23), same format, marked "Supplementary".
- `47cfr-2.106-harmonic-bands.md`: the five harmonic rows (International Table, Federal Table, non-Federal Table, rule parts), the changes since July 2022 quoted from the Federal Register, 45 cited footnotes verbatim from eCFR 2026-09-23, and paragraphs (a) and (b) of 2.106.
- `fcc-19-126-extracts.md` (header, paragraph 32, footnote 100, paragraph 116, footnote 143), `oet65-supplement-b-extracts.md` (title, mobile/portable text, controlled-environment text, duty factor Table 2), `fcc-da-18-581.md` (full text).
- `README.md`: index with a "why it matters" column, provenance, the one-line currency re-check, the 2.106 limitation.

Version metadata worth recording: 97.7, 97.103, 97.105, 97.109, 97.115, 97.119, 97.5 show a single eCFR version (2016-12-15 baseline, no amendment since); 97.3 last amended 2017-09-15; 97.13 2020-06-01; 1.1307 2021-06-29; 1.1310 2020-06-01; 2.1091 and 2.1093 2021-05-03; 2.202 2016-12-15 baseline; 97.301, 97.303, 97.305, 97.307, 97.313 2026-02-13; 97.315 2026-02-10; 2.106 has 90 versions, latest 2026-07-31.

Sources: eCFR API URLs in each file header; https://www.ecfr.gov/api/versioner/v1/versions/title-47.json?part=97&section=97.115 (and likewise per section).

### F2. Control operator framework (97.7, 97.3, 97.5, 97.103, 97.105, 97.109, 97.119), verbatim anchors

- 97.7: "When transmitting, each amateur station must have a control operator. The control operator must be a person: (a) For whom an amateur operator/primary station license grant appears on the ULS consolidated licensee database, or (b) Who is authorized for alien reciprocal operation by § 97.107 of this part."
- 97.3(a)(13): "Control operator. An amateur operator designated by the licensee of a station to be responsible for the transmissions from that station to assure compliance with the FCC Rules." 97.3(a)(14): "Control point. The location at which the control operator function is performed." 97.3(a)(31): "Local control. The use of a control operator who directly manipulates the operating adjustments in the station to achieve compliance with the FCC Rules."
- 97.5(a): "The station apparatus must be under the physical control of a person named in an amateur station license grant on the ULS consolidated license database ... before the station may transmit on any amateur service frequency from any place that is: (1) Within 50 km of the Earth's surface and at a place where the amateur service is regulated by the FCC". 97.5(c): "The person named in the station license grant ... may use, in accordance with the applicable rules of this part, the transmitting apparatus under the physical control of the person at places where the amateur service is regulated by the FCC." Ownership of the apparatus is not a condition: a licensee operating a borrowed radio operates their own station.
- 97.103(a): "The station licensee is responsible for the proper operation of the station in accordance with the FCC Rules. When the control operator is a different amateur operator than the station licensee, both persons are equally responsible for proper operation of the station." 97.103(b): "The station licensee must designate the station control operator. The FCC will presume that the station licensee is also the control operator, unless documentation to the contrary is in the station records." 97.103(c): station and records available for FCC inspection.
- 97.105(a): "The control operator must ensure the immediate proper operation of the station, regardless of the type of control." (b): "A station may only be operated in the manner and to the extent permitted by the privileges authorized for the class of operator license held by the control operator."
- 97.109(b): "When a station is being locally controlled, the control operator must be at the control point." 97.109(d) allows automatic control only for stations "specifically designated elsewhere in this part" (97.203 beacons, 97.221 RTTY/data): a CW handheld is never under automatic control, so a control operator must be at the control point whenever it transmits.
- 97.119(a): "Each amateur station ... must transmit its assigned call sign on its transmitting channel at the end of each communication, and at least every 10 minutes during a communication ... No station may transmit unidentified communications or signals, or transmit as the station call sign, any call sign not authorized to the station." 97.119(e): "When the operator license class held by the control operator exceeds that of the station licensee, an indicator consisting of the call sign assigned to the control operator's station must be included after the call sign."

Sources: corpus files 47cfr-97.7.md, 47cfr-97.3.md, 47cfr-97.5.md, 47cfr-97.103.md, 47cfr-97.105.md, 47cfr-97.109.md, 47cfr-97.119.md (eCFR issue 2026-09-23).

### F3. Third-party framework (97.115, 97.3(a)(47)), verbatim anchors

- 97.3(a)(47): "Third party communications. A message from the control operator (first party) of an amateur station to another amateur station control operator (second party) on behalf of another person (third party)."
- 97.115(a)(1): an amateur station may transmit messages for a third party to "Any station within the jurisdiction of the United States." (Domestic third-party traffic is unrestricted; the (a)(2) international arrangements do not arise for 2 m simplex among friends.)
- 97.115(b): "The third party may participate in stating the message where: (1) The control operator is present at the control point and is continuously monitoring and supervising the third party's participation; and (2) The third party is not a prior amateur service licensee whose license was revoked or not renewed after hearing ... or surrendered for cancellation following notice of revocation, suspension or monetary forfeiture proceedings. The third party may not be the subject of a cease and desist order which relates to amateur service operation and which is still in effect."
- 97.115(c): "No station may transmit third party communications while being automatically controlled except a station transmitting a RTTY or data emission."

The rule speaks of "stating the message" and is not mode-specific; nothing in Part 97 distinguishes an unlicensed person speaking into a microphone from an unlicensed person keying Morse under the same supervision. Confidence Medium on that reading: it follows from the text, but no FCC or ARRL interpretive guidance could be fetched this session (search budget exhausted, fcc.gov 403).

Source: corpus file 47cfr-97.115.md, 47cfr-97.3.md.

### F4. SI-019 applied: what an unlicensed friend may and may not do with a cwht unit

The stakeholder log changed during this assignment: SI-030 (2026-09-25) now states "All operators (owner and friends) hold at least a Technician license". The design baseline therefore assumes licensed friends (F5), but "play radio" with several units in circulation makes an unlicensed guest a foreseeable case that the ConOps must cover as a bounded scenario rather than leave silent.

An unlicensed person MAY:

1. Receive without restriction: listen on headphones, tune the receiver across 144 to 148 MHz, hold and carry a unit that is not transmitting. Part 97 regulates transmission; 97.5(a) and 97.7 attach to the moment the station transmits.
2. Participate as a third party in stating the message (97.115(b)): key Morse on the unit while a licensed control operator is physically present at that unit (the control point) and is "continuously monitoring and supervising" (97.115(b)(1)), and the message goes to a US station (97.115(a)(1)). The unit is then the control operator's station (or the owner's station with that licensee as designated control operator, F5), and the control operator, not the guest, is responsible for identification (97.119), for power and frequency (97.105(a), 97.313(a)) and for stopping the transmission if anything is improper.
3. Be excluded only by the 97.115(b)(2) history test (revoked, suspended or surrendered license, or an active cease and desist order); a person who never held a license passes it.

An unlicensed person MAY NOT:

1. Be the control operator (97.7(a)), so may not operate the unit alone at any power, on any frequency, for any duration, including "just a quick call": there is no de minimis exception.
2. Have the transmitting apparatus under their physical control at the moment it transmits (97.5(a)); taking a unit away from the licensee and keying it is unlicensed operation attributable to the guest, and, if the unit is the owner's station, to the owner as station licensee (97.103(a)).
3. Transmit when the supervising licensee steps away from that unit (97.109(b), 97.115(b)(1)). Two units in two rooms need two licensees.
4. Identify with a call sign not authorized to the station (97.119(a)); the identification is the station's, made or supervised by the control operator.
5. Be assessed at the occupational RF exposure limits. 97.13(c)(1) reserves the occupational/controlled evaluation to the licensee's immediate household; OET 65 B (PDF text lines 385 to 392) explains that "the amateur station licensee and members of his or her immediate household are considered to be in a 'controlled environment'" and "All persons ... who are not members of an amateur station licensee's household are considered to be members of the general public". A guest holding a transmitting handheld is general population (1.1310(c): 1.6 W/kg per 1 g, 4 W/kg in the hand). The prior report's SAR-by-analogy estimate (F8 there, 0.35 W/kg per W at 50 percent duty) puts 5 W at about 109 percent of that limit and 2 W at 44 percent (Medium-Low confidence, one 2021 QEX source). This is a second, independent reason why a guest should not be the one holding a transmitting unit at 5 W.

Not analyzed (not fetched): 97.113 prohibited transmissions (music, broadcasting, business, obscenity) apply to whatever the guest keys; the control operator's supervision duty covers content as well.

Sources: corpus files 47cfr-97.5.md, 47cfr-97.7.md, 47cfr-97.13.md, 47cfr-97.103.md, 47cfr-97.105.md, 47cfr-97.109.md, 47cfr-97.115.md, 47cfr-97.119.md, 47cfr-1.1310.md, oet65-supplement-b-extracts.md; part97-regulatory-basis.md F8.

### F5. What the OPS scenarios must say: licensed friend versus unlicensed friend

Three lawful configurations exist for a unit in a friend's hands. The ConOps should name them and pick a default.

**OPS-A. Licensed friend operates the loaned unit as their own station (recommended default).** Basis: 97.5(c) (a licensee may use any transmitting apparatus under their physical control), 97.103(b) presumption (the licensee of that station is its control operator). Consequences: the friend identifies with their own call sign (97.119(a)); the friend alone is responsible for that unit's operation (97.103(a)), including 97.13(c) RF exposure, for which they qualify for the controlled-environment treatment as the licensee; no station records or designation are needed; privileges are the friend's class, which on 2 m is the full 144 to 148 MHz for Technician and above (97.301(a)); the owner is not a party to that station's transmissions. Two cwht units talking are then two independent stations, and an unlicensed guest at either end is a third party under that end's control operator (OPS-C). The scenario text must say: "Each unit is the amateur station of the licensee holding it; that licensee is its station licensee and control operator, identifies with their own call sign, and is responsible for its compliance."

**OPS-B. Licensed friend operates as designated control operator of the owner's station.** Basis: 97.103(b) designation ("documentation to the contrary ... in the station records": a dated note suffices), 97.105(b) (privileges are the control operator's class; on 2 m identical for Technician and above), 97.103(a) (owner and friend "equally responsible"). Identification is the owner's call sign (97.119(a)); if the friend's class exceeds General, 97.119(e) requires the friend's call sign appended as an indicator. The owner keeps 97.103(c) inspection duties. This configuration is what applies by default if a friend transmits with the owner present and nobody has thought about it, so the ConOps must say which of A or B is intended, and OPS-B must carry the records duty.

**OPS-C. Unlicensed guest as third party.** Basis F4: guest keys only under a licensee present at that unit and continuously supervising; the licensee identifies (or supervises the identification); guest is general population for RF exposure, so the licensee selects a reduced power step (RF-06 of the prior report) or keeps the antenna away from the guest; the guest never operates alone. Receive-only use by anyone is unrestricted.

For SI-030 (occupational limits for all operators): true under OPS-A and OPS-B because every operator is then a licensee operating their own or a designated station; not true for OPS-C, where the guest is general population. Bystanders (SI-030's own wording) are general population in all three.

Sources: as F2 to F4; stakeholder-inputs.md SI-019, SI-030.

### F6. Necessary bandwidth of A1A under 47 CFR 2.202

2.202(b): "Necessary bandwidth. For a given class of emission, the minimum value of the occupied bandwidth sufficient to ensure the transmission of information at the rate and with the quality required for the system employed, under specified conditions." 2.202(g), row "Continuous wave telegraphy": "Bn = BK, K = 5 for fading circuits, K = 3 for non-fading circuits"; example: "25 words per minute; B = 20, K = 5, Bandwidth: 100 Hz"; designator "100HA1A". 2.202(e): B is the modulation rate in bauds. (These are the ITU-R SM.1138 formulas as incorporated in the CFR, which closes the prior report's open item on SM.1138 without fetching the ITU text.)

Modulation rate for Morse (PARIS standard, 50 units per word): dit duration = 1.2/WPM s, so B = WPM/1.2 baud. The rule's example rounds 20.8 to 20.

| Speed | Dit | B (baud) | Bn, K = 3 (non-fading; VHF line-of-sight simplex) | Bn, K = 5 (fading; conservative) | Designator |
|---|---|---|---|---|---|
| 25 WPM | 48.0 ms | 20.8 | 62 Hz | 104 Hz (rule example 100 Hz) | 62H5A1A / 104HA1A (rule: 100HA1A) |
| 50 WPM (SI-033 maximum) | 24.0 ms | 41.7 | 125 Hz | 208 Hz | 125HA1A / 208HA1A |

The FCC's own recent use of an A1A designator for amateurs is footnote US23 to 2.106 (60 m): "CW (150HA1A)", i.e. 150 Hz. For documentation the conservative K = 5 figure 208HA1A at 50 WPM is defensible; the design must in any case keep the measured 26 dB bandwidth below the 500 Hz budget of the prior report's RF-02 (F7 shows about 230 to 300 Hz is achievable).

Sources: corpus file 47cfr-2.202.md (paragraphs (b), (e), (g)); 47cfr-2.106-harmonic-bands.md does not carry US23; US23 text is in the eCFR 2.106 text line "(23) US23 ..." (scratch copy), quoted here from that fetch.

### F7. The 26 dB bandwidth of a raised-cosine keyed carrier (computed)

97.3(a)(8): "Bandwidth. The width of a frequency band outside of which the mean power of the transmitted signal is attenuated at least 26 dB below the mean power of the transmitted signal within the band." Read literally this is power containment: P_outside/P_inside = 10^-2.6 = 0.0025, i.e. 99.75 percent of the mean power inside. Results (pure-Python FFT, method in section 2; "tr" is the full 0 to 100 percent Hann transition; its 10 to 90 percent rise time is 0.59 tr, so tr = 5 ms is 2.95 ms 10-90):

| Case | 2.202(a) occupied (99 percent) | 97.3(a)(8) 26 dB (99.75 percent) | 99.9 percent | All 10 Hz cells below -40 / -50 / -60 dB (rel. total mean power) beyond offset |
|---|---|---|---|---|
| PARIS 25 WPM, hard keying | 195 Hz | 812 Hz | 2021 Hz | not computed |
| PARIS 25 WPM, tr = 3 ms | 119 Hz | 271 Hz | 359 Hz | not computed |
| PARIS 25 WPM, tr = 5 ms | 104 Hz | 188 Hz | 266 Hz | 181 / 242 / 443 Hz |
| PARIS 25 WPM, tr = 8 ms | 72 Hz | 146 Hz | 187 Hz | not computed |
| PARIS 50 WPM, hard keying | 390 Hz | 1625 Hz | 3952 Hz | not computed |
| PARIS 50 WPM, tr = 3 ms | 208 Hz | 357 Hz | 458 Hz | 272 / 403 / 695 Hz |
| **PARIS 50 WPM, tr = 5 ms** | **128 Hz** | **226 Hz** | **292 Hz** | **191 / 272 / 614 Hz** |
| PARIS 50 WPM, tr = 8 ms | 125 Hz | 177 Hz | 209 Hz | not computed |
| Continuous dits 50 WPM, tr = 3 ms | 209 Hz | 375 Hz | not computed | 322 / 403 / 735 Hz |
| **Continuous dits 50 WPM, tr = 5 ms (worst case)** | **208 Hz** | **292 Hz** | not computed | **232 / 272 / 614 Hz** |
| Continuous dits 50 WPM, hard keying | 625 Hz | 2458 Hz | not computed | 1108 / 3777 / 9980 Hz |

Readings:

1. At 50 WPM with 5 ms raised-cosine edges the 26 dB bandwidth is 226 Hz for text and 292 Hz for the worst-case dit stream; the 99 percent occupied bandwidth (128 Hz) matches the K = 3 necessary bandwidth (125 Hz), so 97.307(a) ("no more bandwidth than necessary") is met by construction.
2. Hard keying is 7 to 8 times wider at 26 dB and puts energy above -40 dB out to 1.1 kHz: this is the 97.307(b) "keyclick" case, and it shows that envelope shaping is a compliance function, not a nicety.
3. Going from 5 ms to 3 ms costs 130 to 160 Hz of 26 dB bandwidth and moves the -60 dB point from 614 to 695 to 735 Hz; 8 ms buys little and softens the keying at 50 WPM (a 24 ms dit with 8 ms edges is 33 percent edge). 5 ms full transition (about 3 ms 10-90) is the right nominal; 4 to 6 ms the tolerance.
4. Convention warning: if the design documents "5 ms" as a 10-90 percent rise time, the full Hann transition is 8.5 ms and the 8 ms row applies (narrower). State the convention in RF-07.
5. Model limits: envelope only; PA envelope distortion (a Class-C or E stage with a shaped supply or drive does not reproduce the Hann shape exactly), AM-to-PM conversion and synthesizer phase noise all add sidebands. The numbers are design targets to be confirmed by measurement (owner's tinySA Ultra, SI-034) at TRR.

Sources: bw.py and bw2.py output (scratchpad, 2026-09-25); 47cfr-97.3.md, 47cfr-97.307.md, 47cfr-2.202.md.

### F8. Band-edge guard: keying bandwidth plus frequency error

97.307(b): "Emissions resulting from modulation must be confined to the band or segment available to the control operator." The guard between the carrier and 144.000 or 148.000 MHz must cover (i) half the worst-case 26 dB bandwidth, 146 Hz at 50 WPM/5 ms (188 Hz at 3 ms), (ii) the carrier frequency error, and (iii) the offset beyond which sideband energy is negligible if the project wants a stronger claim than the 26 dB definition. Frequency error at 148 MHz versus reference tolerance:

| Reference tolerance (all causes: initial, temperature, aging) | Error at 148 MHz |
|---|---|
| ±0.5 ppm | ±74 Hz |
| ±1 ppm | ±148 Hz |
| ±2 ppm | ±296 Hz |
| ±2.5 ppm | ±370 Hz |
| ±5 ppm | ±740 Hz |
| ±10 ppm | ±1480 Hz |
| ±20 ppm | ±2960 Hz |
| ±30 ppm | ±4440 Hz |

With the prior report's 1 kHz guard (carrier limited to 144.001 to 147.999 MHz): the 26 dB criterion holds for reference tolerance up to about ±5.7 ppm (1000 minus 146 = 854 Hz); the stronger "everything beyond the edge below -60 dB relative to mean power" criterion (614 Hz at 5 ms) holds up to about ±2.6 ppm (386 Hz). A crystal-only reference of ±20 to ±30 ppm class would need a 3.2 to 4.7 kHz guard and would also miss a 144.050 MHz CW contact by several dits' worth of pitch; the RF synthesizer therefore needs its own TCXO of ±2.5 ppm or better over the operating temperature range, or the guard grows. The Raspberry Pi Pico 2 module's 12 MHz crystal is not specified for RF synthesis use in the sources fetched here (Low confidence on its tolerance; the RP2350 datasheet was not consulted in this assignment). Recommendation: keep RF-02 at 1 kHz (144.001 to 147.999 MHz) and add a reference-accuracy requirement of ±2.5 ppm; 2 kHz is an acceptable alternative if the owner prefers margin over the last kilohertz of the band, which the ARRL plan reserves for EME anyway (prior report F5).

Sources: F7 results; 47cfr-97.307.md; part97-regulatory-basis.md REQ-candidate RF-02.

### F9. US allocations at each 2 m harmonic (from the 2.106 corpus file)

Row content is from the FCC Online Table (July 1, 2022) text, corrected by the Federal Register amendatory text of 88 FR 67514 (WRC-19, effective 2023-10-30) and 91 FR 1405 (WRC-15, effective 2026-02-13); footnotes verbatim from eCFR 2026-09-23. Capitals are primary services; initial capitals secondary.

| Harmonic of 144 to 148 MHz | Band | US Federal Table | US non-Federal Table | Rule parts | Who is on the receiving end |
|---|---|---|---|---|---|
| 2f | 288 to 296 MHz (row 267-322) | FIXED, MOBILE, G27 G100 (military only; G100 adds primary military mobile-satellite in 235-322 MHz) | none (empty cell) | none | Military UHF tactical and satellite communications; no civil users |
| 3f | 432 to 444 MHz (row 420-450) | RADIOLOCATION G2 G129 (military radars; wind profilers 448-450), footnotes 5.286 US64 US87 US230 US269 US270 US397 G8 | Amateur US270 (secondary), footnotes 5.282 5.286 US64 US87 US230 US269 US397 | Private Land Mobile (90), MedRadio (95I), Amateur Radio (97) | Military radar (primary), 70 cm amateurs including the 432.300-432.400 MHz beacon segment (97.203(d)), amateur-satellite 435-438 MHz (5.282), EESS active 432-438 MHz (US397) |
| 4f | 576 to 592 MHz (row 470-608 Federal, 512-608 non-Federal) | none (empty cell) | BROADCASTING NG5 NG14 NG115 NG149 | Broadcast Radio (TV)(73), LPTV/Translator (74G), Low Power Auxiliary (74H) | UHF TV channels 31 to 33 (576-582, 582-588, 588-594 MHz), wireless microphones (NG115), white space devices |
| 5f | 720 to 740 MHz (row 698-758 non-Federal, 614-890 Federal) | none (empty cell) | FIXED, MOBILE, NG159 (BROADCASTING deleted effective 2026-02-13 by 91 FR 1405) | Wireless Communications (27); 74G reference removed 2026 | Commercial 700 MHz LTE/5G (Lower 700 MHz blocks and the 728-746 MHz downlink region; block edges Low confidence, not fetched) |
| 7f | 1008 to 1036 MHz (row 960-1164) | AERONAUTICAL MOBILE (R) 5.327A, AERONAUTICAL RADIONAVIGATION 5.328; 5.328AA US78 US224 added/revised effective 2026-02-13 | identical to Federal | Aviation (87) | DME/TACAN interrogation channels and the 1030 MHz SSR/IFF interrogation frequency (US78); safety-of-life radionavigation, for which 97.3(a)(23) treats interference as harmful per se |

Consequences beyond the numeric 97.307(e) limit (25 uW and 40 dB down, i.e. 53 dB at 5 W, prior report F2): 97.307(c) obliges elimination of any spurious emission that causes harmful interference "in accordance with good engineering practice". The 7th harmonic lands in a safety-of-life band and the 2nd in a military-only band; the 3rd lands on the project's own community, and specifically 144.100 to 144.133 MHz (the top of the 2 m CW segment) maps onto the 432.300 to 432.400 MHz beacon segment. This supports the prior report's 60 dB design target (DECISION-4 there) and argues for measuring 2f, 3f and 7f explicitly in the TRR procedure.

Not covered: 6f (864 to 888 MHz, cellular downlink region) was not in the assignment and was not extracted.

Sources: corpus file 47cfr-2.106-harmonic-bands.md and its header (FCC PDF https://transition.fcc.gov/oet/spectrum/table/fcctable.pdf retrieved 2026-09-25 16:42 UTC; Federal Register full-text XML https://www.federalregister.gov/documents/full_text/xml/2026/01/14/2026-00587.xml and https://www.federalregister.gov/documents/full_text/xml/2023/09/29/2023-14656.xml); 47cfr-97.203.md; 47cfr-97.303.md.

### F10. Rule currency and the pending 2.106 amendment

- Federal Register API, documents affecting 47 CFR 97 published on or after 2026-01-01: exactly one, 2026-00587 (91 FR 1405, published 2026-01-14, effective 2026-02-13). No newer Part 97 rule or proposed rule. Combined with the prior report's 2025 check, nothing has changed for 2 m CW since the eCFR issue used here.
- 2.106: the eCFR text's "Link to an amendment published at 91 FR 48739, July 31, 2026" resolves (Federal Register API, FCC documents of 2026-07-31) to 2026-15598 "Upper C-Band (3.98-4.2 GHz); Expanding Flexible Use of the 3.7 to 4.2 GHz Band", 91 FR 48700 to 48750, effective 2026-09-29: no effect on any band below 3.7 GHz.
- 33 final rules amended 47 CFR part 2 between 2022-07-01 and 2026-09-25; the ones that touched the harmonic-band pages or footnotes are the June 2023 footnote recodification (88 FR 37318), WRC-19 (88 FR 67514: pages 19 to 28, 30, 33, 34; footnotes 5.279A, 5.295, 5.297 as quoted in the corpus), and WRC-15 (91 FR 1405: pages 22, 24, 26 to 28, 30, 32; US270 rewritten into table form; broadcasting deleted from 698-758 MHz; US78 and 5.328AA added at 960-1164 MHz; US224 revised). The Supplemental Coverage from Space rule (89 FR 34148, 2024) was checked and does not mention any of the five bands in its amendatory text.

Sources: https://www.federalregister.gov/api/v1/documents.json?conditions[cfr][title]=47&conditions[cfr][part]=97&conditions[publication_date][gte]=2026-01-01 (brackets percent-encoded in the actual call); the part 2 query with conditions[cfr][part]=2 and publication_date gte 2022-07-01; https://www.federalregister.gov/documents/2026/07/31/2026-15598 (via API fields).

### F11. Reconciliation with part97-regulatory-basis.md: confirmed, refined, superseded

| Item in the prior report | Status after this report |
|---|---|
| F2 harmonic landing spots "from general knowledge; allocation table not fetched"; Open item 6 | **Superseded** by F9 here with sourced rows. Corrections: 2f is US Federal FIXED/MOBILE limited to the military (G27), not "aeronautical mobile" (that is the Region 2 international entry for 225-235 only); 5f is the commercial 700 MHz band (part 27), with the public safety block 758-775 MHz outside 720-740 and the broadcasting allocation deleted in 2026; 3f "shared with federal radiolocation" made precise: Federal radiolocation primary, amateur secondary (5.270, US270), plus the 432.300-432.400 MHz beacon segment coincidence. Open item 6 closed at Medium confidence (row images unread). |
| F11 keying bandwidth "Medium confidence; ITU-R SM.1138 and Handbook not fetched"; Open item 5 | **Superseded** by F6 and F7: the SM.1138 formulas are in 47 CFR 2.202(g) verbatim (Bn = BK, K = 3 or 5); computed 26 dB bandwidths replace the "about 100-150 Hz at 25 WPM" estimate (188 Hz at 25 WPM, 226 to 292 Hz at 50 WPM with 5 ms edges). The Handbook rise-time recommendation remains unfetched but is no longer needed as evidence. |
| REQ-candidate RF-02 (500 Hz 26 dB budget; carrier 144.001 to 147.999) | **Confirmed and refined** (F8): budget is adequate (worst case 292 Hz at 5 ms, 375 Hz at 3 ms); add the reference tolerance term (±2.5 ppm) or widen the guard. |
| REQ-candidate RF-07 (rise/fall 3 to 6 ms, target 5 ms) | **Refined**: 5 ms full Hann transition nominal, 4 to 6 ms tolerance, convention stated; 3 ms is the floor that still meets the 500 Hz budget. |
| REQ-candidate FW-01 (auto-ID at most 20 WPM) | **Confirmed** (97.119(b)(1)) and extended: per-unit stored call sign must be the operator's own under OPS-A (F5). |
| RISK-candidate REG-2 (general population SAR at 5 W) | **Reinforced**: the guest case (OPS-C) is exactly the general-population exposure; ties to the control operator rules. |
| RISK-candidate RF-2 (3rd harmonic in 70 cm) | **Refined** with the beacon segment mapping and the primary/secondary status. |
| ACTION-1 (add rule texts to docs/references/md/regulatory) and Open item 8 (scratch copies) | **Done** (F1). The part97 scratch copies were not found; texts were re-fetched from the same API and issue date, so content is identical by construction. |
| F6 to F8 RF exposure regime and numbers; DECISION-1 posture | **Unchanged**; SI-030 (new) is consistent with 97.13(c)(1) and OET 65 B only for licensees operating their own or designated stations (OPS-A/B), see F5. |
| Control operator and third-party rules | **New** in this report (F2 to F5); the prior report did not treat them. |
| Rule currency (F12 there) | **Confirmed** through 2026-09-25 (F10). |

Nothing in the prior report is contradicted on rule text; the changes are sourcing upgrades and refinements.

## 4. Implications for cwht

Tags: REQ-candidate, RISK-candidate, DECISION-needed, ACTION. Numbering continues the prior report's series.

### Candidate requirements

- **REQ-candidate OPS-02 (operator model).** The ConOps shall state that each cwht unit is the amateur station of the licensee holding it (OPS-A): that licensee is station licensee and control operator, identifies with their own call sign, and is responsible for the unit's compliance (97.5(c), 97.103, 97.105, 97.119). Where a unit is instead operated as the owner's station with a designated control operator (OPS-B), a dated designation note shall be kept in the owner's station records (97.103(b)) and identification shall follow 97.119(a) and (e). Verify: Inspection (ConOps text, records template).
- **REQ-candidate OPS-03 (unlicensed guests).** The ConOps and user documentation shall state that an unlicensed person may listen and tune without restriction, may key the unit only as a third party with a licensee present at that unit and continuously supervising (97.115(b)(1)), may never operate a unit alone (97.7, 97.5(a), 97.109(b)), and is a general-population person for RF exposure (97.13(c)(1)); the supervising licensee shall select a reduced power step for guest keying per the RF exposure evaluation. Verify: Inspection.
- **REQ-candidate FW-03 (receive-only guest lock).** The firmware shall provide a licensee-settable receive-only mode that inhibits the transmitter (key, keyer and any memory) until released by a deliberate action, so that a unit can be handed to a guest without risk of unlicensed transmission. Safety-relevant in the regulatory sense; candidate for SWE-134 scoping with the transmit inhibit of RF-01. Verify: HostUnit, Emulation (key events in guest mode produce no PTT/PA enable), Bench.
- **REQ-candidate FW-04 (per-unit call sign).** Each unit shall store its operator's call sign, show it on the LCD (so the operator and any inspector can see whose station it is), and use it for the automatic identification memory at not more than 20 WPM (97.119(b)(1)); an empty call sign shall disable the auto-ID memory, not send a default. Verify: HostUnit, Emulation, Inspection.
- **REQ-candidate RF-02 (revised band-edge guard).** Transmit carrier limited to 144.001 to 147.999 MHz (unchanged), AND the carrier frequency error from all causes shall not exceed ±370 Hz (±2.5 ppm at 148 MHz) over the operating temperature range and design life, so that all keying sidebands above -60 dB relative to the mean power stay inside the band (F7, F8). Alternative if a looser reference is chosen: guard = 150 Hz + frequency error + 470 Hz, rounded up to the tuning step. Verify: Analysis (F7 spectrum plus reference budget), Bench (tinySA Ultra at the band edge; frequency counter or off-air reference).
- **REQ-candidate RF-07 (revised keying envelope).** Carrier on/off transitions shall follow a raised-cosine (Hann) profile with a full 0 to 100 percent transition time of 5 ms nominal, 4 to 6 ms tolerance (2.4 to 3.5 ms 10-90 percent), at all keyer speeds up to 50 WPM, with no overshoot; the measured 26 dB bandwidth (97.3(a)(8), power containment) shall not exceed 350 Hz at 50 WPM with continuous dits. Verify: Analysis (SPICE envelope of the actual PA into 50 ohms, fed to the FFT script), Bench (tinySA Ultra, narrowest RBW, max-hold over continuous dits).
- **REQ-candidate RF-09 (frequency reference).** The RF synthesizer reference shall be a TCXO of ±2.5 ppm or better total tolerance (initial, -10 to +50 C, one year aging), independent of the Pico 2 module's crystal. Verify: Inspection (datasheet), Bench (frequency at temperature extremes if a chamber or freezer/heat test is available; otherwise Analysis).
- **REQ-candidate RF-10 (harmonics of concern).** The spurious-emission bench procedure (prior ACTION-3) shall report 2f, 3f and 7f individually with the victim service named (military fixed/mobile; Federal radiolocation and 70 cm amateur incl. 432.3-432.4 MHz beacons; aeronautical radionavigation incl. 1030 MHz SSR/IFF), against the 60 dB design target. Verify: Bench.
- **REQ-candidate DOC-02 (operator rules card).** The user documentation shall include a one-page operator rules card: licensed operators only; own call sign; ID every 10 minutes and at the end; guests as third parties under supervision; guest lock; exposure distances and power steps; the 144.000-144.100 CW-only segment. Verify: Inspection.

### Risks

- **RISK-candidate REG-4 (unlicensed operation by a guest).** A unit handed around at a gathering can be keyed by an unlicensed person without a licensee at that unit; if the unit is the owner's station the owner is responsible (97.103(a)), and in any case the transmission is unlawful. Likelihood moderate in the "play radio" use case; consequence an FCC enforcement exposure and community harm. Mitigations: SI-030 (licensed friends only), OPS-A (each licensee owns their unit's compliance), FW-03 guest lock, DOC-02.
- **RISK-candidate REG-5 (2.106 row currency).** The five allocation rows are Medium confidence because the current page images could not be read; a change to a row between July 2022 and September 2026 that the Federal Register text search did not surface would go unnoticed. Consequence limited (rows inform the harmonic-interference argument, not a numeric limit). Mitigation: DECISION-10 owner browser check.
- **RISK-candidate RF-4 (3rd harmonic on the 70 cm weak-signal and beacon segments).** Operating 144.000 to 144.133 MHz puts 3f at 432.0 to 432.4 MHz; at the 97.307(e) limit (-16 dBm) this is a strong local signal for a 70 cm weak-signal or beacon receiver. Mitigation: 60 dB target, RF-10 reporting, operator awareness in DOC-02.
- **RISK-candidate RF-5 (7th harmonic in the 1030 MHz SSR/IFF and DME band).** Safety-of-life radionavigation; 97.3(a)(23) treats interference there as harmful per se. Radiated level from a handheld harmonic at -16 dBm or below is far below aeronautical receiver thresholds at any realistic separation (Analysis not done here; Low confidence on margin), but the design should not rely on the argument: meet the 60 dB target and report 7f. Mitigation: RF-04 target, RF-10.
- **RISK-candidate REG-6 (band-edge violation by reference drift).** A ±20 ppm crystal reference would place the 148.000 MHz edge tune 3 kHz uncertain; with a 1 kHz guard the 26 dB bandwidth crosses the edge. Mitigation: RF-09 TCXO or wider guard.
- **RISK-candidate REG-7 (interpretation of third-party keying).** F3's reading that an unlicensed person may key Morse as a third party under supervision is Medium confidence; if an FCC or ARRL interpretation limits third-party participation differently, OPS-C tightens to "guests listen only". Mitigation: ACTION-7; the design (FW-03) supports either outcome.

### Decisions needed (owner)

- **DECISION-6 (operator model default).** Pick OPS-A (each licensed friend operates the unit as their own station, own call sign) or OPS-B (friends as designated control operators of the owner's station, owner's call sign, records kept). Recommendation: OPS-A.
- **DECISION-7 (guest lock).** Include the licensee-settable receive-only mode FW-03? Recommendation: yes; it is a few lines of firmware and removes the main REG-4 pathway.
- **DECISION-8 (declared necessary bandwidth).** Document A1A at 50 WPM as 208HA1A (K = 5) or 125HA1A (K = 3)? Recommendation: 208HA1A for documentation, with the measured 26 dB bandwidth target of 350 Hz maximum and about 230 to 290 Hz expected.
- **DECISION-9 (reference and guard).** (a) TCXO ±2.5 ppm with the 1 kHz guard (carrier 144.001 to 147.999 MHz), or (b) looser reference with a 2 kHz or wider guard. Recommendation: (a); it also gives the operator a frequency display good to a few hundred hertz, which matters for finding a 100 Hz wide CW signal.
- **DECISION-10 (close the 2.106 image gap).** Owner opens https://www.ecfr.gov/current/title-47/section-2.106 in a browser and compares the 267-322, 420-450, 470-608/512-608, 698-758 and 960-1164 MHz rows with `47cfr-2.106-harmonic-bands.md` (about five minutes), or accepts Medium confidence. Recommendation: do the check before the harmonic-interference argument is used at PDR.
- **DECISION-11 (keying envelope convention).** Fix the RF-07 convention as "5 ms full 0 to 100 percent Hann transition (about 3 ms 10-90)" rather than "5 ms 10-90" (which is 8.5 ms full and slower at 50 WPM). Recommendation: 5 ms full transition.

### Actions

- **ACTION-6.** Fold OPS-02, OPS-03 and DOC-02 text into the ConOps and user documentation; record DECISION-6 as an ADR the same day (charter section 11 rule 6).
- **ACTION-7.** When search budget is available, fetch FCC or ARRL guidance on third-party participation (the ARRL "third party" and "control operator" FAQ pages, and any FCC letter on unlicensed persons operating under supervision) and either confirm F3 or tighten OPS-C.
- **ACTION-8.** Re-run `bw.py` with the simulated PA output envelope (LTspice, prior ltspice-batch-macos.md pipeline) once the PA and keying shaper are designed; record the 26 dB bandwidth and the -60 dB offset in the PDR analysis package. The script is 80 lines of pure Python and can live in `tools/`.
- **ACTION-9.** Confirm the tinySA Ultra minimum RBW and sweep settings for the band-edge and keying-spectrum measurements (not verified here; Low confidence that a 100 Hz class RBW is available) and write the TRR procedure accordingly; if RBW is too coarse, the keying bandwidth evidence stays at Analysis with the bench limited to the band-edge power check.
- **ACTION-10.** Add 47 CFR 97.113 (prohibited transmissions) to the corpus if the ConOps wants to cite the content rules for supervised guests.
- **ACTION-11.** Verify the Pico 2 module crystal tolerance from the RP2350/Pico 2 datasheet and record why it is not used as the RF reference (RF-09).
- **ACTION-12.** Keep ACTION-5 of the prior report: re-run the eCFR versions query for every corpus file before CDR and before first on-air; the README shows the one-line check.

## 5. Confidence

| Finding | Confidence | Basis |
|---|---|---|
| F1 corpus content and provenance | High | Verbatim API text, issue 2026-09-23, headers carry URLs and version metadata; spot-checked 97.301 table, 97.115 text, footnote extraction |
| F2, F3 rule text | High | Verbatim eCFR |
| F3 reading that "stating the message" covers keying Morse | Medium | Text is mode-neutral; no interpretive source fetched (search budget exhausted, fcc.gov 403) |
| F4, F5 application to SI-019 / SI-030 | High for what the rules require; Medium for the OPS-A framing as "recommended default" (a policy choice) | 97.5(c), 97.103, 97.105, 97.115, 97.119 verbatim; OET 65 B controlled-environment text verbatim |
| F4 item 5 exposure numbers | Medium-Low | Inherited from prior report F8 (single 2021 QEX source) |
| F6 necessary bandwidth | High | 2.202(g) verbatim; arithmetic shown |
| F7 26 dB bandwidths | Medium-High | Deterministic pure-Python FFT of an idealized envelope; definition read as power containment; not yet compared with a measured envelope |
| F8 guard budget | High for arithmetic; Low for the Pico 2 crystal remark | ppm arithmetic; datasheet not consulted |
| F9 harmonic allocations: footnotes | High | Verbatim eCFR 2026-09-23 |
| F9 harmonic allocations: row entries | Medium | July 2022 FCC PDF text plus Federal Register amendatory text; current page images unread; part 27 block edges Low |
| F10 rule currency | High | Federal Register API and eCFR versions API, 2026-09-25 |
| F11 reconciliation | High | Direct comparison of the two reports |

## 6. Open items

1. The current 2.106 page images (eCFR graphics) could not be fetched or OCR'd headlessly; the five rows rest on the July 2022 FCC PDF plus Federal Register text. Owner browser check (DECISION-10) closes it.
2. The FCC Online Table of Frequency Allocations may have a revision newer than July 1, 2022 on fcc.gov (HTTP 403 to tools); if so, it would be a better text source than the 2022 file at transition.fcc.gov.
3. No FCC or ARRL interpretive guidance on third-party participation in CW was fetched (WebSearch budget exhausted at 200 of 200 before this assignment started); F3/OPS-C are Medium confidence.
4. The 6th harmonic (864 to 888 MHz) was not in the assignment and was not extracted; add if the harmonic argument is extended.
5. 47 CFR 97.113, 97.107 and 97.215 are not in the corpus.
6. The keying analysis uses an idealized Hann envelope; PA envelope fidelity, AM-to-PM and phase noise are not modeled (ACTION-8).
7. tinySA Ultra RBW capability for a 100 Hz class keying-spectrum measurement not verified (ACTION-9).
8. Pico 2 module crystal tolerance not verified (ACTION-11).
9. The ARRL Handbook keying rise-time recommendation (prior Open item 5) remains unfetched; the CFR 2.202(g) formulas made it unnecessary as evidence, but it would be a useful cross-check for the 5 ms convention.
10. SI-030 arrived mid-assignment and supersedes the "license status unknown" premise; the ConOps should record that OPS-C is retained as a covered misuse case, not as a planned use.

## Sources

- eCFR versioner API, issue 2026-09-23, retrieved 2026-09-25 16:39 UTC: https://www.ecfr.gov/api/versioner/v1/full/2026-09-23/title-47.xml?part=97&section=97.115 and the same pattern for 97.3, 97.5, 97.7, 97.13, 97.101, 97.103, 97.105, 97.109, 97.119, 97.203, 97.221, 97.301, 97.303, 97.305, 97.307, 97.313, 97.315, 97.317; part=1 sections 1.1307, 1.1310; part=2 sections 2.1, 2.106, 2.201, 2.202, 2.815, 2.1057, 2.1091, 2.1093; part=15 section 15.23. Version histories: https://www.ecfr.gov/api/versioner/v1/versions/title-47.json?part=97&section=97.115 (same pattern).
- eCFR reader pages: https://www.ecfr.gov/current/title-47/section-2.106 , https://www.ecfr.gov/current/title-47/section-97.115 , https://www.ecfr.gov/current/title-47/section-2.202
- FCC Online Table of Frequency Allocations, Revised on July 1, 2022: https://transition.fcc.gov/oet/spectrum/table/fcctable.pdf (retrieved 2026-09-25 16:42 UTC)
- Federal Register API: https://www.federalregister.gov/api/v1/documents.json (queries: 47 CFR 97 documents published on or after 2026-01-01; 47 CFR 2 final rules published on or after 2022-07-01; FCC documents published 2026-07-31), retrieved 2026-09-25 16:46 to 16:53 UTC
- Federal Register full-text XML: https://www.federalregister.gov/documents/full_text/xml/2023/06/07/2023-11972.xml ; https://www.federalregister.gov/documents/full_text/xml/2023/09/29/2023-14656.xml ; https://www.federalregister.gov/documents/full_text/xml/2024/04/30/2024-06669.xml ; https://www.federalregister.gov/documents/full_text/xml/2026/01/14/2026-00587.xml ; https://www.federalregister.gov/documents/full_text/xml/2026/02/17/2026-03069.xml ; also 2023-13406, 2024-13641, 2025-15919, 2026-01442
- FCC 19-126: https://docs.fcc.gov/public/attachments/FCC-19-126A1.pdf (retrieved 2026-09-25 16:42 UTC)
- FCC DA 18-581: https://docs.fcc.gov/public/attachments/DA-18-581A1.pdf (retrieved 2026-09-25 16:42 UTC)
- OET Bulletin 65 Supplement B (Edition 97-01): https://transition.fcc.gov/Bureaus/Engineering_Technology/Documents/bulletins/oet65/oet65b.pdf (retrieved 2026-09-25 16:42 UTC)
- Project files: /Users/robinonsay/rust/cwht/docs/research/part97-regulatory-basis.md ; /Users/robinonsay/rust/cwht/docs/requirements/l0-stakeholder/stakeholder-inputs.md (SI-019, SI-030, SI-033, SI-034) ; /Users/robinonsay/rust/cwht/docs/process/00-charter.md section 11
- Computation scripts (session scratchpad, not in repo): bw.py, bw2.py, gen.py, xml2txt.py
