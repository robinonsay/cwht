---
# Peer-review record front matter (charter section 5; docs/process/01-lifecycle-and-reviews.md
# section 13 is the single field list; docs/process/08-agent-briefing.md section 3.2).
id: INSP-029
checklist: peer-review-checklist-visual-product
checklist_revision: A
# checklist_file: the path the assignment names (the template slug is deck-srr and package
# section 2.1 item R6 calls it visual-srr-deck; cross item X-3)
checklist_file: docs/reviews/SRR/checklists/srr-deck.md
product: docs/reviews/SRR/slides/srr.adoc
# product_commit: HEAD at review time. The deck under review is the working-tree re-write of
# 2026-09-26 (package revision 4); it is NOT committed. HEAD holds the revision 3 deck
# (srr.adoc@7b8c6e4f, 40 PNGs). product_files names the working-tree blobs actually reviewed
# (git hash-object) at iteration 2 (the finding-1 fix, re-rendered 04:22); iteration 1 reviewed
# srr.adoc@bb33e806 and srr.html@b2f8db82. tools/validate_docs.py reports them as record drift
# until item R12 commits them (readiness R3).
product_commit: "d7fdf255aeb05291156c408de73399b1808b18aa"
product_files:
  - "docs/reviews/SRR/slides/srr.adoc@6b11731641506692d8ceea59c8de453d19670730"
  - "docs/reviews/SRR/slides/srr.html@e2636649075598642a3caf654db324eb7718e693"
  - "docs/reviews/SRR/slides/srr.css@da8d9463ed1f2885c345c5c466ce6e3c6d07c260"
product_size: 42 slides
renders_inspected: 42
sprint: SRR-prep
author_agent: "deck author (lead SE main session, SRR deck re-write from package revision 4, item R10)"
reviewer_agent: "reviewer:INSP-029"
criticality: neither
assurance_required: false
assurance_reviewer_agent: none
iteration: 2
readiness_met: false
reviewer_verdict: APPROVED
assurance_verdict: not-required
# verdict: iteration 2. finding-1 (Major, CK-VIS-B7) is Verified in the working tree
# (srr.adoc@6b117316, srr.html@e2636649, png/slide-07.png re-rendered and opened); finding-2 to
# finding-6 (Minor) are liens "Lien: fix before PDR" under the convergence rule of 2026-09-26
# (charter section 4 item 3). reviewer_verdict APPROVED (with liens). The record verdict stays
# NEEDS CHANGES only on readiness R2, R3 and R4 (package deck block, commit, author render list),
# the same holding pattern as INSP-018 and INSP-026; no product change is required.
verdict: NEEDS CHANGES
findings_major: 1
findings_minor: 5
findings_open: 0
findings_fixed: 0
findings_verified: 1
findings_deferred: 5
deferred_rids: []
items_no: [CK-VIS-A1, CK-VIS-A2, CK-VIS-A5, CK-VIS-B1, CK-VIS-B7, CK-VIS-B11, CK-VIS-B12]
effort_turns: 67
effort_minutes: 90
record_status: Open
date: 2026-09-26
date_closed: null
---

# Peer review record INSP-029: SRR review deck

**Product.** The SRR pre-review deck re-written from package revision 4 (package section 2.1 item R10, readiness item H3, entrance row S11): `docs/reviews/SRR/slides/srr.adoc` with its generated `srr.html`, the theme `srr.css` and the 42 renders `docs/reviews/SRR/slides/png/slide-01.png` to `slide-42.png`. Checklist `docs/templates/peer-review-checklist-visual-product.md` revision A, sections A (every render) and B (review deck); section C is N/A (the product is the deck, not the package figure set).

**What was reviewed, and its configuration state.** At HEAD `d7fdf255aeb05291156c408de73399b1808b18aa` the committed deck is the revision 3 deck (`git rev-parse HEAD:docs/reviews/SRR/slides/srr.adoc` = `7b8c6e4f`, 40 PNGs since `400e59d`). The deck reviewed here is the uncommitted working-tree re-write (file times 2026-09-26 04:08 to 04:10):

| File | Working-tree blob (`git hash-object`) | HEAD blob (`git rev-parse HEAD:<path>`) |
|---|---|---|
| `docs/reviews/SRR/slides/srr.adoc` | `bb33e806c56a72af3db4cf51102add14f9814198` | `7b8c6e4f086913b0638dd2a74a6caab3df9026ae` |
| `docs/reviews/SRR/slides/srr.html` | `b2f8db828ea08a30904d3c52f63e36d0dd28b1ba` | `38221e4381884b2c22d2bfffb06b8439668a8ed9` |
| `docs/reviews/SRR/slides/srr.css` | `da8d9463ed1f2885c345c5c466ce6e3c6d07c260` | `9f98fac21173d8d39ac9cc52362159f9abd1b18a` |
| `docs/reviews/SRR/package.md` (the source of truth checked against) | `94f5080f8e42465c3b25628da412e8d5929cf649` (revision 4, uncommitted) | `9042d9451779285c8c35bd9bfbbadb167203fa7c` |
| `png/slide-01.png` to `slide-40.png` | 40 modified blobs (for example `slide-01.png` `b8610c4b`, `slide-40.png` `ab68aa9e`) | revision 3 renders |
| `png/slide-41.png`, `slide-42.png` | `8c8dddc4`, `60729721` (untracked) | absent |

