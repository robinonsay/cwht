# TV-008: tools/slides/render_deck.py (git blob b42425e9, commit 28e49e6) with the Chromium headless shell 1223

| Field | Value |
|---|---|
| Record | TV-008 |
| Status | **Validated** (2026-09-25; re-validated 2026-09-26 with the seeded conversion and render failures, INSP-015 finding-5). Independent review and owner accreditation pending (sections 8 and 9) |
| Class | B, evidence-generating (CM plan section 9.1: its PNGs are the record of the presented review, charter section 4 item 2) |
| Governs | SWE-136 (NPR 7150.2D section 4.4.8), SWE-070 (section 4.5.6) through CM plan section 9 |
| Due | SRR (CM plan section 13) |
| Lock rows | `tools/toolchain.lock.md` section 3a (all rows), section 1.1 row `tools/slides/render_deck.py + Chromium headless shell`, section 1.2, section 7 row "Slide toolchain" |
| Author | Claude, tool validation author (SRR package section 2 item H12) |

## 1. Identification

| Item | Identity | Command | State |
|---|---|---|---|
| `tools/slides/render_deck.py` | git blob `b42425e9e9d2ca2b860284914b78ccbabecd38a0`, SHA-256 `6c8015462a480b18fe62e654f4ffba233039a462add1f037bd6034cb34754862` | `git hash-object`; `shasum -a 256` | equal to `28e49e6` |
| `tools/slides/package.json`, `package-lock.json` | blobs `6b44d974...f367`, `baf84c95...2233806` | as above | equal to `28e49e6` |
| Chromium headless shell | `~/Library/Caches/ms-playwright/chromium_headless_shell-1223/chrome-headless-shell-mac-arm64/chrome-headless-shell`; `--version` prints `Google Chrome for Testing 148.0.7778.96`; binary SHA-256 `aa25f2e795c02d5cb5ef5d6987745cc5bbe7d8bea58827390c7a4c81c8d2dd7b`; directory `chromium_headless_shell-1223/` 19 files, tree digest `062fa78bdaf495aca03e9871e7ed4a9b765770912836c57372d9b323dd63a469` | `<path> --version`; `shasum -a 256`; tree digest as in TV-002 section 1 | Playwright cache, not in git |
| Converter chain (class C, lock section 3a) | Node.js `v25.9.0`; `asciidoctor` 3.0.4, `@asciidoctor/reveal.js` 5.2.0, `reveal.js` 5.2.1 from `tools/slides/node_modules/` (1843 files, tree digest `31b84db9a799c373bc43599369976d775accb7ee912d953abef20eda30a9a39e`) | `node --version`; `node -e "console.log(require('./tools/slides/node_modules/<pkg>/package.json').version)"` | gitignored, installed from `package-lock.json` |
| Test and fixture | `tools/tests/test_render_deck.py` blob `ff58fb7b7f1017ab165ad532bac36898f4ed0835` (run 3; modified in the working tree on 2026-09-26: `SeededFailures` added; runs 1 and 2: `539e9593...af52`, equal to `28e49e6`); `tools/tests/fixtures/slides/deck.adoc` (1 file, tree digest `f0519294...636b97`, equal) | | |

**Install source and installer SHA-256 (lock section 7):** the headless shell comes from the Playwright download (`npx playwright install chromium-headless-shell`, lock section 3a); Playwright publishes no checksum that this record could compare, so the binary SHA-256 and directory digest above identify it, and the SAR archive keeps a tar of the directory (lock section 7). The npm packages are pinned by `package-lock.json` (npm verifies their `integrity` hashes on install).

## 2. Purposes covered

1. Refuse, with exit 2 and nothing written, a deck path that is not `docs/reviews/<REVIEW>/slides/<name>.adoc` with `<REVIEW>` a review token of charter section 6 (location guard; `--allow-outside-reviews` is for the known-answer test only).
2. Convert the AsciiDoc deck to self-contained reveal.js HTML beside the source (`<deck>.html`, `reveal.js/`) through the class C converter chain of section 1.
3. Render every slide to `png/slide-NN.png` at the requested size (`--size WxH`, default 1920 x 1080) with the Chromium headless shell, headlessly (charter section 11 rule 8), and print the PNG paths and the slide count.
4. Exit 1 on any conversion or render failure.

## 3. Known-answer test

**Fixture:** `tools/tests/fixtures/slides/deck.adoc`: title slide, agenda (numbered list), table (3 columns, header row) and bullets with speaker notes that must not appear on the slide.

**Run command** (repository root): `.venv/bin/python -m unittest discover -v -s tools/tests -p test_render_deck.py`

