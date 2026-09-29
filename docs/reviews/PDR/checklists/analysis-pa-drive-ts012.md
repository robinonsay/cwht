---
# Peer-review record front matter (charter section 5; docs/process/01-lifecycle-and-reviews.md section 13;
# docs/process/08-agent-briefing.md sections 3.4 and 3.5). Independent review of the WP-PDR-21 PA drive window and
# output power analysis for the TS-012 finalists A4 and A5, iteration 1 at freeze commit b705428 (rule C2).
# Checklist applied: docs/templates/peer-review-checklist-analysis.md revision A as on its CR-012 branch
# (cr/CR-012-pdr-checklist-templates at 7784672, blob 0386cc6e; CR-012 Approved 2026-09-28, merge held at the
# section 9 pre-merge check). tools/validate_docs.py requires the checklist field to name a template that exists
# on main, so the field names peer-review-checklist-design revision B and checklist_analysis records the template
# actually applied, as INSP-056 and INSP-083 did. The delta iteration after CR-012 merges switches the field.
# id: the brief assigned no id. INSP-114 is above every id on main (HEAD 6bff79c), on every cr/ branch and in the
# working tree at the time of filing (INSP-111 is the highest in use).
# Filed by the lead SE on 2026-09-28 from the reviewer's own text: the harness refused the reviewer's Write of this
# new file ("Subagents should return findings as text"). Content is verbatim except the id, reassigned from
# INSP-112 to INSP-114 because three parallel reviewers (review:pa-drive-1 among them) each took INSP-112 as the next free id.
# Iteration 2 (2026-09-28, delta on the Major fixes, rule C1): product re-frozen at 9d01aaf (note revision 1, runs
# results/2026-09-28-r1-*); HEAD d1a9a6a changes no product file. CR-012 is still not merged (branch head 7784672 is
# not an ancestor of main), so the checklist field still names the design checklist and checklist_analysis records
# the template actually applied.
# Iteration 3 (2026-09-28, the last iteration under rule C1; delta on the iteration 2 Major finding-9 and the revision 2
# dispositions of the Minor findings): product re-frozen at 5199c5c (note revision 2, runs results/2026-09-28-r2-*);
# HEAD 79795e4 changes no product file (git diff 5199c5c HEAD on the note and hardware/sim/tx-pa is empty). CR-012 is
# still not merged (cr/CR-012-pdr-checklist-templates head 7784672 is not an ancestor of HEAD), so the checklist field
# still names the design checklist and the record verdict stays held at NEEDS CHANGES although the reviewer approves.
id: INSP-114
checklist: peer-review-checklist-design
checklist_revision: B
checklist_analysis: "docs/templates/peer-review-checklist-analysis.md@0386cc6e78da65578b1cce8b2f793cd3db224921 (revision A, CR-012 branch head 7784672)"
checklist_file: docs/reviews/PDR/checklists/analysis-pa-drive-ts012.md
product: docs/design/analysis/pa-drive-ts012.md
# product_commit (iteration 2): 9d01aaf, note revision 1. Every blob below equals git rev-parse 9d01aaf:<path> and
# HEAD:<path> at HEAD d1a9a6a (55 of 55). The unchanged inputs of iteration 1 (digitizers, data/, d1 run) keep the
# blobs listed in product_files_iteration_1. LTspice .log and .raw are not listed; the reviewer's re-run regenerated them.
# product_commit (iteration 3): 5199c5c, note revision 2. Every blob below equals git rev-parse 5199c5c:<path> and
# HEAD:<path> at HEAD 79795e4 (57 of 57). The eight run-folder copies of run_pa.py equal the checker blob. The
# iteration 2 set is kept as product_files_iteration_2. LTspice .log and .raw and the run-folder deck copies are not
# listed; the reviewer's re-run regenerated them (deck SHA-256 equal to the README's).
product_commit: "5199c5c30471b2e5fd0850c314025cf5697c0f56"
product_files: ["docs/design/analysis/pa-drive-ts012.md@028520582657ea7ea07f7fb94c69204afee31816", "hardware/sim/tx-pa/README.md@8ce85567eef13d1c6175b06bc01861976c13f3a1", "hardware/sim/tx-pa/run_pa.py@44769c4579ef473795504837c96eace1159eca4f", "hardware/sim/tx-pa/decks/coax_a4.cir@5802b885c946ddbaf26f1929399a98b286eccdc6", "hardware/sim/tx-pa/decks/coax_a5.cir@785c17e8498708dc6ddb0604fe00db558cc33497", "hardware/sim/tx-pa/decks/drive_a4.cir@c0d899d22801a616e385484cf7fbd07cd703215d", "hardware/sim/tx-pa/decks/drive_a5.cir@cc6fcd5666440675a294ef3536533d4c5303b639", "hardware/sim/tx-pa/decks/drive_a5_pinpad.cir@46ef146b801531ea88b87e7581a150da38974031", "hardware/sim/tx-pa/decks/gva_check.cir@d73282853f2693d3e3ab9b7d3c62251b1c3a4b3f", "hardware/sim/tx-pa/decks/power_a4.cir@0cfc77b39a2c51818c6cfe90cfe2ae3d0d6c5ec3", "hardware/sim/tx-pa/decks/power_a5.cir@dee04c4b71dce34e07ca16f2d384906f90602f4e", "hardware/sim/tx-pa/decks/power_a5_sot.cir@ef988cca771a5da170c0b2019da664faeda5f850", "hardware/sim/tx-pa/decks/tstep_a4.cir@489cf4b245ed317f76f1741aaaa92b7607ba9751", "hardware/sim/tx-pa/decks/tstep_a5.cir@d31c874a59029497b10fe56b4b01d581a1d11a03", "hardware/sim/tx-pa/results/2026-09-28-r1-d2-drive-a5/corners.json@e16de099f665c1703f705724c8b729a41ce4f1a6", "hardware/sim/tx-pa/results/2026-09-28-r1-d2-drive-a5/drive_a5_corners.png@f413b55dc7c8f170e4155be1325ea1ab3d90d8de", "hardware/sim/tx-pa/results/2026-09-28-r1-d2-drive-a5/drive_a5_h3.png@ae9e29b020e09dd89c18c61f9b8f952c48f2bfbe", "hardware/sim/tx-pa/results/2026-09-28-r1-d2-drive-a5/drive_a5_pinload.png@3519f9abeb3660dcc0f85138dd92ceab83768817", "hardware/sim/tx-pa/results/2026-09-28-r1-d2-drive-a5/result.json@57f424a2ca508903438fae0bd075a687413cba19", "hardware/sim/tx-pa/results/2026-09-28-r1-d2-drive-a5/result.md@49c5bbcf9107e7b1b966b38550d8e5e150328cb2", "hardware/sim/tx-pa/results/2026-09-28-r1-d3-drive-a4/corners.json@4764d92a2f690a14ea279c0934717315ce5aef5d", "hardware/sim/tx-pa/results/2026-09-28-r1-d3-drive-a4/drive_a4_corners.png@97c9352a5a341a864d92dc5bd865522d110b2db5", "hardware/sim/tx-pa/results/2026-09-28-r1-d3-drive-a4/drive_a4_h3.png@77c894de0c18ea760ddba4b4272ab7a61176b088", "hardware/sim/tx-pa/results/2026-09-28-r1-d3-drive-a4/drive_a4_pinload.png@cdbdb7855fba28f7dbae15fb51759a2f4dcb73a1", "hardware/sim/tx-pa/results/2026-09-28-r1-d3-drive-a4/result.json@e89b290aba213be478fcf18fffb9ac9218eedfd0", "hardware/sim/tx-pa/results/2026-09-28-r1-d3-drive-a4/result.md@99964aa1b4e07b0c6032a97360af05a38184142e", "hardware/sim/tx-pa/results/2026-09-28-r1-d4-coax-bound/coax_a4_steps.json@d6c01cbb72b21b29bb22e482f334cfeb76f56f30", "hardware/sim/tx-pa/results/2026-09-28-r1-d4-coax-bound/coax_a5_steps.json@8a621d8299fded13353b61e4287b6987e8457b0c", "hardware/sim/tx-pa/results/2026-09-28-r1-d4-coax-bound/coax_length_bound.png@5dfda8967ade6c8d367b458742a0d6f5a644dced", "hardware/sim/tx-pa/results/2026-09-28-r1-d4-coax-bound/result.json@44a06dbf1808d017111cad1fb1589a9d1af0b514", "hardware/sim/tx-pa/results/2026-09-28-r1-d4-coax-bound/result.md@53ce5b6c821b87f040b753cffb939ce7a864a119", "hardware/sim/tx-pa/results/2026-09-28-r1-d5-drive-a5-pinpad/corners.json@0020777a5bf4cee91427ccae9f1e20d652171e6b", "hardware/sim/tx-pa/results/2026-09-28-r1-d5-drive-a5-pinpad/drive_a5_corners.png@82ec5a45d8cdc42b198d46f6e0097239f3f2c47d", "hardware/sim/tx-pa/results/2026-09-28-r1-d5-drive-a5-pinpad/drive_a5_h3.png@f43c84899b10037017e7d054d8336bc6b11da7ea", "hardware/sim/tx-pa/results/2026-09-28-r1-d5-drive-a5-pinpad/drive_a5_pinload.png@840f3496495fffc585e3e566d5b390c9f0b35dd5", "hardware/sim/tx-pa/results/2026-09-28-r1-d5-drive-a5-pinpad/result.json@1c91493df3799a6f74b7e996bd7fcfd579885307", "hardware/sim/tx-pa/results/2026-09-28-r1-d5-drive-a5-pinpad/result.md@b87d192a72562f1f3c8764f5a325482e74b13e78", "hardware/sim/tx-pa/results/2026-09-28-r2-p1-power-a5/power_a5_sma.png@a2a504186ae394bee7fbb1ef49a1e75e34abff50", "hardware/sim/tx-pa/results/2026-09-28-r2-p1-power-a5/power_a5_temperature.png@ee834cd7006fb0180512f3e263c7ce2fbbe360f3", "hardware/sim/tx-pa/results/2026-09-28-r2-p1-power-a5/result.json@2f6480d766ef722f79e7a9668ff8cc56452e6bbf", "hardware/sim/tx-pa/results/2026-09-28-r2-p1-power-a5/result.md@1091838e8312ddb26650ff671aab27f3b98a9692", "hardware/sim/tx-pa/results/2026-09-28-r2-p2-power-a4/power_a4_sma.png@58ef4beada836c170db60a9cc15919836264e915", "hardware/sim/tx-pa/results/2026-09-28-r2-p2-power-a4/power_a4_temperature.png@8b111c8004de776cf379d5325fe5575073423ed1", "hardware/sim/tx-pa/results/2026-09-28-r2-p2-power-a4/result.json@2bddf0fa63235e01624f50c3eb8fff69723029f6", "hardware/sim/tx-pa/results/2026-09-28-r2-p2-power-a4/result.md@f97656dcfa80caec0cb95930f13b7497ddcc8813", "hardware/sim/tx-pa/results/2026-09-28-r2-p3-power-a5-sot/power_a5_sma.png@364796a6467b09b44b6c6e19da7d9578a5677ef8", "hardware/sim/tx-pa/results/2026-09-28-r2-p3-power-a5-sot/power_a5_temperature.png@2f95ff813fa0831808c98fff4e66342cf3c487ce", "hardware/sim/tx-pa/results/2026-09-28-r2-p3-power-a5-sot/result.json@00bbe1b70266d4af6d1f1c9a078660c0b9d135f4", "hardware/sim/tx-pa/results/2026-09-28-r2-p3-power-a5-sot/result.md@9d0e903631ec44c83b2cc15d8bacfaacad84b124", "hardware/sim/tx-pa/results/2026-09-28-r2-s1-summary/a5_closure_margin.png@92019552a3306434054dbac857f1c3865709bf07", "hardware/sim/tx-pa/results/2026-09-28-r2-s1-summary/a5_overdrive_margin.png@c37f5423ce171af6e689cf719868f6aed0bdeb69", "hardware/sim/tx-pa/results/2026-09-28-r2-s1-summary/a5_sot_reading_sensitivity.png@44cf738c1e71299af95636d667f03d3512945e6f", "hardware/sim/tx-pa/results/2026-09-28-r2-s1-summary/pin_at_pa_vs_pack.png@f5f572fee1a36a2c5c76259bdca41562d302c550", "hardware/sim/tx-pa/results/2026-09-28-r2-s1-summary/pout_at_sma_vs_pack.png@a8efe998e1176f13f1b3808ebb3645cce9e14cbb", "hardware/sim/tx-pa/results/2026-09-28-r2-s1-summary/result.json@c91bc6e63a7401a15bb0d90c20fbb30a6d04a640", "hardware/sim/tx-pa/results/2026-09-28-r2-s1-summary/result.md@42de1a1ebe0b49010d1aa01ddf2310977ab72652", "hardware/sim/tx-pa/results/2026-09-28-r2-s1-summary/verdicts.json@6533b76bbcd89d33c83c579976ac2029485af784"]
# product_commit_iteration_2: 9d01aaf5b708c34865327f9946931f6d965c7356 (note revision 1)
product_files_iteration_2: ["docs/design/analysis/pa-drive-ts012.md@0d210c115a32fcc4aa498ee98672816cb11a8ef4", "hardware/sim/tx-pa/README.md@5e6b160c792941cb41f3b2f97d439de5aa9ad6fe", "hardware/sim/tx-pa/run_pa.py@949e1b365e9026304bc58d78f071fbb7d3308a3c", "hardware/sim/tx-pa/decks/coax_a4.cir@5802b885c946ddbaf26f1929399a98b286eccdc6", "hardware/sim/tx-pa/decks/coax_a5.cir@785c17e8498708dc6ddb0604fe00db558cc33497", "hardware/sim/tx-pa/decks/drive_a4.cir@c0d899d22801a616e385484cf7fbd07cd703215d", "hardware/sim/tx-pa/decks/drive_a5.cir@cc6fcd5666440675a294ef3536533d4c5303b639", "hardware/sim/tx-pa/decks/drive_a5_pinpad.cir@46ef146b801531ea88b87e7581a150da38974031", "hardware/sim/tx-pa/decks/gva_check.cir@d73282853f2693d3e3ab9b7d3c62251b1c3a4b3f", "hardware/sim/tx-pa/decks/power_a4.cir@dc2a84ba824c6f16b411002986b2dafa7c4176a5", "hardware/sim/tx-pa/decks/power_a5.cir@451b56e5e29e562d0b681a980857c943ceef71b3", "hardware/sim/tx-pa/decks/power_a5_sot.cir@e0031296377bc3cb99580284c59f6accae755008", "hardware/sim/tx-pa/decks/tstep_a4.cir@489cf4b245ed317f76f1741aaaa92b7607ba9751", "hardware/sim/tx-pa/decks/tstep_a5.cir@d31c874a59029497b10fe56b4b01d581a1d11a03", "hardware/sim/tx-pa/results/2026-09-28-r1-d2-drive-a5/corners.json@e16de099f665c1703f705724c8b729a41ce4f1a6", "hardware/sim/tx-pa/results/2026-09-28-r1-d2-drive-a5/drive_a5_corners.png@f413b55dc7c8f170e4155be1325ea1ab3d90d8de", "hardware/sim/tx-pa/results/2026-09-28-r1-d2-drive-a5/drive_a5_h3.png@ae9e29b020e09dd89c18c61f9b8f952c48f2bfbe", "hardware/sim/tx-pa/results/2026-09-28-r1-d2-drive-a5/drive_a5_pinload.png@3519f9abeb3660dcc0f85138dd92ceab83768817", "hardware/sim/tx-pa/results/2026-09-28-r1-d2-drive-a5/result.json@581eefb24271a2d97a874c1c4693e75651762d03", "hardware/sim/tx-pa/results/2026-09-28-r1-d2-drive-a5/result.md@e2a2956cc6957eec4aeaba5c49d3ced210ecadf0", "hardware/sim/tx-pa/results/2026-09-28-r1-d3-drive-a4/corners.json@4764d92a2f690a14ea279c0934717315ce5aef5d", "hardware/sim/tx-pa/results/2026-09-28-r1-d3-drive-a4/drive_a4_corners.png@97c9352a5a341a864d92dc5bd865522d110b2db5", "hardware/sim/tx-pa/results/2026-09-28-r1-d3-drive-a4/drive_a4_h3.png@77c894de0c18ea760ddba4b4272ab7a61176b088", "hardware/sim/tx-pa/results/2026-09-28-r1-d3-drive-a4/drive_a4_pinload.png@cdbdb7855fba28f7dbae15fb51759a2f4dcb73a1", "hardware/sim/tx-pa/results/2026-09-28-r1-d3-drive-a4/result.json@83a3334d709317e31fa8e876bff9623230b34991", "hardware/sim/tx-pa/results/2026-09-28-r1-d3-drive-a4/result.md@99964aa1b4e07b0c6032a97360af05a38184142e", "hardware/sim/tx-pa/results/2026-09-28-r1-d4-coax-bound/coax_a4_steps.json@d6c01cbb72b21b29bb22e482f334cfeb76f56f30", "hardware/sim/tx-pa/results/2026-09-28-r1-d4-coax-bound/coax_a5_steps.json@8a621d8299fded13353b61e4287b6987e8457b0c", "hardware/sim/tx-pa/results/2026-09-28-r1-d4-coax-bound/coax_length_bound.png@5dfda8967ade6c8d367b458742a0d6f5a644dced", "hardware/sim/tx-pa/results/2026-09-28-r1-d4-coax-bound/result.json@fda51fc8505c6268d12e68d71be633f4a0d7ea28", "hardware/sim/tx-pa/results/2026-09-28-r1-d4-coax-bound/result.md@53ce5b6c821b87f040b753cffb939ce7a864a119", "hardware/sim/tx-pa/results/2026-09-28-r1-d5-drive-a5-pinpad/corners.json@0020777a5bf4cee91427ccae9f1e20d652171e6b", "hardware/sim/tx-pa/results/2026-09-28-r1-d5-drive-a5-pinpad/drive_a5_corners.png@82ec5a45d8cdc42b198d46f6e0097239f3f2c47d", "hardware/sim/tx-pa/results/2026-09-28-r1-d5-drive-a5-pinpad/drive_a5_h3.png@f43c84899b10037017e7d054d8336bc6b11da7ea", "hardware/sim/tx-pa/results/2026-09-28-r1-d5-drive-a5-pinpad/drive_a5_pinload.png@840f3496495fffc585e3e566d5b390c9f0b35dd5", "hardware/sim/tx-pa/results/2026-09-28-r1-d5-drive-a5-pinpad/result.json@41a71d4d1b037d9e6b58d4dc7e6693640ea395a0", "hardware/sim/tx-pa/results/2026-09-28-r1-d5-drive-a5-pinpad/result.md@147ad6a43a36815f97ba4eaf806fbb0be0dccf13", "hardware/sim/tx-pa/results/2026-09-28-r1-p1-power-a5/power_a5_sma.png@e2f91b0d384a70c4ca57a65605d9f6e8a302b9d0", "hardware/sim/tx-pa/results/2026-09-28-r1-p1-power-a5/power_a5_temperature.png@a543341b7e65aef24a3e8e935279891c5fda5147", "hardware/sim/tx-pa/results/2026-09-28-r1-p1-power-a5/result.json@e34028ab8e03052ead5b945e4722c4246a40621a", "hardware/sim/tx-pa/results/2026-09-28-r1-p1-power-a5/result.md@1832058eaf65e867b7f562dd9af8fbf120e23896", "hardware/sim/tx-pa/results/2026-09-28-r1-p2-power-a4/power_a4_sma.png@c7b439a2cacbc9a73dcc13cc8f083730d589af68", "hardware/sim/tx-pa/results/2026-09-28-r1-p2-power-a4/power_a4_temperature.png@ca2b01e6adb5bcaf0e1cc3487405eaa77ae369f6", "hardware/sim/tx-pa/results/2026-09-28-r1-p2-power-a4/result.json@c389caa2ee49ce6cebdcd8cdb33210b6bbd0c307", "hardware/sim/tx-pa/results/2026-09-28-r1-p2-power-a4/result.md@aea7c8759bb61ff034070f98602424108cba1f58", "hardware/sim/tx-pa/results/2026-09-28-r1-p3-power-a5-sot/power_a5_sma.png@158e912cdd754349ed5ffcde07e4700ac238facc", "hardware/sim/tx-pa/results/2026-09-28-r1-p3-power-a5-sot/power_a5_temperature.png@5c2d4fb17331834594fd5e044523243d95ea1d5a", "hardware/sim/tx-pa/results/2026-09-28-r1-p3-power-a5-sot/result.json@97479f3f49d03f7becfcfaf32a041e314c99fd17", "hardware/sim/tx-pa/results/2026-09-28-r1-p3-power-a5-sot/result.md@3267881cf34212c12b1c1f6233c98b677656a89c", "hardware/sim/tx-pa/results/2026-09-28-r1-s1-summary/a5_closure_margin.png@9c3995b3eee8aaa429663d3a9f97797e2c47b0f1", "hardware/sim/tx-pa/results/2026-09-28-r1-s1-summary/a5_overdrive_margin.png@49c2803191d4f9b28d8dea97ad2fe529f0641951", "hardware/sim/tx-pa/results/2026-09-28-r1-s1-summary/pin_at_pa_vs_pack.png@b579566241c22184d5389bf7291e98bbafd2c408", "hardware/sim/tx-pa/results/2026-09-28-r1-s1-summary/pout_at_sma_vs_pack.png@8058cea2ef28c0694d1cd27a1235094763cf8f89", "hardware/sim/tx-pa/results/2026-09-28-r1-s1-summary/result.json@85512f7ffde389f3096cb3c76cdc74c10b528ec9", "hardware/sim/tx-pa/results/2026-09-28-r1-s1-summary/result.md@4b3f9d480369f647edc1a1e13fe9297100f1db16"]
product_files_iteration_1: ["docs/design/analysis/pa-drive-ts012.md@ecffcb3ff90eb115cf6204a9a3f835756405f0ee", "hardware/sim/tx-pa/README.md@4c44ad9fdc0b6feb57453d8571fbe04bab0e1aab", "hardware/sim/tx-pa/run_pa.py@acbe1457a7a26cf4980afa8e3222350f34e1248a", "hardware/sim/tx-pa/digitize_ra07.py@85c2e226def52682a1d5c622fcb9d57bc31f3584", "hardware/sim/tx-pa/digitize_aft05.py@94bb20e56436d39f423426284fca7ad4a1b3bafb", "hardware/sim/tx-pa/decks/drive_a4.cir@7d06ec7a61b84fb82365a34db0232488e6a8e6e8", "hardware/sim/tx-pa/decks/drive_a5.cir@5cce872bfaec25e26da07e0948ecd96096d44f84", "hardware/sim/tx-pa/decks/gva_check.cir@d73282853f2693d3e3ab9b7d3c62251b1c3a4b3f", "hardware/sim/tx-pa/decks/power_a4.cir@9d935a12cc9d5888de481d1eecc3c790d8a1fd87", "hardware/sim/tx-pa/decks/power_a5.cir@ea5b3ed0e465e4f65d5b82a5ed9477b580a09f07", "hardware/sim/tx-pa/decks/power_a5_sot.cir@515c59356eca9bbad229f3b4410dfd99f44d806d", "hardware/sim/tx-pa/data/aft05_pout_vs_pin_135.csv@c42891a3e844844c433791d7d6fc15e5a982eb29", "hardware/sim/tx-pa/data/aft05_pout_vs_pin_155.csv@c868b3f90db74c4b165aec3c7a578c5af64207c3", "hardware/sim/tx-pa/data/aft05_pout_vs_pin_overlay.png@ef68932c8fcbf2b57f01b30c5ac8b357be9ea7dd", "hardware/sim/tx-pa/data/ra07_pout_vs_pin_135.csv@fa9a9268175ef36e4a5a1315c8ef214216f72009", "hardware/sim/tx-pa/data/ra07_pout_vs_pin_135_overlay.png@c47e16290f9162ecde031ce910fc02f9cd0603c7", "hardware/sim/tx-pa/data/ra07_pout_vs_pin_155.csv@940931a7e169483373ef2155022fa8a15fa55e81", "hardware/sim/tx-pa/data/ra07_pout_vs_pin_155_overlay.png@f12256f8e2d7abb28ac6d6cdeb40ba3ba93bc3a1", "hardware/sim/tx-pa/data/ra07_pout_vs_vdd_135.csv@653ad373080ec2e92f53cbca27072afb6e32963b", "hardware/sim/tx-pa/data/ra07_pout_vs_vdd_135_overlay.png@9feb9fcc54abc91cfb15a39bfb12c68b905eaf80", "hardware/sim/tx-pa/data/ra07_pout_vs_vdd_155.csv@a92785b7f643fe012b431bf655f825f9ff8ff967", "hardware/sim/tx-pa/data/ra07_pout_vs_vdd_155_overlay.png@b96503dd4aab6c4e489f76a664edffde4f3ad5ed", "hardware/sim/tx-pa/data/ra07_pout_vs_vgg_135.csv@9a877b511ffa2e9d0a9a31d53502b80f59cee9c9", "hardware/sim/tx-pa/data/ra07_pout_vs_vgg_135_overlay.png@5033bbe003a3296837a5a1ca313edadb0a11c2ad", "hardware/sim/tx-pa/data/ra07_pout_vs_vgg_155.csv@83a9f93a85484025d2f3217a11b6873f414ced4b", "hardware/sim/tx-pa/data/ra07_pout_vs_vgg_155_overlay.png@0602ee3e1a6ad2fcbd9475d1aec36d88772704fe", "hardware/sim/tx-pa/results/2026-09-28-d1-gva-model/gva_compression.png@e96846e2cb3c2ba197997702d8532427e15372a5", "hardware/sim/tx-pa/results/2026-09-28-d1-gva-model/result.json@db04d4e5c43dc4aa776109be6f65396464b654c6", "hardware/sim/tx-pa/results/2026-09-28-d2-drive-a5/drive_a5_corners.png@9934bf5fd06dd730c50b1627f5bc8c9a79b68b96", "hardware/sim/tx-pa/results/2026-09-28-d2-drive-a5/drive_a5_h3.png@04ad79329eeaca3126e5f2391b2808dc5ad24cc3", "hardware/sim/tx-pa/results/2026-09-28-d2-drive-a5/result.json@6d50c1202e08326ad3869ba5f10602237ffa4697", "hardware/sim/tx-pa/results/2026-09-28-d3-drive-a4/drive_a4_corners.png@353196998dd4e12d418da3b1bf1b9cdf9917cdf3", "hardware/sim/tx-pa/results/2026-09-28-d3-drive-a4/drive_a4_h3.png@15e738c62d1d884631256faa8ba4228ceee72512", "hardware/sim/tx-pa/results/2026-09-28-d3-drive-a4/result.json@fa99e6e09a69f031fce50a8068cb7bc6f6b51e08", "hardware/sim/tx-pa/results/2026-09-28-p1-power-a5/power_a5_sma.png@6eb740e79cb257c7c85157d4cb7427d12869065d", "hardware/sim/tx-pa/results/2026-09-28-p1-power-a5/result.json@9cd9adc302cd808108fdd2c797159b6597484f74", "hardware/sim/tx-pa/results/2026-09-28-p2-power-a4/power_a4_sma.png@fef34efa40494ad77ead4f8b33e75d6ab6cdc68a", "hardware/sim/tx-pa/results/2026-09-28-p2-power-a4/result.json@0eb8087763665980ef64246d151a615373925034", "hardware/sim/tx-pa/results/2026-09-28-p3-power-a5-sot/power_a5_sma.png@09795d539d3e5112a1819fcfb8d91efda50c9f60", "hardware/sim/tx-pa/results/2026-09-28-p3-power-a5-sot/result.json@3836ce85522bd78f126db448ab2a40fabe4e8ece", "hardware/sim/tx-pa/results/2026-09-28-s1-summary/pin_at_pa_vs_pack.png@427733e5ce69f8304f21f18c1a10764bc971be6f", "hardware/sim/tx-pa/results/2026-09-28-s1-summary/pout_at_sma_vs_pack.png@d5735481713975d86ac1f74f460af30a8ca3d27b", "hardware/sim/tx-pa/results/2026-09-28-s1-summary/result.json@2dcb45ab6935bf6ac60e2a8b55153d9652014187"]
analysis_kind: [simulation-deck, cascade, worst-case]
product_size: iteration 3, 1 note (520 lines, revision 2); 10 LTspice decks (810 + 810 + 810 drive corners, 435 + 435 coax-length steps, 15 + 15 time-step corners, 11664 + 13122 + 11664 power corners); 1 checker; 23 result plots (11 new or changed); iteration 2, 1 note (411 lines, revision 1); 10 LTspice decks (810 + 810 + 810 drive corners, 435 + 435 coax-length steps, 15 + 15 time-step corners, 4536 + 10206 + 4536 power corners); 1 checker; 20 result plots; iteration 1, 1 note; 6 LTspice decks (270 + 270 drive corners, 648 + 1458 + 648 power corners, 75 model-check steps); 1 checker; 2 digitizers; 8 digitized curves; 17 renders (10 result plots, 7 digitizer overlays); 66 input rows
tools_used: ["LTspice 26.0.2 for MacOS through tools/ltspice-batch.sh blob 88b71475 (TV-014, Accredited, ACC-LTSPICE-001)", "venv Python 3.13.5 (TV-001 accredits the interpreter); numpy 2.5.3, scipy 1.18.1, spicelib 1.6.3, matplotlib 3.11.2 (class B entries of tools/toolchain.lock.md section 2 without a TV record); no TV record covers hardware/sim/tx-pa/*.py: developer evidence per 05 section 9.1, as the note says"]
# values_proposed: the note proposes no TBR value and no TPM current best estimate; section 7 C4 and C5 put
# requirement-delta choices to the owner through TS-012, not values.
values_proposed: []
# renders_inspected: iteration 3 (the 11 revision 2 result plots of runs r2-p1, r2-p2, r2-p3 and r2-s1; the drive
# plots of d2 to d5 are unchanged blobs, opened at iteration 2); iteration 2 opened 20, iteration 1 opened 17
renders_inspected: 11
sprint: PDR-prep
author_agent: "author:WP-PDR-21 tx-pa (Claude as analysis author, TS-012 discriminating analyses; commit b705428; revision 1 at 9d01aaf)"
reviewer_agent: "reviewer:WP-PDR-21-analysis-pa-drive-iter1 (independent; authored no part of the note, decks, checker, digitizers or TS-012); iteration 2 by reviewer:WP-PDR-21-analysis-pa-drive-iter2 (independent; authored no part of the note, its revision 1, the decks, the checker, the digitizers or TS-012); iteration 3 by reviewer:WP-PDR-21-analysis-pa-drive-iter3 (independent; authored no part of the note, its revisions 1 and 2, the decks, the checker, the digitizers or TS-012)"
# criticality: a hardware-only transmit analysis; it sets no value of a 07 section 14.1 component
criticality: neither
assurance_required: false
assurance_reviewer_agent: none
iteration: 3
readiness_met: true
# reviewer_verdict (iteration 3): APPROVED. finding-9 (Major) is Verified at 5199c5c, with finding-1 and finding-2
# Verified at iteration 2, so no Major finding is open. The revision 2 dispositions of the Minor findings 3 to 8 and 10
# are Verified too. One new Minor finding (finding-11, two wording items introduced by revision 2) is Open as a lien
# for the next revision; it changes no reported result.
reviewer_verdict: APPROVED
assurance_verdict: not-required
# verdict (iteration 3): held at NEEDS CHANGES only because the applied analysis template is still only on cr/CR-012
# (branch head 7784672, not merged; lead SE convention of 2026-09-27, INSP-083). The reviewer verdict is APPROVED;
# no Major finding is open and nothing escalates to the owner under rule C1.
verdict: NEEDS CHANGES
findings_major: 3
findings_minor: 8
findings_open: 1
findings_fixed: 0
findings_verified: 10
findings_deferred: 0
assurance_tasks_applied: []
deferred_rids: []
# items_no (iteration 3): the only item that stays No, on the open Minor finding-11
items_no: [CK-ANA-D2]
items_no_iteration_2: [CK-ANA-A1, CK-ANA-A2, CK-ANA-A5, CK-ANA-A6, CK-ANA-B1, CK-ANA-B6, CK-ANA-D2, CK-ANA-E2, CK-ANA-E3, CK-ANA-E4, CK-ANA-F4, CK-ANA-G7-2, CK-ANA-H1, CK-ANA-H2, CK-ANA-I2]
items_no_iteration_1: [CK-ANA-A1, CK-ANA-A2, CK-ANA-A5, CK-ANA-A6, CK-ANA-B1, CK-ANA-B2, CK-ANA-B6, CK-ANA-D2, CK-ANA-E2, CK-ANA-E3, CK-ANA-E4, CK-ANA-F1, CK-ANA-F4, CK-ANA-G1-3, CK-ANA-G7-2, CK-ANA-H1, CK-ANA-H2, CK-ANA-I2]
# effort: cumulative (iteration 1: 70 turns, 95 minutes; iteration 2: 50 turns, 85 minutes; iteration 3: 55 turns,
# 90 minutes, about 35 of them waiting on the shared LTspice lock)
effort_turns: 175
effort_minutes: 270
record_status: Open
date: 2026-09-28
date_closed: null
---

