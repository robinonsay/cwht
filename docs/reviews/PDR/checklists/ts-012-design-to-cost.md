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
# product_commit (iteration 2): eca24fa, the TS-012 revision 2 commit. The blob below equals git rev-parse
# eca24fa:<path>, HEAD:<path> and git hash-object <path> at HEAD eca24fa on 2026-09-27; it is on main.
# product_files_iteration_1 keeps the 5c16930 blob reviewed at iteration 1.
product_commit: "eca24fa78457b3de9834df78be0ca33c5bea9ecd"
product_blob: 7432bba479c2a4264b317e35b0c7ac48b85370ad
product_files: ["docs/decisions/trade-studies/TS-012-design-to-cost-hand-built.md@7432bba479c2a4264b317e35b0c7ac48b85370ad"]
product_files_iteration_1: ["docs/decisions/trade-studies/TS-012-design-to-cost-hand-built.md@5da2c7c58c8ea759d7bcaa92e2efcb49f16de1bd"]
# product_size (iteration 2); iteration 1 was "5 alternatives (A0 dropped at M1; A1 to A4 scored; 5 pruned), 5 mandatory
# and 8 enhancing criteria; BOM of 33 Mouser rows, 5 other-seller rows, 5 shipping and duty lines; about 80 requirement deltas"
product_size: "6 alternatives (A0 dropped at M1, A1 at M4; A2 to A5 ranked; 7 pruned), 5 mandatory and 8 enhancing criteria; A5 BOM of 31 Mouser rows, 4 estimated rows, 4 other-seller rows, 7 shipping, duty and tariff lines; A4 roll-up; 4 upgrades with risk per dollar; about 90 requirement deltas"
sprint: PDR-prep
author_agent: "author:TS-012 (Claude as trade-study author, invocation of 2026-09-27)"
reviewer_agent: "reviewer:TS-012-iter1 (independent; authored no part of TS-012, its architecture reports or its judge reports); iteration 2 by reviewer:TS-012-iter2 (independent; authored no part of TS-012 revision 1 or 2)"
# criticality: the study decides the hardware controls of REQ-SYS-055, 120, 180, 181, 182 and 092 and the
# Morse menu override command path (safety-critical by SRR decision 9; 07 section 14.1)
criticality: safety-critical
assurance_required: true
assurance_reviewer_agent: "pending (separate invocation; paired record docs/reviews/PDR/checklists/ts-012-design-to-cost-software-assurance.md)"
iteration: 2
# readiness_met: false at iterations 1 and 2 on R1 only (validate_docs.py exits 1 on 10 records unrelated to TS-012;
# this record passes). R3 and R4 hold on revision 2 (iteration 2 readiness table)
readiness_met: false
# reviewer_verdict (iteration 2): APPROVED. finding-1 to finding-3 (Major) Verified; finding-4 to finding-10 (Minor)
# Verified; finding-11 fixed in part and new findings 12 to 16 are Minor and Open, liens due at the CDR readiness
# declaration (PDR work plan rule C1). Iteration 1 was NEEDS CHANGES
reviewer_verdict: APPROVED
assurance_verdict: pending
# verdict: held at NEEDS CHANGES until the software assurance pair (ts-012-design-to-cost-software-assurance.md, not yet
# dispatched; cross item X-2) returns APPROVED and readiness R1 holds (07 section 2.1.1; rule C9)
verdict: NEEDS CHANGES
findings_major: 3
findings_minor: 13
findings_open: 6
findings_fixed: 0
findings_verified: 10
findings_deferred: 0
deferred_rids: []
# items_no: iteration 1 was [CK-RSK-B5, CK-RSK-B7, CK-RSK-B8]; at iteration 2 every B item is Yes (B5 and B8 with liens)
items_no: []
# effort: iteration 1 45 turns, 75 minutes; iteration 2 40 turns, 70 minutes
effort_turns: 85
effort_minutes: 145
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

## Iteration 2: delta verification on TS-012 revision 2 (2026-09-27, HEAD `eca24fa`)

**Scope.** Iteration 2 verifies the fixes of finding-1 to finding-3 (Major) and, because the author answered them in the same revision, finding-4 to finding-11 (Minor). The brief also asks for a re-add of every roll-up, the section 10 cost basis, at least ten price and stock spot checks (every changed line and the new PA, TCXO and prescaler first), the scoring and ranking arithmetic, and the listed-against-estimated presentation. New findings are raised where the revision itself introduced the defect (PDR work plan rule C1).

**Product.** `docs/decisions/trade-studies/TS-012-design-to-cost-hand-built.md` blob `7432bba4` at commit `eca24fa` (revision 2, Status Proposed, 874 lines). `git rev-parse HEAD:<path>` and `git hash-object <path>` both give `7432bba4`; HEAD is `eca24fa` on `main`. No product blob is on a `cr/` branch. Checklist as iteration 1: `peer-review-checklist-risk.md` revision A, section B.

**Independence (rule C4).** This invocation authored no part of TS-012 revision 1 or 2, its architecture, judge or adversarial reports, and edited no product file. It changed only this record.

**Search first (charter section 11 rule 1; rule C3).** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (queries: the TS-012 record and rule C1; the PDR work plan rule C1 text). `grep` then only pinned lines in known paths (the plan, `tools/validate_docs.py`, the status note).

**Owner direction applied (status note section 10, governs cost).** Target USD 200 for the first complete radio; USD 300 is the absolute maximum and the worst case including contingency stays at or below it; sales tax is excluded. Owned and not bought: 24 AWG magnet wire, a 2 m antenna with an SMA-male plug, through-hole resistors and capacitors (surface-mount passives are not owned), a USB power adapter. Assumed until answered: 18650 cells and a charger are not owned (priced); test instruments are outside the cap. Section 8 parts rule unchanged.

