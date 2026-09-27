---
# Peer-review record front matter (charter section 5; docs/process/01-lifecycle-and-reviews.md section 13;
# docs/process/05-configuration-and-data-management.md section 9.2 step 3; docs/process/08-agent-briefing.md
# section 3.2). Independent review of TV-015 to TV-019, the wave 1a tools of PDR work plan WP-PDR-07.
# Record path: the plan names one record for TV-014 to TV-019 (tool-validation-tv-014-to-tv-019.md, INSP-038).
# INSP-038 holds TV-014 alone, has used its three iterations and is escalated to the owner (its iteration 3
# verdict), and its section "TV-015 to TV-019" defers these tools to "a later iteration". A fourth iteration
# is not allowed (07 section 10.2; plan rule C1) and one verdict cannot serve an escalated TV-014 and five
# other tools, so this set is reviewed in its own record under the template's set slug
# tool-validation-tv-nnn-to-tv-mmm.md (cross item X-1 asks the lead SE to confirm the split).
# Checklists applied: docs/templates/peer-review-checklist-tool-validation.md revision A (blob 7be809d4, CR-012
# branch cr/CR-012-pdr-checklist-templates at 7784672; APPROVED by INSP-033), item by item for each record, and
# docs/templates/peer-review-checklist-code.md revision B for the five tool sources (03 section 6.1.1 row "Peer
# review"; section "Code review"). The checklist field names the code checklist because the tool validation
# template is not on main (CR-012 Submitted) and tools/validate_docs.py requires the named template to exist in
# docs/templates/, as INSP-038, INSP-040 and INSP-041 did.
id: INSP-088
checklist: peer-review-checklist-code
checklist_revision: B
checklist_tool_validation: "docs/templates/peer-review-checklist-tool-validation.md@7be809d4ceb9a202473eb19da3627fe0cd427900 (revision A, CR-012 branch head 7784672)"
checklist_file: docs/reviews/PDR/checklists/tool-validation-tv-015-to-tv-019.md
product: docs/cm/tool-validation/TV-015-openscad-freecad-scad2step.md
# product_commit (iteration 2): the re-freeze commit 99feb43 on main (no branch-only products); run 2 of TV-015
# tested 989d257. Every blob of product_files was recomputed with git rev-parse 99feb43:<path> and HEAD:<path> at
# HEAD 1353bb3 (a status-note commit after 99feb43): 64 of 64 equal. Against iteration 1 (product_files_iteration_1,
# freeze 2bfe001), ten identities changed or were added, all by the finding-1 fix (989d257, 99feb43): TV-015
# 4669c5ec, test_scad2step.py bd38fe2b, known-answers.json 05520747, the four API double files (new), the run 2 log
# (new), the TV README 9400963d and the lock 6c7eba57. The lock also carries the d9c7f69 LTspice rows (blob 83bc0520
# at iteration 1); 83bc0520..6c7eba57 touches only the TV-015 rows (sections 1.1, 1.2, 5, one history row).
# tools/scad2step.py is unchanged (d0277ec8). The TV-016 to TV-019 products are unchanged from 2bfe001. Fixture
# directories are listed file by file with their trees in fixture_trees.
# Iteration 2 re-issue 1 (drift delta, 2026-09-27, HEAD 3d320a3): three index blobs changed on main after 99feb43 by
# the TV-014/INSP-038 commits d1148c2, 45531ac, f47360a, bd78bd5 and 1db319a: the TV README 9400963d to 7c90f143
# (via f4757da2 at bd78bd5), the lock 6c7eba57 to e1c811b0 (via be96420b at bd78bd5) and tools/README.md 053e6df2 to
# a5e9cab6. Every hunk touches TV-014/LTspice text only; product_files names the HEAD blobs (64 of 64 equal HEAD).
# product_commit stays 99feb43, the freeze of every TV-015 to TV-019 product that was tested.
product_commit: "99feb43"
product_files: ["docs/cm/tool-validation/TV-015-openscad-freecad-scad2step.md@4669c5ec30bb91eb778dc4dc3a6d03e5a1d600c1", "docs/cm/tool-validation/TV-016-kicad-cli-normalize-fab.md@88ccf56a0fa28677cdfae43b4840d895e0bee5d4", "docs/cm/tool-validation/TV-017-render-tpm.md@be08df365b75f33c11bb6bf4dc10b5139c28d4f9", "docs/cm/tool-validation/TV-018-csa.md@c28685d58aca44be7985d3185078f5e4d37ed72a", "docs/cm/tool-validation/TV-019-check-commit-msg.md@ff88029f7102bcea04548a1ddc5b49978a6abb55", "tools/scad2step.py@d0277ec8d89967576869be95ee5d0300e1f6af51", "tools/normalize_fab.py@f3eaac395b279bceb32fb3ba850632acfe426782", "tools/render_tpm.py@f37985d67e94998c9de4f790dccac7592f9ccd34", "tools/csa.py@dd9b6fede610f61d033d88222450981315559ed5", "tools/check_commit_msg.py@5488dd98b21220261835a74112b49a508865c346", "tools/tests/test_scad2step.py@bd38fe2b5cf7cf75aac65d6f19d2c96633b56119", "tools/tests/test_normalize_fab.py@707a22d594671b9125fd5f8134c57d290121e413", "tools/tests/test_kicad_cli.py@780117af30155408b4c4f56574d72cfd261c0b88", "tools/tests/test_render_tpm.py@a6b93352bffd5c15907e4e37209cfe5911c8b17d", "tools/tests/test_csa.py@58672f3ac0b09aadcdabad0ef9d9f28c55ddf041", "tools/tests/test_check_commit_msg.py@d8595b98493088523e448b29e6d99bd2242e9998", "tools/tests/fixtures/openscad/cube.scad@e8898580965f6859f3b53a04fc7bd251cf60e264", "tools/tests/fixtures/openscad/fake/freecadcmd-hang@ba333283d69d18c538cbf78abdc2e0cb19009906", "tools/tests/fixtures/openscad/fake/freecadcmd-silent@00296ab1f43668b73d64243f077c554d31963a28", "tools/tests/fixtures/openscad/fake/freecadcmd-api-double@e6de6ad25391e85fbfe15e799046aacba0494ff6", "tools/tests/fixtures/openscad/fake/freecad_api/FreeCAD.py@ccdc3e1b62b4acc379ef939f2521d72c6c495b65", "tools/tests/fixtures/openscad/fake/freecad_api/Part.py@549f799f7d356fc8e7385a3f16d1754c9ffc488a", "tools/tests/fixtures/openscad/fake/freecad_api/importCSG.py@e8d4a46d903c35f9814783ca56172c0363cb30e3", "tools/tests/fixtures/openscad/fake/openscad-other-version@a66d1f86bfa22033f85cf3f1f7865b07629ed0b1", "tools/tests/fixtures/openscad/known-answers.json@055207479ceb25b6f868da342ce73d4bda19b5ac", "tools/tests/fixtures/openscad/nonuniform-scale.scad@2c2acb9791a4be0241726bed5c373cda72c5660b", "tools/tests/fixtures/openscad/smoke-shell.scad@3eb43ab5a7966009b5c1dc7dac1c4ae0d4e74465", "tools/tests/fixtures/openscad/taller.scad@4f2a3c9931659257fd4ed5312679b262a78e4869", "tools/tests/fixtures/openscad/twist.scad@36b987989ecdb0122f9f1bb198a3ac78ec6dcb10", "tools/tests/fixtures/openscad/two-roots.scad@edc84f75775682d2d932dcb7def1d19b285db162", "tools/tests/fixtures/openscad/two-solids.scad@396df8f7118b47015112056d3333ce1fce94546e", "tools/tests/fixtures/kicad/clean.kicad_pcb@08d65d3ae7687e6baedf5c168ebeac7f4427580c", "tools/tests/fixtures/kicad/clean.kicad_pro@03cbb6fd496b0e79d5e369d61124be5952c93ea2", "tools/tests/fixtures/kicad/clean.kicad_sch@9bb4d4dcb272867eff63e8a3039ea188cc1461b9", "tools/tests/fixtures/kicad/expected/clean-SHA256SUMS.normalized@d284adf576e474910423d46f9d2479d5e8c85a78", "tools/tests/fixtures/kicad/expected/clean-bom.csv@fd602389e1258c1c02078ca40b24ea3bc298b8de", "tools/tests/fixtures/kicad/expected/clean-cpl.csv@7a1a4c15539d546cda94f4979e4ed2d6eae85e48", "tools/tests/fixtures/kicad/fp-lib-table@2b914a6732f05f444afd43c7838192cb05de60a4", "tools/tests/fixtures/kicad/known-answers.json@f4216971be847fd54ed72fd2b8fdb16ce85ae7dc", "tools/tests/fixtures/kicad/make_expected_normalized.sh@b57067605a0764f2d3db1272defc9fdac1e26389", "tools/tests/fixtures/kicad/make_fixture_pcb.py@871a5f3265d1f132ac7ca86739febd172d0a009e", "tools/tests/fixtures/kicad/make_fixture_sch.py@91cd3ada3a13c2da60f5d84f1fbe89a4c18333f8", "tools/tests/fixtures/kicad/seeded.kicad_pcb@c01cfa3852c400949a5f379b203898cc64c71e5c", "tools/tests/fixtures/kicad/seeded.kicad_pro@71defdc94a9f98a968ca58078df25fa263ab1625", "tools/tests/fixtures/kicad/seeded.kicad_sch@1b1252e79fdad538bf362a36980da1fff68add20", "tools/tests/fixtures/kicad/sym-lib-table@3d6388dc92e476be0048119177a9307c3b0bcebe", "tools/tests/fixtures/render_tpm/expected.json@c6b4787ff14a61e564c9b0852759ac5fbc64ee35", "tools/tests/fixtures/render_tpm/tpm.json@e89f170457ee4ea1e9320cbb956771838897f1e6", "tools/tests/fixtures/csa/build_repo.py@6cd4a56bb3b1a4d937ba14688e56b09865926633", "tools/tests/fixtures/csa/cm-plan-05.md@a8595764b288e038b1df20589d1873976ddc1907", "tools/tests/fixtures/csa/expected.json@443c7a8c3ebe3b3eb18156e1b960d40cc94d0004", "tools/tests/fixtures/csa/hand-csa-9fd0962.json@44992dde659f654f754535f1fae513e34ba8023b", "docs/cm/tool-validation/evidence/pdr-tools-2026-09-27.sh@15cc6a048046c7a9b6fd3b368bd0ff408bd9ec2b", "docs/cm/tool-validation/evidence/scad2step-2026-09-27-run1.log.txt@c685c14fe70ec787602facda8753c2b79c6cf409", "docs/cm/tool-validation/evidence/scad2step-2026-09-27-run2.log.txt@b9285807521d35f2a33fe0f86b2dff7860339f10", "docs/cm/tool-validation/evidence/kicad-normalize-fab-2026-09-27-run1.log.txt@a01a63ad6c337052dca10987b5a952df2b52470b", "docs/cm/tool-validation/evidence/render-tpm-2026-09-27-run1.log.txt@f178d683b734125ffe6e60d6e8b3cdb33721538e", "docs/cm/tool-validation/evidence/csa-2026-09-27-run1.log.txt@16673d791f19a867acbce400a4bf4cb944400a40", "docs/cm/tool-validation/evidence/check-commit-msg-2026-09-27-run1.log.txt@ca94682c8d3ab12c93106e49f49ba0d5d1e00834", "docs/cm/tool-validation/evidence/render-tpm-fixture-tpm-status.png@40d42ca79ca08be026647ccacc6d41fc13278ab7", "docs/cm/tool-validation/evidence/render-tpm-fixture-trend-own-yellow-after-status-note.png@6bfb3e19679cbe5a219be60cbd35170b9844141e", "docs/cm/tool-validation/README.md@7c90f14310f7deedf518596bc57c5b4c7e2fc277", "tools/toolchain.lock.md@e1c811b08b742e8ad24ff053efc9c4476fbffd29", "tools/README.md@a5e9cab6415d6d94a33fef03a18f4a408fc4ca29"]
product_files_iteration_1: ["docs/cm/tool-validation/TV-015-openscad-freecad-scad2step.md@787a117598ee417f97482dd8ae2e38ba6f160ddd", "docs/cm/tool-validation/TV-016-kicad-cli-normalize-fab.md@88ccf56a0fa28677cdfae43b4840d895e0bee5d4", "docs/cm/tool-validation/TV-017-render-tpm.md@be08df365b75f33c11bb6bf4dc10b5139c28d4f9", "docs/cm/tool-validation/TV-018-csa.md@c28685d58aca44be7985d3185078f5e4d37ed72a", "docs/cm/tool-validation/TV-019-check-commit-msg.md@ff88029f7102bcea04548a1ddc5b49978a6abb55", "tools/scad2step.py@d0277ec8d89967576869be95ee5d0300e1f6af51", "tools/normalize_fab.py@f3eaac395b279bceb32fb3ba850632acfe426782", "tools/render_tpm.py@f37985d67e94998c9de4f790dccac7592f9ccd34", "tools/csa.py@dd9b6fede610f61d033d88222450981315559ed5", "tools/check_commit_msg.py@5488dd98b21220261835a74112b49a508865c346", "tools/tests/test_scad2step.py@2e2fc392ccb5a0cba20e7f519527c2e58134f118", "tools/tests/test_normalize_fab.py@707a22d594671b9125fd5f8134c57d290121e413", "tools/tests/test_kicad_cli.py@780117af30155408b4c4f56574d72cfd261c0b88", "tools/tests/test_render_tpm.py@a6b93352bffd5c15907e4e37209cfe5911c8b17d", "tools/tests/test_csa.py@58672f3ac0b09aadcdabad0ef9d9f28c55ddf041", "tools/tests/test_check_commit_msg.py@d8595b98493088523e448b29e6d99bd2242e9998", "tools/tests/fixtures/openscad/cube.scad@e8898580965f6859f3b53a04fc7bd251cf60e264", "tools/tests/fixtures/openscad/fake/freecadcmd-hang@ba333283d69d18c538cbf78abdc2e0cb19009906", "tools/tests/fixtures/openscad/fake/freecadcmd-silent@00296ab1f43668b73d64243f077c554d31963a28", "tools/tests/fixtures/openscad/fake/openscad-other-version@a66d1f86bfa22033f85cf3f1f7865b07629ed0b1", "tools/tests/fixtures/openscad/known-answers.json@59be16ad719ef3b44d58d829399e8ee03e1845cd", "tools/tests/fixtures/openscad/nonuniform-scale.scad@2c2acb9791a4be0241726bed5c373cda72c5660b", "tools/tests/fixtures/openscad/smoke-shell.scad@3eb43ab5a7966009b5c1dc7dac1c4ae0d4e74465", "tools/tests/fixtures/openscad/taller.scad@4f2a3c9931659257fd4ed5312679b262a78e4869", "tools/tests/fixtures/openscad/twist.scad@36b987989ecdb0122f9f1bb198a3ac78ec6dcb10", "tools/tests/fixtures/openscad/two-roots.scad@edc84f75775682d2d932dcb7def1d19b285db162", "tools/tests/fixtures/openscad/two-solids.scad@396df8f7118b47015112056d3333ce1fce94546e", "tools/tests/fixtures/kicad/clean.kicad_pcb@08d65d3ae7687e6baedf5c168ebeac7f4427580c", "tools/tests/fixtures/kicad/clean.kicad_pro@03cbb6fd496b0e79d5e369d61124be5952c93ea2", "tools/tests/fixtures/kicad/clean.kicad_sch@9bb4d4dcb272867eff63e8a3039ea188cc1461b9", "tools/tests/fixtures/kicad/expected/clean-SHA256SUMS.normalized@d284adf576e474910423d46f9d2479d5e8c85a78", "tools/tests/fixtures/kicad/expected/clean-bom.csv@fd602389e1258c1c02078ca40b24ea3bc298b8de", "tools/tests/fixtures/kicad/expected/clean-cpl.csv@7a1a4c15539d546cda94f4979e4ed2d6eae85e48", "tools/tests/fixtures/kicad/fp-lib-table@2b914a6732f05f444afd43c7838192cb05de60a4", "tools/tests/fixtures/kicad/known-answers.json@f4216971be847fd54ed72fd2b8fdb16ce85ae7dc", "tools/tests/fixtures/kicad/make_expected_normalized.sh@b57067605a0764f2d3db1272defc9fdac1e26389", "tools/tests/fixtures/kicad/make_fixture_pcb.py@871a5f3265d1f132ac7ca86739febd172d0a009e", "tools/tests/fixtures/kicad/make_fixture_sch.py@91cd3ada3a13c2da60f5d84f1fbe89a4c18333f8", "tools/tests/fixtures/kicad/seeded.kicad_pcb@c01cfa3852c400949a5f379b203898cc64c71e5c", "tools/tests/fixtures/kicad/seeded.kicad_pro@71defdc94a9f98a968ca58078df25fa263ab1625", "tools/tests/fixtures/kicad/seeded.kicad_sch@1b1252e79fdad538bf362a36980da1fff68add20", "tools/tests/fixtures/kicad/sym-lib-table@3d6388dc92e476be0048119177a9307c3b0bcebe", "tools/tests/fixtures/render_tpm/expected.json@c6b4787ff14a61e564c9b0852759ac5fbc64ee35", "tools/tests/fixtures/render_tpm/tpm.json@e89f170457ee4ea1e9320cbb956771838897f1e6", "tools/tests/fixtures/csa/build_repo.py@6cd4a56bb3b1a4d937ba14688e56b09865926633", "tools/tests/fixtures/csa/cm-plan-05.md@a8595764b288e038b1df20589d1873976ddc1907", "tools/tests/fixtures/csa/expected.json@443c7a8c3ebe3b3eb18156e1b960d40cc94d0004", "tools/tests/fixtures/csa/hand-csa-9fd0962.json@44992dde659f654f754535f1fae513e34ba8023b", "docs/cm/tool-validation/evidence/pdr-tools-2026-09-27.sh@15cc6a048046c7a9b6fd3b368bd0ff408bd9ec2b", "docs/cm/tool-validation/evidence/scad2step-2026-09-27-run1.log.txt@c685c14fe70ec787602facda8753c2b79c6cf409", "docs/cm/tool-validation/evidence/kicad-normalize-fab-2026-09-27-run1.log.txt@a01a63ad6c337052dca10987b5a952df2b52470b", "docs/cm/tool-validation/evidence/render-tpm-2026-09-27-run1.log.txt@f178d683b734125ffe6e60d6e8b3cdb33721538e", "docs/cm/tool-validation/evidence/csa-2026-09-27-run1.log.txt@16673d791f19a867acbce400a4bf4cb944400a40", "docs/cm/tool-validation/evidence/check-commit-msg-2026-09-27-run1.log.txt@ca94682c8d3ab12c93106e49f49ba0d5d1e00834", "docs/cm/tool-validation/evidence/render-tpm-fixture-tpm-status.png@40d42ca79ca08be026647ccacc6d41fc13278ab7", "docs/cm/tool-validation/evidence/render-tpm-fixture-trend-own-yellow-after-status-note.png@6bfb3e19679cbe5a219be60cbd35170b9844141e", "docs/cm/tool-validation/README.md@763f10829dfc372ead42f7fda9ad2b43d4b871ed", "tools/toolchain.lock.md@4e978efc474adaf34337affe75addc51d5ab3d59", "tools/README.md@053e6df2b63350629a264324dcf7444f18f2b4cb"]
fixture_trees: ["tools/tests/fixtures/openscad@35e89b482be8449c31385e3712aa42268477955a", "tools/tests/fixtures/kicad@03063f2a45abd42f532e4b035cfac71fe578de90", "tools/tests/fixtures/render_tpm@9a6aff2536b65027c9fc4eb0a424a92fd139dcc9", "tools/tests/fixtures/csa@92fd0e50c0d61bf2c8e71b9e6b7dc518c6733d30"]
tv_ids: [TV-015, TV-016, TV-017, TV-018, TV-019]
# tool_class: per record (05 section 9.1): TV-015 A; TV-016 A (kicad-cli exports) and B (ERC, DRC,
# normalize_fab.py); TV-017, TV-018, TV-019 B. The field holds the highest class of the set
tool_class: A
# tool_kind: five repository tools (section G1); TV-015 and TV-016 also validate external tools (OpenSCAD,
# FreeCAD, kicad-cli), so section G2 is answered for them too
tool_kind: repository-tool
acc_proposed: [ACC-SCAD2STEP-001, ACC-KICAD-001, ACC-NORMFAB-001, ACC-TPM-001, ACC-CSA-001, ACC-COMMITMSG-001]
# product_size: iteration 1 text kept. Iteration 2 delta (2bfe001..99feb43 over the TV-015 products): tool unchanged;
# test module +81 lines (6 tests, 28 in all); fixture 11 to 15 files (+187 lines: double 14, stand-ins 173) and
# known-answers.json +48; TV-015 +30 -13 lines; run 2 log 73 lines; lock +4 -3; README +1 -1
product_size: 5 records (514 lines), 17 purposes, 118 known-answer tests (22 + 38 + 12 + 33 + 13, 0 skipped), 32 fixture files in 4 trees; 5 tools 1990 lines, 6 test modules 1579 lines
sprint: PDR-prep
author_agent: "author:WP-PDR-07 wave 1a (Claude as tool owner)"
tool_author_agent: "author:WP-PDR-07 wave 1a (Claude as tool owner)"
# reviewer_agent_reissue_1: "reviewer:WP-PDR-07-tv-015-to-tv-019-iter2-reissue1 (independent; authored no part of WP-PDR-07,
# of TV-015 to TV-019, of TV-014, of the five tools, of the INSP-038 fix commits or of iterations 1 and 2)"
reviewer_agent: "reviewer:WP-PDR-07-tv-015-to-tv-019-iter2 (independent; authored no part of WP-PDR-07, of TV-015 to TV-019, of the five tools or of the finding-1 fix)"
reviewer_agent_iteration_1: "reviewer:WP-PDR-07-tv-015-to-tv-019-iter1 (independent; authored no part of WP-PDR-07, of TV-015 to TV-019 or of the five tools)"
# criticality: neither (03 sections 4.3.1 and 6.1.1: no tool is a safety-critical or mission-critical
# component). 07 section 2.1.1: TV records have no row; code of a "Neither" component needs no assurance review
# unless the file holds unsafe (Python has none). The swe-136 and swe-070 section 7.1 tasks are answered in
# section H by this reviewer as the assurance function (charter section 2)
criticality: neither
assurance_required: false
assurance_reviewer_agent: none
iteration: 2
# readiness_met (iteration 2): true. R1, R2, R4 and R5 are met on the re-frozen products. R3 still fails, and only
# for other records: validate_docs exits 1 on eight other records' drift (97 passed, 8 failed at 1353bb3; this record
# PASS) and test_validate_docs.RepositoryTests.test_repository_exit_zero fails for that reason (550 tests, 1
# failure). Iteration 1 held R3 against readiness; this iteration reads it as "No, not attributable to this
# product", as INSP-040 and INSP-041 iteration 2 did for the same condition (section "Iteration 2", R3 row).
# Iteration 1 value: false
readiness_met: true
# reviewer_verdict (iteration 2): APPROVED. finding-1 (Major) Verified; findings 2 to 11 are Minor and Open, liens due
# at the CDR readiness declaration (plan rule C1; PDR package section 15). Iteration 1: NEEDS CHANGES
reviewer_verdict: APPROVED
assurance_verdict: not-required
# verdict: APPROVED. No software assurance pair is required (07 section 2.1.1: code of a "Neither" component
# without unsafe; TV records have no row; cross item X-7), and every reviewed blob is on main (no cr/ branch blob),
# so the record verdict follows the reviewer verdict. Accreditation stays the owner's decision (05 section 9.2 step 3)
verdict: APPROVED
findings_major: 1
findings_minor: 10
findings_open: 10
findings_fixed: 0
findings_verified: 1
findings_deferred: 0
assurance_findings_major: 0
assurance_findings_minor: 0
assurance_tasks_applied: [swe-136 7.1 task 1, swe-070 7.1 task 1]
unsafe_sites_reviewed: 0
deferred_rids: []
# items_no (iteration 2): TV-F1 is Yes for every record now (it was No for TV-015 only, finding-1). TV-B3 and TV-C2
# stay No for TV-017 and TV-018 (Minor findings 5, 6, 7), and are Yes for TV-015
items_no: [TV-A2, TV-B2, TV-B3, TV-C2, TV-E1, TV-G1-1, CK-CODE-E1, CK-CODE-E9, CK-CODE-G1]
# effort (cumulative; iteration 2: 34 turns, 40 minutes; iteration 2 re-issue 1: 16 turns, 15 minutes)
effort_turns: 135
effort_minutes: 110
record_status: Open
date: 2026-09-27
date_closed: null
---