# Peer review record: PA drive window and output power, TS-012 finalists A4 and A5 (INSP-114, iteration 1)

**Product:** `docs/design/analysis/pa-drive-ts012.md` (`ecffcb3f`) with `hardware/sim/tx-pa/` (README `4c44ad9f`; checker `run_pa.py` `acbe1457`; digitizers `digitize_ra07.py` `85c2e226` and `digitize_aft05.py` `94bb20e5`; six decks; eight digitized curves with overlays; seven result runs) at freeze commit `b705428` (rule C2). Every blob equals `git rev-parse HEAD:<path>` at `HEAD` `6bff79c`. No product blob lives on a `cr/` branch.

**Checklist:** the item set of `peer-review-checklist-analysis.md` revision A (CR-012 branch, blob `0386cc6e`; front matter comment). `analysis_kind` simulation-deck, cascade (the transmit line-up drive) and worst-case (extreme-value corners): sections A to F, G1, G5, G7, H and I apply. G2, G3, G4 and G6 are N/A (not a budget, thermal, RF exposure or timing analysis); J is N/A (criticality neither).

**Acceptance criteria (rule C7, every case the governing texts enumerate):**
- REQ-SYS-012 (`docs/requirements/sys/requirements.json`): "The transceiver shall hold its 5 W step within +/-1 dB (TBR) into 50 ohm over its transmit range at 6.4-8.4 V pack." Bounds 3.972 and 6.295 W. Verification note: pre-build supporting simulation "over 6.4 to 8.4 V at 144, 146 and 148 MHz".
- REQ-SYS-008: transmit carrier 144.0012 to 147.9988 MHz (TBR), so the band edges and centre (144, 146, 148 MHz in the decks).
- REQ-SYS-114: "The transceiver shall meet its requirements at ambient temperatures from -10 C to +45 C (TBR)", which conditions REQ-SYS-012.
- TS-012 revision 4 section 7.3, WP-PDR-21 pre-order drive check: "pass: module input 10 to 30 mW at every corner (144 to 148 MHz, 25 and 50 ohm source, GVA gain 22.5 and 25 dB), 3f at the GVA input at least 25 dB below the fundamental."
- RA07M1317M datasheet (Jun. 2019, page 2): Pin 30 mW maximum rating; stability "VDD=4.0/7.2/9.2V, Pin=10/20/30mW, Pout<=8W (VGG control), Load VSWR=4:1"; Pout 10 W maximum at VGG 3.5 V or less; VGG 4 V maximum at VDD 7.2 V or less.
- GVA-84+ Rev. F absolute maximum input +13 dBm.
- TPM-015 (carrier-power: PDR "within +/-1 dB by analysis ... over the pack voltage range"; red threshold includes "the 5 W step unreachable at the cutoff voltage") and TPM-004 (pa-efficiency, planned 60 %, red below 55 %), both in the `mop_ids` of REQ-SYS-012.

