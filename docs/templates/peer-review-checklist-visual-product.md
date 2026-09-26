---
# Peer-review record front matter (charter section 5; charter section 4 item 2 and section 11
# rule 3). To review a review deck or a package figure set, copy this whole file to
# docs/reviews/<REVIEW>/checklists/<product-slug>.md: that copy is the single peer-review record
# (there is no peer-reviews/ folder). Fill every field below, answer every applicable checklist
# item, fill the per-render table and the findings table. Both front-matter parsers (PyYAML and the
# subset parser of tools/validate_docs.py) strip a comment on its own line and a comment written
# after a value (" # ..."); this template keeps each comment on its own line for readability, and
# comment lines may stay or be deleted when filing. tools/validate_docs.py checks the record against
# the field list of docs/process/01-lifecycle-and-reviews.md section 13 (its
# PEER_REVIEW_RECORD_SCHEMA) and fails while the id, checklist_file, product_commit or date
# placeholder is left in place.
# Search first: 'grep' in an evidence column means: run mcp__claude-context__search_code on
# /Users/robinonsay/rust/cwht first (charter section 11 rule 1), then grep -n only to pin the hit.
#
# id: next free INSP-NNN (never reused, charter section 6); Claude assigns it in the assignment block
id: INSP-NNN
checklist: peer-review-checklist-visual-product
checklist_revision: A
# checklist_file: this record's own path: docs/reviews/<REVIEW>/checklists/deck-<review>.md for a
# deck (review token in lower case, for example deck-srr, deck-trr-d1), or
# docs/reviews/<REVIEW>/checklists/figures-<review>.md for the package figure set
checklist_file: docs/reviews/<REVIEW>/checklists/deck-<review>.md
# product: docs/reviews/<REVIEW>/slides/<review>.adoc for a deck (the controlled source; the .html
# and png/slide-NN.png are reviewed with it), or docs/reviews/<REVIEW>/package.md#7-rendered-figures
# for the package figure set
product: docs/reviews/<REVIEW>/slides/<review>.adoc
# product_commit: quoted so that an all-digit hash stays a string
product_commit: "<commit>"
# product_size: N slides, or N figures
product_size: N slides
# renders_inspected: number of PNG or SVG files the reviewer opened with the Read tool
renders_inspected: 0
# sprint: the gate preparation, for example SRR-prep
sprint: SRR-prep
author_agent: <invocation id>
# reviewer_agent: never the author
reviewer_agent: <invocation id>
# criticality: neither (a deck or a figure set belongs to no 07 section 14.1 component)
criticality: neither
# assurance_required: false (07 section 2.1.1 does not list decks or figures)
assurance_required: false
# assurance_reviewer_agent: invocation id, or none when assurance_required is false
assurance_reviewer_agent: none
# iteration: 1 to 3
iteration: 1
readiness_met: true
# reviewer_verdict: APPROVED | NEEDS CHANGES (the file reviewer)
reviewer_verdict: NEEDS CHANGES
# assurance_verdict: APPROVED | NEEDS CHANGES | not-required
assurance_verdict: not-required
# verdict: set by Claude as lead SE; APPROVED only when reviewer_verdict is APPROVED
verdict: NEEDS CHANGES
findings_major: 0
findings_minor: 0
findings_open: 0
findings_fixed: 0
findings_verified: 0
findings_deferred: 0
# deferred_rids: RID-<REVIEW>-NNN entered for each Deferred finding at record closure
deferred_rids: []
# items_no: checklist ids answered No
items_no: []
effort_turns: 0
effort_minutes: 0
# record_status: Open | Closed (set by Claude as lead SE)
record_status: Open
date: 2026-MM-DD
date_closed: null
---

# Peer review checklist: visual products and review decks

**Product types and the sections that apply.** A reviewer answers the applicable items and lists the others under `ITEMS N/A`.

