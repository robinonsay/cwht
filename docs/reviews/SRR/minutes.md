# SRR session minutes

Review: SRR (combined with MCR). Session type: pre-review session per package section 2 (the gate review is not convened until the readiness declaration can be made). Package: `docs/reviews/SRR/package.md`, revision 8 final with the lead SE current-status edit and Minors M1 to M4 (`a6d0959`). Deck: `docs/reviews/SRR/slides/srr.adoc` at `64e53ee`, read with the section 2.2 read-aloud corrections.

Chair, Decision Authority, ETA and SMA TA: Robin Onsay (owner). Presenter: Claude (lead systems engineer).

Chat statements by the owner are transcribed verbatim, as charter section 4 item 4 requires.

## 2026-09-26

### Agenda order

The owner asked why the FW-B0 flash (OA-1, OA-2) came before the review. The presenter moved it to the end of the session, before the disposition; it has no dependency on the review content. The owner may also defer it to PDR as a tailoring decision.

### Deck read-through

The owner reviewed all 42 slides as a PDF before the walk-through, with the read-aloud corrections of package section 2.2 given in chat.

### Rulings

Owner statement, verbatim: "I concur with your recommendations for the key decisions."

Recorded ruling: key decisions K1 to K17 of package section 13.1.1 are ruled as recommended. That covers decisions 36, 37, 41, 42 (K1); 38, 39, 40, 9, 33 (K2); 6, 7, 8 (K3); 14, 11, 32, 3 (K4); 17, 18, 19, 20 (K5); 63, 64 (K6); 70, 72, 73, 74, 75, 76, 85 (K7); 53, 54, 55, 58 (K8); 107, 110 (K9); 108, 109 (K10); 105, 106, 111 (K11); 30, 113, 29, 25 (K12); 90, 86 (K13); 104, 112 (K14); 114 (K15); 47 (K16); 115, 118 (K17). Each ruling's text is the "Recommendation" cell of its row in `decisions-for-owner.md` Part 1.

Open, not yet ruled: the consent agenda of package section 13.1.2; the candidate RIDs of section 15; the proposed tailoring of section 17; the owner's readiness confirmation (row S1); OA-1 and OA-2.

Consequences for the record: the five open Major findings that waited on these rulings (INSP-003 finding-6, INSP-011 F-01 and F-04, INSP-016 F-01 and F-02) can now close through the post-ruling work R16, verified by the reviewers. Decision 109 approves the four toolchain downloads, and decision 110 sets the rustos licence to MIT and approves the manifest work item.

### Owner requests

The owner asked for a plain-language summary of the L1 and L2 requirements and of the ConOps. It is provided as `docs/reviews/SRR/plain-language-summary.md`, a reading aid that is not a controlled product, after an independent fact check against the sources.

### Traceability approach

The owner asked how bidirectional traceability of requirements to design, code, test and V&V will work. The presenter answered from charter section 7, 02 sections 7 and 8, 03 section 8, 04 section 5 and 07 CS-24:
- the link table and its enforcement gates;
- the `@req`, `@design` and `@verify` code tags;
- the orphan checks;
- the credit rules for Verified and Closed;
- the verification and validation matrices;
- `--regression` change impact.

The presenter also recommended adding a requirement field to the safety-critical hardware parts (the hardware transmit timer, the cell protection ICs and the headphone limiter) at PDR.

### Disposition

Owner statement, verbatim: "I approve of this and the SRR."

Recorded by the presenter:
- The traceability approach is approved, including the PDR requirement field on safety-critical hardware parts.
- SRR disposition: **Approved with liens**, the requested disposition of package section 21, with liens L-1 to L-7 of section 20.1.
- The approval adopts the consent agenda of section 13.1.2 as recommended, adopts the candidate RIDs of section 15 as the package recommends, approves the proposed tailoring of section 17, and confirms readiness (row S1).
- OA-1 and OA-2, the FW-B0 flash and picotool verify, were not performed. They are recorded as deferred to PDR under the owner's approval, as a tailoring of the owner part of entrance row 20. The owner was told so in the same exchange and may reverse it.
- The post-ruling work R16 is performed next and verified by the reviewers.
- The baseline tag `baseline/srr` is applied after R16 is verified, so that the functional baseline carries the rulings.

### OA-1 and OA-2 performed (deferral reversed)

The owner brought the Pico 2 during the session. Owner statement, verbatim: "I grabbed the pico so I'm ready to test the flash whenever you are." The deferral to PDR recorded above is therefore reversed. The board was marked "1"; chip id `0xf9c6e0eff60605d1`, RP2350, 4096K flash. Claude ran every command.

