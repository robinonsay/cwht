"""Known-answer tests for tools/normalize_fab.py (TV-016; CM plan section 8.2 normalization table and
section 9.2 table rows kicad-cli and tools/normalize_fab.py).

Fixture-only classes (the validation of the tool; no kicad-cli needed):
  RuleTests          each row of the CM plan section 8.2 table on a hand-written input whose
                     normalized form is written out by hand in the test (independent of the tool)
  SeededFaultTests   a one-byte change outside the date lines changes the normalized hash; a
                     change inside a date line does not; a date line not of the table survives
  CliTests           listing, --sums, --check pass and fail, zip members, excluded names,
                     --write, and every exit status of the docstring (0, 1, 2)

The end-to-end known answer on real kicad-cli exports is tools/tests/test_kicad_cli.py
(NormalizedExportTests).

Run from the repository root:
    .venv/bin/python -m unittest discover -s tools/tests -p test_normalize_fab.py -v
"""
from __future__ import annotations

import hashlib
import io
import os
import subprocess
import sys
import tempfile
import unittest
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TOOL = os.path.join(ROOT, "tools", "normalize_fab.py")
sys.path.insert(0, os.path.join(ROOT, "tools"))
import normalize_fab  # noqa: E402

GERBER = (b"G04 #@! TF.GenerationSoftware,KiCad,Pcbnew,10.0.6*\n"
          b"G04 #@! TF.CreationDate,2026-09-27T12:18:03-05:00*\n"
          b"%TF.CreationDate,2026-09-27T12:18:03-05:00*%\n"
          b"%FSLAX46Y46*%\n"
          b"G04 Created by KiCad (PCBNEW 10.0.6) date 2026-09-27 12:18:03*\n"
          b"%MOMM*%\n"
          b"X110000000Y-110000000D03*\n"
          b"M02*\n")
GERBER_NORM = (b"G04 #@! TF.GenerationSoftware,KiCad,Pcbnew,10.0.6*\n"
               b"%FSLAX46Y46*%\n"
               b"%MOMM*%\n"
               b"X110000000Y-110000000D03*\n"
               b"M02*\n")
DRILL = (b"M48\n; DRILL file KiCad 10.0.6 date 2026-09-27T12:18:15\n; FORMAT={-:-/ absolute / metric / decimal}\n"
         b"; #@! TF.CreationDate,2026-09-27T12:18:15-05:00\n; #@! TF.GenerationSoftware,Kicad,Pcbnew,10.0.6\n"
         b"T1C0.700\n%\nX20.0Y10.0\nM30\n")
DRILL_NORM = (b"M48\n; FORMAT={-:-/ absolute / metric / decimal}\n; #@! TF.GenerationSoftware,Kicad,Pcbnew,10.0.6\n"
              b"T1C0.700\n%\nX20.0Y10.0\nM30\n")
JOB = b'{\n  "Header": {\n    "Version": "10.0.6"\n  },\n    "CreationDate": "2026-09-27T12:18:03-05:00"\n}\n'
JOB_NORM = b'{\n  "Header": {\n    "Version": "10.0.6"\n  },\n    "CreationDate": "normalized"\n}\n'
REPORT = b"Drill report for clean.kicad_pcb\nCreated on 2026-09-27T12:18:15\n\n    Total plated holes count 1\n"
REPORT_NORM = b"Drill report for clean.kicad_pcb\n\n    Total plated holes count 1\n"
STEP = (b"ISO-10303-21;\nHEADER;\nFILE_DESCRIPTION(('Open CASCADE Model'),'2;1');\n"
        b"FILE_NAME('clean.step','2026-09-27T12:18:16',('Pcbnew'),('Kicad'),\n"
        b"  'Open CASCADE STEP processor 7.9','KiCad to STEP converter','Unknown'\n  );\n"
        b"ENDSEC;\nDATA;\n#1 = CARTESIAN_POINT('',(0.,0.,0.));\nENDSEC;\nEND-ISO-10303-21;\n")
STEP_NORM = (b"ISO-10303-21;\nHEADER;\nFILE_DESCRIPTION(('Open CASCADE Model'),'2;1');\n"
             b"FILE_NAME('clean.step','normalized',('Pcbnew'),('Kicad'),\n"
             b"  'Open CASCADE STEP processor 7.9','KiCad to STEP converter','Unknown'\n  );\n"
             b"ENDSEC;\nDATA;\n#1 = CARTESIAN_POINT('',(0.,0.,0.));\nENDSEC;\nEND-ISO-10303-21;\n")
# A STEP header split over lines, with a doubled quote inside the name (STEP string escape).
STEP_SPLIT = b"FILE_NAME(\n  'it''s.step',\n  '2026-01-02T03:04:05',('a'),('b'),'p','o','u');\n"
STEP_SPLIT_NORM = b"FILE_NAME(\n  'it''s.step',\n  'normalized',('a'),('b'),'p','o','u');\n"
PDF = (b"%PDF-1.5\n<< /Producer (KiCad PDF) /CreationDate (D:2026:09:27:12:18:15) "
       b"/ModDate (D:20260927121815-05'00') /Title (x) >>\n%%EOF\n")