# Peer review record INSP-088: tool validation TV-015 to TV-019 (WP-PDR-07 wave 1a tools), iterations 1 and 2

**Products:** the five TV records `docs/cm/tool-validation/TV-015-openscad-freecad-scad2step.md` to `TV-019-check-commit-msg.md`, the five tools, their six known-answer modules, the four fixture trees, the procedure and the six run 1 transcripts, the two inspected renders, the TV index, `tools/toolchain.lock.md` and `tools/README.md`, all at the freeze commit `2bfe001` on `main` (`product_files`; each blob recomputed with `git rev-parse 2bfe001:<path>` and `HEAD:<path>` at HEAD `c91a9eb`: all 32 path identities of the brief equal, and the fixture trees `d9ab4c7d`, `03063f2a`, `9a6aff25`, `92fd0e50` equal). After that check, `d9c7f69` (TV-014 run 4) changed `tools/toolchain.lock.md` to blob `83bc0520`. `git diff 2bfe001 HEAD -- tools/toolchain.lock.md` touches only the LTspice rows (sections 1, 1.1, 1.2, 1.4 finding 15, the section 5 TV-014 row, history). No row this record cites changed, so the reviewed blob stays `4e978efc`. **Checklists:** the tool validation checklist of WP-PDR-03 (revision A, blob `7be809d4`, CR-012 branch), applied item by item to each record in sections A to H below, and the code checklist revision B for the five sources (section "Code review").