### Verification of the Major findings, case by case

| Case | Required by the iteration 1 fix | Revision 2 text | Result |
|---|---|---|---|
| finding-1 (a) | EOL stated in sections 1, 7.2, 8.6 | Section 1 finding 1 ("The revision-1 PA device is End of Life"); 4.1 A4 M2 cell ("End of Life, stock Mouser 72 and Newark 1,519"); 7.1 A4 EOL risk; 7.2 A4 ("the device is End of Life"); 8.2 U1. Section 8.6 now lists A5 parts, where the AFT05 is absent | Verified. Reviewer re-read today: Mouser 72 at 4.62, Newark 1,519 at 4.21, DigiKey 0 (row S17 below) |
| finding-1 (b) | A4 EOL risk in the four-part format, linked to RSK-038 | 7.1 row "Given that the AFT05MS004N is End of Life with finite stock ... 2 (spare in the order) / 4 / 8 Yellow / merged into RSK-038" | Verified |
| finding-1 (c) | Spare AFT05 in the baseline or a reason | Section 8.4 A4: "Mouser 83.79 with two AFT05MS004NT1"; section 9 finding-1 "+4.62". Reviewer re-add of the A4 Mouser subtotal from the A5 rows reproduces 83.79 (table "Roll-up re-add" below) | Verified |
| finding-1 (d) | Fallback named and fitted to the cap | The fallback (RA07M1317M) is now the A5 baseline, and the worst case of 294.51 includes it; G6 names the reverse fallback to the AFT05 | Verified |
| finding-1 (e) | 70 cm benefit removed or qualified | 7.2 A4 "Its 136 to 941 MHz range is not claimed as a later 70 cm benefit"; D15 lists 70 cm as a descope | Verified |
| finding-2 | Sales tax line, or the owner's answer recorded | Owner, status note section 10: "I'm okay with not counting sales tax." Section 8.3 carries "Sales tax 0 0, Excluded by the owner"; M1 and the section 2 reading exclude it; the gate reads no tax | Verified (closed by owner direction) |
| finding-3 | A prescaler with a published toggle rating above 148 MHz with margin, in a hand-solderable package, with listed price and stock; 7.1 corrected; M4 conditional until the datasheet is read | Three Nexperia 74LVC1G80GV as /2 stages (/8, 18.0 to 18.5 MHz into the RP2350 PWM edge counter). Reviewer read of the datasheet (Rev. 17, 12 November 2024, Table 8): fmax minimum 160 MHz at VCC 3.0 to 3.6 V in both the -40 to +85 C and -40 to +125 C columns; tW minimum 2.5 ns against a 3.38 ns half-period at 148 MHz; SOT753 (SC-74A). Mouser 0.15, 12,379 (row S5). The datasheet was read, so M4 no longer needs the conditional mark. The SN74LVC74A row is gone from 7.1; section 1 finding 2 records the revision-1 error | Verified. Margin 8 % on fmax (160 against 148 MHz); the input-swing budget is observation O-5 |

### Minor findings 4 to 11

| Finding | Revision 2 answer | Result |
|---|---|---|
| finding-4 | Row 22 AO3400A 0.52 at 303,947 (Mouser); row 14 1N5711W 0.307 at 3,033; the correction row is gone; 8.2 "+0.86, +0.27" (2 x 0.43 and 4 x 0.067 reproduce) | Verified |
| finding-5 | 8.3 duty line "About 35%~92.5%", base not published; low and planning on the board value, worst at 92.5 % of boards plus high shipping (0.925 x 29.00 = 26.83, reproduced); gate item (3) reads the base | Verified. FAQ re-read today (row S22) |
| finding-6 | 8.6 restates each reason: J310 on cost (4 x 0.23 against 4 x 5.83), 1N5711W on the single order and short leads (DO-35 at Future named), AO3400A on its datasheet trip window, the divider on its rating | Verified. The AO3400A cell says a through-hole N-FET "was not searched", which is an honest basis. The package chosen is SC-74A, not SOIC; it is inside the owner's hand-solder list (observation O-4) |
| finding-7 | 8.10 rows REQ-SYS-066, 085, 163, REQ-SW-KEYER-014, 023, 032; 8.7 ALT-hold path for REQ-SYS-163 and the MENU+ALT guest lock; S-8252AAO values sourced to Rev.4.0_00 Table 2 | Verified. Reviewer read of Table 2: S-8252AAO-M6T1U VCU 4.250, VCL 4.100, VDL 2.500, VDU 3.000, VDIOV 0.200 V. One tolerance claim is new finding-15 |
| finding-8 | 7.3 drain-feed budget (0.26 to 0.45 ohm, 0.52 to 0.90 V at 2.0 A, sum re-added); A5 3.97 to 4.57 W at the SMA (5.3 W x (5.5/6.0)^2 to (5.9/6.0)^2, minus 0.5 dB, reproduced); A4 delta required; pass criterion 0.35 ohm before the order | Verified |
| finding-9 | Monitor port CONSMA001-C-G in the baseline (row 18); EX-13 needs no pad; section 1 states instruments outside the cap; AB1 removed | Verified |
| finding-10 | Row 31 Wakefield 120-SA (4 g, 5.44); row E4 knobs 0 to 4.00 (E) | Verified |
| finding-11 | C8 Low; sink taken at 3.4 K/W (+30 %); gate item 7 reads the drawing (flat centre-channel face at least 30 x 10 mm, mass); larger-sink fallback named, not priced ("no listed part found") | Fixed in part. The priced fallback asked for is still missing. The Mouser description read today is "63.5x18.29x3.17mm", which Farnell and element14 give as 41.91 x 63.5 x 25.4 mm. The profile and the flange face therefore stay unconfirmed until the gate item 7 read. Stays Open as a lien |

### Roll-up re-add (revision 2)

