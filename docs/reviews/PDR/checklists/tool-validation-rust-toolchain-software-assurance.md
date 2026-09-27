---
# Peer-review record front matter (charter sections 2 and 5; docs/process/01-lifecycle-and-reviews.md section 13
# is the single field list; docs/process/07-software-engineering-plan.md sections 2.1.1, 10.2 and 15).
# This is the paired software assurance record (07 section 10.2) of the tool validation review INSP-040
# (docs/reviews/PDR/checklists/tool-validation-rust-toolchain.md, iteration 2 by
# reviewer:WP-PDR-08-rust-toolchain-iter2), requested there as "SA pair needed" (cross item X-2) and named by
# PDR work plan WP-PDR-08 ("Reviewer: independent reviewer plus SA"), wave 0.
# Checklist applied: docs/templates/peer-review-checklist-software-assurance.md revision A AS ON ITS CR-012 BRANCH
# (cr/CR-012-pdr-checklist-templates at 7784672, blob 5b13528504868b2add0f0b1e329c63aa2b54cdf4; not merged).
# The `checklist` field names peer-review-checklist-code revision B, the checklist INSP-040 names for the same
# reason: tools/validate_docs.py fails a record whose `checklist` names a template absent from main, and the lead
# SE convention of 2026-09-27 does not change the validator. The field `assurance_checklist` names the template
# actually applied.
id: INSP-048
checklist: peer-review-checklist-code
checklist_revision: B
assurance_checklist: "docs/templates/peer-review-checklist-software-assurance.md@5b13528504868b2add0f0b1e329c63aa2b54cdf4 (revision A, branch cr/CR-012-pdr-checklist-templates at 7784672)"
checklist_file: docs/reviews/PDR/checklists/tool-validation-rust-toolchain-software-assurance.md
product: docs/cm/tool-validation/TV-020-rust-toolchain.md
# product_commit and product_files: equal to INSP-040 iteration 2 (readiness R1; rule C2). Every blob below is
# on main and equal to its HEAD blob at 2026-09-27 (git rev-parse HEAD:<path>, HEAD d566e01): the products are
# not branch-only.
product_commit: "c827202144e73328b816e666e48dbcd1b3afaae8"
product_files: ["docs/cm/tool-validation/TV-020-rust-toolchain.md@3f11ab13e54557cbfc023662b63b050921a7957b", "docs/cm/tool-validation/TV-021-cargo-llvm-cov.md@9ce8f95682faf75c0c37f8df9e2f7c080214a461", "docs/cm/tool-validation/TV-022-cargo-nextest.md@308dcf66b4196c3a7127a7060e0cae93592c6931", "docs/cm/tool-validation/TV-023-nightly-miri.md@dd169983c878910728e32154eca4dd01aea82f0b", "docs/cm/tool-validation/evidence/rust-tv-2026-09-27.sh@4c7cb7534b96e77cea16c601dfa00c2f42b3ae1a", "docs/cm/tool-validation/evidence/rust-tv-2026-09-27.log.txt@ac0ac0036cee9ad6b68f0aaf6895dfddd1aab556", "docs/cm/tool-validation/evidence/rust-tv-2026-09-27-r3.sh@42ad521a434d7c69929b010464e7d8e02b3a7e26", "docs/cm/tool-validation/evidence/rust-tv-2026-09-27-r3.log.txt@4e8fc033b19c8d0ad101336aabc9249df16662dd", "tools/toolchain.lock.md@b45c8654476be36b3b1918fbe9ff2040ac6c941e", "docs/cm/tool-validation/README.md@87fb1e8cab28baf623981a3386fb260f5263d1be", "tools/tests/fixtures/rust/pdr-known-answers.json@00256755f82af9b37f16dde635094e03a2dfd1c0", "tools/tests/fixtures/rust/known-answers.json@6311da66a6047b51fa6fe4500e4019c58aba2a00", "tools/tests/fixtures/rust/cond-kat/Cargo.lock@e182713ad234cb0299e19db21bdd60fba19f823a", "tools/tests/fixtures/rust/cond-kat/Cargo.toml@e0766feaaaa3ccf98b4695a05923e6effb263843", "tools/tests/fixtures/rust/cond-kat/src/lib.rs@d5b59f44c44a317687f69aea2aceaddaa2dd6580", "tools/tests/fixtures/rust/cov-kat/Cargo.lock@2b383527992def7ad32c9cad707a6a5a9f46c50e", "tools/tests/fixtures/rust/cov-kat/Cargo.toml@e1e0dbbd1665d11c986110dc3541dfa769932650", "tools/tests/fixtures/rust/cov-kat/src/lib.rs@19ded2eadfe063724c21a43a379a5686150380b6", "tools/tests/fixtures/rust/harness-seeded/.config/nextest.toml@a555946aa3ee04e122b8d22df4f50b9e898e556e", "tools/tests/fixtures/rust/harness-seeded/Cargo.lock@0cb6c2dc1a752c57d88bbc79a55720c45f23ab77", "tools/tests/fixtures/rust/harness-seeded/Cargo.toml@386895fd4e74d812e220f70aa75cf24568ec6f04", "tools/tests/fixtures/rust/harness-seeded/src/lib.rs@7f901c951148cc5f6cc19731b8851c4cdb15b8b4", "tools/tests/fixtures/rust/harness-seeded/tests/harness.rs@e62465bc00f2bfd9beb6e80f0f671fcbb8758613", "tools/tests/fixtures/rust/kat-host/Cargo.lock@6e442470154fa509b20b5e1480ac644d2044473a", "tools/tests/fixtures/rust/kat-host/Cargo.toml@fd9ad9df3ed607030dbe5f4459081da1cff04f99", "tools/tests/fixtures/rust/kat-host/clippy.toml@42020b54612e1bcb2c64149353575b6fa6883d96", "tools/tests/fixtures/rust/kat-host/src/lib.rs@1ac6e57e8dc73773077b8a90a65ac9300e6e09af", "tools/tests/fixtures/rust/kat-target/.cargo/config.toml@6ae26913b43fd609fe0e7e78b6ad886dededb810", "tools/tests/fixtures/rust/kat-target/Cargo.lock@7fed9133c31179b0096217c07862c51812d90827", "tools/tests/fixtures/rust/kat-target/Cargo.toml@d9edf91cdd893fca406e44bd24fb88281f2b2dc9", "tools/tests/fixtures/rust/kat-target/build.rs@4753901c8962d0fa4cc459f00c7e85b246bfcda0", "tools/tests/fixtures/rust/kat-target/link.x@70b6d0d8b890d41e4a5db43aa25d06aefb158779", "tools/tests/fixtures/rust/kat-target/src/main.rs@d97ecd8135bfecf4958de803b452cdfce2f2ee82", "tools/tests/fixtures/rust/miri-kat/Cargo.lock@c0e750f3f8397c332f8dd655714a347524142712", "tools/tests/fixtures/rust/miri-kat/Cargo.toml@24a25655c2a40e9c18a616bb4f913e90a207d928", "tools/tests/fixtures/rust/miri-kat/src/lib.rs@84e8f8c9c46190843074170b4220fb546d153f36"]
fixture_trees: ["tools/tests/fixtures/rust/kat-target@1eae87cd88cfec51f5b46f8450b24a2dd7f5894c", "tools/tests/fixtures/rust/kat-host@d70d2554d7ca0f4c3e7e16fdebbb7998cbe80f9a", "tools/tests/fixtures/rust/cov-kat@970e59d5059906dfea91dd2bae5769da2d66fc0d", "tools/tests/fixtures/rust/cond-kat@cca3b34803faee4b9f4a39f4b993e5fc656202f2", "tools/tests/fixtures/rust/miri-kat@bf632e485880160f57271332f77cc5ea9de78ce4", "tools/tests/fixtures/rust/harness-seeded@dbc9eae482a0a62f663b66d0f3ca7e36fddfb0b0"]
# inputs read (not reviewed), blobs at HEAD d566e01
input_files: ["docs/reviews/PDR/checklists/tool-validation-rust-toolchain.md (INSP-040 iteration 2, committed f38159d)", "docs/process/07-software-engineering-plan.md", "docs/process/03-software-classification-and-rmm.md", "docs/process/05-configuration-and-data-management.md", "docs/process/04-verification-and-validation.md", "docs/process/rmm.json", "docs/risk/register.md", "docs/plan/pdr-work-plan.md", "docs/templates/peer-review-checklist-tool-validation.md@7be809d4ceb9a202473eb19da3627fe0cd427900 (CR-012 branch)"]
paired_record: INSP-040
tv_ids: [TV-020, TV-021, TV-022, TV-023]
# product_type: 07 section 2.1.1 has no row for tool validation records (finding-1). Task set applied: the section B
# row "Every product type", the swe-136 and swe-070 tasks the section B row trade-study-or-adr names "when the
# decision selects a tool", and the section 7.1 tasks of every SWE the four records govern (07 section 15)
product_type: tool-validation
# criticality: 03 section 4.3.1 determines the verification software (host test harness with cargo nextest)
# "Not safety-critical; verification software of safety-critical components"; 03 section 4.3 lists the engineering
# tools as neither. The class A compiler builds the image of the 07 section 14.1 safety-critical components
criticality: neither
product_size: 4 TV records (411 lines), 13 purposes, 23 known-answer checks, 6 fixture directories (34 files), 2 procedures, 2 logs
sprint: PDR-prep
author_agent: "author:WP-PDR-08 (Claude as software lead and tool owner)"
reviewer_agent: "sa-reviewer:WP-PDR-08-rust-toolchain"
assurance_required: true
assurance_reviewer_agent: "sa-reviewer:WP-PDR-08-rust-toolchain (software assurance function; paired file review INSP-040 by reviewer:WP-PDR-08-rust-toolchain-iter2, iteration 1 by reviewer:WP-PDR-08-rust-toolchain)"
iteration: 1
readiness_met: true
# reviewer_verdict and assurance_verdict: APPROVED at iteration 1 (no Major; five Minor findings are liens due the
# CDR readiness declaration, PDR work plan rule C1, as INSP-040 is past its first APPROVED reviewer verdict)
reviewer_verdict: APPROVED
assurance_verdict: APPROVED
# verdict: set by Claude as software lead (07 section 10.2). Held at NEEDS CHANGES here: the product blobs are on
# main, but the checklist applied exists only on cr/CR-012-pdr-checklist-templates (lead SE convention of
# 2026-09-27, INSP-031 and INSP-046 practice), and INSP-040 does not yet name this record (paired_record,
# assurance_reviewer_agent, assurance_verdict; each reviewer updates only its own record). The software lead sets
# APPROVED on both records when INSP-040 carries the pairing and CR-012 merges with the template blob unchanged
verdict: NEEDS CHANGES
findings_major: 0
findings_minor: 5
findings_open: 5
findings_fixed: 0
findings_verified: 0
findings_deferred: 0
assurance_findings_major: 0
assurance_findings_minor: 5
assurance_tasks_applied: ["swe-134 7.1 task 5", "swe-022 7.1 task 1", "swe-136 7.1 task 1", "swe-070 7.1 task 1", "swe-135 7.1 task 1", "swe-135 7.1 task 2", "swe-135 7.1 task 7", "swe-061 7.1 task 1", "swe-186 7.1 task 1", "swe-189 7.1 task 1", "swe-190 7.1 task 1", "swe-190 7.1 task 2", "swe-190 7.1 task 3", "swe-191 7.1 task 1", "swe-191 7.1 task 3", "swe-219 7.1 task 1"]
swe134_items_checked: []
deferred_rids: []
items_no: [SA-E3, "swe-191 7.1 task 1"]
effort_turns: 38
effort_minutes: 60
record_status: Open
date: 2026-09-27
date_closed: null
---

