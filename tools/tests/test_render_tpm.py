"""Known-answer tests for tools/render_tpm.py (TV-017; SEMP section 7.4; tpm.json conventions.status_rule).

Fixture: tools/tests/fixtures/render_tpm/ (tpm.json with seven TPMs, one per status case, and
expected.json with the rows, counts, trend points, chip colours, image sizes and seeded faults,
all derived by hand before the first run).

Fixture-only classes (the validation):
  RowKnownAnswerTests   the status, basis, carried value and trend points of every TPM at
                        PDR (as of 2026-10-06) and at TRR-D2 (as of 2027-02-01)
  RenderTests           the files written, their pixel sizes, the status chip colour drawn in each
                        table row, the Markdown table, --check writes nothing
  SeededFaultTests      each seeded data fault exits 1 with its message and writes nothing
  UsageTests            usage errors and unreadable input exit 2
Repository-content check, recorded separately (lock section 1.1):
  RepositoryTests       docs/plan/tpm.json passes the data checks at PDR (--check exits 0)

Run from the repository root:
    .venv/bin/python -m unittest discover -s tools/tests -p test_render_tpm.py -v
"""
from __future__ import annotations

import copy
import json
import os
import subprocess
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TOOL = os.path.join(ROOT, "tools", "render_tpm.py")
FIXTURE = os.path.join(ROOT, "tools", "tests", "fixtures", "render_tpm")
sys.path.insert(0, os.path.join(ROOT, "tools"))
import render_tpm  # noqa: E402

with open(os.path.join(FIXTURE, "tpm.json")) as _fh:
    DATA = json.load(_fh)
with open(os.path.join(FIXTURE, "expected.json")) as _fh:
    EXP = json.load(_fh)


def run(*args):
    return subprocess.run([sys.executable, TOOL, *args], capture_output=True, text=True)


def as_tuple(r):
    return [r.tpm_id, r.status, r.reason, r.cbe, r.entry_review, r.entry_date, r.credit]


class RowKnownAnswerTests(unittest.TestCase):
    def test_pdr_rows(self):
        rows = render_tpm.build_rows(DATA, "PDR", "2026-10-06")
        self.assertEqual([as_tuple(r) for r in rows], EXP["PDR@2026-10-06"])

    def test_trr_d2_rows(self):
        rows = render_tpm.build_rows(DATA, "TRR-D2", "2027-02-01")
        self.assertEqual([as_tuple(r) for r in rows], EXP["TRR-D2@2027-02-01"])

    def test_trend_points(self):
        by_key = {t["key"]: t for t in DATA["tpms"]}
        for key, pts in EXP["PDR@2026-10-06_trend_points"].items():
            with self.subTest(key=key):
                self.assertEqual([list(p) for p in render_tpm.trend_points(by_key[key], "2026-10-06")], pts)


class RenderTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.r = run("--review", "PDR", "--tpm", os.path.join(FIXTURE, "tpm.json"), "--out", cls.tmp.name, "--date", "2026-10-06")

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_exit_and_files(self):
        self.assertEqual(self.r.returncode, 0, self.r.stderr)
        expected = sorted(["tpm-status.png", "tpm-table.md"] + EXP["PDR@2026-10-06_trend_files"])
        self.assertEqual(sorted(os.listdir(self.tmp.name)), expected)
        c = EXP["PDR@2026-10-06_counts"]
        self.assertIn(f"PDR: 7 TPMs; green {c['green']}, yellow {c['yellow']}, red {c['red']}, not due {c['not due']}", self.r.stdout)
        self.assertIn("TPM-003 review-trend: trend plotted by tools/review_trend.py", self.r.stderr)

    def test_pixel_sizes(self):
        from PIL import Image
        with Image.open(os.path.join(self.tmp.name, "tpm-status.png")) as im:
            self.assertEqual(list(im.size), EXP["table_px"])
        for f in EXP["PDR@2026-10-06_trend_files"]:
            with Image.open(os.path.join(self.tmp.name, f)) as im:
                self.assertEqual(list(im.size), EXP["trend_px"], f)

    def test_chip_colour_of_each_row(self):
        from PIL import Image
        rows = EXP["PDR@2026-10-06"]
        with Image.open(os.path.join(self.tmp.name, "tpm-status.png")) as im:
            rgb = im.convert("RGB")
            for i, row in enumerate(rows):
                # Sample inside the chip, left of its centred label: x 8 px from the chip's left edge.
                y = int(render_tpm.row_y(i, len(rows)) + render_tpm.row_h(len(rows)) / 2)
                x = render_tpm.CHIP_X + 8
                with self.subTest(tpm=row[0]):
                    got = rgb.getpixel((x, y))
                    want = EXP["chip_rgb"][row[1]]
                    self.assertTrue(all(abs(g - w) <= 3 for g, w in zip(got, want)), f"{got} vs {want} at {(x, y)}")

    def test_markdown_rows(self):
        with open(os.path.join(self.tmp.name, "tpm-table.md")) as fh:
            md = fh.read()
        self.assertIn("| TPM-004 | `carried-srr-reporting` | Only an SRR entry, PDR is a reporting review | 9.5 | hours | red | "
                      "no estimate at a reporting review | SRR 2026-09-25 | false | d.md |", md)
        self.assertIn("| TPM-005 | `no-history-reporting` | No history, PDR is a reporting review | none | ppm | red | "
                      "no estimate at a reporting review | none | n/a | none |", md)
        self.assertIn("Counts: green 2, yellow 1, red 3, not due 1; 7 TPMs.", md)

    def test_check_writes_nothing(self):
        with tempfile.TemporaryDirectory() as t:
            r = run("--review", "PDR", "--tpm", os.path.join(FIXTURE, "tpm.json"), "--out", t, "--date", "2026-10-06", "--check")
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertIn("| TPM-001 | `own-green` |", r.stdout)
            self.assertEqual(os.listdir(t), [])


class SeededFaultTests(unittest.TestCase):
    def test_each_seeded_fault(self):
        for case in EXP["seeded"]:
            with self.subTest(case=case["name"]), tempfile.TemporaryDirectory() as t:
                data = copy.deepcopy(DATA)
                target = data["tpms"][case["tpm"]]
                if "entry" in case:
                    target = target["history"][case["entry"]]
                target.update(case["set"])
                path = os.path.join(t, "tpm.json")
                with open(path, "w") as fh:
                    json.dump(data, fh)
                out = os.path.join(t, "out")
                os.makedirs(out)
                r = run("--review", "PDR", "--tpm", path, "--out", out, "--date", "2026-10-06")
                self.assertEqual(r.returncode, 1, r.stderr)
                self.assertIn(f"DATA ERROR {case['message']}; nothing written", r.stderr)
                self.assertEqual(os.listdir(out), [])

    def test_empty_tpms(self):
        with tempfile.TemporaryDirectory() as t:
            path = os.path.join(t, "tpm.json")
            with open(path, "w") as fh:
                json.dump({"tpms": []}, fh)
            r = run("--review", "PDR", "--tpm", path, "--out", t, "--check")
            self.assertEqual(r.returncode, 1)
            self.assertIn("tpms is missing or empty", r.stderr)


class UsageTests(unittest.TestCase):
    def test_usage_errors_exit_2(self):
        with tempfile.TemporaryDirectory() as t:
            fx = os.path.join(FIXTURE, "tpm.json")
            bad_json = os.path.join(t, "bad.json")
            with open(bad_json, "w") as fh:
                fh.write("{not json")
            cases = [
                (),                                                         # --review missing
                ("--review", "MCR", "--tpm", fx, "--out", t),               # not a review token
                ("--review", "TRR-Dn", "--tpm", fx, "--out", t),            # the placeholder, not a delta review
                ("--review", "PDR", "--tpm", fx, "--out", t, "--date", "6 Oct"),
                ("--review", "PDR", "--tpm", os.path.join(t, "absent.json"), "--out", t),
                ("--review", "PDR", "--tpm", bad_json, "--out", t),
                ("--review", "PDR", "--tpm", fx, "--out", os.path.join(t, "absent")),
                ("--review", "PDR", "--bogus"),
            ]
            for args in cases:
                with self.subTest(args=args):
                    self.assertEqual(run(*args).returncode, 2)


class RepositoryTests(unittest.TestCase):
    """Repository content, not the tool: the project tpm.json passes the data checks."""

    def test_project_tpm_json_checks(self):
        r = run("--review", "PDR", "--check")
        self.assertEqual(r.returncode, 0, r.stderr)


if __name__ == "__main__":
    unittest.main()
