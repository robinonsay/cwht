---
id: INSP-015
checklist: peer-review-checklist-code
checklist_revision: B
checklist_file: docs/reviews/SRR/checklists/tool-validation-tv-001-to-tv-010.md
product: docs/cm/tool-validation/ (TV-001 to TV-010, README.md, evidence/; TV-012 run 2 from the SRR close-out delta), tools/toolchain.lock.md, tools/traceability.py, tools/complexity_gate.py, tools/render_review_figures.py, tools/tests/
# product_commit: the review baseline of iteration 3 (HEAD adcfe0946d2f1b5cd8f41a8f91eb4219a7fb99a1, 2026-09-26).
# product_files: the committed blobs reviewed at iteration 3, each equal to git rev-parse HEAD:<path> at that commit
# (record drift rule, TV-003 purpose 6). product_files_iteration_1 and product_files_iteration_2 keep the working-tree
# blobs of iterations 1 and 2 (reviewed at HEAD 28e49e6 while the files were untracked or modified; finding-2).
# Re-issue 2026-09-26 (SRR package item R18, delta verification of 96af250 and 860e84e): product_commit is
# HEAD 99ecccbf0c4e61da3f5a0fca65d73d7172b63848; product_files are the HEAD blobs (four changed since adcfe09, plus the nine files of
# tools/tests/fixtures/record_state/); product_files_iteration_3 keeps the list reviewed at iteration 3.
# Re-issue 2 2026-09-26 (post-SRR-ruling delta, package item R16, delta verification of b2d3538 under SRR decision 114):
# product_commit is HEAD 7c7959f1e06ff0169e2b68b0499022250e4d15ff; product_files are the HEAD blobs (twelve changed since 99ecccb, plus the two
# new evidence files rust-tools-2026-09-26.*); product_files_reissue_1 keeps the list of the first re-issue (99ecccb).
# Re-issue 3 2026-09-26 (SRR close-out delta, verification of 37ae576, c774851, bf654e6, 5792350, eb52766, e34a27b and fb22b7a):
# product_commit is HEAD c4b21f8eb1bfd6418c30cee00a87485d70faf4cd; product_files are the HEAD blobs (five changed since 7c7959f, plus TV-012, its tool,
# test module and five fixture files, the picotool known-answer file and the close-out install log); product_files_reissue_2 keeps the list of re-issue 2 (7c7959f).
product_commit: "c4b21f8eb1bfd6418c30cee00a87485d70faf4cd"
product_files: ["docs/cm/tool-validation/README.md@22f7b2bf6a4e2881c7a70c3fcef9f7300a122042", "docs/cm/tool-validation/TV-001-python-jsonschema.md@110a2692ae632ab8d39883455ae9b95182bf2076", "docs/cm/tool-validation/TV-002-traceability.md@bc8abd4306df681e7a1a4f9bf95b7fbdcd53cc53", "docs/cm/tool-validation/TV-003-validate-docs.md@2ea60dc1912bedd0b9849bbe2d5bd505d53ee6ee", "docs/cm/tool-validation/TV-004-render-rmm.md@e76395d5699fc24e373a4154c565126e2a731ef2", "docs/cm/tool-validation/TV-005-render-compliance.md@e8d167dda9f10956a0d1d087201d9ae37a048a9e", "docs/cm/tool-validation/TV-006-render-risk.md@dcce89f00d82551df4cb2a42d5575c6602fb04e1", "docs/cm/tool-validation/TV-007-review-trend.md@3936ab2f6f4be2f8b3645c9f5d32d164ba46b059", "docs/cm/tool-validation/TV-008-render-deck-chromium.md@ab8f2c2a83812d09174083c0b278dfdf4fb09dff", "docs/cm/tool-validation/TV-009-git.md@e3909e453c41a673878ae204fda11560a803abe2", "docs/cm/tool-validation/TV-010-render-review-figures.md@ab0404a25d8760f0e8c811905c530f2e9bfc7dd4", "docs/cm/tool-validation/evidence/python-tools-2026-09-26-r5.py@3be96e440e9d84cbe5771231f9a6c659828304ba", "docs/cm/tool-validation/evidence/python-tools-2026-09-26-r5-head.log.txt@57005ef0fb6aaa413546f874ae123937255987ff", "docs/cm/tool-validation/evidence/python-tools-2026-09-26-r5-worktree.log.txt@09b923952b2a00b861c2fff88b20d0d85cc7fb70", "docs/cm/tool-validation/evidence/python-jsonschema-2026-09-26-r5.sh@7edd2c8fbfd0aaf0ad01c4157eab72a153486c73", "docs/cm/tool-validation/evidence/python-jsonschema-2026-09-26-r5.log.txt@b4a4629ba12262671c4e971c8610529b3ea85ac4", "tools/toolchain.lock.md@8ab0218a195f05685cc60a3d35af23f7f1f6e24f", "tools/traceability.py@12de354531f27afd59e9a18798516d218821d6c0", "tools/validate_docs.py@3aa0368147b9af3e6e1546f808afb7aedf7f2226", "tools/render_review_figures.py@6f3018fdffe25107247f5ef9d010c5cc7d1aaf3e", "tools/tests/test_git_known_answer.py@cd8389823bdc34889edc7fc680f1bd8ae4c928a9", "tools/tests/test_render_compliance.py@c40a7f1f514d3784efcbef300d301391d9de84c0", "tools/tests/test_render_deck.py@ff58fb7b7f1017ab165ad532bac36898f4ed0835", "tools/tests/test_render_review_figures.py@cb54d28b00b8c854056b341ece157c00778476cb", "tools/tests/test_render_risk.py@05d695a4dd8c7d0510fd9a2c078584d6e3316b21", "tools/tests/test_render_rmm.py@0454936bf20498078de9ae2861af727c3a66350e", "tools/tests/test_review_trend.py@1f3ab0067b9ce33ebedefaf2a460664d2a978bdb", "tools/tests/test_tools.py@ed003bad762332310f0bc4d63346ac875f0e0554", "tools/tests/test_traceability.py@072bbdcd1ccbd224ee11d3fb4e1d097bcd0d978c", "tools/tests/test_traceability_srr_rules.py@86606485debd4569954847c5a48e7dd62bbcbcab", "tools/tests/test_validate_docs.py@c70d2c932a3b0965a2adb7827d8cfb5c4e005025", "tools/tests/fixtures/schema/keywords.schema.json@42c0822f6c98928ec2b33c14a7f991b6897dfc95", "tools/tests/fixtures/schema/keywords-invalid.json@272b585e327161ad7988896b54871d1e3093460d", "tools/tests/fixtures/schema/known-answers.json@86051ad7ba51c46cb8765b1271ea5d5646d78d1c", "tools/tests/fixtures/record_state/README.md@ffacc1d2015bff0bffc8ec0fcef63f866c994900", "tools/tests/fixtures/record_state/docs/reviews/SRR/checklists/approved-historical-lines.md@253ace9735a5490a6bc8c616bbe020501d3f04e5", "tools/tests/fixtures/record_state/docs/reviews/SRR/checklists/approved-latest-open-major.md@ba66170b32cf44a790170775ffe75709718a2d02", "tools/tests/fixtures/record_state/docs/reviews/SRR/checklists/approved-open-count-unshown.md@5affb78258960023363df98a10641c13d83f55bc", "tools/tests/fixtures/record_state/docs/reviews/SRR/checklists/approved-open-minor.md@81713d8bf0108d0cfa25e52bfca1918018a2e103", "tools/tests/fixtures/record_state/docs/reviews/SRR/checklists/approved-reviewer-needs-changes.md@b5ba22cc83252be6262ec5b148b7f29749f9bfa4", "tools/tests/fixtures/record_state/docs/reviews/SRR/checklists/approved-superseded-row.md@3221d65e9f62587477712a7b1e3436ffaf162d47", "tools/tests/fixtures/record_state/docs/reviews/SRR/checklists/needs-changes-open-major.md@5d9794c9e3c2d49e060a296c5acc2581c0c04b0a", "tools/tests/fixtures/record_state/docs/templates/peer-review-checklist-requirements.md@7d4c8f3d8d2f927f40ab40dcb3eff13ca546221e", "docs/cm/tool-validation/evidence/rust-tools-2026-09-26.sh@0560ff69af6363271e4fa3aa6636fc0d044fe17e", "docs/cm/tool-validation/evidence/rust-tools-2026-09-26.log.txt@ff74f01eb84cdb67e9c61af714ebe7b187b34891", "docs/cm/tool-validation/TV-012-complexity-gate.md@e4e042cc1165092a5a81a55840f6349defca0f64", "tools/complexity_gate.py@9cdc91959b06ca3f39142b0afcf85b9a64f719b1", "tools/tests/test_complexity_gate.py@1b6039418d5bc72393319a2b1856404e1248af66", "tools/tests/fixtures/complexity_gate/src/app.rs@df859b26d1ab2a1ea38265dc79bd351f6686b658", "tools/tests/fixtures/complexity_gate/src/core.rs@d07c8ecfab8328bd5e3f186513cbe10d32c44b56", "tools/tests/fixtures/complexity_gate/rca.json@36f84b8bc610263235eaf7ee44ff7f7e18597f66", "tools/tests/fixtures/complexity_gate/waivers.json@5bd29451e959edefdd2b11ee3b61cc39070a9578", "tools/tests/fixtures/complexity_gate/docs/reviews/CDR/decision-memo.md@b41a875f07f8a96d174876f0014c1ccd08bc1128", "tools/tests/fixtures/picotool/known-answers.json@bfaf5a1aadb8b418c00cbf44922bdda66914bc7e", "docs/cm/tool-validation/evidence/closeout-installs-2026-09-26.log.txt@c9f6b197ffdfb0ea1ad95a0f62395b99225f2190"]
product_files_reissue_2: ["docs/cm/tool-validation/README.md@22f7b2bf6a4e2881c7a70c3fcef9f7300a122042", "docs/cm/tool-validation/TV-001-python-jsonschema.md@3bcbd80fc15f24fdf75f3cf006b2a6fbf20f0270", "docs/cm/tool-validation/TV-002-traceability.md@7f66d0e6e7ffd08d332ad4b15c9d99f73096bd45", "docs/cm/tool-validation/TV-003-validate-docs.md@2ea60dc1912bedd0b9849bbe2d5bd505d53ee6ee", "docs/cm/tool-validation/TV-004-render-rmm.md@e76395d5699fc24e373a4154c565126e2a731ef2", "docs/cm/tool-validation/TV-005-render-compliance.md@e8d167dda9f10956a0d1d087201d9ae37a048a9e", "docs/cm/tool-validation/TV-006-render-risk.md@dcce89f00d82551df4cb2a42d5575c6602fb04e1", "docs/cm/tool-validation/TV-007-review-trend.md@3936ab2f6f4be2f8b3645c9f5d32d164ba46b059", "docs/cm/tool-validation/TV-008-render-deck-chromium.md@ab8f2c2a83812d09174083c0b278dfdf4fb09dff", "docs/cm/tool-validation/TV-009-git.md@e3909e453c41a673878ae204fda11560a803abe2", "docs/cm/tool-validation/TV-010-render-review-figures.md@ab0404a25d8760f0e8c811905c530f2e9bfc7dd4", "docs/cm/tool-validation/evidence/python-tools-2026-09-26-r5.py@3be96e440e9d84cbe5771231f9a6c659828304ba", "docs/cm/tool-validation/evidence/python-tools-2026-09-26-r5-head.log.txt@57005ef0fb6aaa413546f874ae123937255987ff", "docs/cm/tool-validation/evidence/python-tools-2026-09-26-r5-worktree.log.txt@09b923952b2a00b861c2fff88b20d0d85cc7fb70", "docs/cm/tool-validation/evidence/python-jsonschema-2026-09-26-r5.sh@7edd2c8fbfd0aaf0ad01c4157eab72a153486c73", "docs/cm/tool-validation/evidence/python-jsonschema-2026-09-26-r5.log.txt@b4a4629ba12262671c4e971c8610529b3ea85ac4", "tools/toolchain.lock.md@5c04ea9e04a0d59a563708ca51e3dacdb7384661", "tools/traceability.py@0a867523f78c224afdaa938735911b5df8f2920c", "tools/validate_docs.py@3aa0368147b9af3e6e1546f808afb7aedf7f2226", "tools/render_review_figures.py@6f3018fdffe25107247f5ef9d010c5cc7d1aaf3e", "tools/tests/test_git_known_answer.py@cd8389823bdc34889edc7fc680f1bd8ae4c928a9", "tools/tests/test_render_compliance.py@c40a7f1f514d3784efcbef300d301391d9de84c0", "tools/tests/test_render_deck.py@ff58fb7b7f1017ab165ad532bac36898f4ed0835", "tools/tests/test_render_review_figures.py@cb54d28b00b8c854056b341ece157c00778476cb", "tools/tests/test_render_risk.py@05d695a4dd8c7d0510fd9a2c078584d6e3316b21", "tools/tests/test_render_rmm.py@0454936bf20498078de9ae2861af727c3a66350e", "tools/tests/test_review_trend.py@1f3ab0067b9ce33ebedefaf2a460664d2a978bdb", "tools/tests/test_tools.py@ed003bad762332310f0bc4d63346ac875f0e0554", "tools/tests/test_traceability.py@d76b06976ba62d374d8c30a8eb08a4cb57d394e7", "tools/tests/test_traceability_srr_rules.py@86606485debd4569954847c5a48e7dd62bbcbcab", "tools/tests/test_validate_docs.py@c70d2c932a3b0965a2adb7827d8cfb5c4e005025", "tools/tests/fixtures/schema/keywords.schema.json@42c0822f6c98928ec2b33c14a7f991b6897dfc95", "tools/tests/fixtures/schema/keywords-invalid.json@272b585e327161ad7988896b54871d1e3093460d", "tools/tests/fixtures/schema/known-answers.json@86051ad7ba51c46cb8765b1271ea5d5646d78d1c", "tools/tests/fixtures/record_state/README.md@ffacc1d2015bff0bffc8ec0fcef63f866c994900", "tools/tests/fixtures/record_state/docs/reviews/SRR/checklists/approved-historical-lines.md@253ace9735a5490a6bc8c616bbe020501d3f04e5", "tools/tests/fixtures/record_state/docs/reviews/SRR/checklists/approved-latest-open-major.md@ba66170b32cf44a790170775ffe75709718a2d02", "tools/tests/fixtures/record_state/docs/reviews/SRR/checklists/approved-open-count-unshown.md@5affb78258960023363df98a10641c13d83f55bc", "tools/tests/fixtures/record_state/docs/reviews/SRR/checklists/approved-open-minor.md@81713d8bf0108d0cfa25e52bfca1918018a2e103", "tools/tests/fixtures/record_state/docs/reviews/SRR/checklists/approved-reviewer-needs-changes.md@b5ba22cc83252be6262ec5b148b7f29749f9bfa4", "tools/tests/fixtures/record_state/docs/reviews/SRR/checklists/approved-superseded-row.md@3221d65e9f62587477712a7b1e3436ffaf162d47", "tools/tests/fixtures/record_state/docs/reviews/SRR/checklists/needs-changes-open-major.md@5d9794c9e3c2d49e060a296c5acc2581c0c04b0a", "tools/tests/fixtures/record_state/docs/templates/peer-review-checklist-requirements.md@7d4c8f3d8d2f927f40ab40dcb3eff13ca546221e", "docs/cm/tool-validation/evidence/rust-tools-2026-09-26.sh@0560ff69af6363271e4fa3aa6636fc0d044fe17e", "docs/cm/tool-validation/evidence/rust-tools-2026-09-26.log.txt@ff74f01eb84cdb67e9c61af714ebe7b187b34891"]
product_files_reissue_1: ["docs/cm/tool-validation/README.md@b8e63c4ef5c0baff324e2fc032dddcb7b1111228", "docs/cm/tool-validation/TV-001-python-jsonschema.md@037888d6aec24ff35193d53d6d9aa5930cf3240c", "docs/cm/tool-validation/TV-002-traceability.md@c95e3488e854adb5c9176bfa956bbc9d0e231ccd", "docs/cm/tool-validation/TV-003-validate-docs.md@c6a218c5207b1184825089c9316cc583758ffe08", "docs/cm/tool-validation/TV-004-render-rmm.md@901540e3f17c2519413009883bf796e76ca59754", "docs/cm/tool-validation/TV-005-render-compliance.md@da891666f51fd71d3549b61dac4930c48fbf0874", "docs/cm/tool-validation/TV-006-render-risk.md@b39ddbf1b96d7a650e68629ee68fbf9237b720b4", "docs/cm/tool-validation/TV-007-review-trend.md@39d2e80029cfe8693c3a6af97c22fc6da278e496", "docs/cm/tool-validation/TV-008-render-deck-chromium.md@b4124dd555c23176a2ede67ac836543741c00491", "docs/cm/tool-validation/TV-009-git.md@1d89fd2723ae135c1a2c3c64a44478b30b8e49e8", "docs/cm/tool-validation/TV-010-render-review-figures.md@d6999b28f9484dffefdcbb89767478cb305501fb", "docs/cm/tool-validation/evidence/python-tools-2026-09-26-r5.py@3be96e440e9d84cbe5771231f9a6c659828304ba", "docs/cm/tool-validation/evidence/python-tools-2026-09-26-r5-head.log.txt@57005ef0fb6aaa413546f874ae123937255987ff", "docs/cm/tool-validation/evidence/python-tools-2026-09-26-r5-worktree.log.txt@09b923952b2a00b861c2fff88b20d0d85cc7fb70", "docs/cm/tool-validation/evidence/python-jsonschema-2026-09-26-r5.sh@7edd2c8fbfd0aaf0ad01c4157eab72a153486c73", "docs/cm/tool-validation/evidence/python-jsonschema-2026-09-26-r5.log.txt@b4a4629ba12262671c4e971c8610529b3ea85ac4", "tools/toolchain.lock.md@0ad60317be7e509c1e1968d2d9f4813f3904253f", "tools/traceability.py@0a867523f78c224afdaa938735911b5df8f2920c", "tools/validate_docs.py@3aa0368147b9af3e6e1546f808afb7aedf7f2226", "tools/render_review_figures.py@6f3018fdffe25107247f5ef9d010c5cc7d1aaf3e", "tools/tests/test_git_known_answer.py@cd8389823bdc34889edc7fc680f1bd8ae4c928a9", "tools/tests/test_render_compliance.py@c40a7f1f514d3784efcbef300d301391d9de84c0", "tools/tests/test_render_deck.py@ff58fb7b7f1017ab165ad532bac36898f4ed0835", "tools/tests/test_render_review_figures.py@cb54d28b00b8c854056b341ece157c00778476cb", "tools/tests/test_render_risk.py@05d695a4dd8c7d0510fd9a2c078584d6e3316b21", "tools/tests/test_render_rmm.py@0454936bf20498078de9ae2861af727c3a66350e", "tools/tests/test_review_trend.py@1f3ab0067b9ce33ebedefaf2a460664d2a978bdb", "tools/tests/test_tools.py@ed003bad762332310f0bc4d63346ac875f0e0554", "tools/tests/test_traceability.py@d76b06976ba62d374d8c30a8eb08a4cb57d394e7", "tools/tests/test_traceability_srr_rules.py@86606485debd4569954847c5a48e7dd62bbcbcab", "tools/tests/test_validate_docs.py@c70d2c932a3b0965a2adb7827d8cfb5c4e005025", "tools/tests/fixtures/schema/keywords.schema.json@42c0822f6c98928ec2b33c14a7f991b6897dfc95", "tools/tests/fixtures/schema/keywords-invalid.json@272b585e327161ad7988896b54871d1e3093460d", "tools/tests/fixtures/schema/known-answers.json@86051ad7ba51c46cb8765b1271ea5d5646d78d1c", "tools/tests/fixtures/record_state/README.md@ffacc1d2015bff0bffc8ec0fcef63f866c994900", "tools/tests/fixtures/record_state/docs/reviews/SRR/checklists/approved-historical-lines.md@253ace9735a5490a6bc8c616bbe020501d3f04e5", "tools/tests/fixtures/record_state/docs/reviews/SRR/checklists/approved-latest-open-major.md@ba66170b32cf44a790170775ffe75709718a2d02", "tools/tests/fixtures/record_state/docs/reviews/SRR/checklists/approved-open-count-unshown.md@5affb78258960023363df98a10641c13d83f55bc", "tools/tests/fixtures/record_state/docs/reviews/SRR/checklists/approved-open-minor.md@81713d8bf0108d0cfa25e52bfca1918018a2e103", "tools/tests/fixtures/record_state/docs/reviews/SRR/checklists/approved-reviewer-needs-changes.md@b5ba22cc83252be6262ec5b148b7f29749f9bfa4", "tools/tests/fixtures/record_state/docs/reviews/SRR/checklists/approved-superseded-row.md@3221d65e9f62587477712a7b1e3436ffaf162d47", "tools/tests/fixtures/record_state/docs/reviews/SRR/checklists/needs-changes-open-major.md@5d9794c9e3c2d49e060a296c5acc2581c0c04b0a", "tools/tests/fixtures/record_state/docs/templates/peer-review-checklist-requirements.md@7d4c8f3d8d2f927f40ab40dcb3eff13ca546221e"]
product_files_iteration_3: ["docs/cm/tool-validation/README.md@b8e63c4ef5c0baff324e2fc032dddcb7b1111228", "docs/cm/tool-validation/TV-001-python-jsonschema.md@037888d6aec24ff35193d53d6d9aa5930cf3240c", "docs/cm/tool-validation/TV-002-traceability.md@c95e3488e854adb5c9176bfa956bbc9d0e231ccd", "docs/cm/tool-validation/TV-003-validate-docs.md@ede04566cce5bebda43a2562f4c7752f2907d552", "docs/cm/tool-validation/TV-004-render-rmm.md@901540e3f17c2519413009883bf796e76ca59754", "docs/cm/tool-validation/TV-005-render-compliance.md@da891666f51fd71d3549b61dac4930c48fbf0874", "docs/cm/tool-validation/TV-006-render-risk.md@b39ddbf1b96d7a650e68629ee68fbf9237b720b4", "docs/cm/tool-validation/TV-007-review-trend.md@39d2e80029cfe8693c3a6af97c22fc6da278e496", "docs/cm/tool-validation/TV-008-render-deck-chromium.md@b4124dd555c23176a2ede67ac836543741c00491", "docs/cm/tool-validation/TV-009-git.md@1d89fd2723ae135c1a2c3c64a44478b30b8e49e8", "docs/cm/tool-validation/TV-010-render-review-figures.md@d6999b28f9484dffefdcbb89767478cb305501fb", "docs/cm/tool-validation/evidence/python-tools-2026-09-26-r5.py@3be96e440e9d84cbe5771231f9a6c659828304ba", "docs/cm/tool-validation/evidence/python-tools-2026-09-26-r5-head.log.txt@57005ef0fb6aaa413546f874ae123937255987ff", "docs/cm/tool-validation/evidence/python-tools-2026-09-26-r5-worktree.log.txt@09b923952b2a00b861c2fff88b20d0d85cc7fb70", "docs/cm/tool-validation/evidence/python-jsonschema-2026-09-26-r5.sh@7edd2c8fbfd0aaf0ad01c4157eab72a153486c73", "docs/cm/tool-validation/evidence/python-jsonschema-2026-09-26-r5.log.txt@b4a4629ba12262671c4e971c8610529b3ea85ac4", "tools/toolchain.lock.md@2687fb04594ed4489ac43bdb4522f59faab6db51", "tools/traceability.py@0a867523f78c224afdaa938735911b5df8f2920c", "tools/validate_docs.py@33ab5a83fc2063071e1afece416b180518d9da12", "tools/render_review_figures.py@6f3018fdffe25107247f5ef9d010c5cc7d1aaf3e", "tools/tests/test_git_known_answer.py@cd8389823bdc34889edc7fc680f1bd8ae4c928a9", "tools/tests/test_render_compliance.py@c40a7f1f514d3784efcbef300d301391d9de84c0", "tools/tests/test_render_deck.py@ff58fb7b7f1017ab165ad532bac36898f4ed0835", "tools/tests/test_render_review_figures.py@cb54d28b00b8c854056b341ece157c00778476cb", "tools/tests/test_render_risk.py@05d695a4dd8c7d0510fd9a2c078584d6e3316b21", "tools/tests/test_render_rmm.py@0454936bf20498078de9ae2861af727c3a66350e", "tools/tests/test_review_trend.py@1f3ab0067b9ce33ebedefaf2a460664d2a978bdb", "tools/tests/test_tools.py@ed003bad762332310f0bc4d63346ac875f0e0554", "tools/tests/test_traceability.py@d76b06976ba62d374d8c30a8eb08a4cb57d394e7", "tools/tests/test_traceability_srr_rules.py@86606485debd4569954847c5a48e7dd62bbcbcab", "tools/tests/test_validate_docs.py@4fb5bcc756b910876340e2f254359d3d9fcf80ef", "tools/tests/fixtures/schema/keywords.schema.json@42c0822f6c98928ec2b33c14a7f991b6897dfc95", "tools/tests/fixtures/schema/keywords-invalid.json@272b585e327161ad7988896b54871d1e3093460d", "tools/tests/fixtures/schema/known-answers.json@86051ad7ba51c46cb8765b1271ea5d5646d78d1c"]
product_files_iteration_1: ["docs/cm/tool-validation/README.md@11001b41386ff134f892b4f7b7595e657d3a8971", "docs/cm/tool-validation/TV-001-python-jsonschema.md@ee60bb9398945d240ec62bebea3a4f1e922ec27b", "docs/cm/tool-validation/TV-002-traceability.md@f53fa153199de5e3e599b3a9b96fe47cabbfc095", "docs/cm/tool-validation/TV-003-validate-docs.md@e787b4b19a90f82bdbe2f15e62dae673807d138a", "docs/cm/tool-validation/TV-004-render-rmm.md@7693fd7c81d43ffbd910e2a536084a3bea6cb2ff", "docs/cm/tool-validation/TV-005-render-compliance.md@2d340044f039fb71b5ba4cca3e0821bd1a611edb", "docs/cm/tool-validation/TV-006-render-risk.md@0f065de27cc1578f06c90bc6c44ddc682984a081", "docs/cm/tool-validation/TV-007-review-trend.md@a716f8da3a68190179feb8229c0f513fefb98482", "docs/cm/tool-validation/TV-008-render-deck-chromium.md@df046f215ee0c824f8788308f1c8810157cfb27f", "docs/cm/tool-validation/TV-009-git.md@8089ba35cc371204cb8d43e550ed8bb507186e2c", "docs/cm/tool-validation/TV-010-render-review-figures.md@7273106b5f7838fce6cc1149372d2a54edb05517", "tools/toolchain.lock.md@8b2324584c79bf70be10f2ea8cd3639828072507", "tools/traceability.py@0a867523f78c224afdaa938735911b5df8f2920c", "tools/render_review_figures.py@979beb139d13df8a64e295b2c6aac0d71a83c0e0", "tools/tests/test_git_known_answer.py@cd8389823bdc34889edc7fc680f1bd8ae4c928a9", "tools/tests/test_render_compliance.py@c40a7f1f514d3784efcbef300d301391d9de84c0", "tools/tests/test_render_deck.py@539e9593f8115045f85407cae95536632a53af52", "tools/tests/test_render_review_figures.py@ff5d81facd2d95718be681270238c6c980f2494c", "tools/tests/test_render_risk.py@05d695a4dd8c7d0510fd9a2c078584d6e3316b21", "tools/tests/test_render_rmm.py@0454936bf20498078de9ae2861af727c3a66350e", "tools/tests/test_review_trend.py@1f3ab0067b9ce33ebedefaf2a460664d2a978bdb", "tools/tests/test_tools.py@af6ed8b7d3b34338d52fef0eba76bc84d27cadb1", "tools/tests/test_traceability.py@d76b06976ba62d374d8c30a8eb08a4cb57d394e7", "tools/tests/test_traceability_srr_rules.py@86606485debd4569954847c5a48e7dd62bbcbcab", "tools/tests/test_validate_docs.py@3b10718d465cf3f796a9e5bcdc55c989c97517c4"]
product_files_iteration_2: ["docs/cm/tool-validation/README.md@5d69da3aecd684d4be9424810f2df5a19a90b68a", "docs/cm/tool-validation/TV-001-python-jsonschema.md@646e2cac45dfa7fd4bbb24794611b9eee4fa738f", "docs/cm/tool-validation/TV-002-traceability.md@ac9e27a62c134b6d46d4d31ae600b86f7a576dc6", "docs/cm/tool-validation/TV-003-validate-docs.md@e9575b7e7a9a09140bade49682945c95f456dac3", "docs/cm/tool-validation/TV-008-render-deck-chromium.md@1aa3099c1df6898077cf7b2e5ad4057ce31d710d", "docs/cm/tool-validation/TV-010-render-review-figures.md@8a7e322be16359767cc85fd6abfccf368863990c", "tools/toolchain.lock.md@f5f810a286a7e1e79d2e58f7409d383386d76e35", "tools/tests/fixtures/schema/keywords.schema.json@42c0822f6c98928ec2b33c14a7f991b6897dfc95", "tools/tests/fixtures/schema/keywords-invalid.json@272b585e327161ad7988896b54871d1e3093460d", "tools/tests/fixtures/schema/known-answers.json@86051ad7ba51c46cb8765b1271ea5d5646d78d1c", "tools/tests/test_validate_docs.py@8944a389618686b58c557f60872238321c5a3106", "tools/tests/test_render_deck.py@ff58fb7b7f1017ab165ad532bac36898f4ed0835", "docs/cm/tool-validation/evidence/python-jsonschema-2026-09-26.sh@458621f37562114fa5f5c96dd3b7697280cd2c99", "docs/cm/tool-validation/evidence/python-jsonschema-2026-09-26.log.txt@4a8faec188f30aa1d0fe476796aab4ded2cf0d3b", "docs/cm/tool-validation/evidence/python-tools-2026-09-26.log.txt@9906d1c8840643cd2371f2e591229b6a4dfce52e"]
product_size: 10 TV records and index (953 lines), 32 evidence files, toolchain lock (273 lines), traceability.py (2786 lines; 239-line working-tree delta reviewed), render_review_figures.py (1176 lines), 11 test modules (3844 lines)
sprint: SRR-prep
author_agent: "author:tool-validation (Claude invocation 2026-09-25, SRR package section 2 item H12)"
reviewer_agent: "reviewer:tools"
criticality: neither
assurance_required: false
assurance_reviewer_agent: none
iteration: 3
readiness_met: true
reviewer_verdict: APPROVED
assurance_verdict: not-required
verdict: APPROVED
findings_major: 2
findings_minor: 11
findings_open: 0
findings_fixed: 6
findings_verified: 6
findings_lien: 7
findings_deferred: 0
assurance_findings_major: 0
assurance_findings_minor: 0
assurance_tasks_applied: [swe-136 7.1 task 1]
unsafe_sites_reviewed: 0
deferred_rids: []
items_no: [TV-S9]
effort_turns: 182
effort_minutes: 265
record_status: Open
date: 2026-09-26
date_closed: null
---

