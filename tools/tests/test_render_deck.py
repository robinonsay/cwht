"""Known-answer test for tools/slides/render_deck.py (charter section 4 item 2, section 11 rule 3).

Renders tools/tests/fixtures/slides/deck.adoc (title slide plus three content
slides) in a temporary copy (with --allow-outside-reviews, because the copy is
not under docs/reviews/<REVIEW>/slides/) and checks that the converter produced
the HTML, that exactly four PNGs of the requested size exist, and that each PNG
is a non-trivial image (not blank). Skipped, with the reason printed, when the
npm converter or the Chromium headless shell is not installed on this machine.

LocationGuard checks, without the converter or the shell, that a deck path
outside docs/reviews/<REVIEW>/slides/ exits 2 and writes nothing (no reveal.js/
copy), and that a review-token folder check rejects a non-token folder
(05 section 14.1 AL-14).

Run from the repository root:

    .venv/bin/python -m unittest discover -s tools/tests
"""
from __future__ import annotations

import glob
import os
import shutil
import struct
import subprocess
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TOOL = os.path.join(ROOT, "tools", "slides", "render_deck.py")
CONVERTER = os.path.join(ROOT, "tools", "slides", "node_modules", ".bin", "asciidoctor-revealjs")
FIXTURE = os.path.join(ROOT, "tools", "tests", "fixtures", "slides", "deck.adoc")
SHELL = glob.glob(os.path.expanduser(
    "~/Library/Caches/ms-playwright/chromium_headless_shell-*/chrome-headless-shell-mac-arm64/chrome-headless-shell"))


def png_size(path):
    with open(path, "rb") as f:
        head = f.read(24)
    assert head[:8] == b"\x89PNG\r\n\x1a\n", "not a PNG"
    return struct.unpack(">II", head[16:24])


@unittest.skipUnless(os.path.exists(CONVERTER), "asciidoctor-revealjs not installed (cd tools/slides && npm install)")
@unittest.skipUnless(SHELL, "Chromium headless shell not found under ~/Library/Caches/ms-playwright")
class RenderDeckKnownAnswer(unittest.TestCase):
    def test_fixture_deck_renders_four_slides(self):
        with tempfile.TemporaryDirectory() as tmp:
            adoc = os.path.join(tmp, "deck.adoc")
            shutil.copy(FIXTURE, adoc)
            r = subprocess.run([sys.executable, TOOL, adoc, "--size", "1280x720", "--allow-outside-reviews"],
                               capture_output=True, text=True, timeout=300)
            self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
            self.assertTrue(os.path.exists(os.path.join(tmp, "deck.html")))
            self.assertTrue(os.path.exists(os.path.join(tmp, "reveal.js", "dist", "reveal.js")))
            pngs = sorted(glob.glob(os.path.join(tmp, "png", "slide-*.png")))
            self.assertEqual([os.path.basename(p) for p in pngs],
                             ["slide-01.png", "slide-02.png", "slide-03.png", "slide-04.png"])
            for p in pngs:
                self.assertEqual(png_size(p), (1280, 720), p)
                self.assertGreater(os.path.getsize(p), 5000, f"{p} looks blank")
            self.assertIn("slides: 4", r.stdout)


class LocationGuard(unittest.TestCase):
    def run_tool(self, adoc):
        return subprocess.run([sys.executable, TOOL, adoc], capture_output=True, text=True, timeout=60)

    def test_deck_outside_reviews_exits_2_and_writes_nothing(self):
        with tempfile.TemporaryDirectory() as tmp:
            adoc = os.path.join(tmp, "deck.adoc")
            shutil.copy(FIXTURE, adoc)
            r = self.run_tool(adoc)
            self.assertEqual(r.returncode, 2, r.stdout + r.stderr)
            self.assertIn("nothing written", r.stderr)
            self.assertEqual(sorted(os.listdir(tmp)), ["deck.adoc"])

    def test_location_rule(self):
        sys.path.insert(0, os.path.dirname(TOOL))
        try:
            import render_deck
        finally:
            sys.path.pop(0)
        reviews = os.path.join(ROOT, "docs", "reviews")
        self.assertIsNone(render_deck.location_error(os.path.join(reviews, "SRR", "slides", "srr.adoc")))
        self.assertIsNone(render_deck.location_error(os.path.join(reviews, "TRR-D1", "slides", "trr-d1.adoc")))
        self.assertIsNotNone(render_deck.location_error(os.path.join(reviews, "XRR", "slides", "xrr.adoc")))
        self.assertIsNotNone(render_deck.location_error(os.path.join(reviews, "SRR", "srr.adoc")))
        self.assertIsNotNone(render_deck.location_error(os.path.join(ROOT, "srr.adoc")))
        self.assertIsNotNone(render_deck.location_error(os.path.join(reviews, "SRR", "slides", "srr.txt")))


if __name__ == "__main__":
    unittest.main()
