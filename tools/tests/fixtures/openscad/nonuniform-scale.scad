// Seeded fault for tools/scad2step.py (TV-015): an elliptical hole made by a non-uniform scale of a
// cylinder, outside the restricted dialect of ADR-008. FreeCAD 1.1.3 imports the scale as a
// Matrix_Deformation of BSpline faces and leaves the unscaled cylinder as a second top-level object
// (observed 2026-09-27), so the run stops at check C2 before C5.
difference() {
    cube([30, 20, 10]);
    translate([15, 10, -1]) scale([1, 2, 1]) cylinder(d = 6, h = 12, $fn = 64);
}