# Peer review record INSP-015: tool validation records TV-001 to TV-010 and the toolchain proof

**Checklist:** `docs/templates/peer-review-checklist-code.md` revision B, applied to the Python tool source as `docs/process/03-software-classification-and-rmm.md` (tool rows, "Peer review") directs, plus the tool validation criteria of `docs/process/05-configuration-and-data-management.md` section 9.2 steps 1 to 4 and the SRR row of section 13, which this record lists as items TV-S1 to TV-S10. The code checklist is written for Rust firmware; its Rust-specific items are answered N/A with the reason. **Gate:** SRR (package section 2 item H12; entrance row 20 "Technology readiness and heritage assessment, including toolchain proof", 01 section 4.5 row 20, evidence "toolchain sanity-check results"). **Answer legend:** Yes = Pass, No = Fail, N/A = not applicable, each with evidence.

**Re-issue 3 of iteration 3, SRR close-out delta (2026-09-26, HEAD `c4b21f8`): verdict APPROVED (with liens).** Delta verification of the seven commits that touched the product since `7c7959f` under the close-out rulings (minutes `dd39332`): TV-002 run 5 and `tools/traceability.py` blob `12de3545` (CR-002 step 5, item 5), TV-012 run 2 and `tools/complexity_gate.py` blob `9cdc9195` (CR-005, item 4), TV-001 limitation 3 (item 12) and the lock changes of `37ae576`, CR-004 (`5792350`) and `eb52766` (items 2, 3, 12). Every change applies its ruling correctly; the reviewer reproduced both re-validations, both mutation checks, the repository and gate runs and the CR-004 unsafe audit list in a clean layout. This APPROVED delta is the independent review (CM plan section 9.2 step 3) that makes the ACC-TRACE-001 extension (blob `12de3545`) and ACC-COMPLEXITY-001 (blob `9cdc9195`) effective. No Major finding was open. Three new Minor findings are liens due PDR: F-11 (a narrow let-else under-count), F-12 (lock rows and TV-001 limitation 4 not updated) and F-13 (owner confirmation of the ACC-COMPLEXITY-001 reading). Details: section "SRR close-out delta (2026-09-26, iteration 3 re-issue 3)".

**Re-issue 2 of iteration 3, post-SRR-ruling delta (2026-09-26, HEAD `7c7959f`, SRR package item R16): verdict APPROVED (with liens).** Delta verification of the one commit that touched the product since `99ecccb`, `b2d3538` (SRR decision 114 accreditation of TV-001 to TV-010, decision 109 installs and lock section 1.1 checks, owner ruling 2026-09-26). Every section 9 row transcribes its proposed ACC statement word for word and cites decision 114 and the owner's statement in `minutes.md`; sections 8 record INSP-015 correctly; the index and lock rows read Accredited. No Major finding was open, so none closes on a ruling. One new Minor finding, F-10 (ACC-TRACE-001 and ACC-TREND-001 bind `validate_docs.py` blob `2bedc2a7`, which both tools import, while HEAD runs blob `3aa03681`), is a lien due PDR; F-07 is partly answered and stays a lien. Details: section "Post-SRR-ruling delta (2026-09-26, iteration 3 re-issue 2)".

**Re-issue at iteration 3 (2026-09-26, HEAD `b08e55d`, SRR package item R18, readiness finding R15-F2): verdict APPROVED (with liens).** Delta verification of the tool owner's commits `96af250` (`tools/validate_docs.py` blob `3aa03681`, `test_validate_docs.py` `RecordStateTests`, fixture `tools/tests/fixtures/record_state/`) and `860e84e` (TV-003 run 6, lock rows). The record state rule is correct on every case it claims, the known answers exercise both an open Major that fails and historical Major/Open lines that pass, the TV-003 known-answer set passes (150 tests), and TV-003 run 6 records the result. Two new Minor findings, F-08 (the tool header says the latest iteration section starts at the last heading, the code and TV-003 say the first) and F-09 (a finding table placed before the heading that names the highest iteration is not read), are dispositioned "Lien: fix before PDR" under the convergence rule. No Major finding is open. Details: section "Re-issue at iteration 3: delta verification of package item R18".

