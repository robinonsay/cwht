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