| Product | Sections | Record slug | `product` value |
|---|---|---|---|
| Review deck: `docs/reviews/<REVIEW>/slides/<review>.adoc` with its generated `<review>.html` and `png/slide-NN.png` (charter section 4 item 2; 01 section 3.1 item 4) | A for every slide PNG, B | `deck-<review>`, lower case (`deck-srr`, `deck-trr-d1`) | `docs/reviews/<REVIEW>/slides/<review>.adoc` |
| Package figure set: every figure the package embeds or cites from `docs/reviews/<REVIEW>/figures/` (package section 7 "Rendered figures"; 01 section 3.2 row S9) | A for every figure, C | `figures-<review>`, lower case | `docs/reviews/<REVIEW>/package.md#7-rendered-figures` |
| A render that belongs to another reviewed product (schematic, PCB and enclosure renders, ICD plane figures, ConOps figures, a rendered register matrix) | A and the matching C items, answered inside that product's own record, which cites the `CK-VIS` ids it applied (for ICD and hardware renders, with `peer-review-checklist-design.md` items CK-DES-I4, J2, J5 and J6) | no separate record: one record per product (charter section 5) | the other product |

**Governing:** charter section 4 item 2 (presented reviews; minimum slide set; the deck cites the package and adds no claim), section 11 rules 2 (evidence, not assertion), 3 (visual closure) and 8 (headless only); `docs/process/01-lifecycle-and-reviews.md` section 3.1 item 4 (deck content, render, inspection, notes, claims, record), section 3.2 rows S9 and S11, section 3.4 (slide-by-slide presentation) and section 13 (deck, HTML, PNG and reveal.js records); the VISUAL CLOSURE rule of `docs/process/08-agent-briefing.md` section 1; `tools/slides/render_deck.py` and `tools/toolchain.lock.md` section 3a; `docs/templates/review-package.md` section 1.1 (slide map), section 2 "Slide deck" block and section 7 (rendered figures); NPR 7150.2D SWE-087, SWE-088, SWE-089; NPR 7123.1D App. G Table G-19 (peer review entrance and success criteria); SE HB App. N (technical peer reviews). **Used by:** an independent reviewer agent that did not write the deck or produce the figures (charter sections 2 and 11 rule 4).

Answer every item Yes, No or N/A with evidence (slide number and PNG path, figure path, source line, package section, or pasted tool output). **Major**: a render is missing or was not produced from the committed source (08 section 3.2: a missing render is a Major finding); a value, id or status in a render disagrees with its source; content is clipped, hidden or illegible so that information is lost; a slide carries a claim absent from `package.md`; an entry of the charter minimum slide set has no slide; the PNG count disagrees with the source. **Minor**: layout, wording, a label or legend that is present but unclear, a cosmetic artifact that loses no information.

## Record

This file, copied to `docs/reviews/<REVIEW>/checklists/<product-slug>.md`, is the single peer-review record for the deck or for the package figure set (charter section 5). Slugs follow the `<type>-<product-stem>` rule of `docs/process/01-lifecycle-and-reviews.md` section 13: `deck-<review>` for a deck (stem of `<review>.adoc`), `figures-<review>` for the figure set of package section 7. `<REVIEW>` is the gate the deck or package serves. The front matter above is the first thing in the file, unfenced. A defect found in a slide is a RID against the deck or against the package section it cites (01 section 3.4); `tools/validate_docs.py` compares an RFA/RID log item's `product` with the `product` of the record its `verification.record` names (the part before any `#`), so an item verified by this record carries the same `product` value and names the slide number or figure path in its description.

### Findings (filled by the reviewer; the owner ruling column is transcribed by Claude at the review)

| Finding | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | Major or Minor | CK-VIS-xx | `slide NN` and PNG path, or figure path, and the source line | what is wrong and what would fix it | Open, Fixed, Verified or Deferred | Pending, `Adopt as RID RID-<REVIEW>-NNN`, `Adopt as RFA RFA-<REVIEW>-NNN` or `No action` | `RID-<REVIEW>-NNN` and the owner decision reference, for Deferred only |

