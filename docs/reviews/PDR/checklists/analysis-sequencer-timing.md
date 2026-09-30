---
# Peer-review record front matter (charter section 5; docs/process/01-lifecycle-and-reviews.md section 13;
# docs/process/08-agent-briefing.md sections 3.4 and 3.5). Independent review of the WP-PDR-23a sequencer
# timing analysis at the record path PDR work plan WP-PDR-23 "Records" names (analysis-sequencer-timing.md).
# Iteration 1 at freeze F0 (rule C2), commit 95adefc. Iteration 2 (delta on the Major fixes, rule C1) at the
# revision 1 freeze: commit 8ca7d05 plus fb120d2 (fb120d2 adds the r1-s4 run-folder copy of the timing diagram
# that 8ca7d05 left out; both on main). Iteration 3 (delta on the iteration 2 Major findings 13 and 14, rule C1) at
# the revision 2 freeze, commit 249356b (on main); the third and last author-review iteration before escalation.
# Checklist applied: docs/templates/peer-review-checklist-analysis.md revision A as on its CR-012 branch
# (cr/CR-012-pdr-checklist-templates, blob 0386cc6e; CR-012 Submitted, not merged).
# tools/validate_docs.py requires the checklist field to name a template that exists on main, so the field
# names peer-review-checklist-design revision B (the INSP-071 form) and checklist_analysis records the
# template actually applied; the delta after CR-012 merges switches the field.
# id: INSP-122, the id the paired assurance record INSP-123 (iteration 1, its cross item X-2) left free for this
# record. No record on main or on a cr/ branch uses it at HEAD c0c3205 (highest in use INSP-133), nor at HEAD 249356b
# (iteration 3 check; highest in use INSP-135). The lead SE
# confirms it when filing, since other invocations commit on main.
# The software assurance pair (SW-TXSEQ is safety-critical, plan WP-PDR-23 "reviewer plus SA") is a separate
# invocation with its own record, INSP-123, docs/reviews/PDR/checklists/analysis-sequencer-timing-software-assurance.md.
id: INSP-122
checklist: peer-review-checklist-design
checklist_revision: B
checklist_analysis: "docs/templates/peer-review-checklist-analysis.md@0386cc6e78da65578b1cce8b2f793cd3db224921 (revision A, CR-012 branch)"
checklist_file: docs/reviews/PDR/checklists/analysis-sequencer-timing.md
product: docs/design/analysis/sequencer-timing.md
# product_commit (iteration 3): 249356b, the WP-PDR-23a revision 2 commit that fixes the iteration 2 Major findings
# (re-freeze F0, rule C2). The 23 blobs below equal git rev-parse 249356b:<path>, HEAD:<path> and git hash-object at
# HEAD 249356b. product_files_iteration_2 keeps the fb120d2 blobs; product_files_iteration_1 keeps the 95adefc blobs.
product_commit: "249356bab72557ebfd4307aa7e329d213f85f268"
product_files: ["docs/design/analysis/sequencer-timing.md@b6a5e31af5390f0606d038ca87c2e240536c6ef5", "hardware/sim/tx-seq/seq_run.py@d28ab4a171a7a6e5232d0273bd7213d0cd9e9b01", "hardware/sim/tx-seq/relay_model.py@0285c9c923925f331508a9ad8dcd73355b57fda1", "hardware/sim/tx-seq/expected_states.json@b45bc1b5543943991cfc2ba0b6089fdf8a65b304", "hardware/sim/tx-seq/README.md@71e0d9d9d2ccc681b0b54fd2ff4a0d3c313cb6b8", "hardware/sim/tx-seq/results/2026-09-29-r2-s1-drive/drive_dc.cir@4cfb57f6e43d24a0f4a9caed6ab3f58d54b7a5ed", "hardware/sim/tx-seq/results/2026-09-29-r2-s2-coil/coil_tran.cir@abb7f57363d1ecd1c2fb92fea97873bb01de4a87", "hardware/sim/tx-seq/results/2026-09-29-r2-s2-coil/raw.sha256@ba9a0a1221194a5d6631e936ad07a0c8f3e483ce", "hardware/sim/tx-seq/results/2026-09-29-r2-s4-sequence/icd-tx-sw-timing-table.csv@71d6a4f7f35aed8b3c08e4669c0bc49f681d6044", "hardware/sim/tx-seq/results/2026-09-29-r2-s3-operate/result.json@9323eeed4798615a97e3888aeee949193a3ead5a", "hardware/sim/tx-seq/results/2026-09-29-r2-s4-sequence/result.json@03815632163917f2e6d1e363c379fad575a65ed0", "docs/reviews/PDR/figures/timing-diagram.png@49db873d7a3940ede1135f4be449c6338a444e01", "hardware/sim/tx-seq/results/2026-09-29-r2-s1-drive/s1-coil-current.png@b35f96225844832ac7d591e0b524def31c34a71e", "hardware/sim/tx-seq/results/2026-09-29-r2-s1-drive/s1-coil-voltage-vs-pack.png@6b2906ff52213110639196f6349f2b11fa261b58", "hardware/sim/tx-seq/results/2026-09-29-r2-s2-coil/s2-coil-transient.png@1fd5832159e7e13c642ebb1b371039010e316637", "hardware/sim/tx-seq/results/2026-09-29-r2-s3-operate/s3-operate-vs-coil-temperature.png@6262e1c0e4eb9f7951abfea052bdf319a6e1fdbd", "hardware/sim/tx-seq/results/2026-09-29-r2-s3-operate/s3-release.png@0e445bec986f4815ca9432be9fcb650dc2752213", "hardware/sim/tx-seq/results/2026-09-29-r2-s3-operate/s3-limiter-setpoint.png@bbfc5327aaae6af2aeabe77492f18f8fb7cc4fcf", "hardware/sim/tx-seq/results/2026-09-29-r2-s3-operate/s3-keydown-hold.png@ca5db560cb30ce050552fd829921d19d23e179ad", "hardware/sim/tx-seq/results/2026-09-29-r2-s4-sequence/timing-diagram.png@49db873d7a3940ede1135f4be449c6338a444e01", "hardware/sim/tx-seq/results/2026-09-29-r2-s4-sequence/s4-keydown-budget.png@17aa3f0289530be7532f5aad676460a5b3cdf5a8", "hardware/sim/tx-seq/results/2026-09-29-r2-s4-sequence/s4-margins.png@d7c2c8c5aa1cbe2c8545f104faede3b4065c8912", "hardware/sim/tx-seq/results/2026-09-29-r2-s4-sequence/s4-stale-ratio.png@3ea0ceeabd4c4b0c2415a65a9506b636fe035ef5"]
product_commit_iteration_2: "fb120d298a96de0e838e16d0cb5bad4f254f90bf"
product_files_iteration_2: ["docs/design/analysis/sequencer-timing.md@e4c9ad923beb817238c1ae4ef69dd1f59bc7f5d2", "hardware/sim/tx-seq/seq_run.py@fbcad58599374c6520b47c71d87a6a10dfa3eee5", "hardware/sim/tx-seq/relay_model.py@0285c9c923925f331508a9ad8dcd73355b57fda1", "hardware/sim/tx-seq/expected_states.json@2b730325c35565815d5d8e38d24e2fd5bceba6b3", "hardware/sim/tx-seq/README.md@f29da6c8d0de3b95d5b6f1e4e493503b6d6970fe", "hardware/sim/tx-seq/results/2026-09-29-r1-s1-drive/drive_dc.cir@c24febb0f34cab90d1da0639b7384bdeb6044241", "hardware/sim/tx-seq/results/2026-09-29-r1-s2-coil/coil_tran.cir@5eb43929ade8f8cac94d9de70efc0a100b9c323b", "hardware/sim/tx-seq/results/2026-09-29-r1-s2-coil/raw.sha256@2044ef9237463cbdc8b598360c725987e0075106", "hardware/sim/tx-seq/results/2026-09-29-r1-s4-sequence/icd-tx-sw-timing-table.csv@936573220dd92fd8ba8f281bdc5cb1326d045215", "hardware/sim/tx-seq/results/2026-09-29-r1-s4-sequence/result.json@34758ff9d57136b00850abc6970c5348898f1d7c", "docs/reviews/PDR/figures/timing-diagram.png@2b0f7678d55578a5bac51c3b1a5b576041e1b98e", "hardware/sim/tx-seq/results/2026-09-29-r1-s1-drive/s1-coil-current.png@b35f96225844832ac7d591e0b524def31c34a71e", "hardware/sim/tx-seq/results/2026-09-29-r1-s1-drive/s1-coil-voltage-vs-pack.png@5716d91a828b34b65e87288915f7ef12d48428e0", "hardware/sim/tx-seq/results/2026-09-29-r1-s2-coil/s2-coil-transient.png@2335644aabba931b96c02e65a53dc0c11c0100b9", "hardware/sim/tx-seq/results/2026-09-29-r1-s3-operate/s3-operate-vs-coil-temperature.png@77bc91cae52b144492874e0714dcc7baa24805c0", "hardware/sim/tx-seq/results/2026-09-29-r1-s3-operate/s3-release.png@1a89371bc0ed62f672d51ab8470fb6ef7d1cd57d", "hardware/sim/tx-seq/results/2026-09-29-r1-s3-operate/s3-limiter-setpoint.png@48855f68db4ee8508c28887e3bc31de6a1972e58", "hardware/sim/tx-seq/results/2026-09-29-r1-s4-sequence/timing-diagram.png@2b0f7678d55578a5bac51c3b1a5b576041e1b98e", "hardware/sim/tx-seq/results/2026-09-29-r1-s4-sequence/s4-keydown-budget.png@17aa3f0289530be7532f5aad676460a5b3cdf5a8", "hardware/sim/tx-seq/results/2026-09-29-r1-s4-sequence/s4-margins.png@d7c2c8c5aa1cbe2c8545f104faede3b4065c8912", "hardware/sim/tx-seq/results/2026-09-29-r1-s4-sequence/s4-stale-ratio.png@d1e990e79cd260ce671ab879e7a40a5d2a08723c"]
product_files_iteration_1: ["docs/design/analysis/sequencer-timing.md@8a628de6783ab811a78b6643da2f8288a5a4d331", "hardware/sim/tx-seq/seq_run.py@8de9e1c21919cecb43131fece12dcc90803f5abf", "hardware/sim/tx-seq/relay_model.py@1140d549bac1a393149a14cb3b4e1a7c518e41dc", "hardware/sim/tx-seq/expected_states.json@3610deb45bdbd03f81a8d5c16b62299aea9ca948", "hardware/sim/tx-seq/README.md@df16e5d8b2ed09c99df71ccb5b762bd737414d2f", "hardware/sim/tx-seq/results/2026-09-29-s1-drive/drive_dc.cir@d3c434c86785e3031bd182b66fdb77b5fc340d10", "hardware/sim/tx-seq/results/2026-09-29-s2-coil/coil_tran.cir@98a6ea55f641672e479ade50967f962d5992ac95", "hardware/sim/tx-seq/results/2026-09-29-s2-coil/raw.sha256@29eab463c3f84d98b3d24fd41123d96c5d48ccdd", "hardware/sim/tx-seq/results/2026-09-29-s4-sequence/icd-tx-sw-timing-table.csv@b2aea5b8ffd530737ba890318ff8b3a2812bf4f6", "hardware/sim/tx-seq/results/2026-09-29-s4-sequence/result.json@cda544ddcbf9a6393b2fec001d03290e95610519", "docs/reviews/PDR/figures/timing-diagram.png@c73c949737ca1b32c8cae43cd6f6b8d33dcaa500", "hardware/sim/tx-seq/results/2026-09-29-s1-drive/s1-coil-current.png@f1c72b290a815118e08952e163a2f20e1cf21dfb", "hardware/sim/tx-seq/results/2026-09-29-s2-coil/s2-coil-transient.png@5841e9e18bde505614c34be43cd56e11345728e2", "hardware/sim/tx-seq/results/2026-09-29-s3-operate/s3-operate-vs-coil-temperature.png@e80d44e7b6eaf029a9ccd786d22ddaa1be207e7d", "hardware/sim/tx-seq/results/2026-09-29-s3-operate/s3-release.png@f3bc4f247117562b5bb7e39a5897f51511fb7190", "hardware/sim/tx-seq/results/2026-09-29-s4-sequence/timing-diagram.png@c73c949737ca1b32c8cae43cd6f6b8d33dcaa500", "hardware/sim/tx-seq/results/2026-09-29-s4-sequence/s4-keydown-budget.png@17aa3f0289530be7532f5aad676460a5b3cdf5a8", "hardware/sim/tx-seq/results/2026-09-29-s4-sequence/s4-margins.png@d7c2c8c5aa1cbe2c8545f104faede3b4065c8912"]
analysis_kind: [timing, worst-case, simulation-deck]
# product_size: iteration 1 text first; iteration 2 (fb120d2): note 492 lines, 13 sections; seq_run.py 1758 lines,
# relay_model.py 235 lines; 2 decks; 4 runs; 15 checks; 40 criteria; 39 timing-table rows; 49 input values;
# 10 distinct plots (11 cited paths); 15 delta per-case rows in this record. Iteration 3 (249356b): note 532 lines,
# 14 sections; seq_run.py 1981 lines, relay_model.py 235 lines; 2 decks; 4 runs; 17 checks; 40 criteria; 39
# timing-table rows; 11 distinct plots (12 cited paths); 10 delta per-case rows in this record
product_size: 1 note (366 lines, 12 sections), 2 scripts (1272 and 210 lines), 2 LTspice decks, 4 runs, 13 checks, 29 criteria, 35 timing-table rows, 7 distinct plots (8 cited paths), 39 input values, 2 proposed values, 26 per-case rows in this record
tools_used: ["LTspice 26.0.2 through tools/ltspice-batch.sh blob 88b71475 (TV-014, ACC-LTSPICE-001; .log first line 'LTspice 26.0.2 for MacOS' at iterations 1 and 2)", "venv Python 3.13.5 (TV-001, schema validation only; not for this model)", "numpy 2.5.3, scipy 1.18.1 (solve_ivp, brentq), matplotlib 3.11.2, spicelib 1.6.3 (no TV record)", "seq_run.py and relay_model.py at 95adefc (iteration 1), fb120d2 (iteration 2) and 249356b (iteration 3) (no TV record; developer evidence, 05 section 9.1)"]
# values_proposed (iteration 3, note section 7 at 249356b): REQ-SYS-160 condition (2) restated on the ratio age
values_proposed: ["REQ-SYS-161: 12 ms (unchanged), design lead-in 10 ms, on every radiated element including after a stale-ratio key-down", "REQ-SYS-160: 15 ms (unchanged), with (1) key bounce of at most 1.957 ms and (2) a closure within 83.3 ms of the hang expiry, when the frequency reference ratio is then more than 10 s old, sounded but not radiated (R-FRESH-2); possible after an over longer than 8.83 s, always after one longer than 10 s"]
# renders_inspected (iteration 3): the 11 distinct plots of the revision 2 runs; the figure copy is blob-identical
# to the r2-s4 copy (49db873d) and both paths were checked. Iteration 2: 10; iteration 1: 7
renders_inspected: 11
sprint: PDR-prep
author_agent: "author:WP-PDR-23a (Claude, analysis author invocation, RF designer role, 2026-09-29; revisions 0 to 2)"
reviewer_agent: "reviewer:WP-PDR-23a-sequencer-timing-iter1 (independent; authored no part of WP-PDR-23a, its scripts, its runs or the design data analysed); iteration 2 by reviewer:WP-PDR-23a-sequencer-timing-iter2 (independent; authored no part of WP-PDR-23a revision 0 or 1, and no part of INSP-123); iteration 3 by reviewer:WP-PDR-23a-sequencer-timing-iter3 (independent; authored no part of WP-PDR-23a revisions 0 to 2, of iterations 1 and 2 of this record, or of INSP-123)"
criticality: safety-critical
assurance_required: true
assurance_reviewer_agent: "sa-reviewer:WP-PDR-23a-sequencer-timing (separate invocation, SW-TXSEQ pair; paired record INSP-123, docs/reviews/PDR/checklists/analysis-sequencer-timing-software-assurance.md; 07 section 2.1.1)"
paired_record: INSP-123
iteration: 3
readiness_met: true
# reviewer_verdict (iteration 3): NEEDS CHANGES. finding-14 (Major) Verified. finding-13 (Major) stays Open: its fix
# restates the start voltage, the feed bound and the dropout and states K15-E OPEN, but the third input the fix named,
# the pack fall during an over, is 0.10 V with no source, while REQ-SYS-098 allows 0.27 V; the BM-1 acceptance and the
# lever figure follow from it. finding-15 Fixed. New Minor findings 17 and 18. Third iteration: the lead SE escalates
# to the owner (rule C1; 07 section 10.2).
# reviewer_verdict_iteration_2: NEEDS CHANGES. Findings 1 to 4 (Major) Verified. Two new Major findings in the
# fixes: finding-13 (the option E key-down hold rests on a key-down rail floor that is not the worst case its
# sources allow; K15-E fails at the steep end by the note's own method) and finding-14 (the stale-ratio condition
# proposed to the owner for REQ-SYS-160 states the wrong trigger). Findings 5 to 12 (iteration 1) and the new
# findings 15 and 16 are Minor and Open. Iteration 1: NEEDS CHANGES (4 Major, 8 Minor)
reviewer_verdict: NEEDS CHANGES
reviewer_verdict_iteration_2: NEEDS CHANGES
reviewer_verdict_iteration_1: NEEDS CHANGES
# assurance_verdict: copied from the paired record INSP-123 as last seen (iteration 2 at fb120d2, APPROVED, in the
# record returned to the lead SE); its iteration 3 delta on 249356b is a separate invocation. The software lead updates
# this field from INSP-123 at filing
assurance_verdict: APPROVED
# verdict: set by Claude as lead SE; held at NEEDS CHANGES by the open Major finding-13 (iteration 3; 13 and 14 at
# iteration 2), by INSP-123 until its iteration 3 delta returns, and
# (lead SE convention of 2026-09-27) until CR-012 merges with the analysis template blob 0386cc6e unchanged
verdict: NEEDS CHANGES
findings_major: 6
findings_minor: 12
findings_open: 12
findings_fixed: 1
findings_verified: 5
findings_deferred: 0
assurance_tasks_applied: []
deferred_rids: []
# items_no (iteration 3): A3, A4, B6, E3, F3 (finding-13); D2, D3 (finding-17, finding-5); G1-4 (finding-18); and the
# Minor items still open: A2 (finding-6, in part), A5 (finding-16, finding-10), A6 (finding-12), F2 (finding-9),
# G6-4 (finding-8), I2 (finding-7). E5 is Yes at iteration 3 (finding-14 Verified)
items_no: [CK-ANA-A2, CK-ANA-A3, CK-ANA-A4, CK-ANA-A5, CK-ANA-A6, CK-ANA-B6, CK-ANA-D2, CK-ANA-D3, CK-ANA-E3, CK-ANA-F2, CK-ANA-F3, CK-ANA-G1-4, CK-ANA-G6-4, CK-ANA-I2]
# effort: cumulative (iteration 1: 60 turns, 75 minutes; iteration 2: 62 turns, 85 minutes; iteration 3: 48 turns,
# 60 minutes)
effort_turns: 170
effort_minutes: 220
record_status: Open
date: 2026-09-29
date_closed: null
---