# Peer review record INSP-048: software assurance second review of TV-020 to TV-023 (Rust toolchain, cargo-llvm-cov, cargo-nextest and the HostUnit harness, nightly-2026-08-24 with Miri), WP-PDR-08

**Product.** `docs/cm/tool-validation/TV-020-rust-toolchain.md` (blob `3f11ab13`), `TV-021-cargo-llvm-cov.md` (`9ce8f956`), `TV-022-cargo-nextest.md` (`308dcf66`) and `TV-023-nightly-miri.md` (`dd169983`) at `c827202`, with the fixtures, procedures, logs, lock and README at the blobs of `product_files`, character for character the INSP-040 iteration 2 list. Every blob and fixture tree was recomputed with `git rev-parse HEAD:<path>` at HEAD `d566e01`: all 36 blobs and 6 trees equal, so the products are on `main` and not branch-only. **Checklist applied:** `docs/templates/peer-review-checklist-software-assurance.md` revision A as on its CR-012 branch (`7784672`, blob `5b135285`); the `checklist` field explains why it names the code checklist. **Paired record:** INSP-040 (iteration 1 committed `1b93d83`, iteration 2 `f38159d`), file reviewers `reviewer:WP-PDR-08-rust-toolchain` and `reviewer:WP-PDR-08-rust-toolchain-iter2`.