The package revision 4 is itself uncommitted; every claim below was checked against that working-tree revision 4, which is the revision the deck cites on slide 1.

**Method.** Search first: `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` (queries: the record drift rule of `tools/validate_docs.py`; package section 13.1 decision counts) preceded every manual search; `grep -n` and `awk` were used only afterwards to pin lines in known files. Read in full: charter, 08 sections 1 to 5, package sections 1, 2, 2.1 to 2.4, 4 (counts line), 6, 7, 8, 9, 10, 11, 12, 13 (TBR summary), 13.1 (count, K1 to K17, index), 14, 15 (all 60 items), 16, 17, 18, 20, 20.1 and 21, and the whole deck source. Every PNG was opened with the Read tool and read against its source slide and the cited package section. Structural checks by script: 41 level-1 `== ` sections plus the title = 42 slides; 42 `[.notes]` blocks, 42 `Evidence:` lines and 42 `Question for Robin:` lines; 42 `<section>` and 42 `class="notes"` in `srr.html`; no `===` sub-slides, no `%step` or `.fragment` roles (the six `fragment` strings in `srr.html` are reveal.js configuration comments); every PNG header 1920 x 1080; no em dash or en dash in the source; smallest font size in `srr.css` 24 px (slide number); `slides/reveal.js` is git-ignored (`git check-ignore` prints it). Decision placement was recomputed from the package section 13.1.4 index: 17 key decisions covering 47 numbers, 68 consent numbers in themes A to P, decisions 5 and 12 needing no ruling, 117 in total, each on the slide the deck shows. The 60 candidate items of package section 15 were each placed in exactly one handling row of slide 36 (4 + 8 + 22 + 2 + 17 + 7 = 60, no number missing or repeated). Hazard and risk matrices, TPM zones and the success board were recounted cell by cell against package sections 9, 10, 11 and 20. Citations verified in the corpus: all 40 SWE numbers the deck shows appear as `[SWE-NNN]` in `docs/references/md/npr-7150-2d/` (SWE-087, 088, 089 at `05-chapter5.md` lines 49, 63, 73); SE-24 to SE-31, SE-35 to SE-39, SE-44, SE-51, SE-52, SE-55, SE-56, SE-62 to SE-64 and SE-66 appear as `[SE-NN]` in `docs/references/md/npr-7123-1d/` (SE-62 at `06-chapter6.md` line 52); 47 CFR 97.307(e) (corpus: `47cfr-97.307.md` line 25, eCFR issue 2026-09-23: 25 uW and at least 40 dB for 25 W or less, so 53 dB at 5 W) and 47 CFR 15.23(a) (corpus: `47cfr-15.23.md` line 17, "quantities of five or less for personal use"). The reviewer did not re-run `tools/slides/render_deck.py` (CK-VIS-B1: it rewrites `png/` in place) and edited no product file.

## Tool runs (2026-09-26, HEAD `d7fdf25`, working tree with revision 4, repository root, `.venv/bin/python`)

| Command | Exit | Result |
|---|---|---|
| `tools/traceability.py --report-only --output <scratch>/tr.md --json <scratch>/tr.json` | 0 | 238 requirements, 170 test cases, 0 violations, 3 warnings (HAZARD_INVERSE REQ-SW-KEYER-039; SYS_UNALLOCATED REQ-SYS-125, REQ-SYS-148), as slide 15 states; written to the scratchpad so no repository file changed |
| `tools/render_risk.py --check --gate SRR --hazards docs/safety/hazards.json` | 0 | 65 risks, 159 candidates, 0 warnings, hazard cross-check; `register.md` current (slide 18 counts) |
| `tools/render_rmm.py --check` | 0 | 100 rows, FC 75, T 17, NA 8 (slides 37, 38) |
| `tools/render_compliance.py --check` | 0 | NA SE-24 to SE-31, SE-44; rendered file current (slide 38) |
| `python -m unittest discover -s tools/tests` | 0 | 392 tests OK (slide 4) |
| `tools/validate_docs.py` (after this record was written) | 0 | 48 passed, 0 failed; `PASS docs/reviews/SRR/checklists/srr-deck.md` (NEEDS CHANGES, drift of the three working-tree blobs reported as notes only) |

## Readiness criteria

| # | Criterion | Met | Evidence |
|---|---|---|---|
| R1 | `tools/validate_docs.py` exits 0 | Yes | 48 passed, 0 failed, including this record |
| R2 | Package "Slide deck" block filled for this render and the section 1.1 slide map names this deck's slide numbers | **No** | Package revision 4 header row "Slide deck" and section 2.2 block still describe the deck "committed at `28e49e6`", "not yet written from revision 3 or 4", 42 PNGs, render commit `28e49e6`, inspected 2026-09-25; section 1 agenda and section 1.1 map give the old slide numbers (for example hazards slide 17, trend 36 with candidate RIDs 37 and 38, disposition 42 at `28e49e6`), while this deck puts hazards on 16, trend and candidate RIDs on 36 and tailoring on 38. HEAD itself holds 40 PNGs (since `400e59d`), not 42. Cross item X-1, X-2 |
| R3 | Source, HTML and renders committed at `product_commit` | **No** | `git status --porcelain -- docs/reviews/SRR/slides` lists `srr.adoc`, `srr.css`, `srr.html` and `slide-01.png` to `slide-40.png` modified and `slide-41.png`, `slide-42.png` untracked; the embedded `figures/entrance-checklist.png` and `success-criteria.png` are also modified. Closes with item R12 (routine CM commit), cross item X-4 |
| R4 | Author return lists every render with path, command, exit status and inspection date | **No** | No author return or package entry for this render exists that the reviewer could read (the package block is the revision 2 render, R2). Cross item X-2 |

