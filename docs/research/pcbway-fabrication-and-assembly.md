# PCBWay fabrication and turnkey assembly requirements for the cwht 4-layer RF board

**Assignment key:** pcbway-pcb  
**Date of research:** 2026-09-25  
**Author:** Claude (research subagent)  
**Status:** Research input to PDR/CDR; not a baseline. Every candidate requirement below must pass through the CR process (charter section 11, rule 5) before it enters the requirements set.

## Question

What does PCBWay require from a small-run (5 boards), 4-layer, 50 ohm RF board ordered with turnkey assembly: file requirements (Gerber naming and format, drill, BOM columns and MPN handling, centroid/CPL format and rotation convention, KiCad export compatibility), the standard 4-layer stackups with dielectric data usable for 50 ohm calculations, controlled-impedance options, DFM limits (trace/space, via, annular ring, mask), assembly capabilities (min passive size, QFN/DFN, fine pitch, castellated modules such as the Raspberry Pi Pico 2, through-hole and connectors, double-sided), sourcing rules (Digi-Key/Mouser/LCSC, consigned vs turnkey), minimum quantities, lead times and cost signals, and RF/impedance testing services. Deliver the checklist the CDR package must satisfy.

## Method

1. Read the process charter sections 1, 9 and 11 (`/Users/robinonsay/rust/cwht/docs/process/00-charter.md`) to align the output with the evidence and traceability rules.
2. Fetched PCBWay primary pages (capabilities, stackup library, impedance calculator and impedance-control pages, assembly capabilities, assembly FAQ, assembly file requirements, SMT ordering guide, components-sourcing page, help-center articles on lead time, extra costs, consigned overages, panelization and fiducials, quality-control reports, PCBA testing, KiCad export tutorials, KiCad plugin README).
3. Downloaded and parsed raw HTML where the summarizing fetch tool lost numbers: the multi-layer stackup library (all 4-layer entries), the capabilities table, the 4-layer prototype price page. Commands and outputs are quoted under the relevant findings.
4. Downloaded PCBWay's sample BOM (`Sample_BOM_PCBWay.xlsx`) and sample centroid file (`a-sample-of-PCBWay-Centroid-File.txt`) and inspected the actual columns and values.
5. Downloaded the Raspberry Pi Pico 2 datasheet PDF and extracted section 3.2 (surface-mount footprint) and Appendix A.2 (ordering codes) with `pdftotext`.
6. Downloaded the KiCad 9.0.9 PCB Editor manual and extracted the exact option descriptions for Gerber, drill and component-placement outputs.
7. Ran a local Hammerstad-Jensen microstrip calculation against PCBWay's published 1.6 mm and 1.0 mm stackup numbers to give a first 50 ohm trace width estimate (analysis only; PCBWay recomputes).
8. Web searches for items PCBWay does not publish as a single page (castellated-module assembly practice, rotation conventions, cost examples, KiCad footprint availability).

Scratch files (not part of the repo) are under the session scratchpad `.../scratchpad/pcbway/` (`stackup.html`, `cap.html`, `centroid_sample.txt`, `Sample_BOM_PCBWay.xlsx`, `pico2.pdf`, `pico2.txt`, `kicad9.html`).

## Findings

### A. Fabrication data package

**F1. Required Gerber set and format.** PCBWay requires RS-274X Gerbers containing the board outline, all copper layers, solder mask layers, silkscreen layers and an Excellon NC drill file, compressed into a single .zip and uploaded to the instant quote. The most common rejection is a missing board outline layer. If a layer does not exist (for example no bottom silkscreen), the matching online parameter must be set to "none" rather than omitting it silently.  
Sources: https://www.pcbway.com/helpcenter/file_issues/Gerber_files_are_not_completed.html ; https://www.pcbway.com/blog/Engineering_Technical/What_s_the_Gerber_.html

**F2. KiCad file names PCBWay recognizes.** PCBWay's extension table lists the KiCad defaults verbatim: `F_Cu.gbr, B_Cu.gbr, F_Silkscreen.gbr, B_Silkscreen.gbr, F_Mask.gbr, B_Mask.gbr, F_Paste.gbr, B_Paste.gbr, Edge_Cuts.gbr, NPTH.drl, PTH.drl`. Inner layers (`In1_Cu.gbr`, `In2_Cu.gbr`) are not listed on that page but follow the same KiCad convention; PCBWay's own KiCad 8 tutorial uses the default export without renaming. Altium/Protel extensions (.GTL/.GBL/.G2/.G3/.GTS/.GBS/.GTO/.GBO/.GKO/.TXT) are also recognized, so KiCad's "Use Protel filename extensions" option is acceptable either way.  
Sources: https://www.pcbway.com/helpcenter/technical_support/Gerber_File_Extension_from_Different_Software.html ; https://www.pcbway.com/helpcenter/technical_support/Generate_Gerber_file_from_Kicad.html

**F3. KiCad 9 export options and what they mean (KiCad 9.0.9 manual).** Extracted with `curl https://docs.kicad.org/9.0/en/pcbnew/pcbnew.html | python3 ...`:
- Gerber: "Use Protel filename extensions" names files .GTL/.GBL etc.; "Generate Gerber job file" emits a .gbrjob "that includes information about the PCB stackup, materials, and finish"; "Use extended X2 format ... may not be compatible with older CAM software used by some manufacturers"; "Disable aperture macros ... should only be used ... when requested by your manufacturer"; "Check zone fills before plotting ... Plot outputs may be incorrect if this option is disabled!"; "Subtract soldermask from silkscreen" removes silk from exposed copper.
- Drill: "By default, plated holes and non-plated holes will be generated in two different Excellon files. With this option [PTH and NPTH in single file] enabled, both will be merged ... should not be enabled unless requested"; oval holes default to the route command, "correct for most manufacturers".
- Position file: units selectable; "Include only SMD footprints"; "Exclude all footprints with through hole pads"; "Exclude all footprints with the Do Not Populate flag set"; "Use drill/place file origin"; "Use negative X coordinates for footprints on bottom layer"; "Generate single file with both front and back positions".
PCBWay's tutorials do not override any default, and PCBWay's own extension table lists separate `PTH.drl`/`NPTH.drl`, so KiCad defaults (RS-274X, separate PTH/NPTH, route command for slots) are the compatible choice. Whether PCBWay's CAM accepts X2 attributes is not stated; treat X2 as optional-off.  
Source: https://docs.kicad.org/9.0/en/pcbnew/pcbnew.html (sections "Gerber options", "Drill files", "Component placement files")