**Iteration 3 (2026-09-26, review baseline HEAD `adcfe0946d2f1b5cd8f41a8f91eb4219a7fb99a1`): verdict APPROVED (with liens).** F-02 (Major) is Closed: TV-001 to TV-010 section 3 was re-run on an export of commit `400e59d` (SRR package item R5), every identity of those runs equals the commit, the two tools changed afterwards (TV-003 blob `33ab5a83`, TV-010 blob `6f3018fd`) were committed in `3de1e2d` with their tests and fixture exactly as run, and the reviewer re-ran every record's section 3 on an export of HEAD with every identity equal to HEAD. One new Minor finding, F-07 (the records still call those two blobs uncommitted and name no commit for their runs), is dispositioned "Lien: fix before PDR" under the convergence rule of 2026-09-26 (charter section 4 item 3). No Major finding is open and none needs an owner ruling. Details: section "Iteration 3".

**Iteration 2 (2026-09-26): verdict NEEDS CHANGES.** The author reported F-01, F-03, F-04, F-05 and F-06 fixed and disputed none. The reviewer verified all five against the product (section "Iteration 2 re-review" and the Disposition column). F-02 (Major, commit binding) was not reported fixed and stays Open: `HEAD` is still `28e49e6`, and `docs/cm/`, `tools/render_review_figures.py` and `tools/tests/fixtures/schema/` are still untracked. The verdict can become APPROVED only when F-02 is closed.

**Iteration 1 verdict: NEEDS CHANGES.** Two Major findings: TV-001 claims keyword coverage that it does not have (finding-1), and no validation result is bound to a commit (finding-2). Four Minor findings. Everything else checked holds: every known-answer suite re-runs with the stated counts, every fixture tree digest and tool blob matches its record, and every inspected render agrees with the record.

