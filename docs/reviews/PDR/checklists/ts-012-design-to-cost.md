---
# Peer-review record front matter (charter section 5; docs/process/01-lifecycle-and-reviews.md section 13;
# docs/process/06-risk-and-decision-analysis.md sections 14.2 section B, 14.3 step 6 and 16). Independent
# review of TS-012 with docs/templates/peer-review-checklist-risk.md section B. No template named
# peer-review-checklist-trade-study exists in docs/templates/ and no analysis checklist template exists
# there either, so section B of the risk checklist (the trade-study items CK-RSK-B1 to B10, the checklist the
# TS-012 header names) is applied. Record path as the brief names it; the TS-012 header names
# ts-012-design-to-cost-hand-built.md (cross item X-1).
# id: the brief assigned no id. INSP-110 is above every id on main, on every cr/ branch and in the working tree
# at 5c16930 (highest INSP-107, checked 2026-09-27), leaving INSP-108 and INSP-109 free for concurrent records.
id: INSP-110
checklist: peer-review-checklist-risk
checklist_revision: A
checklist_file: docs/reviews/PDR/checklists/ts-012-design-to-cost.md
product: docs/decisions/trade-studies/TS-012-design-to-cost-hand-built.md
product_commit: "5c16930824044958ee949b099eb4e6b8466facbc"
product_blob: 5da2c7c58c8ea759d7bcaa92e2efcb49f16de1bd
product_files: ["docs/decisions/trade-studies/TS-012-design-to-cost-hand-built.md@5da2c7c58c8ea759d7bcaa92e2efcb49f16de1bd"]
product_size: "5 alternatives (A0 dropped at M1; A1 to A4 scored; 5 pruned), 5 mandatory and 8 enhancing criteria; BOM of 33 Mouser rows, 5 other-seller rows, 5 shipping and duty lines; about 80 requirement deltas"
sprint: PDR-prep
author_agent: "author:TS-012 (Claude as trade-study author, invocation of 2026-09-27)"
reviewer_agent: "reviewer:TS-012-iter1 (independent; authored no part of TS-012, its architecture reports or its judge reports)"
# criticality: the study decides the hardware controls of REQ-SYS-055, 120, 180, 181, 182 and 092 and the
# Morse menu override command path (safety-critical by SRR decision 9; 07 section 14.1)
criticality: safety-critical
assurance_required: true
assurance_reviewer_agent: "pending (separate invocation; paired record docs/reviews/PDR/checklists/ts-012-design-to-cost-software-assurance.md)"
iteration: 1
readiness_met: false
reviewer_verdict: NEEDS CHANGES
assurance_verdict: pending
verdict: NEEDS CHANGES
findings_major: 3
findings_minor: 8
findings_open: 11
findings_fixed: 0
findings_verified: 0
findings_deferred: 0
deferred_rids: []
items_no: [CK-RSK-B5, CK-RSK-B7, CK-RSK-B8]
effort_turns: 45
effort_minutes: 75
record_status: Open
date: 2026-09-27
date_closed: null
---

# Peer review record: TS-012 design-to-cost architecture for a hand-built first radio (INSP-110, iteration 1)

**Product:** `docs/decisions/trade-studies/TS-012-design-to-cost-hand-built.md` blob `5da2c7c5` at commit `5c16930` (Revision 0, Proposed). `git rev-parse HEAD:<path>` and `git hash-object <path>` both give `5da2c7c5` on 2026-09-27. No product blob lives on a `cr/` branch.

**Checklist:** `docs/templates/peer-review-checklist-risk.md` revision A, section B (CK-RSK-B1 to B10). Section A is N/A because the product is a trade study.

**Owner direction applied:** status note `docs/plan/status/status-2026-09-27.md` sections 6 and 8. Where they differ, section 8 governs. The firm constraint is that the first complete radio costs under USD 200 all in. Size and through-hole construction are negotiable. SMD is acceptable if it can be hand-soldered with an iron, a heat gun, solder and flux. BGA and parts that need reflow are excluded. Listed prices only. The UI is a Morse menu.

**Acceptance criteria (every case the brief and the governing clauses list):**
- The cost roll-up of section 8.4 is re-added from the section 8.3 rows.
- At least ten listed prices and stock claims are spot-checked on the web, with a record of which could and could not be verified.
- Every requirement delta of section 8.10 is checked against `docs/requirements/sys/requirements.json`, `docs/requirements/tx/requirements.json` and `docs/requirements/sw/sw-keyer/requirements.json`, including a search for display, LCD, screen, knob, encoder, button and menu wording that the study did not list.
- No estimate is presented as a listed price.
- Each exception of sections 8.6 and 8.9 is shown to be necessary.
- The 06 section 16 trade-study items B1 to B10 are applied.

**Severity rule used (brief):** a finding is Major if the owner would decide on a wrong basis.

