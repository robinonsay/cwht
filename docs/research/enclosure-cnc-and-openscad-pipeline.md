# Research report: PCBWay CNC enclosure service and the OpenSCAD to STEP pipeline

**Assignment key:** pcbway-cnc-openscad
**Date:** 2026-09-25
**Author:** research agent (independent invocation), for the cwht lead systems engineer
**Status:** complete; open items listed at the end
**Governing intent:** charter section 9 (pre-build evidence classes: Analysis, Inspection, rendered-image review) and section 11 (evidence not assertion; visual closure of every CAD product)

## Question

(A) What does PCBWay's CNC machining service accept and guarantee for a small aluminum handheld enclosure: file formats, alloys, finishes, tolerances, minimum wall, internal corner radii and tool access, threads and inserts, engraving, pricing signals and lead time; and is PCBWay 3D printing a useful cheaper fit-check path?

(B) On macOS, how do we get from an OpenSCAD source to a true B-rep STEP file that PCBWay will machine, why is mesh-to-STEP not acceptable, how is FreeCAD's OpenSCAD workbench driven headless, what are the CadQuery/build123d alternatives, how do we render OpenSCAD to PNG from the CLI for review, and how do we produce Bambu Studio-ready 3MF files for fit-check prints on the owner's Bambu Lab H2C? Deliver a recommended pipeline with exact commands.

## Method

1. Web research with WebSearch and WebFetch against primary sources: pcbway.com capability pages, help-center engineering articles and FAQ; FreeCAD documentation mirror on GitHub (the wiki itself blocks automated fetches), FreeCAD source (`importCSG.py`, `OpenSCADUtils.py`, `package/bundle/osx/create_bundle.sh`); OpenSCAD wikibook CLI manual, openscad.org news and downloads pages, the OpenSCAD mailing-list announcement of the Manifold default; Bambu Studio CLI wiki; CadQuery and build123d docs and PyPI pages; Homebrew cask metadata via `brew info`.
2. Local, sandboxed trials in the session scratch directory (nothing installed): OpenSCAD 2021.01 at `/Applications/OpenSCAD-2021.01.app` exported STL, 3MF, CSG and PNG from a purpose-written enclosure half-shell; the render PNG was opened and inspected; Bambu Studio 02.08.02.61 at `/Applications/BambuStudio.app` was driven from the CLI with the H2C system presets to produce project 3MF files and attempt headless slicing.
3. FreeCAD, CadQuery and build123d are not installed on this machine, and the assignment did not authorize installs, so the FreeCAD script in this report is documented against source and docs but is marked untested (ACTION below).

## Findings

### Part A: PCBWay CNC machining and 3D printing

