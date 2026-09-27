// Mesh source for the seeded volume fault of tools/scad2step.py (TV-015, check C7): the cube.scad
// block 11 mm tall instead of 10 mm, so its mesh volume (6289.48 mm^3 for the 64-sided hole) is 9.1 % above the
// 5717.257 mm^3 cube.csg solid.
difference() {
    cube([30, 20, 11]);
    translate([15, 10, -1]) cylinder(d = 6, h = 13, $fn = 64);
}
