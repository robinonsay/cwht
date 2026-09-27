"""Stand-in for the FreeCAD Part module (test double of TV-015; see FreeCAD.py).

export() writes a placeholder STEP file unless the case says it writes none; read() returns the
read-back shape of the case named by CWHT_FAKE_FREECAD_CASE. Both are logged to CWHT_FAKE_FREECAD_LOG.
"""
from __future__ import annotations

import FreeCAD


def export(objects: list, path: str) -> None:
    _, _, writes, _, _, _ = FreeCAD.case()
    if len(objects) != 1 or objects[0].Shape is None:
        raise RuntimeError("FreeCAD test double: export expects one object with a shape")
    if writes:
        with open(path, "w") as fh:
            fh.write("ISO-10303-21;\n/* FreeCAD test double of TV-015, not a STEP model */\nEND-ISO-10303-21;\n")
        FreeCAD.log(f"export {path} written")
    else:
        FreeCAD.log(f"export {path} not written")


def read(path: str) -> "FreeCAD.Shape":
    _, _, _, solids, valid, volume = FreeCAD.case()
    FreeCAD.log(f"read {path}")
    return FreeCAD.Shape("Solid" if solids == 1 else "Compound", solids, valid, volume)
