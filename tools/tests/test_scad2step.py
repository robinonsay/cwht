"""Known-answer tests for tools/scad2step.py with OpenSCAD 2021.01 and FreeCAD 1.1.3 (TV-015; CM plan
section 8.2 step 3 and section 9.2 table row "OpenSCAD + FreeCAD with tools/scad2step.py"; ADR-008).

Expected values are read from tools/tests/fixtures/openscad/known-answers.json (block "scad2step",
hand-derived from the fixture geometry; block "step_export" of 2026-09-25 for the cube).

Classes that need neither OpenSCAD nor FreeCAD:
  MeshVolumeTests      the STL volume reader on hand-written binary and ASCII meshes
  UsageTests           every usage error exits 2
  DoubleTests          not installed (3), other OpenSCAD version (4), no marker from a freecadcmd
                       test double (1), time-out of a hanging double (124, its process group killed)
Classes that run the locked OpenSCAD and FreeCAD (skipped, with the reason, when either is absent;
the TV-015 procedure counts a skip as "not run"):
  ConversionTests      the cube known answer through the driver and through the CM plan form
                       (freecadcmd tools/scad2step.py with the environment); the FreeCAD version
                       checks of the driver (bundle) and of FreeCAD mode (C1)
  SeededCsgTests       C2, C3, C5 and C7 faults each fail with their marker and leave no STEP
  ReproducibilityTests two conversions differ only in the FILE_NAME time stamp (class A)

Run from the repository root:
    .venv/bin/python -m unittest discover -s tools/tests -p test_scad2step.py -v
"""
from __future__ import annotations

import json
import os
import re
import struct
import subprocess
import sys
import tempfile
import time
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TOOL = os.path.join(ROOT, "tools", "scad2step.py")
FIXTURE = os.path.join(ROOT, "tools", "tests", "fixtures", "openscad")
FAKE = os.path.join(FIXTURE, "fake")
with open(os.path.join(FIXTURE, "known-answers.json")) as _fh:
    KA_ALL = json.load(_fh)
KA = KA_ALL["scad2step"]
EXIT = KA["exit_codes"]
sys.path.insert(0, os.path.join(ROOT, "tools"))
import scad2step  # noqa: E402

HAVE_TOOLS = os.access(scad2step.LOCK_OPENSCAD, os.X_OK) and os.access(scad2step.LOCK_FREECADCMD, os.X_OK)
HOOKS = ("CWHT_OPENSCAD", "CWHT_FREECADCMD", "CWHT_SCAD2STEP_EXPECT_OPENSCAD", "CWHT_SCAD2STEP_EXPECT_FREECAD",
         "CWHT_CSG", "CWHT_STL", "CWHT_STEP")


def clean_env(**extra):
    env = {k: v for k, v in os.environ.items() if k not in HOOKS}
    env.update(extra)
    return env


def run(*args, env=None, timeout=600):
    return subprocess.run([sys.executable, TOOL, *args], capture_output=True, text=True, env=env or clean_env(), timeout=timeout)


def box_stl_binary(lx, ly, lz) -> bytes:
    """12 outward triangles of an axis-aligned box from the origin (hand-written mesh)."""
    v = [(0, 0, 0), (lx, 0, 0), (lx, ly, 0), (0, ly, 0), (0, 0, lz), (lx, 0, lz), (lx, ly, lz), (0, ly, lz)]
    faces = [(0, 2, 1), (0, 3, 2), (4, 5, 6), (4, 6, 7), (0, 1, 5), (0, 5, 4),
             (1, 2, 6), (1, 6, 5), (2, 3, 7), (2, 7, 6), (3, 0, 4), (3, 4, 7)]
    body = b"".join(struct.pack("<12fH", 0, 0, 0, *v[a], *v[b], *v[c], 0) for a, b, c in faces)
    return b"\0" * 80 + struct.pack("<I", len(faces)) + body


def step_box(text: str) -> dict:
    cp = {m.group(1): tuple(float(x) for x in m.groups()[1:]) for m in re.finditer(
        r"#(\d+)\s*=\s*CARTESIAN_POINT\s*\(\s*'[^']*'\s*,\s*\(\s*([-0-9.Ee+]+)\s*,\s*([-0-9.Ee+]+)\s*,\s*([-0-9.Ee+]+)\s*\)", text)}
    pts = [cp[m.group(1)] for m in re.finditer(r"VERTEX_POINT\s*\(\s*'[^']*'\s*,\s*#(\d+)\s*\)", text)]
    return {a: [min(p[i] for p in pts), max(p[i] for p in pts)] for i, a in enumerate("xyz")}


