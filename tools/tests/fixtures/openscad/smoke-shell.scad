// Smoke-test half-shell of docs/research/enclosure-cnc-and-openscad-pipeline.md B2 (the seed of the
// enclosure model), for the tools/scad2step.py known answer (TV-015; PDR work plan WP-PDR-07 "smoke
// shell to STEP"). One change from B2: the shell and its bosses are wrapped in union(), so the CSG has
// one top-level object (check C2); B2 left them as two.
$fn = 64;
L = 110; W = 62; H = 18; wall = 2.0; floor_t = 2.0; r_in = 2.0;
module rbox(l, w, h, r) { linear_extrude(h) offset(r) offset(-r) square([l, w], center = true); }
union() {
  difference() {
    rbox(L, W, H, 4);
    translate([0, 0, floor_t]) rbox(L - 2*wall, W - 2*wall, H, r_in);
    for (x = [-1, 1], y = [-1, 1]) translate([x*(L/2 - 6), y*(W/2 - 6), -1]) cylinder(d = 2.5, h = floor_t + 10);
  }
  for (x = [-1, 1], y = [-1, 1]) translate([x*(L/2 - 6), y*(W/2 - 6), floor_t]) difference() { cylinder(d = 6, h = 6); cylinder(d = 2.5, h = 7); }
}
