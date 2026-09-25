"""Known-answer test for tools/slides/render_deck.py (charter section 4 item 2, section 11 rule 3).

Renders tools/tests/fixtures/slides/deck.adoc (title slide plus three content
slides) in a temporary copy and checks that the converter produced the HTML,
that exactly four PNGs of the requested size exist, and that each PNG is a
non-trivial image (not blank). Skipped, with the reason printed, when the npm
converter or the Chromium headless shell is not installed on this machine.

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
            r = subprocess.run([sys.executable, TOOL, adoc, "--size", "1280x720"],
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


if __name__ == "__main__":
    unittest.main()
