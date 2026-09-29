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
# product_commit (iteration 3 re-issue 1, the owner-authorized fourth iteration, 2026-09-28): 37d5824, the TS-012
# revision 5 commit. The blob below equals git rev-parse 37d5824:<path>, HEAD:<path> and git hash-object <path> at
# HEAD 37d5824 on 2026-09-28; it is on main. The same delta read revision 4 (7d0d450, blob fa41032e,
# product_files_revision_4), whose liens answers revision 5 carries. Iteration 3 reviewed d5a3058, blob b1f03fad
# (product_files_iteration_3); iteration 2 reviewed eca24fa, blob 7432bba4 (product_files_iteration_2);
# product_files_iteration_1 keeps the 5c16930 blob reviewed at iteration 1.
# Iteration 3 re-issue 2 (owner-authorized, status note 2026-09-29 section 2; 2026-09-29): 3b93de1, the TS-012
# revision 6 commit (it changes only the TS file). The blob below equals git rev-parse 3b93de1:<path>,
# HEAD:<path> and git hash-object <path> at HEAD 123f048 on 2026-09-29; it is on main. Re-issue 1 reviewed
# revision 5 at 37d5824, blob 731ba0eb (product_files_revision_5).
product_commit: "3b93de11d52c17fa17e7a304656a2e8ff635efce"
product_blob: 0c9fcb9649d3fbf7a1eae3de43d10f05abe1632b
product_files: ["docs/decisions/trade-studies/TS-012-design-to-cost-hand-built.md@0c9fcb9649d3fbf7a1eae3de43d10f05abe1632b"]
product_files_revision_5: ["docs/decisions/trade-studies/TS-012-design-to-cost-hand-built.md@731ba0ebe494c1d970b3b1ba0cac4304ebbab412"]
product_files_revision_4: ["docs/decisions/trade-studies/TS-012-design-to-cost-hand-built.md@fa41032e38fd93cd2eecf84efe74dc74a4103972"]
product_files_iteration_3: ["docs/decisions/trade-studies/TS-012-design-to-cost-hand-built.md@b1f03fad90ad0f7e4a118624792838d495501e56"]
product_files_iteration_2: ["docs/decisions/trade-studies/TS-012-design-to-cost-hand-built.md@7432bba479c2a4264b317e35b0c7ac48b85370ad"]
product_files_iteration_1: ["docs/decisions/trade-studies/TS-012-design-to-cost-hand-built.md@5da2c7c58c8ea759d7bcaa92e2efcb49f16de1bd"]
# product_size (iteration 3 re-issue 2: revision 6, 1248 lines) is the re-issue 1 figure plus: the TCXO required in A4
# (D-17), design items D-17 and D-18, E5 item (g), the A4 + U3 matrix column, sensitivity R6-1 to R6-6, a revision 6
# risk table of 4 rows, table R6-1 and the REQ-SYS-182, 154, 181, 120 and REQ-TX-014 rows restated.
# product_size (iteration 3 re-issue 1: revision 5); iteration 2 was the same without row E5, section 8.14 and tables
# R5-1 to R5-4; iteration 1 was "5 alternatives (A0 dropped at M1; A1 to A4 scored; 5 pruned), 5 mandatory
# and 8 enhancing criteria; BOM of 33 Mouser rows, 5 other-seller rows, 5 shipping and duty lines; about 80 requirement deltas"
product_size: "6 alternatives (A0 dropped at M1, A1 at M4; A2 to A5 ranked; 7 pruned), 5 mandatory and 8 enhancing criteria; A5 BOM of 31 Mouser rows, 4 estimated rows, 4 other-seller rows, 7 shipping, duty and tariff lines; A4 roll-up; 4 upgrades with risk per dollar; about 90 requirement deltas; revision 5 adds estimated row E5, 16 design items (8.14), results of 6 analysis records (tables R5-1 to R5-4) and a revision 5 risk table of 19 rows (14 carried, 8 of them re-scored, and 5 new)"
sprint: PDR-prep
author_agent: "author:TS-012 (Claude as trade-study author, invocation of 2026-09-27)"
reviewer_agent: "reviewer:TS-012-iter1 (independent; authored no part of TS-012, its architecture reports or its judge reports); iteration 2 by reviewer:TS-012-iter2 (independent; authored no part of TS-012 revision 1 or 2); iteration 3 by reviewer:TS-012-iter3 (independent; authored no part of TS-012 revision 1, 2 or 3); iteration 3 re-issue 1 (the owner-authorized fourth iteration) by reviewer:TS-012-iter4 (independent; authored no part of TS-012 revisions 1 to 5, of the six analysis records it cites or of their review records); iteration 3 re-issue 2 (owner-authorized, status note 2026-09-29 section 2) by reviewer:TS-012-iter5 (independent; authored no part of TS-012 revisions 1 to 6, of the analysis records it cites, of frequency-budget.md, or of INSP-117, INSP-118 or iterations 1 to 3 re-issue 1 of this record)"
# criticality: the study decides the hardware controls of REQ-SYS-055, 120, 180, 181, 182 and 092 and the
# Morse menu override command path (safety-critical by SRR decision 9; 07 section 14.1)
criticality: safety-critical
assurance_required: true
# assurance_reviewer_agent and paired_record (iteration 3 re-issue 2; INSP-118 cross item X-1): the pair is filed as INSP-118
assurance_reviewer_agent: "sa-reviewer:TS-012-design-to-cost (software assurance function; paired record INSP-118, docs/reviews/PDR/checklists/ts-012-design-to-cost-software-assurance.md)"
paired_record: INSP-118
# iteration: 3 is the record schema maximum. The owner authorized a fourth iteration (status note 2026-09-28 section 1
# item 3); it is recorded as "Iteration 3 re-issue 1" (precedent INSP-009, INSP-038, INSP-075), and the body calls it
# the fourth iteration. The owner authorized a further iteration on revision 6 (status note 2026-09-29 section 2),
# recorded as "Iteration 3 re-issue 2" (the fifth pass)
iteration: 3
# readiness_met: false at every iteration on R1 only (validate_docs.py exits 1: 10 records unrelated to TS-012 at
# iterations 1 and 2, 8 at iteration 3 and at re-issues 1 and 2; this record passes). R3 and R4 hold on revision 6
readiness_met: false
# reviewer_verdict (iteration 3 re-issue 2, revision 6): APPROVED. finding-1 to 3 (Major) stay Verified; finding-19, 20
# and 23 Verified; finding-21 and 22 stay Open liens; new Minor findings 24 to 26 are Open liens (rule C1). No Major open.
# reviewer_verdict (iteration 3 re-issue 1, revisions 4 and 5): APPROVED. finding-1 to finding-3 (Major) stay Verified;
# finding-14, 17 and 18 Verified (fixed in revision 4, held in revision 5); new Minor findings 19 to 23 are Open, liens
# (PDR work plan rule C1), with finding-19 and finding-20 recommended for the owner-facing Q1 text before B1a.
# Iteration 3 was APPROVED with finding-14, 17, 18 open; iteration 2 APPROVED with finding-11 to 16 open; iteration 1
# NEEDS CHANGES
reviewer_verdict: APPROVED
# assurance_verdict: copied from the paired record INSP-118 (01 section 13; INSP-118 X-1): APPROVED at its iteration 2 on
# revision 6, blob 0c9fcb96 (dd39a64, committed while this delta ran; its iteration 1 at f06690b was NEEDS CHANGES, 3 Major).
# It was "pending" at re-issue 1, before the pair was filed
assurance_verdict: APPROVED
# verdict: held at NEEDS CHANGES only for readiness R1 (validate_docs.py exits 1 on 8 records unrelated to TS-012;
# 07 section 2.1.1; rule C9). Reviewer and assurance verdicts are APPROVED on the same blob 0c9fcb96 (INSP-118 X-7)
verdict: NEEDS CHANGES
findings_major: 3
# findings (iteration 3 re-issue 2): 3 Major and 23 Minor raised in all; open: finding-21, 22, 24, 25, 26;
# verified: finding-1 to 20 and finding-23. Re-issue 1: 20 Minor, open 19 to 23, verified 1 to 18
findings_minor: 23
findings_open: 5
findings_fixed: 0
findings_verified: 21
findings_deferred: 0
deferred_rids: []
# items_no: iteration 1 was [CK-RSK-B5, CK-RSK-B7, CK-RSK-B8]; at iterations 2, 3 and 3 re-issues 1 and 2 every B item is Yes
# (with liens: B5 and B8 at iterations 2 and 3; B5, B7, B8 and B9 at re-issue 1; B5 and B8 at re-issue 2)
items_no: []
# effort: iteration 1 45 turns, 75 minutes; iteration 2 40 turns, 70 minutes; iteration 3 35 turns, 60 minutes;
# iteration 3 re-issue 1 45 turns, 85 minutes; iteration 3 re-issue 2 40 turns, 80 minutes
effort_turns: 205
effort_minutes: 370
record_status: Open
# date: the record's opening date; re-issue 1 is dated 2026-09-28 and re-issue 2 2026-09-29 in their section headings
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

## Iteration 3: delta verification on TS-012 revision 3 (2026-09-27, HEAD `d5a3058`)

**Scope.** Iteration 3 is the delta that rule C2 requires after revision 3 changed the product blob. It verifies the answers to the iteration-2 liens (finding-11 to finding-16) and to the two adversarial refutations of revision 2 that the revision answers (R-1, key-down sequence; R-2, heat inside the case). As the brief asks, it also re-adds every roll-up, confirms the section 10 cost basis, spot-checks prices, stock and datasheet values (the changed lines and the new PA, TCXO and prescaler first), re-computes the scoring and ranking arithmetic and checks the listed-against-estimated presentation. Findings 1 to 10 stay Verified from iteration 2 and are not re-opened. New findings are raised only where revision 3 introduced the defect or left a lien unfixed (PDR work plan rule C1). This is the third iteration, the last one before escalation to the owner under rule C1.

**Product.** `docs/decisions/trade-studies/TS-012-design-to-cost-hand-built.md` blob `b1f03fad` at commit `d5a3058` (revision 3, Status Proposed, 911 lines). `git rev-parse HEAD:<path>` and `git hash-object <path>` both give `b1f03fad`; HEAD is `d5a3058` on `main`, and the commit changes only the TS file. Checklist as before: `peer-review-checklist-risk.md` revision A, section B.

**Independence (rule C4).** This invocation authored no part of TS-012 revision 1, 2 or 3, of its architecture, judge or adversarial reports, or of iteration 1 or 2 of this record. It edited no product file and changed only this record.

**Search first (charter section 11 rule 1; rule C3).** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search, with three queries: the TS-012 record and INSP-110 delta, the 06 section 7 safety override, and the PDR plan rules C1 and C2. After that, `grep` only pinned lines in known paths (`tools/validate_docs.py`, the PDR work plan, the cached datasheet text).

**Owner direction applied.** Status note section 10 governs cost: a USD 200 target and a USD 300 absolute maximum, with the worst case including contingency at or below USD 300. Sales tax is excluded. Owned items: 24 AWG magnet wire, a 2 m antenna with an SMA-male plug, through-hole resistors and capacitors (surface-mount passives are not owned) and a USB power adapter. Status note section 11 (commit `84e7b89`, before `d5a3058`) has since answered the two open assumptions. Cells and charger are not owned, so they are priced. Test equipment sits outside the radio's USD 300 maximum, under a separate USD 300 cap on new equipment. Section 13 records that the owner accredits LTspice (OD-24b). Both answers agree with the assumptions the study carries, so no cost changes; the stale wording is finding-18.

### Verification of the iteration-2 liens and the adversarial answers

| Item | Required | Revision 3 text | Result |
|---|---|---|---|
| finding-11 | Read the drawing, or state a fallback with its cost; C8 Low | Section 7.3: a sink-temperature transmit-duty limit at USD 0, with its requirement cost (a duty-limited REQ-SYS-112 corner, TBR, by CR). The derate is shown to help little (class-B scaling: about 9.5 W at 4 W against 9.95 W at 5 W; reviewer: 1.97 x (4.48/5.6)^0.5 = 1.76 A, 7.9 x 1.76 - 4.48 = 9.44 W). The larger-sink search is recorded with URLs. C8-A5 stays Low. The profile read stays at gate item 7 | Verified. The fallback and its cost are stated, which is the alternative the fix allowed. Wording slip: observation O-8 |
| finding-12 (a) to (d) | Reconcile 8.2 with 7.1; A4 spur Red; "five Red risks" wording | Section 8.2 rebuilt with one 7.1 score per risk. The A4 spur Red (12) and the A4 30 ppm reference Red (12) are now in 7.1. U3 and U4 retire nothing scored. The section 1, 6 item 4, 8 and Q1 wording now reads "four of A4's seven Reds (three by the module, one by the TCXO)". Reviewer re-add: U1 8 + 8 + 6 + 0 - 5 - 9 = 8 (USD 36.88 / 8 = 4.61); U2 12 - 4 = 8 (0.52); total 16, USD 47.07 / 16 = 2.94. A4 Reds: 16, 16, 15, 12, 12, 12, 10 (seven); A5 Reds: 15, 12, 12 (three) | Verified for (a) to (d). A separate omission in the rebuilt table is new finding-17 |
| finding-13 | C7-A5 on its anchors; re-run the sensitivity | C7-A5 is now 3, and the evidence cell lists the KDR relaxations. Section 5 totals and section 6 are re-run (reviewer re-computation below) | Verified |
| finding-14 | Clamp VGG at 3.5 V or less at the LM2940 maximum, or bound Pout at the clamp; open-loop case in WP-PDR-22; correct the wording | 0.68 divider, "5.1 V x 0.68 = 3.47 V at the LM2940 maximum, at or under 3.5 V at every pack voltage". The open-loop case is bounded by REQ-SYS-156 and the 10 s cutoff. WP-PDR-22 now checks at most 8 W at the clamp at 8.4 V, with a pack-dependent clamp from spare parts as the fallback. The "under the 4 V rating" wording is removed | **Fixed in part.** The open-loop case, the wording and the WP-PDR-22 criteria are Verified. The clamp value is not: the LM2940 datasheet (SNVS769J, section 6.5, 5 V column) gives an output of 4.85 to 5.15 V at TJ = 25 C and **4.75 to 5.25 V** over the operating temperature range, not a 5.1 V maximum. At 0.68 the clamp reaches 3.50 V at 25 C and **3.57 V** over temperature, before any divider tolerance. The resistors come from the owner's through-hole stock, whose tolerance is not stated: with 5 % parts the ratio can reach about 0.70. Stays Open (lien); see the finding table |
| finding-15 | State the VDL tolerance over range; propose a band or record at risk | Section 8.10 REQ-SYS-084: at risk. -0.085 / +0.060 V over -40 to +85 C; proposed band 2.415 to 2.560 V (TBR). The reviewer's arithmetic reproduces (2.500 - 0.085, 2.500 + 0.060) | Verified |
| finding-16 | State which contingency basis the gate applies | Section 8.4: the gate applies the M1 basis, 15 % on every line. The reason given is build-time growth (D12). 15 % of 134.19 = 20.13, "up to about USD 20" | Verified |
| R-1 (relay timing) | Relay contacts closed before the ramp; no wind-up; routed | Omron G5V-2 datasheet read by the reviewer (below): "Operate time 7 ms max.", "Release time 3 ms max."; the 5 VDC coil is 100 mA and 50 ohm, about 500 mW. The ramp starts at t0 + 10 ms, with the clamps and a parked integrator until then and a mid-ramp plausibility check. WP-PDR-22 models the contact closing at 7.5 ms and, as a fault, at 12 ms; WP-PDR-23 carries the pass criteria. The requirement texts at HEAD are REQ-SYS-160 "begin the RF rise within 15 ms (TBR) of each straight-key contact closure" and REQ-SYS-161 "the same lead-in of at most 12 ms (TBR) after the receive-to-transmit changeover". 10 ms is at most 12 ms, and 1 + 2 + 10 = 13 ms is at most 15 ms | Verified. The residual step on a late contact is bounded by the clamp, which is finding-14's open value |
| R-2 (heat inside the case) | Withdraw the claim; design controls; risks; routed | "Heat outside the case" is withdrawn from sections 1, 4.2 and 7.3. Revision 3 adds a vented bay, a double-wall bulkhead and the cells at the far end, and keeps the LM393 cell 60 C trip. Cell-heating risks for A3, A4 and A5 are linked to HZ-007 (Catastrophic in `docs/safety/hazards.json`) and merged into RSK-007 ("Li-ion cell thermal event inside the enclosure"). The bands follow the 06 section 7 safety override: Red at likelihood 2 or more, Yellow at 1. WP-PDR-28 has criteria (a) to (c), and the revisit conditions of section 10 name them. The lumped balance reproduces: T = (P + 0.035 x 60 + 0.11 x 45) / 0.145 = 54.1 C at P = 0.8 W and 56.2 C at P = 1.1 W. C8-A5 stays 3 on the anchor "heat near PETG needing design controls" | Verified. The estimate's sensitivity to the assumed 60 C bay is observation O-9 |
| X-6 | finding-12 and finding-14 before B1a | Both answered in revision 3 | finding-12 Verified; finding-14 fixed in part |