**Acceptance criteria (rule C7): every case the governing clauses enumerate.**
- 05 section 9.2 step 1 fields, for each record: version string and command, install source with URL and SHA-256, class, one-line purposes, known answer, fixture paths, run command, pass criteria, result with date, commit and excerpt, class A reproducibility, limitations, triggers.
- 05 section 9.1: class A known answer plus reproducibility (TV-015, and TV-016 for the exports); class B known answer with a seeded fault (TV-016 ERC, DRC and normalization, TV-017, TV-018, TV-019).
- 05 section 9.2 table rows:
  - kicad-cli: exactly the seeded ERC pin and DRC clearance and none on the clean files; the section 8.2 step 2 exports equal to the stored `SHA256SUMS.normalized`; PTH and NPTH hit counts in the report; CPL and BOM line for line; STEP box within 0.01 mm.
  - `tools/normalize_fab.py`: two exports at different times normalize equal; a one-byte copper change outside the date lines changes the hash.
  - OpenSCAD + FreeCAD with `tools/scad2step.py`: CSG to an absolute path; one valid solid and the stored box; the one-solid Compound unwrap; the success marker checked instead of the `freecadcmd` exit status.
- 05 section 8.2: every row of the normalization table; the step 3 checks (one valid solid, no BSpline faces, STEP volume within 0.5 % of the mesh).
- 05 section 6 items 1 to 13 and Table 6-1 (TV-018).
- 05 section 4.5 "Commit message", "Merges to main" and "Checks", and the Table 6-1 trailer metric (TV-019).
- 05 section 13 PDR row, including "installed as the `commit-msg` hook".
- WP-PDR-07 outputs:
  - smoke shell to STEP with the FreeCAD Compound fix;
  - kicad-cli 10.0.6 Gerber, drill and CPL exports normalized;
  - `tools/csa.py` equal to the hand CSA of WP-PDR-05 as known answer;
  - hook install note;
  - lock rows in sections 1.2 and 5.
- Every item of the tool validation checklist for `tool_kind` repository-tool (A to F, G1, H), plus G2 for the external tools of TV-015 and TV-016.
- The INSP-015 finding classes F-01 (a purpose wider than its known answer), F-02 (a result not tied to a commit), F-04 (a limitation contradicted by the tool) and F-05 (an undocumented or untested exit status).

**Independence (rule C4):** this invocation authored no part of WP-PDR-07 and edited no product file. **Search first:** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` was loaded at the start. Queries: "uses of tools/scad2step.py freecadcmd STEP export enclosure, tools/normalize_fab.py SHA256SUMS.normalized, render_tpm, csa.py, check_commit_msg hook"; "ADR-008 STEP acceptance checks one valid solid no BSpline volume within 0.5 percent restricted OpenSCAD dialect"; "SEMP Appendix F item F-15 tools to be written before PDR". One `git grep` for free INSP numbers ran before the first query. Every other `grep` and `git grep` ran afterwards, only to pin lines. **Headless:** every reviewer run is a command-line run. The runs wrote only to the session scratchpad and to `mktemp` directories that the tests remove. Nothing was downloaded or installed. **LTspice:** no LTspice process was started by this review. The first R3 attempt, a plain `unittest discover -s tools/tests` started at 13:20 CDT, includes `test_ltspice_batch.py`. That module called `tools/ltspice-batch.sh`, which was still waiting on its lock at 13:35 (`lockf -s -t 600`; the lock is held by orphaned Wine services, `d9c7f69`). The reviewer then stopped the run (its process and the waiting wrapper, exit 143) before any `wine` or `LTspice.exe` started; `ps` showed no `LTspice.exe`. R3 was re-run module by module without `test_ltspice_batch.py` (section "Reviewer re-runs"). TV-014 is outside this record.

## Iteration 1 (2026-09-27)

### Findings (filled by the reviewer; the owner ruling column is transcribed by Claude at the review)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | reviewer | Major | TV-B3, TV-C2, TV-F1 (INSP-015 F-01 class) | TV-015 section 2 purpose 2 (line 31), section 3 line 63, limitation 2 (line 98), section 9 ACC-SCAD2STEP-001 (line 119); `tools/scad2step.py` lines 138 to 139 (C4) and 147 to 153 (C6) | Purpose 2 claims refusal with exit 1 and no STEP left for "more than one solid (C4)" and "a STEP read-back that differs from the exported solid (C6)", and ACC-SCAD2STEP-001 accredits "purposes 1 to 4". No known answer or seeded fault reaches either branch. Section 3 and limitation 2 say so ("no source in the dialect produces them"). So the proposed accreditation covers two refusals that no test exercises. This is the same defect class as INSP-038 finding-2 in the same WP. Fix: either narrow purpose 2 and the scope statement to C2, C3, C5 and C7, and state C4 and C6 as unvalidated defensive checks; or add seeded cases that reach them, for example `freecad_convert` run under a test double of the `FreeCAD`, `Part` and `importCSG` modules that returns a CompSolid of two solids (C4) and a read-back of another volume (C6), each expected to print its `SCAD2STEP FAIL C4:` or `C6:` marker and leave no STEP | Open | Pending | |
| <a id="finding-2"></a>finding-2 | reviewer | Minor | TV-A2 | TV-015 line 24; TV-016 line 24; `tools/toolchain.lock.md` section 7 rows KiCad 10.0.6, OpenSCAD 2021.01, FreeCAD 1.1.3 and its lead paragraph | TV-015 says "no installer checksum is recorded there for either" and TV-016 says "no installer checksum recorded". Lock section 7 records the installer URL and SHA-256 of all three (`ef4dcd42...02dc68`, `4e4568e1...a3635e`, `f5c0ece7...2667c`). Its lead paragraph also says "the TV record of each tool confirms that its installed bundle matches the archived installer" for KiCad and OpenSCAD. Neither record makes that confirmation or says why it is replaced by the version string. Fix: cite the section 7 URL and SHA-256 in both records, and either record the confirmation or state the version-string substitute and amend the section 7 sentence | Open | Pending | |
| <a id="finding-3"></a>finding-3 | reviewer | Minor | CK-CODE-E1, CK-CODE-E6 | `tools/scad2step.py` docstring line 41 ("A failed run leaves no STEP file") against lines 238 to 256 and 263 to 272 | The driver deletes an existing STEP only in FreeCAD mode (line 114) or after `freecadcmd` returns (lines 276 and 293). An existing file at `--step` survives exit 3, exit 4, an OpenSCAD failure (exit 1) and the input-file usage errors. Reviewer check in the scratchpad: a STEP copied to `--step` was left in place after `CWHT_SCAD2STEP_EXPECT_OPENSCAD="OpenSCAD version 2021.02"` (exit 4) and after `CWHT_OPENSCAD=/nonexistent` (exit 3). In a release directory a stale `cwht-ENC-rev<X>.step` would survive a failed rerun. Fix: remove the output before the first check (or at every non-zero exit), and add the case to `DoubleTests` | Open | Pending | |
| <a id="finding-4"></a>finding-4 | reviewer | Minor | TV-B2 | ADR-008 section 2 ("exports STEP AP214"); TV-015 section 2 "Not covered" (line 35); `tools/scad2step.py` line 146 | ADR-008 states that the pipeline exports STEP AP214. The tool neither sets nor checks the schema. It relies on the FreeCAD default, which a FreeCAD user preference can change. The reviewer's conversions wrote `FILE_SCHEMA(('AUTOMOTIVE_DESIGN { 1 0 10303 214 1 1 1 1 }'))`, which is AP214. The use is named as not covered, and the vendor accepts AP214 or AP242 (research REQ-candidate), so the finding is Minor. Fix: check `FILE_SCHEMA` for the AP214 identifier (or set the export preference explicitly) and add it to the cube known answer, or amend the ADR-008 statement through its owner | Open | Pending | |
| <a id="finding-5"></a>finding-5 | reviewer | Minor | TV-B3, TV-C2 | TV-017 section 2 purpose 2 (line 28) ("a missing or duplicate key"); `tools/tests/fixtures/render_tpm/expected.json` block `seeded` (10 faults); `tools/render_tpm.py` line 95 | The seeded faults include "duplicate key" but no missing (or non-string) key. The `not isinstance(key, str)` operand of line 95 is therefore not exercised, although purpose 2 lists it. Fix: add a seeded fault that deletes `key` from one TPM, with its expected message `TPM-00N: missing or duplicate key None` | Open | Pending | |
| <a id="finding-6"></a>finding-6 | reviewer | Minor | TV-B3, CK-CODE-E1 | TV-018 section 2 purpose 4 (line 31) ("the same revision and date give the same bytes"); `tools/csa.py` docstring lines 4 and 5, lines 282 to 291, 535 and 556 to 559 | Three inputs of the report are not part of the revision. (1) The item 1 row "Local revision against `origin/main`" reads the local ref at run time, so the same revision and date give different bytes after a fetch or a push. (2) Items 1 and 3 read the tags as they exist at run time. (3) The Generator row prints the blob of `tools/csa.py` at the revision, not the blob of the file that ran, so a report made with a modified or newer generator names the wrong generator (05 section 6 item 1 "generator version"). `--check` of a committed CSA would then fail after the next push, and the header can misstate its generator. `test_output_is_reproducible` runs twice in one ref state, so it does not see (1) or (2). Fix: print the running file's blob (`git hash-object` of `__file__`) and flag a difference from the revision's; drop the `origin/main` row or move it behind `--remote`; state in purpose 4 that tags and remote refs are inputs | Open | Pending | |
| <a id="finding-7"></a>finding-7 | reviewer | Minor | TV-C2, R5 | WP-PDR-07 outputs ("equal to the hand CSA of WP-PDR-05 as known answer"); TV-018 section 3 `HandCsaTests` row (line 46) and header (line 6, "the hand CSA comparison included"); `tools/tests/fixtures/csa/hand-csa-9fd0962.json` (keys `tracked_files`, `rows`, `unmatched`, `change_log`, `lacking_trailers`) | The hand-CSA known answer covers items 2 (without levels), 6 and the trailer metric of item 10 only. Items 1, 3, 4, 9, 11, 12, 13 and the other item 10 metrics are not compared, although the author return says "every value it can derive matches". Reviewer comparison: `tools/csa.py --rev 9fd0962 --since baseline/srr --date 2026-09-27` against `b790eaa:docs/process/configuration-status.md`. The derivable values of items 3 (tag object, commit, memo, unsigned), 4 (the nine CRs, their classes, states and rows, CR-008 missing), 10 (five open CRs at 0 d, no cycle time, 3 commits lacking trailers), 11 (entries 1 to 4), 12 (`#W1`) and 13 (TBR counts 109, 14, 11, TPM 4 plus 1, hazard 17; open log items) are equal. Only the hand's notes differ. So no wrong value was found, but the comparison is not in the known answer. Fix: extend `hand-csa-9fd0962.json` and `HandCsaTests` to items 3, 4, 10, 12 and 13 (and 11 by table equality), or state in TV-018 section 3 exactly which items the hand comparison covers | Open | Pending | |
| <a id="finding-8"></a>finding-8 | reviewer | Minor | TV-E1 (INSP-015 F-04 class) | TV-018 limitation 3 (line 77) and section 2 "Not covered" (line 33); `tools/csa.py` docstring line 26 and line 720 ("each control holding a `tbr` field") against `_count_tbr` lines 458 to 466; 05 section 6 items 4, 7 and 8 | (a) Limitation 3 and the report heading say hazard TBRs are counted "per control holding a `tbr` field". `_count_tbr` counts every `tbr` object: 17 at `9fd0962` (HZ-004 K4 holds two), not the 16 controls, which also equals the hand's "17 items". (b) The "Not covered" list omits parts of 05 section 6 that the tool does not produce: item 4 "affected CIs and IDs" (rows only) and "Deferred CRs with their re-look trigger"; item 7 per-release fields (version, commits S and A, ELF and UF2 SHA-256, VDD, units) beyond tags and directories; item 8 date, auditor, result and open discrepancies (paths only). None applies before CDR. Fix: correct limitation 3 and the heading; list (b) under "Not covered" or in the limitations, so that ACC-CSA-001 is bounded by them | Open | Pending | |
| <a id="finding-9"></a>finding-9 | reviewer | Minor | TV-G1-1 | `tools/tests/test_csa.py` lines 60 to 65 (`Table41ParseTests.test_real_cm_plan_parses_55_rows_or_more`); TV-018 section 3 pass criteria (line 52, "28 fixture tests") | A test in a fixture-only class reads the repository's own `docs/process/05-configuration-and-data-management.md`. It is repository content, which the template and 05 section 9.2 keep apart from the validation, and it is counted among the 28 fixture tests. A later edit of 05 (CR-007 adds rows; a row 28 rewrite) can fail the validation for a reason outside the tool. Fix: move it to `HandCsaTests` (or a `RepositoryTests` class) and recount the pass criteria | Open | Pending | |
| <a id="finding-10"></a>finding-10 | reviewer | Minor | TV-E1, CK-CODE-E1 | `tools/check_commit_msg.py` line 275 (`os.path.join(root, ".git", "MERGE_HEAD")`) and lines 270 to 271; TV-019 section 9 OA-TV019-1 hook text (lines 93 to 96), limitation 4 (line 72); `tools/check_commit_msg.py` docstring lines 42 to 44 | (a) In a linked worktree `.git` is a file, so a merge in progress is never seen as a merge. A `merge(CR-NNN)` subject would fail SUBJECT there. Reviewer demonstration in a scratch repository: after `git merge --no-ff --no-commit` in a linked worktree, `git rev-parse --git-path MERGE_HEAD` exists and the tool's path does not. (b) The OA-TV019-1 hook runs `.venv/bin/python tools/check_commit_msg.py` relative to the worktree top. `.venv` is untracked, so in any linked worktree (the WP worktrees under the scratchpad, for example the `cr/CR-014` worktree now registered) the hook exits 127 and blocks every commit. (c) With `git commit --amend` the hook compares the index with HEAD, the commit being amended, so only the newly staged files are checked; limitation 4 does not say so. Fix: use `git rev-parse --git-path MERGE_HEAD`; write the hook with the absolute interpreter and tool paths of the main worktree (or `git rev-parse --git-common-dir`); detect an amend or state it in limitation 4; add a worktree case to `HookTests` | Open | Pending | |
| <a id="finding-11"></a>finding-11 | reviewer | Minor | CK-CODE-E9, CK-CODE-G1 | `tools/check_commit_msg.py` line 70; `tools/normalize_fab.py` lines 165 to 170 and 181 | (a) `CI_KINDS_FAIL` is defined and never used; `tools/csa.py` line 682 repeats the tuple. (b) `--write DIR` joins zip member names into `DIR` without a containment check. A member named `../x` writes outside `DIR`, and a `!` in a plain file name is turned into a directory separator. Fix: remove or use the constant; resolve each `--write` destination and refuse one outside `DIR` (exit 2), with a seeded zip in `CliTests` | Open | Pending | |

