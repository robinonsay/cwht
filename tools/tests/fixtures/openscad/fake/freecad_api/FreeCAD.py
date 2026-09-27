"""Stand-in for the FreeCAD module (test double of TV-015, INSP-088 finding-1; not FreeCAD).

Loaded only by fake/freecadcmd-api-double, which puts this directory on PYTHONPATH and runs
tools/scad2step.py, so that the script's FreeCAD mode runs its own check code on a shape chosen by
CWHT_FAKE_FREECAD_CASE. It implements exactly the attributes FreeCAD mode uses: Version, ParamGet,
newDocument (Name, Objects, recompute, addObject), and, through Part and importCSG, the Shape
attributes ShapeType, Solids, Faces[].Surface, Volume, isValid() and removeSplitter(). An attribute
the script uses and this double lacks raises, and the script then prints "SCAD2STEP FAIL exception",
so the control case fails if the double and the script drift apart.

Cases (the exported shape is always 6000.000 mm^3, the volume of the 30 x 20 x 10 box mesh the
test writes, so that the control case reaches C7 with a hand-known mesh volume):
  control         Solid, valid, 6 planar faces; STEP written; read back 1 valid solid of 6000.003
                  mm^3 (relative difference 5e-7, inside the C6 tolerance 1e-6): PASS
  c4-compsolid    CompSolid of 2 valid solids (3000 mm^3 each): C4
  c6-no-file      as control, but the export writes no file: C6
  c6-two-solids   as control, but the read-back holds 2 solids: C6
  c6-invalid      as control, but the read-back is 1 solid and not valid: C6
  c6-volume       as control, but the read-back is 6000.012 mm^3 (relative difference 2e-6): C6
Each export and read is appended to the file named by CWHT_FAKE_FREECAD_LOG when it is set, so a test
can show that a STEP file existed before the refusal removed it.
"""
from __future__ import annotations

import os

SHAPE_VOLUME = 6000.0
CASES = {
    # case: (root ShapeType, root solid count, export writes a file, read-back solids, valid, volume)
    "control": ("Solid", 1, True, 1, True, 6000.003),
    "c4-compsolid": ("CompSolid", 2, True, 1, True, 6000.0),
    "c6-no-file": ("Solid", 1, False, 1, True, 6000.0),
    "c6-two-solids": ("Solid", 1, True, 2, True, 6000.0),
    "c6-invalid": ("Solid", 1, True, 1, False, 6000.0),
    "c6-volume": ("Solid", 1, True, 1, True, 6000.012),
}


def case():
    name = os.environ.get("CWHT_FAKE_FREECAD_CASE", "")
    if name not in CASES:
        raise RuntimeError(f"FreeCAD test double: unknown CWHT_FAKE_FREECAD_CASE {name!r}")
    return CASES[name]


def log(line: str) -> None:
    path = os.environ.get("CWHT_FAKE_FREECAD_LOG")
    if path:
        with open(path, "a") as fh:
            fh.write(line + "\n")


class Plane:
    """Surface class; scad2step reads only the class name."""


class Face:
    def __init__(self):
        self.Surface = Plane()


class Shape:
    def __init__(self, shape_type: str, solids: int, valid: bool, volume: float):
        self.ShapeType = shape_type
        self.Volume = volume
        self._valid = valid
        self.Faces = [Face() for _ in range(6 * solids)]
        if shape_type == "Solid":
            self.Solids = [self]
        else:
            self.Solids = [Shape("Solid", 1, valid, volume / solids) for _ in range(solids)]

    def isValid(self) -> bool:
        return self._valid

    def removeSplitter(self) -> "Shape":
        return self


class _Object:
    def __init__(self, name: str, shape: Shape | None = None):
        self.Name = name
        self.Shape = shape
        self.InList = []


class _Document:
    def __init__(self, name: str):
        self.Name = name
        self.Objects = []

    def recompute(self) -> None:
        pass

    def addObject(self, type_name: str, name: str) -> _Object:
        if type_name != "Part::Feature":
            raise RuntimeError(f"FreeCAD test double: addObject({type_name!r}) not modelled")
        obj = _Object(name)
        self.Objects.append(obj)
        return obj


class _Params:
    def SetString(self, key: str, value: str) -> None:
        pass

    def SetBool(self, key: str, value: bool) -> None:
        pass


_DOCUMENTS: dict[str, _Document] = {}


def Version():
    return ["1", "1", "3", "test double"]


def ParamGet(path: str) -> _Params:
    return _Params()


def newDocument(name: str) -> _Document:
    doc = _Document(name)
    _DOCUMENTS[name] = doc
    return doc


def getDocument(name: str) -> _Document:
    return _DOCUMENTS[name]