### Roll-up re-add (revision 3)

Section 8.3 is unchanged from revision 2 apart from the gate text. The reviewer script re-parsed the 31 Mouser rows of the committed file. Every line equals quantity times unit price (31 of 31), and the rows sum to 84.31.

| Quantity | TS-012 | Reviewer | Result |
|---|---|---|---|
| Mouser listed subtotal (rows 1 to 31) | 84.31 | 84.31 | Reproduced |
| E1 to E4, low / mid / high | 6.58 / 13.83 / 21.08 | 6.58 / 13.83 / 21.08 | Reproduced |
| Mouser merchandise | 90.89 to 105.39 | 90.89 to 105.39 | Reproduced |
| Listed parts (84.31 + 28.91 + 11.98 + 4.99 + 4.00) | 134.19 | 134.19 | Reproduced |
| Shipping 32.00 / 45.50 / 59.00; duty 1.40 / 2.55 / 26.83; tariff 4.00 / 8.00 / 15.00 | as shown | same (duty worst 0.925 x 29.00 = 26.825) | Reproduced |
| A5 subtotal | 178.17 / 204.07 / 256.10 | 178.17 / 204.07 / 256.095 to 256.10 | Reproduced |
| Contingency 15 % | 26.72 / 30.61 / 38.41 | 26.7255 / 30.6105 / 38.415 | Reproduced (truncation stated in 8.4) |
| A5 capped | 204.89 / 234.68 / 294.51 | 204.8955 / 234.6805 / 294.509 to 294.515 | Reproduced |
| Margin to USD 300 | 5.49 | 5.485 to 5.491 | Reproduced |
| A4 capped | 161.85 / 187.61 / 243.42 | 161.851 / 187.611 / 243.4205 | Reproduced |
| A5 minus A4, planning | 47.07 | 47.07 | Reproduced |
| Gate contingency on listed parts | "up to about USD 20" | 0.15 x 134.19 = 20.13 | Reproduced |

### Owned items and sales tax (revision 3)

| Item | Owner direction | Revision 3 | Result |
|---|---|---|---|
| 24 AWG magnet wire | Owned (section 10) | No wire row; BPF and trifilar windings from owned wire; gate item 9 | Handled |
| 2 m antenna, SMA-male plug | Owned | No antenna row; EX-9, REQ-SYS-172 delta | Handled |
| Through-hole R and C | Owned | Not bought; E2 buys the SMD passives and 0 to 3.00 for assortment gaps | Handled |
| Surface-mount passives | Not owned | Bought (row 4, E1, E2) | Handled |
| USB power adapter | Owned | Powers the MC1; gate item 9 | Handled |
| 18650 cells and charger | Not owned (section 11, answered) | Priced: P28A x 2 11.98, MC1 4.99; still worded "assumed" and Q2 still open | Handled in cost; wording stale (finding-18) |
| Test instruments | Outside the radio cap, separate USD 300 equipment cap (section 11) | EX-13 and Q4 still "to confirm"; tinySA "committed" | Handled in cost; wording stale (finding-18) |
| Sales tax | Excluded (section 10) | Line at 0; M1 excludes it | Handled |

### Price, stock and datasheet spot checks (retrieved 2026-09-27 by this reviewer; nothing logged into, no form, no cart; datasheet PDFs read through the web-fetch cache and pdftotext)

| # | Item (TS-012 row) | TS-012 claim | Read today | Kind | Source | Result |
|---|---|---|---|---|---|---|
| T1 | RA07M1317M-501 at RF Parts (new PA) | 28.91 (27.46 at 10), In Stock, New, USD 15 minimum | "$28.91"; "Buy 10 for $27.46 each"; "In Stock"; New; no EOL note; "Fifteen ($15.00), all inclusive" | L | https://www.rfparts.com/ra07m1317m.html | Verified |
| T2 | RA07M1317M status | "Active" | Supply status "Active"; Mitsubishi Electric US, Telepro, Diamond Advanced Components | L | https://meus-semiconductors.com/products/high-frequency-devices/ra07m1317m | Verified |
| T3 | 74LVC1G80GV,125 (row 28, prescaler) | Mouser 0.15, 12,379; DigiKey 16,398; Newark 1,812 | Mouser 0.15, 12,379; DigiKey 0.15, 16,398; Newark 0.176, 1,812 | A | https://www.oemstrade.com/search/74LVC1G80GV | Verified |
| T4 | TG2520SMN 25.000M-MCGNNM3 (row 29, TCXO) | Mouser 3.61, 1,810 | Mouser 3.61 (3.14 at 10), 1,810, D# 732-TG252S25MCGNNM3 | A | https://www.oemstrade.com/search/TG2520SMN | Verified |
| T5 | Boyd 529802B02500G (finding-11 search, new) | 3.7 C/W; Future 4.51, 73,071; Mouser 10.50, 0 | Same; Newark description "41.9mm W x 38.1mm H x 38.1mm L" | A | https://www.oemstrade.com/search/529802B02500G | Price and stock verified; "same size" not (O-8) |
| T6 | Ohmite RA-T2X-64E (finding-11 search, new) | 3.1 C/W, 42 x 25 x 63.5 mm; TME 4.64, 165 | TME 4.64, 165; 3.1 C/W; "42 x 25 x 63.5mm" | A | https://www.oemstrade.com/search/RA-T2X-64E | Verified |
| T7 | MCP6002-I/P (row 7; now the clamp op-amp) | 0.44, 2,155 | Mouser 0.44, 2,155 | A | https://www.oemstrade.com/search/MCP6002-I%2FP | Verified |
| T8 | G5V-2-DC5 (row 2; R-1) | 3.33, 2,988 | Mouser 3.33, 2,988, "DPDT 5VDC 500mW" | A | https://www.oemstrade.com/search/G5V-2-DC5 | Verified |
| T9 | LM2940CT-5.0/NOPB (row 25; clamp supply) | 2.04, 141; Newark 2.13, 1,002 | Same | A | https://www.oemstrade.com/search/LM2940CT-5.0%2FNOPB | Verified |
| T10 | Molicel P28A x 2 | 5.99 sale (6.99), in stock | "$5.99" sale, "$6.99" regular, "In stock", unprotected flat top | L | https://www.18650batterystore.com/products/molicel-p28a | Verified |
| T11 | XTAR MC1 | 4.99 sale (9.99), in stock, 0.5 A | "$4.99" sale, "$9.99" regular, "In stock", 500 mA; termination voltage not stated | L | https://www.18650batterystore.com/products/xtar-mc1 | Verified |
| T12 | Boyd 530002B02500G (row 3) | 3.39, 3,693; Mouser description 63.5 x 18.29 x 3.17 mm | Mouser 3.39, 3,693, "2.6 Degree C/W, 2.67mm Hole, 63.5x18.29x3.17mm"; no mass | A | https://www.oemstrade.com/search/530002B02500G | Verified; mass still unread (gate item 7) |
| T13 | Fair-Rite 2843000202 (row 30) | 0.88, 47,515 | Mouser 0.88, 47,515, "43 Multi-Aperture" | A | https://www.oemstrade.com/search/2843000202 | Verified |
| T14 | TE CONSMA001-C-G (row 18) | 2.80, 4,598 | Mouser 712-CONSMA001-C-G, 2.80, 4,598 | A | https://www.oemstrade.com/search/CONSMA001-C-G | Verified |
| T15 | Diodes 1N5711W-7-F (row 14) | 0.307, 3,033 | Mouser 621-1N5711W-F, **0.24**, 1,839 (0.17 at 10); the 0.307 and 3,033 row is Diodes Incorporated, listed with Newark | A | https://www.oemstrade.com/search/1N5711W-7-F | **Differs, conservative**: the study is USD 0.54 high (0.62 capped). The row follows iteration 1's reading, which this read contradicts (O-7) |
| T16 | AO3400A (row 22) | 0.52, 303,947 | Today's page extract shows no Mouser or Newark row (DigiKey, TME, LCSC and brokers only) | A | https://www.oemstrade.com/search/AO3400A | Not verifiable today; the iteration-2 read stands |
| T17 | Omron G5V-2 datasheet (R-1) | Operate 7 ms max, release 3 ms max, DC5 coil 100 mA at 50 ohm | "Operate time 7 ms max.", "Release time 3 ms max."; 5 VDC 100 mA, 50 ohm, approx. 500 mW; bounce distribution graph present | L (datasheet) | https://omronfs.omron.com/en_US/ecb/products/pdf/en-g5v_2.pdf | Verified |
| T18 | TI LM2940 datasheet (finding-14 clamp basis) | "5.1 V ... at the LM2940 maximum" | SNVS769J (revised December 2014), section 6.5, 5 V: output 4.85 / 5 / 5.15 V at TJ = 25 C; 4.75 / 5 / 5.25 V over the recommended operating temperature range, 5 mA to 1 A | L (datasheet) | https://www.ti.com/lit/ds/symlink/lm2940-n.pdf | **Differs** (finding-14) |

Totals: 18 checks. 14 verified or verified in part: T1 to T14, where T5 is price and stock only and T12 leaves the mass unread. 2 differ: T15, where the study is conservative, and T18. 1 is not verifiable today (T16). T17 is a datasheet read that confirms the author's figures. Not verifiable without a cart, as before: the Mouser shipping and tariff lines, RF Parts carriage, 18650BatteryStore shipping and the JLCPCB two-design quote. The study carries all of them as E, with the owner's gate read.

### Scoring and ranking arithmetic (revision 3)

- **Matrix totals** (section 5), re-computed from the section 4.2 scores: A1 295, A2 325, A3 320, A4 340, A5 350. The weights sum to 100.
- **Interpolation:**
  - C1-A5 3.61 (4) and C2-A5 1.27 (1); C2-A4 3.83 (4); C2-A2 4.32 (4); C1-A3 3.42 (3).
  - C6-A5: 153 x 70 x 42 mm is +14.75 % volume and +20.0 % with the SMA. That interpolates to 1.88, rounded to 2. Mass 361 g is under 370 g. Unchanged at 2.
- **Weight sensitivity** (16 runs, others rescaled to 100). Every figure in section 6 item 1 reproduces:
  - A5 first in 9 runs.
  - A4 first in 6: C1 +10 (360.0 against 356.2), C2 +10 (346.3 against 323.7), C3 +10 (358.8 against 344.1), C6 +10 (335.6 against 333.3), C5 -10 (357.5 against 331.2) and C8 -10 (356.5 against 355.9).
  - A2 first in 1: C4 -10 (350.0 against 344.4).
  - A5's smallest winning lead is 4.4 (C3 -10, 355.9 against A2 351.5).
  - The section 1 summary of the same runs matches.
- **Low-cell moves.** Exactly five single moves change the top rank: A4 C5 +1 (360 against 350), A4 C8 +1 (355 against 350), A5 C1 -1 (340 against 330), A5 C8 -1 (340 against 335) and A5 C6 -1 (a tie at 340). The joint adverse case gives A4 380, A3 360, A2 355 and A5 305. All reproduce.
- **Robustness verdict.** "Not robust" between A5 and A4, weaker than in revision 2, is stated in sections 1, 6 and 8 and in Q1. Rule 14.5 is met.
- **Risk arithmetic** (section 8.2 against 7.1): reproduced as written (16 points, USD 2.94 per point). The omission of one 7.1 row from the reconciliation is finding-17.

### Estimate against listed-price presentation (revision 3)

Nothing estimated is shown as a listed price. The revision-3 text adds no price row. It adds these figures:
- the two larger-sink reads (kind A with URLs);
- the "USD 33 to 47" replacement-module figure in 8.4 and D12, which is derived from the listed 28.91 and the estimated RF Parts shipping and is labelled as a cost, not a price;
- the thermal estimates, labelled Low.

The E rows, the shipping, duty and tariff kinds, and the planning and worst-case labels in section 1 are unchanged from iteration 2. Row 14 (1N5711W) is a listed read that today's page contradicts; its error is conservative (O-7).

### Findings (iteration 3)

| Finding | Severity | Item | Location | Description | State | Deferred to |
|---|---|---|---|---|---|---|
| finding-1 | Major | CK-RSK-B5, B8 | TS-012 sections 1, 4.1, 7.1, 7.2, 8.4 | See iteration 1; unchanged in revision 3 | Verified (iteration 2; holds on revision 3 at d5a3058) | |
| finding-2 | Major | CK-RSK-B5, B7 | TS-012 sections 2, 3.1 M1, 8.3 | Closed by the owner's section 10 answer; sales tax line 0 unchanged | Verified (iteration 2; holds on revision 3) | |
| finding-3 | Major | CK-RSK-B5, B8 | TS-012 sections 1, 4.1 M4, 8.3 row 28, 8.10 REQ-SYS-182 | 74LVC1G80GV x3, 160 MHz minimum; row 28 re-read today (T3) | Verified (iteration 2; holds on revision 3) | |
| finding-4 to finding-10 | Minor | CK-RSK-B4, B5 | See iteration 2 | Unchanged in revision 3 (finding-4 row 14 see O-7) | Verified (iteration 2) | |
| finding-11 | Minor | CK-RSK-B5 | TS-012 section 7.3 junction bullet, 8.2, 9 | Transmit-duty-limit fallback at USD 0 with its requirement cost; larger-sink reads recorded | Verified (iteration 3, revision 3 at d5a3058) | |
| finding-12 | Minor | CK-RSK-B8, B9 | TS-012 sections 1, 6 item 4, 7.1, 8, 8.2, 8.13 Q1 | Items (a) to (d) and the "five Red risks" wording corrected | Verified (iteration 3) | |
| finding-13 | Minor | CK-RSK-B6 | TS-012 sections 4.2, 5, 6 | C7-A5 3; totals and sensitivity reproduce | Verified (iteration 3) | |
| <a id="finding-14"></a>finding-14 | Minor | CK-RSK-B5 (M4 "inside their published ratings") | TS-012 section 7.3 drive gating ("5.1 V x 0.68 = 3.47 V at the LM2940 maximum, at or under 3.5 V at every pack voltage"), 8.1 block diagram ("<= 3.47 V"), 8.10 REQ-SYS-156 row, 8.12 WP-PDR-22 row, 9 finding-14 disposition | Fixed in part. The open-loop bound, the wording and the WP-PDR-22 criteria are done. The clamp value rests on a 5.1 V LDO maximum that the datasheet does not give. TI SNVS769J section 6.5 (5 V) gives 4.85 to 5.15 V at TJ = 25 C and 4.75 to 5.25 V over temperature, so the 0.68 divider on a rail-to-rail MCP6002 output reaches 3.50 V at 25 C and 3.57 V at the temperature extreme. That is above the 3.5 V condition of the 10 W Pout rating, before the ratio tolerance of resistors "from the owner's through-hole stock" (unstated; 5 % parts allow a ratio of about 0.70, which gives 3.68 V). The excess matters only in the open-loop fault case that the clamp exists for, and the fix costs nothing. The pass criterion "VGG never above 3.5 V" in WP-PDR-22 would catch it only if the deck models the LDO and resistor tolerances. **Fix:** size the divider on 5.25 V and the resistor tolerance (for example 0.66 with 1 % resistors: ratio 0.6555 to 0.6645, so 5.25 x 0.6645 = 3.49 V highest and 4.75 x 0.6555 = 3.11 V lowest), or take the clamp from a reference independent of the 5 V bus. Carry the lower low-end clamp into the REQ-SYS-012 check, which already names "the lowest clamp (LM2940 minimum)", and add LDO and resistor tolerance to the WP-PDR-22 deck | Open | CDR readiness declaration (lien, rule C1); recommended in the WP-PDR-22 deck, before the order |
| <a id="finding-17"></a>finding-17 | Minor | CK-RSK-B8, B9 | TS-012 section 8.2 upgrade table ("risk scores exactly as in section 7.1, one score per risk"), section 1 risk-per-dollar bullet, 6 item 4, 8 rationale, Q1 ("about USD 2.9 per risk point") | The rebuilt table omits one A5 row of section 7.1: "Given a steep, nonlinear VGG transfer, a detector after the T/R relay ... or that an open loop drives the module past its ratings, adversely impacting REQ-SYS-014 and 015 and the RA07M1317M ratings" (6, Yellow). A4 has no matching row. The VGG transfer and the module ratings are module-specific, so under the table's own rule the row is either a risk U1 adds or has an A4 counterpart that cancels it; the table does neither. Counted as added by U1: U1 nets 2 points (USD 18.44 per point), the total is 10 points and **USD 4.71 per point, not 2.94**. The Reds retired (four) and the direction of the argument are unchanged, and the matrix does not use these points, so the ranking holds. But the per-point figure is the one number that section 6 item 4 and Q1 put to the owner. **Fix:** either add the A4 envelope-loop row (A4 uses the same relay and takes the same sequence, section 7.3) with its score and say it cancels, or count the A5 row in U1 and restate the per-point figures in sections 1, 6, 8 and Q1 | Open | CDR readiness declaration (lien, rule C1); cheap to correct in the owner-facing text before B1a if a revision is issued (cross item X-9) |
| <a id="finding-18"></a>finding-18 | Minor | CK-RSK-B5, B10 | TS-012 sections 1 (owner budget bullet), 2 item 1 and 2, 6 item 6, 8.9 EX-4 and EX-13, 8.13 Q2 and Q4 | Revision 3 (committed 18:06) does not apply status note section 11 (committed 17:55, `84e7b89`) or section 13 (`bb09ad2`, 18:00). Q2 (cells and charger) and Q4 (instruments) are still asked as open questions and their assumptions are still called "assumed" or "to confirm". But the owner answered: "I don't have any 18650s or chargers", and "that total of new equipment that I need to buy can't go over $300". The lead SE reading adds that the tinySA counts in that equipment cap if not yet bought, while EX-13 calls it "committed". Section 6 item 6 says "TV-014 (LTspice) is not yet accredited", but section 13 records ACC-LTSPICE-001 accredited for blob 88b71475. The answers agree with the assumptions the cost uses, so no total or score changes, but the owner would be asked two questions they have already answered. **Fix:** record the section 11 answers (cells and charger priced as answered; instruments outside the radio cap under a separate USD 300 equipment cap, with the tinySA and the USD 9.95 thermocouple counted there), close Q2 and Q4, and state the LTspice accreditation in section 6 item 6 | Open | CDR readiness declaration (lien, rule C1) |