### Per-record results

| TV record | Tool and version | Class | Commit tested | Reviewer re-run (command, exit, result) | Items answered No | Finding ids |
|---|---|---|---|---|---|---|
| TV-015 | OpenSCAD `OpenSCAD version 2021.01`, FreeCAD `1.1.3`, `tools/scad2step.py` blob `d0277ec8` | A | `0743499` | `.venv/bin/python -m unittest discover -v -s tools/tests -p test_scad2step.py` at 13:10 CDT (every product blob equal to `2bfe001`): exit 0, 22 run, 22 passed, 0 skipped, 31.5 s; same as run 1. Class A: two driver conversions of `smoke-shell.scad` 14 s apart, raw SHA-256 `f9c514ac...` and `7c473023...`, bodies equal apart from the `FILE_NAME` line (`diff`), `normalize_fab.py` hash `130bb77a...` for both | TV-B2, TV-B3, TV-C2, TV-F1, TV-A2, CK-CODE-E1 | finding-1 to finding-4 |
| TV-016 | kicad-cli `10.0.6`; `tools/normalize_fab.py` blob `f3eaac39` | A (exports), B (ERC, DRC, normalization) | `c90df2d` | `-p test_normalize_fab.py`: exit 0, 24 passed; `-p test_kicad_cli.py`: exit 0, 14 passed, 0 skipped; same as run 1 | TV-A2, CK-CODE-G1 | finding-2, finding-11 |
| TV-017 | `tools/render_tpm.py` blob `f37985d6`, matplotlib 3.11.2, pillow 12.3.0 | B | `c90df2d` | `-p test_render_tpm.py`: exit 0, 12 passed, 0 skipped; same as run 1. Both committed renders opened and inspected (section "Visual closure") | TV-B3, TV-C2 | finding-5 |
| TV-018 | `tools/csa.py` blob `dd9b6fed` with `tools/check_commit_msg.py` blob `5488dd98` | B | `b308f8c` | `-p test_csa.py`: exit 0, 33 passed, 0 skipped, 24.8 s; same as run 1. Hand CSA comparison at `9fd0962` (finding-7): exit 0, derivable values of items 3, 4, 10 to 13 equal | TV-B3, TV-C2, TV-E1, TV-G1-1, CK-CODE-E1 | finding-6 to finding-9 |
| TV-019 | `tools/check_commit_msg.py` blob `5488dd98` with `tools/csa.py` blob `dd9b6fed`, git 2.50.1 | B | `b308f8c` | `-p test_check_commit_msg.py`: exit 0, 13 passed, 0 skipped; same as run 1. Audit `--range baseline/srr..2bfe001`: exit 1, 93 commits, 39 REFS_MISSING and 3 SUBJECT failures; the WP-PDR-07 commits `c90df2d`, `d9dd7bb`, `b308f8c` pass and `2bfe001` warns MIXED_ROW (row 27, a Log change of the lock by 05 section 9.2 step 5); `86ff3b0` fails REFS_MISSING as TV-019 finding 1 states | TV-E1, CK-CODE-E1, CK-CODE-E9 | finding-10, finding-11 |

### Per-purpose results

| TV record | Purpose | Known answer that exercises it | Seeded fault (class B) | Cited uses of the purpose in the project | Finding ids |
|---|---|---|---|---|---|
| TV-015 | 1: `.scad` to CSG (absolute `-o`) to a one-solid STEP with the Compound unwrap and the KAT line | `ConversionTests` (cube: root Compound, 7 faces, 1 cylinder, 5717.257 mm^3, box 0..30, 0..20, 0..10), `test_cm_plan_form_freecad_mode`, `SmokeShellTests` (31 faces, 16 cylinders, 24721.22 mm^3) | class A: none required | 05 section 8.2 step 3 (enclosure release package); ADR-008 section 2; RSK family S1 (acceptance checks run and logged); reconciliation-srr ADR-008 assumption 1 (PDR smoke shell); WP-PDR-39 | finding-4 |
| TV-015 | 2: refuse C2 to C7 with exit 1 and no STEP | `SeededCsgTests`: C2 (`two-roots`, `nonuniform-scale`), C3 (`two-solids`), C5 (`twist`), C7 (cube CSG with the `taller` mesh) | as the known answer; none for C4 and C6 | 05 section 8.2 step 3; ADR-008 acceptance checks | finding-1 |
| TV-015 | 3: version (exit 4), not installed (3), no marker (1), time-out of its own group (124), usage (2) | `DoubleTests` (5), `ConversionTests` version cases (3), `UsageTests` (8 command lines) | as the known answer | lock section 1.4 findings 3 and 4; 05 section 9.2 table row | finding-3 |
| TV-015 | 4: two conversions differ only in the `FILE_NAME` time stamp | `ReproducibilityTests`; procedure part D; reviewer run on the smoke shell | class A | 05 section 9.1 class A; section 9.2 step 1 | none |
| TV-016 | 1: ERC and DRC report exactly the violations present | `ErcDrcTests` (4): clean exit 0 none; seeded ERC exit 5 `pin_not_connected` R1 pin 2; seeded DRC exit 5 one 0.1 mm clearance | the seeded schematic and board | 05 section 8.2 step 1 (ERC and DRC clean before release); WP-PDR-37 preliminary schematic and floorplan | none |
| TV-016 | 2: the section 8.2 step 2 exports F3, F6, F7 plus BOM and STEP carry the board's content | `ExportTests` (5): 9 Gerbers plus the job file, PTH 1 at 0.7 mm and NPTH 1 at 3.2 mm in files and report, CPL and BOM line for line, STEP box 0..30, 0..20, 0..1.51 | class A: `NormalizedExportTests` reproducibility | 05 section 8.2 step 2; PCA-01 | none |
| TV-016 | 3: normalize exactly the section 8.2 table; `--sums`, `--check`; zip members | `RuleTests` (10, one per table row with hand-written expected bytes), `CliTests` (10), `NormalizedExportTests` against the grep and perl list `expected/clean-SHA256SUMS.normalized` | `SeededFaultTests` (4); the one-byte `clean-F_Cu.gbr` change exits 1 with exactly one `CHANGED` | 05 section 8.2 step 2 `SHA256SUMS.normalized`; PCA-01; 05 section 9.2 table row | finding-11 |
| TV-017 | 1: status of every TPM at a review and as-of date | `RowKnownAnswerTests` (3) at PDR 2026-10-06 and TRR-D2 2027-02-01 against `expected.json` | the late entry and the not-reporting TPM | SEMP section 7.4; `tpm.json` `reporting_interval` (1) and `status_rule`; WP-PDR-29 package figures | none |
| TV-017 | 2: refuse malformed drawn data with exit 1 and nothing written | `SeededFaultTests` (2) | ten seeded faults and an empty `tpms`; no missing key | as purpose 1 | finding-5 |
| TV-017 | 3: `tpm-status.png`, `tpm-table.md`, `tpm-trend-<key>.png`; `--check` writes nothing | `RenderTests` (5): files, counts, pixel sizes, chip colour per row, Markdown rows | exit 2 cases in `UsageTests` | `docs/reviews/PDR/figures/` (WP-PDR-29); review package TPM table | none |
| TV-018 | 1: Table 4-1 parse and the 05 section 4.2 matching rule | `Table41ParseTests`, `MatchRuleTests`, `FixtureRepoTests.test_rows`, `HandCsaTests` row counts | misnumbered and missing table; ties; unmatched | 05 section 6 item 2; section 7.4 interim check | finding-9 |
| TV-018 | 2: per-row count, hash, last commit, CRs, records, level | `FixtureRepoTests` (rows, last commits, hashes equal to `git rev-parse`), `HandCsaTests` | the unmatched status note; `--strict` | 05 section 6 item 2 (levels excluded by ACC-CSA-001) | finding-7 |
| TV-018 | 3: items 1, 3 to 13 | `FixtureRepoTests` (baseline, CR register with CR-003 missing, editorial log, change log, metrics, deviations, waiver, TBRs, open log items, release and audit "None") | c2, c7, c13 flagged; c3, c4, c8, c11 not flagged | 05 section 6 and Table 6-1; the PDR package CSA (WP-PDR-48) | finding-7, finding-8 |
| TV-018 | 4: write, `--check`, `--strict`, exit statuses, reproducibility | `CliTests` (5), `test_output_is_reproducible` | a hand edit makes `--check` exit 1; an unmatched file makes `--strict` exit 1 | 05 section 6 (hand edits prohibited once accredited; the `--check` audit) | finding-6 |
| TV-019 | 1: subject rule | `SubjectTests` (2); c9 | the six bad subjects; `merge(...)` on a non-merge | 05 section 4.5 "Commit message" and "Merges to main" | finding-10 |
| TV-019 | 2: trailer rules REFS_MISSING, REFS_UNRECOGNIZED, CR_ID_BAD, CR_TRAILER_MISSING, MIXED_ROW, SPLIT_CR_FROM | `RangeTests` (15 fixture commits against `expected.json`), `RefsTests` (29 forms), `RepositoryTests` (the three hand-CSA commits) | c2, c7, c10, c12, c13 fail; c5, c6 warn; c8, c11 and the merge pass | 05 section 4.5 "Checks"; Table 6-1 trailer metric; TV-018 item 6 | none |
| TV-019 | 3: hook, audit and message-file modes with exit 0, 1, 2 | `HookTests` (5), `RangeTests`, `UsageTests` (6 cases) | a staged row 2 change without trailers fails; a `Refs:` line cut off by a blank line fails | 05 section 13 PDR row (hook); OA-TV019-1 | finding-10 |

## Readiness criteria

| # | Criterion | Answer | Evidence |
|---|---|---|---|
| R1 | Everything committed; `product_files` lists every blob; `fixture_trees` gives the trees | Yes | every identity of the brief recomputed at `2bfe001` and HEAD (equal); `git ls-tree -r 2bfe001` of the four fixture directories gives the 32 files listed; `git status --short` shows no change under `tools/` or `docs/cm/` |
| R2 | Each record's section 3 command exits 0 on the committed state | Yes | the six module runs of the per-record table, 13:10 to 13:11 CDT, all exit 0 with the recorded counts and no skip; the procedure itself was not re-run, because its part E overwrites the committed renders (the module runs are its part C) |
| R3 | `unittest discover -s tools/tests` passes and `validate_docs.py` exits 0 | No (not caused by these products) | At HEAD `d9c7f69`, the 20 modules other than `test_ltspice_batch.py` were run one by one (that module was left out: LTspice is outside this wave). All passed except `test_validate_docs.RepositoryTests.test_repository_exit_zero`. `validate_docs.py` exits 1: 88 passed, 8 failed. This record passes. The eight failing records are other WPs' record drift: INSP-015 on the TV README and lock, the SRR ADR, TS and 02 records, and the PDR `cm-plan-05-software-assurance`, `configuration-status` and `lessons-learned` records. No product of this record causes a failure, so R3 does not change a finding here |
| R4 | Lock rows (sections 1, 1.1, 1.2, 5) and README index rows exist | Yes | lock blob `4e978efc` lines 11, 45, 46 (section 1), 67, 68, 96, 101 to 103 (section 1.1), 122 to 128 (section 1.2), 269 to 273 (section 5), 311 (history); README lines 39 to 43; `tools/README.md` line 21 |
| R5 | The author return lists purposes, cited uses, tests, runs with commits, proposed scope | Yes, with finding-7 | author summary in the brief (per tool: purposes, known answers, run 1 with commit and counts); scopes in each section 9; "every value it can derive matches" overstates the test (finding-7) |

## A. Identification