## Participants

Author: the deck author (lead SE main session). Reviewer: this invocation (reviewer:INSP-029), which did not write the deck, the package or any figure. No software assurance review is required (07 section 2.1.1 does not list decks).

## A. Every render

| Id | Answer | Evidence |
|---|---|---|
| CK-VIS-A1 | **No** (committed part) | All 42 PNGs exist at `docs/reviews/SRR/slides/png/slide-01.png` to `slide-42.png` beside the source; none of the 42 current renders is committed (readiness R3). No render is missing |
| CK-VIS-A2 | **No** (not recorded) | The renders are consistent with `tools/slides/render_deck.py` (PNG and HTML times 04:10 after the source at 04:09; 1920 x 1080; slide-number footer `N / 42`), but the run (command, exit status, date) is recorded nowhere the reviewer can read (readiness R2, R4) |
| CK-VIS-A3 | Yes | Source and renders are both uncommitted; by file time every PNG and the HTML post-date the last source edit. Every PNG's text matches its source slide word for word as read (per-render table); the reviewer did not re-render (B1) |
| CK-VIS-A4 | Yes | All 42 opened with Read: every text run readable at native size, nothing cut at an edge, no overlap, no missing-glyph boxes, no blank region where content is expected. Small but readable text inside two embedded figures is finding-5 |
| CK-VIS-A5 | **No** | At least three values per slide checked against the package (per-render table). Two render values abridge their source so that information is lost: finding-3 (slide 21, decision 37 default omits OQ-SAF-004) and finding-4 (slide 10, the plans row). Every other value, id, count and status matched, including the entrance counts 5/15/19, the success counts 4/6/8, the TPM zones 3/4/3/10, the hazard matrices (initial High 5, Serious 8, Medium 2; residual Low 10, Medium 3, Serious 2), the risk matrix (Red 32 with RSK-034 by override, Yellow 25, Green 8), the TBR table (115 = 14 + 101; 25; 5; 17) and every key-decision option, recommendation and default |
| CK-VIS-A6 | Yes | Every slide has a title and the package section tag; embedded charts carry axis labels and legends (slide 14 legend with method counts; slide 18 legend and scoring footnote; slide 16 legend and likelihood axis) |
| CK-VIS-A7 | Yes | Every coloured status also carries text: lane headers and counts (slides 5, 7, 9, 39), zone words on every TPM card (17), band letters and legend counts (18), band words in every hazard cell (16), words in the status chips (37) |
| CK-VIS-A8 | Yes | Package section 7 defects touching the deck: section 15 item 56 (figure generator) is Closed by blob `6f3018fd`; the success-board footer wording (section 7 row 2, cross item for the tool owner) is worked around by the deck-drawn board of slide 39, disclosed in its notes (finding-6 records the residual) |

## B. Review deck

