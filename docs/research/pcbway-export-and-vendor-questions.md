# PCBWay export recipe (kicad-cli 10.0.6), PA thermal DFM, vendor confirmation email, and the build-quantity decision

**Assignment key:** pcbway-export  
**Date of research:** 2026-09-25  
**Author:** Claude (research subagent)  
**Status:** Research input to PDR/CDR; not a baseline. Candidate requirements go through the CR process (charter section 11, rule 5) before entering the requirements set.  
**Extends:** `pcbway-fabrication-and-assembly.md` (cited below as PCBWAY-FAB F1..F23, its CDR checklist and actions A-PCB-01..05) and `verification-tooling-inventory.md` (cited as TOOLS F1..F13). Nothing from those reports is repeated except where a number is needed inline.

## Question

1. Produce the exact `kicad-cli` 10.0.6 command lines that generate a PCBWay-compatible fabrication and assembly package: Gerber layer set, KiCad or Protel file extensions, X2 attributes on or off with the reason, Excellon PTH/NPTH drill files with the map, a centroid (CPL) CSV in the form PCBWay expects (units, origin, side, rotation convention) and the BOM export. Run them on a small known-answer board built with the KiCad-bundled Python (pcbnew SWIG), list the resulting file names and check them against PCBWay's recognized names.
2. Add the PA thermal DFM section the critic asked for: thermal via count and drill for the PA package candidates (no `pa-device-candidates.md` exists, so the RD07MUS2B and AFT05MS006N packages named in `2m-cw-transceiver-reference-designs.md` F22/F24 are used), PCBWay resin-filled via-in-pad and cap-plating options with cost signals, copper pour to an enclosure contact, and the flatness a thermal pad needs.
3. Draft the vendor confirmation email covering: reflow of a castellated Pico 2 module in turnkey assembly and its handling, the Dk test frequency of the 7628 prepreg, the CPL zero-degree rotation reference and a placement preview, impedance testing on a 5-piece order, anodize masking of tapped holes and ground pads on CNC parts, and helicoil availability.
4. State the build-quantity constraint (fabrication minimum 5; 47 CFR 15.23 five-unit personal-use limit for the digital section) as a decision for the owner with a recommendation.

## Method

