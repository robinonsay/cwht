# ADR-008: Enclosure authored in OpenSCAD, exported to STEP through headless FreeCAD, machined by PCBWay CNC in aluminum

| Field | Value |
|---|---|
| ID | ADR-008 |
| Status | Accepted |
| Date proposed | 2026-09-25 |
| Date decided | 2026-09-25 |
| Decision authority | Robin (owner; the decision fixes the enclosure source format and spends money at CDR) |
| Author | Claude (technical data manager invocation, 2026-09-25) |
| Independent reviewer | Pending: reviewer agent invocation before SRR (01 section 3.2 row S3; 06 section 14.2) |
| Life-cycle phase | Pre-A / A |
| Baseline affected | baseline/srr (functional baseline); product baseline at CDR carries the STEP and drawing |
| Change request | none (pre-baseline) |

## 1. Context

The owner wants an aluminum enclosure with the antenna on one end, designed in OpenSCAD and CNC-machined by PCBWay (SI-008). PCBWay accepts only B-rep formats (STEP, X_T, IGES, SLDPRT) for CNC and refuses STL and mesh-derived STEP; OpenSCAD has no STEP export in any version. The gap is closed by FreeCAD's OpenSCAD workbench, which rebuilds true B-rep solids from OpenSCAD's CSG tree and exports STEP from the command line; the owner approved installing FreeCAD via Homebrew for that purpose (SI-032). The charter's headless rule (11.8) forbids any GUI automation, so the pipeline must be scriptable end to end.

- Driving inputs and expectations: SI-008, SI-032, SI-012 (H2C prints for fit checks), SI-016 (renders inspected), SI-001 (pocket form factor)
- Requirements that constrain the decision: none yet
- Hazards in play: HZ-003 (PA heat path through the machined enclosure); none new
- Research consulted: `docs/research/enclosure-cnc-and-openscad-pipeline.md` A1 (STEP required; STL and STL-derived STEP refused), A2 (2D drawing required for threads, tolerances, marking), A3 (alloys 6061, 7075, 5052, 2A12), A4 (finishes; bead blast plus Type II anodize), A5 (ISO 2768-m default; class f by callout), A6 (pocket radius, wall, depth rules), A7 (threads as pilot holes, tap before anodize), A10 (price signals USD 250 to 370 class), A11 (SLA print as a second-tier fit check), B1 (no STEP in OpenSCAD; 2021.01 stable, 2026.09.23 snapshot), B2 (OpenSCAD CLI renders verified), B3 (mesh to STEP unacceptable), B4 (FreeCAD workbench: primitives, booleans, extrusions become B-rep; hull, minkowski, text, non-uniform scale degrade), B5 (FreeCAD 1.1.3 cask with `freecadcmd`), B6 (build123d and CadQuery alternative), "Recommended pipeline"; `docs/research/verification-tooling-inventory.md` F11 (OpenSCAD 2021.01 installed under Rosetta; snapshot exists); `docs/research/antenna-and-erp.md` F8 (SMA jack bulkhead-retained by an enclosure boss so the PCB carries no antenna bending moment)
- Guidance consulted: charter section 11 rule 8 (headless only); SWE-136 (tool accreditation, applied to the CAD toolchain as an engineering tool); SE HB §6.8

## 2. Decision

The enclosure source is OpenSCAD in a restricted dialect: primitives (cube, cylinder, sphere, polyhedron), booleans, `linear_extrude`, `rotate_extrude`, `offset` and rigid transforms only; no `hull`, `minkowski`, `text`, `resize` or non-uniform `scale` in any machined solid. The build is a script (`tools/scad2step.py`, to be written): `openscad -o part.csg part.scad` for the CSG tree and PNG renders, then `freecadcmd` imports the CSG through the OpenSCAD workbench and exports STEP AP214 (single solid per machined part), then acceptance checks run and are logged: valid STEP, exactly one solid, no BSpline faces, volume within tolerance of the OpenSCAD mesh volume. The machined parts are ordered from PCBWay CNC in aluminum 6061 with bead blast plus Type II anodize (proposed finish), with a 2D PDF drawing carrying every toleranced dimension, thread (modeled as tap-drill pilot holes, M3 minimum), roughness, marking and anodize-masking callout (chassis ground and the SMA boss contact area left conductive). The antenna SMA jack is retained by an enclosure boss. Fit checks are printed on the owner's H2C from the OpenSCAD 3MF; an SLA print of the CDR-baselined STEP is optional when a plus or minus 0.2 mm fit matters. FreeCAD is installed by `brew install --cask freecad` (SI-032).

## 3. Alternatives considered