| Id | Answer | Evidence |
|---|---|---|
| CK-VIS-B1 | **No** | The package "Slide deck" block describes the revision 2 render (`28e49e6`, 2026-09-25), not this one (readiness R2, cross item X-2) |
| CK-VIS-B2 | Yes | 41 `== ` sections + title = 42 slides = 42 PNGs numbered `slide-01` to `slide-42` without gap = 42 `<section>` in `srr.html`; the package block's "42" refers to the old deck (X-2) |
| CK-VIS-B3 | Yes | Every PNG header reads 1920 x 1080 (script); none blank |
| CK-VIS-B4 | Yes | No `[%step]`, `.fragment` or `===` in the source (grep after vector search) |
| CK-VIS-B5 | Yes | Charter section 4 item 2 minimum set: title and agenda 1, 2; purpose, scope and entrance-criteria status 4 to 9 (opening action 3); products with evidence links and counts 10 to 13; requirements and traceability 14, 15; hazards and safety 16; risks and TPMs 17, 18 (milestones 19); TBD/TBR and open decisions with recommendations 20 to 35 (17 key decisions on 21 to 32 with options, recommendation and default for all 47 numbers; consent agenda of 68 on 33 to 35); RFA/RID trend 36; proposed tailoring and liens 37 to 40; requested disposition 42 (owner actions 41). The package section 1.1 map still gives the old numbers (X-1) |
| CK-VIS-B6 | Yes | Every slide title carries `[.src]#§N#`; every cited section (1, 2, 2.1, 2.2, 2.3, 2.4, 3, 4, 6, 6.2, 6.5, 6.12, 6.15, 7, 8, 9, 10, 11, 12, 13, 13.1, 13.1.1 K1 to K17, 13.1.2, 14, 15, 16, 16.1, 17, 18, 18.1, 20, 20.1, 20.2, 21) exists in revision 4 |
| CK-VIS-B7 | **No** (lien only) | finding-1 (Major): slide 7 notes stated a record verdict the package contradicts; Verified at iteration 2. finding-2 (Minor, lien): slide 1 states the revision and records as committed. Every other number, count, status, date and statement on the slides and in the notes was found in the cited section (per-render table), including the notes-only claims checked individually (for example 1608 B flash and 8200 B RAM, 13.0 h to 10.4 h, USD 62 margin, 104 Proposed and 14 Requirement pending controls, 31 risks opened, the 7f aeronautical band of V-5, the 22 Accepted ADR files of decision 105) |
| CK-VIS-B8 | Yes | 42 `[.notes]` blocks, one per slide; each cites its package section and closes with an `Evidence:` line and a `Question for Robin:` line; every slide that asks for a ruling names the decision numbers |
| CK-VIS-B9 | Yes | No notes text on any PNG |
| CK-VIS-B10 | Yes | `srr.css` sizes: 48 px titles, 28 to 32 px body, tables and boards, 24 px slide number, nothing below 20 px; every table shows its last row and column; `:revealjs_slideNumber: c/t` prints `N / 42` |
| CK-VIS-B11 | **No** | Six embedded figures from `docs/reviews/SRR/figures/` (entrance board, ConOps modes, concept block diagram, requirements by group, hazard matrices, TPM status, risk matrix: seven images) are the package section 7 renders and their content matches the package; two of them are not committed at HEAD (`entrance-checklist.png`, `success-criteria.png` modified; readiness R3), block labels of the concept diagram and the risk-matrix footnote are small at slide scale (finding-5), and slide 39 replaces the committed success-criteria figure with a board drawn in the deck (finding-6) |
| CK-VIS-B12 | **No** | Source, HTML and PNGs uncommitted (readiness R3); `slides/reveal.js` is git-ignored (`git check-ignore` prints the path) |
| CK-VIS-B13 | Yes | Slide 1 names the review token (SRR combined with MCR), package revision 4 of 2026-09-26, the chair (Robin, with DA, ETA and SMA TA) and the presenter (Claude), and states in a warning callout that this is a pre-review session and the gate review is not convened (tense of one sentence: finding-2) |
| CK-VIS-B14 | N/A | First review record of this deck (the 2026-09-25 deck review of the revision 2 deck has no INSP record) |

**Honest readiness.** The deck does not overstate readiness: slides 1, 4, 5, 6, 9, 19, 39 and 42 say the declaration cannot be made, list the open Hard rows (S1, S3, S11, 20 Not met; 14 Hard rows Partially met), the eight open H items, every remaining R item with its owner, and request no disposition at this session. The only tense slip is finding-2.

## Per-render results

All 42 PNGs were opened with the Read tool on 2026-09-26. Legible = every text run readable, nothing clipped or overlapping. "Agrees" = content agrees with the source slide and the package values checked. B6 = cited section exists. B7 = every claim on the slide and in its notes is in the package.