Reviewer script (scratchpad): every Mouser line equals quantity times unit (31 of 31). The rows sum to 84.306, shown as **84.31**.

| Quantity | TS-012 | Reviewer | Result |
|---|---|---|---|
| Mouser listed subtotal (rows 1 to 31) | 84.31 | 84.31 | Reproduced |
| Estimated rows E1 to E4, low / mid / high | 6.58 / 13.83 / 21.08 | 6.58 / 13.83 / 21.08 | Reproduced |
| Mouser merchandise | 90.89 to 105.39 | 90.89 to 105.39 | Reproduced |
| Listed parts (84.31 + 28.91 + 11.98 + 4.99 + 4.00) | 134.19 | 134.19 | Reproduced |
| Shipping, low / mid / high (5+10+5+12; 8+18+8+25) | 32.00 / 45.50 / 59.00 | 32.00 / 45.50 / 59.00 | Reproduced |
| Board duty, low / planning / worst | 1.40 / 2.55 / 26.83 | 1.40 / 2.55 / 26.825 | Reproduced |
| Tariff pass-through | 4.00 / 8.00 / 15.00 | same | Reproduced |
| A5 subtotal | 178.17 / 204.07 / 256.10 | 178.17 / 204.07 / 256.10 | Reproduced |
| A5 capped (x 1.15) | 204.89 / 234.68 / 294.51 | 204.8955 / 234.6805 / 294.515 | Reproduced to the cent, with the low and worst values rounded down (observation O-1) |
| A5 margin to USD 300 | 5.49 | 5.485 | Reproduced (5.48 or 5.49 by rounding) |
| A4 Mouser (84.31 - GVA 2.99 - TCXO 3.61 - cores 1.76 - 4 x 1N5711W 1.228 + MMBFJ310 0.23 - DMP3099L 0.40 + 2 x AFT05 9.24) | 83.79 | 83.792 | Reproduced |
| A4 listed / subtotals / capped | 104.76; 140.74 / 163.14 / 211.67; 161.85 / 187.61 / 243.42 | 104.76; 140.74 / 163.14 / 211.67; 161.851 / 187.611 / 243.4205 | Reproduced |
| A5 minus A4, planning capped | 47.07 | 234.68 - 187.61 = 47.07; (204.07 - 163.14) x 1.15 = 47.07 | Reproduced |
| U1 (28.91 + 14.00 + 0.40 - 9.24 - 2.00) x 1.15; U2 3.61 x 1.15; U4 2.99 x 1.15; U3 2.60 (pre 2.26, the JFET bias parts about 0.50) | 36.88; 4.15; 3.44; 2.60 | 36.88; 4.15; 3.44; 2.60 (U3 bias-part credit not itemised) | Reproduced |
| A1 re-roll: 193.85 - 15.17 - 5.18 - 4.03 + 0.86 | 170.33 | 170.33 | Reproduced |
| A2 re-roll: 202.67 - 14.28 - 5.18 - 4.03 + 0.86 | 180.04 | 180.04 | Reproduced |
| A1, A2 worst: about 214 and 225, minus wire, plug 6.90 and passives 1.73, plus (24.43 duty + 3.00 tariff) x 1.15 = 31.54 | 221.74; 233.63 | 221.74; 233.63 | Reproduced (the base values are "about" figures; Low, as stated) |
| A3 common basis: 234.68 - 6.62 (+ 11.50); worst 294.51 - 6.62 (+ 23.00) | 228.06 to 239.56; 287.89 to 310.89 | same | Reproduced |
| Guards and add-backs: G1 8.00 x 1.15; G2 6.50 x 1.15; G3 2.00 x 1.15; AB-A 28.91 x 1.15; AB-B 2.00 x 1.15; spare module worst 294.51 + 33.25 | 9.20; 7.48; 2.30; 33.25; 2.30; about 327.8 | 9.20; 7.475; 2.30; 33.25; 2.30; 327.76 | Reproduced |

### Owned items and sales tax (status note section 10)

| Item | Section 10 | Revision 2 | Result |
|---|---|---|---|
| 24 AWG magnet wire | Owned | No wire row; BPF air coils and the BN-43-202 trifilar windings from owned wire (8.1, 8.3 owner-stock row, EX-8); gate item 9 checks about 3 m | Handled |
| 2 m antenna, SMA-male plug | Owned | No antenna row; REQ-SYS-172 delta; EX-9 confirms the mate with the radio's SMA female | Handled |
| Through-hole R and C | Owned | Not bought; row E2 buys the SMD passives (about 22 values) and 0 to 3.00 for assortment gaps | Handled |
| Surface-mount passives | Not owned | Bought (E1, E2, row 4) | Handled |
| USB power adapter | Owned | Powers the MC1; gate item 9 checks 5 V, 1 A | Handled |
| 18650 cells and charger | Assumed not owned | Priced: P28A x 2, 11.98; MC1, 4.99 (both L); Q2 asks the owner | Handled |
| Test instruments | Assumed outside the cap | EX-13, Q4 | Handled |
| Sales tax | Excluded | Line at 0; M1 excludes it | Handled |

### Price, stock and datasheet spot checks (retrieved 2026-09-27; nothing logged into, no form, no cart, no file download beyond the datasheet PDFs the web-fetch tool cached)

