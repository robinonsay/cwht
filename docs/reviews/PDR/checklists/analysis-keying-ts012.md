---
# Peer-review record front matter (charter section 5; docs/process/01-lifecycle-and-reviews.md section 13;
# docs/process/08-agent-briefing.md sections 3.4 and 3.5). Independent review of the WP-PDR-22 pre-order keying
# envelope and key-click analysis of the TS-012 finalists A4 and A5, iteration 1 at freeze commit 4ea4607 (rule C2).
# Checklist applied: docs/templates/peer-review-checklist-analysis.md revision A as on its CR-012 branch
# (cr/CR-012-pdr-checklist-templates at 7784672, blob 0386cc6e). tools/validate_docs.py requires the checklist field to
# name a template that exists on main, so the field names peer-review-checklist-design revision B and
# checklist_analysis records the template actually applied, as INSP-056, INSP-083 and INSP-114 did.
# id: the brief assigned no id. INSP-116 is above every id on main (HEAD 35fc7ee), on every cr/ branch and in the
# working tree at the time of filing (INSP-114 is the highest in use). If a parallel reviewer filed INSP-116 first, the
# lead SE renumbers this record.
# Filed by the lead SE on 2026-09-28 from the reviewer's own text (its later, scratch-copy Write, which differs from
# the first only in HEAD citations and effort counts): the harness refused the reviewer's Write of this new file
# ("Subagents should return findings as text"). Content is verbatim except the id, reassigned from INSP-115 to
# INSP-116 because review:lpf-1 also took INSP-115.
id: INSP-116
checklist: peer-review-checklist-design
checklist_revision: B
checklist_analysis: "docs/templates/peer-review-checklist-analysis.md@0386cc6e78da65578b1cce8b2f793cd3db224921 (revision A, CR-012 branch head 7784672)"
checklist_file: docs/reviews/PDR/checklists/analysis-keying-ts012.md
product: docs/design/analysis/keying-ts012.md
# product_commit (iteration 3): be86c02, note revision 2. Every blob in product_files equals git rev-parse
# be86c02:<path> and HEAD:<path> at HEAD 79795e4 (66 of 66): the note, README, checker, expected_states.json, the 14
# decks and every png, csv and json of the ten r2 runs and the r2 summary. The r1 run folders and the revision 0 runs
# stay in the tree, superseded, with the blobs of product_files_iteration_2 and product_files_iteration_1. LTspice
# .log and .raw are not listed; the reviewer's re-run regenerated them. Iteration 2 was at e9f1440 (note revision 1).
product_commit: "be86c02f97e26dafaa6ebf94ee93e1f0c2223732"
product_files: ["docs/design/analysis/keying-ts012.md@5121cc90807d8a5b56b1ae93a20074e33a2154f2", "hardware/sim/tx-keying/README.md@0dae6167945b5d00d770fe679f85f808d6248c89", "hardware/sim/tx-keying/keying_run.py@5db0ef28382f2085b744672fee7ebedb6b41c620", "hardware/sim/tx-keying/expected_states.json@230a13c38875552f97593fc38bc5edbadd8764c8", "hardware/sim/tx-keying/det_char.cir@059595d7034f385a08dc8a84654d01c8692f9485", "hardware/sim/tx-keying/det_char_biased.cir@5911e4396425b17bf4b48c4146e3b0b898b1c2c4", "hardware/sim/tx-keying/keying_a4_asis.cir@f6cc1d9e6974cff9120430061980e1e3b8a5d72d", "hardware/sim/tx-keying/keying_a4_fix.cir@b1fb92ec724e69d37318dec235d1af51cba48aef", "hardware/sim/tx-keying/keying_a4_mitig.cir@d209bbd419e0b106375b7a2856ef64c8af2702a2", "hardware/sim/tx-keying/keying_a4_sens.cir@89710e115480b351b804b33ad731d0f20e560e9a", "hardware/sim/tx-keying/keying_a4_sweep0.cir@9a6e1650b7d9c54ef3566933953f6018232d54de", "hardware/sim/tx-keying/keying_a4_sweep1.cir@23612e8457cbfbeca7b5b63b25e47602a83165da", "hardware/sim/tx-keying/keying_a5_asis.cir@9265effb2026c8f68ed45c6d99a61bef62b921d1", "hardware/sim/tx-keying/keying_a5_fix.cir@f79fb1f8ea86043df7c411414d7dee5bc540fd7a", "hardware/sim/tx-keying/keying_a5_mitig.cir@fd4ec933178342d196e2c5943736094e54dc77a2", "hardware/sim/tx-keying/keying_a5_sens.cir@16cf230adef090378516cccae1ccddfb7210858d", "hardware/sim/tx-keying/keying_a5_sweep0.cir@d517774461229912dde02207ce0cad5f00723a61", "hardware/sim/tx-keying/keying_a5_sweep1.cir@a442e964141496efd4d6bc12923cbfc9947bda47", "hardware/sim/tx-keying/results/2026-09-28-r2-a4-asis/envelope.png@7008acbb08e7372e57e33f42404a35f01aa30412", "hardware/sim/tx-keying/results/2026-09-28-r2-a4-asis/keyup_level.png@a229f99f6335e92cba617e7132f1c6dbcfe05441", "hardware/sim/tx-keying/results/2026-09-28-r2-a4-asis/result.csv@e23530e583f1a5e3ee21bec9343e79a680626572", "hardware/sim/tx-keying/results/2026-09-28-r2-a4-asis/result.json@9df45bcab2b8556aa89b16b83816d96b61ad9d2a", "hardware/sim/tx-keying/results/2026-09-28-r2-a4-asis/spectrum.png@4c3c211d1eba61e22556e5d1bd1c4195ef666b5d", "hardware/sim/tx-keying/results/2026-09-28-r2-a4-fix/corners.png@91080b563e55979de0d7fa04bfc43c9a7c25b52c", "hardware/sim/tx-keying/results/2026-09-28-r2-a4-fix/envelope.png@1e824337deafeac088cc0f30396c61b9ecb7c76d", "hardware/sim/tx-keying/results/2026-09-28-r2-a4-fix/keyup_level.png@aa79ca0b2496accedce2c0e8626562107e31f4bd", "hardware/sim/tx-keying/results/2026-09-28-r2-a4-fix/result.csv@337a04468edb186d672474458bf1c88493b88941", "hardware/sim/tx-keying/results/2026-09-28-r2-a4-fix/result.json@d333c75928965b49aa36a9530ad30846f66170c3", "hardware/sim/tx-keying/results/2026-09-28-r2-a4-fix/spectrum.png@d146b21ea4530bd5bf536fd540e6d038bb8bfb8b", "hardware/sim/tx-keying/results/2026-09-28-r2-a4-fix/t1090.png@ff4f31f6c4c2309960cc4c29e6697d5633dd5e8e", "hardware/sim/tx-keying/results/2026-09-28-r2-a4-sens/result.csv@30c10925be55c6337c5a21348a1fbff335fbae6d", "hardware/sim/tx-keying/results/2026-09-28-r2-a4-sens/result.json@384e76b0c15d344eb5629bc321fa01901503e1c5", "hardware/sim/tx-keying/results/2026-09-28-r2-a4-sens/sens_curves.png@20cff70a6c77ec30529dbb294a2d29249e69c64a", "hardware/sim/tx-keying/results/2026-09-28-r2-a4-sens/sens_windows.png@e0224a0a65e2d8398377f7abe17562b3a392482e", "hardware/sim/tx-keying/results/2026-09-28-r2-a4-sweep0/result.csv@ce90610c5cbfe7500eb2b1500a25b5e14dd6af0f", "hardware/sim/tx-keying/results/2026-09-28-r2-a4-sweep0/result.json@1a64c649a89b4bc414820db1c18877527776d450", "hardware/sim/tx-keying/results/2026-09-28-r2-a4-sweep0/window.png@d9849660fb84386675fbf6ef43f910eb9ceb32dd", "hardware/sim/tx-keying/results/2026-09-28-r2-a4-sweep1/result.csv@b5706560761eddfc9394d04bd4df4bfc057c9e93", "hardware/sim/tx-keying/results/2026-09-28-r2-a4-sweep1/result.json@7dbb3a0d7cb56ddecd9791a0effa562c56ceeae9", "hardware/sim/tx-keying/results/2026-09-28-r2-a4-sweep1/window.png@c033d0411b01cbb8bec1ce9612fbb99163b4ae32", "hardware/sim/tx-keying/results/2026-09-28-r2-a5-asis/envelope.png@83373e0d227e06ea70206b050c2778444632467b", "hardware/sim/tx-keying/results/2026-09-28-r2-a5-asis/keyup_level.png@0e7d74973f26cdf7badf3b382bc5cd1e65a8af03", "hardware/sim/tx-keying/results/2026-09-28-r2-a5-asis/result.csv@c9bb2586b1651fe4685c6ea1f2c81d36a2463b80", "hardware/sim/tx-keying/results/2026-09-28-r2-a5-asis/result.json@ecf678fa2d1420d1dfd5975ae6f59913f0843eac", "hardware/sim/tx-keying/results/2026-09-28-r2-a5-asis/spectrum.png@176f20133e8d6f861b9f066da9c7e9a0ad5a8bc6", "hardware/sim/tx-keying/results/2026-09-28-r2-a5-fix/corners.png@e8a386d529e88fbfaaa50f5b165930b9a5642fa5", "hardware/sim/tx-keying/results/2026-09-28-r2-a5-fix/envelope.png@7869f1273f26906347bba87220518fdf87397093", "hardware/sim/tx-keying/results/2026-09-28-r2-a5-fix/keyup_level.png@1d378cf98768a8ac4942d479d09ce60d6c974647", "hardware/sim/tx-keying/results/2026-09-28-r2-a5-fix/result.csv@5920385778e1c81442c60b4b81dc9b1cdb6cd2fe", "hardware/sim/tx-keying/results/2026-09-28-r2-a5-fix/result.json@e8a0e6f6d545df1fb7af638ba58b212fdd7154ad", "hardware/sim/tx-keying/results/2026-09-28-r2-a5-fix/spectrum.png@d8308e4b68a781e3faff6416e621dfd88fb15139", "hardware/sim/tx-keying/results/2026-09-28-r2-a5-fix/t1090.png@69a87c8ee105dcfe3de1921cf3d4b166cfe4e5e4", "hardware/sim/tx-keying/results/2026-09-28-r2-a5-sens/result.csv@40316f289049ad94cc12fb9bb9938d5bb3cb23cd", "hardware/sim/tx-keying/results/2026-09-28-r2-a5-sens/result.json@87efc1dde86ba1c841c71f358ec40486896100f5", "hardware/sim/tx-keying/results/2026-09-28-r2-a5-sens/sens_curves.png@b781b185a96247cd1230cadbac12105224bc3a7c", "hardware/sim/tx-keying/results/2026-09-28-r2-a5-sens/sens_windows.png@aaa19a9fc9635ef85c07bfa7a05a5e9fe92cefe3", "hardware/sim/tx-keying/results/2026-09-28-r2-a5-sweep0/result.csv@e13faa26334ec7a664ac1b16d29efc6e159cfa91", "hardware/sim/tx-keying/results/2026-09-28-r2-a5-sweep0/result.json@f08180460e651b73b85523602540fa6f9a2f6a92", "hardware/sim/tx-keying/results/2026-09-28-r2-a5-sweep0/window.png@38a2e52672d650251311d2efaa824d5f63bea2a3", "hardware/sim/tx-keying/results/2026-09-28-r2-a5-sweep1/result.csv@5cf2d34a14c03265859bddcb3bb0982afa1f8784", "hardware/sim/tx-keying/results/2026-09-28-r2-a5-sweep1/result.json@8fbdf1856d587b5680b31f71d0e7744723120c13", "hardware/sim/tx-keying/results/2026-09-28-r2-a5-sweep1/window.png@a449483588cb776cfda1b69827185b749bf222c3", "hardware/sim/tx-keying/results/2026-09-28-r2-summary/pwm_ripple.png@df5c4a9e81e19c8a711e450fea599346f92ebc1f", "hardware/sim/tx-keying/results/2026-09-28-r2-summary/summary.json@c57000c3893a2ef12acfe72a8fdb6a41fabb3e28", "hardware/sim/tx-keying/results/2026-09-28-r2-summary/summary.png@3401f226ce8909854294c5bcd45bbc7e16e3c82b", "hardware/sim/tx-keying/results/2026-09-28-r2-summary/windows.png@23630a21fb9c156845d865b802f75d87de55d0e8"]
# product_files_iteration_2: the 55 blobs of iteration 2 at e9f1440 (note revision 1, runs r1-*), unchanged at HEAD
product_files_iteration_2: ["docs/design/analysis/keying-ts012.md@934ff1f4ce68473a8b3f446b11c4f93c9a42d6fc", "hardware/sim/tx-keying/README.md@c4c7a3f8dd17f7a2b11e5b1a4c51a6ef8f3976c2", "hardware/sim/tx-keying/keying_run.py@5b241f55bda52b9145320b1e9bf92512abc1cdba", "hardware/sim/tx-keying/det_char.cir@059595d7034f385a08dc8a84654d01c8692f9485", "hardware/sim/tx-keying/det_char_biased.cir@5911e4396425b17bf4b48c4146e3b0b898b1c2c4", "hardware/sim/tx-keying/keying_a4_asis.cir@f6cc1d9e6974cff9120430061980e1e3b8a5d72d", "hardware/sim/tx-keying/keying_a4_fix.cir@1e6d0c5489a75822c9829991670cd77c993117ac", "hardware/sim/tx-keying/keying_a4_mitig.cir@d209bbd419e0b106375b7a2856ef64c8af2702a2", "hardware/sim/tx-keying/keying_a4_sweep0.cir@9a6e1650b7d9c54ef3566933953f6018232d54de", "hardware/sim/tx-keying/keying_a4_sweep1.cir@23612e8457cbfbeca7b5b63b25e47602a83165da", "hardware/sim/tx-keying/keying_a5_asis.cir@9265effb2026c8f68ed45c6d99a61bef62b921d1", "hardware/sim/tx-keying/keying_a5_fix.cir@34c2f33ca43e80da24bdd719247ad970d36f4b2e", "hardware/sim/tx-keying/keying_a5_mitig.cir@fd4ec933178342d196e2c5943736094e54dc77a2", "hardware/sim/tx-keying/keying_a5_sweep0.cir@d517774461229912dde02207ce0cad5f00723a61", "hardware/sim/tx-keying/keying_a5_sweep1.cir@a442e964141496efd4d6bc12923cbfc9947bda47", "hardware/sim/tx-keying/results/2026-09-28-r1-a4-asis/envelope.png@7008acbb08e7372e57e33f42404a35f01aa30412", "hardware/sim/tx-keying/results/2026-09-28-r1-a4-asis/keyup_level.png@a229f99f6335e92cba617e7132f1c6dbcfe05441", "hardware/sim/tx-keying/results/2026-09-28-r1-a4-asis/result.csv@e23530e583f1a5e3ee21bec9343e79a680626572", "hardware/sim/tx-keying/results/2026-09-28-r1-a4-asis/result.json@1ad8d9f40d4f1879d5b1a12761e5de7c6ab321ca", "hardware/sim/tx-keying/results/2026-09-28-r1-a4-asis/spectrum.png@4c3c211d1eba61e22556e5d1bd1c4195ef666b5d", "hardware/sim/tx-keying/results/2026-09-28-r1-a4-fix/corners.png@e1172716b99057bd825c857e356472ec0c807744", "hardware/sim/tx-keying/results/2026-09-28-r1-a4-fix/envelope.png@1e824337deafeac088cc0f30396c61b9ecb7c76d", "hardware/sim/tx-keying/results/2026-09-28-r1-a4-fix/keyup_level.png@aa79ca0b2496accedce2c0e8626562107e31f4bd", "hardware/sim/tx-keying/results/2026-09-28-r1-a4-fix/result.csv@963d26e1508a7991ff94b12d636337577156e66d", "hardware/sim/tx-keying/results/2026-09-28-r1-a4-fix/result.json@5e2361556286f42d185acb935bf5e7a1a0d60fc8", "hardware/sim/tx-keying/results/2026-09-28-r1-a4-fix/spectrum.png@d146b21ea4530bd5bf536fd540e6d038bb8bfb8b", "hardware/sim/tx-keying/results/2026-09-28-r1-a4-fix/t1090.png@406f05e6b2cce8b745ed6c4abf11e9db2f251631", "hardware/sim/tx-keying/results/2026-09-28-r1-a4-sweep0/result.csv@ce90610c5cbfe7500eb2b1500a25b5e14dd6af0f", "hardware/sim/tx-keying/results/2026-09-28-r1-a4-sweep0/result.json@869274d29f1f427d9c938d435bb744a797f15149", "hardware/sim/tx-keying/results/2026-09-28-r1-a4-sweep0/window.png@7e71a13ceda0f66d994445fb35afb8ab02549325", "hardware/sim/tx-keying/results/2026-09-28-r1-a4-sweep1/result.csv@b5706560761eddfc9394d04bd4df4bfc057c9e93", "hardware/sim/tx-keying/results/2026-09-28-r1-a4-sweep1/result.json@88e2ebc94be00a6dd983b2fa80dbf6129cc387ed", "hardware/sim/tx-keying/results/2026-09-28-r1-a4-sweep1/window.png@3ec60588c15eb3c40a1347a975dfeed57358b027", "hardware/sim/tx-keying/results/2026-09-28-r1-a5-asis/envelope.png@83373e0d227e06ea70206b050c2778444632467b", "hardware/sim/tx-keying/results/2026-09-28-r1-a5-asis/keyup_level.png@0e7d74973f26cdf7badf3b382bc5cd1e65a8af03", "hardware/sim/tx-keying/results/2026-09-28-r1-a5-asis/result.csv@c9bb2586b1651fe4685c6ea1f2c81d36a2463b80", "hardware/sim/tx-keying/results/2026-09-28-r1-a5-asis/result.json@9b7bdbeb7030dbc09d903d65bf4c34b1c383717d", "hardware/sim/tx-keying/results/2026-09-28-r1-a5-asis/spectrum.png@176f20133e8d6f861b9f066da9c7e9a0ad5a8bc6", "hardware/sim/tx-keying/results/2026-09-28-r1-a5-fix/corners.png@086505562a844d5976364261f9b84a52e4cfa078", "hardware/sim/tx-keying/results/2026-09-28-r1-a5-fix/envelope.png@7869f1273f26906347bba87220518fdf87397093", "hardware/sim/tx-keying/results/2026-09-28-r1-a5-fix/keyup_level.png@1d378cf98768a8ac4942d479d09ce60d6c974647", "hardware/sim/tx-keying/results/2026-09-28-r1-a5-fix/result.csv@7e0b2e2604304a113505969b23a4c3af63f05797", "hardware/sim/tx-keying/results/2026-09-28-r1-a5-fix/result.json@9ea50b3943bad4ff7f0265a692b82ae4587ba31b", "hardware/sim/tx-keying/results/2026-09-28-r1-a5-fix/spectrum.png@d8308e4b68a781e3faff6416e621dfd88fb15139", "hardware/sim/tx-keying/results/2026-09-28-r1-a5-fix/t1090.png@760d89367a8a37a47e8a96c608c3d61ebd4da35e", "hardware/sim/tx-keying/results/2026-09-28-r1-a5-sweep0/result.csv@e13faa26334ec7a664ac1b16d29efc6e159cfa91", "hardware/sim/tx-keying/results/2026-09-28-r1-a5-sweep0/result.json@ca67cdcf0d7005ddcc4fc95609d6b805b49619a2", "hardware/sim/tx-keying/results/2026-09-28-r1-a5-sweep0/window.png@7d341664ce3fdaa2b16db4b87c0a15dc6139c2f7", "hardware/sim/tx-keying/results/2026-09-28-r1-a5-sweep1/result.csv@5cf2d34a14c03265859bddcb3bb0982afa1f8784", "hardware/sim/tx-keying/results/2026-09-28-r1-a5-sweep1/result.json@2bc4cc4a854714425f106270aef2447611bff1e4", "hardware/sim/tx-keying/results/2026-09-28-r1-a5-sweep1/window.png@f34d2798c7d2ce80f177e275cdc871bfa6f66233", "hardware/sim/tx-keying/results/2026-09-28-r1-summary/pwm_ripple.png@0af37f327a9c73ac43e6d520bbaea110ab149cad", "hardware/sim/tx-keying/results/2026-09-28-r1-summary/summary.json@4c13fbf5fa03994c2f550b2e78d5daad9bd47a55", "hardware/sim/tx-keying/results/2026-09-28-r1-summary/summary.png@757f506c013037318b4347c897ad655fa3e84c78", "hardware/sim/tx-keying/results/2026-09-28-r1-summary/windows.png@83673618dc52ac80e66a6faa936c43605172c2f4"]
product_files_iteration_1: ["docs/design/analysis/keying-ts012.md@bad537544e50cad797be11fb5009eb8e7ea448c3", "hardware/sim/tx-keying/README.md@031c25f9f44b7f11bf2db05c161a3c1402b9357e", "hardware/sim/tx-keying/det_char.cir@059595d7034f385a08dc8a84654d01c8692f9485", "hardware/sim/tx-keying/det_char_biased.cir@5911e4396425b17bf4b48c4146e3b0b898b1c2c4", "hardware/sim/tx-keying/keying_a4_asis.cir@2c4f1d86aa0b3895fdbbe3a60a3126c652b0ee6a", "hardware/sim/tx-keying/keying_a4_mitig.cir@d209bbd419e0b106375b7a2856ef64c8af2702a2", "hardware/sim/tx-keying/keying_a5_asis.cir@aebb89253184c785598442ac80533241db037bac", "hardware/sim/tx-keying/keying_a5_mitig.cir@fd4ec933178342d196e2c5943736094e54dc77a2", "hardware/sim/tx-keying/keying_run.py@f85f2e2965d18288cce8cd55b7b60aa6fd1f774f", "hardware/sim/tx-keying/results/2026-09-28-a4-asis/envelope.png@66a0c0de303bf92b781080b8df4ef3b1b89ad55b", "hardware/sim/tx-keying/results/2026-09-28-a4-asis/keyup_level.png@0fe31b1ef50030051232237295421c307e926b7d", "hardware/sim/tx-keying/results/2026-09-28-a4-asis/result.json@abbfca5dde2e19f6c109b5ec25a1752fa944a6f2", "hardware/sim/tx-keying/results/2026-09-28-a4-asis/spectrum.png@89eb1791e90b4c3c5cb245569138362d10e66ac3", "hardware/sim/tx-keying/results/2026-09-28-a4-mitig/corners.png@15cadaf455c525a84599bbb54789fe258c564fa6", "hardware/sim/tx-keying/results/2026-09-28-a4-mitig/envelope.png@0010dc46e65aacdae1713c7d38777d7c6297166d", "hardware/sim/tx-keying/results/2026-09-28-a4-mitig/keyup_level.png@57a805ded1f9f768bd6bf6247b6c1400620795c3", "hardware/sim/tx-keying/results/2026-09-28-a4-mitig/result.json@c7ea5dc5fcfa69266f51c1e1aca72b0b2a88e382", "hardware/sim/tx-keying/results/2026-09-28-a4-mitig/spectrum.png@ca11b04a0497f1526f67e3864ca4e9686fe051ed", "hardware/sim/tx-keying/results/2026-09-28-a5-asis/envelope.png@b387cf0ad695fbfbc59c2fa4e6a598f1fc8bfd0c", "hardware/sim/tx-keying/results/2026-09-28-a5-asis/keyup_level.png@06525e4f2d1ccf6af06cfe260c38efc433821188", "hardware/sim/tx-keying/results/2026-09-28-a5-asis/result.json@3e473721292dfce47c5ba21352cc85f1c5b6cd1e", "hardware/sim/tx-keying/results/2026-09-28-a5-asis/spectrum.png@f1d37da0de814cc307b5cd7e23b9a383d602f9e2", "hardware/sim/tx-keying/results/2026-09-28-a5-mitig/corners.png@ef095896f28b454e7dda755a51e014d378970320", "hardware/sim/tx-keying/results/2026-09-28-a5-mitig/envelope.png@3af80d18b2a8ab8168c36f867de8494eb8de52be", "hardware/sim/tx-keying/results/2026-09-28-a5-mitig/keyup_level.png@255cd4d1eef0786603d502c069be2da2938f209f", "hardware/sim/tx-keying/results/2026-09-28-a5-mitig/result.json@2792dd1a30da7c34ed3af37cabc765fa0e6a958b", "hardware/sim/tx-keying/results/2026-09-28-a5-mitig/spectrum.png@92e69e6dab86396c566181c6e7a3768c6b50dd49", "hardware/sim/tx-keying/results/2026-09-28-det-char-biased/det_law.png@be1c380b6b5c3a42a4254a18a0bbcd4b0d23c071", "hardware/sim/tx-keying/results/2026-09-28-det-char-biased/result.json@584d5e6dace081012c3b8997a3ce0be88c01f985", "hardware/sim/tx-keying/results/2026-09-28-det-char/det_law.png@582e4e076e638cfd78cdc438de6223157432e53e", "hardware/sim/tx-keying/results/2026-09-28-det-char/result.json@17c4d924c8e04b0541e49493ea84ac9b62b4a0a9", "hardware/sim/tx-keying/results/2026-09-28-summary/pwm_ripple.png@2e28ecce6f1a0872f8e2d2dfc6ed3c3917a57323", "hardware/sim/tx-keying/results/2026-09-28-summary/summary.json@6fc2fe2ee6969365c3f12e30dcaa68c07df5e63f", "hardware/sim/tx-keying/results/2026-09-28-summary/summary.png@069cb9295c9aef4d952f4a2fd0be8b60c839f6a8"]
analysis_kind: [simulation-deck, timing, worst-case]
product_size: iteration 3, 1 note (600 lines, revision 2); 14 decks (2 detector, 12 keying: 6 + 78 + 180 + 156 + 2604 steps per finalist in revision 2); 1 generator and checker; 1 expected-states file; 27 result plots (15 changed or new); iteration 2, 1 note (519 lines, revision 1); 12 decks (2 detector, 10 keying: 6 + 78 + 108 + 156 steps per finalist in revision 1); 1 generator and checker; 23 result plots; iteration 1, 1 note; 2 detector decks (13 amplitudes each at 146 MHz); 4 envelope decks (6 + 6 + 30 + 30 runs); 1 generator and checker; 18 renders (16 cited); 22 input rows
tools_used: ["LTspice 26.0.2 for MacOS through tools/ltspice-batch.sh blob 88b71475 (TV-014, Accredited, ACC-LTSPICE-001)", "venv Python 3.13.5 (TV-001 accredits the interpreter); numpy 2.5.3, spicelib 1.6.3, matplotlib 3.11.2 (class B entries of tools/toolchain.lock.md section 2 without a TV record); no TV record covers hardware/sim/tx-keying/keying_run.py: developer evidence per 05 section 9.1, as the note says"]
# values_proposed (iteration 2): revision 1 section 8 item 8 proposes keeping the REQ-TX-005 TBR tolerance at +/-10 %
# (plan step: the TS-006-class simulation at PDR); it edits no requirement file. Iteration 1 had none.
values_proposed: ["REQ-TX-005: +/-10 %"]
# renders_inspected: iteration 3 (the 15 revision 2 plots that are new or differ from their r1 counterpart; the other
# 12 r2 plots are pixel-identical to r1 plots that iteration 2 opened); iteration 2 opened 31; iteration 1 opened 18
renders_inspected: 15
sprint: PDR-prep
author_agent: "author:WP-PDR-22 tx-keying (Claude as analysis author, TS-012 discriminating analyses; commit 4ea4607; revision 1 at e9f1440; revision 2 at be86c02)"
reviewer_agent: "reviewer:WP-PDR-22-analysis-keying-iter1 (independent; authored no part of the note, decks, checker or TS-012); iteration 2 by reviewer:WP-PDR-22-analysis-keying-iter2 (independent; authored no part of the note, its revision 1, the decks, the checker, TS-012 or iteration 1); iteration 3 by reviewer:WP-PDR-22-analysis-keying-iter3 (independent; authored no part of the note, its revisions 1 and 2, the decks, the checker, the keying fixes, TS-012 or iterations 1 and 2)"
# criticality: a hardware transmit analysis; the firmware ramp and feedforward tables it proposes are SW design items
# not yet allocated, and it sets no value of a 07 section 14.1 component
criticality: neither
assurance_required: false
assurance_reviewer_agent: none
iteration: 3
readiness_met: true
reviewer_verdict: APPROVED
assurance_verdict: not-required
# verdict (rule C1, iteration 3, the last iteration): finding-10 (Major) is Verified at be86c02, so no Major is open
# and the reviewer verdict is APPROVED. The Minor finding-11 to finding-14, which revision 2 also answered, are
# Verified. finding-4 to finding-9 (not addressed) and the new finding-15 (Minor, introduced by revision 2: the A5
# slope and the 61 kHz excess are quoted from one 0.02 V digitized segment) are Open Minor liens, due at the CDR
# readiness declaration. The record verdict stays NEEDS CHANGES only because the applied analysis template is still
# only on cr/CR-012 (lead SE convention of 2026-09-27, INSP-083); it becomes APPROVED when CR-012 merges.
# verdict (rule C1, iteration 2): finding-1, finding-2 and finding-3 (Major) are Verified at e9f1440 (finding-3 for
# its part a; its parts b and c, which change no number or verdict, are re-raised as finding-11, Minor). The new
# finding-10 (Major, introduced by revision 1: section 4.6 quotes revision 0's PWM ripple, which the revision 1
# checker output contradicts) is Open, so NEEDS CHANGES. Iteration 3 is a delta on finding-10. finding-4 to
# finding-9 and the new finding-11 to finding-14 are Minor and Open. The record verdict would in any case be held
# while the applied analysis template is only on cr/CR-012 (lead SE convention of 2026-09-27, INSP-083).
verdict: NEEDS CHANGES
findings_major: 4
findings_minor: 11
# findings (iteration 3): 15 in all. Verified 8 (finding-1, 2, 3, 10 Major; finding-11 to 14 Minor). Open 7, all
# Minor (finding-4 to 9 and finding-15).
findings_open: 7
findings_fixed: 0
findings_verified: 8
findings_deferred: 0
assurance_tasks_applied: []
deferred_rids: []
# items_no (iteration 3): the items that are No on the open findings (finding-4 to 9 and finding-15)
items_no: [CK-ANA-A1, CK-ANA-A4, CK-ANA-A6, CK-ANA-B1, CK-ANA-B3, CK-ANA-C1, CK-ANA-D2, CK-ANA-D3, CK-ANA-F2, CK-ANA-H1, CK-ANA-H2, CK-ANA-H3]
items_no_iteration_2: [CK-ANA-A1, CK-ANA-A4, CK-ANA-A5, CK-ANA-A6, CK-ANA-B1, CK-ANA-B6, CK-ANA-C1, CK-ANA-D2, CK-ANA-D4, CK-ANA-E4, CK-ANA-F2, CK-ANA-F4, CK-ANA-G7-2, CK-ANA-H1, CK-ANA-H2, CK-ANA-H3]
items_no_iteration_1: [CK-ANA-A1, CK-ANA-A4, CK-ANA-A5, CK-ANA-A6, CK-ANA-B1, CK-ANA-B6, CK-ANA-C1, CK-ANA-D4, CK-ANA-E3, CK-ANA-E4, CK-ANA-F1, CK-ANA-F2, CK-ANA-F4, CK-ANA-G7-2, CK-ANA-H1, CK-ANA-H2, CK-ANA-H3]
# effort: cumulative (iteration 1: 80 turns, 130 minutes; iteration 2: 65 turns, 110 minutes; iteration 3: 60 turns,
# 120 minutes, of which about 45 minutes LTspice wall time behind the shared wrapper lock)
effort_turns: 205
effort_minutes: 360
record_status: Open
date: 2026-09-28
date_closed: null
---