**Search rule.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` (the PA drive analysis, the INSP id register) preceded every `grep` and `find`; `grep` only pinned lines in TS-012, INSP-110, 04 and the requirement file. The rustos tree was not read.

**Sources re-read by the reviewer (2026-09-28).** The four vendor PDFs the note cites, from the session cache, each matching the SHA-256 prefix in the block README: Mitsubishi RA07M1317M Jun. 2019 (`5a847a09`), https://www.mitsubishielectric.com/semiconductors/hf/products/datasheet/ra07m1317m.pdf; NXP AFT05MS004N Rev. 0 (`84cd9fae`), https://www.nxp.com/docs/en/data-sheet/AFT05MS004N.pdf; Mini-Circuits GVA-84+ Rev. F (`49daf1cb`), https://www.minicircuits.com/pdfs/GVA-84+.pdf; Skyworks Si5351A/B/C-B Rev. 1.3 (`f3bc5285`), https://www.skyworksinc.com/-/media/Skyworks/SL/documents/public/data-sheets/Si5351-B.pdf. RA07M1317M pages 3 to 5 were rendered at 110 dpi and read beside the overlays.

## Findings (iteration 1)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | reviewer | Major | CK-ANA-G1-3, B2, E3, A6 | decks `drive_a5.cir` and `drive_a4.cir` lines `Rsrc vs clk`, `Ctap clk 0 5p`, `C1 clk 0 18p`; note sections 2, 4.2 ("Overdrive is designed out"), 5 (a), 4.7; TS-012 section 8.1 block diagram | The Si5351-to-drive-LPF interface is not modelled as designed, and the drive result that decides the A5 window rests on it. (i) The decks put the LPF's 18 pF input capacitor and the 5 pF tap directly on the CLK1 pin, 23 pF in all, against the Si5351 "Load Capacitance CL ... 15 pF" maximum (Rev. 1.3 Table 7); the edge and duty values the source model takes from Table 7 are specified at CL 5 pF inside that limit, so every reported drive corner uses the source outside its specified load range. (ii) TS-012 section 8.1 puts the Si5351 on the Adafruit 2045 module and the drive LPF on the separate RF board, so a board-to-board interconnect lies between them; the note does not model or mention it. Reviewer estimate (a frequency-domain model that reproduces the note's 270 A5 corners within 0.02 dB, with a lossless 50 ohm line, velocity factor 0.66, the tap at the pin): the A5 drive range becomes 5.8 to 30.5 mW with 5 cm of line (1 corner above 30 mW), 5.7 to 32.7 mW with 10 cm (12 corners above) and 5.7 to 36.2 mW with 15 cm (18 corners above); over any line length the highest corner spans 29.6 to 48.7 mW. The note's highest corner, 29.5 mW, is 0.07 dB under the 30 mW maximum rating, yet sections 4.2 and 5 (a) state "Overdrive is designed out" and the author summary "Overdrive never happens": that margin is far below the uncertainty of this unmodelled term and of the estimated source terms (25 ohm corner, 0.5 ns edge, VDDO +/-3 %). Fix: state the designed interface (placement, line or wire length and impedance, where the tap sits) and model it, or bound it over the plausible lengths; keep the CLK1 load within 15 pF (for example an L-first drive filter or a series element at the pin) or state the out-of-rating use and send it to the TS-012 author as a design request (A6); report the overdrive margin with its uncertainty and withdraw "designed out" unless shown. The select-on-test route (C1) absorbs a fixed line in the build reading, which the note can say once the interface is stated | Open | Pending | |
| <a id="finding-2"></a>finding-2 | reviewer | Major | CK-ANA-F1, A5, G7-2, B6, E3 | note sections 2 ("Corners"), 3, 5 (b), 6, 7 C2 and C3; decks `power_a5.cir`, `power_a4.cir` | REQ-SYS-114 makes REQ-SYS-012 hold from -10 C to +45 C ambient; the note has no temperature case, and it does not state that every curve and value it uses is at Tcase or TA 25 C (both PA datasheets and the GVA-84+ and Si5351 tables), nor in which direction temperature moves the result. The terms that move with temperature are not small against the closure margin the note reports: the drain feed includes two cells whose resistance rises in the cold (TS-012 section 7.3 takes 0.04 to 0.06 ohm at room temperature, estimate), and the module sits on a sink whose flange TS-012 estimates at 70 to 99 C at the 45 C corner, while the RA07M1317M output data are all at Tcase 25 C. The closure claim of section 5 (b), "The lowest corner passes (4.31 to 4.45 W) with two TS-012 items", has +0.35 dB of margin at 4.31 W (+0.23 dB at the VGG the revision-4 clamp can reach, finding-3), and the note does not compare that margin with its uncertainty (graph reads about +/-0.1 W, the separable module model, the output-loss allocation). The GVA-84+ gain drift is negligible (0.0004 dB/C at 0.1 GHz, Rev. F), so the open terms are the cell resistance and the module output at temperature. Fix: add a cold (-10 C) and a hot (+45 C ambient, with the WP-PDR-28 flange temperature) corner with sourced or labelled-estimate values for the cell resistance and the module output, or state the omission as a limitation with its direction and carry it into the C2 and C3 pass criteria; state the uncertainty of the (b) margin | Open | Pending | |
| <a id="finding-3"></a>finding-3 | reviewer | Minor | CK-ANA-A5, B1 | note section 3 row "VGG at the ALC top: 3.5 V, or 3.08 V"; sections 4.4, 5 (b), 6 item 2, 7 C3; `run_pa.py` `A5_VGG_CLAMP_LO`, `ivgg` values | The revision-4 clamp puts VGG at 3.08 to 3.46 V (nominal 5.0 x 0.654 = 3.27 V), so the "3.5 V" level that the nominal and highest corners and the closure figure 4.31 W use is above what the design can reach. Reviewer re-solve of the same model: nominal at 6.4 V 4.70 W at 3.27 V (4.87 W reported at 3.5 V, -0.15 dB); lowest corner with the feed at most 0.35 ohm 4.28 W at 3.46 V and 4.19 W at 3.3 V (C3's "at least 3.3 V"), against 4.31 W reported. No verdict changes, but C3's pass figure is at a VGG the design cannot reach. Also, limitation 2 gives a direction only for the VGG-at-low-VDD term; the drive and VGG interaction at the lowest corner (Pin 6 mW with VGG 3.08 V, a less saturated module, where Pin sensitivity is larger than the 0.28 dB the VGG 3.5 V curve shows) may be optimistic, and the note should say so. Fix: use the clamp's nominal and maximum for the nominal and highest corners, state C3 at the VGG it requires, and state the interaction's direction | Open | Pending | |
| <a id="finding-4"></a>finding-4 | reviewer | Minor | CK-ANA-F4, E3, A6 | note section 4.2 "Select-on-test pad", its pad table; section 7 C1; `run_pa.py` `SOT_STEP_DB`, `SOT_MEAS_DB` | The select-on-test result 11.0 to 27.2 mW (0.41 dB inside the window) rests on three things the note does not show. (i) The step: the E24 table's losses step by up to 1.38 dB (19.88 to 21.26) and 1.26 dB (17.79 to 19.05), not 1 dB; with a 0.69 dB half-step the band is 10.5 to 28.4 mW (reviewer, same method). (ii) The +/-1 dB level reading at about 17 mW with a diode probe on the Fluke 174 has no basis: 04 section 6.2 expects the probe's 10 to 15 % at the 5 W level, while at 17 mW the peak is about 1.3 V, where the diode drop is a large fraction; with +/-1.5 dB the band is 9.8 to 30.5 mW, outside the window (F4 sensitivity, not shown). (iii) The REQ-SYS-144 delta that admits "drive pad selection" is a Proposed row of TS-012 section 8.10 and names the NanoVNA and tinySA, not the diode probe; REQ-SYS-144 as baselined allows no adjustment. Fix: use the table's real steps, state the reading method and its uncertainty basis (or a probe characterization at this level) with the sensitivity, and say that C1 depends on the owner accepting the REQ-SYS-144 delta and on the instrument (the owner buys the tinySA later, status note 2026-09-28 section 1) | Open | Pending | |
| <a id="finding-5"></a>finding-5 | reviewer | Minor | CK-ANA-E4 | `run_pa.py` `main()` | The checker computes pass flags against the acceptance values into `result.json` and `result.md`, but always exits 0, including on the FAIL verdicts the note reports (reviewer run: exit 0 with d2, p1, p2 and p3 FAIL). 08 section 3.4 and E4 ask for a non-zero exit on a failing case. Fix: exit non-zero when a verdict fails (or add a `--check` mode that does, with the expected FAIL states listed in the note so that a changed verdict is detected) | Open | Pending | |
| <a id="finding-6"></a>finding-6 | reviewer | Minor | CK-ANA-A1, A2, E2, H1, H2 | note header "Serves" row, sections 4.4, 5, 7 C4 | (i) TPM-015 and TPM-004 (the `mop_ids` of REQ-SYS-012) are not named: the nominal corner under 5.0 W at 6.4 V for both finalists meets TPM-015's red wording "the 5 W step unreachable at the cutoff voltage" if 6.4 V is that voltage, and A5's 0.45 minimum efficiency is below TPM-004's 55 % red line; the note gives the numbers but not the TPM comparison or a request to the TPM owner. (ii) REQ-SYS-114 is not named (finding-2). (iii) Hazards are not named: HZ-001's description assumes "up to 10 W at 8.4 V full drive" with the ALC open, which the note's 9.86 W module and 8.99 W at the SMA bound, and HZ-003 carries the module dissipation; no request goes to the `hazards.json` writer. (iv) The re-quantified REQ-SYS-012 risks (TS-012 section 7.1 rows A5 9 Yellow and A4 15 Red) go to the owner in C4 but not as a request to the WP-PDR-18 risk writer. (v) The design data are cited as "TS-012 revision 4" without its commit (`7d0d450`). Fix: add the ids, the TPM threshold comparison and the requests (PDR work plan section 5.3) | Open | Pending | |
| <a id="finding-7"></a>finding-7 | reviewer | Minor | CK-ANA-D2, I2 | note section 5, A4 second bullet; `results/2026-09-28-d2-drive-a5/result.md` first line and last bullet; `results/2026-09-28-p3-power-a5-sot/power_a5_sma.png` title | (i) Section 5 says A4 misses 3.97 W "at every corner below about 6.8 V"; section 4.5 and `p2` give the highest corner 4.49 W at 6.4 V, so it is the nominal corner that crosses at 6.8 V. (ii) `result.md` of d2 reads "FAIL at all 270 corners (210 in the window ...)", which reads as all corners failing; it means the all-corners verdict. Its line "A fixed pad 0.00 dB larger would bring the maximum to 30 mW" carries no information. (iii) The p3 plot has the same title as the p1 plot and does not name the select-on-test case (I2). Fix: reword the three | Open | Pending | |
| <a id="finding-8"></a>finding-8 | reviewer | Minor | CK-ANA-B1 | note sections 2 and 6 item 4; `run_pa.py` `GAINS`, `RAPP_*` | TS-012 section 7.3 names "the GVA-84+ S-parameters" for this check; the note uses a flat 50 ohm behavioural block with the 0.1 GHz gain limits and does not say it departed from the named method or why. The departure is reasonable (Rev. F gives 22.9 and 23.3 dB input and output return loss at 0.1 GHz), but the typical gain falls from 24.1 dB at 0.1 GHz to 21.7 dB at 1 GHz, so taking the 0.1 GHz limits at 144 to 148 MHz is slightly optimistic for the under-drive corners, and the direction is not stated. Fix: state the departure and its direction, or read the gain at 146 MHz from the vendor S2P file | Open | Pending | |

Two Major findings are open, so the reviewer verdict is NEEDS CHANGES. The arithmetic, the digitizing, the LTspice runs and the datasheet reads all hold (sections B5, C4 and the input check below); both Majors concern what the model leaves out (the CLK1 interface and temperature) against margins of 0.07 and 0.35 dB that the note reports as conclusions.

### Per-case results (section F; one row per case the governing texts name)

| Case | Condition | Governing id and limit | Result (checker output) | Margin with sign | Uncertainty | Reviewer re-check | Finding ids |
|---|---|---|---|---|---|---|---|
| C-1 | A5 drive, all 270 corners (Si5351 25 and 50 ohm, 3 edge and VDDO cases, GVA gain 22.5 to 25.3 dB, 3 P1dB sets, 144, 146, 148 MHz) | TS-012 WP-PDR-21: 10 to 30 mW; RA07M1317M Pin 30 mW maximum | 6.0 to 29.5 mW, nominal 12.6 mW; 60 below 10 mW, 0 above 30 mW | low -2.2 dB (FAIL); high +0.07 dB | not stated; interface term up to +2.2 dB (finding-1) | LTspice re-run identical; phasor model 5.98 to 29.58 mW, 60 below | finding-1 |
| C-2 | A5 drive, TS-012 criterion corners (25 and 50 ohm, gain 22.5 and 25.0 dB, 144 to 148 MHz, nominal Si5351 case) | TS-012: 10 to 30 mW | 8.5 to 22.7 mW, 27 of 36 inside | low -0.71 dB (FAIL) | as C-1 | phasor 8.51 to 22.71 mW, 27 inside | finding-1 |
| C-3 | 3f at the GVA-84+ input, both chains | TS-012: at most -25 dBc | worst -34.4 dBc (A5), -34.5 dBc (A4) | +9.4 dB | edge-time estimate | re-run same; tight-step run same (-34.42 dBc) | none |
| C-4 | GVA-84+ input level | Rev. F: +13 dBm maximum | -7.5 dBm (A5), -1.1 dBm (A4) | +20.5 dB, +14.1 dB | small | phasor -7.51 and -1.05 dBm | none |
| C-5 | A4 drive, all 270 corners | AFT05 Table 9 0.2 W ruggedness drive (informative, no rating) | 50 to 168 mW, nominal 96 mW | +0.76 dB | as C-1 | phasor 50.4 to 168.4 mW | finding-1 |
| C-6 | A5 at 6.4 V pack, lowest corner, typical module | REQ-SYS-012: at least 3.972 W | 3.71 W | -0.30 dB (FAIL) | graph reads, separable model, no temperature | Python fixed-point re-solve 3.71 W | finding-2, finding-3 |
| C-7 | A5 at 6.4 V, nominal corner | REQ-SYS-012 band; TPM-015 5 W reachable | 4.87 W (at VGG 3.5 V) | +0.89 dB to 3.97 W; -0.11 dB to 5.0 W | as C-6 | re-solve 4.87 W; 4.70 W at the 3.27 V nominal clamp | finding-3, finding-6 |
| C-8 | A5 at 6.4 V, datasheet-minimum module, lowest corner | REQ-SYS-012: 3.972 W | 3.03 W (3.62 W with feed at most 0.35 ohm and VGG 3.5 V) | -1.18 dB (FAIL) | uniform 6.5 W scale (estimate) | re-solve 3.04 W | none (stated, C4 to the owner) |
| C-9 | A5 at 6.4 V, lowest corner with the C2 and C3 levers | REQ-SYS-012: 3.972 W | 4.31 W | +0.35 dB | not stated | re-solve 4.30 W; 4.19 W at VGG 3.3 V | finding-2, finding-3 |
| C-10 | A5 at 8.4 V, ALC open (VGG 3.5 V) | RA07M1317M: stability to 8 W; 10 W maximum | module 9.13 W nominal, 9.86 W highest; above 8 W from 7.5 V | -0.9 dB to 8 W (outside the stability range); +0.06 dB to 10 W | as C-6 | re-solve 9.15 W nominal | none (stated, WP-PDR-22) |
| C-11 | A5 with the select-on-test drive, 6.4 V | REQ-SYS-012 | lowest 3.83 W, nominal 4.93 W | -0.16 dB (FAIL) | as C-6 | re-run identical | finding-4 |
| C-12 | A5 select-on-test drive window | TS-012: 10 to 30 mW | 11.0 to 27.2 mW (estimate) | +0.41 dB | not stated | 10.5 to 28.4 mW with the table's steps; 9.8 to 30.5 mW at +/-1.5 dB reading | finding-4 |
| C-13 | A4 at 6.4 V: lowest, nominal, highest | REQ-SYS-012: 3.972 W | 2.05, 3.54, 4.49 W | lowest -2.87 dB, nominal -0.50 dB (FAIL) | estimated (Vd/7.5)^n and match loss (Low) | re-solve 2.05, 3.54, 4.50 W; hand: 6.75 W x (5.96/7.5)^2 x 0.944 x 0.891 = 3.56 W | finding-7 |
| C-14 | A4 at 8.4 V lowest corner | REQ-SYS-012: 3.972 W | 3.76 W | -0.24 dB (FAIL over the whole range) | as C-13 | re-solve 3.76 W | none |
| C-15 | Band edges and centre, 144.0012 and 147.9988 MHz | REQ-SYS-008 | 144, 146 and 148 MHz in every deck | n/a | 0.34 dB drive span in a unit | corners checked | none |
| C-16 | -10 C and +45 C ambient | REQ-SYS-114 with REQ-SYS-012 | not analysed | not shown | not stated | none possible | finding-2 |
| C-17 | GVA-84+ model check | Rev. F P1dB 19.4 / 20.4 dBm, Psat 21.7 dBm | 19.37 / 20.37 / 21.37 and 20.69 / 21.69 / 22.69 dBm | within 0.03 dB | model fit | re-run identical | none |

## Readiness criteria

| # | Criterion | Result | Evidence |
|---|---|---|---|
| R1 | Frozen: every `product_files` blob equals `git rev-parse b705428:<path>` | Yes | 43 of 43 equal at `b705428` and at `HEAD` `6bff79c` (Python loop over `git rev-parse`) |
| R2 | The checker runs by one command and exits with the stated result; LTspice through the wrapper | Yes | Clean export of `b705428` (`git archive`) to the scratchpad with the author's `results/` moved aside; `.venv/bin/python hardware/sim/tx-pa/run_pa.py all`: exit 0, every run's LTspice provenance `exit 0`, log first line `LTspice 26.0.2 for MacOS` (six decks), no "warning" in any log |
| R3 | `validate_docs.py` on a JSON product | N/A | No JSON product under a schema |
| R4 | Author's return states question, assumptions, inputs, results, limitations, values and tools | Yes | Author summary in the brief; note sections 1 to 7 and header |
| R5 | No `TBD`; every TBR relied on named by id | Yes | Search, then grep: no `TBD` in the note or README; REQ-SYS-012 named with its TBR |
| R6 | Every cited render exists | Yes | 9 cited renders present, plus the p3 plot and 7 overlays |

## Reviewer re-run (CK-ANA-C4) and independent checks (CK-ANA-B5)

- **Full re-run.** All seven runs regenerated from LTspice (not the `CWHT_PA_REPLOT` path, so the author's "redrawn without re-running LTspice" last pass is also covered). Against the committed outputs: all six decks and all six `result.md` byte-identical; all seven `result.json` identical after removing the provenance block; both `corners.json` identical; all 10 result PNGs pixel-identical (matplotlib image arrays equal); the seven copies of `run_pa.py` in `results/` equal the checker blob.
- **Numerical settings (B4).** A variant of `drive_a5.cir` with `.tran 0 230n 200n 2p` (maximum step 2 ps instead of 10 ps, settling 200 ns instead of 90 ns) at the highest (idx 128), lowest (141) and nominal (202) corners, through the wrapper (exit 0, no warning): 29.521, 5.967 and 12.612 mW and 3f -34.42, -56.00, -45.39 dBc, equal to the note's corners within 0.0001 dB.
- **Drive chain by a different method (B5).** A frequency-domain model written by the reviewer: trapezoid Fourier coefficient (2 Vpp / pi) |sin(pi d)| sinc(f tr), nodal solution of the source, tap, LPF with its parasitics and pads, and the Rapp limiter as a describing function on a sine. A5 5.98 / 12.64 / 29.58 mW, 60 corners below 10 mW, 27 of 36 criterion corners inside, GVA input -10.07 and -7.51 dBm; A4 50.4 / 96.0 / 168.4 mW. Agreement within 0.02 dB. Hand checks: ideal 3.3 Vpp square into 50 / 50 ohm, 10.43 dBm available (TS-012's +10.4 dBm); 1 ns 20-80 % edge factor at 146 MHz -0.86 dB; 18 / 82 / 18 C-L-C Butterworth corner 1 / (2 pi 18 pF 50 ohm) = 177 MHz and 10 log(1 + (146/177)^6) = 1.19 dB (the note's 1.2 dB).
- **Power path by a different method (B5).** A Python fixed-point solve of Vd = Vp - Rf (Ibus + P / (eta Vd)) on the digitized curves read by median and interpolation (not the author's resampled tables or LTspice): A5 at 6.4 V nominal 4.87 W (Vd 5.76 V), lowest 3.71 W, highest 5.42 W, minimum module 3.04 W, levers 4.30 W; at 8.4 V nominal 8.15 W, module 9.15 W; A4 3.54 / 2.05 / 4.50 W at 6.4 V and 6.15 / 3.76 / 7.60 W at 8.4 V. All within 0.02 W of the note.
- **Sensitivity terms.** Recomputed from `corners.json` and the p1 and p2 `.raw`: A5 drive gain 2.74, Si5351 case 2.37, source R 1.51, frequency 0.26, P1dB 0.04 dB, within-unit frequency span 0.336 dB; A5 power at 6.4 V module spread 0.95, feed 0.44, VGG 0.41, drive 0.30, efficiency 0.20, loss 0.20, frequency 0.03 dB; A4 drive 1.66, n 0.44, match 0.44, feed 0.33, frequency 0.22, loss 0.20, efficiency 0.10 dB; A4 drive spread 5.23 dB. Match the note within 0.01 dB.
- **Pads.** ABCD recomputation of the eight select-on-test pads and the three design pads: losses as tabulated, return loss 25.8 dB or more, design pads 18.42, 3.00 and 11.97 dB.

## Inputs checked against their sources (CK-ANA-A4; every input that sets a reported result)

| Note section 3 row | Source read by the reviewer | Agreement |
|---|---|---|
| Si5351 ZO 50 ohm; edge 1 / 1.5 ns at CL 5 pF; duty 45 to 55 % below 160 MHz | Rev. 1.3 Table 4 "Output Impedance ZO ... 50" (3.3 V VDDO, default high drive); Table 7 rows as quoted | Yes; Table 7 also gives CL maximum 15 pF, not respected (finding-1) |
| GVA-84+ gain 22.9 / 24.1 / 25.3 dB; P1dB +19.4 min, +20.4 typ; Psat +21.7 at 3 dB compression; input +13 dBm maximum | Rev. F electrical specifications at 0.1 GHz and absolute maximum ratings | Yes (finding-8 on the frequency) |
| RA07M1317M: 6.5 W minimum at 7.2 V, VGG 3.5 V, Pin 20 mW; efficiency 45 % minimum at 6 W; Pin 30 mW, Pout 10 W at VGG 3.5 V or less, stability conditions, input VSWR 4:1 | Datasheet page 2 | Yes |
| RA07M1317M curves (Pout versus Pin, VDD, VGG at 135 and 155 MHz) | Pages 3 to 5 rendered; overlays opened; spot values: VDD curve 155 MHz 5.85 W at 6.0 V and about 8.2 W at 7.2 V; VGG curve 135 MHz 7.2 W at 3.0 V and 8.6 W at 3.5 V; Pin curve 39.38 dBm at 13 dBm (135 MHz) | Yes; the note's correction of TS-012 (5.85 W, not 5.3 W, at 6.0 V) is right. TS-012 section 7.3's "4 W at 3.0 V, 7 W at 3.5 V" on the VGG graph does not match the page (X-2) |
| RA07M1317M efficiency 0.60 typical | Page 4: about 1.63 A at 6.0 V, 155 MHz | Yes (graph read, estimate) |
| AFT05MS004N Figure 13 and Table 8 | Datasheet: Table 8 6.0 W at 135 MHz, Pin 0.10 W (62.3 %); 6.0 W at 155 MHz, Pin 0.06 W (69.1 %); Table 9 0.2 W at 155 MHz, 9.0 V; no Pin rating in Table 1. Overlay: the blue-dotted track is the 135 MHz curve (gain check at 0.03 W) | Yes; the 155 MHz track reads 6.32 W at 0.06 W against Table 8's 6.0 W (+0.2 dB, within a typical-curve read) |
| Drain feed 0.26 / 0.35 / 0.45 ohm; LPF 0.4 dB plus relay 0.1 dB; bus 0.2 A in TS-012 | TS-012 section 7.3 | Yes; 0.25 A bus is conservative |
| VGG clamp 3.08 V | TS-012 section 7.3: 4.75 x 0.6493 = 3.08 V, maximum 3.46 V | Yes for the low end; the 3.5 V level is above the clamp (finding-3) |
| REQ-SYS-012 bounds 3.972 and 6.295 W | requirements.json; 5 x 10^(-0.1) = 3.9716 W | Yes; the checker's 3.972 W rounds toward the stricter side |
| Stability window 10 to 30 mW | Datasheet: stability tested at Pin 10, 20 and 30 mW | Yes (a reasonable reading of three test points as a window) |

## Checklist answers

### A. Question, scope and traceable inputs

| Item | Answer | Evidence |
|---|---|---|
| CK-ANA-A1 | No | REQ-SYS-012, REQ-SYS-144, TS-012 criteria and WP-PDR-22 named and exist; REQ-SYS-114, TPM-015, TPM-004 and the hazards are not (finding-6, finding-2) |
| CK-ANA-A2 | No | TS-012 revision 4 cited by revision, not commit; no schematic exists yet, and the drive LPF values are "chosen here" (stated) (finding-6) |
| CK-ANA-A3 | Yes | Section 3 gives a source or "estimate" for every row |
| CK-ANA-A4 | Yes | Reviewer table above; disagreements listed (findings 1, 3, 8; X-2) |
| CK-ANA-A5 | No | Temperature assumption unstated (finding-2); VGG level and the drive and VGG interaction direction (finding-3) |
| CK-ANA-A6 | No | The CLK1 load and interface consequence is not sent to TS-012 (finding-1); the REQ-SYS-144 delta status (finding-4) |

### B. Model validity

| Item | Answer | Evidence |
|---|---|---|
| CK-ANA-B1 | No | Simplifications listed in section 6, but the interconnect, temperature and the GVA-84+ departure from S-parameters are not (findings 1, 2, 8) |
| CK-ANA-B2 | No | No vendor SPICE model is used; the Si5351 source is built from Table 7 values specified at CL 5 pF, used at 23 pF against the 15 pF maximum (finding-1) |
| CK-ANA-B3 | Yes | d1 fits the GVA-84+ compression within 0.03 dB; digitized curves checked against Table 8 and the RA07M1317M frequency plot; overlays |
| CK-ANA-B4 | Yes | `.tran` 10 ps maximum step, 90 ns settling, `plotwinsize=0`; the reviewer's 2 ps / 200 ns variant moves nothing (above) |
| CK-ANA-B5 | Yes | Phasor and fixed-point re-solves agree within 0.02 dB and 0.02 W (above) |
| CK-ANA-B6 | No | Graph-read error and estimates listed, but the combined uncertainty is not set against the thin margins (0.07 dB overdrive, 0.35 dB closure, 0.41 dB select-on-test) (findings 1, 2, 4) |

### C. Tools, validation status and reproducibility

| Item | Answer | Evidence |
|---|---|---|
| CK-ANA-C1 | Yes | Log first line `LTspice 26.0.2 for MacOS` equals the lock; venv versions equal the note (Python 3.13.5, scipy 1.18.1, spicelib 1.6.3, matplotlib 3.11.2) |
| CK-ANA-C2 | Yes | LTspice accredited (TV-014, ACC-LTSPICE-001, wrapper blob `88b71475`); the Python checker has no TV record and the note marks the result developer evidence |
| CK-ANA-C3 | Yes | `run_pa.py all` reproduces every number; netlists, one analysis each |
| CK-ANA-C4 | Yes | Reviewer re-run identical (above) |
| CK-ANA-C5 | Yes | TV-014 limitations respected: short run directory, lock, no `.asc` runs, exit and log checks by the wrapper |

### D. Units, arithmetic and consistency

| Item | Answer | Evidence |
|---|---|---|
| CK-ANA-D1 | Yes | mW, dBm, dBc, W and V consistent; dB conversions re-computed (for example 10 log(4.87 / 3.54) = 1.39 dB, the note's 1.4 dB) |
| CK-ANA-D2 | No | Numbers equal the checker output throughout; one sentence contradicts the table (finding-7) |
| CK-ANA-D3 | Yes | Limits rounded toward the stricter side (3.972 W); results given to the input precision |
| CK-ANA-D4 | Yes | `REQ012_LO`, `A5_PIN_MIN_MW`, `A5_PIN_MAX_MW`, `H3_MIN_DBC`, `GVA_ABSMAX_IN_DBM` with their source in the comment next to each |

### E. Results, margins, proposed values and credit

| Item | Answer | Evidence |
|---|---|---|
| CK-ANA-E1 | Yes | REQ-SYS-012, the TS-012 criterion and the datasheet limits quoted with their ids and sources |
| CK-ANA-E2 | No | Margins have the right sign; TPM-015 and TPM-004 thresholds not compared (finding-6) |
| CK-ANA-E3 | No | "Overdrive designed out" at +0.07 dB (finding-1); the (b) closure and the select-on-test pass at +0.35 and +0.41 dB without their uncertainty (findings 2, 4) |
| CK-ANA-E4 | No | Exit 0 on FAIL (finding-5) |
| CK-ANA-E5 | N/A | No TBR value proposed |
| CK-ANA-E6 | N/A | No TPM current best estimate proposed (the missing comparison is finding-6) |
| CK-ANA-E7 | Yes | Supporting pre-build evidence for a Test-method requirement (REQ-SYS-012), developer evidence; no credit claimed |

### F. Every case named

| Item | Answer | Evidence |
|---|---|---|
| CK-ANA-F1 | No | Pack ends and band edges covered; the REQ-SYS-114 temperature extremes are missing (C-16, finding-2) |
| CK-ANA-F2 | Yes | Open-loop ALC at 8.4 V analysed (C-10); cell at end of discharge is the 6.4 V end |
| CK-ANA-F3 | Yes | Extreme-value corners with the worst combination named per result (result files "Lowest corner" lines) |
| CK-ANA-F4 | No | Sensitivity tables given for drive and power; the select-on-test pass is not shown against its reading uncertainty (finding-4) |

### G1. Simulation decks and checkers

| Item | Answer | Evidence |
|---|---|---|
| CK-ANA-G1-1 | Yes | Decks, checker and plots under `hardware/sim/tx-pa/`, run-id folders tie them |
| CK-ANA-G1-2 | Yes | Drive decks `.tran` only, power decks `.dc` only; the wrapper's `NC_` check passed |
| CK-ANA-G1-3 | No | The CLK1 interface is not the designed interface (finding-1); the 50 ohm PA inputs follow the datasheet ZG = ZL = 50 ohm definition (stated) |
| CK-ANA-G1-4 | Yes | The checker reads the `.raw` through spicelib; the replot path re-reads only when the deck SHA-256 equals the recorded one; the wrapper removes stale outputs |

### G5. Cascades

| Item | Answer | Evidence |
|---|---|---|
| CK-ANA-G5-1 | Yes | Source, LPF with parasitics, tap, pads, GVA-84+ and PA input, each sourced (the missing interconnect is finding-1) |
| CK-ANA-G5-2 | Yes | Reviewer recomputed the cascade by a different method (B5) |
| CK-ANA-G5-3 | Yes | The only spurious criterion in scope, 3f at the GVA-84+ input, is evaluated at every corner; the other lines belong to WP-PDR-20 |

### G7. Worst-case and tolerance

| Item | Answer | Evidence |
|---|---|---|
| CK-ANA-G7-1 | Yes | Extreme-value corners, full factorial, stated in section 2 |
| CK-ANA-G7-2 | No | Initial tolerances used; temperature coefficients over REQ-SYS-114 not included (finding-2); ageing N/A |

### H. Hazards, risks and records

| Item | Answer | Evidence |
|---|---|---|
| CK-ANA-H1 | No | HZ-001 and HZ-003 not named; no request to the hazards writer (finding-6) |
| CK-ANA-H2 | No | Risk re-quantification not sent to the risk writer (finding-6) |
| CK-ANA-H3 | Yes | Change log revision 0 with its date |

### I. Visual closure

| Item | Answer | Evidence |
|---|---|---|
| CK-ANA-I1 | Yes | The reviewer opened all 9 cited plots, the p3 plot and the 7 digitizer overlays (17), and rendered and read RA07M1317M pages 3 to 5 |
| CK-ANA-I2 | No | Axes, units, limits with ids and legends present on all; the p3 plot title does not name its case (finding-7). Plotted values agree with the checker at the marked points (for example 29.5 mW top point, 3.71 W envelope floor at 6.4 V, 8 W crossing at 7.5 V) |

**ITEMS N/A:** CK-ANA-E5, CK-ANA-E6, CK-ANA-G2 to G4, CK-ANA-G6 (analysis_kind is simulation-deck, cascade and worst-case), CK-ANA-J1 to J3 (criticality neither).

## Cross items (returned to Claude as lead SE)

- **X-1. Output-loss allocation against the new LPF result.** `docs/design/analysis/lpf-ts012.md` (commit `6bff79c`, Draft, not reviewed) reports passband loss of the TS-012 LPF at median 0.76 dB and worst 1.21 dB with the BOM values, and worst 0.71 dB retuned. This note allocates 0.4 to 0.6 dB including the relay. Reviewer arithmetic (estimate): with the retuned worst 0.71 + 0.1 dB the (b) closure figure 4.31 W becomes about 4.11 W; with the BOM worst 1.21 + 0.1 dB about 3.66 W, under 3.97 W. The note's C6 anticipates this rerun; it belongs with the finding-2 fix.
- **X-2. TS-012 VGG graph read.** TS-012 section 7.3 "Drive gating" reads the RA07M1317M VGG graph as "about 0 W at 1.5 V, 2 W at 2.5 V, 4 W at 3.0 V, 7 W at 3.5 V". The datasheet page 5 (135 MHz) gives about 1.0 W at 2.5 V, 7.2 W at 3.0 V and 8.6 W at 3.5 V, consistent with its own text "nominal output power becomes available at 3V (typical)". The WP-PDR-22 envelope-loop deck should take the digitized curve, not the TS-012 figures. A request to the TS-012 author.
- **X-3. Section 4.7 margin wording.** "At least 1.0 V of margin" for the prescaler input is the total margin (0.5 V on each side with the bias midway), the same convention as INSP-110 O-5's 0.45 V. Not a finding; the WP-PDR-20 and prescaler designers should read it as a total.

## Commands

- Search: `mcp__claude-context__search_code` path `/Users/robinonsay/rust/cwht`, queries "PA drive window output power analysis TS-012 A4 A5 WP-PDR-21" and "INSP id register next free inspection id assigned".
- Freeze and blobs: Python loop over `git rev-parse b705428:<path>` and `git rev-parse HEAD:<path>` (43 files).
- Re-run: `git archive b705428 tools hardware/sim/tx-pa | tar -x -C <scratchpad>/exp`; author results moved to `results-author`; `cd <scratchpad>/exp && /Users/robinonsay/rust/cwht/.venv/bin/python hardware/sim/tx-pa/run_pa.py all` (exit 0); JSON, Markdown, deck and PNG comparisons in Python.
- Tight-step check: `tools/ltspice-batch.sh -t 600 -o <scratchpad>/rv/b4 -b drive_a5_b4.cir` (PASS, exit 0, sha256 `ba314986`).
- Independent models: `<scratchpad>/rv/phasor.py`, `<scratchpad>/rv/power_check.py`, `<scratchpad>/rv/line.py` (scratchpad only, not committed).
- Datasheets: `pdftotext -layout` and `pdftoppm -r 110 -f 3 -l 5` on the cached PDFs, SHA-256 checked against the block README.
- Record check: `/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/validate_docs.py --quiet` (this record not listed among the failures; the failures listed are pre-existing records).

## Verdict (returned by the reviewer)

```
VERDICT: NEEDS CHANGES
PRODUCT: docs/design/analysis/pa-drive-ts012.md@ecffcb3f, hardware/sim/tx-pa/run_pa.py@acbe1457, decks and results as in product_files, at b705428
FINDINGS:
- [Major] CK-ANA-G1-3, B2, E3, A6 finding-1: CLK1 loaded with 23 pF (Si5351 CL maximum 15 pF) and the Si5351-to-LPF interconnect of TS-012 8.1 not modelled; 5 to 15 cm of line puts 1 to 18 A5 corners above 30 mW (reviewer estimate); "overdrive designed out" rests on a 0.07 dB margin.
- [Major] CK-ANA-F1, A5, G7-2, B6, E3 finding-2: REQ-SYS-114 (-10 to +45 C) not analysed or stated; the +0.35 dB closure margin of section 5 (b) is not set against its uncertainty.
- [Minor] CK-ANA-A5, B1 finding-3: VGG 3.5 V is above the revision-4 clamp (3.08 to 3.46 V); nominal and C3 figures at an unreachable VGG; interaction direction unstated.
- [Minor] CK-ANA-F4, E3, A6 finding-4: select-on-test band uses 1 dB steps (table has up to 1.38 dB), an unsourced +/-1 dB reading, and a Proposed REQ-SYS-144 delta.
- [Minor] CK-ANA-E4 finding-5: checker exits 0 on FAIL.
- [Minor] CK-ANA-A1, A2, E2, H1, H2 finding-6: TPM-015, TPM-004, REQ-SYS-114, HZ-001, HZ-003, risk requests and the TS-012 commit not named.
- [Minor] CK-ANA-D2, I2 finding-7: A4 "every corner below 6.8 V" wording; d2 result.md wording; p3 plot title.
- [Minor] CK-ANA-B1 finding-8: departure from the TS-012 GVA-84+ S-parameter method and its direction unstated.
ITEMS N/A: CK-ANA-E5, E6, G2 to G4, G6 (analysis_kind simulation-deck, cascade, worst-case), CK-ANA-J1 to J3 (criticality neither)
VALUES PROPOSED: none
MEASUREMENTS: size=6 decks, 3294 LTspice corners; inputs_checked=10 rows (every input that sets a reported result); renders=17; turns=70; minutes=95; major=2; minor=6
```

## Iteration 2: delta verification of finding-1 and finding-2 (Major) (2026-09-28, HEAD `d1a9a6a`)

**Scope (rule C1).** Iteration 2 is a delta that verifies the fixes of finding-1 and finding-2 (Major) and scans the changed text, decks, checker and results for defects the revision introduced. The author also answered finding-3 (Minor) and asked the reviewer to confirm that the answer covers its full text; that check is below. finding-4 to finding-8 (Minor) were not addressed by revision 1 and are not re-reviewed, except where the revision moved a number they cite. Product: the 55 blobs of front matter `product_files`, committed as `9d01aaf` (note revision 1, runs `results/2026-09-28-r1-*`, re-freeze under rule C2). Each equals `git rev-parse 9d01aaf:<path>` and `git rev-parse HEAD:<path>` at HEAD `d1a9a6a`; `git log 9d01aaf..HEAD` is one commit (`d1a9a6a`, status note and deviations only). The run folders' copies of `run_pa.py` equal the committed checker. No product blob is on a `cr/` branch. Checklist as iteration 1: `peer-review-checklist-analysis.md` revision A, blob `0386cc6e`, still only on `cr/CR-012-pdr-checklist-templates` (head `7784672`, not an ancestor of `main`).

**Independence (rule C4).** This invocation authored no part of the note, its revision 1, the decks, the checker, the digitizers or TS-012, and edited no product file. It changed only this record.

**Search first (charter section 11 rule 1).** One `git log`/`git show --stat` and one `ls` of the checklists directory (known paths, not searches) ran first. `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` then ran before every manual search (queries: "PA drive note revision 1 CLK1 coax select-on-test pad DR-PAD-1 temperature cases"; "iteration 2 delta review record verifying Major fixes front matter"; "A5 design-change thermal model case temperature 105.7 C at 9.94 W 45 C ambient steady key-down"). `grep` then only pinned lines in known files (TS-012, `run_pa.py`, `tools/validate_docs.py`, the note, the status note). The rustos tree was not read.

**Sources re-read by the reviewer (2026-09-28, public vendor pages through the web-fetch tool; SHA-256 prefixes equal the block README).** Skyworks Si5351A/B/C-B Rev. 1.3 (`f3bc5285`), https://www.skyworksinc.com/-/media/Skyworks/SL/documents/public/data-sheets/Si5351-B.pdf: Table 7 "Load Capacitance CL ... 15 pF" (max), rise and fall time at "20%-80%, CL = 5 pF", duty 45 to 55 % below 160 MHz, all at TA -40 to 85 C; section 7.6 Figure 16, "ZO = 50 ohms", "R = 0 ohms (Optional resistor for EMI management)". Molicel INR-18650-P28A (`05db826b`), https://www.molicel.com/wp-content/uploads/INR18650P28A-V1-80093.pdf: "DC (10A/1s) 20 mΩ"; the 2.8 A discharge-temperature chart rendered at 200 dpi and read: at mid capacity (about 1400 mAh) the 0 C curve sits about 0.12 V and the -20 C curve about 0.25 V under the 23 C curve (the note: 0.11 and 0.27 V; agreement within a graph read). NXP AFT05MS004N Rev. 0 (`84cd9fae`), Table 8 re-read: 135, 155, 175 MHz at Pin 0.10, 0.06, 0.10 W (the d3 plot's "100 mW ... at 135 and 175 MHz" is right). Adafruit product page 2045, https://www.adafruit.com/product/2045: "Outputs are 3Vpp, either through a breadboard-friendly header or, for RF work, an optional SMA connector."

**Reproduction (CK-ANA-C4, readiness R2).** Clean `git archive 9d01aaf tools hardware/sim/tx-pa docs/design/analysis/pa-drive-ts012.md` in the scratchpad, the author's eight `results/2026-09-28-r1-*` folders moved aside, then `/Users/robinonsay/rust/cwht/.venv/bin/python hardware/sim/tx-pa/run_pa.py all`: exit 0. Every LTspice run went through `tools/ltspice-batch.sh` (blob `88b71475`): ten "result: PASS ... version_line='LTspice 26.0.2 for MacOS' ltspice_exit=0" lines with deck SHA-256 equal to the README's; no "warning" in any `.log`. Against the committed outputs, 59 of 59 files agree: every deck and `result.md`, `corners.json` and `coax_*_steps.json` byte-identical, every `result.json` identical after removing the wrapper provenance block, all 20 PNGs pixel-identical (image arrays equal), and the eight script copies. The `.raw` files were read by the checker through spicelib 1.6.3.

**Reviewer scripts (scratchpad, not product):** `phasor2.py` (a frequency-domain model of the revision 1 chain written by the reviewer: trapezoid Fourier coefficient, pin capacitance, lossless-line input impedance and voltage transfer, C-L-C filter with its parasitics, pads, and the Rapp limiter as a describing function by FFT), `d4chk.py` (length sweep on a 1 mm grid), `power2.py` (fixed-point solve of Vd = Vp - Rf (Ibus + P / (eta Vd)) on the digitized CSVs, binned by median; not the deck tables), `selfheat.py` (the same solve with the PA case at its steady key-down temperature).

### Verification of finding-1 (Major), case by case (rule C7)

| Finding | Case the finding named | Check at `9d01aaf` | Result |
|---|---|---|---|
| finding-1 | (i) CLK1 loaded with 23 pF against the 15 pF of Table 7 | Decks `drive_a5.cir`, `drive_a4.cir`, `drive_a5_pinpad.cir`, `coax_*.cir`, `tstep_*.cir`: only `Ctap clk 0 5p` and `Cstub clk 0 2p` sit on the pin; the drive LPF's `C1 lpfin 0 18p` is at the far end of `T1`. Lumped 7 pF against 15 pF (estimate, PASS). The line-fed load at the fundamental is reported as an equivalent shunt capacitance, 13.6 to 24.7 pF in d2 (about 14 / 19 / 25 pF at 5 / 10 / 15 cm), -16.4 to +30.4 pF over any length (d4), 9.6 to 11.9 pF with the d5 pin pad. Reviewer phasor model: 13.6 to 24.7 pF (d2, every corner within 0.02 pF), 9.6 to 11.9 pF (d5), -16.4 to +30.4 pF (1 mm grid). The note's reading of Table 7 (a lumped CL; Figure 16 names a 50 ohm line but not its termination; the driver's Table 7 edge and swing are not shown into this load) matches the datasheet text. The out-of-table load is stated and sent to TS-012 as DR-PAD-1 (section 7) with a modelled alternative (A6) | Yes |
| finding-1 | (ii) the board-to-board interconnect of TS-012 section 8.1 not modelled | TS-012 `7d0d450` section 8.1: the RF board carries "drive LPF, pads, GVA-84+, relay, output LPF, detector, 40 dB tap"; section 7.3: "Only the DC, drive and coax leads pass the bulkhead"; the Adafruit 2045 sits on the main board on its header. The note models the drive lead as a 50 ohm coax from the Adafruit SMA (Figure 16 topology), 5 / 10 / 15 cm, VF 0.66, lossless, and bounds the length over every electrical length (d4, 0.5 to 70 cm, 2.5 cm steps; half a wavelength is 68.7 cm at 144 MHz). It states what it does not bound (another line impedance, a coplanar trace; limitation 7) and asks TS-012 to state the interface (DR-PAD-1). Reviewer phasor model against every step: d2 within +0.011 / -0.006 dB, d5 within +0.009 / -0.002 dB, d4 A5 within +0.020 / -0.004 dB, d3 and d4 A4 within 0.04 dB (GVA-84+ in compression); 3f within 0.04 dB. Reviewer 1 mm length grid: highest A5 corner 48.75 mW at 33.8 cm (-2.11 dB), against d4's 48.65 mW at 32.5 cm (-2.10 dB); the 2.5 cm grid misses the peak by 0.01 dB. The time-step check (15 corners, 10 ps against the 20 ps of d2 and d3): 0.0005 dB, criterion 0.02 dB, PASS | Yes |
| finding-1 | (iii) "Overdrive is designed out" on a 0.07 dB margin; report the overdrive margin with its uncertainty | Withdrawn in sections 4.2 and 5 (a) and in the README. Fixed pad: 5.4 to 35.5 mW, 28 of 810 corners above 30 mW (1 / 9 / 18 per length), margin -0.73 dB (-0.83 dB with the 0.1 dB temperature allowance), -2.10 dB at any length; 195 corners under 10 mW; spread 8.19 dB against the 4.77 dB window. The select-on-test route is given with its terms and both sums (+0.42 dB worst-case, +1.22 dB RSS). Reviewer: the author's arithmetic reproduces (half-width 0.169 + 0.5 + 1.0 + 0.3 = 1.97 dB; 10 log(30 / 17.3) - 1.97 = +0.42 dB); the frequency term is symmetric about the 146 MHz alignment point (at most +0.166 and -0.172 dB from 146 MHz in any unit, against span / 2 = 0.169 dB), so taking half the span is right. The step and reading terms are still finding-4's (below): with the table's own largest gap the margin is +0.24 dB | Yes |
| finding-1 | Fix option: keep the pin load within 15 pF, or state the out-of-rating use and send it to TS-012 | DR-PAD-1 gives TS-012 both: (a) accept the line-fed load with the build alignment as the control, or (b) the d5 pad (150 / 36 / 150 ohm, 5.90 dB, reviewer ABCD 5.90 dB), which keeps the equivalent load at 9.6 to 11.9 pF, cuts the length sensitivity to 0.2 dB and improves 3f to -35.4 dBc, at a lower tap swing (1.59 Vpp, routed to WP-PDR-20 as C9) | Yes |

Also checked: the 3f criterion over the whole length sweep, which the note says d4 does not report (section 4.7). Reviewer model, 25 and 50 ohm, all three Si5351 cases, 144 to 148 MHz, 2 mm grid to 72 cm: worst 3f at the GVA-84+ input -30.7 dBc at 4.2 cm for A5 and A4 (-35.3 dBc with d5); the criterion (at most -25 dBc) holds at every length with at least 5.7 dB.

**Result: finding-1 Verified.**

### Verification of finding-2 (Major), case by case (rule C7)

| Finding | Case the finding named | Check at `9d01aaf` | Result |
|---|---|---|---|
| finding-2 | REQ-SYS-114 named; the 25 C basis of every curve stated | Header "Serves", section 1 question 4, section 2 "Temperature cases", section 3 rows (RA07M1317M "all at Tcase 25 C"; Si5351 Table 7 at TA -40 to 85 C; GVA-84+ coefficient), section 4.4 "All the curves of revision 0 were at 25 C, which revision 0 did not say" | Yes |
| finding-2 | Cold (-10 C) corner with sourced or labelled cell resistance | Section 3.1 and `FEED_PARTS`: cells from the P28A datasheet (DC IR 20 mohm read by the reviewer; the discharge-temperature graph read agrees within 0.02 V), multipliers x3.0 to x3.3, the other parts labelled estimates with a direction. Reviewer recomputation of `feed_at()`: at the criterion level the parts sum to 0.4174 ohm at -10 C against 0.355 ohm at 25 C, scaled to 0.4114 ohm (deck `rf` table 0.41135); low and high levels 0.3016 and 0.5396 ohm, hot 0.293 / 0.4174 / 0.5675 ohm, as the deck. Observation O-7 on the level coupling | Yes |
| finding-2 | Hot (+45 C) corner with the WP-PDR-28 flange temperature and the module output at temperature | Four hot cases: case 80 C (WP-PDR-28 A5-DC case 105.69 C at 9.94 W and 45 C, `verdicts.md` of run `ts012-r2`: (105.69 - 45) / 9.94 = 6.11 K/W, times 3.2 to 5.9 W) and a 100 C bound; PA factor -0.005 or -0.015 dB/K (estimate, Low, basis and direction stated), +0.1 dB copper term. `kt` and `kxl` in the deck equal 10^(-0.275/10) = 0.9386, 10^(-1.125/10) = 0.7718 and 10^(-0.01) = 0.9772. Reviewer steady-state check at 45 C ambient with the same 6.1 K/W: lever-corner case 75.5 to 78.3 C, consistent with the 80 C case. But the 25 C ambient case takes the PA case at 25 C, which the same thermal inputs do not support: new finding-9 | Yes (hot and cold cases); see finding-9 |
| finding-2 | Carried into the C2 and C3 pass criteria; C8 for what is not shown | C2 adds at most 0.42 ohm at -10 C and +45 C and the RDS(on) and polyfuse temperature reads; C3's pass criterion names 25 C and -10 C with the unmodelled terms; C8 puts the +45 C, 6.4 V corner to the owner (conditional delta or a bench check at 80 C flange) | Yes |
| finding-2 | Uncertainty of the closure margin stated | Three terms not carried as corners (LPF loss above the allocation -0.21 dB from the committed LPF runs r6 and r7, graph read +/-0.07 dB, GVA-84+ in LM2940 dropout -0.05 dB), added worst-way per temperature case (s1 table and `a5_closure_margin.png`). Reviewer re-solve (`power2.py`, independent of the deck tables) at the lever corner: 4.266 / 4.093 / 3.795 / 3.439 / 3.727 / 3.255 W for 25 C, -10 C and the four hot cases against the note's 4.28 / 4.10 / 3.81 / 3.45 / 3.74 / 3.26 W (within 0.015 W); p3 4.449 / 4.261 / 3.954 / 3.587 / 3.886 / 3.397 W against 4.45 / 4.27 / 3.96 / 3.59 / 3.89 / 3.40 W; nominal 4.856 W (Vd 5.76 V) against 4.85 W | Yes |

**Result: finding-2 Verified** for what it asked (the cold and hot corners with sourced or labelled inputs, the direction, the C2, C3 and C8 criteria and the margin's uncertainty). The same revision introduced an inconsistency in the 25 C row of the new temperature model, raised as the new finding-9 (Major).

### finding-3 (Minor): the author's disposition does not cover the full text

The finding reached the author truncated (note section 9). Its full text is the iteration 1 row above: the revision-4 clamp puts VGG at 3.08 to 3.46 V (nominal 3.27 V), so the 3.5 V level used for the nominal, highest and lever figures is above what the design can reach; fix: use the clamp's nominal and maximum for the nominal and highest corners, state C3 at the VGG it requires, and state the direction of the drive and VGG interaction at the lowest corner. Revision 1 defines every figure and writes its parameter set (that part holds), but section 4.4 still takes "VGG 3.5 V" for the nominal and lever figures, `power_a5_temperature.png` says "VGG 3.5 V" in its legend, and C3 asks for "at least 3.3 V (estimate)" while its pass figures (-0.01 / +0.16 dB at 25 C) are computed at 3.5 V. Limitation 2 now gives a direction for taking the VGG factor at 7.2 V (pessimistic) but not for the drive and VGG interaction at a low VGG and 6 mW of drive (likely optimistic). Reviewer re-solve at 25 C, lever corner: 4.27 W at 3.5 V, 4.24 W at 3.46 V, 4.15 W at 3.3 V (+0.19 dB), 4.13 W at 3.27 V; nominal 4.86 / 4.83 / 4.71 / 4.68 W. **finding-3 stays Open (Minor).**

### Minor findings not addressed in revision 1 (status only)

- finding-4: Open. The select-on-test text still says "a set in 1 dB steps" while its own E24 table steps by 0.73 to 1.38 dB; with the largest half-gap (0.69 dB) the as-designed band is 10.5 to 28.5 mW and the overdrive margin +0.24 dB (under +0.22 dB), not +0.42 dB; with a +/-1.5 dB reading -0.26 dB; with the tinySA at +/-0.5 dB (estimate) +0.74 dB, not "about +0.9 dB". The +/-1 dB reading still has no basis at 17 mW, and section 4.2 still says the REQ-SYS-144 delta "already admits" pad selection (a Proposed TS-012 row). The Fluke 174 named in the note is the owner's meter (status note 2026-09-28 section 2).
- finding-5: Open. `run_pa.py all` exits 0 with FAIL verdicts in d2, p1, p2 and p3 (reviewer re-run).
- finding-6: Open. TPM-015, TPM-004, HZ-001, HZ-003 and the TS-012 commit are still not named (REQ-SYS-114 now is).
- finding-7: Open, partly moot. (i) is gone (section 5 now says the nominal corner reaches 3.97 W from 6.85 V); (ii) d2 `result.md` still reads "FAIL at all 810 corners (587 in the window, ...)"; (iii) the p3 plots `power_a5_sma.png` and `power_a5_temperature.png` carry the same titles as p1 and do not name the select-on-test drive.
- finding-8: Open. The departure from the GVA-84+ S-parameters and its direction are still not stated.

### New findings (iteration 2)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-9"></a>finding-9 | reviewer | Major | CK-ANA-G7-2, E3, B6, A5 | `run_pa.py` `TC_CASES` row `("t25", "25 C", 25, 25, "t25", 0.0, 0.0)`; note sections 3.1, 4.4 (both tables, "The closure figure against its uncertainty"), 5 (c), 5 (d) and the A5 verdict line, 7 C3; s1 closure table and `a5_closure_margin.png` | The temperature model is not applied consistently. The hot cases take the PA case at its steady key-down temperature (80 C = 45 C ambient plus 6.1 K/W times 3.2 to 5.9 W, from WP-PDR-28), but the 25 C ambient case takes the PA case at 25 C, the datasheet test condition, with no self-heating. With the note's own 6.1 K/W the case at 25 C ambient in the same steady key-down is 58 to 62 C at the lever corner (module 4.9 W at eta 0.45, 6.0 W dissipated) and 46 to 47 C at the nominal corner. Applying the note's own coefficient above 25 C case (reviewer `selfheat.py`, case solved with the output): p1 lever corner 4.13 W (+0.17 dB) at -0.005 dB/K and 3.89 W (-0.09 dB) at -0.015 dB/K, against 4.28 W (+0.32 dB); with the unmodelled terms -0.16 to +0.24 and -0.42 to -0.02 dB, against -0.01 to +0.39 dB. p3: 4.30 W (+0.35 dB) and 4.05 W (+0.08 dB), with the terms +0.02 to +0.42 and -0.25 to +0.15 dB, against +0.16 to +0.56 dB. Nominal 4.75 and 4.56 W against 4.85 W. The -10 C case is consistent (case about 25 C in steady key-down, so the 0 dB factor holds) and the hot cases are (75.5 to 78.3 C against 80 C). So the section 5 statements "closable before the order at 25 C" and "at 25 C, with the select-on-test pad, by +0.16 dB at worst", and C3's 25 C pass figures, are not supported: at -0.015 dB/K the 25 C lever corner is not shown even with the select-on-test drive, and C3 at 3.3 V (finding-3) takes a further 0.12 dB. The A5 against A4 comparison of section 5 does not change direction. Fix: take the PA case at 25 C ambient from the same thermal model as the hot cases (or define every case at one thermal state, for example the start of a key-down from soak, and move the hot cases to match), rerun p1 and p3 and s1, and restate 5 (c), 5 (d), the A5 verdict line, C3 and C8 (C8's bench check may need to cover 25 C ambient too) | Open | Pending | |
| <a id="finding-10"></a>finding-10 | reviewer | Minor | CK-ANA-I2 | `results/2026-09-28-r1-p2-power-a4/power_a4_temperature.png` | The y axis starts at 1.5 W, so the lowest-corner marker of "+45 C, case 100 C, -0.015 dB/K" (1.42 W, the value section 4.5 quotes as the worst temperature case) is off the plot, and the "+45 C, case 80 C, -0.015 dB/K" marker (1.51 W) sits on the axis. Fix: set the lower limit below the smallest plotted value | Open | Pending | |

### Per-case results (iteration 2; section F, one row per case the governing texts name)

Values are the checker's (all estimates), from the committed `result.json` files, which the reviewer's re-run reproduced.

| Case | Condition | Governing id and limit | Result (checker output) | Margin with sign | Uncertainty | Reviewer re-check | Finding ids |
|---|---|---|---|---|---|---|---|
| C-1 | A5 drive, fixed 18 dB pad, 810 corners (270 part corners x 5 / 10 / 15 cm coax) | TS-012 WP-PDR-21: 10 to 30 mW; RA07M1317M Pin 30 mW maximum | 5.4 to 35.5 mW, nominal 11.4 mW; 195 under 10 mW, 28 over 30 mW: FAIL | high -0.73 dB (-0.83 dB with the 0.1 dB allowance); low -2.68 dB | coax length (C-3), source terms (estimates) | re-run identical; phasor 5.39 to 35.46 mW, 28 over, 191 under (every corner within 0.011 dB) | none |
| C-2 | A5, TS-012 criterion corners (25 and 50 ohm, gain 22.5 and 25.0 dB, 144 to 148 MHz, nominal Si5351 case, three lengths) | TS-012: 10 to 30 mW | 7.7 to 27.4 mW, 81 of 108 inside: FAIL | low -1.14 dB | as C-1 | re-run identical | none |
| C-3 | A5 fixed pad, any coax length (d4) | RA07M1317M 30 mW | 5.4 to 48.6 mW: FAIL | -2.10 dB (-2.20 dB) | 2.5 cm grid | phasor 1 mm grid 48.75 mW at 33.8 cm (-2.11 dB) | none |
| C-4 | 3f at the GVA-84+ input, both chains, 5 to 15 cm | TS-012: at most -25 dBc | worst -30.9 dBc (d2, d3); -35.4 dBc (d5): PASS | +5.9 dB | edge-time estimate | phasor within 0.04 dB; any length -30.7 dBc (+5.7 dB) | none |
| C-5 | GVA-84+ input level | Rev. F: +13 dBm maximum | -6.7 dBm (A5), -0.2 dBm (A4): PASS | +19.7, +13.2 dB | small | re-run identical | none |
| C-6 | CLK1 lumped load as designed | Si5351 Table 7: CL at most 15 pF | 7 pF (tap 5 pF + stub 2 pF, estimates): PASS | +8 pF | estimates | deck lines read | none |
| C-7 | CLK1 line-fed load at the fundamental | Si5351 Table 7 (not covered: lumped CL only) | 13.6 to 24.7 pF equivalent, 36 to 65 ohm; any length -16.4 to +30.4 pF | not a Table 7 case; DR-PAD-1 | coax impedance and length | phasor 13.6 to 24.7 pF; -16.4 to +30.4 pF | none (routed as DR-PAD-1) |
| C-8 | Option d5 (6 dB at the pin, 12 dB on the RF board) | Table 7 15 pF; 10 to 30 mW | 9.6 to 11.9 pF: PASS; drive 6.7 to 41.6 mW (fixed pad: FAIL) | +3.1 pF; -1.42 dB | as C-1 | phasor 9.6 to 11.9 pF, 6.75 to 41.65 mW | none |
| C-9 | A4 drive, 810 corners and any length | AFT05 Table 9 0.2 W ruggedness drive (informative) | 45.8 to 180.0 mW; any length 195.9 mW | +0.46 dB; +0.09 dB (-0.01 dB with the allowance) | as C-1 | phasor 45.9 to 179.4 mW (within 0.04 dB) | none |
| C-10 | Time step of d2 and d3 (20 ps) against 10 ps, 15 corners | note criterion: 0.02 dB (power), 0.5 dB (3f) | 0.0005 dB, 0.013 dB: PASS | +0.0195 dB | n/a | re-run identical; phasor agreement 0.011 dB | none |
| C-11 | A5 select-on-test drive in service | TS-012: 10 to 30 mW | 11.0 to 27.2 mW (estimate): PASS | +0.42 dB (RSS +1.22 dB) | reading +/-1 dB (no basis), step | +0.24 dB with the table's 1.38 dB gap; -0.26 dB at a +/-1.5 dB reading | finding-4 |
| C-12 | A5 at 6.4 V, 25 C, lowest corner, typical module | REQ-SYS-012: at least 3.972 W | 3.68 W: FAIL | -0.33 dB | graph reads, separable model | re-solve 3.67 W | finding-9 |
| C-13 | A5 at 6.4 V, 25 C ambient, lever corner (C2, C3), fixed pad | REQ-SYS-012: 3.972 W | 4.28 W | +0.32 dB (-0.01 to +0.39 dB with the terms) | PA case taken at 25 C | re-solve 4.27 W; with the PA case at its steady 58 to 60 C: 4.13 / 3.89 W, +0.17 / -0.09 dB; at VGG 3.3 V 4.15 W | finding-9, finding-3 |
| C-14 | Same with the select-on-test drive (p3) | REQ-SYS-012: 3.972 W | 4.45 W | +0.49 dB (+0.16 to +0.56 dB) | as C-13 | re-solve 4.45 W; self-heated 4.30 / 4.05 W, +0.35 / +0.08 dB (-0.25 to +0.42 dB with the terms) | finding-9 |
| C-15 | A5 lever corner at -10 C (cells and parts cold, PA +0 dB) | REQ-SYS-012 with REQ-SYS-114 | 4.10 W (p1), 4.27 W (p3) | +0.14 dB (-0.19 to +0.21), +0.31 dB (-0.02 to +0.38) | cell graph read; PA cold gain taken as 0 (conservative) | re-solve 4.09 / 4.26 W; steady case about 25 C, so the 0 dB factor is consistent | none |
| C-16 | A5 lever corner at +45 C, four cases | REQ-SYS-012 with REQ-SYS-114 | 3.26 to 3.81 W (p1), 3.40 to 3.96 W (p3): FAIL | -0.86 to -0.18 dB; -0.68 to -0.02 dB | PA coefficient (no vendor data) | re-solve 3.26 to 3.80 W and 3.40 to 3.95 W | none (C8 to the owner) |
| C-17 | A5 datasheet-minimum module with C2 and C3 | REQ-SYS-012: 3.972 W | 3.47 W at 25 C; 2.64 W worst hot | -0.58 dB; -1.78 dB | uniform 6.5 W scale | s1 table | none (C4 to the owner) |
| C-18 | A5 open loop at 8.4 V (VGG 3.5 V), highest corner | RA07M1317M: stability to 8 W; 10 W maximum | module 9.90 W at 25 C; 10.76 W at -10 C, +0.53 dB | -0.93 dB to 8 W; -0.32 dB to 10 W at -10 C | cold coefficient estimate | re-run identical | none (WP-PDR-22) |
| C-19 | A4 at 6.4 V: nominal and lowest, 25 C and worst hot | REQ-SYS-012: 3.972 W | 3.48 / 1.90 W; 2.63 / 1.42 W: FAIL | -0.57 / -3.21 dB at 25 C | estimated n and match loss (Low) | re-run identical | finding-10 (plot) |
| C-20 | REQ-SYS-114 ambient -10 C and +45 C (iteration 1 C-16) | REQ-SYS-114 with REQ-SYS-012 | seven cases in every power run | as C-15, C-16 | PA coefficient | above | finding-9 (25 C row) |
| C-21 | Band edges and centre | REQ-SYS-008 | 144, 146, 148 MHz in every deck | n/a | 0.34 dB drive span in a unit | corners read | none |

### Findings (iteration 2; current state of every finding of this record)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| finding-1 | reviewer | Major | CK-ANA-G1-3, B2, E3, A6 | decks, note sections 2, 4.2, 5, 7 | See iteration 1 and the verification table | Verified (iteration 2, revision 1 at 9d01aaf) | n/a | |
| finding-2 | reviewer | Major | CK-ANA-F1, A5, G7-2, B6, E3 | note sections 3.1, 4.4, 5, 6, 7; power decks | See iteration 1 and the verification table; the 25 C row defect is finding-9 | Verified (iteration 2) | n/a | |
| finding-3 | reviewer | Minor | CK-ANA-A5, B1 | note section 4.4, 6 item 2, 7 C3 | See iteration 1; the revision 1 disposition covers traceability only (above) | Open | Pending | |
| finding-4 | reviewer | Minor | CK-ANA-F4, E3, A6 | note section 4.2, 7 C1; `SOT_STEP_DB`, `SOT_MEAS_DB` | See iteration 1; margin +0.24 dB with the table's steps (above) | Open | Pending | |
| finding-5 | reviewer | Minor | CK-ANA-E4 | `run_pa.py` `main()` | See iteration 1 | Open | Pending | |
| finding-6 | reviewer | Minor | CK-ANA-A1, A2, E2, H1, H2 | note header, sections 4.4, 5, 7 | See iteration 1 (REQ-SYS-114 now named) | Open | Pending | |
| finding-7 | reviewer | Minor | CK-ANA-D2, I2 | d2 `result.md`; p3 plot titles | See iteration 1; item (i) moot | Open | Pending | |
| finding-8 | reviewer | Minor | CK-ANA-B1 | note sections 2, 6 item 4 | See iteration 1 | Open | Pending | |
| finding-9 | reviewer | Major | CK-ANA-G7-2, E3, B6, A5 | `TC_CASES` 25 C row; note sections 4.4, 5, 7 C3 | See the new findings table | Open | Pending | |
| finding-10 | reviewer | Minor | CK-ANA-I2 | `power_a4_temperature.png` | See the new findings table | Open | Pending | |

### Observations (not findings)

- O-6. The pin swing reaches 3.67 Vpp at the 25 ohm, fast-edge corners, above the 3.4 V VDDO: the linear Thevenin source lets reflections carry the pin beyond the rails, which a CMOS driver with clamp diodes would limit. Limitation 6 covers the linear source; the effect is on the high side of the drive (conservative for overdrive) and on the tap swing's upper end only.
- O-7. The cold cell multiplier is applied per level (x3.0 on 0.04 ohm, x3.3 on 0.06 ohm). The datasheet pair value 0.04 ohm with the steady-state 68 mohm per cell gives 0.176 ohm, above the 0.1575 ohm the criterion level takes; about 0.02 ohm more feed at -10 C, about -0.07 dB on C-15. Inside the "about 0 dB" the note already states.
- O-8. TS-012 names a "drive" lead through the bulkhead, not a coax (its "coax" lead is the output). The note's reading (the Adafruit SMA and a 50 ohm coax) is stated as the design basis and DR-PAD-1 asks TS-012 to confirm it; a plain wire would change the fixed-pad results and the pin load, not the select-on-test route.
- O-9. `drive_a5_pinpad.cir` (d5) keeps the first-line title "drive_a5.cir: ..." of the deck it came from; the README says so. Harmless.

### Cross items (iteration 2, returned to Claude as lead SE)

- X-4. The DR-PAD-1 interface (Adafruit SMA edge jack, a 5 to 15 cm RG-174 or RG-316 lead, a mating connector or solder launch on the RF board) is not in the TS-012 `7d0d450` BOM or its cost roll-up (no coax, SMA or U.FL row). A request to the TS-012 author with DR-PAD-1.
- X-5. The closure term for the output LPF (-0.21 dB) rests on the retuned LPF runs r6 and r7 committed at `9d01aaf`; the BOM-value runs give more loss (iteration 1 X-1), and the LPF block has uncommitted runs r8 to r16 in the working tree (another session's work, not read). C6 covers the rerun once TS-012 fixes the LPF values.
- X-6. finding-9 reaches C8: if the fix confirms it, the owner decision C8 should cover the 25 C ambient steady key-down case too, not only +45 C.

### Checklist items changed at iteration 2

Now Yes: CK-ANA-B2 (the lumped pin load is inside Table 7; the out-of-table line-fed load is stated and routed), CK-ANA-F1 (the REQ-SYS-114 extremes are cases), CK-ANA-G1-3 (the interface is the stated design basis, bounded over every length). Still No: CK-ANA-A5 (finding-3), A6 (finding-4 item iii; DR-PAD-1 itself is routed), B1 (finding-8), B6 and E3 (finding-9, finding-4), G7-2 (finding-9), I2 (finding-7 iii, finding-10), and A1, A2, D2, E2, E4, F4, H1, H2 on the untouched Minor findings. CK-ANA-B4: Yes, the 20 ps step is checked at 10 ps in d4 and by the reviewer's independent model. CK-ANA-B5: Yes, the phasor and fixed-point re-solves agree within 0.04 dB and 0.015 W. CK-ANA-C1 to C5: Yes, as iteration 1, with the re-run above. CK-ANA-H3: Yes, change log revision 1 with its date and reason.

### Visual closure (iteration 2)

All 20 revision 1 result plots opened with the Read tool (`renders_inspected: 20`): d2 `drive_a5_corners.png` (both limits drawn, 28 points above 30 mW in the 25 ohm high-gain blocks, the 15 cm points highest), `drive_a5_h3.png` (limit -25 dBc, worst near -31 dBc), `drive_a5_pinload.png` (15 pF limit, 7 pF lumped, three bands at about 14, 19 and 24 pF); d3 `drive_a4_corners.png` (200 mW line, top point 180 mW; the 100 mW line at 135 and 175 MHz agrees with Table 8), `drive_a4_h3.png`, `drive_a4_pinload.png`; d4 `coax_length_bound.png` (peak about 48.6 mW near 32 cm, the shaded 5 to 15 cm design range); d5 `drive_a5_corners.png`, `drive_a5_h3.png`, `drive_a5_pinload.png` (9.6 to 11.9 pF under 15 pF); p1 `power_a5_sma.png` and `power_a5_temperature.png` (limits 3.97, 5.0, 6.30, 8 and 10 W; markers equal the checker values, for example 4.28 W lever at 25 C and 3.26 W at the worst hot case); p2 `power_a4_sma.png`, `power_a4_temperature.png` (finding-10); p3 `power_a5_sma.png`, `power_a5_temperature.png` (titles as p1: finding-7 iii); s1 `pin_at_pa_vs_pack.png`, `pout_at_sma_vs_pack.png`, `a5_overdrive_margin.png` (bars equal the s1 table), `a5_closure_margin.png` (error bars equal the terms; the 25 C points carry finding-9). The reviewer also rendered and read the P28A discharge-temperature chart.

### Commands (iteration 2)

- Freeze: Python loop over `git rev-parse 9d01aaf:<path>` and `git rev-parse HEAD:<path>` (55 of 55 equal); `git log 9d01aaf..HEAD`; `git merge-base --is-ancestor cr/CR-012-pdr-checklist-templates HEAD` (not merged).
- Re-run: `git archive 9d01aaf tools hardware/sim/tx-pa docs/design/analysis/pa-drive-ts012.md | tar -x -C <scratchpad>/it2/exp`; author r1 folders moved to `results-author`; `CWHT_LTSPICE_LOCK_WAIT=3000 /Users/robinonsay/rust/cwht/.venv/bin/python hardware/sim/tx-pa/run_pa.py all` (exit 0); comparisons in Python (bytes, JSON without provenance, PNG arrays).
- Independent models: `<scratchpad>/it2/rv/phasor2.py`, `d4chk.py`, `power2.py`, `selfheat.py` (scratchpad only, not committed).
- Datasheets: web-fetch of the four URLs above; `pdftotext -layout` and `pdftoppm -r 200` on the fetched PDFs, SHA-256 checked against the block README.
- Record check: `/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/validate_docs.py --quiet`.

### Verdict (iteration 2)

```
ITERATION 2 (2026-09-28, HEAD d1a9a6a, product commit 9d01aaf): REVIEWER VERDICT: NEEDS CHANGES; RECORD VERDICT: NEEDS CHANGES
PRODUCT: docs/design/analysis/pa-drive-ts012.md@0d210c11, hardware/sim/tx-pa/run_pa.py@949e1b36, README.md@5e6b160c, 10 decks and runs results/2026-09-28-r1-* at 9d01aaf
FINDINGS:
- [Major] finding-1 Verified: pin load 7 pF lumped, line-fed 13.6 to 24.7 pF routed as DR-PAD-1 with the d5 option; coax modelled and bounded over every length (48.6 mW, -2.10 dB); "designed out" withdrawn; fixed-pad margin -0.73 dB; phasor model within 0.02 dB of every A5 step.
- [Major] finding-2 Verified: seven temperature cases, P28A-sourced cold feed, WP-PDR-28 hot case, direction stated, C2, C3, C8 carry temperature, closure margin with three unmodelled terms; re-solve within 0.015 W.
- [Major] finding-9 (new) Open: the 25 C ambient case takes the PA case at 25 C while the hot cases take steady key-down self-heating; with the note's own 6.1 K/W the case is 58 to 62 C and the 25 C lever margin becomes +0.17 / -0.09 dB (p1) and +0.35 / +0.08 dB (p3), -0.25 dB at worst with the terms; "closable at 25 C" and C3's 25 C figures not supported.
- [Minor] finding-3 Open: VGG still 3.5 V above the 3.08 to 3.46 V clamp; C3's figures not at its own 3.3 V; interaction direction missing (the author's disposition covered traceability only).
- [Minor] finding-4 Open: select-on-test margin +0.24 dB with the table's own steps, not +0.42 dB; reading basis and REQ-SYS-144 status unchanged.
- [Minor] finding-5, finding-6, finding-8 Open (untouched); finding-7 Open (items ii and iii).
- [Minor] finding-10 (new) Open: A4 temperature plot clips the 1.42 W worst point.
ITEMS N/A: CK-ANA-E5, E6, G2 to G4, G6 (analysis_kind simulation-deck, cascade, worst-case), CK-ANA-J1 to J3 (criticality neither)
VALUES PROPOSED: none
MEASUREMENTS: size=10 decks, 22,608 LTspice steps; blobs equal HEAD 55/55; re-run exit 0, 59/59 outputs identical; inputs re-checked against sources=4 datasheets and 1 product page; renders=20; turns=50; minutes=85 (cumulative 120 and 180); major open=1; minor open=7; iteration=2
```

## Iteration 3: delta verification of finding-9 (Major) and the revision 2 dispositions (2026-09-28, HEAD `79795e4`)

**Scope (rule C1, the last iteration).** Iteration 3 is a delta on revision 2 of the note (`5199c5c`). It verifies the fix of the iteration 2 Major finding-9 case by case, re-runs every affected deck and script, opens every changed plot, checks the new values against their sources, and checks the revision 2 dispositions of the Minor findings 3 to 8 and 10 (the author answered each; a Minor that is verified is closed here rather than carried). New findings are raised only where revision 2 introduced a defect or where a defect now decides a reported result. Product: the 57 blobs of front matter `product_files`, each equal to `git rev-parse 5199c5c:<path>` and to `HEAD:<path>` at HEAD `79795e4`; `git diff 5199c5c HEAD` on the note and `hardware/sim/tx-pa` is empty (the four later commits touch TS-012, the keying note, the receiver BPF note and review records only). The eight run-folder copies of `run_pa.py` equal the checker blob `44769c45`. No product blob is on a `cr/` branch. Checklist as before: `peer-review-checklist-analysis.md` revision A, blob `0386cc6e`, still only on `cr/CR-012-pdr-checklist-templates` (head `7784672`, not an ancestor of HEAD).

**Independence (rule C4).** This invocation authored no part of the note or its revisions, the decks, the checker, the digitizers or TS-012, and edited no product file. It changed only this record.

**Search first (charter section 11 rule 1).** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran first (queries: "pa-drive-ts012 steady key-down PA heating finding-9 INSP-114"; "thermal run ts012-r2 verdicts A5-DC module case 105.69 C 9.94 W; A4-DC AFT05 tab temperature"; "TS-012 revision 5 section 4.2 scores C5 C8 A4 A5 cost row E5 pa-drive output power REQ-SYS-012"; "TPM-015 carrier-power red threshold 5 W step unreachable at the cutoff voltage"). `grep` and `sed` then only pinned lines in files those searches or the brief named (`run_pa.py`, the power decks, the WP-PDR-28 `verdicts.md` and `bands.csv`, TS-012, `docs/plan/tpm.json`, `tools/validate_docs.py`). One `ls` of `hardware/sim/tx-pa/data` (a known path). The rustos tree was not read.

**Sources re-read by the reviewer (2026-09-28).**
- WP-PDR-28 thermal run `hardware/sim/thermal/results/2026-09-28-ts012-r2/verdicts.md`: V05 A5-DC module case "105.7 +19.9", PA dissipation at the corner 9.94 W, LTspice cross-check CASE 105.69 C; `bands.csv` row `A5-DC,case_ss,105.6945,19.8531,9.5577`. So (105.69 - 45) / 9.94 = 6.106 K/W and the band +19.9 / -9.6 K, as the note says. Run `2026-09-28-ts012-r1/verdicts.md`: A4-DC "AFT05 tab 98.2" at 5.55 W, so (98.2 - 45) / 5.55 = 9.59 K/W (the note: 9.6).
- `docs/plan/tpm.json`: TPM-015 red "above 1.5 dB, or the 5 W step unreachable at the cutoff voltage"; TPM-004 planned 60 %, red "below 55 %" and defined as final-stage drain efficiency. The note's section 7.1 comparisons read them correctly.
- tinySA Ultra specification page, https://tinysa.org/wiki/pmwiki.php?n=TinySA4.Specification (web fetch): "Absolute power level accuracy after power level calibration of +/- 2dB", as the note quotes.
- TS-012 revision 5 (`37d5824`, unchanged at HEAD) sections 4.1, 4.2, 8.3 row E5, 8.14 and 10, for the finalist effect below.

**Reproduction (CK-ANA-C4, readiness R2).** Clean `git archive 5199c5c tools hardware/sim/tx-pa docs/design/analysis/pa-drive-ts012.md` in the scratchpad; the author's eight current run folders (`r1-d2` to `r1-d5`, `r2-p1` to `r2-s1`) moved aside; then `CWHT_LTSPICE_LOCK_WAIT=3000 .venv/bin/python hardware/sim/tx-pa/run_pa.py all`: every deck rerun in LTspice through `tools/ltspice-batch.sh` (blob `88b71475`), every provenance block `exit 0` with log first line `LTspice 26.0.2 for MacOS`, no "warning" in any `.log`, power deck SHA-256 `e01cd46d9ddb0f14`, `0cb13db4b6881b42`, `e0557851af3c9c76` as the README; **exit status 1** (every check passes, criteria fail), as section 8.1 and the README say. Then `CWHT_PA_REPLOT=1 run_pa.py all --expect`: "0 verdict(s) differ from the analysis record", **exit status 0**. The verdict list printed equals the section 8.1 table row for row (d2 to s1). Thermal-law check: largest difference 7.63e-6 K (p1, p3) and 9.54e-6 K (p2) at 6.4 V. Against the committed outputs, **61 of 61 files agree**: decks and `result.md` byte-identical, `result.json`, `corners.json`, `coax_*_steps.json` and `verdicts.json` identical after removing the wrapper provenance, all PNGs pixel-identical (image arrays equal), and the script copies.

**Reviewer script (scratchpad, not product):** `power3.py`, written for this iteration: a fixed-point solve of Vd = Vp - Rf (Ibus + P / (eta Vd)) together with Tc = Ta + Rth (P (1/eta - 1) + Pin) and the PA factor, on the digitized CSVs (median-binned, linear interpolation; not the deck tables and not LTspice), over the same corners and the nine temperature cases. `extra.py` (open-loop case temperature and the HZ-003 dissipation figures) and `cross.py` (5 W and 3.97 W crossings) use the same solver.

### Verification of finding-9 (Major), case by case (rule C7)

| Finding | Case the finding named | Check at `5199c5c` | Result |
|---|---|---|---|
| finding-9 | The 25 C ambient case took the PA case at 25 C while the hot cases took steady key-down self-heating | `TC_CASES` now has 25 C key-down rows `t25a` / `t25b` with the PA case solved in the deck (`Btc tc 0 V=if(tcfix>-500,tcfix,ta+rth*(V(pmod)*(1/eta-1)+pinw_pa))`, `rth` 6.11 A5, 9.6 A4) and `kt(V(tc))` on the output, the same law as the +45 C key-down rows. The feed levels at key-down (`rf` table 0.27562 / 0.39358 / 0.53392 at 25 C) and the copper term (`cu` = 0.00195 x (Ta + 44 - 25): 0.0858, 0.01755, 0.1248, and -0.06825 for the -10 C soak) follow the same state. The datasheet-condition row is kept, labelled informative. Deck lines read; reviewer recomputation of `cu` equal | Yes |
| finding-9 | "the case at 25 C ambient ... is 58 to 62 C at the lever corner" | Note: 57 to 60 C. `power3.py`: 58.6 C (-0.005 dB/K) and 56.7 C (-0.015 dB/K) at the p1 lever corner, 60.0 and 58.0 C in p3; nominal 45.6 / 44.8 C; -10 C key-down lever 23.4 C (so the "no gain below 25 C" rule gives 0 dB, conservative); +45 C 77.5 / 74.8 C (the note: 75 to 79 C); A4 nominal 43.7 / 43.0 C (the note: 43 to 44 C). The self-consistency check in the checker holds to 7.6e-6 K at 6.4 V | Yes |
| finding-9 | Rerun p1, p3 and s1 | New runs `r2-p1`, `r2-p3`, `r2-s1` (and `r2-p2`), reproduced by the reviewer's LTspice re-run (above). `power3.py` against the note's section 4.4 tables (p1 nominal, lowest, lever, lever at the LPF worst case, every lever at its best; p3 the same, eight cases each; 72 figures): every figure within 0.016 W (0.02 dB). Examples at 25 C key-down: p1 nominal 4.085 / 3.937 W (note 4.09 / 3.94), lowest 3.186 W (3.19), lever 3.652 / 3.449 W (3.66 / 3.46), every lever at its best 4.363 / 4.092 W (4.37 / 4.09); p3 lever 3.797 / 3.585 W (3.81 / 3.59); A4 nominal 3.059 W (3.06), lowest 1.693 W (1.69); open loop at 8.4 V 9.40 W (9.38) and 10.69 W at the -10 C start (10.68) | Yes |
| finding-9 | Restate 5 (c), 5 (d), the A5 verdict line, C3 and C8 | 5 (c): -0.19 to -0.60 dB, -0.12 to -0.75 dB with the terms (-0.15 / +0.07 dB, the sum of the three `CLOSURE_UNC` rows), -1.29 to -1.71 dB at the LPF worst case, nominal +0.13 / -0.04 dB: recomputed from the tables, equal. 5 (d): -0.34 / -0.17 dB at -10 C, -0.36 to -1.21 dB hot, nominal under 3.97 W in every hot case but p3 at -0.005 dB/K (+0.03 dB): equal. Verdict line and section 4.4: "closable before the order at 25 C" withdrawn. C3 carries no REQ-SYS-012 figure and states the VGG window it requires. C8 covers every steady key-down case with a room-temperature bench reading (X-6). C4 re-quantified (-0.36 to -0.60 and -0.19 to -0.44 dB at the LPF median; "+1/-1.5 dB" covers every key-down case with the terms, worst -1.36 dB, not the LPF worst case to -2.51 dB or the datasheet-minimum module hot, -2.14 dB; reviewer 2.422 W, -2.14 dB) | Yes |
| finding-9 | The A5 against A4 comparison does not change direction | Section 5: A5 nominal 4.09 W against A4 3.06 W (1.26 dB), lowest 3.19 against 1.69 W (2.76 dB), recomputed. Direction unchanged | Yes |

The Rth_ca values are read correctly from WP-PDR-28 (sources above) and their use is stated as an estimate with its band; the one residual (Rth taken from a 9.94 W, 8.4 V operating point and applied at 5.5 to 6.6 W) is observation O-10, not decisive.

**Result: finding-9 Verified.**

### Minor findings: the revision 2 dispositions checked

| Finding | Check at `5199c5c` | Result |
|---|---|---|
| finding-3 | Deck `kv0` to `kv3` at 3.08, 3.27, 3.30, 3.46 V relative to 3.5 V; nominal at 3.27 V, highest and open loop at 3.46 V, lever at 3.30 V; no figure at 3.5 V (note and plots: legends say VGG 3.27 / 3.3 / 3.46 V). C3 states the 3.30 to 3.50 V window at 6.4 V. Limitation 2 gives both directions (VGG factor at 7.2 V pessimistic; drive factor at low VGG and 5.4 mW optimistic; net unknown) | Verified |
| finding-4 | Pad set: reviewer ABCD of the 14 E24 pads gives 13.48 to 22.04 dB, return loss 25.4 to 42.6 dB, largest adjacent gap 0.766 dB, all as tabulated. Band: 0.17 + 0.385 + 1.0 + 0.3 = 1.855 dB about 17.3 mW, so 11.27 to 26.5 mW, margin 10 log(30 / 26.5) = +0.54 dB and +0.53 dB above 10 mW; break-even 10 log(30 / 17.3) - 0.855 = 1.54 dB; tinySA +/-2 dB -0.46 dB; RSS +1.26 dB (the note: +1.27, rounding). The reading is an allocation with its sensitivity, C1 depends on a 17 mW probe characterization and on the Proposed REQ-SYS-144 delta. The tinySA figure re-read at its source | Verified |
| finding-5 | `run_pa.py all` exits 1 and `--expect` exits 0 (reviewer runs); exit 2 on a failed check and 3 on a changed verdict in `main()`; README and section 8.1 state them | Verified |
| finding-6 | Header "Serves" and section 7.1 name TPM-015, TPM-004, HZ-001, HZ-003, the risk rows and TS-012 `7d0d450`. TPM thresholds as `tpm.json`; A5 lowest at 25 C key-down 10 log(3.19 / 5) = -1.95 dB (the note: -2.0), A4 -4.71 dB. HZ-003 figures reproduced by `extra.py`: hottest A5 corner at 6.4 V 6.65 W and 65.6 C (25 C), 6.45 W and 84.4 C (+45 C); open loop at 8.4 V and +45 C 109.1 C at 10.49 W (the note: 6.6 W / 66 C, 6.4 W / 84 C, 109 C / 10.5 W) | Verified |
| finding-7 | (ii) d2 and d5 `result.md` read "taken over all 810 corners: **FAIL** (587 corners inside the window, ...)"; the empty "0.00 dB larger" line is gone. (iii) p3 plots titled "A5, select-on-test drive pad (in-service band of s1)", p1 "drive as designed" | Verified |
| finding-8 | Section 6 item 4 states the departure, the Rev. F values and the direction per result. Reviewer: 24.1 - 2.4 x (46 / 900) = 0.12 dB (linear in frequency) and 2.4 x log10(1.46) = 0.39 dB (linear in log frequency) below 24.1 dB; times the 0.08 dB/dB module slope, the -0.03 dB closure term | Verified |
| finding-10 | `power_a4_temperature.png` y axis from about 0.5 W; the 1.03 W worst point is on the plot | Verified |

### New findings (iteration 3)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-11"></a>finding-11 | reviewer | Minor | CK-ANA-D2 | note section 4.4, paragraph after the closure-margin table; note section 2 "The deck checks itself"; `run_pa.py` thermal-law check | Two statements introduced by revision 2 do not match the results. (i) Section 4.4 says the every-lever stack "fails in the +45 C, -0.015 dB/K cases (p1 -0.16 and -0.45 dB; p3 +0.02 and -0.25 dB)", but p3 at +45 C key-down, -0.015 dB/K is +0.02 dB (3.99 W; reviewer 3.984 W, +0.01 dB), a pass before the unmodelled terms, and section 5 (e) correctly says "p3: all but the 100 C bound at -0.015 dB/K". (ii) Section 2 says the checker recomputes the thermal law "for every key-down corner"; `run_pa.py` checks it only at the 6.4 V point of each corner (its own verdict detail says "at 6.4 V"), so the 8.4 V open-loop case temperatures the note quotes (109 C in section 4.4 and the HZ-003 request) are outside the check. The reviewer's independent solve reproduces 109.1 C, so no figure changes. Fix: say "fails, or passes by +0.02 dB before the unmodelled terms" in (i), and "for every key-down corner at 6.4 V" in (ii) (or extend the check to the sweep) | Open | Pending | |

### Per-case results (iteration 3; the cases finding-9 and revision 2 moved; the drive cases C-1 to C-11 of iteration 2 are unchanged and were re-run identical)

Values are the checker's (all estimates), reproduced by the reviewer's LTspice re-run; the re-check column is `power3.py`.

| Case | Condition | Governing id and limit | Result (checker output) | Margin with sign | Uncertainty | Reviewer re-check | Finding ids |
|---|---|---|---|---|---|---|---|
| C-12 | A5 at 6.4 V, 25 C key-down, lowest corner, typical module, LPF median | REQ-SYS-012: at least 3.972 W | 3.19 W (-0.005 dB/K), 3.04 W (-0.015): FAIL | -0.95, -1.16 dB | PA coefficient, graph reads | 3.186, 3.038 W | none |
| C-13 | A5 lever corner (C2, C3 at 3.30 V), fixed pad, 25 C key-down, LPF median | REQ-SYS-012 | 3.66 / 3.46 W (case 59 / 57 C): FAIL | -0.36 / -0.60 dB (-0.51 to -0.29, -0.75 to -0.53 with the terms) | as C-12 | 3.652 / 3.449 W, 58.6 / 56.7 C | none |
| C-14 | Same, select-on-test drive (p3) | REQ-SYS-012 | 3.81 / 3.59 W: FAIL | -0.19 / -0.44 dB | as C-12 | 3.797 / 3.585 W | none |
| C-15 | A5 lever corner, -10 C key-down | REQ-SYS-012 with REQ-SYS-114 | 3.68 W (p1), 3.82 W (p3): FAIL | -0.34, -0.17 dB | cell graph read; no PA cold gain | 3.666, 3.814 W; case 23.4 C | none |
| C-16 | A5 lever corner, +45 C, four cases | REQ-SYS-012 with REQ-SYS-114 | 3.00 to 3.52 W (p1), 3.14 to 3.66 W (p3): FAIL | -1.21 to -0.53, -1.03 to -0.36 dB | PA coefficient | 2.999 to 3.511, 3.126 to 3.650 W | none |
| C-17 | A5 lever corner, LPF worst case (1.86 dB) | REQ-SYS-012 | 2.31 to 3.11 W (p1), 2.41 to 3.24 W (p3): FAIL | down to -2.36 dB | LPF r13 search (Draft) | 2.303 to 3.103, 2.400 to 3.236 W | none |
| C-18 | A5 every design lever at its best | REQ-SYS-012 | p1 3.58 to 4.61 W, p3 3.75 to 4.82 W | p1 -0.45 to +0.65 dB; p3 -0.25 to +0.84 dB; p3 +45 C -0.015 dB/K +0.02 dB | as C-12; the 0.5 dB loss no LPF build meets | 3.583 to 4.607, 3.747 to 4.811 W | finding-11 (i) |
| C-19 | A5 datasheet-minimum module with C2 and C3, LPF median | REQ-SYS-012 | 2.99 W at 25 C key-down, 2.43 W worst bound | -1.23, -2.14 dB | uniform 6.5 W scale | 2.990, 2.422 W | none |
| C-20 | A5 open loop at 8.4 V, VGG 3.46 V, highest corner | RA07M1317M 8 W stability, 10 W rating | 9.38 W (25 C key-down), 10.68 W (-10 C start, +0.53 dB): FAIL both | -0.69 dB to 8 W; -0.29 dB to 10 W | cold coefficient estimate | 9.40, 10.69 W; case 109.1 C at +45 C | finding-11 (ii) |
| C-21 | A4 at 6.4 V, 25 C key-down, nominal and lowest; worst bound | REQ-SYS-012 | 3.06 / 1.69 W; 2.44 / 1.35 W: FAIL | -1.13 / -3.70 dB | estimated n and match loss (Low) | 3.059 / 1.693, 2.438 / 1.346 W | none |
| C-22 | Nominal-corner crossings, 25 C key-down | REQ-SYS-012; TPM-015 | A5 5.0 W from 7.15 V; A4 3.97 W from 7.3 V, 5.0 W from 8.25 V (first 0.05 V grid point) | n/a | grid step | 7.126 V; 7.298 V, 8.201 V (interpolated): consistent with the grid convention | none |
| C-23 | A5 select-on-test drive in service (s1) | TS-012: 10 to 30 mW | 11.3 to 26.5 mW at +/-1.0 dB: PASS; +/-2 dB: FAIL | +0.54 dB; -0.46 dB | reading allocation | recomputed (finding-4 row) | none |

### Findings (iteration 3; current state of every finding of this record)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| finding-1 | reviewer | Major | CK-ANA-G1-3, B2, E3, A6 | decks, note sections 2, 4.2, 5, 7 | See iteration 1 and the iteration 2 verification table | Verified (iteration 2) | n/a | |
| finding-2 | reviewer | Major | CK-ANA-F1, A5, G7-2, B6, E3 | note sections 3.1, 4.4, 5, 6, 7; power decks | See iteration 1 and the iteration 2 verification table | Verified (iteration 2) | n/a | |
| finding-3 | reviewer | Minor | CK-ANA-A5, B1 | note sections 2, 4.4, 6 item 2, 7 C3 | See iteration 1; revision 2 disposition checked above | Verified (iteration 3, revision 2 at 5199c5c) | n/a | |
| finding-4 | reviewer | Minor | CK-ANA-F4, E3, A6 | note sections 4.2, 5 (a), 7 C1 | See iteration 1; revision 2 disposition checked above | Verified (iteration 3) | n/a | |
| finding-5 | reviewer | Minor | CK-ANA-E4 | `run_pa.py` `main()`, `EXPECTED` | See iteration 1; exit 1 and `--expect` exit 0 reproduced | Verified (iteration 3) | n/a | |
| finding-6 | reviewer | Minor | CK-ANA-A1, A2, E2, H1, H2 | note header, section 7.1 | See iteration 1; revision 2 disposition checked above | Verified (iteration 3) | n/a | |
| finding-7 | reviewer | Minor | CK-ANA-D2, I2 | d2 and d5 `result.md`; p3 plot titles | See iteration 1; items ii and iii fixed, item i moot at iteration 2 | Verified (iteration 3) | n/a | |
| finding-8 | reviewer | Minor | CK-ANA-B1 | note section 6 item 4 | See iteration 1; revision 2 disposition checked above | Verified (iteration 3) | n/a | |
| finding-9 | reviewer | Major | CK-ANA-G7-2, E3, B6, A5 | `TC_CASES`, power decks; note sections 2, 3.1, 4.4, 5, 7 | See iteration 2 and the verification table above | Verified (iteration 3) | n/a | |
| finding-10 | reviewer | Minor | CK-ANA-I2 | `power_a4_temperature.png` | See iteration 2 | Verified (iteration 3) | n/a | |
| finding-11 | reviewer | Minor | CK-ANA-D2 | note sections 2 and 4.4 | See the new findings table above | Open | Pending | |

### Observations (not findings)

- O-10. Rth_ca comes from the WP-PDR-28 corner (9.94 W at 8.4 V with the ALC backing off, the whole box heated) and is applied at 5.5 to 6.6 W at 6.4 V. With natural convection the effective case-to-ambient resistance rises somewhat at lower dissipation, while the other box heat in the ratio overstates it; the net is within the run's +19.9 / -9.6 K band. At +45 C the 100 C bound covers the hot side. At 25 C there is no bound row: scaling the lever corner's 34 K rise by the full +33 % band adds about 11 K, -0.17 dB at -0.015 dB/K, so the p1 lever figure would be about -0.77 dB (-0.92 dB with the terms), still inside the "+1/-1.5 dB" delta C4 and TS-012 carry. No verdict changes; C8's bench reading measures it.
- O-11. `r2-p1` `result.md` reads "above 10 W (maximum rating) from nowhere below 8.4 V (reference)", machine wording for "not reached at or below 8.4 V". Harmless.
- O-12. The every-lever p3 margin at +45 C, -0.015 dB/K (+0.02 dB) is smaller than the graph-read term alone (+/-0.07 dB); section 5 (e) states the figure before the terms, as the note defines it.

### Cross items (iteration 3, returned to Claude as lead SE)

- X-7. TS-012 revision 5 section 4.2, row C5-A5, reads "-0.17 to -1.21 dB with every lever". In the note that range is the C2 and C3 lever figure over the key-down cases (p3 -10 C to p1 +45 C bound); "every design lever at its best" is -0.45 to +0.84 dB (section 5 (e)). The score does not depend on the wording; a request to the TS-012 author for revision 6.
- X-8. TS-012 section 10 names "a re-review of the PA drive ... changes a figure this study scores on" as a revisit condition, and INSP-110 X-13 names PA drive iteration 3 as pending for C5-A5. Iteration 3 changes no figure TS-012 revision 5 uses (finalist effect below); the lead SE can record that the condition did not trigger.

### Finalist effect (TS-012 revision 5)

The final numbers change nothing TS-012 revision 5 relies on for A4 against A5. Section 4.2 **C5-A5 = 4** rests on this note's nominal 4.09 W and lowest 3.19 W at 6.4 V, 25 C key-down (reviewer 4.085 and 3.186 W), the -0.17 to -1.21 dB C2 and C3 range (reproduced) and 223 of 810 fixed-pad corners outside 10 to 30 mW (195 + 28, re-run identical); **C5-A4 = 2** rests on 3.06 W nominal and 1.69 W lowest (reviewer 3.059 and 1.693 W) and the lowest corner short of 3.97 W at every pack voltage (confirmed). **C8** (A5 1, A4 2) rests on the WP-PDR-28 junction ranges, not on this note; the note only borrows WP-PDR-28's case-to-ambient resistance and returns no figure to C8. **Row E5** (c), 5 to 15 cm of RG-316 or RG-174 soldered at both ends (USD 1.00 to 4.00, estimate), and D-7's pads from owned resistors are unchanged by revision 2 (the coax lengths and the 14-pad set are as E5 and D-7 carry them), so C1 and C2 do not move. The ranking A4 315, A5 270 stands.

### Checklist items changed at iteration 3

Now Yes: CK-ANA-A1, A2, E2, H1, H2 (finding-6), A5 and B1 (findings 3, 8), A6 and F4 (finding-4), B6, E3 and G7-2 (finding-9, finding-4), E4 (finding-5), I2 (findings 7 iii and 10). Still No: CK-ANA-D2 (finding-11). CK-ANA-B5: Yes, `power3.py` agrees with every section 4.4 figure within 0.016 W and with the A4, open-loop and HZ-003 figures. CK-ANA-C1 to C5: Yes, with the re-run above (LTspice 26.0.2, wrapper `88b71475`, exit 1 and `--expect` exit 0, 61 of 61 outputs identical). CK-ANA-H3: Yes, change log revision 2 with its date and reason.

### Visual closure (iteration 3)

All 11 revision 2 result plots opened with the Read tool (`renders_inspected: 11`): p1 `power_a5_sma.png` (limits 3.97, 5.0, 6.30, 8 and 10 W; nominal crosses 5.0 W near 7.13 V; open-loop line over 8 W from about 7.2 V and over 10 W from about 8.1 V) and `power_a5_temperature.png` (markers equal the section 4.4 table; tick labels give the case temperatures 25 / 59 / 57 / 23 / 78 / 75 / 100 / 100 C); p3 the same two, titled "select-on-test drive pad" (finding-7 iii); p2 `power_a4_sma.png` (nominal crosses 3.97 W near 7.3 V and 5.0 W near 8.2 V) and `power_a4_temperature.png` (1.03 W worst point shown: finding-10); s1 `a5_closure_margin.png` (both LPF states; bars and error bars equal the closure table; datasheet-minimum -1.23 dB at 25 C key-down), `a5_overdrive_margin.png` (bars equal the s1 table), `a5_sot_reading_sensitivity.png` (break-even at 1.54 dB, the +/-2 dB tinySA line at -0.46 dB), `pin_at_pa_vs_pack.png` (bands 5.4 to 35.5 mW and 45.8 to 180.0 mW; select-on-test hatch 11.3 to 26.5 mW) and `pout_at_sma_vs_pack.png` (25 C key-down, -0.005 dB/K curves of both finalists). Every plot has axes with units, the limits with their ids and a legend. The d2 to d5 plots are the unchanged blobs opened at iteration 2.

### Commands (iteration 3)

- Freeze: Python loop over `git rev-parse 5199c5c:<path>` and `git rev-parse HEAD:<path>` (57 of 57 equal); `git diff --stat 5199c5c HEAD -- hardware/sim/tx-pa docs/design/analysis/pa-drive-ts012.md` (empty); `git merge-base --is-ancestor cr/CR-012-pdr-checklist-templates HEAD` (not merged).
- Re-run: `git archive 5199c5c tools hardware/sim/tx-pa docs/design/analysis/pa-drive-ts012.md | tar -x -C <scratchpad>/it3/exp`; the eight current run folders moved to `results-author`; `CWHT_LTSPICE_LOCK_WAIT=3000 /Users/robinonsay/rust/cwht/.venv/bin/python hardware/sim/tx-pa/run_pa.py all` (exit 1); `CWHT_PA_REPLOT=1 ... run_pa.py all --expect` (exit 0); `compare.py` (bytes, JSON without provenance, PNG arrays; 61 of 61).
- Independent models: `<scratchpad>/it3/rv/power3.py`, `extra.py`, `cross.py`; pad ABCD in a one-off Python snippet (scratchpad only, not committed).
- Sources: `sed` of the WP-PDR-28 `verdicts.md` (r1, r2) and `bands.csv`; `docs/plan/tpm.json` read in Python; web fetch of the tinySA specification page.
- Record check: `/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/validate_docs.py --quiet`.

### Verdict (iteration 3)

```
ITERATION 3 (2026-09-28, HEAD 79795e4, product commit 5199c5c): REVIEWER VERDICT: APPROVED; RECORD VERDICT: NEEDS CHANGES (held: the applied analysis template is only on cr/CR-012)
PRODUCT: docs/design/analysis/pa-drive-ts012.md@02852058, hardware/sim/tx-pa/run_pa.py@44769c45, README.md@8ce85567, 10 decks and runs results/2026-09-28-r1-d2 to -d5 and -r2-p1 to -r2-s1 at 5199c5c
FINDINGS:
- [Major] finding-9 Verified: every low-bound case is steady key-down with the PA case solved from the dissipation (A5 6.11 K/W, A4 9.6 K/W, both read at WP-PDR-28); lever corner 57 to 60 C at 25 C; 72 section 4.4 figures reproduced within 0.016 W by an independent solve; "closable at 25 C" withdrawn; 5 (c), 5 (d), C3, C4, C8 restated and recomputed.
- [Major] finding-1, finding-2: Verified at iteration 2 (unchanged).
- [Minor] finding-3 to finding-8 and finding-10 Verified (VGG clamp levels; E24 pad set 0.766 dB gap and the reading allocation with break-even 1.54 dB; exit 1 and --expect 0; TPM, hazard and risk requests; wording and titles; GVA-84+ departure; A4 plot range).
- [Minor] finding-11 (new) Open: section 4.4 calls the p3 +0.02 dB every-lever case a failure; section 2 says the thermal law is checked at every key-down corner, the checker checks 6.4 V only. No figure changes.
ITEMS N/A: CK-ANA-E5, E6, G2 to G4, G6 (analysis_kind simulation-deck, cascade, worst-case), CK-ANA-J1 to J3 (criticality neither)
VALUES PROPOSED: none
FINALIST EFFECT: none. TS-012 revision 5 C5-A5 4, C5-A4 2, C8 (WP-PDR-28, not this note) and row E5 (c) rest on figures this iteration reproduces; A4 315, A5 270 stands.
MEASUREMENTS: size=10 decks, 39,780 LTspice steps re-run; blobs equal HEAD 57/57; re-run exit 1 (as recorded), --expect exit 0, 61/61 outputs identical; inputs re-checked against sources=WP-PDR-28 r1 and r2, tpm.json, tinySA specification; renders=11; turns=55; minutes=90 (cumulative 175 and 270); major open=0; minor open=1; iteration=3
```
