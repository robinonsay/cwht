---
# Peer-review record front matter (charter section 5; docs/process/01-lifecycle-and-reviews.md
# section 13 is the single field list; docs/process/08-agent-briefing.md section 3.2).
id: INSP-002
checklist: peer-review-checklist-design
checklist_revision: B
checklist_file: docs/reviews/SRR/checklists/conops-and-concept.md
# product: the SE-36 concept definition, reviewed as one product: the ConOps (operational view) with
# its figures, the concept description (technical view) and the concept block diagram render.
product: docs/conops/conops.md
# product_commit: iteration 3 review baseline, HEAD adcfe0946d2f1b5cd8f41a8f91eb4219a7fb99a1 (2026-09-26);
# iterations 1 and 2 reviewed 28e49e6 and the uncommitted working tree (blob tables in the body)
product_commit: "adcfe09"
# product_files: committed blobs reviewed at iteration 3 (git rev-parse HEAD:<path> at adcfe09); equal to HEAD 860e84e at re-issue 2.
# iteration 2 (working tree, not in the object store): conops.md@b2e93594, concept.md@f9c4af43; the six figure files are unchanged
product_files: ["docs/conops/conops.md@b2c76c80b199bc5021535a612617871a1b20554e", "docs/conops/figures/conops-context.mmd@55ebae2e15589bf9951456dc04400b7ccb96ea27", "docs/conops/figures/conops-context.png@2e4647f81c61a1d2df05637efa3ee3d71a506e09", "docs/conops/figures/conops-modes.mmd@829a46f800db84ae5196cf3946d4376eb813fc0f", "docs/conops/figures/conops-modes.png@b3a08b6770c7c019b67e4b19cd2cdcbba3e8ce6c", "docs/design/concept.md@729190a21066f27525fe5d6e5160e3fa4d22e21b", "docs/reviews/SRR/figures/concept-block-diagram.png@3ef6e911d5201ce0a88c9f2d358b6d85dc425038", "docs/reviews/SRR/figures/concept-block-diagram.py@3806a3449d3bfe3e14dde14726bc1466b94e36af"]
product_size: ConOps 865 lines at iteration 1, 866 at iteration 2, 867 at iteration 3 (22 scenarios, 9 modes, 25 transitions, 20 causes, appendices A to D); concept 365 lines at iteration 1, 381 at iterations 2 and 3 (22 blocks, 10 functions, 18 ICDs, 6 trade studies); 3 renders
sprint: SRR-prep
author_agent: "author:conops-concept (Claude main session, lead systems engineer: ConOps revision 2 at commit 28e49e6, fixes committed at 8a37f8e, appendix D statuses at 1543c9f; concept description and the three renders revised by the H10 author run, committed at 8a37f8e)"
reviewer_agent: "reviewer:conops-concept"
# criticality and assurance: the ConOps and concept are not products of 07 sections 2.1.1 or 14.1
criticality: neither
assurance_required: false
assurance_reviewer_agent: none
iteration: 3
# readiness_met: true at the re-issue of 2026-09-26: R4 met by the author self-check filed at 5b1f2cf (package item R7),
# verified by the reviewer without a further product review (package item R8); R1 Yes, R2 N/A, R3 N/A
readiness_met: true
# reviewer_verdict: APPROVED with liens finding-19 to finding-22 (convergence rule, charter section 4 item 3); no Major open
# verdict: held at NEEDS CHANGES at the re-issue of c7aa3a3 by the validate_docs.py open-Major line test (see Re-issue); re-issued APPROVED
# with liens finding-19 to finding-22 at re-issue 2 of iteration 3 (2026-09-26, HEAD 860e84e, package item R18), after the record state rule of 96af250
reviewer_verdict: APPROVED
assurance_verdict: not-required
verdict: APPROVED
findings_major: 4
# finding-19 is new at iteration 2; finding-20 to finding-22 are new at iteration 3 (all Minor);
# finding-18 is withdrawn (disputed accepted) and counted in neither open nor verified;
# findings_deferred counts the four liens (finding-19 to finding-22, "Lien: fix before PDR")
findings_minor: 18
findings_open: 0
findings_fixed: 0
findings_verified: 17
findings_deferred: 4
assurance_findings_major: 0
assurance_findings_minor: 0
assurance_tasks_applied: []
deferred_rids: []
# re-issue answers (iteration 1: R3, R4, CK-DES-H1, CK-DES-H3, CK-VIS-A1, CK-REQ-C5; iteration 2: R3, R4, CK-DES-H1, CK-VIS-A1; iteration 3: R4, CK-DES-H1)
items_no: [CK-DES-H1]
renders_inspected: 3  # iteration 3 re-opened the block diagram (--check exit 0 against the committed concept); the two ConOps renders are the blobs inspected at iterations 1 and 2
# effort: iterations 1 and 2 (58 turns, 95 min), iteration 3 (30 turns, 40 min) the re-issue of 2026-09-26 (8 turns, 12 min) and re-issue 2 (10 turns, 15 min)
effort_turns: 106
effort_minutes: 162
record_status: Open
date: 2026-09-25
date_closed: null
---

# Peer review record INSP-002: ConOps and concept description (SE-36)

**Product.** The SE-36 concept definition (NPR 7123.1D section 5.2.2.2 a (2), "Baselined concept definition [SE-36]", corpus `npr-7123-1d/05-chapter5.md` line 68; App. H row SE-36), reviewed as one product for SRR entrance rows 4, 5, 6, 10 and 17 (01 section 4.3) and minimum product SE-36 (01 section 4.5): the ConOps `docs/conops/conops.md` with its two Mermaid figures (operational view), the concept description `docs/design/concept.md` (technical view) and the concept block diagram render `docs/reviews/SRR/figures/concept-block-diagram.png` with its generator.

| File | Git blob (hash-object, working tree) | Blob at HEAD 28e49e6 | Status |
|---|---|---|---|
| `docs/conops/conops.md` | `559aed3ad8dcdc7806504b9310412b7539ea0bb4` | same | committed, clean |
| `docs/conops/figures/conops-context.mmd` | `55ebae2e15589bf9951456dc04400b7ccb96ea27` | same | committed, clean |
| `docs/conops/figures/conops-context.png` | `2e4647f81c61a1d2df05637efa3ee3d71a506e09` | same | committed, clean |
| `docs/conops/figures/conops-modes.mmd` | `829a46f800db84ae5196cf3946d4376eb813fc0f` | `8e004f85f7ef...` | modified, uncommitted |
| `docs/conops/figures/conops-modes.png` | `b3a08b6770c7c019b67e4b19cd2cdcbba3e8ce6c` | `af7d1ad9c052...` | modified, uncommitted |
| `docs/design/concept.md` | `86cb6f413c2b5439ea72412fbd42b1d6e826ef41` | `5d03bdf2a944...` | modified, uncommitted |
| `docs/reviews/SRR/figures/concept-block-diagram.png` | `ae2deab051150305d146b94076627323dea27252` | `f22e322bab60...` | modified, uncommitted |
| `docs/reviews/SRR/figures/concept-block-diagram.py` | `7d636a7c8a87b8b3d8996b76627dcd7da76327b8` | none | untracked |