**A1. Accepted CAD formats for CNC: STEP/STP, Parasolid X_T, IGES, SLDPRT. STL is refused, and PCBWay states that STL converted to STEP is still unacceptable.**
The CNC ordering guide lists "*.step, *.stp, *.x_t, *.iges, *.sldprt" and "up to 12 files at a time" (https://www.pcbway.com/blog/CNC_Machining/CNC_Ordering_Process_PCBWay_Website_Exploration_07_59da1665.html). The FAQ says "STL files cannot be used to fabricate CNC, Sheet Metal, or Injection Molded components" (https://www.pcbway.com/rapid-prototyping/cnc-faq.html). PCBWay's 2024-06-14 article explains that in STL "a perfect circle becomes a polygon" and that "Even if STL files are converted to other formats such as STEP, the lack of original geometric information cannot be compensated for and therefore remains unsuitable for CNC machining" (https://www.pcbway.com/blog/CNC_Machining/Why_the_stl_file_can_not_be_used_for_CNC_dca4b7d9.html). Confidence: High.

**A2. A 2D drawing is required whenever the part has threads, tighter-than-default tolerances, roughness callouts, part marking or assembly requirements; the CAD file takes precedence over the drawing.**
"an additional technical drawing is required to indicate critical dimensions if your design contains threads or needs tighter tolerances, roughness, part marking, or requirements for the part assembly" (ordering guide, URL as A1). Laser engraving artwork must be AI or SVG and its "dimension and placement" marked on the 2D drawing (https://www.pcbway.com/rapid-prototyping/Surface-Finishing/silkscreen/laser-engraving/). Confidence: High.

**A3. Aluminum alloys offered for CNC: 6061, 7075, 5052, 2A12. 6063 is not on the menu.**
Materials list on https://www.pcbway.com/rapid-prototyping/cnc-machining/ and https://www.pcbway.com/rapid-prototyping/cnc-machining/cnc-milling.html. The 6061 material page gives tensile 310 MPa, yield 276 MPa, "Build Time: 3-5 Business Days" and no temper designation (https://www.pcbway.com/rapid-prototyping/cnc-machining/metal/aluminum/Aluminum-6061/). A third-party machining vendor notes that 7075 "anodizes unevenly compared to 6061" because of its zinc content and recommends 6061 or 6063 for consistent decorative anodize (https://baoshengindustry.com/cnc-machining-aluminum-parts/). Confidence: High for the menu; Medium for the 7075 anodize note (secondary source, consistent with general industry practice).

**A4. Finishes and their published parameters (CNC milling page).**
As-milled "comparable to 125 uin Ra"; bead blast "#120 grit"; anodized "Type II or Type III"; bead blast plus anodize "8-12 um clear, 4-8 um color"; powder coat "18-72 um"; brushed "#80-120 grit" (https://www.pcbway.com/rapid-prototyping/cnc-machining/cnc-milling.html). The bead-blast-plus-anodize page lists twelve colors (natural, black, gray, gold, rose gold, red, blue, champagne, brown, purple, green, orange), warns "There will be a certain color difference between the actual color after anodizing and the above color board" and "Rack marks are inherent to the anodizing process ... identify where the part will be racked" (https://www.pcbway.com/rapid-prototyping/Surface-Finishing/anodized/bead-blast-anodized-color/). Aluminum has "up to 28 kinds of surface finish options" (ordering guide). The 2025-12-11 anodized sample showcase repeats that results "may vary slightly depending on material and production conditions" (https://www.pcbway.com/blog/CNC_Machining/Anodized_Samples_Showcase_Real_Finishes_Colors_and_Surface_Quality_cd34a546.html). Confidence: High.

**A5. Tolerances: ISO 2768-1 class m is the default for metals with no drawing; the marketing figure of +/-0.005 in (0.125 mm) applies to dimensions called out on a drawing.**
Help center (updated 2026-07-13): metals default "Class m", table 0.5-3 mm +/-0.1, 3-6 mm +/-0.1, 6-30 mm +/-0.2, 30-120 mm +/-0.3; class f is +/-0.05/0.05/0.1/0.15 over the same ranges; default roughness Ra 6.3 um; "ISO 2768 applies only to dimensions and geometrical features for which no individual tolerances are specified" (https://www.pcbway.com/helpcenter/cnc_engineering_questions/ISO_2768_General_Tolerances_for_CNC_Machining.html). The quality-control page repeats the ISO 2768-1 default and offers "Standard Inspection with Formal Report", "CMM Inspection with Formal Report" and "Source Material Certification" (https://www.pcbway.com/rapid-prototyping/quality-control-cnc.html). The milling page states "+/- 0.005 in" for features of size and location on 0-12 in parts and angularity "1/2 degree" (URL as A4); the FAQ says tolerances tighter than +/-0.005 in must be added in the Features tab. Confidence: High that both statements are published; Medium on how they interact (the help-center text is the more specific and more recent).

**A6. DFM rules published by PCBWay for pockets, walls, holes and tools.**
Corner radius article (updated 2026-07-15): "Internal Radius >= 1.3 x Cutter Radius"; "the corner radius should ideally be at least one-third of the pocket depth"; going from R0.5 to R3 "can typically reduce machining time by more than 30%" (https://www.pcbway.com/helpcenter/cnc_engineering_questions/CNC_Corner_Radius__Types__Machining_Standards_and_Design_Guidelines.html). The search excerpt of the same article states a minimum internal radius of R0.5 at depth <= 3 mm; the numeric tables are images and could not be extracted, so treat that specific value as Medium. Cost-reduction article (2025-12-03): "keep cavity depth/width ratios within 4-6", holes depth <= 10x diameter, slots depth <= 4x width, slot widths matching 3/4/6/8/10/12 mm end mills, drill sizes on whole or 0.5 mm steps, tight tolerances cost "3-5x" (https://www.pcbway.com/blog/CNC_Machining/10_Ways_to_Reduce_CNC_Machining_Costs_Practical_Design_Tips_b70d5b19.html). CAD-prep article (2021-10-14): end mills cut "three to four times their diameter" deep; minimum wall 0.8 mm metal, 1.5 mm plastic; threads "M6 or larger" recommended, "avoid anything smaller than M2"; 0.5 mm spacing between engraved characters (https://www.pcbway.com/blog/CNC_Machining/Tips_to_Know_When_Preparing_CAD_Model_for_CNC_Milling.html). Confidence: High for quoted rules.

**A7. Threads and inserts: model pilot holes, not thread geometry; specify threads in the Features tab and on the drawing; tapped holes need masking or "tap before anodizing".**
PCBWay's tapping guideline: "do not model physical thread geometry! Draw smooth, plain cylindrical pilot holes"; engagement "1.0 to 1.5 times the nominal bolt diameter"; for CNC blind holes drill "at least 3x Pitch (3P) beyond the effective thread depth"; specify "Tap before anodizing" or request thread masking (https://www.pcbway.com/blog/Tapping/Tapped_Parts_Design_Guidelines_23598863.html; the article is written for sheet metal but its CNC blind-hole rule is explicit). The tap drill for M3x0.5 is 2.5 mm (standard; also cited in the PCBWay corner-radius search excerpt). Helicoil and PEM inserts are listed among PCBWay CNC options in the search summary of their quote pages, but no help-center page with insert rules was found (Medium). Community questions on modeling threaded holes (2023-09-18, 2025-01-29) show PCBWay expects a drawing showing thread centers (https://www.pcbway.com/project/question/Modeling_threaded_holes_.html). Confidence: High for the modeling rule; Medium for inserts.

**A8. Marking: CNC engraving 0.2-0.5 mm deep; laser marking is surface-level, AI/SVG artwork only, flat surfaces only.**
Part-marking guide (updated 2026-07-21): engraving depth "0.2-0.5 mm is recommended", deep engraving above 0.5 mm, "simple sans-serif fonts", "Sharp internal corners cannot be fully machined because cutting tools have a fixed radius" (https://www.pcbway.com/helpcenter/cnc_engineering_questions/CNC_Part_Marking_Guide_for_Machined_Parts_with_Engraving__Laser_Marking__and_Screen_Printing.html). Laser engraving page: "ONLY Ai and svg formats are acceptable", "can be made only on flat surfaces" (URL as A2). Third-party guidance suggests 4 pt (1.42 mm) minimum laser text and 5 mm high, 0.8 mm deep CNC text (https://www.protocase.com/products/materials-components-finishes/finishes/laser-marking.php, https://www.hlhprototypes.com/designing-text-for-cnc-machining/). Confidence: High for PCBWay text; Low for third-party sizes.

**A9. Counterbore and countersink rules (PCBWay, 2026-09-07).**
90 degree countersinks for metric screws; counterbore diameter 0.5-1.0 mm larger than the head, depth 0.2-0.4 mm deeper than head height; edge distance >= 2x countersink major diameter; use standard CBORE/CSINK callouts on the drawing (https://www.pcbway.com/blog/Countersink-Counterbore/Countersink_Counterbore_Holes_Design_Guidelines_f328f60a.html). Confidence: High.

**A10. Pricing and lead-time signals.**
Minimum order "$25 excluding shipping" (FAQ). Cost drivers: machining time, material, setup and tooling, quantity discounts (cost article, A6). Milling "as fast as 2 day"; 6061 "3-5 Business Days" (A3). Real orders: several small anodized-blue aluminum parts, about $370, 13-15 days to manufacture plus 3 days delivery, versus $630+ quoted in Europe (2023-03-27, https://www.lets-talk-about.tech/2023/03/pcbway-cnc-machining.html); a single small aluminum block with a bore and an M7 thread quoted $257.69 machining only (2023-10-14, https://hackaday.io/project/190831/log/224322-a-pcbway-cnc-fabrication-costs-usd257-334). Reviews report good finish with occasional light scratches (https://www.pcbway.com/project/share/1.html?type=CNC). Quotes are instant on upload then manually reviewed (ordering guide). Confidence: Medium (third-party, 2023 prices).

**A11. PCBWay 3D printing as a fit-check path.**
Formats "*.stl, *.obj, *.step, and *.stp", each under 500 MB, 12 files per upload (https://www.pcbway.com/helpcenter/3d_ordering/What_file_formats_are_accepted_for_3D_printing_.html). SLA: accuracy "L<100mm, +/-0.2mm. L>100mm, +/-0.2%*L", minimum wall 0.8 mm, surface 3-10 um Ra, "as fast as 1 day" (https://www.pcbway.com/rapid-prototyping/3D-Printing/3D-Printing-SLA.html). SLS PA12: +/-0.25 mm under 100 mm, minimum wall 1 mm, ships in 3-4 days, 400 x 390 x 390 mm build (https://www.pcbway.com/rapid-prototyping/3D-Printing/3D-Printing-SLS.html). Process list FDM, SLA, SLS, MJF, SLM, DLP (https://www.pcbway.com/rapid-prototyping/3d-printing/). Because the owner has an H2C, PCBWay printing is a second-tier fit-check (for example an SLA print of the final STEP when a 0.2 mm tolerance check of a snap or boss pattern is wanted before the aluminum order). Confidence: High.

### Part B: OpenSCAD to STEP, PNG and 3MF on macOS

**B1. OpenSCAD has no STEP export in any version; 2021.01 is still the latest stable release, and development snapshots (2026.09.23 on Homebrew) are the maintained line with Manifold as the default engine since 2025-08-17.**
`OpenSCAD --help` on the installed 2021.01 lists output types "stl, off, amf, 3mf, csg, dxf, svg, pdf, png, echo, ast, term, nef3, nefdbg" (command below). The news page shows no stable release after 2021.01 (https://openscad.org/news.html). Marius Kintel's 2025-08-17 announcement made Manifold the default backend in snapshots, revertible with `--backend=cgal` (https://lists.openscad.org/empathy/thread/TMJEJCZINIJNYJX2YF7IDNBAPQY66KIF). Snapshots need "macOS 11 'Big Sur' or newer, universal build" (https://openscad.org/downloads.html). Locally: `brew info --cask openscad` reports 2021.01 "Disabled because it does not pass the macOS Gatekeeper check! It was disabled on 2026-09-01", while `brew info --cask openscad@snapshot` reports 2026.09.23 available. CLI options (`--camera`, `--imgsize`, `--projection`, `--render`, `--preview`, `--colorscheme`, `--autocenter`, `--viewall`, `-D`, `-p/-P`, `--export-format`, `--backend`, `--enable`) are documented at https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Using_OpenSCAD_in_a_command_line_environment. Confidence: High.

**B2. Local trial: OpenSCAD 2021.01 CLI exported STL, 3MF, CSG and two PNGs from a representative half-shell; the render was inspected and is correct.**
Test source (also the seed for the real enclosure model):
```scad
// cwht enclosure pipeline smoke test: pocketed half-shell, fillets, M3 bosses
$fn = 64;
L = 110; W = 62; H = 18; wall = 2.0; floor_t = 2.0; r_in = 2.0;
module rbox(l, w, h, r) { linear_extrude(h) offset(r) offset(-r) square([l, w], center = true); }
difference() {
  rbox(L, W, H, 4);
  translate([0, 0, floor_t]) rbox(L - 2*wall, W - 2*wall, H, r_in);
  for (x = [-1, 1], y = [-1, 1]) translate([x*(L/2 - 6), y*(W/2 - 6), -1]) cylinder(d = 2.5, h = floor_t + 10);
}
for (x = [-1, 1], y = [-1, 1]) translate([x*(L/2 - 6), y*(W/2 - 6), floor_t]) difference() { cylinder(d = 6, h = 6); cylinder(d = 2.5, h = 7); }
```
Commands and output (scratch dir, 2026-09-25):
```
OS=/Applications/OpenSCAD-2021.01.app/Contents/MacOS/OpenSCAD
$OS -o shell.stl shell.scad          # Facets: 859, Volumes: 2; 9.8 s user (CGAL); 501 KB ASCII STL
$OS -o shell.3mf shell.scad          # 37 KB 3MF
$OS -o shell.csg shell.scad          # 2.4 KB CSG tree (difference/group/linear_extrude/offset/square/multmatrix ...)
$OS -o shell_preview.png --imgsize=1200,800 --autocenter --viewall --projection=p --colorscheme=Tomorrow shell.scad   # 0.17 s
$OS -o shell_render.png --render --imgsize=1200,800 --camera=0,0,0,55,0,25,300 --projection=p shell.scad
```
The render PNG shows the pocketed shell with R4 outer corners, R2 pocket corners and four bosses, as designed. Confidence: High.

**B3. Mesh-to-STEP is not an acceptable CNC path: PCBWay refuses it (A1), and the only tool route (FreeCAD Part ShapeFromMesh) yields one planar face per triangle with no analytic cylinders or planes.**
FreeCAD's ShapeFromMesh converts a mesh face-by-face and usually needs sewing, Part MakeSolid and Part RefineShape afterwards (https://raw.githubusercontent.com/FreeCAD/FreeCAD-documentation/main/wiki/Part_ShapeFromMesh.md). The result carries no hole, cylinder or plane definitions for CAM feature recognition, cannot be dimensioned to ISO 2768 unambiguously, and is bloated (the 859-facet test shell is already 0.5 MB as ASCII STL). Tessellation error itself is small at $fn=64 (chord sagitta r(1-cos(180/n)): 0.0015 mm on a 2.5 mm tap drill, 0.0036 mm on a 6 mm boss) but the loss of topology is the disqualifier, as PCBWay states. Confidence: High.

**B4. FreeCAD's OpenSCAD workbench builds true B-rep solids from the CSG tree for the constructs the enclosure needs; hull, minkowski, text and mesh import fall back to triangulated geometry.**
From `src/Mod/OpenSCAD/importCSG.py` (https://raw.githubusercontent.com/FreeCAD/FreeCAD/main/src/Mod/OpenSCAD/importCSG.py): cube -> Part::Box; sphere -> Part::Sphere; cylinder -> Part::Cylinder or Part::Cone (a Part::Prism polygon only when $fn is below the `useMaxFN` threshold, default 16); polyhedron -> shell and solid; union -> Part::Fuse/MultiFuse; difference -> Part::Cut; intersection -> Part::Common/MultiCommon; multmatrix -> Placement, Part::Mirroring or transformGeometry; linear_extrude -> Part::Extrusion (twist/scale via a FeaturePython); rotate_extrude -> Part::Revolution; offset -> Part::Offset2D/Offset; resize -> transformGeometry; color, render, group pass through. hull and minkowski go through `CGALFeatureObj`, and the workbench doc says "Currently we run the OpenSCAD binary in order to perform hull and minkowski operations and import the result. This means that the involved geometry will be triangulated" (https://raw.githubusercontent.com/FreeCAD/FreeCAD-documentation/main/wiki/OpenSCAD_Workbench.md). text is rendered by OpenSCAD to DXF; import of STL/OFF stays a mesh; projection(cut=false), surface and other CGAL ops are unsupported. Non-uniform scaling converts primitives "to BSpline prior to performing such deformations. Those BSplines are known to cause trouble in later boolean operations" (same page). `open()`/`insert()` accept `.csg` directly, and for `.scad` call `callopenscad()` to generate the CSG first. The OpenSCAD executable is read from parameter group `User parameter:BaseApp/Preferences/Mod/OpenSCAD`, key `openscadexecutable`; `callopenscad()` runs `openscad -o out.csg in.scad`; other keys: `fnForImport` (default 32), `transfermechanism`, `useMultmatrixFeature`, `useViewProviderTree`, `usePlaceholderForUnsupported` (https://raw.githubusercontent.com/FreeCAD/FreeCAD/main/src/Mod/OpenSCAD/OpenSCADUtils.py). Confidence: High (source-derived).

**B5. FreeCAD 1.1.3 for macOS is on Homebrew as a cask and ships a headless binary inside the bundle.**
`brew info --cask freecad` reports "freecad (FreeCAD): 1.1.3 ... Not installed" (local command). The bundle script copies `freecad`, `freecadcmd`, `python` and `pip` into `FreeCAD.app/Contents/Resources/bin/` and installs the launcher at `FreeCAD.app/Contents/MacOS/FreeCAD`; the build self-tests with `"${conda_env}/bin/freecadcmd" --safe-mode --version` (https://raw.githubusercontent.com/FreeCAD/FreeCAD/main/package/bundle/osx/create_bundle.sh, lines 6, 53-57, 82-83, 116). Headless scripting: `FreeCADCmd /path/to/script.py`, or `FreeCAD -c`; a script can `Part.export([obj], "file.step")` (https://raw.githubusercontent.com/FreeCAD/FreeCAD-documentation/main/wiki/Start_up_and_Configuration.md, https://reqrefusion.github.io/FreeCAD-Documentation-html/wiki/Headless_FreeCAD.html). STEP export preferences offer AP203, AP214 and AP242 schemes, units, "Write out curves in parametric space of surface", and header Company/Author/Product fields (https://reqrefusion.github.io/FreeCAD-Documentation-html/wiki/Import_Export_Preferences.html). Confidence: High for paths (source-derived); the script below is untested here.

**B6. CadQuery and build123d are current, pip-installable OCCT front ends that export STEP, STL and 3MF from one Python source.**
CadQuery 2.8.0 (2026-06-21, Python >= 3.11, `pip install cadquery`) exports STEP, STL, 3MF, AMF, DXF, SVG, glTF with `tolerance` and `angularTolerance` controls and STEP `unit`/`outputUnit` options (https://pypi.org/project/cadquery/, https://cadquery.readthedocs.io/en/latest/importexport.html). build123d 0.13.0 (2026-09-21, Python >= 3.11, < 3.15, `pip install build123d`) provides `export_step()`, `export_stl()`, `export_brep()`, `Mesher().write()` for 3MF, `ExportSVG` (https://pypi.org/project/build123d/, https://build123d.readthedocs.io/en/latest/import_export.html). Both need `cadquery-ocp` wheels (Apple Silicon wheels exist). Confidence: High.

**B7. Bambu Studio 02.08.02.61 is installed with H2C system presets; the CLI produces H2C project 3MF files from an STL, but headless slicing fails on the H2C's dual-extruder filament mapping in every variant tried.**
CLI usage per https://github.com/bambulab/BambuStudio/wiki/Command-Line-Usage and local `--help`: `--load-settings "machine.json;process.json"`, `--load-filaments`, `--arrange`, `--orient`, `--slice 0`, `--export-3mf`, `--export-png`, `--outputdir`. Presets on this Mac: `~/Library/Application Support/BambuStudio/system/BBL/machine/Bambu Lab H2C 0.4 nozzle.json` (printer_model "Bambu Lab H2C", default_print_profile "0.20mm Standard @BBL H2C", printable_area 330 x 320 mm with per-extruder 325 x 320 mm areas), `process/0.20mm Standard @BBL H2C.json`, `filament/Bambu PLA Basic @BBL H2C.json`. Trials:
```
BS=/Applications/BambuStudio.app/Contents/MacOS/BambuStudio
P="$HOME/Library/Application Support/BambuStudio/system/BBL"
$BS --export-3mf shell_plain.3mf --outputdir "$PWD" shell.stl                       # OK: 53 KB project 3MF
$BS --load-settings "$P/machine/Bambu Lab H2C 0.4 nozzle.json;$P/process/0.20mm Standard @BBL H2C.json" \
    --load-filaments "$P/filament/Bambu PLA Basic @BBL H2C.json;$P/filament/Bambu PLA Basic @BBL H2C.json" \
    --arrange 1 --export-3mf shell_h2c_project.3mf --outputdir "$PWD" shell.stl     # OK: project_settings.config has printer_model "Bambu Lab H2C", print_settings_id "0.20mm Standard @BBL H2C"
# adding --slice 0 (with 1 or 2 filaments, --load-filament-ids "1", --load-defaultfila 1, or a process copy with
# filament_map_mode "manual") fails every time with:
#   [error] plate 1 : some filaments can not be mapped under auto mode for multi extruder printer
```
OpenSCAD's own `-o shell.3mf` (B2) is also a valid Bambu Studio input; Bambu Studio imports 3MF, STL, STEP, OBJ and more (https://wiki.bambulab.com/en/software/bambu-studio/step). H2C build volume is 325 x 320 x 325 mm single-nozzle and 300 x 320 x 320 mm dual-nozzle per https://bambulab.com/en/h2c/specs (page blocks fetch; value from search excerpt and consistent with the local preset). Confidence: High for the CLI results (reproduced); Medium for the build volume.

### Recommended pipeline (exact commands)

Design rule for the OpenSCAD source (so that FreeCAD produces analytic B-rep): use only cube, cylinder, sphere, square, circle, polygon, linear_extrude, rotate_extrude, offset, union, difference, intersection, translate, rotate, mirror, uniform scale; set `$fn >= 32` on every round feature (above the `useMaxFN` prism threshold, gives true cylinders and arcs); do not use hull, minkowski, text, import, resize, non-uniform scale, projection or surface in the production enclosure file (put decorative text on the 2D drawing as SVG for laser marking instead).

Step 1, review renders (works today with 2021.01; identical flags on snapshots):
```
OS=/Applications/OpenSCAD-2021.01.app/Contents/MacOS/OpenSCAD   # or: brew install --cask openscad@snapshot; OS=/Applications/OpenSCAD.app/Contents/MacOS/OpenSCAD
for v in "55,0,25" "55,0,115" "55,0,205" "55,0,295" "0,0,0" "90,0,0"; do
  $OS -o render_${v//,/_}.png --render --imgsize=1600,1000 --projection=p --camera=0,0,0,$v,320 --colorscheme=Tomorrow enclosure.scad
done
```
Attach the PNGs to the review package (charter 11.3).

Step 2, CSG tree and mesh outputs from the same source:
```
$OS -o enclosure.csg enclosure.scad
$OS -o enclosure.3mf enclosure.scad                          # Bambu Studio fit-check input
$OS -o enclosure.stl --export-format binstl enclosure.scad   # binary STL for PCBWay SLA or volume cross-check
```

Step 3, headless FreeCAD: CSG to STEP (install `brew install --cask freecad`, then run; untested on this machine):
```
FCC=/Applications/FreeCAD.app/Contents/Resources/bin/freecadcmd
$FCC "$PWD/scad2step.py"
```
`scad2step.py`:
```python
import os, sys, FreeCAD, Part, importCSG
src = os.path.abspath("enclosure.csg"); out = os.path.abspath("enclosure.step")
p = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/OpenSCAD")
p.SetString("openscadexecutable", "/Applications/OpenSCAD-2021.01.app/Contents/MacOS/OpenSCAD")
p.SetBool("usePlaceholderForUnsupported", False)   # fail loudly instead of inserting placeholders
doc = FreeCAD.newDocument("enclosure")
importCSG.insert(src, doc.Name)
doc.recompute()
roots = [o for o in doc.Objects if hasattr(o, "Shape") and not o.InList]   # top-level result(s)
assert len(roots) == 1, "expected one top-level solid, got %d" % len(roots)
shape = roots[0].Shape.removeSplitter()                                     # refine coplanar faces
if shape.ShapeType == "Compound" and len(shape.Solids) == 1:               # FreeCAD 1.1.3 returns Part::Cut as a one-solid Compound
    shape = shape.Solids[0]                                                  # correction 2026-09-26, lock section 1.4 item 4
assert shape.isValid() and shape.ShapeType in ("Solid", "CompSolid"), "invalid or non-solid result"
assert len(shape.Solids) == 1, "STEP must contain exactly one solid for CNC"
faces = [f.Surface.__class__.__name__ for f in shape.Faces]
assert "BSplineSurface" not in faces, "BSpline faces present; check for non-uniform scale/resize"
print("volume mm^3:", round(shape.Volume, 2), "faces:", len(faces), "cylinders:", faces.count("Cylinder"))
feat = doc.addObject("Part::Feature", "EnclosureRefined"); feat.Shape = shape; doc.recompute()
Part.export([feat], out)                                                    # scheme AP214/AP242 per FreeCAD Import-Export preferences
print("wrote", out)
```

**Correction 2026-09-26 (integrator; tools/toolchain.lock.md section 1.4 item 4; evidence `docs/cm/tool-validation/evidence/openscad-freecad-2026-09-25-listing-run2.py`).** FreeCAD 1.1.3 returns the OpenSCAD `Part::Cut` result as a `Compound` holding exactly one `Solid`, which the original assertion rejected on a correct result; the listing now unwraps it. `freecadcmd` exits 0 even when the script raises, so the caller checks a success marker (the `wrote` line) and the STEP file, never the exit status. OpenSCAD resolves a relative `-o` path against the input file's directory, so every export names an absolute output path (lock section 1.4 item 3).
Acceptance checks recorded with the STEP: `isValid()`, exactly one solid, no BSpline faces, and STEP volume within 0.5 % of the STL mesh volume (compute the mesh volume with a five-line numpy divergence sum over the binary STL). These become Inspection evidence for the CAD requirement.

Step 4, fit-check on the H2C: open `enclosure.3mf` (or `enclosure.step`) in Bambu Studio, pick "Bambu Lab H2C 0.4 nozzle" and "0.20mm Standard @BBL H2C", slice and print. The CLI-produced project file `enclosure_h2c_project.3mf` (B7) can be generated for archival, but slicing is done in the GUI until the CLI mapping issue is resolved (open item).

Step 5, PCBWay order package: `enclosure.step` (AP214 or AP242), a PDF drawing with critical dimensions, thread callouts (for example "4x M3x0.5 - 6H, depth 6, tap before anodize or mask"), roughness, marking placement and racking location; SVG artwork for laser marking; order options aluminum 6061, bead blast plus anodize (color of choice), CMM inspection report if the mounting pattern carries a +/-0.1 mm callout.

Alternative (DECISION-needed): author the enclosure directly in build123d. One Python file then yields `export_step()`, `export_stl()`, `Mesher().write("x.3mf")` and `ExportSVG` with no FreeCAD stage, and geometry is analytic B-rep from the start. Cost: the source is no longer OpenSCAD; a `.venv` install of build123d is needed (assignment did not authorize it for this agent).

## Implications for cwht

- REQ-candidate (ME): The enclosure design data package shall consist of a single-solid STEP AP214 or AP242 B-rep file per machined part, a 2D drawing (PDF) carrying every toleranced dimension, thread, roughness, marking and racking callout, and SVG artwork for laser marking; STL or mesh-derived STEP shall not be submitted for CNC. Basis A1, A2, B3.
- REQ-candidate (ME): Internal pocket corners shall have radius >= 1.3x the intended cutter radius and >= one third of the pocket depth (project default R3 for pockets deeper than 6 mm, R2 minimum elsewhere); pocket depth-to-width <= 4; minimum wall 1.5 mm (margin over PCBWay's 0.8 mm); drilled depth <= 10x diameter; slot widths from {3, 4, 6, 8, 10, 12} mm. Basis A6.
- REQ-candidate (ME): Threaded features shall be modeled as tap-drill pilot holes (M3: 2.5 mm) with engagement 1.0-1.5x nominal and blind-hole drill depth >= thread depth + 3 pitches; threads shall be masked during anodize or tapped after; the drawing shall list every thread. Basis A7.
- REQ-candidate (ME/RF): Chassis ground and RF connector contact areas shall be masked from anodize or otherwise left conductive (anodize is an insulator), and the masked areas shall be shown on the drawing. Basis A4 and the transceiver's need for a low-impedance chassis ground (design fact, not a PCBWay statement).
- REQ-candidate (ME): Dimensions affecting PCB mounting, display window and connector positions shall carry explicit tolerances (+/-0.1 mm class f equivalents) on the drawing; all other dimensions default to ISO 2768-m. Basis A5.
- REQ-candidate (SW/tooling): The CAD build shall be reproducible from the command line: render PNGs, CSG, 3MF and STEP generated by a script with recorded tool versions, and STEP acceptance checks (valid, one solid, no BSpline faces, volume match) run and logged. Basis B2, B4, B5, charter 11.3.
- DECISION-needed: Alloy 6061 with bead blast plus Type II anodize (recommended; 7075 offers no benefit for a handheld and anodizes unevenly; 6063 not offered). Basis A3, A4.
- DECISION-needed: Keep OpenSCAD as the source with the restricted dialect plus FreeCAD headless STEP stage, or move the enclosure to build123d. Recommendation: prototype both on the smoke-test shell at PDR and choose on STEP quality and effort; record as an ADR. Basis B4, B6.
- DECISION-needed: Whether a PCBWay SLA print of the final STEP is ordered before the aluminum order (about 1 day plus shipping, 0.8 mm minimum wall) or whether H2C FDM prints are the sole fit-check. Recommendation: H2C prints for every iteration, one SLA print of the CDR-baselined STEP only if a +/-0.2 mm fit matters (display bezel, connector cutouts). Basis A11, B7.
- RISK-candidate: Anodize color and rack marks vary; the cosmetic outcome is not controllable through the quote. Mitigation: specify racking location on a non-visible face, accept color variation in the requirement wording.
- RISK-candidate: PCBWay's published tolerance statements conflict (+/-0.125 mm headline vs ISO 2768-m default up to +/-0.3 mm at 30-120 mm); an undocumented assumption could leave PCB mounting holes out of tolerance. Mitigation: explicit callouts and a CMM report on the mounting pattern.
- RISK-candidate: Small threads (M2, M2.5) may be rejected or added at cost; PCBWay recommends M6 or larger and warns below M2. Mitigation: M3 minimum in aluminum, helicoil option noted on the drawing.
- RISK-candidate: FreeCAD import fidelity: any hull/minkowski/text/resize in the source silently degrades to mesh or BSpline; the scad2step acceptance checks are the control.
- RISK-candidate: Toolchain age: OpenSCAD 2021.01 is the installed build and its Homebrew cask is disabled (Gatekeeper); the snapshot line changes behavior (Manifold default) and can carry 3MF export regressions. Mitigation: pin the exact OpenSCAD build in the CM plan; STEP is produced from CSG, which is stable across versions.
- RISK-candidate: Headless slicing for the H2C fails from the Bambu Studio CLI; the fit-check print therefore has a manual GUI step that is not fully reproducible from a script.
- ACTION: Owner to install FreeCAD 1.1.3 (`brew install --cask freecad`) and, if the build123d path is to be evaluated, authorize `pip install build123d` into `.venv`; then run `scad2step.py` on the smoke-test shell and record the acceptance checks.
- ACTION: Upload the first STEP to PCBWay's instant quote at PDR (aluminum 6061, bead blast plus anodize, quantity 1 and 2) to seed the cost and lead-time TPMs; ask PCBWay 3dcnc@pcbway.com for Type II thickness, masking practice and whether M3 tapping in 6061 is standard.
- ACTION: Resolve or waive Bambu Studio CLI slicing for the H2C (open item) and record the chosen procedure in the fit-check test procedure.

## Confidence

| Finding | Confidence | Basis |
|---|---|---|
| A1 formats, STL refusal | High | PCBWay FAQ, ordering guide, 2024 article |
| A2 drawing requirement | High | PCBWay ordering guide, laser page |
| A3 alloys | High (menu) / Medium (7075 anodize) | PCBWay pages; third-party vendor |
| A4 finishes | High | PCBWay milling and finish pages |
| A5 tolerances | High (published) / Medium (interaction) | PCBWay help center 2026-07-13 |
| A6 DFM rules | High (quotes) / Medium (R0.5 at 3 mm) | PCBWay articles 2021-2026 |
| A7 threads | High (modeling) / Medium (inserts) | PCBWay tapping guide |
| A8 marking | High (PCBWay) / Low (third-party sizes) | PCBWay guide 2026-07-21 |
| A9 counterbores | High | PCBWay article 2026-09-07 |
| A10 pricing, lead time | Medium | Third-party 2023 orders, PCBWay FAQ |
| A11 3D printing | High | PCBWay pages |
| B1 OpenSCAD status | High | Local help output, openscad.org, mailing list, brew |
| B2 local exports | High | Reproduced, render inspected |
| B3 mesh-to-STEP | High | PCBWay article, FreeCAD docs |
| B4 FreeCAD CSG import | High | FreeCAD source and docs |
| B5 FreeCAD macOS headless | High (paths) / Medium (script, untested) | Packaging script, docs |
| B6 CadQuery/build123d | High | PyPI, docs |
| B7 Bambu CLI | High (trials) / Medium (build volume) | Reproduced locally; vendor spec blocked |

## Open items

1. Bambu Studio CLI slicing for the H2C: find the correct filament mapping flags or process keys (the error "some filaments can not be mapped under auto mode for multi extruder printer" persisted with two filaments, `--load-filament-ids`, `--load-defaultfila` and a manual `filament_map` in a process copy); alternative is to slice in the GUI and archive the resulting `.gcode.3mf`.
2. FreeCAD `scad2step.py` is written against source and docs but has not been executed here (FreeCAD not installed); first run must confirm `importCSG.insert` behavior with the `offset()` rounded rectangles and the `Part.export` scheme preference (set AP242 or AP214 in the Import-Export preferences or via the `Mod/Import/hSTEP` parameter group).
3. PCBWay's Type II anodize thickness, masking practice for tapped holes and RF contact pads, and whether the "Features" tab covers helicoil inserts for CNC parts: confirm by email or a trial quote.
4. Exact numeric minimum internal radius table in the PCBWay corner-radius article is an image; the R0.5 at <= 3 mm depth figure comes from a search excerpt and should be confirmed on the page.
5. H2C build-volume page blocked automated fetch; value taken from the vendor search excerpt and the local preset.
6. Third-party pricing data are from 2023; a live PCBWay quote at PDR is the only reliable cost signal.