**F4. Layer orientation and order.** PCBWay: "When viewed from the top of the design file, we need all the top and inner layers to appear as a true board in normal visual form, but for all the bottom layers, a mirrored visual is required." Unique TOP/BOT labels in copper are recommended so orientation errors are caught visually before lamination. PCBWay does not publish a mechanism for confirming inner-layer sequence beyond filenames; the KiCad Gerber job file plus a stackup note in the order remarks closes that gap.  
Source: https://www.pcbway.com/pcb_prototype/Layer_Orientation.html

### B. Stackup and impedance

**F5. PCBWay standard 4-layer stackups (through-hole vias only).** Extracted from the raw stackup library HTML (`curl .../multi-layer-laminated-structure.html`, parsed with Python). All 4-layer builds use one prepreg between L1/L2 and L3/L4 and one core between L2/L3. For 1 oz outer / 1 oz inner:

| Finished thickness | Outer Cu | Prepreg (type, RC, Dk) | PP nominal -> after lamination (70 % / 50 % / 30 % inner residual Cu) | Core (Dk 4.6) | Finished thickness stated |
|---|---|---|---|---|---|
| 1.6 mm | 0.5 oz base plated to 1 oz (0.0175 mm base) | 7628 RC46 %, Dk 4.74 | 0.1960 -> 0.1855 / 0.1785 / 0.1715 mm | 1.030 mm (1.1 mm with Cu) | 1.61 / 1.59 / 1.58 mm, tol. +/-10 % |
| 1.2 mm | same | 7628 RC46 %, Dk 4.74 | 0.1960 -> 0.1855 / 0.1785 / 0.1715 mm | 0.630 mm | 1.21 / 1.19 / 1.18 mm |
| 1.0 mm | same | 7628 RC46 %, Dk 4.74 | 0.1960 -> 0.1855 / 0.1785 / 0.1715 mm | 0.430 mm | 1.01 / 0.99 / 0.98 mm |
| 0.8 mm | same | 7628 RC46 %, Dk 4.74 | 0.1960 -> 0.1855 / 0.1785 / 0.1715 mm | 0.230 mm | 0.81 / 0.79 / 0.78 mm |

2 oz outer variants of 1.6 mm use the same 7628 prepreg over a 0.93 mm core (finished 1.58 / 1.56 / 1.55 mm). Other prepregs appearing in the library: 2116 RC58 % Dk 4.45 (0.130 mm nominal, ~0.1195 mm laminated), 3313 RC58 % Dk 4.45 (0.103 mm), 1080 RC68 % Dk 4.21 (0.081 mm). The page states: "This is a through-hole board stack-up, not applicable for blind and buried vias. PCBWay supports customers to customize structures." Custom stackups are requested by ticking "Custom stack-up" under "Additional Options" at order time; PCBWay warns that customized stackups "especially boards with impedance control" may be adjusted "due to manufacture capability or material stock issue".  
Sources: https://www.pcbway.com/multi-layer-laminated-structure.html ; https://www.pcbway.com/pcb_prototype/_Stack_up_for_Prototypes.html

**F6. 50 ohm first estimate on the standard stackup (analysis, not vendor data).** Hammerstad-Jensen microstrip with thickness correction, L1 over L2 ground, t = 35 um, Er = 4.74 (local Python, output reproduced):
```
1.6mm 1oz/1oz 70% residual (PP 7628 0.1855mm): W(50ohm) ~ 0.307 mm (12.1 mil), eps_eff ~ 3.55; W=0.30mm -> 50.6 ohm, W=0.32mm -> 48.8 ohm, W=0.35mm -> 46.5 ohm
1.6mm 1oz/1oz 50% residual (PP 7628 0.1785mm): W(50ohm) ~ 0.294 mm (11.6 mil)
1.6mm 1oz/1oz 30% residual (PP 7628 0.1715mm): W(50ohm) ~ 0.282 mm (11.1 mil)
1.0mm 1oz/1oz 70% residual (PP 7628 0.1855mm): W(50ohm) ~ 0.307 mm (12.1 mil)
```
Sensitivity is about -1 ohm per +0.01 mm of width and about +/-2 ohm across the residual-copper range, so a 0.30 mm nominal microstrip lands within PCBWay's +/-5 ohm band before mask. PCBWay's own impedance blog gives the rule of thumb that the solder resist lowers single-ended impedance by about 2 ohm, and its calculator page states that for microstrip, edge-coupled and coplanar models "the outer layer impedance testing does not include the solder mask" and that "the final values and the corresponding layer construction have to be calculated by us." The calculator supports microstrip, embedded microstrip, edge-coupled microstrip, stripline variants and coplanar waveguide. Note that the same 7628 prepreg is used for 1.6 mm and 1.0 mm boards, so the outer-layer 50 ohm geometry does not change if cwht chooses a thinner board for the pocket enclosure.  
Sources: local command (see Method step 7); https://www.pcbway.com/pcb_prototype/impedance_calculator.html ; https://www.pcbway.com/blog/Engineering_Technical/PCB_impedance_control_technology.html

**F7. Impedance control service terms.** Capabilities table: impedance tolerance "+/-10% (50 ohm and below: +/-5 ohm)"; tighter needs Advanced PCB review. Impedance control is an option in the instant quote form. PCBWay's impedance page: minimum dielectric thickness between layers 50 um; PCBWay performs "random check the impedance in production and random check the finished product". PCBWay's quality-control page lists an "Impedance Test Report" among the reports "available upon request" together with microsection and thermal-stress reports; it does not describe coupon geometry or TDR method on any page found.  
Sources: https://www.pcbway.com/capabilities.html ; https://www.pcbway.com/pcb_prototype/Impedance_Control.html ; https://www.pcbway.com/oem/quality-control.html ; https://www.pcbway.com/orderonline.aspx

**F8. RF laminates.** Rogers RO4003C and RO4350B are offered under "Advanced PCB", including FR-4/Rogers hybrids ("the mature mixed pressure process realizes the mixing of FR-4 and high-frequency materials"). Advanced-PCB build time for 4 layers is 5 days (<1 m^2), 48 hours extra-urgent. At 144 MHz the loss and Dk stability of Tg150 FR-4 are adequate for a 50 ohm feed of a few centimeters; Rogers is not justified for cwht unless the PA matching network needs tighter Dk tolerance than +/-10 % impedance allows (decision, see Implications).  
Sources: https://www.pcbway.com/pcb-products/Advanced_PCB_ROGERS_4350B.html ; https://www.pcbway.com/quickturn-pcb-fabrication.html