| # | Item (TS-012 row) | TS-012 claim | Read today | Kind | Source | Result |
|---|---|---|---|---|---|---|
| S1 | RA07M1317M-501, RF Parts (other sellers, new PA) | 28.91 (27.46 at 10), "In Stock", "New", USD 15 minimum, no EOL note | "$28.91", 10 for "$27.46", "In Stock", New, "Fifteen ($15.00), all inclusive", no EOL or discontinued note | L | https://www.rfparts.com/ra07m1317m.html | Verified |
| S2 | RA07M1317M status, Mitsubishi Electric US | "Active" | Supply status "Active"; distributors Mitsubishi Electric US, Telepro, Diamond Advanced Components (no Mouser, as EX-3 says) | L | https://meus-semiconductors.com/products/high-frequency-devices/ra07m1317m | Verified |
| S3 | RA07M1317M datasheet (Jun. 2019) | Pin 20 mW; efficiency 45 % minimum at 6 W, 7.2 V; 2fo -25, 3fo -30 dBc maximum; stability at VDD 4.0 to 9.2 V, Pin 10 to 30 mW, Pout up to 8 W, VSWR 4:1; 20:1 at 9.2 V and 7 W; Rth(ch-case) 4.5 and 2.4 K/W; "designed for manual soldering"; case 90 C | All present as stated. Absolute maxima: VGG 4 V under the condition VDD 7.2 V or less and Pin 20 mW; Pout 10 W under the condition VGG 3.5 V or less; IDD 3 A; Pin 30 mW; Tcase(OP) -30 to +110 C. The 90 C figure is the long-term-reliability guidance | L (datasheet) | https://www.mitsubishielectric.com/semiconductors/hf/products/datasheet/ra07m1317m.pdf | Verified; the rating conditions are finding-14 |
| S4 | TG2520SMN 25.000M-MCGNNM3 (row 29, new TCXO) | Mouser 3.61, 1,810 | Mouser 3.61, 1,810 (3.14 at 10) | A | https://www.oemstrade.com/search/TG2520SMN | Verified (the +/-0.5 ppm grade was not read by the reviewer) |
| S5 | 74LVC1G80GV,125 (row 28, new prescaler) | Mouser 0.15, 12,379; DigiKey 16,398; Newark 1,812 | Mouser 0.15, 12,379; DigiKey 0.15, 16,398; Newark 0.176, 1,812 | A | https://www.oemstrade.com/search/74LVC1G80GV | Verified |
| S6 | 74LVC1G80 datasheet Rev. 17 | fmax 160 MHz minimum at 3.0 to 3.6 V, -40 to +125 C; tW 2.5 ns; SC-74A | Table 8: fmax min 160 MHz (typ 350) at 3.0 to 3.6 V in both temperature columns; tW min 2.5 ns; tpd max 5.0 ns (85 C) and 6.5 ns (125 C); tsu min 1.3 ns; SOT753 (SC-74A) | L (datasheet) | https://assets.nexperia.com/documents/data-sheet/74LVC1G80.pdf | Verified |
| S7 | Fair-Rite 2843000202 (row 30, new) | 0.88, 47,515 | Mouser 0.88, 47,515 | A | https://www.oemstrade.com/search/2843000202 | Verified |
| S8 | Wakefield-Vette 120-SA (row 31, new) | 5.44, 1,532, 4 g | Mouser 5.44, 1,532, "4 Gram Plastic Pak" | A | https://www.oemstrade.com/search/120-SA | Verified |
| S9 | TE CONSMA001-C-G (row 18, new) | 2.80, 4,598 | Mouser 2.80, 4,598 | A | https://www.oemstrade.com/search/CONSMA001-C-G | Verified |
| S10 | KEMET C0805C101J5GACTU (row E2 basis, new) | 0.12 at 1, 0.049 at 10, 503,544 | Mouser 0.12, 0.049, 503,544 | A | https://www.oemstrade.com/search/C0805C101J5GACTU | Verified |
| S11 | Mini-Circuits TC1-1T+ (A3 M2) | 0 stock at Mouser and DigiKey, 3.68 | DigiKey TC1-1T+ 0 at 3.68. The aggregator's Mouser row is TC1-1T-75X+ (355 at 3.35), which the Mini-Circuits datasheet title gives as a 75 ohm, 5 to 120 MHz transformer, a different part. No exact TC1-1T+ Mouser row was shown | A | https://www.oemstrade.com/search/TC1-1T+ ; https://www.minicircuits.com/pdfs/TC1-1T-75X+.pdf (search result title) | DigiKey verified; Mouser partly verified (observation O-3) |
| S12 | XTAR MC2 (AB-B) | 6.99, "Sold out" | 6.99, "Sold out" | L | https://www.18650batterystore.com/products/xtar-mc2 | Verified |
| S13 | Omron B3F-1052 (row 15, now 2) | 0.39, 9,504 | Mouser 0.39, 9,504 | A | https://www.oemstrade.com/search/B3F-1052 | Verified |
| S14 | Coilcraft 1812SMS-82NJLC (row 5, stock 79 not re-read at iteration 1) | 1.90, 79 | Mouser 1.90, 79; Coilcraft direct 1.01, 8,402 | A | https://www.oemstrade.com/search/1812SMS-82NJLC | Verified (2 needed) |
| S15 | Boyd 530002B02500G (row 3) | 3.39, 3,693; 63.5 x 41.9 x 25.4 mm | Mouser 3.39, 3,693; Mouser description "63.5x18.29x3.17mm"; Farnell and element14 titles 41.91 x 63.5 x 25.4 mm | A | https://www.oemstrade.com/search/530002B02500G ; https://uk.farnell.com/aavid-thermalloy/530002b02500g/heat-sink-2-6k-w-to-220/dp/2295719 | Price verified; profile still unread (finding-11) |
| S16 | KEMET C1206C220J1GACTU (row 4) | 0.29, 3,978 | Mouser 0.29, 3,978 | A | https://www.oemstrade.com/search/C1206C220J1GACTU | Verified |
| S17 | AFT05MS004NT1 (A4, two now) | Mouser 72; Newark 1,519 | Mouser 4.62, 72; Newark 4.21, 1,519; DigiKey 4.15, 0 | A | https://www.oemstrade.com/search/AFT05MS004NT1 | Verified |
| S18 | TE/Linx CONSMA003.062-G (row 17, not re-read at iteration 1) | 4.47, 2,641 | Mouser 4.47, 2,641 | A | https://www.oemstrade.com/search/CONSMA003.062 | Verified |
| S19 | Adafruit 2045 at Mouser (row 9) | 485-2045, 7.95, 242 | 7.95, 242 | A | https://www.oemstrade.com/search/485-2045 | Verified |
| S20 | AO3400A datasheet Rev 3.1 (8.6, 8.10 REQ-SYS-085) | 18 / 26.5 mohm at VGS 10 V; 28 / 38 at 125 C; 19 / 32 at 4.5 V | Same; VGS rating +/-12 V; "Rev 3.1: July 2023" | L (datasheet) | https://www.aosmd.com/res/datasheets/AO3400A.pdf | Verified |
| S21 | ABLIC S-8252 Rev.4.0_00 (row 21, 8.10 REQ-SYS-083 to 085) | VCU 4.250 V +/-25 mV (-10 to +60 C); VDL 2.500 V +/-0.050 V; VDIOV 0.200 V +/-10 mV | Table 2 values as stated; VCU +/-25 mV at -10 to +60 C; VDIOV +/-10 mV at 25 C and at -40 to +85 C; **VDL +/-50 mV at Ta = +25 C only, -85 / +60 mV at -40 to +85 C** | L (datasheet) | https://www.ablic.com/en/doc/datasheet/battery_protection/S8252_E.pdf | Verified except the VDL tolerance claim (finding-15) |
| S22 | JLCPCB US tariff FAQ (duty line) | "About 35%~92.5%", base unpublished | Same; the page does not state the base | L | https://jlcpcb.com/help/article/us-tariff-policy-faq | Verified |
| S23 | RF Parts shipping (other sellers) | Calculated; USD 2.75 residential UPS surcharge (search summary) | "$2.75 per package delivered to a residential destination"; USD 15 minimum; carrier-calculated rates, no table | L (page) for the surcharge; E for the 10 to 18 carriage | https://www.rfparts.com/customerservice-shipping | Surcharge verified by a direct read; carriage not verifiable without a cart |