**Checklist.** `docs/templates/peer-review-checklist-design.md` revision B, as assigned, with `docs/templates/peer-review-checklist-visual-product.md` revision A section A and items C3 and C5 for the three renders (its product-type row 3: a render inside another product is checked in that product's record). The design checklist sections A to G and I to J address software architecture and design, ICDs and hardware; the product here is the operational and concept-level system view, so those sections are N/A and section H with the readiness criteria carries the design-checklist judgment. Because `docs/process/08-agent-briefing.md` section 3.5 names the requirements checklist (sections A, B, F; ConOps row: A3, A4, A8, B4, C5, C6, F2, G1, G2) for "expectations, ConOps and the concept", the reviewer also applied the three ConOps-row items that bear on content (B4, C5, C6) as supplementary evidence; the record's `checklist` field names the assigned template only. The mismatch between the assignment and 08 section 3.5 is reported to Claude in the return.

**Reviewer.** `reviewer:conops-concept`, independent of the author (charter section 2; section 11 rule 4). The reviewer did not edit the product. Search first: `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before every `grep` (queries: SRR readiness shortfalls ConOps concept block diagram H items; SE-36 concept definition; Appendix S annotated outline nominal and off-nominal); `grep -n` was used afterwards only to pin lines. Numbers were checked against `docs/requirements/sys/requirements.json`, `docs/safety/hazards.json` (0.3.0-pha), `docs/risk/register.json`, `docs/plan/tpm.json`, the research reports named in each finding and the regulatory corpus.

**Verdict (re-issue 2 of iteration 3, 2026-09-26): APPROVED with liens finding-19 to finding-22; reviewer verdict APPROVED; readiness met.** The record state rule of `tools/validate_docs.py` (`96af250`, package item R18) replaced the line heuristic that held the record verdict; the product blobs equal HEAD `860e84e`. See "Re-issue 2 of iteration 3" at the end of this record.

**Verdict (re-issue, 2026-09-26): reviewer verdict APPROVED with liens finding-19 to finding-22; record verdict NEEDS CHANGES on a tool condition only.** Readiness R4 is met by the author self-check filed at `5b1f2cf`; the product blobs equal HEAD `8ef95d3`; no Major finding is open. See "Re-issue" at the end of this record.

**Verdict (iteration 1): NEEDS CHANGES.** Four Major findings (finding-1 to finding-4) and fourteen Minor findings. The ConOps content against SE HB App. S is complete and of high quality (every App. S section 1.0 to 8.0 and Appendices A and B present, 12 nominal and 10 off-nominal scenarios, modes with a full transition table and forbidden transitions, operator model, postures, support concept); the Major findings are disagreements between the two views and the L1 set on hazard-control values and the state set, which the functional baseline cannot carry, because REQ-SYS-002 makes ConOps section 3.4 binding.

## Findings

Severity: Major blocks the baseline; Minor is fixed before the next review. The Disposition column holds the reviewer's latest disposition (iteration 3 where the row says so: Closed, Disputed accepted, Lien or Open, with evidence). Under the lead SE convergence rule of 2026-09-26 (charter section 4 item 3), every Minor finding still open at iteration 3 is a lien, "Lien: fix before PDR"; Major findings still open go to the owner's ruling (01 section 10.1).

| Finding | Severity | Item | Location | Description and expected fix | State | Disposition |
|---|---|---|---|---|---|---|
| <a id="finding-1"></a>F-01 (finding-1) | Major | CK-DES-H1; CK-REQ-C5 | ConOps section 3.4 Table 3.4-1 Transmit-keyed row, Table 3.4-4 preamble, OPS-002 branch A; Appendix D item D3 | The ConOps states that every Inhibit and Latched cause "ends a carrier through the shaped fall within 10 ms (TBR) of detection (REQ-SYS-004 as aligned in Appendix D)". REQ-SYS-004 now reads "at most -40 dBc (TBR) within 20 ms (TBR) of detecting any inhibit, flag or latched fault". REQ-SYS-002 makes ConOps section 3.4 binding, so the functional baseline would carry two different values for one HZ-004 control. D3 is also stale: its scope extension is applied in REQ-SYS-004, its value is not. Fix: state one value in both products (the REQ-SYS-004 TBR with its plan, or a CR-ready change to REQ-SYS-004) and update D3's status. | Verified | Closed. ConOps line 165 (Table 3.4-1 Transmit-keyed row), line 212 (Table 3.4-4 preamble) and line 397 (OPS-002 branch A) state "at most -40 dBc within 20 ms (TBR, REQ-SYS-004)", equal to the REQ-SYS-004 statement and its TBR (owner Robin, plan ICD-TX-SW timing analysis, close_by PDR); Appendix D item D3 (line 851) is marked Closed with the 12.7 ms figure, which matches the REQ-SYS-004 rationale. No other carrier-end value remains (grep of `shaped fall` and `dBc`) |
| <a id="finding-2"></a>F-02 (finding-2) | Major | CK-DES-H1 | ConOps Table 3.4-1 Transmit-keyed row, Table 3.4-4 row 3, section 3.5.1 item 10, OPS-013 step 3, Appendix C stuck-key row; concept F3.6, section 8 first row, section 14 item 3 | Both products state the paddle watchdog as "128 identical elements or 30 s". REQ-SYS-054 reads "128 consecutive identical paddle elements or 10 s (TBR)", with the TBR plan "Robin decides D-KN3 at SRR (10 s cap, or 30 s with MOE-012 amended)". The concept's own convention says the requirements file wins where the two differ. Package section 15 items 7 and 15 record the same conflict. Fix: carry the pending owner decision explicitly (for example "10 s (TBR, REQ-SYS-054; 30 s is the alternative of decision 37)") in both products, or align the L1 value after the ruling. | Verified | Closed. ConOps lines 165, 218, 276, 537 and 822 and concept F3.6 (line 164), section 8 first row (line 239) and section 14 item 3 (line 367) state "128 consecutive identical elements or 10 s (TBR, REQ-SYS-054)" with 30 s named as the alternative of package decision 37 (D-KN3). Equals REQ-SYS-054 and its TBR plan |
| <a id="finding-3"></a>F-03 (finding-3) | Major | CK-DES-H1 (concept against L1 and ConOps) | concept section 4 paragraph 2, section 5 block B07 and edge `CHG -->|"charge active"| CUT`, section 7.2 last sentence, section 8 first row; render `concept-block-diagram.png` block B07 and the "charge active" edge | The concept ties the hardware transmit inhibit to the charger's charge-active state ("the PA is inhibited by hardware while the charger is active"; B07 "TX inhibit while charging"). REQ-SYS-092 requires a hardware inhibit "whenever USB VBUS is present", and the ConOps (flag USB, Table 3.4-3; Table 3.4-4 row 6; OPS-002) pauses charging while the radio receives with USB present. With charging paused the charge-active signal is inactive, so the concept as drawn releases the hardware inhibit exactly in the Receive-with-USB case of HZ-011. Fix: source the B07 inhibit from VBUS presence (for example from B16) in section 4, 7.2, 8, B07's label and the Mermaid edge, then re-render and re-inspect the figure. | Verified | Closed. Concept section 4 paragraph 2 (line 40), section 7.2 (line 205, VBUS sense divider of B16 through `ICD-TX-PWR`, "whether or not the charger is charging"), F7.6 (line 168), section 8 (line 239), B07 label and the edge `USBP -->|"VBUS present"| CUT` (lines 81, 132); `ICD-TX-PWR` row (line 263) carries the inhibit line. Render re-made by the reviewer (`concept-block-diagram.py --check` exit 0, `--output` to scratch exit 0, byte-identical) and opened: B07 reads "TX inhibit while VBUS present" and the VBUS present edge runs from B16 to B07 |
| <a id="finding-4"></a>F-04 (finding-4) | Major | CK-DES-H1; CK-REQ-C5 | concept section 4.1 | The concept-level state list (Off, Boot, Interlock, Receive, TxPending, Transmit, Hang; orthogonal GuestLock, Charging, Tune, SafeState) differs from the ConOps mode set that REQ-SYS-002 binds (nine modes Off, Charging, Self-test, Receive, Transmit-keyed, Tune, Bench-test, Firmware-update, Fault-safe; flags GUEST, PRACTICE, USB, LOWBATT; inhibits KEY, HOT, GUARD). Beyond names, the semantics conflict: concept SafeState is entered on "any watchdog or fault" with audio muted, while ConOps Table 3.4-4 sends a watchdog reset through Self-test (row 9), keeps the key causes in Receive as self-clearing inhibits with the sidetone sounding (rows 2 and 3), and latches only the Latched class (Appendix D item D6 records the same conflict against REQ-SYS-130). Section 4.1 also claims its names "are the CamelCase enum spellings the requirements use", but REQ-SYS-060 uses "Receive, Transmit-keyed and Tune modes". Fix: restate section 4.1 as a mapping onto the ConOps modes, flags and inhibits (implementation sub-states such as TxPending and Hang may remain, marked as sub-states of Transmit-keyed), and drop the "any fault" SafeState rule. | Verified | Closed. Concept section 4.1 (lines 48 to 66) is now a mapping onto the nine ConOps modes, four flags and three inhibits; `Boot`, `TxPending`, `TxElement` and `Hang` are marked proposed sub-states; Fault-safe is entered only by the Latched class, a reset returns through Self-test (T18, row 9), and inhibits keep the unit in Receive with the stuck-key sidetone. The "any fault" SafeState rule and the claim about the requirements' spelling are gone; the CamelCase citation now points at 02 section 4.2 WR-07, which does name the architecture enum spelling (02 line 235) |
| <a id="finding-5"></a>F-05 (finding-5) | Minor | CK-DES-H1 | ConOps section 3.5.1 item 1; Appendix C receiver-set row ("offset +/-500 Hz in 10 Hz steps") | The ConOps presents a "pitch offset adjustable over +/-500 Hz in 10 Hz steps" as an operator capability, and in section 3.5.1 item 4 a sidetone of 300 to 1000 Hz locked to the receive offset. `docs/research/cw-selectivity-options.md` implication 4 makes the +/-500 Hz a stored per-unit BFO calibration range; REQ-SYS-045 (sidetone 300 to 1000 Hz) and REQ-SYS-144 (pitch centre is stored calibration) agree, and the concept section 7.3 says "stored per unit". Same defect as INSP-001 finding-2 against NGO-012. Fix: state the operator pitch as the 300 to 1000 Hz sidetone range and the +/-500 Hz as the stored calibration range. | Verified | Closed. ConOps section 3.5.1 item 1 (operator pitch is the 300 to 1000 Hz sidetone, REQ-SYS-045 and REQ-SYS-046; +/-500 Hz is the stored BFO calibration, REQ-SYS-144), OPS-003 step 3 (line 408) and the Appendix C receiver-set row agree |
| <a id="finding-6"></a>F-06 (finding-6) | Minor | CK-DES-H1 | concept section 7.1 ("reference antennas Signal Stick half-wave class") | `docs/research/antenna-and-erp.md` line 55 lists the Signal Stick as "1/4 wave (144 to 148 MHz)", and ANT-05 (line 271) names it the quarter-wave pocket reference; ConOps assumption 3 and Appendix C say quarter-wave. Package section 15 item 6. Fix: "Signal Stick quarter-wave (48 cm)". | Verified | Closed. Concept section 7.1 (line 201): "Signal Stick quarter-wave (48 cm)" |
| <a id="finding-7"></a>F-07 (finding-7) | Minor | CK-DES-H1 | concept section 9, `ICD-TX-ANT` row ("1000 matings") | Concept section 7.1 says "500 mating cycles class", the ConOps section 3.3 says 500 matings and that REQ-SYS-106 and HZ-009 K2 correct the research figure of 1000, and REQ-SYS-106 reads "after 500 mating cycles". Fix: 500 matings in the ICD row. | Verified | Closed. Concept section 9 `ICD-TX-ANT` row (line 255): "500 matings (REQ-SYS-106)" |
| <a id="finding-8"></a>F-08 (finding-8) | Minor | CK-DES-H1 | ConOps section 2.2 rows for `hazards.json` ("HZ-001 to HZ-014") and `register.json` ("RSK-001 to RSK-033"); section 8 lead-in; Table 3.4-5 | `docs/safety/hazards.json` is version 0.3.0-pha with HZ-001 to HZ-015 (HZ-015 owner hand assembly, phase Assembly), and `docs/risk/register.json` holds RSK-001 to RSK-059. Table 3.4-5 maps the Off row to the Assembly phase but omits HZ-015, and omits HZ-010, whose phases include Handling. Fix: update the ranges and add HZ-015 and HZ-010 to the Off row. | Verified | Closed as specified: ConOps section 2.2 rows give hazards.json 0.3.0-pha HZ-001 to HZ-015 and the Table 3.4-5 Off row adds HZ-010 and HZ-015 (checked against `hazards.json`: HZ-010 phases include Handling, HZ-015 phase Assembly). The register range was right when fixed and has since moved; see finding-19 |
| <a id="finding-9"></a>F-09 (finding-9) | Minor | CK-DES-H1 | ConOps section 4, "Handling and thermal" row | "the amplifier dissipates about 4 to 7 W while keyed at 5 W (efficiency about 60 percent, TPM-004)". At the TPM-004 planned 60 percent drain efficiency the final stage dissipates 5/0.6 - 5 = 3.3 W; 4 to 7 W corresponds to 42 to 56 percent overall efficiency (the figure comes from `docs/research/keyer-verification-and-key-input-network.md` line 230, citing an RSK thermal entry). Fix: state which stages and which efficiency the 4 to 7 W assumes, or quote 3.3 W at 60 percent drain efficiency with the driver and bias added separately. | Verified | Closed. ConOps section 4 Handling and thermal row (line 339): 3.3 W final-stage dissipation at the TPM-004 60 percent drain efficiency, the 4 to 7 W research figure explained as a 42 to 56 percent line-up efficiency, both replaced by the PDR thermal analysis. Arithmetic checked |
| <a id="finding-10"></a>F-10 (finding-10) | Minor | CK-DES-H1 | ConOps section 3.5.1 item 6 | "show an identification reminder when 10 minutes have passed since the first transmission after the previous reminder". REQ-SYS-068 reads "9 min 00 s +/-5 s (TBR)", which leaves margin before the 10 minute interval of 47 CFR 97.119(a). Fix: cite the REQ-SYS-068 value. | Verified | Closed. ConOps section 3.5.1 item 6 and OPS-004 step 4 (line 422) cite REQ-SYS-068 9 min 00 s +/-5 s (TBR) and 47 CFR 97.119(a) (verified in corpus `47cfr-97.119.md` line 17: "at least every 10 minutes") |
| <a id="finding-11"></a>F-11 (finding-11) | Minor | CK-DES-H1 | concept section 3, "Environment" paragraph | "0 to 40 C design point for battery and thermal analyses ... no ingress rating in rev A". REQ-SYS-114 sets -10 to +45 C (TBR), TPM-006 carries the -10 to +45 C span, and REQ-SYS-117 sets IPX2 for 10 min; the ConOps section 4 agrees. The concept section 7.8 thermal line (40 C ambient) may stay as an analysis case if so labelled. Fix: state the -10 to +45 C operating span and the IPX2 light-rain condition, and name 40 C as the thermal analysis ambient. | Verified | Closed. Concept section 3 Environment (line 34): -10 C to +45 C (REQ-SYS-114, TBR), IPX2 10 min (REQ-SYS-117, TBR), 40 C named as the PA thermal analysis ambient |
| <a id="finding-12"></a>F-12 (finding-12) | Minor | CK-DES-H1 | concept section 6, F3.4 ("lead-in 5 ms") | The ConOps OPS-004 step 1 and the glossary give the first-element lead-in as 8 to 12 ms; REQ-SYS-161 bounds it at 12 ms (TBR); `docs/research/tr-switch-candidates.md` line 178 gives "8 ms lead-in" for the HF3 relay (5 ms operate plus 3 ms bounce, line 41). Fix: "lead-in 8 to 12 ms (REQ-SYS-161, TBR)". | Verified | Closed. Concept F3.4 (line 164): "first-element lead-in 8 to 12 ms, at most 12 ms by REQ-SYS-161, TBR" |
| <a id="finding-13"></a>F-13 (finding-13) | Minor | CK-DES-H1 | concept section 6, F9.5 ("10-minute identification reminder and CW ID at most 20 WPM") | The ConOps (section 3.5.1 item 6; section 3.5.4; Appendix C automatic-ID row) and REQ-SYS-007 provide no automatic identification in revision A; concept section 12 itself lists "CW ID beyond the identification reminder" as deferred. Fix: remove the CW ID from F9.5, or mark it as the deferred capability with its 47 CFR 97.119(b)(1) cap. | Verified | Closed. Concept F9.5 (line 170): reminder at 9 min 00 s +/-5 s (REQ-SYS-068), no automatic identification (REQ-SYS-007), the 20 WPM CW ID named as the deferred capability of section 12 |
| <a id="finding-14"></a>F-14 (finding-14) | Minor | CK-DES-H1 | concept section 7 table (CTL scope: "hardware monostable for the cutoff, TX_KEY and PA_EN pull-downs") and section 7.5 last sentence, against block B07 in the TX group (section 5) and the TX row "hardware PA-enable cutoff" | The cutoff block is allocated to TX in the block diagram and the TX scope statement, and to CTL in the CTL scope statement and section 7.5. `allocation.json` will inherit one of them. Fix: allocate B07 to one module and name the ICD (`ICD-TX-CTL`) that carries the other side. | Verified | Closed. Concept section 7 CTL scope (line 195) and section 7.5 last sentence (line 219) allocate B07 to TX and route CTL through `ICD-TX-CTL`; section 7.2 (line 205) says the same; `ICD-TX-CTL` row (line 262) carries TX_KEY, PA_EN and cutoff Q |
| <a id="finding-15"></a>F-15 (finding-15) | Minor | CK-DES-H1 | ConOps OPS-013 step 3 ("3.1 s of dits at 50 WPM, 30.7 s at 5 WPM") | The figures count key-down time only: at 50 WPM a dit is 24 ms and 128 dits are 3.07 s keyed, but 6.1 s elapsed with the inter-element spaces; at 5 WPM 128 dits take 61 s elapsed. The watchdog's time basis (elapsed or key-down) is not stated, and REQ-SYS-054 "10 s (TBR) of them" is equally silent. Fix: state the basis in the ConOps and raise the same point against REQ-SYS-054. | Verified | Closed. ConOps OPS-013 step 3 (line 537) states the elapsed-time basis with correct figures (128 dits: 6.1 s at 50 WPM, 20.5 s at 15 WPM, 61 s at 5 WPM; crossover about 31 WPM at 10 s and about 10 WPM at 30 s; 128 dahs 12.3 s at 50 WPM, all checked by the reviewer at dit = 1.2/WPM s); Appendix D item D18 raises the basis against REQ-SYS-054 |
| <a id="finding-16"></a>F-16 (finding-16) | Minor | CK-DES-H4 (charter section 11 rule 2) | ConOps header ("revision 2 of 2026-09-25 after the independent ConOps review"); Appendix C rows "review finding on guest-lock claims" and "review finding on Fault-safe" | No record of an earlier ConOps review exists (`docs/reviews/SRR/checklists/` holds no ConOps record before this one; package section 6.2: "Review record: none"). A claim or source without a linked artifact is not evidence. Fix: remove the claim and the two source entries, or cite this record's findings once they are adopted. | Verified | Closed. ConOps header (line 3) now cites this record instead of an earlier review; the two "review finding" source entries of Appendix C are removed (grep: no "review finding" or "independent ConOps review" remains) |
| <a id="finding-17"></a>F-17 (finding-17) | Minor | CK-VIS-A1; visual-product R3 | `conops-modes.mmd`, `conops-modes.png`, `concept.md`, `concept-block-diagram.png` (modified) and `concept-block-diagram.py` (untracked) | The renders and their sources are not committed, so the record cannot name a commit that holds the reviewed product and CK-VIS-A1 ("is committed") is not met. Package section 2 item H17 tracks the commit. Fix: commit the files when the findings are dispositioned and re-issue the record's `product_commit`. | Verified | Iteration 3: Closed. All eight product files are committed (`git status` clean at HEAD `adcfe09`; conops.md, conops-modes.mmd and .png, concept.md, concept-block-diagram.png and .py last changed at `8a37f8e`, appendix D at `1543c9f`) and `product_commit` and `product_files` now name the HEAD blobs. Iteration 2: Open. Not refuted: the working-tree files are still modified or untracked (`git diff --stat HEAD` lists conops.md, conops-modes.mmd and .png, concept.md, concept-block-diagram.png; the .py is untracked). The author cannot commit under its assignment; tracked by package section 2 item H17 (Robin authorizes, Claude commits). Closes when the commit exists and `product_commit` is re-issued |
| <a id="finding-18"></a>F-18 (finding-18) | Minor | CK-DES-H3 | `docs/conops/conops.md` (865 lines) | The design checklist limits a file to 500 lines with an index linking sub-files. The ConOps exceeds it; the concept (365 lines) meets it. Fix: split the ConOps (for example scenarios in `docs/conops/scenarios.md` and appendices C and D in their own file, indexed from `conops.md`), or have the owner rule H3 not applicable to the ConOps. | Withdrawn | Disputed accepted. The author's sources are right: 08 section 3.5 names the requirements checklist (sections A, B, F), which has no file-length rule, as the ConOps checklist, and CK-DES-H3 is a presentation rule for design files; charter section 5 maps the ConOps to `docs/conops/conops.md` with scenarios OPS-NNN, and `tools/traceability.py` reads OPS headings and the TBD scan only from that path (`CONOPS` constant, line 91; codes EXPECTATIONS_INCONSISTENT, VAL_TARGET_UNRESOLVED, TBD_PRESENT). The finding misapplied H3 to an operational product; withdrawn. H3 is N/A for the ConOps and Yes for the concept (381 lines) |
| <a id="finding-19"></a>F-19 (finding-19) | Minor | CK-DES-H1 | ConOps section 2.2 `register.json` row and section 8 lead-in (line 684) | New at iteration 2. Both say "RSK-001 to RSK-059"; `docs/risk/register.json` in the working tree now holds RSK-001 to RSK-065 (65 risks). Of the new entries, RSK-064 (open or cold owner-soldered joint in a power path, the Assembly phase of the Off row) and RSK-065 (lending units treated as outside the 47 CFR 15.23 exemption, the loan scenario) bear on operations, and the section 8 table names neither. Fix: cite the register without a fixed upper id (or update it to RSK-065), and add RSK-064 and RSK-065 to the section 8 table or say why they are not operational. | Lien | Iteration 3: Lien: fix before PDR. Not fixed at HEAD: `conops.md` line 105 and line 685 still read "RSK-001 to RSK-059" while `docs/risk/register.json` 0.6.0-pre-srr holds RSK-001 to RSK-065 (`register.md` summary: 65 active); section 8 still names neither RSK-064 nor RSK-065. Iteration 2: Open |
| <a id="finding-20"></a>F-20 (finding-20) | Minor | CK-DES-H1 | ConOps section 2.2 `hazards.json` row (line 103) | New at iteration 3. The row cites "`docs/safety/hazards.json` (version 0.3.0-pha)"; the committed file is 0.4.2-pha (HZ-001 to HZ-015 unchanged). Appendix D items D6 and D10 of the same file cite 0.4.2-pha, so the ConOps names two versions of one input. Fix: cite 0.4.2-pha, or cite the file without a version as section 2.2 does for other inputs. | Lien | Lien: fix before PDR |
| <a id="finding-21"></a>F-21 (finding-21) | Minor | CK-DES-H4 | ConOps Appendix D status column header (line 848) | New at iteration 3. The header reads "Status (2026-09-26, products at commit 400e59d)", but the D6 and D10 statuses cite `hazards.json` 0.4.2-pha and the section 7 rows of `hazard-analysis.md` at 0.4.2-pha, which first exist at `1543c9f` (`git show 400e59d:docs/safety/hazards.json` is 0.4.0-pha). The evidence commit named for the statuses does not hold all of the evidence (charter section 11 rule 2). Fix: name the commit that holds every cited product (`1543c9f` or later), or date each status by its own commit. | Lien | Lien: fix before PDR |
| <a id="finding-22"></a>F-22 (finding-22) | Minor | CK-DES-H1 | ConOps OPS-013 step 6, last sentence (line 540) | New at iteration 3 (text not quoted at iteration 2). "If both are declined, firmware alone bounds a toggling stream" contradicts the same step, which says "REQ-SYS-054 as written counts identical elements only": with the HZ-004 K4 no-gap watchdog (decision 37) and REQ-SYS-180 (decision 38) both declined, no L1 requirement bounds an alternating squeeze stream from a shorted TRS cable in an iambic mode, and `docs/safety/hazard-analysis.md` section 8.2 row 3 records it as "open single point if declined". The ConOps also overstates the Expected outcome in that case. The underlying choice is already before the owner (package decisions 37 and 38, OQ-SAF-006), so the defect is the sentence, not the hazard record. Fix: state that with both declined no requirement bounds the stream and it is the open single point of hazard-analysis section 8.3, in the OPS-013 edit that R9 (OQ-SAF-006) already schedules after the rulings. | Lien | Lien: fix before PDR |

## Readiness criteria

| # | Criterion | Result | Evidence |
|---|---|---|---|
| R1 | Every figure rendered beside its source and stated inspected | Yes | ConOps header "Figures are rendered from Mermaid sources ... and were inspected"; concept section 5 rendering note "Rendered and inspected 2026-09-25"; the three PNGs exist beside their sources |
| R2 | `design_refs` allocation shown by `traceability.py` | N/A | Concept-level product at SRR; allocation is preliminary (`docs/design/allocation.json`, T-18 at Warning level, package item H6) |
| R3 | Requirements implemented are Active or the brief names the CR | No | All 177 non-retired REQ-SYS are Draft (package section 8); expected at SRR, where this product and the L1 set are baselined together. Not a finding |
| R4 | Author return lists acceptance criteria and self-check | No | The author summary covers the H10 figure work only (layout checks, `--check` exit 0); no self-check of `conops.md` or the concept text against this checklist exists |

`readiness_met: false` records R3 and R4.

## Checklist items

Result values: Yes (Pass), No (Fail), N/A.

| Id | Result | Evidence |
|---|---|---|
| CK-DES-A1 to A8 | N/A | Software architecture content; the software architecture is a PDR product (`docs/design/architecture.md`). Concept section 7.6 fixes concept-level firmware rules only |
| CK-DES-B1 to B5 | N/A | REQ-SW allocation and design-unit tags do not exist at SRR. At concept level, concept section 8 maps each hazard family to its independent layers, used as evidence for F-03 |
| CK-DES-C1 to C15 | N/A | SWE-134 unit-level provisions belong to the module designs (CDR) |
| CK-DES-D1 to D13 | N/A | Detailed design (CDR) |
| CK-DES-E1 to E4 | N/A | Pin-level ICD consistency (PDR); the external ICD stubs have their own record (design section I) |
| CK-DES-F1 to F3, G1, G2 | N/A | Software design cybersecurity and reuse (PDR, CDR) |
| CK-DES-H1 | No | Contradictions quoted in finding-1 to finding-15: between the concept and the ConOps (F-04, F-12, F-13), between each product and the L1 set (F-01, F-02, F-03, F-05, F-07, F-10, F-11), inside a product (F-07, F-09, F-14) and against research (F-06, F-15). No contradiction with ADR-011 was found in concept section 7.6 (single NVIC priority, PWM slices 0 to 7, GPIO through SIO, TIMER0 alarms) |
| CK-DES-H2 | Yes | All three figures are legible; every figure is referenced in text (ConOps Figure 1.3-1 and Figure 3.4-1; concept section 5 rendering note); state names in `conops-modes.png` equal Table 3.4-1 (Off, Charging, Self-test, Receive, Transmit-keyed, Tune, Bench-test, Firmware-update, Fault-safe) and the edge labels carry the Table 3.4-2 ids T01 to T25 (T17 to T20 on the Radio-on box, as the caption states) |
| CK-DES-H3 | No | `wc -l`: `conops.md` 865, `concept.md` 365 (finding-18) |
| CK-DES-H4 | Yes, with finding-16 | Verified in the corpus: SE HB App. S (`nasa-se-handbook/41-appendix-s-concept-of-operations-annotated-outline.md`, sections 1.1 to 8.0 and 6.1, 6.2 nominal and off-nominal); SE HB section 4.1.1.2.4 (`04-4-1-stakeholder-expectations-definition.md` line 183); SE-36 (`npr-7123-1d/05-chapter5.md` line 68, `14-appendixh.md` line 70); App. G Table G-3 entrance items 3.2 (concept ready to be baselined, technically feasible), 5.2 (alternative concepts), 5.4 (descope options) and 5.10 (single point failure and fault tolerance philosophy), and Table G-4 entrance items 6.1 (updated concept definition) and 6.11 (external interfaces), as the concept header cites them (`13-appendixg.md`, entrance lists 3, 5 and 6); 47 CFR 97.307(e) (corpus `47cfr-97.307.md` line 25: 25 uW and 40 dB, so 53.0 dB at 5 W as both products state), 97.119(b)(1) 20 WPM (line 21), 15.23(a) five units, not a kit (line 17). F-16 is an unsupported internal citation |
| CK-DES-I1 to I8 | N/A | ICD stubs are reviewed in their own record; concept section 9 lists the 18 ICDs and matches the 02 section 3.5 ordering (F-07 is a value error in one row) |
| CK-DES-J1 to J10 | N/A | No schematic, PCB, enclosure or BOM at SRR |

### Visual-product items applied to the three renders (CK-VIS)

| Id | Result | Evidence |
|---|---|---|
| CK-VIS-A1 | No | All three renders exist beside their sources; the modes figure and the concept block diagram are not committed (finding-17) |
| CK-VIS-A2 | Yes | Headless: `mmdc` (mermaid-cli, `/opt/homebrew/bin/mmdc`) with the command written in each `.mmd` header; `concept-block-diagram.py` (matplotlib, headless) reads the Mermaid block of concept section 5 |
| CK-VIS-A3 | Yes | Reviewer re-renders into the scratch directory: `mmdc -i conops-modes.mmd -o <scratch>/modes.png -b white -w 1600 -s 2` exit 0, byte-identical to the working-tree PNG; `mmdc -i conops-context.mmd -o <scratch>/context2.png -b white -s 2` exit 0, same 1568 x 906 size, bytes differ, opened side by side and visually identical; `concept-block-diagram.py --check` exit 0 ("is current"), and `--output <scratch>/cbd.png` exit 0, byte-identical to the working-tree PNG |
| CK-VIS-A4 | Yes | Per-render table below |
| CK-VIS-A5 | Yes | Concept render: all 22 blocks B01 to B22 with the Mermaid labels, 6 groups, and all 32 edges with their labels, including the B17 "I2C, sense" link, the two 3.3 V rail connectors from B20 to B08 and B06, "heat", "retention" and "runs on" (the script reports "22 blocks, 6 groups, 32 edges; layout checks passed"). Modes render: every T01 to T25 id appears; the "T08 pass" label now sits on the Self-test to Receive edge (package section 7 defect closed). Context render: actors, equipment and ICD ids agree with ConOps section 3.3 and section 3.2 users |
| CK-VIS-A6 | Yes | ConOps figures carry numbered captions in the text; the concept render has a legend (RF and signal, power, control, association) and is titled by concept section 5 and package section 7 |
| CK-VIS-A7 | Yes | No red, amber or green status coding in the three renders; the Fault-safe box tint in the modes figure is backed by its "(latched)" label |
| CK-VIS-A8 | Yes | The two package section 7 defects (T08 label, concept diagram not rendered) are fixed in the working tree; package section 7 rows are now stale (reported to Claude) |
| CK-VIS-C3 | Yes | Block, state and edge names match the governing documents (see A5); `ICD-` ids in the context figure equal ConOps section 3.3 |
| CK-VIS-C5 | N/A | No package copy of a ConOps render; the deck's `conops-modes-scenarios.png` is a separate figure of `tools/render_review_figures.py`, not reviewed here |

### Per-render results

| Render | Source | Opened with Read (A4) | Legible, nothing clipped or overlapping (A4) | Content agrees with source (A5) | Finding ids |
|---|---|---|---|---|---|
| `docs/conops/figures/conops-context.png` (1568 x 906) | `conops-context.mmd` | Yes | Yes | Yes | none |
| `docs/conops/figures/conops-modes.png` (3168 x 2324) | `conops-modes.mmd` | Yes | Yes (long crossing edges on the left, all labels readable and on their edges) | Yes | finding-17 |
| `docs/reviews/SRR/figures/concept-block-diagram.png` (1760 x 860) | concept section 5 Mermaid block through `concept-block-diagram.py` | Yes | Yes (two reviewed crossings of the B07 to B03 line, as the script reports) | Yes: it draws the source faithfully; the source defect of finding-3 is visible in block B07 and the "charge active" edge | finding-3, finding-17 |

### Supplementary: requirements-checklist ConOps row items (08 section 3.5)

| Id | Result | Evidence |
|---|---|---|
| CK-REQ-B4 | Yes | Every OPS-001 to OPS-022 heading carries an "Exercises" line naming MOEs and NGOs (OPS-015 and OPS-020 name MOE-006; OPS-013 names MOE-012); both key types are exercised (OPS-004 paddle, OPS-005 straight key, OPS-013 steps 1 to 3) |
| CK-REQ-C5 | No | State names differ between ConOps section 3.4 and concept section 4.1 (finding-4); the carrier-end value differs from REQ-SYS-004 (finding-1) |
| CK-REQ-C6 | Yes | Ten off-nominal scenarios OPS-013 to OPS-022 (stuck key and mono plug, over-temperature, antenna fault, charging fault, RF pickup, bystander, guest, band edge, reset during transmit, face posture), plus off-nominal branches in OPS-001 and OPS-002; every entrance row 10 case is present |

## SE-36 content judgment

The ConOps follows SE HB App. S section by section (header section map, verified against the App. S file), and states its additions (sections 3.6, 3.7, Appendices C and D) as App. S permits ("additional subsections should be added as necessary"). Scenarios are labelled for traceability as App. S section 6.0 advises, cover nominal and off-nominal conditions separately (6.1, 6.2), and each has actors, preconditions, steps, expected outcome and exercised expectations (02 section 3.3). The concept description covers the Table G-3 concept items (feasibility by catalog parts and research basis, alternatives dispositioned in 11.1 with six PDR trade studies, ten descope options, the single point failure and fault tolerance philosophy in section 8) and Table G-4 item 11 (section 9). Spot checks that agree with their sources: FM comparison 12.7 dB, 2.1x and 4.3x range (`antenna-and-erp.md` line 246); bystander distances 0.58 m, 0.91 m, 0.41 m, 0.29 m, 0.26 m and the per-step reminders 0.2, 0.3, 0.4, 0.6 m (`rf-exposure-evaluation.md` Table 2 lines 83 to 92 and line 191); the SAR percentages of section 3.6 and OPS-022 (0.35 W/kg per W at the stated duty factors against 8 and 1.6 W/kg); the 53.0 dB spurious limit at 5 W; the REQ-SYS-020 tune limit of 5.5 s in both products (package section 15 item 15 on the tune value is closed in the working tree; its paddle part remains as finding-2).

## Measurements (SWE-089)

Iteration 1: items checked 18 design-checklist items or groups (H1 to H4 answered; A to G, I, J N/A), 10 CK-VIS items, 3 supplementary CK-REQ items, 4 readiness criteria. Items answered No: R3, R4, CK-DES-H1, CK-DES-H3, CK-VIS-A1, CK-REQ-C5. Findings: 4 Major, 14 Minor; fixed 0; deferred 0. Renders inspected: 3.

Iteration 2: items re-checked 10 (closure table). Items answered No: R3, R4, CK-DES-H1, CK-VIS-A1. Findings: 4 Major, 15 Minor (finding-19 new); verified 16, withdrawn 1 (finding-18), open 2 Minor, deferred 0. Renders re-inspected: 1 (block diagram). Effort for the iteration: 24 turns, 35 minutes.

## Closure (iteration 2, 2026-09-25)

**Re-review scope.** The author said finding-1 to finding-16 were fixed. It disputed finding-17 (the commit is outside its assignment and is routed to the main session) and finding-18 (splitting the file would break the references that bind to `conops.md`). The reviewer (`reviewer:conops-concept`, a new invocation in the same role) did not edit the product. It re-read the working-tree blobs in the front matter against `git diff HEAD` of `conops.md` and the whole of `concept.md` (381 lines), and checked each fix against its source. The sources were `docs/requirements/sys/requirements.json` (REQ-SYS-004, 045, 046, 054, 068, 092, 106, 114, 117, 144, 161 statements and TBR blocks), `docs/safety/hazards.json` 0.3.0-pha, `docs/risk/register.json`, `docs/process/02-requirements-and-traceability.md` line 235 (WR-07), `tools/traceability.py` line 91 and the regulatory corpus `47cfr-97.119.md` line 17. Search first: `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any `grep`. The queries were "peer review record closure block findings disposition" and "paddle watchdog 128 identical elements 30 s ConOps concept". `grep -n` then pinned lines. The changed passages contain no em dash (count 0 in both files) and no bare TBD.

**Render (visual closure).** The reviewer ran `concept-block-diagram.py --check` (exit 0, "22 blocks, 6 groups, 32 edges; layout checks passed") and `--output <scratchpad>/cbd.png` (exit 0). The output is byte-identical (`cmp`) to `docs/reviews/SRR/figures/concept-block-diagram.png`, blob `3ef6e911`. The reviewer opened that render with Read. It is legible with nothing clipped. B07 reads "Hardware PA-enable cutoff, T_max 10 s, TX inhibit while VBUS present", the "VBUS present" edge runs from B16 to B07, and the "charge active" edge is gone. `conops-modes.png` and `conops-context.png` have the same blobs as at iteration 1 (inspected then).

**Dispositions.**

| Disposition | Count | Findings |
|---|---|---|
| Closed (fix verified in the product, state Verified) | 16 (Major 4, Minor 12) | finding-1 to finding-16 |
| Disputed accepted (state Withdrawn) | 1 (Minor) | finding-18 |
| Open | 2 (Minor) | finding-17 (commit; package H17, Robin authorizes, Claude commits); finding-19 (new: the RSK range is stale after concurrent register growth to RSK-065) |

Open Major: 0. Open Minor: 2.

**Iteration 2 answers.**

| Item | Answer | Evidence |
|---|---|---|
| R1 | Yes | Block diagram re-rendered and inspected (above); the ConOps renders are unchanged |
| R2 | N/A | As at iteration 1 |
| R3 | No | All REQ-SYS are still Draft, as expected at SRR (not a finding) |
| R4 | No | The author's iteration 2 return gives a list of fixed ids and two dispute reasons. It gives no acceptance criteria and no checklist self-check of `conops.md` or `concept.md` |
| CK-DES-H1 | No | finding-1 to finding-15 closed; finding-19 open |
| CK-DES-H2 | Yes | As at iteration 1; the block diagram labels now equal concept section 5 |
| CK-DES-H3 | N/A (ConOps); Yes (concept, 381 lines) | finding-18 withdrawn |
| CK-DES-H4 | Yes | finding-16 closed; 47 CFR 97.119(a) verified in the corpus; the 02 WR-07 citation of concept section 4.1 verified (02 line 235) |
| CK-VIS-A1 | No | finding-17 |
| CK-REQ-C5 | Yes | finding-1 and finding-4 closed |

**Verdict (iteration 2): NEEDS CHANGES.** No Major finding is open. Minor findings would ride with APPROVED (08 section 3.2), but the readiness criteria are not met: R4 has no author self-check, and R3 is structural until the SRR baseline. `tools/validate_docs.py` rejects APPROVED while `readiness_met` is false. The record can move to APPROVED when three things are done: the author supplies the self-check (R4) or the owner waives it; finding-19 is fixed; and finding-17 is closed by the H17 commit, or the owner defers it to that commit with a decision reference. `record_status` stays Open for the lead SE (07 section 10.2).

```
VERDICT (iteration 2): NEEDS CHANGES
FINDINGS: Closed 16 (finding-1 to finding-16; Major 4, Minor 12); Disputed accepted 1 (finding-18); Open 2 Minor (finding-17, finding-19); open Major 0
MEASUREMENTS: items re-checked 10; items answered No 4 (R3, R4, CK-DES-H1, CK-VIS-A1); renders re-inspected 1; iteration 2
```

## Iteration 3 (2026-09-26, committed product at HEAD `adcfe09`; SRR package items R8 and H17)

**Scope and independence.** A new invocation of `reviewer:conops-concept`, independent of the author (charter section 2; section 11 rule 4); it did not edit the product. Review baseline: HEAD `adcfe0946d2f1b5cd8f41a8f91eb4219a7fb99a1`, with the blobs of `git rev-parse HEAD:<path>` named in `product_files`. The iteration 2 blobs `conops.md` `b2e93594` and `concept.md` `f9c4af43` are not in the object store (package section 2.3), so the reviewer could not diff them. It therefore re-checked every closure quote of finding-1 to finding-16 against the committed text, line by line. It then read every hunk of `git diff 28e49e6 8a37f8e` and `git diff 8a37f8e HEAD` of `conops.md`: the appendix D status column of `1543c9f`, and OPS-013 step 6 with its revised Expected outcome, which no earlier iteration quoted. The six figure files have the same blobs as at iteration 2. Search first: `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any `grep`. The queries were "validate_docs record drift rule product_files blobs differ from HEAD APPROVED record", "ConOps register.json RSK range section 8 operational risks RSK-064 RSK-065", "author self-check INSP-002 ConOps concept decision 115 readiness R4 waiver" and "ConOps author self-check against checklist acceptance criteria conops.md concept.md". `grep -n` then pinned lines. Sources checked: `docs/requirements/sys/requirements.json` (statements and rationales of REQ-SYS-002 to 005, 007, 020, 045, 046, 052 to 056, 060, 065, 066, 068, 092, 102, 103, 106, 114 to 117, 121, 130, 144, 161, 163, 180, 183), `docs/safety/hazards.json` 0.4.2-pha (HZ-001 K2 and K6, HZ-004 K2, HZ-006 K2, the phase list), `docs/safety/hazard-analysis.md` sections 7 and 8.2 (rows 3 and 20), `docs/plan/tpm.json` (MOP-001, MOP-002, TPM-001, TPM-016 `moe_ids`), `docs/decisions/adr/ADR-015-*.md`, `docs/research/rf-exposure-evaluation.md` line 94, `docs/risk/register.md` and `git show 400e59d:docs/safety/hazards.json`. The changed passages contain no em dash (count 0 in both files) and no bare TBD.

**Render (visual closure).** The reviewer ran `concept-block-diagram.py --check` against the committed concept: exit 0, "22 blocks, 6 groups, 32 edges; layout checks passed ... is current". It then opened `docs/reviews/SRR/figures/concept-block-diagram.png` (blob `3ef6e911`) with Read. The render is legible with nothing clipped. B07 reads "Hardware PA-enable cutoff, T_max 10 s, TX inhibit while VBUS present", and the "VBUS present" edge runs from B16 to B07. `conops-context.png` and `conops-modes.png` are the blobs inspected at iterations 1 and 2 (`2e4647f8`, `b3a08b67`).

**Disposition table.**

| Finding | Severity | Iteration 3 disposition | Evidence at HEAD `adcfe09` |
|---|---|---|---|
| finding-1 | Major | Closed | `conops.md` line 212 (Table 3.4-4 preamble) and line 397 (OPS-002 branch A) bring RF "to the RF-off level of REQ-SYS-183 within 20 ms (TBR)", equal to the REQ-SYS-004 statement; line 165 (Transmit-keyed row) cites "20 ms (TBR, REQ-SYS-004)"; D3 (line 852) matches. No other carrier-end value remains (grep of `dBc` and `RF-off`) |
| finding-2 | Major | Closed | "128 consecutive identical elements or 10 s (TBR) ... 30 s is the alternative of package decision 37" at `conops.md` lines 165, 218, 276, 537 and 823 and `concept.md` line 164 (F3.6) and line 367 (section 14 item 3); line 239 (section 8) gives the same values. REQ-SYS-054 reads "128 consecutive identical paddle elements or 10 s (TBR) elapsed since the first" |
| finding-3 | Major | Closed | `concept.md` line 81 (B07 label), line 132 (edge `USBP -->\|"VBUS present"\| CUT`), line 148 (NOT VBUS from B16), line 263 (`ICD-TX-PWR` inhibit line); render as above. REQ-SYS-092 reads "whenever USB VBUS is present" |
| finding-4 | Major | Closed | `concept.md` section 4.1 (lines 48 to 66): mapping onto the nine ConOps modes, four flags and three inhibits; Fault-safe entered only by the Latched class (rows 10 to 15); inhibits apply the transmit part only; a reset returns through Self-test |
| finding-5 | Minor | Closed | `conops.md` line 267 (sidetone 300 to 1000 Hz, REQ-SYS-045, REQ-SYS-046), line 831 (BFO calibration range +/-500 Hz) |
| finding-6 | Minor | Closed | `concept.md` line 201: "Signal Stick quarter-wave (48 cm)" |
| finding-7 | Minor | Closed | `concept.md` line 255: "500 matings (REQ-SYS-106)" |
| finding-8 | Minor | Closed | `conops.md` line 103 (HZ-001 to HZ-015; its stale file version is new finding-20); Table 3.4-5 Off row unchanged since iteration 2 |
| finding-9 | Minor | Closed | `conops.md` line 339: 3.3 W final-stage dissipation at the TPM-004 60 percent drain efficiency |
| finding-10 | Minor | Closed | `conops.md` line 272: "9 min 00 s +/-5 s (TBR)", equal to REQ-SYS-068 |
| finding-11 | Minor | Closed | `concept.md` line 34: -10 C to +45 C (REQ-SYS-114, TBR), 40 C named as the thermal analysis ambient |
| finding-12 | Minor | Closed | `concept.md` line 164 (F3.4): "first-element lead-in 8 to 12 ms, at most 12 ms by REQ-SYS-161, TBR" |
| finding-13 | Minor | Closed | `concept.md` line 170 (F9.5): reminder per REQ-SYS-068, no automatic identification in rev A (REQ-SYS-007), CW ID deferred |
| finding-14 | Minor | Closed | `concept.md` line 195 (CTL scope), line 219 (section 7.5), line 262 (`ICD-TX-CTL`): B07 allocated to TX |
| finding-15 | Minor | Closed | `conops.md` line 537: elapsed-time basis with 6.1 s, 20.5 s, 61 s and 12.3 s figures; D18 (line 867) Edited, REQ-SYS-054 now says "elapsed since the first" |
| finding-16 | Minor | Closed | `conops.md` line 3 cites this record; no "review finding" or "independent ConOps review" text remains |
| finding-17 | Minor | Closed | All product files committed; `product_commit` `adcfe09` and `product_files` name the HEAD blobs (front matter) |
| finding-18 | Minor | Disputed accepted (Withdrawn) | Unchanged from iteration 2 |
| finding-19 | Minor | Lien: fix before PDR | `conops.md` lines 105 and 685 still read "RSK-001 to RSK-059"; the register holds RSK-001 to RSK-065 |
| finding-20 | Minor (new) | Lien: fix before PDR | `conops.md` line 103 cites `hazards.json` 0.3.0-pha; HEAD is 0.4.2-pha |
| finding-21 | Minor (new) | Lien: fix before PDR | `conops.md` line 848: "products at commit 400e59d"; D6 and D10 cite 0.4.2-pha, first committed at `1543c9f` |
| finding-22 | Minor (new) | Lien: fix before PDR | `conops.md` line 540 (OPS-013 step 6): "If both are declined, firmware alone bounds a toggling stream" contradicts "REQ-SYS-054 as written counts identical elements only" and hazard-analysis section 8.2 row 3 |

**Appendix D statuses (new text at `1543c9f`, checked).** The reviewer checked each status claim of the new status column against the committed products. D1, D2, D4, D5, D8, D16 and D18 hold: REQ-SYS-002, 003, 005, 053, 054, 007, 121, 102, 103 and 114 to 117 carry the stated text or sources. D3 holds. The L1 parts of D6 (REQ-SYS-130), D9 (REQ-SYS-065) and D10 (REQ-SYS-052, 056, 163) hold. The D7 edits hold: REQ-SYS-020 at 5.5 s, the REQ-SYS-055 rationale, HZ-001 K2, HZ-006 K2, and `concept.md` lines 59, 170, 240 and 366. The hazard parts of D6 and D10 are in 0.4.2-pha (HZ-004 K2 text; hazard-analysis section 7 exists), and their verification belongs to the INSP-008 reviewer, as the column says. The Open claims hold: D9 (ADR-015 section 2 unchanged), D11 (phases still Assembly, Charging, Firmware load, Handling, Receive, Storage, Transmit, Tune), D12 (HZ-001 K6 cites no OPS-022), D13 (the four items parent to MOE-001), D14 (`rf-exposure-evaluation.md` line 94 unchanged), D15 and D17. The only defect in the column is its header commit (finding-21).

**New Major scan.** None found. The text changed since the iteration 2 quotes is the appendix D status column and OPS-013 step 6 with its Expected outcome. Step 6 carries one Minor misstatement (finding-22). The hazard it describes is already before the owner as package decisions 37 and 38 (OQ-SAF-006; hazard-analysis section 8.2 row 3). The ConOps discloses that REQ-SYS-054 does not cover the squeeze stream, and OPS-013 is not in section 3.4, the part that REQ-SYS-002 binds. So the sentence does not put a conflicting value into the functional baseline.

**Lien table** (carried by the package as Routine items; charter section 4 item 3, a Minor RID is fixed before the next review).

| Finding | Severity | Disposition | Owner | Due |
|---|---|---|---|---|
| finding-19 | Minor | Lien: fix before PDR | ConOps author (Claude, lead SE) | PDR readiness declaration |
| finding-20 | Minor | Lien: fix before PDR | ConOps author (Claude, lead SE) | PDR readiness declaration |
| finding-21 | Minor | Lien: fix before PDR | ConOps author (Claude, lead SE) | PDR readiness declaration |
| finding-22 | Minor | Lien: fix before PDR | ConOps author (Claude, lead SE), in the OPS-013 edit of R9 (OQ-SAF-006) after decisions 37 and 38 | PDR readiness declaration |

**Iteration 3 answers.**

| Item | Answer | Evidence |
|---|---|---|
| R1 | Yes | Every figure is committed beside its source and inspected (render paragraph above) |
| R2 | N/A | As at iteration 1 |
| R3 | N/A | Changed from No: before SRR every requirement is Draft by rule (08 section 3.1 Status), and this product is baselined with the L1 set at SRR, so no Active requirement or CR can exist. This matches the R3 answer of INSP-012 and INSP-013 on the same checklist. At iterations 1 and 2 the answer No was already marked "not a finding" |
| R4 | No | No author self-check of `conops.md` or `concept.md` against this checklist, and no acceptance criteria, came with the iteration 3 assignment or appear in the repository (claude-context search above). Package decision 115 carries this for INSP-002. Its recommendation is no waiver: the author files the self-check |
| CK-DES-H1 | No (liens only) | finding-1 to finding-15 Closed; finding-19, finding-20 and finding-22 are liens |
| CK-DES-H2 | Yes | As at iteration 2 |
| CK-DES-H3 | N/A (ConOps); Yes (concept, 381 lines) | As at iteration 2 |
| CK-DES-H4 | Yes, with finding-21 (lien) | finding-16 Closed |
| CK-VIS-A1 | Yes | finding-17 Closed: every render and source is committed |
| CK-REQ-C5 | Yes | finding-1 and finding-4 Closed |

**Counts after iteration 3.** There are 22 findings. Closed (Verified): 17 (Major 4, Minor 13). Disputed accepted: 1 (finding-18). Lien: 4 (Minor: finding-19 to finding-22). Open: 0. Open Major: 0.

**Verdict (iteration 3): NEEDS CHANGES, on readiness only.** Every finding is Closed, Disputed-accepted or a lien, so under the convergence rule the findings allow APPROVED (with liens). Readiness R4 is not met, however. The design checklist's verdict rule requires R1 to R4 to hold for APPROVED, and SWE-088 b calls for established readiness criteria. `tools/validate_docs.py` rejects APPROVED while `readiness_met` is false. A readiness criterion is not a finding, so a lien cannot discharge it. The record is re-issued APPROVED (with liens finding-19 to finding-22), with no further product review, when either of two things happens: the ConOps author files the self-check against design checklist section H and the ConOps-row items of the requirements checklist, and the reviewer confirms it; or the owner rules decision 115 as a waiver to PDR, with the decision reference recorded here. `record_status` stays Open for the lead SE (07 section 10.2).

```
VERDICT (iteration 3): NEEDS CHANGES (readiness R4 only; package decision 115)
FINDINGS: Closed 17 (finding-1 to finding-17; Major 4, Minor 13); Disputed accepted 1 (finding-18); Lien 4 (finding-19 to finding-22, "Lien: fix before PDR"); Open 0; open Major 0
MEASUREMENTS: items re-checked 22 findings and 10 items; items answered No 2 (R4, CK-DES-H1 on liens); renders re-inspected 1; iteration 3; 30 turns, 40 minutes
PRODUCT: HEAD adcfe09; conops.md b2c76c80, concept.md 729190a2, six figure files as in product_files
```

## Author self-check (written by the author; package item R7, readiness R4)

**Ownership.** This section is the author's return for readiness R4 of the design checklist ("The author's return lists the brief's acceptance criteria and the self-check"), filed in the record because 01 section 13 keeps no record only in conversation. It is written by `author:conops-concept` (Claude, lead SE), not by the reviewer. The author changed nothing else in this record: the front matter, findings, readiness answers, verdict and measurements stay the reviewer's. Whether R4 is now met, and the re-issue of the record, are the reviewer's (package item R8). No product content changed with this self-check (convergence rule, charter section 4 item 3).

**Product checked.** The committed blobs named in `product_files` at HEAD `d4cce27`, unchanged since the iteration 3 review (`git rev-parse HEAD:<path>`: `conops.md` `b2c76c80`, `concept.md` `729190a2`, the four ConOps figure files and the two block-diagram files as listed). Date 2026-09-26. Search first: `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ("author self-check readiness fields R1 to R4 peer review record"; "author self-check section filed by the author against checklist, acceptance criteria listed, decision 115") ran before any `grep`.

**Acceptance criteria.** The original author briefs of ConOps revision 2 (`28e49e6`) and of the H10 concept run (`8a37f8e`) are not in the repository, so the criteria are restated from the governing sources the briefs pointed to:

| # | Acceptance criterion | Source |
|---|---|---|
| AC-1 | Concept developed to a level that shows technical feasibility, ready to baseline; concept summary and block sketch render | 01 section 4.3 row 4 (G-3 3.2; SE-36) |
| AC-2 | Descope options listed in a "Deferred capabilities" section | 01 section 4.3 row 6 (G-3 5.4) |
| AC-3 | Nominal and off-nominal `OPS-NNN` scenarios with MOE links, including straight key and paddle, headphones, tuning, charging, high SWR and stuck key | 01 section 4.3 row 10 (G-4 6.2; SE-36) |
| AC-4 | External interfaces identified by ICD id | 01 section 4.3 row 17 (G-4 6.11) |
| AC-5 | ConOps follows SE HB App. S; modes, flags and transitions of section 3.4 agree with the L1 set, because REQ-SYS-002 binds them | charter section 5; SE HB App. S; REQ-SYS-002 |
| AC-6 | Every figure rendered headlessly beside its source and inspected | charter section 11 rule 3; 08 section 1 visual closure |
| AC-7 | No TBD; a TBR only by reference to an L1 TBR with owner, plan and close_by; no em dash | charter section 7; 08 section 1 WRITING |
| AC-8 | Only Major findings change the product before SRR; Minor findings are liens due PDR | charter section 4 item 3 (lead SE convergence rule, 2026-09-26) |

**Self-check against the checklist.** Design checklist revision B section H and readiness R1 to R4, plus the ConOps row of `docs/templates/peer-review-checklist-requirements.md` (A3, A4, A8, B4, C5, C6, F2, G1, G2) that 08 section 3.5 names for "expectations, ConOps and the concept".

| Item | Author answer | Evidence |
|---|---|---|
| R1 | Yes | `concept-block-diagram.py --check` exit 0 today ("22 blocks, 6 groups, 32 edges; layout checks passed ... is current"). The author opened all three committed renders with Read on 2026-09-26: `concept-block-diagram.png` (B07 "TX inhibit while VBUS present", VBUS present edge from B16, legend present, nothing clipped), `conops-modes.png` (the nine modes of Table 3.4-1, T01 to T25 on their edges, Fault-safe labelled latched), `conops-context.png` (actors, equipment and ICD ids of ConOps sections 3.2 and 3.3). All legible |
| R2 | N/A | Concept-level product; no `REQ-SW-*` design allocation at SRR |
| R3 | N/A | Every requirement is Draft before the SRR memo (08 section 3.1 Status); product and L1 set baseline together |
| R4 | Yes (this section) | Acceptance criteria AC-1 to AC-8 and this table |
| CK-DES-H1 | No: liens only | No contradiction found in the values bound by REQ-SYS-002: `conops.md` lines 165, 212 and 397 give 20 ms (TBR, REQ-SYS-004) and lines 165 and 218 give 128 elements or 10 s (TBR, REQ-SYS-054), equal to the L1 statements read today; USB inhibit on VBUS presence equals REQ-SYS-092. Known and accepted as liens due PDR: finding-19 (lines 105 and 685 read RSK-001 to RSK-059; RSK-064 and RSK-065 not named), finding-20 (line 103 cites `hazards.json` 0.3.0-pha), finding-22 (line 540, OPS-013 step 6 sentence), all to be fixed in the PDR revision |
| CK-DES-H2 | Yes | As R1; every figure is referenced in the text (Figure 1.3-1, Figure 3.4-1, concept section 5) |
| CK-DES-H3 | N/A (ConOps); Yes (concept) | `concept.md` 381 lines; the ConOps (867 lines) is outside H3 per finding-18 (withdrawn) |
| CK-DES-H4 | Yes, with finding-21 as a lien | SE-36 in `npr-7123-1d/05-chapter5.md`; SE HB App. S in `nasa-se-handbook/41-appendix-s-concept-of-operations-annotated-outline.md`; 47 CFR citations checked by the reviewer against the regulatory corpus. finding-21 (Appendix D header names commit `400e59d`, line 848) is accepted, fix before PDR |
| CK-REQ-A3 | Yes | Quantities carry units and bounds (for example 20 ms, 10 s, 9 min 00 s +/-5 s, 0.5 to 5 W, -10 to +45 C), each tied to its L1 requirement and TBR |
| CK-REQ-A4 | Yes | The ConOps states no "shall" requirement; `grep -cw TBD` gives 0 in both files and `tools/traceability.py --report-only` (exit 0, 0 violations, 3 warnings none on the ConOps) raises no TBD_PRESENT or ConOps code |
| CK-REQ-A8 | Yes | Mode names equal Table 3.4-1 and REQ-SYS-002; key types written "straight key" (11 uses) and "iambic paddle(s)" (5 uses) |
| CK-REQ-B4 | Yes | Scripted check today: all 22 `OPS-NNN` headings carry an "Exercises" line naming at least one MOE or NGO; OPS-004 (paddle), OPS-005 (straight key) and OPS-013 exercise both key types |
| CK-REQ-C5 | Yes | ConOps section 3.4 is the mode set REQ-SYS-002 binds; concept section 4.1 maps its proposed sub-states onto it (finding-4 Closed) |
| CK-REQ-C6 | Yes | Ten off-nominal scenarios OPS-013 to OPS-022 plus off-nominal branches in OPS-001 and OPS-002 (AC-3) |
| CK-REQ-F2 | Yes | Terms and enum spellings as A8; concept section 4.1 names the ConOps modes, flags and inhibits unchanged |
| CK-REQ-G1 | Yes | The ConOps expands charter section 5 (ConOps row) and does not contradict the charter, RMM or an Accepted ADR; concept section 7.6 agrees with ADR-011 (reviewer H1 evidence) |
| CK-REQ-G2 | Yes | Each scenario names actors, preconditions, steps, expected outcome and exercised expectations; 0 hits for "as appropriate" or "should consider" in either file |
| AC-2, AC-4 | Yes | `conops.md` section 3.5.4 "Deferred capabilities" (line 290); ICD ids in ConOps section 3.3, the context render and concept section 9 (18 ICDs) |
| AC-7 | Yes | Em dash count 0 in both files; every TBR in the text cites its L1 requirement |

**Author statement.** The product meets AC-1 to AC-8 with the four Minor liens finding-19 to finding-22 open, owned by the author and due at the PDR readiness declaration. No finding is disputed.

## Re-issue (independent reviewer, 2026-09-26; package items R7 and R8, no further product review)

**Scope and independence.** New invocation of the reviewer role (`reviewer:conops-concept`); it did not author the products or the self-check and edited no product and no author section. Search first: `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual pin. Convergence rule of the lead SE (charter section 4 item 3) applied: no product change is asked.

**Product blobs.** `git rev-parse HEAD:<path>` at HEAD `8ef95d3` equals every blob in `product_files` (the eight files of iteration 3; last product commits `1543c9f` for `conops.md` and `8a37f8e` for the rest). No product changed since the iteration 3 review, so no delta verification is needed; `product_commit` and `product_files` stand.

**Self-check verification (readiness R4).** The author self-check section above (commit `5b1f2cf`, written by `author:conops-concept`) lists acceptance criteria AC-1 to AC-8, restated from the governing sources because the original briefs are not in the repository, and answers design checklist section H, R1 to R4 and the ConOps-row items of the requirements checklist with evidence. The reviewer re-ran its checkable claims on the HEAD blobs: em dash 0 and `TBD` 0 in `conops.md` (867 lines) and `concept.md` (381 lines); 0 hits for "as appropriate" or "should consider"; 22 `OPS-NNN` headings, each followed by an "Exercises" line; "Deferred capabilities" at `conops.md` line 290; the lien locations cited (lines 103, 105, 685 and 848) still hold the text of finding-19 to finding-21; `concept-block-diagram.py --check` exit 0 ("22 blocks, 6 groups, 32 edges; layout checks passed ... is current"); `concept-block-diagram.png` opened and inspected (B07 "TX inhibit while VBUS present", VBUS present edge from B16, legend present, nothing clipped). Every claim checked holds, and the author and reviewer answers agree (CK-DES-H1 No on liens only). R4 is met.

| # | Criterion | Re-issue answer | Evidence |
|---|---|---|---|
| R1 | Every figure rendered beside its source and inspected | Yes | As at iteration 3; block diagram `--check` exit 0 and render re-opened at this re-issue |
| R2 | `design_refs` allocation shown by `traceability.py` | N/A | As at iteration 1 |
| R3 | Requirements implemented are Active or the brief names the CR | N/A | As at iteration 3 (every requirement Draft before the SRR memo) |
| R4 | Author return lists acceptance criteria and self-check | Yes | Author self-check section (`5b1f2cf`), verified above |

**Findings.** Unchanged from iteration 3: 22 findings; Closed (Verified) 17 (Major 4, Minor 13); Disputed accepted 1 (finding-18); Lien 4 (finding-19 to finding-22, Minor, "Lien: fix before PDR", owner the ConOps author, due the PDR readiness declaration); none open; no Major open. No Major needs an owner ruling.

**Verdict (re-issue).** `readiness_met: true`; reviewer verdict APPROVED with liens finding-19 to finding-22. The record `verdict` is held at NEEDS CHANGES by one tool condition, not by a finding and not by readiness: `tools/validate_docs.py` (`open_major_findings`, line 664) counts as an open Major finding any body line that carries a `finding-<n>` anchor together with the words "Major" and "Open". Four count summary lines of iterations 2 and 3 (the iteration 2 verdict paragraph and VERDICT block, the iteration 3 counts paragraph and VERDICT block) match that test although no Major finding is open, so the tool refuses `verdict: APPROVED`. The reviewer did not reword record text to pass the tool. The record is re-issued APPROVED, with no further review, when the lead SE corrects the tool heuristic or rules how the record text may be adjusted (reported with this re-issue). `record_status` stays Open for the lead SE (07 section 10.2) until the liens close.

```
VERDICT (re-issue, 2026-09-26): reviewer APPROVED (with liens finding-19 to finding-22); record NEEDS CHANGES on the validate_docs.py open-Major line test only
PRODUCT: HEAD 8ef95d3; conops.md b2c76c80, concept.md 729190a2, six figure files as in product_files (unchanged since iteration 3)
READINESS: R1 Yes, R2 N/A, R3 N/A, R4 Yes (author self-check 5b1f2cf verified)
FINDINGS: Closed 17; Disputed accepted 1; Lien 4 (Minor); none open; no Major open
MEASUREMENTS: claims re-checked 12; renders re-inspected 1; re-issue 8 turns, 12 minutes
```

## Re-issue 2 of iteration 3 (independent reviewer, 2026-09-26; package item R18, readiness finding R15-F2; no further product review)

**Scope and independence.** New invocation of the reviewer role (`reviewer:conops-concept`); it did not author the products, the self-check or the tool change, and it edited no product and no author section. Earlier sections of this record are left as written (audit trail); only the front matter fields `verdict`, `effort_turns` and `effort_minutes`, their comments and the verdict line at the top of the body changed. Search first: `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ("validate_docs record state rule open Major findings structured replaces line heuristic") ran before any `grep`, which then pinned lines of `tools/validate_docs.py` and `docs/reviews/SRR/package.md`. Convergence rule of the lead SE (charter section 4 item 3) applied: no product change is asked.

**Tool condition removed.** Package item R18 is done by the tool owner: `tools/validate_docs.py` (blob `3aa03681`, commit `96af250`; TV-003 run 6 at `860e84e`) replaces the line heuristic with the record state rule of its module docstring. An APPROVED record is now read from its front matter and the finding tables of its latest iteration section only; prose lines, fenced blocks and count summaries are not read. The reviewer checked the rule against this record with `validate_docs.current_findings`: the latest iteration section is the "Iteration 3" section with the author self-check and re-issue sections after it; its disposition table, lien table and the table below give 22 findings, none in state Open, the four Major findings (finding-1 to finding-4) Closed. No record text was reworded to pass the tool.

**Product blobs.** `git rev-parse HEAD:<path>` at HEAD `860e84e` equals `git hash-object` of the working tree and every blob in `product_files` for all eight files; `git log 8ef95d3..HEAD` shows no commit to any of them. `concept-block-diagram.py --check` exit 0 ("22 blocks, 6 groups, 32 edges; layout checks passed ... is current"). No delta verification is needed; `product_commit` (`adcfe09`, the review baseline) and `product_files` stand.

**Readiness.** Unchanged from the re-issue of `c7aa3a3`: R1 Yes, R2 N/A, R3 N/A, R4 Yes (author self-check `5b1f2cf` verified); `readiness_met: true`.

**Current finding state (re-issue 2).**

| Finding | Severity | State | Note |
|---|---|---|---|
| finding-1 | Major | Closed (Verified) | Iteration 3 disposition table |
| finding-2 | Major | Closed (Verified) | Iteration 3 disposition table |
| finding-3 | Major | Closed (Verified) | Iteration 3 disposition table |
| finding-4 | Major | Closed (Verified) | Iteration 3 disposition table |
| finding-5 to finding-17 | Minor | Closed (Verified) | Iteration 3 disposition table (13 findings) |
| finding-18 | Minor | Disputed accepted (Withdrawn) | Iteration 2 |
| finding-19 | Minor | Lien: fix before PDR | Owner the ConOps author; due the PDR readiness declaration |
| finding-20 | Minor | Lien: fix before PDR | As finding-19 |
| finding-21 | Minor | Lien: fix before PDR | As finding-19 |
| finding-22 | Minor | Lien: fix before PDR | As finding-19, in the OPS-013 edit after decisions 37 and 38 |

**Verdict (re-issue 2).** APPROVED with liens finding-19 to finding-22. The reviewer verdict, readiness and findings are those of the re-issue of `c7aa3a3`; the only change is that the tool condition which held the record verdict no longer exists. `record_status` stays Open for the lead SE (07 section 10.2) until the four liens close.

```
VERDICT (re-issue 2 of iteration 3, 2026-09-26): APPROVED (with liens finding-19 to finding-22); reviewer APPROVED; assurance not required
PRODUCT: HEAD 860e84e; conops.md b2c76c80, concept.md 729190a2, six figure files as in product_files (unchanged since iteration 3)
READINESS: R1 Yes, R2 N/A, R3 N/A, R4 Yes; readiness_met true
FINDINGS: Closed 17 (Major 4, Minor 13); Disputed accepted 1; Lien 4 (Minor); none open; no Major open
TOOL: validate_docs.py record state rule (96af250, blob 3aa03681) replaces the line heuristic; package item R18 closed for this record
MEASUREMENTS: blobs re-checked 8; renders re-checked 1 (--check); re-issue 2 10 turns, 15 minutes; cumulative 106 turns, 162 minutes
```