**Search rule.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` was run before every `grep`. It covered the checklist template, the INSP ids, display requirements and sales tax. All other files were read by known path.

## Findings (iteration 1)

| Finding | Severity | Item | Location | Description | State | Deferred to |
|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | Major | CK-RSK-B5, B8 | TS-012 section 7.2 row A4 ("The AFT05 is in active production"); section 8.6 row AFT05MS004NT1; section 8.4 AB3; section 7.1 A4 risks; section 10 revisit conditions | NXP's own product page, read 2026-09-27, marks the AFT05MS004N **"End of Life"**. It adds "Contact support, your local sales representative or an NXP Authorized Distributor for product availability" and lists the part under "Legacy RF Power". TS-012 says the device is "in active production" and counts a later 70 cm revision on the same device as a benefit. Distributor stock does exist today (Mouser 72, Newark 1,519, DigiKey 0; via the aggregator). But the owner would be choosing an architecture whose one hand-matched RF device is end of life, and would treat the spare (AB3) as an optional add-back. **Fix:** (a) state the EOL status in sections 1, 7.2 and 8.6; (b) add an A4 risk in the four-part format (linked to RSK-038); (c) either make AB3 (spare AFT05, USD 5.31 capped) part of the baseline order, or state in section 1 why it is not; (d) name the fallback if stock runs out before the order (the RA07M1317M at about +USD 45 already appears in EX-3), and say whether it fits the cap; (e) remove the 70 cm reuse benefit or qualify it | Open | |
| <a id="finding-2"></a>finding-2 | Major | CK-RSK-B5, B7 | TS-012 sections 1 (cost bullet), 4.1 M1, 6 item 4, 8.3 "Shipping, duty and tariff", 8.4 roll-up and ordering gate | The "all in" roll-up has **no US sales tax line**. The owner said the cap is "all in". Mouser and 18650BatteryStore charge sales tax in states that levy it, and the ordering gate reads only merchandise, shipping and tariff. Taxable goods at planning are about USD 120 (Mouser goods at their midpoint, cells, charger and magnet wire). At 6 % the capped planning total becomes **USD 199.10**; at 8.25 % it is **202.22**; at 10 % it is **204.64**. Those figures also include the finding-4 correction (reviewer computation, table "Roll-up re-add" below). So in many states the planning case, not only the high case, needs guard G1. The owner's state is not recorded in the repository. **Fix:** (a) add a sales tax line (the owner's state rate times taxable goods, and shipping where the state taxes it), marked E until the owner confirms the rate; (b) add the tax line to the ordering-gate reads; (c) recompute sections 1, 4.1, 4.2 (C1 and C2 for every alternative) and 6; (d) ask the owner whether "all in" includes sales tax, and record the answer | Open | |
| <a id="finding-3"></a>finding-3 | Major | CK-RSK-B5, B8 | TS-012 sections 4.1 row A4 M4 ("pass (both controls restored)"); 4.2 C5-A4 ("frequency counter"); 7.1 A4 risk "recalled near 150 MHz"; 8.1; 8.2; 8.6; 8.10 REQ-SYS-182 | The REQ-SYS-182 control depends on an SN74LVC74A toggling at up to 148 MHz. TI's product page, read 2026-09-27, lists "Clock frequency (max) (MHz) 100". The study relies on a recalled figure near 150 MHz. The mandatory M4 pass of A4 and the claim that "both controls" are restored therefore rest on a part used about 48 % above its published maximum clock rate. A4 is still the only alternative to pass M4 after A1 is excluded, so the owner would be deciding on an unsupported mandatory pass. **Fix:** choose a prescaler with a published maximum toggle frequency above 148 MHz with margin at the supply used, in a hand-solderable package (SOIC or SOT-23 preferred over SSOP; see finding-6). Record its listed price and stock (kind A or L). Correct the 7.1 risk statement to the published value, and mark M4 for A4 conditional until the new part's datasheet is read. The cost change is likely small, so the ranking is unlikely to change, but the basis must be corrected | Open | |
| <a id="finding-4"></a>finding-4 | Minor | CK-RSK-B5 | TS-012 section 8.3 rows 15, 22 and 33; section 8.2 row "AO3400A high-case correction"; section 8.11 item 1 | Row 22 gives AO3400A as "0.09 ... 50,678 ... A (re-read today)" under Mouser. On the aggregator page read today, the 0.09 and 50,678 row is **Newark at quantity 10**. The Mouser row is **USD 0.52, 303,947 in stock**. A Newark quantity-10 price is therefore shown as a Mouser quantity-1 listed price, and the correction is carried only as an estimate (row 33, 0 to 0.86). With 0.52 in the listed subtotal (Mouser listed 68.26) and row 33 removed, the capped totals are **168.94 / 190.78 / 212.64** (planning +0.49). Row 15 (1N5711W-7-F, 0.24, 1,839) also differs from today's aggregator read (Mouser 0.307, 3,033; 0.24 is an RS quantity-50 price). **Fix:** correct rows 15 and 22, remove row 33, and update the section 8.4 totals | Open | |
| <a id="finding-5"></a>finding-5 | Minor | CK-RSK-B5 | TS-012 section 8.3 "US duty on the boards" (1.40 to 2.40, "35 % (JLCPCB tariff FAQ, listed) to 60 % (Hack Club cost guide)"); section 6 item 3 | JLCPCB's US tariff FAQ, read 2026-09-27, states "Total tariff rate: About 35%~92.5%" and does not say whether the rate applies to the board value or to the whole order. The high case uses 60 %, not the published 92.5 %. At 92.5 % of USD 4.00 the high duty is 3.70 (+1.30, +1.50 capped). The high case moves to 214.13 with finding-4, and G1 still holds it at about 198.96 before any sales tax. **Fix:** use 35 % to 92.5 % from the FAQ, state that the base is not published, and add the duty base to ordering-gate read (2) | Open | |
| <a id="finding-6"></a>finding-6 | Minor | CK-RSK-B4, B5 | TS-012 sections 7.3 ("The TO-92 J310 is out of stock at LCSC"), 3.2 pruned list, 8.6 rows MMBFJ310, 1N5711W, AO3400A and SN74LVC74ADBR; 8.9 EX-1 | Some reasons given for the SMD exceptions do not match what was read today, although the exceptions themselves mostly hold. (a) The through-hole J310 is in stock at Mouser (InterFET J310, USD 5.83, 381) and at DigiKey (Linear Integrated Systems, USD 5.61, per a search summary). The SOT-23 choice is justified by cost (4 x about USD 5.6), not by stock. (b) A through-hole DO-35 1N5711 is listed (STMicroelectronics at Future Electronics, USD 0.295, 527). SOD-123 is justified by keeping a single Mouser order, and the study should say so. (c) "Through-hole protector FETs out of stock" (AO3400A) has no evidence in the study. (d) SN74LVC74ADBR is SSOP-14 at the owner's 0.65 mm limit, while the SOIC-14 variants of the same part are stocked at Mouser (SN74LVC74ADRQ1 USD 0.58, 2,940; SN74LVC74AD USD 1.13, 441). The owner prefers the easiest package when cost is near-equal. This part is replaced by finding-3 anyway. **Fix:** restate each reason with its evidence, and prefer SOIC for the finding-3 replacement | Open | |
| <a id="finding-7"></a>finding-7 | Minor | CK-RSK-B5 | TS-012 section 8.10 | Reviewer search of the requirement files (table "Requirement delta check" below) found requirements that A4's UI and power design affect but that section 8.10 does not list. **REQ-SYS-066** asks for a "held button combination" and A4 has one button. **REQ-SYS-163** asks for key-input mode selection "while any key input reads closed", but the Morse menu takes its selection letters from the key or paddle, so a key that reads closed blocks the very recovery REQ-SYS-163 exists for; section 8.7 gives no button-only path. **REQ-SYS-085** needs a 3 A to 10 A discharge trip, and the S-8252AAO detection voltage with 2 x AO3400A is not shown to fall in that window. **REQ-SW-KEYER-014, 023 and 032** name display frames, encoders, the display interface and "displayed speed". The S-8252AAO detection voltages (4.25 V, 2.50 V) behind the REQ-SYS-083 and 084 claims are not shown with a source. The series datasheet summary gives the ranges, not the AAO rank. **Fix:** add these rows to section 8.10, and give REQ-SYS-163 a button-only design answer | Open | |
| <a id="finding-8"></a>finding-8 | Minor | CK-RSK-B5 | TS-012 sections 1 ("estimated 4.4 W at 6.4 V"), 7.3 PA output, 8.10 REQ-SYS-012 | The estimate of 4.4 W at 6.4 V scales the vendor 7.5 V figure by pack voltage squared. It does not include the drop in the drain feed: 2 x AO3400A, MF-R300, DMP3099L, the holder contacts and the choke, at about 1.3 A. The reviewer estimates about 0.2 to 0.3 V from typical on-resistance classes, not from datasheets read in this review. It also ignores LDMOS knee voltage. At about 6.1 V on the drain, V-squared scaling gives about 4.0 W, which is at the 3.97 W floor of REQ-SYS-012 (a KDR). Knee voltage lowers this further. The study already says "marginal", so this does not change the ranking. **Fix:** add a drain-feed drop budget, and record REQ-SYS-012 as a probable delta at the low pack voltage, or state the drop budget that keeps it | Open | |
| <a id="finding-9"></a>finding-9 | Minor | CK-RSK-B5 | TS-012 section 1 (cost bullet); 8.4 AB1; 8.9 EX-13; 8.8 D11 | "Fits the USD 200 cap" relies on EX-13, which puts a 10 W 30 dB pad (estimated USD 15 to 25) and a thermocouple (USD 9.95) outside the cap. The owner's direction covers only the committed tinySA Ultra ("to be confirmed"). Both items are needed to verify the first radio: the tinySA harmonic measurement before on-air use, and the REQ-SYS-112 and 113 checks. AB1 (monitor port) removes the pad for USD 2.80 before contingency. That makes AB1 cheaper than the pad it replaces, yet AB1 is an add-back. The arithmetic of AB1 is also inconsistent: 2.80 x 1.15 = 3.22, not 3.45. **Fix:** state the EX-13 condition in section 1; move AB1 into the baseline or explain why not; correct the AB1 figure | Open | |
| <a id="finding-10"></a>finding-10 | Minor | CK-RSK-B5 | TS-012 sections 7.3 thermal chain ("then 1 K/W interface"), 8.3 BOM, 8.9 EX-8 | The thermal chain counts a 1 K/W interface between the PA board and the sink, but no thermal interface material (compound or pad) appears in the BOM, the estimates or the owner-stock list. Knobs for the two owner potentiometers are also not listed (REQ-SYS-111 still applies to them). **Fix:** add these as estimated lines or owner-stock items | Open | |
| <a id="finding-11"></a>finding-11 | Minor | CK-RSK-B5 | TS-012 sections 4.2 C8-A4 (score 4), 7.3 thermal chain, 8.1 "screwed flat to the inside face", 8.5 | Two distributor descriptions read today (through the aggregator) describe the Boyd 530002B02500G as "Heat Sink, Extruded, Double Center Channel and Radial Fins" and "TO-220 ... Vertical". The 2.6 K/W rating is for a TO-220 on the centre channel in free air. With a double-channel radial profile, some fin area may face into the case, and the inside face may not be a flat 40 x 35 mm plane for the PA board. The thermal chain assumes both. The Tj estimate of 86 to 97 C and the C8 score of 4 depend on this. Owner check item 6 asks for the drawing, but the study does not carry the case where the assumption fails. The sink mass (30 to 60 g) is also unread. **Fix:** read the drawing, or state a fallback (a flat plate spreader, or a sink rotated so that all fins are outside) with its cost, and give C8 a Low-confidence range | Open | |

**Summary.** Three Major findings. In each, the owner would decide on a wrong or unsupported basis:
- the PA device is end of life, not in active production (finding-1);
- the "all in" total has no sales tax, which can remove the planning margin (finding-2);
- the REQ-SYS-182 prescaler, and with it the A4 mandatory safety pass, relies on a part with a published maximum of 100 MHz (finding-3).

A4 still ranks first, 85 points ahead, on the enhancing matrix. Each Major has a cheap repair, so the recommendation may survive. It cannot be put to the owner until the three bases are corrected.

## Readiness criteria

| # | Criterion | Result | Evidence |
|---|---|---|---|
| R1 | `validate_docs.py` exits 0 | **No** | `validate_docs: 98 passed, 10 failed, 108 checked`, exit 1. All 10 failures are record drift in other records (CR-007, TS-001, TS-002, ADR-001 to 003, TV and SRR records). None involves TS-012. The review proceeded because the product and this record are unaffected (the same practice as earlier PDR records) |
| R2 | Section A render check | N/A | Product is a trade study |
| R3 | Sections 1 to 9 filled; section 10 empty | Yes | TS-012 sections 1 to 9 present; section 10 "Left empty until the owner decides" |
| R4 | Author return lists the decision need and gate | Yes (from the product) | Header "Decide by": B1a 2026-09-29, no later than B1b 2026-10-01 |

## B. Trade study (06 section 16, items 1 to 10)

| Id | Answer | Evidence |
|---|---|---|
| CK-RSK-B1 | Yes | Header row "Decision class trigger" names 06 section 14.1 class 1 items (a), (b), (c), (d), (f). Decision maker: Robin. Gate: B1a or B1b |
| CK-RSK-B2 | Yes | Section 3.1: eight enhancing criteria, each with an operational definition and anchored 1 to 5 scale; M1 to M5 pass or fail. The "Criteria considered" line covers safety (M4, C8), first power-on (C4), cost (M1, C1, C2), schedule (omitted, with reason), performance margin (M5, C5) and system security (omitted, with reason) |
| CK-RSK-B3 | Yes | 25+10+15+10+15+10+5+10 = 100, integers; rationale in section 3.3 |
| CK-RSK-B4 | Yes | A0 do-nothing present and dropped at M1. Five pruned alternatives with reasons. Some pruning and exception reasons need correction (finding-6) but do not change coverage |
| CK-RSK-B5 | **No** | Evidence gaps behind M1 (finding-2), M4 (finding-3), C8 (finding-11), the AO3400A price (finding-4) and the A4 benefit statement (finding-1) |
| CK-RSK-B6 | Yes | Reviewer recomputation: A1 255, A2 215, A3 255, A4 340, as in section 5. Roll-up re-added exactly (table below) |
| CK-RSK-B7 | **No** | Section 6 follows 14.4: weight ±10, Low cells ±1, verdict, value of information, limitations. But its "Not robust" cost verdict leaves out the sales tax line (finding-2) and the published duty ceiling (finding-5), and it does not name the M4 dependence on the prescaler (finding-3) |
| CK-RSK-B8 | **No** | Section 7.1 has four-part risks for A2, A3 and A4. It lacks an A4 PA end-of-life risk (finding-1), and the prescaler risk statement rests on a recalled 150 MHz where the published value is 100 MHz (finding-3) |
| CK-RSK-B9 | Yes (conditional) | A4 has the highest total (340) and is recommended. The recommendation follows from the matrix, but its M1 and M4 bases need findings 2 and 3 corrected |
| CK-RSK-B10 | Yes | Section 9 lists the panel dissent and the pending independent review; section 10 empty |

## Independent checks

### Roll-up re-add (section 8.4)

Mouser listed rows 1 to 28 re-added: **67.40**. Every line equals quantity times unit price. Listed parts: 67.40 + 11.98 + 4.99 + 13.19 + 4.00 = **101.56**. Estimated rows 29 to 33: 17.08 / 22.51 / 27.94. Mouser merchandise: 84.48 to 95.34. Guard and add-back values: G1 -15.17, G3 -3.45 to -6.90 and -14.38 to -21.28, G4 -5.74, G6 -6.55, AB2 +4.15 and AB3 +5.31 all reproduce. AB1 does not (finding-9).

| Case | TS-012 subtotal | TS-012 capped | Reviewer, as written | Reviewer, with finding-4 and finding-5 | Same, plus sales tax 6 % / 8.25 % / 10 % on goods (finding-2, E) |
|---|---|---|---|---|---|
| Low | 146.04 | 167.95 | 146.04 / 167.95 | 146.90 / 168.94 | 176.90 / 179.89 / 182.22 |
| Planning | 165.47 | 190.29 | 165.47 / 190.29 | 165.90 / 190.78 | **199.10 / 202.22 / 204.64** |
| High | 184.90 | 212.64 | 184.90 / 212.64 (212.635) | 186.20 / 214.13 | 222.79 / 226.04 / 228.56 |

Taxable goods (reviewer): Mouser goods plus cells, charger and magnet wire, about 115.50 / 120.50 / 125.50. The tax rates are illustrative, not the owner's rate. With G1 (-15.17 capped), the planning case with 8.25 % tax returns to about 187 (reviewer estimate, not a recomputation of the tax base without the wire).

### Price and stock spot checks (retrieved 2026-09-27; nothing logged into, no form, no cart, no download)

| # | Item (TS-012 row) | TS-012 claim | Read today | Kind | Source | Result |
|---|---|---|---|---|---|---|
| 1 | Adafruit 2045 Si5351A (row 10) | 7.95, in stock | "$7.95", "In stock" | L | https://www.adafruit.com/product/2045 | Verified |
| 2 | Pico 2 (row 9) | PiShop 5.00 in stock; Mouser 5.00, 2,078 | PiShop "$5.00" "IN STOCK"; Mouser SC1631 5.00, 2,078 | L; A | https://www.pishop.us/product/raspberry-pi-pico-2/ ; https://www.oemstrade.com/search/SC1631 | Verified |
| 3 | Molicel P28A x2 | 5.99 sale (6.99), in stock | "$5.99" sale, "$6.99" regular, "In stock" | L | https://www.18650batterystore.com/products/molicel-p28a | Verified |
| 4 | XTAR MC1 | 4.99 sale (9.99), in stock | "$4.99" sale, "$9.99" regular, "In stock", 500 mA; termination voltage not stated | L | https://www.18650batterystore.com/products/xtar-mc1 | Verified (termination voltage not on page) |
| 5 | Remington 20SNSP.125 | 13.19, 40 ft, free shipping | "$13.19", 40 ft, shipping "$0" | L | https://www.remingtonindustries.com/magnet-wire/magnet-wire-20-awg-enameled-copper-9-spool-sizes/ | Verified |
| 6 | JLCPCB boards | "From $2.00 / 5 pcs" each | "From $2.00 / 5 pcs"; no size or multi-design terms on the page. Hack Club guide: "$2 for 2 layer boards under 100x100mm" | L (floor only) | https://jlcpcb.com/ ; https://highway.hackclub.com/guides/JLC-cost-optimizing | Floor verified; two-design price is owner to verify in the quote tool |
| 7 | AFT05MS004NT1 (row 1) | Mouser 4.62, 72; Newark 4.21, 1,519; DigiKey 4.15, 0 | Same figures | A | https://www.oemstrade.com/search/AFT05MS004NT1 | Verified; **NXP status "End of Life"** (finding-1), https://www.nxp.com/products/radio-frequency-rf/legacy-rf/legacy-rf-power/136-941-mhz-4-w-7-5-v-wideband-rf-power-ldmos-transistor:AFT05MS004N ; the same page gives 6.1 W, 17.8 dB, 61.8 % at 7.5 V, 136 to 174 MHz |
| 8 | GVA-84+ (row 2) | 2.99, 2,754 | Mouser 2.99, 2,754 | A | https://www.oemstrade.com/search/GVA-84+ | Verified |
| 9 | Omron G5V-2-DC5 (row 3) | 3.33, 2,988 | Mouser 3.33, 2,988 | A | https://www.oemstrade.com/search/G5V-2-DC5 | Verified |
| 10 | Boyd 530002B02500G (row 4) | 3.39, 3,693; 63.5 x 41.9 x 25.4 mm | Mouser 3.39, 3,693; "Double Center Channel and Radial Fins"; Farnell title 41.91 x 63.5 x 25.4 mm | A | https://www.oemstrade.com/search/530002B02500G | Price verified; profile concern (finding-11); mass **not verifiable** (Amazon HTTP 500, RS HTTP 403) |
| 11 | Coilcraft 1812SMS-68NJLC (row 6) | 1.90, 784; Coilcraft direct 1.01, 2,989 | Same | A | https://www.oemstrade.com/search/1812SMS-68NJLC | Verified (1812SMS-82NJLC stock 79 not re-read) |
| 12 | AO3400A (row 22) | Mouser 0.09, 50,678 | Mouser 0.52, 303,947; 0.09 at 50,678 is Newark at quantity 10 | A | https://www.oemstrade.com/search/AO3400A | **Discrepancy** (finding-4) |
| 13 | SN74LVC74ADBR (row 28) | 0.34, 4,292 | Mouser 0.34, 4,292; SOIC variants at Mouser 0.58 (ADRQ1, 2,940) and 1.13 (AD, 441). TI page: "Clock frequency (max) (MHz) 100" | A; L | https://www.oemstrade.com/search/SN74LVC74AD ; https://www.ti.com/product/SN74LVC74A | Price verified; **fmax** (finding-3) |
| 14 | Keystone 1043P (row 20) | 2.95, 10,041 | Mouser 2.95, 10,041; single 18650 holder | A | https://www.oemstrade.com/search/1043P | Verified |
| 15 | LM2940CT-5.0/NOPB (row 25) | 2.04, 141 | Mouser 2.04, 141 (Newark 2.13, 1,002) | A | https://www.oemstrade.com/search/LM2940CT-5.0%2FNOPB | Verified |
| 16 | S-8252AAO-M6T1U (row 21) | 1.66, 3,390 | Mouser 1.66, 3,390; 2-cell protector, SOT-23-6 | A | https://www.oemstrade.com/search/S-8252AAO-M6T1U | Price verified; AAO rank thresholds **not verifiable** without the datasheet PDF (not downloaded) |
| 17 | ECS-80-20-4X (row 12) | 0.532 at 10+, 1,990 | Mouser 0.61 at 1, 0.53 at 10, 1,990 | A | https://www.oemstrade.com/search/ECS-80-20-4X | Verified; quantity-1 price now captured (0.61) |
| 18 | MMBFJ310LT1G (row 11) | 0.23, 184,334 | Mouser 0.23, 184,334 | A | https://www.oemstrade.com/search/MMBFJ310LT1G | Verified |
| 19 | 1N5711W-7-F (row 15) | 0.24, 1,839 | Mouser 0.307, 3,033 (aggregator rows partly mixed) | A | https://www.oemstrade.com/search/1N5711 | **Discrepancy** (finding-4), USD 0.27 on 4 parts |
| 20 | JLCPCB shipping, forum 2026-03-19 | about 12 shipping, about 2 tax, USD 10 boards, 12 days | Same ("Two batches of 10 boards") | Forum report | https://forum.allaboutcircuits.com/threads/jlcpcb-global-standard-direct-line-shipping.209788/ | Verified |
| 21 | JLCPCB duty | 35 % (FAQ) to 60 % (Hack Club) | FAQ "About 35%~92.5%"; Hack Club "60% when the order is placed" | L | https://jlcpcb.com/help/article/us-tariff-policy-faq | **Range wider** (finding-5) |
| 22 | Mouser free-shipping threshold | USD 100 (search summary, Low) | Mouser help page timed out; EEVblog and ModWiggler threads HTTP 403; a search summary says USD 100 for US orders | E | https://www.mouser.com/help/orders-shipping/ | **Not verifiable**; owner to verify in a browser |
| 23 | Mouser tariff pass-through | "a percentage of the imposed tariffs" | Mouser tariff page timed out; a search summary gives the same wording and a 50 % Section 301 rate on HTS 8541 and 8542 from 2025-01-01 | E | https://www.mouser.com/en/section-301-tariff-updates/ | **Not verifiable**; stays E |
| 24 | 18650BatteryStore shipping | USD 5 to 8 (E) | Shipping page URL guessed as /pages/shipping-policy returned HTTP 404; no rate read | E | - | **Not verifiable**; owner to verify at the cart |
| 25 | TO-92 J310 (section 7.3) | "unverified at DigiKey and Mouser" | InterFET J310 at Mouser 5.83, 381 | A | https://www.oemstrade.com/search/J310 | Available (finding-6) |

Totals: 21 items verified or shown to differ, 4 not verifiable (Mouser shipping threshold, Mouser tariff page, 18650BatteryStore shipping, Boyd mass), and 2 datasheet facts not verifiable without downloading a PDF (S-8252AAO rank thresholds, XTAR MC1 termination tolerance). Rows not re-read: 5, 7, 8, 13, 14, 16, 17, 18, 19, 23, 24, 26, 27, the 1812SMS-82NJLC stock, CONSMA001-C-G and TG2520SMN.

### Estimate against listed-price presentation

- Section 8.3 separates L, A and E consistently. The rows marked E (29 to 33, shipping, tariff) are labelled as estimates with their bases.
- Exceptions:
  - Row 22 presents a Newark quantity-10 price as the Mouser price (finding-4).
  - The board duty labels 35 % as "listed", but the published range runs to 92.5 % (finding-5).
  - The JLCPCB board line is a listed floor ("From $2.00"). It is correctly marked "owner to verify", but it is carried as L in the listed subtotal. The reviewer accepts this with the owner check.
- In the executive summary, "USD 190.29" is a planning figure that includes estimates, and the summary says so ("planning").

### Requirement delta check (section 8.10 against the requirement files at HEAD)

- Every "Current" value in section 8.10 was compared with the requirement text. REQ-SYS-006, 008, 009, 010, 012, 013, 017, 018, 022, 023, 029, 031, 032, 033, 044, 055, 057 to 063, 067 to 070, 081 to 094, 096, 100 to 104, 106, 109, 112, 113, 120, 124, 137 to 141, 144 to 147, 164, 165, 167, 171, 172, 175, 177, 178, 180 to 183, 185, 186 and REQ-TX-002, 009 to 011 all match their current wording and values.
- Classes (KDR, Baseline, Goal) agree where the study states them: KDR for 010, 012, 102, 103, 137, 140; Goal for 023, 069, 171, 177.
- The display search (display, LCD, screen, legible, character, knob, encoder, detent, button, menu, show, indicate) found every display requirement in section 8.10 except those in finding-7. Missing: REQ-SYS-066, 163 and 085, and REQ-SW-KEYER-014, 023 and 032. REQ-SYS-111 (knob clearance) needs no delta because the potentiometers keep knobs.
- Derived values re-checked:
  - REQ-SYS-008/009 guard: 30 ppm x 148 MHz = 4.44 kHz, + 0.83 kHz = 5.27 kHz, giving 144.0053 MHz.
  - REQ-SYS-182: 60 ppm x 148 MHz = 8.88 kHz, inside 10 kHz. Counter gate quantization is not counted.
  - REQ-SYS-102: mass 277 to 347 g re-added from the part masses.
  - REQ-SYS-103: 142 x 70 x 42 mm stack re-added (142.4 mm unrounded). Volume +6.5 % and +11.7 % with the SMA reproduce (417,480 and 438,060 against 392,000 mm3).

### Exceptions necessity (sections 8.6 and 8.9)

| Exception | Necessary? | Basis |
|---|---|---|
| EX-1 SOT-89 AFT05 and GVA-84+ | Yes | No through-hole device reaches 5 W from catalog stock (RD06HVF1 at 3.8 W at 7 V is in section 7.3 but was not re-read) |
| EX-1 MMBFJ310 | Yes, on cost | The through-hole J310 is listed at about USD 5.6 to 5.8 (finding-6) |
| EX-1 1N5711W | Marginal | A DO-35 part is listed at another distributor (finding-6) |
| EX-1 AO3400A, DMP3099L, S-8252AAO | Yes for S-8252; AO3400A reason not evidenced | finding-6 |
| EX-1 SSOP-14 prescaler | No as chosen | SOIC variants in stock; the part changes anyway (findings 3 and 6) |
| EX-1 Coilcraft 1812SMS, 0805 and 1206 | Yes | LPF quality and VHF lead inductance |
| EX-2 modules | Yes | Owner direction item, to be confirmed |
| EX-3 AFT05 at 5 W | Yes, with EOL disclosed | NXP page gives 6.1 W at 7.5 V in the 136 to 174 MHz circuit (finding-1) |
| EX-4, EX-5, EX-9, EX-14 | Yes, on cost | Each has a stated add-back or owner-stock route |
| EX-7 | Only if AB2 is funded | Leadless TCXO, correctly flagged |
| EX-13 | Not shown to be necessary | AB1 is cheaper than the pad (finding-9) |

## Visual closure

No figure, render or chart is part of the product. N/A.

## Items N/A

CK-RSK-A1 to CK-RSK-A11 (the product is a trade study, not the register).

## Cross items for the lead SE (not findings on TS-012)

- **X-1.** The TS-012 header row "Independent reviewer" names `docs/reviews/PDR/checklists/ts-012-design-to-cost-hand-built.md` and "INSP-NNN". This record is filed at `docs/reviews/PDR/checklists/ts-012-design-to-cost.md` as INSP-110, as the brief directs. The header should name this path and id in revision 1.
- **X-2.** `assurance_required: true`, because the study decides safety-critical hardware controls and the Morse menu override path (07 section 2.1.1 row "Trade studies and ADRs"). The software assurance pair is not yet dispatched.
- **X-3.** `validate_docs.py` has 10 failures from record drift that is unrelated to TS-012 (readiness R1).
- **X-4.** The owner's state for sales tax (finding-2) is an owner input and belongs in the status note or the re-baseline CR with the next free SI id.

## Commands

```
git rev-parse HEAD:docs/decisions/trade-studies/TS-012-design-to-cost-hand-built.md   # 5da2c7c58c8ea759d7bcaa92e2efcb49f16de1bd
git hash-object docs/decisions/trade-studies/TS-012-design-to-cost-hand-built.md       # 5da2c7c58c8ea759d7bcaa92e2efcb49f16de1bd
/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/validate_docs.py   # 98 passed, 10 failed, 108 checked (exit 1; failures unrelated to TS-012)
python3 (scratchpad) roll-up re-add of section 8.3 rows 1 to 28 and section 8.4; matrix totals of section 5; requirement text extraction and display-word search over docs/requirements/**/requirements.json
```

## Measurements (SWE-089)

size = 5 alternatives, 13 criteria, 38 BOM and 5 shipping rows; turns = 45; minutes = 75; major = 3; minor = 8.

## Verdict (returned by the reviewer)

```
VERDICT: NEEDS CHANGES
FINDINGS:
- [Major] CK-RSK-B5, B8 section 7.2, 8.6: AFT05MS004N is "End of Life" on the NXP page; the study says active production (finding-1).
- [Major] CK-RSK-B5, B7 section 8.3, 8.4: no sales tax line in the "all in" total; planning becomes 199 to 205 at 6 to 10 % (finding-2).
- [Major] CK-RSK-B5, B8 section 4.1 M4, 7.1: SN74LVC74A published maximum clock 100 MHz against 148 MHz; the REQ-SYS-182 control and the A4 M4 pass are unsupported (finding-3).
- [Minor] CK-RSK-B5 section 8.3 rows 15, 22, 33: AO3400A shows Newark's quantity-10 price as Mouser's; Mouser is 0.52 (finding-4).
- [Minor] CK-RSK-B5 section 8.3 duty: JLCPCB FAQ gives 35 to 92.5 % (finding-5).
- [Minor] CK-RSK-B4, B5 section 7.3, 8.6: exception reasons (J310 TO-92, DO-35 1N5711, AO3400A, SSOP against SOIC) (finding-6).
- [Minor] CK-RSK-B5 section 8.10: REQ-SYS-066, 163, 085 and REQ-SW-KEYER-014, 023, 032 missing; S-8252AAO thresholds unsourced (finding-7).
- [Minor] CK-RSK-B5 section 7.3: REQ-SYS-012 power ignores the drain-feed drop (finding-8).
- [Minor] CK-RSK-B5 section 1, 8.9 EX-13: pad and thermocouple outside the cap; AB1 cheaper; AB1 arithmetic (finding-9).
- [Minor] CK-RSK-B5 section 8.3: thermal interface material and pot knobs missing (finding-10).
- [Minor] CK-RSK-B5 section 7.3, 8.1: Boyd radial double-channel profile against the flat-face and fins-outside assumptions; mass unread (finding-11).
ITEMS N/A: CK-RSK-A1 to CK-RSK-A11 (product is a trade study)
MEASUREMENTS: size=5 alternatives, 13 criteria; turns=45; minutes=75; major=3; minor=8
```
