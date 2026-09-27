// Seeded fault for tools/scad2step.py (TV-015): two disjoint blocks in one union, so the single
// top-level result is a compound of two solids, not one solid (check C3).
union() {
    cube([10, 10, 10]);
    translate([20, 0, 0]) cube([10, 10, 10]);
}