**Search-first compliance:** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` was loaded and run before any repository search (queries: "tool validation and accreditation TV record criteria SWE-136 section 13"; "SRR package H12 toolchain proof sanity checks readiness shortfall"; "SWE-136 validate and accredit software tools"). One `grep -n '^## 13'` of `docs/process/01-lifecycle-and-reviews.md` ran before the tool was loaded. It pinned a section heading in a file already open at a known path. It is reported here so the order can be audited. All later `grep -n` calls only pinned lines that a search hit or a known file pointed at.

**Independence:** the reviewer did not author any product file and edited none. The known-answer suites were re-run read-only. `tools/traceability.py --report-only` rewrote `docs/vv/traceability-report.md` and `docs/vv/traceability.json`, as the assignment's command requires. `render_deck.py` was not re-run, because it rewrites `png/` in place. The TV-001 procedure was re-run on its own temporary copy.

**Criticality and assurance:** `criticality: neither`. 03 section 4.3.1 finds no tool safety-critical or mission-critical, and the 07 section 2.1.1 code row gives "No" for Neither when no file contains `unsafe` (Python has none), so `assurance_required: false`. The reviewer still applied the SWEHB `swe-136-software-tool-accreditation.md` section 7.1 task 1 ("Confirm that the software tool(s) needed to create and maintain software is validated and accredited") as the software assurance function of charter section 2. Result: every tool is Validated. None is yet Reviewed or Accredited, and two of those gaps are findings 1 and 2.

## Product files reviewed

Blob hashes are from `git hash-object` on 2026-09-26. The last column is the state against `HEAD` `28e49e6`, from `git status --short`.

| File | Blob | State | Findings |
|---|---|---|---|
| `docs/cm/tool-validation/README.md` | `11001b41` | untracked | finding-2, finding-3 |
| `docs/cm/tool-validation/TV-001-python-jsonschema.md` | `ee60bb93` | untracked | finding-1, finding-2 |
| `docs/cm/tool-validation/TV-002-traceability.md` | `f53fa153` | untracked | finding-2, finding-6 |
| `docs/cm/tool-validation/TV-003-validate-docs.md` | `e787b4b1` | untracked | finding-2, finding-5 |
| `docs/cm/tool-validation/TV-004-render-rmm.md` | `7693fd7c` | untracked | finding-2 |
| `docs/cm/tool-validation/TV-005-render-compliance.md` | `2d340044` | untracked | finding-2 |
| `docs/cm/tool-validation/TV-006-render-risk.md` | `0f065de2` | untracked | finding-2 |
| `docs/cm/tool-validation/TV-007-review-trend.md` | `a716f8da` | untracked | finding-2 |
| `docs/cm/tool-validation/TV-008-render-deck-chromium.md` | `df046f21` | untracked | finding-2, finding-5 |
| `docs/cm/tool-validation/TV-009-git.md` | `8089ba35` | untracked | finding-2 |
| `docs/cm/tool-validation/TV-010-render-review-figures.md` | `7273106b` | untracked | finding-2, finding-3, finding-4 |
| `docs/cm/tool-validation/evidence/` (32 files) | per file | untracked | finding-2 |
| `tools/toolchain.lock.md` | `8b232458` | modified | finding-3 |
| `tools/traceability.py` | `0a867523` | modified (235 added, 4 removed) | finding-2 |
| `tools/render_review_figures.py` | `979beb13` | untracked | finding-2, finding-4 |
| `tools/tests/` (11 modules, blobs in front matter; fixtures by tree digest below) | per file | mixed: `test_tools.py` and `test_traceability.py` modified; `test_git_known_answer.py`, `test_render_review_figures.py` and `test_traceability_srr_rules.py` untracked; the rest equal | finding-2 |

Tool blobs checked against their records: `traceability.py` `0a867523` (TV-002), `validate_docs.py` `2bedc2a7` (TV-003), `render_rmm.py` `2386a37f` (TV-004), `render_compliance.py` `d67d6b5e` (TV-005), `render_risk.py` `d38ba1dd` (TV-006), `review_trend.py` `04493157` (TV-007), `slides/render_deck.py` `b42425e9` (TV-008) and `render_review_figures.py` `979beb13` (TV-010). All eight equal their record. SHA-256 prefixes also match. Repository inputs named in TV-005, TV-006 and TV-007 also equal their records: `se-compliance-matrix.schema.json` `ef156b0f`, App. H corpus `8afa36e0`, `docs/risk/schema.json` `473cd797`, `rfa-rid-log.example.json` `0e913114`, `rfa-rid-log.schema.json` `38898b0c` and `docs/reviews/SRR/rfa-rid-log.json` `0dc293ad`.

Fixture tree digests were recomputed with the `tree` function of `evidence/python-tools-2026-09-25.py` (SHA-256 of the sorted `sha256  path` list). Each equals its record:

| Fixture | Files | Digest (prefix) | Record |
|---|---|---|---|
| `valid_project/` | 38 | `6a58c19d` | TV-002, TV-003 |
| `invalid_project/` | 32 | `2377caa9` | TV-002, TV-003 |
| `rmm/` | 17 | `fa7f91af` | TV-004 |
| `compliance/` | 15 | `a95aad46` | TV-005 |
| `risk/` | 5 | `3a594f97` | TV-006 |
| `review_trend/` | 6 | `c7d63b0f` | TV-007 |
| `slides/` | 1 | `f0519294` | TV-008 |
| `git/` | 2 | `bfc6387c` | TV-009 |
| `review_figures/` | 6 | `9cab14eb` | TV-010 |

## Commands run by the reviewer (2026-09-26, repository root, `.venv/bin/python`)

| Command | Exit | Result |
|---|---|---|
| `tools/validate_docs.py` | 1 | 34 passed, 2 failed. The failures are `docs/design/allocation.json` and `docs/plan/measurements.json`, whose schemas `docs/design/allocation.schema.json` and `docs/plan/measurements.schema.json` do not exist. Both are outside this product (cross item 1). This record passes after it was written (see Closure) |
| `tools/traceability.py --report-only` | 0 | 237 requirements, 170 test cases, 0 violations, 7 warnings (`HAZARD_INVERSE` x2, `SYS_UNALLOCATED` for REQ-SYS-125 and REQ-SYS-148, among others) |
| `tools/render_risk.py --check --gate SRR --hazards docs/safety/hazards.json` | 0 | 65 risks, 159 candidates, 0 warnings; `register.md` current |
| `tools/render_rmm.py --check` | 0 | |
| `tools/render_compliance.py --check` | 0 | |
| `-m unittest discover -s tools/tests` | 1 | 331 tests, 1 failure: `test_validate_docs.RepositoryTests.test_repository_exit_zero`, the same two missing schemas (repository content, cross item 1) |
| TV-002 section 3, three commands | 0 | 27 + 32 + 114 = 173 tests, OK |
| TV-003 section 3, two commands | 0 | 18 + 114 = 132 tests, OK |
| TV-004 `-p test_render_rmm.py` | 0 | 20 tests, OK |
| TV-005 `-p test_render_compliance.py -k CorpusParseTests -k ValidFixtureTests -k SeededFaultTests` | 0 | 26 tests, OK (whole module 27, OK) |
| TV-006 `-p test_render_risk.py` | 0 | 27 tests, OK; `faults.json` holds the 23 named faults |
| TV-007 `-p test_review_trend.py` | 0 | 20 tests, OK |
| TV-008 `-p test_render_deck.py` | 0 | 3 tests, OK, none skipped; Chromium `--version` `Google Chrome for Testing 148.0.7778.96`, binary SHA-256 `aa25f2e7...d2dd7b` equal to TV-008 |
| TV-009 `-p test_git_known_answer.py` | 0 | 6 tests, OK; `git --version` 2.50.1 (Apple Git-155), `xcrun --find git` equal to TV-009 |
| TV-010 `-p test_render_review_figures.py -k ParserTests -k DataKnownAnswerTests -k RunTests` | 0 | 32 tests, OK |
| TV-001 procedure `evidence/python-jsonschema-2026-09-25.sh` | 0 | both cases MATCH, PASS; the negative control fails as required (exit 1) |
| `tools/render_review_figures.py --review SRR --check` | 1 | "package group 'Keying and keyer' ... differs": the package says 11 TBR, `requirements.json` gives 16. This is the tool's specified behavior (TV-010 purpose 2) acting on repository content (cross item 2) |

**Independent known answers computed by the reviewer (not by the tool under test):**

- TV-009: blob `d184c928...`, tree `bf3b5c84...` and commit `779d21e2...` for the fixed identity and date 1790294400 +0000 were computed in Python from the git object formats. All three equal `known-answers.json`. The record says only the blob was cross-checked; the reviewer's computation now covers the tree and the commit.
- LTspice: 1/(2 pi x 1 kOhm x 159.155 nF) = 999.99964 Hz, equal to the stored 999.9996 Hz. The transcript measurement is 999.999642 Hz.
- OpenSCAD and FreeCAD: 30 x 20 x 10 - pi x 3^2 x 10 = 5717.257 mm^3, equal to the transcript.

**Renders opened with the Read tool (visual closure, charter section 11 rule 3):** `evidence/render-deck-fixture-slide-01.png` to `-04.png`. They show the title and author, the agenda items 1 and 2, the 3-column table with one row, and the alpha and beta bullets with no note text, all at 1280 x 720, matching the TV-008 inspection row. Also opened: the nine `evidence/render-review-figures-fixture-*.png`. They show entrance 1/2/1 with the dagger; success 2/0/1 with both footers; groups Transmitter 3 and Receiver 2 with 1 TBR; KDRs REQ-SYS-001 and -004; HZ-001 B to D Catastrophic and HZ-002 C to E Marginal; risk RSK-001 at R16, RSK-002 at Y10 with the safety override, RSK-003 at G2; the TPM board Red/Yellow/Not reported; ConOps OPS-001 and OPS-002; and the concept diagram, which is legible. These match the TV-010 inspection row. Also opened: `evidence/kicad-fixture-clean-top.png` and `kicad-fixture-seeded-top.png`, where the seeded trace runs close to TP1 against the clean route, and `evidence/openscad-fixture-cube.png` (block with a through hole).

## Readiness criteria

The R1 to R6 criteria of the code checklist are written for Rust crates. For the Python tools they are read as follows.

| # | Criterion | Answer | Evidence |
|---|---|---|---|
| R1 | Gate G1 (`cargo fmt`, `clippy`) | N/A | Python tools; no linter is locked for `tools/` (lock section 2 has none) |
| R2 | File at most 500 lines, functions at most 60 lines (CS-18) | N/A | CS-18 is a firmware rule (07 section 7). Measured for the record: `traceability.py` 2786 lines, `render_review_figures.py` 1176 lines (`wc -l`) |
| R3 | Design unit Active | N/A | Tools have no design unit. Their specification is `tools/README.md` together with 05 section 9.2 |
| R4 | `@req` tags | N/A | Rust tag convention |
| R5 | Test file exists | Yes | Every tool has a known-answer module (list above); all pass |
| R6 | `unsafe_audit.py` | N/A | No `unsafe` in Python |
| R-TV | Adapted readiness: every TV record exists, and its section 3 command runs | Yes | Ten records; every command re-run above exits 0 |

`readiness_met: true` on R5 and R-TV.

## Tool validation criteria (05 section 9.2 steps 1 to 4; 05 section 13 SRR row)

| Id | Check | Answer | Evidence |
|---|---|---|---|
| TV-S1 | Step 1 identification: exact version, command, install source with installer URL and SHA-256, SHA-256 or blob of every file validated, "commit SHA tested" | No | Versions, commands and blobs are present and verified above. Installer URLs are absent where upstream publishes none, and each record says so and names its substitute (TV-001 section 1; TV-008 section 1; TV-009 section 1): acceptable. Fails because no record can name a commit containing the files it tested: finding-2 |
| TV-S2 | Step 1 class and purposes, one line each | Yes | Each record, section 2. All are class B, as 05 section 9.1 lists them |
| TV-S3 | Step 1 known-answer test with fixture path under `tools/tests/fixtures/<tool>/`, run command and pass criteria with seeded faults (class B: "Known-answer test with a seeded fault", 05 section 9.1) | Yes, with gaps | Each record, section 3. Seeded faults exist for every tool: `invalid_project` (TV-002, TV-003); 10 RMM faults; 11 compliance faults whose strings were checked in `test_render_compliance.py`; 23 risk faults; zone and CLI cases; the location guard; the git fsck corruption; figure disagreements; 4 plus 18 schema faults with a negative control. Gaps: finding-5 (two accredited exit-code purposes have no known answer) |
| TV-S4 | Step 1 accredited purposes are all exercised by the known-answer test | No | finding-1 (TV-001 keyword `minProperties`); finding-5 (TV-003 purpose 5 exit 2; TV-008 purpose 4 exit 1) |
| TV-S5 | Step 1 result: date, test count, output excerpt, evidence file | Yes | Each record, section 4, cites `evidence/python-tools-2026-09-25.log.txt` or `python-jsonschema-2026-09-25.log.txt`. The counts reproduce (commands table) |
| TV-S6 | Step 1 reproducibility (class A only) | N/A | All ten are class B. Each still records two identical runs |
| TV-S7 | Step 1 limitations and step 4 re-validation triggers present and correct | Yes, with an error | Present in every record (sections 6 and 7). TV-010 limitation 3 misdescribes the tool: finding-4 |
| TV-S8 | Step 3 reviewer checks the TV record and the fixture: the fixture's expected answers are independent of the tool | Yes | Expected values were hand-written for TV-001 (`known-answers.json` pairs), TV-004 to TV-007 (stored strings and 01 section 11 counts), TV-009 (reviewer's independent computation above) and TV-010 (fixture counts checked against the renders). Revisions after a failed run are documented in the transcripts (kicad STEP z, LTspice precondition); both are PDR-due tools |
| TV-S9 | 05 section 13 SRR row: TV records exist for the ten named tools, each reviewed and accredited | No | Ten records exist and match the ten tools of 05 section 13 line 583. Review: this record, NEEDS CHANGES. Accreditation: pending in all ten sections 9. Stale statements that the plan does not list TV-010: finding-3 |
| TV-S10 | Lock section 1.1 records each SRR sanity check with date, the commit tested and the test count (step 2), and section 5 agrees with the records | Yes, with gaps | Lock lines 60 to 87 record the runs of 2026-09-25 23:06 to 23:47 with evidence names. Section 5 lists TV-001 to TV-010 as Validated, equal to the README index. Gaps: finding-2 (commit) and finding-3 (stale note) |

## SRR row 20 toolchain proof: lock section 1.1 sanity checks

This table covers the H12 list only: kicad-cli, LTspice, rustc and cargo, clippy, picotool, OpenSCAD with FreeCAD, and the venv Python with jsonschema. Each check was read against its transcript and `known-answers.json`.

| Lock row | Transcript result | Reviewer check | Answer |
|---|---|---|---|
| kicad-cli (lock line 60) | run 2 pass: ERC clean 0, seeded `pin_not_connected` R1 pin 2 (exit 5); DRC one `clearance`; drill 1 PTH 0.70 mm and 1 NPTH 3.20 mm; CPL and BOM equal; STEP box to z 1.51 mm; normalized hashes blocked | Renders opened. The 1.51 mm correction equals the 1.6 mm board minus two 35 um copper and two 10 um mask layers. It was revised after run 1 and documented (lock section 1.4 finding 5) | Yes (partial: normalized exports blocked until `tools/normalize_fab.py`; TV due PDR) |
| LTspice (line 63) | runs 3 and 4 pass | Analytic value recomputed; seeded netlist exit 1; hang guard counted as failure | Yes |
| rustc / cargo (line 64) | both runs pass; ELF `3201d382...df7d` identical over 3 builds | `known-answers.json` records that the ELF hash came from run 1 (regression value); the 05 section 9.2 criterion is equality across builds, which holds | Yes |
| clippy (line 65) | `absurd_extreme_comparisons` and `unwrap_used` seeded, exit 101 | The seeded `unwrap_used` shows that the project lint table is in force | Yes |
| picotool (line 74) | `uf2 convert` and `info` pass; `verify` blocked (needs a device) | Documented blocked item; TV due CDR | Yes (partial) |
| OpenSCAD + FreeCAD (line 86) | run 2 pass with a one-line listing adaptation; `tools/scad2step.py` absent | Volume recomputed; render opened | Yes (partial: script absent; TV due PDR) |
| python + jsonschema (line 78) | 4 runs pass | Re-run by the reviewer: PASS; negative control exit 1 | Yes (see finding-1 for scope) |

Row 20 status from this product alone: the lock's sanity-check results now exist for every tool H12 names. The blocked parts carry a named reason and gate. The FW-B0 part of row 20 is reviewed in `checklists/fw-b0-toolchain-proof.md`, not here.

## A. Environment, dependencies and build (CS-01 to CS-04)

| Id | Answer | Evidence |
|---|---|---|
| CK-CODE-A1 | N/A | `no_std` rule for image crates; the tools are host Python |
| CK-CODE-A2 | Yes | `render_review_figures.py` adds matplotlib, which is locked (lock section 2: 3.11.2, class B) and named in TV-010 section 1. `tools/requirements.txt` still lists it unpinned (AL-4; cross item 3) |
| CK-CODE-A3 | N/A | Rust `cfg` rule |

## B. Unsafe code (CS-05 to CS-10)

| Id | Answer | Evidence |
|---|---|---|
| CK-CODE-B1 to B8 | N/A | No `unsafe` in Python; no MMIO |

## C. Panics, errors and arithmetic (CS-11 to CS-16)

| Id | Answer | Evidence |
|---|---|---|
| CK-CODE-C1 | Yes (adapted) | `load_allocation` (traceability.py, working-tree delta) returns early on an absent file, stores a parse error in `allocation_error` instead of raising, and type-checks every node (`isinstance`). `check_stakeholders` skips non-dict entries. The repository run completes with exit 0 and no traceback |
| CK-CODE-C2 | Yes (adapted) | Failures become catalogue findings (`STAKEHOLDERS_MISSING`, `SYS_UNALLOCATED`) or exit codes, never silent. `render_review_figures.py --check` exits 1 with a named disagreement (commands table) |
| CK-CODE-C3 to C7 | N/A | Rust error and arithmetic rules |

## D. Structure, complexity and target platform rules

| Id | Answer | Evidence |
|---|---|---|
| CK-CODE-D1 | N/A | SWE-220 applies to firmware components (07 section 14.1); no complexity tool is locked for Python |
| CK-CODE-D2 | Yes | `load_allocation.visit` recurses over the parsed JSON tree, whose depth is bounded by the file. No other recursion appears in the delta |
| CK-CODE-D3 to D9 | N/A | Rust and target rules |

## E. Correctness against design and requirements

| Id | Answer | Evidence |
|---|---|---|
| CK-CODE-E1 | No | The specification of the tools is the TV purposes plus `tools/README.md`. TV-010 limitation 3 states behavior the code does not have (finding-4). `traceability.py` T-18 and T-21 match 02 sections 2.3 and 3.0 as cited in the docstrings, and the known answers in `test_traceability_srr_rules.py` pass (32 tests) |
| CK-CODE-E2 | N/A | Firmware timing constants |
| CK-CODE-E3 to E8 | N/A | Keyer, register and safe-state rules |
| CK-CODE-E9 | Yes | The two figure functions outside the SRR set (`risk`, `concept`) are kept deliberately, with known-answer tests and a comment (render_review_figures.py lines 953 to 957). The catalogue guard test `CatalogueTests` fails on any code without a known answer |

## F. Traceability tags

| Id | Answer | Evidence |
|---|---|---|
| CK-CODE-F1 to F3 | N/A | `@design` and `@req` are Rust conventions. The Python tools cite their process sections in their docstrings instead (for example `check_allocation`: "02 T-18 at SRR") |

## G. Secure coding

| Id | Answer | Evidence |
|---|---|---|
| CK-CODE-G1 | Yes | The inputs are repository files. JSON goes through `validate_docs.load_json` with the error captured, and every field is type-checked before use |
| CK-CODE-G2 to G4 | N/A | Firmware input rules |
| CK-CODE-G5 | N/A | Gate G5 is a firmware gate |

## H. Tests and testability

| Id | Answer | Evidence |
|---|---|---|
| CK-CODE-H1 | Yes | Every tool takes `--root` or an explicit path, and the known answers run on fixtures in temporary copies (TV-002 to TV-010 section 3) |
| CK-CODE-H2 | N/A | 05 section 9.2 step 3 puts fixture independence under the reviewer's check (TV-S8) instead of a separate test author. The tests exist and pass |
| CK-CODE-H3 | N/A | MC/DC applies to safety-critical firmware |

## I. Documentation and style

| Id | Answer | Evidence |
|---|---|---|
| CK-CODE-I1 | Yes | Every new function in the delta has a docstring citing its rule (`load_allocation`, `check_stakeholders`, `check_allocation`, `is_l2_module`, `child_modules`, `allocated_modules`, `receiving_modules`). Exception: `allocation_state` has none (trivial) |
| CK-CODE-I2 | Yes | Names are descriptive |
| CK-CODE-I3 | N/A | `cargo fmt`. Observed: three blank lines before `verification_row` in traceability.py (cosmetic; no finding) |
| CK-CODE-I4 | Yes | No commented-out code in the delta |

## J. Common review traps

| Id | Answer | Evidence |
|---|---|---|
| CK-CODE-J1 | Yes | Every API used resolves: the suites run with 0 errors |
| CK-CODE-J2 | Yes | `validate_docs.load_json` is called as defined |
| CK-CODE-J3 | Yes | T-18 treats "child_ids or allocation.json" as one union (`receiving_modules`), as 02 section 2.3 states |
| CK-CODE-J4 | Yes | Lines measured with `wc -l` (product_size) |

## Iteration 2 re-review (2026-09-26)

Same reviewer role, new invocation. The author reported `{"fixed":["F-01","F-03","F-04","F-05","F-06"],"disputed":[]}`. Search-first: `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` was loaded and queried ("minProperties seeded fault keywords schema TV-001") before any `grep`; later `grep -n` calls only pinned lines in files at known paths. The reviewer edited no product file. The TV-001 procedure ran with `TMPDIR` set to the reviewer's scratch directory, so its temporary copies did not touch the fixture.

| Command | Exit | Result |
|---|---|---|
| `bash docs/cm/tool-validation/evidence/python-jsonschema-2026-09-26.sh` | 0 | case `requirement` 0 and 4 errors MATCH; case `keywords` 0 and 19 errors MATCH (including `entries/16/margins` `minProperties`); PASS; negative control exit 1; survey 9 schemas, 23 keywords, none missing, exit 0; survey negative control names `minProperties`, exit 1 |
| `-m unittest discover -s tools/tests -p test_render_deck.py -v` | 0 | 5 tests OK, none skipped (`SeededFailures` 2 new) |
| `-m unittest discover -s tools/tests -p test_validate_docs.py -k UsageErrorTests -v` | 0 | 2 tests OK |
| `git diff --numstat 28e49e6 -- tools/traceability.py` | 0 | 235 added, 4 removed |
| `git hash-object` on `render_review_figures.py`, `traceability.py`, `validate_docs.py`, `slides/render_deck.py` | 0 | `979beb13`, `0a867523`, `2bedc2a7`, `b42425e9`: every tool is unchanged since iteration 1, so the fixes touched records, tests and fixtures only |
| `git log -1`; `git status --short` on the product | 0 | `28e49e6`; `docs/cm/`, `render_review_figures.py`, `fixtures/schema/` untracked, `traceability.py` modified (F-02 stays Open) |

Checklist answers changed by iteration 2: TV-S4 is now Yes (F-01 and F-05 closed: every accredited purpose, including the `minProperties` keyword and the two exit-code purposes, has a known answer). CK-CODE-E1 is now Yes (F-04 closed: TV-010 limitation 3 matches the code). TV-S3 and TV-S7 lose their gaps. TV-S1, TV-S9 and TV-S10 remain No or gapped on F-02 alone. The iteration 1 tables above are kept as written.

## Iteration 3 (2026-09-26)

**Scope and independence.** New invocation of the reviewer role (`reviewer:tools`); it authored no product file and edited none. Review baseline: HEAD `adcfe0946d2f1b5cd8f41a8f91eb4219a7fb99a1`; every product file is identified by its committed blob in `product_files` (`git rev-parse HEAD:<path>`). The tool paths of the product are clean against HEAD (`git status --short` lists only other review records). Search-first: `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` was loaded and queried ("tool validation commit tested TV record result row HEAD committed INSP-015 F-02") before any manual search; `grep -n` and `git grep -n` afterwards only pinned lines in files at known paths. The known-answer procedures ran on an export of HEAD (`git archive HEAD`) in the reviewer's scratch directory, with `TMPDIR` there, so nothing in the repository was written. Convergence rule (lead SE direction 2026-09-26, applying charter section 4 item 3: a Minor RID is fixed before the next review and does not block the baseline): only Major findings change products in this round; every Minor finding is dispositioned "Lien: fix before PDR".

**Commands run by the reviewer (repository root, `.venv/bin/python`).**

| Command | Exit | Result |
|---|---|---|
| `git log --oneline`; `git rev-parse <commit>:<tool>` for the eight Python tools at `1d423e5`, `400e59d`, `3de1e2d` and HEAD | 0 | `400e59d` is an ancestor of HEAD. `traceability.py` `0a867523`, `render_rmm.py` `2386a37f`, `render_compliance.py` `d67d6b5e`, `render_risk.py` `d38ba1dd`, `review_trend.py` `04493157`, `slides/render_deck.py` `b42425e9` are equal at all four. `validate_docs.py` is `2bedc2a7` at `1d423e5` and `400e59d`, `33ab5a83` at `3de1e2d` and HEAD; `render_review_figures.py` is `979beb13`, then `6f3018fd` from `3de1e2d` |
| `evidence/python-tools-2026-09-26-r5.py <export of HEAD> worktree` | 0 | TV-002 176, TV-003 142, TV-004 20, TV-005 26, TV-006 27, TV-007 20, TV-008 5, TV-009 6, TV-010 42 tests, each PASS; all 49 identity lines "equal to HEAD". Apart from paths, run times and the repository-content check, the output equals the author's `python-tools-2026-09-26-r5-worktree.log.txt`: the same results for every tool and the same identities. The repository-content check now passes (the author's run failed it on INSP-005 and INSP-013, since fixed by R13) |
| `evidence/python-jsonschema-2026-09-26-r5.sh <export of HEAD>` | 0 | case `requirement` 0 and 4 errors MATCH; case `keywords` 0 and 19 errors MATCH (including `entries/16/margins` `minProperties`); PASS; negative control exit 1; survey of 11 schemas and 23 keywords, none missing, PASS; the survey negative control names `minProperties` |
| Fixture tree digest of `tools/tests/fixtures/review_figures/` at HEAD (the `tree` function of the procedure) | 0 | `1a2dae0b...b07c`, equal to TV-010 run 4 |
| `tools/validate_docs.py` | 0 | 37 passed, 0 failed; this record PASSES as APPROVED under the record drift rule (every `product_files` blob equals HEAD) |
| `tools/traceability.py --report-only` | 0 | 237 requirements, 170 test cases, 0 violations, 2 warnings (`SYS_UNALLOCATED` REQ-SYS-125, REQ-SYS-148); the rewritten report equals the committed one (`git status` clean) |
| `tools/render_risk.py --check --gate SRR --hazards docs/safety/hazards.json` | 0 | 65 risks, 159 candidates, 0 warnings; `register.md` current |
| `tools/render_rmm.py --check`; `tools/render_compliance.py --check` | 0; 0 | both current |
| `tools/render_review_figures.py --review SRR --check` | 0 | check passed for 7 figures, nothing written (cross item 2 is resolved) |
| `-m unittest discover -s tools/tests` | 0 | 392 tests, OK |

**Renders opened with the Read tool (visual closure, charter section 11 rule 3), the five of TV-010 inspection 2:** `render-review-figures-fixture-2026-09-26-entrance-checklist.png` (Not met 1: S1; Partially met 2: rows 1 and 2; Met 1: S4 with the dagger and the note "dagger: fixture note"), `...-success-criteria.png` (2, 0, 1 with both footer lines), `...-kdr-map.png` (REQ-SYS-001 tagged "Test TBR PDR", REQ-SYS-004 "Inspection", footer "2 KDRs, 1 with an open TBR"), `render-review-figures-layout-19-rows-entrance.png` (lanes of 5, 19 and 15 rows; P18 ends inside its lane; the three-line footnotes of the first and last lanes clear the rows) and `...-layout-19-rows-success.png` (11 two-line and 19 one-line rows, the last row P18 inside its box, the footer below the boxes). Each matches the TV-010 "Inspection 2" row. The entrance layout arithmetic in the test docstring (`test_render_review_figures.py` lines 293 and 294: (834 - 78) / 19 = 39.789 px, 20 x 39.789 / 43 = 18.51 pt) was re-computed and holds.

**Changed text checked for new Major defects** (diff `1d423e5..HEAD` of the TV records, the README and the lock). TV-003 purpose 6 was compared with `tools/validate_docs.py` lines 760 to 838: the `path@blob` pattern, `git ls-tree -r --full-tree HEAD`, the prefix match, the failure for an APPROVED record that names no blob, the `note:` line for other verdicts, and the "not applied" note outside a work-tree top all match. The TV-010 purpose 2 and 3 additions agree with `LabelAndDaggerTests` and `LayoutKnownAnswerTests` and with the renders above. The ten "R5 re-run" paragraphs and the section 4 rows at `400e59d` agree with the committed transcripts: every identity line reads "equal to HEAD", and the counts are TV-002 176, TV-003 137, TV-010 32, and TV-001 7 and 8 PASS. Lock line 59 and README action 3 describe the R5 runs correctly. No new Major defect. The residual status text on the two tools changed after `400e59d` is the new Minor F-07.

**Disposition table.**

| Finding | Severity | Iteration 3 disposition | Evidence at HEAD |
|---|---|---|---|
| F-01 | Major | Closed | Verified at iteration 2. At HEAD the fixture files are unchanged (`keywords.schema.json` `42c0822f`, `keywords-invalid.json` `272b585e`, `known-answers.json` `86051ad7`, equal to the iteration 2 blobs), and the reviewer re-ran the procedure on the export of HEAD: PASS, and the survey of 11 schemas finds no keyword missing (`TV-001-python-jsonschema.md` section 4 rows 7 and 8) |
| F-02 | Major | Closed | TV-001 to TV-010 section 4 each carry a row "`HEAD` `400e59d` ... an export of the commit" (for example TV-002 line 56, TV-003 line 58, TV-010 line 51), backed by `evidence/python-tools-2026-09-26-r5-head.log.txt` and `python-jsonschema-2026-09-26-r5.log.txt`, whose identity lines all read "equal to HEAD" at `400e59d`. `docs/cm/`, the tools, tests and fixtures are committed; lock line 59 names the commit; README line 49 withdraws owner action 3 for this finding. The later blobs `33ab5a83` and `6f3018fd` and their tests and fixture are committed in `3de1e2d` exactly as run 5 and run 4 identified them, and the reviewer's run on HEAD reproduces them. The remaining record wording is F-07 |
| F-03 | Minor | Closed | Verified at iteration 2; `TV-010-render-review-figures.md` line 9 and README line 34 still give Due SRR with no stale note |
| F-04 | Minor | Closed | Verified at iteration 2; `render_review_figures.py` changed (`6f3018fd`), so the reviewer checked limitation 3 again: `TV-010-render-review-figures.md` line 67 states `max(29, largest group count + 3)` and `max(20, largest open-TBR count + 3)`, as `tools/render_review_figures.py` lines 723 and 724 at HEAD read (`git grep -n set_xlim`) |
| F-05 | Minor | Closed | Verified at iteration 2; `UsageErrorTests` and `SeededFailures` are committed (`test_validate_docs.py` `4fb5bcc7`, `test_render_deck.py` `ff58fb7b`) and pass in the reviewer's run on HEAD (TV-003 142, TV-008 5, none skipped) |
| F-06 | Minor | Closed | Verified at iteration 2; `TV-002-traceability.md` line 19 still reads 235 added and 4 removed against `28e49e6` |
| F-07 (new) | Minor | Lien: fix before PDR | See the findings table: TV-003 and TV-010 status lines (line 6 of each) and README line 49 still call the committed blobs uncommitted; no result row names `3de1e2d` or later |

Note on F-04: the line numbers moved with the blob. The reviewer pinned them at HEAD with `git grep -n`.

**Lien table.**

| Finding | Severity | Disposition | Owner | Due | Package carriage |
|---|---|---|---|---|---|
| F-07 | Minor | Lien: fix before PDR | Tool validation author (Claude) | PDR readiness declaration | Routine item (package section 20.1, convergence rule) |

**Checklist answers changed by iteration 3.** TV-S1 is now Yes: every record names a commit holding what it tested, `400e59d` for the R5 rows, and the two later blobs are committed unchanged (F-07 is a naming lien). TV-S10 is Yes, with the F-07 lien on lock rows 106 and 112. TV-S9 stays No for one reason only: section 9 of each record still waits for the owner's accreditation (decision 114; owner action OA-7). That is the owner's step 3 decision, which follows this review. It is not a product defect and not a finding. The iteration 1 and 2 tables above are kept as written.

**Cross-document items at HEAD.** Item 1 is resolved: both schemas exist and `validate_docs.py` exits 0. Item 2 is resolved: `render_review_figures.py --check` exits 0. Item 3 is still open as package section 15 item 55 (CM author). Item 4 is still open as package item 38 (H10). Item 5 is still an owner process item.

**Counts.** 7 findings: 2 Major (both Closed), 5 Minor (4 Closed, 1 Lien). Disputed-accepted 0. Open Major 0. No finding needs an owner ruling.

VERDICT (iteration 3, independent reviewer): APPROVED (with liens)

FINDINGS: F-01 to F-06 Closed; F-07 Minor (new) Lien: fix before PDR

MEASUREMENTS: findings re-checked 6 plus the changed passages of 13 files; closed 6; lien 1; open Major 0; iteration 3; turns 32; minutes 45

## Findings

| Finding | Origin | Severity | Item | Location | Description | State | Deferred to | Disposition (iteration 2, 2026-09-26) |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>F-01 (finding-1) | reviewer | Major | TV-S4 | `docs/cm/tool-validation/TV-001-python-jsonschema.md` line 30 (section 2); `tools/tests/fixtures/schema/keywords.schema.json` | TV-001 line 30 says every keyword that the nine repository schemas use is in the purpose 2 list. This is false. `docs/plan/tpm.schema.json` line 168 uses `minProperties`, and the file was committed in `4e3f891`, before the survey. `minProperties` is not in the list and has no seeded fault. `docs/plan/tpm.json` is an SRR product that `validate_docs.py` validates with this schema. By TV-001 limitation 1 and TV-003 limitation 2 that keyword is outside the accreditation, yet the record's claim hides the gap. A second error on the same line: "`maxItems` ... no repository schema uses it yet" is also false, because `docs/process/rmm.schema.json` line 52 uses it. A reviewer survey of all nine schemas finds exactly one keyword outside the list, `minProperties`. The claim is wrong and it narrows an SRR evidence path, so it blocks accreditation. Fix: add a `minProperties` constraint to `keywords.schema.json` with one seeded fault in `keywords-invalid.json` and the stored pair in `known-answers.json`; re-run; add the keyword to purpose 2 and to ACC-PYJS-001; correct the `maxItems` note. Citation: charter section 11 rule 2; 05 section 9.2 step 1 | Verified | | Closed. TV-001 section 2 purpose 2 now lists `minProperties`, and the survey note says the 2026-09-25 survey missed `minProperties` and wrongly said no schema used `maxItems`. ACC-PYJS-001 (section 9) lists 23 keywords including `minProperties`. `keywords.schema.json` `definitions.entry.properties.margins` has `minProperties: 1`; `keywords-invalid.json` `entries[16].margins` is `{}`; `known-answers.json` stores `["entries/16/margins", "minProperties"]` (19 pairs); `keywords-valid.json` exercises the passing case. The reviewer re-ran `evidence/python-jsonschema-2026-09-26.sh`: both cases MATCH, PASS, exit 0; negative control exit 1; the new keyword survey finds 9 schemas and 23 keywords, none missing, exit 0, and its negative control fails naming `minProperties`, exit 1. The survey result equals the reviewer's iteration-1 survey (exactly one keyword was missing), and the survey is now a standing step of the procedure and a re-validation trigger (section 7). Lock section 1.1 row `python (venv) + jsonschema` records runs 5 and 6 |
| <a id="finding-2"></a>F-02 (finding-2) | reviewer | Major | TV-S1, TV-S9, TV-S10 | TV-002, TV-009 and TV-010 section 1 and section 4 "Commit tested"; TV-003 section 1 (`test_tools.py`, `valid_project`); lock section 1.1 lines 60 to 87 ("fixture untracked"); all of `docs/cm/tool-validation/` | 05 section 9.2 step 1 requires the "commit SHA tested". 05 section 13 (SRR row) requires the TV records reviewed and accredited, with the tool files as configuration items (Table 4-1 row 28). 01 section 3.1 item 1 requires evidence rows to cite a commit. No result is tied to a commit containing what it tested. `tools/traceability.py` is modified. `tools/render_review_figures.py`, `test_git_known_answer.py`, `test_traceability_srr_rules.py`, `test_render_review_figures.py` and the fixtures `git/`, `schema/`, `review_figures/`, `kicad/`, `ltspice/`, `rust/`, `picotool/` and `openscad/` are untracked. `test_tools.py`, `test_traceability.py` and `valid_project/` are modified. The records and evidence themselves (`docs/cm/`) are untracked. The blob identities make the tested content exact, and README item 3 raises the question honestly. But a baseline cannot cite untracked records, and the owner cannot accredit "at version v" when no commit holds v. Fix: after owner authorization (package item H17), commit the tools, tests, fixtures, records and evidence. Re-run each record's section 3 on that commit, append a result row naming the commit, and update lock section 1.1. Then withdraw README owner action 3. Citation: 05 sections 9.2 step 1 and 13; 01 section 3.1 item 1 | Closed | | Iteration 3: Closed (see section "Iteration 3"). Iteration 2: not reported fixed and not fixed: `git log -1` was `28e49e6`; `git status` shows `docs/cm/`, `tools/render_review_figures.py` and `tools/tests/fixtures/schema/` untracked and `tools/traceability.py` modified. Every new result row (TV-001 runs 5 and 6, TV-003 run 3, TV-008 run 3) again names `HEAD` `28e49e6` with untracked or modified files. README owner action 3 now lists the commit content and ties it to package item H17 and this finding, which is the correct path. Closes when the commit is made after owner authorization, each record's section 3 is re-run on it, and the result rows and lock section 1.1 name that commit |
| <a id="finding-3"></a>F-03 (finding-3) | reviewer | Minor | TV-S9, TV-S10 | TV-010 line 9 (Due); `docs/cm/tool-validation/README.md` line 34; `tools/toolchain.lock.md` line 105 (section 1.2) and line 237 (section 5) | Four places say that CM plan section 13 does not list `tools/render_review_figures.py` and call adding it a cross-document item. The working-tree 05 section 13 SRR row (line 583) lists it with its known-answer test, and 05 section 9.2 has its row (line 473). The statements are stale and contradict the single authoritative schedule. Fix: set Due to "SRR (CM plan section 13)" in TV-010 and the README index, and remove the notes in lock sections 1.2 and 5 | Verified | | Closed. TV-010 line 9 Due is "SRR (CM plan section 13, SRR row; its known-answer row is in CM plan section 9.2)". README index line 34 gives Due SRR under the column "Due (CM plan section 13)" with no cross-document note. Lock line 105 (section 1.2) and line 237 (section 5) carry no statement that the plan omits the tool; the lock change log row of 2026-09-26 (line 255) records the removal |
| <a id="finding-4"></a>F-04 (finding-4) | reviewer | Minor | CK-CODE-E1, TV-S7 | TV-010 line 62 (limitation 3); `tools/render_review_figures.py` lines 621 and 622 | Limitation 3 says the axis ranges of the requirements-by-group figure are fixed ("0 to 25 and 0 to 20"), so a count above them would draw outside the axis. The code sets `ax.set_xlim(0, max(29, widest + 3))` and `ax2.set_xlim(0, max(20, most_tbr + 3))`. The axes grow with the data, and the main axis starts at 29, not 25. The record states a defect the tool does not have and misstates the range. Fix: rewrite limitation 3 to describe the actual rule (minimum ranges 29 and 20, extended to the largest count plus 3), or add a known answer with a count above 29 and cite it | Verified | | Closed. TV-010 line 62 limitation 3 now states the ranges `max(29, largest group count + 3)` and `max(20, largest open-TBR count + 3)`, which equal `tools/render_review_figures.py` lines 621 and 622 (blob still `979beb13`, the tool is unchanged). The thresholds it names (group count above 26, open-TBR count above 17) follow from those expressions, and it states honestly that the extension branch has no known answer |
| <a id="finding-5"></a>F-05 (finding-5) | reviewer | Minor | TV-S3, TV-S4 | TV-003 line 33 (purpose 5, "2 on a usage error"); TV-008 line 30 (purpose 4, "Exit 1 on any conversion or render failure"); `tools/tests/test_render_deck.py` lines 54 and 75 | Two accredited exit-code purposes have no known answer. No test asserts exit 2 of `validate_docs.py`. The reviewer observed exit 2 from argparse on `--bogus`, but that run is not part of the record. `test_render_deck.py` asserts only exit 0 and exit 2, and no seeded conversion or render failure checks exit 1 (`render_deck.py` lines 77, 82, 113). 05 section 9.1 requires class B tools to have a known-answer test with a seeded fault for what is accredited. Fix: add a usage-error test to `test_validate_docs.py` and a seeded failure (for example a deck with an AsciiDoc error, or an unreachable shell path) to `test_render_deck.py`, or remove those clauses from the purposes and scope statements | Verified | | Closed. `test_validate_docs.py` (blob `8944a389`) adds `UsageErrorTests`: `--bogus` and a `--root` that is not a directory each assert exit 2, the argparse message on stderr and no PASS or FAIL output (`validate_docs.py` line 865 `parser.error`). `test_render_deck.py` (blob `ff58fb7b`) adds `SeededFailures`: an unreadable deck makes the converter fail (exit 1, `EACCES`, no HTML, no `png/`) and a headless shell replaced by `/usr/bin/false` makes slide 1 fail (exit 1, "render failed for slide 1", no slide PNG). The tools are unchanged (`validate_docs.py` `2bedc2a7`, `render_deck.py` `b42425e9`). Reviewer re-run: `-p test_render_deck.py` 5 tests OK, none skipped; `-p test_validate_docs.py -k UsageErrorTests` 2 tests OK. TV-003 (run 3, 134 tests) and TV-008 (run 3, 5 tests, 0 skipped) cite them in sections 3 and 4 |
| <a id="finding-6"></a>F-06 (finding-6) | reviewer | Minor | TV-S1 | TV-002 line 19 | The record says "239 lines added and 9 removed against `28e49e6`". `git diff --numstat 28e49e6 -- tools/traceability.py` gives 235 added and 4 removed (239 changed lines in all). Fix: correct the counts | Verified | | Closed. TV-002 line 19 now reads "235 lines added and 4 removed against `28e49e6`", equal to `git diff --numstat 28e49e6 -- tools/traceability.py` (235, 4) re-run by the reviewer; the tool blob is still `0a867523`. Observation, no finding: the sentence that follows ("corrected 2026-09-26 after INSP-015 finding-6 by another author on 2026-09-25") joins two clauses ambiguously; the facts it carries are right |
| <a id="finding-7"></a>F-07 (finding-7) | reviewer (iteration 3) | Minor | TV-S1, TV-S10 | `docs/cm/tool-validation/TV-003-validate-docs.md` lines 1, 6, 20 to 21 and 103; `TV-010-render-review-figures.md` lines 1, 6, 17 to 19, 65 and 85; `README.md` lines 27, 34 and 49; `tools/toolchain.lock.md` lines 106 and 112 | At HEAD the records still describe `tools/validate_docs.py` blob `33ab5a83` and `tools/render_review_figures.py` blob `6f3018fd` as working-tree files "not yet committed", the proposed scopes ACC-VALDOCS-001 and ACC-FIGS-001 say "once committed", and README owner action 3 is "Open again ... authorize their commit". Both blobs, with `test_validate_docs.py` `4fb5bcc7`, `test_render_review_figures.py` `cb54d28b` and the `review_figures/` fixture (tree digest `1a2dae0b`, recomputed by the reviewer), were committed in `3de1e2d` and are unchanged at HEAD, but no result row of TV-003 or TV-010 names a commit that contains them (05 section 9.2 step 1, "commit SHA tested"). The tested content is exact and committed, and the reviewer's run on an export of HEAD reproduces TV-003 (142 tests) and TV-010 (42 tests) with every identity equal to HEAD, so the gap is in the record text, not in the evidence. Fix: append a section 4 row to TV-003 and TV-010 naming `3de1e2d` or a later commit, correct the status lines, headings, identification states, limitation 1 of TV-010 and the two scope statements, close README owner action 3 for TV-003 and TV-010, and update lock rows 106 and 112 | Lien | PDR | Lien: fix before PDR (convergence rule; charter section 4 item 3) |

## Cross-document items (outside this product; for Claude)

1. `docs/design/allocation.schema.json` and `docs/plan/measurements.schema.json` are absent while their instances exist. `validate_docs.py` exits 1, and `test_validate_docs.RepositoryTests` fails (repository content, lock repository-content row). Owners: the allocation and measurements authors.
2. `tools/render_review_figures.py --review SRR --check` exits 1. `docs/reviews/SRR/package.md` section 8 gives group "Keying and keyer" 11 open TBR, while `docs/requirements/sys/requirements.json` gives 16. Owner: the package author. The figures cannot be regenerated until this is fixed.
3. `tools/requirements.txt` lists ten unpinned names. 05 section 13 SRR row (AL-4) requires `==` pins of lock section 2. This is TV-001 limitation 4, and a remaining row 20 or CM shortfall. Owner: the CM author.
4. `docs/reviews/SRR/figures/risk-matrix.py` and `concept-block-diagram.py` generate package figures (render_review_figures.py comment, lines 953 to 957). 05 section 9.1 class B covers review-package figure generators, but neither has a TV record or a place in 05 section 13. Owner: package item H10.
5. `docs/cm/tool-validation/README.md` owner action 1 notes that no checklist template for TV records exists, and 08 section 3.5 holds a review without its checklist. This review used the code checklist plus 05 section 9.2 and section 13 as items TV-S1 to TV-S10, as assigned. A `peer-review-checklist-tool-validation.md`, or a TV section added to the code checklist, would make the criteria auditable. This is a charter or process issue for the owner.

## Measurements (SWE-089)

Iteration 1: items checked: 10 TV criteria, 7 lock rows, 7 readiness rows and 55 code-checklist items (40 N/A). Items answered No: TV-S1, TV-S4, TV-S9 and CK-CODE-E1. Findings: 2 Major, 4 Minor. Effort: 48 turns, 65 minutes. Lines reviewed: 953 record lines, 273 lock lines, a 239-line tool delta and 1176 new tool lines (sampled around the cited ranges), and 3844 test lines (by execution and targeted reading).

Iteration 2: six findings re-checked; five Verified (F-01 Major; F-03, F-04, F-05, F-06 Minor), one Open (F-02 Major); 0 disputed, 0 deferred. Items answered No after iteration 2: TV-S1 and TV-S9 (both F-02). Effort for iteration 2: 14 turns, 20 minutes (cumulative 62 turns, 85 minutes in the front matter).

Iteration 3: six findings re-checked, all Closed; one new Minor (F-07), Lien: fix before PDR; 0 disputed, 0 deferred. Items answered No after iteration 3: TV-S9 (owner accreditation pending, decision 114; not a finding). Effort for iteration 3: 32 turns, 45 minutes (cumulative 94 turns, 130 minutes in the front matter).

## Closure

The record stays Open (`record_status: Open`, `date_closed: null`) until the software lead closes it. The verdict is APPROVED (with liens) at iteration 3.

| Finding | Severity | Disposition (iteration 3) | Where verified |
|---|---|---|---|
| F-01 | Major | Closed | TV-001 sections 2, 3, 4 and 9; `fixtures/schema/` at HEAD; reviewer re-run of `python-jsonschema-2026-09-26-r5.sh` on an export of HEAD |
| F-02 | Major | Closed | TV-001 to TV-010 section 4 rows at `400e59d`; `evidence/python-tools-2026-09-26-r5-head.log.txt`; lock line 59; README line 49; reviewer re-run on an export of HEAD with every identity equal to HEAD |
| F-03 | Minor | Closed | TV-010 line 9; README line 34 |
| F-04 | Minor | Closed | TV-010 line 67 against `render_review_figures.py` lines 723 and 724 (blob `6f3018fd`) |
| F-05 | Minor | Closed | `test_validate_docs.py` `UsageErrorTests`; `test_render_deck.py` `SeededFailures`; reviewer re-run on HEAD |
| F-06 | Minor | Closed | TV-002 line 19 |
| F-07 | Minor | Lien: fix before PDR | TV-003 and TV-010 line 6; README lines 27, 34 and 49; lock lines 106 and 112 |

Counts: 0 Major open; 1 Minor lien; 6 Closed; 0 disputed; 0 deferred. Verdict APPROVED (with liens).

Next steps: the software lead closes the record. CM plan section 9.2 step 3 is then completed by writing this record's id, date and result into section 8 of each TV record, which the F-07 edit can carry. The owner records the accreditation decision in section 9 of each record (decision 114, owner action OA-7). For TV-003 and TV-010 that decision names the committed blobs `33ab5a83` and `6f3018fd`. The iteration 2 closure text is kept below for the audit trail.

### Closure as written at iteration 2

The record is Open (`record_status: Open`, `date_closed: null`).

| Finding | Severity | Disposition (iteration 2) | Where verified |
|---|---|---|---|
| F-01 | Major | Closed (Verified) | TV-001 sections 2, 3, 4 and 9; `fixtures/schema/` `keywords.schema.json`, `keywords-invalid.json`, `known-answers.json`; reviewer re-run of `python-jsonschema-2026-09-26.sh` |
| F-02 | Major | Open | not reported fixed; `HEAD` `28e49e6`, product untracked or modified |
| F-03 | Minor | Closed (Verified) | TV-010 line 9; README line 34; lock lines 105, 237 and 255 |
| F-04 | Minor | Closed (Verified) | TV-010 line 62 against `render_review_figures.py` lines 621 and 622 |
| F-05 | Minor | Closed (Verified) | `test_validate_docs.py` `UsageErrorTests`; `test_render_deck.py` `SeededFailures`; TV-003 and TV-008 run 3; reviewer re-runs |
| F-06 | Minor | Closed (Verified) | TV-002 line 19 against `git diff --numstat` |

Counts: 1 Major Open, 0 Minor Open; 5 Verified; 0 disputed; 0 deferred. Verdict stays NEEDS CHANGES while F-02 is Open.

To close: the owner authorizes the commit (package item H17; README owner action 3); Claude commits the tools, tests, fixtures, records and evidence; each TV record's section 3 is re-run on that commit and a result row names it; lock section 1.1 names it. A re-review (iteration 3; 01 section 13 limits `iteration` to 1 to 3) then verifies F-02, sets the verdict, and the software lead closes the record. After closure, CM plan section 9.2 step 3 is completed by writing into section 8 of each TV record: this record's id, date and result. The owner then records the accreditation decision in section 9 of each record.

## Re-issue at iteration 3: delta verification of package item R18 (2026-09-26)

**Scope and independence.** New invocation of the reviewer role (`reviewer:tools`), assigned by the SRR package item R18 (readiness finding R15-F2). It authored no product file and edited none; it wrote only this record. Review baseline: HEAD `b08e55d9829bf674d8713d311725dfb59eab42a5`. The front matter `iteration` stays 3 (01 section 13 limits it to 1 to 3); this is a re-issue of iteration 3 on a delta, not a new full review. The delta is exactly two commits: `git log adcfe09..HEAD` over every `product_files` path and `tools/tests/fixtures/record_state/` lists only `96af250` and `860e84e`, and `git diff --stat adcfe09 HEAD` over the iteration 3 list changes four files (`tools/validate_docs.py` `33ab5a83` to `3aa03681`, `tools/tests/test_validate_docs.py` `4fb5bcc7` to `c70d2c93`, `TV-003-validate-docs.md` `ede04566` to `c6a218c5`, `tools/toolchain.lock.md` `2687fb04` to `0ad60317`); the nine files of `tools/tests/fixtures/record_state/` are new. `product_files` now names the HEAD blobs of all 43 files and `product_files_iteration_3` keeps the list of iteration 3. Search-first: `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` was loaded and queried ("validate_docs record state rule open Major finding latest iteration section") before any manual search; `grep -n` afterwards only pinned lines in files at known paths. Convergence rule (lead SE direction 2026-09-26, charter section 4 item 3): no product content changes in this run; Minor findings are liens due PDR.

**Commands run by the reviewer (repository root, `.venv/bin/python`, HEAD `b08e55d`).**

| Command | Exit | Result |
|---|---|---|
| `git show 96af250`; `git show 860e84e`; `git rev-parse HEAD:<path>` for the four changed files and `git ls-tree -r HEAD tools/tests/fixtures/record_state` | 0 | the diff read in full; blobs as in `product_files` |
| `-m unittest discover -s tools/tests -p test_validate_docs.py -k ValidProjectTests -k InvalidProjectTests -k PeerReviewRecordTests -k UsageErrorTests -k RecordDriftTests -k RecordStateTests` | 0 | 33 tests, OK |
| `-m unittest discover -s tools/tests -p test_tools.py` | 0 | 117 tests, OK (TV-003 run 6 total 150, as recorded) |
| `-m unittest discover -v -s tools/tests -p test_validate_docs.py -k RecordStateTests` | 0 | 8 tests, OK |
| `-m unittest discover -s tools/tests` | 1 | 400 tests, 1 failure: `test_validate_docs.RepositoryTests.test_repository_exit_zero`, the repository-content check (below), as TV-003 run 6 states; no known-answer test fails |
| `tools/validate_docs.py` before this re-issue | 1 | 47 passed, 2 failed: `checklists/hazard-analysis.md` (INSP-008 drift, package item R17, another reviewer's record) and this record (drift of the four changed blobs, which this re-issue closes) |
| `tools/render_risk.py --check --gate SRR --hazards docs/safety/hazards.json` | 0 | 65 risks, 159 candidates, 0 warnings; `register.md` current |
| `tools/traceability.py --report-only` | 0 | 238 requirements, 170 test cases, 0 violations, 3 warnings; `docs/vv/traceability-report.md` and `docs/vv/traceability.json` restored with `git checkout` (lien L-5) |
| Reviewer scratch script over all 30 SRR records at HEAD (outside the repository): the replaced line heuristic, `open_major_findings`, `current_findings`, `approval_errors` and every table line of the latest iteration section holding Major and Open whose first cell is not a finding id | 0 | table below |

**The rule against the code (`tools/validate_docs.py` blob `3aa03681`).**

| Claim (tool header lines 50 to 84; TV-003 purpose 7) | Code | Answer |
|---|---|---|
| (a) `readiness_met` not true fails | `approval_errors` first test | Yes; known answer `test_tools.py` line 1354 (unchanged) |
| (b) `reviewer_verdict` present and not `APPROVED` fails | `approval_errors` second test | Yes; fixture `approved-reviewer-needs-changes.md` (INSP-106) |
| (c) current row with id `finding-<n>` or `F-<nn>`, severity beginning Major and a state cell beginning Open fails | `FINDING_ID_CELL`, `finding_rows`, `current_findings` (later row replaces earlier by `pop` then insert), `open_major_findings` | Yes; fixture `approved-latest-open-major.md` (INSP-102) fails naming finding-3; `approved-superseded-row.md` (INSP-105) passes because its later F-01 row is Closed |
| (d) `findings_open` above zero needs as many distinct open Minor findings shown | `approval_errors` last test, a set of names | Yes; `approved-open-count-unshown.md` (INSP-103) fails, `approved-open-minor.md` (INSP-104) passes |
| Latest iteration section from the first heading naming the highest N, blocks under a lower-iteration heading left out, fenced blocks blanked | `latest_iteration_section` line 741 `next(...)` (first), the heading stack, `_unfenced_lines` | Yes, as TV-003 purpose 7 and the commit message state; the header's word "last" (line 68) is wrong: F-08 |
| Finding table: first header cell begins "Finding", a severity column and a state, disposition, decision or result column | `finding_rows` | Yes; `test_cell_reading` shows a non-finding table (`#` first cell) is ignored |
| Cell reading: markup removed, first alphabetic word, "Closed (was Open)" and "Lien: fix before PDR" not Open, "Minor (was Major)" is Minor | `CELL_MARKUP`, `_leading_word` | Yes; `test_cell_reading` asserts all three and the HTML anchor id cell `<a id="finding-4"></a>F-04 (finding-4)` read as `F-04` |
| NEEDS CHANGES records are not held | rule called only for `verdict: APPROVED` | Yes; `needs-changes-open-major.md` (INSP-107) passes while `open_major_findings` still names finding-1 |
| Historical Major/Open lines no longer hold an APPROVED record | the rule reads no prose | Yes; `approved-historical-lines.md` (INSP-101) carries at least 5 lines the replaced heuristic matched and passes; `test_approved_record_with_historical_major_open_lines_passes` asserts both |