Neither new finding, nor the part of finding-14 still open, is Major. finding-14's remainder is a zero-cost divider change inside a pre-order LTspice check, and it affects only a fault case. finding-17 changes the size of the risk-per-dollar case (2.94 to 4.71 USD per point), but it does not change the Reds retired, the direction of the argument or the matrix. finding-18 is stale wording; the answers match the assumptions used. None of them would lead the owner to choose between A5 and A4 on a wrong basis.

### Observations (iteration 3; not findings)

- **O-7.** Correction to this record's iteration-1 row 19 and finding-4 (history is kept as written). Today's read of the Mouser section is part 621-1N5711W-F at USD 0.24, 1,839 in stock. The 0.307 and 3,033 row is Diodes Incorporated, listed with Newark. The study's row 14 (0.307) therefore follows a reviewer mis-read. It overstates cost by USD 0.54 (0.62 capped), which is the conservative direction, so no change is required. The owner's cart read at the gate settles it.
- **O-8.** Section 7.3 and section 11 call the two larger-sink candidates "weaker TO-220 extrusions of the same size". The Ohmite RA-T2X-64E (42 x 25 x 63.5 mm) is the same size, but the Newark description of the Boyd 529802B02500G gives 41.9 x 38.1 x 38.1 mm, which is shorter. The conclusion ("weaker") holds.
- **O-9.** The R-2 balance takes the bay side of the bulkhead at 60 C, and the chimney flow is not estimated, as the study says. If the bay air sat at revision 2's unvented 74 C, the same balance gives 57.5 to 59.6 C in the cell bay; at the 83 C sink face it gives 59.7 to 61.8 C. The 0.035 W/K bulkhead conductance is generous for two 1.2 mm walls and a 3 mm gap: with film coefficients of about 5 W/m2 K on 29 cm2, the reviewer estimates 0.006 to 0.01 W/K, which makes the result much less sensitive to the bay temperature. So the Low estimate is plausible. WP-PDR-28 should report the bay air temperature it assumes or computes.
- **O-10.** The G5V-2 bounce figure (0.3 to 0.5 ms, graph read) comes from the datasheet's distribution graphs, whose samples are labelled G5V-2 and G5V-2 12 VDC, not the DC5 coil. The 2.5 ms margin in the 10 ms settle covers the difference. The WP-PDR-23 bench logic capture should measure the DC5 part.

### Readiness (iteration 3)

| # | Criterion | Result | Evidence |
|---|---|---|---|
| R1 | `validate_docs.py` exits 0 | **No** | Before this delta: `validate_docs: 101 passed, 8 failed, 109 checked`, exit 1. The 8 failures are other records (CM plan SA, configuration status, lessons learned, SRR ADRs 001 to 025, process 02, TV-001 to 010, TS-001 and TS-002, TS-002 SA); none involves TS-012. This record passes (Commands) |
| R2 | Section A | N/A | Trade study |
| R3 | Sections 1 to 9 filled; section 10 empty | Yes | Section 10 fields empty; revisit conditions updated for R-1 and R-2 |
| R4 | Decision need and gate | Yes | Header "Decide by": B1a 2026-09-29, no later than B1b 2026-10-01 |

### B. Trade study items re-answered (iteration 3)

| Id | Answer | Evidence |
|---|---|---|
| CK-RSK-B5 | Yes (liens) | The M1 roll-up, the M2 reads (T1 to T14) and the M4 relay and heat answers are re-checked. Lien: the finding-14 clamp basis (T18); finding-18 wording |
| CK-RSK-B6 | Yes | Totals, interpolation and C7-A5 reproduce |
| CK-RSK-B7 | Yes | Section 6 re-run reproduces: 16 weight runs, five Low-cell moves and the joint case. The verdict is "Not robust", stated as weaker; the value of information names WP-PDR-28 for the cell bay |
| CK-RSK-B8 | Yes (lien) | Four-part risks now include the cell-heating rows for A3, A4 and A5 under the safety override and the A4 spur and reference Reds. The 8.2 reconciliation omission is finding-17 |
| CK-RSK-B9 | Yes | A5 350 is the highest among the alternatives that pass every mandatory criterion; A4 (340) is named with its condition |
| CK-RSK-B10 | Yes | Section 9 lists the iteration-2 dispositions and R-1 and R-2; section 10 is empty |
| CK-RSK-B1 to B4 | Yes | As at iteration 2 |

### Cross items (iteration 3, returned to Claude)

- **X-9.** The software assurance pair (X-2, X-5) is still not filed (`docs/reviews/PDR/checklists/` has no `ts-012-design-to-cost-software-assurance.md`), so the record verdict still waits for it. Rule C1 allows at most three iterations before escalation to the owner (07 section 10.2), and this is the third. A revision 4 that fixes finding-14, 17 or 18 would change the blob and need a fourth iteration, which escalates to the owner. Recommendation: either carry them as liens and fix finding-14 in the WP-PDR-22 deck, or batch all three into one revision with the owner's agreement at B1a.
- **X-10.** The author's summary reports two points about this revision. First, the computed task text that briefed the author was cut off partway through R-2, so any adversarial refutation after R-2 was not delivered or answered. The adversarial report is not committed (section 11 says so), so this record cannot check completeness. The lead SE should confirm whether the check of revision 2 raised refutations beyond R-2 and route any to TS-012. Second, the author reports running two `grep -n` reads in the known record file before loading `search_code` (the charter section 11 rule 1 order). That is a process deviation in the author invocation, not in the product. It is noted for the lessons-learned log.
- **X-11.** The status note section 11 equipment cap (USD 300 on new equipment, tinySA if not yet bought, a thermocouple not owned) belongs in the V&V plan and owner action pack (WP-PDR-43), outside TS-012's cost (finding-18 asks only for the TS-012 wording).

### Commands (iteration 3)

```
git rev-parse HEAD                                                                    # d5a3058bbe42a28d5b6fad43aa331fa83cdbd93a
git rev-parse HEAD:docs/decisions/trade-studies/TS-012-design-to-cost-hand-built.md   # b1f03fad90ad0f7e4a118624792838d495501e56
git hash-object docs/decisions/trade-studies/TS-012-design-to-cost-hand-built.md       # b1f03fad90ad0f7e4a118624792838d495501e56
git diff -U0 eca24fa d5a3058 -- <TS-012 path>                                         # hunks outside 8.3 rows; roll-up rows unchanged
/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/validate_docs.py   # before the delta: 101 passed, 8 failed, 109 checked (exit 1)
  after the delta: 101 passed, 8 failed, 109 checked (exit 1); PASS docs/reviews/PDR/checklists/ts-012-design-to-cost.md; the same 8 records fail
python3 (scratchpad) re-parse of 8.3 rows 1 to 31 and 8.4 for A5 and A4; matrix totals; C1, C2, C6 interpolation; 16 weight runs;
  every Low-cell move and the joint case; 8.2 risk points; R-2 lumped balance and its bay-temperature sensitivity; VGG clamp at 5.0, 5.1, 5.15 and 5.25 V
python3 over docs/requirements/sys/requirements.json: REQ-SYS-012, 014, 084, 102, 103, 112, 113, 156, 160, 161 descriptions; hazards.json HZ-003, HZ-007; register.json RSK-006, 007, 026
pdftotext -layout on the web-fetch cached datasheets: TI LM2940 SNVS769J section 6.5; Omron G5V-2 characteristics and coil table
```

### Measurements (iteration 3)

size = 6 alternatives, 13 criteria, 35 A5 BOM rows, 7 shipping, duty and tariff lines, 18 spot checks; turns = 35; minutes = 60; major = 0 new (3 Verified); minor = 2 new, 5 Verified this iteration (finding-11, 12, 13, 15, 16), 1 fixed in part (finding-14).

### Record verdict and verdict format (iteration 3)

`reviewer_verdict: APPROVED`. The three Major findings stay Verified, and no Major is open. finding-11, 12, 13, 15 and 16 are Verified on revision 3. finding-14 (fixed in part) and the new Minor findings 17 and 18 are liens due at the CDR readiness declaration (plan rule C1), with the TS-012 author as owner. The record `verdict` stays NEEDS CHANGES for two reasons: the software assurance pair is still not filed (07 section 2.1.1; `assurance_verdict: pending`), and readiness R1 fails on records unrelated to TS-012. When the pair returns APPROVED and R1 holds, the lead SE sets `verdict: APPROVED`, provided `git rev-parse HEAD:<path>` still equals `b1f03fad`. A changed blob needs a fourth iteration, which rule C1 escalates to the owner (X-9).

```
VERDICT: APPROVED (reviewer); record verdict held for the software assurance pair and readiness R1
FINDINGS:
- [Major] finding-1, finding-2, finding-3: Verified (hold on revision 3 at d5a3058).
- [Minor] finding-11 to finding-13, finding-15, finding-16: Verified on revision 3.
- [Minor] CK-RSK-B5 section 7.3: finding-14 fixed in part; the 0.68 clamp assumes a 5.1 V LDO maximum, but LM2940 SNVS769J gives 5.15 V at 25 C and 5.25 V over temperature (3.50 and 3.57 V at VGG), before the resistor tolerance (lien).
- [Minor] CK-RSK-B8, B9 section 8.2: the A5 envelope-loop row (6) is left out of the risk-per-dollar reconciliation; counted, USD 4.71 per point, not 2.94 (finding-17, lien).
- [Minor] CK-RSK-B5, B10 sections 1, 2, 6, 8.9, Q2, Q4: status note sections 11 and 13 answers not applied (finding-18, lien).
ITEMS N/A: CK-RSK-A1 to CK-RSK-A11 (product is a trade study)
MEASUREMENTS: size=6 alternatives, 13 criteria, 18 spot checks; turns=35; minutes=60; major=0 new; minor=2 new; verified=15; open=3
```

## Iteration 3 re-issue 1: the owner-authorized fourth iteration, delta on TS-012 revisions 4 and 5 (2026-09-28, HEAD `37d5824`)

**Authority and scope (rule C1, rule C2).** Iteration 3 was the last iteration before escalation (X-9). The owner authorized a fourth iteration: status note `docs/plan/status/status-2026-09-28.md` section 1, item 3 ("Authorize the fourth INSP-110 iteration on TS-012 revision 4"), read by the lead SE as approved ("good to continue"). In the same answer the owner approved item 2, the discriminating analyses before the A4 and A5 choice. Revision 5 folds those analyses in, and it was committed before this iteration ran. This pass therefore reviews revision 4 (the liens and the adversarial answers) and revision 5 (the analysis results, the re-scoring, the ranking and the recommendation) in one delta, as the brief directs. The front matter keeps `iteration: 3`, the record schema maximum (precedent INSP-009, INSP-038 and INSP-075). The body calls this pass the fourth iteration. The lead SE should record in the status note that the item-3 authorization covers revision 5 (cross item X-14). Findings 1 to 13, 15 and 16 stay Verified and are not re-opened. New findings are raised only where revision 4 or 5 introduced the defect.

**Products.** Revision 4: blob `fa41032e` at `7d0d450` (the commit changes only the TS file). Revision 5: blob `731ba0eb` at `37d5824`, Status Proposed, 1133 lines. `git rev-parse 37d5824:<path>`, `git rev-parse HEAD:<path>` and `git hash-object <path>` all give `731ba0eb`. HEAD is `37d5824` on `main`, and `git show --stat 37d5824` lists only the TS file. The cited analysis records and their review records were read at HEAD (table "Review verdicts cited" below). Checklist as before: `peer-review-checklist-risk.md` revision A, section B.

**Independence (rule C4).** This invocation authored no part of TS-012 revisions 1 to 5. It did not author the six analysis records or their runs, their review records (INSP-112 to INSP-116), or iterations 1 to 3 of this record. It edited no product file and changed only this record.

