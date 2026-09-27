// Seeded fault for tools/scad2step.py (TV-015): a twisted extrusion, one top-level object whose
// side faces FreeCAD 1.1.3 builds as BSplineSurface (check C5; observed 2026-09-27).
linear_extrude(height = 10, twist = 90) square([6, 3], center = true);