Totals: 23 checks. 20 are verified. 3 are verified in part: S11 (the Mouser row is a different part), S15 (profile) and S21 (VDL tolerance). Not verifiable without a cart: the Mouser free-shipping threshold and tariff line, the RF Parts carriage, the 18650BatteryStore shipping (unchanged from iteration 1 rows 22 to 24). The study carries all four as E, with the owner's gate read.

### Scoring and ranking arithmetic

- **Matrix totals** (section 5), re-computed: A1 295, A2 325, A3 320, A4 340, A5 355. Every row of weight times score reproduces, and the weights sum to 100.
- **Interpolated cost scores**, re-computed from the anchors:

  | Criterion | A1 | A2 | A3 | A4 | A5 |
  |---|---|---|---|---|---|
  | C1 | 5 | 5 | 3.42 (3) | 5 | 3.61 (4) |
  | C2 | 4.91 (5) | 4.32 (4) | 1 at 310.89 | 3.83 (4) | 1.28 (1) |

  All match. For A3, C1 uses the planning basis with the LCSC-shipping midpoint, and C2 uses the LCSC-separate worst case. That is consistent with the M1 definition.
- **Weight sensitivity** (16 runs, others rescaled to 100), re-computed. Every figure in section 6 item 1 reproduces:
  - A4 first at C2 +10 (346.3 against 328.2), C3 +10 (358.8 against 348.5) and C5 -10 (357.5 against 336.9);
  - A5 and A2 tie at 350.0 at C4 -10;
  - A5's smallest winning lead is 0.6 (C1 +10, 360.6 against 360.0).
- **Low-cell moves**, re-computed:
  - A4 C5 +1 gives 360; A4 C8 +1 ties at 355; A5 C1 -1 gives 335 against 340; A5 C8 -1 ties at 340;
  - the joint adverse case gives A4 380, A3 360, A2 355, A5 310.

  All reproduce.
- **Anchors.** C3, C4, C5, C6 and C8 scores are consistent with their anchors. C7 for A5 is not (finding-13).
- **Robustness verdict** "Not robust" between A5 and A4 is correct and stated in section 1, section 6 item 4, section 8 and Q1. Rule 14.5 is met: the closely ranked A4 is named with the condition under which it is the right choice.

### Estimate against listed-price presentation (revision 2)

Nothing estimated is shown as a listed price:
- Rows E1 to E4 are marked "est." with their bases.
- Every shipping, duty and tariff line carries its kind. The duty percentage is L from the FAQ; the base and the dollar values are derived.
- The U1 cost uses the "RF Parts shipping 14.00 midpoint", labelled as such.
- Section 1 labels 234.68 "planning" and 294.51 "worst case", with the estimated lines named.
- Row 11 shows the quantity-10 price (0.532) under "Unit (qty 1)" with "(0.61 at 1)" beside it. Ten are bought, so the line total is right.
- The JLCPCB board line stays a listed floor with the owner check (as accepted at iteration 1).

### Findings (iteration 2)