def kat(stdout: str) -> dict:
    m = re.search(r"^SCAD2STEP KAT (.*)$", stdout, re.M)
    if not m:
        return {}
    line = re.sub(r"surfaces=\{[^}]*\} ", "", m.group(1))
    return dict(item.split("=", 1) for item in line.split())


class MeshVolumeTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()

    def tearDown(self):
        self.tmp.cleanup()

    def write(self, name, data):
        p = os.path.join(self.tmp.name, name)
        with open(p, "wb") as fh:
            fh.write(data)
        return p

    def test_binary_box(self):
        vol, n = scad2step.stl_volume(self.write("b.stl", box_stl_binary(30, 20, 10)))
        self.assertAlmostEqual(vol, 6000.0, places=3)
        self.assertEqual(n, 12)

    def test_ascii_unit_tetrahedron(self):
        # Tetrahedron (0,0,0) (1,0,0) (0,1,0) (0,0,1): volume 1/6, faces wound outward.
        tris = [((0, 0, 0), (0, 1, 0), (1, 0, 0)), ((0, 0, 0), (1, 0, 0), (0, 0, 1)),
                ((0, 0, 0), (0, 0, 1), (0, 1, 0)), ((1, 0, 0), (0, 1, 0), (0, 0, 1))]
        text = "solid t\n" + "".join("facet normal 0 0 0\nouter loop\n" + "".join(f"vertex {x} {y} {z}\n" for x, y, z in t)
                                     + "endloop\nendfacet\n" for t in tris) + "endsolid t\n"
        vol, n = scad2step.stl_volume(self.write("t.stl", text.encode()))
        self.assertAlmostEqual(vol, 1 / 6, places=9)
        self.assertEqual(n, 4)

    def test_truncated_binary_rejected(self):
        with self.assertRaises(ValueError):
            scad2step.stl_volume(self.write("x.stl", box_stl_binary(1, 1, 1)[:-10]))


class UsageTests(unittest.TestCase):
    def test_usage_errors_exit_2(self):
        with tempfile.TemporaryDirectory() as t:
            cube = os.path.join(FIXTURE, "cube.scad")
            cases = [
                (),                                                       # --step missing
                ("--step", os.path.join(t, "a.step")),                    # no input
                ("--scad", cube, "--stl", cube, "--step", os.path.join(t, "a.step")),  # --scad with --stl
                ("--csg", cube, "--step", os.path.join(t, "a.step")),     # --csg without --stl
                ("--scad", os.path.join(t, "absent.scad"), "--step", os.path.join(t, "a.step")),
                ("--scad", cube, "--step", os.path.join(t, "no", "dir", "a.step")),
                ("--scad", cube, "--step", os.path.join(t, "a.step"), "--timeout", "0"),
                ("--bogus",),
            ]
            for args in cases:
                with self.subTest(args=args):
                    self.assertEqual(run(*args).returncode, EXIT["usage"])


class DoubleTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.step = os.path.join(self.tmp.name, "out.step")
        self.csg = os.path.join(self.tmp.name, "in.csg")
        self.stl = os.path.join(self.tmp.name, "in.stl")
        for p, data in ((self.csg, b"cube(size = [1, 1, 1], center = false);\n"), (self.stl, box_stl_binary(1, 1, 1))):
            with open(p, "wb") as fh:
                fh.write(data)

    def tearDown(self):
        self.tmp.cleanup()

    def test_openscad_not_installed(self):
        r = run("--scad", os.path.join(FIXTURE, "cube.scad"), "--step", self.step, env=clean_env(CWHT_OPENSCAD="/nonexistent/OpenSCAD"))
        self.assertEqual(r.returncode, EXIT["missing"])
        self.assertIn("TEST HOOK CWHT_OPENSCAD", r.stderr)

    def test_freecadcmd_not_installed(self):
        r = run("--csg", self.csg, "--stl", self.stl, "--step", self.step, env=clean_env(CWHT_FREECADCMD="/nonexistent/freecadcmd"))
        self.assertEqual(r.returncode, EXIT["missing"])

    def test_openscad_other_version(self):
        r = run("--scad", os.path.join(FIXTURE, "cube.scad"), "--step", self.step,
                env=clean_env(CWHT_OPENSCAD=os.path.join(FAKE, "openscad-other-version")))
        self.assertEqual(r.returncode, EXIT["version"])
        self.assertIn("'OpenSCAD version 2019.05', expected 'OpenSCAD version 2021.01'", r.stderr)

    def test_no_marker_is_a_failure(self):
        r = run("--csg", self.csg, "--stl", self.stl, "--step", self.step, env=clean_env(CWHT_FREECADCMD=os.path.join(FAKE, "freecadcmd-silent")))
        self.assertEqual(r.returncode, EXIT["check"])
        self.assertIn("no SCAD2STEP marker", r.stderr)
        self.assertFalse(os.path.exists(self.step))

    def test_timeout_kills_own_process_group(self):
        t0 = time.monotonic()
        r = run("--csg", self.csg, "--stl", self.stl, "--step", self.step, "--timeout", "3",
                env=clean_env(CWHT_FREECADCMD=os.path.join(FAKE, "freecadcmd-hang")))
        elapsed = time.monotonic() - t0
        self.assertEqual(r.returncode, EXIT["timeout"])
        self.assertLess(elapsed, 20)
        self.assertGreaterEqual(elapsed, 3)
        left = subprocess.run(["pgrep", "-f", os.path.join(FAKE, "freecadcmd-hang")], capture_output=True, text=True)
        self.assertEqual(left.stdout.strip(), "", "the hanging double survived")