1. Read charter section 11, PCBWAY-FAB (all findings, checklist, actions and open items 1 to 9) and TOOLS F1 to F10 (kicad-cli command tree, bundled Python 3.9.13 with pcbnew 10.0.6, library-table recipe).
2. Ran `kicad-cli pcb export gerbers -h`, `pcb export drill -h`, `pcb export pos -h`, `sch export bom -h` on `/Applications/KiCad/KiCad.app/Contents/MacOS/kicad-cli` (10.0.6, arm64) and recorded every option and default. Confirmed the defaults against the KiCad 10.0 CLI manual (https://docs.kicad.org/10.0/en/cli/cli.html, fetched 2026-09-25).
3. Wrote `make_ka_board.py` (pcbnew SWIG, run under KiCad's Python 3.9.13) that builds an 80 x 40 mm 4-layer board with: the official `Module:RaspberryPi_Pico_SMD_HandSolder` footprint (Pico 2 stand-in, 86 SMD pads plus 4 NPTH mounting holes), two 0603 resistors at 0 and 90 degrees, one 0402 capacitor on the bottom at 270 degrees, one DNP 0603, one SOT-89 at 180 degrees, one QFN-16 with exposed pad and four 0.3 mm thermal vias, one 1x3 THT header, one M3 NPTH mounting hole, a track, GND/VCC zones on In1/In2/B.Cu, TOP/BOT copper labels, silkscreen text, and the drill/place (aux) origin at the board's lower-left corner. Saved as `ka.kicad_pcb` in the session scratch directory (`.../scratchpad/pcbway_export/ka/`). Two API notes: `FOOTPRINT.SetLayerAndFlip()` segfaults on a footprint not yet added to a board; add first, then `Flip(pos, FLIP_DIRECTION_TOP_BOTTOM)`.
4. Ran the export commands in Findings 1 to 5 on that board, inspected file names, Gerber and Excellon headers, the job file, the drill report, and the CPL and BOM contents; rendered the board top and bottom with `kicad-cli pcb render` to PNG and inspected the images (charter rule 3). Ran `kicad-cli pcb drc` on the fixture for completeness (22 violations, all fixture artefacts such as courtyard overlaps and copper-to-edge; irrelevant to the export test).
5. Wrote a minimal `ka.kicad_sch` (schematic version 20250114, inline lib symbols, custom fields Manufacturer, MPN, Type, Description; one DNP symbol) plus `ka.kicad_pro`, exported the BOM with `kicad-cli sch export bom` in PCBWay's template column order, and cross-checked BOM designators against the CPL with a 12-line Python script.
6. Fetched PCBWay primary pages: via covering, via-in-pad (product and ordering-parameter pages), via filled with copper, capabilities table, extra-cost list, the online order form, impedance control, the KiCad Gerber and position-file help pages (current and legacy), the stackup library, the bow-and-twist article, the tapping/thread-insert page. Fetched the KiCad forum thread on PCBWay and X2 (2019).
7. Downloaded the Mitsubishi RD07MUS2B datasheet (G2K-Si-240116-1, Jan 2024) and rendered page 1 to PNG to read the outline drawing; downloaded NXP AN4005 (Rev 0, 11/1997) and the AFT05MS006N datasheet (Rev 0, 2/2014; NXP blocks plain curl, the fetch tool saved the PDF) and rendered pages 18 to 20 (pad layout, package outline) to PNG; extracted text with `pdftotext -layout` and counted the Figure 21 via array on a 300 dpi crop.
8. Computed thermal-via array resistances, TIM resistances and a junction-temperature budget with a short Python script (formulas and inputs stated with each number).
9. Pulled 47 CFR 15.23 and 2.803 from the eCFR versioner API at issue date 2026-09-23: `curl -sL --compressed "https://www.ecfr.gov/api/versioner/v1/full/2026-09-23/title-47.xml?part=15&section=15.23"` (and `part=2&section=2.803`), stripped tags with Python; version history from `.../versions/title-47.json?part=15&section=15.23` (last amended 2016-12-15).
10. The web-search budget of this session ran out before the KiCad Library Convention zero-rotation rule could be quoted; that item is carried as an open item and asked in the email.

Scratch files (not part of the repo): `.../scratchpad/pcbway_export/ka/` (`make_ka_board.py`, `ka.kicad_pcb`, `ka.kicad_sch`, `ka.kicad_pro`, `out_kicad/`, `out_protel/`, `out_default/`, `out_drill/`, `out_drill_legacy/`, `out_pos/`, `out_bom/`, `ka-gerbers-kicad.zip`, `ka-gerbers-protel.zip`, `ka-top.png`, `ka-bottom.png`, `ka_drc.json`), `.../scratchpad/pcbway_export/ds/` (datasheets, AN4005, page renders), `.../scratchpad/pcbway_export/ecfr/` (15.23, 2.803, 2.1 XML).

## Findings

### Part 1. kicad-cli 10.0.6 export recipe, verified on the known-answer board

**F1. kicad-cli defaults differ from the GUI and from what PCBWay wants; every relevant option must be passed explicitly.** From `-h` output on 10.0.6 and the 10.0 CLI manual: Gerbers default to X2 on (`--no-x2` disables), Protel extensions on (`--no-protel-ext` gives `.gbr`), netlist attributes on (`--no-netlist`), precision 6, and with no `--layers` argument all 26 enabled layers are plotted (observed: F/B Adhesive, Courtyard, Fab, User_1..4, Eco1/2, Margin, Comments, Drawings in addition to the copper, mask, paste, silk and outline files). Drill defaults: `excellon`, `--drill-origin absolute`, zeros `decimal`, units `mm`, and `--excellon-oval-format alternate` (the GUI default and the KiCad manual's "correct for most manufacturers" choice is `route`, PCBWAY-FAB F3); PTH and NPTH are merged unless `--excellon-separate-th` is given. Position defaults: `ascii`, `in`, `both` sides, absolute origin. BOM default fields `Reference,Value,Footprint,QUANTITY,DNP`.  
Sources: local `kicad-cli ... -h` (Method 2); https://docs.kicad.org/10.0/en/cli/cli.html ("X2 format is enabled by default", "Options are `in` (default) or `mm`").

**F2. Layer names on the command line are the untranslated KiCad names with dots; a wrong name is only a warning and the exit code stays 0.** `-l ...,Edge_Cuts` printed `Invalid layer name 'Edge_Cuts'`, skipped the outline and exited 0; `Edge.Cuts` works. Since a missing outline is PCBWay's most common rejection (PCBWAY-FAB F1), the wrapper must grep stderr for `Invalid layer name` and count the output files (expect 11 Gerbers plus the job file).  
Source: local run (Method 4).

**F3. Recommended Gerber command (KiCad names, X2 off) and its output.**
```
KICAD_CLI=/Applications/KiCad/KiCad.app/Contents/MacOS/kicad-cli
LAYERS="F.Cu,In1.Cu,In2.Cu,B.Cu,F.Mask,B.Mask,F.Silkscreen,B.Silkscreen,F.Paste,B.Paste,Edge.Cuts"
"$KICAD_CLI" pcb export gerbers -o out/gerbers/ -l "$LAYERS" \
    --no-x2 --no-netlist --no-protel-ext --use-drill-file-origin \
    --subtract-soldermask --check-zones --precision 6 cwht.kicad_pcb
```
Output on the fixture (prefix is the board file basename): `ka-F_Cu.gbr ka-In1_Cu.gbr ka-In2_Cu.gbr ka-B_Cu.gbr ka-F_Mask.gbr ka-B_Mask.gbr ka-F_Silkscreen.gbr ka-B_Silkscreen.gbr ka-F_Paste.gbr ka-B_Paste.gbr ka-Edge_Cuts.gbr ka-job.gbrjob` (12 files, 141 kB of Gerber). The job file is always written by kicad-cli (there is no flag); it carried `LayerNumber: 4`, `BoardThickness: 1.6`, `Size 80.1 x 40.1`, 13 material-stackup entries and `Finish: "None"` because the fixture has no board-setup stackup; the real board must have its stackup and finish (ENIG) entered in Board Setup so the job file states them (PCBWAY-FAB F4 relies on it).  
Header of `ka-F_Cu.gbr` with `--no-x2`: no `%TF` lines at all (0), but 40 `G04 #@!` attribute-comment lines (TF, TA and TD, for example `G04 #@! TF.FileFunction,Copper,L1,Top*`), that is the same attributes carried as standard RS-274X comments, plus `%FSLAX46Y46*%`, `%MOMM*%`. `--no-netlist` removed every `TO.N` net attribute (16 in the default output, 0 here). Five `%AM` aperture macros remain (rounded-rectangle pads); `--disable-aperture-macros` exists if PCBWay ever asks (the KiCad manual says use it only on request, PCBWAY-FAB F3). Coordinates with `--use-drill-file-origin`: the outline runs `X0Y40000000` to `X80000000Y40000000`, so the lower-left corner is (0,0) and Y is up, matching the drill and position files.  
Source: local run (Method 4).

**F4. Protel-extension variant.** Same command without `--no-protel-ext` gives `ka-F_Cu.gtl ka-In1_Cu.g1 ka-In2_Cu.g2 ka-B_Cu.gbl ka-F_Mask.gts ka-B_Mask.gbs ka-F_Silkscreen.gto ka-B_Silkscreen.gbo ka-F_Paste.gtp ka-B_Paste.gbp ka-Edge_Cuts.gm1 ka-job.gbrjob`. Both naming styles are recognized by PCBWay (PCBWAY-FAB F2); the KiCad names are recommended for cwht because PCBWay's extension table lists the KiCad names verbatim (`F_Cu.gbr`, ..., `Edge_Cuts.gbr`, `PTH.drl`, `NPTH.drl`) and because they are self-describing in a review package. Inner layers `In1_Cu.gbr`/`In2_Cu.gbr` are not on PCBWay's table (Medium; PCBWAY-FAB open item 4; asked in the email).  
Source: local run; https://www.pcbway.com/helpcenter/technical_support/Gerber_File_Extension_from_Different_Software.html (via PCBWAY-FAB F2).

**F5. X2 must be off; reason.** PCBWay's own KiCad Gerber instructions (legacy help page, still live): "Do NOT check 'Use extended X2 format', otherwise, the format will not be accpeted [sic]" and "please do NOT check the 'Include extended attributes' before Plot"; the same page tells KiCad users to select "Suppress leading zeros" and "Minimal header" for the drill file. A KiCad forum thread (2019-12-27, KiCad 5.1.5): "I've just resubmitted a job to PCBWay and can confirm that they don't handle extended attributes (X2)." PCBWay's newer KiCad 8 page gives its settings only as screenshots the fetch tool could not read. With `--no-x2`, KiCad writes X1 files whose attributes are embedded as `G04 #@!` comments, which is the Gerber specification's X1-compatible carrier and is ignored by any RS-274X reader; this is the form PCBWay has accepted from KiCad 5 onward.  
Sources: https://www.pcbway.com/blog/help_center/Generate_Gerber_file_from_Kicad.html ; https://forum.kicad.info/t/pcbway-cannot-read-kicad-gerber-file-solved/20420 ; https://www.pcbway.com/helpcenter/technical_support/Generate_Gerber_file_from_Kicad.html (KiCad 8 version).

**F6. Recommended drill command and output.**
```
"$KICAD_CLI" pcb export drill -o out/gerbers/ --format excellon --drill-origin plot \
    --excellon-units mm --excellon-zeros-format decimal --excellon-oval-format route \
    --excellon-separate-th --generate-map --map-format pdf \
    --generate-report --report-path out/gerbers/cwht-drill-report.rpt cwht.kicad_pcb
```
Output: `ka-PTH.drl ka-NPTH.drl ka-PTH-drl_map.pdf ka-NPTH-drl_map.pdf ka-drill-report.rpt`. PTH header: `M48 / ; FORMAT={-:-/ absolute / metric / decimal} / FMAT,2 / METRIC / T1C0.300 / T2C1.000`, coordinates like `X39.5Y6.5` (the QFN via at KiCad (39.5, 33.5) mm, referred to the lower-left origin because `--drill-origin plot` uses the aux origin). Attributes again appear only as `; #@! TF...` comments. The report listed PTH T1 0.300 mm x 4 (thermal vias), T2 1.000 mm x 3 (header), NPTH 1.85 mm x 2 and 2.20 mm x 2 (the Pico footprint's mounting holes) and 3.20 mm x 1 (H1); total 7 plated, 5 unplated. `--drill-origin plot` must be used together with `--use-drill-file-origin` on the Gerbers and the position file so all three share one origin.  
Legacy variant matching PCBWay's KiCad-5 instruction (`--excellon-zeros-format suppressleading --excellon-min-header`) gives `M48 / METRIC,TZ / T1C0.300 ... X39500Y6500`, that is 3.3 format with leading zeros suppressed. Both are valid Excellon; the decimal form is unambiguous and is the KiCad 6+ default, so it is recommended, with the legacy form kept in the wrapper as a fallback. Asked in the email (item 7).  
Source: local run (Method 4); https://www.pcbway.com/blog/help_center/Generate_Gerber_file_from_Kicad.html.

**F7. Recommended position (CPL) command and the two traps it avoids.**
```
"$KICAD_CLI" pcb export pos -o out/assembly/cwht-cpl.csv --format csv --units mm \
    --use-drill-file-origin --side both --smd-only --exclude-dnp cwht.kicad_pcb
```
Output (fixture):
```
Ref,Val,Package,PosX,PosY,Rot,Side
"C1","100n","C_0402_1005Metric",14.000000,8.000000,-90.000000,bottom
"Q1","PA","SOT-89-3",26.000000,7.000000,180.000000,top
"R1","10k","R_0603_1608Metric",6.000000,8.000000,0.000000,top
"R2","10k","R_0603_1608Metric",10.000000,8.000000,90.000000,top
"U1","Pico2","RaspberryPi_Pico_SMD_HandSolder",40.000000,26.000000,0.000000,top
"U2","MMIC","QFN-16-1EP_3x3mm_P0.5mm_EP1.7x1.7mm",40.000000,6.000000,0.000000,top
```
Properties: units mm, six decimals, origin lower-left with Y up (R1 placed at KiCad (6, 32) on a 40 mm tall board reports (6, 8)), side column `top`/`bottom`, both sides in one file, bottom-side X not negated (PCBWay's sample shows positive coordinates on both sides, "top point of view", PCBWAY-FAB F12; `--bottom-negate-x` gave `-14.000000` for C1 and must not be used), rotation is the footprint's stored orientation normalized to (-180, 180]: C1 set to 270 degrees reports `-90.000000`. PCBWay's sample uses 0 to 360 (both 0 and 360 appear, PCBWAY-FAB F12); a post-processing step `rot = rot mod 360` makes the file look like the sample and is harmless.  
Trap 1: `--exclude-fp-th` drops the Pico module. The official Pico footprint has the SMD attribute (`FP_SMD = 2`) but contains 4 NPTH mounting-hole pads, so `--exclude-fp-th` removed U1 (output: C1, Q1, R1, R2, U2 only) while `--smd-only` kept it. Use `--smd-only`, never `--exclude-fp-th`, on any board carrying the Pico. The THT header J1 and the mounting hole H1 (attributes `exclude from position files` and `exclude from BOM`, value 12) are dropped either way; R3 (DNP) is dropped by `--exclude-dnp`.  
Trap 2: without `--units mm --use-drill-file-origin` the default output is inches from the page origin with negative Y (`C1 ... 0.551181,-1.259843`).  
Source: local run (Method 4); https://www.pcbway.com/helpcenter/design_instruction/Generate_Position_File_in_Kicad.html ("place the origin at the bottom left corner of the PCB board frame"; the page names units, side or rotation conventions nowhere).

**F8. CPL rotation reference.** KiCad writes the footprint orientation as drawn in the library at 0 degrees, counter-clockwise positive, and for bottom-side parts writes the stored value without mirroring. PCBWay defines only "a 0 to 360 degree value from the origin" with "top point of view" for both sides (PCBWAY-FAB F12) and does not publish which pin-1 position it treats as zero; assemblers reconcile the value against their own feeder/part library during human review, and the risk R-PCB-01 stands. The KiCad Library Convention page that states the library's zero-degree convention could not be fetched (site behind a JavaScript challenge and the session's search budget was exhausted), so the convention is not quoted here; the email asks PCBWay to state its zero reference and to send a placement preview (item 3). Mitigation that does not depend on the answer: pin-1 and polarity marks on silkscreen plus an F.Fab/B.Fab assembly drawing (PCBWAY-FAB REQ PCB-ASM-03).  
Sources: local CPL output; PCBWAY-FAB F12 and its sources.

**F9. BOM export in PCBWay's column order.**
```
"$KICAD_CLI" sch export bom -o out/assembly/cwht-bom.csv \
    --fields "ITEM_NUMBER,Reference,QUANTITY,Manufacturer,MPN,Description,Footprint,Type,DNP" \
    --labels "Item #,Designator,Qty,Manufacturer,Mfg Part #,Description / Value,Package/Footprint,Type,DNP" \
    --group-by "MPN,Footprint,Value,DNP" --ref-delimiter "," --ref-range-delimiter "" cwht.kicad_sch
```
Output (fixture, 7 rows) matched PCBWay's template header `Item # | Designator | Qty | Manufacturer | Mfg Part # | Description / Value | Package/Footprint | Type | Notes` (PCBWAY-FAB F11) except that the last column is KiCad's generated `DNP` field; the DNP row (`R3 ... "DNP"`) must be post-processed to `DNS` in the Type column, which is how PCBWay's sample marks do-not-place parts, and the column relabelled `Your Instructions / Notes`. `--ref-range-delimiter ""` keeps `R1,R2` instead of `R1-R2` so designators match the CPL one-to-one. Requirements on the schematic: custom fields `Manufacturer`, `MPN`, `Type` (`SMD`/`THT`), `Description` on every symbol; the schematic must have a matching `.kicad_pro` (TOOLS F6). The Footprint field carries `Library:Name`; PCBWay accepts that as the package string but a cleaner `Package` field (0603, QFN-16 3x3, ...) can replace it. The BOM must be delivered as .xlsx or .csv (PCBWAY-FAB F10); the CSV is accepted as is.  
Cross-check: BOM SMD designators (not DNP) = {C1, Q1, R1, R2, U1, U2} equals the CPL set; DNP = {R3}: `MATCH`. This 12-line check becomes the Inspection script for PCBWAY-FAB REQ PCB-ASM-02.  
Source: local run (Method 5).

**F10. File-name check against PCBWay's recognized list (zip contents).** `ka-gerbers-kicad.zip` (49.5 kB): 9 of 11 Gerbers plus `PTH.drl`/`NPTH.drl` carry suffixes listed verbatim by PCBWay; `In1_Cu.gbr`/`In2_Cu.gbr` follow the KiCad convention PCBWay's KiCad tutorials use without renaming but are not on the extension table (Medium); `ka-job.gbrjob` and the two `-drl_map.pdf` files are extras PCBWay does not list (PCBWay's engineer review treats extra files as reference; harmless, and the job file documents the stackup). `ka-gerbers-protel.zip` (34.4 kB): every extension (`.gtl .gbl .g1 .g2 .gts .gbs .gto .gbo .gtp .gbp .gm1 .drl`) is on PCBWay's Altium/Protel list. PCBWay's quote form ignores the "via process" selection for Gerber uploads ("For Gerber files this choice will not affect anything, PCB will be made using the parameters of the files"), so mask openings over vias must be right in `F_Mask`/`B_Mask`.  
Sources: local zip listings; PCBWAY-FAB F2; https://www.pcbway.com/orderonline.aspx (tooltip quoted).

**F11. Visual closure of the fixture.** `kicad-cli pcb render --side top` and `--side bottom` produced 1200 x 700 PNGs (`ka-top.png`, `ka-bottom.png`); inspection confirmed the Pico module centred with its USB end overhanging the top edge (deliberate, to exercise copper-to-edge DRC), R1/R2/R3/Q1 in a row with Q1 rotated 180 degrees, the QFN, the header, the NPTH hole, the "TOP" copper label on the front and the mirrored value text of C1 on the back. The pos file's `bottom` entry for C1 corresponds to the part visible only in the bottom render.  
Source: local renders (Method 4).

**F12. Wrapper outline for `tools/kicad_export/pcbway_package.sh`** (ACTION, not yet written): run F3, F6, F7, F9 in sequence with `set -e`; fail on `Invalid layer name`; assert 11 `.gbr` + 1 `.gbrjob` + 2 `.drl`; run the F9 designator cross-check; normalize CPL rotation to 0..360 and map BOM `DNP` to `DNS`; write `README-fab.txt` (layer order L1 F_Cu, L2 In1_Cu, L3 In2_Cu, L4 B_Cu; stackup per PCBWAY-FAB F5; finish; impedance nets) into the zip; zip as `cwht-<rev>-gerbers.zip`, `cwht-<rev>-bom.csv`, `cwht-<rev>-cpl.csv`; filter the Fontconfig warning (TOOLS F6). The fixture and its expected outputs (12 Gerber names, 7 PTH and 5 NPTH hits, 6 CPL rows, 7 BOM rows, `MATCH`) become the accreditation case for the wrapper (TOOLS implication 1).

### Part 2. PA thermal DFM

**F13. PA package facts.**  
(a) Mitsubishi RD07MUS2B (datasheet G2K-Si-240116-1, Jan 2024, outline read from the page-1 drawing rendered to PNG): body 6.0 +/-0.15 x 4.9 +/-0.15 mm, height 1.0 +/-0.05 mm; bottom-side source (GND) pad about 3.3 +/-0.05 x 3.5 +/-0.05 mm (Medium: read from the drawing, not from a dimension table); drain and gate leads 0.75 +/-0.05 mm wide, 0.2 +/-0.05 mm thick; Rth j-c 2.5 C/W (delta-VF method), Tch max 150 C, Pch 50 W at Tc 25 C; supply forms RD07MUS2B-601 (pallet, 25 pcs, "for evaluation"), -T612 (reel 2,000), -T614 (reel 4,000), so a 5-piece turnkey buy will be loose parts or a broken reel from an authorized channel (PCBWAY-FAB F17/F18 overage rules apply).  
(b) NXP AFT05MS006N (datasheet Rev 0, 2/2014): package PLD-1.5W, mechanical outline 98ASA00476D Rev O (14 Jun 2012), case 2297-01, non-JEDEC; RthJC 1.0 C/W (Tc 79 C, 6.0 W CW, 7.5 V, 520 MHz); TJ max 150 C; MSL 3, 260 C peak (JESD22-A113, J-STD-020); tape and reel only (T1 suffix, 1,000 units, 16 mm tape). Figure 21 "PCB Pad Layout for PLD-1.5W": source/thermal pad 0.28 x 0.089 in (7.11 x 2.26 mm) with a via array drawn as three staggered rows of 11, 10 and 11 = 32 vias; gate and drain pads 0.165 x 0.085 in (4.91 x 2.16 mm); pad-to-pad extent 0.155 in (3.94 mm). EOL status per REF-DESIGNS F22 unchanged.  
Sources: https://www.mitsubishielectric.com/semiconductors/hf/products/datasheet/rd07mus2b.pdf ; https://www.nxp.com/docs/en/data-sheet/AFT05MS006N.pdf (pages 2, 18 to 20).

**F14. Vendor via guidance (AN4005).** NXP/Freescale AN4005 "Thermal Management and Mounting Method for the PLD 1.5 RF Power Surface Mount Package" (Rev 0, 11/1997): a through-board metal slug is "not recommended for leadless power surface mount components" (CTE mismatch); "The recommended method for thermal management of the PLD 1.5 package is the use of solder filled thermal vias fabricated in the PCB"; Figure 1c: "12 mil Diameter Centers, 15 x 30 mil Pitch" (0.30 mm vias on a 0.38 x 0.76 mm staggered grid); measured on 0.040 in (1.0 mm) glass-epoxy: junction-to-heat-sink 4.2 C/W typical, "allowing for as much as 20% voiding in the thermal vias, the junction-to-heatsink thermal resistance is specified to be 6.25 C/W maximum"; "it is recommended that the vias are kept small, i.e., less than 0.012 diameter" to limit solder drainage; vias are to be pre-filled by the board supplier (1997 practice: HASL fill), otherwise a second paste print is needed. Modern equivalent of "supplier fills vias" is IPC-4761 Type VII resin fill with copper cap, or copper-paste fill (F15).  
Source: https://www.nxp.com/docs/en/application-note/AN4005.pdf.

**F15. PCBWay via-in-pad and fill options.** Via covering page: Type I tenting "on vias less than or equal to 0.3 mm"; Type III plugging "diameter between 0.4 to 0.5 mm"; Type V filled; Type VII "plated-through and cleaned, a non-conductive paste is filled in and hardened ... the surface is planar and solderable. This is the technology in via-in-pads." Via-in-pad pages: "After drilling the vias on the pad, it must be filled with epoxy resin" with "an electroplated cap for convenient customer soldering"; "higher production costs" and "longer production time", no figures. Copper fill: electroplated fill only for boards <= 0.6 mm and holes <= 0.2 mm (not applicable); copper-paste fill for holes 0.1 to 1.0 mm on boards 0.2 to 4.0 mm, "flat surface suitable for via-in-pad design". Order form: "Via in pad" and "All vias filled with resin and capped" under "Customized Services and Advanced Options", with "We may add extra cost for these special options which will be confirmed after review" (no published price; the extra-cost help page lists none). Capability table: solder-mask plug for 0.20 to 0.40 mm holes (70 % fullness) and 0.4 to 0.7 mm (100 %), boards 0.4 to 2.4 mm; thickness-to-diameter ratio <= 8 normal, 10 high difficulty, > 12 not made (1.6 mm / 0.3 mm = 5.3; 1.0 mm / 0.3 mm = 3.3). PCBWAY-FAB F15 already records that via-in-pad must be resin filled for assembly. Cost signals from secondary sources (Low): resin fill roughly US$0.008 to 0.03 per via; Type VII filled-and-capped "typically add 2.5-3x the cost of unfilled vias and extend lead time by 2-3 days"; PCBWay's actual surcharge is only known after engineer review of a quote.  
Sources: https://www.pcbway.com/pcb_prototype/PCB_Via_Covering.html ; https://www.pcbway.com/helpcenter/ordering_parameter_instruction/Via_in_Pad.html ; https://www.pcbway.com/pcb_prototype/PCB_Via_in_Pad.html ; https://www.pcbway.com/helpcenter/ordering_parameter_instruction/Via_Filled_with_Copper.html ; https://www.pcbway.com/orderonline.aspx ; https://www.pcbway.com/capabilities.html ; https://www.queenems.com/blog/how-to-choose-between-copper-fill-vs-resin-fill-for-via-in-pad-design/ ; https://pcbsync.com/ipc-4761/ (secondary).

**F16. Thermal via array: count, drill, pitch for each package on PCBWay Standard.** PCBWay's via-to-via rule for vias <= 0.45 mm is >= 11 mil (0.28 mm) edge to edge (PCBWAY-FAB F9). The AN4005 pattern (0.30 mm on 0.38 x 0.76 mm stagger) has 0.08 mm edge-to-edge in-row and 0.24 mm to the staggered neighbour, so it cannot be built in the Standard class; relaxing to a 0.65 mm square pitch (0.35 mm edge-to-edge) keeps the PCBWay rule with margin. With a 0.2 mm keep-in from the pad edge:  
- RD07MUS2B source pad 3.3 x 3.5 mm: 5 x 5 = 25 vias, 0.30 mm drill, 0.65 mm pitch (array 2.9 x 2.9 mm).  
- PLD-1.5W thermal pad 7.11 x 2.26 mm: 10 x 3 = 30 vias, 0.30 mm drill, 0.65 mm pitch (array 6.15 x 1.6 mm), close to NXP's 32.  
Per-via conduction resistance R = L / (k A) with copper k = 390 W/mK, barrel wall 25 um (IPC Class 2 minimum average is 20 um; 35 um if PCBWay plates heavier; treat 25 um as the design value), computed locally:

| Board | Drill | Wall | Per via, barrel only | 25 vias | 30 vias |
|---|---|---|---|---|---|
| 1.6 mm | 0.30 mm | 25 um | 190 K/W | 7.6 K/W | 6.3 K/W |
| 1.6 mm | 0.30 mm | 35 um | 141 K/W | 5.6 K/W | 4.7 K/W |
| 1.6 mm | 0.40 mm | 25 um | 139 K/W | 5.6 K/W (20 vias at 0.75 mm pitch: 7.0) | |
| 1.0 mm | 0.30 mm | 25 um | 119 K/W | 4.7 K/W | 4.0 K/W |
| 1.0 mm | 0.30 mm | 35 um | 88 K/W | 3.5 K/W | 2.9 K/W |

Solder-filled barrels (AN4005 practice) lower the 1.6 mm / 0.30 mm / 25 um figure from 190 to 147 K/W per via; resin fill adds nothing useful (epoxy k about 0.3 to 1 W/mK); copper-paste fill helps but its k is not published by PCBWay. Bare FR-4 under the pad (k 0.3 W/mK) is 178 to 311 K/W, so the vias carry essentially all the heat. Conclusion: 0.30 mm drill, 0.65 mm pitch, as many vias as the pad holds, and the board thickness is the strongest lever (1.0 mm gives 35 to 40 % lower array resistance than 1.6 mm), which feeds decision D-PCB-01. 0.30 mm is also the largest drill PCBWay tents with dry film (F15), and stays below AN4005's 0.012 in wicking limit.  
Source: local computation (Method 8); PCBWAY-FAB F9; F14; F15.

**F17. Junction-temperature budget (derived, RD07MUS2B worst case).** At 5.0 W output and 60 % drain efficiency the device dissipates 5/0.60 - 5 = 3.33 W (4.09 W at 55 %, 2.69 W at 65 %). Chain at continuous key-down: Rth j-c 2.5 + via array 4.7 to 7.6 (F16) + plane spreading about 1 + TIM 0.7 to 1.7 (F18) + enclosure to ambient about 4.6 (a 100 x 60 x 30 mm box, outer area 0.0216 m2, natural convection 10 W/m2K) = 13.5 to 17.4 K/W; rise 45 to 58 K; Tj = 85 to 98 C at 40 C ambient, 70 to 83 C at 25 C. This is below the 150 C limit with margin and below the 110 C target that keeps LDMOS MTTF comfortable (NXP Figure 3 trend; AN4005 sizes for 150 C). CW keying (about 50 % on-time) and the enclosure's thermal mass lower the average; the budget does not depend on a separate heatsink, only on the enclosure contact in F18. For AFT05MS006N (Rth j-c 1.0) subtract 1.5 K/W.  
Source: local computation (Method 8); F13; F16.

**F18. Copper pour to an enclosure contact, and the flatness a thermal pad needs.**  
Design: place the PA over a solid B.Cu copper area of at least 12 x 12 mm (15 x 15 mm preferred) that is mask-free and ENIG finished (ENIG cost scales with gold area, PCBWAY-FAB F9), fed by the F16 array and by stitching vias (0.30 mm on a 1.0 mm grid) to L2 ground around the device; keep this area clear of bottom-side parts (PCBWAY-FAB PCB-ASM-08 single-side placement already recommends none). Enclosure: a machined pedestal (boss) on the floor under that area, height set so the gap to the board is the TIM's compressed thickness, with two M3 screws into the pedestal or within 10 mm of it to clamp the board flat locally. TIM: a 0.5 mm silicone gap pad, k >= 3 W/mK, gives R = t/(kA) = 0.0005/(3 x 1.0e-4) = 1.7 K/W at 10 x 10 mm and 0.74 K/W at 15 x 15 mm and absorbs 10 to 50 % of its thickness in tolerance (0.05 to 0.25 mm); thermal grease at 50 um, k 1 W/mK, gives 0.5 K/W at 10 x 10 mm but no tolerance absorption. The pad is recommended.  
Flatness: Fuji Electric's module-mounting guidance is "flatness of the heat sink surface is less than 50 um per 100 mm between screw mounting points and the surface roughness is less than 10 um" (for direct metal-to-metal contact with grease); Boyd states 0.001 in/in (25 um per 25 mm) for satisfactory device-to-heat-sink contact. PCBWay's default machining tolerance is ISO 2768-m with Ra 6.3 um and as-milled finish "comparable to 125 uin Ra" (about 3.2 um) (ENCLOSURE A3/A5). Board side: PCBWay's bow-and-twist limit is <= 0.75 % (IPC-6012 for SMT boards; 0.5 to 0.75 % medium, < 0.5 % high difficulty, asymmetric boards 1.2 %), which is 0.11 mm across a 15 mm pedestal and 0.6 mm across an 80 mm board. Therefore: (1) drawing callout on the pedestal face: flatness 0.05 mm, Ra 3.2 um; (2) the 0.5 mm pad's compression range covers the 0.11 mm local board deviation plus the 0.05 mm pedestal; (3) mask the pedestal face from anodize (Type II is 8 to 12 um of alumina, thermally only about 0.1 K/W over 10 x 10 mm, but it is an insulator and the face should double as the RF ground contact, ENCLOSURE REQ-candidate ME/RF) and request chromate conversion on masked faces if PCBWay offers it (email item 10); (4) request a CMM report on the pedestal and the mounting pattern (ENCLOSURE A5).  
Sources: https://www.fujielectric.com/products/semiconductor/model/igbt/application/box/doc/pdf/REH985b/REH985b_05.pdf (section 2.1) ; https://boydcorp.com/resources/temperature-control/reducing-contact-thermal-resistance.html (search snippet, Medium) ; https://www.pcbway.com/capabilities.html ; https://www.pcbway.com/blog/PCB_Basic_Information/What_is_PCB_Bow_and_Twist_PCB_Knowledge_0d18d920.html ; ENCLOSURE A3, A4, A5, A7.

**F19. Solder-joint and stencil notes for the PA pad on a turnkey build.** With open (unfilled) vias in the source pad, PCBWay's stencil (cut from F_Paste, PCBWAY-FAB F20) will print paste over the via holes and reflow will drain some solder into the barrels (AN4005's reason for small vias); PCBWay's assembly rule that via-in-pad "must be resin filled" (PCBWAY-FAB F15) means an unfilled design may be flagged at review. Two compliant options: (a) order "Via in pad" plus "All vias filled with resin and capped" (Type VII) for the whole board, which also covers the QFN exposed pads, at an unpublished surcharge and 2 to 3 extra days (Low on numbers); (b) segment the F_Paste aperture into a window-pane pattern (about 50 to 60 % coverage, typical QFN practice) over unfilled 0.30 mm vias, tent nothing, and accept some wicking. Option (a) is recommended for a first-power-on target because it removes voiding from the critical thermal joint; it must be priced at the quote (ACTION).  
Sources: F14; F15; PCBWAY-FAB F15, F20.

### Part 3. Vendor confirmation email

**F20. Draft, ready to send.** Two addresses: PCB and assembly questions to service@pcbway.com (PCBWAY-FAB A-PCB-01), CNC questions to 3dcnc@pcbway.com (ENCLOSURE action); the draft is written as one message with two sections so it can be sent to both or split. Attachments to include: Raspberry Pi Pico 2 datasheet RP-008299-DS-3 section 3.2 (surface-mount footprint, paste 163 %) and the PCBWay sample centroid file with our proposed CPL header. Questions state our default assumption so a one-word confirmation suffices.

```
Subject: Pre-order engineering questions for a 4-layer RF board with turnkey assembly (5 pcs) and a CNC aluminum enclosure

Hello PCBWay engineering team,

I am preparing a 5-piece order for a 4-layer, 50 ohm, 144 MHz amateur-radio transceiver board with
turnkey assembly, plus a CNC-machined 6061 aluminum enclosure. Before I upload the files I would
like written confirmation of the points below so the design matches your process the first time.
Where I state an assumption, a simple "confirmed" is enough.

PART A: PCB fabrication and assembly (service@pcbway.com)

1. Castellated module in turnkey assembly. One component is a Raspberry Pi Pico 2 module (SC1631,
   51 x 21 mm, 40 castellated pads on 2.54 mm pitch plus USB-shell and test-point pads), to be
   reflowed as an SMD part on the top side; footprint and 163 % paste apertures follow section 3.2
   of the attached datasheet. (a) Will you place and reflow this module in the same pass as the
   other SMD parts? (b) Do you require it consigned or will you buy SC1631 from an authorized
   reseller? (c) The datasheet gives no MSL rating: what baking or handling do you apply, and how
   many extra units do you need for a 5-piece run? (d) If you would rather hand-solder it, please
   say so, and whether that changes the quote.

2. Dk test frequency. Your stackup library lists 7628 prepreg RC46 % Dk 4.74 and core Dk 4.6. At
   what test frequency are these values stated (1 MHz, 1 GHz, other), and which laminate brand
   and grade do you use for the Tg150 FR-4 4-layer standard build?

3. Centroid file rotation and preview. I will send a KiCad 10 CSV with the header
   "Ref,Val,Package,PosX,PosY,Rot,Side", units mm, origin at the board's lower-left corner, top and
   bottom in one file, bottom-side X not mirrored, rotation counter-clockwise positive. (a) What is
   your zero-degree reference (pin 1 position, or the part's tape orientation)? (b) Do you accept
   negative angles (-90) or should I normalize to 0 to 360? (c) Will your engineers send a placement
   preview or first-article photo of polarized parts and the module for approval before reflow?

4. Impedance testing on a 5-piece order. I will select "Impedance control" for 50 ohm microstrip on
   L1 over L2, standard stackup, target 50 ohm +/-5 ohm. For a 5-piece prototype order: (a) do you
   add a test coupon and run TDR, or only "random check"? (b) Is the impedance test report
   available for this order size, and is it measured with or without solder mask? (c) What is the
   surcharge?

5. Via-in-pad for the RF power transistor and QFN exposed pads. I plan 0.30 mm thermal vias on a
   0.65 mm pitch inside the PA source pad (about 25 to 30 vias) and in QFN exposed pads. (a) Do you
   require these to be resin filled and capped (IPC-4761 Type VII) for assembly, or will you
   reflow over open vias? (b) What is the surcharge and added lead time for "All vias filled with
   resin and capped" on 5 pieces of a 4-layer 1.6 mm (or 1.0 mm) board? (c) Do you offer
   copper-paste filled vias as an alternative on this board?

6. Gerber format. Files will be KiCad 10 RS-274X with X2 attributes off (attributes present only as
   G04 #@! comments), aperture macros enabled, KiCad file names (F_Cu.gbr, In1_Cu.gbr, In2_Cu.gbr,
   B_Cu.gbr, F_Mask.gbr, B_Mask.gbr, F_Silkscreen.gbr, B_Silkscreen.gbr, F_Paste.gbr, B_Paste.gbr,
   Edge_Cuts.gbr) plus a .gbrjob job file. Please confirm this is accepted without renaming, in
   particular the In1_Cu/In2_Cu inner-layer names.

7. Drill format. Excellon, metric, decimal coordinates (FORMAT={-:-/ absolute / metric / decimal}),
   full header, separate PTH.drl and NPTH.drl, slots as G85 route commands, PDF drill map included.
   Your older KiCad guide asks for suppressed leading zeros and minimal header; is the decimal
   format acceptable?

8. BOM. CSV with columns Item #, Designator, Qty, Manufacturer, Mfg Part #, Description / Value,
   Package/Footprint, Type (SMD/THT, DNS for do-not-place), Your Instructions / Notes. Confirm
   acceptable, and confirm that LCSC part numbers may be given in the Notes column for passives.

PART B: CNC enclosure (3dcnc@pcbway.com)

9. Tapped holes and anodize. The part has M3x0.5 tapped holes and will be bead-blasted and Type II
   anodized. Do you mask the tapped holes during anodizing or tap after anodizing? Please state
   which you do by default and how to request the other.

10. Ground and thermal contact faces. Several faces (a pedestal under the RF transistor, the RF
    connector seat, and the PCB mounting bosses) must stay electrically conductive. Can you mask
    these faces from anodize, and do you offer chromate conversion (chem film) on the masked faces?
    How should I mark them on the drawing?

11. Helicoil inserts. Your tapping page lists "Tapping + Thread Inserts". Do you install stainless
    helicoil inserts (M3) in 6061, is this done before or after anodizing, and what pilot hole do
    you want modeled?

12. Flatness. For the pedestal face I will call out flatness 0.05 mm and Ra 3.2 um on the drawing.
    Is this within your standard process for a 15 x 15 mm face, and what does it add to the price?

Thank you. I will attach your answers to my design review package.

Best regards,
Robin Onsay
```
Sources: assembled from F5 to F9, F15 to F19, PCBWAY-FAB open items 1 to 8, ENCLOSURE open items 3 and 4.

### Part 4. Build quantity

**F21. Rule texts (eCFR issue 2026-09-23).** 47 CFR 15.23 (last amended 2016-12-15): "(a) Equipment authorization is not required for devices that are not marketed, are not constructed from a kit, and are built in quantities of five or less for personal use. (b) It is recognized that the individual builder of home-built equipment may not possess the means to perform the measurements for determining compliance with the regulations. In this case, the builder is expected to employ good engineering practices to meet the specified technical standards to the greatest extent practicable. The provisions of § 15.5 apply to this equipment." 47 CFR 2.803(a): "Marketing, as used in this section, includes sale or lease, or offering for sale or lease, including advertising for sale or lease, or importation, shipment, or distribution for the purpose of selling or leasing or offering for sale or lease." (The eCFR page notes an amendment to 2.803 published at 91 FR 57800, 2026-09-11, not yet in the 2026-09-23 issue text.) PART97 F9 already established that the transmitter itself needs no equipment authorization and that a PCBWay-assembled board to the owner's design is not "constructed from a kit"; the five-unit cap therefore comes only from the Part 15 digital section (RP2350, LCD, DC-DC converters, USB charging).  
Sources: eCFR versioner API calls in Method 9; PART97 F9.

**F22. Vendor quantities.** PCBWay fabrication quotes start at 5 pieces (PCBWAY-FAB F20); assembly "minimum is as low as 5 pieces" and 1 piece is possible with a setup fee; PCBWay assembles only boards it fabricated (PCBWAY-FAB F10). So the smallest coherent order is 5 fabricated boards with 1 to 5 of them assembled, and PCBWAY-FAB's checklist line "quantity 5 (or 10 if unit price is close)" must be read against 15.23: ten built units would exceed the cap even if the unit price were attractive.

**F23. Decision statement.** Options: (A) 5 fabricated, 5 assembled, all five kept as the owner's personal units, lent (not transferred) to friends for joint operation (SI-019); (B) 5 fabricated, 3 assembled, 2 bare boards retained as rework or re-spin spares (built count 3, room for two future builds); (C) more than 5 built units, which requires the digital section to be authorized under Supplier's Declaration of Conformity with an accredited-lab test before any unit beyond five is built, or the units to be redesigned so the Part 15 portion is a separately authorized module (out of scope). Recommendation: A, recorded as an ADR with the 15.23 text, the 2.803(a) marketing definition, the SI-019 loan arrangement, and a hard cap of five built units across all revisions until an ADR revises it; order extra consigned parts (for example two spare Pico 2) but not extra assembled boards. Legal caveat: "personal use" in 15.23 is not defined in the rule and whether lending built units to friends is within it is a reading, not a finding; this is Low confidence and not legal advice.

## Implications for cwht

Tags: REQ-candidate, RISK-candidate, DECISION-needed, ACTION.

1. REQ-candidate PCB-FAB-07 (export recipe): The fabrication package shall be produced by `kicad-cli` 10.0.6 with exactly the commands in F3, F6, F7 and F9 (X2 off, netlist attributes off, KiCad file names, drill/place origin at the board lower-left, Excellon metric decimal with separate PTH/NPTH and route-format slots, CPL as CSV mm with `--smd-only --exclude-dnp` and no X negation, BOM in PCBWay template order); a wrapper script shall fail on `Invalid layer name` and on a file count other than 11 Gerbers, 1 job file and 2 drill files. Verification: Inspection (wrapper self-check against the fixture expected values). [F1, F2, F3, F6, F7, F9, F12]
2. REQ-candidate PCB-ASM-09 (CPL filter): Position files for any board carrying the Pico 2 module shall be filtered with `--smd-only`; `--exclude-fp-th` is prohibited because the module footprint contains NPTH pads and would be dropped. Verification: Inspection (designator cross-check, F9). [F7]
3. REQ-candidate PCB-ASM-10 (BOM fields): Every schematic symbol shall carry `Manufacturer`, `MPN`, `Type` and `Description` fields; the BOM post-processor shall map DNP to `DNS` in the Type column and keep designators unranged. Verification: Inspection (schema check on the CSV). [F9]
4. REQ-candidate PCB-FAB-08 (board setup): The board file shall carry the PCBWay stackup and the ENIG finish in Board Setup so the `.gbrjob` states them. Verification: Inspection of the job file. [F3]
5. REQ-candidate PCB-THM-01 (PA thermal path): The PA source pad shall contain a thermal via array of 0.30 mm drill on 0.65 mm pitch filling the pad (25 vias for RD07MUS2B, 30 for PLD-1.5W), connected to a continuous L2 ground and to a mask-free ENIG copper area of >= 12 x 12 mm on B.Cu under the device, with 0.30 mm stitching vias on a 1.0 mm grid around it. Verification: Analysis (F16 model, updated with PCBWay's plating thickness) and Inspection (via count in the drill report). [F14, F15, F16]
6. REQ-candidate PCB-THM-02 (junction temperature): At 5 W output, 60 % drain efficiency, 40 C ambient and continuous key-down, the PA junction temperature shall not exceed 110 C by analysis and the enclosure surface over the PA shall not exceed 60 C by test. Verification: Analysis (F17 chain) and Test (thermocouple or IR spot on the enclosure at TRR, since no junction sensor is fitted). [F17]
7. REQ-candidate ME-THM-01 (enclosure pedestal): The enclosure shall have a pedestal under the PA copper area with flatness 0.05 mm and Ra 3.2 um called out, masked from anodize (chem film if offered), two M3 fasteners within 10 mm, and a 0.5 mm, >= 3 W/mK gap pad specified in the assembly BOM. Verification: Inspection (drawing, CMM report) and Test (TRR thermal test). [F18]
8. REQ-candidate PCB-FAB-09 (via fill): The PA pad vias and QFN exposed-pad vias shall be ordered as via-in-pad, resin filled and capped (IPC-4761 Type VII), unless PCBWay's answer to email item 5 makes open vias with window-pane paste acceptable; the order notes shall state it. Verification: Inspection of order parameters and of the PCBWay engineering review reply. [F15, F19]
9. RISK-candidate R-PCB-08 (silent export loss): a mis-typed layer name or a footprint-attribute mismatch removes a file or a part from the package with exit code 0. Mitigation: implication 1 and 2 checks; render and inspect the Gerbers (GerbView is GUI; use `kicad-cli pcb export svg` of the same layers as a proxy) before upload. [F2, F7]
10. RISK-candidate R-PCB-09 (via-in-pad surcharge and lead time): Type VII fill is priced only after review and secondary sources put it at 2.5 to 3x via cost and 2 to 3 days; a 1.0 mm board choice may change fill feasibility. Mitigation: get the quote at PDR with both thicknesses (ACTION 14). [F15]
11. RISK-candidate R-PCB-10 (plating thickness unknown): the via-array resistance scales inversely with barrel wall; PCBWay does not publish the finished hole copper (IPC Class 2 average 20 um minimum assumed 25 um). Mitigation: ask in the quote; request the microsection report (PCBWAY-FAB F23) which gives hole-wall copper. [F16]
12. RISK-candidate R-REG-01 (five-unit cap): ordering 10 boards "if unit price is close" or building spares would breach 15.23(a). Mitigation: ADR with the hard cap, and the parts-not-boards spares policy. [F21, F22, F23]
13. DECISION-needed D-PCB-06 (build quantity): choose option A (5 fab, 5 assembled, all retained and lent) versus B (5 fab, 3 assembled). Recommendation A. [F23]
14. DECISION-needed D-PCB-01 (revisited): board thickness 1.6 mm vs 1.0 mm is now also a thermal trade: 1.0 mm cuts the via-array resistance by 35 to 40 % (7.6 to 4.7 K/W at 25 vias) and eases pedestal conformity, at the cost of stiffness under the encoder and jacks. Recommendation: 1.0 mm if the enclosure floor supports the board on at least four bosses; otherwise 1.6 mm with 35 um plating requested. [F16, F18]
15. DECISION-needed D-PCB-07 (via fill method): Type VII resin fill and cap (recommended) vs open vias with window-pane paste vs copper-paste fill. [F15, F19]
16. DECISION-needed D-PCB-08 (Gerber naming): KiCad names (recommended) vs Protel extensions; both verified. [F4, F10]
17. ACTION A-PCB-06: Send the F20 email now (before PDR) so the answers are in the CDR package; attach the Pico 2 datasheet section 3.2 and the proposed CPL header. Owner: Robin.
18. ACTION A-PCB-07: Create `tools/kicad_export/` with the F3/F6/F7/F9 wrapper, the fixture generator `make_ka_board.py` (copied from scratch and adapted to the project library tables), the BOM/CPL cross-check, and the expected-value file; register it under `tools/accredit/` (TOOLS implication 1). Owner: Claude.
19. ACTION A-PCB-08: Upload the fixture zip (`ka-gerbers-kicad.zip`) to PCBWay's instant quote to see whether the CAM front-end accepts the KiCad 10 X1-with-comments Gerbers and inner-layer names without a manual ticket; record the result with date. Owner: Robin (needs the account).
20. ACTION A-PCB-09: At PDR, run PCBWay instant quotes for 5 pcs at 1.6 mm and 1.0 mm, with and without "Via in pad + All vias filled with resin and capped" and "Impedance control", and log the four prices and lead times as TPMs. Owner: Robin.
21. ACTION A-PCB-10: Write the ADR for D-PCB-06 with the 15.23 and 2.803 texts quoted from the eCFR API. Owner: Claude, approval Robin.

## Confidence

| Finding | Confidence | Basis |
|---|---|---|
| F1, F2, F3, F4, F6, F7, F9, F10, F11 (kicad-cli behaviour, file names, CPL/BOM content) | High | Run locally on 10.0.6 with outputs quoted |
| F5 (X2 off required) | High for the instruction, Medium for current CAM behaviour | PCBWay page quoted; forum evidence is 2019 |
| F8 (rotation reference) | Low | PCBWay does not publish it; KLC page not fetched |
| F12 (wrapper outline) | n/a (proposal) | |
| F13 (package facts) | High for datasheet numbers; Medium for RD07MUS2B pad size read from the drawing | Datasheets downloaded; drawing rendered and read |
| F14 (AN4005) | High | Text extracted from the PDF |
| F15 (PCBWay via options) | High for options and limits; Low for cost figures | PCBWay pages quoted; costs from secondary sources |
| F16, F17 (thermal numbers) | Medium | Closed-form model; plating thickness and spreading assumed |
| F18 (contact and flatness) | Medium | Fuji and PCBWay figures quoted; pad and geometry choices are engineering judgement |
| F19 (paste and fill options) | Medium | PCBWay rule from PCBWAY-FAB F15; vendor practice from AN4005 |
| F20 (email) | n/a (draft) | |
| F21 (rule texts) | High | eCFR API, issue 2026-09-23 |
| F22 (quantities) | High | PCBWAY-FAB F10, F20 |
| F23 (decision reading of "personal use") | Low | Rule text only; not legal advice |

## Open items

1. PCBWay's written answers to email items 1 to 12 (A-PCB-06); until item 6 and 7 are answered, keep the Protel and legacy-drill variants available in the wrapper.
2. KiCad Library Convention zero-rotation rule text (site blocked; search budget exhausted): fetch and quote it in the CPL section of the CDR package.
3. PCBWay finished hole-wall copper thickness (assumed 25 um) and whether 35 um can be requested; microsection report.
4. Actual surcharge and lead time for Type VII via fill and for impedance control on 5 pieces (A-PCB-09).
5. Whether PCBWay's instant-quote CAM accepts the fixture zip without a ticket (A-PCB-08).
6. RD07MUS2B source-pad dimensions from a dimension table rather than the drawing (Mitsubishi package page or a distributor drawing); the thermal via count (25) should be re-derived once confirmed.
7. Gap-pad part number and its compressed-thickness curve; pedestal height tolerance stack with the PCB thickness tolerance (+/-10 % at >= 1.0 mm, PCBWAY-FAB F9).
8. The 2.803 amendment at 91 FR 57800 (2026-09-11) was not read; confirm it does not change the marketing definition before the ADR is signed.
9. Whether the `Package` BOM column should carry the KiCad footprint name or a plain package string (PCBWay accepts either; decide at CDR).

## Sources

- KiCad CLI manual 10.0: https://docs.kicad.org/10.0/en/cli/cli.html
- PCBWay KiCad Gerber help (legacy, X2 instruction): https://www.pcbway.com/blog/help_center/Generate_Gerber_file_from_Kicad.html
- PCBWay KiCad Gerber help (KiCad 8): https://www.pcbway.com/helpcenter/technical_support/Generate_Gerber_file_from_Kicad.html
- PCBWay KiCad position file help: https://www.pcbway.com/helpcenter/design_instruction/Generate_Position_File_in_Kicad.html
- KiCad forum, PCBWay and X2 (2019-12-27): https://forum.kicad.info/t/pcbway-cannot-read-kicad-gerber-file-solved/20420
- PCBWay via covering: https://www.pcbway.com/pcb_prototype/PCB_Via_Covering.html
- PCBWay via-in-pad (ordering parameter): https://www.pcbway.com/helpcenter/ordering_parameter_instruction/Via_in_Pad.html
- PCBWay via-in-pad (product page): https://www.pcbway.com/pcb_prototype/PCB_Via_in_Pad.html
- PCBWay via filled with copper: https://www.pcbway.com/helpcenter/ordering_parameter_instruction/Via_Filled_with_Copper.html
- PCBWay online quote form (option labels and tooltip): https://www.pcbway.com/orderonline.aspx
- PCBWay capabilities table: https://www.pcbway.com/capabilities.html
- PCBWay extra-cost list: https://www.pcbway.com/helpcenter/paymentproblems/What_PCBs_will_be_charged_of_extra_cost_.html
- PCBWay impedance control: https://www.pcbway.com/pcb_prototype/Impedance_Control.html
- PCBWay stackup library (no Dk frequency stated): https://www.pcbway.com/multi-layer-laminated-structure.html
- PCBWay bow and twist: https://www.pcbway.com/blog/PCB_Basic_Information/What_is_PCB_Bow_and_Twist_PCB_Knowledge_0d18d920.html
- PCBWay tapping and thread inserts: https://www.pcbway.com/rapid-prototyping/Sheet-metal/tapping.html
- Mitsubishi RD07MUS2B datasheet (G2K-Si-240116-1, Jan 2024): https://www.mitsubishielectric.com/semiconductors/hf/products/datasheet/rd07mus2b.pdf
- NXP AFT05MS006N datasheet (Rev 0, 2/2014): https://www.nxp.com/docs/en/data-sheet/AFT05MS006N.pdf
- NXP AN4005 (Rev 0, 11/1997): https://www.nxp.com/docs/en/application-note/AN4005.pdf
- Fuji Electric application manual REH985b chapter 5 (heat sink flatness): https://www.fujielectric.com/products/semiconductor/model/igbt/application/box/doc/pdf/REH985b/REH985b_05.pdf
- Boyd, reducing contact thermal resistance (secondary): https://boydcorp.com/resources/temperature-control/reducing-contact-thermal-resistance.html
- Secondary via-fill cost signals: https://www.queenems.com/blog/how-to-choose-between-copper-fill-vs-resin-fill-for-via-in-pad-design/ ; https://pcbsync.com/ipc-4761/
- eCFR versioner API, 47 CFR 15.23 and 2.803, issue 2026-09-23: https://www.ecfr.gov/api/versioner/v1/full/2026-09-23/title-47.xml?part=15&section=15.23 ; https://www.ecfr.gov/api/versioner/v1/full/2026-09-23/title-47.xml?part=2&section=2.803 ; version history https://www.ecfr.gov/api/versioner/v1/versions/title-47.json?part=15&section=15.23
- Prior project reports: `/Users/robinonsay/rust/cwht/docs/research/pcbway-fabrication-and-assembly.md`, `/Users/robinonsay/rust/cwht/docs/research/verification-tooling-inventory.md`, `/Users/robinonsay/rust/cwht/docs/research/2m-cw-transceiver-reference-designs.md` (F22, F24), `/Users/robinonsay/rust/cwht/docs/research/enclosure-cnc-and-openscad-pipeline.md` (A3, A4, A5, A7), `/Users/robinonsay/rust/cwht/docs/research/part97-regulatory-basis.md` (F9)