| Render | Source slide | Opened (A4) | Legible (A4) | Agrees (A5) | B6 | B7 | Values checked against the package | Finding ids |
|---|---|---|---|---|---|---|---|---|
| `png/slide-01.png` | Title | Yes | Yes | Yes | Yes | No | HEAD `d7fdf25`; revision 3 at `adcfe09`; S1, S3, S11, 20; 14 Partially met (sections 2, 4) | finding-2 |
| `png/slide-02.png` | Agenda | Yes | Yes | Yes | Yes | Yes | block to section and slide ranges; OA-1, OA-2 first (section 2.2 "Start of the review session") | none |
| `png/slide-03.png` | Opening action OA-1, OA-2 | Yes | Yes | Yes | Yes | Yes | pass 10 to 120 (63), 3 to 45 (16); run 2 Blocked, UF2 byte-identical; notes 1608 B, 8200 B, 2 FAIL, 5 MISSING, 36 sites (sections 2.2, 6.15, 16) | none |
| `png/slide-04.png` | Purpose, scope and readiness | Yes | Yes | Yes | Yes | Yes | 392 tests; K15; never-a-lien rule; notes 47 passed, 3 warnings (sections 1, 2, 21) | none |
| `png/slide-05.png` | Readiness items H1 to H17 | Yes | Yes | Yes | Yes | Yes | lanes 8 / 5 / 4 against the H table states; H1 5 Major, 2 missing, 16 self-checks, 3 re-issues (section 2) | none |
| `png/slide-06.png` | What remains before the declaration | Yes | Yes | Yes | Yes | Yes | R1 key list K1, K2, K9 to K12, K14 to K17; R3, R4, R5, R11, R13, R14 Done; R16 waits on R1, R2 (section 2.1) | none |
| `png/slide-07.png` | Review records: 28 records | Yes (iterations 1 and 2) | Yes | Yes | Yes | Yes (iteration 2) | lanes 10 / 12 / 3 / 3 and every record placement match section 2.4; 115 liens plus E-10; iteration 2 notes agree with section 2.4 on INSP-001 and INSP-002 | finding-1 (Verified) |
| `png/slide-08.png` | Open Major findings and blob check | Yes | Yes | Yes | Yes | Yes | five open Majors with decisions 30, 106, 47, 109, 110, 108; 26 of 28; drifts at `0f5a529`, `f2e02aa` (sections 2.3, 2.4, 15) | none |
| `png/slide-09.png` | Entrance-criteria checklist (figure) | Yes | Yes | Yes | Yes | Yes | Not met 5 (S1, S3, S10, S11, 20), Partially met 15, Met 19, daggers S4, 8, 24 (section 4 counts line) | none |
| `png/slide-10.png` | Products with evidence links and counts | Yes | Yes | **No** | Yes | Yes | 36 SI, 10 stakeholders, 30 NGO, 13 MOE, 28 CON; 183 / 181 / 2, 18 KDR, 115 TBR; 16 + 39, 170 cases; 15 hazards, 118 controls; 65 risks, Red 32; 100 and 62 rows; 26 ADRs, 4 Proposed; 20 MOPs, 20 TPMs; USD 276 to 548 (section 6) | finding-4 |
| `png/slide-11.png` | ConOps modes and scenarios (figure) | Yes | Yes | Yes | Yes | Yes | 22 scenarios, 12 nominal, 10 off-nominal; row 10 Partially met; D5, D7, D18 on decisions 36, 37 (sections 6.2, 7) | none |
| `png/slide-12.png` | Concept block diagram (figure) | Yes | Yes (small) | Yes | Yes | Yes | B01 to B22, B07 text "TX inhibit while VBUS present", item 38 in L-4 (sections 6.2, 7) | finding-5 |
| `png/slide-13.png` | Concept feasibility | Yes | Yes | Yes | Yes | Yes | TRL 6; F-02 at `4fe6f28`; A0 400 of 500; blobs `2a0c40a8`, `574cee3d`; TRL 3 and RSK-008 (sections 6.12, 6.15, 13.1.1 K4) | none |
| `png/slide-14.png` | L1 requirements by functional group (figure) | Yes | Yes | Yes | Yes | Yes | 111 / 41 / 21 / 8, 11 groups with row totals, TBR bars 6, 18, 16, 17, 12, 10, 18, 16, 0, 0, 2 = 115 (section 8 group table) | none |
| `png/slide-15.png` | Traceability and verification planning | Yes | Yes | Yes | Yes | Yes | PASS, 0 violations, 3 warnings; 110 / 16 / 43 / 1; Bench 96, HostUnit 35, Simulation 27, Inspection 12; 179 allocated; 22 KDRs (sections 6.5, 8); re-run confirmed | none |
| `png/slide-16.png` | Hazards and safety (figure and bullets) | Yes | Yes | Yes | Yes | Yes | both matrices cell by cell against section 9 table; 19 questions 6 / 4 / 9; SPF rows 3, 4, 8 with REQ-SYS-180, 182, 181 (sections 9, 18.1, 2 H7) | none |
| `png/slide-17.png` | TPM status and margins (figure) | Yes | Yes | Yes | Yes | Yes | 20 cards: Red 001, 002, 016; Yellow 004, 008, 014, 020; Green 003, 007, 019; -189 %, 58 %, 17 dB, 9.5 h, USD 548 (USD 610 TBR) (section 10) | none |
| `png/slide-18.png` | Risk matrix (figure) | Yes | Yes (small footnote) | Yes | Yes | Yes | cell counts 2, 8, 4, 2, 6, 15, 17, 3, 1, 1, 1, 5 = 65; Red 32 with RSK-034 override (section 11); `render_risk.py --check` exit 0 | finding-5 |
| `png/slide-19.png` | Milestones and procurement | Yes | Yes | Yes | Yes | Yes | four milestones, dates, RSK-014, RSK-053 2026-10-01 to 10-04, RSK-038 parts (section 12) | none |
| `png/slide-20.png` | TBR list and the decision agenda | Yes | Yes | Yes | Yes | Yes | 115 = 14 + 101; 25; 5; 17; 117 = 47 + 68 + 2; the 14 SRR TBR to decision mapping in the notes (sections 13, 13.1) | none |
| `png/slide-21.png` | K1 | Yes | Yes | **No** | Yes | Yes | 36 options a and b, 74LVC1G123; 37 options and recommendation; 41 values and default (13.1.1 K1) | finding-3 |
| `png/slide-22.png` | K2 | Yes | Yes | Yes | Yes | Yes | 38 150 to 180 s, 39 95 C +/-3 C and 100 ms, 40 10 kHz and 100 ms, 9, 33, with each default (13.1.1 K2) | none |
| `png/slide-23.png` | K3 and K15 | Yes | Yes | Yes | Yes | Yes | 6, 7, 8, 114 options, recommendations and defaults (13.1.1 K3, K15) | none |
| `png/slide-24.png` | K4 | Yes | Yes | Yes | Yes | Yes | 14, 11, 32 (0.35 W/kg per W, 1 g, 50 %), 3 (13.1.1 K4) | none |
| `png/slide-25.png` | K5 | Yes | Yes | Yes | Yes | Yes | 17 to 20; HZ-006 Critical-D Medium default (13.1.1 K5) | none |
| `png/slide-26.png` | K6 and K13 | Yes | Yes | Yes | Yes | Yes | 63, 64 (100, 150, 30 mVrms, 20 h), 90 (USD 610, 276 to 548), 86 (15.23) (13.1.1 K6, K13) | none |
| `png/slide-27.png` | K7 | Yes | Yes | Yes | Yes | Yes | 70, 72, 75, 76 (3.20 V, 3.00 V, 60 C), 85 (-10 to +45 C, 0 to 45 C, -20 to +60 C, 1.0 m, IPX2) (13.1.1 K7) | none |
| `png/slide-28.png` | K8 | Yes | Yes | Yes | Yes | Yes | 53, 54, 55 (97 mA, 0.5 dB; 30 mA, 2 to 3 dB; 7 dB), 58 (P1 PD54008L-E, P3, P4, 12.5 V); USD 118 against 2 to 5 (13.1.1 K8) | none |
| `png/slide-29.png` | K9 and K10 | Yes | Yes | Yes | Yes | Yes | 107 (400, 265, 220, 220), 110 (36 sites, G5), 108 (CS-11, CS-38, CS-12), 109 (1.98.0, nightly-2026-08-24) (13.1.1 K9, K10) | none |
| `png/slide-30.png` | K11 and K16 | Yes | Yes | Yes | Yes | Yes | 105 (21 ADRs, options A to C, 19 superseding), 106, 111, 47 (8 dits, 3 to 30, 12 ms) (13.1.1 K11, K16) | none |
| `png/slide-31.png` | K12 | Yes | Yes | Yes | Yes | Yes | 30 ten requirements by method, 113 four requirements, 29 60 dB against 53 dB, V-5 a and c (13.1.1 K12; 47 CFR 97.307(e) corpus line 25) | none |
| `png/slide-32.png` | K14 and K17 | Yes | Yes | Yes | Yes | Yes | 104, 112 (034, 035, 036, 038, 039), 115 (a) and (b) with defaults (13.1.1 K14, K17) | none |
| `png/slide-33.png` | Consent agenda A to C | Yes | Yes | Yes | Yes | Yes | decision sets A (7), B (11), C (1) match section 13.1.4; block content matches the theme rows (for example 208HA1A, 2.5 ppm, 6.3 W, PRACTICE) | none |
| `png/slide-34.png` | Consent agenda D to I | Yes | Yes | Yes | Yes | Yes | D (9), E (2), F (4), G (5), H (3), I (3) match section 13.1.4; 144.010 MHz, +27 dBm, TPA6132A2, 1043P, LS013B7DH03 found in the theme rows | none |
| `png/slide-35.png` | Consent agenda J to P | Yes | Yes | Yes | Yes | Yes | J (5), K (4), L (4), M (3), N (4), O and P (3) match section 13.1.4; total 68 | none |
| `png/slide-36.png` | RFA/RID trend and candidate RIDs | Yes | Yes | Yes | Yes | Yes | log empty, TPM-003 Green (section 14); every one of the 60 items in one row, matching section 15 states (items 56 and 59 Closed by the integration updates) | none |
| `png/slide-37.png` | Software status | Yes | Yes | Yes | Yes | Yes | SWE rows and states against section 16 and 16.1; FC 75, T 17, NA 8; gate exit 1, 2 FAIL, 5 MISSING | none |
| `png/slide-38.png` | Proposed tailoring | Yes | Yes | Yes | Yes | Yes | 17 T and 8 NA RMM rows and 4 T and 9 NA compliance rows, each listed once, against sections 17 and 18 | none |
| `png/slide-39.png` | Success criteria self-assessment | Yes | Yes | Yes | Yes | Yes | 4 / 6 / 8 and every criterion lane against section 20 | finding-6 |
| `png/slide-40.png` | Proposed liens L-1 to L-7 | Yes | Yes | Yes | Yes | Yes | L-1 101, 25, 4, 17; L-4 items 2, 3, 8, 11, 38, 55, 58; L-6 115 plus E-10 (section 20.1) | none |
| `png/slide-41.png` | Owner actions | Yes | Yes | Yes | Yes | Yes | OA-3 to OA-9 action, when and closes against section 2.2 | none |
| `png/slide-42.png` | Requested disposition | Yes | Yes | Yes | Yes | Yes | no disposition now; R6 to R10, R12, R15, R16; Approved with liens L-1 to L-7 at the gate; OA-8 (sections 2.1, 21) | none |