**Both cases exercised.** The known answers seed the failing case (an open Major in the latest iteration, INSP-102) and the case R18 was raised for (historical "Major ... Open" lines with the latest iteration Closed, INSP-101), and `test_exactly_the_seeded_records_fail` requires that exactly INSP-102, 103 and 106 fail among the seven. The pass and fail messages are asserted by fragment (`test_seeded_failure_messages`), and the section bounds (no iteration heading, a lower-iteration block after the latest, a fenced table) by `test_latest_iteration_section_bounds`.

**The 30 SRR records at HEAD `b08e55d` (reviewer scratch script).** Every APPROVED record (24, INSP-002 now among them after `b08e55d`) produces no rule error. The replaced heuristic matched 6 lines in INSP-002, 16 in INSP-003, 4 in INSP-011 and 2 in INSP-016; the new rule finds exactly INSP-003 finding-6, INSP-011 F-01 and F-04, and INSP-016 F-01 and F-02, the five open Major findings of package section 2 row H1, so the tool owner's statement holds. Three table lines of latest sections hold Major and Open outside a finding id cell (INSP-019 checklist item CK-REQ-A8, INSP-029 a render row, INSP-030 a command row); none is a finding row, so none is missed. Two records have no finding row read at all: INSP-028 (APPROVED) and INSP-029 (NEEDS CHANGES), the subject of F-09. Their states are right today: INSP-028 has four Minor liens and no Major, and INSP-029 is not APPROVED.