### C. Fabrication DFM limits (Standard PCB service)

**F9. Capability table values** (fetched 2026-09-25; items marked * were re-verified from the raw HTML):
- Layers 1-14*; material FR-4 (multilayer base "automatically upgraded to TG150 for FREE"), Aluminum, Copper base; Rogers/PTFE under Advanced.
- Board thickness 0.2-3.2 mm in steps 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.6, 2.0, 2.4, 2.6, 2.8, 3.0, 3.2*; tolerance +/-10 % (t >= 1.0 mm)*, +/-0.1 mm (t < 1.0 mm)*.
- Min trace and spacing: "Min manufacturable trace is 4mil (0.1mm)"* and spacing 4 mil*; the quote form offers 3/3, 4/4, 5/5, 6/6, 8/8 mil classes; 1 oz outer layers are quoted at 5-6 mil trace / 6 mil space, 2 oz outer 7/8 mil, inner 1 oz 4/5 mil. 5/5 mil and 0.25 mm holes receive a price discount (PCBWay 2022 announcement); 6/6 mil and 0.3 mm is the cheapest class.
- Drill: min 0.15 mm (0.2 mm practical minimum); finished PTH tolerance +/-0.08 mm (example: 0.6 mm nominal accepted 0.52-0.68 mm)*; position +/-0.075 mm; via <= 0.45 mm treated as via with >= 11 mil via-to-via spacing; component hole spacing >= 16 mil*.
- Min annular ring 0.15 mm (6 mil); 4-layer inner isolation ring 6.5 mil.
- Solder mask LPI; mask bridge (dam) 4 mil green with 8 mil pad spacing between IC pins*, 4.5 mil for colours other than green/black*; 3-4 mil dam possible at 7-8 mil pitch; mask plug for 0.20-0.40 mm vias.
- Silkscreen min line 0.15 mm*, min height 0.8 mm, ratio 1:5.
- Outline tolerance +/-0.2 mm routed, +/-0.5 mm V-score*; min board 3 x 3 mm (fab) but see assembly panel rules; copper-to-edge 0.25 mm for milling; plated slot >= 0.5 mm, non-plated slot >= 0.8 mm, slot length/width >= 2*.
- Finishes: HASL (Pb and Pb-free), ENIG, OSP, hard gold, immersion Ag, immersion Sn, ENEPIG, bare copper. PCBWay's finish comparison recommends ENIG for fine-pitch (flat surface); ENIG price scales with gold area.
- Castellated holes (if ever needed on cwht itself): min 0.6 mm diameter, >= 0.55 mm spacing, pads on every copper layer, surcharge applies.
Sources: https://www.pcbway.com/capabilities.html ; https://www.pcbway.com/orderonline.aspx ; https://www.pcbway.com/blog/News/Big_News_Sale_Promotion_for_Multilayer_PCB_86a5864f.html ; https://www.pcbway.com/pcb_prototype/Comparison_of_several_PCB_surface_finish_types.html ; https://www.pcbway.com/helpcenter/paymentproblems/What_PCBs_will_be_charged_of_extra_cost_.html ; https://www.pcbway.com/pcb_prototype/What_are_Plated_Half_Holes_Castellated_Holes_.html

### D. Assembly data package

**F10. Files for assembly.** "Gerber files, Centroid data and BOM"; the assembler needs at minimum the copper, silkscreen and solder-paste layers of the same RS-274X set used for fabrication. BOM in .xls/.xlsx/.csv; "We do not accept BOM files in pdf". Assembly drawings and photos are optional but recommended. Only PCBWay-made PCBs are assembled ("Currently we do not use other's PCB to assemble").  
Sources: https://www.pcbway.com/assembly-file-requirements.html ; https://www.pcbway.com/assembly-faq.html ; https://www.pcbway.com/smt_ordering_guide.html

**F11. BOM columns.** Required for consigned: Line #, Quantity per part number, Reference Designator, Part Number, Part Description, Package, Type (SMD / THT / hybrid). For turnkey or partial turnkey add Manufacturer's Name, Manufacturer's Part Number, Distributor's Part Number. The downloaded template (`Sample_BOM_PCBWay.xlsx`, parsed via `unzip` + `sharedStrings.xml`) has header row: `Item # | Designator* | Qty* | Manufacturer | Mfg Part #* | Description / Value | Package/Footprint* | Type | Your Instructions / Notes` (asterisk = mandatory) and marks do-not-place parts by writing `DNS` in the Type column (rows U2,U4 and CN3,CN4 in the sample). PCBWay's Q&A also accepts "DNP, DNS" in the notes column. Customer-preferred distributors are indicated by "remark the supplier name or include the link in the BOM".  
Sources: https://www.pcbway.com/assembly-file-requirements.html ; https://www.pcbway.com/img/images/pcbway/Sample_BOM_PCBWay.xlsx ; https://www.pcbway.com/blog/PCB_Basic_Information/PCBWay_Q_A_003___Common_Questions_for_PCBA_Ordering_01.html ; https://www.pcbway.com/helpcenter/pcb_assembly_ordering/Can_we_buy_components_from_specific_supplier_or_provide_link_for_purchasing_.html

**F12. Centroid (CPL) format and rotation convention.** The sample file header is `Designator Footprint Mid X Mid Y Ref X Ref Y Pad X Pad Y TB Rotation Comment`; coordinates in the sample carry a `mil` suffix, the side column `TB` uses `T`/`B`, rotation values are 0.00 / 90.00 / 180.00 / 270.00 / 360.00 (both 0 and 360 appear). PCBWay's definition: X/Y are the component centre measured from the board origin at the lower-left corner; "The rotation is a 0 to 360 degree value from the origin. Both the top and reverse side components use a top point of view as their reference point." Accepted formats: Excel, .txt, .pos; units mm accepted (PCBWay's KiCad page says place the drill/place origin at the bottom-left of the board frame). "Only surface mounting parts are listed in the Centroid" and "THT designators can be excluded". PCBWay does not define the zero-degree pin-1 reference or the positive direction; its help list warns that files where top and bottom data are mixed without clear layer identification, or where designators are missing or do not match the BOM/silkscreen, are rejected. Independent evidence (KiCad forum, 2023) is that CPL rotation is assembler-dependent and that assemblers correct against their own part library; verification is essential. PCBWay's process is human review of every assembly order ("Our engineers will double check the files before the production").  
Sources: https://www.pcbway.com/img/images/pcbway/a-sample-of-PCBWay-Centroid-File.txt ; https://www.pcbway.com/helpcenter/design_instruction/How_to_create_a_Centroid_File_from_Eagle__Altium_Sprint_Layout_and_ORCAD_.html ; https://www.pcbway.com/helpcenter/design_instruction/Generate_Position_File_in_Kicad.html ; https://www.pcbway.com/helpcenter/Assembly_files_problems/Top_13_suggestions_for_solving_PCB_Assembly_files_problems.html ; https://forum.kicad.info/t/pos-file-and-footprint-orientation/42065