## Findings

| Finding | Origin | Severity | Item | Location | Description and expected fix | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | reviewer | Major | CK-VIS-B7 | slide 07 notes (`srr.adoc` line 222), `png/slide-07.png` | The notes say of the twelve records in the "Self-check only" lane: "their reviewers found no open finding, and the reviewer verdict of each is APPROVED with liens". Package section 2.4 gives `reviewer_verdict` NEEDS CHANGES for INSP-001 (expectations) and INSP-002 (ConOps and concept), and both record files read `reviewer_verdict: NEEDS CHANGES`; only ten of the twelve have a reviewer verdict APPROVED. The notes are the narrative the owner hears, so a record status the package contradicts reaches the Decision Authority (checklist Major class: a claim absent from `package.md`). Fix: reword to the package's own statement, for example "their reviewers found no open finding; ten of them carry a reviewer verdict APPROVED with liens, and INSP-001 and INSP-002 carry reviewer verdict NEEDS CHANGES on readiness only", then re-render and re-open slide 07. **Iteration 2 (2026-09-26): Verified.** `srr.adoc@6b117316` notes of slide 07 (line 222) now read "Ten of the twelve carry reviewer verdict APPROVED with liens; INSP-001 and INSP-002 carry reviewer verdict NEEDS CHANGES, on readiness only (package section 2.4)"; the same sentence is in `srr.html@e2636649` (once) and the old sentence is gone from both. Checked against the twelve record files: `reviewer_verdict` NEEDS CHANGES for INSP-001, 002 and APPROVED for INSP-010, 014, 018 to 024, 026, as package section 2.4 lists. `png/slide-07.png` (`732e8831`, 1920 x 1080, 04:22) opened: lanes 10 / 12 / 3 / 3 unchanged and correct, no notes text on the render | Verified | not needed | |
| <a id="finding-2"></a>finding-2 | reviewer | Minor | CK-VIS-B7, CK-VIS-B13 | slide 01 body and notes (`srr.adoc` lines 19 and 31) | "revision 4 and the iteration 3 records are committed under item R12" reads as a present fact; at review time both are uncommitted (`git status`), and package revision 4 says Claude commits them under R12. Fix: "are to be committed under item R12" (and the same tense in the notes) | Lien: fix before PDR | Pending | |
| <a id="finding-3"></a>finding-3 | reviewer | Minor | CK-VIS-A5 | slide 21, decision 37 "If no answer" cell (`srr.adoc` line 499) | The slide reads "OQ-SAF-001, 002 stay open as RIDs"; package 13.1.1 K1 decision 37 says OQ-SAF-001, OQ-SAF-002 and OQ-SAF-004 stay open as RIDs against REQ-SYS. The manual-closure timeout question OQ-SAF-004 is dropped from the owner's view of the default. Fix: add 004 | Lien: fix before PDR | Pending | |
| <a id="finding-4"></a>finding-4 | reviewer | Minor | CK-VIS-A5 | slide 10, row "SEMP (SE-38, SE-66), plans 01 to 08, RMM, matrix", Record cell (`srr.adoc` line 280) | "INSP-005, 009, 017 APPROVED; the rest self-check" omits that 05 (INSP-006) is also held by the missing paired software assurance record (package sections 6.9 and 2.4; item R6) and does not name 06 (INSP-007, APPROVED, shown only in the hazards and risks row). The notes state it correctly. Fix: "the rest self-check; 05 also waits for its assurance record (R6)" | Lien: fix before PDR | Pending | |
| <a id="finding-5"></a>finding-5 | reviewer | Minor | CK-VIS-B11, CK-VIS-B10 | `png/slide-12.png` (concept block diagram), `png/slide-18.png` (risk matrix footnote and corner band labels) | Readable at native size, but the block labels, edge labels and legend of the concept diagram and the footnote line and corner band labels of the risk matrix render at roughly 13 to 16 px on the 1920 x 1080 slide, below the 20 px floor the checklist sets for deck text; at projection distance they are hard to read. Fix: re-export the two figures larger (or crop the legend and footnote into slide text) in `concept-block-diagram.py` and `risk-matrix.py`, whose missing TV records are package item 38 | Lien: fix before PDR | Pending | |
| <a id="finding-6"></a>finding-6 | reviewer | Minor | CK-VIS-B11, CK-VIS-A8 | slide 39 (`srr.adoc` lines 934 to 975) | The success-criteria board is hand-drawn HTML in the deck instead of the committed generated figure `figures/success-criteria.png`, because the generator's footer still counts an owner approval as pending (disclosed in the notes; package section 7 row 2 cross item). The content matches section 20 today, but it is a second, unchecked copy of the package data. Fix: once the tool owner corrects the footer, embed `figures/success-criteria.png` as slide 9 does for the entrance board | Lien: fix before PDR | Pending | |

