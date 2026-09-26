// Known-answer fixture for OpenSCAD 2021.01 + FreeCAD 1.1.3 (tools/toolchain.lock.md section 1.1).
// A 30 x 20 x 10 mm block with one 6 mm through hole on the vertical axis at (15, 10).
// Restricted dialect of ADR-008: cube, cylinder, difference, translate; $fn >= 32 on the round feature.
difference() {
    cube([30, 20, 10]);
    translate([15, 10, -1]) cylinder(d = 6, h = 12, $fn = 64);
}