| Step | Image and command | Result | Owner observation (verbatim) | Verdict |
|---|---|---|---|---|
| TC-SW-TOOL-001 step 11 (OA-1) | `rustos-blinky.uf2` (sha256 `c45b5268...08d3`): `picotool info -d`, `picotool load -v`, `picotool reboot`, 19:17 to 19:18 CDT | load and verify OK, reboot exit 0 | "On/Off time looks about equal and it blinked about 60-63 times in 60s. It's not exactly 1 second but its close" | Pass: 60 to 63 cycles in 60 s, window 10 to 120, predicted about 63 |
| TC-SW-TOOL-001 step 12 (OA-1) | `cwht-app.uf2` (sha256 `4e0bd133...3529`): the same commands, 19:20 CDT | load and verify OK, reboot exit 0 | "Yes that looks correct", then "18 in 60s" | Pass: 18 cycles in 60 s, window 3 to 45, predicted about 16 |
| OA-2 picotool verify known answer | `kat-target.uf2`, from `picotool uf2 convert` (sha256 `f8ef643e...c093`, equal to the known answer), loaded; `picotool verify kat-target.elf`; then a copy with one byte flipped at flash `0x1000002f`, 19:23 CDT | true image OK (exit 0); altered copy "First mismatch at 0x1000002f", exit 245 | none needed | Pass |

Raw outputs are filed with the TC-SW-TOOL-001 run 4 report after the close-out run finishes. This closes the owner part of entrance row 20. INSP-016 re-verifies the evidence.

### Schedule and enclosure inputs (after the disposition)

Owner statement on the schedule, verbatim: "But in general, I agree with the schedule. I'm fine with, you know, slipping the schedule I'd rather do it right." The proposed rebaseline is approved:
- PDR about Tue 2026-09-29;
- CDR and orders about Sat 2026-10-03 to Sun 2026-10-04, with PCBWay closed 10-01 to 10-04;
- boards about 10-20 to 10-23;
- enclosures and TRR about 10-22 to 10-27.

`docs/plan/schedule.md` is updated after the close-out run, with an INSP-023 delta re-issue.

Owner input on the enclosure, verbatim: "something we should consider for the enclosure for the radio is a like cots um, aluminum or metal box that we can buy from like Amazon or some other provider uh, instead of getting it CNC'd, which might be cheaper. Uh, and building it to that specification rather than CNCing our own. Um, another thought is like 3D printing with the H2C uh, and coating it with like a spray a metal spray paint, which we've done before on other projects, and it has been you know RF proof uh, quote unquote. Uh, we've been able to verify that it like um, you know would uh, limit EMI for GPS testing. So like that might be another possibility."

Lead SE disposition:
- The input is recorded as a new stakeholder input, SI-037.
- REQ-SYS-109 (CNC-machined aluminum enclosure, anodized) names a solution. A change request (CR-003) is drafted to make it solution-neutral, keeping every performance requirement the enclosure carries:
  - thermal: REQ-SYS-112 and 113;
  - shielding: REQ-SYS-177;
  - antenna-port load: REQ-SYS-105;
  - drop and rain: REQ-SYS-116 and 117;
  - legend: REQ-SYS-124;
  - edges and clearance: REQ-SYS-110 and 111;
  - envelope and mass: REQ-SYS-102 and 103.
- The CR goes to the owner for disposition after `baseline/srr` is tagged, so the tag carries exactly what was approved at SRR.
- An enclosure trade study for PDR compares four options:
  - (A) PCBWay CNC aluminum;
  - (B) a catalog extruded-aluminum box from DigiKey or Mouser, machined by the owner or by PCBWay secondary operations;
  - (C) an H2C print with a conductive metal coating;
  - (D) a hybrid of an extruded aluminum body with printed front and end parts.

Owner preference, verbatim: "I like option C plus we could buy a heat sink to place in the enclosure." This is recorded with SI-037 as the owner's preferred enclosure concept: an H2C-printed case with a conductive metal coating and a purchased heatsink. It becomes the planning baseline of the PDR enclosure trade study. The study confirms it with a thermal analysis and a shielding measurement, or reports the gap. CR-003 makes REQ-SYS-109 solution-neutral and amends REQ-SYS-124 ("marked into its enclosure metal") so that a printed case can comply.

Owner direction, verbatim, superseding the option C preference above: "Actually, I want to try both B and the 3d printed option. I don't have any machining tools so we would need someone else to drill the holes..."

Recorded:
- The PDR enclosure trade carries B and C as parallel prototypes on one common board and envelope:
  - B: a catalog extruded aluminum box, with no owner machining;
  - C: an H2C-printed case with a conductive coating and a purchased heatsink.
- Selection happens on bench thermal and shielding measurements before the delivered-unit configuration is fixed.
- The owner has no machining tools, so B must reach the owner with every opening already cut. The trade study evaluates these routes:
  - (1) an enclosure style whose face and end plates are separate flat panels, ordered cut to drawing, either as PCBWay CNC aluminum plates or as bare PCB panels in the same PCBWay order (copper for shielding, silkscreen for the legend), so that the extruded body needs no holes;
  - (2) a machining-to-drawing service for catalog enclosures, whose capability, quote and lead time the study must confirm;
  - (3) PCBWay CNC of the complete box (option A) as the fallback.