**Lien table** (convergence rule of 2026-09-26, charter section 4 item 3: a Minor finding is fixed before the next review and does not block the baseline).

| Finding | Severity | Disposition | Owner | Due |
|---|---|---|---|---|
| finding-2 | Minor | Lien: fix before PDR | deck author (Claude) | PDR readiness declaration |
| finding-3 | Minor | Lien: fix before PDR | deck author (Claude) | PDR readiness declaration |
| finding-4 | Minor | Lien: fix before PDR | deck author (Claude) | PDR readiness declaration |
| finding-5 | Minor | Lien: fix before PDR | figure owner (Claude; tool owner for the two scripts) | PDR readiness declaration |
| finding-6 | Minor | Lien: fix before PDR | deck author; tool owner for the success-board footer | PDR readiness declaration |

## Cross items (outside this product; not findings against it)

- X-1 (package author): package revision 4 section 1 agenda (Slides column) and section 1.1 slide map cite the `28e49e6` slide numbers; this deck maps the minimum set to slides 1, 2 / 4 to 9 / 10 to 13 / 14, 15 / 16 / 17, 18 (19) / 20 to 35 / 36 / 37 to 40 / 42, with the opening action on 3 and owner actions on 41. Update the Slides columns (readiness R2).
- X-2 (package author): the header row "Slide deck", section 2 item H3, section 2.1 item R10 and the section 2.2 "Slide deck" block still describe the revision 2 deck (render commit `28e49e6`, 42 PNGs "committed", inspected 2026-09-25, "not yet written from revision 3 or 4"); HEAD has held a 40-PNG deck since `400e59d`. Record this render (command, exit status, 42 outputs, date, inspection, claims confirmation) and the author's render list (readiness R2, R4).
- X-3 (package author, template owner): the record slug is named three ways: `visual-srr-deck` (package section 2 H1, section 2.1 R6), `deck-srr` (template `peer-review-checklist-visual-product.md`), `srr-deck` (this assignment). Align the package and the template on one slug.
- X-4 (Claude, item R12): commit `srr.adoc`, `srr.css`, `srr.html`, `png/slide-01.png` to `slide-42.png` and the modified `figures/entrance-checklist.png` and `success-criteria.png` together with package revision 4 (readiness R3, CK-VIS-B12); this record then names the committed blobs at its next iteration.

