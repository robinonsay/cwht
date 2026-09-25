# Regulatory reference corpus for cwht

Primary-source rule texts that govern a US amateur-built 2 m (144.000 to 148.000 MHz) 5 W true-CW (A1A) handheld transceiver operated by a General-class licensee under 47 CFR Part 97. Built 2026-09-25 by the reg-corpus research subagent (research report: `docs/research/regulatory-corpus-and-operators.md`). Cite entries in project documents as, for example, `47 CFR 97.115(b)(1) (corpus: 47cfr-97.115.md, eCFR issue 2026-09-23)`.

## Provenance and currency

- All CFR texts were pulled verbatim from the eCFR versioner API, point-in-time full text for **issue date 2026-09-23** (the latest eCFR issue date available on 2026-09-25), retrieved 2026-09-25 16:39 UTC:
  `curl -sL --compressed "https://www.ecfr.gov/api/versioner/v1/full/2026-09-23/title-47.xml?part=97&section=97.115"`
  Each file header carries the API URL, the reader URL, and the amendment dates returned by the versions API (`https://www.ecfr.gov/api/versioner/v1/versions/title-47.json?part=97&section=97.115`).
- To re-check currency (ACTION-5 of part97-regulatory-basis.md, before CDR and before first on-air), re-run the versions query for each section and compare `latest_amendment_date` with the header of the corpus file. As of 2026-09-25 the Federal Register API lists no Part 97 rule published in 2026 other than 91 FR 1405 (2026-01-14, effective 2026-02-13, WRC-15 implementation), which is already incorporated.
- Rule text is verbatim. The XML was converted to markdown by a script: paragraphs one per block, tables flattened to pipe-delimited rows, original punctuation kept (including the em dashes the CFR itself uses, for example in 2.202(b)(3)). Nothing was reworded.
- The three FCC documents are US Government works (public domain); they are included as verbatim pdftotext extracts of the passages the project relies on, with the source URL and retrieval time in each header.

## Index