# Peer review record INSP-122: sequencer timing analysis, WP-PDR-23a (iterations 1 to 3)

**Iteration 3 in one paragraph (2026-09-29, product commit `249356b`, revision 2).** Reviewer verdict NEEDS CHANGES. The re-run from an export reproduces every output, and all 17 checks pass. finding-14 (Major) is Verified: the stale-ratio condition proposed for REQ-SYS-160 is now stated on the ratio's age, with the over lengths that give it (8.83 s, or 1.63 s of keying with the longest hang). finding-13 (Major) stays Open. Its fix restates the start voltage (6.30 V), the feed bound (0.5646 ohm at 2.140 A) and the limiter dropout (0.10 V), and states K15-E OPEN, which is right. But the third input the fix named, the pack fall during an over, is carried as 0.10 V with no source, while the design's own in-over end (REQ-SYS-098, cells at 2.95 V under load) allows 0.27 V. With it the coil sees 4.72 V (0.945 to 0.970 x), the BM-1 pass mark becomes 4.72 V instead of 4.89 V, and the lever option gives 1.017 to 1.043 x instead of 1.050 to 1.077 x. finding-15 is Fixed; two new Minor findings (17, 18). This is the third iteration, so the lead SE escalates to the owner (cross item X-8). Section "Iteration 3" at the end holds the delta.

**Iteration 2 in one paragraph (2026-09-29, product commit `fb120d2`, revision 1).** Reviewer verdict NEEDS CHANGES. Findings 1 to 4 (Major) are Verified: the H1 maximum-voltage graph is read and applied to the imposed peak, the H1 must-operate slope comes from its graph, the release is analysed at -10 C, and the stale-ratio key-down case is settled. The re-run from an export reproduces every output byte for byte. Two new Major findings sit in the fixes. finding-13: option E's key-down hold (K15-E) rests on a rail floor that leaves out the REQ-SYS-097 tolerance and the WP-PDR-21 revision 3 feed bound; with them the hold is 0.995 to 1.021 x by the note's own method. finding-14: the stale-ratio condition proposed to the owner for REQ-SYS-160 states the wrong trigger. Two new Minor findings (15, 16). Section "Iteration 2" at the end holds the delta.

The iteration 1 text follows unchanged, except the finding states and the new rows in the findings table.

**Product (iteration 1).** The 18 `product_files_iteration_1` above at freeze commit `95adefc` (F0, rule C2): the note `sequencer-timing.md` revision 0 (`8a628de6`), the runner `seq_run.py` (`8de9e1c2`), the relay model `relay_model.py` (`1140d549`), the expected-state list, the block README, the two LTspice decks, the `raw.sha256` manifest, the ICD-TX-SW timing table CSV, the s4 `result.json` and the eight cited plot paths (seven distinct images; the figure copy and the s4 copy are the same blob `c73c9497`). Every blob equals `git rev-parse 95adefc:<path>`, `git rev-parse HEAD:<path>` at HEAD `f8dcf8c`, and `git hash-object` of the working tree. `95adefc` is on `main`.

**Checklist.** `peer-review-checklist-analysis.md` revision A (CR-012 branch, blob `0386cc6e`): readiness R1 to R6, sections A to F, G1, G6, G7, H, I and J (criticality safety-critical: the note sets SW-TXSEQ timing values, 07 section 14.1).

**Search first.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any grep ("WP-PDR-23a sequencer timing review record checklist"; "Omron G5V-2 datasheet must operate voltage 75% operate time 7 ms H1 high sensitivity coil 150 mW"). grep and read-only Python were used afterwards only to pin lines.

**Verdict (rule C1): NEEDS CHANGES.** Four Major and eight Minor findings. The re-run reproduces every number of the note exactly. The schedule arithmetic (K1 to K9) is correct and the criteria states are right. The Major findings are all in the relay part of the analysis, where two datasheet graphs the note left unread change the recommended design, and in two worst cases that are not analysed:
- the H1 coil's maximum coil voltage at the PA-bay ambient is below the proposed 168 % pull-in (finding-1);
- the H1's must-operate voltage rises faster with temperature than the copper coefficient the model uses, which cuts the option C margin from 2.39 ms to about 0.6 ms and the hold guarantee from 1.07 x to about 1.00 x (finding-2);
- the T/R release is analysed only at the hot coil, while the cold coil is the worst case: 24.0 ms, not 13.92 ms (finding-3);
- the stale-ratio key-down case that `frequency-budget.md` asks this WP to settle is missing (finding-4).

No pass or fail state of the note's criteria list changes, except that K19 becomes a FAIL for the drive as proposed. Several values that go into ICD-TX-SW change, and so does the D-5 recommendation.

## Findings (iterations 1 to 3)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | reviewer | Major | CK-ANA-A4, CK-ANA-E3 | note sections 4.3 (last bullet), 5 row K19, 6.1 item 2; `seq_run.py` K19 (line 851) | **The recommended pull-in exceeds the H1's maximum coil voltage at the bay ambient.** The note leaves K19 OPEN because the "Ambient Temperature vs. Maximum Coil Voltage" graph was not read. The reviewer read it from the Omron datasheet (en-g5v_2.pdf, K046-E1-06, page 2, rendered at 600 dpi). The H1 3 to 24 VDC curve is flat at 180 % to about 54 C, then falls linearly to about 151 % at 70 C; the reading resolution is about +/-2 % and +/-1 K. At the relay ambients of `thermal-ts012.md` for A5 that gives about 167 % at 61.4 C and about 156 % at 67.1 C. Section 6.1 item 2 (100 % from the pack for 25 ms, 168 % at 8.4 V) is therefore outside the rating at both bay corners. The same datasheet note ("the maximum coil voltage refers to the maximum value in a varying range of operating power voltage, not a continuous voltage") leaves open whether the limit applies to the 8.4 V PWM peak or to the average. With a 2.27 % current ripple the coil sees the average, but the note must state its reading. Under a peak reading, any H1 drive from a pack above about 7.5 V is out of rating at 70 C, including the hold. **Fix:** record the graph read and its resolution. Make the capped pull-in the recommendation, for example pull-in duty min(1, 7.5 V / V_pack), 150 % or less, within the curve to 70 C. Restate K19 as a pass criterion on the capped drive, and state the average-versus-peak basis, as a question for the manufacturer if it cannot be settled from the datasheet. Show that K1b-C, K1b-D and K14 are unchanged: at 6.35 V the duty stays 100 % | Verified | Pending | |
| <a id="finding-2"></a>finding-2 | reviewer | Major | CK-ANA-A4, CK-ANA-B3 | `relay_model.py` docstring lines 20 to 22 and `ALPHA_CU`; note sections 2 (copper row), 4.2, 4.3, 5 rows K1b-C, K15-D, 8 row KD-12, 9 row BM-2 | **The H1's must-operate voltage rises faster with temperature than the copper coefficient the model uses.** The model holds the pick-up current constant, so the must-operate voltage rises at the copper 0.393 %/K for both coils. The docstring says the datasheet graph "shows the same trend". For the standard coil it does: the reviewer's read of the "max" curve is about 0.37 %/K relative. For the G5V-2-H1 it does not: the "max" curve runs from about 40 % at -55 C to about 86 % at 88 C, which is 0.48 to 0.51 %/K relative (10-piece sample). The reviewer re-ran s3 for options C and D, with the pick-up current and spring preload scaled by the extra factor, over all 13 accepted sets (`rv_h1_tempco.py`, below). With the extra factor 0 it reproduces the note exactly. At 0.48 %/K and 0.51 %/K:
- option C at 85 C: band maximum 8.00 and 8.40 ms (note: 7.11), so 8.5 to 8.9 ms with bounce against 9.5 ms;
- option D: 6.91 and 7.16 ms (note: 6.32);
- the ratio of the H1 5.0 V hold to the worst unit's must-operate current at an 85 C coil: 1.02 and 1.00 (note: 1.07).
No criterion changes state. But the "2.39 ms inside the limit" of the Summary and section 4.2 becomes about 0.6 to 1.0 ms, and the hold is no longer guaranteed with margin (K15-D). KD-12's maximum (7.61 ms) becomes about 8.5 to 8.9 ms. BM-2's acceptance of at most 8.5 ms would fail a unit the datasheet allows. **Fix:** use the H1 graph slope, or bound it, for the H1 coil. Raise the hold average to keep a stated margin over the read uncertainty (for example 5.5 V). Update KD-12, BM-1 and BM-2, and restate the option C and D margin comparison in section 6.1 item 1 | Verified | Pending | |
| <a id="finding-3"></a>finding-3 | reviewer | Major | CK-ANA-F1, CK-ANA-F3 | note sections 4.4 (release bullet), 5 rows K12-A and K12-D, 8 row KU-07; `seq_run.py` s3 release (lines 554 to 565), s4 K12 (lines 822 to 829) | **The T/R release is analysed only at the hot coil, which is the best case for release.** K12 and KU-07 evaluate the release at an 85 C coil, from a 5.0 V hold average. For release that is the fastest corner: the closed-gap time constant L/R is smallest there. REQ-SYS-036 applies over the REQ-SYS-114 ambient of -10 to +45 C. The note's own duty rule, D = min(1, 5.0 V / (V_pack - 0.9 V)), gives a receive-time average of 5.83 V at 6.35 V and 5.60 V at 8.4 V, not 5.0 V. The note's s2 case D_hold_cold already shows a 41.06 mA hold at -10 C. The reviewer ran the release in the note's own model (`rv_release_cold.py`, slowest diode form, 13 accepted sets). At a -10 C coil the band maximum is 22.60 to 23.04 ms, so **23.6 to 24.0 ms** with the 0.5 ms ordering and the 0.5 ms NC bounce. The ICD row KU-07 says 13.92 ms. At a 23 C coil it is 19.7 to 20.0 ms. K12-D still passes (30 ms share), but its margin is 6.0 ms, not 16.1 ms, and the KU-07 maximum passed to WP-PDR-36a and WP-PDR-19 is understated by about 10 ms. **Fix:** run the release over the coil range (-10 C to 85 C), both pack ends and the hold average of the duty rule. Carry the worst case into K12, KU-07 and BM-3, and give the options A and B release the same treatment | Verified | Pending | |
| <a id="finding-4"></a>finding-4 | reviewer | Major | CK-ANA-F2, CK-ANA-A6 | note sections 1 (scope), 4, 8; `frequency-budget.md` section 5 row "WP-PDR-23a" (revisions 2 to 4) | **The stale-ratio key-down case that WP-PDR-20a asks this WP to settle is missing.** Every revision of `frequency-budget.md` since revision 2 asks WP-PDR-23a to "Fix the R-FRESH-2 outcome for a key-down on a ratio older than A_kd = 10 s: late element or element not radiated". The note does not mention R-FRESH-2 or A_kd, and the timing table has no row for it. The case is a key-down sequence case inside this WP's scope. Either outcome touches a governing requirement: a late first element breaks the equal lead-in of REQ-SYS-161 and may break the 15 ms of REQ-SYS-160; a withheld element needs a SW-TXSEQ rule and the operator indication, and interacts with REQ-SYS-182. **Fix:** add the case with its criterion and timing-table rows, choosing the outcome and showing its effect on K2, K2b and K3. Or state explicitly that it is deferred, with the product and the owner route that takes it | Verified | Pending | |
| <a id="finding-5"></a>finding-5 | reviewer | Minor | CK-ANA-D2 | note Summary (interval-13 bullet), 4.6, 5 row K9, 6.2 row WP-PDR-54; `s4-keydown-budget.png` panel (b); `seq_run.py` lines 728 to 733 and 803 to 809 | **The note and its own plot disagree on the interval-13 fallback.** The note says the fallback fits only if PA_EN may follow TX_KEY, taking the D-18 gate's 0.25 ms turn-on bound: 11.443 ms, 0.06 ms inside 11.5 ms. The plot's "PA_EN may follow TX_KEY, 1 ms drive settle" line gives 12.19 ms at zero relock excess for the same ordering. That uses the 1 ms driver-settled allocation of the note's own K7, and it exceeds 12 ms. Both numbers come from the checker. The note must say which bound governs: with K7's allocation the fallback does not fit at all. The note also leaves `frequency-budget.md` revision 3's RL-6f figure of 0.308 ms from PA_EN to the ramp unaddressed. K9 is FAIL either way | Open | Pending | |
| <a id="finding-6"></a>finding-6 | reviewer | Minor | CK-ANA-A2 | note header row "Inputs from records under review", section 6.2 row WP-PDR-20a, section 12 | **Stale input citations.**
- The note cites `frequency-budget.md` revision 2 (`7593cea`), but revision 3 (`9dc9d63`) was committed 22 minutes before the freeze. Revision 3 already sets L_max = 1.9 ms, which is the change the 6.2 request to WP-PDR-20a asks for. It also adds M-1 ladder (c): the frequency is within 5 Hz of the settled frequency by t0 + 10 ms, else the ramp moves to t0 + 12 ms. The note does not carry ladder (c).
- `thermal-ts012.md` sets the coil-temperature corners of every relay result. It is cited without a revision or commit, and without its review state (revision 1, INSP-112 NEEDS CHANGES), and it is missing from the "records under review" row.
- `pa-permit-gate-d18.md` revision 1 (`c397ab1`, after the freeze) keeps the 0.25 ms turn-on bound. The delta should re-pin it together with `frequency-budget.md` revision 4 (`d030ce2`) | Open | Pending | |
| <a id="finding-7"></a>finding-7 | reviewer | Minor | CK-ANA-I2 | `timing-diagram.png` panel (a); `s2-coil-transient.png` right panel; `s4-margins.png` panel (b) | **Plot presentation.**
- Timing diagram panel (a): the annotation box covers the envelope-reference trace from about 17 ms onward, so the ramp is hidden.
- s2 right panel: the two dashed lines (about 20.5 and 25 mA, the worst-unit must-operate currents of the hot and the cold unit) have no label; only the left panel's title explains its dashed line.
- s4-margins panel (b): the criterion (margin at least 0) cannot be drawn on the log axis. Say so in the title.
No plotted value disagrees with the checker at the points the reviewer checked (listed under section I) | Open | Pending | |
| <a id="finding-8"></a>finding-8 | reviewer | Minor | CK-ANA-G6-4 | note section 4.4 (fault-path bullet), 5 row K16, 8 rows FP-01 to FP-03 | **K16 is compared with the 20 ms of REQ-SYS-004, but the design value is 10 ms.** 07 section 14.2 row j says `hazard-analysis.md` section 7 row j "states 10 ms (the design uses 10 ms until the REQ-SYS-004 TBR closes at PDR)". The note should compare against 10 ms as well, and name the hazard and control the fault path serves (HZ-004, with K8 for the two-condition RF rule), as CK-ANA-G6-4 requires. 1.1 ms passes both | Open | Pending | |
| <a id="finding-9"></a>finding-9 | reviewer | Minor | CK-ANA-F2 | note sections 4.4 and 8 (KU rows) | **A re-key during the end-of-over ordering or the relay release is not analysed.** Nothing covers a key-down during the 0.5 ms end-of-over ordering, or while the armature is releasing (up to about 24 ms after t_h, finding-3). The note should state the SW-TXSEQ rule, for example "a new over with a fresh t0 and the full lead-in". It should also state that the operate time from a partly released armature is bounded by the full operate time, or leave that to BM-2. This is an input to WP-PDR-32 and 35 | Open | Pending | |
| <a id="finding-10"></a>finding-10 | reviewer | Minor | CK-ANA-A5 | `seq_run.py` line 153 (`QBJT_VCESAT_DS`), s1 deck (RP 40 ohm, RbA 220 ohm); note section 2 row 2N3904 | **The 2N3904 drop floor is taken outside its datasheet condition.** The 0.30 V VCE(sat) floor is the datasheet point at 50 mA collector and 5 mA base current. Option A runs about 100 mA with about 10 mA of base current from a 3.3 V GPIO through 260 ohm, where the datasheet gives no maximum. That affects only option A, which already fails. The 40 ohm pad resistance also implies a GPIO drive-strength setting, and that setting is not routed to WP-PDR-36a's pad configuration. For option C the limiting corner is 26.5 mA, inside the datasheet point, so no result changes | Open | Pending | |
| <a id="finding-11"></a>finding-11 | reviewer | Minor | CK-ANA-A6 | note sections 4.3 (25 kHz bullet), 6.2 row WP-PDR-20b | **The 25 kHz hold PWM is routed only as a receive spur line, and it conflicts with ADR-031 rule 3.** The note calls the 25 kHz hold PWM a "dense-class" line for the spur plan. ADR-031 rule 3 (Proposed) requires dense-class clocks of at least 100 kHz, so on the note's own classification 25 kHz conflicts with it. But the PWM runs only while the relay is in TX, when the receiver is disconnected, so the receive rules may not be what applies. The transmit-side effect is not routed at all. The hold current pulses (about 25 to 41 mA at 25 kHz) flow in the pack feed (0.26 to 0.45 ohm) that also supplies the PA, which puts about 10 to 18 mV of ripple on the PA supply. That is a candidate for carrier sidebands at +/-25 kHz. **Fix:** state which rule applies, and route the transmit ripple to WP-PDR-22 and 20b. A frequency of 100 kHz or more, coherent per ADR-031, would meet rule 3 and lower the ripple | Open | Pending | |
| <a id="finding-12"></a>finding-12 | reviewer | Minor | CK-ANA-A6 | note section 6.1, 6.2 row WP-PDR-23b | **The H1's other datasheet differences are not passed to WP-PDR-23b.** The recommendation switches to the G5V-2-H1 but passes only its shock rating to WP-PDR-23b. The datasheet also differs from the standard part in contact resistance (100 mohm max against 50 mohm), maximum switching current (1 A against 2 A), rated load (1 A at 24 VDC) and dielectric strength between contacts of the same polarity (500 VAC against 750 VAC), which may mean a smaller contact gap and different RF isolation. These belong in the 23b request (isolation and stuck-relay cases) and in the OD-42 gate read | Open | Pending | |
| <a id="finding-13"></a>finding-13 | reviewer (iteration 2) | Major | CK-ANA-A3, CK-ANA-A4, CK-ANA-E3, CK-ANA-F3 | note section 2 rows "Switched pack rail" (r1, 5.45 V) and "(r1) Option E coil-supply limiter"; section 4.3 table row "H1, limiter in dropout at the 5.45 V key-down rail (E)" and the bullet "Option E's hold does not depend on any reading"; section 4.9 K22 bullet ("the key-down hold is 1.051 x with no reading used"); section 5 rows K15-E, K22-E; section 6.1 item 2; section 9 rows BM-1, BM-6; `seq_run.py` INPUTS `v_rx_min`, `v_kd_min` (lines 155, 156) | **The option E key-down hold rests on a rail floor that is not the worst case its sources allow.** K15-E (1.051 to 1.079 x) is the hold guarantee of the recommended design. It takes the lowest key-down coil voltage as 5.25 V: 6.4 V, less 0.05 V in receive, less 0.9 V of feed drop at 2 A, less the 0.2 V limiter dropout. Two of these inputs are not the worst case. (a) REQ-SYS-097 refuses a transmission only while a cell "reads below 3.20 V +/-0.05 V (TBR)", measured in receive. A transmission can therefore start at 6.30 V, not 6.4 V. The note's row calls 6.4 V "the REQ-SYS-097 transmit floor" and drops the tolerance. (b) The 0.9 V comes from TS-012's 0.26 to 0.45 ohm estimate, which is for parts at 25 C. WP-PDR-21 revision 3 (`f1070cf`, on main before this freeze) gives the drain-feed bound at the +45 C key-down corner: 0.5646 ohm (`hardware/sim/tx-pa/results/2026-09-29-r3-p4-power-a5-design/result.json`, `by_tc.hot45a.feed_ohm.bound`). That is the same corner that gives the 85 C coil. At the note's 2.0 A it is a 1.13 V drop. With both inputs, and the note's own method (coil at 85 C, dropout 0.2 V), the coil sees 4.97 V. The hold is then **0.995 x at the steep end of the slope band and 1.021 x at the shallow end**. So K15-E does not pass at the steep end, which is the end the note says governs (reviewer check `rv_k15e_rail.py`, plot `rv_k15e_rail.png`, iteration 2 section). The note's pairing of this rail with an 85 C coil is conservative. At 4.97 V the coil dissipates about 0.13 W and sits near 78 C (67.1 C bay air plus 80 K/W), where the hold is 1.024 x. With 0.1 V of cell discharge during an over it is 1.006 x. REQ-SYS-097 checks the cells only at the start, and the note bounds no discharge during an over of up to 180 s. So the hold may still be met, but the note has not shown it: the stated 5 % margin is not there, and what is left is smaller than the slope-band and feed uncertainty. The same floor also moves the pull-in low corner from 6.15 V to 6.05 V (6.30 V less 0.05 V less 0.2 V). The model's worst unit then operates in 8.36 ms at an 85 C coil, 8.86 ms with bounce (reviewer run of the frozen model, 13 sets, both slopes). K1b-E still passes, with 1.14 ms instead of 1.61 ms, but KD-12's maximum becomes 8.86 ms. Major: an input that sets a reported result is not the worst case its source allows, and with it the criterion the recommendation relies on (K15-E; also K22-E's "1.051 x") fails by the note's own method. **Fix:** take the lowest key-down coil voltage from the REQ-SYS-097 tolerance, from the WP-PDR-21 revision 3 feed bound at the key-down corner that sets the coil temperature, and from a stated bound on the cell voltage during an over (or the design's in-over under-voltage end). Then do one of: (i) pair that voltage with the coil temperature it produces and show K15-E of at least 1.0, with its margin stated against the slope and feed uncertainty; (ii) tighten the limiter's dropout requirement, for example to at most 0.1 V at the hold current; or (iii) state K15-E as OPEN, with BM-1's acceptance restated. Carry the 6.05 V pull-in corner into K1b-E, KD-12 and BM-2, and restate BM-6. **Iteration 3 (249356b):** fixed in part. The start at 6.30 V, the feed bound 0.5646 ohm with the p4 current 2.140 A, the 0.10 V dropout, K15-E OPEN, the 6.11 V pull-in floor (K1b-E 8.57 ms, KD-12, BM-2), BM-6 and K22-E are done. Not done: the pack fall during an over is 0.10 V, class E, sourced to this record's own illustration, not bounded; REQ-SYS-098 (a cell may read 2.95 V under load) gives 0.27 V, a 4.720 V coil and 0.945 to 0.970 x. BM-1's 4.89 V acceptance and the lever's 1.050 to 1.077 x follow from the unbounded value (at the REQ-SYS-098 end: 4.72 V, and 1.017 to 1.043 x). Fix: take the in-over floor from REQ-SYS-098 or from a cited cell bound over the longest over, and restate K15-E, BM-1, BM-4, BM-6 and the lever figure (iteration 3 section) | Open | Pending | |
| <a id="finding-14"></a>finding-14 | reviewer (iteration 2) | Major | CK-ANA-E5, CK-ANA-A5 | note Summary (K20 bullet), section 4.8 (lines 246 and 255), section 5 row K20-c, section 7 row REQ-SYS-160 condition (2), section 8 row SR-01; `seq_run.py` lines 1380 and 1694 (SR-01 text, `s4-stale-ratio.png` axis label) | **The stale-ratio condition proposed to the owner for REQ-SYS-160 states the wrong trigger.** Condition (2) reads "a closure within 82.8 ms of the return to receive after an over longer than 10 s is sounded but not radiated". The design rule of section 4.8, and R-FRESH-2 itself, are written on the ratio's age at t0: older than A_kd = 10 s. That age is the over, from its t0 to the hang expiry, plus the ratio's age when the over started. In receive the ratio is up to 1.083 s old (`frequency-budget.md` revision 4 line 382, FR-2r: the 1 s refresh plus 82.8 ms). So the case starts after an over of about **8.9 s**, not 10 s. Section 4.8 also counts the hang apart from the over ("an over longer than 10 s and a pause after it only slightly longer than the hang"). Read that way, the text understates the case further: with the longest hang, 30 dits at 5 WPM (7.2 s), about 1.7 s of keying is enough. Condition (2) is part of a proposed value (rule C10), and a test written from it (TC-SYS-102) would expect RF on key-downs after overs of 8.9 to 10 s, which the design correctly withholds. Major under the template's "changes ... a proposed value". The firmware rule and the HostUnit cases (ratio age 10.1 s and 9.9 s) are right. **Fix:** state condition (2) on the ratio age, "a closure within 82.8 ms of the return to receive, when the ratio is older than 10 s: after an over of about 8.9 s or more, counted from its first element to the hang expiry". Say how often that arises with a long hang, so the owner can judge the condition, and align the SR-01 text and the plot label | Verified | Pending | |
| <a id="finding-15"></a>finding-15 | reviewer (iteration 2) | Minor | CK-ANA-D2 | note Summary (line 23, "E has 1.11 ms to the limit"), section 4.2 reading (line 190, "option E by 7.89 ms, 1.11 ms inside it") | **The option E operate margin is stated as 1.11 ms, but by the note's own criterion it is 1.61 ms.** K1b-E's limit is "operate + 0.5 ms <= 10.0 ms" (s4 `result.json`), which is 8.39 ms against 10 ms. The 1.11 ms compares 8.39 ms with 9.5 ms, a limit that already has the bounce taken off, so the bounce is subtracted twice. The error is on the conservative side and no state changes. After finding-13 the figure becomes about 1.14 ms (6.05 V corner). Fix: state one margin with its limit. Iteration 3: the Summary and section 4.2 give 1.43 ms, equal to K1b-E (8.57 against 10 ms) | Fixed | Pending | |
| <a id="finding-16"></a>finding-16 | reviewer (iteration 2) | Minor | CK-ANA-A5 | note section 4.9 (K21 bullet: "It is shorter than every hang (72 ms or more) and than the release margin, so a real return to receive always re-arms it"); section 6.2 row WP-PDR-26 | **The reason given for the 30 ms re-arm qualification is wrong.** The backstop re-arms only after TR_DRV has been low for 30 ms. TR_DRV goes low at the hang expiry (KU-06), so the low time is the operator's pause after the hang, not the hang. A key-down within 30 ms of the hang expiry starts a new over while the backstop is still counting from the last one. REQ-SYS-180 then ends RF early. That is the safe side (a nuisance cut-off, not a hazard), and at that point the relay may not have released anyway (KU-07 up to 25.86 ms). Fix: correct the sentence, and pass the case to WP-PDR-26 with the intended behaviour (the count runs on, or restarts at the new t0 only once the contacts have reached receive) | Open | Pending | |
| <a id="finding-17"></a>finding-17 | reviewer (iteration 3) | Minor | CK-ANA-D2, CK-ANA-D3 | note Summary line 25 ("dropout at most 0.2 V"); Summary, section 4.3 and section 5 row K15-E ("0.980") | **Stale dropout in the Summary, and a ratio rounded toward the limit.** (a) The Summary gives the option E limiter as "dropout at most 0.2 V"; section 2 and section 6.1 item 2, the part requirement for WP-PDR-37 and 38, say 0.10 V. (b) The key-down hold 0.97969 x is printed as 0.980 x, rounded toward the 1.0 limit (`s3-keydown-hold.png` prints 0.9797). No state changes. Fix: 0.10 V in the Summary; 0.979 or 0.9797 | Open | Pending | |
| <a id="finding-18"></a>finding-18 | reviewer (iteration 3) | Minor | CK-ANA-G1-4 | `seq_run.py` `p4_feed_check` (lines 1177 to 1186); note section 3.4; README | **The new check `p4_feed_current` passes when its input file is absent.** The WP-PDR-21 p4 `.raw` is over 5,000,000 bytes and, under CR-017 C2, exists only in the owner's working tree. Without it the check returns PASS ("inputs used as recorded, not re-derived"), so in any export or clone `seq_run.py all --expect` still reports 17 checks passing (reviewer run with the file removed: exit 0). Section 3.4 describes the check as re-deriving the currents. The values are right (reviewer re-derivation by separate code). Fix: a separate state (for example NOT RUN) that `--expect` records, or a statement in section 3.4 and the README that the check runs only where the `.raw` is kept | Open | Pending | |