| Id | TV-015 | TV-016 | TV-017 | TV-018 | TV-019 |
|---|---|---|---|---|---|
| TV-A1 | Yes: reviewer 13:18 CDT `OpenSCAD --version` last line `OpenSCAD version 2021.01`; `defaults read .../Info.plist CFBundleVersion` `1.1.3`; KAT line `freecad=1.1.3` | Yes: `kicad-cli version` `10.0.6`; `test_locked_version` passed | Yes: interpreter `Python 3.13.5`; matplotlib `3.11.2`, pillow `12.3.0` | Yes: `Python 3.13.5`; `git version 2.50.1 (Apple Git-155)` | Yes: as TV-018 |
| TV-A2 | No (Minor): lock section 7 has URL and SHA-256; the record says none (finding-2) | No (Minor): as TV-015 (finding-2) | Yes: repository and `tools/requirements.txt` | Yes: repository | Yes: repository |
| TV-A3 | Yes: SHA-256 `004c0b3f...` (tool), `88570c47...` (module), fixture digest `55ff76df...` recomputed, equal | Yes: `f22d843c...`, `4bb1169f...`, `377f57a5...`, digest `0d9fca9d...`, equal | Yes: `95a0cffb...`, `18f5232b...`, digest `02c031f2...`, renders `af7a8ac9...` and `bca50ca4...`, equal | Yes: `919d3d56...`, `a805a681...`, digest `cdc66c09...`, equal | Yes: `8e7e981d...`, `e87d78dc...`, digest `cdc66c09...`, equal |
| TV-A4 | Yes: `git rev-parse 0743499:` gives `d0277ec8`, `2e2fc392`, tree `d9ab4c7d`; transcript part A "unchanged from HEAD", 0 untracked | Yes: `c90df2d` gives `f3eaac39`, `707a22d5`, `780117af`, tree `03063f2a` | Yes: `c90df2d` gives `f37985d6`, `a6b93352`, tree `9a6aff25` | Yes: `b308f8c` gives `dd9b6fed`, `5488dd98`, `58672f3a`, tree `92fd0e50`, 05 `f8de2081` | Yes: `b308f8c` gives `5488dd98`, `dd9b6fed`, `d8595b98`, tree `92fd0e50` |
| TV-A5 | Yes: A, the CSG and STEP enter the enclosure release package (05 section 9.1 row A) | Yes: A for the exports, B for ERC, DRC and `normalize_fab.py` (05 section 9.1 rows A and B) | Yes: B (05 section 9.1 row B names `tools/render_tpm.py`) | Yes: B (row B names `tools/csa.py`) | Yes: B (row B names `tools/check_commit_msg.py`) |
| TV-A6 | Yes: command line only; `freecadcmd` headless | Yes: `kicad-cli` only | Yes: Agg backend | Yes: git plumbing only, no network without `--remote` | Yes; the hook install is an owner configuration step (OA-TV019-1), not a GUI step |

## B. Purposes

| Id | TV-015 | TV-016 | TV-017 | TV-018 | TV-019 |
|---|---|---|---|---|---|
| TV-B1 | Yes: four one-line purposes with inputs, outputs and exits (lines 30 to 33) | Yes: three (lines 28 to 30) | Yes: three (lines 27 to 29) | Yes: four (lines 28 to 31) | Yes: three (lines 27 to 29) |
| TV-B2 | No (Minor): every cited use (05 section 8.2 step 3, ADR-008 acceptance checks, the RSK S1 step, the smoke-shell assumption) is covered except the ADR-008 AP214 statement (finding-4) | Yes: 05 section 8.2 steps 1 and 2, PCA-01, WP-PDR-37 ERC and DRC. The `pcbway_package.sh` checks are rightly excluded (due CDR) | Yes: SEMP section 7.4 and `tpm.json` `reporting_interval` (table with alert colour, trend plots; `review-trend` left to `tools/review_trend.py`) | Yes: 05 section 6, Table 6-1, the WP-PDR-48 CSA; levels excluded from scope | Yes: 05 section 4.5 "Checks", Table 6-1, TV-018 item 6 |
| TV-B3 | No: C4 and C6 in purpose 2 (finding-1, Major) | Yes: every table row, the zip handling and the listed exits have a case | No (Minor): "missing key" (finding-5) | No (Minor): purpose 4 reproducibility (finding-6) | Yes: each rule name, mode and exit status is exercised |

## C. Known-answer test

| Id | TV-015 | TV-016 | TV-017 | TV-018 | TV-019 |
|---|---|---|---|---|---|
| TV-C1 | Yes: `tools/tests/fixtures/openscad/` (11 files), `known-answers.json` block `scad2step`, section 3 command and numeric criteria (22 run, none skipped) | Yes: `tools/tests/fixtures/kicad/` (15 files), `expected/`, criteria 24 and 14, none skipped | Yes: `tools/tests/fixtures/render_tpm/` (2 files), criteria 12 | Yes: `tools/tests/fixtures/csa/` (4 files), criteria 33 | Yes: shared `csa` fixture, block `check_commit_msg`, criteria 13 |
| TV-C2 | No: C4, C6 (finding-1) | Yes | No (Minor): finding-5 | No (Minor): finding-7 | Yes |
| TV-C3 | Yes: reviewer recomputation of the smoke shell: outer 110 x 62 - (4 - pi) 16 = 6806.2655 mm^2 x 18 = 122512.78; pocket 106 x 58 - (4 - pi) 4 = 6144.566 x 16 = 98313.06; four holes pi 1.25^2 x 2 = 39.27; four bosses pi (9 - 1.5625) 6 = 560.77; total 24721.22 mm^3. Faces 16 plus 15. Cube 6000 - 90 pi = 5717.257; mesh 6000 - 32 sin(pi/32) 90 = 5717.711 | Yes: expected list from `make_expected_normalized.sh` (grep -v and perl from the 05 table, not the tool); `RuleTests` expected bytes written by hand; ERC, DRC, drill, CPL, BOM, box from the 2026-09-25 hand derivation | Yes: `expected.json` derived from the status rule; reviewer check of the seven rows of the render against the rule (red for TPM-004, -005, -007 at a reporting review without a PDR entry; grey for TPM-006) | Yes: `expected.json` hand-derived for the `build_repo.py` plan; `hand-csa-9fd0962.json` parsed from the hand issue, not from the tool | Yes: findings derived from the commit plan of `build_repo.py`; `RepositoryTests` against the hand CSA section 10 |
| TV-C4 | Yes: 05 section 9.2 row: CSG to an absolute path (driver line 247), one valid solid and the stored box (`test_step_bounding_box`), Compound unwrap (`root=Compound`), marker instead of exit status (`test_freecad_mode_missing_environment`) | Yes: 05 section 9.2 rows kicad-cli (seeded ERC and DRC exactly, clean none, normalized exports equal to the stored list, PTH and NPTH counts, CPL and BOM, box 0.01 mm) and `normalize_fab.py` (two exports, one-byte copper change) | N/A: no 05 section 9.2 row | N/A: no 05 section 9.2 row (the WP clause is TV-C2) | N/A: no 05 section 9.2 row |
| TV-C5 | Yes: 22 of 22 | Yes: 24 and 14 | Yes: 12 | Yes: 33 | Yes: 13 |

## D. Results and reproducibility

| Id | TV-015 | TV-016 | TV-017 | TV-018 | TV-019 |
|---|---|---|---|---|---|
| TV-D1 | Yes: run 1 row with 12:51 CDT, `0743499`, counts, KAT excerpt and part D hashes; transcript lines agree | Yes: 12:49 CDT, `c90df2d`, 24 and 14 | Yes: 12:48 CDT, `c90df2d`, 12, render SHA-256 equal to the committed files | Yes: 12:58 CDT, `b308f8c`, 33 | Yes: 12:58 CDT, `b308f8c`, 13 |
| TV-D2 | Yes: lock line 96 run 1 and line 269 Validated | Yes: lines 67, 68 and 270 | Yes: lines 101 and 271 | Yes: lines 102 and 272 | Yes: lines 103 and 273 |
| TV-D3 | Yes: part D (cube) and the reviewer's smoke-shell pair: identical after the `FILE_NAME` time stamp is normalized | Yes: `NormalizedExportTests` two exports 1.1 s apart normalize equal (18 files) | N/A (class B) | N/A (class B); `test_output_is_reproducible` (see finding-6) | N/A (class B) |

## E. Limitations and re-validation triggers

| Id | TV-015 | TV-016 | TV-017 | TV-018 | TV-019 |
|---|---|---|---|---|---|
| TV-E1 | Yes: limitation 4 confirmed by code (version strings only, lines 241 to 246 and 267 to 272, no bundle hash); limitation 5 (`_hooked` prints `TEST HOOK`, line 182). The docstring claim of finding-3 is not a limitation | Yes: limitation 5 confirmed (`normalize()` returns "raw" for `.json`, line 116; TV-016 finding 2 routed as cross item X-4); limitation 1 by the fixture (2 layers, 3 footprints) | Yes: limitation 4 confirmed (`short_units`, line 151; the render shows "percent of allocation", "USD per unit") | No (Minor): limitation 3 misdescribes the count; omitted 05 section 6 parts (finding-8). Limitation 4 confirmed (cycle time from `date_opened`, line 693) | No (Minor): limitation 4 incomplete (finding-10). Limitation 3 confirmed (`clean_message`, line 142) |
| TV-E2 | Yes: tool, module, fixture; OpenSCAD or FreeCAD version or reinstall; macOS major; interpreter; class A expiry; defect with NCR | Yes: as TV-015 plus the 05 section 8.2 table and commands | Yes: tool, module, fixture; matplotlib, pillow, interpreter, macOS; `tpm.schema.json` pattern and `status_rule`; defect | Yes: tool, `check_commit_msg.py`, module, fixture; 05 Table 4-1 format, CR and record front matter; git, interpreter, macOS; defect | Yes: tool, `csa.py`, module, fixture; 05 section 4.5, Table 4-1, charter section 6, index format; git, interpreter, macOS; defect |

## F. Accreditation readiness, schedule and indexes

| Id | TV-015 | TV-016 | TV-017 | TV-018 | TV-019 |
|---|---|---|---|---|---|
| TV-F1 | No: ACC-SCAD2STEP-001 covers C4 and C6 (finding-1); otherwise it names the blob, the driver without hooks, the locked paths, the dialect and one top-level object | Yes: ACC-KICAD-001 (commands, severities, path) and ACC-NORMFAB-001 (blob, interpreter, kicad-cli 10.0.6 outputs) | Yes: blob, interpreter, matplotlib | Yes, with finding-6 and finding-8 to be reflected: blob pair, git, levels excluded | Yes: blob pair, interpreter, git |
| TV-F2 | Yes: due PDR (05 section 13); first use WP-PDR-39 | Yes: due PDR; first use WP-PDR-37 | Yes: due PDR; first use WP-PDR-29 figures | Yes: due PDR; the CSA stays hand-written until accreditation | Yes: due PDR with the hook |
| TV-F3 | Yes: README line 39, lock line 269 and header agree (Validated, PDR) | Yes: README line 40, lock line 270 | Yes: README line 41, lock line 271 | Yes: README line 42, lock line 272 | Yes: README line 43, lock line 273, header (hook not installed) |
| TV-F4 | Yes: section 9 leaves the decision to the owner; limitation 7 developer evidence | Yes: limitation 6 | Yes: limitation 5 | Yes: limitation 7; header | Yes: limitation 6; OA-TV019-1 after accreditation |
| TV-F5 | N/A: first record | N/A | N/A | N/A | N/A |

## G1. Repository tools

| Id | TV-015 | TV-016 | TV-017 | TV-018 | TV-019 |
|---|---|---|---|---|---|
| TV-G1-1 | Yes: every class reads only the fixture and the installed programs | Yes: both modules fixture-only | Yes: `RepositoryTests` separate and excluded from the 11 fixture tests | No (Minor): finding-9 | Yes: `RepositoryTests` separate |
| TV-G1-2 | Yes: 0, 1, 2, 3, 4, 124 each have a case | Yes: 0, 1, 2 | Yes: 0, 1, 2 | Yes: 0, 1, 2 | Yes: 0, 1, 2 |
| TV-G1-3 | Yes: section "Code review" at blob `d0277ec8` | Yes: at `f3eaac39` | Yes: at `f37985d6` | Yes: at `dd9b6fed` | Yes: at `5488dd98` |

## G2. External tools (TV-015 and TV-016)

| Id | TV-015 | TV-016 |
|---|---|---|
| TV-G2-1 | Yes: the locked paths (lines 58 to 61); the absolute `-o` of lock section 1.4 finding 3 (line 247); the marker, not the `freecadcmd` exit status (finding 4). The ACC scope requires the driver form while 05 section 8.2 step 3 prints the `freecadcmd tools/scad2step.py` form (cross item X-3) | Yes: `export_all` uses the 05 section 8.2 step 2 flags F3, F6, F7 exactly (compared flag by flag with 05 line 400) |
| TV-G2-2 | Yes: `_run` starts a new session and kills its process group only (lines 186 to 200); `test_timeout_kills_own_process_group` | Yes, as applicable: kicad-cli has no hang finding in lock section 1.4; each call has a 300 s `subprocess` time-out |
| TV-G2-3 | Yes: no download or install for TV-015 (lock history 2026-09-27 row line 311: "No tool version changed") | Yes: as TV-015 |

## G3, G4

N/A: no emulator, no instrument firmware.

## H. Software assurance tasks