**Search first (charter section 11 rule 1; rule C3).** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` was queried twice: "PDR work plan rule C1 review iterations verdict escalation to owner" and "TS-012 thermal analysis A5 junction band 113.6 wholly over 110 C INSP-112 reviewer verdict". After that, `grep` only pinned lines in known paths. **Deviation, recorded:** one `grep -n '^#'` heading listing of two known files (this record and TS-012) ran after the tool was loaded but before its first query. The rule requires the query first. No result of this review depends on that listing. The deviation is noted for the lessons-learned log (cross item X-15).

**Owner direction applied.** Status note 2026-09-27 sections 10, 11 and 13 as before. Status note 2026-09-28 sections 1 and 2:
- item 2 (the analyses) approved;
- the tinySA Ultra is not yet bought and the owner will buy it later;
- the multimeter is a Fluke 174 without a temperature input, so a stand-alone K-type thermometer is added inside the USD 300 equipment cap;
- the resistor tolerance is not answered, and the 1 % parts are priced in the E2 allowance.

Revision 5 records all four in sections 1, 2, 8.9 EX-13 and 8.14 D-16.

### Verification of the iteration-3 liens and the revision-4 adversarial answers

| Item | Required | Revision 4 text (held in revision 5) | Result |
|---|---|---|---|
| finding-14 | Size the VGG divider on 5.25 V and the resistor tolerance, or use an independent reference; carry the lower clamp into the REQ-SYS-012 check; LDO and resistor tolerance in the WP-PDR-22 deck | 0.654 divider from two 1 % E24 values (2.7 k over 5.1 k); ratio 0.6493 to 0.6584; VGG 3.08 to 3.46 V; WP-PDR-22 criteria name the LDO range, dropout, the resistor tolerance, the op-amp headroom and the module's VGG current; the 3.08 V low end is in the REQ-SYS-012 check | **Verified.** Reviewer: 5.1 / 7.8 = 0.6538. At 1 %, 5.151 / 7.824 = 0.6584 and 5.049 / 7.776 = 0.6493. 5.25 x 0.6584 = 3.457 V; 4.75 x 0.6493 = 3.084 V. The PA drive analysis revision 2 runs at this clamp range (its section 3 table). Revision 5 adds the pack-dependent clamp as design item D-9 for the open-loop case |
| finding-17 | Count the A5 envelope-loop row in U1, or add an A4 counterpart | Revision 4 counts it in U1 (-6). Revision 5 adds the A4 counterpart from the keying analysis (6) and raises the A5 row to 9, so U1 takes -3 | **Verified.** Revision 4: U1 8 + 4 + 6 - 5 - 9 - 6 = -2; total 6 points, 47.07 / 6 = 7.85. Revision 5: see the risk arithmetic below |
| finding-18 | Apply status note sections 11 and 13; close Q2 and Q4; state the LTspice accreditation | Q2 and Q4 closed as answered; EX-4 and EX-13 rewritten; ACC-LTSPICE-001 stated in sections 2, 3.4 and 6 item 8 | **Verified.** Q4's recommendation still names "a thermocouple (USD 9.95)" where revision 5 moved to a K-type thermometer (EX-13, D-16). That is stale wording only (O-15) |
| R-3 (48 MHz in transmit) | Withdraw; list the transmit clocks | Withdrawn with the RP2350 clk_adc reason. The 125 MHz clk_sys, the 25 MHz reference harmonics and the /8 products are named, and a WP-PDR-20 transmit clock-plan item is added | **Verified.** Revision 5 reports the item run (`spurs-ts012.md`, INSP-113 reviewer APPROVED) and adopts clk_sys 96 MHz (D-12) |
| R-4 (junction "bound") | Restate as an estimate | 87 to 119 C estimate; C8-A5 3 to 2 on the stated section 3.1 range rule; A4 340, A5 335 presented together | **Verified.** Reviewer re-computation of the revision 4 table: 8.54 x 2.9 = 24.8 K, so 69.8 / 86.7 / 76.5 C; 9.95 x 3.8 = 37.8 K, so 82.8 / 103.1 / 89.6 C; 9.95 x 5.4 = 53.7 K, so 98.7 / 119.0 / 105.5 C; 10.95 x 5.4 = 59.1 K, so 104.1 / 126.8 / 110.9 C. Stage-2 rise is 2.4 K/W on (P - 1.5 W) and stage-1 rise 4.5 x 1.5 = 6.75 K. Superseded in revision 5 by WP-PDR-28 |
| X-10 | Confirm the adversarial list | Revision 4 and revision 5 (X-R5-1) both report a truncated brief | Carried to the lead SE (X-10 stands) |

### Revision 5: score changes checked against the evidence and the anchors

| Cell | Revision 4 to 5 | Evidence read by the reviewer | Result |
|---|---|---|---|
| C1-A5 | 4 to 3 | 247.80 interpolates to 5 - 2 x 47.80 / 50 = 3.09 | Reproduced |
| C2-A2, C2-A4 | 4 to 3 | 253.90: 3 + 2 x 6.10 / 40 = 3.31; 263.69: 3 - 2 x 3.69 / 40 = 2.82 | Reproduced |
| C5-A5 | 5 to 4 | PA drive revision 2 section 5: A5 "FAIL as designed"; 195 corners under 10 mW and 28 over 30 mW of 810 (195 + 28 = 223); nominal 4.09 W and lowest corner 3.19 W at 6.4 V and 25 C key-down; datasheet-minimum module 2.99 W. LPF revision 2: 5 W at 8.4 V is a back-off state on the -17 dBc convention. Keying revision 2: A5's first element fails the worst-case sum by 0.045 V (17 of 72) | Reproduced. The anchor judgement (between 3 and 5) is supported: A5 loses "power held", the stability-condition claim and the guarantee at the binding case, and keeps the catalog LPF, the TCXO, the validated mixer, the DPDT relay and the monitor port. Rests on two records not yet re-reviewed (X-13) |
| C5-A3 | 5 to 4 | Same module; A3 was not analysed | Accepted as a disclosed inference. The drive-window part depends on A5's pad and coax, which A3 may not share. The low-pack power part applies |
| C5-A4 | 2, confirmed | Nominal 3.06 W and lowest corner 1.69 W at 6.4 V (-3.71 dB); every lever still 2.5 dB short; no harmonic data; JFET half-IF representative (8 of 16 cases unconverged) | Supported. A4 already carried "power short" at revision 4, so no anchor attribute changes. Its -1 move is in section 6 |
| C6-A4, C6-A5 | 3 to 1, 2 to 1 | Thermal section 6: the wrap guard adds about +14 mm length, +4 mm width and +10 mm height at the sink end for both. Reviewer volume from the study's method: A4 44 x 74 x 52 + 117 x 70 x 42 = 513,292 mm3, +30.9 %; A5 44 x 74 x 52 + 123 x 70 x 42 = 530,932 mm3, +35.4 %; both over the 20 % anchor | Reproduced. A4 moves 18.6 mm (142 + 6.6 + 12), not 14 mm, because revision 4's A4 had no end guard; C6 is 1 either way |
| C8-A5 | 2 to 1 | `bands.csv` / `verdict_set.csv` V01 A5-DC: 125.9480 - 12.3628 = 113.59 C and + 19.9691 = 145.92 C, wholly over 110 C. A4-DC: 122.6192 - 14.7445 = 107.87 C and + 20.2877 = 142.91 C, which spans 110 C | Arithmetic reproduced. The study is right that the thermal record's sentence "its band spans 110 C, as A4's does" does not match the record's own V01 A5-DC numbers. The rule's basis changed, however (O-11) |
| C8-A3 | 2 to 1 | A5 as revision 4 drew it: 142.1 - 18.6 = 123.5 C, wholly over; A3's sink is wholly inside the case | Accepted as a disclosed inference |
| C8-A2 | 3 to 2 | A2 not analysed; Tj about 92 C (architect, unbounded) read as a range spanning 110 C by parity with the finalists' model results | Accepted as a disclosed inference. It decides the A4 and A2 order (finding-19), and the "20 to 40 K" figure is loose for A4 (O-12) |
| C3, C4, C7 | unchanged | D-10's 74LVC1G66-class switch in SC-74A and the 2N7002 in SOT-23 are not flagged; the third BPF section is common; the select-on-test pad is a tuning step (note only); both finalists add deltas of the same anchor class | Supported |

**M1 and M4 (section 4.1).** M1: A5 at 314.78 is "conditional", with guards G1 and G2 taken to 298.10. A3 at 308.16 (LCSC merged) is "fail on estimated lines", with no guard (finding-21). M4: both finalists pass. The A5 open-loop note (the 10 W rating may be exceeded from 8.1 V at a -10 C start, PA drive section 5 (g)) is carried as D-9. D-11 changes the implementation of the REQ-SYS-120 second condition without saying so (finding-23).

### Roll-up re-add (revision 5)

| Quantity | TS-012 | Reviewer | Result |
|---|---|---|---|
| E5 components (a) to (f), low / high | 5.19 / 17.63 | 1.00 + 0.20 + 1.00 + 0.40 + 0 + 2.59 + 0 = 5.19; 4.50 + 1.35 + 4.00 + 1.00 + 0.58 + 3.40 + 2.80 = 17.63 | Reproduced ((b) 0.10 + 0.10 = 0.20 low and 0.30 + 0.30 + 0.44 + 0.31 = 1.35 high; (f) 1.90 + 3 x 0.23 = 2.59 and 1.90 + 3 x 0.50 = 3.40) |
| E5 planning, needed items (a) to (e) | 11.41; 2.60 to 11.43 | 11.41; 2.60 to 11.43 | Reproduced |
| E5 capped | 5.96 / 13.12 / 20.27 | 5.9685 / 13.1215 / 20.2745 | Reproduced (truncated) |
| A5 subtotal | 183.36 / 215.48 / 273.73 | 134.19 + 6.58 + 5.19 + 32.00 + 1.40 + 4.00 = 183.36; 134.19 + 13.83 + 11.41 + 45.50 + 2.55 + 8.00 = 215.48; 134.19 + 21.08 + 17.63 + 59.00 + 26.83 + 15.00 = 273.73 | Reproduced |
| A5 capped | 210.86 / 247.80 / 314.78 | 210.864 / 247.802 / 314.7895 | Reproduced |
| A5 after G1, G2 | 305.58; 298.10 | 314.7895 - 9.20 = 305.5895; - 7.475 = 298.1145 | 305.58 reproduced; 298.10 is the difference of truncated steps; exact 298.11 (O-16) |
| A5 needed-only E5 | 242.74 planning; 307.65 worst | 211.085 x 1.15 = 242.748; 267.53 x 1.15 = 307.660 | Reproduced |
| A4 subtotal and capped | 145.93 / 174.55 / 229.30; 167.81 / 200.73 / 263.69 | 140.74 + 5.19; 163.14 + 11.41; 211.67 + 17.63; x 1.15 = 167.8195 / 200.7325 / 263.695 | Reproduced |
| A4 needed-only E5 | 195.67; 256.56 | 170.155 x 1.15 = 195.678; 223.10 x 1.15 = 256.565 | Reproduced |
| A4 with U3; with U2 and U3 | 203.33 / 266.29; matrix 300 | 200.73 + 2.60; 263.69 + 2.60. With U2 as well: 207.48 (C1 4.70, 5) and 270.44 (C2 2.48, 2), C3 3, C5 3: 315 - 30 + 20 - 5 = 300 | Reproduced |
| A2, A3 re-rolls | 193.16 / 253.90; 252.68 / 308.16 / 331.16 | 180.04 + 13.12; 233.63 + 20.27; 239.56 + 13.12; 287.89 + 20.27; 310.89 + 20.27 | Reproduced |
| A5 minus A4, planning | 47.07 | 247.80 - 200.73 | Reproduced |
| Mouser merchandise with E5 | about 96.08 to 123.02 | 90.89 + 5.19; 105.39 + 17.63 | Reproduced |

### Analysis results cited against their records (read at HEAD `37d5824`)

| # | TS-012 figure (section) | Record and location | Result |
|---|---|---|---|
| A1 | A4 122.7 C (+20.3 / -14.7 K), A5 126.0 C (+20.0 / -12.4 K); 131.0 and 142.1 C as revision 4 drew them (1, 4.2, R5-2 row 1) | `thermal-ts012.md` section 4.1 table; `bands.csv` | Matches |
| A2 | V02 104.4 / 105.6 C OPEN; K7 107.1 / 106.5 C; case 105.7 C against 90 C | Section 5 verdict set V02, V03, V05 | Matches |
| A3 | Inhibit on the PA case: A4 114.2 C nominal FAIL, about 77 C needed; A5 108.3 C and 111.3 C at +3 C, about 81 C needed; sink NTC A4 does not act, A5 at 5.7 min with 110.1 C | Section 4.1 inhibit table; section 6 | Matches (77.1 and 80.9 C) |
| A4 | Surfaces 64.2 / 49.7 C as drawn, 32.3 / 29.5 C with the wrap guard; PETG 66.0 / 59.7 C; cells 58.9 / 55.2 C long session; bay air 67.1 / 61.0 C | V07, V08, V12, V17 | Matches |
| A5 | "A5 two box failures outside their bands, A4 none"; "1.5 to 6.3 K cooler" | Section 5, band-sorted table and paragraph | Matches |
| A6 | In-situ sink 5.6 to 7.9 K/W | Section 3 item 1 (A5 5.6 and 7.2, A4 6.5 and 7.9 K/W) | Matches |
| A7 | A5 nominal 4.09 W, lowest corner 3.19 W; -0.17 to -1.21 dB with the feed and VGG levers; -1.13 to -2.51 dB at the LPF worst case; 2.99 W datasheet minimum | `pa-drive-ts012.md` section 4.4 table, section 5 (c), (d), (f) | Matches. The section 1 and C5-A5 wording "with every lever" departs from the record's own "every lever" (O-13) |
| A8 | A4 nominal 3.06 W, lowest corner 1.69 W, 2.5 dB short with every lever; drive 45.8 to 180 mW; 3f -30.9 dBc | Section 4.3, 4.5, 5 | Matches |
| A9 | Fixed pad 5.4 to 35.5 mW; select-on-test 11.3 to 26.5 mW, +0.54 dB at a +/-1.0 dB reading | Section 4.2 tables; section 5 (a) | Matches |
| A10 | Open loop over 8 W from 7.7 V; 10.68 W at 8.4 V from -10 C | Section 5 (g) | Matches |
| A11 | 97.307(e) A5 7.5 / 9.5 dB, A4 5.5 / 7.5 dB; A4 60 dBc -0.5 / +1.5 dB; loss 0.74 median, 1.76 worst | `lpf-ts012.md` section 5 and run r13 row | Matches. INSP-115 finding-10 (open lien) holds that the 1.76 dB bound mixes board states (board-consistent 1.34 to 1.62 dB), so the study's worst loss is conservative |
| A12 | Image 51 dB (2 + 3); 70.2 dB by 0.2 dB (2 + 3 + 3); 80.1; 72.5 | `rx-bpf-ts012.md` sections 0 and 4 | Matches |
| A13 | MDS A4 -141.5 / -138.7 dBm, A5 -141.2 / -138.0 dBm; half-IF 12 to 16 dB (8 of 16 unconverged) and 34 to 37 dB | Sections 4.5, 4.6 and 7 item 7 | Matches |
| A14 | 3 lines over 25 uW in plan PB; 150.000 MHz at -12.1 dBm; A4 within 0.8 dB | `spurs-ts012.md` sections 1 and 4 | Matches |
| A15 | A4 first-element margin 0.021 V (0.015 V with offset); A4 fails by 0.009 V without a stored trim; A5 fails by 0.045 V, 17 of 72; windows 1.6 to 1.8 x; A5 bandwidth 583 Hz | `keying-ts012.md` section 0, the 4.4.3 table, the section 4 comparison table | Matches; `windows.png` shows A4 -0.169 / +0.211 V against the stored budget -0.107 / +0.190 V and A5 -0.085 / +0.137 V against -0.110 / +0.182 V |
| A16 | REQ-TX-014 A4 -23 to -19 dBm; A5 needs 43 dB | Sections 3 and 8 item 3 | Matches |

Totals: 16 citation checks, 16 match. One is a wording departure (A7, O-13).

### Review verdicts cited (table R5-1) against the review records

| Record | TS-012 statement | Review record at HEAD | Result |
|---|---|---|---|
| Thermal (35fc7ee) | INSP-112 iteration 2 (`d1c403f`) reviewer APPROVED; 4 Major and 10 Minor Verified; finding-15 to 17 open | Front matter `iteration: 2`, `reviewer_verdict: APPROVED`, `findings_open: 3`, product commit `35fc7ee`; verdict block the same | Matches |
| PA drive (5199c5c) | INSP-114 iteration 2 (`1b6c053`) NEEDS CHANGES, Major finding-9; revision 2 answers it; iteration 3 not run | `reviewer_verdict: NEEDS CHANGES`, product commit `9d01aaf` (revision 1); Major finding-9 Open | Matches |
| LPF (92e3805) | INSP-115 iteration 2 (`c5ccea8`) APPROVED; Major 1 to 3 Verified; finding-6 to 11 open | `reviewer_verdict: APPROVED`, `findings_open: 6`, product commit `92e3805` | Matches |
| Receiver BPF (a82f21b) | Iterations 1 and 2 relayed; no record on main; iteration 3 not run | No `analysis-rx-bpf-ts012.md` in `docs/reviews/PDR/checklists/` at HEAD | Matches; a process gap outside TS-012 (X-13) |
| Spurs (5a36ecd) | INSP-113 iteration 2 (`4d02827`) APPROVED; Major 1 and 2 Verified | `reviewer_verdict: APPROVED`, product commit `5a36ecd`; Minor 3 to 12 open (the study does not list them; no effect) | Matches |
| Keying (be86c02) | INSP-116 iteration 2 (`54c028d`) NEEDS CHANGES, Major finding-10; revision 2 answers it; iteration 3 not run | `reviewer_verdict: NEEDS CHANGES`, product commit `e9f1440` (revision 1); Major finding-10 Open | Matches |

### Scoring and ranking arithmetic (revision 5)

- **Matrix totals** (section 5), re-computed from the section 4.2 scores and the weights (sum 100): A1 295, A2 305, A3 285, A4 315, A5 270. Revision 4 re-computed first: A2 325, A3 320, A4 340, A5 335.
- **Weight sensitivity** (16 runs, others rescaled to 100, A2 to A5):
  - The revision 4 figures reproduce: A4 first in 9, A5 in 5, A2 in 2.
  - Revision 5: A4 first in 12, A2 in 4. The four A2 runs are C3 -10 (A2 329.1, A3 295.0), C4 -10 (327.8 against A4 316.7), C5 +10 (316.9 against 300.6) and C6 +10 (315.6 against 291.1). A5 is first in none.
  - Between the finalists, A4 leads in 16 of 16. The smallest lead is 14.4 (C5 +10: 300.6 against 286.2) and the largest 75.6 (C5 -10).
  - At C3 -10, A4 is third (293.2), behind A3; the study names only the top two. That is correct but not complete.
- **Low-cell moves between A4 and A5.** The moves are A4 C1, C2, C5, C8 down and A5 C1, C2, C5, C6, C8 up (A4 C6 is at the floor). None of 9 single moves and none of 36 pairs closes the 45-point gap. 46 of the 84 triples reach a tie or better. The examples in the study reproduce: A5 C1 + C2 + C5 gives a 315 tie; A5 C1 + C5 with A4 C5 gives 310 against 295.
- **A2 single moves** reproduce: C8 +1 (320), C6 +1 (tie 315), A4 C1 -1, C5 -1 (305 against 295), A4 C8 -1 (305 against 300).
- **Joint adverse cases** reproduce. Against A5: A4 365, A3 345, A2 335, A5 230. Against A4: A3 345, A5 340, A2 335, A4 255.
- **Named readings (section 6 item 3)** reproduce:
  - C8 at 2 for both: A5 285.
  - A4's C6 back to 3: A4 335.
  - U3: 315. U2 and U3: 300.
  - Needed-only E5: no score change (C1-A5 3.3; C2-A4 3.2).
- **Risk arithmetic (sections 7.1, 8.2).**
  - Reds: A4 has eight (20, 16, 16, 15, 12, 12, 12, 10); A5 has eight (20, 16, 16, 15, 15, 12, 12, 12).
  - U1 = 8 + 6 - 3 - 5 - 3 - 12 = -9; U2 +8; U3 0; U4 0; total -1. With A5's cost Red, -17.
  - All reproduce.
- **Robustness verdict.** "Robust between the finalists; not robust against A2" names the perturbations, but it is not the 06 section 14.4 verdict (finding-19).

### Estimate against listed-price presentation (re-issue 1)

Nothing estimated is shown as a listed price:
- Row E5 is labelled "est." and E in section 8.3, in every roll-up line and in section 1.
- Its parts not read on a page are marked "(E, not read)": the CLK1 coax and the 2 % grades.
- Its per-part values reuse listed row prices (rows 5, 6, 7, 14 and 26) and the E2 per-value range. They are an estimate built from listed prices, and the study labels them that way.

The Adafruit 1865 read (USD 2.50, out of stock, 2026-09-28) is not carried in any total. It was not re-read by this reviewer. The engineering figures of the analyses are labelled as estimates in section 1 ("every figure an estimate"), in 3.4, in 6 item 5 and in the R5-2 lead-in.

### Findings (iteration 3 re-issue 1)

| Finding | Severity | Item | Location | Description | State | Deferred to |
|---|---|---|---|---|---|---|
| finding-1 | Major | CK-RSK-B5, B8 | TS-012 sections 1, 4.1, 7.1, 7.2, 8.4 | Unchanged in revisions 4 and 5 | Verified (iteration 2; holds on revision 5 at 37d5824) | |
| finding-2 | Major | CK-RSK-B5, B7 | TS-012 sections 2, 3.1 M1, 8.3 | Unchanged; sales tax line 0 | Verified (iteration 2; holds on revision 5) | |
| finding-3 | Major | CK-RSK-B5, B8 | TS-012 sections 4.1 M4, 8.3 row 28 | Unchanged | Verified (iteration 2; holds on revision 5) | |
| finding-4 to finding-13, finding-15, finding-16 | Minor | CK-RSK-B4 to B9 | See iterations 2 and 3 | Unchanged in revisions 4 and 5 | Verified (iterations 2 and 3) | |
| finding-14 | Minor | CK-RSK-B5 | TS-012 sections 7.3, 8.1, 8.12 WP-PDR-22 | 0.654 divider of 1 % E24 values, VGG 3.08 to 3.46 V, tolerances in the WP-PDR-22 deck (revision 4) | Verified (iteration 3 re-issue 1, revision 5 at 37d5824) | |
| finding-17 | Minor | CK-RSK-B8, B9 | TS-012 section 8.2 | A5 envelope-loop row counted in U1 (revision 4); A4 counterpart added from the keying analysis (revision 5) | Verified (iteration 3 re-issue 1) | |
| finding-18 | Minor | CK-RSK-B5, B10 | TS-012 sections 1, 2, 6, 8.9, Q2, Q4 | Status note sections 11 and 13 applied (revision 4); status note 2026-09-28 applied (revision 5); Q4 wording residue is O-15 | Verified (iteration 3 re-issue 1) | |
| <a id="finding-19"></a>finding-19 | Minor | CK-RSK-B7, B9 (06 sections 14.4 items 3 and 4, 14.5) | TS-012 sections 1 ("Robustness verdict: Robust between the finalists"), 5 rank row, 6 items 4 and 6, 8 "Why not A2", 8.13 Q1 ("The owner question stays between A4 and A5") | A2 (305) is 10 points behind A4 and passes every mandatory criterion. Four weight runs and five single Low-cell moves put A2 level with or ahead of A4 (reproduced), so under 06 section 14.4 item 3 the verdict is Not robust. Item 4 then requires either the analysis that would settle the Low cells (named, with cost and gate) or a recommendation of the closely ranked alternatives for the owner's choice. Section 14.5 requires alternatives less than 25 points apart to be presented together. The study adds a "finalist" category that 06 does not have. It gives A2 no value-of-information step and leaves A2 out of Q1. Also, A4 ranks over A2 only because of C8-A2 3 to 2, an evidence-parity inference applied in the matrix without analysing A2 (A2 C8 +1 gives A2 320 against A4 315). The parallel C6 inference, which would lower A2 further, is left to section 6 item 4. The facts are disclosed in sections 1, 6 and 8, and the A4-over-A5 basis is correct, so the owner is not misled on the A4 and A5 choice. But the presentation the process requires is missing, and A2 keeps USB in-radio charging (SI-022, CON-010), which both finalists give up (D2). **Fix:** state the 06 verdict as Not robust, naming the A2 perturbations. Name the value-of-information step for A2 (its C6 and C8 cells) with cost and gate. Either put A2 in Q1 as the closely ranked alternative, with the reasons the study does not recommend it (three flagged parts, a new-old-stock PA not available for export, an LCSC-only charger chain with HZ-002 in the box), or record the owner's concurrence that the choice set is A4 and A5. Apply the evidence-parity reading to A2's C6 and C8 alike in the matrix, or state why only C8 | Open | Lien (rule C1); recommended for the B1a presentation of Q1 (X-16) |
| <a id="finding-20"></a>finding-20 | Minor | CK-RSK-B9 | TS-012 section 8 first bullet ("every discriminating result that moved a score moved it against A5"); 8.13 Q1 ("The analyses the owner approved moved every discriminating score against A5") | Not true as stated. C6 moved A4 by -20 and A5 by -10, and C2 moved A4 by -5 and A5 by 0, so those two changes narrowed A5's deficit by 15 points. The net statement holds (A5 -65, A4 -25), and so does the direction of each discriminating analysis (thermal heat, drive window, low-pack power, first element, cost). But Q1 is the sentence the owner decides on. **Fix:** state the net and name the common changes. For example: "net of the re-scoring A5 fell 65 points and A4 25; the common guard envelope removed A4's C6 advantage" | Open | Lien (rule C1); recommended for the B1a Q1 text (X-16) |
| <a id="finding-21"></a>finding-21 | Minor | CK-RSK-B5, B6 | TS-012 section 4.1 mandatory table (A3 "fail on estimated lines", A5 "conditional"), section 5 rank row, section 6 item 6 | M1 is defined on the worst case before guards, and both A3 and A5 exceed USD 300 on estimated lines. The study reads them differently. A5, at 314.78 (the larger excess), is "conditional", with guards G1 and G2 taken to 298.10. A3, at 308.16 with LCSC merged, is "fail on estimated lines", with no guard applied. A3 shares A5's Mouser order and owner-hardware lines, so the same G1 and G2 give 308.16 - 9.20 - 7.48 = 291.48. Revision 4 read A3 as "conditional" at 287.89. Neither label changes the recommendation, since both are below A4. But the owner is shown A5 passing a mandatory criterion that the study fails A3 on. **Fix:** apply one reading to both, either "fail on estimated lines, scored for information" (section 3.1) or "conditional on the gate guards", and restate the A3 and A5 rows, the rank row and section 6 item 6 | Open | Lien (rule C1) |
| <a id="finding-22"></a>finding-22 | Minor | CK-RSK-B8 (06 sections 4, 6, 7) | TS-012 section 7.1 revision 5 table, rows "A4 New: PETG, bay and surfaces (HZ-003)", "A4 New: REQ-TX-014", "A4 New: envelope loop, first element", "A5 New: REQ-TX-014" | Four new risk rows carry a short name, a score and evidence, but no four-part statement ("Given ..., there is a possibility that ..., adversely impacting ..., leading to ..."). Only the A5 drive-window row has one. These rows count in the section 7.1 aggregate ("eight Reds") and in the section 8.2 risk per dollar, and two of them are Red or HZ-linked. **Fix:** write the four-part statement, with its "would be entered as" target, for each new row | Open | Lien (rule C1); due before the risk writer enters them |
| <a id="finding-23"></a>finding-23 | Minor | CK-RSK-B5, B8; M4 (REQ-SYS-120, HZ-004 K8) | TS-012 section 7.3 drive gating ("CLK1 enable is the second, independent condition of REQ-SYS-120"); section 8.14 D-11 ("GVA-84+ bias and CLK1 enable follow TX_KEY", adopted into the baseline of both finalists); 7.1 A4 REQ-TX-014 row (the step "retires it"); 8.13 follow-on decision 4 | D-11 makes CLK1 enable follow TX_KEY. Section 7.3 still names CLK1 enable as the second, independent condition of REQ-SYS-120 ("both a keyer key-down and a separately maintained PA permit", HZ-004 K8, "no single software fault initiates a transmission"). As written, the second condition would follow the first, and the study does not say what keeps the PA permit independent: for example, whether the gate is hardware on TX_KEY with the permit on a separate line, or whether it is a firmware write. REQ-TX-014 is tagged safety and HZ-004 (the transmitter half of REQ-SYS-120). The study proposes restating its condition by CR, but it has no safety note, and it counts the change as retiring A4's REQ-TX-014 Red at no cost. The ranking does not depend on it: the keying record's option (b), a series drive switch, is a small cost line. But M4 for both finalists rests on REQ-SYS-120 being implemented. **Fix:** state how D-11 keeps REQ-SYS-120's two conditions independent (which signal gates the drive, in hardware or firmware, and which line carries the PA permit). Route the REQ-TX-014 restatement to the HZ-004 analysis (WP-PDR-16, 17) and to the software assurance pair (X-12). If independence cannot be kept, carry option (b) as a cost line | Open | Lien (rule C1); due before the re-baseline CR carries the REQ-TX-014 restatement |

No new finding is Major. On the severity rule the brief sets (Major if the owner would decide on a wrong basis), the owner's choice between A4 and A5 rests on a correct basis. Every analysis figure the study uses matches its record (16 of 16). The roll-ups, the matrix and the sensitivity reproduce. A4 stays first between the finalists under every single and paired Low-cell move, and under a reversal of either contested C8 reading (O-11). finding-19 and finding-20 concern how the choice is framed in Q1, and both are cheap to correct in the owner presentation. finding-21 concerns labels of alternatives below A4. finding-22 is format. finding-23 is a safety-traceability gap in a design item whose fallback costs little.

### Observations (iteration 3 re-issue 1; not findings)

- **O-11.** The section 3.1 range rule was written in revision 4 for scenario ranges (87 to 119 C, 100 to 135 C). Revision 5 applies it to the thermal record's one-at-a-time RSS bands. Both finalists are nominal FAILs in that record (V01), and the C8 split between them (A4 2, A5 1: 15 points) rests on A4's lower band edge sitting 2.1 K under 110 C and A5's 3.6 K over it. The record's revision 0 reported full-stack ranges (A5-DC 97 to 174 C, A4-DC 92 to 174 C) that both span 110 C. Every reading of the rule leaves A4 ahead by at least 30:
  - both at 2: A4 315, A5 285;
  - both at 1: A4 300, A5 270;
  - A4 at 1 and A5 at 2 (both moves adverse to A4): A4 300, A5 285, a 15-point lead that 06 section 14.5 would present together.

  The study states only the first. Worth one sentence in section 6 item 3.
- **O-12.** Section 4.2 C8-A2 says the model "put both analysed PAs 20 to 40 K above their catalog-rating estimates (A4 100 to 135 C to 122.7 C ...)". 122.7 C lies inside A4's revision-4 range. It is 12 to 26 K above A4's revision-1 path values (97 to 111 C). For A5 the rise is 39 K on the catalog-rating case. A2's 92 C plus 12 to 40 K still spans 110 C, so C8-A2 = 2 holds, but the stated basis is loose.
- **O-13.** Section 1 item 2 and the C5-A5 cell say "with every lever -0.17 to -1.21 dB". In the PA drive record, "every lever" (section 5 (e): feed 0.26 ohm, VGG 3.46 V and 0.5 dB output loss) reaches 3.97 W in all but the hottest cases. The TS figures are the C2 and C3 levers at the LPF median, as R5-2 row 5 correctly says. The conclusion ("not shown") holds, because no LPF build meets 0.5 dB.
- **O-14.** Sections 8.5 and EX-11 still give A5 as 153 x 70 x 42 mm, a mass of 286 to 361 g and a sink of 30 to 60 g "not read". The thermal record read the sink at 57 g, and C6, 8.10 REQ-SYS-102 and 103 and Q6 carry 167 x 74 x 52 mm and 311 to 371 g. Section 8 says sections 8.1 to 8.12 are re-issued after the choice, which covers this. EX-11 is an owner exception, though, and should not be asked at the stale size. D-7's select-on-test pad needs a set of 14 E24 1 % pad values from "owned resistors". The owner has not answered on the tolerance (status note 2026-09-28 section 1), so for A5 the set may fall on the E2 allowance (A5 only; no ranking effect).
- **O-15.** Q4's recommendation still reads "The tinySA Ultra (if not yet bought), a thermocouple (USD 9.95)". The tinySA is now known not to be bought, and the thermocouple became a K-type thermometer (EX-13, D-16). The cost basis (equipment cap) is unchanged.
- **O-16.** 298.10 after G1 and G2 is the difference of truncated steps. The exact value is 298.1145 (298.11 truncated). Immaterial.

### Readiness (iteration 3 re-issue 1)

| # | Criterion | Result | Evidence |
|---|---|---|---|
| R1 | `validate_docs.py` exits 0 | **No** | Before this delta: `validate_docs: 107 passed, 8 failed, 115 checked`, exit 1. The 8 failures are other records: the CM plan SA, configuration status, lessons learned, SRR ADRs 001 to 025, process 02, TV-001 to 010, TS-001 and TS-002, and the TS-002 SA. None involves TS-012. This record passes (Commands) |
| R2 | Section A | N/A | Trade study |
| R3 | Sections 1 to 9 filled; section 10 empty | Yes | Section 10 decision fields empty; revisit conditions updated for revision 5 |
| R4 | Decision need and gate | Yes | Header "Decide by": B1a 2026-09-29, no later than B1b 2026-10-01 |

### B. Trade study items re-answered (iteration 3 re-issue 1)

| Id | Answer | Evidence |
|---|---|---|
| CK-RSK-B1 to B4 | Yes | As at iteration 3; no alternative added or pruned; criteria and weights unchanged since revision 2 |
| CK-RSK-B5 | Yes (liens) | 16 of 16 analysis citations match their records. The review verdicts are cited correctly (6 of 6). Three records are under re-review and disclosed as such (X-13). Liens: finding-21 (M1 reading), finding-23 (REQ-SYS-120 under D-11) |
| CK-RSK-B6 | Yes | Totals, interpolations, C6 volumes, E5 and every roll-up reproduce |
| CK-RSK-B7 | Yes (lien) | 16 weight runs, every single, paired and triple move, the joint cases and the named readings reproduce. The verdict wording and the value of information for A2 are finding-19 |
| CK-RSK-B8 | Yes (liens) | Revision 5 lists 14 existing rows (8 re-scored) and adds 5, with the analysis that sets each. Four new rows lack the four-part statement (finding-22); D-11's safety link is finding-23 |
| CK-RSK-B9 | Yes (liens) | A4 has the highest total among all scored alternatives (315) and is recommended; the A4-over-A5 case follows from the evidence. Liens: A2 presentation (finding-19), Q1 wording (finding-20) |
| CK-RSK-B10 | Yes | Section 9 carries tables R5-1 and R5-4, the author's revision 5 dissent (the C8-A5 reading against the thermal record's) and the revision 4 dispositions; section 10 is empty |

### Cross items (iteration 3 re-issue 1, returned to Claude)

- **X-12.** The software assurance pair (X-2, X-5, X-9) is still not filed. `docs/reviews/PDR/checklists/` has no `ts-012-design-to-cost-software-assurance.md` at HEAD `37d5824`. The record verdict still waits for it. finding-23 (REQ-SYS-120 and the REQ-TX-014 restatement) is in its scope.
- **X-13.** Three records that revision 5 scores on are under re-review. PA drive (INSP-114 iteration 3) and keying (INSP-116 iteration 3) feed C5-A5. The receiver BPF record feeds E5 (a) and the MDS rows, and its review has no record on main. The review of the receiver record should be filed as a record (charter section 5: the filled checklist is the single record). Section 10's revisit conditions name the risk. The most adverse pending pair for A4 is C5-A5 back to 5 and C8-A5 read as 2, which gives A4 315 and A5 305: 10 points apart, which 06 section 14.5 would present together.
- **X-14.** The owner's item 3 authorized the fourth iteration "on TS-012 revision 4". This pass reviewed revisions 4 and 5 together. The lead SE should record that reading in the status note. Revision 6 (sections 8.1 to 8.12 re-issued for the chosen alternative, and any fix of finding-19 to 23) changes the blob and needs a further delta. Rule C1 escalates that to the owner again.
- **X-15.** Search-order deviation of this invocation (one heading listing of two known files before the first `search_code` query; see "Search first" above), for the lessons-learned log, alongside the author deviation of X-10.
- **X-16.** For the B1a presentation of Q1: present A2 as the closely ranked alternative, or ask the owner to confirm the A4 and A5 choice set (finding-19). Use the net wording of finding-20. Neither needs a TS revision before the owner is asked; both can be applied in revision 6.

### Commands (iteration 3 re-issue 1)

```
git rev-parse HEAD                                                                    # 37d5824e30348728142f74dbb7ddf45939c2b60b
git rev-parse 7d0d450:<TS-012 path> 37d5824:<TS-012 path> HEAD:<TS-012 path>         # fa41032e..., 731ba0eb..., 731ba0eb...
git hash-object docs/decisions/trade-studies/TS-012-design-to-cost-hand-built.md       # 731ba0ebe494c1d970b3b1ba0cac4304ebbab412
git show --stat 7d0d450; git show --stat 37d5824                                     # each changes only the TS file
git log --oneline -- <review records of INSP-112 to INSP-116>                          # d1c403f, 1b6c053, c5ccea8, 4d02827, 54c028d
/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/validate_docs.py   # before the delta: 107 passed, 8 failed, 115 checked (exit 1)
  after the delta: see the record commit; this record PASS, the same 8 records fail