| Option | Description | Why not chosen (or why chosen) |
|---|---|---|
| A (chosen) | OpenSCAD restricted dialect, FreeCAD headless CSG to STEP, PCBWay CNC 6061 | Owner direction (SI-008, SI-032); B-rep STEP with analytic cylinders and planes; fully scriptable |
| B | build123d or CadQuery Python source with native STEP export | Not chosen: departs from the owner's OpenSCAD direction; kept as the PDR prototype comparison (research recommendation) and as the fallback if the STEP acceptance checks fail |
| C | OpenSCAD STL converted to STEP | Rejected: PCBWay refuses mesh-derived STEP (A1, B3); one planar face per triangle |
| D | FreeCAD or another parametric CAD as the source | Rejected: the owner named OpenSCAD; GUI-centric authoring conflicts with the headless rule |
| E | 3D-printed enclosure only | Rejected by SI-008 (aluminum); the PA thermal path needs metal (HZ-003) |

No trade study: the owner named the source format and the vendor; the alloy and finish are class 2 proposals recorded here for PDR.

## 4. Consequences

### 4.1 Requirements created or changed

| Requirement | Relationship | Note |
|---|---|---|
| REQ-SYS-NNN (enclosure constraint: machined aluminum, antenna on one end, OpenSCAD source; L1 author allocates) | new, constraint traced to SI-008 | |
| REQ-ME-NNN (design data package: single-solid STEP AP214 or AP242 per part, 2D drawing, SVG marking artwork; no mesh-derived STEP) | new at PDR, self-derived from this ADR | Basis A1, A2, B3 |
| REQ-ME-NNN (DFM rules: internal radius at least 1.3 times cutter radius and one third of pocket depth, minimum wall 1.5 mm, depth-to-width at most 4, threads M3 minimum as 2.5 mm pilot holes) | new at PDR, self-derived from this ADR | Basis A6, A7 |
| REQ-ME-NNN (anodize masking of chassis-ground and SMA boss contact areas) | new at PDR | Basis A4 and the RF ground need |
| REQ-ME-NNN (SMA jack retained by the enclosure boss; PCB carries no antenna moment) | new at PDR | `antenna-and-erp.md` F8 |
| REQ-SYS-NNN or tooling rule (CAD build reproducible from the command line with logged acceptance checks) | new, self-derived from this ADR | charter 11.3 and 11.8 |

### 4.2 Interfaces, design and code

- ICDs affected: `ICD-TX-ANT` (SMA jack mechanical retention), a PCB-to-enclosure mechanical ICD at PDR (bosses, board thickness 1.0 mm pending boss layout, display window, connector openings)
- Design elements created or changed: `hardware/enclosure/*.scad`, `tools/scad2step.py`, `tools/toolchain.lock.md` entries for OpenSCAD (exact build) and FreeCAD 1.1.3
- New `SW-<SUB>` modules created by this ADR: none
- ICDs created by this ADR: none (created by the ICD process at PDR)

### 4.3 Verification and safety

- Verification cases to add or change: TC-ME-NNN (STEP acceptance checks, Inspection by tool), TC-ME-NNN (printed fit check of PCB, display, jacks, USB opening, Demonstration), TC-ME-NNN (receipt inspection of the machined parts against the drawing; CMM report on the mounting pattern optional)
- Evidence class implications: Inspection by rendered images (charter 11.3) and by the acceptance script; a tool-validation record `TV-NNN` for the CAD chain (05 section 9.2)
- Hazard analysis update required: no (HZ-003 thermal path is a design consequence, handled at PDR)
- Safety-critical software scope changed: no

### 4.4 Cost, schedule, risk

- Enclosure cost: USD 250 to 370 class per small anodized aluminum order (A10, 2023 prices, Medium confidence); lead time 3 to 5 business days machining plus 13 to 15 days observed end to end
- Gate affected: PDR (smoke-test shell through the pipeline, first PCBWay instant quote), CDR (STEP and drawing baselined)
- Risks opened, closed or re-scored: RSK-006 (thermal path) stays open; new risks proposed: "FreeCAD import fidelity degrades silently if a forbidden construct enters the source" (control: acceptance checks), "tolerance statements conflict between PCBWay pages" (control: explicit callouts), "OpenSCAD toolchain age and snapshot behaviour change" (control: pin exact build)
- TPMs affected: TPM-001 (mass), TPM-014 (unit cost)

## 5. Compliance and tailoring

none (engineering tools are Class E by App. D and controlled as configuration items with SWE-136 accreditation, 03 section 1)

## 6. Decision record

> Owner (2026-09-25, SI-008): "Fits an aluminum enclosure with the antenna on one end; enclosure designed in OpenSCAD and CNC-machined by PCBWay."

> Owner (2026-09-25, SI-032): "FreeCAD installation via Homebrew approved for headless OpenSCAD-to-STEP export."

Transcribed from chat into `stakeholder-inputs.md`.

## 7. Related

- Supersedes: none
- Superseded by: none
- Trade study: none (the alloy and finish are class 2)
- Review where presented: SRR; pipeline proof (smoke-test shell STEP and its acceptance log) at PDR
- Revisit conditions: the PDR smoke-test STEP fails the acceptance checks or PCBWay's engineering review rejects it (then option B by a superseding ADR); the owner asks for a printed enclosure for a prototype unit