| Id | Answer | Evidence |
|---|---|---|
| TV-H1 | N/A for all five | swe-136 7.1 task 1 applied: none of the five builds or checks firmware, so no 07 section 8.4 gate step cites them. `check_commit_msg.py` checks CM trailers, not a software gate |
| TV-H2 | Yes for TV-016 purpose 1; N/A for the others | swe-070 7.1 task 1 applied: kicad-cli ERC and DRC are the only analysis output among the five that is cited toward qualification of flight equipment (Inspection evidence of WP-PDR-37). TV-016 validates them with seeded faults, and limitation 2 pushes a project DRC rule file to its own seeded case. The other outputs are CM, product-generation and reporting outputs |
| TV-H3 | Yes | `assurance_tasks_applied` lists both tasks |

## Code review (peer-review-checklist-code.md revision B)

The code checklist is written for Rust firmware. For these Python host tools the reviewer applied the language-neutral intent of each item and lists the Rust-specific items as N/A, as INSP-015, INSP-038 and INSP-042 did. Criticality neither; no `unsafe` (07 section 2.1.1: no assurance review). Measured with `wc -l` and the `ast` line spans of each function.

| Tool (blob) | Lines | Longest functions |
|---|---|---|
| `tools/scad2step.py` (`d0277ec8`) | 314 | `driver` 97, `freecad_convert` 67 |
| `tools/normalize_fab.py` (`f3eaac39`) | 259 | `main` 52 |
| `tools/render_tpm.py` (`f37985d6`) | 323 | `main` 65 |
| `tools/csa.py` (`dd9b6fed`) | 810 | `build` 234, `main` 60 |
| `tools/check_commit_msg.py` (`5488dd98`) | 284 | `evaluate` 58, `main` 53 |

All five compile (`py_compile`).

| Id | Answer | Evidence |
|---|---|---|
| R1 to R6 | N/A | Rust gates and firmware tags. CS-18 (R2, D7) is a firmware rule (07 section 7); `csa.py` 810 lines and `build` 234 lines are recorded for the measurement only, as INSP-042 did for `traceability.py` |
| CK-CODE-A1 to A3, B1 to B8, C4 to C7, D1, D3, D5, D6, D8, D9, E2 to E4, E7, E8, F1 to F3, G2 to G5, H3, I1 to I3, J1, J2 | N/A | Rust, firmware, register, keyer, safe-state, MC/DC and traceability-tag items do not apply to host Python tools |
| CK-CODE-C1 | Yes | No unguarded abort path. Each tool maps its errors to its documented exit statuses: `CheckFailed` and the catch-all in FreeCAD mode (scad2step lines 165 to 169); `UsageError` and `OSError` to 2 (normalize_fab lines 253 to 255); `DataError` to 1 (render_tpm line 284); `CsaError` to 2 (csa line 774); `CsaError` and `CalledProcessError` to 2 (check_commit_msg line 278) |
| CK-CODE-C2 | Yes | Every documented failure has an exit status and a message on standard error |
| CK-CODE-C3 | Yes | Fail closed: a refusal withholds the product (no STEP in FreeCAD mode, nothing written by render_tpm, a non-zero `--check`) |
| CK-CODE-D2 | Yes | No recursion; loops over finite inputs; waits are bounded by time-outs (scad2step `_run`; kicad tests 300 s) |
| CK-CODE-D4 | Yes | No suppressed warnings except the documented `noqa` for the FreeCAD-only imports and the broad FreeCAD exception (scad2step lines 104 and 167) |
| CK-CODE-E1 | No (Minor) | Behaviour matches each docstring except the scad2step "no STEP file" claim (finding-3), the csa generator row and reproducibility claim (finding-6) and the check_commit_msg merge detection in a linked worktree (finding-10) |
| CK-CODE-E5 | Yes | Prerequisites in the documented order: scad2step checks usage, installation, OpenSCAD version, conversion, FreeCAD installation, bundle version, then C1 to C7; check_commit_msg checks subject, rows, then trailers |
| CK-CODE-E6 | Yes, with finding-3 | Read-back: scad2step C6 re-reads the STEP, and the driver checks the marker and the file (line 285); normalize_fab `--check` compares every name both ways; csa `--check` diffs the whole report |
| CK-CODE-E9 | No (Minor) | `CI_KINDS_FAIL` unused (finding-11); no other dead item found |
| CK-CODE-G1 | No (Minor) | Inputs validated at the boundary (argument sets, dates, review tokens, stored-list lines, zip readability, TPM data), except the `--write` destination of zip members (finding-11) |
| CK-CODE-H1, H2 | Yes | Testable through documented hooks and fixtures without the owner's files; the modules are the tool author's known-answer modules. 05 section 9.2 step 3 makes this review the independent check |
| CK-CODE-I4 | Yes | Comments state why (for example the `freecadcmd` exit status, the one-second time-stamp resolution, the STEP quote escape); no commented-out code |
| CK-CODE-J3 | Yes | Compound rules are atomic: CR_TRAILER_MISSING is satisfied only by a valid `CR:`, `Editorial:` or `merge(CR-NNN)` (line 194), and scad2step PASS needs both the marker and the file (line 285) |
| CK-CODE-J4 | Yes | Line counts and function spans measured (table above) |

Observations with no finding:
- scad2step: the time-out kills the process group of the `freecadcmd` it started, including any OpenSCAD child the workbench starts.
- normalize_fab: its rules equal the 05 section 8.2 table row for row. The PDF rule keeps lengths, so no offset table moves.
- render_tpm: the PNGs are written without the `Software` metadata key.
- check_commit_msg: git parses the trailers itself, so a `Refs:` line cut off by a blank line counts as missing (c13).

## Visual closure

Both committed renders were opened and inspected:
- `docs/cm/tool-validation/evidence/render-tpm-fixture-tpm-status.png` (SHA-256 `af7a8ac9...`, 1920 x 1080): seven legible rows. The chips are green, yellow, green, red, red, grey ("not due"), red, and each follows the status rule for its fixture case. The subtitle names `tools/tests/fixtures/render_tpm/tpm.json` and the as-of date 2026-10-06.
- `render-tpm-fixture-trend-own-yellow-after-status-note.png` (`bca50ca4...`, 1600 x 900): point 2 is red at `status-2026-09-30` and point 5 is yellow at PDR 2026-10-06. The dashed planned line at 7 lies inside the frame with its legend.

Nothing is cut off or overlapping.

## Reviewer re-runs (commands, exits)

| Command | Exit | Result |
|---|---|---|
| The six known-answer modules, `.venv/bin/python -m unittest discover -v -s tools/tests -p <module>`, 13:10 to 13:11 CDT (every product blob equal to `2bfe001`) | 0 each | 22, 24, 14, 12, 33, 13 run and passed, 0 skipped |
| `tools/scad2step.py --scad tools/tests/fixtures/openscad/smoke-shell.scad --step <scratch>/s1.step`, then `s2.step` | 0, 0 | KAT `faces=31 cylinders=16 bspline=0 volume=24721.221 stl_error_pct=0.0080 freecad=1.1.3`; normalized STEP equal |
| scad2step with a pre-existing `--step` file under the version hook, then under `CWHT_OPENSCAD=/nonexistent` | 4, 3 | the old STEP file remains (finding-3) |
| `tools/csa.py --rev 9fd0962 --since baseline/srr --date 2026-09-27 --output <scratch>/csa-9fd0962.md --json <scratch>/csa-9fd0962.json` | 0 | compared with `git show b790eaa:docs/process/configuration-status.md` (finding-7) |
| `tools/check_commit_msg.py --range baseline/srr..2bfe001` | 1 | 93 commits; 39 REFS_MISSING, 3 SUBJECT |
| Scratch repository with a linked worktree and `git merge --no-ff --no-commit` | 0 | `git rev-parse --git-path MERGE_HEAD` exists; `<worktree>/.git/MERGE_HEAD` does not (finding-10) |
| `cd /Users/robinonsay/rust/cwht && .venv/bin/python -m unittest discover -s tools/tests`, 13:20 CDT | 143 | stopped by the reviewer while `test_ltspice_batch.py` waited on the wrapper lock; no LTspice process started (header) |
| `.venv/bin/python -m unittest discover -s tools/tests -p <module>` for each of the 20 modules except `test_ltspice_batch.py`, at HEAD `d9c7f69` | 0 for 19; 1 for `test_validate_docs.py` | 544 tests; the one failure is `test_repository_exit_zero` (repository drift of other records) |
| `.venv/bin/python tools/validate_docs.py` (this record in place) | 1 | 88 passed, 8 failed; this record PASS (with a drift note for the lock, which `d9c7f69` changed on the LTspice rows only) |

## Cross items (not findings against TV-015 to TV-019; routed to the named owner)

| Id | Item | Owner |
|---|---|---|
| X-1 | This record is separate from INSP-038 (header comment). Two follow-ups: TV-015 to TV-019 section 8 and the README and lock section 5 "pending" cells name `tool-validation-tv-014-to-tv-019.md`, and the author's section 8 entry after this record is filed should name INSP-088 and this path; the INSP-038 section "TV-015 to TV-019" can point here at its next edit | Lead SE (plan WP-PDR-07 record list); TV author |
| X-2 | OA-TV019-1 (hook installation, 05 section 13 PDR row "installed as the `commit-msg` hook") is defined in TV-019 section 9 and the README only. It is not in the plan section 6.1 owner actions. It should be registered for the owner session after accreditation, with the finding-10 correction to its text | Lead SE |
| X-3 | 05 section 8.2 step 3 prints `freecadcmd tools/scad2step.py` as the STEP command, a form whose exit status is always 0. TV-015 and ACC-SCAD2STEP-001 make the driver `.venv/bin/python tools/scad2step.py` the accredited entry point. 05 is a baselined item (Log or Class II CR per 05) | CM plan owner (configuration manager) |
| X-4 | TV-016 finding 2: the kicad-cli ERC and DRC JSON reports carry a `date` member that the 05 section 8.2 normalization table lacks, although 05 puts every generated package file in `SHA256SUMS.normalized`. TV-016 says PCA-01 "excludes the two reports by name" until then. That is a procedure change that belongs in 05 (a table row for JSON reports), not in a TV record | CM plan owner (a CR on 05 section 8.2) |
| X-5 | TV-019 finding 1 and TV-018 finding 2: `86ff3b0` committed the five tools under another session's message with no `Refs:` (a 05 section 4.5 departure for the deviations log). 39 of the 93 commits of `baseline/srr..2bfe001` fail REFS_MISSING against a Table 6-1 threshold of 0; they are RID candidates for the PDR package | Lead SE (deviations log, PDR package) |
| X-6 | TV-018 finding 1: the level rule (an APPROVED record naming a file in `product_files` makes the row L1) reads inputs as products. A record field that separates inputs from products, or a 05 section 4.1 reading, is needed before levels can be accredited | Lead SE |
| X-7 | Software assurance pair: not required. 07 section 2.1.1 gives No for code of a "Neither" component without `unsafe`, and TV records have no row; section H is answered here as the template directs | Lead SE |

## Verdict

```
VERDICT: NEEDS CHANGES
PRODUCT: TV-015, TV-016, TV-017, TV-018, TV-019 at 2bfe001 (tools d0277ec8, f3eaac39, f37985d6, dd9b6fed, 5488dd98)
FINDINGS:
- [Major] finding-1 TV-B3/TV-C2/TV-F1 TV-015 purpose 2 and ACC-SCAD2STEP-001: the C4 and C6 refusals have no known answer or seeded fault.
- [Minor] finding-2 TV-A2 TV-015 and TV-016: lock section 7 records installer SHA-256 the records say is absent; bundle-to-installer confirmation not made.
- [Minor] finding-3 CK-CODE-E1 scad2step: a stale STEP survives exits 3 and 4 and an OpenSCAD failure.
- [Minor] finding-4 TV-B2 TV-015: the ADR-008 AP214 statement is not checked.
- [Minor] finding-5 TV-B3 TV-017: no seeded missing key.
- [Minor] finding-6 TV-B3 TV-018: reproducibility depends on refs; the generator row names the revision's blob.
- [Minor] finding-7 TV-C2 TV-018: the hand-CSA known answer covers items 2, 6 and the trailer metric only (the reviewer found the other derivable values equal).
- [Minor] finding-8 TV-E1 TV-018: limitation 3 wording; 05 section 6 item 4, 7, 8 parts not listed as not covered.
- [Minor] finding-9 TV-G1-1 TV-018: a repository-content test in a fixture class.
- [Minor] finding-10 TV-E1 TV-019: linked worktree merge detection, relative hook paths, amend.
- [Minor] finding-11 CK-CODE-E9/G1: unused constant; zip member path containment in normalize_fab --write.
ITEMS N/A: TV-C4 (TV-017 to TV-019, no 05 section 9.2 row), TV-D3 (class B records), TV-F5 (first records), TV-G2 (TV-017 to TV-019), TV-G3, TV-G4, TV-H1; Rust-specific code items listed above
RE-RUN: the six modules; exit 0 each; 22, 24, 14, 12, 33, 13 tests, 0 skipped; same as runs 1
MEASUREMENTS: size=5 records, 17 purposes, 118 tests, 32 fixture files, 1990 tool LOC; turns=85; minutes=55; major=1; minor=10; unsafe_sites=0
```

## Iteration 2: delta verification of finding-1 (Major) (2026-09-27, HEAD `1353bb3`)