python3 (scratchpad sens.py): matrix totals for revisions 4 and 5; 16 weight runs each; all 1-, 2- and 3-move combinations between A4 and A5;
  A2 single moves; joint adverse cases; E5, A4, A5, A2, A3 roll-ups; interpolation; C6 volumes; risk points
python3 re-reads of docs/design/analysis/{thermal,pa-drive,lpf,rx-bpf,spurs,keying}-ts012.md and bands.csv, verdict_set.csv (V01)
docs/requirements/sys/requirements.json REQ-SYS-120; docs/requirements/tx/requirements.json REQ-TX-014 (tags safety, HZ-004)
Plots opened and checked: thermal margins_vs_band.png; tx-pa r2-s1-summary pout_at_sma_vs_pack.png; tx-pa r1-d2 drive_a5_corners.png;
  tx-keying r2-summary windows.png. Every plot path TS-012 names resolves to a file at HEAD (script check, relative names resolved by hand)
```

### Measurements (iteration 3 re-issue 1)

size = 6 alternatives, 13 criteria, 10 re-scored cells, 16 analysis citations, 6 review verdicts, 19 risk rows; turns = 45; minutes = 85; major = 0 new (3 Verified); minor = 5 new (finding-19 to 23), 3 Verified this pass (finding-14, 17, 18).

### Record verdict and verdict format (iteration 3 re-issue 1)

`reviewer_verdict: APPROVED`. The three Major findings stay Verified, and no Major is open. finding-14, 17 and 18 are Verified on revision 5. The new Minor findings 19 to 23 are liens (rule C1), with the TS-012 author as owner. finding-19 and finding-20 are recommended for the owner-facing Q1 before B1a (X-16), and finding-23 is due before the re-baseline CR carries the REQ-TX-014 restatement.

The record `verdict` stays NEEDS CHANGES, for two reasons:
- the software assurance pair is still not filed (07 section 2.1.1; `assurance_verdict: pending`; X-12);
- readiness R1 fails on records unrelated to TS-012.

When the pair returns APPROVED and R1 holds, the lead SE sets `verdict: APPROVED`, provided `git rev-parse HEAD:<path>` still equals `731ba0eb`. A changed blob needs a further delta, which rule C1 escalates to the owner (X-14).

```
VERDICT: APPROVED (reviewer); record verdict held for the software assurance pair and readiness R1
PRODUCT: docs/decisions/trade-studies/TS-012-design-to-cost-hand-built.md@731ba0eb (revision 5, 37d5824), delta from @fa41032e (revision 4, 7d0d450)
FINDINGS:
- [Major] finding-1, finding-2, finding-3: Verified (hold on revision 5).
- [Minor] finding-14, finding-17, finding-18: Verified (fixed in revision 4, held in revision 5).
- [Minor] CK-RSK-B7, B9 sections 1, 6, 8, Q1: A2 is 10 points behind A4 and takes the top in 4 weight runs and 5 single moves; 06 14.4 and 14.5 need "Not robust" and A2 presented or analysed; A4 over A2 rests on the inferred C8-A2 change (finding-19).
- [Minor] CK-RSK-B9 section 8, Q1: "every discriminating score moved against A5" is not true for C6 and C2; state the net (finding-20).
- [Minor] CK-RSK-B5, B6 section 4.1: A5 (314.78) "conditional" with guards, A3 (308.16) "fail" without; one M1 reading for both (finding-21).
- [Minor] CK-RSK-B8 section 7.1: four new risk rows lack the four-part statement (finding-22).
- [Minor] CK-RSK-B5, B8, M4 sections 7.3, 8.14 D-11: drive gating on TX_KEY makes the REQ-SYS-120 second condition (CLK1 enable) follow the first; independence not stated; REQ-TX-014 (safety, HZ-004) restated without a safety note (finding-23).
ITEMS N/A: CK-RSK-A1 to CK-RSK-A11 (product is a trade study)
MEASUREMENTS: size=6 alternatives, 13 criteria, 16 citation checks, 6 verdict checks; turns=45; minutes=85; major=0 new; minor=5 new; verified=18; open=5
```

## Iteration 3 re-issue 2: delta on TS-012 revision 6 (2026-09-29, HEAD `123f048`)

**Authority and scope (rule C1, rule C2).** Re-issue 1 was the owner-authorized fourth iteration. After it, the software assurance pair INSP-118 returned three Major findings, and the owner authorized TS-012 revision 6, this further INSP-110 iteration and INSP-118 iteration 2. The authorization is status note `docs/plan/status/status-2026-09-29.md` section 2, verbatim "Yes both recs sound good". The front matter keeps `iteration: 3`, the schema maximum, and this pass is recorded as "Iteration 3 re-issue 2" (the fifth pass). The pass is a delta on revision 6. It verifies:
- the three INSP-118 Major fixes as the study carries them;
- finding-19 and finding-20 in Q1, finding-23, and INSP-114 X-7;
- the table R5-1 citations against the review records, including INSP-117's current state;
- the roll-ups with the TCXO required, the re-scoring, the totals, the weight runs and the robustness arithmetic, all reproduced;
- that the recommendation follows.

New findings are raised only where revision 6 introduced the defect. Findings 1 to 18 are not re-opened.

**Product.** Revision 6 is blob `0c9fcb96` at `3b93de1`, Status Proposed, 1248 lines. `git rev-parse 3b93de1:<path>`, `git rev-parse HEAD:<path>` and `git hash-object <path>` all give `0c9fcb96` at HEAD `123f048`. `git show --stat 3b93de1` lists only the TS file (244 insertions, 129 deletions against `37d5824`). The two later commits (`63122e7`, `123f048`) do not touch TS-012. `tools/check_commit_msg.py --range 3b93de1^..3b93de1` gives PASS (`Refs: TS-012, INSP-110, INSP-118`), so INSP-118 finding-8's request for the revision 6 commit is met. The checklist is as before: `peer-review-checklist-risk.md` revision A, section B.

**Independence (rule C4).** This invocation authored no part of TS-012 revisions 1 to 6. It did not author `frequency-budget.md`, the six analysis records or their runs, INSP-112 to INSP-118, or earlier iterations of this record. It edited no product file and changed only this record.

**Search first (charter section 11 rule 1).** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran first ("TS-012 design-to-cost trade study INSP-110 review record iteration 3 re-issue"). After it, `grep` and `sed` only read known paths. No deviation.

**Author's claims checked.** Each author claim was checked directly:
- The commit is TS-only and its message passes the checker.
- `validate_docs.py` gives 109 passed and 8 failed of 117. The 8 failures are the same unrelated records as at re-issue 1, and none involves TS-012.
- The brief's path "frequency-budget-and-clock-plan.md" is the INSP-056 record (`docs/reviews/PDR/checklists/analysis-frequency-budget-and-clock-plan.md`). The analysis itself is `docs/design/analysis/frequency-budget.md`, as the author says.

### Verification of the INSP-118 Major fixes as reflected in the study

| INSP-118 finding | Fix required (INSP-118 "Fix") | Revision 6 text | Reviewer check | Result |
|---|---|---|---|---|
| finding-1 (REQ-SYS-182, REQ-SYS-154) part 1 | Replace the budget with the `frequency-budget.md` method, per finalist | Section 7.3 "Revision 6: frequency verification"; section 8.10 row REQ-SYS-182, 154; the revision 5 budget withdrawn | Re-ran the committed checker functions (`hardware/sim/freq/freq_budget.py`): `healthy_disagreement("R3",12)` = 4517.996 Hz, `("R3",13)` = 2517.996 Hz; `undetected_bound("R3",12)` = 9517.996 Hz; `fc0_accuracy_ceiling(12)` = 560.25 Hz; `tx_detection_time(13)` = 46 ms; R1 with 2.5 ppm: d 13 989.9 Hz (interval 12), 11 989.9 Hz (13), `min_154_limit` 23 609.8 Hz (13). A4 on R1 at 30 ppm by the same formula: d 18 059.9 Hz (12) and 16 059.9 Hz (13); REQ-SYS-154 floor 27 679.8 Hz (13). XOSC 65 ppm x 147.9988 MHz = 9 619.9 Hz. Margins 5 000 - 4 518 = 482 Hz and 12 000 - 4 518 - 5 000 = 2 482 Hz. The study's 16.1, 27.7, 12.0 and 23.7 kHz are the checker values rounded up to 0.1 kHz (the note's `ceil1` convention) | **Verified** |
| finding-1 part 2 | Put the TCXO in A4 with route R3, or record the CR deltas with Q1; add R3's second GPIN for A5 | TCXO required in A4 (D-17; row 29 at USD 3.61); R1 deltas stated and not proposed; GPIN1 route in the section 8.1 diagram for both; G5 withdrawn; Q1, Q5 and the section 1 findings say the TCXO is required | Roll-ups and C3 below. The TCXO path is stated, but its squaring stage is not shown to work (finding-25, new) | **Verified** (lien finding-25) |
| finding-1 part 3 | Restate the key-down sequence so the pre-PA_EN check fits the 12 ms lead-in, consistent with D-11 | Sequence: 1 ms (I2C writes and PLL settle, allocated and flagged unsourced), interval 12 from t0 + 1 to t0 + 5 ms, 2 ms software, PA_EN at t0 + 7 ms, TX_KEY at t0 + 8 ms, ramp at t0 + 10 ms; fallback on interval 13: check ends at t0 + 11 ms, ramp at t0 + 11.5 ms | 1 + 4 + 2 = 7 ms; 1 + 2 + 10 = 13 ms against REQ-SYS-160's 15 ms; lead-in 10 ms against REQ-SYS-161's 12 ms. On the fallback, 1 + 8 + 2 = 11 ms, and 1 + 2 + 11.5 = 14.5 ms against 15 ms. The 1 ms relock allocation is disclosed as open, with a revisit condition (section 10) | **Verified** |
| finding-1 part 4 | Requests to WP-PDR-20, 35, 16b | Section 7.3 "Requests" and the section 8.12 rows WP-PDR-20, 35 and 41, 36a, and 16 and 17 | Present | **Verified** |
| finding-2 (REQ-SYS-181 for A4) parts 1 and 2 | State per finalist where the sensor sits and the trip junction; read the AFT05 junction rating | NTC-2 on the A4 tab copper (D-6; the 8.10 REQ-SYS-181 row); AFT05MS004N Rev. 0, 7/2014, read | This reviewer fetched the NXP datasheet, SHA-256 `84cd9fae...6dd036`, the same file the study names. `pdftotext`: "Operating Junction Temperature Range (1,2) TJ -40 to +150 C", "Case Operating Temperature Range ... -40 to +150", "Total Device Dissipation @ TC = 25C ... 28 W", "Thermal Resistance, Junction to Case ... 4.4 C/W", Figure 3 "MTTF versus Junction Temperature". `inhibit.csv` rows A4-DC: `case_minus_reading_at_first_off` 4.5009 K (nominal, p_pa 5.5506 W) and 10.4355 K (all adverse, p_pa 6.8561 W, `a4_rjc=4.84`). 95 + 4.50 + 5.55 x 4.4 = 123.9 C; 98 + 4.50 + 24.42 = 126.9 C; 98 + 10.44 + 6.856 x 4.84 = 141.6 C, which is 8.4 K under 150 C. The offset limit is 150 - 98 - 33.2 = 18.8 K. The nominal steady tab reading is 122.7 - 5.55 x 4.4 - 4.5 = 93.8 C. `trips.csv`: `hw_sink` nan for A4-DC | **Verified** |
| finding-2 parts 3 and 4 | M4-A4 conditional; A4 values to thermal R-3 and WP-PDR-16b | M4-A4 "pass on the revision 6 conditions", revision 5's pass withdrawn; routed to WP-PDR-16b (HZ-003 K9) and the REQ-SYS-181 writer; revisit condition on the bench NTC offset | Present. The monotonic argument (a hotter box only makes a device-side sensor trip sooner) holds for the lumped model | **Verified** |
| finding-3 (REQ-SYS-120 permit) parts 1 and 2 | Name PA_EN and what it gates in hardware; say whether D-11 is hardware or firmware | PA_EN is a GPIO with a 4.7 k pull-down, written only by SW-SAFE. A 74LVC1G10 NAND of TX_KEY, PA_EN and Q drives a gate-bias clamp FET and the gate of a GVA-84+ supply P-FET (D-18). D-11 is that hardware gate; CLK1 enable is a firmware I2C action and no longer a condition | Logic checked: NAND output high (any input low) turns the clamp on and the P-FET off; all three high releases both. A single stuck line leaves the bias clamped. The P-FET half is not realisable as drawn from a 3.3 V NAND on the 5 V bus (finding-24, new). The clamp half carries REQ-SYS-120 on its own | **Verified** (lien finding-24) |
| finding-3 parts 3 and 4 | REQ-TX-014 restatement with an HZ-004 note, or option (b) as a cost line; reconcile D-11 with the pre-PA_EN check | Restatement with its HZ-004 note (8.10); follow-on decision 4 after WP-PDR-16, 17 and INSP-118 iteration 2; CLK1 runs from the changeover, so the counter works before PA_EN | Key-up path estimate reproduced from `keying-ts012.md` section 4.5 (the REQ-SYS-183 table): A4 +10.4 - 18 - 20 - 39 = -66.6 dBm; A5 +10.4 - 18 - 20 - 3 - 30 = -60.6 dBm; CLK1 off: -117 and -111 dBm. The -20 dB "GVA-84+ unpowered" term is the keying note's estimate, and it assumes the driver is unpowered (finding-24) | **Verified** (lien finding-24) |

### INSP-110 liens and INSP-114 X-7

| Item | Required | Revision 6 text | Result |
|---|---|---|---|
| finding-19 | State the verdict as Not robust, naming the A2 perturbations. Name the value-of-information step for A2, with cost and gate. Put A2 in Q1 or record the owner's concurrence. Apply the parity reading to A2's C6 and C8 alike, or say why only C8 | Section 1 and R6-5: "Not robust", with the A2, A3 and A4 + U3 weight runs named. R6-4 names the A2 analysis: the WP-PDR-28 re-run on A2's layout, the WP-PDR-21 runs for the RD01/RD07 line-up and the gate reads; about two working days plus reviews, no money, gate before the Q1 decision. Q1 presents A2 with its reasons and asks the owner to confirm the A4 and A5 choice set or order the analysis. Section 4.2 (revision 6 paragraph) says why C6 is not moved by parity: the finalists' C6 loss comes from their own sink-end layout, which A2 does not have. It carries C6 as a named reading (A2 275 to 295). Section 8 "Why not A2" follows 06 section 14.5 | **Verified** |
| finding-20 | State the net and name the common changes in Q1 | Section 8 "How the ranking got here (net)" and Q1: A5 -65 and the recommended A4 -40 since revision 4. The guard envelope removed A4's C6 advantage (A4 -20, A5 -10), C2 fell for A4 only, and revision 6 took 30 from A4 on C3 and gave back 20 on C5. Reviewer: 340 - 20 (C6) - 5 (C2) - 30 (C3) + 20 (C5) - 5 (C2 with the ring) = 300; 335 - 65 = 270 | **Verified** |
| finding-23 | State how REQ-SYS-120's two conditions stay independent; route the REQ-TX-014 restatement to the HZ-004 analysis and the assurance pair | As INSP-118 finding-3 above | **Verified** (the realisation defect is finding-24) |
| finding-21 | One M1 reading for A3 and A5 | Unchanged; the A3 row now names the lien | Open (lien, rule C1) |
| finding-22 | Four-part statements for four revision 5 rows | Unchanged; section 7.1 names the lien | Open (lien, rule C1) |
| INSP-114 X-7 | Correct the "with every lever" wording | Sections 1 item 2 and C5-A5: the C2 and C3 levers give -0.17 to -1.21 dB at the filter median; every lever at its best gives -0.45 to +0.84 dB and needs a 0.5 dB filter that no build meets. Matches `analysis-pa-drive-ts012.md` X-7 | **Verified** (also closes O-13) |

### Review verdicts cited (table R5-1, revision 6) against the records at HEAD `123f048`

| Record | TS-012 revision 6 statement | Review record at HEAD | Result |
|---|---|---|---|
| Thermal | INSP-112 iteration 2 (`d1c403f`), reviewer APPROVED; 4 Major and 10 Minor Verified; finding-15 to 17 open | `iteration: 2`, `reviewer_verdict: APPROVED`, `findings_verified: 14`, `findings_open: 3`, product `35fc7ee` | Matches |
| PA drive | INSP-114 iteration 3 (`f5960d3`), reviewer APPROVED; finding-9 and 3 to 8 and 10 Verified; lien finding-11; X-7 applied; X-8 no figure changed | `iteration: 3`, `reviewer_verdict: APPROVED`, `findings_verified: 10`, `findings_open: 1` (finding-11, "No figure changes"), product `5199c5c`; X-7 and X-8 as cited | Matches |
| LPF | INSP-115 iteration 2 (`c5ccea8`), reviewer APPROVED; Major 1 to 3 Verified; 6 to 11 open | `reviewer_verdict: APPROVED`, `findings_verified: 5`, `findings_open: 6`, product `92e3805` | Matches |
| Receiver BPF | INSP-117 iteration 3 (`e647ab1`) NEEDS CHANGES, Major finding-7; iteration 4 authorized and "in progress"; D-15 2 + 3 + 4 at IF 8 MHz, residual limit +/-0.97 %; image "about 79.4 dB over -10 to +45 C" | Correct when `3b93de1` was committed. **Superseded at HEAD.** Note revision 4 (`63122e7`) and INSP-117 iteration 3 re-issue 1 (`123f048`): `reviewer_verdict: APPROVED`, product `63122e7`, finding-7 Verified. The note gives the 2 + 3 + 4 worst case over REQ-SYS-114 as 75.37 dB (+5.37 dB) hot at the +/-0.3 % estimate, the limit over temperature as +/-0.64 %, the alignment acceptance as +/-0.62 %, the room limit as +/-0.95 % (the +/-0.97 % "0.01 % on the unsafe side") and whole-chain isolation as about 89 dB. The MDS figures the study quotes (-141.1 / -136.3 dBm A4, -140.7 / -134.9 dBm A5) match the note's section 8 table | Stale since `63122e7`; the study's own revisit condition triggered (finding-26, new; INSP-117 X-R4-1) |
| Spurs | INSP-113 iteration 2 (`4d02827`), reviewer APPROVED; Major 1 and 2 Verified | `reviewer_verdict: APPROVED`, product `5a36ecd` | Matches |
| Keying | INSP-116 iteration 3 (`810850b`), reviewer APPROVED; finding-10 and 11 to 14 Verified; liens 4 to 9 and 15; X-8 | `iteration: 3`, `reviewer_verdict: APPROVED`, `findings_verified: 8`, `findings_open: 7`, product `be86c02`; X-8 as cited | Matches |
| Frequency budget (cited in 7.3) | "INSP-056 APPROVED" | `analysis-frequency-budget-and-clock-plan.md`: `reviewer_verdict: APPROVED`, `verdict: NEEDS CHANGES` (held for its assurance pair and the CR-012 template) | Reviewer verdict matches; the record verdict is held (O-17) |

All six analysis records are now reviewer APPROVED at HEAD. The study's R6-6 statement "five ... APPROVED; the receiver's iteration 4 in progress" is one step behind (finding-26).

### Roll-up re-add (revision 6)

| Quantity | TS-012 | Reviewer | Result |
|---|---|---|---|
| E5 item (g), low / high | 0.30 / 1.50 | NAND 0.10 + clamp FET 0.10 + buffer 0.10 + P-FET 0 = 0.30; 0.40 + 0.30 + 0.40 + 0.40 (row 23) = 1.50 | Reproduced |
| E5 revision 6 | 5.49 / 12.31 / 19.13; needed items 2.90 to 12.93 | 5.19 + 0.30; midpoint 12.31; 17.63 + 1.50; 2.60 + 0.30 and 11.43 + 1.50 | Reproduced |
| A5 subtotal and capped | 183.66 / 216.38 / 275.23; 211.20 / 248.83 / 316.51 | 183.36 + 0.30, 215.48 + 0.90, 273.73 + 1.50; x 1.15 = 211.209 / 248.837 / 316.5145; contingency 27.54 / 32.45 / 41.28 | Reproduced (truncated) |
| A5 after G1, G2 | 307.31; 299.83, margin 0.17 | 316.5145 - 9.20 = 307.3145; - 7.475 = 299.8395 | Reproduced; exact margin 0.16 (O-18) |
| A5 without E5 (f) | 309.38 | (275.23 - 6.20) x 1.15 = 309.3845 | Reproduced |
| A4 subtotal and capped | 149.84 / 179.06 / 234.41; 172.31 / 205.91 / 269.57 | 145.93 + 3.61 + 0.30; 174.55 + 3.61 + 0.90; 229.30 + 3.61 + 1.50; x 1.15 = 172.316 / 205.919 / 269.5715 | Reproduced |
| A4 + U3 | 174.91 / 208.51 / 272.17 | + 2.60 capped | Reproduced |
| Cost of the three conditions (section 1) | USD 5.19 capped at planning | 3.61 x 1.15 + 0.90 x 1.15 = 4.1515 + 1.035 = 5.19 | Reproduced |
| A2, A3 re-rolls | 194.19 / 255.62; 253.72 / 309.89 / 332.89 | + 1.035 and + 1.725 on the revision 5 figures | Reproduced (A3 rounded, not truncated; immaterial) |
| Needed-only E5 (R6-3) | A5 243.78 / 309.38; A4 200.86 / 262.44; A4 + U3 203.46 / 265.04 | 242.748 + 1.035; 307.66 + 1.725; 195.678 + 1.035 + 4.15; 256.565 + 1.725 + 4.15; + 2.60 | Reproduced |
| Differences | A5 - A4 42.92; A5 - (A4 + U3) 40.32; U1 + U3 + U4 42.92 | 248.83 - 205.91; 248.83 - 208.51; 36.88 + 2.60 + 3.44 | Reproduced |
| Mouser merchandise | about 96.38 to 124.52 | 96.08 + 0.30; 123.02 + 1.50 | Reproduced |
| EX-10 | planning 48.83 over the target; 16.51 over; 299.83 | as above | Reproduced |

No estimate is shown as a listed price. Item (g) is labelled E, with row prices where it reuses them (row 23). The TG2520SMN is the listed row 29. The TCXO's 0.8 Vpp minimum output is labelled "as summarized by a web search ... not read directly" and is sent to the gate reads.

### Scoring, totals, weight runs and robustness (reproduced)

- **Cells (section 4.2).** C3-A4 goes from 5 to 3 on the anchor (one flagged part, the leadless TCXO). The other interpolations are unchanged:
  - C1-A4: 5 - 2 x 5.91 / 50 = 4.76, and 4.66 with the ring;
  - C2-A4: 3 - 2 x 9.57 / 40 = 2.52, and 2.39 with the ring (scores 2);
  - C1-A5 3.05; C2-A2 3.22; C1-A3 2.85.

  C5-A4 is 2 alone and 3 with the TCXO and the ring together. That is revision 5's U2 plus U3 reading, which re-issue 1 reproduced at 300.
- **Totals (section 5).** A2 305, A3 285, A4 285, A4 + U3 300, A5 270. Reproduced. The revision 5 totals (A4 315, A2 305, A3 285, A5 270) reproduce first.
- **Weight runs (R6-1; 16 runs, others rescaled to 100).**
  - Revision 5 is reproduced first: A4 12, A2 4.
  - With A4 + U3: A2 first in 10, A4 + U3 in 4 (C2 -10: 310.5 against 305.5; C3 +10: 300.0 against 280.9; C5 -10: 300.0 against 293.1; C6 -10: 322.2 against 294.4), A3 in 2 (C1 -10: 283.1; C4 +10: 308.9), A5 in none.
  - A4 + U3 against A5: first in 16 of 16, smallest lead 8.8 (C1 -10), largest 51.2 (C1 +10).
  - With A4 alone: A2 11, A4 3, A3 2. A4 against A5 is first in 13, and A5 leads at C1 -10 (266.2 against 258.1), C2 -10 (287.9 against 283.4) and C5 +10 (286.2 against 274.4).
  - All reproduced.
- **Low-cell moves (R6-2).** The Low cells are as in revision 5.
  - A2 against A4 + U3 (5 points): 8 of 8 favourable single moves tie or reverse the order; 7 adverse single moves widen A2's lead (to 320 against 300).
  - A5 against A4 + U3 (30 points): 9 moves; 0 of 9 singles, 19 of 36 pairs and 81 of 84 triples reach a tie or better.
  - A5 against A4 (15 points): 6 of 9 singles, 35 of 36 pairs.
  - All reproduced.
- **Joint adverse cases.** Against A5: A4 + U3 350, A3 345, A2 335, A5 230. Against A4 + U3: A3 345, A5 340, A2 335, A4 + U3 240. Against A2: A4 + U3 350, A3 345, A5 340, A2 255. Reproduced.
- **Named readings.** C8-A5 at 2 gives A5 285. A2 with C6 lowered by 1 to 3 gives 295, 285 or 275. Reproduced.
- **Robustness verdict.** "Not robust" (06 section 14.4 item 3) is correct. The top rank changes in 6 of 16 weight runs and under every single favourable Low-cell move. Between the finalists the order holds on weights and against every single move (30 points, over the 25-point rule). Item 4 is met by the named A2 analysis, and section 14.5 by presenting A2 with the finalists.
- **Risk (7.1, 8.2).**
  - A4 Reds: eight, less the 30 ppm Red (retired) and REQ-TX-014 (12 to 6, Yellow), which leaves six, maximum 20. A5 has eight.
  - U1 = 8 + 0 - 3 - 5 - 3 - 12 = -15. U2 has left the upgrade set (common). U3 and U4 are 0. The total is -15, and -31 with A5's cost Red.
  - Reproduced. The REQ-TX-014 Yellow for A4 depends on the unpowered driver (finding-24).

**Does the recommendation follow?** Yes, on the evidence:
- A4 + U3 has the highest total between the finalists. It leads A5 by 30 in every weight run and against every single Low-cell move. Every discriminating analysis still goes against A5 (heat, drive window, low-pack power, first element, cost).
- The three assurance conditions cost USD 5.19 capped and 15 points net, and they leave the order unchanged.
- A2 is ranked first but unanalysed. It is presented as 06 section 14.5 requires, with named reasons (supply of the NOS PA, three flagged parts, HZ-002 in the box, the LCSC-only chain) and a costed analysis. The owner is asked to confirm the choice set.

New findings 24 to 26 concern the circuit realisation of two design items and superseded receiver figures that are common to both finalists. None moves a score or the order.

### Findings (iteration 3 re-issue 2)

| Finding | Severity | Item | Location | Description | State | Deferred to |
|---|---|---|---|---|---|---|
| finding-1 to finding-3 | Major | CK-RSK-B5, B7, B8 | See iteration 2 | Unchanged in revision 6 | Verified (iteration 2; hold on revision 6 at `3b93de1`) | |
| finding-4 to finding-18 | Minor | CK-RSK-B4 to B10 | See iterations 2, 3 and 3 re-issue 1 | Unchanged in revision 6 | Verified | |
| finding-19 | Minor | CK-RSK-B7, B9 | TS-012 sections 1, 4.2, 6 R6-4 and R6-5, 8, Q1 | Not robust stated; A2 analysis named with cost and gate; A2 in Q1 with the choice-set question; C6 parity reasoning stated | Verified (iteration 3 re-issue 2, revision 6) | |
| finding-20 | Minor | CK-RSK-B9 | TS-012 section 8, Q1 | Net wording with the common changes named | Verified (iteration 3 re-issue 2) | |
| finding-21 | Minor | CK-RSK-B5, B6 | TS-012 section 4.1 | Unchanged (A3 309.89 "fail", A5 316.51 "conditional") | Open | Lien (rule C1) |
| finding-22 | Minor | CK-RSK-B8 | TS-012 section 7.1 | Unchanged | Open | Lien (rule C1) |
| finding-23 | Minor | CK-RSK-B5, B8; M4 | TS-012 sections 7.3, 8.10, 8.14 D-11, D-18 | PA_EN named; hardware NAND with TX_KEY and Q; D-11 restated; REQ-TX-014 restatement with an HZ-004 note routed to WP-PDR-16, 17 and INSP-118 iteration 2 | Verified (iteration 3 re-issue 2; realisation lien finding-24) | |
| <a id="finding-24"></a>finding-24 | Minor | CK-RSK-B5, B8 (REQ-TX-014, HZ-004) | TS-012 section 7.3 "Hardware gate (D-18)" item (ii); section 8.14 D-18; row E5 (g); section 8.1 diagram "(supply P-FET on the NAND output)"; section 7.1 revision 6 row A4 REQ-TX-014 | **The GVA-84+ supply P-FET cannot be switched off by the NAND as drawn.** The GVA-84+ runs from the 5 V bus (`pa-drive-ts012.md` inputs: "GVA-84+ 0.108 A typ" on the 5 V bus; section 8.1 "3rd DMP3099L -> TX 5 V"). The 74LVC1G10 takes TX_KEY and PA_EN from the RP2350 at 3.3 V, so it runs at 3.3 V, and its output high is at most 3.3 V. A 74LVC part at 5 V would not accept a 3.3 V input as high: its VIH is 0.7 VCC. A high-side P-FET with its source at 5 V then sees VGS of about -1.7 V when it should be off. The DMP3099L (row 23, the price E5 (g) uses) has VGS(th) -1.0 to -2.1 V (Diodes DS36081 Rev. 5-2, read 2026-09-29 by this reviewer), so it may conduct. In that case, with TX_KEY low and PA_EN high (between elements), the driver is partly powered. The -20 dB "GVA-84+ unpowered" term, and with it the -67 dBm (A4) key-up level and the A4 REQ-TX-014 move from 12 Red to 6 Yellow, is then not supported. With the driver powered, the keying note gives -23 to -19 dBm, a failure. REQ-SYS-120 itself is not affected: the clamp FET (an N-FET driven at 3.3 V) holds the gate bias at 0 V on its own. **Fix:** state the gate drive of the P-FET, for example an N-FET level shifter with a pull-up to the 5 V rail (cents, inside E5 (g)), or a 5 V gate with TTL-threshold inputs. Put the key-up case with the realised gate into the WP-PDR-22 request that D-18 already names. INSP-118 iteration 2 (`dd39a64`, committed while this delta ran) raised the same defect as its finding-9, and one fix closes both | Open | Lien (rule C1); due with the WP-PDR-22 key-up rerun, before the re-baseline CR carries the REQ-TX-014 restatement |
| <a id="finding-25"></a>finding-25 | Minor | CK-RSK-B5 (REQ-SYS-182 route R3) | TS-012 section 7.3 "The TCXO's second path (D-17)"; section 8.14 D-17; section 8.1 diagram; row E5 (g) | **The TCXO squaring stage is not shown to toggle at the TCXO's minimum output.** A 74LVC1G17 is a non-inverting Schmitt buffer, so it cannot be self-biased by feedback. With a fixed bias divider the input window is set by its thresholds. At VCC 3.0 V: VT+ 1.29 to 1.71 V, VT- 0.88 to 1.24 V, hysteresis 0.31 to 0.64 V, -40 to +85 C (Nexperia 74LVC1G17 Rev. 16.1, Table 8, read by this reviewer). The clipped-sine minimum the study quotes is 0.8 Vpp, from a search summary, not read. Swing past both thresholds needs 0.8 V to exceed the part's hysteresis plus the error between the fixed bias and the threshold centre. The allowed bias window is 0.8 V less the hysteresis, 0.16 to 0.49 V wide. The threshold centre varies from part to part by about +/-0.2 V. So some parts in a build would not count, or would count at the wrong duty. Route R3, and with it REQ-SYS-182 and REQ-SYS-154 as written, depends on this count for both finalists. An FC0 failure to count would read as DIED, so the fault is safe (no RF), but it is an availability failure. **Fix:** name a stage that works at 0.8 Vpp: a self-biased unbuffered inverter (74LVC1GU04 class with a feedback resistor), or a comparator, still powered in receive only. Read the TG2520SMN output level at the gate, as the study already plans (section 8.11 item 1). Include the stage in the WP-PDR-20 request. No cost change (cents, inside E5 (g)) | Open | Lien (rule C1); due with the WP-PDR-20 clock-plan item |
| <a id="finding-26"></a>finding-26 | Minor | CK-RSK-B5, B10 | TS-012 section 1 item 4 and pre-order checks line; section 6 R6-6; section 7.1 revision 6 row "Receiver MDS and image" ("image about 79.4 dB over temperature"); table R5-2 row 10; table R5-3 WP-PDR-19 row; section 8.10 rows REQ-SYS-032, 033; section 8.14 D-15 ("residual limit +/-0.97 %"); section 9 table R5-1 receiver row | **The receiver figures and review state in revision 6 are superseded by note revision 4 (`63122e7`) and INSP-117 (`123f048`, reviewer APPROVED).** They were correct when `3b93de1` was committed. At HEAD, 2 + 3 + 4 holds REQ-SYS-033 over REQ-SYS-114 at a worst case of 75.37 dB, not "about 79.4 dB", with an alignment acceptance of +/-0.62 % at 20 to 30 C. D-15 still carries +/-0.97 %, a design-item build value that the note calls "0.01 % on the unsafe side" at room temperature and that does not hold over temperature. The study's own revisit condition ("INSP-117 iteration 4 ... changes an image or MDS figure") has triggered (INSP-117 O-10, X-R4-1). The ranking does not move: the filter, its nine C0G parts (the top of row E5 (a)) and the MDS figures are common to both finalists, and the MDS figures the study quotes match the note. **Fix:** in the next revision, carry the note's revision 4 figures into D-15 (acceptance +/-0.62 %, limit +/-0.64 % over REQ-SYS-114), the 7.1 row, R5-2 row 10, R5-3, 8.10, section 1 and table R5-1 (INSP-117 reviewer APPROVED on revision 4), and record that the revisit condition triggered with no score effect. For the owner's Q1 presentation, the lead SE quotes 75.37 dB | Open | Lien (rule C1); due at revision 7 (the re-issue of sections 8.1 to 8.12 after the choice), before the re-baseline CR |

No new finding is Major. On the brief's rule (Major if the owner would decide on a wrong basis), the owner's Q1 choice rests on a correct basis:
- the INSP-118 conditions are costed and scored, and their arithmetic reproduces;
- the ranking, the weight runs and the robustness verdict reproduce;
- A2 is presented as 06 requires.

finding-24 and finding-25 are cents-level circuit realisations of design items. Their safety direction is benign: the bias clamp holds REQ-SYS-120, and a failed TCXO count reads as DIED. finding-26 is a common-mode figure update with no score effect.

### Observations (iteration 3 re-issue 2; not findings)

- **O-13** (re-issue 1) is closed by X-7. **O-15** stands: Q4 still reads "a thermocouple (USD 9.95)". **O-11, O-12, O-14 and O-16** are unchanged.
- **O-17.** Section 7.3 cites the frequency-budget note as "INSP-056 APPROVED". The record is reviewer APPROVED, with its record verdict held (assurance pair and the CR-012 template), the same convention table R5-1 states for the six analysis records. Worth the same wording.
- **O-18.** A5's margin after G1 and G2 is 0.1605 exactly (299.8395). "USD 0.17" is the difference of truncated figures, the O-16 pattern. Immaterial, but it is the margin the owner is shown in Q1.
- **O-19.** On the interval-13 fallback, PA_EN is set at t0 + 11 ms. TX_KEY has then been up since t0 + 9.5 ms (2 ms before a ramp at 11.5 ms), so the driver powers and the bias clamp releases only 0.5 ms before the ramp, not 2 ms. This belongs in the WP-PDR-22 turn-on case with the D-18 gate. Not a defect of the study.
- **O-20.** The study's R1 limits (16.1, 27.7, 12.0, 23.7 kHz) are the checker values rounded up to 0.1 kHz. INSP-118 finding-1's "above about 32 kHz" (2d) was a coarser bound. The study's 27.7 kHz follows the checker's `min_154_limit` (T + counter + XOSC), which is the correct form.

### Readiness (iteration 3 re-issue 2)

| # | Criterion | Result | Evidence |
|---|---|---|---|
| R1 | `validate_docs.py` exits 0 | **No** | Before this delta: `validate_docs: 109 passed, 8 failed, 117 checked`, exit 1. The same 8 unrelated records fail as at re-issue 1: cm-plan-05 SA, configuration-status, lessons-learned, SRR adrs-001-to-025, process-02, TV-001 to 010, TS-001 and TS-002, and the TS-002 SA. This record passes. Its drift note (reviewed blob `731ba0eb` against HEAD `0c9fcb96`) is removed by this delta |
| R1 (figures) | Figures rendered | N/A | Revision 6 adds no plot. Its new figures are arithmetic on committed CSVs and checker functions, reproduced above |
| R2 | Section A | N/A | Trade study |
| R3 | Sections 1 to 9 filled; section 10 empty | Yes | Section 10 decision fields empty; revisit conditions added for revision 6 |
| R4 | Decision need and gate | Yes | Header "Decide by": B1a 2026-09-29, no later than B1b 2026-10-01; the owner's Q1 follows INSP-110 re-issue 2 and INSP-118 iteration 2 (status note 2026-09-29 section 2) |

### B. Trade study items re-answered (iteration 3 re-issue 2)

| Id | Answer | Evidence |
|---|---|---|
| CK-RSK-B1 to B4 | Yes | No alternative added or pruned. A4 + U3 is a configuration column of A4, not a new alternative. Criteria and weights unchanged since revision 2 |
| CK-RSK-B5 | Yes (liens) | Frequency budget reproduced from the committed checker. The AFT05 rating was read from the same datasheet file. The thermal offsets match `inhibit.csv`. 5 of 6 review verdicts match at HEAD, and the sixth (receiver) is superseded after the commit. Liens: finding-21, 24, 25, 26 |
| CK-RSK-B6 | Yes | Every roll-up, interpolation and total reproduces |
| CK-RSK-B7 | Yes | "Not robust" stated. 16 weight runs, every single, paired and triple move, the joint cases and the named readings reproduce. The value of information for A2 is named with cost and gate (finding-19 Verified) |
| CK-RSK-B8 | Yes (liens) | Revision 6 risk table: 30 ppm row retired, REQ-TX-014 re-scored, receiver cause widened. finding-22 (format) stays. finding-24 bears on the REQ-TX-014 re-score |
| CK-RSK-B9 | Yes | A4 + U3 is recommended over A5 on the evidence. A2, the highest total, is presented with the reasons it is not recommended and the choice-set question (06 section 14.5). Q1 uses the net wording (finding-20 Verified) |
| CK-RSK-B10 | Yes (lien) | Section 9 carries tables R5-1 and R6-1 with every INSP-118, INSP-110 and INSP-114 item dispositioned. Section 10 is empty. The receiver row is superseded (finding-26) |

### Cross items (iteration 3 re-issue 2, returned to Claude)

- **X-12, X-13, X-14, X-16:** closed.
  - X-12: the pair is filed as INSP-118. This record now names it in `paired_record` and copies its iteration 2 verdict, APPROVED (INSP-118 X-1).
  - X-13: all six analysis records are reviewer APPROVED at HEAD.
  - X-14: the owner authorized revision 6 and this pass.
  - X-16: revision 6 applies finding-19 and finding-20.
- **X-17 (for the next INSP-118 delta; WP-PDR-35 and 36a).** HZ-004 K8 requires that "a single GPIO write ... cannot produce RF". TX_KEY and PA_EN are both RP2350 GPIO outputs. If both sit in the SIO output register, one write of `GPIO_OUT` with both bits set raises both. The assurance pair should judge whether "written only by the safe-state manager" is enough, or whether PA_EN needs a different mechanism: a dynamic (toggling) permit through a PIO or PWM channel with a hardware detector, or a pin driven by a different peripheral. This is the assurance lens, not a TS-012 finding.
- **X-18.** INSP-117 X-R4-1 and finding-26 are the same update. The lead SE can give the owner the note's revision 4 figures in the Q1 presentation, and record in the status note that the TS-012 revisit condition on INSP-117 iteration 4 triggered with no score effect.
- **X-19.** For the Q1 presentation, both circuit liens (finding-24, finding-25) are cents-level. They do not change the TCXO-required condition or the PA_EN condition that the owner is asked to accept.

### Commands (iteration 3 re-issue 2)

```
git rev-parse 3b93de1 HEAD                                                      # 3b93de11..., 123f0489...
git rev-parse 3b93de1:<TS-012 path>; git hash-object <TS-012 path>              # 0c9fcb96... both; HEAD:<path> the same
git show --stat 3b93de1; git log 3b93de1..HEAD -- docs/decisions/trade-studies/ # TS file only; no later TS commit
git diff -U0 37d5824 3b93de1 -- <TS-012 path>                                     # the revision 6 delta, read hunk by hunk
python tools/check_commit_msg.py --range 3b93de1^..3b93de1                       # PASS, Refs: TS-012, INSP-110, INSP-118
python tools/validate_docs.py                                                    # before: 109 passed, 8 failed, 117 checked (exit 1)
  after the delta: see the record commit; this record PASS, the same 8 records fail