**F13. Silkscreen and polarity.** Add cathode/anode and pin-1 marks on the silkscreen, or supply a separate assembly drawing; designators must exist on silkscreen (or drawing) and match BOM and CPL exactly; no duplicate designators; LED colour and brand must be in the BOM.  
Sources: https://www.pcbway.com/smt_ordering_guide.html ; https://www.pcbway.com/helpcenter/Assembly_files_problems/Top_13_suggestions_for_solving_PCB_Assembly_files_problems.html

**F14. PCBWay KiCad plugin.** One-click export of Gerbers, IPC netlist, BOM and pick-and-place, then upload to the quote page. Requires schematic fields Designator, Quantity, MPN/Part Number, Package (required) and Manufacturer, Description (optional), and "Update Board from Schematic" before export. README mentions KiCad 10 support for direct assembly ordering. Repository shows 21 open issues; treat as a convenience, not the qualified path.  
Source: https://github.com/pcbway/PCBWay-Plug-in-for-Kicad

### E. Assembly capabilities

**F15. Capability limits.** Board size 10 x 10 mm min (smaller must be panelized), 250 x 500 mm max; passives "as small as 01005, 0201, 0402"; "0.25mm fine pitch parts"; BGA 0.3 mm pitch on rigid boards (FAQ: 0.25 mm pitch BGA with X-ray); package list includes BGA, uBGA, QFN, QFP, SOIC, PLCC, PoP, "Small Chip Packages (0.2mm pitch)"; SMT, THT and mixed; single or double-sided placement ("printing, placement, and reflow process can be repeated" for the second side); leaded and lead-free; 3D SPI, online and offline AOI, X-ray; IPC-A-610 Class 2 by default (Class 3 advertised); part formats accepted: reels, cut tape, tube/tray, loose parts, bulk. THT is soldered "either manually or using an automated soldering machine". Vias in BGA/QFN pad areas: tented and filled with mask near pads; via-in-pad must be resin filled.  
Sources: https://www.pcbway.com/assembly-capabilities.html ; https://www.pcbway.com/pcb_prototype/SMT_Assembly_Capabilities.html ; https://www.pcbway.com/pcb_prototype/Through_Hole_Assembly.html ; https://www.pcbway.com/assembly-faq.html

**F16. Castellated module (Raspberry Pi Pico 2) as a component.** PCBWay publishes no explicit policy on placing castellated modules; its capability text covers packages, not modules, and its accepted part formats include "Loose Parts and Bulk". The Pico 2 datasheet (RP-008299-DS-3, extracted with `pdftotext`) section 3.2 "Surface-mount footprint" states: "The following footprint (Figure 5) is recommended for systems which will be reflow-soldering Pico 2 units as modules"; the footprint includes the test-point pads and "the 4 USB connector shell ground pads (A,B,C,D)" because "solder does pool at these pads during manufacture and can stop the module sitting completely flat"; "Through trials with customers, we have determined that the paste stencil must be bigger than the footprint ... We recommend paste zones 163% larger than the footprint." Unused test points may have copper voided under them. Board is 51 x 21 mm, 1 mm thick, single sided, 40 castellated pins on 2.54 mm pitch. Ordering codes (Table 3): SC1631 Pico 2, "1+ pcs / Bulk", RRP US$5.00; SC1632 with headers (not usable as SMT module). No reel packaging, MSL rating or reflow profile is given in the datasheet. The official KiCad footprint library carries `Module.pretty/RaspberryPi_Pico_SMD_HandSolder.kicad_mod` (Pico 1 outline, identical 51 x 21 mm, 2.54 mm castellations); no Pico 2 specific footprint was found, and the Pico 2 datasheet changelog notes "Removed KiCad link until the file is ready." Multiple PCBWay shared projects use Pico carriers, but none found documents PCBWay reflowing the module in turnkey assembly.  
Sources: https://pip-assets.raspberrypi.com/categories/1005-raspberry-pi-pico-2/documents/RP-008299-DS-3-pico-2-datasheet.pdf (redirect target of https://datasheets.raspberrypi.com/pico/pico-2-datasheet.pdf) ; https://gitlab.com/kicad/libraries/kicad-footprints/-/blob/f3fd1cf61314110dd3f5c33b6bf7fe8a95c92b35/Module.pretty/RaspberryPi_Pico_SMD_HandSolder.kicad_mod ; https://www.pcbway.com/assembly-capabilities.html

### F. Sourcing, quantities, lead time, cost

**F17. Sourcing models and distributors.** Four options: (1) full turnkey, "purchased from authorized and reliable distributors"; (2) "We purchase all components from distributors you recommend"; (3) consigned/kitted; (4) combo. Named distributors: Digi-Key, Mouser, Farnell element14, Arrow, Avnet (LCSC is not named, but a supplier name or purchase link may be written into the BOM). "No substitutes will be used without getting your approval." Component unit prices in PCBWay's quote "include the shipping cost, customs charge, Labor procurement cost" and extra quantity for attrition; parts imported from overseas distributors "will take us 5-7 working days at least". Unused parts are not returned by default.  
Sources: https://www.pcbway.com/pcb_prototype/Electronic_Components.html ; https://www.pcbway.com/helpcenter/pcb_assembly_ordering/Why_the_unit_cost_of_components_is_higher_than_suppliers_such_as_Digiky_.html ; https://www.pcbway.com/helpcenter/pcb_assembly_ordering/Why_is_online_lead_time_different_from_final_lead_time_for_assembly_order_.html ; https://www.pcbway.com/assembly-faq.html