## Iteration 2 (2026-09-26, delta verification of finding-1)

Author return: `{"fixed":["finding-1"],"disputed":[]}`. Scope per the iteration 1 verdict: the delta of slide 07 only.

| Check | Result |
|---|---|
| Search first | `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` (slide 7 notes, INSP-001, INSP-002 verdicts) before any `grep` |
| Blobs reviewed (`git hash-object`, working tree; HEAD still `d7fdf25`) | `srr.adoc` `6b11731641506692d8ceea59c8de453d19670730`, `srr.html` `e2636649075598642a3caf654db324eb7718e693`, `srr.css` `da8d9463ed1f2885c345c5c466ce6e3c6d07c260` (unchanged), `png/slide-07.png` `732e88316523c2738c109199ced03d2b2d7e1578` |
| finding-1 | Verified (finding row). The fix is the reviewer's suggested wording and every claim in it is in package section 2.4 and the record front matter |
| Re-render | All 42 PNGs carry file times 04:22:27 to 04:22:35 (one `render_deck.py` run after the source edit at 04:22); 42 PNGs, 42 `[.notes]`, 42 `<section>`; `slide-07.png` 1920 x 1080 |
| Visual closure | `png/slide-07.png` opened with Read: unchanged body, correct lanes. `png/slide-01.png` and `png/slide-08.png` opened as re-render spot checks: legible, content as at iteration 1 |
| No other change | The finding-2, finding-3 and finding-4 texts are unchanged at `srr.adoc` lines 19, 499 and 280 (liens, as the convergence rule directs) |
| Readiness | R1 Yes (`validate_docs.py` after this update: 48 passed, 0 failed, this record PASS with the three expected drift notes); R2 No (package line 26, section 2.2 block lines 151 to 159 and section 1.1 map still describe the `28e49e6` deck); R3 No (`git status --porcelain -- docs/reviews/SRR/slides` lists the source, HTML and 40 modified plus 2 untracked PNGs); R4 No (no author render list beyond the fix claim) |

## Verdict

**Iteration 2: reviewer verdict APPROVED (with liens); record verdict NEEDS CHANGES held only by readiness R2, R3 and R4.** finding-1 is Verified; finding-2 to finding-6 remain liens "Lien: fix before PDR"; no Major finding is open and no product change is required. The record turns APPROVED with liens when item R12 commits the deck (this record then names the committed blobs) and the package records this render in its "Slide deck" block, section 1 agenda and section 1.1 map (cross items X-1, X-2, X-4).

Iteration 1 text follows. **NEEDS CHANGES, iteration 1.** The deck carries the whole charter section 4 item 2 minimum set, every one of the 17 key decisions (47 numbers) with options, recommendation and default, and the 68-item consent agenda with its block rulings; it is legible on all 42 renders and states readiness honestly (no disposition requested; every open H and R item named). It is held by one Major finding and by readiness: finding-1 (a record verdict in the slide 7 narrative that the package contradicts) must be fixed and slide 07 re-rendered and re-opened; readiness R2 and R4 (the package does not record this render) and R3 (nothing is committed) close with cross items X-1, X-2 and X-4. finding-2 to finding-6 (Minor) are liens "Lien: fix before PDR". Iteration 2 needs only the delta of slide 07, the commit, and the package block; no other slide needs re-review.

```
VERDICT: NEEDS CHANGES (readiness R2, R3, R4 only; reviewer verdict APPROVED with liens)
PRODUCT: docs/reviews/SRR/slides/srr.adoc@6b117316 (working tree), srr.html@e2636649, srr.css@da8d9463, png/slide-01.png to slide-42.png (working tree, slide-07.png@732e8831); HEAD d7fdf25
FINDINGS:
- [Major] finding-1 CK-VIS-B7 slide 07 notes: record verdicts of INSP-001 and INSP-002; Verified at iteration 2.
- [Minor] finding-2 CK-VIS-B7 slide 01: revision 4 and records stated as committed; Lien: fix before PDR.
- [Minor] finding-3 CK-VIS-A5 slide 21: decision 37 default omits OQ-SAF-004; Lien: fix before PDR.
- [Minor] finding-4 CK-VIS-A5 slide 10: plans row omits the missing 05 assurance record; Lien: fix before PDR.
- [Minor] finding-5 CK-VIS-B11 slides 12, 18: embedded figure text about 13 to 16 px; Lien: fix before PDR.
- [Minor] finding-6 CK-VIS-B11 slide 39: success board drawn in the deck instead of the committed figure; Lien: fix before PDR.
READINESS: R1 Yes; R2 No; R3 No; R4 No
ITEMS N/A: CK-VIS-B14, CK-VIS-C1 to CK-VIS-C5 (product is the deck)
MEASUREMENTS: size=42 slides; renders_inspected=42; items checked 22; items No 7; major=1; minor=5; open_major=0; verified=1; lien=5; iteration=2; turns=67; minutes=90
```
