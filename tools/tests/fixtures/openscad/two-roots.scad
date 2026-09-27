// Seeded fault for tools/scad2step.py (TV-015): two top-level objects (no enclosing union), so the
// CSG import has two roots (check C2).
cube([10, 10, 10]);
translate([20, 0, 0]) cube([10, 10, 10]);