**Independence (rule C4; 07 section 2.1).** This invocation authored no part of WP-PDR-08, TV-020 to TV-023, their fixtures or procedures, and wrote neither iteration of INSP-040; it edited no product file. Author, file reviewers and assurance reviewer are distinct invocations.

**Search first (charter section 11 rule 1).** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (queries: "INSP-040 WP-PDR-08 tool validation record peer review"; "SWEHB swe-136 software assurance 7.1 tasking software tool accreditation"; "validate_docs paired assurance record product_type allowed values assurance_reviewer_agent rule"; "03 section 4.3.1 host test harness criticality cwht-hal-mock contract tests tool classification"; "risk compiler miscompilation rustc defect inserts error into safety-critical image toolchain risk"). `grep -n`, `awk` extraction of the SWEHB section 7.1 lists and of SWEHB topic 8.10 section 6, and `git log` were used afterwards only to pin lines. **No download, no tool run of the toolchain:** INSP-040 re-ran both procedures (iterations 1 and 2); this review read the evidence logs, re-derived the X10 fixture answers by hand and checked the records against the plans, the RMM and the risk register. The rustos working tree was not read.

## Record

### Findings

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | assurance | Minor | SA-A1 | 07 section 2.1.1 table (lines 114 to 124); TV-020 line 117 ("independent reviewer plus a software assurance second review (PDR work plan WP-PDR-08; 07 section 2.1.1)"); TV template (CR-012 branch `7784672`) front matter lines 59 to 63 (`assurance_required: false`, "07 section 2.1.1 has no row for TV records"); PDR work plan WP-PDR-06 and WP-PDR-08 Reviewer lines | The dispatch rule for this review is inconsistent across three controlled texts. 07 section 2.1.1 is "the single rule for dispatching the software assurance reviewer" and has no row for tool validation records; the TV template therefore sets `assurance_required: false` and puts the swe-136 and swe-070 tasks in its own section H; the owner-approved PDR work plan names an SA second review for the credit tools (WP-PDR-06 "SA second review (tool used for credit)", WP-PDR-08 "independent reviewer plus SA"); and TV-020 section 8 cites 07 section 2.1.1 as the basis, which that table does not support. The SA template itself says a product that should be routed and is not "is reported as a cross item to the software lead, not reviewed on the reviewer's own initiative"; this review runs on the plan's instruction, so the routing holds for this record, but a later TV record of a credit tool (TV-024, the CDR set) has no rule that sends it here. INSP-040 raised the same conflict as cross item X-2 without a finding; the assurance lens makes it a dispatch-integrity item (SA-A1), Minor because no safety conclusion changes (03 section 4.3.1 keeps the tools not safety-critical). Fix: the 07 writer of plan section 5.3 (WP-PDR-13 or WP-PDR-47) adds a 07 section 2.1.1 row "TV records of class A tools and of class B tools whose output is credited evidence for a safety-critical or mission-critical component" (Yes, Yes, No) with the swe-136 and swe-070 tasks; the SA template gains the matching section B row and the TV template's `assurance_required` comment follows it (CR-012 revision or its follow-on); TV-020 section 8 cites the plan, not 07 section 2.1.1, until then | Open | Pending | |
| <a id="finding-2"></a>finding-2 | assurance | Minor | `swe-191 7.1 task 1` | 03 section 4.3.1 host test harness row (line 194: "the seeded tests re-run at every release"); 03 section 6.5 item X10 (line 338, owner "07 author; PDR"); TV-022 section 6 limitation 2; 04 section 10.5 firmware regression set (line 396); PDR work plan WP-PDR-08 "Closes: C-079, C-080" | X10 has two parts: add the seeded failing independence-pair test and seeded mock fault to the harness TV record (done: TV-022 K22-4 to K22-6, re-derived below), and re-run them at every release. The second part is the regression-side obligation 03 section 4.3.1 sets for the verification software of the safety-critical components, and SWEHB `swe-191` 7.1 task 1 (SC) asks assurance to confirm that regression testing is planned and adequate. It is carried only by TV-022 limitation 2 ("cross item for the release procedure and TC-SW-REG-001"), with no owner, no work package and no due event: the 04 section 10.5 regression set (the `TC-SW-REG-001` run of every tagged release) and 05 section 8.1 release procedure do not name the seeded harness run, 07 has no text for it (X10 names 07 sections 9 and 17.3), and no PDR work package in plan section 3 writes `tools/release.sh` or the `sw-reg` case. WP-PDR-08 claims C-080 (X10) closed. No release exists yet (the first candidate is FW-B2, before CDR), so nothing is lost today. Fix: add the seeded harness re-run (TV-022 procedure section 10, or its successor in `tools/release.sh`) to the 04 section 10.5 regression set and to `TC-SW-REG-001`, with the 07 section 9.3 sentence X10 asks for, owned by the 07 writer and the V&V plan writer, due before the first release candidate; record C-080 as partly closed (TV part) until then | Open | Pending | |
| <a id="finding-3"></a>finding-3 | assurance | Minor | `swe-136 7.1 task 1`, SA-F1 | TV-020 sections 2, 3 and 6 and the ACC-RUST-001 statement (section 9); `docs/risk/register.md` RSK-020 mitigation step S1 and likelihood rationale; RSK-062 given-clause | SWEHB `swe-136` section 1.1 states the purpose of accreditation as ensuring that tools "do not generate or insert errors in the software executable components", and its section 7.2 asks that tool limitations be documented "along with the corresponding mitigation actions". No known answer of TV-020 checks the semantics of target code generation: K20-1 compares the `kat-target` ELF with a hash produced earlier by the same compiler, and K20-4 and K20-5 check reproducibility at one path; a miscompilation present in both runs passes every check. TV-020 section 6 does not state this limitation, and RSK-020 (upstream rustc miscompiles a safety-critical construct for Cortex-M33) counts "the accreditation by tests with a TV record" as the evidence for its likelihood anchor 2, with S1 "accredit the pinned rustc by the known-answer tests ..., the reproducible rebuild (MSR-28) and the emulation scenario set on the release image"; TV-020 contains no emulation element, so S1 cannot close on TV-020 alone. RSK-062 still says "no accepted TV record exists for the Rust toolchain" and names only the 2026-09-25 log. The mitigation that does bound the risk, Bench Test of every hazard-tracing requirement on the delivered unit (RSK-020 S3; 07 section 9.7), is in place in the plans, so no safety conclusion changes. Fix: TV-020 adds limitation 8 ("no check verifies the semantics of generated target code; miscompilation is covered by RSK-020 S3 and, for event order, the emulation set once ACC-EMU-001 exists") and ACC-RUST-001 says the same; this record submits to the risk register writer (WP-PDR-18, plan section 5.3) the re-assessment of RSK-020 (S1 split into the TV-020 part, now done, and the emulation part with its own artifact; likelihood rationale restated) and the refresh of the RSK-062 given-clause, tag `assurance` | Open | Pending | |
| <a id="finding-4"></a>finding-4 | assurance | Minor | SA-E3 | Commits `c28dd60` and `c827202` | Both commits touch TV configuration items (the `pdr-known-answers.json` and procedure of TV-020 and TV-021; TV-020, TV-021 and their evidence), so 05 section 4.5 makes `Refs:` mandatory. Each message has a `Refs:` line (`Refs: TV-013, TV-020, TV-021` and `Refs: TV-013, TV-020, TV-021, INSP-040, INSP-041`), but a blank line separates it from `Co-Authored-By:`, so git does not parse it as a trailer: `git log --format='%h %s%n  trailers: %(trailers:only,unfold)'` over the product paths prints only `Co-Authored-By` for both, while `a3cacee` and `71bf509` parse correctly. This is the pattern the CSA (`docs/process/configuration-status.md` line 154) already counts as "not parsed" for `9fd0962`, and INSP-046 finding-4 for `ac9b7a5`. No `CR:` trailer is needed (the tools are not Accredited, so their records and fixtures are Log or Record class, 05 Table 4-1 rows 28 and 30). INSP-040 R1 did not check trailers. Fix: the CSA lists `c28dd60` and `c827202` as RID candidates at PDR as it does `9fd0962`; `main` history is not rewritten (05 section 4.5 History integrity); `tools/check_commit_msg.py` (TV-019, WP-PDR-07) rejects the pattern once installed as the hook | Open | Pending | |
| <a id="finding-5"></a>finding-5 | assurance | Minor | `swe-135 7.1 task 2` | 07 section 8.3 (line 344: "the Rust toolchain, coverage and static analysis tools and the emulator are accredited by PDR"); 05 section 13 CDR row (line 588: TV records for `cargo-audit`, `cargo-deny`, `cargo-geiger`, `rust-code-analysis-cli` due CDR); TV-020 Annex A rows MSR-09 to MSR-11 and MSR-17 ("due CDR", "agree") | SWEHB `swe-135` 7.1 task 2 (SC) asks assurance to confirm that the static analysis tools are used with checkers for security and coding errors and defects. This TV set validates the coding-defect checker (clippy, K20-3) and the Miri UB detector (non-credit); the security and unsafe-use checkers (`cargo-audit`, `cargo-deny`, `cargo-geiger`) and the complexity tool are scheduled for CDR by 05 section 13, while 07 section 8.3 says the static analysis tools are accredited by PDR. TV-020 Annex A, whose purpose is the E-14 check of 07 sections 7 and 8 against the lock, reports those rows as "agree" without noting the gate conflict, and WP-PDR-08 claims the SWE-135 row. The lock sanity runs of 2026-09-26 (lock section 1.1 rows cargo-audit and cargo-deny: seeded advisory and seeded licence detected) show the checkers work, so the gap is one of schedule and record, not of detection. Fix: the 07 writer aligns 07 section 8.3 with 05 section 13 (static analysis tools other than clippy and Miri by CDR) or the owner pulls those TV records to PDR; TV-020 Annex A marks the four rows "07 section 8.3 differs from 05 section 13 (due gate)"; the SWE-135 row closure at PDR is stated as partial (clippy, Miri) | Open | Pending | |