## Readiness criteria

| # | Criterion | Evidence | Met |
|---|---|---|---|
| R1 | Blobs frozen | All 18 `product_files` blobs equal `git rev-parse 95adefc:<path>` = `HEAD:<path>` (`f8dcf8c`) = `git hash-object` of the working tree; `git branch --contains 95adefc` gives `main` | Yes |
| R2 | One command, stated exit | `git archive 95adefc` exported to the scratchpad (`rv23a-95adefc/`), the committed results moved aside; `.venv/bin/python hardware/sim/tx-seq/seq_run.py all --expect` exit **0** in 47.5 s; without `--expect` exit **1** (checks pass, K1b-A, K1b-B, K9 FAIL, K15-B, K19 OPEN), as note section 3.4 states. LTspice ran only through `tools/ltspice-batch.sh` (blob `88b71475`, the ACC-LTSPICE-001 blob), which checks `CaptureAnalytics=false` through iconv and guards the time-out | Yes |
| R3 | validate_docs | `expected_states.json` has no schema, so N/A for the product; `tools/validate_docs.py` on the export exits 0 (117 passed). The reviewer could not run it on this record, because the record file is created by the lead SE; the lead SE runs it when filing | N/A for the product |
| R4 | Author return complete | The WP return lists question, runs, criteria, main finding, blobs, the large-file handling and the check status; values proposed and tools are in the note header and section 7 | Yes |
| R5 | No TBD; TBR ids | No `TBD` in the note; every TBR relied on is named by id (REQ-SYS-004, 036, 044, 159, 160, 161, 182) and each has its `tbr` object at HEAD | Yes |
| R6 | Renders exist | The 7 plot files and the figure copy exist beside their run (`results/<run>/`) and at `docs/reviews/PDR/figures/timing-diagram.png` | Yes |

## A. Question, scope and traceable inputs

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-A1 | Yes | Header "Serves" and section 1 table: REQ-SYS-160, 161, 120, 182, 036, 044, 004, 159; 07 section 14.2 rows b, c, h; HZ-004 K8 (exists in `hazards.json`, "Two independent software conditions for RF"); D-5, D-11, D-17, D-18; TC-SYS-102, 030, 024. Each requirement id exists and its text at HEAD matches the note's short text (REQ-SYS-160 "begin the RF rise within 15 ms (TBR) of each straight-key contact closure": the ramp start is the right event) |
| CK-ANA-A2 | No | TS-012 revision 8 `bb5dee7` and `keying-ts012.md` are pinned. `frequency-budget.md` is pinned at revision 2 while revision 3 preceded the freeze, and `thermal-ts012.md` is unpinned (finding-6) |
| CK-ANA-A3 | Yes | Every input in section 2 has a class and a source; allocations are labelled A and estimates E |
| CK-ANA-A4 | No | Per-input check below. Two curve inputs that set results were not read: the H1 maximum coil voltage against ambient (finding-1) and the H1 must-operate voltage against ambient (finding-2) |
| CK-ANA-A5 | Yes, with finding-10 | Section 10 bounds the model, the worst-case unit, the coil corners, the bounce and the upstream inputs. The 2N3904 floor is outside its datasheet condition (finding-10, affects option A only) |
| CK-ANA-A6 | No | The analysis edits no file and routes requests (section 6.2). But the R-FRESH-2 request made to it is dropped silently (finding-4), and the hold PWM's conflict with ADR-031 and the H1 contact differences are not routed (findings 11 and 12) |

**Per-input check (CK-ANA-A4), against the sources.**

| Input | Note | Source read by the reviewer | Agreement |
|---|---|---|---|
| G5V-2 operate, release | 7 ms max, 3 ms max, both types | Omron en-g5v_2.pdf (K046-E1-06, 2016) page 1 Characteristics: "Operate time 7 ms max.", "Release time 3 ms max." (one row for both) | Agrees |
| Must-operate, must-release | 75 % max, 5 % min, coil 23 C | Page 2 Ratings: both types 75 % max, 5 % min; Note 2 "measured at a coil temperature of 23 C" | Agrees |
| Coils | std 100 mA, 50 ohm, about 500 mW, 120 %; H1 30 mA, 166.7 ohm, about 150 mW, 180 %; +/-10 % | Page 2 Ratings 5 VDC rows and Note 1 | Agrees |
| Ambient | std -25 to 65 C; H1 -25 to 70 C | Page 1 Characteristics | Agrees |
| Shock malfunction | H1 100 m/s2 against 200 m/s2 | Page 1 | Agrees |
| H1 maximum coil voltage against ambient | "graph, not text-readable", 180 % at 23 C only | Page 2 graph: 180 % to about 54 C, about 151 % at 70 C | **Not read in the note** (finding-1) |
| Must-operate against temperature | copper 0.393 %/K for both coils | Page 2 graphs: std about 0.37 %/K (agrees); H1 about 0.48 to 0.51 %/K | **Disagrees for the H1** (finding-2) |
| Relay ambient 61.4 C, 67.1 C | A5 duty limit, continuous | `thermal-ts012.md` revision 1 section 7 table, row "Relay ambient", A5 column: "FAIL continuous (67.1 C); OPEN at the duty limit (61.4 C)" | Agrees (the source is under review, finding-6) |
| 5 V bus 4.75 to 5.25 V | LM2940 SNVS769J 6.5 | TS-012 INSP T18 reading "4.75 / 5 / 5.25 V over the recommended operating temperature range" | Agrees |
| C6 writes 0.650 ms | frequency-budget RL-2 | `frequency-budget.md` revision 4 line 287: "0.650 ms, or 0.723 ms with the reg 177 reset" | Agrees |
| FC0 interval 12, 13 | 4.096, 8.192 ms bound | Carried from `frequency-budget.md` revision 3 RL-4 (4.096 ms) | Agrees |
| Lock read and compare 2 ms; lead 2 ms; tail 1 ms; ramp 10 ms after t0 | TS-012 7.3 rev 6 | TS-012 line 491: "within the 2 ms software allocation ... TX_KEY rises at t0 + 8 ms ... at t0 + 10 ms the reference clamp releases" | Agrees |
| Interval-13 fallback 11 / 11.5 ms; revisit 3 ms | TS-012 | TS-012 lines 491 and 1219 | Agrees |
| D-18 turn-on 0.25 ms, powered 1.2 us | `pa-permit-gate-d18.md` rev 0 | Revision 1 (`c397ab1`) lines 28, 172, 301: same values | Agrees |
| Key sampling 1 ms, filter 2 samples within 2 ms | REQ-SW-KEYER-019, 020, 018 | Carried from the keyer requirements; the K3 arithmetic 1 + 2 + 10 + 0.043 = 13.043 ms re-computed | Agrees |
| Ramp 3 to 8 ms; hang 3 to 30 dits; speeds 5 to 50 WPM | REQ-SYS-014, 044, REQ-SW-KEYER-015 | REQ-SYS-014 and 044 texts at HEAD | Agrees |
| REQ-SYS-004 20 ms | requirement | Agrees; 07 row j design value 10 ms (finding-8) | Agrees |
| Envelope PWM period 0.0427 ms at clk_sys 96 MHz | TS-012 D-12 | TS-012 line 611 "clk_sys = clk_peri = 96 MHz" in TX; ADR-031 (Proposed) has 150 MHz, where the period is 0.0273 ms. 96 MHz is the conservative choice | Agrees (conservative) |