@unittest.skipUnless(HAVE_TOOLS, "OpenSCAD 2021.01 or FreeCAD 1.1.3 not installed at the locked path")
class ConversionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.csg = os.path.join(cls.tmp.name, "cube.csg")
        cls.step = os.path.join(cls.tmp.name, "cube.step")
        cls.r = run("--scad", os.path.join(FIXTURE, "cube.scad"), "--csg", cls.csg, "--step", cls.step)

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_exit_and_marker(self):
        self.assertEqual(self.r.returncode, KA["cube"]["exit"], self.r.stderr + self.r.stdout)
        self.assertIn(f"SCAD2STEP PASS wrote {self.step}", self.r.stdout)
        self.assertTrue(os.path.isfile(self.step))

    def test_kat_values(self):
        k, e = kat(self.r.stdout), KA["cube"]
        for key in ("root", "solids", "valid", "faces", "cylinders", "bspline"):
            with self.subTest(key=key):
                self.assertEqual(k[key], str(e[key]))
        self.assertLessEqual(abs(float(k["volume"]) - e["volume_mm3"]) / e["volume_mm3"], KA_ALL["step_export"]["volume_tolerance_fraction"])
        self.assertAlmostEqual(float(k["step_volume"]), float(k["volume"]), places=3)
        self.assertLessEqual(abs(float(k["stl_volume"]) - e["stl_volume_mm3"]), e["stl_volume_tolerance_mm3"])
        self.assertEqual(k["freecad"], scad2step.LOCK_FREECAD_VERSION)

    def test_csg_content(self):
        with open(self.csg) as fh:
            csg = fh.read()
        for line in KA_ALL["csg_export"]["must_contain"]:
            self.assertIn(line, csg)

    def test_step_bounding_box(self):
        with open(self.step) as fh:
            box = step_box(fh.read())
        exp, tol = KA["cube"]["bounding_box_mm"], KA["cube"]["bounding_box_tolerance_mm"]
        for a in "xyz":
            for j in (0, 1):
                self.assertLessEqual(abs(box[a][j] - exp[a][j]), tol)

    def test_cm_plan_form_freecad_mode(self):
        """freecadcmd tools/scad2step.py with the environment (CM plan section 8.2 step 3)."""
        stl = os.path.join(self.tmp.name, "cube.stl")
        subprocess.run([scad2step.LOCK_OPENSCAD, "--export-format", "binstl", "-o", stl, os.path.join(FIXTURE, "cube.scad")],
                       capture_output=True, check=True, timeout=300)
        out = os.path.join(self.tmp.name, "direct.step")
        r = subprocess.run([scad2step.LOCK_FREECADCMD, TOOL], capture_output=True, text=True, timeout=600,
                           env=clean_env(CWHT_CSG=self.csg, CWHT_STL=stl, CWHT_STEP=out))
        self.assertIn(f"SCAD2STEP PASS wrote {out}", r.stdout)
        self.assertTrue(os.path.isfile(out))

    def test_freecad_mode_missing_environment(self):
        r = subprocess.run([scad2step.LOCK_FREECADCMD, TOOL], capture_output=True, text=True, timeout=600, env=clean_env())
        self.assertIn("SCAD2STEP FAIL usage: environment variable(s) not set: CWHT_CSG, CWHT_STL, CWHT_STEP", r.stdout)
        self.assertEqual(r.returncode, 0, "freecadcmd exits 0 on a failed script (lock section 1.4 finding 4)")

    def test_freecad_bundle_version_other_than_expected(self):
        out = os.path.join(self.tmp.name, "v.step")
        r = run("--scad", os.path.join(FIXTURE, "cube.scad"), "--step", out, env=clean_env(CWHT_SCAD2STEP_EXPECT_FREECAD="1.1.4"))
        self.assertEqual(r.returncode, EXIT["version"])
        self.assertIn("FreeCAD bundle version is '1.1.3', expected '1.1.4'", r.stderr)

    def test_freecad_mode_version_check_c1(self):
        out = os.path.join(self.tmp.name, "c1.step")
        r = run("--scad", os.path.join(FIXTURE, "cube.scad"), "--step", out,
                env=clean_env(CWHT_FREECADCMD=scad2step.LOCK_FREECADCMD, CWHT_SCAD2STEP_EXPECT_FREECAD="1.1.4"))
        self.assertEqual(r.returncode, EXIT["version"])
        self.assertIn("SCAD2STEP FAIL C1: FreeCAD is 1.1.3, expected 1.1.4", r.stdout)
        self.assertFalse(os.path.exists(out))

    def test_openscad_expected_version_hook(self):
        r = run("--scad", os.path.join(FIXTURE, "cube.scad"), "--step", os.path.join(self.tmp.name, "o.step"),
                env=clean_env(CWHT_SCAD2STEP_EXPECT_OPENSCAD="OpenSCAD version 2021.02"))
        self.assertEqual(r.returncode, EXIT["version"])