**F18. Consigned-parts overage rules.** 0603/0805/1206/2225/SOT/SOD/MELF: minimum 50 pieces and at least 30 more than the assembly quantity; 0201/0402/miniMELF: minimum 100 pieces and at least 50 more; ICs, BGA, QFP, connectors: 1-5 extra depending on run size. SMT parts must arrive on one continuous strip or reel (not cut pieces), labelled with BOM line, MPN and quantity, with a packing list. Setup fee applies to very small runs ("we can do even 1 piece for you, as long as you'd like to pay the set-up fee").  
Sources: https://www.pcbway.com/blog/PCB_Basic_Information/PCBWay_Q_A_004___Common_Questions_for_PCB_Assembly_Service_on_PCBWay_02.html ; https://m.pcbway.com/assembly-special-remind.html ; https://www.pcbway.com/blog/PCB_Basic_Information/PCBWay_Q_A_003___Common_Questions_for_PCBA_Ordering_01.html

**F19. Panelization, rails and fiducials for assembly.** Panelization required "when your PCB dimension is smaller than 50mmx100mm, or when your PCB is of any shapes (circular, or odd shape) other than rectangle". Break-away rails required "at the two longer paralleled edges" if copper-to-edge clearance is < 3.5 mm (138 mil) or the board is panelized; rail width >= 3 mm, process edges of 5, 6, 7, 8 or 10 mm offered. Fiducials: 3 per panel, 1.0 mm bare-copper dot (1.0-3.0 mm allowed) with 1.7 mm mask opening, clear area radius 2R, >= 5 mm from the board edge, L-shaped arrangement, placed in the rails; 4 tooling holes (2 mm NPTH) per panel. Panel 50 x 50 mm min, 330 x 530 mm max; V-score gaps 0 or 3 mm; tab-route gap 1.6 mm, mouse-bite holes >= 0.45 mm (0.55-0.6 mm typical), >= 0.35 mm apart, 5-6 per tab, tab width >= 2 mm. "Panel design can be provided by you or we do the panel design according to your request." Extra fab cost applies when one side < 20 mm or both sides < 50 x 50 mm, or > 10 V-cuts, or multiple designs in one panel (minimum US$5 extra).  
Sources: https://www.pcbway.com/assembly-faq.html ; https://www.pcbway.com/pcb_prototype/Panel_Requirements_for_Assembly.html ; https://www.pcbway.com/helpcenter/design_instruction/PCB_Panelization__Breakaway_Rails__Fiducial_Marks__Tooling_Holes.html ; https://www.pcbway.com/helpcenter/paymentproblems/What_PCBs_will_be_charged_of_extra_cost_.html

**F20. Quantities.** Fabrication quote quantities start at 5 pieces (5, 10, 15, 20, 25, 30 ...). Assembly: capability page says "Our minimum is as low as 5 pieces"; Q&A says 1 piece is possible with a setup fee. Stencil is made automatically and included in the assembly quote ("There is no need to submit a stencil order").  
Sources: https://www.pcbway.com/orderonline.aspx ; https://www.pcbway.com/assembly-capabilities.html ; https://www.pcbway.com/helpcenter/pcb_assembly_ordering/Should_I_submit_a_stencil_order_for_SMT_project_made_by_PCBWay_.html

**F21. Lead times (2026-09).** Fabrication: standard PCBs "24 hours" for < 50 pcs and < 1 m^2 after engineering review, 3-4 days for 1-5 m^2; 48 h and 72 h options; Advanced PCB 4-layer 5 days (< 1 m^2), 48 h extra-urgent. The instant quote shows the exact build time per configuration (not published as a table). Assembly: "PCBA lead time 3-5 days" (marketing) and "normally 3 working days for prototypes" (Q&A) after all parts and PCBs are ready; the online lead time "is just the estimated lead time for assembly process only"; "Final lead time is confirmed after passing the audit, and it includes the time for pcb production, components procurement and assembly" and is sent by email; quotation within 1 business day. PCBWay builds the PCBs and stencil while parts are in transit. Factory closures: 2026-09-25 and 2026-10-01 to 10-04 (GMT+8).  
Sources: https://www.pcbway.com/quickturn-pcb-fabrication.html ; https://www.pcbway.com/pcb-assembly.html ; https://www.pcbway.com/blog/PCB_Basic_Information/PCBWay_Q_A_004___Common_Questions_for_PCB_Assembly_Service_on_PCBWay_02.html ; https://www.pcbway.com/helpcenter/pcb_assembly_ordering/Why_is_online_lead_time_different_from_final_lead_time_for_assembly_order_.html ; https://www.pcbway.com/helpcenter/lead_time/

**F22. Cost signals.** 4-layer 100 x 100 mm prototype product page shows "US $48.00" (quantity for that price not stated on the page; minimum order 5; raw HTML shows `4 Layers PCB Prototype ... Price: US $ 48.00`). 2022 announcement: up to 20 % reduction on 4/6-layer and further discount for 5/5 mil and 0.25 mm-hole designs. Assembly marketing: "Only 29$ for 20pcs PCBA" with free stencil (US$15 value). Independent 2020 worked example (10 x Arduino Uno clone): PCB US$5, assembly US$30, parts US$230. Assembly price drivers in the quote form: quantity, sides, number of unique parts, SMD pads, BGA/QFP count, THT count, sourcing mode; the online figure is "an estimated price for assembly only" and the full quotation with quoted BOM arrives by email after review. ENIG adds cost proportional to gold area; impedance control and custom stackup are quoted by engineers (no published surcharge).  
Sources: https://www.pcbway.com/pcb_prototype/4_Layer_pcb/ ; https://www.pcbway.com/blog/News/Big_News_Sale_Promotion_for_Multilayer_PCB_86a5864f.html ; https://www.pcbway.com/pcb-assembly.html ; https://atadiat.com/en/e-first-time-to-order-pcb-assembly-a-guide-to-pcbways-pcba/ ; https://www.pcbway.com/blog/News/How_to_Place_a_PCB_Assembly_Order_at_PCBWay_PCBWay_Website_Exploration_02_021f07fa.html

### G. Testing services