## B. Model validity

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-B1 | Yes | Section 3.3 and the `relay_model.py` docstring state the lumped magnetic circuit, no saturation or eddy currents, the co-energy force and the spring line, and the effect (section 10 item 1) |
| CK-ANA-B2 | Yes | The 2N3904 and 1N4148 models are copied from LTspice `standard.bjt` and `standard.dio` (named in the deck). The AO3400A VDMOS is a fit marked class E and checked against the datasheet 48 mohm at 2.5 V (s1 check `mos_ron_range_mohm` 29 to 32 mohm). Its validity covers 5 to 105 mA and 25 to 70 C |
| CK-ANA-B3 | No | The anchoring (7 ms at the datasheet point, release at most 3 ms without a diode) is quantified (under 0.01 ms). But the temperature behaviour, which sets every hot-corner result, is validated only for the standard coil. The H1 graph disagrees (finding-2) |
| CK-ANA-B4 | Yes | s2 `.tran 0 90m 0 8u` with 25 kHz PWM (5 points per 40 us period and the 50 ns edges forced by the source): the closed forms agree within 0.39 %. s3 `solve_ivp` max_step 10 us, rtol 1e-8; the operate events resolve to 10 us against margins of at least 0.6 ms |
| CK-ANA-B5 | Yes | Independent checks, listed under "Independent checks" below: the ratio table by hand (16 of 16 agree to 0.001), the D-5 hold currents by hand, the K1 to K9 schedule by hand, and a separate harness over the note's model (reproduces the C and D corner results exactly, then the sensitivity of finding-2) |
| CK-ANA-B6 | Yes, partly | Section 10 lists the model band, the unit limits, the thermal band, the bounce read and the upstream inputs. The operate and release bands are quantified per corner. The margin comparison fails E3 through findings 1 to 3 |

## C. Tools, validation status and reproducibility

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-C1 | Yes | Both `.log` first lines read `LTspice 26.0.2 for MacOS`, the wrapper blob is `88b71475` (the ACC-LTSPICE-001 blob), and the venv versions are numpy 2.5.3, scipy 1.18.1, matplotlib 3.11.2 and spicelib 1.6.3 (`pip list`) |
| CK-ANA-C2 | Yes | LTspice is accredited (TV-014, ACC-LTSPICE-001, purposes 1 to 4). The Python model has no TV record, and the note marks the evidence as developer evidence (header "Evidence status"). The proposed values go to the owner only after this record is APPROVED (rule C10), and the owner rules on developer evidence |
| CK-ANA-C3 | Yes | One command. The decks are `.cir` netlists, one analysis each (`.dc`, `.tran`), and the LTspice run never uses an `.asc` |
| CK-ANA-C4 | Yes | Reviewer re-run from the export (commands below):
- s3 `result.json` and runs, s4 criteria, the ICD CSV, and all 7 PNGs are byte-identical to the committed files;
- s1 and s2 `result.json` differ only in the wrapper out-dir path and the deck-free `.raw` hash;
- the `.raw` files differ only in the header `Date:` line: the binary data section after `Binary:` is bit-identical (SHA-256 of the data section, `coil_tran.raw` `a7e14a4d...` both runs, `drive_dc.raw` `11d6a565...` both);
- the working-tree `coil_tran.raw` hash equals `raw.sha256` (`bb627b82...`).

A `.raw` hash cannot be reproduced run to run for this reason. This is not a finding: CR-017 C2 keeps the file |
| CK-ANA-C5 | Yes | TV-014 section 6 limitations are respected: wrapper only, netlists, time-out guard, short run directory, lock |

## D. Units, arithmetic and consistency

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-D1 | Yes | ms, mA, V, ohm, K, % of rated are used throughout. The copper coefficient is applied from 23 C, not 20 C; the difference is 0.004 %/K and conservative |
| CK-ANA-D2 | No | The note tables, `result.md` files and plots agree at every point checked. The exception is the interval-13 "PA_EN may follow" case: 11.443 ms in the note and 12.19 ms in the plot (finding-5) |
| CK-ANA-D3 | Yes | The 1.903 ms latest start is reported to 0.001 ms, and `frequency-budget.md` rounds it down to 1.9. Margins are given to 0.01 ms against inputs of 0.01 ms or better |
| CK-ANA-D4 | Yes | `t_key_rf_req` 15.0, `t_leadin_req` 12.0, `t_leadin_eq` 0.5, `t_rf_off_req` 20.0, `t_sidetone_req` 4.0, `t_rx_alloc` 50.0: each carries its requirement id and an inclusive comparison (`<=`) as the requirement words "within" and "at most" read |

## E. Results, margins, proposed values and credit

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-E1 | Yes | Limits are quoted with ids (section 1 table; `INPUTS` sources) |
| CK-ANA-E2 | Yes | Margins are computed as limit minus result with the right sign (K3b 1.957 ms, K10 52.96 ms). No TPM applies |
| CK-ANA-E3 | No | K1b-C's stated 2.39 ms, K15-D's 1.07 x and K12-D's 16.1 ms do not cover the datasheet-graph and cold-corner uncertainty (findings 2, 3). The drive proposed for K19 is out of rating (finding-1) |
| CK-ANA-E4 | Yes | `seq_run.py` asserts 13 checks (exit 2 on a check failure) and every criterion (exit 1 on FAIL or OPEN). `--expect` compares the states with `expected_states.json` (exit 3 on any change). Observed exits: 0 with `--expect`, 1 without |
| CK-ANA-E5 | Yes | Section 7: REQ-SYS-161 12 ms kept with a 10 ms design lead-in (margin 1.96 ms); REQ-SYS-160 15 ms kept with the bounce condition of 1.957 ms. Both carry the `tbr.plan` step ("The T/R element trade at PDR fixes the lead-in / the relay operate and bounce times"), no CR branch, and no edit to the requirement file. Supported by the schedule as analysed. The condition "on section 6.1 or BM-2" must be restated once findings 1 and 2 change section 6.1 |
| CK-ANA-E6 | N/A | No TPM estimate proposed |
| CK-ANA-E7 | Yes | Both requirements are `verification_method` Test; the note claims supporting Analysis only (TC-SYS-102 method) |

## F. Every case named

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-F1 | No | The per-case table below lists every case the governing texts name. REQ-SYS-036 at the cold end of REQ-SYS-114 is missing (finding-3); every other case is present |
| CK-ANA-F2 | No | The fault path (FP-01 to FP-03), the stuck and dropped relay (routed to 23b) and the late contact (section 4.2 reading) are covered. The stale-ratio key-down (finding-4) and a re-key during the end of the over or the release (finding-9) are not |
| CK-ANA-F3 | No | The worst combination is stated for operate (lowest supply, hottest coil, worst unit, band maximum). For release the worst combination (cold coil, highest hold average) is not analysed (finding-3) |
| CK-ANA-F4 | Yes, partly | Options B and C sit within twice their uncertainty. Section 4.2's temperature sweep and the band give the sensitivity to coil temperature and the model parameters. The supply sensitivity is in `s3 result.md` (48 rows) |

### Per-case results

| Case | Condition | Governing id and limit | Result (checker) | Margin | Uncertainty | Reviewer re-check | Finding ids |
|---|---|---|---|---|---|---|---|
| C-1 | ramp start after T/R command | plan criterion 1: at least 10 ms | 10.000 ms | 0.000 ms (later only by 0.043 ms quantisation) | none (schedule) | hand: L = 10.0 | none |
| C-2 | first element lead-in | REQ-SYS-161: at most 12 ms | 9.980 to 10.043 ms | +1.957 ms | software allocations (section 10 item 6) | hand: 10 - 0.02, 10 + 4096/96 MHz | none |
| C-3 | later elements, 5 to 50 WPM, ramp 3/5/8 ms | REQ-SYS-161 equality 0.5 ms (TC-SYS-102) | spread 0.063 ms | +0.437 ms | as C-2 | hand | none |
| C-4 | straight key, bounce 0 | REQ-SYS-160: at most 15 ms | 13.043 ms | +1.957 ms | as C-2 | hand: 1 + 2 + 10 + 0.043 | none |
| C-5 | straight key with bounce B | REQ-SYS-160 | holds for B at most 1.957 ms (condition) | condition on the key | key bounce unknown (WP-PDR-40) | plot `s4-margins.png` (a) crosses 15 ms at 1.96 ms | none |
| C-6 | clamps and integrator | plan criterion 4 | VGG clamp off t0 + 8, reference at t0 + 10 | 2 ms / 0 ms | none | hand | none |
| C-7 | frequency check before PA_EN, interval 12 | TS-012 rev 8 8.12 | 7.097 against 7.5 ms | +0.403 ms (0.903 ms to TX_KEY) | relock time (M-1) | hand: 1 + 0.0006 + 4.096 + 2 | none |
| C-8 | interval-13 fallback | REQ-SYS-161 12 ms | 13.193 ms (FAIL) | -1.193 ms | as C-7 | hand; plot shows 12.19 ms for the "may follow" case | finding-5 |
| C-9 | PA_EN before TX_KEY | REQ-SYS-120, D-18 | 7.5 against 8.0 ms | +0.5 ms | none | hand | none |
| C-10 | driver settled before ramp | K7 | 9.0 ms | +1.0 ms | D-18 rev 1: 1.2 us | hand | none |
| C-11 | option A, 4.75 V, coil 23/49/75/85 C | contact + bounce before ramp (9.5 ms) | 9.11 / 12.59 / none / none (FAIL) | negative | model band; ratio above 1 is datasheet-only | ratio by hand: 0.843, 0.929, 1.015, 1.048 | none |
| C-12 | option B, same corners | 9.5 ms | 7.77 / 9.65 / 14.10 / 19.56 (FAIL) | negative from 49 C | model band | ratio by hand 0.790 to 0.982 | none |
| C-13 | option C, 6.35 V, coil to 85 C | 9.5 ms | 7.11 ms band max (PASS) | +2.39 ms in the note; about +0.6 to +1.0 ms with the H1 graph slope | model band plus tempco | reviewer model run: 8.00 to 8.40 ms | finding-2 |
| C-14 | option D, same | 9.5 ms | 6.32 ms (PASS) | +3.18 ms; +1.84 to +2.09 ms with the H1 slope | as C-13 | reviewer: 6.91 to 7.16 ms | finding-2 |
| C-15 | H1 pull-in at 8.4 V, bay ambient 61.4 / 67.1 C | datasheet maximum coil voltage | 168 % (OPEN in the note) | about -1 % at 61.4 C, about -12 % at 67.1 C (graph read) | +/-2 % read | graph read | finding-1 |
| C-16 | standard coil 63 % hold | datasheet hold guarantee | 0.64 x (OPEN) | negative | none (datasheet) | hand: 0.63 x 4.75 / 62.18 ohm = 48.1 mA; 48.1 / 75.4 mA | none |
| C-17 | H1 5.0 V hold, 85 C coil | hold at least the worst unit's must-operate current | 1.07 x (PASS) | +7 %; +0 to +2 % with the H1 slope | graph read | hand: 1.3333 / 1.2437 = 1.072 | finding-2 |
| C-18 | hold ripple, 25 kHz | K13 5 % | 2.27 % | +2.73 % | LTspice | `s2 result.md` | finding-11 |
| C-19 | release, options C/D, 85 C coil, 5.0 V hold | REQ-SYS-036 30 ms share | 13.92 ms (PASS) | +16.08 ms | model band | reproduced | finding-3 |
| C-20 | release, options C/D, -10 C coil, duty-rule hold 5.6 to 5.83 V | REQ-SYS-036 30 ms share | not analysed | reviewer: 24.04 ms, +5.96 ms | model band | reviewer model run | finding-3 |
| C-21 | key-up cold switching, 50 WPM, 3 dits, 8 ms fall | K10 | 52.96 ms | +52.96 ms | none | hand: 72 - 19.043 | none |
| C-22 | REQ-SYS-044 floor 3 dits, 5 to 50 WPM | hang at least lead-in + fall + tail | 72 against 19.04 ms at 50 WPM | +52.96 ms (larger at lower speeds) | none | plot `s4-margins.png` (b) | none |
| C-23 | inhibit to RF off | REQ-SYS-004 20 ms (design 10 ms, 07 row j) | 1.1 ms | +18.9 ms (+8.9 ms) | allocations | hand | finding-8 |
| C-24 | sidetone, key or paddle, bounce 0 | REQ-SYS-159 4 ms | 3.1 ms | +0.9 ms | allocations | hand: straight key 1 + 2 + 0.1; paddle REQ-SYS-043 3 + 0.1 | none |
| C-25 | TX_KEY windows, 50 WPM, 8 ms ramps | K18 | 13.0 ms gap | +13.0 ms | none | hand: 24 - 8 - 2 - 1 | none |
| C-26 | key-down on a stale TCXO ratio (A_kd 10 s) | REQ-SYS-161, 182 | not analysed | - | - | - | finding-4 |

