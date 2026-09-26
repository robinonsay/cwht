# Listing of docs/research/enclosure-cnc-and-openscad-pipeline.md step 3, run from a scratch copy for the
# 2026-09-25 freecadcmd sanity check. Changes from the listing: input and output paths come from the
# environment (CWHT_CSG, CWHT_STEP) instead of the fixed names, and the measured values are printed
# as one KAT line. It is not tools/scad2step.py (not yet written; CM plan section 8.2 step 3).
import os, sys, FreeCAD, Part, importCSG
src = os.path.abspath(os.environ["CWHT_CSG"]); out = os.path.abspath(os.environ["CWHT_STEP"])
p = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/OpenSCAD")
p.SetString("openscadexecutable", "/Applications/OpenSCAD-2021.01.app/Contents/MacOS/OpenSCAD")
p.SetBool("usePlaceholderForUnsupported", False)   # fail loudly instead of inserting placeholders
doc = FreeCAD.newDocument("enclosure")
importCSG.insert(src, doc.Name)
doc.recompute()
roots = [o for o in doc.Objects if hasattr(o, "Shape") and not o.InList]   # top-level result(s)
assert len(roots) == 1, "expected one top-level solid, got %d" % len(roots)
shape = roots[0].Shape.removeSplitter()                                     # refine coplanar faces
assert shape.isValid() and shape.ShapeType in ("Solid", "CompSolid"), "invalid or non-solid result"
assert len(shape.Solids) == 1, "STEP must contain exactly one solid for CNC"
faces = [f.Surface.__class__.__name__ for f in shape.Faces]
assert "BSplineSurface" not in faces, "BSpline faces present; check for non-uniform scale/resize"
print("volume mm^3:", round(shape.Volume, 2), "faces:", len(faces), "cylinders:", faces.count("Cylinder"))
feat = doc.addObject("Part::Feature", "EnclosureRefined"); feat.Shape = shape; doc.recompute()
Part.export([feat], out)                                                    # scheme AP214/AP242 per FreeCAD Import-Export preferences
print("wrote", out)
back = Part.read(out)
print("KAT solids=%d valid=%s faces=%d cylinders=%d bspline=%d volume=%.3f step_reread_solids=%d step_reread_volume=%.3f" % (
    len(shape.Solids), shape.isValid(), len(faces), faces.count("Cylinder"), faces.count("BSplineSurface"), shape.Volume,
    len(back.Solids), back.Volume))