**F23. Bare-board and PCBA tests.** Bare board: E-test (flying probe or fixture) standard; free reports "available upon request": impedance test report, microsection report, thermal stress report, dimensional report. PCBA: AOI, X-ray, flying probe, ICT, functional test including "power consumption and RF/GPS/Bluetooth/Wi-Fi functional testing", MCU/flash programming, burn-in and environmental tests; the customer must "Provide Test Requirement: Test plan / Procedure / Acceptance criteria", PCBWay reviews feasibility and reports results. No spectrum-analyzer or network-analyzer RF characterization service is described; treat PCBWay functional test as go/no-go against a customer procedure.  
Sources: https://www.pcbway.com/oem/quality-control.html ; https://www.pcbway.com/pcb-assembly/pcb-assembly-testing.html

## Implications for cwht

Tags: REQ-candidate (goes to the requirements set through a CR), RISK-candidate (goes to the risk register), DECISION-needed (ADR or trade study), ACTION (task with owner).

### Requirements candidates (fabrication)

- REQ-candidate PCB-FAB-01: The fabrication data package shall be RS-274X Gerbers (F_Cu, In1_Cu, In2_Cu, B_Cu, F_Mask, B_Mask, F_Silkscreen, B_Silkscreen, F_Paste, B_Paste, Edge_Cuts) plus Excellon PTH.drl and NPTH.drl, a Gerber job file, and a README stating layer order and stackup, zipped as one archive. Verification: Inspection (file manifest check script). [F1, F2, F3]
- REQ-candidate PCB-FAB-02: The board shall be manufacturable in PCBWay's Standard PCB class with min trace/space >= 6/6 mil (0.152 mm) outside the RF section, >= 5/5 mil only where the RF or QFN geometry requires, min drill >= 0.3 mm (0.25 mm allowed for QFN escapes), annular ring >= 0.15 mm, mask dam >= 4 mil with green mask, copper-to-edge >= 0.3 mm (>= 3.5 mm or rails, see PCB-ASM-06). Verification: Inspection (KiCad DRC rule set derived from F9). [F9]
- REQ-candidate PCB-FAB-03: The board shall use PCBWay's standard 4-layer through-hole stackup: 1 oz outer / 1 oz inner, 7628 RC46 % prepreg (Dk 4.74, 0.1855 mm laminated at 70 % inner residual copper), FR-4 Tg150 core Dk 4.6; nominal thickness 1.6 mm (or 1.0 mm if the enclosure trade selects it, same outer dielectric). No blind or buried vias. Verification: Inspection of order parameters and PCBWay stackup confirmation. [F5]
- REQ-candidate PCB-FAB-04: All 50 ohm interconnects (PA output to LPF, LPF to antenna connector, receiver front end) shall be microstrip on L1 referenced to a continuous L2 ground, nominal width per the PCBWay-confirmed calculation (first estimate 0.30 mm), and the order shall select "Impedance control" with a stackup drawing that lists each controlled net, layer, reference plane, target 50 ohm +/-5 ohm. Verification: Analysis (calculation) plus Inspection (PCBWay impedance test report requested in order notes). [F6, F7]
- REQ-candidate PCB-FAB-05: Surface finish shall be ENIG (flatness for QFN/DFN and the Pico 2 castellations, lead-free). Verification: Inspection of order. [F9]
- REQ-candidate PCB-FAB-06: The design shall keep inner-layer residual copper >= 60 % (solid L2 ground, L3 mostly power/ground) so PCBWay's 70 % stackup variant applies and the outer dielectric is 0.1855 mm. Verification: Analysis (copper area script on In1/In2 Gerbers). [F5, F6]

### Requirements candidates (assembly)

- REQ-candidate PCB-ASM-01: The BOM shall be an .xlsx following PCBWay's template columns (Item #, Designator, Qty, Manufacturer, Mfg Part #, Description/Value, Package/Footprint, Type, Notes) with manufacturer and MPN for every line, distributor part number where known, `DNS` in Type for do-not-place parts, and a supplier link where a specific source is mandatory (for example Pico 2 from an authorized Raspberry Pi reseller). Verification: Inspection (BOM schema check). [F11]
- REQ-candidate PCB-ASM-02: The centroid file shall be generated from KiCad with units mm, drill/place origin at the board lower-left corner, SMD footprints only (THT excluded), DNP footprints excluded, single file with a Top/Bottom side column, no negative-X mirroring, and shall list exactly the SMD designators in the BOM. Verification: Inspection (script cross-checking BOM, CPL and silkscreen designators). [F3, F12]
- REQ-candidate PCB-ASM-03: Every polarized or keyed part (diodes, LEDs, electrolytic/tantalum capacitors, ICs, connectors, the Pico 2 module) shall carry a pin-1 or polarity mark on the silkscreen outside the pad area, and an assembly drawing (PDF render of F.Fab/B.Fab with rotations) shall be delivered with the package. Verification: Inspection (rendered image review per charter rule 3). [F13]
- REQ-candidate PCB-ASM-04: Passive packages shall be 0603 or larger unless RF performance requires 0402; no 0201 or 01005. QFN/DFN pitch >= 0.5 mm preferred; if 0.4 mm is used, ENIG and mask-defined dams per F9 apply. Verification: Inspection (footprint audit). [F15]
- REQ-candidate PCB-ASM-05: The Pico 2 footprint shall follow datasheet Figure 5 (castellated pads, test-point pads, USB shell ground pads A-D) with paste apertures enlarged to about 163 % of pad area as the datasheet recommends, since PCBWay cuts the stencil from F_Paste. Verification: Inspection (footprint review against datasheet) and Test (first-article X-ray or visual fillet inspection). [F16]
- REQ-candidate PCB-ASM-06: If any board edge has copper or components closer than 3.5 mm, or the board is smaller than 50 x 100 mm, the deliverable shall be a panel with two >= 5 mm rails on the long edges, three 1.0 mm fiducials (1.7 mm mask opening) in the rails, and 2 mm tooling holes, or the order shall explicitly request PCBWay panel design. Verification: Inspection. [F19]
- REQ-candidate PCB-ASM-07: The key/paddle jack shall be a 3-conductor (TRS) jack wired tip = dit/straight key, ring = dah, sleeve = common, so a straight key (tip-sleeve) and an iambic paddle (tip-ring-sleeve) are both supported without configuration hardware; the jack shall be a THT part with a PCBWay-placeable footprint and a manufacturer MPN. Note: this reflects the owner's stated core requirement that both straight keys and iambic paddles be supported; the electrical debouncing and keyer mode selection belong to the firmware and electrical requirement sets. Verification: Test (bench, both key types). [owner statement 2026-09-25; F15]
- REQ-candidate PCB-ASM-08: Double-sided placement shall be avoided in the first build (all SMT on top, THT connectors and jacks on top where possible) to remove the second reflow pass and the module-on-bottom risk. Verification: Inspection. [F15]

