"""Known-answer tests for kicad-cli 10.0.6 with tools/normalize_fab.py (TV-016; CM plan section 9.2
table row kicad-cli; tools/toolchain.lock.md section 1.1 kicad-cli and tools/normalize_fab.py rows).

Every expected value is read from tools/tests/fixtures/kicad/known-answers.json (derived by hand from
the fixture geometry before the first run, 2026-09-25) or from the stored files in
tools/tests/fixtures/kicad/expected/ (the CPL and BOM written by hand; clean-SHA256SUMS.normalized
written by make_expected_normalized.sh with grep and perl, independently of tools/normalize_fab.py).
Each class works on a temporary copy of the fixture directory, because kicad-cli writes .kicad_prl
files beside a project it opens.

  VersionTests            kicad-cli version is the locked 10.0.6
  ErcDrcTests             ERC and DRC: exactly the seeded violation and exit 5 on the seeded files,
                          none and exit 0 on the clean files
  ExportTests             drill hit counts and diameters (drill files and drill report), CPL and BOM
                          line for line, STEP bounding box within 0.01 mm, the Gerber set of the
                          CM plan section 8.2 step 2 layer list on the 2-layer fixture board
  NormalizedExportTests   two complete exports taken at least 1.1 s apart: 16 raw files differ,
                          the normalized lists are equal to each other and to the stored list;
                          a one-byte change in a copper layer makes normalize_fab --check exit 1

The classes are skipped when kicad-cli is not installed at the locked path; the TV-016 procedure
counts a skip as "not run", never as a pass.

Run from the repository root:
    .venv/bin/python -m unittest discover -s tools/tests -p test_kicad_cli.py -v
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FIXTURE = os.path.join(ROOT, "tools", "tests", "fixtures", "kicad")
NORMALIZE = os.path.join(ROOT, "tools", "normalize_fab.py")
KICAD = "/Applications/KiCad/KiCad.app/Contents/MacOS/kicad-cli"
with open(os.path.join(FIXTURE, "known-answers.json")) as _fh:
    KA = json.load(_fh)
HAVE_KICAD = os.path.exists(KICAD)
GERBER_LAYERS = "F.Cu,In1.Cu,In2.Cu,B.Cu,F.Mask,B.Mask,F.Silkscreen,B.Silkscreen,F.Paste,B.Paste,Edge.Cuts"


def kicad(*args, cwd):
    return subprocess.run([KICAD, *args], capture_output=True, text=True, cwd=cwd, timeout=300)


def export_all(work: str, out: str) -> None:
    """The CM plan section 8.2 step 2 exports (F3, F6, F7) plus the STEP and BOM exports, as in
    make_expected_normalized.sh."""
    os.makedirs(out)
    o = os.path.relpath(out, work)
    for args in (
        ["pcb", "export", "gerbers", "-o", o + "/", "-l", GERBER_LAYERS, "--no-x2", "--no-netlist", "--no-protel-ext",
         "--use-drill-file-origin", "--subtract-soldermask", "--check-zones", "--precision", "6", "clean.kicad_pcb"],
        ["pcb", "export", "drill", "-o", o + "/", "--format", "excellon", "--drill-origin", "plot", "--excellon-units", "mm",
         "--excellon-zeros-format", "decimal", "--excellon-oval-format", "route", "--excellon-separate-th",
         "--generate-map", "--map-format", "pdf", "--generate-report", "--report-path", o + "/clean-drill-report.rpt",
         "clean.kicad_pcb"],
        ["pcb", "export", "pos", "-o", o + "/clean-cpl.csv", "--format", "csv", "--units", "mm", "--use-drill-file-origin",
         "--side", "both", "--smd-only", "--exclude-dnp", "clean.kicad_pcb"],
        ["pcb", "export", "step", "--board-only", "--drill-origin", "-o", o + "/clean.step", "clean.kicad_pcb"],
        ["sch", "export", "bom", "-o", o + "/clean-bom.csv", "clean.kicad_sch"],
    ):
        r = kicad(*args, cwd=work)
        if r.returncode != 0:
            raise AssertionError(f"kicad-cli {' '.join(args[:3])} exit {r.returncode}: {r.stdout}{r.stderr}")


def file_sha(path: str) -> str:
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def fixture_copy(tmp: str) -> str:
    work = os.path.join(tmp, "work")
    shutil.copytree(FIXTURE, work)
    return work


def step_box(text: str) -> dict:
    cp = {m.group(1): tuple(float(x) for x in m.groups()[1:]) for m in re.finditer(
        r"#(\d+)\s*=\s*CARTESIAN_POINT\s*\(\s*'[^']*'\s*,\s*\(\s*([-0-9.Ee+]+)\s*,\s*([-0-9.Ee+]+)\s*,\s*([-0-9.Ee+]+)\s*\)", text)}
    pts = [cp[m.group(1)] for m in re.finditer(r"VERTEX_POINT\s*\(\s*'[^']*'\s*,\s*#(\d+)\s*\)", text)]
    return {a: [min(p[i] for p in pts), max(p[i] for p in pts)] for i, a in enumerate("xyz")}


@unittest.skipUnless(HAVE_KICAD, f"kicad-cli not installed at {KICAD}")
class VersionTests(unittest.TestCase):
    def test_locked_version(self):
        r = subprocess.run([KICAD, "version"], capture_output=True, text=True, timeout=60)
        self.assertEqual(r.stdout.strip(), KA["kicad_cli_version"])


@unittest.skipUnless(HAVE_KICAD, f"kicad-cli not installed at {KICAD}")
class ErcDrcTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.work = fixture_copy(cls.tmp.name)

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def erc(self, name):
        r = kicad("sch", "erc", "--format", "json", "--severity-all", "--exit-code-violations", "-o", f"{name}-erc.json",
                  f"{name}.kicad_sch", cwd=self.work)
        with open(os.path.join(self.work, f"{name}-erc.json")) as fh:
            d = json.load(fh)
        got = [[v["type"], v["severity"]] + [i["description"] for i in v["items"]] for s in d["sheets"] for v in s["violations"]]
        return r.returncode, got

    def drc(self, name):
        r = kicad("pcb", "drc", "--format", "json", "--severity-all", "--exit-code-violations", "-o", f"{name}-drc.json",
                  f"{name}.kicad_pcb", cwd=self.work)
        with open(os.path.join(self.work, f"{name}-drc.json")) as fh:
            d = json.load(fh)
        got = [[v["type"], v["severity"], v["description"]] + [i["description"] for i in v["items"] if i["description"].startswith("Pad")]
               for v in d["violations"]]
        return r.returncode, got, len(d["unconnected_items"])

    def test_erc_clean_none(self):
        rc, got = self.erc("clean")
        self.assertEqual((rc, got), (KA["erc"]["clean"]["exit"], KA["erc"]["clean"]["violations"]))

    def test_erc_seeded_exactly_one_unconnected_pin(self):
        rc, got = self.erc("seeded")
        self.assertEqual((rc, got), (KA["erc"]["seeded"]["exit"], KA["erc"]["seeded"]["violations"]))

    def test_drc_clean_none(self):
        rc, got, unconnected = self.drc("clean")
        exp = KA["drc"]["clean"]
        self.assertEqual((rc, got, unconnected), (exp["exit"], exp["violations"], exp["unconnected_items"]))

    def test_drc_seeded_exactly_one_clearance(self):
        rc, got, unconnected = self.drc("seeded")
        exp = KA["drc"]["seeded"]
        self.assertEqual((rc, got, unconnected), (exp["exit"], exp["violations"], exp["unconnected_items"]))


@unittest.skipUnless(HAVE_KICAD, f"kicad-cli not installed at {KICAD}")
class ExportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.work = fixture_copy(cls.tmp.name)
        cls.out = os.path.join(cls.work, "out")
        export_all(cls.work, cls.out)

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def read(self, name):
        with open(os.path.join(self.out, name)) as fh:
            return fh.read()

    def test_gerber_set_of_the_layer_list(self):
        gerbers = sorted(f for f in os.listdir(self.out) if f.endswith(".gbr"))
        self.assertEqual(gerbers, sorted(KA["normalized_exports"]["gerber_files"]))
        self.assertIn("clean-job.gbrjob", os.listdir(self.out))

    def test_drill_files_hits_and_diameters(self):
        hits = lambda t: len(re.findall(r"^X-?[0-9.]+Y-?[0-9.]+$", t, re.M))
        tools_ = lambda t: [float(x) for x in re.findall(r"^T\d+C([0-9.]+)", t, re.M)]
        pth, npth = self.read("clean-PTH.drl"), self.read("clean-NPTH.drl")
        d = KA["drill"]
        self.assertEqual((hits(pth), tools_(pth)), (d["plated_holes"], [d["plated_diameter_mm"]]))
        self.assertEqual((hits(npth), tools_(npth)), (d["non_plated_holes"], [d["non_plated_diameter_mm"]]))

    def test_drill_report_counts(self):
        rpt = self.read("clean-drill-report.rpt")
        d = KA["drill"]
        self.assertEqual(int(re.search(r"Total plated holes count (\d+)", rpt).group(1)), d["plated_holes"])
        self.assertEqual(int(re.search(r"Total unplated holes count (\d+)", rpt).group(1)), d["non_plated_holes"])

    def test_cpl_and_bom_line_for_line(self):
        for key in ("cpl", "bom"):
            with self.subTest(key=key):
                with open(os.path.join(FIXTURE, KA[key]["expected_file"])) as fh:
                    self.assertEqual(self.read(f"clean-{key}.csv").splitlines(), fh.read().splitlines())

    def test_step_bounding_box(self):
        box = step_box(self.read("clean.step"))
        exp, tol = KA["step"]["bounding_box_mm"], KA["step"]["tolerance_mm"]
        for a in "xyz":
            for j in (0, 1):
                self.assertLessEqual(abs(box[a][j] - exp[a][j]), tol, f"{a}[{j}] {box[a][j]} vs {exp[a][j]}")


@unittest.skipUnless(HAVE_KICAD, f"kicad-cli not installed at {KICAD}")
class NormalizedExportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.work = fixture_copy(cls.tmp.name)
        cls.a, cls.b = os.path.join(cls.work, "a"), os.path.join(cls.work, "b")
        export_all(cls.work, cls.a)
        time.sleep(1.1)  # the Gerber, drill and STEP time stamps have one-second resolution
        export_all(cls.work, cls.b)
        cls.stored = os.path.join(FIXTURE, KA["normalized_exports"]["expected_file"])

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def normalize(self, *args):
        return subprocess.run([sys.executable, NORMALIZE, "--quiet", *args], capture_output=True, text=True)

    def test_raw_exports_differ(self):
        differ = []
        for f in sorted(os.listdir(self.a)):
            if file_sha(os.path.join(self.a, f)) != file_sha(os.path.join(self.b, f)):
                differ.append(f)
        self.assertEqual(sorted(os.listdir(self.a)), sorted(os.listdir(self.b)))
        self.assertEqual(len(differ), KA["normalized_exports"]["raw_files_differing"], differ)

    def test_two_exports_normalize_equal(self):
        ra, rb = self.normalize(self.a), self.normalize(self.b)
        self.assertEqual((ra.returncode, rb.returncode), (0, 0))
        self.assertEqual(ra.stdout, rb.stdout)
        self.assertEqual(len(ra.stdout.splitlines()), KA["normalized_exports"]["files"])

    def test_exports_match_stored_list(self):
        for d in (self.a, self.b):
            with self.subTest(export=os.path.basename(d)):
                r = self.normalize("--check", self.stored, d)
                self.assertEqual(r.returncode, 0, r.stderr)

    def test_one_byte_change_in_copper_fails_check(self):
        seeded = os.path.join(self.work, "seeded")
        shutil.copytree(self.b, seeded)
        path = os.path.join(seeded, "clean-F_Cu.gbr")
        with open(path, "rb") as fh:
            data = fh.read()
        m = re.search(rb"^X(\d)", data, re.M)
        self.assertIsNotNone(m, "no coordinate line in clean-F_Cu.gbr")
        i = m.start(1)
        data = data[:i] + (b"8" if data[i:i + 1] != b"8" else b"7") + data[i + 1:]
        with open(path, "wb") as fh:
            fh.write(data)
        r = subprocess.run([sys.executable, NORMALIZE, "--check", self.stored, seeded], capture_output=True, text=True)
        self.assertEqual(r.returncode, 1)
        self.assertIn("CHANGED clean-F_Cu.gbr", r.stderr)
        self.assertEqual(r.stderr.count("CHANGED"), 1)


if __name__ == "__main__":
    unittest.main()