python (hardware/sim/freq): freq_budget.healthy_disagreement, undetected_bound, min_window, min_154_limit (R1, R3; 12, 13),
  fc0_accuracy_ceiling(12), tx_detection_time(13); R1 at 30 ppm by the same formula
python3 (scratchpad sens6.py): totals rev 5 and 6; 16 weight runs with A4 + U3 and with A4; all 1-, 2-, 3-move combinations
  A5/A4 + U3, A5/A4, A2/A4 + U3; joint adverse cases; named readings; roll-ups re-added by hand
hardware/sim/thermal/results/2026-09-28-ts012-r2/inhibit.csv (A4-DC rows), trips.csv (A4-DC hw_sink nan)
docs/design/analysis/keying-ts012.md section 4.5 (REQ-SYS-183 table); pa-drive-ts012.md inputs (5 V bus, GVA-84+ 0.108 A)
docs/design/analysis/rx-bpf-ts012.md revision 4 (63122e7) sections 0, 5, 8; review records analysis-*-ts012.md front matter and git log
WebFetch (datasheets, cached PDF, pdftotext): NXP AFT05MS004N Rev. 0 7/2014 (SHA-256 84cd9fae...6dd036);
  Nexperia 74LVC1G17 Rev. 16.1 Table 8; Diodes DMP3099L DS36081 Rev. 5-2 (VGS(th) -1.0 to -2.1 V). Nothing logged into, no form