### Risks

- RISK-candidate R-PCB-01: Centroid rotation mismatch between KiCad footprint zero references and PCBWay's library causes mis-oriented ICs or the Pico 2. Mitigation: assembly drawing with rotations, pin-1 silk marks, request PCBWay's placement preview before the run. [F12]
- RISK-candidate R-PCB-02: PCBWay has no published commitment to reflow castellated modules; the Pico 2 may be refused or hand-soldered, and the datasheet gives no MSL or reflow-profile limit. Mitigation: pre-CDR written confirmation from PCBWay sales; fall-back is consigned Pico 2 with hand-solder instruction, or bare RP2350 design (out of current scope). [F16]
- RISK-candidate R-PCB-03: Impedance of outer-layer microstrip is only verified without solder mask, and PCBWay may alter trace width to hit target. Mitigation: request masked-trace impedance confirmation, keep RF traces short, and verify with NanoVNA at TRR. [F6, F7]
- RISK-candidate R-PCB-04: Parts import into China adds >= 5-7 working days and holiday closures (2026-10-01 to 10-04) extend lead time; single-source parts may be substituted only with approval, but approvals stall the schedule. Mitigation: BOM with approved alternates listed at CDR; order after CDR closure but before holidays. [F17, F21]
- RISK-candidate R-PCB-05: Component pricing through PCBWay includes shipping, customs and attrition, so 5-board BOM cost may be 1.5-2x distributor list; small passives are bought in overage quantities. Mitigation: cost estimate at CDR using PCBWay's rules; consider consigning only expensive parts (combo mode). [F17, F18, F22]
- RISK-candidate R-PCB-06: A pocket-size board below 50 mm on one side triggers panelization, rails and extra fab charges, and changes the enclosure interface if rails are removed by hand. Mitigation: decide panel vs single at PDR; specify mouse-bite or V-score removal and post-depanel edge finish. [F19]
- RISK-candidate R-PCB-07: Dk of PCBWay's 7628 (4.74) and core (4.6) are stated without test frequency; the effective value at 144 MHz may differ by a few percent. Impact is small at 144 MHz (roughly 1 ohm on a 50 ohm line), so accept; do not use FR-4 for any high-Q printed element. [F5, F6]

### Decisions needed

- DECISION-needed D-PCB-01: Board thickness 1.6 mm vs 1.0 mm (enclosure and connector fit vs stiffness); outer-layer 50 ohm geometry is unchanged, so this is a mechanical trade. [F5, F6]
- DECISION-needed D-PCB-02: FR-4 Tg150 (Standard PCB) vs Rogers hybrid (Advanced PCB) for the RF section; recommendation is FR-4 at 144 MHz, record as ADR with the loss estimate. [F8]
- DECISION-needed D-PCB-03: Sourcing mode: full turnkey vs combo (consign Pico 2, LCD, encoder, jacks, battery holder; turnkey passives and ICs). [F17, F18]
- DECISION-needed D-PCB-04: Single board with >= 3.5 mm copper-free edges vs panel with rails; interacts with enclosure and the 0.25 mm copper-to-edge fab limit. [F9, F19]
- DECISION-needed D-PCB-05: Functional test at PCBWay (power-on, current, USB enumeration of the Pico 2 firmware) using a customer test procedure vs all functional test on the owner's bench at TRR. [F23]

### Actions

- ACTION A-PCB-01: Before CDR, email PCBWay (service@pcbway.com) with the Pico 2 datasheet footprint and ask (a) whether they reflow castellated modules in turnkey assembly, (b) required part format for SC1631 (bulk/tray) and any baking, (c) rotation convention they expect for KiCad .pos files, (d) whether they accept KiCad X2 Gerbers, (e) impedance-control surcharge and whether coupons/TDR report are included for a 5-piece order. Attach the reply to the CDR package.
- ACTION A-PCB-02: Run PCBWay's impedance calculator with the F5 stackup numbers and record the result next to the local estimate (F6) in the RF analysis note; request PCBWay engineering confirmation at order.
- ACTION A-PCB-03: Add KiCad DRC rules and a fabrication-output script that produce the exact file set in PCB-FAB-01 and PCB-ASM-02, and a checker that cross-references BOM, CPL and silkscreen designators.
- ACTION A-PCB-04: Create or qualify a Pico 2 SMD footprint (start from the official KiCad `RaspberryPi_Pico_SMD_HandSolder` outline, add test-point and USB-shell pads and 163 % paste per datasheet), render it and inspect against Figure 5.
- ACTION A-PCB-05: Produce a cost and lead-time estimate for 5 assembled boards using the instant quote (fab), the assembly estimator and a BOM priced at distributor plus PCBWay's stated overheads; log the date because PCBWay prices change.

## Confidence

| Finding | Confidence | Basis |
|---|---|---|
| F1 Gerber set and format | High | Two PCBWay help pages agree |
| F2 KiCad names recognized | High (outer/paste/drill), Medium (inner-layer names) | PCBWay extension table; inner names not listed |
| F3 KiCad 9 option semantics | High | KiCad 9.0.9 manual text extracted verbatim |
| F4 Layer orientation | High | PCBWay page quoted |
| F5 Standard 4-layer stackups | High | Values parsed from PCBWay HTML, cross-checked against WebFetch summary |
| F6 50 ohm estimate | Medium | Own closed-form calculation; PCBWay states it recalculates; mask effect approximate |
| F7 Impedance tolerance and report | Medium-High | Tolerance from capabilities table; report listed as "on request"; coupon/TDR method not described |
| F8 Rogers availability | Medium | Product page; no 4-layer hybrid price found |
| F9 DFM limits | High for starred items (raw HTML), Medium for others (summarized fetch) | |
| F10 Assembly file set | High | Three PCBWay pages agree |
| F11 BOM columns and DNS marking | High | Template downloaded and parsed |
| F12 Centroid format | High (format), Medium (rotation handling) | Sample file parsed; rotation zero reference not defined by PCBWay |
| F13 Silkscreen/polarity | High | PCBWay guide |
| F14 KiCad plugin | Medium | README only; open issues |
| F15 Assembly capabilities | High | Capability pages and FAQ |
| F16 Pico 2 as module | High (datasheet facts), Low (PCBWay acceptance) | Datasheet text extracted; no PCBWay statement found |
| F17 Sourcing models | High | PCBWay pages quoted |
| F18 Consigned overages | High | Two PCBWay pages agree |
| F19 Panelization/fiducials | High | Three PCBWay pages agree |
| F20 Quantities | High | Quote form and Q&A |
| F21 Lead times | Medium | Marketing figures plus help pages; exact 4-layer prototype build time only in quote tool |
| F22 Cost signals | Low-Medium | Price page quantity ambiguous; examples dated 2020-2022 |
| F23 Testing services | Medium | Service pages; no RF characterization service |