**TV-003 records the result.** Purpose 7 (line 42) states the rule as the code implements it; section 3 adds `-k RecordStateTests` and the fixture; section 4 run 6 names `HEAD` `96af250`, tool `3aa03681`, `test_validate_docs.py` `c70d2c93`, `test_tools.py` `ed003bad`, fixture tree `b7c20457`, 150 tests, 0 skipped, pass, which equals the HEAD blobs and the reviewer's re-run; the full-directory note gives 400 tests with the one repository-content failure; limitation 7 (line 97) states that finding tables are the only body input; the proposed accreditation extension names blob `3aa03681`. Lock section 1.1, sections 1.2 and 5 and the change history carry the same run. TV-003 line 6 now also says `33ab5a83` was committed in `3de1e2d`, which answers the TV-003 part of F-07; the TV-010 and README parts of F-07 are unchanged, so F-07 stays a lien.

**Checklist answers after the delta.** TV-S1 stays Yes: run 6 names the commit `96af250` that holds what it tested. TV-S3 and TV-S4 are Yes for purpose 7: its known answer carries seeded faults for (b), (c) and (d), and (a) keeps its earlier known answer. TV-S7 is Yes with the F-09 lien on limitation 7. TV-S9 stays No for the owner's accreditation only (decision 114, OA-7). Readiness: R5 Yes (every known-answer module passes; the one full-directory failure is repository content, INSP-008 drift, item R17, not a test of the tool) and R-TV Yes (TV-003 section 3 re-run, exit 0), so `readiness_met` stays true.

**Finding table (current state after the re-issue).**

| Finding | Severity | State | Disposition (re-issue, 2026-09-26) | Location | Description and expected fix |
|---|---|---|---|---|---|
| F-01 | Major | Closed | Closed | TV-001 | unchanged since iteration 3 |
| F-02 | Major | Closed | Closed | TV-001 to TV-010 section 4 | unchanged since iteration 3 |
| F-03 | Minor | Closed | Closed | TV-010, README | unchanged since iteration 3 |
| F-04 | Minor | Closed | Closed | TV-010 limitation 3 | unchanged since iteration 3 |
| F-05 | Minor | Closed | Closed | `UsageErrorTests`, `SeededFailures` | unchanged since iteration 3 |
| F-06 | Minor | Closed | Closed | TV-002 line 19 | unchanged since iteration 3 |
| F-07 | Minor | Lien | Lien: fix before PDR | TV-010 lines 1, 6; README lines 27, 34, 49; lock rows for TV-010 | TV-003 part answered by line 6 at `c6a218c5`; the TV-010 and README parts remain as described in the findings table above |
| <a id="finding-8"></a>F-08 (finding-8) | Minor | Lien | Lien: fix before PDR | `tools/validate_docs.py` line 68 (tool header, "Definitions") | The header says the latest iteration section "runs from the last Markdown heading ... that names the highest iteration"; the code (line 741, `next(...)` over the headings in order) starts at the first such heading, and TV-003 purpose 7, the function docstring (line 730) and the commit message `96af250` all say first. The header is the rule of record, so the tool contradicts its own specification (05 section 9.2 step 1 purpose statement). The code is the intended behaviour, and the difference is not academic: eight SRR records (INSP-002, 003, 005, 006, 013, 014, 017, 018) have two or three headings naming iteration 3, so the two readings select different sections on them. Fix: change "last" to "first" in the header; no code change. Citation: 05 section 9.2 step 1; charter section 11 rule 2 |
| <a id="finding-9"></a>F-09 (finding-9) | Minor | Lien | Lien: fix before PDR | `tools/validate_docs.py` `latest_iteration_section` (lines 727 to 754); TV-003 limitation 7 (line 97); `checklists/fw-b0-tests-test-author.md` (INSP-028) lines 92 to 108 and 212; `checklists/srr-deck.md` (INSP-029) lines 190 to 209 and 232 | A finding table placed before the first heading that names the highest iteration is never read. INSP-028 is a single-iteration record whose only iteration heading is "Closure block (iteration 1)" (line 212) after its finding tables (lines 94 and 103), so its body is read from line 212 and none of its four findings is seen, although the header says a one-iteration record is read whole. INSP-029 keeps its master table under "Findings" (line 190), before "Iteration 3" (line 232), whose block has no finding table. Rule (c) then rests on the front matter checks (b) and (d) alone for such a record, a false-pass path the replaced heuristic did not have. No result is wrong today (both records checked above), and limitation 7 states the mechanism but not its effect or these two records. Fix, at PDR: read the whole body when the highest iteration is 1, and include a section headed "Findings" wherever it stands (later rows still supersede); add a known answer with a finding table before the iteration heading; or, at least, extend TV-003 limitation 7 to name the effect and the records it applies to. Citation: 05 section 9.1 (class B known answer for what is accredited); SWE-088 c |

**Counts.** 9 findings: 2 Major (both Closed), 7 Minor (4 Closed, 3 Lien: F-07, F-08, F-09). Disputed 0. Open Major 0. No finding needs an owner ruling. `findings_open` stays 0 (a lien is not Open).

**Lien table.**

| Finding | Severity | Disposition | Owner | Due | Package carriage |
|---|---|---|---|---|---|
| F-07 | Minor | Lien: fix before PDR | Tool validation author (Claude) | PDR readiness declaration | Routine item (package section 20.1) |
| F-08 | Minor | Lien: fix before PDR | Tool owner (Claude) | PDR readiness declaration | Routine item (package section 20.1) |
| F-09 | Minor | Lien: fix before PDR | Tool owner (Claude); TV-003 author for limitation 7 | PDR readiness declaration | Routine item (package section 20.1) |

**Measurements (SWE-089), this re-issue.** Items re-checked: the rule's nine claims above, TV-S1, S3, S4, S7, S9, readiness R5 and R-TV, and the changed passages of four files; new findings 2 (Minor); closed 0; liens 3; effort 26 turns, 40 minutes (cumulative 120 turns, 170 minutes in the front matter). `findings_minor` is 7 and `findings_lien` 3 in the front matter.

VERDICT (re-issue at iteration 3, independent reviewer): APPROVED (with liens F-07, F-08, F-09)

**Closure.** The record stays Open (`record_status: Open`, `date_closed: null`) until the software lead closes it; the next steps of the section "Closure" above are unchanged, and the owner's accreditation decision for TV-003 (decision 114, OA-7) names blob `3aa03681` if the proposed extension ACC-VALDOCS-001 is adopted.


## Post-SRR-ruling delta (2026-09-26, iteration 3 re-issue 2)

**Scope and independence.** New invocation of the reviewer role (`reviewer:tools`) for SRR package item R16, after the owner approved the SRR on 2026-09-26 (disposition Approved with liens L-1 to L-7; `docs/reviews/SRR/minutes.md`; every key and consent decision ruled as recommended). It authored no product file and edited none; it wrote only this record. Review baseline: HEAD `7c7959f1e06ff0169e2b68b0499022250e4d15ff`. The front matter `iteration` stays 3; this is a second re-issue of iteration 3 on a delta, not a new full review. The delta is exactly one commit: `git log 99ecccb..HEAD` over `docs/cm/tool-validation/` and `tools/` lists only `b2d3538` ("SRR R16 (a): tool accreditation, decision 109 installs and sanity checks ..."), and `git diff --stat 99ecccb HEAD` over those paths changes 17 files: the eleven files of TV-001 to TV-010 and the README, `tools/toolchain.lock.md` (`0ad60317` to `5c04ea9e`), TV-011 to TV-013 (not products of this record; outside decision 114) and two new evidence files `rust-tools-2026-09-26.sh` and `.log.txt`. No tool source, test or fixture changed, so every tool blob, known answer and fixture digest of the first re-issue stands. `product_files` now names the HEAD blobs (45 entries, the two new evidence files added) and `product_files_reissue_1` keeps the list of the first re-issue. Convergence rule (charter section 4 item 3): no product content changes in this run; Minor findings are liens due PDR.

**Search-first compliance.** Deviation, reported so the order can be audited: before `mcp__claude-context__search_code` was loaded, this invocation ran `grep -n` over files already open at known paths (this record's headings and finding rows; `minutes.md` and `decisions-for-owner.md` for decisions 109, 114 and K15; the TV records' section 9 rows; `import validate_docs` in `tools/traceability.py` and `tools/review_trend.py`; lock rows). None was a repository-wide search. The tool was then loaded and queried on `/Users/robinonsay/rust/cwht` ("tool accreditation SRR decision 114 ACC-TRACE-001 validate_docs blob scope"); its hits (TV-002, TV-003, TV-005, TV-006, TV-007 section 9, README line 37, decisions K15) agree with the lines pinned by hand. Later `grep -n` calls only pinned lines in those files.

**Commands run by the reviewer (repository root, `.venv/bin/python`).**

| Command | Exit | Result |
|---|---|---|
| `git log --oneline 99ecccb..HEAD -- docs/cm/tool-validation tools/`; `git diff --stat 99ecccb HEAD -- <product paths>`; `git show b2d3538` (message and the diffs of TV-001 to TV-010, README and lock) | 0 | one commit, `b2d3538`; diffs read in full for the products of this record |
| `git rev-parse HEAD:<path>` for every `product_files` path | 0 | twelve blobs changed (README, TV-001 to TV-010, lock), the rest equal; new list in the front matter |
| `-m unittest discover -s tools/tests` | 1 | 400 tests, 1 failure: `test_validate_docs.RepositoryTests.test_repository_exit_zero`, the repository-content check; every known-answer test passes (as in the first re-issue; no tool, test or fixture changed) |
| `tools/validate_docs.py` before this re-issue | 1 | 41 passed, 9 failed; this record failed on the record drift rule for the twelve changed blobs, which this re-issue closes; the other eight failures are other reviewers' records (drift after the R16 product commits, and one `iteration: 4`) |
| `tools/validate_docs.py` after this re-issue | see closure line below | this record passes |