Finding rules applied: the INSP-040 findings are not raised again. The assurance lens was checked against each and changes none: finding-3 (`rust-objcopy` unidentified) and finding-8 (procedures exit 0 on a FAIL line) could let a wrong reproducibility result pass unnoticed in a later scripted re-run, but every recorded run was read line by line by the author and by the reviewer (the r3 log holds 12 PASS lines per run and FAIL lines only in the K21-4 mutation appendix, where they are expected), so both stay Minor; finding-5 (target clippy and `--locked`) touches the image crate `cwht-app`, but the same clippy driver and lint table are validated on the host fixture, so it stays Minor and is cited under `swe-135` task 2 below. Disposition of all five findings of this record: liens due the CDR readiness declaration (PDR work plan rule C1; listed in PDR package section 15). Finding-2 has a harder due event inside that window: before the first release candidate.

### Task table (row "Every product type", the swe-136 and swe-070 tool tasks, and the SWEs the four records govern)

The SWEs are those each record's "Governs" row names (TV-020: SWE-136, SWE-070, SWE-135, SWE-061; TV-021: SWE-136, SWE-070, SWE-189, SWE-190, SWE-135; TV-022: SWE-136, SWE-070, SWE-186, SWE-191; TV-023: SWE-136, SWE-070, SWE-219, SWE-135), plus SWE-201, which every record names as a re-validation trigger. Task texts are the SWEHB section 7.1 lists ("From NASA-STD-8739.8B"); SC marks are from SWEHB topic 8.10 section 6 (`8-10-facility-software-with-safety-considerations.md` line 298 onward: SWE-022 task 1, SWE-134 task 5, SWE-135 tasks 2, 5 and 6, SWE-191 task 1, SWE-219 task 1; SWE-136, SWE-070, SWE-061, SWE-186, SWE-189, SWE-190 and SWE-201 carry none).