# Peer review record: keying envelope and key clicks, TS-012 finalists A4 and A5 (INSP-116, iteration 1)

**Product:** `docs/design/analysis/keying-ts012.md` (`bad53754`) with `hardware/sim/tx-keying/` (README `031c25f9`; generator and checker `keying_run.py` `f85f2e29`; decks `det_char.cir`, `det_char_biased.cir` and the four keying decks; seven result runs) at freeze commit `4ea4607` (rule C2). Every blob equals `git rev-parse HEAD:<path>` at `HEAD` `35fc7ee`. No product blob lives on a `cr/` branch.

**Checklist:** the item set of `peer-review-checklist-analysis.md` revision A (CR-012 branch, blob `0386cc6e`; front matter comment). `analysis_kind` simulation-deck, timing (keying envelope edges, which G6 names) and worst-case (extreme-value corners): sections A to F, G1, G6, G7, H and I apply. G2 to G5 are N/A; J is N/A (criticality neither).

**Acceptance criteria (rule C7; texts read at HEAD from `requirements.json` and `test_cases.json`):**
- REQ-SYS-014: "shape keyed rises and falls as raised cosines with an operator-set 10-to-90 percent time of 3 to 8 ms (TBR)". TC-SYS-013: normalized envelope within 5 % of full scale of the ideal raised cosine at every sample, and 10-to-90 % times equal to the setting within +/-0.5 ms, at 3, 5 and 8 ms, "nominal and at every tolerance corner".
- REQ-SYS-015: "26 dB bandwidth at most 350 Hz (TBR) at every envelope setting with continuous dits at 50 WPM" (97.3(a)(8) power containment).
- REQ-TX-005: "10-to-90 percent times within +/-10 percent (TBR) of the command". TC-TX-005 accepts 2.7 to 3.3 ms, 4.5 to 5.5 ms and 7.2 to 8.8 ms "at the 0.5 W and 5 W steps, at 6.4, 7.4 and 8.4 V supply and at every shaping-network tolerance corner".
- REQ-TX-006: "at least 60 dB below total mean power beyond 750 Hz (TBR) offset with continuous 50 WPM dits"; its verification note says "at the 3, 5 and 8 ms settings and every tolerance corner". TC-TX-006 step 2 is a known answer (614 Hz within one cell) and step 6 reads "Repeat the three settings at the 0.5 W step and at every shaping-network tolerance corner".
- REQ-TX-014: at most 1 uW (TBR) "while TX_KEY is deasserted with PA_EN asserted and the exciter driven". REQ-SYS-183: -57 dBm (TBR) in every RF-ended, inhibited or off state.
- REQ-SYS-011: "0.5, 1 and 2 W steps within +/-1 dB (TBR)"; REQ-SYS-064 makes 1 W the default step. REQ-SYS-114: requirements met from -10 C to +45 C (TBR).
- TS-012 revision 4 section 7.3, WP-PDR-22 pre-order criteria: overshoot at most 0.2 dB, loop phase margin at least 45 degrees, VGG never above 3.5 V with the LM2940 at 4.75 to 5.25 V, and the 12 ms late-contact and open-loop fault cases.