**Pass criteria:** 5 tests pass and none is skipped (`RenderDeckKnownAnswer` and `SeededFailures` skip when the converter or the headless shell is missing, so a skip is a failure of this check). `RenderDeckKnownAnswer`: on a temporary copy with `--size 1280x720 --allow-outside-reviews`, exit 0, `deck.html` and `reveal.js/dist/reveal.js` exist, exactly `slide-01.png` to `slide-04.png`, each 1280 x 720 and larger than 5000 bytes, stdout contains `slides: 4`. `LocationGuard`: a deck outside `docs/reviews/<REVIEW>/slides/` exits 2 and writes nothing; the location rule accepts only review-token folders. `SeededFailures` (purpose 4; added 2026-09-26, INSP-015 finding-5): seeded conversion failure, the fixture deck copy made unreadable (mode 000) so that `asciidoctor-revealjs` exits non-zero, must give exit 1 with `EACCES` on stderr, no `deck.html`, no `png/` and no `slides:` line; seeded render failure, the headless shell replaced by `/usr/bin/false` (the tool's `find_shell` patched in process), must give exit 1 with `render failed for slide 1` on stderr, `deck.html` present and no slide PNG.

**Inspection (added by this record):** the fixture deck is also rendered once more with the same options and each PNG is opened and compared with the fixture source (charter section 11 rule 3).

## 4. Result

| Run | Date and time (CDT) | Commit tested | Tests | Result |
|---|---|---|---|---|
| 1 | 2026-09-25 23:36 | `28e49e6` (tool, `package*.json`, test and fixture byte-identical to the commit) with the headless shell of section 1 | 3 (`RenderDeckKnownAnswer` 1, `LocationGuard` 2), 0 skipped | pass |
| Inspection | 2026-09-25 23:37 | same | 4 PNGs | pass: slide 1 title "FIXTURE DECK FOR RENDER_DECK.PY" and author line; slide 2 "AGENDA" with items 1 and 2; slide 3 "TABLE" with the 3-column header and one row; slide 4 "BULLETS" with alpha and beta and no speaker-note text; all legible, 1280 x 720 |
| 2 | 2026-09-25 23:45 | same | 3, 0 skipped | pass |
| 3 | 2026-09-26 00:15 | tool and `package*.json` equal to `28e49e6`; test blob `ff58fb7b` (modified: `SeededFailures`); fixture equal; headless shell binary SHA-256 re-observed `aa25f2e7...` | 5 (`RenderDeckKnownAnswer` 1, `LocationGuard` 2, `SeededFailures` 2), 0 skipped | pass |

Renders inspected: `docs/cm/tool-validation/evidence/render-deck-fixture-slide-01.png` to `-04.png`. Earlier runs on the working tree at `b8214ca` are in lock section 1.1. Evidence: `docs/cm/tool-validation/evidence/python-tools-2026-09-25.log.txt` (runs 1 and 2) and `evidence/python-tools-2026-09-26.log.txt` (run 3).

## 5. Reproducibility

Not required for class B. The known-answer runs gave identical results. PNG bytes are not compared between runs (font rasterization may vary); the criterion is count, size and non-blankness plus inspection.

## 6. Limitations

1. The automated check proves slide count, pixel size and non-blankness, not content: a slide that renders legibly but wrongly (a missing table row, a clipped line) passes the test. Content correctness rests on the author inspecting every PNG of every deck before the review (charter section 4 item 2, section 11 rule 3) and on the visual-product checklist review.
2. The converter chain (Node.js, Asciidoctor.js, the reveal.js converter and reveal.js) is class C and is not validated separately; its faults can only show in the rendered PNGs, which is why they are inspected. Upgrading reveal.js to 6.x breaks the converter's asset paths (lock section 3a).
3. Each slide is captured after a virtual-time budget of 4000 ms; animated or late-loading content beyond that budget may be captured incomplete.
4. The Playwright cache can be purged or replaced by `npx playwright install`; the binary SHA-256 of section 1 must then be re-observed (lock section 3a) and this record re-validated.
5. Output is developer evidence until section 9 records the accreditation.

## 7. Re-validation triggers

- Any change of `render_deck.py`, `package.json`, `package-lock.json`, the test module or the fixture deck (CM plan section 9.2 step 4).
- Any change of the headless shell binary (SHA-256 of section 1) or of the Node.js or npm package versions.
- A macOS major version change.
- A defect found in a rendered slide that the tool caused (an NCR per SWE-201).

## 8. Independent review (CM plan section 9.2 step 3)

Pending. The reviewer re-runs section 3 and opens the four inspection PNGs. Reviewer invocation, date and result are recorded here.

## 9. Accreditation (owner)

Proposed scope statement **ACC-DECK-001**: "Accredited for purposes 1 to 4 for `tools/slides/render_deck.py` at git blob `b42425e9e9d2ca2b860284914b78ccbabecd38a0` (commit `28e49e6`) with the Chromium headless shell 1223 (Chrome for Testing 148.0.7778.96, binary SHA-256 `aa25f2e7...d2dd7b`) and the converter versions of section 1, for decks whose every PNG is inspected by the author (limitation 1)."

| Decision | Date | Recorded by |
|---|---|---|
| Pending (owner, at SRR, after section 8) | | |