| Task | Safety-critical designation (SWEHB 8.10 section 6) | Applied | Result and evidence | Relief (N/A only) | Finding ids |
|---|---|---|---|---|---|
| swe-134 7.1 task 5 | SC | Yes | This record is the assurance participation in the review of tools that build (TV-020 class A) and verify (TV-021 to TV-023; the 03 section 4.3.1 host harness) the 07 section 14.1 safety-critical components | | none |
| swe-022 7.1 task 1 | SC | Yes | Performed against the project SA plan (07 section 15) with the SA checklist of CR-012 as its tasking part | NASA-STD-8739.8 part: `rmm.json` SWE-022 T | none |
| swe-136 7.1 task 1 | | Yes | Validated: each record has identification with binary SHA-256 and install source, one-line purposes, a known answer per purpose with a seeded fault for every class B purpose (INSP-040 per-purpose table and finding-2 Verified), results of runs 1 to 4, limitations, triggers. Accredited: not yet; the owner decision is section 9 of each record, due PDR as OD-24 (b), and each record and the lock state "developer evidence until section 9 records the accreditation" (TV-020 limitation 7; lock rows). No credited use precedes it: `grep -l '^credit: true' -r docs/vv/reports` finds none (the six `TC-SW-TOOL-001` reports are the only reports). Limitation of the compiler checks not documented | | finding-3 |
| swe-070 7.1 task 1 | | Yes | The tools used to qualify the software by HostUnit (the `cwht-hal-mock` device models driven by `cargo nextest`, `rmm.json` SWE-070 "the cwht-hal-mock device models") are validated for their fault path (TV-022 K22-4 to K22-6). Model fidelity against silicon is outside this set by TV-022 scope and is carried by RSK-063 S1 (contract suite, due PDR) and S2 (fidelity statement, due CDR); accreditation pending as for swe-136 | | none |
| swe-135 7.1 task 1 | | Yes | Engineering data analysed: the lint table is in force (K20-3 `seeded-unwrap` fails only because the project table denies `clippy::unwrap_used`, which clippy allows by default), coverage thresholds enforced (K21-2 exit 1), UB detected (K23-5) | | none |
| swe-135 7.1 task 2 | SC | Yes | Clippy with the 07 Annex B lint table (K20-3; TV-020 purpose 3) and Miri (K23-4 to K23-6, non-credit) validated; the security and unsafe-use checkers are scheduled for CDR with a gate conflict against 07 section 8.3; target clippy not exercised (INSP-040 finding-5) | | finding-5 |
| swe-135 7.1 task 3 | | N/A | No static analysis result on product code is in this product (FW-B0 host crates only, used as known answers) | 07 section 8.4 (gate results are addressed per sprint) | none |
| swe-135 7.1 task 4 | | N/A | The security scan tools are outside this TV set | 05 section 13 CDR row (`cargo-audit`, `cargo-deny` TV records) | finding-5 |
| swe-135 7.1 task 5 | SC | N/A | No safety-critical code exists at FW-B0 (TV-022 limitation 1: no `cwht-core` decision has more than one condition); the tools that will supply the SWE-219 record are validated here (task row swe-219) | 07 section 9.6 (coverage report `TC-SW-COV-001-r<N>` per release) | none |
| swe-135 7.1 task 6 | SC | N/A | Complexity tool not in this set | 05 section 13 CDR row (`rust-code-analysis-cli` with `tools/complexity_gate.py`, TV-012) | none |
| swe-135 7.1 task 7 | | Yes | Thresholds defined and exercised: `-D warnings` over the lint table (K20-3), `--fail-under-lines 100 --fail-under-regions 100` (K21-1, K21-2; 07 section 9.5) | | none |
| swe-061 7.1 task 1 | | Yes | Coding standard 07 section 7 (CS-01 to CS-38) selected; TV-020 Annex A confirms its tool versions against the lock (E-14 software part), with the `rustfmt` CS-26 gap of INSP-040 finding-7 | | none |
| swe-061 7.1 task 2 | | N/A | No product code is reviewed here; conformance of code is the code review's | 07 section 2.1.1 code row | none |
| swe-186 7.1 task 1 | | Yes | Procedures (`rust-tv-2026-09-27.sh` `4c7cb753`, `-r3.sh` `42ad521a`), as-run logs (`ac0ac003`, `4e8fc033`), fixtures and stored answers are committed; K20-6 and K22-7 show the HostUnit suite twice identical by triples and by `tools/measurements.py --diff-runs`; INSP-040 reproduced both procedures from `git archive` exports | | none |
| swe-189 7.1 task 1 | | Yes | MSR-13 selected and performed with the validated tool (K21-3: `cwht-core` 17 of 17, `cwht-hal-mock` 53 of 53, twice identical); recording with each release starts with the first release (`TC-SW-COV-001-r<N>`) | | none |
| swe-190 7.1 task 1 | | Yes | Coverage analysis uses the tool results (`lcov` read by `tools/measurements.py --coverage`, K21-4 seeded gap reported as `lines 5/6 = 83.33 %`) | | none |
| swe-190 7.1 task 2 | | Yes | Uncovered code is identified by the text report (K21-2 names line 6) and the `lcov` export (K21-4a `DA:6,0`); target-only code is outside the measure and stated (TV-021 limitation 2) | | none |
| swe-190 7.1 task 3 | | Yes | Risk of the unmeasured target-only code (`cwht-app`, MMIO and boot code of `pico2`) is assessed in 07 section 9.5 item 2 and covered by dev-board checks and Bench cases (TV-023 limitation 4) | | none |
| swe-191 7.1 task 1 | SC | No | Regression artifacts validated (TV-022 purpose 2: JUnit triples kept per run); the 03 section 4.3.1 re-run of the seeded harness tests at every release is not in the planned regression set | | finding-2 |
| swe-191 7.1 task 2 | | N/A | No release exists; the first `TC-SW-REG-001` run is at the first release candidate | 04 section 10.5 | none |
| swe-191 7.1 task 3 | | Yes | Risks of the regression set identified: finding-2; TV-022 limitation 1 (the pair is a fixture decision) | | finding-2 |
| swe-191 7.1 task 4 | | N/A | No critical anomaly has been corrected in the tested software | 07 section 12 (NCR route) | none |
| swe-219 7.1 task 1 | SC | Yes | The three SWE-219 elements of 07 section 9.6 (`rmm.json` SWE-219 T) each have a validated tool: independence-pair reporting (K22-4: a masked condition fails exactly its pair test), MSR-13 credit coverage (TV-021), MSR-14 non-credit branch and condition coverage (TV-023 K23-1, K23-2, labelled non-credit in its class row and ACC-NIGHTLY-001). No safety-critical code to cover exists yet | | none |
| swe-201 7.1 tasks 1 and 2 | | N/A | No non-conformance has been raised against these tools; each record names "a defect found in the tool (an NCR per SWE-201)" as a trigger | 07 section 12 | none |