Finding rules: ids are `finding-<n>`, numbered from 1 in this record, each with the anchor `<a id="finding-<n>"></a>` in its first cell so that `checklists/<product-slug>.md#finding-<n>` resolves (01 section 13). The reviewer writes `Pending` in the owner ruling column; Claude transcribes the owner's ruling (*Adopt as RID*, *Adopt as RFA* or *No action*, 01 section 10.1) at the review. `tools/validate_docs.py` rejects `verdict: APPROVED` while any line holding a `finding-<n>` id also holds the words `Major` and `Open`, so write the state only in the State column and do not quote slide text containing "Open" inside a finding row. Replace the placeholder row above; do not leave it in a filed record.

### Per-render results (one row per slide PNG, or per figure)

| Render | Source | Opened with Read (A4) | Legible, nothing clipped or overlapping (A4) | Content agrees with source (A5) | Package section named and exists (B6, deck only) | Every claim present in `package.md` (B7, deck only) | Finding ids |
|---|---|---|---|---|---|---|---|
| `slides/png/slide-NN.png` or `figures/<file>.png` | `<review>.adoc` slide title, or the generating script, `.mmd` or data file | Yes or No | Yes or No | Yes or No | Yes, No or N/A | Yes, No or N/A | `finding-<n>` or none |

## Readiness criteria (all true before the review starts)

| # | Criterion | Evidence |
|---|---|---|
| R1 | `/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/validate_docs.py` exits 0 | tool output line |
| R2 | Deck: the package "Slide deck" block of section 2 is filled (source, render command with exit status 0, outputs with the slide count, render commit, inspection date, claims confirmation) and the package section 1.1 slide map names a slide number for every entry. Figure set: package section 7 lists every figure with path, source artifact and inspection date | package sections 1.1, 2 and 7 |
| R3 | The source, the HTML and the renders are committed at `product_commit`: `git -C /Users/robinonsay/rust/cwht status --porcelain -- <paths>` prints nothing | command output |
| R4 | The author's return lists every render with its path, the command that produced it, the exit status and the date the author inspected it (charter section 11 rule 3) | author return |

## A. Every render (charter section 11 rule 3; 08 section 1 VISUAL CLOSURE)

| Id | Check | Evidence to inspect |
|---|---|---|
| CK-VIS-A1 | The render exists as a PNG or SVG at the path its governing rule names (beside its source; `docs/reviews/<REVIEW>/figures/`; `docs/reviews/<REVIEW>/slides/png/`) and is committed; a visual product without a render is a Major finding | file listing at `product_commit` |
| CK-VIS-A2 | The render was produced headlessly from the committed source by the command its governing process or `tools/toolchain.lock.md` names (`tools/slides/render_deck.py`, `tools/review_trend.py`, `tools/render_risk.py`, `kicad-cli`, the OpenSCAD CLI, an LTspice batch run with its checker plot), or by the command recorded in the package section 7 row; no screen capture or GUI export (charter section 11 rule 8) | package section 7; author return; `tools/toolchain.lock.md` |
| CK-VIS-A3 | Currency: the source's last commit is not newer than the render's (`git -C /Users/robinonsay/rust/cwht log -1 --format=%H -- <path>` for both). Where the command writes to a path the reviewer chooses, the reviewer re-renders into its scratch directory and compares the two images by opening both; a content difference is Major. The reviewer never overwrites a committed render (a reviewer does not edit the product) | git log output; re-render in scratch |
| CK-VIS-A4 | The reviewer opened the render with the Read tool (visual closure) and found every text run readable at native size, nothing cut at an edge, no overlapping labels, no missing-glyph boxes and no blank region where content is expected; the per-render table records each render | per-render table |
| CK-VIS-A5 | Content agrees with the source of truth at `product_commit`: every id, count, status and value shown matches the governing data file or document; the reviewer checks at least three values per render and every value on which a requirement, TPM, hazard, risk or owner decision depends | data files; package sections |
| CK-VIS-A6 | Labels: a title or caption states what is shown; axes carry quantity and unit; a legend is present when more than one series or colour code appears; every limit, threshold or margin line is labelled with the `REQ-`, `TPM-`, `MOP-` id or the 47 CFR clause it represents | render |
| CK-VIS-A7 | Meaning does not depend on colour alone: a label, symbol or pattern also carries every red, amber or green status (Minor when missing) | render |
| CK-VIS-A8 | Every defect the author recorded at inspection (in package section 7, where a package adds a Result column as the SRR package does, or in the author return) is fixed and re-inspected, or carried as a finding here; a cited figure marked "not rendered" is a Major finding against row S9 | package section 7; author return |