**Search rule.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` (the keying analysis; the INSP id register) preceded every `grep`; `grep` only pinned lines in TS-012, INSP-110, the research note F7, the note and the checker. The rustos tree was not read.

**Sources re-read by the reviewer (2026-09-28).**
- NXP AFT05MS004N Rev. 0 (https://www.nxp.com/docs/en/data-sheet/AFT05MS004N.pdf), fetched through the web-fetch tool; SHA-256 prefix `84cd9fae`, equal to the prefix in the `hardware/sim/tx-pa` README. Read: Table 5 (VGS(th) 1.7 / 2.2 / 2.5 V at VDS 10 V, ID 67 uA; Crss 1.63 pF; Ciss 57.6 pF), and Figure 12 on page 11, rendered at 200 dpi.
- Mitsubishi RA07M1317M (Jun. 2019), through the digitized curves `hardware/sim/tx-pa/data/ra07_pout_vs_vgg_{135,155}.csv` and `ra07_pout_vs_vdd_{135,155}.csv` (reviewed under INSP-114 with their overlays).
- `docs/research/regulatory-corpus-and-operators.md` F7.

## Findings (iteration 1)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | reviewer | Major | CK-ANA-F1, E3, A5 | note sections 1, 2 (runs per deck), 4.3 and 5.1; author summary ("both pass every keying check at every corner I tried"); `keying_run.py` `run_params` (`pset = 5.0`) | **The power steps below 5 W are not analysed, and the note does not say so.** REQ-SYS-011 sets 0.5, 1 and 2 W steps, and 1 W is the default (REQ-SYS-064). The keying requirements hold at every step. TC-TX-005 and TC-TX-006 name the 0.5 W step, and TC-TX-005 also names 7.4 V. This case exercises the mechanism the note itself identifies. The biased detector sees down to -35.5 dB re 5 W, which is only -25.5 dB re 0.5 W, so the feedforward alone shapes a 10 dB larger part of each edge. **Reviewer run** (the note's own mitigated model and five corners, setpoint 0.5 W, both drain ends, 30 runs per finalist, through the wrapper): nominal and the +/-1 mV corners pass for both finalists. At the -0.1 V corner: A5 has shape error 6.3 % and rise 3.40 ms at 3 ms (REQ-TX-005 +13 %), rise 5.68 ms at 5 ms and 9.02 ms at 8 ms (TC-SYS-013 +/-0.5 ms fails). A4 has rise 3.38 ms at 3 ms (+13 %) and 5.54 ms at 5 ms (TC-SYS-013 and REQ-TX-005 fail), with shape at most 4.4 %. At the +0.1 V corner: A5 has rise 2.57 ms at 3 ms (-14 %) and shape 5.5 %. So at the note's own corner set both finalists fail REQ-TX-005 at the 0.5 W step, and A5 also fails REQ-SYS-014. **Fix:** add the 0.5, 1 and 2 W steps (and 7.4 V) to the decks and the per-case results. If they fail, the mitigation needs a step-dependent change (for example a detector tap or gain switched with the step, or a tighter calibration), and the verdicts of sections 4.3 and 5.1 and the summary are restated | Open | Pending | |
| <a id="finding-2"></a>finding-2 | reviewer | Major | CK-ANA-A4, A5, B6, E3, F4, G7-2 | note section 4.3 corners; section 3 rows "AFT05MS004N Crss, VGS(th)" and "Sub-threshold slope"; section 7 item 1; section 8 item 2 ("A5 only"); `keying_run.py` `CORNERS_MITIG` | **The PASS "at every corner" rests on a +/-0.1 V transfer-curve corner that has no source and is narrower than the known variation.** The variation comes from the note's own inputs and the project's other analyses, and the reviewer's wider corners show that both finalists' margins are about the corner's size. (i) Lot spread: the AFT05MS004N VGS(th) is 1.7 to 2.5 V (Table 5, the note's own input row), yet section 8 asks for per-unit feedforward calibration for A5 only. (ii) Drive level: Figure 12 shows the Pout-versus-VGS curve moving about +0.5 V when Pin halves from 0.1 to 0.05 W. `docs/design/analysis/pa-drive-ts012.md` gives A4 drive 50 to 168 mW and A5 6 to 29.5 mW over its corners, with a 0.34 dB span within one unit over 144 to 148 MHz. The RA07M1317M VGG curve is given at 20 mW only. (iii) Temperature: neither REQ-SYS-114 (-10 to +45 C) nor the module heating that TS-012 section 7.3 estimates (flange 70 to 99 C) is a corner. Section 7 item 1 lists "no thermal drift of the threshold" as a limitation, but the verdict does not carry it. An LDMOS threshold coefficient of the order of -2 mV/C (reviewer estimate, not read from either datasheet) moves the curve 0.1 to 0.2 V over those ranges. (iv) The A5 table sits up to about 0.05 V left of the project's digitized curves at 2.3 to 2.5 V (finding-4). **Reviewer runs** (the mitigated decks with wider threshold corners, 36 runs per finalist, through the wrapper): A5 at -0.15 V: rise 3.47 ms at 3 ms (REQ-TX-005 +16 %; the checker still reports t1090 PASS, finding-3) and shape 5.1 %. A5 at -0.2 V: rise 3.60 ms, shape 6.4 to 6.6 %. A5 at +0.2 V: shape 5.0 to 5.1 %. A5 at +/-0.4 V: setpoint not reached, worst cell -55.0 dB. A4 at -0.2 V: shape 5.2 % (3 ms, 6.1 V). A4 at -0.4 V: rise 3.50 ms, shape 6.6 %, worst cell -60.1 dB. A4 at +0.4 V: setpoint not reached, rise 2.67 ms (-11 %). So A5 holds for about +/-0.12 V of residual curve error and A4 for about +/-0.15 to 0.2 V. The note's A5 margin (3.285 ms against 3.3 ms) is 0.015 ms, against an uncertainty the note does not bound. **Fix:** bound the residual curve error after calibration (lot, drive over frequency and temperature, device temperature, table read) with sources or labelled estimates. State that A4 also needs per-unit calibration and what calibration covers. Add the temperature case, and report the margin against that bound. Or state the pass as conditional on a residual of at most about 0.1 V (A5) and 0.15 V (A4), and carry that as a design requirement and a risk | Open | Pending | |
| <a id="finding-3"></a>finding-3 | reviewer | Major | CK-ANA-E4, D4, D2 | `keying_run.py` `REQ` (`t1090_tol_ms: 0.5`), `analyse()` `pass`, `stage_deck()`; note section 4.3 table row "10-to-90 % error" | **The checker does not assert REQ-TX-005.** Its only timing criterion is TC-SYS-013's +/-0.5 ms. That is looser than REQ-TX-005's +/-10 % at the 3 ms setting (2.7 to 3.3 ms) and tighter at 8 ms (7.2 to 8.8 ms). The note's "+9.7 % of 10 %" is a hand computation on the checker output. In the reviewer runs the checker reports t1090 PASS for A5 at 3.47 ms and for A4 at 3.38 ms and 2.67 ms, all outside REQ-TX-005. The checker also exits 0 whatever the verdicts (reviewer runs: exit 0 on every as-written FAIL). Its `setpoint` criterion (+/-0.5 dB) has no source, and it passes A5 as written at 4.48 W against 5 W (-0.48 dB) although the integrator has wound up. **Fix:** add a REQ-TX-005 criterion (+/-10 % of the setting, with its id in a comment) and keep TC-SYS-013's separately. Source or drop the setpoint criterion (REQ-SYS-012 is +/-1 dB of 5 W). Exit non-zero on a failing case, or add a `--check` mode with the expected FAIL states listed | Open | Pending | |
| <a id="finding-4"></a>finding-4 | reviewer | Minor | CK-ANA-A4, A3 | note section 3 rows "RA07M1317M Pout vs VGG", "Pout vs VDD", "AFT05MS004N Pout vs VGS" and "Sub-threshold slope"; section 6 F1; `keying_run.py` `A5_W`, `A5_SCALE`, `A4_W` | **The graph reads disagree with the project's digitized curves by more than the stated 0.05 W resolution at the foot.** A5 table against the mean of `ra07_pout_vs_vgg_135.csv` and `_155.csv`: 0.17 against 0.08 W at 2.3 V, 0.55 against 0.36 W at 2.4 V, and 1.25 against 1.02 W at 2.5 V (about 0.03 to 0.05 V of curve shift). F1's "1.1 to 1.3 W at 2.5 V" reads 0.98 to 1.06 W on the digitized curves. VDD scale at 155 MHz: 4.8 / 7.75 / 9.1 W at 5.5 / 7.2 / 7.9 V against 4.93 / 8.23 / 9.76 W digitized (ratio at 5.5 V 0.619 against 0.599). AFT05 Figure 12 (rendered): the Pin 0.1 W curve ends near 2.42 V and 5.7 W, not 2.35 V and 5.6 W. The 100 dB/V sub-threshold estimate is about three times steeper than the last graph segments (A5 about 33 dB/V at 2.2 to 2.3 V, A4 about 39 dB/V at 1.2 to 1.5 V), and its direction is not stated. **Fix:** take the digitized RA07M1317M curves (or state why not), state the read resolution, and state the direction of the slope estimate | Open | Pending | |
| <a id="finding-5"></a>finding-5 | reviewer | Minor | CK-ANA-C1 | note header "Tool" row | **Wrong tool version.** The note says "spicelib 2.5", but the venv has spicelib 1.6.3 (`pip show`); numpy is 2.5.3. **Fix:** correct the version and list numpy and matplotlib | Open | Pending | |
| <a id="finding-6"></a>finding-6 | reviewer | Minor | CK-ANA-A1, H1, H2, H3 | note header "Serves" row, sections 5.1 and 8; no change history | **Missing ids, requests and change history.** (i) The hazards are not named: HZ-008 (REQ-SYS-014, 015, REQ-TX-005, 006) and HZ-004 (REQ-TX-014, REQ-SYS-183). REQ-SYS-011 and REQ-SYS-114 are not named (findings 1 and 2), nor is RSK-011 (Analysis accepted). (ii) Section 5.1 re-scores the TS-012 section 7.1 A5 envelope-loop risk ("a certainty" as written) and shows that A4 carries the same loop (INSP-110 finding-17 asked for the A4 counterpart row). No request goes to the WP-PDR-18 risk writer or to the `hazards.json` writer (PDR work plan section 5.3). (iii) The note has no change history. **Fix:** add the ids, the two requests and a change log | Open | Pending | |
| <a id="finding-7"></a>finding-7 | reviewer | Minor | CK-ANA-B3, A6 | note section 7 item 9; section 2 step 3 | **The explanation of the -60 dB point is not shown.** The note gives 395 Hz here against F7's 614 Hz and attributes the difference to "record length and window: a radix-2 record in F7, whose rectangular-window leakage raises the far cells". Reviewer computation on the ideal envelope: an integer number of periods gives 395 Hz (5.08 ms full transition) and 435 Hz (5.00 ms). A radix-2 rectangular record (2^15 samples at 10 kHz) gives 435 Hz for both, and a Blackman-Harris window gives 395 and 435 Hz. None reproduces 614 Hz. The metric also jumps with the position of the spectral nulls (395 against 435 Hz for a 1.6 % change of transition). TC-TX-006 step 2 requires the checker to place the point at 614 Hz within one cell, which this checker does not. The 26 dB bandwidth (292 Hz) agrees, and that is the check that matters here. **Fix:** state the cause as not established, and send a request to the TC-TX-006 and F7 owners (the 614 Hz known answer feeds the REQ-SYS-008 and REQ-TX-006 rationale) | Open | Pending | |
| <a id="finding-8"></a>finding-8 | reviewer | Minor | CK-ANA-A6, F2 | note header "Work package" row, section 1 "It does not cover", author summary | **A partial WP-PDR-22 run is presented as the pre-order check.** The header calls the note "the pre-order LTspice check that TS-012 revision 4 section 7.3 names", but most WP-PDR-22 pass criteria of TS-012 section 7.3 are not run: the 12 ms late-contact fault case (at most 8 W, and the mid-ramp check tripping); the open-loop case at 8.4 V (at most 8 W at the clamp); VGG with the LM2940 at 4.75 to 5.25 V and the divider at +/-1 % (the decks use 5.00 V; 5.25 V gives 3.43 V as written); the module VGG input current; and the 3.08 V clamp REQ-SYS-012 check. Section 1 lists some of these exclusions and section 8 item 1 carries two, but a reader of the header and the summary takes the pre-order item as done. **Fix:** call it a partial WP-PDR-22 run in the header, and list every TS-012 criterion not run with where it closes | Open | Pending | |
| <a id="finding-9"></a>finding-9 | reviewer | Minor | CK-ANA-B1, D2 | `det_char.cir` hold capacitor; note sections 4.1, 4.3 and 4.5 | **Three statements need correcting.** (i) The detector law is characterized with a 22 pF hold (50 ohm at 146 MHz) instead of the design's 470 pF. The RF divides between the diode capacitance and the hold, so the square-law output is about 17 % low (reviewer analytic, below). The direction is conservative (with 470 pF the blind point moves about 0.3 to 0.6 dB lower) but is not stated. (ii) Section 4.5 says the 30.5 kHz feedforward ripple fails REQ-TX-006. The figure is a bound: it holds duty 0.5 at the steepest slope continuously, while the steep part of the transfer is crossed for only a few ms per 48 ms. "Not shown" is the supported wording. The 122 kHz rule stands as a conservative choice, and the 10-bit staircase it implies is not simulated (section 7 item 6 says so). (iii) Section 4.3 says "gate step -54 to -57 dB", but A5 reaches -53.5 dB (`result.json` `gate_step_rel_db`). **Fix:** state (i), reword (ii), correct (iii) | Open | Pending | |

Three Major findings are open, so the reviewer verdict is NEEDS CHANGES.

What holds:
- The re-run reproduces every number, plot and verdict of the note exactly.
- The detector law agrees with an independent analytic solution.
- The as-written failure is sound.
- REQ-TX-014 and REQ-SYS-183 are handled with the right caution.
- The comparative reading (A4 has more keying margin than A5) holds in every reviewer run.

The three Majors concern the claim that the mitigated loop passes for both finalists:
- The claim was not tried at the lower power steps, where both finalists fail REQ-TX-005 at the note's own corners (finding-1).
- The corner set is narrower than the known curve variation, and both finalists' margins are about the corner's size (finding-2).
- The checker cannot flag a REQ-TX-005 failure (finding-3).

### Per-case results (section F; one row per case the governing texts name)

| Case | Condition | Governing id and limit | Result (checker output) | Margin with sign | Uncertainty | Reviewer re-check | Finding ids |
|---|---|---|---|---|---|---|---|
| C-1 | As written, 5 W, 3 / 5 / 8 ms, both drain ends | REQ-SYS-014 and TC-SYS-013: shape 5 %, +/-0.5 ms | A4 shape 10.0 to 19.2 %, rise 1.64 to 7.46 ms; A5 17.8 to 27.1 %, rise 1.31 to 5.66 ms | negative (FAIL both) | model | re-run identical | none |
| C-2 | As written, 3 ms | REQ-SYS-015: 350 Hz | A4 417 Hz, A5 542 Hz | -67 / -192 Hz (FAIL) | model | re-run identical; ideal envelope 291.7 Hz by independent code | none |
| C-3 | As written | REQ-TX-006: -60 dB beyond 750 Hz | A4 -49.8 dB, A5 -48.3 dB | -10.2 / -11.7 dB (FAIL) | model | re-run identical | none |
| C-4 | Mitigated, 5 W (4.0 / 2.9 W at the low pack end), 5 corners | REQ-SYS-014 and TC-SYS-013 | shape at most 2.5 % (A4) and 3.3 % (A5); times within 0.06 / 0.29 ms | +2.5 / +1.7 % shape; +0.44 / +0.21 ms | curve corner not bounded | re-run identical; 4 us step and 2 us resampling move times by at most 0.008 ms | finding-2 |
| C-5 | Mitigated, 3 ms, A5 -0.1 V corner | REQ-TX-005: 2.7 to 3.3 ms | 3.285 ms | +0.015 ms (0.5 %) | not bounded; -0.15 V gives 3.47 ms | re-run identical; wide corners | finding-2, finding-3 |
| C-6 | Mitigated, all corners | REQ-SYS-015: 350 Hz | 292 / 208 / 125 Hz | +58 Hz | small | re-run identical | none |
| C-7 | Mitigated, all corners | REQ-TX-006: -60 dB | A4 -67.2 dB, A5 -64.1 dB | +7.2 / +4.1 dB | not bounded (A4 -60.1 dB at -0.4 V, A5 -55.0 dB at +0.4 V) | re-run identical; fine-step worst cells unchanged (-67.21, -64.10 dB) | finding-2 |
| C-8 | Mitigated, 0.5 W step, the note's 5 corners | REQ-SYS-014, REQ-TX-005, REQ-TX-006 (TC-TX-005, TC-TX-006) | not analysed | not shown | | reviewer run: A5 FAIL (shape 6.3 %, rise 3.40 ms at 3 ms and 5.68 ms at 5 ms at -0.1 V; 2.57 ms at +0.1 V); A4 FAIL (rise 3.38 ms at 3 ms and 5.54 ms at 5 ms at -0.1 V); worst cells -60.6 dB (A5), -62.1 dB (A4) | finding-1 |
| C-9 | 1 W and 2 W steps; 7.4 V supply | REQ-SYS-011 with the keying requirements; TC-TX-005 | not analysed | not shown | | none | finding-1 |
| C-10 | -10 C and +45 C ambient, module heating | REQ-SYS-114 | not analysed | not shown | threshold drift 0.1 to 0.2 V (reviewer estimate) | none possible | finding-2 |
| C-11 | Overshoot, both variants | TS-012 WP-PDR-22: 0.2 dB | at most 0.01 dB | +0.19 dB | small | re-run identical | none |
| C-12 | VGG maximum, A5 | TS-012 WP-PDR-22: 3.5 V with the LM2940 at 4.75 to 5.25 V | 3.26 V (as written, 5.00 V rail), 3.13 V (mitigated) | +0.24 / +0.37 V | 5.25 V rail not modelled (3.43 V) | hand: 5.25 x 0.654 = 3.43 V | finding-8 |
| C-13 | Loop phase margin, mitigated | TS-012 WP-PDR-22: 45 degrees | 75.8 to 80.2 degrees (analytic) | +30.8 degrees | first-order model | hand: 90 - atan(2 pi 1706 x 17.7 us) - atan(2 pi 1706 x 4.7 us) = 76.4 degrees (A5, 7.9 V) | none |
| C-14 | Key-up, exciter driven | REQ-TX-014: -30 dBm | A4 -19.5 dBm (modelled leakage; range -23 to -19), A5 -17.5 dBm (at 30 dB isolation) | A4 -7 to -11 dB (FAIL by estimate); A5 not shown | estimates | hand: 2.0 to 3.0 mA through 1.63 pF at 146 MHz into 2.56 ohm gives 5.2 to 11.5 uW | none |
| C-15 | RF-ended states | REQ-SYS-183: -57 dBm | about -117 (A4) and -111 dBm (A5) | +54 to +60 dB | estimates | chain arithmetic re-added | none |
| C-16 | 12 ms late contact; open loop at 8.4 V | TS-012 WP-PDR-22 fault cases | not analysed (declared) | not shown | | none | finding-8 |
| C-17 | PWM carrier ripple at 30.5 / 61 / 122 kHz | REQ-TX-006 | A5 feedforward -43.2 / -60.7 / -78.7 dBc (analytic bound) | bound | conservative | hand: 2.10 V x 0.01183 x 0.283 x 44.1 V/V / 44.7 V = -43.2 dBc | finding-9 |

## Readiness criteria

| # | Criterion | Result | Evidence |
|---|---|---|---|
| R1 | Frozen: every `product_files` blob equals `git rev-parse 4ea4607:<path>` | Yes | 34 of 34 equal at `4ea4607` and at `HEAD`, checked with a Python loop over `git rev-parse`. The seven copies of `keying_run.py` in `results/` and the four run-directory decks equal the checked-in files |
| R2 | The checker runs by one command and exits with the stated result; LTspice through the wrapper | Yes | README commands run on a clean export of `4ea4607` (`git archive`) with the author's `results/` moved aside. Both detector decks and the four keying decks ran through `tools/ltspice-batch.sh`: every run PASS, exit 0, log first line `LTspice 26.0.2 for MacOS`, no warning in any log. `detchar`, the four `deck` stages and `summary` exit 0 |
| R3 | `validate_docs.py` on a JSON product | N/A | No JSON product under a schema |
| R4 | Author's return states question, assumptions, inputs, results, limitations, values and tools | Yes | Author summary in the brief; note sections 1 to 9 |
| R5 | No `TBD`; every TBR relied on named by id | Yes | Search, then grep: no `TBD` in the note or the README; the six requirements are named with their TBRs |
| R6 | Every cited render exists | Yes | 16 cited renders present, plus the two uncited key-up plots |

## Reviewer re-run (CK-ANA-C4) and independent checks (CK-ANA-B5)

- **Full re-run.** Every run regenerated from LTspice. Against the committed outputs:
  - all six decks byte-identical (the generator rewrote the four keying decks identically);
  - `det_law.csv`, every `result.json`, every `result.csv` and `summary.json` byte-identical;
  - all 18 PNGs pixel-identical (matplotlib image arrays equal).
- **Numerical settings (B4).** A variant of each mitigated deck with a 4 us maximum step (20 us in the record), analysed with 2 us resampling (10 us in the record), all 30 runs, through the wrapper:
  - rise and fall within 0.008 ms and shape within 0.1 % of the record in every run;
  - 26 dB bandwidths unchanged;
  - worst cells unchanged (A5 -64.10 dB, A4 -67.21 dB); individual runs within 1 dB (A5) and 2.8 dB (A4).

  The detector deck's convergence claim was not re-run; the analytic check below agrees with it.
- **Detector law by a different method (B5).** The reviewer solved the large-signal equation Is (exp(-Vo/nVt) I0(V/nVt) - 1) = Vo/RL with the deck's diode parameters, the 0.0756 tap, and the RF division between the diode capacitance (1.6 pF), the 22 pF hold and the 166 ohm tap source (factor 0.909). Results against LTspice agree within 5 %:

  | Amplitude (V peak) | Analytic | LTspice |
  |---|---|---|
  | 0.05 | 5.09 uV | 4.87 uV |
  | 0.35 | 0.259 mV | 0.248 mV |
  | 1 | 2.68 mV | 2.56 mV |
  | 1.7 | 11.2 mV | 10.6 mV |
  | 3 | 51.8 mV | 49.4 mV |
  | 22.36 | 1.27 V | 1.24 V |

  Without the hold division (the 470 pF design) the output is about 17 % higher (finding-9).
- **Spectrum routine (B5).** Independent code on the ideal envelope gives 291.7 / 208.3 / 125.0 Hz and -74.0 / -84.5 / -91.8 dB at 3 / 5 / 8 ms, equal to the note. The 28 800-sample record is exactly six periods. The F7 comparison is finding-7.
- **Analytic items.** The PWM ripple and loop margin hand checks are in rows C-13 and C-17. The slopes in `summary.json` (44.1 and 20.6 V/V, ratio 2.14) agree with the note's 44, 21 and 2.1.
- **Reviewer variants (scratchpad only, not committed).** `keying_rv.py` adds two variants to a copy of the checker:
  - `p05`: setpoint 0.5 W at both drain ends, the note's five corners;
  - `wide`: threshold corners -0.4, -0.2, -0.15, +0.15, +0.2 and +0.4 V.

  `keying_rv2.py` adds `fine` (B4). Every deck ran through `tools/ltspice-batch.sh` (PASS, exit 0). The reviewer opened the `p05` A5 corners render; it shows the foot step at the -0.1 V corner. Results are quoted in findings 1 and 2 and in rows C-5, C-7 and C-8.

## Inputs checked against their sources (CK-ANA-A4; every input that sets a reported result)

| Note section 3 row | Source read by the reviewer | Agreement |
|---|---|---|
| RA07M1317M Pout vs VGG (7.2 V, 20 mW) | `hardware/sim/tx-pa/data/ra07_pout_vs_vgg_{135,155}.csv` (digitized, INSP-114) | Above 2.6 V within 0.1 W; at 2.3 to 2.5 V the table is 0.9 to 3.3 dB high (finding-4) |
| RA07M1317M Pout vs VDD at VGG 3.5 V | `ra07_pout_vs_vdd_155.csv` | Scale 0.619 against 0.599 at 5.5 V, and 1.174 against 1.186 at 7.9 V (finding-4, small effect) |
| AFT05MS004N Pout vs VGS (Figure 12, 155 MHz, 7.5 V, 0.1 W) | Datasheet page 11, rendered | Shape agrees within graph reading at 1.5 to 2.2 V. The curve ends at about 2.42 V and 5.7 W (finding-4), and moves about +0.5 V at Pin 0.05 W (finding-2) |
| AFT05MS004N Crss 1.63 pF, VGS(th) 1.7 / 2.2 / 2.5 V | Table 5 | Yes (the spread is finding-2) |
| A4 drain scaling; A5 and A4 leakage | TS-012 sections 1 and 7.3 (estimates) | Quoted correctly; labelled E |
| 1N5711W model (HSMS-280x parameters) | Deck `.model` line against the note | Consistent; the surrogate is labelled E; analytic cross-check above |
| Idle bias 4.7 M, 10.6 mV | 5 V x 10 k / 4.7 M = 10.6 mV | Yes; the value is the author's (TS-012 gives none), labelled E |
| Divider 0.654, 1.77 k, 10 nF | TS-012 section 7.3: 2.7 k / 5.1 k | 5.1 / 7.8 = 0.654, and 2.7 k parallel 5.1 k = 1.77 k: yes |
| Key-down sequence 7.5 / 8 / 10 ms, gate 1 ms | TS-012 section 7.3 | Yes |
| Losses 0.5 dB; drain 5.5 / 7.9 V (A5) | TS-012 section 7.3 | Yes. `lpf-ts012.md` reports up to 1.21 dB passband loss (INSP-114 X-1), which moves the low-pack setpoint, not the keying shape |
| Firmware PWM 12 bits at 30.5 kHz | 125 MHz / 4096 = 30.52 kHz, 32.768 us | The arithmetic holds; the 125 MHz clock is an assumption (ADR-031 gives 150 MHz) |
| Raised-cosine convention | REQ-SYS-014 rationale: 3 ms is a 5.1 ms full transition | `RC_1090` = 0.5903: yes |

## Checklist answers

### A. Question, scope and traceable inputs

| Item | Answer | Evidence |
|---|---|---|
| CK-ANA-A1 | No | Six requirements, RSK-045, TC-SYS-013 and WP-PDR-22 are named and exist. HZ-008, HZ-004, REQ-SYS-011, REQ-SYS-114 and RSK-011 are not named (finding-6) |
| CK-ANA-A2 | Yes | TS-012 revision 4 is cited with its commit `7d0d450`; no schematic exists; every value the note chooses is labelled |
| CK-ANA-A3 | Yes | Section 3 gives a class and a source for every row |
| CK-ANA-A4 | No | Reviewer table above: the foot of the A5 curve and the end of the A4 curve disagree with the sources (finding-4) |
| CK-ANA-A5 | No | The +/-0.1 V corner is unsourced and not bounded; the temperature and drive-level assumptions are unstated (finding-2) |
| CK-ANA-A6 | No | The F7 and TC-TX-006 conflict is not routed (finding-7); the header does not state the partial WP-PDR-22 coverage (finding-8) |

### B. Model validity

| Item | Answer | Evidence |
|---|---|---|
| CK-ANA-B1 | No | Simplifications are listed in section 7, but the detector hold value and the ripple bound are not stated as such (finding-9) |
| CK-ANA-B2 | Yes | The only third-party model is the HSMS-280x diode, identified and labelled a surrogate |
| CK-ANA-B3 | Yes | The bandwidth routine is checked against F7's 292 Hz, and the detector law agrees with the reviewer's analytic solution within 5 % (the unexplained -60 dB point is finding-7) |
| CK-ANA-B4 | Yes | Detector step convergence is stated; the reviewer's 4 us / 2 us variant moves no reported number (above) |
| CK-ANA-B5 | Yes | Analytic detector law, independent spectrum code, and loop-margin and ripple hand checks (above) |
| CK-ANA-B6 | No | Uncertainty is listed qualitatively but not set against the A5 REQ-TX-005 margin of 0.015 ms or the corner width (finding-2) |

### C. Tools, validation status and reproducibility

| Item | Answer | Evidence |
|---|---|---|
| CK-ANA-C1 | No | The LTspice `.log` first line equals the lock; the note's spicelib version is wrong (finding-5) |
| CK-ANA-C2 | Yes | LTspice is accredited (TV-014, ACC-LTSPICE-001, wrapper blob `88b71475`); the checker has no TV record and the note marks the result developer evidence |
| CK-ANA-C3 | Yes | The README commands reproduce every number; netlists, one analysis each |
| CK-ANA-C4 | Yes | Reviewer re-run identical (above) |
| CK-ANA-C5 | Yes | TV-014 limitations respected: wrapper only, short run directories, lock, exit and log checks |

### D. Units, arithmetic and consistency

| Item | Answer | Evidence |
|---|---|---|
| CK-ANA-D1 | Yes | V peak, dBm, dB relative to total power and dBc are used consistently; conversions re-computed (for example 22.36 V peak = 5 W in 50 ohm) |
| CK-ANA-D2 | Yes | Every table value equals the checker output. The 9.7 % is 3.29 / 3 from the rounded 3.285 ms, rounded toward the limit. The -54 dB wording is finding-9 (iii), not a number used |
| CK-ANA-D3 | Yes | Rounding goes toward the limit where it matters (3.29 ms, +9.7 %) |
| CK-ANA-D4 | No | No REQ-TX-005 constant; the setpoint constant has no source (finding-3) |

### E. Results, margins, proposed values and credit

| Item | Answer | Evidence |
|---|---|---|
| CK-ANA-E1 | Yes | Limits are quoted with their ids and match the requirement texts at HEAD |
| CK-ANA-E2 | Yes | Margins have the right sign; no TPM applies to these requirements |
| CK-ANA-E3 | No | A5 REQ-TX-005 is reported PASS with 0.015 ms of margin against an unbounded corner, and both finalists' PASS depends on the corner width (finding-2); the 0.5 W step fails (finding-1) |
| CK-ANA-E4 | No | Exit 0 on FAIL; REQ-TX-005 not asserted (finding-3) |
| CK-ANA-E5 | N/A | No TBR value proposed |
| CK-ANA-E6 | N/A | No TPM current best estimate proposed |
| CK-ANA-E7 | Yes | Developer evidence on preliminary design data; no closing credit claimed |

### F. Every case named

| Item | Answer | Evidence |
|---|---|---|
| CK-ANA-F1 | No | 3, 5 and 8 ms and both pack ends are covered. The 0.5, 1 and 2 W steps, 7.4 V and the REQ-SYS-114 temperatures are missing (C-8 to C-10; findings 1 and 2) |
| CK-ANA-F2 | No | TS-012's late-contact and open-loop fault cases are not run (declared in section 1; finding-8) |
| CK-ANA-F3 | Yes | The worst corner is named per criterion in `result.json` and section 4.3 (the -0.1 V corner at 3 ms) |
| CK-ANA-F4 | No | The A5 REQ-TX-005 margin is within its uncertainty, and no sensitivity to the curve shift, drive level or temperature is shown (finding-2) |

### G1. Simulation decks and checkers

| Item | Answer | Evidence |
|---|---|---|
| CK-ANA-G1-1 | Yes | Decks, checker and plots are under `hardware/sim/tx-keying/`, and run-id folders tie them together |
| CK-ANA-G1-2 | Yes | Detector decks are `.tran` with `.meas`; keying decks are `.tran` only; the wrapper's `NC_` check passed |
| CK-ANA-G1-3 | Yes | The as-written loop follows TS-012 section 7.3 (reference, detector, idle bias, integrator, divider, clamps, sequence). The values TS-012 does not state (tap, idle bias, Cf, VGG node capacitor) are labelled as the author's |
| CK-ANA-G1-4 | Yes | The checker reads the `.raw` with spicelib and the `.meas` table of the log; `replot` refuses a changed deck; the wrapper removes stale outputs |

### G6. Timing

| Item | Answer | Evidence |
|---|---|---|
| CK-ANA-G6-1 | Yes | PWM period 32.768 us from an assumed 125 MHz clock (labelled); relay 7 ms plus 0.5 ms bounce from TS-012 |
| CK-ANA-G6-2 | Yes | The keying sequence edges (relay, CLK1, ramp start, drive gate) are all in the decks |
| CK-ANA-G6-3 | Yes | No duration comes from an Emulation run |
| CK-ANA-G6-4 | N/A | No off-nominal response time is claimed (the late-contact case is finding-8) |

### G7. Worst-case and tolerance

| Item | Answer | Evidence |
|---|---|---|
| CK-ANA-G7-1 | Yes | Extreme-value corners, one factor at a time, stated in section 4.3 |
| CK-ANA-G7-2 | No | No temperature coefficient; the threshold corner is not derived from the device tolerances (finding-2) |

### H. Hazards, risks and records

| Item | Answer | Evidence |
|---|---|---|
| CK-ANA-H1 | No | HZ-008 and HZ-004 are not named; no request to the hazards writer (finding-6) |
| CK-ANA-H2 | No | The re-scored envelope-loop risk is not sent to the risk writer (finding-6) |
| CK-ANA-H3 | No | No change history (finding-6) |

### I. Visual closure

| Item | Answer | Evidence |
|---|---|---|
| CK-ANA-I1 | Yes | The reviewer opened all 16 cited renders and the two uncited key-up plots (18), plus the rendered AFT05MS004N Figure 12 |
| CK-ANA-I2 | Yes | Axes carry units; limits are drawn with their ids (TC-SYS-013 band, REQ-SYS-015 band, REQ-TX-006 mask, REQ-TX-014 and REQ-SYS-183 lines); legends are present; each title names its case. Plotted values agree with `result.json` at the titled points (for example A5 as written, 542 Hz and -48.4 dB at 3 ms, 5.5 V; A5 mitigated, -64.1 dB at the -0.1 V corner) |

**ITEMS N/A:** CK-ANA-E5, CK-ANA-E6, CK-ANA-G2 to G5 (analysis_kind is simulation-deck, timing and worst-case), CK-ANA-G6-4, CK-ANA-J1 to J3 (criticality neither).

## Cross items (returned to Claude as lead SE)

- **X-1. TS-012 section 7.3 VGG graph read.** The note's F1 agrees with INSP-114 X-2: TS-012's "about 0 W at 1.5 V, 2 W at 2.5 V, 4 W at 3.0 V, 7 W at 3.5 V" does not match the RA07M1317M page 5 curves (digitized: about 1.0 W at 2.5 V, 7.1 W at 3.0 V, 8.4 W at 3.5 V). One request to the TS-012 author covers both.
- **X-2. TC-TX-006 known answer.** Two independent computations give 395 to 435 Hz for the -60 dB point, not the 614 Hz of F7 that TC-TX-006 step 2 uses as the checker's known answer. The TC-TX-006 author and the F7 owner should re-derive it before the TC-TX-006 checker is written (finding-7).
- **X-3. Owner-facing reading.** Three conclusions of the note hold in every reviewer run and can be read now: A4 has more keying margin than A5; the loop as written fails for both; REQ-TX-014 fails for A4 by estimate. The absolute claim "both pass every keying check" should not go to the owner until findings 1 and 2 are answered: at the 0.5 W step both finalists fail REQ-TX-005 at the note's own corners.

## Commands

- Search: `mcp__claude-context__search_code` on path `/Users/robinonsay/rust/cwht`, with the queries "keying envelope analysis TS-012 ALC detector key click review checklist" and "INSP id register next free inspection id INSP-116".
- Freeze and blobs: a Python loop over `git rev-parse 4ea4607:<path>` and `git rev-parse HEAD:<path>` (34 files).
- Re-run:
  1. `git archive 4ea4607 tools hardware/sim/tx-keying | tar -x -C <scratchpad>/kx`, then move the author's results to `results-author`.
  2. Run the two `tools/ltspice-batch.sh -t 600 -o ... -b det_char*.cir` commands of the README.
  3. Run `.venv/bin/python hardware/sim/tx-keying/keying_run.py` with `detchar`, `deck a4 asis`, `deck a4 mitig`, `deck a5 asis`, `deck a5 mitig` and `summary` (every exit 0).
  4. Compare bytes and pixels in Python.
- Variants: `<scratchpad>/kv/hardware/sim/tx-keying/keying_rv.py deck {a5,a4} {wide,p05}` and `keying_rv2.py deck {a5,a4} fine`, each through the wrapper (PASS, exit 0).
- Datasheet: the AFT05MS004N PDF from the web-fetch tool (SHA-256 prefix `84cd9fae`), read with `pdftotext -layout` and `pdftoppm -r 200 -f 11 -l 11`.
- Record check: `/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/validate_docs.py` (result in the reviewer's return).

## Verdict (returned by the reviewer)

```
VERDICT: NEEDS CHANGES
PRODUCT: docs/design/analysis/keying-ts012.md@bad53754, hardware/sim/tx-keying/keying_run.py@f85f2e29, decks and results as in product_files, at 4ea4607
FINDINGS:
- [Major] CK-ANA-F1, E3, A5 finding-1: the 0.5, 1 and 2 W steps (REQ-SYS-011; TC-TX-005 and TC-TX-006 name 0.5 W) are not analysed; reviewer run at 0.5 W with the note's own +/-0.1 V corners: A5 fails REQ-SYS-014 and REQ-TX-005 (shape 6.3 %, rise 3.40 ms at 3 ms, 5.68 ms at 5 ms), A4 fails REQ-TX-005 (rise 3.38 ms at 3 ms, 5.54 ms at 5 ms).
- [Major] CK-ANA-A4, A5, B6, E3, F4, G7-2 finding-2: the +/-0.1 V curve corner is unsourced and narrower than lot spread (AFT05 VGS(th) 1.7 to 2.5 V), drive-level shift (Figure 12) and temperature; A5 holds for about +/-0.12 V and A4 for about +/-0.15 to 0.2 V; the A5 REQ-TX-005 margin is 0.015 ms.
- [Major] CK-ANA-E4, D4, D2 finding-3: the checker does not assert REQ-TX-005 (+/-0.5 ms only), exits 0 on FAIL, and its setpoint criterion has no source.
- [Minor] CK-ANA-A4, A3 finding-4: graph reads differ from the project's digitized RA07M1317M curves at the foot and from Figure 12's end point; the slope estimate's direction is unstated.
- [Minor] CK-ANA-C1 finding-5: spicelib version misstated (1.6.3, not 2.5).
- [Minor] CK-ANA-A1, H1, H2, H3 finding-6: HZ-008, HZ-004, REQ-SYS-011, REQ-SYS-114 and RSK-011 not named; no risk or hazard requests; no change history.
- [Minor] CK-ANA-B3, A6 finding-7: the 395 against 614 Hz explanation is not shown; the TC-TX-006 known-answer conflict is not routed.
- [Minor] CK-ANA-A6, F2 finding-8: the header presents a partial WP-PDR-22 run as the pre-order check; the fault cases and the LDO range are not run.
- [Minor] CK-ANA-B1, D2 finding-9: detector hold value effect, PWM ripple "fail" wording on a bound, gate-step range.
ITEMS N/A: CK-ANA-E5, E6, G2 to G5, G6-4 (analysis_kind simulation-deck, timing, worst-case), CK-ANA-J1 to J3 (criticality neither)
VALUES PROPOSED: none
MEASUREMENTS: size=6 decks, 84 envelope runs and 26 detector steps; inputs_checked=12 rows (every input that sets a reported result); renders=18; turns=80; minutes=130; major=3; minor=6
```

## Iteration 2: delta verification of finding-1, finding-2 and finding-3 (Major) (2026-09-28, HEAD `65331c6`)

**Scope (rule C1).** Iteration 2 is a delta. It verifies the fixes of finding-1, finding-2 and finding-3 (Major) and scans the changed note, decks, checker and results for defects that revision 1 introduced. finding-4 to finding-9 (Minor) were not addressed by revision 1 (note section 10 lists findings 1 to 3 only) and are not re-reviewed, except for a status line below. Product: the 55 blobs of front matter `product_files`, committed as `e9f1440` (note revision 1, runs `results/2026-09-28-r1-*`, re-freeze under rule C2). Each equals `git rev-parse e9f1440:<path>` and `git rev-parse HEAD:<path>` at HEAD `65331c6`. `git log e9f1440..HEAD` holds two commits (`8527083`, `65331c6`, CR-007 review records only). The eight run folders' copies of `keying_run.py` and of their decks equal the checked-in files. No product blob is on a `cr/` branch. Checklist as iteration 1: `peer-review-checklist-analysis.md` revision A, blob `0386cc6e`, still only on `cr/CR-012-pdr-checklist-templates` (head `7784672`, not an ancestor of `main`).

**Independence (rule C4).** This invocation authored no part of the note, its revision 1, the decks, the checker, TS-012 or the iteration 1 review, and edited no product file. It changed only this record.

**The truncated finding-3 text.** The author received finding-3 cut off after "It checks only TC-SYS-0" and took it to mean REQ-TX-005's +/-10 % was not asserted. Its full text is the iteration 1 row above: (a) REQ-TX-005 not asserted; (b) the checker exits 0 whatever the verdicts; (c) the `setpoint` criterion (+/-0.5 dB) has no source. The fix asked for all three. Part (a) is what made the finding Major (the template's "the checker does not assert the acceptance value": the note's "+9.7 %" came from a hand computation, and the checker passed 3.47 ms at the 3 ms setting). Parts (b) and (c) change no number, margin or verdict of the note, so they are Minor by the template's definition. They are re-raised as finding-11 (Minor) rather than holding finding-3 open.

**Search first (charter section 11 rule 1).** One `git log`/`git show --stat` and one `ls` of the checklists directory (known paths, not searches) ran first. `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` then ran before every manual search (queries: "keying analysis review INSP findings iteration 1 REQ-TX-005 TC-SYS-013 rise time"; "rule C1 review iteration verdict APPROVED NEEDS CHANGES Major findings delta iteration liens"; "thermal note junction temperature 45 C ambient AFT05MS004N RA07M1317M section 4.1"). `grep` then only pinned lines in known files (the note, `keying_run.py`, TS-012, `thermal-ts012.md`, `pa-drive-ts012.md`, the d2 and d3 `result.md`). The rustos tree was not read.

**Sources re-read by the reviewer (2026-09-28).** The digitized RA07M1317M curves `hardware/sim/tx-pa/data/ra07_pout_vs_vgg_{135,155}.csv` and `ra07_pout_vs_vdd_{135,155}.csv` (recomputed below); `docs/design/analysis/thermal-ts012.md` section 4.1 (junction and inhibit tables); `docs/design/analysis/pa-drive-ts012.md` section 4.2 and runs `r1-d2`, `r1-d3` (`result.md`: A5 5.4 / 11.4 / 35.5 mW, A4 45.8 / 89.4 / 180.0 mW; select-on-test 11.0 to 27.2 mW); `requirements.json` REQ-TX-005 (text and `tbr` object); Nexperia 74LVC1G66 product data sheet Rev. 14.1, 3 September 2024, https://assets.nexperia.com/documents/data-sheet/74LVC1G66.pdf (web-fetch tool, SHA-256 prefix `5e35437c`), Table 7: IS(OFF) typ +/-0.1 uA, max +/-0.2 uA (-40 to +85 C), +/-0.5 uA (-40 to +125 C), at VCC 5.5 V.

**Reproduction (CK-ANA-C4, readiness R2).** Clean `git archive e9f1440 tools hardware/sim/tx-keying hardware/sim/tx-pa/data` in the scratchpad, the author's nine `results/2026-09-28-r1-*` folders moved to `results-author` (the detector runs `2026-09-28-det-char*`, unchanged since iteration 1, kept). Then `/Users/robinonsay/rust/cwht/.venv/bin/python hardware/sim/tx-keying/keying_run.py deck <fin> <var>` for a4 and a5 with asis, sweep0, fix and sweep1, then `summary`. Every deck ran through `tools/ltspice-batch.sh` (blob `88b71475`): eight "result: PASS ... version_line='LTspice 26.0.2 for MacOS' ltspice_exit=0" lines, each with the deck SHA-256 of the author's `wrapper.txt`. No `.log` contains "warning". The first `a5 sweep1` attempt returned the wrapper's exit 5 (lock busy: the reviewer's own variant runs held it for more than 600 s); it was rerun with `CWHT_LTSPICE_LOCK_WAIT=2400` and passed. Against the committed outputs, **57 of 57 files agree**: every deck, `result.json`, `result.csv` and `summary.json` byte-identical, all 23 PNGs pixel-identical (image arrays equal). The eight LTspice logs differ only in the temporary run directory and the start and elapsed times. Every `deck` stage and `summary` exited 0, including `a5 fix`, whose `result.json` lists 18 failing element-1 runs (finding-11).

**Reviewer scripts (scratchpad, not product):**
- `rv_el2.py`: element 2 (which the checker does not check) from the author's `.raw`.
- `rv_indep.py`: an independent 10-to-90 % and shape computation on the native time points (no resampling), for four `a5 fix` runs.
- `rv_fine.py` (imports the product `keying_run.py` unchanged): `sweepfine`, VSH at 0.01 V steps across each element-1 window edge, at 6.4, 7.4 and 8.4 V packs, at 0.5 and 2 W (270 runs per finalist); `sweepvos`, the same edges with the +/-1 mV residual offset acting the same way, at the four steps, 7.4 V (180 runs per finalist).
- `rv_slope.py`: the revision 1 threshold sweep with the estimated sub-threshold slope `SUBTH_DB_PER_V` at 65 and 150 dB/V instead of 100 (both the PA and the firmware table below the graph), at 0.5 and 2 W, 7.4 V (78 runs each).

All reviewer decks ran through the wrapper (PASS, exit 0), 1212 LTspice steps in all.

### Verification of finding-1 (Major), case by case (rule C7)

| Finding | Case the finding named | Check at `e9f1440` | Result |
|---|---|---|---|
| finding-1 | The 0.5 W step, at the note's own corners | Run `sweep0` (revision 0 design, VSH -0.30 to +0.30 V, 0.5 and 5 W, 7.4 V) reproduces the iteration 1 reviewer numbers: A5 at -0.1 V rise 3.40 ms (3 ms), 5.68 ms (5 ms), 9.01 ms (8 ms), shape 6.2 %; A4 3.38 and 5.53 ms; A5 at +0.1 V 2.57 ms. The checker now flags them (A5 0.5 W, -0.1 V, 3 ms: `t1090_req_tx005` FAIL, `shape` FAIL). Revision 0's "PASS at every corner" is withdrawn in the summary, section 4.3 and section 5.1 | Yes |
| finding-1 | The 1 W and 2 W steps (REQ-SYS-011; 1 W default, REQ-SYS-064) | `fix` and `sweep1` run 0.5, 1, 2 and 5 W. The binding step is 2 W, where the +7 dB tap is off and the visibility floor is 31.5 dB under the envelope top (0.5 W with the tap: 32.5 dB; 1 W: 35.5 dB). The windows follow that order in `sweep1` (2 W narrowest for both finalists) | Yes |
| finding-1 | 7.4 V (TC-TX-005 names 6.4, 7.4 and 8.4 V) | `fix` runs all three packs (108 runs per finalist). The sweeps run at 7.4 V only, and the note says the 7.4 V windows stand for the others (the pack moves element 1's error by at most 1.8 % (A4) and 1.2 % (A5), reproduced from `fix`: 1.79 and 1.18 %). Reviewer `sweepfine` at every pack: edges move by at most 0.005 V (A5 2 W: -0.083 / +0.136 at 6.4 V, -0.084 / +0.137 at 7.4 V, -0.084 / +0.132 at 8.4 V; A4 2 W: -0.169 / +0.213, -0.169 / +0.213, -0.171 / +0.211). The 8.4 V A5 high edge is 0.005 V inside the quoted +0.137 V (in finding-13) | Yes |
| finding-1 | A step-dependent change if the low steps fail, and restated verdicts | Items 9 (held trim) and 10 (+7 dB tap at 0.5 and 1 W) are added, modelled in `fix` and `sweep1`, and the verdicts of the summary, 4.3, 4.4 and 5.1 are restated. Loop margin with the tap: reviewer hand check of the A5 7.9 V steepest point with the tap off (slope 59.3 V/V recomputed from the digitized CSVs, detector slope 0.0679 V/V between 9 and 15 V, RC 44.8 us): crossover 2.29 kHz, 90 - atan(2 pi 2287 x 17.7 us) - atan(2 pi 2287 x 4.7 us) = 71.9 degrees, equal to `summary.json`; minimum with the tap 58.4 degrees (A4, 8.1 V), against 45 degrees | Yes |
| finding-1 | "Every element after the first passes" (new claim) | The checker checks elements 3 to 8 and element 1, not element 2. Reviewer `rv_el2.py` on the author's `sweep1` and `fix` `.raw`: element 2 passes in all 528 runs (worst 10-to-90 error 2.13 %, shape 0.88 %), the same as elements 3 to 8: the trim converges within element 1. So the claim holds for element 2 too, with the ideal hold of the model (see finding-14) | Yes |

**Result: finding-1 Verified.**

### Verification of finding-2 (Major), case by case (rule C7)

| Finding | Case the finding named | Check at `e9f1440` | Result |
|---|---|---|---|
| finding-2 | Bound the residual curve error after calibration with sources or labelled estimates (lot, drive over frequency and temperature, device temperature, table read) | Section 3.2 and `THRESHOLD_BUDGET` carry four cases (uncalibrated, calibrated, compensated, stored trim), each term classed D, DD or E with a source. Reviewer recomputation of every total: calibrated -0.2775 / +0.1525 V (RSS -0.218 / +0.100); compensated -0.1635 / +0.086 V (RSS -0.110 / +0.054); stored -0.112 / +0.1745 V (RSS -0.073 / +0.096); uncalibrated A4 -1.27 / +0.92, A5 -1.06 / +0.74 V. Drive terms: 10 log(180 / 89.4) = 3.04 dB and 10 log(89.4 / 45.8) = 2.90 dB (A4, r1-d3); 10 log(27.2 / 11.0) / 2 = 1.97 dB (A5, pa-drive 4.2); in-unit 0.17 + 0.10 dB, times 0.167 V/dB = 0.045 V. Temperature: -2.5 mV/C x (110 - 25) = -0.2125 V and x (-10 - 25) = +0.0875 V. Two terms are mis-bounded against their own sources (finding-12, Minor) | Yes (finding-12 raised) |
| finding-2 | A4 also needs per-unit calibration; state what calibration covers | Summary, 3.2 and item 7: per-unit table for both finalists, measured at build with the drive on into the dummy load, down to the visibility floor, at 146 MHz, bench pack and room temperature | Yes |
| finding-2 | The temperature case (REQ-SYS-114, module heating) | Carried as a budget term (die -10 to 110 C at -1.3 to -2.5 mV/C, E, two web sources cited with date), with NTC compensation (item 8) and its residual. REQ-SYS-114 named in 3.2 | Yes |
| finding-2 | The A5 table off the digitized curves (iv) | A5 now uses the mean of the project's digitized curves. Reviewer recomputation from the CSVs: 0.113 / 0.359 / 1.021 / 2.222 / 3.721 / 5.265 / 7.072 W at 2.32 / 2.40 / 2.50 / 2.60 / 2.70 / 2.80 / 3.00 V, and VDD scale 0.606 / 0.875 / 1.180 at 5.5 / 6.7 / 7.9 V, equal to section 3.1 | Yes |
| finding-2 | Report the margin against that bound (or state the pass as conditional) | The +/-0.1 V corner is replaced by a 0.05 V sweep with interpolated windows, compared with each budget (section 4.4.3, `windows.png`). Reviewer 0.01 V `sweepfine` reproduces the interpolated edges within 0.005 V (A5 2 W -0.084 / +0.137, A4 2 W -0.169 / +0.213 at 7.4 V, against -0.084 / +0.137 and -0.168 / +0.211). Independent crossing and shape code (`rv_indep.py`) on four `a5 fix` runs agrees with the checker within 0.001 ms and 0.04 % (run 49: 3.540 ms, +18.0 %, shape 6.65 % against 6.67 %). Margins recomputed: A4 stored-trim worst-case sum 0.056 V low and 0.0365 V high; A5 over by 0.028 and 0.0375 V; A5 RSS margin 0.011 and 0.041 V; A4 compensated 0.0045 V inside. The 0.015 ms A5 margin statement is withdrawn. Sensitivity of the windows (slope, offset, pack) is not quantified (finding-13, Minor) | Yes (finding-13 raised) |

**Result: finding-2 Verified.**

### Verification of finding-3 (Major), part (a)

| Finding | Case the finding named | Check at `e9f1440` | Result |
|---|---|---|---|
| finding-3 | (a) Add a REQ-TX-005 criterion (+/-10 % of the setting, id in a comment), keep TC-SYS-013's separately | `REQ["t1090_rel_tol"] = 0.10` with the comment "REQ-TX-005 / TC-TX-005"; `analyse()` sets `t1090_req_tx005` (every rise and fall of elements 3 to 8 within 10 % of the setting), `t1090_tc_sys013` (+/-0.5 ms) and `shape` separately, and `first_t1090_req_tx005`, `first_t1090_tc_sys013`, `first_shape` for element 1; a NaN crossing fails. `failing_runs` lists the runs per criterion; `t1090.png` and `window.png` draw both limits. Known-answer check on the iteration 1 cases: A5 `sweep0` 5 W, -0.15 V, 3 ms (3.45 ms, +15.0 %): `t1090_req_tx005` FAIL, `t1090_tc_sys013` PASS; 0.5 W, -0.1 V (3.40 ms, +13.3 %): the same. The +9.7 % hand computation is gone from the note | Yes |
| finding-3 | (b) Exit non-zero on a failing case, or a `--check` mode with the expected FAIL states; (c) source or drop the `setpoint` criterion | Not done: `stage_deck()` exits 0 after writing FAIL verdicts (re-run: every stage exit 0, `a5 fix` with 18 failing element-1 runs, both `asis` runs failing every criterion). `setpoint` is still +/-0.5 dB, now listed under the "TS-012 section 7.3 WP-PDR-22 criteria" row of section 1, which has no such criterion (TS-012 `7d0d450` has no 0.5 dB setpoint limit; REQ-SYS-012 is +/-1 dB of 5 W). Neither changes a reported number or verdict (the `setpoint` criterion passes in every revision 1 design run, within 0.009 dB) | Re-raised as finding-11 (Minor) |

**Result: finding-3 Verified** for part (a), the part that made it Major. Parts (b) and (c) are finding-11.

### Minor findings not addressed in revision 1 (status only)

- finding-4: Open, partly answered. The A5 table is now the digitized curves (verified above), and limitation 3 states the direction of the 100 dB/V estimate (a steeper foot narrows the windows; the digitized A5 foot is 63 to 71 dB/V, reviewer 62.9 dB/V at 2.32 to 2.40 V). The A4 table still ends at 2.35 V and 5.6 W, and no read resolution is stated.
- finding-5: Open. The wrong "spicelib 2.5" is gone, but the Tool row now gives no version of spicelib, numpy or matplotlib.
- finding-6: Open. HZ-008, HZ-004, REQ-SYS-011 in the header, RSK-011, the two requests and a change log are still missing (REQ-SYS-114 is now named in section 3.2).
- finding-7: Open. Limitation 13 keeps the unsupported cause of the 395 against 614 Hz difference; no request to the TC-TX-006 and F7 owners.
- finding-8: Open. The header still calls the note "the pre-order LTspice check"; section 8 item 1 now lists the fault cases for the WP-PDR-22 rerun.
- finding-9: Open. (i) the 22 pF hold of `det_char.cir` is not stated; (ii) section 4.6 still says the 30.5 kHz ripple "fail[s] REQ-TX-006" on a bound; (iii) moot (section 4.5 now quotes the backwave level, not the gate step).

### New findings (iteration 2)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-10"></a>finding-10 | reviewer | Major | CK-ANA-D2, E1 | note section 4.6 (whole), section 4.4.3 first bullet ("44 V of RF amplitude per volt of VGG ... against 21 V/V"), section 4.6 last bullet ("its slope is 2.1 times A4's"); README run row `2026-09-28-r1-summary` ("PWM result unchanged from revision 0"); against `results/2026-09-28-r1-summary/summary.json` key `pwm_ripple` and `pwm_ripple.png` | **Section 4.6 quotes revision 0's PWM ripple results, which the revision 1 checker output contradicts.** The note says the section is "Unchanged from revision 0 (the trim gain does not enter the feedforward path)". But revision 1 replaced the A5 PA table with the digitized curves, and the ripple bound scales with the steepest PA slope. The revision 1 `summary.json` gives A5 slope 59.2 V/V (revision 0 44.1; reviewer recomputation from the CSVs 59.3 V/V) and feedforward sidebands of -40.6 dBc at 30.5 kHz, **-58.1 dBc at 61 kHz** and -76.1 dBc at 122 kHz. The note says -43, **-60.7 ("marginal")** and -79 dBc. So the 61 kHz (11-bit) option for A5 changes from a 0.7 dB pass to a 1.9 dB fail of REQ-TX-006, and the cited `pwm_ripple.png` draws it red (FAIL) beside a text that calls it marginal. The A5 to A4 slope ratio is 2.9, not 2.1. The same stale 44 V/V appears in section 4.4.3 as the explanation of A5's narrower window. The A4 figures and the design rule (122 kHz or a third pole, A5 at 122 kHz -76.1 dBc, +16.1 dB) are unaffected, and so is the TS-012 reading. **Fix:** restate section 4.6 and the 4.4.3 bullet from the revision 1 `summary.json` (-40.6 / -58.1 / -76.1 dBc; 59 V/V against 21 V/V, ratio 2.9; 61 kHz fails for A5), and correct the README row | Open | Pending | |
| <a id="finding-11"></a>finding-11 | reviewer | Minor | CK-ANA-E4, D4 | `keying_run.py` `stage_deck()` (no exit status on FAIL); `analyse()` `setpoint` criterion and `window_of()` "steady" set; note section 1 table, last row | **The two unaddressed parts of finding-3's fix** (the author received a truncated text). (b) The checker exits 0 with FAIL verdicts (re-run: all eight `deck` stages exit 0, `a5 fix` with 18 failing element-1 runs; 08 section 3.4 and CK-ANA-E4 ask for a non-zero exit on a failing case). Several runs are expected to fail (as written; the revision 0 design; element 1 at the budget corners), so a `--check` mode with the expected FAIL states per run id is the practical form. (c) The `setpoint` criterion (top power within +/-0.5 dB of the setpoint) has no source, and section 1 now lists it under "TS-012 section 7.3 WP-PDR-22 criteria", which has no such limit; REQ-SYS-012 is +/-1 dB. It passes in every revision 1 design run (within 0.009 dB), so no result moves. **Fix:** exit non-zero on an unexpected FAIL (or add `--check` with the expected states); label the setpoint criterion as the analysis's own model-health check (or tie it to REQ-SYS-012 at +/-1 dB) and move it out of the TS-012 row | Open | Pending | |
| <a id="finding-12"></a>finding-12 | reviewer | Minor | CK-ANA-A4, A5, G7-2 | `keying_run.py` `_comp_hi`, `T_DIE`, the stored and compensated gradient terms; note section 3.2 ("110 C is the junction bound of the thermal note", "the die up to 25 K above the NTC", compensated high end +0.021 V) | **Two budget terms are narrower than their own sources.** (i) The compensated high end takes the coefficient residual (+/-0.6 mV/C) only on the cold side (+0.6 mV/C x 35 K = +0.021 V). The same residual acts on the hot side with the opposite sign when the true coefficient is -1.3 mV/C and the firmware applies -1.9 mV/C: +0.6 mV/C x 60 K = +0.036 V. The compensated worst-case high end is then +0.101 V, not +0.086 V (the `fix` record corner is +0.086 V). Both finalists' element-1 windows still cover it (A4 +0.211, A5 +0.137 V). (ii) `thermal-ts012.md` section 4.1 does not give 110 C as a junction bound: with the 85 C REQ-SYS-118 inhibit on the PA case the junction reaches 108.2 C (A5-DC) and 113.8 C (A4-DC) at the trip, 111.3 and 117.0 C with the +3 C tolerance, and 126.0 and 122.7 C steady without protection. The die-to-NTC difference at the trip is 23 K (A5) and 29 K (A4), against the 25 K used for both. With A4's 29 K at 2.5 mV/C the A4 stored-trim high end becomes about +0.185 V (margin 0.026 V instead of 0.036 V; still PASS). The A4 compensated low end becomes about -0.174 to -0.175 V against a -0.168 V window, which turns section 5.1's "Marginal" into a fail by 0.007 V (estimate). That is the power-on case with no stored trim, so item 9's stored trim becomes necessary for A4 as well. **Fix:** take the residual on both sides; take the die maximum and the die-to-NTC difference per finalist from `thermal-ts012.md` section 4.1 (or state why 110 C and 25 K bound them); restate the compensated rows of 4.4.3 and 5.1 | Open | Pending | |
| <a id="finding-13"></a>finding-13 | reviewer | Minor | CK-ANA-B6, F4 | note sections 4.4.3 (windows against budgets), 5.1, limitation 3 and limitation 11; `window_interp()` | **The element-1 windows that decide A4 against A5 are compared with the budgets without the residual offset, the other packs, or the estimated sub-threshold slope, and the note does not quantify these.** Reviewer runs, element 1, worst step (2 W) unless stated: (i) +/-1 mV residual offset (the note's own VOS corner, which `sweep1` leaves at 0): A5 -0.080 / +0.132 V, A4 -0.163 / +0.204 V; (ii) 8.4 V pack: A5 high edge +0.132 V; (iii) sub-threshold slope 65 dB/V: A5 -0.119 / +0.151 V, A4 -0.162 / +0.269 V; 150 dB/V: A5 -0.064 / +0.117 V, A4 -0.128 / +0.172 V. The step at the foot of element 1 (about 14 % amplitude in about 0.4 ms, `corners.png`) sits at about 10 to 70 mW, below the graphs, where the 100 dB/V estimate sets the PA gain: a VSH of -0.164 V multiplies the foot amplitude by about 10^(16.4 / 20) = 6.6. Consequences: A5 fails the stored-trim worst-case sum at every slope tried; its RSS pass keeps 0.007 V of margin with the offset and fails by 0.009 V at 150 dB/V. A4's worst-case pass holds at 65 and 100 dB/V and with the offset (margin 0.029 V high), and fails by 0.003 V at 150 dB/V. The A4-to-A5 window ratio stays 1.6 to 1.7 in every case, so the comparative reading holds. Also, `window_interp()` interpolates linearly across the step-like jump of the element-1 time error (A4 3 ms 2 W: 5.4 % at -0.18 V, 17.9 % at -0.19 V), which is not conservative in general; here the jump lies outside the shape edge (-0.169 V), and the 0.01 V sweep moves no edge by more than 0.005 V. **Fix:** state these sensitivities in 4.4.3 (or run the budget comparison with the offset corner and at the packs), and say that A4's worst-case pass holds for a sub-threshold slope up to about 145 dB/V (the graph segments suggest shallower) | Open | Pending | |
| <a id="finding-14"></a>finding-14 | reviewer | Minor | CK-ANA-B1 | note section 5.2 item 9 ("The MCP6002's 1 pA bias current into Cf ... droops the held output by well under 1 mV per second, so the hold lasts through normal pauses"); limitation 7 | **The hold-droop statement leaves out the switch leakage of the part it names, which the datasheet bounds far higher.** The held trim is what makes every element after the first pass (section 4.4.1: "The one that matters most"). The deck models an ideal hold. For the 74LVC1G66 the note names, Nexperia Rev. 14.1 Table 7 gives IS(OFF) +/-0.1 uA typical and +/-0.2 uA maximum (-40 to +85 C, VCC 5.5 V). At 0.2 uA into Cf the integrator output moves 45 V/s (A5, 4.48 nF) and 104 V/s (A4, 1.92 nF), 7 and 17 mV of VGG per ms through KTRIM 0.16, or 0.17 V and 0.4 V over one 24 ms gap at 50 WPM. The limit is at 5.5 V across the switch, and the real leakage near virtual ground is likely orders of magnitude lower (estimate), but the note's "well under 1 mV per second" is not shown for the named part. The MCP6002 bias also rises with temperature (not quantified in the note). A firmware route exists: item 9's ADC capture applied at every element would make each element start from the last one's trim with only the ADC step (+/-0.01 V) and short-term drift, inside every window. **Fix:** bound the droop with the chosen switch's and op-amp's datasheet leakage at the REQ-SYS-114 hot end and the actual voltage across the switch, or make the per-element capture the design basis; carry the hold into the section 8 item 1 rerun | Open | Pending | |

### Per-case results (iteration 2; section F, one row per case the governing texts name)

Values are the checker's (estimates where the inputs are), from the committed `result.json` and `summary.json`, which the reviewer's re-run reproduced.

| Case | Condition | Governing id and limit | Result (checker output) | Margin with sign | Uncertainty | Reviewer re-check | Finding ids |
|---|---|---|---|---|---|---|---|
| C-1 | As written, 5 W, 6.4 and 8.4 V, both finalists | REQ-SYS-014 via TC-SYS-013; REQ-TX-005 | A4 10-to-90 error up to -45 %, shape 19.2 %; A5 -59 %, 28.8 %: FAIL | negative | model | re-run identical | none |
| C-2 | As written, 3 ms | REQ-SYS-015: 350 Hz | A4 417 Hz, A5 583 Hz: FAIL | -67 / -233 Hz | model | re-run identical | none |
| C-3 | As written | REQ-TX-006: -60 dB | A4 -49.8 dB, A5 -46.9 dB: FAIL | -10.2 / -13.1 dB | model | re-run identical | none |
| C-4 | Revision 0 design, 0.5 W, 7.4 V, VSH sweep | REQ-TX-005, TC-SYS-013 | window A4 -0.079 to +0.111 V, A5 -0.053 to +0.067 V, against the calibrated budget -0.2775 to +0.1525 V: FAIL | negative | budget estimates | re-run identical; iteration 1 numbers reproduced | none |
| C-5 | Revision 1 design, elements 3 to 8, 0.5 / 1 / 2 / 5 W, 6.4 / 7.4 / 8.4 V, 3 / 5 / 8 ms, record corners (108 runs) | REQ-TX-005 10 %; TC-SYS-013 0.5 ms and 5 % | worst error 2.2 % (A4), 1.9 % (A5); shape 0.9 %: PASS | +7.8 % / +8.1 %; +4.1 % | ideal hold (finding-14) | re-run identical; element 2 passes too (2.13 %, 0.88 %) | finding-14 |
| C-6 | Same, elements 3 to 8, VSH -0.30 to +0.30 V (sweep) | same | PASS over the whole sweep at every step | covers the calibrated budget | ideal hold | re-run identical | finding-14 |
| C-7 | Same, every step and pack | REQ-SYS-015: 350 Hz | 292 / 208 / 125 Hz | +58 Hz | small | re-run identical | none |
| C-8 | Same, every step including 0.5 W | REQ-TX-006: -60 dB | A4 -69.1 dB, A5 -69.4 dB | +9.1 / +9.4 dB | small | re-run identical | none |
| C-9 | Element 1, stored-trim budget (worst-case sum -0.112 / +0.1745 V), worst step 2 W, 7.4 V | REQ-TX-005, TC-SYS-013 | A4 window -0.168 / +0.211 V: PASS; A5 -0.084 / +0.137 V: FAIL | A4 +0.056 / +0.0365 V; A5 -0.028 / -0.0375 V | slope, offset, pack, gradient | 0.01 V sweep within 0.005 V; with the offset A4 +0.029 V high; A4 -0.003 V at 150 dB/V | finding-12, finding-13 |
| C-10 | Element 1, stored-trim RSS (-0.073 / +0.096 V) | same | A4 PASS; A5 PASS | A5 +0.011 / +0.041 V | as C-9 | A5 +0.007 V with the offset; -0.009 V at 150 dB/V | finding-13 |
| C-11 | Element 1 after power-on without a stored trim, compensated worst-case sum (-0.1635 / +0.086 V) | same | A4 0.0045 V inside at 7.4 V (2 runs fail shape by 0.1 % with the offset): "Marginal"; A5 FAIL | A4 about 0; A5 -0.080 V | as C-9 | A4 about -0.007 V with the thermal note's 29 K gradient (finding-12) | finding-12 |
| C-12 | Loop phase margin, revision 1, tap off and +7 dB | TS-012 WP-PDR-22: 45 degrees | 71.9 to 79.5 degrees (tap off, steepest), 58.4 to 65.9 degrees (tap on) | +13.4 degrees | first-order model | hand: 71.9 degrees (A5, 7.9 V) | none |
| C-13 | Overshoot; VGG maximum (A5) | TS-012: 0.2 dB; 3.5 V | 0.004 dB; 3.14 V | +0.196 dB; +0.36 V | small | re-run identical | none |
| C-14 | PWM carrier ripple, feedforward, A5 | REQ-TX-006 | 30.5 kHz -40.6 dBc, 61 kHz -58.1 dBc, 122 kHz -76.1 dBc (checker); note -43 / -60.7 / -79 dBc | 122 kHz +16.1 dB; 61 kHz -1.9 dB (note: +0.7 dB) | analytic bound | slope recomputed 59.3 V/V | finding-10 |
| C-15 | Key-up, exciter driven | REQ-TX-014: -30 dBm | A4 -19.5 dBm, A5 -17.5 dBm (modelled leakage): FAIL by estimate | -10.5 / -12.5 dB | estimates | re-run identical; loop tail -73.5 dBm (A4), below -100 dBm (A5) | none |
| C-16 | Step and pack coverage | REQ-SYS-011, REQ-SYS-064, TC-TX-005 | 0.5 / 1 / 2 / 5 W; 6.4 / 7.4 / 8.4 V in `fix`; sweeps at 7.4 V | edges move at most 0.005 V between packs | | reviewer `sweepfine` | finding-13 |
| C-17 | REQ-SYS-114 temperatures | REQ-SYS-114 | carried as the die-temperature budget term (-10 to 110 C) | see C-9 to C-11 | coefficient E | thermal note re-read | finding-12 |

### Findings (iteration 2; current state of every finding of this record)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| finding-1 | reviewer | Major | CK-ANA-F1, E3, A5 | note sections 1, 2, 4.3, 4.4, 5.1 | See iteration 1 and the verification table | Verified (iteration 2, revision 1 at e9f1440) | n/a | |
| finding-2 | reviewer | Major | CK-ANA-A4, A5, B6, E3, F4, G7-2 | note sections 3.1, 3.2, 4.3, 4.4.3, 5.1 | See iteration 1 and the verification table; budget-term defects are finding-12, sensitivities finding-13 | Verified (iteration 2) | n/a | |
| finding-3 | reviewer | Major | CK-ANA-E4, D4, D2 | `keying_run.py` `REQ`, `analyse()` | Part (a), REQ-TX-005 asserted; parts (b) and (c) are finding-11 | Verified (iteration 2, part a) | n/a | |
| finding-4 | reviewer | Minor | CK-ANA-A4, A3 | note section 3.1, `A4_W` | See iteration 1; the A5 part answered | Open | Pending | |
| finding-5 | reviewer | Minor | CK-ANA-C1 | note header "Tool" row | See iteration 1; no version now given | Open | Pending | |
| finding-6 | reviewer | Minor | CK-ANA-A1, H1, H2, H3 | note header, sections 5.1 and 8 | See iteration 1 | Open | Pending | |
| finding-7 | reviewer | Minor | CK-ANA-B3, A6 | note limitation 13 | See iteration 1 | Open | Pending | |
| finding-8 | reviewer | Minor | CK-ANA-A6, F2 | note header | See iteration 1 | Open | Pending | |
| finding-9 | reviewer | Minor | CK-ANA-B1, D2 | `det_char.cir`; note section 4.6 | See iteration 1; item (iii) moot | Open | Pending | |
| finding-10 | reviewer | Major | CK-ANA-D2, E1 | note sections 4.6 and 4.4.3; README | See the new findings table | Open | Pending | |
| finding-11 | reviewer | Minor | CK-ANA-E4, D4 | `keying_run.py` `stage_deck()`, `setpoint`; note section 1 | See the new findings table | Open | Pending | |
| finding-12 | reviewer | Minor | CK-ANA-A4, A5, G7-2 | `THRESHOLD_BUDGET`; note section 3.2 | See the new findings table | Open | Pending | |
| finding-13 | reviewer | Minor | CK-ANA-B6, F4 | note section 4.4.3, 5.1, limitations 3 and 11 | See the new findings table | Open | Pending | |
| finding-14 | reviewer | Minor | CK-ANA-B1 | note section 5.2 item 9 | See the new findings table | Open | Pending | |

### Cross items (iteration 2, returned to Claude as lead SE)

- X-4. **Owner-facing reading for TS-012.** What holds in every reviewer run: the loop as written fails for both finalists; with the revision 1 design every element after the first passes for both; the first element of an over binds; A4's first-element window is 1.6 to 1.7 times A5's at 65, 100 and 150 dB/V, with and without the offset, at every pack. A5 fails the stored-trim worst-case sum in all of these. A4's worst-case pass is an estimate that holds at a sub-threshold slope up to about 145 dB/V and with the +/-1 mV offset (finding-13). This can go to the owner now as "keying now favours A4". finding-10 does not touch it.
- X-5. **Item 9 for A4.** With the thermal note's A4 die-to-NTC difference (29 K at the inhibit trip), A4's power-on case without a stored trim fails by about 0.007 V (finding-12). WP-PDR-22 should treat the stored trim (or the per-element capture of finding-14) as required for both finalists, not only as an A5 need.
- X-6. **Hold circuit.** The ideal hold carries the "every element after the first" result. The WP-PDR-22 circuit needs a leakage bound (finding-14). The firmware capture at every element removes the dependence and costs no part.
- X-7. **TC-TX-005 automation.** TC-TX-005 names a checker option `--corners` and expects the checker to report per keyed element. When that checker is built from `keying_run.py`, finding-11's exit status matters (08 section 3.4). Iteration 1 X-2 (the TC-TX-006 614 Hz known answer) is still open.

### Checklist items changed at iteration 2

Now Yes:
- CK-ANA-F1: every step and pack of REQ-SYS-011, REQ-SYS-064 and TC-TX-005 is a case; REQ-SYS-114 is a budget term.
- CK-ANA-E3: margins are reported against the budgets, and the A5 worst-case fail is not reported as passing. finding-13 asks for the sensitivities.
- CK-ANA-E5: Yes. Section 8 item 8 proposes keeping REQ-TX-005 at +/-10 % (TBR), names its plan step (the TS-006-class evidence), states the margin (large after the first element; the first element with A4 at the worst-case sum) and the A5 branch (a CR option in item 7), and edits no requirement file. `values_proposed` now lists it.
- CK-ANA-B4: Yes; the 0.05 V sweep resolution is checked at 0.01 V (edges within 0.005 V).
- CK-ANA-B5: Yes; independent crossing and shape code within 0.001 ms and 0.04 %, and the loop margin and slope hand checks.
- CK-ANA-C2 to C5: Yes, as iteration 1, with the re-run above.
- CK-ANA-I1, I2: Yes. The plots agree with `result.json`; the 4.6 text disagrees with its plot (finding-10, counted under D2).

Still No: CK-ANA-D2, now on finding-10 (the section 4.6 values differ from the checker output); CK-ANA-A1, H1, H2, H3 (finding-6); A4 (finding-4, finding-12); A5 and G7-2 (finding-12); A6 (finding-7, finding-8); B1 (finding-9, finding-14); B6 and F4 (finding-13); C1 (finding-5); D4 and E4 (finding-11); F2 (finding-8).

### Visual closure (iteration 2)

The reviewer opened all 23 revision 1 result plots with the Read tool:
- `r1-a4-asis` and `r1-a5-asis`: `envelope.png`, `spectrum.png`, `keyup_level.png`;
- `r1-a4-sweep0`, `r1-a5-sweep0`, `r1-a4-sweep1`, `r1-a5-sweep1`: `window.png` (limits REQ-TX-005 +/-10 %, TC-SYS-013 per setting, 5 % and -60 dB; calibrated and compensated budgets shaded; element-1 curves dashed);
- `r1-a4-fix` and `r1-a5-fix`: `corners.png` (the foot step at -0.164 V; red titles on the failing A5 panels and the A4 3 ms 2 W panel), `envelope.png`, `spectrum.png`, `keyup_level.png`, `t1090.png`;
- `r1-summary`: `summary.png`, `windows.png` (the stored-trim bands against the element-1 windows, as section 4.4.3 reads them), `pwm_ripple.png` (A5 61 kHz drawn red, finding-10).

The plotted values agree with `result.json` at the titled points (for example A5 `fix` 3 ms 0.5 W 7.4 V: el.1 +18.0 %, shape 6.7 %; A4 3 ms 2 W: +6.1 %, 5.1 %). The reviewer also opened the eight `window.png` of its own variant runs (`rv2-a4/a5-sweepfine`, `rv2-a4/a5-sweepvos`, `rvs65` and `rvs150` for both finalists): 31 renders in all.

### Commands (iteration 2)

- Freeze: Python loop over `git rev-parse e9f1440:<path>` and `git rev-parse HEAD:<path>` (55 of 55 equal); `cmp` of every run folder's `keying_run.py` and deck copy against the checked-in files; `git log e9f1440..HEAD`; `git merge-base --is-ancestor 7784672 HEAD` (not merged).
- Re-run: `git archive e9f1440 tools hardware/sim/tx-keying hardware/sim/tx-pa/data | tar -x -C <scratchpad>/kr1`; the author's r1 folders moved to `results-author`. Then `/Users/robinonsay/rust/cwht/.venv/bin/python hardware/sim/tx-keying/keying_run.py deck {a4,a5} {asis,sweep0,fix,sweep1}` and `summary` (every exit 0; `a5 sweep1` rerun with `CWHT_LTSPICE_LOCK_WAIT=2400` after a lock-busy exit 5). Comparison script `rv_cmp.py` (bytes; PNG arrays).
- Reviewer variants: `<scratchpad>/kr1/hardware/sim/tx-keying/rv_fine.py {a5,a4} {sweepfine,sweepvos}` and `rv_slope.py {a5,a4} {65,150}`, each through the wrapper (PASS, exit 0); `<scratchpad>/rv_el2.py`, `rv_indep.py` on the author's `.raw`.
- Datasheet: 74LVC1G66 PDF from the web-fetch tool, read with `pdftotext -layout`.
- Record check: `/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/validate_docs.py --quiet`.

### Verdict (iteration 2)

```
ITERATION 2 (2026-09-28, HEAD 65331c6, product commit e9f1440): REVIEWER VERDICT: NEEDS CHANGES; RECORD VERDICT: NEEDS CHANGES
PRODUCT: docs/design/analysis/keying-ts012.md@934ff1f4, hardware/sim/tx-keying/keying_run.py@5b241f55, README.md@c4c7a3f8, 12 decks and runs results/2026-09-28-r1-* at e9f1440
FINDINGS:
- [Major] finding-1 Verified: 0.5, 1, 2, 5 W and 6.4, 7.4, 8.4 V in every keying check; iteration 1 numbers reproduced and now flagged; +7 dB tap and held trim added; loop margin 58.4 degrees minimum (hand check 71.9 degrees tap off, A5 7.9 V); element 2 also passes (reviewer).
- [Major] finding-2 Verified: four-case sourced or labelled threshold budget (every total recomputed); per-unit table for both; temperature as a term; A5 on the digitized curves (recomputed); 0.05 V sweep windows against the budgets, edges within 0.005 V of a 0.01 V reviewer sweep.
- [Major] finding-3 Verified (part a): REQ-TX-005 +/-10 % asserted separately from TC-SYS-013 on elements 3 to 8 and element 1; the iteration 1 cases now FAIL REQ-TX-005 and PASS TC-SYS-013 time as they should. Parts b and c are finding-11.
- [Major] finding-10 (new) Open: section 4.6 quotes revision 0's PWM ripple; revision 1 checker gives A5 -40.6 / -58.1 / -76.1 dBc (slope 59.2 V/V, ratio 2.9), so the 61 kHz option fails by 1.9 dB where the note says marginal pass; the 4.4.3 "44 V/V" is stale. Design rule and TS-012 reading unaffected.
- [Minor] finding-11 (new) Open: checker exits 0 on FAIL; setpoint +/-0.5 dB unsourced and filed under TS-012 criteria.
- [Minor] finding-12 (new) Open: compensated high end +0.101 V not +0.086 V; die maximum and die-to-NTC difference not per the thermal note (A4 29 K); A4 power-on case fails by about 0.007 V.
- [Minor] finding-13 (new) Open: element-1 window sensitivities not stated (offset, pack, sub-threshold slope 65 to 150 dB/V); A4 worst-case pass holds up to about 145 dB/V; comparative reading holds (ratio 1.6 to 1.7).
- [Minor] finding-14 (new) Open: hold droop ignores the named switch's leakage (74LVC1G66 IS(OFF) 0.2 uA max: 45 to 104 V/s on Cf).
- [Minor] finding-4 to finding-9 Open (not addressed in revision 1; finding-4 partly answered, finding-9 iii moot).
ITEMS N/A: CK-ANA-E6, G2 to G5, G6-4 (analysis_kind simulation-deck, timing, worst-case), CK-ANA-J1 to J3 (criticality neither)
VALUES PROPOSED: REQ-TX-005: +/-10 % (keep the TBR value; note section 8 item 8)
MEASUREMENTS: size=8 keying decks, 696 steps re-run; blobs equal HEAD 55/55; re-run 57/57 outputs identical; reviewer variant steps=1212; inputs re-checked=6 (digitized VGG and VDD curves, budget drive terms, thermal note 4.1, pa-drive 4.2, 74LVC1G66 Table 7); renders=31; turns=65; minutes=110 (cumulative 145 and 240); major open=1; minor open=10; iteration=2
```

Iteration 3 is a delta on finding-10 (rule C1). The Minor findings become liens at the first APPROVED reviewer verdict, due at the CDR readiness declaration. The record verdict is also held while the applied analysis template is only on `cr/CR-012` (lead SE convention of 2026-09-27, INSP-083).

## Iteration 3: delta verification of finding-10 (Major) on note revision 2 (2026-09-28, HEAD `f5960d3`)

**Scope (rule C1; the last iteration).** Iteration 3 is a delta. It verifies the fix of finding-10, the only Major open after iteration 2, and re-runs every deck and stage that revision 2 produced. Revision 2 also answered the Minor finding-11 to finding-14, so they are checked here as well. New findings are raised only where revision 2 introduced them or where a defect now decides a reported result. finding-4 to finding-9 were not addressed (note section 10.2 lists finding-10 to finding-14 only); a status line is given below. An open Major after this iteration would go to the owner; none is open.

**Product.** The 66 blobs of front matter `product_files`, committed as `be86c02` (note revision 2, runs `results/2026-09-28-r2-*`, re-freeze under rule C2). Each equals `git rev-parse be86c02:<path>` and `git rev-parse HEAD:<path>` at HEAD `f5960d3` (66 of 66). `git diff be86c02 HEAD -- docs/design/analysis/keying-ts012.md hardware/sim/tx-keying` is empty. The five commits after `be86c02` (`37d5824`, `22e7d74`, `30681fc`, `79795e4`, `f5960d3`) touch TS-012 and other review records only. No product blob is on a `cr/` branch. Checklist as before: `peer-review-checklist-analysis.md` revision A, blob `0386cc6e`, still only on `cr/CR-012-pdr-checklist-templates`.

**Independence (rule C4).** This invocation authored no part of the note or its revisions 1 and 2, the decks, the checker, `expected_states.json`, TS-012, or iterations 1 and 2 of this review. It edited no product file. It changed only this record.

**Search first (charter section 11 rule 1).** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search. Queries: "keying analysis TS-012 INSP-116 iteration 2 findings"; "thermal note inhibit setpoint 81 C A5 77 C A4 junction 110 C sensor adverse +3 C tolerance change 6"; "validate_docs peer review record schema findings_open findings_verified reviewer_verdict iteration checks". After that, `grep` only pinned lines in known files: the note, `keying_run.py`, the README, TS-012 and `thermal-ts012.md`. The rustos tree was not read.

**Sources re-read by the reviewer (2026-09-28).**
- `docs/design/analysis/thermal-ts012.md`: section 4.1, the closed-loop inhibit table (setpoints 80.9 C for A5 and 77.1 C for A4 in the "+3 C, offset and lag at their adverse ends" row; 113.9 C and 117.1 C at 85 C in the same row), and section 8 change 6 (81 C and 77 C).
- Microchip MCP6001/1R/1U/2/4 data sheet DS20001733L (https://ww1.microchip.com/downloads/en/DeviceDoc/MCP6001-1R-1U-2-4-1-MHz-Low-Power-Op-Amp-DS20001733L.pdf), fetched through the web-fetch tool (SHA-256 prefix `4f879ab3`) and read with `pdftotext -layout`. DC electrical characteristics on page 3: IB +/-1.0 pA typical; 19 pA typical at TA +85 C; 1100 pA typical at +125 C.
- The checker's PA tables (`FIN[...]["table"]`, imported from the product `keying_run.py`) and `hardware/sim/tx-pa/data/ra07_pout_vs_vgg_{135,155}.csv`.
- TS-012 revision 5 (`37d5824`): section 4.2 (C5 and C8 rows), section 7.1 keying risk rows, section 7.3 table R5-2 row 9, section 8.4 row E5 (b), and section 8.14 D-10.

**Reproduction (CK-ANA-C4, readiness R2).**
- Export: `git archive be86c02 tools hardware/sim/tx-keying hardware/sim/tx-pa/data` into the scratchpad. The author's 11 `results/2026-09-28-r2-*` folders were moved aside, and the detector runs were kept.
- Runs: `/Users/robinonsay/rust/cwht/.venv/bin/python hardware/sim/tx-keying/keying_run.py deck <fin> <var>` for a4 and a5 with asis, sweep0, fix, sweep1 and sens, then `summary`.
- Wrapper: every deck ran through `tools/ltspice-batch.sh` (blob `88b71475`). All 10 wrapper lines read "result: PASS ... version_line='LTspice 26.0.2 for MacOS' ltspice_exit=0", each with the deck SHA-256 of the author's `wrapper.txt`. That is 6048 LTspice steps (6 + 78 + 180 + 156 + 2604 per finalist). No `.log` contains "warning".
- Exit status: every `deck` stage printed "expected-state check ...: AS EXPECTED" and exited 0. `summary` exited 0 with `design_rule_checks` all true.
- Comparison with the committed outputs: **69 of 69 files agree**. Every `result.json`, `result.csv`, `summary.json`, deck copy and checker copy is byte-identical, and all 27 PNGs are pixel-identical (image arrays equal).

**Negative checks of the exit status (finding-11), on the scratch copy only.**
1. One expected FAIL was removed from `expected_states.json` (`2026-09-28-r2-a5-asis`, `t1090_req_tx005`, run 1). `replot a5 asis` then printed DIFFERS (`unexpected_fail: {t1090_req_tx005: [1]}`) and exited 3.
2. The TC-SYS-013 shape limit was tightened to 0.8 % in the scratch `keying_run.py`. `replot a4 fix --accept` then printed REFUSED (`forbidden_fail: shape` in 17 runs), left `expected_states.json` unchanged, and exited 3. Without `--accept` it printed DIFFERS and exited 3.

Both scratch files were then restored.

### Verification of finding-10 (Major), item by item (rule C7)

| Finding | What the fix asked | Check at `be86c02` | Result |
|---|---|---|---|
| finding-10 | Restate section 4.6 from the checker's `summary.json` (A5 -40.6 / -58.1 / -76.1 dBc) | Section 4.6 now has a table per finalist and PWM rate. The A5 values -40.6 / -58.1 / -76.1 dBc and the A4 values -49.8 / -67.3 / -85.3 dBc equal `summary.json` key `pwm_ripple` (-40.62, -58.15, -76.09; -49.79, -67.32, -85.26). The reference channel reads -68 / -86 dBc against -67.99 / -85.78. Reviewer hand recomputation with the checker's A5 table: loaded 2-section RC ladder \|H\| = 1 / \|1 - x^2 + j3x\| with x = 2 pi f 47 us gives 0.00305 at 61 kHz; the VGG node pole (17.7 us) gives 0.1458. Then (2/pi) 3.3 V x 0.00305 x 0.1458 x 59.24 / (2 x 22.36 V) = -58.15 dBc. The margins in the table (19.4 and 1.9 dB over; 16.1 and 25.3 dB margin) are the limit minus the value | Yes |
| finding-10 | Say that 61 kHz fails for A5 | Stated in the summary ("PWM rule"), section 4.6 ("61 kHz ... FAIL by 1.9 dB"; "Revision 1 called ... 'marginal' ... it fails") and section 5.2 item 1. The design rule is unchanged: 122 kHz or a third pole, recorded in TS-012 D-10 | Yes |
| finding-10 | Correct the stale 44 V/V and "2.1 times" | Section 4.4.3 bullet: "59.2 V ... against 20.6 V/V for A4 (ratio 2.9)". The bullet now explains why the window ratio (1.6 to 1.8) is smaller than the slope ratio: the error is set at the foot, where the two transfers differ less. Section 4.2 item 2 now reads "about three times as steep". `grep` finds no "44 V/V" outside the revision notes, no "2.1 times", "twice", "halves" or "about half" in the note body, and no "-60.7" except in the revision 1 correction sentence. The superseded README rows keep their historical values under "(revision 0, superseded)" and "(revision 1, superseded)" | Yes |
| finding-10 | Correct the README row | The `2026-09-28-r1-summary` row carries a correction that names finding-10 and the correct values. The new `2026-09-28-r2-summary` row states A5 -40.6 / -58.1 (61 kHz FAIL by 1.9 dB) / -76.1 dBc and A4 -49.8 / -67.3 / -85.3 dBc | Yes |
| finding-10 | Plot and text agree (CK-ANA-D2, I2) | `r2-summary/pwm_ripple.png` prints every value with its margin or excess, draws A5 61 kHz and both 30.5 kHz feedforward bars red, and titles the slopes "A5 59.2 V/V, A4 20.6 V/V (ratio 2.9)". This matches the note. The `summary` stage now asserts the 122 kHz rule (`pwm_122k_feedforward_passes: true`; the reviewer's re-run gives the same) | Yes |
| finding-10 | (reviewer check of the new value) | The 59.24 V/V is the steepest single 0.02 V segment of the digitized A5 mean curve (2.54 to 2.56 V). Over 0.04 to 0.10 V spans the steepest slope is 52.1 to 56.8 V/V. At every span 61 kHz still fails for A5 (by 0.7 to 1.9 dB) and 122 kHz still passes (16.1 to 17.3 dB). The stated precision is finding-15 (Minor, new). It changes no verdict and no design rule | Yes (finding-15 raised) |

**Result: finding-10 Verified.**

### Verification of the Minor findings answered in revision 2 (finding-11 to finding-14)

| Finding | Case the finding named | Check at `be86c02` | Result |
|---|---|---|---|
| finding-11 | (b) A non-zero exit on an unexpected FAIL, or a `--check` mode with the expected states | `check_expected()` compares every FAIL state (criterion and run) with `expected_states.json` (every r2 run id, with a reason). It exits 3 on DIFFERS, NO EXPECTED STATES or REFUSED, and 2 on a wrapper error. `FORBIDDEN_FAIL` makes `--accept` refuse any element-3-to-8 criterion, VGG or setpoint FAIL in `fix` and `sweep1`. `summary` exits 3 on a design-rule failure. The reviewer's two negative checks (above) gave exit 3, and every stage of the re-run exited 0 | Yes |
| finding-11 | (c) Source or relabel the `setpoint` criterion | Section 1 gives it its own row, "Model-health check of this analysis (not a requirement ...)", and says REQ-SYS-012 is not assessed here. The 4.4.2 table labels it "(this analysis's own check)". It is no longer under the TS-012 row | Yes |
| finding-12 | (i) Residual on both sides; (ii) die maximum and die-to-NTC difference per finalist from the thermal note | `_comp_term()` takes +/-0.6 mV/C over max(T_NTC_MAX - 25, 35) K on both sides. `T_NTC_MAX` is 81 C (A5) and 77 C (A4), from thermal note section 8 change 6 and the section 4.1 inhibit table (80.9 C and 77.1 C). `DIE_TO_NTC_K` is 29 K and 33 K. Reviewer recomputation of every total: A4 compensated -0.1787 / +0.0962 V (RSS -0.124 / +0.058); A5 compensated -0.1711 / +0.0986 V (RSS -0.117 / +0.060); A4 stored -0.1072 / +0.1897 V (RSS -0.070 / +0.108); A5 stored -0.1096 / +0.1821 V (RSS -0.071 / +0.102). All equal section 3.2, the `fix` corners and `summary.json`. The 85 C comparison (113.9 C and 117.1 C) is the "+3 C, offset and lag adverse" row of the same table, as the note says. Observation (no finding): the pairing takes the setpoint itself as the highest reading. With the +3 C trip tolerance the reading at the trip can be 3 K higher. The die-above-reading term is then 3 K smaller (-7.5 mV) and the residual span 3 K larger (+1.8 mV), so the budget as written is conservative by about 6 mV on the stored-trim high end | Yes |
| finding-13 | Quantify the element-1 window sensitivity (offset, packs, sub-threshold slope) and state the A4 slope limit; the interpolation across the step | New `sens` variant: 0.02 V, 7 cases, 2604 runs per finalist, reproduced 69/69 above. At 100 dB/V the `sens` nominal case equals `sweep1` at the 84 shared points per finalist. The reviewer's own comparison of `first_err_pct` and `first_shape_err` gives a maximum difference of 2e-7 %. The iteration 2 reviewer's 0.01 V edges are reproduced within 0.002 V (for example A4 65 dB/V -0.163 / +0.267 against -0.162 / +0.269; A5 offset -0.080 / +0.132, identical). Margins recomputed from `summary.json` `element1_window_margins_v`: A4 stored worst-case sum +0.0213 V (+0.0149 with the offset; +0.0103 on the grid edges; -0.018 at 150 dB/V). The slope limit 100 + 50 x 0.0213 / 0.0395 = 127 dB/V is linear, as stated. A5 stored worst-case sum -0.045 V (-0.033 to -0.064 V across cases); A4 compensated worst-case sum -0.0095 V. The reviewer read the first failing 0.02 V grid point per criterion, at 2 W, for every case and setting of both `sens` results. The step-like jump in the element-1 time error lies at or beyond the shape edge in every case. In one case they coincide: A4, 3 ms, VOS +1 mV, where both criteria first fail at -0.18 V. There the edge is uncertain by less than one 0.02 V step, on A4's low side, where the stored-trim margin is 0.055 V. The conservative grid edges, which the note also reports, reverse no verdict | Yes |
| finding-14 | Bound the droop with the named parts, or make the per-element capture the basis | Item 9 makes the per-element ADC capture, with the integrator reset while parked, the design basis. The 74LVC1G66 figures are as iteration 2 read them. Reviewer check of the MCP6002 figures against DS20001733L: 19 pA / 4.48 nF = 4.2 mV/s and 19 pA / 1.92 nF = 9.9 mV/s, times KTRIM 0.16 = 0.7 to 1.6 mV/s of VGG ("under 2 mV/s"). Reset-switch leakage as an offset: 0.2 uA x 10 k = 2 mV, taken into the zero calibration, and its bound left to WP-PDR-22 (section 8 item 1). Editorial: the note cites "page 2" of DS20001733L; the IB rows are on page 3 (no finding; correct it at the next revision) | Yes |

**Result: finding-11, finding-12, finding-13 and finding-14 Verified.**

### Minor findings not addressed in revision 2 (status only)

finding-4 to finding-9 are unchanged since iteration 2 and stay Open Minor (see the iteration 2 status lines). The note's section 10 does not list them. They become liens with this APPROVED reviewer verdict.

### New findings (iteration 3)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-15"></a>finding-15 | reviewer | Minor | CK-ANA-A4, D3 | note sections 4.6 ("A5 59.2 V/V ... 2.9 times"; the 61 kHz row "FAIL by 1.9 dB"), 4.4.3 bullet ("ratio 2.9"), 4.2 item 2, summary "PWM rule"; `keying_run.py` `pwm_ripple()` (`np.max(np.diff(amp) / np.diff(vg))`); `pwm_ripple.png` title | **The A5 slope and the 61 kHz excess are quoted from one 0.02 V segment of a digitized curve, at a precision the input does not carry, and against an A4 slope taken over 0.1 V.** The 59.24 V/V is the single segment 2.54 to 2.56 V of the digitized mean curve (1.3415 to 1.6225 W); its neighbours are 31.0 and 52.9 V/V. Over 0.04, 0.06 and 0.10 V spans the steepest A5 slope is 56.1, 56.8 and 52.1 V/V. A4's 20.6 V/V is one 0.1 V segment (1.3 to 1.4 V) of its hand-read table. So the A5 61 kHz sideband is -58.1 to -59.3 dBc (excess 0.7 to 1.9 dB), the 122 kHz margin 16.1 to 17.3 dB, and the like-for-like slope ratio 2.5 to 2.9. The verdicts hold at every span: 61 kHz fails for A5, and the 122 kHz rule passes with more than 16 dB. The single-segment value is the conservative end for the ripple bound, and the loop-margin check takes the same steepest point, also conservatively. No TS-012 figure moves. **Fix:** state the slope with its reading span (52 to 59 V/V) and the 61 kHz A5 excess as 0.7 to 1.9 dB (or take the slope over a stated span, for example 0.1 V, for both finalists); state the ratio as about 2.5 to 2.9 | Open | Pending | |

### Per-case results (iteration 3; the cases revision 2 changed, one row per case)

Values are the checker's (estimates where the inputs are), from the committed `result.json` and `summary.json`, which the reviewer's re-run reproduced byte for byte. Rows C-1 to C-4, C-6, C-7, C-12 and C-15 to C-17 of iteration 2 are unchanged (their decks and outputs are identical to r1), except that C-17 now takes the per-finalist die figures (finding-12).

| Case | Condition | Governing id and limit | Result (checker output) | Margin with sign | Uncertainty | Reviewer re-check | Finding ids |
|---|---|---|---|---|---|---|---|
| C-5 | Revision 1 design, elements 3 to 8, 0.5 / 1 / 2 / 5 W, 6.4 / 7.4 / 8.4 V, 3 / 5 / 8 ms, 5 record corners (180 runs) | REQ-TX-005 10 %; TC-SYS-013 0.5 ms and 5 % | worst error 2.2 % (A4), 1.9 % (A5); shape 0.9 %: PASS | +7.8 % / +8.1 %; +4.1 % | per-element capture error (+/-0.01 V) | re-run identical | none |
| C-8 | Same, every step | REQ-TX-006: -60 dB | A4 -69.1 dB, A5 -69.2 dB | +9.1 / +9.2 dB | small | re-run identical | none |
| C-9 | Element 1, stored-trim worst-case sum (A4 -0.107 / +0.190 V, A5 -0.110 / +0.182 V), worst step, 0.02 V `sens` windows; and the 72 `fix` corner runs per finalist | REQ-TX-005, TC-SYS-013 | A4 window -0.169 / +0.211 V: PASS, 72 of 72 corner runs pass; A5 -0.085 / +0.137 V: FAIL, 17 of 72 corner runs fail | A4 +0.021 V (+0.015 with the offset, +0.010 on grid edges); A5 -0.045 V | slope (A4 fails above about 127 dB/V: -0.018 V at 150); offset; packs within 0.003 V | margins recomputed; `sens` and `fix` re-run identical | finding-13 (Verified) |
| C-10 | Element 1, stored-trim RSS (A4 -0.070 / +0.108, A5 -0.071 / +0.102 V) | same | A4 PASS; A5 PASS (FAIL at 150 dB/V) | A4 +0.100 V; A5 +0.013 V (+0.009 with the offset; -0.008 at 150 dB/V) | as C-9 | recomputed | none |
| C-11 | Element 1 after power-on without a stored trim, compensated worst-case sum (A4 -0.179 / +0.096, A5 -0.171 / +0.099 V) | same | A4 FAIL (5 of 36 corner runs: 3 ms, 0.5 W at 6.4 and 7.4 V, 2 W at 6.4, 7.4 and 8.4 V); A5 FAIL (18 of 36) | A4 -0.009 V; A5 -0.087 V | as C-9 | runs 37, 43, 49, 55, 67 read from `result.csv` | none (stored trim required for both: TS-012 D-10) |
| C-13 | Overshoot; VGG maximum (A5) | TS-012: 0.2 dB; 3.5 V | 0.00 dB; A5 3.24 V (stored-trim high corner); A4 2.60 V | +0.2 dB; +0.26 V | small | re-run identical | none |
| C-14 | PWM carrier ripple, feedforward, A5 | REQ-TX-006: -60 dB | 30.5 kHz -40.6 dBc, 61 kHz -58.1 dBc, 122 kHz -76.1 dBc (checker and note agree) | 122 kHz +16.1 dB; 61 kHz -1.9 dB (-0.7 to -1.9 dB by slope span) | analytic bound; digitized slope | hand recomputation -58.15 dBc | finding-10 (Verified), finding-15 |

### Findings (iteration 3; current state of every finding of this record)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| finding-1 | reviewer | Major | CK-ANA-F1, E3, A5 | note sections 1, 2, 4.3, 4.4, 5.1 | See iteration 1 and the iteration 2 verification table | Verified (iteration 2, revision 1 at e9f1440) | n/a | |
| finding-2 | reviewer | Major | CK-ANA-A4, A5, B6, E3, F4, G7-2 | note sections 3.1, 3.2, 4.3, 4.4.3, 5.1 | See iteration 1 and the iteration 2 verification table | Verified (iteration 2) | n/a | |
| finding-3 | reviewer | Major | CK-ANA-E4, D4, D2 | `keying_run.py` `REQ`, `analyse()` | Part (a); parts (b) and (c) were finding-11 | Verified (iteration 2, part a) | n/a | |
| finding-4 | reviewer | Minor | CK-ANA-A4, A3 | note section 3.1, `A4_W` | See iteration 1; the A5 part answered in revision 1 | Open (lien) | Pending | |
| finding-5 | reviewer | Minor | CK-ANA-C1 | note header "Tool" row | See iteration 1; no library versions given | Open (lien) | Pending | |
| finding-6 | reviewer | Minor | CK-ANA-A1, H1, H2, H3 | note header, sections 5.1 and 8 | See iteration 1 | Open (lien) | Pending | |
| finding-7 | reviewer | Minor | CK-ANA-B3, A6 | note limitation 13 | See iteration 1 | Open (lien) | Pending | |
| finding-8 | reviewer | Minor | CK-ANA-A6, F2 | note header | See iteration 1 | Open (lien) | Pending | |
| finding-9 | reviewer | Minor | CK-ANA-B1, D2 | `det_char.cir`; note section 4.6 | See iteration 1; item (iii) moot. Item (ii) persists: section 4.6 still gives the 30.5 kHz FAIL on the analytic bound | Open (lien) | Pending | |
| finding-10 | reviewer | Major | CK-ANA-D2, E1 | note sections 4.6 and 4.4.3; README | Section 4.6 restated from the checker; 61 kHz fails for A5; 44 V/V corrected; README and plot agree | Verified (iteration 3, revision 2 at be86c02) | n/a | |
| finding-11 | reviewer | Minor | CK-ANA-E4, D4 | `keying_run.py` `check_expected()`, `FORBIDDEN_FAIL`, `REQ["setpoint_db"]`; note section 1 | Exit 3 on unexpected states (negative checks by the reviewer); setpoint relabelled | Verified (iteration 3) | n/a | |
| finding-12 | reviewer | Minor | CK-ANA-A4, A5, G7-2 | `THRESHOLD_BUDGET`, `T_NTC_MAX`, `DIE_TO_NTC_K`; note section 3.2 | Residual on both sides; per-finalist die figures from the thermal note; totals recomputed | Verified (iteration 3) | n/a | |
| finding-13 | reviewer | Minor | CK-ANA-B6, F4 | note sections 2, 4.4.2, 4.4.3, 5.1, limitations 3 and 11 | `sens` variant; sensitivities, grid edges and the 127 dB/V limit stated; reproduced | Verified (iteration 3) | n/a | |
| finding-14 | reviewer | Minor | CK-ANA-B1 | note section 5.2 items 2 and 9, limitation 7 | Per-element capture is the basis; switch and op-amp leakage bounded from their datasheets | Verified (iteration 3) | n/a | |
| finding-15 | reviewer | Minor | CK-ANA-A4, D3 | note sections 4.6, 4.4.3, 4.2, summary; `pwm_ripple()` | A5 slope and 61 kHz excess from one 0.02 V digitized segment; state the range | Open (lien) | Pending | |

### Effect on TS-012 revision 5 (A4 against A5)

TS-012 revision 5 (`37d5824`) already quotes the revision 2 keying figures. The re-run reproduces every one of them: in section 1 item 6, table R5-2 row 9, the section 7.1 keying risk rows, section 8.10 (REQ-SYS-014/015 row) and section 8.14 D-10. The figures are: A4 first element PASS at the worst-case sum by 0.015 to 0.021 V, failing above about 127 dB/V and by 0.009 V without a stored trim; A5 first element FAIL by 0.045 V (17 of 72 corner runs) and PASS at RSS; window ratio 1.6 to 1.8; the 122 kHz rule.
- **C5** (section 4.2): C5-A4 = 2 and C5-A5 = 4 rest on the PA drive, low-pack power, harmonic and receiver evidence. Their cell texts cite no keying number. Table R5-4 carries keying F9 "in C5-A5", and F9's statement (the A5 window 1.6 to 1.8 times narrower) is unchanged. No C5 cell moves.
- **C8** (section 4.2): C8-A4 = 2 and C8-A5 = 1 come from the thermal record. The keying note only consumes thermal figures (the inhibit setpoints and the die-above-reading differences) and feeds nothing back. No C8 cell moves.
- **Row E5** (section 8.4, part b, keying-loop items USD 0.20 to 1.35): revision 2 replaces the analog hold by a per-element ADC capture with the integrator reset while parked. It still uses one 74LVC1G66-class switch (now the reset switch) and one ADC channel. The 2N7002 tap switch, a third MCP6002 and a ninth 1N5711W are unchanged. The E5 range and the A4 and A5 roll-ups do not change.
- finding-15 changes only the size of the A5 61 kHz excess (0.7 to 1.9 dB). TS-012 uses only the 122 kHz rule (D-10), which holds by at least 16 dB. **Nothing that TS-012 revision 5 relies on for A4 against A5 changes.** Table R5-1's keying row ("iteration 3 not yet run") and the X-R5-3 and section 10 revisit condition can now cite this iteration.

### Cross items (iteration 3, returned to Claude as lead SE)

- X-8. **TS-012 table R5-1.** Update the keying row to "INSP-116 iteration 3 (this record): reviewer APPROVED; finding-10 Verified; Minor liens finding-4 to 9 and finding-15; record verdict held for the CR-012 template". The section 10 revisit condition "a re-review of the ... keying ... record changes a figure this study scores on" did not trigger.
- X-5 and X-6 (iteration 2) are answered in the note: the stored trim is required for both finalists (TS-012 D-10 carries it), and the per-element capture replaces the analog hold. The WP-PDR-22 circuit still needs the reset switch's leakage bound at the REQ-SYS-114 hot end (note section 8 item 1).
- X-7 (iteration 2) is answered in part: the checker now has an exit status tied to expected states, which TC-TX-005 automation can use. Iteration 1 X-2 (the TC-TX-006 614 Hz known answer; finding-7) is still open.

### Checklist items changed at iteration 3

Now Yes:
- CK-ANA-A5 and CK-ANA-G7-2: finding-12 Verified.
- CK-ANA-B6 and CK-ANA-F4: finding-13 Verified.
- CK-ANA-D4 and CK-ANA-E4: finding-11 Verified.
- CK-ANA-I1 and CK-ANA-I2: Yes. The 15 changed or new plots were opened, and their text agrees with the note.

Now No: CK-ANA-D3 (finding-15).

Still No: CK-ANA-D2 (finding-9 item ii; finding-10's part is Verified); CK-ANA-A1, H1, H2, H3 (finding-6); A4 (finding-4, finding-15); A6 (finding-7, finding-8); B1 (finding-9); B3 (finding-7); C1 (finding-5); F2 (finding-8).

### Visual closure (iteration 3)

The reviewer compared every r2 PNG with its r1 counterpart (image arrays).
- **Pixel-identical to r1 (12):** the six `asis` plots, and `envelope.png`, `spectrum.png` and `keyup_level.png` of both `fix` runs (they plot the nominal corner only). Iteration 2 opened these.
- **Changed or new (15), each opened with the Read tool:** `r2-a4-fix` and `r2-a5-fix` `corners.png` and `t1090.png`; `r2-a4-sens` and `r2-a5-sens` `sens_curves.png` and `sens_windows.png`; the four `window.png` of `r2-a4/a5-sweep0` and `r2-a4/a5-sweep1`; and `r2-summary` `pwm_ripple.png`, `summary.png` and `windows.png`.

The plotted values agree with `result.json` and `summary.json` at the marked points. Examples:
- A5 `fix`, 3 ms, 2 W, stored-trim high: -13.2 %, shape 6.2 % FAIL. A4 `fix`, 3 ms, 2 W, compensated low: +16.8 %, shape 5.5 % FAIL.
- `windows.png` shows the A4 stored band -0.107 / +0.190 inside the nominal A4 window -0.169 / +0.211, and the A5 stored band -0.110 / +0.182 outside the A5 window -0.085 / +0.137.
- `pwm_ripple.png` shows A5 61 kHz -58.1 dBc, "over by 1.9 dB".

Every plot draws its limits (REQ-TX-005 +/-10 %, TC-SYS-013, 5 %, -60 dB) and the budget bands.

### Commands (iteration 3)

- Freeze: shell loop over `git rev-parse be86c02:<path>` and `git rev-parse HEAD:<path>` for the 66 product files (66 of 66 equal); `git diff be86c02 HEAD -- docs/design/analysis/keying-ts012.md hardware/sim/tx-keying` (empty); `git show --stat be86c02`; `git diff e9f1440 be86c02 -- docs/design/analysis/keying-ts012.md`.
- Re-run: `git archive be86c02 tools hardware/sim/tx-keying hardware/sim/tx-pa/data | tar -x -C <scratchpad>/kr2`; the author's r2 folders moved aside. With `CWHT_LTSPICE_LOCK_WAIT=3600`: `/Users/robinonsay/rust/cwht/.venv/bin/python hardware/sim/tx-keying/keying_run.py deck {a4,a5} {asis,sweep0,fix,sweep1,sens}`, then `summary` (every exit 0). Comparison script `kr2_cmp.py` (bytes; PNG arrays): 69 of 69.
- Negative checks: the edited `expected_states.json`, then `replot a5 asis` (exit 3); `shape_tol` 0.008 in the scratch checker, then `replot a4 fix --accept` (REFUSED, exit 3) and `replot a4 fix` (DIFFERS, exit 3); scratch files restored.
- Reviewer scripts, inline Python in the venv: the PWM sideband hand recomputation; A5 slope over 0.02 to 0.10 V spans from the checker's table; the `sens` nominal against `sweep1` at the 84 shared points; the budget totals; the r2 against r1 PNG identity.
- Data sheet: MCP6001/2/4 DS20001733L through the web-fetch tool, `pdftotext -layout` pages 1 to 4.
- Record check: `/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/validate_docs.py`.

### Verdict (iteration 3)

```
ITERATION 3 (2026-09-28, HEAD f5960d3, product commit be86c02): REVIEWER VERDICT: APPROVED; RECORD VERDICT: NEEDS CHANGES (held: applied analysis template only on cr/CR-012)
PRODUCT: docs/design/analysis/keying-ts012.md@5121cc90, hardware/sim/tx-keying/keying_run.py@5db0ef28, README.md@0dae6167, expected_states.json@230a13c3, 14 decks and runs results/2026-09-28-r2-* at be86c02
FINDINGS:
- [Major] finding-10 Verified: section 4.6 restated from the checker (A5 -40.6 / -58.1 / -76.1 dBc, A4 -49.8 / -67.3 / -85.3 dBc; hand recomputation -58.15 dBc); 61 kHz fails for A5; 59.2 against 20.6 V/V; README and pwm_ripple.png agree; the summary stage asserts the 122 kHz rule.
- [Major] finding-1, finding-2, finding-3 Verified (iteration 2).
- [Minor] finding-11 Verified: exit 3 on unexpected FAIL states (two reviewer negative checks); setpoint relabelled as a model-health check.
- [Minor] finding-12 Verified: residual on both sides; 29 K / 33 K and 81 C / 77 C from the thermal note; every total recomputed.
- [Minor] finding-13 Verified: sens variant (2604 runs per finalist) reproduced; A4 stored-trim pass +0.021 V (+0.015 with offset), limit about 127 dB/V; A5 fails at every case.
- [Minor] finding-14 Verified: per-element capture is the basis; leakage bounded from the 74LVC1G66 and MCP6002 data sheets (page cite to correct: page 3).
- [Minor] finding-15 (new) Open: A5 slope 59.2 V/V is one 0.02 V digitized segment (52 to 57 V/V over 0.04 to 0.10 V); state the 61 kHz A5 excess as 0.7 to 1.9 dB and the ratio as 2.5 to 2.9. No verdict or TS-012 figure moves.
- [Minor] finding-4 to finding-9 Open (not addressed).
ITEMS N/A: CK-ANA-E6, G2 to G5, G6-4 (analysis_kind simulation-deck, timing, worst-case), CK-ANA-J1 to J3 (criticality neither)
VALUES PROPOSED: REQ-TX-005: +/-10 % (keep the TBR value; note section 8 item 8)
TS-012 EFFECT: none. C5 (A4 2, A5 4), C8 (A4 2, A5 1) and row E5 (b) (USD 0.20 to 1.35) unchanged; A4 315 against A5 270 stands.
MEASUREMENTS: size=10 keying decks, 6048 steps re-run; blobs equal HEAD 66/66; re-run 69/69 outputs identical; negative checks=2 (exit 3 each); inputs re-checked=5 (thermal 4.1 inhibit table and 8 change 6, MCP6002 DS20001733L IB, budget totals, A5 digitized slope, PWM filter and VGG pole); renders=15; turns=60; minutes=120 (cumulative 205 and 360); major open=0; minor open=7; iteration=3
```

finding-4 to finding-9 and finding-15 are Minor liens (rule C1), owned by the analysis author and due at the CDR readiness declaration. No Major is open after the last iteration, so nothing goes to the owner. The record verdict becomes APPROVED when the analysis template of CR-012 merges (lead SE convention of 2026-09-27, INSP-083).