**Decision 114 against the product.** Ruling: key decision K15, decision 114, recommendation "Accredit each record as proposed (INSP-015 APPROVED)", adopted by the owner's statement recorded verbatim in `minutes.md` line 21.

| Check | Where | Answer |
|---|---|---|
| Each section 9 row states the proposed ACC statement with a date, or a refusal with the reason (CM plan section 9.2 step 3) | TV-001 to TV-010 section 9, new row after the "Pending" row | Yes. Each new row reads "**Accredited** as proposed" and repeats the proposed scope statement of the same section word for word (checked for ACC-PYJS-001, ACC-TRACE-001, ACC-VALDOCS-001, ACC-RMM-001, ACC-COMPL-001, ACC-RISK-001, ACC-TREND-001, ACC-DECK-001, ACC-GIT-001, ACC-FIGS-001), dated 2026-09-26, recorded by Claude transcribing the owner's ruling. The "Pending" rows are kept (history not rewritten) |
| TV-003 carries its proposed extension to blob `3aa03681` | TV-003 section 9 | Yes: purposes 1 to 7 at `3aa0368147b9...` (commit `96af250`) for runs from 2026-09-26 06:11, with the earlier blobs for earlier runs; F-08 and F-09 named as liens riding with the accreditation, as decision 114 names them |
| TV-001 owner action `brew pin python@3.13` not claimed as ruled | TV-001 section 9 | Yes: stated as outside decision 114 and still open (limitation 3; OA-3) |
| Section 8 records this review correctly | TV-001 to TV-010 section 8 | Yes: INSP-015, `reviewer:tools`, checklist revision B, iterations 1 and 2 NEEDS CHANGES, iteration 3 APPROVED with liens, first re-issue at `99ecccb` (record commit `b4abcc5`); F-01 to F-06 Closed; no Major open. TV-003 names F-08 and F-09; the other nine name F-07 only (see F-10 for TV-002 and TV-007) |
| Status lines updated without rewriting history | line 6 of each record | Yes: an "Update 2026-09-26 (SRR decision 114 ...)" sentence is appended; earlier text kept |
| Index and lock say Accredited only for TV-001 to TV-010 | README table rows TV-001 to TV-013; lock section 1 rows python (venv), git, Chromium, `render_deck.py`; section 1.2 rows; section 5; change history row "Tool owner: owner accreditation recorded for TV-001 to TV-010" | Yes; TV-011 to TV-013 read "not covered by SRR decision 114". README owner actions 1 and 2 are marked Done with the decision, earlier text kept |
| Decision 109 rows of the lock (product file of this record, outside TV-001 to TV-010) | lock section 1 rows rustc, rustup, toolchains, rust-code-analysis-cli; change history; `evidence/rust-tools-2026-09-26.*` | Sampled: the four installs recorded are the four decision 109 approves; the optional crate download is recorded as not made; the unapproved rustup self-update to 1.29.1 is disclosed (log line 80, lock finding 7) and left to the owner; the rust-code-analysis-cli sanity check is recorded as fail on the CC counting convention and TV-012 limitation 1 stays open, which the log (lines 382 to 389) supports. The accreditation of these tools belongs to their own TV records (due PDR/CDR), not this review |

**Findings resolved by the rulings.** None was open: F-01 and F-02 (the only Major findings) were Closed at iteration 3 on product fixes, not on rulings. Checklist item TV-S9 ("owner accreditation recorded") changes from No to Yes for TV-001 to TV-010 on decision 114 as recorded in `b2d3538`; `items_no` keeps TV-S9 as the historical answer of iteration 3.

**F-07 after `b2d3538`.** Partly answered: README rows TV-003 and TV-010 now name `3de1e2d` and `96af250`. Still open: TV-010 line 6 keeps "Blob `6f3018fd` is in the working tree, not yet committed" with no update sentence saying it was committed in `3de1e2d`; README line 49 (owner action 3) still says "Open again ... authorize their commit" for blobs that are committed; lock lines 108 and 114 still say "working-tree blob `33ab5a83`" and "working-tree blob `6f3018fd`". F-07 stays "Lien: fix before PDR".

**Finding table (current state after re-issue 2).**

| Finding | Severity | State | Disposition (re-issue 2, 2026-09-26) | Location | Description and expected fix |
|---|---|---|---|---|---|
| F-01 | Major | Closed | Closed | TV-001 | unchanged since iteration 3 |
| F-02 | Major | Closed | Closed | TV-001 to TV-010 section 4 | unchanged since iteration 3 |
| F-03 | Minor | Closed | Closed | TV-010, README | unchanged since iteration 3 |
| F-04 | Minor | Closed | Closed | TV-010 limitation 3 | unchanged since iteration 3 |
| F-05 | Minor | Closed | Closed | `UsageErrorTests`, `SeededFailures` | unchanged since iteration 3 |
| F-06 | Minor | Closed | Closed | TV-002 line 19 | unchanged since iteration 3 |
| F-07 | Minor | Lien | Lien: fix before PDR | TV-010 line 6; README line 49; lock lines 108 and 114 | Partly answered by `b2d3538` (README rows TV-003 and TV-010); the remaining wording is listed above |
| F-08 | Minor | Lien | Lien: fix before PDR | `tools/validate_docs.py` line 68 | unchanged since the first re-issue (tool unchanged); accredited with this lien under decision 114 |
| F-09 | Minor | Lien | Lien: fix before PDR | `tools/validate_docs.py` `latest_iteration_section`; TV-003 limitation 7 | unchanged since the first re-issue (tool unchanged); accredited with this lien under decision 114 |
| <a id="finding-10"></a>F-10 (finding-10) | Minor | Lien | Lien: fix before PDR | TV-002 section 9 (ACC-TRACE-001); TV-007 section 9 (ACC-TREND-001); lock section 1.2 rows `tools/traceability.py` and `tools/review_trend.py`; TV-002 and TV-007 section 8 | ACC-TRACE-001 and ACC-TREND-001 accredit their tools "with `tools/validate_docs.py` at blob `2bedc2a7`". Both tools import `validate_docs` at run time (`tools/traceability.py` line 73, `tools/review_trend.py` line 70), and HEAD has held `validate_docs.py` blob `33ab5a83` since `3de1e2d` and `3aa03681` since `96af250`. A run of either tool at HEAD therefore falls outside its accreditation as recorded, while the lock rows say "Accredited" with no qualifier. The transcription applies decision 114 correctly ("as proposed"); the gap is in the proposed statements, which the reviewer did not flag at iteration 3. Also, section 8 of TV-002 and TV-007 names only F-07 as open, though F-08 and F-09 sit on the module these tools import. Not Major: the changes after `2bedc2a7` add record rules (drift, state) that neither tool calls; the schema and front matter functions they use are covered by TV-003 at `3aa03681`. Fix, at PDR: re-run TV-002 and TV-007 section 3 at a commit holding the current `validate_docs.py` and propose an extension of each ACC statement for the owner (as TV-003 did), or state the qualifier in the lock rows; name F-08 and F-09 in section 8 of both. Citation: CM plan section 9.2 steps 1 and 3; SWE-136 |

**Counts.** 10 findings: 2 Major (both Closed), 8 Minor (4 Closed, 4 Lien: F-07, F-08, F-09, F-10). Disputed 0. Open Major 0. No finding needs an owner ruling. `findings_open` stays 0 (a lien is not Open).

**Lien table.**

| Finding | Severity | Disposition | Owner | Due | Package carriage |
|---|---|---|---|---|---|
| F-07 | Minor | Lien: fix before PDR | Tool validation author (Claude) | PDR readiness declaration | Routine item (package section 20.1) |
| F-08 | Minor | Lien: fix before PDR | Tool owner (Claude) | PDR readiness declaration | Routine item (package section 20.1) |
| F-09 | Minor | Lien: fix before PDR | Tool owner (Claude); TV-003 author for limitation 7 | PDR readiness declaration | Routine item (package section 20.1) |
| F-10 | Minor | Lien: fix before PDR | Tool validation author (Claude); owner for the extended ACC statements | PDR readiness declaration | Routine item (package section 20.1) |

**Measurements (SWE-089), this re-issue.** Items re-checked: the seven decision 114 checks above, F-07, TV-S9, and the changed passages of twelve files; new findings 1 (Minor); closed 0; liens 4; effort 22 turns, 35 minutes (cumulative 142 turns, 205 minutes in the front matter). `findings_minor` is 8 and `findings_lien` 4 in the front matter.

VERDICT (iteration 3 re-issue 2, post-SRR-ruling delta, independent reviewer): APPROVED (with liens F-07, F-08, F-09, F-10)

**Closure.** The record stays Open (`record_status: Open`, `date_closed: null`) until the software lead closes it at the PDR readiness declaration with the four liens.

## SRR close-out delta (2026-09-26, iteration 3 re-issue 3)