## G1. Simulation decks and checkers

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-G1-1 | Yes | The decks and runner are under `hardware/sim/tx-seq/`, with the plots beside each run |
| CK-ANA-G1-2 | Yes | `drive_dc.cir` `.dc` only, `coil_tran.cir` `.tran` only (the `.op.raw` is LTspice's own initial point); no `NC_` nets in either netlist (every node named and connected) |
| CK-ANA-G1-3 | Yes | The drivers and coils equal the TS-012 BOM rows 12 and 22 and the datasheet coils. The source impedance (40 ohm pad) is an estimate (finding-10) |
| CK-ANA-G1-4 | Yes | s1 and s2 read the `.raw` through spicelib and check the step count, and `run_ltspice` exits 2 on a wrapper failure |

## G6. Timing

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-G6-1 | Yes | 1.000 ms sampling, 12 MHz clk_ref for FC0_DELAY, and clk_sys 96 MHz (TS-012 D-12) for the envelope PWM are stated. Crystal ppm is negligible at ms scale |
| CK-ANA-G6-2 | Yes | Detection, I2C, PLL, count, compare, relay operate and bounce, driver settle and quantisation are all summed. The software latencies are allocations for WP-PDR-32 (section 10 item 6) |
| CK-ANA-G6-3 | Yes | No duration is taken from an Emulation run. The timing table's "Emulation event order" entries are ordering only |
| CK-ANA-G6-4 | No | The fault path is analysed, but not against the 07 row j design value, and without naming the hazard and control (finding-8) |

## G7. Worst-case

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-G7-1 | Yes | Extreme value: the worst-case unit at both datasheet limits, the lowest supply, the hottest coil and the band maximum |
| CK-ANA-G7-2 | Yes, with findings 1 and 2 | Coil tolerance +/-10 %, copper tempco, bus and pack range. The H1 derating curve and must-operate slope are not applied |

## H. Hazards, risks and records

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-H1 | Yes | HZ-004 K8 is named, and the late-contact failure mode (TS-012 R-1) is tied to REQ-SYS-156. No `hazards.json` edit |
| CK-ANA-H2 | Yes | A new risk entry is requested of WP-PDR-18 (section 6.2), with an "if, then" statement |
| CK-ANA-H3 | Yes | Change history row for revision 0 |

## I. Visual closure

Opened with the Read tool (7 distinct renders; the figure copy is blob-identical to the s4 copy, and both paths were checked):
- `docs/reviews/PDR/figures/timing-diagram.png`: panel (a) events match KD rows (PA_EN 10.5 ms, TX_KEY 11 ms, ramp 13 ms after the contact; option B tick at t0 + 10.15 ms). Panel (b): release band t_h to t_h + 14 ms, REQ-SYS-036 at t_h + 50 ms;
- `s1-coil-current.png`: 68.7 mA (2N3904) and 69.4 mA (AO3400A) at 4.75 V against 68.2 mA, as section 3.2 states;
- `s2-coil-transient.png`: hold levels 39.6, 25.3 and 41.1 mA, as `s2 result.md` states;
- `s3-operate-vs-coil-temperature.png`: B 9.65 ms at 49 C and 14.1 ms at 75 C; A 12.6 ms at 49 C; limit line at 9.5 ms;
- `s3-release.png`: D hold5v 6.3 ms nominal, 12.9 ms band;
- `s4-keydown-budget.png`: panel (a) ramp at 13.00 and 16.19 ms. Panel (b) 10 ms crossing at 0.9 ms of excess and 12 ms at 2.9 ms; the orange dashed line at 12.19 ms is finding-5;
- `s4-margins.png`: 15 ms crossing at 1.96 ms bounce, 4 ms at 0.9 ms; 53 ms at 50 WPM.

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-I1 | Yes | `renders_inspected: 7` equals the distinct renders cited |
| CK-ANA-I2 | No | finding-7 (and the plotted interval-13 case, finding-5) |

## J. Software assurance items (this reviewer's evidence for the assurance pair)

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-J1 | No accredited model | The relay model and the sequence model have no TV record. The note carries them as developer evidence, and the SA pair decides under SWE-070 7.1 task 1 whether that suffices for SW-TXSEQ values at PDR |
| CK-ANA-J2 | Partly | The SW-TXSEQ values (constant 10 ms lead-in, PA_EN never after TX_KEY, the end-of-over order, the fault path) agree with 07 section 14.2 rows b, c and h. Row j's key-up text conflicts with the constant lead-in, as the note itself reports. The 10 ms design value of row j is not used (finding-8) |
| CK-ANA-J3 | For the SA pair | `assurance_tasks_applied` is left to the SA record |

## Items N/A

CK-ANA-E6 (no TPM); G2 to G5 (not a budget, thermal, RF-exposure or cascade analysis).

## Independent checks (CK-ANA-B5)

1. **Must-operate ratio table (note section 4.2), by hand.**
   - Vpu(T) = 3.75 V x (1 + 0.00393 (T - 23)), divided by the coil voltage (4.45, 4.75, 6.05 and 6.35 V).
   - At 23/49/75/85 C: A 0.843 / 0.929 / 1.015 / 1.048; B 0.790 / 0.871 / 0.951 / 0.982; C 0.620 / 0.683 / 0.747 / 0.771; D 0.591 / 0.651 / 0.711 / 0.734.
   - All 16 agree within 0.001.
2. **D-5 hold table (section 4.3), by hand.** At 85 C: 76.4 mA (4.75 / 62.18 ohm), 48.1 mA, 40.5 mA (8.4 / 207.3), 24.1 mA (5.0 / 207.3). The ratios 1.02, 0.64, 1.80 and 1.07 agree.
3. **Schedule (K1 to K9), by hand.** 10.000; 9.980 to 10.043; 0.063; 13.043; 7.097; 1.903; 13.193 (1 + 0.0006 + 8.192 + 2 + 2); 11.443 and 12.193 (finding-5). All agree with `s4 result.json`.
4. **Separate harness over the note's model.** `rv_h1_tempco.py` and `rv_release_cold.py` import `relay_model.py` and the drive fits of s1 and add their own corners.
   - With the extra tempco set to 0, `rv_h1_tempco.py` reproduces the note's C and D corners exactly (C 85 C 6.77 ms nominal, 6.40 to 7.11 ms band; D 6.17 ms, 5.78 to 6.32 ms).
   - It then gives the finding-2 values.
   - `rv_release_cold.py` gives 13.79 to 14.10 ms at 85 C (the note's 12.92 ms at 5.0 V rises with the duty-rule average) and 22.60 to 23.04 ms at -10 C (finding-3).
5. **LTspice re-run.** The data sections are bit-identical to the author's (C4).

## Cross items for the lead SE (not findings on the note)

- X-1: The H1 maximum-coil-voltage read (finding-1) also bears on `thermal-ts012.md` design change 5 and on the OD-42 gate read. The H1's ambient rating is 70 C against a 67.1 C continuous bay, a 2.9 K margin inside the thermal note's band.
- X-2: The note's own finding that 07 section 14.2 row j conflicts with the constant lead-in stands; the reviewer confirmed the row j text at HEAD.

## Commands (reviewer, 2026-09-29)

```
cd /Users/robinonsay/rust/cwht
git rev-parse 95adefc:<path>; git rev-parse HEAD:<path>; git hash-object <path>     # R1, 18 paths
git archive 95adefc | tar -x -C <scratchpad>/rv23a-95adefc                           # export
mv <export>/hardware/sim/tx-seq/results <export>/hardware/sim/tx-seq/results-author   # author results aside
cd <export>; .venv/bin/python hardware/sim/tx-seq/seq_run.py all --expect            # exit 0, 47.5 s
cd <export>; .venv/bin/python hardware/sim/tx-seq/seq_run.py all                     # exit 1 (as stated)
diff -rq results-author/<run> results/<run>; cmp of every PNG                        # C4
cd <export>/hardware/sim/tx-seq; .venv/bin/python <scratchpad>/rv_h1_tempco.py 0.0|0.00087|(default 0.00117)
cd <export>/hardware/sim/tx-seq; .venv/bin/python <scratchpad>/rv_release_cold.py
pdftotext / pdftoppm -r 600 on en-g5v_2.pdf (K046-E1-06) page 2                       # datasheet reads
```

## Measurements (SWE-089)

size = 26 cases; inputs_checked = 18 rows against sources (39 inputs in the note); renders = 7; turns = 60; minutes = 75; major = 4; minor = 8.

## Iteration 2: delta verification of findings 1 to 4 (Major) (2026-09-29, HEAD `c0c3205`)

**Scope (rule C1).** Iteration 2 is a delta. It verifies the fixes of the four Major findings of iteration 1 and checks the text and runs those fixes added. Findings 5 to 12 (Minor) were left alone by the author (note section 13, "Minor findings of iteration 1 are not addressed in this revision (rule C1)"). They are not re-reviewed; their status at revision 1 is listed below for the lead SE. The two Major findings of the paired assurance record (INSP-123 findings 1 and 2: the hold PWM on TR_DRV, and the firmware-set coil parameters) are verified by the INSP-123 delta. This record reads K21 and K22 only as far as they are analysis results.

**Product and freeze (rule C2).** The 21 `product_files` above: note revision 1, the runner and the relay model, the expected states, the README, the two revision 1 decks, the `raw.sha256` manifest, the ICD-TX-SW CSV, the r1-s4 `result.json`, and the 11 cited plot paths (10 distinct images; the figure copy and the r1-s4 copy are both blob `2b0f7678`). The freeze is split across two commits. `8ca7d05` holds every revision 1 file except the r1-s4 copy of the timing diagram, which `fb120d2` adds. `product_commit` is therefore `fb120d2`. Every blob equals `git rev-parse fb120d2:<path>`, `git rev-parse HEAD:<path>` at HEAD `c0c3205` and `git hash-object` of the working tree (21 of 21). The four `scripts/` copies in the run folders equal the working `seq_run.py` and `relay_model.py` (`cmp`, 8 of 8). `git log fb120d2..HEAD` touches no product file. Both commits are on `main`.

**Independence (rule C4).** This invocation authored no part of WP-PDR-23a revision 0 or 1, no part of the iteration 1 review, and no part of INSP-123. It edited no product file.

**Search first (charter section 11 rule 1).** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any grep or find. Queries: "WP-PDR-23a sequencer timing review checklist record iteration"; "peer review record analysis-sequencer-timing independent review finding-1 H1 maximum coil voltage"; "feed drop pack to PA drain 0.26 to 0.45 ohm at 2 A key-down pack sag cell internal resistance". grep then pinned lines in known paths only. No rustos file was read.

**Reproduction (CK-ANA-C4).** `git archive fb120d2` was exported to the scratchpad (`rv23a-it2-fb120d2/`), and the committed results were copied aside first. Then `.venv/bin/python hardware/sim/tx-seq/seq_run.py all --expect` ran in the export: **exit 0**. All 15 checks pass (s1 `steps`, `mos_ron_range_mohm`, `q_vcesat_range_v`, `fit_resid`, `limiter_closed_form`; s2 `steps`, `closed_form`, `ripple`; s3 `calibration_ref_7ms`, `accepted_sets`, `nominal_accepted`, `model_vs_ltspice_rise`, `slope_law`; s4 `schedule_monotonic`, `upstream_checks`). All 40 verdicts equal the note's section 5. Comparison with the committed files:
- `result.md` of all four runs, `result.json` of r1-s3 and r1-s4, and the ICD CSV are byte-identical;
- all 10 PNGs are byte-identical, and so is the figure copy;
- r1-s1 and r1-s2 `result.json` differ only in the wrapper's out-dir path, one lock-wait line and the `.raw` hashes;
- the `.raw` files carry a `Date:` header, so their hashes change from run to run (iteration 1 C4 showed that the data sections are bit-identical);
- the kept working-tree `coil_tran.raw` (8,013,112 bytes) hashes to `f8f577f6...c3f67e9d`, the value in `raw.sha256` (CR-017 C2).

LTspice ran only through `tools/ltspice-batch.sh` (blob `88b71475`, the ACC-LTSPICE-001 blob). The `.log` first line reads `LTspice 26.0.2 for MacOS`.

**Datasheet re-read (CK-ANA-A4).** The Omron G5V-2 datasheet `en-g5v_2.pdf` (K046-E1-06) has SHA-256 `7a0edd8490dca7c983db239a794a4d26223e8d95c534689de0c6068c1fc9d55a`, equal to the note's. The text comes from `pdftotext -layout` pages 1 and 2. Page 2 was rendered at 600 dpi, the two G5V-2-H1 graphs were cropped, and the traces were read by pixel analysis: grid lines located, then the thick-trace centre found in each column.
- Ratings note 3 reads "The maximum voltage is the highest voltage that can be imposed on the relay coil". The graph note reads "The maximum coil voltage refers to the maximum value in a varying range of operating power voltage, not a continuous voltage". Both are quoted correctly in the note.
- "Ambient Temperature vs. Maximum Coil Voltage", H1 3 to 24 VDC: 180.0 % up to 54.0 C; 178.0 % at 55 C; 168.7 % at 60 C; **166.3 % at 61.4 C**; **156.1 % at 67.1 C**; 151.7 % at 69.5 C; the end at about 69.8 C and 151 %. The note has 166.6 % and 156.3 %, 0.3 points above this read. That is inside the read resolution. It changes no state: K19-CD fails by 1.7 points or more, and K19-E passes by 22.5 points.
- "Ambient Temperature vs. Must Operate or Must Release Voltage", H1, 10 samples: the "max" line reads 53.65 % at -10 C, 64.04 % at 23 C and 83.63 % at 85 C. That is 0.493 %/K relative to its 23 C value, and a ratio of 1.306 from 23 C to 85 C. The mean line gives 0.477 %/K and the min line 0.458 %/K. The note's band, 0.48 %/K to 0.5347 %/K from 23 C (ratios 1.2976 to 1.3315), covers the "max" line. Its steep end, the one the results use, is 2 % above this read, so it is conservative.

### Verification of finding-1, case by case (rule C7)

| # | Case (from the finding-1 fix) | Check | Result |
|---|---|---|---|
| 1 | Record the graph read and its resolution | Note section 2 row "(r1) G5V-2-H1 maximum coil voltage against ambient": knee 53.9 C, end 69.8 C at 151 %; 166.6 % at 61.4 C, 156.3 % at 67.1 C. The reviewer's read agrees within 0.3 points (above). Section 10 item 4 states the read and why it decides nothing | Yes |
| 2 | State whether the limit applies to the PWM average or the peak | Note section 2 row "(r1) Meaning of maximum voltage" and section 4.3: the limit applies to the imposed voltage at any instant, so to the PWM on-phase. That follows ratings note 3 and the graph note, quoted as the PDF text reads. It is the only reading the datasheet supports without the manufacturer | Yes |
| 3 | Make the capped pull-in (150 % or less) the recommendation | Option E (section 6.1): 6.3 V +/-2 % limiter, static TR_DRV, no pull-in phase. Hand check: 6.3 x 1.02 / 5.0 = 128.5 %, peak equal to average (no PWM), against 151 % at 70 C: +22.5 points (K19-E). The PWM capped at 150 % average is shown not to meet the limit on the peak reading (168 % on-phase at 8.4 V) | Yes |
| 4 | Restate K19 on the drive | K19 is split into K19-CD FAIL and K19-E PASS (r1-s4 `result.json`). The crossovers by hand: 151 % x 5 V = 7.55 V, 156.3 % gives 7.82 V, 166.6 % gives 8.33 V, as section 4.3 states. `s1-coil-voltage-vs-pack.png` draws both panels | Yes |
| 5 | Knock-on items of the new drive | Coil power at 85 C, -10 % unit: 6.43^2 / (150.03 x 1.2437) = 0.2216 W against the 0.225 W the corner assumes (hand; section 4.3). Limiter dissipation 0.11 W to WP-PDR-28 (section 6.1 item 7). The hold at the lowest key-down rail is not shown with the worst-case rail: finding-13 | finding-13 |

**Result: finding-1 Verified.** The graph is read, the peak-versus-average question is answered on the datasheet's own words, and the recommended drive is within the maximum at every bay ambient with 22.5 points to spare. The hold claim of the new drive is a separate defect: finding-13.

### Verification of finding-2, case by case

| # | Case | Check | Result |
|---|---|---|---|
| 1 | Use the H1 graph slope, or bound it | Band 0.48 %/K from 23 C to 0.51 %/K from 20 C (0.5347 %/K from 23 C), in `INPUTS` `s_mo_h1`. It covers the reviewer's "max"-line read of 0.493 %/K and iteration 1's 0.48 to 0.51 %/K, at both reference points. Each result takes the worse slope (section 3.3) | Yes |
| 2 | The model law | `relay_model.py` `k_mo`, `force_scale`, `i_pickup`: the spring force scales by (k_mo / k_cu)^2, so the must-operate and must-release currents move together. With the copper case the law reduces exactly to revision 0. The `slope_law` check passes in the re-run | Yes |
| 3 | Operate times at 85 C | C 8.36 ms, D 7.13 ms, E 7.89 ms (band maxima, both slopes; re-run identical). Iteration 1's harness gave C 8.00 to 8.40 ms and D 6.91 to 7.16 ms. The author's check run from 20 C (C 8.02 to 8.36 ms, D 6.92 to 7.13 ms) agrees within 0.05 ms | Yes |
| 4 | The hold guarantee | K15-D by hand: 5.0 / (3.75 x 1.3315) = 1.0014 and 5.0 / (3.75 x 1.2976) = 1.0275, as stated. The fix asked for a stated margin over the read uncertainty; the note answers it with option E instead (K15-E 1.051 to 1.079). That answer rests on the rail floor of finding-13 | finding-13 |
| 5 | KD-12, BM-1, BM-2 restated | KD-12 3.826 to 8.388 ms (7.888 + 0.5 bounce), BM-1 "at most 5.0 V at the hot coil", BM-2 at 6.15 V with an 85 C coil, acceptance at most 8.5 ms (model worst 8.39 ms), and the re-anchor rule above 8.5 ms. The 6.05 V pull-in corner of finding-13 moves KD-12 to 8.86 ms | Yes, with finding-13 |

**Result: finding-2 Verified.** The slope comes from the graph, is bounded on the conservative side, and is carried into operate, hold and release. The restated KD-12 and BM-2 follow from it. The remaining hold question belongs to finding-13.

### Verification of finding-3, case by case

| # | Case | Check | Result |
|---|---|---|---|
| 1 | Release over the coil range, both pack ends, the duty-rule hold | s3 `REL_TEMPS` (-10, 23, 85 C) and `_release_holds`: A and B full and 63 %; C and D the key-down 5.0 V, the end-of-over 5.60 V (8.4 V pack) and 5.83 V (6.35 V), and the full pack; E 6.15 and 6.43 V. `s3-release.png` draws the 24 hold and temperature pairs | Yes |
| 2 | Worst case into K12, KU-07 and BM-3 | K12-A 21.63 ms, K12-D 24.78 ms, K12-E 25.86 ms, all at -10 C, against the 30 ms share. KU-07 maximum 25.86 ms (option E); BM-3 at the 6.43 V corner, acceptance 29.0 ms | Yes |
| 3 | Agreement with the iteration 1 check | Iteration 1 (copper law): 22.60 to 23.04 ms band maximum at -10 C, so 23.6 to 24.0 ms with ordering and bounce. Revision 1 with the graph slope: 23.35 to 23.78 ms, so 24.78 ms. The slope lowers the cold must-release current, so the cold release is slower, in the direction expected | Yes |
| 4 | Options A and B given the same treatment | K12-A at -10, 23 and 85 C from 4.75 V and from the 63 % hold | Yes |

**Result: finding-3 Verified.** The cold corner is analysed, and the worst case (-10 C, highest hold) is carried to K12, KU-07 and BM-3. Option E keeps 4.14 ms of the 30 ms share.

### Verification of finding-4, case by case

| # | Case | Check | Result |
|---|---|---|---|
| 1 | Add the case with its criterion and timing-table rows | Section 4.8, K20-a, K20-b, K20-c, rows SR-01 to SR-04, `s4-stale-ratio.png`, s4 `stale_ratio_case` | Yes |
| 2 | Choose the outcome and show its effect on K2, K2b and K3 | Outcome (b), elements not radiated, with the reason (REQ-SYS-161, SRR decision 47). K2 and K2b hold for every radiated element (9.980 to 10.043 ms). K3 cannot hold in the window, and K20-c goes to the owner. Hand checks: 82.8 + 10.043 = 92.84 ms for outcome (a). At 50 WPM, elements start at 0 and 48 ms inside 82.8 ms, so 2 are not radiated; at 25 WPM (96 ms period), 1 | Yes |
| 3 | The SW-TXSEQ rule and its cases | Section 4.8 firmware rule on the ratio age (no changeover while the ratio is older than A_kd and a refresh runs), HostUnit cases at ratio ages 10.1 s and 9.9 s, and the no-FC0-conflict argument, which agrees with `frequency-budget.md` revision 4 lines 385 to 390 | Yes |
| 4 | The owner route | Section 7 condition (2) of REQ-SYS-160. Its trigger, "after an over longer than 10 s", leaves out the ratio's age when the over started (up to 1.083 s) and is ambiguous about the hang | finding-14 |

**Result: finding-4 Verified.** The case is in the analysis, settled, and carried to the table and the firmware rule. The text of the condition that goes to the owner has the wrong trigger: finding-14.

### Per-case results (iteration 2; the cases the delta touches)

| Case | Condition | Governing id and limit | Result (checker) | Margin | Uncertainty | Reviewer re-check | Finding ids |
|---|---|---|---|---|---|---|---|
| D-1 | C and D, voltage imposed at 8.4 V; bay air 61.4, 67.1, 70 C | H1 maximum coil voltage (ratings note 3, graph) | 168 % against 166.6, 156.3, 151 % (K19-CD FAIL) | -1.4, -11.7, -17 points | +/-0.3 points (read) | pixel read 166.3, 156.1, about 151 % | none |
| D-2 | E, limiter high corner, any pack | same, 151 % at 70 C | 128.5 % (K19-E) | +22.5 points | read | hand 6.426 / 5.0 | none |
| D-3 | C, 6.35 V, 85 C coil, worst unit | operate at most 9.5 ms | 8.36 ms (K1b-C) | +1.14 ms | model band, slope band | re-run identical | none |
| D-4 | D, same | 9.5 ms | 7.13 ms (K1b-D) | +2.37 ms | as D-3 | re-run identical | none |
| D-5 | E, 6.15 V, 85 C coil | operate + 0.5 ms at most 10 ms | 8.39 ms (K1b-E) | +1.61 ms (note: 1.11) | as D-3 | re-run; at 6.05 V the frozen model gives 8.86 ms, +1.14 ms | finding-13, finding-15 |
| D-6 | C and D hold, 5.0 V average, 85 C coil | hold at least the worst unit's must-operate | 1.001 to 1.028 x (K15-D) | +0.1 to +2.8 % | slope band | hand 1.0014, 1.0275 | none |
| D-7 | E hold, lowest key-down coil voltage, 85 C coil | same | 1.051 to 1.079 x at 5.25 V (K15-E) | +5.1 to +7.9 % as stated | rail floor not bounded | `rv_k15e_rail.py`: 0.995 to 1.021 x at 4.97 V (REQ-SYS-097 tolerance, WP-PDR-21 r3 feed); 1.024 to 1.049 x at the coil's own 78 C | finding-13 |
| D-8 | A and B release, -10 C | REQ-SYS-036 share 30 ms | 21.63 ms (K12-A) | +8.37 ms | model band | re-run identical | none |
| D-9 | C and D release, -10 C, 5.83 V end-of-over hold | 30 ms | 24.78 ms (K12-D) | +5.22 ms | model band | agrees with iteration 1 (24.0 ms, copper law) in the expected direction | none |
| D-10 | E release, -10 C, 6.43 V | 30 ms | 25.86 ms (K12-E) | +4.14 ms | model band | re-run identical; plot bar 24.86 ms plus 1.0 ms | none |
| D-11 | stale ratio, outcome (b), radiated elements | REQ-SYS-161 12 ms, equal within 0.5 ms | 9.980 to 10.043 ms (K20-b) | +1.957 ms | as iteration 1 C-2 | hand | none |
| D-12 | stale ratio, outcome (a), first element | REQ-SYS-161 | 92.84 ms (K20-a FAIL, rejected) | -80.84 ms | none | hand 82.8 + 10.043 | none |
| D-13 | stale ratio, straight-key closure in the window | REQ-SYS-160 15 ms | not met (K20-c FAIL, to the owner) | not applicable | trigger threshold | ratio age = over + up to 1.083 s | finding-14 |
| D-14 | E, TR_DRV as the backstop sees it | K21: static level; T_rearm longer than the release | 2 edges per over; 30 ms against 25.86 ms (K21-E) | +4.14 ms | model band | hand | finding-16 |
| D-15 | E coil power, 85 C, -10 % unit, 6.43 V | 0.225 W the 85 C corner assumes | 0.221 W | +0.004 W | thermal band | hand 0.2216 W | none |

### New findings of iteration 2

- **finding-13 (Major, Open).** Option E's key-down hold, K15-E. See the findings table. The reviewer check is `rv_k15e_rail.py`, run in the export's `hardware/sim/tx-seq/` folder. It imports the frozen `relay_model.py` and `seq_run.py` and reads the r1-s1 drop fits. Results:

  | Rail basis | Rail | Coil | Coil temperature | Hold / must-operate (steep, shallow) |
  |---|---|---|---|---|
  | note: 6.4 V, 0.05 V receive and 0.9 V key-down drop | 5.450 V | 5.250 V | 85 C | 1.051, 1.079 |
  | REQ-SYS-097 low tolerance, 6.30 V | 5.350 V | 5.150 V | 85 C | 1.031, 1.058 |
  | and the WP-PDR-21 r3 feed bound, 0.565 ohm x 2.0 A | 5.170 V | 4.970 V | 85 C | **0.995**, 1.021 |
  | the same, coil at its own temperature | 5.170 V | 4.970 V | 77.9 C | 1.024, 1.049 |
  | and 0.1 V of cell discharge during the over | 5.070 V | 4.870 V | 77.5 C | 1.006, 1.029 |

  Option E operate time at an 85 C coil, over the 13 accepted sets and both slopes: 7.89 ms at 6.15 V, reproducing the note, and **8.36 ms at 6.05 V** (8.86 ms with bounce). The plot `rv_k15e_rail.png` was opened after rendering. It shows the hold ratio against the pack voltage at the start of the over for both feed bases and both slope ends, and the self-heated case. It marks the 1.00 line, the REQ-SYS-097 6.30 V and 6.40 V points, and the note's 1.051 point, which lies on the note-method line.
- **finding-14 (Major, Open).** The stale-ratio condition for REQ-SYS-160 states the wrong trigger. See the table.
- **finding-15 (Minor, Open).** The option E operate margin is stated as 1.11 ms against 1.61 ms by the note's own criterion.
- **finding-16 (Minor, Open).** The reason given for the 30 ms re-arm qualification in section 4.9 is wrong.

### Iteration 1 Minor findings at revision 1 (not re-reviewed; for the lead SE)

| Finding | Status seen at `fb120d2` |
|---|---|
| finding-5 | Unchanged: `s4-keydown-budget.png` is the same blob (`17aa3f02`) and section 4.6 is unchanged |
| finding-6 | In part: the header and section 12 now pin `frequency-budget.md` revision 4 (`d030ce2`) and `pa-permit-gate-d18.md` revision 1 (`c397ab1`). `thermal-ts012.md` is still cited with no revision or review state (section 2 row "Coil temperature corners", section 12). M-1 ladder (c) is still not carried |
| finding-7 | Unchanged. In `timing-diagram.png` panel (a) the annotation box still hides the envelope trace from about 17 ms. In `s2-coil-transient.png` the dashed lines of panels 2 and 3 are still unlabelled; they are the 23 C must-operate currents (0.75 x 5 V / R23, `seq_run.py` line 619), not the 85 C values with the slope. `s4-margins.png` is the same blob |
| finding-8 | Unchanged (K16 against 20 ms only) |
| finding-9 | Unchanged (re-key during the end of the over or the release; see also finding-16) |
| finding-10 | Affects option A only; the 2N3904 is no longer recommended (section 6.1 item 3) |
| finding-11 | Overtaken: option E has no PWM, and section 6.2 row WP-PDR-20b withdraws the 25 kHz line. The lead SE may close it on re-reading |
| finding-12 | Unchanged (section 6.2 row WP-PDR-23b does not pass the H1 contact differences) |

### Checklist items at iteration 2 (the items the delta bears on)

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-A1 | Yes | Section 1 table adds REQ-SYS-180, HZ-004 K12, HZ-014 K8 and the K20 rows; each id exists |
| CK-ANA-A4 | No | The datasheet reads are right (above). The two rail inputs that set K15-E, and the pull-in corner, are not the worst case their sources allow (finding-13) |
| CK-ANA-A5 | No | The option E limiter behaviour, the coil corners and the slope application are stated with direction. The T_rearm reasoning is wrong (finding-16). The stale-ratio trigger leaves out the starting ratio age (finding-14) |
| CK-ANA-A6 | Yes for the delta | Commit `8ca7d05` changes only `docs/design/analysis/sequencer-timing.md`, `hardware/sim/tx-seq/` and the figure (`git show --stat`). Every consequence goes out as a request (section 6.2: WP-PDR-16, 20a, 20b, 22, 26, 32, 35, 37, 38, 23b, 43, 54). Finding-12 remains |
| CK-ANA-B3 | Yes | The H1 temperature law is now validated against its own graph (finding-2 case 1) |
| CK-ANA-B5 | Yes | Independent checks: the two datasheet graphs by pixel analysis; K19 crossovers, K15-D and K15-E ratios, coil power, the stale-ratio counts and lead-in by hand; a separate harness over the frozen model for the 6.05 V operate time and the rail cases (finding-13) |
| CK-ANA-C4 | Yes | Re-run from the `fb120d2` export, exit 0, outputs identical (above) |
| CK-ANA-D2 | No | Note, `result.json`, CSV and plots agree at every point checked except the 1.11 ms statement (finding-15) and the plotted interval-13 case of iteration 1 (finding-5) |
| CK-ANA-E3 | No | K15-E's stated margin does not cover the rail floor (finding-13). Every other delta margin exceeds its stated uncertainty |
| CK-ANA-E4 | Yes | 15 checks asserted (exit 2 on failure), 40 criteria (exit 1 on FAIL or OPEN), `--expect` against `expected_states.json` (exit 3 on a change); observed exit 0 with `--expect` |
| CK-ANA-E5 | No | REQ-SYS-161 12 ms is supported. The REQ-SYS-160 condition (2) states the wrong trigger (finding-14) |
| CK-ANA-F1 | Yes for findings 3 and 4 | REQ-SYS-036 at -10, 23 and 85 C, and the R-FRESH-2 case, are in the per-case table |
| CK-ANA-F3 | No | The worst combination for the option E hold (lowest start voltage within the REQ-SYS-097 tolerance, hot feed, discharge during the over) is not analysed (finding-13) |
| CK-ANA-G6-4 | Yes for the delta | K21-E and the option E failure-mode table name HZ-004 K12, HZ-014 K8, HZ-008 C5 and C6, and REQ-SYS-156. Finding-8 remains |
| CK-ANA-H1 | Yes | The option E failure modes go to WP-PDR-16 as requests; `hazards.json` is not edited |
| CK-ANA-H3 | Yes | Change history row for revision 1, with section 13 mapping each finding to its fix |
| CK-ANA-I1 | Yes | 10 distinct renders opened (below); `renders_inspected: 10` |
| CK-ANA-I2 | No | Finding-7 remains (the three iteration 1 plot defects). The new plots have labelled axes, limits and legends. The author's own note on `s1-coil-current.png` holds: the right panel's legend runs past the axes but stays readable |

### Visual closure (iteration 2)

Opened with the Read tool after the re-run (10 distinct renders, all byte-identical to the committed files):
- `s1-coil-voltage-vs-pack.png`: panel (a) C and D on-phase line from 100 % at 5 V to 172 % at 8.6 V, crossing 151 % at about 7.55 V. E flat at 126 % (nominal set point) above 6.5 V, with its +/-2 % band. The three maximum lines at 167, 156 and 151 %. Panel (b) the graph curve against ambient, C and D at 168 %, E at 128.5 %, markers at 61.4, 67.1 and 70 C. Agrees with section 4.3;
- `s1-coil-current.png`: H1 at 6.35 V about 27.8 mA against the 21.9 mA must-operate line (slope 0.53 %/K); standard coil 68.2 mA line. Agrees with section 3.2;
- `s2-coil-transient.png`: E_rise_hot settles at about 27 mA; E_dc_cold at about 49 mA, decaying after 66 ms. Finding-7 applies to the dashed lines;
- `s3-operate-vs-coil-temperature.png`: panel (b) at 85 C, C band to about 8.4 ms, E to about 7.9 ms, D to about 7.1 ms, under the 9.5 ms line. Agrees with section 4.2;
- `s3-release.png`: E e_max at -10 C, band bar 24.86 ms; C and D full at -10 C about 27.8 ms (not a design hold); the 29 ms line. Agrees with section 4.4;
- `s3-limiter-setpoint.png`: operate + bounce 10.04 ms at a 6.0 V set point and 8.39 ms from 6.3 V. Release at -10 C 25.86 ms at 6.3 V. The hold flat at 1.051 whatever the set point, which shows it depends only on the rail and the dropout (finding-13). Highest coil voltage 128.5 % at 6.3 V; coil power 98 % of 0.225 W;
- `timing-diagram.png` (and the figure copy): panel (a) PA_EN at 10.5 ms, TX_KEY at 11 ms, ramp at 13 ms after the contact; E band ending at t0 + 8.39 ms; option B tick at t0 + 10.15 ms. Panel (b) the T/R drive as one level from t0 to the hang expiry, release band after t_h, REQ-SYS-036 at t_h + 50 ms. Finding-7's annotation box remains;
- `s4-keydown-budget.png`, `s4-margins.png`: unchanged blobs, as read at iteration 1;
- `s4-stale-ratio.png`: panel (a) 82.8 ms refresh, two dits sounded but not radiated, T/R drive at about 97 ms, ramp at t0 + 10 ms. Panel (b) outcome (a) falling from 92.8 ms to the 12 and 15 ms limits near 80 ms; outcome (b) flat at 10.04 ms. Agrees with section 4.8. The axis label "an over longer than 10 s" is part of finding-14.

The reviewer's own plot `rv_k15e_rail.png` (scratchpad) was opened as well (finding-13).

### Cross items (iteration 2, returned to Claude)

- X-3. Iteration 1 of this record is not yet filed on main. This text is the complete record at iteration 2: the iteration 1 body is kept unchanged except for the finding states and the new finding rows. INSP-123 cross item X-2 (pairing fields, SA-A3 and SA-A4) applies when it is filed.
- X-4. Iteration 2 closes with two Major findings open, so the next delta is iteration 3, the last before escalation to the owner (rule C1; 07 section 10.2). Both fixes are small (a restated rail floor with a K15-E result, and a restated condition text), and neither changes the schedule results.
- X-5. WP-PDR-21 revision 3 bounds the drain feed at 0.53 to 0.61 ohm in the key-down cases (`by_tc.*.feed_ohm.bound`). That is above the 0.26 to 0.45 ohm of TS-012 that other records still carry, for example `frequency-budget.md` FR-3 (r_feed 0.26 to 0.45 ohm) and `thermal-ts012.md`. The lead SE may want the users of that input re-checked. It is not a finding on this note, except where finding-13 uses it.
- X-6. The freeze of revision 1 is split across `8ca7d05` and `fb120d2`. The reviewer brief named neither commit. This record uses `fb120d2`, at which every product blob is present.
- X-7. Rule C10 and iteration 1 C2 still hold: the values rest on developer evidence (no TV record for `seq_run.py` or `relay_model.py`).

### Completion criteria (SWE-088), iteration 2

Not met on the reviewer side: two Major findings are open (13 and 14). R1 to R6 hold at `fb120d2`:
- R1: 21 blobs frozen;
- R2: one command, exit 0 with `--expect`;
- R3: `expected_states.json` has no schema. `tools/validate_docs.py` on a `git archive HEAD` (`c0c3205`) export with this record placed at its path: exit 0, 122 passed, the record PASS against the built-in peer-review record schema;
- R4: the author return and note section 13;
- R5: no `TBD`;
- R6: every cited render is beside its run.

`reviewer_verdict: NEEDS CHANGES`. The record `verdict` is held at NEEDS CHANGES.

```
ITERATION 2 (2026-09-29, HEAD c0c3205, product commit fb120d2; freeze 8ca7d05 + fb120d2): REVIEWER VERDICT: NEEDS CHANGES
PRODUCT: docs/design/analysis/sequencer-timing.md@e4c9ad92 (revision 1), seq_run.py@fbcad585, relay_model.py@0285c9c9, runs 2026-09-29-r1-s1 to r1-s4 (21 blobs) at fb120d2
FINDINGS:
- [Major] finding-1: Verified (H1 maximum-voltage graph read and applied to the imposed peak; option E 128.5 % against 151 % at 70 C).
- [Major] finding-2: Verified (H1 slope band 0.48 to 0.535 %/K covers the graph's max line, 0.493 %/K; carried into operate, hold, release, KD-12, BM-2).
- [Major] finding-3: Verified (release at -10, 23, 85 C from every hold; K12-E 25.86 ms, margin 4.14 ms).
- [Major] finding-4: Verified (R-FRESH-2 case added; outcome (b); K20-a/b/c; SR-01 to SR-04).
- [Major] finding-13 (new): K15-E rests on a 5.45 V key-down rail. With the REQ-SYS-097 tolerance (6.30 V start) and the WP-PDR-21 r3 feed bound (0.565 ohm at +45 C key-down) the coil sees 4.97 V and the hold is 0.995 to 1.021 x at 85 C. Not shown to pass; the pull-in corner moves to 6.05 V (8.86 ms with bounce).
- [Major] finding-14 (new): REQ-SYS-160 condition (2) says "after an over longer than 10 s"; the trigger is ratio age over 10 s, so an over of about 8.9 s or more.
- [Minor] finding-15 (new): option E operate margin 1.11 ms stated, 1.61 ms by the K1b-E criterion (bounce subtracted twice).
- [Minor] finding-16 (new): the reason given for T_rearm is wrong; a re-key within 30 ms of the hang expiry keeps the backstop count running.
- [Minor] findings 5 to 12: Open, not in the delta (finding-11 overtaken by option E).
ITEMS N/A: CK-ANA-E6; G2 to G5.
VALUES PROPOSED: REQ-SYS-161: 12 ms (supported); REQ-SYS-160: 15 ms with conditions (1) bounce 1.957 ms (supported) and (2) the stale-ratio case (not supported as worded, finding-14).
MEASUREMENTS: blobs equal HEAD 21/21; checks 15 PASS, --expect exit 0; outputs byte-identical (result.md 4/4, PNG 10/10, CSV 1/1); delta cases 15; renders inspected 10; major open=2; minor open=10; turns=62; minutes=85 (cumulative 122 and 160); iteration=2
```

### Commands (reviewer, iteration 2)

```
cd /Users/robinonsay/rust/cwht
git rev-parse fb120d2:<path>; git rev-parse HEAD:<path>; git hash-object <path>          # R1, 21 paths
git archive fb120d2 | tar -x -C <scratchpad>/rv23a-it2-fb120d2                            # export
cp -R <export>/hardware/sim/tx-seq/results <scratchpad>/rv23a-it2-ref/results             # committed results aside
cd <export>; .venv/bin/python hardware/sim/tx-seq/seq_run.py all --expect                 # exit 0
diff / cmp of result.md, result.json, CSV and every PNG against rv23a-it2-ref             # C4
shasum -a 256 hardware/sim/tx-seq/results/2026-09-29-r1-s2-coil/coil_tran.raw             # equals raw.sha256
shasum -a 256 en-g5v_2.pdf; pdftotext -layout -f 1 -l 2; pdftoppm -f 2 -l 2 -r 600       # datasheet
cd <export>/hardware/sim/tx-seq; .venv/bin/python <scratchpad>/rv23a-it2/rv_k15e_rail.py <png>   # finding-13
```

### Measurements (SWE-089), iteration 2

size = 15 delta cases; inputs_checked = 8 (the two graph reads, ratings note 3, the graph note, REQ-SYS-097, the WP-PDR-21 r3 feed bound, the `frequency-budget.md` receive ratio age, the TS-012 feed budget); renders = 10; turns = 62; minutes = 85; major = 2 new (6 in total); minor = 2 new (10 in total).

## Iteration 3: delta verification of findings 13 and 14 (Major) (2026-09-29, HEAD `249356b`)

**Scope (rule C1).** Iteration 3 is a delta. It verifies the fixes of the two Major findings of iteration 2 (finding-13, the option E key-down rail floor behind K15-E; finding-14, the trigger of the REQ-SYS-160 stale-ratio condition) and checks the text and runs those fixes added. The Minor findings 5 to 12, 15 and 16 were left alone by the author (note section 14, "Minor findings are not addressed (rule C1)"); their status at revision 2 is listed below for the lead SE. This is the third author-review iteration on WP-PDR-23a: with NEEDS CHANGES the next step is escalation to the owner (rule C1; 07 section 10.2), not a fourth iteration.

**Product and freeze (rule C2).** The 23 `product_files` above: note revision 2, the runner and the relay model, the expected states, the README, the two revision 2 decks, the r2-s2 `raw.sha256`, the ICD-TX-SW CSV, the r2-s3 and r2-s4 `result.json`, and the 12 cited plot paths (11 distinct images; the figure copy and the r2-s4 copy are both blob `49db873d`). Every blob equals `git rev-parse 249356b:<path>`, `git rev-parse HEAD:<path>` at HEAD `249356b` and `git hash-object` of the working tree (23 of 23). The four `scripts/` copies in the r2 run folders equal the working `seq_run.py` and `relay_model.py` (`cmp`, 8 of 8). `249356b` is on `main`. `tools/check_commit_msg.py --range 249356b~1..249356b`: PASS.

**Independence (rule C4).** This invocation authored no part of WP-PDR-23a revisions 0 to 2, no part of iterations 1 and 2 of this record, and no part of INSP-123. It edited no product file. Iterations 1 and 2 of this record are not yet filed on main; this text is built on the iteration 2 record as returned to the lead SE (scratchpad `rv23a-it2/analysis-sequencer-timing.md`), whose body is kept unchanged except for the finding states and the new rows.

**Search first (charter section 11 rule 1).** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any grep or find. Queries: "WP-PDR-23a review checklist record iteration K15-E key-down hold coil supply dropout"; "battery under-voltage during transmission cutoff cell voltage key-down end transmit REQ-SYS-097 REQ-SYS-098"; "P28A cell voltage sag during key-down over discharge curve end of discharge 3.15 V per cell transmit". grep then pinned lines in known paths only. No rustos file was read.

**Reproduction (CK-ANA-C4).** `git archive 249356b` was exported to the scratchpad (`rv23a-it3-249356b/`), and the committed results were copied aside first (`rv23a-it3-ref/`). The WP-PDR-21 p4 `.raw` (20,405,166 bytes, not committed under CR-017 C2) was copied into the export from the main working tree; its SHA-256 `886371f6...83a57306` equals its committed `raw.sha256`. Then `.venv/bin/python hardware/sim/tx-seq/seq_run.py all --expect` ran in the export: **exit 0** in 46.7 s. All 17 checks pass (the 15 of iteration 2 plus s3 `hold_ratio_closed_form` and s4 `p4_feed_current`, which re-derived 2.1403, 2.2151 and 2.2335 A from the `.raw`). All 40 verdicts equal the note's section 5 (K15-E OPEN). Comparison with the committed files:
- `result.md` of all four r2 runs, `result.json` of r2-s3 and r2-s4, `runs.json`, the ICD CSV and Markdown: byte-identical;
- all 11 PNGs and the figure copy: byte-identical;
- r2-s1 and r2-s2 `result.json` differ only in the wrapper's out-dir path, the elapsed seconds and the `.raw` hashes. The `.raw` files carry a `Date:` header; after the header the data sections of `drive_dc.raw` and `coil_tran.raw` are bit-identical to the committed and kept files;
- the kept working-tree r2-s2 `coil_tran.raw` (8,010,152 bytes) hashes to `49905b7b...88dd73ff`, the value in its `raw.sha256` (CR-017 C2).
A second run of `seq_run.py s4 --expect` with the p4 `.raw` removed from the export also exits 0: `p4_feed_current` reports PASS with the note "p4 .raw not present: inputs used as recorded, not re-derived" (finding-18). LTspice ran only through `tools/ltspice-batch.sh` (blob `88b71475`, the ACC-LTSPICE-001 blob); the `.log` first line reads `LTspice 26.0.2 for MacOS`.

**Inputs checked against their sources (CK-ANA-A4).**

| # | Input (note section 2) | Source read | Result |
|---|---|---|---|
| 1 | Pack at the start of a transmission, 6.30 V | REQ-SYS-097 at HEAD: "refuse to start a transmission while either cell, measured in receive, reads below 3.20 V +/-0.05 V (TBR)"; both cells at 3.15 V may start one | agrees |
| 2 | Feed bound 0.5646 ohm (+45 C key-down), 0.614 ohm (-10 C), 0.3841 ohm (lever) | `hardware/sim/tx-pa/results/2026-09-29-r3-p4-power-a5-design/result.json` `by_tc.hot45a.feed_ohm` bound 0.564648 and lever 0.384144, `by_tc.cold0.feed_ohm.bound` 0.613955; `pa-drive-ts012.md` revision 3 section R3.5 ("0.614 ohm at -10 C and 0.565 ohm at +45 C") | agrees |
| 3 | Key-down pack current 2.140, 2.215, 2.233 A at 6.4 V | reviewer's own read of the p4 `.raw` with spicelib (separate code from the note's check): 1728 corners at the +45 C bound, largest 2.1403 A, drop 1.2085 V; 432 corners at the -10 C bound, 2.2151 A, 1.3600 V; 1728 lever corners, 2.2335 A, 0.8580 V | agrees |
| 4 | "Taken at 6.30 V too: the current falls with the pack" | p4 deck: the D-9 VGG top `vggof` is flat at 3.50 V from 6.4 to 7.1 V and capped at 3.50 V below 6.4 V. On the largest-current corner the pack current rises from 2.140 A at 6.4 V to 2.296 A at 7.15 V at that fixed VGG, then falls to 1.993 A at 8.4 V as the clamp lowers VGG. So below 6.4 V, at the capped VGG, the current falls with the pack | agrees (the rail is higher at every pack above 6.4 V) |
| 5 | Receive ratio age at most 1.083 s | `frequency-budget.md` revision 4 line 382 (FR-2r): "never older than 1.083 s: the 1 s refresh plus the 50 ms stage settle and the 32.768 ms interval-15 count" | agrees |
| 6 | No G5V-2-H1 coil below 5 VDC | Omron G5V-2 datasheet K046-E1-06, SHA-256 `7a0edd84...fc9d55a` (equal to the note's), Ordering Information: G5V-2-H1 in 5, 12, 24 and 48 VDC | agrees |
| 7 | Pack fall during an over, 0.10 V (class E) | Source given: "review finding-13 figure". The iteration 2 record used 0.1 V as an illustration and said the note "bounds no discharge during an over of up to 180 s"; it is not a source. The design's own in-over bound is REQ-SYS-098 at HEAD: "power down its loads when either cell reads below 3.00 V +/-0.05 V (TBR)", with no receive qualifier, so a cell may read 2.95 V under key-down load. Cell resistance: `pa-drive-ts012.md` revision 3 input table and `run_pa.py` `FEED_CELLS` (two P28A, 0.04 to 0.06 ohm at 25 C, x1.00 at the +45 C bound, x3.3 at the -10 C bound) | **no source; the in-over bound the design states is lower (finding-13, iteration 3)** |
| 8 | Receive current 0.111 A plus the coil's 0.035 A at pull-in (class E) | unchanged revision 1 basis; the pull-in floor uses the larger feed bound (0.614 ohm), which is conservative | agrees as an estimate |

### Verification of finding-13, case by case (rule C7)

| # | Case (from the finding-13 fix) | Check | Result |
|---|---|---|---|
| 1 | Take the start of the over from the REQ-SYS-097 tolerance | 6.30 V (section 2, `v_pack_floor`) | Yes |
| 2 | Take the WP-PDR-21 revision 3 feed bound at the key-down corner that sets the coil temperature | +45 C, 0.5646 ohm, with the modelled current 2.140 A (above the 2.0 A iteration 2 used). Hand: 6.30 - 2.140 x 0.5646 = 5.0918 V at the start of the over | Yes |
| 3 | Take "a stated bound on the cell voltage during an over (or the design's in-over under-voltage end)" | The note carries 0.10 V, class E, sourced to the iteration 2 record's illustration. Its own `s3-keydown-hold.png` panel (b) runs to 0.30 V, but every stated result and acceptance uses 0.10 V. With the design's in-over end, REQ-SYS-098 (a cell may read 2.95 V under load), the lowest rail is 2 x 2.95 V less 2.140 A through the feed without the cells (0.5646 - 0.060 = 0.5046 ohm): **4.820 V**, coil **4.720 V**, hold **0.945 to 0.970 x** at an 85 C coil (reviewer check `rv_k15e_it3.py`, plot `rv_k15e_it3.png`). That is a pack fall of 0.272 V below its receive reading, against the 0.10 V carried. If the cell reading is taken on the board side of the holder contacts (0.04 ohm at the bound), the coil sees 4.81 V (0.963 x); either way it is below the note's 4.89 V | **No** |
| 4 | One of (i) show K15-E at least 1.0, (ii) tighten the dropout, (iii) state K15-E OPEN with BM-1 restated | (ii) and (iii) taken: dropout 0.10 V at 60 mA over -10 to 85 C; K15-E OPEN in section 5, `expected_states.json` and the Summary. The state is right at either floor | Yes |
| 5 | BM-1's acceptance restated | BM-1: must-operate at the hot coil "at most 4.89 V". At the REQ-SYS-098 end the coil sees 4.72 V, so a fitted unit that passes BM-1 at 4.80 V would not hold at the lowest rail the design allows while transmitting. The acceptance follows case 3 | **No** |
| 6 | Closing path (i), the WP-PDR-21 P-FET lever | Note: 1.050 to 1.077 x at 0.10 V. At the REQ-SYS-098 end: rail 5.90 - 2.233 x (0.3841 - 0.060) = 5.176 V, coil 5.076 V, **1.017 to 1.043 x**. The lever still closes K15-E, with 1.7 % at the steep end, not 5.0 % | Route valid; figure overstated |
| 7 | Carry the pull-in corner into K1b-E, KD-12 and BM-2 | 6.11 V = 6.30 - 0.146 A x 0.614 ohm - 0.10 V (hand 6.1104 V; the set point's low corner 6.174 V is higher). Operate 8.07 ms, 8.57 ms with bounce (re-run identical). The iteration 2 harness gave 7.89 ms at 6.15 V and 8.36 ms at 6.05 V on the same model; linear interpolation at 6.11 V gives 8.08 ms. K1b-E PASS with 1.43 ms; KD-12 3.826 to 8.567 ms; BM-2 at 6.11 V, at most 8.7 ms. The pull-in happens in receive at the start of the over, so the in-over bound of case 3 does not act on it | Yes |
| 8 | Restate BM-6 | 4.99, 6.21 and 8.4 V points; acceptance at least 4.89 V at 4.99 V tests the 0.10 V dropout, which is right as a part test. Its 4.99 V point follows case 3 only as a label | Yes |
| 9 | K22-E no longer quotes the hold ratio | Section 4.9 and K22-E row: "the hold's hardware margin is K15-E" | Yes |
| 10 | The coil's own temperature (iteration 2 remark) | Hand: 6.24 V all the time, -10 % unit (150.0 ohm at 23 C), 80 K/W, 67.1 C air: 83.86 C, 0.984 x at 4.89 V; nominal unit at 4.89 V: 76.6 C, 1.014 x. The note keeps the 85 C corner, which is conservative | Yes |
| 11 | A lower-voltage H1 coil | None: the ordering table lists 5, 12, 24, 48 VDC (input 6) | Yes |

Hand checks of the note's own figures (all agree): rail 4.9918 V and coil 4.8918 V after the 0.10 V; worst must-operate at 85 C 4.9932 V (steep, 0.75 x 5 V x (1 + 0.005347 x 62)) and 4.8660 V (shallow); ratios 0.9797 and 1.0053 (start of the over 0.9997 and 1.0258); lever 1.0499 and 1.0773; -10 C 1.5019 to 1.5348. The note prints the first as 0.980, which rounds away from the conservative side (finding-17).

**Finding-13 at iteration 3: Open (Major).** Cases 1, 2, 4, 7, 8, 9, 10 and 11 are fixed. Case 3, the third input the fix named, is not: the pack fall during an over has no source, and the bound the design itself states (REQ-SYS-098) is 0.27 V, not 0.10 V. The state of K15-E does not change (OPEN at either floor), but three things the note hands on do: the BM-1 acceptance (4.72 V, not 4.89 V), the size of the gap (0.945 to 0.970 x, not 0.980 to 1.005 x) and the lever figure (1.017 to 1.043 x, not 1.050 to 1.077 x). BM-1 is one of the two ways the note says K15-E closes, so its acceptance would declare the hold guaranteed for a unit the design does not cover: a drop-out under RF near the end of a long over at a low pack, which is hot switching and a VGG step on reclosure (HZ-008 C5 and C6; detection REQ-SYS-156). **Fix (small):** take the in-over floor from REQ-SYS-098 (2 x 2.95 V at the cells under load, less the key-down current through the feed without the cells), or from a cited bound on the P28A cells over the longest over (REQ-SYS-180, 180 s) if that is higher and shown. Then restate the K15-E values, the BM-1 acceptance, the lever figure, and the BM-4 and BM-6 test points, and say which of the two is used. No new run is needed beyond `seq_run.py`'s `v_discharge` input or a second floor.

### Verification of finding-14, case by case

| # | Case (from the finding-14 fix) | Check | Result |
|---|---|---|---|
| 1 | State condition (2) on the ratio age | Section 7 row REQ-SYS-160: "a closure within 83.3 ms of the hang expiry, when the frequency reference ratio is then more than 10 s old, is sounded but not radiated (R-FRESH-2)" | Yes |
| 2 | Give the over lengths that can give it | Hand: 10 - 1.083 - (0.5 + 82.8) / 1000 = 8.834 s, stated as 8.83 s (rounded toward the shorter over, conservative); "always after an over longer than 10 s"; longest hang 30 dits x 0.24 s = 7.2 s at 5 WPM, so 1.63 s of keying. `result.json` `stale_ratio_case.over_min_s` 8.8337, `keying_min_s` 1.6337 | Yes |
| 3 | Align SR-01 and the plot label | CSV SR-01: "The rows below apply when the ratio is older than A_kd (10 s) at the closure (revision 2: set by the ratio age, possible after an over longer than 8.83 s)"; `s4-stale-ratio.png` x-axis: "ratio older than A_kd = 10 s at the key-down (after an over longer than 8.83 s)"; K20-c row restated | Yes |
| 4 | Say how often the case arises, and how TC-SYS-102 sets it up | Section 4.8: after an over of 8.83 s or more (1.63 s of keying with the longest hang); the TC-SYS-102 procedure sets the case up by the ratio age (HostUnit or Emulation with the age injected; on the bench an over of more than 10 s). The note edits no test-case file | Yes |
| 5 | No text left that states the trigger as the over length | grep of the note, `seq_run.py`, the README and the CSV for "longer than 10 s": each remaining use is the sufficient condition ("always") or the revision 1 history; section 4.8 names revision 1's wording as the sufficient condition only | Yes |

**Finding-14 at iteration 3: Verified.** The firmware rule, rows SR-02 to SR-04 and the HostUnit ages (10.1 s and 9.9 s) were already on the ratio age and are unchanged.

### Per-case results (iteration 3; the cases the delta touches)

| Case | Condition | Governing id and limit | Result (checker) | Margin | Uncertainty | Reviewer re-check | Finding ids |
|---|---|---|---|---|---|---|---|
| T-1 | E hold, pack 6.30 V at the start of the over, +45 C feed bound 0.5646 ohm at 2.140 A, dropout 0.10 V, 85 C coil | K15-E: hold at least the worst unit's must-operate (datasheet guarantee) | 0.9997 to 1.026 x at 4.99 V (OPEN) | -0.03 to +2.6 % | slope band; feed bound | hand 0.99972, 1.0258 | none |
| T-2 | T-1 after the note's 0.10 V pack fall | same | 0.980 to 1.005 x at 4.89 V (OPEN) | -2.0 to +0.5 % | discharge unbounded | hand 0.9797, 1.0053 | finding-13, finding-17 |
| T-3 | T-1 at the REQ-SYS-098 in-over end (cells 2.95 V under load) | same | not analysed | -5.5 to -3.0 % (reviewer) | cell sense point (0.963 x with the holder contacts inside it) | `rv_k15e_it3.py`: 4.720 V, 0.9453 to 0.9700 x | finding-13 |
| T-4 | T-2 with the WP-PDR-21 P-FET lever (0.3841 ohm, 2.233 A) | same | 1.050 to 1.077 x | +5.0 to +7.7 % | discharge unbounded | hand 1.0499, 1.0773 | finding-13 |
| T-5 | T-4 at the REQ-SYS-098 in-over end | same | not analysed | +1.7 to +4.3 % (reviewer) | as T-3 | `rv_k15e_it3.py`: 5.076 V, 1.0166 to 1.0432 x | finding-13 |
| T-6 | E hold, -10 C, feed 0.614 ohm at 2.215 A, after the 0.10 V fall, coil -10 C | same | 1.502 to 1.535 x | +50 % | none that matters | hand 1.5019, 1.5348 | none |
| T-7 | E pull-in at 6.11 V (6.30 V, 0.146 A through 0.614 ohm, dropout 0.10 V), 85 C coil, worst unit | K1b-E: operate + 0.5 ms at most 10 ms | 8.07 + 0.5 = 8.57 ms (PASS) | +1.43 ms | model band, slope band | re-run identical; interpolation of the iteration 2 harness 8.08 ms | none |
| T-8 | E release at -10 C from 6.43 V | K12-E: REQ-SYS-036 share 30 ms | 25.86 ms (PASS) | +4.14 ms | model band | re-run identical | none |
| T-9 | E coil own temperature at the lowest pack, -10 % unit | 85 C corner kept | 83.8 C (0.984 x at 4.89 V) | +1.2 K to the corner | 40 to 80 K/W | hand 83.86 C | none |
| T-10 | Stale ratio: shortest over that can give a ratio older than 10 s at a closure in the window | R-FRESH-2; REQ-SYS-160 condition (2) | 8.83 s (1.63 s keying with a 7.2 s hang); always after 10 s (K20-c FAIL, to the owner) | not applicable | FR-2r 1.083 s | hand 8.834 s | none |

### New findings of iteration 3

- **finding-17 (Minor, Open).** CK-ANA-D2, CK-ANA-D3. (a) The Summary's option E bullet still gives the limiter as "a low-dropout regulator set to 6.3 V +/-2 %, dropout at most 0.2 V" (note line 25). Section 2 and section 6.1 item 2, the part requirement handed to WP-PDR-37 and 38, say 0.10 V. (b) The key-down hold 0.97969 x is printed as 0.980 x (Summary, sections 4.3 and 5), rounded toward the 1.0 limit; `s3-keydown-hold.png` prints 0.9797. No state changes. Fix: 0.10 V in the Summary; 0.979 (or 0.9797).
- **finding-18 (Minor, Open).** CK-ANA-G1-4. The new s4 check `p4_feed_current` returns PASS when the WP-PDR-21 p4 `.raw` is absent ("inputs used as recorded, not re-derived"). That `.raw` is over 5,000,000 bytes and, under CR-017 C2, exists only in the owner's working tree, so in any export or clone the check passes without checking, and `seq_run.py all --expect` still exits 0 with "17 checks pass". Note section 3.4 describes the check as re-deriving the currents. The values are right (reviewer re-derivation, input 3). Fix: report a separate state (for example NOT RUN) that `--expect` records, or say in section 3.4 and the README that the check runs only where the `.raw` is kept.

### Minor findings at revision 2 (not re-reviewed under rule C1; for the lead SE)

| Finding | Status seen at `249356b` |
|---|---|
| finding-5 | Unchanged: `s4-keydown-budget.png` is the same blob (`17aa3f02`) and section 4.6 is unchanged |
| finding-6 | In part, as at iteration 2: `thermal-ts012.md` is still cited with no revision or review state; M-1 ladder (c) not carried |
| finding-7 | Unchanged: in `timing-diagram.png` (blob `49db873d`) panel (a) the annotation box still hides the envelope trace from about 17 ms; the `s2-coil-transient.png` dashed lines are still unlabelled; `s4-margins.png` same blob |
| finding-8 | Unchanged (K16 against 20 ms only) |
| finding-9 | Unchanged |
| finding-10 | Affects option A only (2N3904 not recommended) |
| finding-11 | Overtaken by option E (no PWM; section 6.2 row WP-PDR-20b withdraws the 25 kHz line). The lead SE may close it on re-reading |
| finding-12 | Unchanged |
| finding-15 | **Fixed** by the revision 2 restatement: the Summary gives "E has 1.43 ms to the limit" and section 4.2 "8.07 ms (r2), 1.43 ms inside it", both equal to K1b-E (8.57 ms against 10 ms). State set to Fixed for the lead SE to verify |
| finding-16 | Unchanged: section 4.9 still says the 30 ms re-arm "is shorter than every hang (72 ms or more) ..., so a real return to receive always re-arms it" |

### Checklist items at iteration 3 (the items the delta bears on)

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-A1 | Yes | REQ-SYS-097, REQ-SYS-160, TC-SYS-102, WP-PDR-21 and FR-2r named by id; each exists |
| CK-ANA-A3 | No | Every revision 2 input has a source except the 0.10 V pack fall, whose "source" is the previous review's illustration (finding-13) |
| CK-ANA-A4 | No | Inputs 1 to 6 and 8 agree with their sources (table above). Input 7 does not: the design's in-over bound gives 0.27 V (finding-13) |
| CK-ANA-A5 | Yes for the delta | The direction of each revision 2 assumption is stated (feed bound used in receive: overstated; current at 6.4 V used at 6.30 V: overstated by about 1.5 %, confirmed by input 4; chokes kept in the bound). finding-16 remains |
| CK-ANA-A6 | Yes for the delta | `249356b` touches only the note, `hardware/sim/tx-seq/` and the figure (`git show --stat`, 42 files). The lever and the rail floor go out as requests (section 6.2 rows WP-PDR-21 and WP-PDR-24). finding-12 remains |
| CK-ANA-B5 | Yes | Independent: the p4 `.raw` currents by separate code; the current-against-pack direction; every K15-E ratio, the pull-in floor, the coil temperature and the stale-ratio over lengths by hand; `rv_k15e_it3.py` for the REQ-SYS-098 floor |
| CK-ANA-B6 | No | The discharge is the one class E input of K15-E without a bound; section 10 item 6 names it but bounds it only by the plotted sensitivity (finding-13) |
| CK-ANA-C4 | Yes | Re-run from the `249356b` export, exit 0, outputs identical (above) |
| CK-ANA-D2 | No | Summary dropout 0.2 V against 0.10 V in sections 2 and 6.1 (finding-17). Every other number checked agrees across the note, `result.json`, the CSV and the plots |
| CK-ANA-D3 | No | 0.9797 printed as 0.980 (finding-17) |
| CK-ANA-E3 | No | K15-E is honestly OPEN, but the stated gap, the lever margin and the BM-1 acceptance rest on the unbounded discharge (finding-13) |
| CK-ANA-E4 | Yes | 17 checks asserted (exit 2 on failure), 40 criteria (exit 1 on FAIL or OPEN), `--expect` (exit 3 on a change). finding-18 on the absent-file behaviour |
| CK-ANA-E5 | Yes | REQ-SYS-161 12 ms supported. REQ-SYS-160 condition (2) now stated on the ratio age with the over lengths that give it (finding-14 Verified) |
| CK-ANA-F3 | No | The worst combination for the option E hold is not closed: the in-over low end is not the design's own bound (finding-13) |
| CK-ANA-F4 | Yes | `s3-keydown-hold.png` shows the hold against the rail and against the pack fall, for both slopes and the lever |
| CK-ANA-G1-4 | No | `p4_feed_current` passes when its input file is absent (finding-18) |
| CK-ANA-H1 | Yes | The drop-out consequence (hot switching, VGG step, REQ-SYS-156 detection) is stated and routed (section 4.9 table to WP-PDR-16) |
| CK-ANA-H3 | Yes | Change history row for revision 2; section 14 maps each finding to its fix |
| CK-ANA-I1 | Yes | 11 distinct renders opened (below); `renders_inspected: 11` |
| CK-ANA-I2 | No | finding-7 remains. The new `s3-keydown-hold.png` has labelled axes, the 1.0 limit, legends and marked points that agree with the hand values |

### Visual closure (iteration 3)

Opened with the Read tool after the re-run (11 distinct renders, all byte-identical to the re-run outputs):
- `s3-keydown-hold.png` (new): panel (a) hold against the key-down rail for the revision 1 (0.20 V) and revision 2 (0.10 V) dropout, steep and shallow ends; points 0.9797 at 4.99 V, 0.9997 at 5.09 V, 1.0499 at the lever's 5.34 V; the revision 1 5.45 V floor. Panel (b) hold against the pack fall from 0 to 0.30 V: the feed-bound steep line from 1.000 to 0.94, the lever steep line from 1.07 to 1.01, the 0.10 V allowance marked. Agrees with section 4.3 and the hand values. It shows, but does not state, that at the REQ-SYS-098 end (0.27 V) the feed-bound line is at about 0.945;
- `s3-limiter-setpoint.png`: operate plus bounce 10.04 ms at a 6.0 V set point and 8.57 ms from 6.3 V; release at -10 C 25.86 ms at 6.3 V; hold flat at 0.980 at every set point (in dropout); highest coil voltage 128.5 % at 6.3 V. Agrees with section 4.3;
- `s3-operate-vs-coil-temperature.png`: E at 6.11 V, band to about 8.1 ms at 85 C under the 9.5 ms line; legend "E: ... at 6.11 V". Agrees with section 4.2;
- `s3-release.png`: E e_max 6.43 V at -10 C band 24.86 ms; E e_min now 6.11 V; the 29 ms line. Agrees with section 4.4;
- `s1-coil-voltage-vs-pack.png`: receive rail shaded from 6.21 V (revision 2 floor); E flat at 126 % above about 6.4 V, C and D on-phase crossing 151 % at about 7.55 V; panel (b) unchanged. Agrees;
- `s1-coil-current.png`: H1 at 6.35 V about 27.8 mA against the 21.9 mA line (unchanged blob from r1, `b35f9622`);
- `s2-coil-transient.png`: E rise hot at 6.11 V settles at about 26.8 mA; finding-7 dashed lines unchanged;
- `timing-diagram.png` (and the figure copy): panel (a) text "relay made (E, worst) t0 + 8.57 ms", E band ending at 11.57 ms after the contact; finding-7's annotation box remains;
- `s4-stale-ratio.png`: x-axis label "after an over longer than 8.83 s"; panel (a) two dits not radiated, T/R drive at about 97 ms; panel (b) outcome (b) flat at 10.04 ms. Agrees with section 4.8;
- `s4-keydown-budget.png`, `s4-margins.png`: unchanged blobs, as read at iteration 1.

The reviewer's own plot `rv_k15e_it3.png` (scratchpad `rv23a-it3/`) was opened as well: hold against the pack fall for the feed bound and the lever at both slope ends, the 1.0 line, the note's 0.10 V allowance and the REQ-SYS-098 end at 0.272 V, with the points 0.945 and 1.017 marked (the lever's own end is at 0.266 V; its value is computed there).

### Cross items (iteration 3, returned to Claude)

- X-8. **Escalation (rule C1; 07 section 10.2).** Iteration 3 closes with one Major finding open (finding-13, one input of its fix). This is the third author-review iteration, so the lead SE takes it to the owner rather than running a fourth. In plain terms for the owner: the relay that switches the antenna between receive and transmit may let go near the end of a long transmission when the battery is nearly flat and the radio is hot. The note says so and marks the check open, which is right. What is not right yet is how much battery drop during a transmission it allows for: it assumes 0.1 V, while the radio's own low-battery shutoff allows about 0.27 V. That changes the pass mark of the bench test that could close the item (4.72 V instead of 4.89 V) and shrinks the margin of the lower-resistance switch option from 5 % to about 2 % (it still works). The fix is a restated input and three restated numbers; no design change and no new simulation. The options for the owner are: (a) accept one more short author fix with the lead SE verifying it against this record, or (b) accept the note as is with the finding carried as a lien on BM-1 and the lever figure.
- X-9. **Cold start at the transmit floor (not a finding on this note).** With the WP-PDR-21 revision 3 cell resistance at its -10 C bound (0.198 ohm for the pair), a key-down at 2.215 A from a 6.30 V receive reading puts each cell at about 2.93 V under load at once, below the REQ-SYS-098 power-down (3.00 V +/-0.05 V). A unit started at the REQ-SYS-097 floor at -10 C may therefore power down on the first key-down. That is for WP-PDR-24 (`power-protection-thresholds.md`, the REQ-SYS-097 and 098 values and any key-down filtering of the reading) and WP-PDR-21.
- X-10. The p4 `.raw` exists only in the main working tree (CR-017 C2). This review's re-derivation depended on it; the lead SE may want the WP-PDR-21 record to state that its users re-derive from it (finding-18).
- X-11. `assurance_verdict` is copied from INSP-123 as last seen (iteration 2 at `fb120d2`: APPROVED, per the record returned to the lead SE). Its iteration 3 delta on `249356b` is a separate invocation; the software lead updates the field from INSP-123 at filing. Iterations 1 to 3 of this record are unfiled; this text is the complete record (X-3 of iteration 2 still applies).

### Completion criteria (SWE-088), iteration 3

Not met on the reviewer side: one Major finding is open (finding-13). R1 to R6 hold at `249356b`:
- R1: 23 blobs frozen;
- R2: one command, exit 0 with `--expect`;
- R3: `expected_states.json` has no schema. `tools/validate_docs.py` on a `git archive HEAD` (`249356b`) export with this record placed at its path: exit 0, 124 passed, the record PASS against the built-in peer-review record schema;
- R4: the author return and note section 14;
- R5: no `TBD` in the note;
- R6: every cited render is beside its run.

`reviewer_verdict: NEEDS CHANGES`. The record `verdict` is held at NEEDS CHANGES.

```
ITERATION 3 (2026-09-29, HEAD 249356b, product commit 249356b): REVIEWER VERDICT: NEEDS CHANGES
PRODUCT: docs/design/analysis/sequencer-timing.md@b6a5e31a (revision 2), seq_run.py@d28ab4a1, relay_model.py@0285c9c9, runs 2026-09-29-r2-s1 to r2-s4 (23 blobs) at 249356b
FINDINGS:
- [Major] finding-13: Open. Fixed: the REQ-SYS-097 6.30 V start, the WP-PDR-21 r3 feed bound 0.5646 ohm with the p4 current 2.140 A, the 0.10 V dropout, K15-E stated OPEN, the 6.11 V pull-in floor (K1b-E 8.57 ms), K22-E. Not fixed: the pack fall during an over is 0.10 V with no source; REQ-SYS-098 (cells 2.95 V under load) gives 0.27 V, a 4.72 V coil and 0.945 to 0.970 x. BM-1's 4.89 V acceptance and the lever's 1.050 x follow from the unbounded value (at the REQ-SYS-098 end: 4.72 V, 1.017 x).
- [Major] finding-14: Verified (condition (2), K20-c, SR-01 and the plot label on the ratio age; 8.83 s, 1.63 s of keying).
- [Minor] finding-15: Fixed (1.43 ms against K1b-E).
- [Minor] finding-17 (new): Summary dropout 0.2 V against 0.10 V; 0.9797 printed as 0.980.
- [Minor] finding-18 (new): p4_feed_current passes when the p4 .raw is absent.
- [Minor] findings 5 to 12, 16: Open, not in the delta (finding-11 overtaken by option E).
ITEMS N/A: CK-ANA-E6; G2 to G5.
VALUES PROPOSED: REQ-SYS-161: 12 ms (supported); REQ-SYS-160: 15 ms with conditions (1) bounce 1.957 ms (supported) and (2) the stale-ratio case on the ratio age (supported as worded).
MEASUREMENTS: blobs equal HEAD 23/23; checks 17 PASS, --expect exit 0; outputs byte-identical (result.md 4/4, PNG 11/11, CSV 1/1); delta cases 10; inputs checked 8; renders inspected 11; major open=1; minor open=11; turns=48; minutes=60 (cumulative 170 and 220); iteration=3
```

### Commands (reviewer, iteration 3)

```
cd /Users/robinonsay/rust/cwht
git rev-parse 249356b:<path>; git rev-parse HEAD:<path>; git hash-object <path>          # R1, 23 paths
.venv/bin/python tools/check_commit_msg.py --range 249356b~1..249356b                    # PASS
git archive 249356b | tar -x -C <scratchpad>/rv23a-it3-249356b                            # export
cp -R <export>/hardware/sim/tx-seq/results <scratchpad>/rv23a-it3-ref/results             # committed results aside
cp hardware/sim/tx-pa/results/2026-09-29-r3-p4-power-a5-design/power_a5_design.raw <export>/...   # CR-017 kept file
cd <export>; .venv/bin/python hardware/sim/tx-seq/seq_run.py all --expect                 # exit 0, 46.7 s
cmp / diff of every r2 output against rv23a-it3-ref; .raw data sections after the header  # C4
(p4 .raw moved out) .venv/bin/python hardware/sim/tx-seq/seq_run.py s4 --expect           # exit 0, check PASS "not present"
shasum -a 256 power_a5_design.raw coil_tran.raw en-g5v_2.pdf                              # manifests, datasheet
spicelib read of power_a5_design.raw: I(Vp), V(d), V(vg) per step at 6.4 to 8.4 V         # inputs 3 and 4
cd <export>/hardware/sim/tx-seq; .venv/bin/python <scratchpad>/rv23a-it3/rv_k15e_it3.py <png>   # finding-13 residual
validate_docs.py on a git archive HEAD export with this record placed                     # R3
```

### Measurements (SWE-089), iteration 3

size = 10 delta cases; inputs_checked = 8 (REQ-SYS-097, the p4 feed bounds, the p4 currents by separate code, the current-against-pack direction, FR-2r, the datasheet ordering table, the discharge allowance against REQ-SYS-098, the receive current basis); renders = 11; turns = 48; minutes = 60; major = 0 new (finding-13 still Open; 6 in total); minor = 2 new (12 in total).
