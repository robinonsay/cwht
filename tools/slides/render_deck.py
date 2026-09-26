#!/usr/bin/env python3
"""Render a review slide deck: AsciiDoc -> reveal.js HTML -> one PNG per slide.

Usage: render_deck.py <repo>/docs/reviews/<REVIEW>/slides/<review>.adoc [--size 1920x1080]
       render_deck.py <any path>.adoc --allow-outside-reviews [--size WxH]   (known-answer tests only)

Location guard (05 section 14.1 AL-14; 01 section 3.1 item 4): the deck must be
<repo>/docs/reviews/<REVIEW>/slides/<name>.adoc, where <REVIEW> is a review token of
charter section 6 (SRR, PDR, CDR, TRR, TRR-Dn, SAR). Any other path exits 2 before
anything is written, so no reveal.js/ copy lands outside a deck folder. The flag
--allow-outside-reviews lifts the guard; only tools/tests/test_render_deck.py uses it,
for its temporary copy of the fixture deck.

Pipeline (charter section 4 item 2, section 11 rule 3):
  1. asciidoctor-revealjs (tools/slides/node_modules) converts <deck>.adoc to <deck>.html
     next to the source, with reveal.js copied to <deck dir>/reveal.js/ so the HTML is
     self-contained and offline.
  2. The Playwright Chromium headless shell screenshots every slide (URL fragment #/N)
     into <deck dir>/png/slide-NN.png. No GUI, no macOS privacy permission (rule 8).
  3. Prints the PNG paths; the author must open and inspect each one before the review.
Exit status 1 on any failure; 2 if the deck path fails the location guard or the headless shell is missing.
"""
import glob, os, re, shutil, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
REVIEWS = os.path.join(REPO, "docs", "reviews")
REVIEW_TOKEN = re.compile(r"^(SRR|PDR|CDR|TRR|SAR|TRR-D[1-9][0-9]?)$")
ALLOW_FLAG = "--allow-outside-reviews"
CONVERTER = os.path.join(HERE, "node_modules", ".bin", "asciidoctor-revealjs")
REVEAL_SRC = os.path.join(HERE, "node_modules", "reveal.js")
SHELL_GLOB = os.path.expanduser(
    "~/Library/Caches/ms-playwright/chromium_headless_shell-*/chrome-headless-shell-mac-arm64/chrome-headless-shell")


def location_error(adoc):
    """None when adoc is <repo>/docs/reviews/<REVIEW>/slides/<name>.adoc, else the reason."""
    if not adoc.endswith(".adoc"):
        return f"deck must be an .adoc file: {adoc}"
    rel = os.path.relpath(adoc, REVIEWS)
    parts = rel.split(os.sep)
    if rel.startswith("..") or len(parts) != 3 or parts[1] != "slides":
        return f"deck must be {REVIEWS}/<REVIEW>/slides/<review>.adoc, got {adoc}"
    if not REVIEW_TOKEN.match(parts[0]):
        return f"'{parts[0]}' is not a review token (SRR, PDR, CDR, TRR, TRR-Dn, SAR; charter section 6)"
    return None


def find_shell():
    hits = sorted(glob.glob(SHELL_GLOB))
    return hits[-1] if hits else None


def main(argv):
    if len(argv) < 2:
        print(__doc__); return 1
    adoc = os.path.abspath(argv[1])
    size = "1920x1080"
    if "--size" in argv:
        size = argv[argv.index("--size") + 1]
    w, h = size.split("x")
    if ALLOW_FLAG not in argv:
        reason = location_error(adoc)
        if reason:
            print(f"render_deck: {reason}; nothing written", file=sys.stderr); return 2
    deck_dir = os.path.dirname(adoc)
    stem = os.path.splitext(os.path.basename(adoc))[0]
    html = os.path.join(deck_dir, stem + ".html")
    png_dir = os.path.join(deck_dir, "png")

    # 1. reveal.js runtime next to the deck (offline, self-contained)
    reveal_dst = os.path.join(deck_dir, "reveal.js")
    if not os.path.isdir(reveal_dst):
        shutil.copytree(REVEAL_SRC, reveal_dst,
                        ignore=shutil.ignore_patterns("node_modules", "*.md", "*.d.ts", "test", "examples", "js", "css", "gulpfile.js"))
    if not os.path.exists(CONVERTER):
        print("asciidoctor-revealjs not installed: cd tools/slides && npm install", file=sys.stderr); return 1
    r = subprocess.run([CONVERTER, "-a", "revealjsdir=reveal.js", "-a", "revealjs_history=true",
                        "-a", "revealjs_transition=none", "-a", "revealjs_hash=true",
                        "-o", html, adoc], capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stdout, r.stderr, file=sys.stderr); return 1
    if r.stderr.strip():
        print(r.stderr.strip(), file=sys.stderr)

    # 2. count top-level slides (title slide + each <section> child of .slides)
    src = open(html, encoding="utf-8").read()
    slides_block = src[src.index('<div class="slides">'):]
    depth, count, i = 0, 0, 0
    for m in re.finditer(r"<section\b|</section>", slides_block):
        if m.group(0) == "</section>":
            depth -= 1
        else:
            if depth == 0:
                count += 1
            depth += 1
        if depth < 0:
            break
    shell = find_shell()
    if not shell:
        print("Chromium headless shell not found under ~/Library/Caches/ms-playwright", file=sys.stderr); return 2
    if os.path.isdir(png_dir):
        shutil.rmtree(png_dir)
    os.makedirs(png_dir)
    outs = []
    for n in range(count):
        out = os.path.join(png_dir, f"slide-{n+1:02d}.png")
        url = f"file://{html}#/{n}"
        cmd = [shell, "--headless", "--disable-gpu", "--hide-scrollbars", f"--window-size={w},{h}",
               "--virtual-time-budget=4000", "--force-device-scale-factor=1", f"--screenshot={out}", url]
        rr = subprocess.run(cmd, capture_output=True, text=True)
        if rr.returncode != 0 or not os.path.exists(out):
            print(f"render failed for slide {n+1}: {rr.stderr[-400:]}", file=sys.stderr); return 1
        outs.append(out)
    print(f"deck: {html}\nslides: {count}\npng: {png_dir}")
    for o in outs:
        print(o)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