Not applied, with reason: the section 7.1 tasks of the product-type rows `requirements`, `plans`, `design`, `code`, `test`, `ncr` and `mcdc-or-unsafe-audit` are not SWEs these records implement; `swe-187` (items under test under configuration management) is answered as SA-E4 because the TV runs are test executions of tools, not of software items.

### Independent assurance checks

| Check | Method | Result |
|---|---|---|
| Blob identity with INSP-040 and with `main` | `git rev-parse HEAD:<path>` for the 36 `product_files` and 6 `fixture_trees` | all equal to INSP-040 iteration 2 and to HEAD `d566e01` |
| X10 seeded faults fail for the stated reason (TV-022 section 8 reviewer instruction; 03 section 4.3.1) | Hand derivation from `harness-seeded/src/lib.rs` `7f901c95` and `tests/harness.rs` `e62465bc` | `seeded-pair` makes `permit(a, b)` return `a`: `d01_tt` (true, true) passes, `d01_c1_false` (false, true) passes, `d01_c2_false` asserts `!permit(true, false)` = `!true` and fails. `seeded-mock-fault` swaps in `MockOutput::failing_after(1)`: the first `step` returns `Ok(true)`, the second an error, so the `Ok(false)` assertion of `heartbeat_through_mock_toggles` fails; `injected_fault_reaches_the_unit_under_test` uses `failing_after(0)` in both builds and passes. Both are assertion failures (exit 100), not build failures, as K22-4 to K22-6 and the JUnit lists record |
| PASS and FAIL lines of the credit runs | `grep -n 'PASS\|FAIL'` on the r3 log `4e8fc033` | runs 3 and 4: K20-4a/b, K20-5a/b, K21-4a to K21-4d PASS and the SWE-186 PASS line; FAIL lines only in the K21-4 mutation appendix (lines 492 to 507, as intended) and the `seeded_failure` test output |
| No credited use before accreditation (05 section 9.1) | `grep -l '^credit: true' -r docs/vv/reports` | none |
| Commit trailers of the product commits (SA-E3) | `git log --format='%h %s%n  trailers: %(trailers:only,unfold)'` over the product paths | `a3cacee`, `71bf509` parsed `Refs:`; `c28dd60`, `c827202` not parsed (finding-4) |

