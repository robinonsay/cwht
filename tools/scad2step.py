#!/usr/bin/env python3
"""OpenSCAD CSG to STEP through headless FreeCAD, with the acceptance checks of ADR-008 (TV-015).

CM plan section 8.2 step 3 and docs/research/enclosure-cnc-and-openscad-pipeline.md step 3
(corrected 2026-09-26). The same file runs in two modes.

FreeCAD mode, the form the CM plan names (run by freecadcmd; inputs from the environment):

    CWHT_CSG=/abs/part.csg CWHT_STL=/abs/part.stl CWHT_STEP=/abs/part.step \\
        /Applications/FreeCAD.app/Contents/Resources/bin/freecadcmd tools/scad2step.py

  imports the CSG through the FreeCAD OpenSCAD workbench (placeholders for unsupported
  operations disabled), takes the single top-level result, refines it (removeSplitter),
  unwraps a Compound of exactly one Solid (FreeCAD 1.1.3 returns the OpenSCAD cut that way,
  tools/toolchain.lock.md section 1.4 finding 4), and checks, in this order:
    C1 FreeCAD is the locked 1.1.3
    C2 exactly one top-level object
    C3 the shape is valid and a Solid (or CompSolid)
    C4 exactly one solid
    C5 no BSplineSurface face (non-uniform scale or resize in the source)
    C6 the STEP written and read back holds exactly one valid solid whose volume equals the
       exported shape's within 1e-6 (relative)
    C7 the STEP volume is within 0.5 % of the volume of the OpenSCAD mesh CWHT_STL
       (binary or ASCII STL, signed tetrahedron sum)
  It prints one "SCAD2STEP KAT ..." line with the measured values and ends with the success
  marker "SCAD2STEP PASS wrote <path>", or with "SCAD2STEP FAIL <check>: <reason>" and no STEP
  file left behind. freecadcmd exits 0 even when a script raises, so a caller checks the marker
  and the STEP file, never the exit status of freecadcmd (lock section 1.4 finding 4).

Driver mode (the project interpreter; the checked entry point for release packages):

    .venv/bin/python tools/scad2step.py --scad SRC.scad --step OUT.step [--csg OUT.csg] [--timeout S]
    .venv/bin/python tools/scad2step.py --csg SRC.csg --stl SRC.stl --step OUT.step [--timeout S]

  With --scad it first runs OpenSCAD 2021.01 with absolute output paths (lock section 1.4
  finding 3): -o CSG (to --csg, or a temporary file) and --export-format binstl -o a temporary
  STL, after checking that "OpenSCAD --version" prints exactly "OpenSCAD version 2021.01". It
  then checks that the FreeCAD bundle CFBundleVersion is exactly 1.1.3 (skipped when the
  CWHT_FREECADCMD hook is set; check C1 inside FreeCAD mode always applies), runs freecadcmd on
  this file in FreeCAD mode under a time-out guard that kills only the process group it
  started, and turns the marker into an exit status. A failed run leaves no STEP file.

  Exit status: 0 success marker and a STEP file present; 1 an acceptance check failed, OpenSCAD
  failed, or no success marker; 2 usage error; 3 OpenSCAD or freecadcmd not installed at the
  locked path; 4 OpenSCAD or FreeCAD is not the locked version; 124 time-out (default 600 s).

Test hooks (never set for a run for the record; each one prints "scad2step: TEST HOOK" on stderr):
  CWHT_OPENSCAD, CWHT_FREECADCMD replace the executables (test doubles); CWHT_SCAD2STEP_EXPECT_OPENSCAD
  and CWHT_SCAD2STEP_EXPECT_FREECAD name a second version that must also match (add-only: they
  cannot replace the locked values).
"""
from __future__ import annotations

import os
import struct
import sys

LOCK_OPENSCAD = "/Applications/OpenSCAD-2021.01.app/Contents/MacOS/OpenSCAD"
LOCK_OPENSCAD_VERSION = "OpenSCAD version 2021.01"
LOCK_FREECADCMD = "/Applications/FreeCAD.app/Contents/Resources/bin/freecadcmd"
LOCK_FREECAD_PLIST = "/Applications/FreeCAD.app/Contents/Info.plist"
LOCK_FREECAD_VERSION = "1.1.3"
VOLUME_TOLERANCE = 0.005      # C7: STEP against mesh (CM plan section 8.2 step 3)
REREAD_TOLERANCE = 1e-6       # C6: STEP read back against the exported shape
MARK = "SCAD2STEP"