PDF_NORM = (b"%PDF-1.5\n<< /Producer (KiCad PDF) /CreationDate (D:0000:00:00:00:00:00) "
            b"/ModDate (D:00000000000000-00'00') /Title (x) >>\n%%EOF\n")
CSV = b'Ref,Val,Package,PosX,PosY,Rot,Side\n"R1","10k","R_0603_1608Metric",10.000000,10.000000,0.000000,top\n'


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def run(*args, cwd=None):
    return subprocess.run([sys.executable, TOOL, *args], capture_output=True, text=True, cwd=cwd)


class RuleTests(unittest.TestCase):
    """One known answer per row of the CM plan section 8.2 table."""

    def check(self, name, data, expected, rule, count):
        out, got_rule, n = normalize_fab.normalize(name, data)
        self.assertEqual(out, expected)
        self.assertEqual(got_rule, rule)
        self.assertEqual(n, count)

    def test_gerber_three_date_lines_deleted(self):
        self.check("clean-F_Cu.gbr", GERBER, GERBER_NORM, "gerber", 3)

    def test_gerber_crlf_lines(self):
        self.check("x.GBR", GERBER.replace(b"\n", b"\r\n"), GERBER_NORM.replace(b"\n", b"\r\n"), "gerber", 3)

    def test_excellon_two_date_lines_deleted(self):
        self.check("clean-PTH.drl", DRILL, DRILL_NORM, "excellon", 2)

    def test_gerber_job_creation_date_member(self):
        self.check("clean-job.gbrjob", JOB, JOB_NORM, "gerber-job", 1)

    def test_drill_report_created_on_deleted(self):
        self.check("clean-drill-report.rpt", REPORT, REPORT_NORM, "drill-report", 1)

    def test_step_file_name_time_stamp(self):
        self.check("clean.step", STEP, STEP_NORM, "step", 1)

    def test_stp_split_header_with_escaped_quote(self):
        self.check("part.stp", STEP_SPLIT, STEP_SPLIT_NORM, "step", 1)

    def test_pdf_dates_zeroed_same_length(self):
        self.check("map.pdf", PDF, PDF_NORM, "pdf", 2)
        self.assertEqual(len(PDF), len(PDF_NORM))

    def test_csv_unchanged(self):
        self.check("clean-cpl.csv", CSV, CSV, "csv-none", 0)

    def test_other_type_is_raw(self):
        self.check("manifest.md", b"date 2026-09-27\n", b"date 2026-09-27\n", "raw", 0)


class SeededFaultTests(unittest.TestCase):
    """CM plan section 9.2 table: a one-byte change outside the date lines changes the normalized hash."""

    def test_one_byte_change_in_copper_changes_hash(self):
        seeded = GERBER.replace(b"X110000000", b"X110000001")
        self.assertNotEqual(sha(normalize_fab.normalize("F_Cu.gbr", seeded)[0]), sha(GERBER_NORM))

    def test_time_stamp_change_keeps_hash(self):
        later = GERBER.replace(b"12:18:03", b"12:19:44")
        self.assertNotEqual(sha(later), sha(GERBER))
        self.assertEqual(sha(normalize_fab.normalize("F_Cu.gbr", later)[0]), sha(GERBER_NORM))

    def test_date_like_line_outside_table_survives(self):
        # A comment carrying a date but matching no table pattern is not removed ("nothing else").
        data = b"G04 Plotted on 2026-09-27*\nM02*\n"
        self.assertEqual(normalize_fab.normalize("x.gbr", data)[0], data)

    def test_one_byte_change_in_step_body_changes_hash(self):
        seeded = STEP.replace(b"(0.,0.,0.)", b"(0.,0.,1.)")
        self.assertNotEqual(normalize_fab.normalize("a.step", seeded)[0], STEP_NORM)


class CliTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.d = os.path.join(self.tmp.name, "pkg")
        os.makedirs(os.path.join(self.d, "gerbers"))
        files = {"gerbers/F_Cu.gbr": GERBER, "PTH.drl": DRILL, "job.gbrjob": JOB, "a.step": STEP,
                 "map.pdf": PDF, "cpl.csv": CSV, "SHA256SUMS": b"raw list\n", ".hidden": b"x"}
        for name, data in files.items():
            with open(os.path.join(self.d, name), "wb") as fh:
                fh.write(data)
        self.expected = {"gerbers/F_Cu.gbr": sha(GERBER_NORM), "PTH.drl": sha(DRILL_NORM), "job.gbrjob": sha(JOB_NORM),
                         "a.step": sha(STEP_NORM), "map.pdf": sha(PDF_NORM), "cpl.csv": sha(CSV)}

    def tearDown(self):
        self.tmp.cleanup()

    def listing(self, stdout):
        return {line.split("  ", 1)[1]: line.split("  ", 1)[0] for line in stdout.splitlines()}

    def test_listing_is_sorted_shasum_format_and_excludes_sums_and_hidden(self):
        r = run(self.d)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(self.listing(r.stdout), self.expected)
        names = [line.split("  ", 1)[1] for line in r.stdout.splitlines()]
        self.assertEqual(names, sorted(names))

    def test_sums_then_check_pass(self):
        sums = os.path.join(self.tmp.name, "SUMS.txt")
        self.assertEqual(run("--sums", sums, self.d).returncode, 0)
        with open(sums) as fh:
            self.assertEqual(self.listing(fh.read()), self.expected)
        r = run("--check", sums, self.d)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("check PASS: 6 listed, 0 difference(s)", r.stderr)

    def test_check_fails_on_changed_added_and_missing(self):
        sums = os.path.join(self.tmp.name, "SUMS.txt")
        run("--sums", sums, self.d)
        with open(os.path.join(self.d, "gerbers", "F_Cu.gbr"), "wb") as fh:
            fh.write(GERBER.replace(b"X110000000", b"X110000001"))
        with open(os.path.join(self.d, "extra.csv"), "wb") as fh:
            fh.write(CSV)
        os.remove(os.path.join(self.d, "map.pdf"))
        r = run("--check", sums, self.d)
        self.assertEqual(r.returncode, 1)
        for line in ("CHANGED gerbers/F_Cu.gbr", "ADDED extra.csv", "MISSING map.pdf"):
            self.assertIn(line, r.stderr)
        self.assertIn("check FAIL", r.stderr)

    def test_check_passes_after_time_stamp_only_change(self):
        sums = os.path.join(self.tmp.name, "SUMS.txt")
        run("--sums", sums, self.d)
        with open(os.path.join(self.d, "gerbers", "F_Cu.gbr"), "wb") as fh:
            fh.write(GERBER.replace(b"12:18:03", b"23:59:59"))
        self.assertEqual(run("--check", sums, self.d).returncode, 0)

    def test_zip_members_listed_zip_itself_not(self):
        buf = io.BytesIO()
        with zipfile.ZipFile(buf, "w") as zf:
            zf.writestr("gerbers/F_Cu.gbr", GERBER)
            zf.writestr("gerbers/", b"")
            zf.writestr("cpl.csv", CSV)
        zpath = os.path.join(self.tmp.name, "upload.zip")
        with open(zpath, "wb") as fh:
            fh.write(buf.getvalue())
        r = run(zpath)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(self.listing(r.stdout), {"upload.zip!gerbers/F_Cu.gbr": sha(GERBER_NORM), "upload.zip!cpl.csv": sha(CSV)})

    def test_write_dir_holds_normalized_files(self):
        out = os.path.join(self.tmp.name, "norm")
        self.assertEqual(run("--write", out, self.d).returncode, 0)
        with open(os.path.join(out, "gerbers", "F_Cu.gbr"), "rb") as fh:
            self.assertEqual(fh.read(), GERBER_NORM)

    def test_root_names_relative_to_root(self):
        r = run("--root", self.tmp.name, os.path.join(self.d, "PTH.drl"))
        self.assertEqual(self.listing(r.stdout), {"pkg/PTH.drl": sha(DRILL_NORM)})

    def test_usage_errors_exit_2(self):
        cases = [
            (),                                              # no path
            ("--bogus", self.d),                             # unknown option
            (os.path.join(self.tmp.name, "absent"),),        # missing input
            ("--sums", "a", "--check", "b", self.d),         # exclusive options
            ("--check", os.path.join(self.tmp.name, "absent.txt"), self.d),  # unreadable stored list
        ]
        for args in cases:
            with self.subTest(args=args):
                self.assertEqual(run(*args).returncode, 2)

    def test_bad_stored_line_and_bad_zip_exit_2(self):
        bad = os.path.join(self.tmp.name, "bad.txt")
        with open(bad, "w") as fh:
            fh.write("not a hash line\n")
        self.assertEqual(run("--check", bad, self.d).returncode, 2)
        z = os.path.join(self.tmp.name, "broken.zip")
        with open(z, "wb") as fh:
            fh.write(b"PK not a zip")
        r = run(z)
        self.assertEqual(r.returncode, 2)
        self.assertIn("not a readable zip", r.stderr)

    def test_empty_directory_exit_2(self):
        empty = os.path.join(self.tmp.name, "empty")
        os.makedirs(empty)
        r = run(empty)
        self.assertEqual(r.returncode, 2)
        self.assertIn("no file to list", r.stderr)


if __name__ == "__main__":
    unittest.main()