| Finding | Severity | Item | Location | Description | State | Deferred to |
|---|---|---|---|---|---|---|
| finding-1 | Major | CK-RSK-B5, B8 | TS-012 sections 1, 4.1, 7.1, 7.2, 8.4 | See iteration 1; cases (a) to (e) above | Verified (iteration 2, revision 2 at eca24fa) | |
| finding-2 | Major | CK-RSK-B5, B7 | TS-012 sections 2, 3.1 M1, 8.3 | See iteration 1; closed by the owner's section 10 answer | Verified (iteration 2, revision 2 at eca24fa) | |
| finding-3 | Major | CK-RSK-B5, B8 | TS-012 sections 1, 4.1 M4, 8.1, 8.3 row 28, 8.10 REQ-SYS-182 | See iteration 1; 74LVC1G80GV datasheet read by the reviewer | Verified (iteration 2, revision 2 at eca24fa) | |
| finding-4 | Minor | CK-RSK-B5 | TS-012 section 8.3 rows 14, 22 | See iteration 1 | Verified (iteration 2) | |
| finding-5 | Minor | CK-RSK-B5 | TS-012 section 8.3 duty line, 8.4 gate | See iteration 1 | Verified (iteration 2) | |
| finding-6 | Minor | CK-RSK-B4, B5 | TS-012 section 8.6 | See iteration 1 | Verified (iteration 2) | |
| finding-7 | Minor | CK-RSK-B5 | TS-012 sections 8.7, 8.10 | See iteration 1 | Verified (iteration 2) | |
| finding-8 | Minor | CK-RSK-B5 | TS-012 sections 7.3, 8.10 REQ-SYS-012 | See iteration 1 | Verified (iteration 2) | |
| finding-9 | Minor | CK-RSK-B5 | TS-012 sections 1, 8.3 row 18, 8.9 EX-13 | See iteration 1 | Verified (iteration 2) | |
| finding-10 | Minor | CK-RSK-B5 | TS-012 section 8.3 rows 31, E4 | See iteration 1 | Verified (iteration 2) | |
| finding-11 | Minor | CK-RSK-B5 | TS-012 sections 4.2 C8-A5, 7.3, 8.11 item 7 | Fixed in part: C8 is Low and the sink is derated, but the larger-sink fallback is still unpriced and the profile unread (Mouser "63.5x18.29x3.17mm" against the distributors' 41.91 x 63.5 x 25.4 mm) | Open | CDR readiness declaration (lien, rule C1); the gate item 7 read closes it earlier |
| <a id="finding-12"></a>finding-12 | Minor | CK-RSK-B8, B9 | TS-012 sections 1 (risk-per-dollar bullet), 6 item 4, 8 rationale, 8.2 upgrade table, 8.13 Q1 | The risk bought per dollar in section 8.2 does not agree with the section 7.1 risk scores, and the owner-facing text overstates it. (a) U1 counts "EOL PA 12 -> 8", but section 7.1 scores the A4 EOL risk 8 (Yellow, spare in the order), so the change is 0. (b) U1 counts "no harmonic data 16 -> 8" and "match rebuilt on another substrate 12 -> 0" separately, but section 7.1 has one A4 risk for both ("Given no AFT05 harmonic data and a match re-derived for a different substrate", 16), so it is counted twice. (c) U3 counts "unvalidated JFET mixer 12 -> 8", but the A5 receiver risk in 7.1 is still 12 (Red, MDS). (d) The A5 non-harmonic-spur Red (12) comes from about 45 dB of gain on an unshielded board, which A4's GVA-84+ and AFT05 line-up also has; it is not listed for A4. On the 7.1 scores, U1 retires 8 + 8 + 6 - 9 = 13 points (USD 2.84 per point, not 1.27), and A4 to A5 retires about 27 to 30 points (about USD 1.6 per point, not 0.94). The module retires three A4 Reds (harmonic data and match, junction bound, low-pack power), not "five Red risks". The EOL risk is Yellow in A4. The direction of the argument holds, and the matrix does not use these points, so the ranking is unchanged. But section 6 item 4 makes this trade the single question put to the owner. **Fix:** reconcile 8.2 with 7.1 (one score per risk, the same before-and-after values); add the spur risk to A4 or give the reason it differs; correct the "five Red risks" wording in sections 1 and 8 and in Q1 | Open | CDR readiness declaration (lien, rule C1); recommended before the owner is asked at B1a (cross item X-6) |
| <a id="finding-13"></a>finding-13 | Minor | CK-RSK-B6 | TS-012 section 4.2 C7-A5 (score 4), section 5 | The C7 anchors are "5: wording-only deltas, no firmware added" and "3: deltas recorded including KDR relaxations, moderate firmware". A5 records relaxations of four of the KDRs the header names: REQ-SYS-102 (to 360 g TBR), 103 (to 148 x 70 x 42 mm), 137 (retired) and 140 (RF Parts added). It also relaxes REQ-SYS-031 (85 to 78 dB), 029, 083, 106 and 109. It adds the Morse menu, adaptive decoder and envelope-loop firmware (8.7). By the anchors this is a 3, as for A4; the evidence cell names only 010, 012 and 141 as kept. At 3, A5 totals 350 and stays first by 10. But one Low-cell move (A4 C8 +1, 355 against 350) then puts A4 first instead of tying, and the robustness statement changes. **Fix:** score C7-A5 3, or state the anchor evidence for 4; re-run the section 6 sensitivity and restate it | Open | CDR readiness declaration (lien, rule C1) |
| <a id="finding-14"></a>finding-14 | Minor | CK-RSK-B5 (M4 "inside their published ratings") | TS-012 section 7.3 drive gating ("VGG is bounded at 3.8 V ... under the 4 V rating") and the "At 8.4 V the module can make about 10.5 W" line; 8.1; 8.10 REQ-SYS-055 row | Datasheet (row S3): the 4 V VGG maximum holds under the condition VDD 7.2 V or less; the 10 W Pout maximum holds under VGG 3.5 V or less; the stability guarantee holds for Pout up to 8 W. The design lets VGG reach 3.83 V at VDD up to 8.4 V. By the study's own figure, a single fault of the envelope loop (open detector, or the error amplifier at its rail) gives about 10.5 W at a full pack. That is above the 10 W maximum, outside the Pout range of the stability guarantee, and near the 3 A IDD maximum (about 2.8 A at 45 % efficiency). The 10 s cutoff bounds the time, but not the level. The fix costs nothing, and 5 W at 6.4 V does not need VGG above 3.5 V (datasheet: nominal output at 3 V typical, 3.5 V maximum). **Fix:** clamp VGG at 3.5 V or less at the LM2940 maximum (for example a 0.68 divider, 5.1 x 0.68 = 3.47 V), or bound Pout at the clamp at 8.4 V against 8 W. Add the open-loop ALC case to the WP-PDR-22 pass criteria, and correct the "under the 4 V rating" wording | Open | CDR readiness declaration (lien, rule C1); recommended before the WP-PDR-22 run |
| <a id="finding-15"></a>finding-15 | Minor | CK-RSK-B5 | TS-012 section 8.10 REQ-SYS-084 ("S-8252AAO VDL 2.500 V +/-0.050 V matches exactly") | The S-8252 datasheet (Rev.4.0_00, row S21) gives VDL +/-0.050 V at Ta = +25 C only and -0.085 / +0.060 V over -40 to +85 C. REQ-SYS-084 has no temperature qualifier, so it applies over the operating range (the study uses -10 to +45 C for REQ-SYS-010). The datasheet gives no tighter VDL band for that range, so "matches exactly" holds only at 25 C. This is the HZ-007 K1 control. **Fix:** state the tolerance over the operating range and either propose a TBR band (for example 2.415 to 2.560 V) or record REQ-SYS-084 as at risk, as done for REQ-SYS-083 | Open | CDR readiness declaration (lien, rule C1) |
| <a id="finding-16"></a>finding-16 | Minor | CK-RSK-B5, B7 | TS-012 section 8.4 ordering gate ("15 % contingency on the remaining estimates") against section 3.1 M1 ("all times 1.15") and the section 2 item 1 reading ("the worst case including 15 % contingency stays at or below it") | The gate re-computes the worst case with contingency on the remaining estimates only, so the verified listed parts (134.19 at planning) lose their 1.15. That is up to about USD 20 looser than the M1 test the owner is shown, and the A5 margin under M1 is 5.49. Either basis can be right: contingency on verified prices may be unnecessary, but it also covers build-time growth such as a blown module or re-ordered parts. The study applies two bases without saying which one governs the "absolute maximum". **Fix:** state which basis the gate applies to the USD 300 test and why. If contingency is dropped on verified lines, say what covers build-time losses (AB-A, D12) and put the change to the owner with Q1 | Open | CDR readiness declaration (lien, rule C1) |

None of the new findings is Major. Finding-12 corrects the size of the risk-per-dollar case, but every Red that the module retires in section 7.1 is still retired, so its direction holds. Finding-13 lowers A5's total to 350, and A5 stays first. Finding-14 is a zero-cost clamp change inside a pre-order LTspice check. Finding-15 is a tolerance statement. Finding-16 is a basis statement at a gate that comes after the owner's decision. The owner would not choose between A5 and A4 on a wrong basis because of any of them.

### Observations (not findings)

- **O-1.** Rounding. The low and worst totals are rounded down: 204.8955 is shown as 204.89 and 294.515 as 294.51, while the planning 234.6805 is shown as 234.68. The margin reads 5.49, and 5.48 under half-up rounding. The convention should be stated once, because the worst-case margin is quoted to the cent.
- **O-2.** Section 6 item 3 says "INSP-110 re-read 25 more rows". The iteration 1 table had 25 entries, of which 21 were price or stock reads and 4 were page checks.
- **O-3.** A3's M2 "fail as submitted": DigiKey 0 is confirmed. The aggregator's Mouser row today is a different 75 ohm part (row S11). The fail holds on the DigiKey read and on the absence of an exact Mouser row.
- **O-4.** Section 9 finding-3 calls SC-74A at 0.95 mm pitch "easier than SOIC". SOIC is 1.27 mm. Both are on the owner's hand-solder list, so only the wording is wrong.
- **O-5.** Divider input swing. CLK1 is loaded by the drive LPF and pad, so it swings about 1.65 Vpp (7.3). AC-coupled through 100 pF and biased, the 74LVC1G80 input at 3.3 V needs VIL 0.8 V and VIH 2.0 V to be crossed. That leaves about 0.45 V of total margin, set by the bias point. This is for the WP-PDR-21 drive-chain run, not for the decision.
- **O-6.** Header row "Independent reviewer" says iteration 1 ran "on revision 1 at 5c16930". The change log (and this record at iteration 1) calls that text revision 0. The change log row for revision 2 explains the numbering, so this is naming only.

### Readiness (iteration 2)

| # | Criterion | Result | Evidence |
|---|---|---|---|
| R1 | `validate_docs.py` exits 0 | **No** | `validate_docs: 99 passed, 10 failed, 109 checked`, exit 1, at `eca24fa` before this delta. After this delta, the same 10 failing records remain (other records' drift: CM plan SA, configuration status, lessons learned, TV-015 to 019, TS-004, ADRs 001 to 025, process 02, TV-001 to 010, TS-001 and TS-002, TS-002 SA). This record passes (Commands) |
| R2 | Section A | N/A | Trade study |
| R3 | Sections 1 to 9 filled; section 10 empty | Yes | Section 10 fields empty; "Left empty until the owner decides" |
| R4 | Decision need and gate | Yes | Header "Decide by": B1a 2026-09-29, no later than B1b 2026-10-01 |

### B. Trade study items re-answered (iteration 2)

| Id | Answer | Evidence |
|---|---|---|
| CK-RSK-B5 | Yes (liens) | The evidence behind M1, M2 and M4 is now read and reproduced (roll-up re-add, rows S1 to S23). Minor evidence liens: finding-11, finding-14, finding-15 and finding-16 |
| CK-RSK-B6 | Yes (lien) | Totals and interpolation reproduce; C7-A5 anchor (finding-13) |
| CK-RSK-B7 | Yes | Section 6 re-computed: weights (16 runs), Low cells, joint case, verdict "Not robust", value of information (gate reads, LTspice runs), limitations. The cost screen names its Low worst case |
| CK-RSK-B8 | Yes (lien) | Four-part risks for A2 to A5, including the A4 EOL risk and the A5 heat, spur, MDS and cost-margin risks; consistency with 8.2 is finding-12 |
| CK-RSK-B9 | Yes | A5 has the highest total among the alternatives that pass every mandatory criterion (A3 is conditional at M1 and M2). A4 is named as the closely ranked alternative |
| CK-RSK-B1 to B4, B10 | Yes | As iteration 1. B4: A5 is added and seven pruned alternatives have reasons, including in-radio charging and the spare module. B10: section 9 lists the INSP-110 dispositions, the adversarial dispositions and the panel dissent; section 10 is empty |

### Cross items (iteration 2, returned to Claude)

- **X-5.** The software assurance pair (X-2) is still not dispatched. The record verdict waits for it.
- **X-6.** Rule C1 makes findings 12 to 16 liens due at the CDR readiness declaration. Two of them should be fixed before B1a, though C1 does not require it: finding-12 is in the owner-facing text of Q1 and section 1, and finding-14 is in the design the owner is asked to adopt. A revision that fixes them changes the product blob and needs a delta iteration of this record (rule C2).
- **X-7.** X-1 is closed: the header names INSP-110 and this path.
- **X-8.** Owner inputs still open, carried by the study as assumptions: cells and charger owned (Q2), instruments outside the cap (Q4). The status note section 10 lists both as unanswered.

### Commands (iteration 2)

```
git rev-parse HEAD                                                                    # eca24fa78457b3de9834df78be0ca33c5bea9ecd
git rev-parse HEAD:docs/decisions/trade-studies/TS-012-design-to-cost-hand-built.md   # 7432bba479c2a4264b317e35b0c7ac48b85370ad
git hash-object docs/decisions/trade-studies/TS-012-design-to-cost-hand-built.md       # 7432bba479c2a4264b317e35b0c7ac48b85370ad
/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/validate_docs.py   # before the delta: 99 passed, 10 failed, 109 checked (exit 1)
python3 (scratchpad) roll-up re-add of 8.3 rows 1 to 31, E1 to E4 and 8.4 for A5 and A4; A1 to A3 re-rolls; upgrade and guard values;
  matrix totals; C1 and C2 interpolation; 16 weight runs; Low-cell moves and the joint case
pdftotext -layout on the web-fetch cached datasheets: 74LVC1G80 Rev. 17 Table 8; RA07M1317M Jun. 2019 ratings, characteristics and
  thermal design; AO3400A Rev 3.1; S-8252 Rev.4.0_00 Table 2 and the electrical characteristics at 25 C and -40 to +85 C
```

### Measurements (iteration 2)

size = 6 alternatives, 13 criteria, 35 A5 BOM rows, 7 shipping, duty and tariff lines, 23 spot checks; turns = 40; minutes = 70; major = 0 new (3 Verified); minor = 5 new (7 Verified, 1 fixed in part).

### Record verdict and verdict format (iteration 2)

`reviewer_verdict: APPROVED`. The three Major findings are Verified, finding-4 to finding-10 are Verified, and no Major is open. finding-11 (fixed in part) and the new Minor findings 12 to 16 are liens due at the CDR readiness declaration (plan rule C1), each with the TS-012 author as owner. The record `verdict` stays NEEDS CHANGES for two reasons: the software assurance pair is not yet filed (07 section 2.1.1; `assurance_verdict: pending`), and readiness R1 fails on records unrelated to TS-012. When the pair returns APPROVED and R1 holds, the lead SE sets `verdict: APPROVED`, provided `git rev-parse HEAD:<path>` still equals `7432bba4`. A changed blob needs a delta iteration (rule C2).

```
VERDICT: APPROVED (reviewer); record verdict held for the software assurance pair and readiness R1
FINDINGS:
- [Major] finding-1 AFT05 end of life: Verified (EOL stated, A4 risk, spare in the A4 baseline, fallback, 70 cm benefit removed).
- [Major] finding-2 sales tax: Verified (closed by owner direction, status note section 10).
- [Major] finding-3 prescaler: Verified (74LVC1G80GV x3, fmax 160 MHz min at 3.0 to 3.6 V, -40 to +125 C, datasheet Rev. 17 read).
- [Minor] finding-4 to finding-10: Verified.
- [Minor] CK-RSK-B5 section 7.3, 8.11 item 7: finding-11 fixed in part; larger-sink fallback unpriced, profile unread (lien).
- [Minor] CK-RSK-B8, B9 section 1, 8.2, Q1: risk per dollar disagrees with 7.1; "five Red risks" is three (finding-12, lien).
- [Minor] CK-RSK-B6 section 4.2: C7-A5 scored 4 against anchors that give 3; A5 350, still first (finding-13, lien).
- [Minor] CK-RSK-B5 section 7.3: VGG clamp 3.83 V at up to 8.4 V; datasheet 4 V is at VDD 7.2 V or less, Pout 10 W at VGG 3.5 V or less (finding-14, lien).
- [Minor] CK-RSK-B5 section 8.10 REQ-SYS-084: S-8252 VDL +/-50 mV is at 25 C only (finding-15, lien).
- [Minor] CK-RSK-B5, B7 section 8.4: gate contingency basis differs from M1 (finding-16, lien).
ITEMS N/A: CK-RSK-A1 to CK-RSK-A11 (product is a trade study)
MEASUREMENTS: size=6 alternatives, 13 criteria, 23 spot checks; turns=40; minutes=70; major=0 new; minor=5 new; verified=10; open=6
```