EXIT_PASS, EXIT_CHECK, EXIT_USAGE, EXIT_MISSING, EXIT_VERSION, EXIT_TIMEOUT = 0, 1, 2, 3, 4, 124


# --------------------------------------------------------------------------- mesh volume (both modes)
def stl_volume(path: str) -> tuple[float, int]:
    """Signed volume (mm^3) and facet count of a binary or ASCII STL (sum of origin tetrahedra)."""
    with open(path, "rb") as fh:
        data = fh.read()
    triangles = []
    if len(data) >= 84:
        (n,) = struct.unpack_from("<I", data, 80)
        if 84 + 50 * n == len(data):
            for i in range(n):
                v = struct.unpack_from("<12f", data, 84 + 50 * i)
                triangles.append((v[3:6], v[6:9], v[9:12]))
    if not triangles:
        text = data.decode("ascii", errors="strict")
        if not text.lstrip().startswith("solid"):
            raise ValueError(f"{path}: neither a binary nor an ASCII STL")
        verts = [tuple(float(x) for x in line.split()[1:4]) for line in text.splitlines() if line.strip().startswith("vertex")]
        if len(verts) % 3 or not verts:
            raise ValueError(f"{path}: ASCII STL with {len(verts)} vertices")
        triangles = [tuple(verts[i:i + 3]) for i in range(0, len(verts), 3)]
    vol = 0.0
    for (ax, ay, az), (bx, by, bz), (cx, cy, cz) in triangles:
        vol += (ax * (by * cz - bz * cy) - ay * (bx * cz - bz * cx) + az * (bx * cy - by * cx)) / 6.0
    return vol, len(triangles)


# --------------------------------------------------------------------------- FreeCAD mode
class CheckFailed(Exception):
    def __init__(self, check: str, reason: str):
        super().__init__(f"{check}: {reason}")
        self.check = check


def freecad_convert() -> int:
    import FreeCAD  # noqa: F401  (present only under freecadcmd)
    import Part
    import importCSG

    out = None
    try:
        missing = [k for k in ("CWHT_CSG", "CWHT_STL", "CWHT_STEP") if not os.environ.get(k)]
        if missing:
            raise CheckFailed("usage", "environment variable(s) not set: " + ", ".join(missing))
        src, stl, out = (os.path.abspath(os.environ[k]) for k in ("CWHT_CSG", "CWHT_STL", "CWHT_STEP"))
        if os.path.exists(out):
            os.remove(out)
        version = ".".join(FreeCAD.Version()[:3])
        for expected in filter(None, (LOCK_FREECAD_VERSION, os.environ.get("CWHT_SCAD2STEP_EXPECT_FREECAD"))):
            if version != expected:
                raise CheckFailed("C1", f"FreeCAD is {version}, expected {expected}")
        for p in (src, stl):
            if not os.path.isfile(p):
                raise CheckFailed("usage", f"no such file {p}")
        prefs = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/OpenSCAD")
        prefs.SetString("openscadexecutable", LOCK_OPENSCAD)
        prefs.SetBool("usePlaceholderForUnsupported", False)
        doc = FreeCAD.newDocument("scad2step")
        importCSG.insert(src, doc.Name)
        doc.recompute()
        roots = [o for o in doc.Objects if hasattr(o, "Shape") and not o.InList]
        if len(roots) != 1:
            raise CheckFailed("C2", f"expected one top-level object, got {len(roots)}")
        shape = roots[0].Shape.removeSplitter()
        root_type = shape.ShapeType
        if shape.ShapeType == "Compound" and len(shape.Solids) == 1:
            shape = shape.Solids[0]
        if not (shape.isValid() and shape.ShapeType in ("Solid", "CompSolid")):
            raise CheckFailed("C3", f"invalid or non-solid result (ShapeType {shape.ShapeType}, valid {shape.isValid()})")
        if len(shape.Solids) != 1:
            raise CheckFailed("C4", f"STEP must hold exactly one solid, got {len(shape.Solids)}")
        faces = [f.Surface.__class__.__name__ for f in shape.Faces]
        if "BSplineSurface" in faces:
            raise CheckFailed("C5", f"{faces.count('BSplineSurface')} BSplineSurface face(s); check for non-uniform scale or resize")
        feat = doc.addObject("Part::Feature", "Refined")
        feat.Shape = shape
        doc.recompute()
        Part.export([feat], out)
        if not os.path.isfile(out):
            raise CheckFailed("C6", "FreeCAD wrote no STEP file")
        back = Part.read(out)
        if len(back.Solids) != 1 or not back.isValid():
            raise CheckFailed("C6", f"STEP read back holds {len(back.Solids)} solid(s), valid {back.isValid()}")
        if abs(back.Volume - shape.Volume) > REREAD_TOLERANCE * shape.Volume:
            raise CheckFailed("C6", f"STEP volume {back.Volume:.6f} differs from the shape volume {shape.Volume:.6f}")
        mesh_vol, facets = stl_volume(stl)
        err = abs(back.Volume - mesh_vol) / abs(mesh_vol) if mesh_vol else float("inf")
        kinds = {k: faces.count(k) for k in sorted(set(faces))}
        print(f"{MARK} KAT root={root_type} solids={len(shape.Solids)} valid={shape.isValid()} faces={len(faces)} "
              f"cylinders={faces.count('Cylinder')} bspline={faces.count('BSplineSurface')} surfaces={kinds} "
              f"volume={shape.Volume:.3f} step_volume={back.Volume:.3f} stl_volume={mesh_vol:.3f} stl_facets={facets} "
              f"stl_error_pct={err * 100:.4f} freecad={version}", flush=True)
        if err > VOLUME_TOLERANCE:
            raise CheckFailed("C7", f"STEP volume {back.Volume:.3f} is {err * 100:.3f} % from the mesh volume {mesh_vol:.3f} (limit 0.5 %)")
        print(f"{MARK} PASS wrote {out}", flush=True)
        return 0
    except CheckFailed as exc:
        _fail(str(exc), out)
    except Exception as exc:  # noqa: BLE001 - any FreeCAD error is a failed conversion
        _fail(f"exception: {type(exc).__name__}: {exc}", out)
    return 1