## Readiness criteria

| # | Criterion | Result | Evidence |
|---|---|---|---|
| R1 | Product committed and frozen; `product_files` equal to the paired record's | Yes | The list is copied from INSP-040 iteration 2 and checked blob by blob against HEAD (table above) |
| R2 | 07 section 2.1.1 row and criticality identified | Yes, with finding-1 | No 07 section 2.1.1 row exists for TV records; routed by PDR work plan WP-PDR-08. Criticality neither: 03 section 4.3.1 host harness row "Not safety-critical; verification software of safety-critical components"; 03 section 4.3 engineering tools neither; 07 section 14.1 line 607 |
| R3 | `validate_docs.py` exits 0 on the product's files; traceability clean for the ids touched | Yes | The four records and the procedures are Markdown and shell outside the validator's JSON conventions; `validate_docs.py` on HEAD before this record: 67 passed, 1 failed, the failure being the SRR record drift of `docs/reviews/SRR/checklists/tool-validation-tv-001-to-tv-010.md` (INSP-040 X-3, not attributable to this product). The product touches no REQ, TC or HZ id (records cite SWE and MSR ids only), so no `--report-only` run is needed and none was made |
| R4 | Paired file review filed under its own invocation; this reviewer independent | Yes | INSP-040 filed (`1b93d83`, `f38159d`); `author_agent` "author:WP-PDR-08 (Claude as software lead and tool owner)", reviewers `reviewer:WP-PDR-08-rust-toolchain` and `-iter2`; this invocation is none of them |

## A. Dispatch, independence and record integrity

| Id | Answer | Evidence |
|---|---|---|
| SA-A1 | Yes, with finding-1 | Routed by PDR work plan WP-PDR-08 (owner-approved 2026-09-27); no 07 section 2.1.1 row; criticality from 03 section 4.3.1 |
| SA-A2 | Yes | Four distinct invocations: author:WP-PDR-08, reviewer:WP-PDR-08-rust-toolchain (iteration 1), reviewer:WP-PDR-08-rust-toolchain-iter2 (iteration 2), sa-reviewer:WP-PDR-08-rust-toolchain (this record). INSP-040 names the SA pair as "pending (separate invocation, PDR work plan WP-PDR-08)"; its reviewer updates it (see "Record verdict") |
| SA-A3 | Yes | Same `product`, `product_commit`, `product_files` and `fixture_trees` as INSP-040 iteration 2; no product change after `c827202` |
| SA-A4 | Yes | INSP-040 applied the TV checklist item set (revision A, CR-012 branch) for `tool_kind` external-tool (sections A to F, G2, H) plus the code checklist items for the fixtures, answered every item with evidence, re-ran the procedure in both iterations, and verified both Majors element by element; `swe-088` 7.1 task 1 criteria a to d met (checklist, readiness R1 to R5 and completion criteria, findings with states and liens, participants recorded) |

## B. SWE-to-task table

| Id | Answer | Evidence |
|---|---|---|
| SA-B1 | Yes | Every task of the row "Every product type", the two tool tasks and the section 7.1 tasks of every governed SWE are in the task table; `assurance_tasks_applied` lists every Yes and No row |
| SA-B2 | Yes | Every N/A row cites the 07 or 04 or 05 section that relieves it; the SC N/A rows (swe-135 tasks 5 and 6) cite 07 section 9.6 and 05 section 13, and the criticality is neither |
| SA-B3 | Yes | The one No row (swe-191 task 1) carries finding-2 |

## C. SWE-134 items a to l

N/A (`criticality: neither`). No SWE-134 provision is implemented by a tool; the tools build and verify the components that carry them. `swe134_items_checked` is empty.

## D. Software safety analysis and hazard traceability

| Id | Answer | Evidence |
|---|---|---|
| SA-D1 to SA-D6 | N/A | The tools are in no hazard's causal chain in `hazards.json` (03 section 4.3.1 "Basis for none": host tools before release, command or detect nothing on the radio, failure mode is a false pass or false closure); the product changes no hazard, control, component or requirement. The compiler's contribution to the image is a product risk carried by RSK-020 and RSK-062 (finding-3). Relief: 07 section 2.1.1 and 03 section 4.3.1 |

## E. Peer review, change and configuration assurance

| Id | Answer | Evidence |
|---|---|---|
| SA-E1 | Yes | INSP-040 finding-1 and finding-2 (Major) Verified at iteration 2 against the new blobs with element tables and a reviewer re-run; finding-3 to finding-8 carried as liens with owner (Claude as software lead and tool owner) and due event (CDR readiness declaration); none closed without evidence |
| SA-E2 | Yes | INSP-040 front matter: `findings_major` 2, `findings_minor` 6, `findings_verified` 2, `effort_turns` 64, `effort_minutes` 90, `iteration` 2; this record carries the same fields |
| SA-E3 | No | finding-4 (`c28dd60`, `c827202` `Refs:` lines not parsed). No `CR:` trailer is required: none of the four tools is Accredited, so row 28 is still Log class for them and the TV records are Record class (05 Table 4-1 rows 28 and 30) |
| SA-E4 | Yes | Every credit run is on a `git archive` export of a named commit (`d3de579`, `c28dd60`) with rustos exported from the pin object `2ec64c0`; no release is claimed |

## F. Assurance risks, metrics and reporting

