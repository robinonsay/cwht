#!/usr/bin/env python3
"""Render a review slide deck: AsciiDoc -> reveal.js HTML -> one PNG per slide.

Usage: render_deck.py <deck.adoc> [--size 1920x1080]

Pipeline (charter section 4 item 2, section 11 rule 3):
  1. asciidoctor-revealjs (tools/slides/node_modules) converts <deck>.adoc to <deck>.html
     next to the source, with reveal.js copied to <deck dir>/reveal.js/ so the HTML is
     self-contained and offline.
  2. The Playwright Chromium headless shell screenshots every slide (URL fragment #/N)
     into <deck dir>/png/slide-NN.png. No GUI, no macOS privacy permission (rule 8).
  3. Prints the PNG paths; the author must open and inspect each one before the review.
Exit status 1 on any failure; 2 if the headless shell is missing.
"""
import glob, os, re, shutil, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CONVERTER = os.path.join(HERE, "node_modules", ".bin", "asciidoctor-revealjs")
REVEAL_SRC = os.path.join(HERE, "node_modules", "reveal.js")
SHELL_GLOB = os.path.expanduser(
    "~/Library/Caches/ms-playwright/chromium_headless_shell-*/chrome-headless-shell-mac-arm64/chrome-headless-shell")


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