**Scope (rule C1).** Iteration 2 is a delta that verifies the finding-1 fix only. The author left the Minor findings 2 to 11 untouched, and they are not re-reviewed. The fix takes the second route that finding-1 offered: seeded C4 and C6 cases run through a test double of the `FreeCAD`, `Part` and `importCSG` modules. The author did not narrow the purpose.

**Products.** The ten identities the fix changed or added, at the re-freeze commit `99feb43` on `main`. TV-015 run 2 tested `989d257`.
- `TV-015` blob `4669c5ec`.
- `tools/tests/test_scad2step.py` blob `bd38fe2b`.
- `known-answers.json` blob `05520747`.
- `fake/freecadcmd-api-double` blob `e6de6ad2` (mode 100755).
- `fake/freecad_api/FreeCAD.py` blob `ccdc3e1b`, `Part.py` blob `549f799f` and `importCSG.py` blob `e8d4a46d`.
- The run 2 log, blob `b9285807`.
- The TV README, blob `9400963d`.
- The lock, blob `6c7eba57`.

The tool `tools/scad2step.py` is unchanged: blob `d0277ec8` at `2bfe001`, `989d257`, `99feb43` and HEAD. The fixture tree is `35e89b48` (15 files). Its digest was recomputed from `git ls-files | sort | shasum -a 256`: `72b0ab2d...`, equal to the run 2 transcript. The SHA-256 of the test module and the tool were recomputed too: `78c7480b...` and `004c0b3f...`, equal. `git rev-parse 99feb43:<path>` equals `HEAD:<path>` for all 64 `product_files`. `git diff --stat 99feb43 HEAD` touches only `docs/plan/status/status-2026-09-27.md`. `git status --short` shows no change under `tools/` or `docs/cm/`. The lock diff `83bc0520..6c7eba57` changes 3 rows and adds 1 row, all TV-015: section 1.1 line 96, section 1.2 line 128, section 5 line 270 and a history row. The LTspice rows are as `d9c7f69` left them. The TV-016 to TV-019 products are unchanged since `2bfe001`. The checklists are the same as iteration 1: tool validation checklist revision A (blob `7be809d4`, CR-012 branch, not merged) and the code checklist revision B.

**Independence (rule C4).** This invocation authored no part of WP-PDR-07, of TV-015, of the tool, of the test double or of iteration 1 of this record. It edited no product file. **Search first.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search, with the query "INSP-088 tool validation TV-015 scad2step review record finding-1 C4 C6". `grep -n` then only pinned lines in the plan, `tools/validate_docs.py`, the tool and TV-015. **Headless.** The runs wrote only to the session scratchpad and to `mktemp` directories. Nothing was downloaded or installed. **LTspice:** not run. `test_ltspice_batch.py` was left out of every run.

### Verification of finding-1, case by case (rule C7)

The cases are the finding-1 locations, the two refusals purpose 2 claims (C4, and C6 with its three raise statements, one of which has two operands), the "exit 1 and no STEP left" rule, and the checks the fix needs to be a valid known answer: hand-derived expected values, no dependence on the fixture's own tool output, and a control case.