| Id | Answer | Evidence |
|---|---|---|
| SA-F1 | Yes | Concerns that are not product defects are named as existing risks: RSK-020 and RSK-062 (compiler and supply chain; the re-assessment request of finding-3 goes to the register writer WP-PDR-18 with tag `assurance`), RSK-063 (mock fidelity; the TV-022 scope excludes it), RSK-010 (manual MC/DC; TV-023 is its non-credit cross-check), RSK-009 (NASA-STD-8739.8 tasking not in the corpus). No new risk entry is submitted |
| SA-F2 | Yes | Front matter: `findings_*`, `assurance_findings_*`, `items_no`, `effort_turns`, `effort_minutes` |
| SA-F3 | Yes | Verdict, five Minor liens, tasks applied, reliefs used and the independent checks are in this record alone |

## Concurrence with INSP-040

This record concurs with every answer of INSP-040 iteration 2 (TV items A1 to H3, readiness R1 to R5, code items) and with its reviewer verdict APPROVED with liens finding-3 to finding-8. For TV-H1 and TV-H2 (the swe-136 and swe-070 tasks the TV template gives the file reviewer), the task rows above add: accreditation is still the owner's (OD-24 (b)); the compiler limitation (finding-3); the regression-side X10 obligation (finding-2); the static-analysis due-gate conflict (finding-5). The INSP-040 cross items X-2 (now finding-1 here), X-4, X-5 and X-6 stand.

## Validation

`/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/validate_docs.py` on `main` with this record (HEAD `443b2a3`): the record passes (64 passed, 5 failed, 69 checked). The five failures are SRR records whose products other wave 0 and 1a work packages changed after `d566e01` (`adrs-001-to-025.md`, `process-02-requirements-and-traceability.md`, `trade-studies-ts-001-ts-002.md`, `trade-study-ts-002-software-assurance.md`, by `0f4a7ad`, `11b1b1d`, `443b2a3`) and the pre-existing drift of `tool-validation-tv-001-to-tv-010.md` (INSP-040 X-3); none is attributable to this record or its product. `git diff --stat d566e01 443b2a3` on `docs/cm/tool-validation`, `tools/toolchain.lock.md` and `tools/tests/fixtures/rust` is empty, so every product blob is still equal at HEAD.

## Record verdict

The assurance reviewer's verdict is APPROVED with five Minor liens (finding-1 to finding-5, due the CDR readiness declaration; finding-2 due before the first release candidate). No Major finding is open. The product blobs are on `main`, so the record drift rule would accept an APPROVED record; the record `verdict` stays NEEDS CHANGES because the software lead sets it (07 section 10.2) and two conditions remain: INSP-040's reviewer updates INSP-040 with `paired_record: INSP-048`, `assurance_reviewer_agent` naming this invocation and `assurance_verdict: APPROVED`; and the checklist applied reaches `main` with CR-012 at blob `5b135285` unchanged (lead SE convention of 2026-09-27, as INSP-046). The software lead then sets `verdict: APPROVED` on INSP-040 and on this record in the same commit.

```
ASSURANCE VERDICT: APPROVED (record verdict held NEEDS CHANGES: INSP-040 pairing not yet recorded; SA checklist branch-only, lead SE convention 2026-09-27)
PRODUCT: TV-020@3f11ab13, TV-021@9ce8f956, TV-022@308dcf66, TV-023@dd169983 with fixtures, procedures, logs, lock, README at c827202 (all equal at HEAD d566e01); PAIRED RECORD: INSP-040
PRODUCT TYPE: tool-validation (no 07 section 2.1.1 row; routed by PDR work plan WP-PDR-08); CRITICALITY: neither
FINDINGS:
- [Minor] finding-1 SA-A1: 07 section 2.1.1, the TV template and the PDR work plan disagree on SA routing of credit-tool TV records; TV-020 section 8 cites 07 section 2.1.1 wrongly.
- [Minor] finding-2 swe-191 7.1 task 1: the 03 section 4.3.1 / X10 re-run of the seeded harness tests at every release has no owner or due event in 04 section 10.5, 05 section 8.1 or 07.
- [Minor] finding-3 swe-136 7.1 task 1, SA-F1: no TV-020 check covers target codegen semantics and the limitation is unstated; RSK-020 S1 and RSK-062 need re-assessment.
- [Minor] finding-4 SA-E3: c28dd60 and c827202 Refs lines not parsed as trailers.
- [Minor] finding-5 swe-135 7.1 task 2: 07 section 8.3 (static analysis accredited by PDR) conflicts with 05 section 13 (cargo-audit, cargo-deny, cargo-geiger, rust-code-analysis by CDR); TV-020 Annex A says agree.
TASKS APPLIED: swe-134 7.1 task 5, swe-022 7.1 task 1, swe-136 7.1 task 1, swe-070 7.1 task 1, swe-135 7.1 tasks 1, 2, 7, swe-061 7.1 task 1, swe-186 7.1 task 1, swe-189 7.1 task 1, swe-190 7.1 tasks 1 to 3, swe-191 7.1 tasks 1 and 3, swe-219 7.1 task 1
TASKS N/A (relief): swe-135 7.1 task 3 (07 section 8.4), task 4 (05 section 13 CDR row), task 5 (07 section 9.6), task 6 (05 section 13 CDR row); swe-061 7.1 task 2 (07 section 2.1.1 code row); swe-191 7.1 task 2 (04 section 10.5), task 4 (07 section 12); swe-201 7.1 tasks 1 and 2 (07 section 12)
SWE-134 ITEMS CHECKED: none (criticality neither)
MEASUREMENTS: size=4 TV records, 13 purposes, 23 checks, 34 fixture files; tasks=16 applied, 8 N/A rows; tasks_no=1; turns=38; minutes=60; major=0; minor=5
```