## B. Review deck (charter section 4 item 2; 01 sections 3.1 item 4, 3.4 and 13; row S11)

| Id | Check | Evidence to inspect |
|---|---|---|
| CK-VIS-B1 | The render run is recorded: the package "Slide deck" block names the command `/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/slides/render_deck.py /Users/robinonsay/rust/cwht/docs/reviews/<REVIEW>/slides/<review>.adoc`, its exit status 0, the slide count of the Outputs row, the render commit and the inspection date. The reviewer does not re-run `render_deck.py`: it rewrites `png/` in place (the product), and its `--allow-outside-reviews` flag is reserved for the known-answer test (08 section 1 COMMANDS) | package section 2 "Slide deck" block |
| CK-VIS-B2 | Slide count: the number of `png/slide-NN.png` files equals the number of top-level slides in the source (the title slide plus each level-1 `==` section) and the package block's count; numbering runs from `slide-01.png` without a gap or a stale extra file | `ls` of `png/` at `product_commit`; count of `^== ` lines in the source plus one |
| CK-VIS-B3 | Every PNG has the render size (`render_deck.py` default 1920 x 1080, or the `--size` recorded in the package block) and none is blank | PNG header, or the reviewer's image read |
| CK-VIS-B4 | Nothing is hidden from the record: the source has no fragments (`[%step]`, `.fragment` roles) and no vertical sub-slides (`===` sections), because `render_deck.py` captures each top-level slide once at `#/N` before any fragment step, so fragment or sub-slide content never appears in a PNG | vector search, then grep of the source |
| CK-VIS-B5 | Minimum slide set: each of the ten entries of charter section 4 item 2 (title and agenda; purpose, scope and entrance-criteria status; products with evidence links and counts; requirements and traceability status; hazards and safety; risks and TPMs; TBD/TBR and open decisions with recommendations; RFA/RID trend from prior reviews; proposed tailoring and liens; requested disposition) has at least one slide, and the package section 1.1 slide map gives its slide numbers | slide map; PNGs |
| CK-VIS-B6 | Every slide names the package section it summarizes (row S11; the deck convention is the `[.src]#§N#` role in the slide title), and that section exists in the package revision the deck cites | slide titles; package headings |
| CK-VIS-B7 | No claim absent from the package: every number, count, status, date and statement on the slide and in its notes block is present in the cited `package.md` section (01 section 3.1 item 4; charter section 4 item 2); one absent claim is a Major finding | PNG, notes block, package section |
| CK-VIS-B8 | Every slide has exactly one `[.notes]` block, the committed speaker narrative (01 section 3.4): it cites the package section it rests on and, where the package asks the owner for a ruling, names that decision; the existing decks close the block with an `Evidence:` line and a `Question for Robin:` line | source; count of `[.notes]` blocks equals the slide count |
| CK-VIS-B9 | No notes text appears on any slide PNG (reveal.js keeps `[.notes]` in the speaker view only) | PNGs |
| CK-VIS-B10 | Legibility at the render size: no text is set below 20 px at 1920 x 1080 (about 1.9 percent of the slide height) in the deck CSS named by `:customcss:` or in inline styles; every table fits the slide with its last row and column visible; the slide number is shown (`:revealjs_slideNumber:`) so the minutes can cite `slide NN` (01 section 3.4) | deck CSS; PNGs |
| CK-VIS-B11 | Every figure embedded in a slide is a committed render from `docs/reviews/<REVIEW>/figures/` or from its product's figure path, passes section A, and is readable at slide scale | image macros in the source; PNGs |
| CK-VIS-B12 | Records (01 section 13): `<review>.adoc`, `<review>.html` and `png/` are committed together with the package at the same commit; `slides/reveal.js/` is git-ignored and not committed (`git -C /Users/robinonsay/rust/cwht check-ignore docs/reviews/<REVIEW>/slides/reveal.js` prints the path) | git output |
| CK-VIS-B13 | The title slide names the review token, the package revision and date, the chair and the presenter, and states when the session is a pre-review session rather than the gate review | slide 01 |
| CK-VIS-B14 | Re-review (01 section 12.1): the deck was revised, re-rendered and re-inspected per 01 section 3.1 item 4 before the new session, and the PNGs at `product_commit` are the ones to be presented (N/A for a first review) | package "Slide deck" block; git log |