| # | Case | Reviewer check | Result |
|---|---|---|---|
| 1 | C4 is reached: a CompSolid of two solids is refused with exit 1 and `SCAD2STEP FAIL C4:` | Code path read: the CompSolid of the double passes C3 (`ShapeType` in `("Solid", "CompSolid")`, valid) and fails at line 138 (`len(shape.Solids) != 1`). A Compound of two solids would stop at C3, so a CompSolid is the only shape that reaches C4, and the double uses it. `test_c4_compsolid_of_two_solids` asserts exit 1, the marker `SCAD2STEP FAIL C4: STEP must hold exactly one solid, got 2` on stdout and its text on stderr, no STEP left, and no export logged | Yes |
| 2 | C6 "FreeCAD wrote no STEP file" (line 146) is reached | `c6-no-file`: the double's `Part.export` logs "not written" and writes nothing; the test expects the line 147 marker | Yes |
| 3 | C6 read-back check (line 149), both operands: `len(back.Solids) != 1` and `not back.isValid()` | `c6-two-solids` (2 solids, valid) exercises the first operand alone. `c6-invalid` (1 solid, not valid) exercises the second alone. The expected markers `holds 2 solid(s), valid True` and `holds 1 solid(s), valid False` are the line 150 format string filled in by hand | Yes |
| 4 | C6 volume check (line 152), with the tolerance on both sides | Shape 6000 mm^3, so the limit is 1e-6 x 6000 = 0.006 mm^3. The control reads back 6000.003 (0.003 inside the limit), and it passes. `c6-volume` reads back 6000.012 (0.012 outside), and it fails with `STEP volume 6000.012000 differs from the shape volume 6000.000000` (`:.6f`, hand-filled). The two cases bracket the limit, so the comparison direction and the scale are fixed | Yes |
| 5 | "No STEP left" after each refusal, with a STEP that existed | The double logs each export. `export_logged` is true for `c6-two-solids`, `c6-invalid` and `c6-volume`, so the file existed and was removed. For C4, a stale STEP placed at `--step` before the run is gone afterwards | Yes, see observation O-1 |
| 6 | The control case shows the double reaches PASS when no fault is seeded, so a refusal is not an artefact of the double | `test_control_case_passes`: exit 0, `SCAD2STEP PASS wrote <step>`, STEP present, and every KAT field equal to the hand values. The box mesh volume of 6000.000 over 12 facets is the product 30 x 20 x 10. C7 passes at 0 % error. `freecad=1.1.3` | Yes |
| 7 | The expected values are hand-derived, not taken from tool output | `known-answers.json` block `scad2step.api_double` holds the raise format strings filled in by hand. The reviewer filled in the format strings of lines 139, 147, 150 and 153 independently and got the same six markers | Yes |
| 8 | The checks run are the tool's own at blob `d0277ec8`, not a copy | The driver passes `os.path.abspath(__file__)` to the `freecadcmd` hook (line 275). The double runs `"$CWHT_FAKE_PYTHON" "$@"` with `PYTHONPATH` set to `fake/freecad_api/`, so `_in_freecad()` is true and `freecad_convert()` of the tool file runs. The stand-ins model shapes only. They contain no check logic | Yes |
| 9 | Reviewer mutation check (independent of the author's) | 14 mutants of scratch copies of the tool, each run with `-k ApiDoubleTests` against the committed module and fixture. Killed (at least one test fails): remove C4; move C4 after the export; remove the C6 no-file check; remove the whole read-back check; drop the solids operand; drop the `isValid()` operand; remove the volume check; compare the read-back with itself; tolerance 1e-5; tolerance 1e-7 (the control fails). 10 of 10 check-logic mutants were killed. The 3 single-layer no-STEP mutants survived, and their combination was killed (O-1) | Yes |
| 10 | TV-015 purpose 2 (finding-1 location, line 31) | It now names the three C6 sub-cases. It says C2, C3, C5 and C7 are validated with FreeCAD 1.1.3, and C4 and C6 against the double (limitation 2). The purpose is no wider than its known answer | Yes |
| 11 | TV-015 section 3 (finding-1 location, line 63) | Sentence replaced by the `ApiDoubleTests` table (six cases, stand-in shape and expected result for each) and the author mutation note. The markers in the table equal `known-answers.json`. Pass criteria: 28 tests. The per-class counts (6, 9, 5, 3, 1, 2, 1, 1) add to 28 and equal the run 2 transcript | Yes |
| 12 | TV-015 limitation 2 (finding-1 location, line 98) | It states what the double shows (the check logic, exit 1, no STEP) and what it does not show (that FreeCAD 1.1.3 can produce such a result, or that the stand-in reproduces FreeCAD's reporting). This is consistent with the code | Yes |
| 13 | ACC-SCAD2STEP-001 (finding-1 location, line 119) | The scope now bounds purpose 2: C2, C3, C5 and C7 validated with FreeCAD 1.1.3; C4 and C6 "as check logic against the FreeCAD API test double only (limitation 2)". The rest is unchanged | Yes |
| 14 | TV-015 run 2 result, tied to a commit (INSP-015 F-02) | Run 2 row: 13:48 CDT, `989d257`, 28 of 28, 0 skipped, part D normalized `f2b3afbf...` equal to run 1. The transcript agrees line for line: part A all "unchanged from HEAD", 0 untracked, versions 2021.01 and 1.1.3, `Ran 28 tests`, `RESULT normalized STEP identical` | Yes |
| 15 | Index rows (TV-F3) | README TV-015 row, lock section 1.2 row (blob `bd38fe2b`, 28 tests), section 5 row and the header all say Validated with run 2 at `989d257`. The section 1.1 row and the history row describe run 2 and limit C4 and C6 to check logic | Yes |
| 16 | Re-validation trigger covers the double | TV-015 section 7 first trigger: any change of `tools/tests/fixtures/openscad/`, which contains `fake/freecad_api/` | Yes |
| 17 | No em dashes added | 0 in the added lines of the ten changed files | Yes |

**Result: finding-1 Verified.** TV-B3, TV-C2 and TV-F1 are Yes for TV-015. The same holds for the INSP-015 F-01 class: the purpose and the scope are no wider than the known answers.

**Observation O-1 (no finding).** A refusal removes the STEP in two places: FreeCAD mode (`_fail`, and the stale-file removal at line 114) and the driver (line 292). The `ApiDoubleTests` fail only when both are removed. That is sufficient for the accredited entry point, the driver named in ACC-SCAD2STEP-001. For the `freecadcmd tools/scad2step.py` form that 05 section 8.2 step 3 prints, only the FreeCAD-mode layer applies, and no test isolates it. That form is outside the proposed scope, and cross item X-3 already routes the 05 wording.

**Code checklist on the added test code (CK-CODE, language-neutral items).** The double exits 0 like the real `freecadcmd` (lock section 1.4 finding 4). When `CWHT_FAKE_PYTHON` is unset it prints a line and gives no marker, which is the "no marker" path, exit 1. An unknown case raises. The stand-ins model only the attributes FreeCAD mode uses: Version, ParamGet, newDocument, addObject, Shape.ShapeType, Solids, Faces[].Surface, Volume, isValid, removeSplitter, Part.export, Part.read and importCSG.insert. `HOOKS` in the module now clears the three `CWHT_FAKE_*` variables. No finding.

### Readiness criteria (iteration 2)

| # | Answer | Evidence |
|---|---|---|
| R1 | Yes | 64 of 64 `product_files` equal at `99feb43` and HEAD; `git ls-tree -r 99feb43 tools/tests/fixtures/openscad` gives the 15 files, tree `35e89b48`; nothing uncommitted under the product paths |
| R2 | Yes | `.venv/bin/python -m unittest discover -v -s tools/tests -p test_scad2step.py`, 13:56 CDT at HEAD `1353bb3` (every TV-015 blob equal to `99feb43`): 28 run, 28 passed, 0 skipped, 32.2 s |
| R3 | No, not attributable to this product | 13:59 to 14:00 CDT: the 20 modules other than `test_ltspice_batch.py`, one by one: 550 tests, all pass except `test_validate_docs.RepositoryTests.test_repository_exit_zero`. `validate_docs.py`: 97 passed, 8 failed, and this record passes. The 8 failures are record drift of other records: the SRR ADR, TS and 02 records; INSP-015 on the TV README and lock (drift since before iteration 1; each TV status update moves those blobs); and the PDR `cm-plan-05-software-assurance`, `configuration-status` and `lessons-learned` records on CR-007. Read as INSP-040 and INSP-041 iteration 2 read it |
| R4 | Yes | Case 15 |
| R5 | Yes | The author summary lists the route, the added cases, the mutation check, run 2 with commit and counts, and the scope change |

### Per-record result (iteration 2)

| TV record | Commit tested | Reviewer re-run (command, exit, result) | Items answered No (TV-015) | Finding ids |
|---|---|---|---|---|
| TV-015 | `989d257` (run 2); re-frozen at `99feb43` | R2 row above: exit 0, 28 of 28, 0 skipped. Mutation check, case 9 | TV-A2, TV-B2, CK-CODE-E1 (Minor findings 2 to 4; TV-B3, TV-C2 and TV-F1 now Yes) | finding-1 Verified; finding-2 to finding-4 Open (liens) |

TV-016 to TV-019: unchanged products, not re-reviewed (rule C1).

### Findings (iteration 2; current state of every finding)

| Finding | Origin | Severity | Item | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|
| finding-1 | reviewer | Major | TV-B3, TV-C2, TV-F1 | Verified (iteration 2; route 2, seeded C4 and C6 through the FreeCAD API test double at `989d257`, TV-015 re-frozen at `99feb43`) | N/A | |
| finding-2 | reviewer | Minor | TV-A2 | Open (lien, plan rule C1) | Pending | CDR readiness declaration |
| finding-3 | reviewer | Minor | CK-CODE-E1, CK-CODE-E6 | Open (lien, plan rule C1) | Pending | CDR readiness declaration |
| finding-4 | reviewer | Minor | TV-B2 | Open (lien, plan rule C1) | Pending | CDR readiness declaration |
| finding-5 | reviewer | Minor | TV-B3, TV-C2 | Open (lien, plan rule C1) | Pending | CDR readiness declaration |
| finding-6 | reviewer | Minor | TV-B3, CK-CODE-E1 | Open (lien, plan rule C1) | Pending | CDR readiness declaration |
| finding-7 | reviewer | Minor | TV-C2, R5 | Open (lien, plan rule C1) | Pending | CDR readiness declaration |
| finding-8 | reviewer | Minor | TV-E1 | Open (lien, plan rule C1) | Pending | CDR readiness declaration |
| finding-9 | reviewer | Minor | TV-G1-1 | Open (lien, plan rule C1) | Pending | CDR readiness declaration |
| finding-10 | reviewer | Minor | TV-E1, CK-CODE-E1 | Open (lien, plan rule C1) | Pending | CDR readiness declaration |
| finding-11 | reviewer | Minor | CK-CODE-E9, CK-CODE-G1 | Open (lien, plan rule C1) | Pending | CDR readiness declaration |

No new finding.

### Cross items (iteration 2)

- X-1 still applies. TV-015 section 8, and the README and lock section 5 "pending" cells, name `tool-validation-tv-014-to-tv-019.md`. The TV author's section 8 entry should name INSP-088 and this path. After that, a reviewer re-issue at this iteration confirms that the diff is confined to sections 8 and 9, the status line and the status rows (TV template, "The reviewer edits no TV record"). From that edit until the re-issue, the record drift rule fails this APPROVED record.
- X-7 still applies: no software assurance pair. The added files are Python test code of a "Neither" component with no `unsafe`.

### Completion criteria (SWE-088), iteration 2

No Major finding is open, and readiness is met (R3 not attributable). Findings 2 to 11 are Minor liens due at the CDR readiness declaration (plan rule C1; PDR package section 15). `reviewer_verdict: APPROVED`, `assurance_verdict: not-required` and `verdict: APPROVED`. TV-015 to TV-019 can each move to Reviewed, with no open Major. Accreditation (ACC-SCAD2STEP-001, ACC-KICAD-001, ACC-NORMFAB-001, ACC-TPM-001, ACC-CSA-001, ACC-COMMITMSG-001) is the owner's decision (05 section 9.2 step 3).

```
ITERATION 2 (2026-09-27, HEAD 1353bb3, product commit 99feb43, run 2 at 989d257): VERDICT: APPROVED (reviewer APPROVED; assurance not required)
FINDINGS:
- [Major] finding-1: Verified (C4 and the three C6 raises, both read-back operands, reached through the FreeCAD API test double; control passes; 10 of 10 check-logic mutants killed; purpose 2, section 3, limitation 2 and ACC-SCAD2STEP-001 bounded to check logic).
- [Minor] finding-2 to finding-11: Open, not in the delta (liens due the CDR readiness declaration).
OBSERVATION: O-1 the no-STEP rule is covered only jointly by the FreeCAD-mode and driver layers (driver is the accredited entry point).
RE-RUN: test_scad2step.py exit 0, 28 of 28, 0 skipped; 20 modules 550 tests, 1 failure (repository drift, not this product); validate_docs 97 passed, 8 failed (other records), this record PASS
MEASUREMENTS: blobs equal HEAD 64/64; cases 17/17 Yes; mutants 14 (10 check-logic killed, 3 single-layer survived, 1 combined killed); major open=0; minor open=10; turns=34; minutes=40 (cumulative 119 and 95); iteration=2
```

## Iteration 2 re-issue 1: drift delta on the three index blobs (2026-09-27, HEAD `3d320a3`)

**Scope (rule C1).** A re-issue of iteration 2 on a delta, not a new review: the front matter keeps `iteration: 2` (precedents INSP-009, INSP-038 "iteration 3 re-issue 1", SRR `tool-validation-tv-001-to-tv-010.md`). No TV-015 to TV-019 record, tool, test module or fixture changed. `validate_docs.py` failed this APPROVED record on the record drift rule for three `product_files` entries, the shared indexes that TV-014 work also edits. The lens is this record's: does any hunk change a statement about TV-015 to TV-019, or a statement this record relied on? The TV-014 content of the hunks is INSP-038's to review and is not judged here.

**Independence (rule C4).** This invocation authored no part of WP-PDR-07, of TV-014 to TV-019, of the five tools, of the INSP-038 fix commits or of iterations 1 and 2 of this record, and it edited no product file. **Search first.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ("record drift delta iteration re-issue product_files blob changed APPROVED record rule C1 iteration limit") ran before any later manual search. One `grep -n "^#"` over this record's own path ran before the tool was loaded; it is recorded here as a deviation from the rule's order. **Headless.** Only `git` reads and `validate_docs.py` ran. No test module ran, because no executable product changed. LTspice was not run.

**Drift, commit by commit.** `git log 99feb43..HEAD` over the three paths lists exactly the commits the assignment named:

| Path | Iteration 2 blob | Commits | HEAD blob |
|---|---|---|---|
| `docs/cm/tool-validation/README.md` | `9400963d` | `f47360a`, `bd78bd5`, `1db319a` | `7c90f143` |
| `tools/toolchain.lock.md` | `6c7eba57` | `f47360a`, `bd78bd5`, `1db319a` | `e1c811b0` |
| `tools/README.md` | `053e6df2` | `d1148c2`, `45531ac` | `a5e9cab6` |

The assignment named `f4757da2` and `be96420b`: those are the README and lock blobs at `bd78bd5`. The owner accreditation commit `1db319a` changed both once more, so this re-issue reviews up to the HEAD blobs. `d1148c2` and `45531ac` do not touch the README or the lock. The commits after `1db319a` up to HEAD `3d320a3` touch no product path.

**Hunks read (every one; `git diff` and `git diff --word-diff=porcelain` blob to blob).**

| # | File, hunk | Change | Touches TV-015 to TV-019 or a statement this record relied on? |
|---|---|---|---|
| 1 | TV README line 38 (TV-014 row) | The wrapper blob and commit change from `64e1c723`/`c9d2c54` to `88b71475`/`45531ac`. The status changes from "Not yet validated" to Validated (runs 5 and 6) and Accredited (OD-24b, ACC-LTSPICE-001) | No. The TV-015 to TV-019 rows (lines 39 to 43) are byte-identical, at the same line numbers |
| 2 | Lock section 1, LTspice row | The TV cell adds runs 5 and 6 and "accredited 2026-09-27 ... for wrapper blob `88b71475`". The status becomes Accredited | No |
| 3 | Lock section 1, Wine layer row | "Not yet validated" becomes "Accredited (with LTspice, ACC-LTSPICE-001)" | No |
| 4 | Lock section 1.1, LTspice row | The "validation run is now ... released" text is replaced by the run 5 and run 6 records (HEADs, blobs, procedures, counts 43 and 46, parts D to G) | No |
| 5 | Lock section 1.2, `tools/ltspice-batch.sh` row | Blob history `d5d3876`, `bdc4513f`, `88b71475`. The integration switch `CWHT_LTSPICE_INTEGRATION=1`. Runs 5 and 6 passed | No. The five TV-015 to TV-019 rows of section 1.2, including the `scad2step.py` row (blob `bd38fe2b`, 28 tests) that case 15 relied on, are unchanged |
| 6 | Lock section 1.4, finding 15 | "Closed 2026-09-27" is appended (cause INSP-038 finding-20, fix `b893382`, session end `bdc4513f`) | No |
| 7 | Lock section 5, TV-014 row | Wrapper `88b71475`/`45531ac`, Validated with runs 5 and 6, and the accreditation cell | No. The TV-015 to TV-019 rows of section 5 are unchanged |
| 8 | Lock history | Two rows are added after the TV-015 run 2 row (TV-014 runs 5 and 6) | No. The TV-015 run 2 row (case 15) is unchanged |
| 9 | `tools/README.md` line 19 ("LTspice." paragraph) | The everyday suite uses the test doubles. Real LTspice runs only with `CWHT_LTSPICE_INTEGRATION=1`. The session end is `wineserver -k`, and session membership covers only Wine processes of the bundle (TV-014 finding 5, INSP-038 finding-21) | No. The "PDR tools of WP-PDR-07" paragraph (line 21: TV-015 to TV-019 usage, classes and the "developer evidence only" rule) is unchanged |

Mechanical cross-check: every line of each old blob and each new blob that names TV-015 to TV-019, one of the five tools, OpenSCAD or kicad-cli was extracted. The old set and the new set are equal for all three files: the README and `tools/README.md` also at the same line numbers, and the lock in content (its line numbers after the history insertion do not move those rows). The word-level diff of the lock has 0 added or removed tokens naming TV-015 to TV-019 or their tools. No em dash was added.

**Blobs (rule C2).** At HEAD `3d320a3`, `git rev-parse HEAD:<path>` equals the named blob for all 64 `product_files` entries (61 unchanged since `99feb43`, 3 updated above). The four fixture trees are unchanged: `35e89b48`, `03063f2a`, `9a6aff25` and `92fd0e50`. `git status --short` shows nothing under `tools/` or `docs/cm/tool-validation/`. The checklists are unchanged: tool validation revision A blob `7be809d4` on `cr/CR-012-pdr-checklist-templates`, and code checklist revision B.

**Items.** No item answer of iteration 1 or 2 changes. TV-F3 (the index rows agree with the records) is still Yes for TV-015 to TV-019: the README TV-015 to TV-019 rows, the lock section 1.2 and section 5 rows and the section 1.1 OpenSCAD and kicad-cli rows read as at iteration 2.

### Findings (iteration 2 re-issue 1; current state of every finding)

| Finding | Origin | Severity | Item | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|
| finding-1 | reviewer | Major | TV-B3, TV-C2, TV-F1 | Verified (iteration 2; unchanged by the drift) | N/A | |
| finding-2 | reviewer | Minor | TV-A2 | Open (lien, plan rule C1) | Pending | CDR readiness declaration |
| finding-3 | reviewer | Minor | CK-CODE-E1, CK-CODE-E6 | Open (lien, plan rule C1) | Pending | CDR readiness declaration |
| finding-4 | reviewer | Minor | TV-B2 | Open (lien, plan rule C1) | Pending | CDR readiness declaration |
| finding-5 | reviewer | Minor | TV-B3, TV-C2 | Open (lien, plan rule C1) | Pending | CDR readiness declaration |
| finding-6 | reviewer | Minor | TV-B3, CK-CODE-E1 | Open (lien, plan rule C1) | Pending | CDR readiness declaration |
| finding-7 | reviewer | Minor | TV-C2, R5 | Open (lien, plan rule C1) | Pending | CDR readiness declaration |
| finding-8 | reviewer | Minor | TV-E1 | Open (lien, plan rule C1) | Pending | CDR readiness declaration |
| finding-9 | reviewer | Minor | TV-G1-1 | Open (lien, plan rule C1) | Pending | CDR readiness declaration |
| finding-10 | reviewer | Minor | TV-E1, CK-CODE-E1 | Open (lien, plan rule C1) | Pending | CDR readiness declaration |
| finding-11 | reviewer | Minor | CK-CODE-E9, CK-CODE-G1 | Open (lien, plan rule C1) | Pending | CDR readiness declaration |

No new finding against TV-015 to TV-019.

### Cross items (re-issue 1; not findings against this record's products)

- X-1 still applies. The README TV-015 row and the lock section 5 TV-015 to TV-019 "pending" cells still name `tool-validation-tv-014-to-tv-019.md`, not INSP-088 at this path.
- X-8 (new, routed to the TV-014 author and INSP-038; outside this record's lens). (a) The lock section 5 TV-014 status cell says "pending: INSP-038 delta on finding-21 ..." and also "**Accredited** 2026-09-27". The pending and accredited states sit in one cell. (b) Commit `1db319a` moves the LTspice and Wine layer rows to Accredited, but the history table has no row for it. The two new history rows each end "Log change (tool not yet accredited ...)". (c) The section 1.2 blob `d5d3876` has 7 hex digits, where the other blobs in the row have 8. INSP-038 decides whether any of these is a finding.

### Completion criteria (SWE-088), re-issue 1

No Major finding is open, and readiness stands as at iteration 2 (R1 now holds at HEAD `3d320a3` for all 64 entries; R3 is still not attributable to this product). `reviewer_verdict: APPROVED`, `assurance_verdict: not-required`, `verdict: APPROVED`. Every reviewed blob is on `main`, so the lead SE convention on `cr/` branch blobs does not apply.

```
ITERATION 2 RE-ISSUE 1 (2026-09-27, HEAD 3d320a3, drift delta): VERDICT: APPROVED (reviewer APPROVED; assurance not required)
DELTA: TV README 9400963d -> 7c90f143 (f47360a, bd78bd5, 1db319a); lock 6c7eba57 -> e1c811b0 (same commits); tools/README.md 053e6df2 -> a5e9cab6 (d1148c2, 45531ac). The assigned f4757da2 and be96420b are the bd78bd5 blobs, superseded by 1db319a
HUNKS: 9 read (README 1, lock 7, tools/README 1); all TV-014/LTspice; TV-015 to TV-019 lines identical in all three files
FINDINGS: finding-1 Verified (unchanged); finding-2 to finding-11 Minor, Open (liens, CDR readiness declaration); no new finding
CROSS: X-1 still applies; X-8 new (TV-014 index wording, routed to INSP-038)
VALIDATE_DOCS: this record PASS (it failed on the drift rule before this re-issue); 101 passed, 8 failed (other records' drift and state), exit 1 not attributable to this record
MEASUREMENTS: blobs equal HEAD 64/64; fixture trees 4/4 unchanged; turns=16; minutes=15 (cumulative 135 and 110)
```