| File | Citation | Why it matters for cwht | Scope |
|---|---|---|---|
| 47cfr-97.3.md | 47 CFR 97.3 Definitions | Control operator (a)(13), control point (a)(14), third party communications (a)(47), bandwidth (a)(8), spurious emission (a)(43), harmful interference (a)(23), CW versus MCW (c)(1), (c)(4) | Assigned |
| 47cfr-97.5.md | 47 CFR 97.5 Station license required | (a) apparatus must be under the physical control of a licensee before it transmits; (c) a licensee may use any transmitting apparatus under their physical control as their station | Supplementary |
| 47cfr-97.7.md | 47 CFR 97.7 Control operator required | Every transmitting station needs a licensed control operator | Assigned |
| 47cfr-97.13.md | 47 CFR 97.13 Restrictions on station location | (c) RF exposure duty: 1.1307(b), 2.1091, 2.1093; household evaluated at occupational limits; OET 65 B referenced | Assigned |
| 47cfr-97.101.md | 47 CFR 97.101 General standards | Good engineering and good amateur practice; cooperation in channel selection; no willful interference | Assigned |
| 47cfr-97.103.md | 47 CFR 97.103 Station licensee responsibilities | Licensee responsible; joint responsibility with a different control operator; presumption unless station records say otherwise | Assigned |
| 47cfr-97.105.md | 47 CFR 97.105 Control operator duties | Immediate proper operation; privileges limited to the control operator's class | Assigned |
| 47cfr-97.109.md | 47 CFR 97.109 Station control | Local control requires the control operator at the control point | Supplementary |
| 47cfr-97.115.md | 47 CFR 97.115 Third party communications | Unlicensed persons may participate in stating the message only with the control operator present and continuously supervising | Assigned |
| 47cfr-97.119.md | 47 CFR 97.119 Station identification | Call sign every 10 minutes and at the end; automatic CW ID at most 20 WPM; indicator when the control operator's class exceeds the licensee's | Assigned |
| 47cfr-97.203.md | 47 CFR 97.203 Beacon station | 144.275-144.300 MHz beacon segment; 432.300-432.400 MHz (third harmonic of 144.100-144.133 MHz) | Assigned |
| 47cfr-97.221.md | 47 CFR 97.221 Automatically controlled digital station | Automatic control is limited to RTTY/data; a CW station cannot be automatically controlled (cf. 97.109(d), 97.115(c)) | Assigned |
| 47cfr-97.301.md | 47 CFR 97.301 Authorized frequency bands | (a) 2 m: 144-148 MHz in ITU Region 2 for Technician and above | Assigned |
| 47cfr-97.303.md | 47 CFR 97.303 Frequency sharing requirements | (a) general principle; (b), (m) 70 cm secondary to Federal radiolocation (third harmonic); (k) applies only in Regions 1 and 3 | Assigned |
| 47cfr-97.305.md | 47 CFR 97.305 Authorized emission types | (a) CW on any authorized frequency; (c) 144.1-148.0 MHz table for other modes | Assigned |
| 47cfr-97.307.md | 47 CFR 97.307 Emission standards | (a) necessary bandwidth, (b) confinement and keyclicks, (c) spurious reduction, (e) 30-225 MHz spurious limits (25 uW and 40 dB below 25 W) | Assigned |
| 47cfr-97.313.md | 47 CFR 97.313 Transmitter power standards | (a) minimum power necessary; (b) 1.5 kW PEP ceiling | Assigned |
| 47cfr-97.315.md | 47 CFR 97.315 Certification of external RF power amplifiers | Not applicable to an integral PA; amateur-built amplifiers exempt | Assigned |
| 47cfr-97.317.md | 47 CFR 97.317 Standards for certification of external RF power amplifiers | Reference only | Supplementary |
| 47cfr-1.1307.md | 47 CFR 1.1307 Actions that may have a significant environmental effect | (b) RF exposure evaluation and exemption framework (Table 1, lambda/2pi rule) | Assigned |
| 47cfr-1.1310.md | 47 CFR 1.1310 Radiofrequency radiation exposure limits | SAR and MPE limits, averaging times, occupational versus general population | Assigned |
| 47cfr-2.1.md | 47 CFR 2.1 Terms and definitions | Necessary bandwidth, occupied bandwidth, out-of-band and spurious emission, harmful interference, service definitions used by 2.106 | Supplementary |
| 47cfr-2.201.md | 47 CFR 2.201 Emission, modulation, and transmission characteristics | Emission designator symbols (A1A) | Supplementary |
| 47cfr-2.202.md | 47 CFR 2.202 Bandwidths | (a) occupied bandwidth (99 percent power), (b) necessary bandwidth, (g) Bn = BK for CW telegraphy, K = 3 or 5, example 100HA1A at 25 WPM | Assigned |
| 47cfr-2.106-harmonic-bands.md | 47 CFR 2.106 Table of Frequency Allocations (extract) | US allocations at 288-296, 432-444, 576-592, 720-740 and 1008-1036 MHz with the cited footnotes; see the file header for the table-image limitation and the July 2022 FCC PDF fallback | Assigned |
| 47cfr-2.815.md | 47 CFR 2.815 External radio frequency power amplifiers | Marketing prohibition context | Supplementary |
| 47cfr-2.1057.md | 47 CFR 2.1057 Frequency spectrum to be investigated | Tenth-harmonic measurement span used as the analog for the spurious bench procedure | Supplementary |
| 47cfr-2.1091.md | 47 CFR 2.1091 RF exposure evaluation: mobile devices | 20 cm mobile definition | Assigned |
| 47cfr-2.1093.md | 47 CFR 2.1093 RF exposure evaluation: portable devices | Portable definition; SAR regime; time averaging | Assigned |
| 47cfr-15.23.md | 47 CFR 15.23 Home-built devices | Five-or-fewer personal-use exemption for the unintentional radiators | Supplementary |
| fcc-19-126-extracts.md | FCC 19-126 (adopted 2019-11-27) | Paragraph 32, footnote 100, paragraph 116, footnote 143 (no exemption below 239 MHz for portables) | Assigned |
| oet65-supplement-b-extracts.md | OET Bulletin 65 Supplement B (1997) | Duty factors (CW 40 percent), source-based averaging, controlled-environment status of licensee and household, pre-2021 mobile/portable text | Assigned |
| fcc-da-18-581.md | FCC Enforcement Advisory DA 18-581 (2018-06-05) | Amateur-only transmitters exempt from equipment authorization; license still required to operate | Assigned |

## Known limitation: the 2.106 table body

The eCFR (and the Federal Register) publish the body of the Table of Frequency Allocations as page images, not text. In this headless environment the images could not be downloaded (HTTP 406 from ecfr.gov graphics, 403 from images.federalregister.gov) and no OCR tool is installed. `47cfr-2.106-harmonic-bands.md` therefore takes the five rows from the FCC's own "Online Table of Frequency Allocations, Revised on July 1, 2022" PDF (text), applies the changes since then from the Federal Register amendatory text (WRC-19 implementation 2023, WRC-15 implementation 2026), and quotes every cited footnote verbatim from the eCFR issue 2026-09-23 text. Row content is Medium confidence until the owner views the current page images in a browser (eCFR reader URL in the file header); footnotes are High confidence.

## Not in this corpus

47 CFR 97.113 (prohibited transmissions), 97.107 (reciprocal operation) and 97.215 (telecommand of model craft) were not fetched; add them if the ConOps needs them. The ARRL band plan and the Richard Tell QEX 2021 SAR paper are cited in `docs/research/part97-regulatory-basis.md` but are not reproduced here (copyrighted).