## Open items

1. Written PCBWay confirmation that a castellated Pico 2 module will be reflowed in turnkey assembly, plus their handling requirements (A-PCB-01).
2. Pico 2 MSL rating, allowable reflow profile and any tape-and-reel SKU; the datasheet lists only SC1631 bulk.
3. Exact standard build time and price for 5 pieces of the cwht board size in 4 layers with ENIG and impedance control (only available through the quote tool; record with date).
4. Whether PCBWay accepts KiCad X2 Gerber attributes and In1_Cu/In2_Cu naming without renaming (expected yes; confirm).
5. PCBWay's zero-degree rotation reference for the CPL and whether they publish a placement preview for approval.
6. Impedance-control surcharge for prototype quantities and whether coupons and TDR are run on a 5-piece order or only "random check".
7. Test frequency of the quoted Dk values (4.74 prepreg, 4.6 core).
8. Whether LCSC-stocked parts can be specified by LCSC part number in turnkey mode (PCBWay names Digi-Key, Mouser, Farnell, Arrow, Avnet only, but accepts supplier links).
9. Official KiCad Pico 2 footprint release status (datasheet changelog: link removed until ready).

## CDR package checklist (PCBWay turnkey, 4-layer RF board)

Fabrication data
- [ ] One .zip with RS-274X Gerbers for F_Cu, In1_Cu, In2_Cu, B_Cu, F_Mask, B_Mask, F_Silkscreen, B_Silkscreen, F_Paste, B_Paste, Edge_Cuts; Excellon PTH.drl and NPTH.drl (separate); Gerber job file; README with layer order, stackup, finish, mask colour, impedance nets.
- [ ] KiCad plot settings recorded: zone fills checked before plot, drill/place origin at board lower-left, X2 off unless PCBWay confirms, aperture macros enabled, oval holes as route commands.
- [ ] Bottom-layer Gerbers appear mirrored when viewed from top (KiCad default); TOP/BOT copper labels present.
- [ ] Board outline closed and single; no copper within 0.3 mm of edge (0.25 mm limit) except intentional.
- [ ] DRC passes against a rule set encoding F9 (trace/space class chosen, drill >= 0.25/0.3 mm, annular >= 0.15 mm, mask dam >= 0.1 mm, slot >= 0.5/0.8 mm).
- [ ] Order parameters: 4 layers, FR-4 (Tg150), 1.6 mm (or 1.0 mm per D-PCB-01), 1 oz outer / 1 oz inner, ENIG, green mask, impedance control = yes, custom stackup = no (standard 7628/core), quantity 5 (or 10 if unit price is close).

Stackup and RF
- [ ] Stackup drawing referencing PCBWay standard 4-layer 1.6 mm: 7628 RC46 % Dk 4.74 0.1855 mm; core 1.03 mm Dk 4.6; inner residual copper >= 60 %.
- [ ] Impedance table: net, layer, reference plane, width, target 50 ohm +/-5 ohm, with local calculation and PCBWay calculator screenshot; note mask effect.
- [ ] Order notes request the impedance test report and state whether measurement is with or without mask.
- [ ] Rogers decision recorded as ADR (D-PCB-02).

Assembly data
- [ ] BOM .xlsx in PCBWay template columns; every line has Manufacturer and MPN; distributor P/N and link for critical parts; DNS in Type for do-not-place; approved alternates listed in Notes.
- [ ] CPL from KiCad: mm, drill/place origin, SMD only, DNP excluded, single file with side column, no negative X; designator set equals BOM SMD set.
- [ ] Silkscreen shows every designator and pin-1/polarity marks; assembly drawing PDF (F.Fab/B.Fab render with rotations) attached; rendered image reviewed per charter rule 3.
- [ ] Solder paste layer present for all SMD pads; Pico 2 pads over-pasted about 163 %; no paste on test points not used.
- [ ] Packages: no 0201/01005; QFN/DFN pitch documented; via-in-pad avoided or resin-filled specified.
- [ ] Single-side placement confirmed or second side justified.
- [ ] Assembly quote inputs recorded: quantity, unique parts, SMD pad count, QFN count, THT count, sourcing mode.

Pico 2 module
- [ ] PCBWay written confirmation on module reflow attached (A-PCB-01).
- [ ] Footprint matches datasheet Figure 5 including USB shell pads A-D and test-point pads; copper voided under unused test points.
- [ ] Pico 2 (SC1631, no headers) on the BOM with authorized-reseller link; format bulk/tray acceptable to PCBWay.

Panel and DFA
- [ ] Copper and components >= 3.5 mm from the two long edges, or panel with >= 5 mm rails, 3 fiducials 1.0 mm / 1.7 mm mask opening in rails, 2 mm tooling holes, tab-route gaps 1.6 mm with 0.55-0.6 mm mouse bites, or PCBWay panel-design request in notes.
- [ ] Board size versus the 50 x 100 mm panelization threshold and the < 20 mm / < 50 x 50 mm surcharge checked.

Sourcing, schedule, cost
- [ ] Sourcing mode decided (D-PCB-03); consigned parts list with overage quantities per F18 and labelling plan if combo.
- [ ] Lead-time plan: quote response 1 business day, parts import >= 5-7 working days, assembly ~3 days, shipping; holiday calendar checked.
- [ ] Cost estimate for 5 assembled boards with date; contingency for PCBWay component overheads.

Verification hooks
- [ ] V&V matrix rows for PCB-FAB-01..06 and PCB-ASM-01..08 with methods (Inspection scripts, Analysis, Bench test at TRR).
- [ ] Bench procedure for NanoVNA check of the 50 ohm path and for straight-key and iambic-paddle jack test (PCB-ASM-07).
