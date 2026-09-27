"""Stand-in for the FreeCAD OpenSCAD workbench importCSG module (test double of TV-015; see FreeCAD.py).

insert() ignores the CSG content and adds one top-level object whose shape is the root of the case
named by CWHT_FAKE_FREECAD_CASE.
"""
from __future__ import annotations

import os

import FreeCAD


def insert(path: str, doc_name: str) -> None:
    if not os.path.isfile(path):
        raise IOError(f"FreeCAD test double: no such CSG {path}")
    root_type, root_solids, _, _, _, _ = FreeCAD.case()
    doc = FreeCAD.getDocument(doc_name)
    doc.Objects.append(FreeCAD._Object("Root", FreeCAD.Shape(root_type, root_solids, True, FreeCAD.SHAPE_VOLUME)))