```

### Measurements (iteration 3 re-issue 2)

size = 1 trade study revision (1248 lines; 244 insertions, 129 deletions), 3 INSP-118 Majors in 10 parts, 4 INSP-110 items and X-7, 7 review verdicts, 13 roll-up checks, 16 x 2 weight runs, 3 datasheets; turns = 40; minutes = 80; major = 0 new (3 Verified); minor = 3 new (finding-24 to 26), 3 Verified this pass (finding-19, 20, 23).

### Record verdict and verdict format (iteration 3 re-issue 2)

`reviewer_verdict: APPROVED`. No Major finding is open. The INSP-118 Major fixes are carried correctly into the study. finding-19, 20 and 23 are Verified. The new Minor findings 24 to 26 are liens (rule C1), with the TS-012 author as owner, and finding-21 and 22 stay liens.

**Assurance pair.** INSP-118 iteration 2 was committed at `dd39a64` while this delta ran, on the same blob `0c9fcb96`: assurance verdict APPROVED, finding-1 to 3 Verified, new Minor finding-9. `assurance_verdict: APPROVED` is copied under INSP-118 X-1, and this record names blob `0c9fcb96` as INSP-118 X-7 asks. INSP-118 finding-9 and this record's finding-24 describe the same D-18 P-FET gate-drive defect, found independently. One fix closes both, and each record verifies it under its own lens: finding-24 here for the REQ-TX-014 re-score, finding-9 there for the gate's unpowered state. The HZ-004 K8 "single GPIO write" question of X-17 is not among INSP-118 iteration 2's findings, so it stays a cross item for its next delta.

The record `verdict` stays NEEDS CHANGES for one reason: readiness R1 fails on records unrelated to TS-012. The reviewer and assurance verdicts are both APPROVED on blob `0c9fcb96`. When R1 holds, the lead SE sets `verdict: APPROVED`, provided `git rev-parse HEAD:<path>` still equals `0c9fcb96`. INSP-118's own record verdict is also held for the CR-012 template, which is that record's condition, not this one's. A changed blob needs a further delta.

**Commit message deviation.** The first commit of this delta (`17b6865`) used the subject type `review`, which is not one of the 05 section 4.5 types, so `check_commit_msg.py` reports SUBJECT. It is the same form as the project's other review commits (17 of the last 40, including `dd39a64` and `123f048`). History is not rewritten. The follow-up commit uses `docs`. This is noted for the configuration-status change log, alongside INSP-118 finding-8.

```
VERDICT: APPROVED (reviewer); assurance APPROVED (INSP-118 iteration 2, dd39a64); record verdict held for readiness R1
PRODUCT: docs/decisions/trade-studies/TS-012-design-to-cost-hand-built.md@0c9fcb96 (revision 6, 3b93de1), delta from @731ba0eb (revision 5, 37d5824)
FINDINGS:
- [Major] finding-1, finding-2, finding-3: Verified (hold on revision 6).
- [Minor] finding-19, finding-20, finding-23: Verified on revision 6. finding-21, finding-22: Open liens (unchanged).
- [Minor] CK-RSK-B5, B8 section 7.3 D-18, E5 (g): the GVA-84+ supply P-FET on the 5 V bus cannot be turned off by a 3.3 V NAND output (DMP3099L VGS(th) -1.0 to -2.1 V); the -67 dBm key-up level and the A4 REQ-TX-014 Yellow depend on it; state the level shift (finding-24; same defect as INSP-118 finding-9).
- [Minor] CK-RSK-B5 section 7.3 D-17: a Schmitt 74LVC1G17 cannot be self-biased, and a fixed bias does not guarantee toggling at 0.8 Vpp (hysteresis up to 0.64 V, threshold spread); name a working squaring stage (finding-25).
- [Minor] CK-RSK-B5, B10 sections 1, 7.1, R5-2, R5-3, 8.10, D-15, R5-1: receiver figures superseded by note revision 4 and INSP-117 APPROVED (75.37 dB over temperature, acceptance +/-0.62 %, not 79.4 dB and +/-0.97 %); revisit condition triggered, no score effect (finding-26).
ITEMS N/A: CK-RSK-A1 to CK-RSK-A11 (product is a trade study)
MEASUREMENTS: size=1 revision, 13 criteria, 7 verdict checks, 13 roll-up checks, 32 weight runs; turns=40; minutes=80; major=0 new; minor=3 new; verified=21; open=5
```