def _fail(message: str, out: str | None) -> None:
    if out and os.path.exists(out):
        os.remove(out)
    print(f"{MARK} FAIL {message}", flush=True)


# --------------------------------------------------------------------------- driver mode
def _hooked(name: str) -> str | None:
    value = os.environ.get(name)
    if value:
        print(f"scad2step: TEST HOOK {name}={value}", file=sys.stderr)
    return value


def _run(cmd: list[str], timeout: float, env: dict | None = None):
    """Run cmd in its own process group; on time-out kill that group only. Returns (rc, output) or None on time-out."""
    import signal
    import subprocess
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, env=env, start_new_session=True)
    try:
        out, _ = proc.communicate(timeout=timeout)
        return proc.returncode, out
    except subprocess.TimeoutExpired:
        try:
            os.killpg(proc.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
        proc.communicate()
        return None


def driver(argv: list[str]) -> int:
    import argparse
    import subprocess
    import tempfile
    import time

    ap = argparse.ArgumentParser(prog="scad2step.py", description="OpenSCAD CSG to STEP through headless FreeCAD (TV-015)")
    ap.add_argument("--scad")
    ap.add_argument("--csg")
    ap.add_argument("--stl")
    ap.add_argument("--step", required=True)
    ap.add_argument("--timeout", type=float, default=600.0)
    try:
        args = ap.parse_args(argv)
    except SystemExit as exc:
        return EXIT_USAGE if exc.code else 0
    valid = (args.scad and not args.stl) or (not args.scad and args.csg and args.stl)
    if not valid or args.timeout <= 0:
        print("scad2step: error: give --scad SRC (with optional --csg OUT), or --csg SRC with --stl SRC; --timeout > 0",
              file=sys.stderr)
        return EXIT_USAGE
    step = os.path.abspath(args.step)
    if not os.path.isdir(os.path.dirname(step)):
        print(f"scad2step: error: output directory of {step} does not exist", file=sys.stderr)
        return EXIT_USAGE
    openscad = _hooked("CWHT_OPENSCAD") or LOCK_OPENSCAD
    freecadcmd = _hooked("CWHT_FREECADCMD") or LOCK_FREECADCMD
    deadline = time.monotonic() + args.timeout
    work = tempfile.mkdtemp(prefix="scad2step.")
    try:
        if args.scad:
            scad = os.path.abspath(args.scad)
            if not os.path.isfile(scad):
                print(f"scad2step: error: no such file {scad}", file=sys.stderr)
                return EXIT_USAGE
            if not os.access(openscad, os.X_OK):
                print(f"scad2step: OpenSCAD not installed at {openscad}", file=sys.stderr)
                return EXIT_MISSING
            r = _run([openscad, "--version"], 60)
            got = (r[1].strip().splitlines() or [""])[-1] if r else ""
            for expected in filter(None, (LOCK_OPENSCAD_VERSION, _hooked("CWHT_SCAD2STEP_EXPECT_OPENSCAD"))):
                if got != expected:
                    print(f"scad2step: OpenSCAD version is '{got}', expected '{expected}'", file=sys.stderr)
                    return EXIT_VERSION
            csg = os.path.abspath(args.csg) if args.csg else os.path.join(work, "part.csg")
            stl = os.path.join(work, "part.stl")
            for cmd in ([openscad, "-o", csg, scad], [openscad, "--export-format", "binstl", "-o", stl, scad]):
                r = _run(cmd, max(1.0, deadline - time.monotonic()))
                if r is None:
                    print(f"scad2step: TIMEOUT after {args.timeout} s in OpenSCAD", file=sys.stderr)
                    return EXIT_TIMEOUT
                if r[0] != 0 or not os.path.isfile(cmd[-2]):
                    print(f"scad2step: OpenSCAD failed (exit {r[0]}): {r[1].strip()[-400:]}", file=sys.stderr)
                    return EXIT_CHECK
        else:
            csg, stl = os.path.abspath(args.csg), os.path.abspath(args.stl)
            for p in (csg, stl):
                if not os.path.isfile(p):
                    print(f"scad2step: error: no such file {p}", file=sys.stderr)
                    return EXIT_USAGE
        if not os.access(freecadcmd, os.X_OK):
            print(f"scad2step: freecadcmd not installed at {freecadcmd}", file=sys.stderr)
            return EXIT_MISSING
        if not os.environ.get("CWHT_FREECADCMD"):
            plist = subprocess.run(["defaults", "read", LOCK_FREECAD_PLIST, "CFBundleVersion"], capture_output=True, text=True)
            got = plist.stdout.strip()
            for expected in filter(None, (LOCK_FREECAD_VERSION, os.environ.get("CWHT_SCAD2STEP_EXPECT_FREECAD"))):
                if got != expected:
                    print(f"scad2step: FreeCAD bundle version is '{got}', expected '{expected}'", file=sys.stderr)
                    return EXIT_VERSION
        env = dict(os.environ, CWHT_CSG=csg, CWHT_STL=stl, CWHT_STEP=step)
        r = _run([freecadcmd, os.path.abspath(__file__)], max(1.0, deadline - time.monotonic()), env)
        if r is None:
            if os.path.exists(step):
                os.remove(step)
            print(f"scad2step: TIMEOUT after {args.timeout} s in freecadcmd (its process group killed)", file=sys.stderr)
            return EXIT_TIMEOUT
        lines = [ln for ln in r[1].splitlines() if ln.startswith(MARK + " ")]
        for ln in lines:
            print(ln)
        if lines and lines[-1].startswith(f"{MARK} FAIL C1:"):
            return EXIT_VERSION
        if lines and lines[-1] == f"{MARK} PASS wrote {step}" and os.path.isfile(step):
            print(f"scad2step: PASS {step} (freecadcmd exit {r[0]})", file=sys.stderr)
            return EXIT_PASS
        if not lines:
            print(f"scad2step: FAIL no {MARK} marker from freecadcmd (exit {r[0]}); output tail: {r[1].strip()[-400:]}",
                  file=sys.stderr)
        else:
            print(f"scad2step: {lines[-1][len(MARK) + 1:]}", file=sys.stderr)
        if os.path.exists(step) and not (lines and lines[-1].startswith(f"{MARK} PASS")):
            os.remove(step)
        return EXIT_CHECK
    finally:
        for name in sorted(os.listdir(work)):
            os.remove(os.path.join(work, name))
        os.rmdir(work)


def _in_freecad() -> bool:
    try:
        import FreeCAD  # noqa: F401
    except ImportError:
        return False
    return True


if _in_freecad():
    # freecadcmd executes the file as a script; its exit status is not meaningful (lock section 1.4 finding 4).
    freecad_convert()
elif __name__ == "__main__":
    sys.exit(driver(sys.argv[1:]))