## C. Package figures (package section 7; row S9)

| Id | Check | Evidence to inspect |
|---|---|---|
| CK-VIS-C1 | Package section 7 lists every figure the package embeds or cites, each with path, source artifact and inspection date; every file in `docs/reviews/<REVIEW>/figures/` is cited by the package, and every cited figure exists | package section 7; `ls` of `figures/` |
| CK-VIS-C2 | Plots are generated by a committed script from committed data (`tools/review_trend.py` for the review-trend TPM, `tools/render_risk.py`, `render_tpm.py` once it exists); re-running the script's check mode, where it has one, exits 0 (for example `render_risk.py --check`), and the plotted values match the data file | script, data file, check output |
| CK-VIS-C3 | Diagrams (context, block, state and mode diagrams): every block, state, edge and label matches the names in the governing document (architecture state names in their CamelCase spelling, `ICD-` ids, `OPS-` ids, module tokens); every edge the source labels shows its label on its own edge | diagram source (for example `.mmd`) and governing document |
| CK-VIS-C4 | Matrices and tables rendered as images (risk matrix, hazard matrix, entrance checklist, success criteria, TPM status): every cell count and status recomputes from its source (`docs/risk/register.json`, `docs/safety/hazards.json`, `docs/plan/tpm.json`, the package tables) | source files |
| CK-VIS-C5 | A package copy of a render that belongs to another product (schematic, PCB, enclosure, ICD or ConOps figure) is the same image as the render beside its source, or was produced from the same commit by the same command | both files; git log |

## Completion criteria (SWE-088 b, c)

`verdict: APPROVED` when: readiness R1 to R4 were true; every applicable item is answered and the others are listed as N/A; the per-render table has one row per slide PNG or per figure, each opened with the Read tool, and `renders_inspected` equals the row count; zero open Major findings; every Minor finding fixed, or deferred with an owner decision reference and a gate; the front matter is complete with the measurements (SWE-089) filled; and `/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/validate_docs.py` passes on the record itself. A deck with an open finding against it is corrected, re-rendered and re-inspected before the session, and the deck is not edited during a session (01 section 3.4). On record closure each Deferred finding becomes `RID-<REVIEW>-NNN` in the `rfa-rid-log.json` of its named gate, citing this `INSP-NNN` and the finding id, and is listed in `deferred_rids`.

## Verdict format (returned by the reviewer)

```
VERDICT: APPROVED | NEEDS CHANGES
FINDINGS:
- [Major] CK-VIS-B7 slide NN: the count shown is not in the cited package section N.
- [Minor] CK-VIS-A6 figures/<file>.png: y axis has no unit.
ITEMS N/A: CK-VIS-C1 to CK-VIS-C5 (product is the deck)
MEASUREMENTS: size=N slides; renders_inspected=N; turns=N; minutes=N; major=N; minor=N
```