**Scope and independence.** New invocation of the reviewer role (`reviewer:tools`, engineering lens) for the SRR close-out, after the owner ruled the twelve close-out items as recommended (`docs/reviews/SRR/minutes.md`, section "Close-out decisions (after the first close-out run)", commit `dd39332`, owner statement "I concur with your recommendations"). It authored no product file, no CR and no TV record, edited no product, and wrote only this section, the verdict paragraph added at the top and the front matter. Review baseline: HEAD `c4b21f8eb1bfd6418c30cee00a87485d70faf4cd` (the product blobs equal those of `3b45ed7`; the five commits after `3b45ed7` touch other reviewers' records only). The front matter `iteration` stays 3; this is a third re-issue of iteration 3 on a delta. Convergence rule (charter section 4 item 3): only open Major findings and ruled work change products; new Minor findings are liens due PDR. Search first: `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` was loaded and queried ("INSP-015 tool validation checklist TV-001 to TV-010 product_commit product_files"; "TV-012 complexity_gate independent review record ACC-COMPLEXITY-001 INSP-015 delta extension conditional"; "CR-001 CS-38 per-file allowance CS-11 failure arm board take target-only straight-line") before any `grep`; later `grep -n` calls only pinned lines in files at known paths. The owner's rustos working tree was not read: every rustos input came from `git -C /Users/robinonsay/rust/rustos archive 2ec64c0` into a scratch layout beside `git archive` of cwht `3b45ed7`. Nothing was downloaded or installed.

**What this delta covers.** (a) The independent review (CM plan section 9.2 step 3) of three tool re-validations the close-out rulings asked for: TV-002 run 5 (`tools/traceability.py` blob `12de3545`, CR-002 step 5, close-out item 5), TV-012 run 2 (`tools/complexity_gate.py` blob `9cdc9195`, CR-005, close-out item 4) and the TV-001 limitation 3 closure (close-out item 12). (b) The lock changes of `37ae576` (picotool `verify` known answer, `sw_gate.sh` `--paths` fix record), of CR-004 (`5792350`, rustos pin `c54d35a` to `2ec64c0`) and of `eb52766` (close-out items 2, 3 and 12). (c) Every other file of `product_files` that changed since `7c7959f`. TV-012 and its tool, test module and fixture are not TV-001 to TV-010, but the close-out record ("the changed tools are re-validated, and their accreditations are extended once the independent review of each validation record is complete") and CR-005 section 5 step 5 assign the review of TV-012 run 2 to this record, so they are added to `product` and `product_files`.

**Delta.** `git log 7c7959f..HEAD` over `product_files` and the added TV-012 files, with each changed blob from `git rev-parse HEAD:<path>`:

| Commit | Product files changed (blob before to after) | Ruling, CR or finding it applies |
|---|---|---|
| `37ae576` | `tools/toolchain.lock.md` (`5c04ea9e` to an intermediate blob) | TC-SW-TOOL-001 run 4 (OA-1, OA-2 performed with the owner, SRR minutes); INSP-016 finding-14 (`sw_gate.sh` one `--paths` per path) |
| `c774851` | `tools/traceability.py` (`0a867523` to `12de3545`); `tools/tests/test_traceability.py` (`d76b0697` to `072bbdcd`) | CR-002 step 5 (CR-002 item 7; 04 rule 7.3.6 as amended at `d992052`; SRR decision 113); close-out item 5 |
| `bf654e6` | `TV-002-traceability.md` (`7f66d0e6` to `bc8abd43`) | close-out items 5 and 7; CR-002 step 5 record |
| `5792350` | `tools/toolchain.lock.md` (section 3 pin, section 1.2 `unsafe_audit.py` row, change history) | CR-004 (close-out item 1) |
| `eb52766` | `TV-001-python-jsonschema.md` (`3bcbd80f` to `110a2692`); `tools/toolchain.lock.md` (to `8ab0218a`); new `evidence/closeout-installs-2026-09-26.log.txt`; `tools/tests/fixtures/picotool/known-answers.json` | close-out items 2, 3 and 12; TC-SW-TOOL-001 run 4 recommendation 5 |
| `e34a27b` | `tools/complexity_gate.py` (`9214fefb` to `9cdc9195`); `tools/tests/test_complexity_gate.py` (`a3b0661b` to `1b603941`); `tools/tests/fixtures/complexity_gate/src/app.rs`, `src/core.rs`, `rca.json` | CR-005 steps 2 and 3 (close-out item 4); CR-001 step 3 |
| `fb22b7a` | `TV-012-complexity-gate.md` (to `e4e042cc`) | CR-005 step 4 (close-out item 4) |

No other file of the re-issue 2 `product_files` changed (README, TV-003 to TV-010, `validate_docs.py`, `render_review_figures.py`, every other test module and fixture, and every earlier evidence file are equal at HEAD). `be270f1` (`tools/requirements.txt` pinned, AL-4) is not a product file; it makes TV-001 limitation 4 stale (F-12).

**Commands run by the reviewer (`.venv/bin/python`, Python 3.13.5; scratch layout `insp015-d3/` in the session scratchpad: `cwht/` is `git archive 3b45ed7`, `rustos/` is `git archive 2ec64c0`).**

| Command | Exit | Result |
|---|---|---|
| `git show` of `37ae576`, `c774851`, `bf654e6`, `5792350`, `eb52766`, `e34a27b`, `fb22b7a` (the product hunks read in full, the lock by `--word-diff`) | 0 | every hunk read; table above |
| TV-002 section 3 on the export: `-p test_traceability.py -k ValidProjectTests -k InvalidProjectTests -k WordListTests -k InspectionRouteTests`; `-p test_traceability_srr_rules.py -k CatalogueTests -k StakeholdersKnownAnswerTests -k AllocationKnownAnswerTests`; `-p test_tools.py` | 0, 0, 0 | 33, 32 and 117 tests, OK, 0 skipped: 182, equal to TV-002 run 5 |
| Mutation check: the export with `tools/traceability.py` replaced by blob `0a867523`, `-k InspectionRouteTests` | 1 | 6 tests, 7 failures (subtests), as TV-002 run 5 states |
| `tools/traceability.py --root <export> --output <scratch>` (plain run, blob `12de3545`) | 0 | 245 requirements, 173 test cases, 0 violations, 2 warnings (`SYS_UNALLOCATED` REQ-SYS-125, REQ-SYS-148); equal to TV-002 section 4.1 R-2. Blob `0a867523` on the same content: exactly 4 `HAZARD_REQ_NOT_TESTED`, REQ-SYS-122, 124, 137, 138 (R-1) |
| TV-012 section 3 on the export: `-v -p test_complexity_gate.py` (`rust-code-analysis-cli 0.0.25` on `PATH`) | 0 | 18 tests, OK, 0 skipped (`AnalyzerEndToEndTests` ran: the analyzer output on the fixture equals `rca.json`, version 0.0.25) |
| Mutation check: the export with `tools/complexity_gate.py` replaced by blob `9214fefb`, `-p test_complexity_gate.py` | 1 | 18 tests, 3 failures and 10 errors, as TV-012 run 2 states |
| Gate row of TV-012 run 2: `rust-code-analysis-cli --metrics --output-format json --paths <cwht>/firmware --paths <rustos>/api --paths <rustos>/firmware/pico2`, then `tools/complexity_gate.py --max 15 --input` | 0, 1 | identical result lines: `FAIL CS-38 .../cwht-app/src/main.rs:30 main CC 4 > 3`; COUNT lines for `build.rs:11 main` (2 real let-else, checked in the source) and `main.rs:30 main`; `ALLOWANCE ... main.rs: 3 (2 CS-11 failure arm(s), 1 CS-19 halt loop(s))`; `MSR-17 functions 52, max_cc 5, mean_cc 1.46, above_12 0, ...`; `FAIL (1 failure(s))`. `firmware/`, the tool and `unsafe_audit.py` are unchanged from `e34a27b` to HEAD |
| `tools/unsafe_audit.py --check --gate SRR`, then `--write --date 2026-09-26`, in the export (rustos defaults `../rustos/api`, `../rustos/firmware/pico2` resolve to the `2ec64c0` export) | 0, 0 | PASS, 37 sites (block 16, fn 11, impl 1, extern 3, attr 6), 0 without SAFETY, 37 unsigned; the regenerated `firmware/unsafe-audit.md` has git blob `18ef484b`, equal to the CR-004 commit and to HEAD |
| `git -C /Users/robinonsay/rust/rustos rev-parse master`, `rev-parse 2ec64c0^`, `diff --shortstat c54d35a 2ec64c0`, count of added `// SAFETY:` lines | 0 | `2ec64c0f15c8...`; parent `c54d35aa8e7f...`; 7 files, 200 insertions, 0 deletions; 36 SAFETY lines (history only; no working-tree file read) |
| Read-only re-observation: `HOMEBREW_NO_AUTO_UPDATE=1 brew list --pinned`; `~/.rustup/settings.toml`; `rustup --version`; `rustup component list --installed --toolchain nightly-2026-08-24`; SHA-256 of the installed nightly channel manifest and of the `python3.13` binary; venv `--version` | 0 | `python@3.13` pinned; `auto_self_update = "disable"`; rustup 1.29.1; `rust-src` and `miri` installed; manifest `0bfdc1de...7690` unchanged; interpreter `a1f6d9dc...8d5bc5`; `Python 3.13.5`: every lock and TV-001 claim of `eb52766` holds |
| `cmp` of `evidence/closeout-installs-2026-09-26.log.txt` with the raw log `closeout-installs-2026-09-26.txt` in the session scratchpad | 0 | identical; the log shows each command and exit 0 (items 3, 12, 2) |
| `shasum -a 256` of `docs/vv/reports/TC-SW-TOOL-001-r4/kat-target-1byte.elf`; `xxd` at offset `0x1002f` of both ELFs; `cmp -l`; JSON load of `picotool/known-answers.json` | 0 | `a669b565...6b73`; `0xab` true, `0x54` altered; exactly one byte (offset 65584); JSON valid; `oa2-verify.txt` shows "First mismatch at 0x1000002f" and exit 245 |
| `-m unittest discover -s tools/tests` (repository) | 1 | 415 tests, 1 failure: `test_validate_docs.RepositoryTests.test_repository_exit_zero`, the repository-content check (this record's drift, closed by this re-issue, and another reviewer's record); no known-answer test fails |
| `tools/validate_docs.py` before this re-issue | 1 | 48 passed, 2 failed: this record (drift of TV-001, TV-002 and the lock) and INSP-021 (`process-04-verification-and-validation.md`, drift of CR-002, another reviewer's record) |
| `tools/render_risk.py --check --gate SRR --hazards docs/safety/hazards.json`; `tools/render_rmm.py --check`; `tools/render_compliance.py --check` | 0, 0, 0 | 65 risks, 0 warnings, `register.md` current; `rmm.md` current; compliance valid and current |

**Checks against the rulings.**

| Change | Ruling or CR | Check | Answer |
|---|---|---|---|
| `c774851` `HAZARD_INSPECTION_NOTE`, Inspection branch of `check_hazard_verification` | CR-002 item 7; 04 rule 7.3.6 (line 248) and section 3 (line 68) as amended at `d992052` | The route needs all three of: a module other than `SW` and `SW-<SUB>` (the software branch returns before it), method Inspection, a live closing case of method Inspection (`closing_cases` filters on the requirement's method) and a note beginning `Inspection accepted per CR-002` (anchored regex with `\b`, so `CR-0021` fails). A missing note and a missing case each give one `HAZARD_REQ_NOT_TESTED` with a distinct message; the Analysis route and the Test route are unchanged | Yes, exactly the rule text. `InspectionRouteTests` asserts exact finding sets and messages, and the old blob fails 7 subtests |
| TV-002 run 5, section 4.1, ACC-TRACE-001 extension | close-out item 5 ("update ... then re-validate and re-accredit it"); minutes "Recorded" line on items 4 and 5 | Identities equal HEAD; 182 tests reproduced; repository runs R-1 and R-2 reproduced; the extension binds `validate_docs.py` `3aa03681`, the blob HEAD runs, which answers F-10 for TV-002 | Yes |
| TV-001 limitation 3 closed | close-out item 12 | `brew pin python@3.13` in the evidence log, exit 0, and re-observed pinned; the interpreter hash is unchanged | Yes |
| Lock: rustup, nightly, Python rows, section 1.4 findings 7 and 8, section 7 rows, Miri sysroot crate row | close-out items 2, 3, 12 | Each row matches the evidence log and the re-observation above; `--no-self-update` kept for later installs; the sysroot crates are recorded with their source and archive plan | Yes |
| Lock: picotool rows, finding 6; `picotool/known-answers.json` | TC-SW-TOOL-001 run 4 (OA-2); run 4 recommendation 5 | The altered-image hash, byte, address and exit status equal the run 4 evidence; the fixture now states the known answer and the device dependency | Yes |
| Lock: `sw_gate.sh` row and finding 10 | INSP-016 finding-14 | Blob `52b9f803` is the `sw_gate.sh` of `37ae576`; the re-validation outside the gate and its result are stated as the evidence shows; the result "FAIL G5 complexity on finding 9" was true at `37ae576` | Yes |
| Lock: section 3 rustos pin, section 1.2 `unsafe_audit.py` row, change history | CR-004 (close-out item 1) | Pin `2ec64c0f15c8...` equals rustos `master`; parent `c54d35a`; 7 files, 200 insertions; the clean-export rule is stated; the regenerated audit list reproduces byte for byte in a clean layout, with `--check --gate SRR` exit 0 | Yes |
| `e34a27b` `complexity_gate.py`: CC = analyzer + one per `let ... else`; CS-38 allowance of CR-001 and CR-005, per function | CR-005 section 1 items 1, 2 and 4; CR-001 section 1 item 2 | The measure is the analyzer's own CC plus the let-else count; admitted arms need an else block that is only `safe_state_halt()`; the halt-loop +1 needs the `#[panic_handler]` function or `safe_state_halt` and a bare `loop` in it; each function is checked against its own items; the file total is printed. The reviewer re-derived the 18 fixture values by hand from `src/app.rs` and `src/core.rs` (sum 80, mean 4.44, three above 12, six target-only above 1, file allowance 4) and they equal section 3 of TV-012 and the tool | Yes. A two-arm `match` failure branch fails closed (TV-012 limitation 7). One narrow under-count path: F-11 |
| TV-012 run 2, gate row, limitation 8 | CR-005 step 4 | Reproduced line for line. `cwht-app::main` CC 4 against 3: the CS-19 main loop has no CS-38 allowance under the ruling as written. That is a gap in the rule (07 CS-38 and CR-005), which INSP-010 finding-21, INSP-018 finding-10 and INSP-016 F-01 carry as Major for the owner's decision; the tool applies the ruled rule correctly, so it is not a defect of this product. If the owner widens the allowance, the tool changes and TV-012 section 7 triggers re-validation | Yes for the tool |
| TV-012 section 9 ACC-COMPLEXITY-001 | close-out item 4 with the minutes "Recorded" line | Scope names blob `9cdc9195`, analyzer 0.0.25, the CR-005 convention and the TV-001 interpreter; TV-012 had no earlier accreditation, and the row says the concurrence is the accreditation decision for this blob | Accepted as recorded; owner confirmation asked by F-13 |

**Accreditation extensions made effective by this review.** This APPROVED delta is the independent review of CM plan section 9.2 step 3 for TV-002 run 5 and TV-012 run 2, on which the close-out record makes each extension depend. From 2026-09-26, the date of this record: (1) the ACC-TRACE-001 extension recorded in TV-002 section 9 is **effective**: `tools/traceability.py` at git blob `12de354531f27afd59e9a18798516d218821d6c0` (commit `c774851`) with `tools/validate_docs.py` at blob `3aa0368147b9af3e6e1546f808afb7aedf7f2226`, under the TV-001 interpreter, purposes 1 to 4 including the rule 7.3.6 Inspection route; (2) ACC-COMPLEXITY-001 as recorded in TV-012 section 9 is **effective**: `tools/complexity_gate.py` at git blob `9cdc91959b06ca3f39142b0afcf85b9a64f719b1` (commit `e34a27b`), purposes 1 to 5, fed by `rust-code-analysis-cli` 0.0.25 under the CR-005 convention, under the TV-001 interpreter, with the liens F-11 and F-13. The tool owner records this result in section 8 of TV-002 and TV-012 (the reviewer does not edit the product). The TV-001 limitation 3 closure changes no accreditation scope (ACC-PYJS-001 is unchanged).

**Findings resolved.** No Major finding was open in this record, so none closes. F-10 is partly answered: the TV-002 extension now binds `validate_docs.py` `3aa03681`; ACC-TREND-001 (TV-007) still binds `2bedc2a7`, and section 8 of TV-002 and TV-007 still names F-07 only, so F-10 stays a lien. F-07, F-08 and F-09 are unchanged (no TV-003, TV-010, README or `validate_docs.py` change).

**Finding table (current state after re-issue 3).**

| Finding | Severity | State | Disposition (re-issue 3, 2026-09-26) | Location | Description and expected fix |
|---|---|---|---|---|---|
| F-01 | Major | Closed | Closed | TV-001 | unchanged since iteration 3 |
| F-02 | Major | Closed | Closed | TV-001 to TV-010 section 4 | unchanged since iteration 3 |
| F-03 | Minor | Closed | Closed | TV-010, README | unchanged since iteration 3 |
| F-04 | Minor | Closed | Closed | TV-010 limitation 3 | unchanged since iteration 3 |
| F-05 | Minor | Closed | Closed | `UsageErrorTests`, `SeededFailures` | unchanged since iteration 3 |
| F-06 | Minor | Closed | Closed | TV-002 line 19 | unchanged since iteration 3 |
| F-07 | Minor | Lien | Lien: fix before PDR | TV-010 line 6; README line 49; lock lines 108 and 114 | unchanged since re-issue 2 |
| F-08 | Minor | Lien | Lien: fix before PDR | `tools/validate_docs.py` line 68 | unchanged (tool unchanged) |
| F-09 | Minor | Lien | Lien: fix before PDR | `tools/validate_docs.py` `latest_iteration_section`; TV-003 limitation 7 | unchanged (tool unchanged) |
| F-10 | Minor | Lien | Lien: fix before PDR | TV-007 section 9 (ACC-TREND-001); lock section 1.2 row `tools/review_trend.py`; TV-002 and TV-007 section 8 | Partly answered by `bf654e6` (the ACC-TRACE-001 extension binds `validate_docs.py` `3aa03681`); the TV-007 part and the section 8 wording remain |
| <a id="finding-11"></a>F-11 (finding-11) | Minor | Lien | Lien: fix before PDR | `tools/complexity_gate.py` `let_else_sites`, the `=` test (`code[k - 1] not in "<>!="`) | The binding `=` is not recognized when it directly follows a `>` that closes a type annotation, so `let Some(x): Option<Vec<u8>>= v else { return 0 };` is not counted (reviewer probe: 0 sites; with a space before `=`: 1). This is an under-count, a false-pass path of CS-17 by one per such statement. It is narrow: gate G1 runs `cargo fmt --check` on the cwht workspace, which writes ` = `, so it cannot occur in `firmware/`; the rustos crates the gate also reads are not formatted by that step. No site exists today (the HEAD gate run above). Fix, at PDR: take the first depth-0 `=` of a `let` statement that is not part of `==` or `=>` as the binding (a pattern or a type cannot hold `<=`, `>=` or `!=`), and add the no-space form to `LetElseTests`; or state the formatting precondition in TV-012 limitation 6. Citation: 05 section 9.1 (class B known answer for what is accredited); SWE-220 |
| <a id="finding-12"></a>F-12 (finding-12) | Minor | Lien | Lien: fix before PDR | `tools/toolchain.lock.md` lines 78 (rust-code-analysis-cli sanity check), 85 (unit-test commands of `traceability.py`), 95 (`complexity_gate.py` known answers), 107 and 125 (section 1.2 rows), 164 (section 1.4 finding 9), 246 and 256 (section 5 rows TV-002 and TV-012); `TV-001-python-jsonschema.md` limitation 4 (line 101) | The lock rows were not updated for `c774851`, `e34a27b` and `fb22b7a`: line 85 omits `-k InspectionRouteTests`, line 95 still describes 9 tests on hand-written analyzer output, lines 78 and 164 still say the end-to-end check fails and the analyzer is not fed for the record, lines 107 and 246 name no blob or extension, and lines 125 and 256 still read "end-to-end check open" and "pending". TV-001 limitation 4 still says `tools/requirements.txt` is not pinned, which `be270f1` did. The TV records are current and are the records of the accreditation; the lock is the summary a reader re-runs from, so a re-run from line 85 would not exercise the Inspection route. Fix, at PDR: bring those rows and limitation 4 up to date with the runs, blobs and effective extensions above (a Log change). Citation: CM plan section 9.2 steps 1 and 5; SWE-081 |
| <a id="finding-13"></a>F-13 (finding-13) | Minor | Lien | Lien: fix before PDR | `TV-012-complexity-gate.md` section 9, last row | The close-out record says the changed tools' "accreditations are extended once the independent review of each validation record is complete". TV-012 had no accreditation to extend (SRR decision 114 covered TV-001 to TV-010; the TV-012 due gate is CDR), and the row states that the concurrence is therefore the accreditation decision for blob `9cdc9195`. That reading is reasonable, because item 4's changed tool is `complexity_gate.py` and the record names items 4 and 5 together, and it is disclosed; but it infers a first accreditation from the word "extended", and accreditation is the owner's decision (CM plan section 9.2 step 3). Fix: the owner confirms, or corrects, the ACC-COMPLEXITY-001 reading at the next owner decision point and the tool owner records it in TV-012 section 9. Until then this record treats the extension as effective as recorded. Citation: CM plan section 9.2 step 3; charter section 2 (approvals transcribed) |

**Counts.** 13 findings: 2 Major (both Closed), 11 Minor (4 Closed, 7 Lien: F-07 to F-13). Disputed 0. Open Major 0. No finding needs an owner ruling to reach APPROVED; F-13 asks for an owner confirmation due PDR. `findings_open` stays 0 (a lien is not Open).

**Lien table.**

| Finding | Severity | Disposition | Owner | Due | Package carriage |
|---|---|---|---|---|---|
| F-07 | Minor | Lien: fix before PDR | Tool validation author (Claude) | PDR readiness declaration | Routine item (package section 20.1) |
| F-08 | Minor | Lien: fix before PDR | Tool owner (Claude) | PDR readiness declaration | Routine item (package section 20.1) |
| F-09 | Minor | Lien: fix before PDR | Tool owner (Claude); TV-003 author for limitation 7 | PDR readiness declaration | Routine item (package section 20.1) |
| F-10 | Minor | Lien: fix before PDR | Tool validation author (Claude); owner for the extended ACC-TREND-001 | PDR readiness declaration | Routine item (package section 20.1) |
| F-11 | Minor | Lien: fix before PDR | Tool owner (Claude) | PDR readiness declaration | Routine item (package section 20.1) |
| F-12 | Minor | Lien: fix before PDR | Tool owner (Claude), lock maintainer | PDR readiness declaration | Routine item (package section 20.1) |
| F-13 | Minor | Lien: fix before PDR | Owner (confirmation); tool owner records it | PDR readiness declaration | Routine item (package section 20.1) |

**Cross-document items (outside this product; for Claude).**

1. TV-002 section 8 and TV-012 section 8: record this review (INSP-015 re-issue 3, date, result APPROVED with liens, the effective extensions) as CM plan section 9.2 step 3 requires; TV-002 and TV-012 status lines then read Reviewed and Accredited for the new blobs. Owner: tool owner.
2. `docs/reviews/SRR/baseline-record.md` section 2c row 28 still names `tools/traceability.py` blob `0a867523` and lists `complexity_gate.py` as "Validated, not accredited"; after this review the accredited blobs are `12de3545` (ACC-TRACE-001 extension) and `9cdc9195` (ACC-COMPLEXITY-001). Owner: baseline record author.
3. CR-005 section 7 proposes Class II and section 6 skips the independent impact review on that basis; CR-004, by the CM plan Class II definition that excludes a change to verification evidence, is proposed Class I because it turns G5 results. CR-005 also changes a G5 result (the complexity outcome) and 07 CS-17 and CS-38, so the same reasoning points to Class I and to an independent review of its impact assessment. The class is Pending owner confirmation in both CRs. Owner: CR-005 author, for the owner.

**Readiness and checklist answers after the delta.** TV-S1 Yes: TV-002 run 5 and TV-012 run 2 each name the commit that holds what they tested, and the reviewer reproduced both on an export. TV-S3 and TV-S4 Yes for the changed purposes: each new rule has a seeded known answer (the Inspection route: one accepted form, four rejected notes, a missing closing case and two excluded modules; CR-005: let-else counted and not counted, admitted and rejected arms, halt-loop credit), and each mutation check fails on the previous blob. TV-S7 Yes, with limitations 6 to 9 of TV-012 and the lien F-11. TV-S9 Yes for TV-001 to TV-010 (decision 114) and, from this review, for the two effective extensions. Readiness R5 Yes (every known-answer module passes; the one full-directory failure is repository content) and R-TV Yes (section 3 of TV-002 and TV-012 re-run, exit 0), so `readiness_met` stays true.

**Measurements (SWE-089), this re-issue.** Items re-checked: seven commits, the changed hunks of thirteen files (five of the re-issue 2 list and eight of the ten added entries), nine ruling checks, the 18 fixture values of TV-012 re-derived by hand, two mutation checks, two repository runs, one gate run, one unsafe-audit regeneration and nine re-observed lock values; new findings 3 (Minor); closed 0; liens 7; effort 40 turns, 60 minutes (cumulative 182 turns, 265 minutes in the front matter). `findings_minor` is 11 and `findings_lien` 7 in the front matter.

VERDICT (iteration 3 re-issue 3, SRR close-out delta, independent reviewer): APPROVED (with liens F-07, F-08, F-09, F-10, F-11, F-12, F-13)

**Closure.** The record stays Open (`record_status: Open`, `date_closed: null`) until the software lead closes it at the PDR readiness declaration with the seven liens.