@unittest.skipUnless(HAVE_TOOLS, "OpenSCAD 2021.01 or FreeCAD 1.1.3 not installed at the locked path")
class SeededCsgTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()

    def tearDown(self):
        self.tmp.cleanup()

    def check(self, r, exp, step):
        self.assertEqual(r.returncode, exp["exit"], r.stdout + r.stderr)
        last = [ln for ln in r.stdout.splitlines() if ln.startswith("SCAD2STEP ")][-1]
        if "marker" in exp:
            self.assertEqual(last, exp["marker"])
        else:
            self.assertTrue(last.startswith(exp["marker_prefix"]), last)
        self.assertFalse(os.path.exists(step), "a failed conversion left a STEP file")

    def test_seeded_scad_files(self):
        for name in ("two-roots.scad", "two-solids.scad", "nonuniform-scale.scad", "twist.scad"):
            with self.subTest(name=name):
                step = os.path.join(self.tmp.name, name + ".step")
                self.check(run("--scad", os.path.join(FIXTURE, name), "--step", step), KA["seeded"][name], step)

    def test_mesh_volume_mismatch_c7(self):
        csg = os.path.join(self.tmp.name, "cube.csg")
        stl = os.path.join(self.tmp.name, "taller.stl")
        subprocess.run([scad2step.LOCK_OPENSCAD, "-o", csg, os.path.join(FIXTURE, "cube.scad")], capture_output=True, check=True, timeout=300)
        subprocess.run([scad2step.LOCK_OPENSCAD, "--export-format", "binstl", "-o", stl, os.path.join(FIXTURE, "taller.scad")],
                       capture_output=True, check=True, timeout=300)
        step = os.path.join(self.tmp.name, "v.step")
        exp = KA["seeded"]["cube.csg with the taller.scad mesh"]
        r = run("--csg", csg, "--stl", stl, "--step", step)
        self.check(r, exp, step)
        self.assertAlmostEqual(float(kat(r.stdout)["stl_volume"]), exp["stl_volume_mm3"], places=2)


@unittest.skipUnless(HAVE_TOOLS, "OpenSCAD 2021.01 or FreeCAD 1.1.3 not installed at the locked path")
class ReproducibilityTests(unittest.TestCase):
    def test_two_conversions_differ_only_in_file_name_time_stamp(self):
        with tempfile.TemporaryDirectory() as t:
            texts = []
            for i in (1, 2):
                step = os.path.join(t, f"run{i}", "cube.step")
                os.makedirs(os.path.dirname(step))
                r = run("--scad", os.path.join(FIXTURE, "cube.scad"), "--step", step)
                self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
                with open(step) as fh:
                    texts.append(fh.read())
                time.sleep(1.1)
            stamp = re.compile(r"(FILE_NAME\s*\(\s*'(?:[^']|'')*'\s*,\s*)'(?:[^']|'')*'", re.S)
            self.assertNotEqual(texts[0], texts[1], "time stamps expected to differ between runs 1.1 s apart")
            norm = [stamp.sub(r"\1'normalized'", s, count=1) for s in texts]
            self.assertEqual(norm[0], norm[1])


if __name__ == "__main__":
    unittest.main()
