---
id: INSP-016
checklist: peer-review-checklist-code
checklist_revision: B
checklist_file: docs/reviews/SRR/checklists/fw-b0-toolchain-proof.md
# product: the FW-B0 toolchain proof of 07 sections 3.1 and 3.2 (SRR package section 2 item H12),
# reviewed as one product: the firmware workspace, the gate script, the case and its run 1 report
product: firmware/ (FW-B0 workspace), tools/sw_gate.sh, docs/test_cases/sw-tool/test_cases.json, docs/vv/reports/TC-SW-TOOL-001-r1.md, docs/vv/reports/TC-SW-TOOL-001-r3.md (post-SRR-ruling delta), docs/vv/reports/TC-SW-TOOL-001-r4.md, docs/vv/reports/TC-SW-TOOL-001-r5.md, firmware/unsafe-audit.md (close-out delta), docs/vv/reports/TC-SW-TOOL-001-r6.md (close-out delta 2)
# product_commit: iteration 3 review baseline (committed); product_files lists every reviewed file
# as path@blob from git rev-parse HEAD:<path> (record drift rule, SRR package section 2.3, R13)
product_commit: "738da038d4655caa0dfa4ad7c58383423ab6c50a"
product_files:
  - "docs/test_cases/sw-tool/test_cases.json@fee1e7246af59d5e8a43ed1b9cdf483854053fdc"
  - "docs/vv/reports/TC-SW-TOOL-001-r1.md@04bc3354352139eb30b33fadff43e1c9b61d0d8e"
  - "docs/vv/reports/TC-SW-TOOL-001-r1/blink-rate-prediction.txt@78f1ac59aeaf1254d2e4ba0b6c2c5972cb94d5a9"
  - "docs/vv/reports/TC-SW-TOOL-001-r1/blinky-build.txt@2aa80fcc749a3b2fb5e949341ad7f6344dfaf227"
  - "docs/vv/reports/TC-SW-TOOL-001-r1/cwht-app.elf@6d9965a04a81895a5a2e355e685aa07ae5f65f7a"
  - "docs/vv/reports/TC-SW-TOOL-001-r1/cwht-app.map@e5557024967701cbee3661601e39572bf22afa80"
  - "docs/vv/reports/TC-SW-TOOL-001-r1/cwht-app.uf2@640951c4994cbc5e8a45e8f89eff3879795da144"
  - "docs/vv/reports/TC-SW-TOOL-001-r1/gate-known-answer.sh@eaaca0e699da5312e85c5750e7228cfc1d87a5c4"
  - "docs/vv/reports/TC-SW-TOOL-001-r1/gate-known-answer.txt@df92abe952c77acfbbf48d61a90491be3b9e3fe5"
  - "docs/vv/reports/TC-SW-TOOL-001-r1/host-build-test.txt@ca478c7e9eb0243b0561e744b10165ebf28ee652"
  - "docs/vv/reports/TC-SW-TOOL-001-r1/rustos-blinky.elf@5dd8b02ad79c8544fed5e6059e2a4626bcabe822"
  - "docs/vv/reports/TC-SW-TOOL-001-r1/rustos-blinky.uf2@f0e9fb343ed9c24f0e5b791fc344b51093c48ab9"
  - "docs/vv/reports/TC-SW-TOOL-001-r1/sw-gate-full.txt@3fca1c2c9510e9dfd34b24c71811f703743899d9"
  - "docs/vv/reports/TC-SW-TOOL-001-r1/sw-gate-keep-going.txt@b31755e2afac05c3c217180147f2f04a80ade42c"
  - "docs/vv/reports/TC-SW-TOOL-001-r1/uf2-info.txt@ea4694c2a3fa09a86fc227d32f2fe5edb5a1362e"
  - "docs/vv/reports/TC-SW-TOOL-001-r1/versions.txt@22e56c97597f7dae54d5a9168162a9ffb0fc620a"
  - "firmware/.cargo/config.toml@b677319fa0fe9b62431d01fa8b749bbd7e585b0d"
  - "firmware/.config/nextest.toml@00b81042cf7f73ff6ffa67f013b4c78ef6884a63"
  - "firmware/Cargo.lock@784605ca28b94ea0d3ace66a5797c11cbbced80d"
  - "firmware/Cargo.toml@7799f6b63e26e8fca0c2cb68270c3ff9d7841d05"
  - "firmware/clippy.toml@42020b54612e1bcb2c64149353575b6fa6883d96"
  - "firmware/cwht-app/Cargo.toml@236df1403dc94cc8534e9397d6addc819dc3c053"
  - "firmware/cwht-app/build.rs@41dea79e96a75c4919491630fd5a83978d3c9f18"
  - "firmware/cwht-app/src/main.rs@e32006a582bc49af6b2b12e8856015173210afd0"
  - "firmware/cwht-core/Cargo.toml@3774fca09cead334004aeaa00e07eb2c6ff9d941"
  - "firmware/cwht-core/src/heartbeat.rs@f38b716a57d7e88bdbcb0cc5d20fb270ea75e71f"
  - "firmware/cwht-core/src/lib.rs@01c49f60f82689aab61570e7200bf9bf4064cbd1"
  - "firmware/cwht-core/tests/heartbeat.rs@718a0246da10eec9c8f3be5d939d326e2133cb4c"
  - "firmware/cwht-hal-mock/Cargo.toml@565c5597b2b4e0d4611fd2e1079f653cd4337f41"
  - "firmware/cwht-hal-mock/src/gpio.rs@fc8872bd420ecbd4760d2f2fc05b236ee842c801"
  - "firmware/cwht-hal-mock/src/lib.rs@f5141c137073e0493a455681aa1d5ae18f53db38"
  - "firmware/cwht-hal-mock/tests/gpio.rs@f1b302bcfa7f55105ad73d8b01d98d0fb7901312"
  - "firmware/deny.toml@4cd6de9c2f49c9da254ca05cb31973286c9ac2c8"
  - "firmware/emu/README.md@ae79ea6c77595157c0774a136735191196c03d99"
  - "firmware/rust-toolchain.toml@ca29c2548ff35887352c340bf5c5b49475758ddb"
  - "firmware/rustfmt.toml@dce38290b859775f8e3732df729561b198f991a3"
  - "tools/sw_gate.sh@29a37127312e242bce2aa8f41602e3bcd4360f2f"
  - "docs/vv/reports/TC-SW-TOOL-001-r3.md@f4303e3a47d15a8772406a722e2a38238d6f43c6"
  - "docs/vv/reports/TC-SW-TOOL-001-r3/blink-rate-prediction.txt@1804b53db1ddcf4a0050979eaae999f03a0631e2"
  - "docs/vv/reports/TC-SW-TOOL-001-r3/blinky-build.txt@2ee533929ea482468f61a94d67320f1b4fe1ff88"
  - "docs/vv/reports/TC-SW-TOOL-001-r3/complexity-diagnostic.txt@69233507c79ab2fce0337aac37b87fec47e8fd00"
  - "docs/vv/reports/TC-SW-TOOL-001-r3/cwht-app-build.txt@d439781b7ee14da43ff01ab860f65f633901e509"
  - "docs/vv/reports/TC-SW-TOOL-001-r3/cwht-app.elf@e0d5973ba89b57066d74b60ae8181f64c2aed238"
  - "docs/vv/reports/TC-SW-TOOL-001-r3/cwht-app.map@91d80bef60717035b6ec4b4177233bff78575621"
  - "docs/vv/reports/TC-SW-TOOL-001-r3/cwht-app.uf2@640951c4994cbc5e8a45e8f89eff3879795da144"
  - "docs/vv/reports/TC-SW-TOOL-001-r3/gate-known-answer.sh@9ed69d2d51815c728d2167efb5a6575e26398f1f"
  - "docs/vv/reports/TC-SW-TOOL-001-r3/gate-known-answer.txt@1f6555c860f94cc7d432edaaedbf9eab55544de3"
  - "docs/vv/reports/TC-SW-TOOL-001-r3/host-build-test.txt@600799af98a59bf87f9f7d1a46accf9438123dc4"
  - "docs/vv/reports/TC-SW-TOOL-001-r3/run3.sh@1e6a23e6ada76c63d5f4e4c66aea5e74617881f6"
  - "docs/vv/reports/TC-SW-TOOL-001-r3/rustos-blinky.elf@5c54e3117807190491cef85dfcf6bcfe06f8f984"
  - "docs/vv/reports/TC-SW-TOOL-001-r3/rustos-blinky.uf2@f0e9fb343ed9c24f0e5b791fc344b51093c48ab9"
  - "docs/vv/reports/TC-SW-TOOL-001-r3/rustos-build-test.txt@c43b72e0842fc1bca6bae3b8105656204b31ee54"
  - "docs/vv/reports/TC-SW-TOOL-001-r3/rustup-guard.sh@16d8bb5a3305b74cfbdb7902aec16500ff912fcf"
  - "docs/vv/reports/TC-SW-TOOL-001-r3/sw-gate-full.txt@e0f536d49199de7e290af505a1a1fa1331509699"
  - "docs/vv/reports/TC-SW-TOOL-001-r3/sw-gate-keep-going.txt@4cb525bb3c2d0dcebbf33665b0d0a3597fc158b4"
  - "docs/vv/reports/TC-SW-TOOL-001-r3/uf2-info.txt@5129cb30127041be05223aac813348655947b77c"
  - "docs/vv/reports/TC-SW-TOOL-001-r3/unsafe-audit.txt@31043488252f3a39ba7aed8681181f0831f8a2f7"
  - "docs/vv/reports/TC-SW-TOOL-001-r3/versions.txt@ddf897ceb812164421ca4ce7c7ff45a044b35585"
  - "firmware/unsafe-audit.md@18ef484bf050797e9493d68071efdc0259d423a6"
  - "docs/vv/reports/TC-SW-TOOL-001-r4.md@572c0f946970cc3eaa339f1b27d269cbf81fc76f"
  - "docs/vv/reports/TC-SW-TOOL-001-r4/complexity-invocation-check.sh@dccbb8db2b4e9c83ffedfed4ad2d94dce43ca9e9"
  - "docs/vv/reports/TC-SW-TOOL-001-r4/complexity-invocation-check.txt@6726f9bed05488227536764f1adf00d6d91e9d90"
  - "docs/vv/reports/TC-SW-TOOL-001-r4/image-identity.txt@62d41739bc4e337a05fd582ba930bb2091c229a7"
  - "docs/vv/reports/TC-SW-TOOL-001-r4/kat-target-1byte.elf@1900e53ecdcadb811aec885e21730a0a87ab34fa"
  - "docs/vv/reports/TC-SW-TOOL-001-r4/kat-target.elf@79fbef95a91b8f4cb046edd0cde57d9799fa12ed"
  - "docs/vv/reports/TC-SW-TOOL-001-r4/kat-target.uf2@5f935da3323482fe63b784da374cdcfdbbbec1fb"
  - "docs/vv/reports/TC-SW-TOOL-001-r4/oa2-observation.txt@09a723f3c0f8d9d3c3f7f6d9af1b215d453cb043"
  - "docs/vv/reports/TC-SW-TOOL-001-r4/oa2-verify.txt@b755372d9e2cf5779c9bca9c5254d8bf948053c3"
  - "docs/vv/reports/TC-SW-TOOL-001-r4/step11-info.txt@147eee6eae1392f1bbd9d26abbc1e252ffd6fedc"
  - "docs/vv/reports/TC-SW-TOOL-001-r4/step11-load.txt@2c71e1e6a07d2b8705cbd47c6d6678798aa765f8"
  - "docs/vv/reports/TC-SW-TOOL-001-r4/step11-observation.txt@c72a9eb1e6eb1867868eab4a29ed521fe3b4304d"
  - "docs/vv/reports/TC-SW-TOOL-001-r4/step12-load.txt@fcad3112d3ce318d45d916ff093fc0b2e5be9c13"
  - "docs/vv/reports/TC-SW-TOOL-001-r4/step12-observation.txt@02f85088699f3586845336ac0fd609f91f86707a"
  - "docs/vv/reports/TC-SW-TOOL-001-r5.md@ffe44ed250a5bc0925e738b9342431e5981cef02"
  - "docs/vv/reports/TC-SW-TOOL-001-r5/blink-rate-prediction.txt@639f692af3b4d89f64679be74612f11e13dd9092"
  - "docs/vv/reports/TC-SW-TOOL-001-r5/blinky-build.txt@9c5c2200aebb3504448684771443a8d06ed49e93"
  - "docs/vv/reports/TC-SW-TOOL-001-r5/cwht-app-build.txt@c235e58cea0caec5078110c0599f2034647c7c46"
  - "docs/vv/reports/TC-SW-TOOL-001-r5/cwht-app.elf@436137aa1bd3ca0c8b7db91ec929a91296bccf3c"
  - "docs/vv/reports/TC-SW-TOOL-001-r5/cwht-app.map@a13230fbf2779475acb193d967f625bdbd0097f4"
  - "docs/vv/reports/TC-SW-TOOL-001-r5/cwht-app.uf2@640951c4994cbc5e8a45e8f89eff3879795da144"
  - "docs/vv/reports/TC-SW-TOOL-001-r5/elf-diff.txt@63287580e27fe2516f9ac7128a8eba764e9eda75"
  - "docs/vv/reports/TC-SW-TOOL-001-r5/gate-known-answer.sh@77aef38dd4abb8cf8f4ee4d0695d4acee4b41665"
  - "docs/vv/reports/TC-SW-TOOL-001-r5/gate-known-answer.txt@ac05d9c262c3f9271e16e49239a8a0ab456842ac"
  - "docs/vv/reports/TC-SW-TOOL-001-r5/host-build-test.txt@fee5ff5d09628b4df3e2de42e416c08a829a92a0"
  - "docs/vv/reports/TC-SW-TOOL-001-r5/layout-after.txt@49446fcd965d72615d9979e0f9a2ec2f0e06a107"
  - "docs/vv/reports/TC-SW-TOOL-001-r5/run5.sh@978fb60d88e40dc418ac7e58864c0bab086feeff"
  - "docs/vv/reports/TC-SW-TOOL-001-r5/rustos-blinky.elf@de5b31c3422d5f8537055eac57c26f5212b6b896"
  - "docs/vv/reports/TC-SW-TOOL-001-r5/rustos-blinky.uf2@f0e9fb343ed9c24f0e5b791fc344b51093c48ab9"
  - "docs/vv/reports/TC-SW-TOOL-001-r5/rustup-guard.sh@16d8bb5a3305b74cfbdb7902aec16500ff912fcf"
  - "docs/vv/reports/TC-SW-TOOL-001-r5/sw-gate-full.txt@4de3ad9a38ea6a4a0442f2aef88e5fdeab9f77f7"
  - "docs/vv/reports/TC-SW-TOOL-001-r5/sw-gate-keep-going.txt@4a7c714bcb72b73f5928dfd854a0f5d1d6939ebf"
  - "docs/vv/reports/TC-SW-TOOL-001-r5/uf2-info.txt@f5316c9be006be226821b7930f6720ef2420575b"
  - "docs/vv/reports/TC-SW-TOOL-001-r5/unsafe-audit.txt@130d2e1dac4f6b62a033ece8f1bd5555ad69c5a4"
  - "docs/vv/reports/TC-SW-TOOL-001-r5/versions.txt@3ee8623d5a040217367d2561b81aa777a350d4b1"
  - "docs/vv/reports/TC-SW-TOOL-001-r6.md@8d12b38333b4ae863dc8689eed39658dcc276e68"
  - "docs/vv/reports/TC-SW-TOOL-001-r6/blink-rate-prediction.txt@b53552e4e1af0c7005e4d494d336f8c730e54299"
  - "docs/vv/reports/TC-SW-TOOL-001-r6/blinky-build.txt@e737be2c0b7816172de6c2ac198a9889b9b75f6f"
  - "docs/vv/reports/TC-SW-TOOL-001-r6/cwht-app-build.txt@0a137a3c0b1c976e824b352127e55fdaa9de714f"
  - "docs/vv/reports/TC-SW-TOOL-001-r6/cwht-app.elf@327faade6c7808cdf6f192725105c38570ee2f64"
  - "docs/vv/reports/TC-SW-TOOL-001-r6/cwht-app.map@c4482eb0f5060ff5c202a8bd0a2f7568c4d3899b"
  - "docs/vv/reports/TC-SW-TOOL-001-r6/cwht-app.uf2@640951c4994cbc5e8a45e8f89eff3879795da144"
  - "docs/vv/reports/TC-SW-TOOL-001-r6/download-check.txt@723cf368c0b718fec6e66398b55c6f650ccd6b08"
  - "docs/vv/reports/TC-SW-TOOL-001-r6/elf-diff.sh@48a7d6514b395974e2ab8c57470e78ad17dca823"
  - "docs/vv/reports/TC-SW-TOOL-001-r6/elf-diff.txt@b64b63a1e5950cd59e413fb8a6a6db7e8b8dd415"
  - "docs/vv/reports/TC-SW-TOOL-001-r6/gate-known-answer.sh@4142d8490c33e22c5ad05a53da06324725d0f470"
  - "docs/vv/reports/TC-SW-TOOL-001-r6/gate-known-answer.txt@d265a67b53b16143a4cd2c591804e98d00a88664"
  - "docs/vv/reports/TC-SW-TOOL-001-r6/host-build-test.txt@3036a77e698ac620dab1a651dc0bea334cea3e64"
  - "docs/vv/reports/TC-SW-TOOL-001-r6/layout-after.txt@0f967477ade458f2b195dccc75bd8fd1bfca9cc3"
  - "docs/vv/reports/TC-SW-TOOL-001-r6/run6.sh@84846352709b4c6541cde0a383aeb8ce16965f36"
  - "docs/vv/reports/TC-SW-TOOL-001-r6/rustos-blinky.elf@86894dc5937f2791ddca794ae7228e904c36a76d"
  - "docs/vv/reports/TC-SW-TOOL-001-r6/rustos-blinky.uf2@f0e9fb343ed9c24f0e5b791fc344b51093c48ab9"
  - "docs/vv/reports/TC-SW-TOOL-001-r6/rustup-guard.sh@16d8bb5a3305b74cfbdb7902aec16500ff912fcf"
  - "docs/vv/reports/TC-SW-TOOL-001-r6/sw-gate-full.txt@798b98ccd71e4fa1edf62c5f695faaffd4c0a069"
  - "docs/vv/reports/TC-SW-TOOL-001-r6/sw-gate-keep-going.txt@f1d27b6da53b71b91de6e470e8ab5eec9b3bae54"
  - "docs/vv/reports/TC-SW-TOOL-001-r6/uf2-info.txt@df3d6de2666835f181c89ba368d3547be2abf9ac"
  - "docs/vv/reports/TC-SW-TOOL-001-r6/unsafe-audit.txt@d577ac37ce04569ba22c4af982e621fccbeb8976"
  - "docs/vv/reports/TC-SW-TOOL-001-r6/versions.txt@493876285ec9b1dd7f80ee3031cb97c2c91c0469"
product_size: 8 Rust and 10 TOML files plus Cargo.lock and emu/README.md (678 lines under firmware/, excluding target/); sw_gate.sh 300 lines; test_cases.json 117 lines; report 170 lines with 14 artifacts; run 3 report 203 lines with 20 artifacts (post-SRR-ruling delta); close-out delta: sw_gate.sh 370 lines, run 4 report 179 lines with 13 artifacts, run 5 report 201 lines with 20 artifacts, unsafe-audit.md 54 lines; close-out delta 2: sw_gate.sh 381 lines, run 6 report 261 lines with 22 artifacts
sprint: FW-B0 (07 section 3.2)
author_agent: author:fw-b0 (Claude, software lead; uncommitted working tree on 28e49e6)
reviewer_agent: reviewer:fw-b0
criticality: neither
assurance_required: false
assurance_reviewer_agent: none
iteration: 3
readiness_met: true
reviewer_verdict: APPROVED
assurance_verdict: not-required
verdict: APPROVED
findings_major: 2
findings_minor: 15
findings_open: 0
findings_fixed: 14
findings_verified: 14
findings_deferred: 3
assurance_findings_major: 0
assurance_findings_minor: 0
assurance_tasks_applied: []
unsafe_sites_reviewed: 0
deferred_rids: []
items_no: [CK-CODE-C1, CK-CODE-C4, CK-CODE-C7, CK-CODE-D1, CK-CODE-D9, CK-CODE-G5, CK-CODE-H2, CK-CODE-I4, K5, K6, K7]
effort_turns: 160
effort_minutes: 240
record_status: Open
date: 2026-09-27
date_closed: null
---

# Peer review record INSP-016: FW-B0 toolchain proof

**Checklist:** `docs/templates/peer-review-checklist-code.md` revision B (items CK-CODE-A1 to J4), applied to every Rust file of the workspace, plus reviewer-added section K for the three non-Rust products (gate script, case, report), because no template covers a gate script or a verification report and the assignment names them as one product with the code. **Record format:** 01 section 13 (Peer review record row) and 08 section 3.2. **Scope note (SWE-087 d):** the template asks for one file per review; the assignment defines the FW-B0 set as one product, so each item below names the file it was answered on.

**Verdict (SRR close-out delta, 2026-09-26, at HEAD `3b45ed7`): NEEDS CHANGES.** F-14 (Minor) Closed: the one-`--paths`-per-path fix (`37ae576`) is verified and works inside the gate (run 5); F-01 (Major) stays Open: CR-004 (`5792350`) and close-out item 2 cleared run 3 items B1, B2, B8 and B10, but the run 5 gate on the pinned toolchain and rustos `2ec64c0` still exits 1 (FAIL G5 complexity, B9, an open owner decision under CR-005 section 9; FAIL G5 Miri, B11, the gate's Miri scope), reproduced by this reviewer; two new Minor findings F-15 and F-16 are liens; F-13 stays a lien (section "SRR close-out delta" below). **Verdict (post-SRR-ruling delta, 2026-09-26, at HEAD `5e9506a`): NEEDS CHANGES.** F-02 (Major) Closed on SRR decision 108 (CR-001 Approved, 07 amended at `4364ebb`); F-04 Closed on INSP-028; F-01 (Major) stays Open: decisions 109 and 110 are applied (`b2d3538`) but the gate still exits 1 (section "Post-SRR-ruling delta" below); two new Minor findings F-13 and F-14 are liens. **Verdict (iteration 3, 2026-09-26, at HEAD `adcfe09`): NEEDS CHANGES.** F-01 and F-02 (Major) stay Open on owner rulings (package decisions 108, 109, 110 and owner action OA-1); F-04 (Minor) is a lien; the other nine findings are Closed (section "Iteration 3" below). **Iteration 1 verdict: NEEDS CHANGES.** Two Major findings: the FW-B0 exit criterion of 07 section 3.2 is not met (the gate exits 1, reproduced), and `cwht-app` carries a second decision in target-only code against CS-11 and CS-38 without an approved deviation. Ten Minor findings. The workspace itself is sound: every build, test, format and lint result in the report reproduced exactly, the release ELF rebuilt bit-identical in a separate target directory, all 14 artifact SHA-256 values and the procedure blob match, and all seven gate known-answer runs reproduced.

## Product files (git hash-object, 2026-09-25)

| Blob | File |
|---|---|
| `7799f6b63e26e8fca0c2cb68270c3ff9d7841d05` | `firmware/Cargo.toml` |
| `784605ca28b94ea0d3ace66a5797c11cbbced80d` | `firmware/Cargo.lock` |
| `ca29c2548ff35887352c340bf5c5b49475758ddb` | `firmware/rust-toolchain.toml` |
| `dce38290b859775f8e3732df729561b198f991a3` | `firmware/rustfmt.toml` |
| `42020b54612e1bcb2c64149353575b6fa6883d96` | `firmware/clippy.toml` |
| `4cd6de9c2f49c9da254ca05cb31973286c9ac2c8` | `firmware/deny.toml` |
| `416883d5ce997a47c5586348c7102689b6333915` | `firmware/.cargo/config.toml` |
| `00b81042cf7f73ff6ffa67f013b4c78ef6884a63` | `firmware/.config/nextest.toml` |
| `236df1403dc94cc8534e9397d6addc819dc3c053` | `firmware/cwht-app/Cargo.toml` |
| `41dea79e96a75c4919491630fd5a83978d3c9f18` | `firmware/cwht-app/build.rs` |
| `64b2b3e49e7388d16f4beac22a0d56cbe1954433` | `firmware/cwht-app/src/main.rs` |
| `3774fca09cead334004aeaa00e07eb2c6ff9d941` | `firmware/cwht-core/Cargo.toml` |
| `01c49f60f82689aab61570e7200bf9bf4064cbd1` | `firmware/cwht-core/src/lib.rs` |
| `f38b716a57d7e88bdbcb0cc5d20fb270ea75e71f` | `firmware/cwht-core/src/heartbeat.rs` |
| `718a0246da10eec9c8f3be5d939d326e2133cb4c` | `firmware/cwht-core/tests/heartbeat.rs` |
| `565c5597b2b4e0d4611fd2e1079f653cd4337f41` | `firmware/cwht-hal-mock/Cargo.toml` |
| `f5141c137073e0493a455681aa1d5ae18f53db38` | `firmware/cwht-hal-mock/src/lib.rs` |
| `59b991e2450d16874d845cb957e1d0900e7866e4` | `firmware/cwht-hal-mock/src/gpio.rs` |
| `f1b302bcfa7f55105ad73d8b01d98d0fb7901312` | `firmware/cwht-hal-mock/tests/gpio.rs` |
| `ae79ea6c77595157c0774a136735191196c03d99` | `firmware/emu/README.md` |
| `d74436ab93d20e1ab5889ea4bd1ab12ca5e5b691` | `tools/sw_gate.sh` (SHA-256 `6bae8445...d9473d`, equal to the value in `gate-known-answer.txt`) |
| `04d08adfffce810b6933f42d242ef124f88f4162` | `docs/test_cases/sw-tool/test_cases.json` (equals the report's `procedure_blob`) |
| `3b180d100096a782ce13f4ba2a40470969693f4b` | `docs/vv/reports/TC-SW-TOOL-001-r1.md` |
| `22e56c97597f7dae54d5a9168162a9ffb0fc620a` | `docs/vv/reports/TC-SW-TOOL-001-r1/versions.txt` |
| `ca478c7e9eb0243b0561e744b10165ebf28ee652` | `docs/vv/reports/TC-SW-TOOL-001-r1/host-build-test.txt` |
| `3fca1c2c9510e9dfd34b24c71811f703743899d9` | `docs/vv/reports/TC-SW-TOOL-001-r1/sw-gate-full.txt` |
| `b31755e2afac05c3c217180147f2f04a80ade42c` | `docs/vv/reports/TC-SW-TOOL-001-r1/sw-gate-keep-going.txt` |
| `eaaca0e699da5312e85c5750e7228cfc1d87a5c4` | `docs/vv/reports/TC-SW-TOOL-001-r1/gate-known-answer.sh` |
| `df92abe952c77acfbbf48d61a90491be3b9e3fe5` | `docs/vv/reports/TC-SW-TOOL-001-r1/gate-known-answer.txt` |
| `2aa80fcc749a3b2fb5e949341ad7f6344dfaf227` | `docs/vv/reports/TC-SW-TOOL-001-r1/blinky-build.txt` |
| `5dd8b02ad79c8544fed5e6059e2a4626bcabe822` | `docs/vv/reports/TC-SW-TOOL-001-r1/rustos-blinky.elf` |
| `f0e9fb343ed9c24f0e5b791fc344b51093c48ab9` | `docs/vv/reports/TC-SW-TOOL-001-r1/rustos-blinky.uf2` |
| `6d9965a04a81895a5a2e355e685aa07ae5f65f7a` | `docs/vv/reports/TC-SW-TOOL-001-r1/cwht-app.elf` |
| `640951c4994cbc5e8a45e8f89eff3879795da144` | `docs/vv/reports/TC-SW-TOOL-001-r1/cwht-app.uf2` |
| `e5557024967701cbee3661601e39572bf22afa80` | `docs/vv/reports/TC-SW-TOOL-001-r1/cwht-app.map` |
| `ea4694c2a3fa09a86fc227d32f2fe5edb5a1362e` | `docs/vv/reports/TC-SW-TOOL-001-r1/uf2-info.txt` |
| `78f1ac59aeaf1254d2e4ba0b6c2c5972cb94d5a9` | `docs/vv/reports/TC-SW-TOOL-001-r1/blink-rate-prediction.txt` |

## Reviewer's own runs (2026-09-25 local, 2026-09-26T04:03Z gate time stamps)

All with `RUSTUP_TOOLCHAIN=stable`, `RUSTUP_AUTO_INSTALL=0`; `rustc 1.98.0 (88d9e12ae 2026-08-18)`, equal to the lock rustc row. rustos HEAD `c54d35aa8e7f9ad30f6508bca458a59c1fc009db` (lock row), `api/` and `firmware/` clean before and after.

| Run | Command (in `firmware/` unless stated) | Exit | Result |
|---|---|---|---|
| 1 | `cargo build` | 0 | host crates build |
| 2 | `cargo test` | 0 | 10 passed (5 `cwht-core`, 5 `cwht-hal-mock`), 0 failed |
| 3 | `cargo fmt --check` | 0 | no diff |
| 4 | `cargo clippy --workspace --exclude cwht-app --all-targets -- -D warnings` | 0 | no warning |
| 5 | `cargo clippy -p cwht-app --target thumbv8m.main-none-eabihf -- -D warnings` | 0 | no warning |
| 6 | `cargo build -p cwht-app --release --target thumbv8m.main-none-eabihf` with `CARGO_TARGET_DIR` in the reviewer's scratch directory (clean build) | 0 | FLASH 1608 B (0.04 %), RAM 8200 B (1.54 %); ELF SHA-256 `3992e5d8...80ec1`, identical to the report's `cwht-app.elf`; one rustc warning `linker_messages` (finding-12) |
| 7 | `sh tools/sw_gate.sh` (repo root) | 1 | G0 to G3: 11 PASS; `FAIL G4 traceability` (violations in `docs/requirements/sw/sw-keyer/`, `docs/requirements/tx/`, none in a product file) |
| 8 | `sh tools/sw_gate.sh --keep-going` | 1 | 2 FAIL (G4; G5 cargo deny: `api` and `pico2` unlicensed, `pico2` wildcard path dependency), 9 MISSING, 3 geiger PASS, G6 stable coverage PASS; same result lines as `sw-gate-keep-going.txt` |
| 9 | `sh docs/vv/reports/TC-SW-TOOL-001-r1/gate-known-answer.sh <scratch>` | 0 | KA-0 to KA-6 all MATCH, same first FAIL lines as `gate-known-answer.txt` |
| 10 | clippy on the KA-4 copy | 101 | three distinct errors: `usage of an unsafe block`, `use of a disallowed method core::mem::transmute`, `unnecessary transmute`: the report's "three independent detections" claim holds |
| 11 | `shasum -a 256` on the 14 artifacts; `git hash-object` on the case file | 0 | all 14 equal the front matter; blob equals `procedure_blob` |

Numbers checked against sources: the ring oscillator range 4.6 MHz to 19.6 MHz, nominal 11 MHz (rustos `docs/extracted/rp2350-datasheet.md` lines 37428 to 37429); the delay constant `movw #0x4b40` / `movt #0x4c` = 5 000 000 in `blink-rate-prediction.txt`; the blink windows recomputed (blinky 66 to 132 cycles per 64 spins gives 13.4 to 114.0 per 60 s, nominal 63.0; cwht-app 3 to 6 cycles per spin gives 4.6 to 39.2, nominal 16.5), all equal; `rust-size` sections 272 + 20 + 1316 = 1608 B, equal to the linker FLASH figure; the gate memory limits 70 % and 75 % used equal the TPM-010 red line "below 30 %" unused and the TPM-011 red line "below 25 %" unused (`docs/plan/tpm.json`); the three requirement statements of the report section 1 equal `docs/requirements/sys/requirements.json` (REQ-SYS-127 and 128 Inspection, REQ-SYS-133 Demonstration, all Draft); "rule 7.3.12" and the `SUPPORT` row resolve in `docs/process/04-verification-and-validation.md` (lines 83, 124, 251, 283).

## Readiness criteria

| # | Criterion | Answer | Evidence |
|---|---|---|---|
| R1 | Gate G1 passes on the crates | Yes | runs 3 to 5 above |
| R2 | File at most 500 lines; functions at most 60 lines | Yes | largest file `cwht-hal-mock/src/gpio.rs` 135 lines; clippy `too_many_lines` at threshold 60 (`clippy.toml:2`) passes |
| R3 | The design unit is Active and named in `// @design` | No | no software design exists before PDR (`docs/design/software-design.md` is a CDR product, 07 section 3.1); the tags `cwht-core/heartbeat`, `cwht-hal-mock/gpio`, `cwht-app/main` name units that no design document defines. Inherent to FW-B0, so no finding is raised; this is why `readiness_met` is false. **Post-SRR-ruling delta (2026-09-26):** waived by the owner, SRR decision 115 (b) (owner ruling 2026-09-26), recorded in 07 section 10.2 readiness row at `4364ebb` (blob `37d472b5`) for this record only; the waived criterion counts as met, so `readiness_met` is now true |
| R4 | `@req` tag for every requirement assigned | N/A | the brief assigns no `REQ-SW-*` (`heartbeat.rs:7-8`) |
| R5 | Test author's file exists | Yes, with finding-4 | `cwht-core/tests/heartbeat.rs`, `cwht-hal-mock/tests/gpio.rs` |
| R6 | `tools/unsafe_audit.py --check` for `pico2` or `api` | N/A | no rustos file is in this product; rustos is read only |

## Participants

Author agent `author:fw-b0` (absent). Reviewer agent `reviewer:fw-b0`. Software assurance reviewer not required: no file contains `unsafe` and no file belongs to a component of 07 section 14.1 (`criticality: neither`). Owner for dispositions.

## A. Environment, dependencies and build

| Id | Answer | Evidence |
|---|---|---|
| CK-CODE-A1 | Yes | `cwht-core/src/lib.rs:13`, `cwht-hal-mock/src/lib.rs:11`, `cwht-app/src/main.rs:10-11` (`#![no_std]`, `#![no_main]`); grep for `alloc`, `std::`, `Box`, `Vec`, `String`, `format!` finds only `build.rs:8-9` (`std::env`, `std::path`), which is a host build script, not image code; gate G2 allocator-symbol check PASS |
| CK-CODE-A2 | Yes | dependencies are `api`, `pico2` (rustos by path) and the workspace crates only (`Cargo.lock`, 5 packages); `deny.toml:23-29` denies every other crate; gate G2 image dependency set PASS |
| CK-CODE-A3 | Yes | no `#[cfg` and no `debug_assert!` in any `.rs` file |

## B. Unsafe code

| Id | Answer | Evidence |
|---|---|---|
| CK-CODE-B1 | Yes | workspace lint `unsafe_code = "forbid"` (`Cargo.toml:30`) and `#![forbid(unsafe_code)]` in each crate root and in `build.rs:6`; grep finds no `unsafe` block; geiger `:)` for all three crates (run 8) |
| CK-CODE-B2 to B8 | N/A | no `unsafe` in the product; no `pico2` or `api` file in scope; no `static mut` (`static_mut_refs = "deny"`, `Cargo.toml:32`); CS-10 functions banned in `clippy.toml:4-16` and shown effective by run 10 |

## C. Panics, errors and arithmetic

| Id | Answer | Evidence |
|---|---|---|
| CK-CODE-C1 | No | no `unwrap`, `expect`, `panic!`, indexing or slicing in source (`gpio.rs:59` uses `get(..).unwrap_or(&[])`); but `main.rs:36-38` adds a second halt arm, `let Ok(mut led) = gpio.output_from_handle(..) else { safe_state_halt() }`, beyond the single board `take()` arm CS-11 permits (finding-2) |
| CK-CODE-C2 | Yes | `Heartbeat::step` returns `Result<bool, P::Error>` (`heartbeat.rs:48`); `MockGpioError` is a module enum (`gpio.rs:12-15`); `main.rs:42` `let Ok(_level) = ..` is irrefutable because `Rp2350GpioOut` has `Error = Infallible` (rustos `firmware/pico2/src/gpio/gpio.rs`), so no error is dropped; no `let _ =` on a `Result` |
| CK-CODE-C3 | N/A | no design error table exists (R3); the one error enum has one variant used only by tests |
| CK-CODE-C4 | No | `gpio.rs:77` `checked_sub(1)` and `gpio.rs:83` `saturating_add(1)` carry no comment on the choice CS-14 asks for (finding-5); `for _ in 0..count` (`heartbeat.rs:61`) has no arithmetic |
| CK-CODE-C5 | Yes | no `as` cast in any `.rs` file; `as_conversions = "deny"` (`Cargo.toml:48`) |
| CK-CODE-C6 | Yes | no `f32` or `f64` in any file (none is safety-critical in any case) |
| CK-CODE-C7 | No | `main.rs:56-59`: the panic handler only halts; it writes no safe-state register, records no marker and requests no watchdog reset (CS-12). FW-B0 has no safe-state outputs, which the comment says, but no deferral to a gate is recorded (finding-3) |

## D. Structure, complexity and target platform rules

| Id | Answer | Evidence |
|---|---|---|
| CK-CODE-D1 | No | no G5 complexity output exists: `rust-code-analysis-cli` is not installed and `tools/complexity_gate.py` is not written (run 8, two MISSING lines); clippy `cognitive_complexity` at 15 passes, which is not the CS-17 measure (finding-1) |
| CK-CODE-D2 | Yes | loops: `main.rs:40` main loop, `main.rs:50` halt loop, `heartbeat.rs:61` over `0..count`; no recursion |
| CK-CODE-D3 | Yes | no `match` on an enum in `cwht-core`; `gpio.rs:75-79` matches an `Option<u32>` with explicit arms and no `_ =>`; `wildcard_enum_match_arm = "deny"` |
| CK-CODE-D4 | Yes | no `#[allow]` or `#[expect]`; shadow lints denied (`Cargo.toml:50-52`) and clippy clean |
| CK-CODE-D5 | N/A | no interrupt handler |
| CK-CODE-D6 | Yes | nothing references core 1 |
| CK-CODE-D7 | Yes | longest function `MockOutput::write` 14 lines; nesting depth at most 3 |
| CK-CODE-D8 | N/A | no NVIC, IO_BANK0 interrupt, PWM or TICKS access in the product; GPIO goes through the rustos driver |
| CK-CODE-D9 | No | `main.rs` is tagged `// @target-only` (line 2) and holds two decisions (the `take()` match and the `output_from_handle` match), so its cyclomatic complexity is 3 against the CS-38 limit of 1 plus the `take()` match; the report section 9 item 5 raises the rule conflict as a recommendation only, with no CR or deviation (finding-2) |

## E. Correctness against design and requirements

| Id | Answer | Evidence |
|---|---|---|
| CK-CODE-E1 | N/A | no design to compare (R3); the behaviour matches the file's own contract: `Heartbeat::step` toggles and keeps the level on a failed write (`heartbeat.rs:48-53`, test `failed_write_keeps_level_and_retries_same_transition`) |
| CK-CODE-E2 | Yes | the one constant `BLINK_HALF_PERIOD_SPINS` (`heartbeat.rs:20`) carries its unit in the name and its source in the doc comment; no requirement value applies |
| CK-CODE-E3 to E8 | N/A | no keyer, register, guard, I/O read-back, `safe_state()` or integrity code in FW-B0 |
| CK-CODE-E9 | Yes | every public item is used by `cwht-app` or by a test; `MockInput` is test tooling exercised by `input_reads_set_level_and_injected_fault` |

## F. Traceability tags

| Id | Answer | Evidence |
|---|---|---|
| CK-CODE-F1 | Yes | `// @design` headers at `main.rs:1`, `heartbeat.rs:1`, `gpio.rs:1`; correctness against a design cannot be judged before the design exists (R3) |
| CK-CODE-F2 | N/A | no requirement assigned |
| CK-CODE-F3 | Yes | the units are the FW-B0 infrastructure that 07 section 3.2 names ("Workspace skeleton ... blinky"); the files state that they implement no `REQ-SW-*` (`heartbeat.rs:7-8`, `cwht-core/tests/heartbeat.rs:1-2`) |

## G. Secure coding

| Id | Answer | Evidence |
|---|---|---|
| CK-CODE-G1 | N/A | no external input in FW-B0 |
| CK-CODE-G2 | N/A | no key line |
| CK-CODE-G3 | Yes | `HISTORY_CAPACITY` named (`gpio.rs:8`); writes past capacity are dropped through `get_mut` (`gpio.rs:81`) |
| CK-CODE-G4 | N/A | no diagnostic interface, no event log |
| CK-CODE-G5 | No | the G5 output shows `FAIL G5 cargo deny` and MISSING for `cargo audit`, deny advisories, unsafe audit, complexity and Miri (run 8); zero findings is not shown (finding-1) |

## H. Tests and testability

| Id | Answer | Evidence |
|---|---|---|
| CK-CODE-H1 | Yes | `Heartbeat::step` is generic over `api::common::Write<bool>`; `spin_wait` takes the spin action as a closure, so the host test counts calls (`heartbeat.rs:60`); no `RegAddr` in `cwht-core` |
| CK-CODE-H2 | No | tests pass twice with identical result sets (run 7, G3), but both test files were written by the code author (report section 2: "Claude created the firmware workspace"; author summary) (finding-4) |
| CK-CODE-H3 | N/A | no safety-critical file |

## I. Documentation and style

| Id | Answer | Evidence |
|---|---|---|
| CK-CODE-I1 | Yes | `missing_docs = "deny"` for every member (`Cargo.toml:31`, `[lints] workspace = true` in each crate); every `pub` item has a doc comment; clippy clean |
| CK-CODE-I2 | Yes | `BLINK_HALF_PERIOD_SPINS`, `HISTORY_CAPACITY`, `writes_before_fault` carry units or meaning |
| CK-CODE-I3 | Yes | runs 3 to 5 |
| CK-CODE-I4 | Yes | comments state reasons (for example `main.rs:22-24` on the private `entry` module, `main.rs:41` on the irrefutable pattern); no commented-out code. **Post-SRR-ruling delta (2026-09-26): No at HEAD `5e9506a`** (finding F-13: the reason stated at `main.rs:36-40` became false with SRR decision 108) |

## J. Common review traps

| Id | Answer | Evidence |
|---|---|---|
| CK-CODE-J1 | Yes | `Rp2350::take`, `Rp2350Gpio::new`, `output_from_handle`, `board.pins.led`, `pico2::entry!` exist in rustos `c54d35a` (target clippy and build compile against them, runs 5 and 6) |
| CK-CODE-J2 | Yes | `pin.write(next)` (`heartbeat.rs:50`), `gpio.output_from_handle(..)` (`main.rs:36`) are trait calls |
| CK-CODE-J3 | N/A | no compound requirement |
| CK-CODE-J4 | Yes | line counts measured with `wc -l` (678 lines under `firmware/` excluding `target/`, 20 files) |

## K. Reviewer-added checks: gate script, case and report (not template items)

| Id | Check | Answer | Evidence |
|---|---|---|---|
| K1 | Every build, test and lint result claimed in the report reproduces | Yes | runs 1 to 6, 11 |
| K2 | The gate result lines claimed in the report reproduce, including the counts (11 PASS through G3; 9 MISSING) | Yes | runs 7 and 8 |
| K3 | The known-answer runs reproduce and discriminate | Yes | runs 9 and 10 |
| K4 | Artifact hashes and procedure blob match; the release image is reproducible | Yes | run 11; run 6 rebuilt the ELF bit-identical in a clean target directory |
| K5 | The FW-B0 content and exit criteria of 07 section 3.2 are met | No | gate exit 1; `tools/emu_run.sh` (a FW-B0 deliverable of 07 section 1.2 row "Scripts"), `tools/unsafe_audit.py`, `tools/complexity_gate.py`, `tools/measurements.py` not written; section 8 tools not all installed; `tools/toolchain.lock.md` section 1.1 sanity checks for rustc and cargo, nextest, llvm-cov, audit, deny, geiger, binutils and picotool read "not yet run"; steps 11 and 12 Pending owner (finding-1) |
| K6 | The gate script is robust and its header matches its behaviour | No | findings 6 and 7 |
| K7 | Every claim in the report is backed by a cited artifact and every deviation from the plan is recorded | No | findings 8 to 11 |
| K8 | The case meets the dev-board rule of 04 section 4: `type` Bench, `Article: pico2-devboard-1.`, `Credit: false (dev-board run, charter section 3).`, `Credit row: SUPPORT.`, and the `Configuration:`, `Safety:`, `Environment:` lines; numeric acceptance criteria; named artifacts | Yes | `docs/test_cases/sw-tool/test_cases.json:13-14, 31, 36-113`; `validate_docs.py` passes the file |
| K9 | The report records the run honestly: `result: Blocked`, `credit: false`, no requirement status changed, no NCR needed for an absent prerequisite | Yes | report front matter lines 8-9 and sections 7 and 9 |
| K10 | rustos is unmodified | Yes | `git -C /Users/robinonsay/rust/rustos status --porcelain -- api firmware Cargo.toml Cargo.lock .cargo` empty; HEAD equals the lock row |

## Findings

| Finding | Origin | Severity | Item | Location | Description | State | Disposition |
|---|---|---|---|---|---|---|---|
| F-01 <a id="finding-1"></a>finding-1 | reviewer | Major | K5, CK-CODE-D1, CK-CODE-G5 | `tools/sw_gate.sh` result; 07 section 3.2 row FW-B0; 07 line 28 | The FW-B0 exit criterion is not met: `tools/sw_gate.sh` exits 1 in both modes (reproduced: FAIL G4, FAIL G5 cargo deny, 9 MISSING), so SRR package item H12 and criterion row 20 stay Not met. Four of the gaps are software-lead deliverables that need no download: `tools/emu_run.sh` (07 section 1.2 says it is written in FW-B0 as the SKIP-line stub), `tools/unsafe_audit.py`, `tools/complexity_gate.py`, `tools/measurements.py`. The rest need owner-approved installs (pinned 1.98.0, `miri` and `llvm-tools` on `nightly-2026-08-24`, `rust-code-analysis-cli`, RustSec database), the rustos manifest change for cargo deny, and a clean repository-wide traceability run for G4. The second exit criterion (lock lists every tool with version and sanity-check result) is also not met. Fix: write the four scripts; obtain the owner's approval for the installs and record them in the lock; run and record the lock section 1.1 sanity checks; re-run the gate to exit 0 and file run 2 after steps 11 and 12 | Open | Open (iteration 2). Not addressed in the author return: none of `tools/emu_run.sh`, `tools/unsafe_audit.py`, `tools/complexity_gate.py`, `tools/measurements.py` exists, the lock sanity checks are not recorded and the gate is not shown to exit 0 in full mode (the reviewer `--keep-going` run KA-8 still lists 9 MISSING). Major stays Open. **Iteration 3: Open, owner ruling needed (decisions 109 and 110, OA-1).** The four scripts are committed at HEAD; reviewer run IT3-1 exits 1 with 2 FAIL (G5 cargo deny; G5 unsafe audit, 36 rustos sites without CS-06 SAFETY comments) and 5 MISSING; lock section 1.1 rows for cargo-llvm-cov, nightly, cargo-nextest, cargo-audit, cargo-deny, cargo-geiger, cargo-binutils still read "not yet run" (`tools/toolchain.lock.md:69-75`) **SRR close-out delta (2026-09-26, HEAD `3b45ed7`): Open.** B1 and B2 closed by CR-004 (`5792350`: lock pin `2ec64c0`, `firmware/unsafe-audit.md` regenerated), B8 by the F-14 fix (`37ae576`), B10 by close-out item 2, B7 by run 4; the run 5 gate on the pinned `1.98.0` and rustos `2ec64c0` exits 1 with FAIL G5 complexity (CS-38 `cwht-app/src/main.rs:30 main CC 4 > 3`, B9, owner decision of CR-005 section 9) and FAIL G5 Miri (`pico2` does not compile for the Mach-O host, B11; F-15); both reproduced by the reviewer on a clean `git archive` export (CO-3, CO-5) |
| F-02 <a id="finding-2"></a>finding-2 | reviewer | Major | CK-CODE-C1, CK-CODE-D9 | `firmware/cwht-app/src/main.rs:36-38` | Target-only code holds a second decision, the `output_from_handle` `let ... else` halt arm, which CS-11 (only the `take()` `None` arm) and CS-38 (straight-line except the `take()` match) do not permit; the rustos driver returns `GpioError`, so the arm is needed, and the report (section 9 item 5) proposes changing the rules, but no CR or recorded deviation covers the code as filed (charter section 11 rule 5). Fix: an owner-dispositioned CR amending CS-11 and CS-38 to admit driver-construction failure arms that call `safe_state_halt()`, or an entry in `docs/cm/deviations.md`, cited by a comment at `main.rs:36` | Verified | Open (iteration 2). Partly addressed: `main.rs:36-40` now cites deviation D8, recorded in report section 2 line 71 and section 9 item 5. The fix asked for an owner-dispositioned CR or an entry in `docs/cm/deviations.md`; neither exists (`docs/cm/` holds only `tool-validation/`, no `cr/` folder and no `deviations.md`). A deviation written in the run report by the author is not an approved deviation (charter section 11 rule 5; 07 section 10.2 action tracking). Author agrees it closes on the owner disposition. Major stays Open. **Iteration 3: Open, owner ruling needed (decision 108).** `main.rs:36-40` now cites `docs/cm/cr/CR-001-cs11-cs38-driver-construction-arms.md`, but CR-001 front matter reads `status: Submitted`, `disposition: null` (lines 4, 18) and `docs/cm/deviations.md` does not exist at HEAD **Post-SRR-ruling delta (2026-09-26): Closed on SRR decision 108 (owner ruling 2026-09-26).** CR-001 front matter `status: Dispositioned`, `disposition: Approved`, `disposition_date: 2026-09-26` and section 7 Decision Approved, Class II (`4364ebb`, blob `0f4cca4c`); 07 CS-11, CS-12 and CS-38 amended as CR-001 section 1 items 1 to 3, with the section 1.2 `cwht-app` row and the section 8.2 complexity row (`4364ebb`, 07 blob `37d472b5`, revision A.5). The amended CS-11 admits exactly the construct at `main.rs:41-43` (`let Ok(mut led) = gpio.output_from_handle(..) else { safe_state_halt() }`, nothing else in the failure branch); the amended CS-38 admits it within a per-file allowance; the comment at `main.rs:36-40` cites CR-001. The fix the finding asked for is in place. The stale wording of that comment is new finding F-13 (Minor) |
| F-03 <a id="finding-3"></a>finding-3 | reviewer | Minor | CK-CODE-C7 | `firmware/cwht-app/src/main.rs:55-59` | The panic handler halts only; CS-12 content (safe-state registers, marker, watchdog reset) is absent. Acceptable for a board with no safe-state outputs, but the deferral is recorded only in a doc comment. Fix: record the deferral with its gate (FW-B1 sprint record or package open-items list) and cite it in the comment | Verified | Closed. `main.rs:60-64` cites deferral FD-1; report section 9 deferral table row FD-1 (line 170) names CS-12, the gate FW-B1 and the evidence. Adding FD-1 to the package open-items list remains a cross item |
| F-04 <a id="finding-4"></a>finding-4 | reviewer | Minor | CK-CODE-H2 | `firmware/cwht-core/tests/heartbeat.rs`, `firmware/cwht-hal-mock/tests/gpio.rs` | Both test files were written by the author of the code they test (charter section 2 and section 11 rule 4). No requirement is verified by them, which keeps this Minor. Fix: have an independent test-author invocation review or replace the tests, or have 07 section 3.2 state that FW-B0 toolchain-proof tests are exempt | Verified | Open (iteration 2). Not addressed in the author return; no independent test-author review exists and 07 section 3.2 carries no exemption. **Iteration 3: Lien: fix before PDR** (convergence rule of 2026-09-26; package item R4, Routine). Both test files are unchanged at HEAD (blobs `718a0246`, `f1b302bc`) **Post-SRR-ruling delta (2026-09-26): Closed; lien L-016-1 discharged.** The fix's first option is met: INSP-028 (`docs/reviews/SRR/checklists/fw-b0-tests-test-author.md`), an independent test-author invocation, reviewed both files at the blobs this record names (`718a0246`, `f1b302bc`, unchanged at HEAD `5e9506a`) and returned `verdict: APPROVED` with 0 Major findings; its four Minor liens are carried by INSP-028, not here |
| F-05 <a id="finding-5"></a>finding-5 | reviewer | Minor | CK-CODE-C4 | `firmware/cwht-hal-mock/src/gpio.rs:77, 83` | `checked_sub(1)` and `saturating_add(1)` carry no comment on why that arithmetic form was chosen (CS-14). Fix: one comment per site (the `Some(0)` arm makes the `checked_sub` total; `len` cannot pass `HISTORY_CAPACITY` because `get_mut` gates the increment) | Verified | Closed. `gpio.rs` `write`: one CS-14 comment above the `checked_sub` arm and one above the `saturating_add`; both reasons are correct (the `Some(0)` arm returns first; `get_mut` succeeding bounds `len`). `cargo fmt --check` exit 0 and reviewer KA-0 clippy PASS |
| F-06 <a id="finding-6"></a>finding-6 | reviewer | Minor | K6 | `tools/sw_gate.sh:176-189` | When a nextest run fails, the `cp` to `runN-junit.xml` is skipped but the comparison step still reads `run1-junit.xml` and `run2-junit.xml`, which may be left from an earlier invocation; in `--keep-going` mode the line `PASS G3 identical result sets` can then print against stale files (the overall gate still fails). Fix: `rm -f` both files before the loop and fail the comparison when either is absent or older than the run | Verified | Closed. `sw_gate.sh:235` removes both copies; lines 245-246 fail the comparison when either is absent. Reviewer KA-8 (stale identical `run1/run2-junit.xml` planted, failing test seeded, `--keep-going`): stale files removed, `FAIL G3 identical result sets (JUnit file of run 1 or run 2 not written by this invocation)`, exit 1 |
| F-07 <a id="finding-7"></a>finding-7 | reviewer | Minor | K6 | `tools/sw_gate.sh:21-23` versus lines 129, 133, 155, 165; case step 6 | The header says `--keep-going` "runs G1 to G6 past a FAIL" and names only G0 as stopping, and case step 6 says it "runs every step", but G2 build, link-map presence, `rust-nm` and `cargo tree` failures call `fatal()` and stop the script. Fix: document the G2 stops in the header and the case, or convert them to `fail()` where the later steps can still run | Verified | Closed. `fatal()` now appears only at setup (line 89) and G0 (lines 94-119); every G2 check uses `fail()` and the ELF, map and `rust-nm` steps are gated on `G2_BUILT` (lines 133-218); header lines 26-30 and case step 6 state that only setup and G0 failures stop the script |
| F-08 <a id="finding-8"></a>finding-8 | reviewer | Minor | K7 | report section 2 deviations; `tools/sw_gate.sh:4-5, 21` | The gate adds a G0 toolchain-identity step that 07 section 8.4 and Annex C do not list, and `--quick` runs G0 to G3 where 07 section 8.4 says G1 to G3; deviations D1 to D5 do not record this. Fix: add a deviation to the report and raise the 07 section 8.4 update (cross item) | Verified | Closed. Deviation D7 in report section 2 (line 70) and gate header lines 21-22; the 07 section 8.4 and Annex C update stays a cross item |
| F-09 <a id="finding-9"></a>finding-9 | reviewer | Minor | K7 | report section 5, "Reproducibility" | The statement that the cwht-app UF2 was identical before and after a rebuild that changed only debug information cites `uf2-info.txt`, which records one set of hashes and no rebuild (charter section 11 rule 2). The reviewer's clean rebuild (run 6) did reproduce the ELF bit for bit, so the claim can be evidenced. Fix: record the rebuild and both hashes in an artifact, or delete the sentence | Verified | Closed. Report section 5 "Reproducibility" (line 130) now claims rebuild identity for the blinky only, backed by `blinky-build.txt` (two identical SHA-256 `ef16271d...`), cites reviewer run 6 for cwht-app, and assigns the cwht-app rebuild record to run 2 |
| F-10 <a id="finding-10"></a>finding-10 | reviewer | Minor | K7 | report sections 2 and 3; 07 section 3.2 row FW-B0 | 07 asks for a "blinky on the cwht pin map"; `cwht-app` drives the Pico 2 on-board LED (GPIO25) because the pin map (`docs/icd/ICD-CTL-SW.md`, a PDR product, 07 row o) does not exist (`docs/icd/` is empty). The substitution is sound but is not recorded as a deviation. Fix: add it to the deviation list | Verified | Closed. Deviation D6 (report line 69), configuration note (line 79) and deferral FD-2 (line 171) |
| F-11 <a id="finding-11"></a>finding-11 | reviewer | Minor | K7 | report section 1 (REQ-SYS-128 row) and section 9; `tools/toolchain.lock.md` cargo-llvm-cov row | The report cites 100 percent line and region coverage, while the lock's cargo-llvm-cov row says its TV is due "before FW-B0 coverage is cited". The report does label all output as developer evidence (section 3), so the conflict is one of wording. Fix: mark the coverage figure at each citation as developer evidence pending the cargo-llvm-cov TV, or file that TV first | Verified | Closed. Every coverage citation (report lines 55, 93, 127, 155) carries the developer-evidence and cargo-llvm-cov TV pending label |
| F-12 <a id="finding-12"></a>finding-12 | reviewer | Minor | K6 | `firmware/.cargo/config.toml:9` | `--print-memory-usage` makes every target build emit the rustc warning `linker_messages` (reproduced in run 6), so the G2 log always carries a warning and a new build warning would not stand out; G1 checks clippy only. Fix: take the memory figures from the link map (measurements.py) and have G2 fail on any compiler warning other than a documented expected one | Verified | Closed. `--print-memory-usage` removed (`.cargo/config.toml`, blob `b677319f`); G2 fails on any `^warning` line (`sw_gate.sh:142-149`) and takes memory from the link map and `link.ld` MEMORY. Reviewer KA-0: no warning line, FLASH 1608 B (0.04 %), RAM 8200 B (1.54 %), equal to run 1; reviewer KA-7 (`cargo:warning` in `build.rs`): `FAIL G2 no compiler warning`, exit 1 |
| F-13 <a id="finding-13"></a>finding-13 | reviewer (post-SRR-ruling delta) | Minor | CK-CODE-I4 | `firmware/cwht-app/src/main.rs:36-40` | The comment above the driver-construction arm is stale after SRR decision 108: it still says the arm is "outside CS-11 and CS-38 as written", cites deviation D8 as the record, and says "owner disposition before FW-B1"; since `4364ebb` CR-001 is Approved and the amended CS-11 and CS-38 admit the arm, so the comment now states the opposite of the governing rule (the run 3 report section 2 D8 and section 11 say the same). No behaviour is affected. Fix: CR-001 step 2 (section 5 table): reword the comment to cite CR-001 as Approved and the amended CS-11, with the `CR: CR-001` trailer; this record verifies it | Lien | **Lien: fix before PDR** (convergence rule of 2026-09-26; CR-001 step 2, software lead). New in the post-SRR-ruling delta |
| F-14 <a id="finding-14"></a>finding-14 | reviewer (post-SRR-ruling delta) | Minor | K6 | `tools/sw_gate.sh:316` | The G5 complexity step passes three paths to one `--paths` option; `rust-code-analysis-cli` 0.0.25 accepts one value per occurrence, so since the decision 109 install the step always fails on an argument error before any function is measured (reproduced: exit 2, "Found argument '../rustos/api' which wasn't expected"). The gate fails safe (FAIL, not a false PASS), which keeps this Minor, but the gate cannot exit 0 until it is fixed, so F-01 cannot close before it. Fix: one `--paths` per path (run 3 recommendation 3), with a known-answer run showing the step reaches `tools/complexity_gate.py` | Verified | **Lien: fix before PDR, and before F-01 can close** (convergence rule of 2026-09-26). New in the post-SRR-ruling delta **SRR close-out delta (2026-09-26): Closed (Verified); lien L-016-3 discharged.** `37ae576` changes `tools/sw_gate.sh` (blob `54b13800` to `52b9f803`) only at the G5 complexity invocation: `--paths "$FW" --paths "$RUSTOS/api" --paths "$RUSTOS/firmware/pico2"` plus a two-line comment citing this finding. Reviewer CO-4: the superseded form still exits 2 with the argument error; the fixed form reads all three roots and reaches `tools/complexity_gate.py` (MSR-17 functions 52); run 4 `complexity-invocation-check.txt` shows the seeded CC 17 function caught under each root, and run 5 `sw-gate-full.txt` shows the step integrated in the gate |
| F-15 <a id="finding-15"></a>finding-15 | reviewer (SRR close-out delta) | Minor | K6 | `tools/sw_gate.sh:326` (G5 Miri step) | The gate runs `cargo +nightly-2026-08-24 miri test -p api -p pico2 --lib` on the host, but `pico2` is target-only: its two `#[unsafe(link_section = ...)]` statics (`rustos/firmware/pico2/src/lib.rs:149` `.boot_info`, `:539` `.vector_table`) are ELF section names that the Mach-O host rejects (`error: invalid Mach-O section specifier`), so the step always fails. 07 section 8.1 (Miri row) scopes Miri to "the host tests of `api` and of the host-compilable `pico2` decision functions (CS-38)", and `pico2` has none today; the command is wider than the plan. The gate fails safe (FAIL, not a false PASS), which keeps this Minor, but the gate cannot exit 0 until it is fixed, so F-01 cannot close before it (run 5 item B11). Fix: narrow the step to the host-compilable crates of 07 (for example `-p api` until `pico2` has host-compilable decision functions), or, as the owner's act as rustos maintainer, gate the two `link_section` attributes to the target with `cfg_attr` and move the pin by CR; then a known-answer run and a gate re-run | Lien | **Lien: fix before PDR, and before F-01 can close** (convergence rule of 2026-09-26). New in the SRR close-out delta; reproduced by reviewer CO-5 |
| F-16 <a id="finding-16"></a>finding-16 | reviewer (SRR close-out delta) | Minor | K6 | `tools/sw_gate.sh:117-121` (G0 rustos identity) against `tools/toolchain.lock.md` section 3 `rustos` row (CR-004) | Since CR-004 the lock row says every build, audit and gate for the record reads a `git archive` export of the pinned commit and names `git -C /Users/robinonsay/rust/rustos rev-parse master` as the command, while G0 runs `git -C "$RUSTOS" rev-parse HEAD` and `git status` on `../rustos`, which an export has no metadata for (`rustos HEAD none`, fatal). No gate run for the record can follow the lock rule as written: run 5 substituted a local clone at `2ec64c0` whose tree it showed equal to the export (deviation D20). The substitution is sound and disclosed, so this is Minor. Fix: give G0 a documented export mode (for example compare a recorded tree hash of the export with `git rev-parse 2ec64c0^{tree}`), or amend the lock rule to name the clone method of run 5 D20 | Lien | **Lien: fix before PDR** (convergence rule of 2026-09-26). New in the SRR close-out delta (run 5 recommendation 4) |

## Cross items (outside this product; for the owners of those files)

- `tools/toolchain.lock.md` section 1.2 row `tools/sw_gate.sh` still reads "not written"; the rustup row (line 16) says the `firmware/` pin is "not yet committed". Update both as Log changes.
- `docs/process/07-software-engineering-plan.md` section 8.4 and Annex C: add G0 and the `MISSING` exit status 3; reconcile the FW-B0 need for `tools/unsafe_audit.py`, `tools/complexity_gate.py` and `tools/measurements.py` with the lock section 1.2 due dates (CDR, CDR, PDR).
- rustos (owner): `publish = false` and `license` in `api/Cargo.toml` and `firmware/pico2/Cargo.toml` (report section 9 item 3) to clear gate G5 cargo deny.

## Closure (iteration 2, 2026-09-25, reviewer:fw-b0, new invocation)

**Author return:** fixed F-02 (partly), F-03, F-05 to F-12; disputed none; F-01 and F-04 not addressed. **Result:** 9 Verified (F-03, F-05 to F-12), 3 Open (F-01 Major, F-02 Major, F-04 Minor), 0 Deferred, 0 disputes. The record stays `record_status: Open` and `verdict: NEEDS CHANGES` (07 section 10.2: Closed only when every finding is Verified or Deferred).

Revised product files (git hash-object, 2026-09-25; unlisted files unchanged from the table above):

| Blob | File |
|---|---|
| `b677319fa0fe9b62431d01fa8b749bbd7e585b0d` | `firmware/.cargo/config.toml` |
| `b2464fb270ad04a15f9c75dd0b56e8ec386cf309` | `firmware/cwht-app/src/main.rs` |
| `fc8872bd420ecbd4760d2f2fc05b236ee842c801` | `firmware/cwht-hal-mock/src/gpio.rs` |
| `93bffdeb67579e427ce1b776529a2862787faea1` | `tools/sw_gate.sh` (362 lines, SHA-256 `fe206ee7...433d0b`) |
| `fee1e7246af59d5e8a43ed1b9cdf483854053fdc` | `docs/test_cases/sw-tool/test_cases.json` |
| `04bc3354352139eb30b33fadff43e1c9b61d0d8e` | `docs/vv/reports/TC-SW-TOOL-001-r1.md` |

The 14 run 1 artifacts are unchanged (`shasum -a 256` equal to the report front matter, including `cwht-app.elf` `3992e5d8...`); the report records the post-run edits in its section 10 without altering the run 1 results.

Reviewer runs of iteration 2 (seeded copies of `firmware/` plus the revised `tools/sw_gate.sh` and `tools/toolchain.lock.md` in the reviewer scratch directory, same construction as `gate-known-answer.sh`; `RUSTUP_TOOLCHAIN=stable`, rustc 1.98.0, rustos `c54d35a`):

| Run | Seed and mode | Exit | First FAIL line and result |
|---|---|---|---|
| KA-0 | unmodified, `--quick` | 0 | no FAIL; 11 PASS G0 to G3 plus `G2 no compiler warning`; FLASH 1608 B of 4194304 B (0.04 %), RAM 8200 B of 532480 B (1.54 %); no `warning` line in the G2 log |
| KA-6 | unwrap in `cwht-app`, `--quick` | 1 | `FAIL G1 clippy target` (regression check of run 1 KA-6) |
| KA-7 | `println!("cargo:warning=...")` in `cwht-app/build.rs`, `--quick` | 1 | `FAIL G2 no compiler warning` |
| KA-8 | identical stale `run1-junit.xml` and `run2-junit.xml` planted, failing host test seeded, `--keep-going` | 1 | `FAIL G3 host tests run 1`, `FAIL G3 host tests run 2`, `FAIL G3 identical result sets (JUnit file of run 1 or run 2 not written by this invocation)`; stale files gone after the run; 9 MISSING still reported |

Open items needed to close the record: F-01 (four scripts, owner-approved installs, lock sanity checks, gate exit 0 and run 2), F-02 (owner-dispositioned CR amending CS-11 and CS-38, or an owner-approved entry in `docs/cm/deviations.md`), F-04 (independent test-author review of the two test files, or a 07 section 3.2 exemption by CR).

## Iteration 3 (2026-09-26, reviewer:fw-b0, new invocation)

**Review baseline:** HEAD `adcfe0946d2f1b5cd8f41a8f91eb4219a7fb99a1`. Every reviewed file is named with its committed blob (`git rev-parse HEAD:<path>`) in the front matter `product_files` (37 files). Against the iteration 2 table, two files changed: `firmware/cwht-app/src/main.rs` (reviewed `b2464fb2`, not in the object store; HEAD `e32006a5`) and `tools/sw_gate.sh` (reviewed `93bffdeb`; HEAD `54b13800`). The other 35 blobs equal the iteration 1 and 2 tables. **Rule applied:** convergence rule of the lead SE, 2026-09-26 (charter section 4 item 3: a Minor RID is fixed before the next review and does not block the baseline): only Major findings change products in this round; every Minor finding is dispositioned "Lien: fix before PDR".

**Search:** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` (record drift rule) before any manual search; `grep -n` used afterwards only to pin lines.

**Changed text reviewed (scan for new Major defects):**

- `main.rs` (diff against the iteration 2 quote): the comment at lines 36-40 now cites CR-001 and states "owner disposition before FW-B1", which matches CR-001 section 1 item 4 and package decision 108 ("Needed by: SRR memo (before FW-B1)"). Code unchanged: the two halt arms at lines 32-34 and 41-43 are the ones F-02 names. No new defect.
- `tools/sw_gate.sh` (`git diff 93bffdeb 54b13800`, two hunks): header lines 44-48 name the three scripts and state that the inline Python checks run only when `tools/measurements.py` is absent, which lines 159-162 and 249-252 implement; line 331 removes the three G6 outputs before G6, so the G6 measurements step reads only files this invocation wrote (reviewer run IT3-1: `MSR-14 NOT PRODUCED`, `emulation report NOT PRODUCED`). `PASS G6 emulation` on the stub's `SKIP` line is what 07 section 8.4 row G6 specifies before PDR ("or the `SKIP` line before PDR", 07 line 357). No new defect.
- Outside this product but read as evidence for F-01: `docs/vv/reports/TC-SW-TOOL-001-r2.md` (blob `de5c9403`), `tools/emu_run.sh` (`17f102aa`), `tools/unsafe_audit.py` (`cc3aaa2a`), `tools/complexity_gate.py` (`9214fefb`), `tools/measurements.py` (`abe25acb`), CR-001 (`d582073e`). The run 2 result lines (2 FAIL, 5 MISSING, exit 1) equal reviewer run IT3-1. Their own review belongs to the records of those products (TV-011 to TV-013; a run 2 report review is a cross item).

**Reviewer run of iteration 3** (repository root, `RUSTUP_AUTO_INSTALL=0`, rustc 1.98.0 via stable per G0, rustos HEAD `c54d35aa8e7f9ad30f6508bca458a59c1fc009db`; `git status --porcelain firmware tools` empty before and after):

| Run | Command | Exit | Result |
|---|---|---|---|
| IT3-1 | `sh tools/sw_gate.sh --keep-going` (gate time stamp 2026-09-26T08:15:00Z, repo `adcfe09`) | 1 | G0 to G4 all PASS (G4 traceability now PASS; FLASH 1608 B 0.04 %, RAM 8200 B 1.54 % through `tools/measurements.py --link-map`; G3 identical result sets through `--diff-runs`); `FAIL G5 cargo deny (bans, licenses, sources)`; `FAIL G5 unsafe audit` (36 rustos `api` and `pico2` sites without a CS-06 `// SAFETY:` comment); 3 geiger PASS; `PASS G6 coverage (stable, MSR-13)`; `SKIP emulation: no accepted emulator ADR` then `PASS G6 emulation`; `PASS G6 measurements`; 5 MISSING (cargo audit database, cargo deny advisories database, `rust-code-analysis-cli`, Miri, nightly llvm-tools); final line `sw_gate: FAIL (2 step(s) failed, 5 prerequisite(s) missing)` |

**Disposition table (iteration 3):**

| Finding | Severity | Iteration 3 disposition | Evidence at HEAD `adcfe09` |
|---|---|---|---|
| F-01 | Major | **Open**, owner ruling needed: package decisions 109 (downloads) and 110 (rustos licence, manifests and the SAFETY-comment work item), owner action OA-1 (steps 11 and 12) | Claude-owned part done: `tools/emu_run.sh`, `tools/unsafe_audit.py`, `tools/complexity_gate.py`, `tools/measurements.py` committed (blobs above). Not met: gate exit 1 (IT3-1: FAIL G5 cargo deny, FAIL G5 unsafe audit, 5 MISSING); lock section 1.1 sanity checks for cargo-llvm-cov, nightly, cargo-nextest, cargo-audit, cargo-deny, cargo-geiger, cargo-binutils read "not yet run" (`tools/toolchain.lock.md:69-75`; the ones that need no download remain Claude's); steps 11 and 12 Pending owner (`TC-SW-TOOL-001-r2.md` status paragraph). 07 section 3.2 FW-B0 exit criterion not met |
| F-02 | Major | **Open**, owner ruling needed: package decision 108 (CR-001) | `main.rs:36-40` cites CR-001; `docs/cm/cr/CR-001-cs11-cs38-driver-construction-arms.md:4` `status: Submitted`, `:18` `disposition: null`; no `docs/cm/deviations.md` in HEAD |
| F-03 | Minor | Closed | `main.rs:60-64` cites FD-1; `TC-SW-TOOL-001-r1.md:170` row FD-1 (report blob unchanged `04bc3354`) |
| F-04 | Minor | **Lien: fix before PDR** | test files unchanged (`718a0246`, `f1b302bc`); no independent test-author review; package item R4 |
| F-05 | Minor | Closed | `firmware/cwht-hal-mock/src/gpio.rs:77-79` and `:85-87` CS-14 comments (blob `fc8872bd`, unchanged since iteration 2) |
| F-06 | Minor | Closed | `tools/sw_gate.sh:237` removes both JUnit copies; `:247-248` fails the comparison when either is absent |
| F-07 | Minor | Closed | `tools/sw_gate.sh:76` `fatal()` used only at `:91` (setup) and `:96-121` (G0); header `:26-30`; case blob `fee1e724` unchanged |
| F-08 | Minor | Closed | `TC-SW-TOOL-001-r1.md:70` deviation D7; `tools/sw_gate.sh:21-22` |
| F-09 | Minor | Closed | `TC-SW-TOOL-001-r1.md:130` |
| F-10 | Minor | Closed | `TC-SW-TOOL-001-r1.md:69` (D6), `:79`, `:171` (FD-2) |
| F-11 | Minor | Closed | `TC-SW-TOOL-001-r1.md:55, 93, 127, 155` |
| F-12 | Minor | Closed | `firmware/.cargo/config.toml:6` (no `--print-memory-usage`, blob `b677319f`); `tools/sw_gate.sh:144-151` fails G2 on any `^warning` line; IT3-1 `PASS G2 no compiler warning` |

New findings of iteration 3: none (no new Major, no new Minor).

**Lien table (carried by the package as Routine items, "Lien: fix before PDR"):**

| Lien | Finding | Item | Closure action | Owner | Due |
|---|---|---|---|---|---|
| L-016-1 | F-04 (Minor) | CK-CODE-H2 | An independent test-author invocation reviews or replaces `firmware/cwht-core/tests/heartbeat.rs` and `firmware/cwht-hal-mock/tests/gpio.rs`, or a CR exempts FW-B0 toolchain-proof tests in 07 section 3.2; this record then verifies it | Test-author invocation (package item R4); Claude dispatches | Before PDR |

**Verdict (iteration 3): NEEDS CHANGES.** Two Major findings remain Open (F-01, F-02), both waiting on owner rulings; under the convergence rule the record cannot be APPROVED while a Major is Open. One lien (F-04). `record_status` stays Open. When decisions 108 to 110 and OA-1 are done, this reviewer verifies CR-001 dispositioned (F-02) and a gate exit 0 with run 3 and the lock sanity rows recorded (F-01).

## Post-SRR-ruling delta (2026-09-26, reviewer:fw-b0, new invocation; package item R16)

**Basis.** The owner approved the SRR on 2026-09-26 (disposition Approved with liens L-1 to L-7; `docs/reviews/SRR/minutes.md`). Key decisions K1 to K17 are ruled as recommended (owner statement "I concur with your recommendations for the key decisions"); for this record that is decision 108 (K10, CR-001: Approve), decision 109 (K10, the four toolchain installs: Approve), decision 110 (K9, rustos licence MIT and the manifest and SAFETY-comment work item: Approve) and decision 115 (b) (K17, owner waiver of readiness R3 for this record). The minutes at `0a6f461` record that the owner reversed the PDR deferral of OA-1 and OA-2 in the same session and that both were performed with a Pass (steps 11 and 12 and the picotool verify known answer), with the raw outputs to be filed with run 4. Under the convergence rule of 2026-09-26 (charter section 4 item 3) only Major findings block; new Minor findings are liens due before PDR.

**Review baseline.** HEAD `5e9506acecb81de38ed6920498ca9e39d9aa74bf`. Search: `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` first (CR-001 disposition; INSP-016 finding-1 and row 20 status); `grep -n` afterwards only to pin lines.

**Commits since the iteration 3 baseline `adcfe09` that touched the products.** `git log adcfe09..HEAD` over `firmware/`, `tools/sw_gate.sh`, `docs/test_cases/sw-tool/` and `docs/vv/reports/TC-SW-TOOL-001-*` lists one commit, `b2d3538` (SRR R16 (a), decisions 109, 110 and 114); none after it. Every one of the 37 iteration 3 product blobs equals its HEAD blob (checked path by path with `git rev-parse HEAD:<path>`), so `firmware/`, `tools/sw_gate.sh`, the case (`fee1e724`) and the run 1 report are unchanged. `b2d3538` adds the run 3 report `docs/vv/reports/TC-SW-TOOL-001-r3.md` (blob in `product_files`, 203 lines) with 20 artifacts, now in `product_files`, and changes `tools/toolchain.lock.md` and the TV records (outside this product; read as evidence for F-01). Commits read as ruling evidence, outside this product: `4364ebb` (07 and CR-001, decisions 108 and 115 (b)) and the rustos branch `cwht/wp-sw-licence-manifest-safety` at `2ec64c0f15c8cd2dbcaa241abffdd72f8cae467c` in the worktree `/Users/robinonsay/rust/rustos-wp-sw-licence` (decision 110; not merged, the lock pin stays `c54d35a`).

**Delta check of each change against its ruling.**

| Change | Ruling cited | Check | Result |
|---|---|---|---|
| CR-001 dispositioned; 07 CS-11, CS-12, CS-38, section 1.2 `cwht-app` row, section 8.2 complexity row (`4364ebb`) | Decision 108 | CR-001 section 7 reads Approved, Class II, date 2026-09-26, source the owner's chat statements; the 07 diff equals CR-001 section 1 items 1 to 3; the amended CS-11 admits `let ... else { safe_state_halt() }` on a rustos constructor returning `Result` with nothing else in the failure branch, which is `main.rs:41-43` exactly; CS-12 places the handler in `cwht-app` (`main.rs:65-68`; its content stays deferred as FD-1) | Applied correctly; F-02 closes. Stale code comment: F-13 (Minor) |
| 07 section 10.2 readiness waiver (`4364ebb`) | Decision 115 (b) | Waives INSP-016 readiness R3 by name, for this record only, ending when INSP-016 closes | Applied; `readiness_met` set true |
| Four installs and lock section 1.1 sanity checks (`b2d3538`, `tools/toolchain.lock.md` blob `5c04ea9e`) | Decision 109 | Lock rows 71 to 78: pass for cargo-llvm-cov, nightly branch coverage, cargo-nextest, cargo-audit, cargo-deny, cargo-geiger, cargo-binutils; rust-code-analysis-cli fail (counting convention); Miri blocked (`rust-src` not in decision 109). Reviewer: `rust-code-analysis-cli --version` gives 0.0.25; G0 now selects the pinned 1.98.0 (IT4-1) | Applied within the ruling. Lock section 1.4 findings 7 (rustup self-update 1.29.0 to 1.29.1) and 8 (two `rust-src` downloads by cargo-miri, removed) went beyond decision 109; both are recorded openly and go to the owner (cross item X-4) |
| rustos work item on a branch (`2ec64c0`) | Decision 110 | `git diff c54d35a 2ec64c0`: 7 files, 200 insertions, 0 deletions; `LICENSE` MIT; `license = "MIT"` and `publish = false` in `api/Cargo.toml` and `firmware/pico2/Cargo.toml`; in the `.rs` files every added line is a `//` comment and 36 of them open a `// SAFETY:` comment; sampled comments in `gpio.rs` state the invariant and cite the datasheet section | Applied correctly and comment-only. Not merged: the ruling approves the work item, and the merge is the owner's act as rustos maintainer (run 3 recommendation 1) |
| Run 3 report and artifacts (`b2d3538`) | Decisions 109, 110 | See reviewer runs below; `result: Blocked`, `credit: false`, no requirement status changed; deviations D11 to D15 disclose the temporary layout, the lock copy, the download guard, the Miri prompt and the unrun steps 11 and 12; `witness: owner` follows the report template rule for Bench cases (`owner for Bench and OnAir`) while section 12 explains that no owner step ran in run 3 | Honest and reproducible (K1, K4, K9 Yes for run 3). No new Major defect |

**Reviewer runs of the delta** (repository root, `RUSTUP_AUTO_INSTALL=0`, `CARGO_NET_OFFLINE=true`, `MIRI_AUTO_OPS=no`; no download; the full gate was not run because its G5 Miri step stops at cargo-miri's `rust-src` install prompt (run 3 D14) and that download is not approved):

| Run | Command | Exit | Result |
|---|---|---|---|
| IT4-1 | `sh tools/sw_gate.sh --quick` at HEAD `7c7959f` (products identical to `5e9506a`), rustos `c54d35a` | 0 | 15 PASS lines G0 to G3, `PASS G0 toolchain identity` on the pinned 1.98.0; FLASH 1608 B (0.04 %), RAM 8200 B (1.54 %), equal to run 3; `sw_gate: PASS (quick: G0 to G3)`; `git status --porcelain firmware tools` empty after |
| IT4-2 | `cargo deny --offline check bans licenses sources` in `firmware/` against the pinned rustos `c54d35a` | 1 | `error[unlicensed]` for `api` and `pico2`: the repository gate still has run 2 blocker B1 |
| IT4-3 | the same command in a scratch layout (`git archive HEAD firmware tools docs/process`, `../rustos` a link to the branch worktree `2ec64c0`, worktree clean) | 0 | `bans ok, licenses ok, sources ok`: run 3 claim B1 reproduced on the branch |
| IT4-4 | `tools/unsafe_audit.py --write` then `--check` in the IT4-3 layout | 0 | 37 sites (block 16, fn 11, impl 1, extern 3, attr 6), 0 without SAFETY, 37 unsigned (a note until CDR): run 3 claim B2 reproduced on the branch |
| IT4-5 | `rust-code-analysis-cli --metrics --output-format json --paths firmware ../rustos/api ../rustos/firmware/pico2` (the `sw_gate.sh:316` form) | 2 | "Found argument '../rustos/api' which wasn't expected": run 3 cause B8 reproduced; finding F-14 |
| IT4-6 | `rust-code-analysis-cli ... --paths firmware/cwht-app/src/main.rs`, cyclomatic sums per function | 0 | `main` 2, `safe_state_halt` 2, `panic` 1: the analyzer counts the bare `loop`, as run 3 cause B9 says; not a product defect (cross item X-2) |
| IT4-7 | `shasum -a 256` of the 20 run 3 artifacts against the report front matter; `cmp` of both run 3 UF2 files with runs 1 and 2 | 0 | 20 of 20 match; `cwht-app.uf2` and `rustos-blinky.uf2` byte-identical to runs 1 and 2, so the OA-1 images of the minutes are the run 3 images |

The scratch layout and the analyzer error file were deleted after the runs.

**Disposition table (post-SRR-ruling delta):**

| Finding | Severity | Delta disposition | Evidence at HEAD `5e9506a` |
|---|---|---|---|
| F-01 | Major | **Open.** Decisions 109 and 110 are applied (`b2d3538`, branch `2ec64c0`) and OA-1 is performed (minutes `0a6f461`), but the finding's criterion, the FW-B0 exit criterion of 07 section 3.2 (gate exit 0), is not met: the repository gate at the pin `c54d35a` still fails G5 cargo deny (IT4-2) and G5 unsafe audit, and on the branch the gate exits 1 with FAIL G5 complexity and FAIL G5 Miri (run 3 section 7, reproduced in part by IT4-3 to IT4-6). The lock's second exit criterion is now met except the rust-code-analysis-cli row (fail) and the Miri half of the nightly row (blocked) | Closes when: (1) the owner merges `cwht/wp-sw-licence-manifest-safety` and a CR moves the lock pin and regenerates `firmware/unsafe-audit.md` (B1, B2); (2) F-14 is fixed (B8); (3) the 07 owner rules the CC convention and a halt-loop rule, and CR-001 step 3 gives `tools/complexity_gate.py` the driver-arm allowance (B9); (4) the owner approves the `rust-src` and Miri sysroot downloads, or dispositions G5 Miri for FW-B0 (B10); (5) the gate exits 0 at HEAD and run 4 files it with the OA-1 and OA-2 raw outputs. This reviewer then verifies it. Not a lien (a Major finding; package section 15 candidate RID 52) |
| F-02 | Major | **Closed** (Verified) on decision 108 | CR-001 Approved (`4364ebb`, blob `0f4cca4c`); 07 CS-11 and CS-38 amended (blob `37d472b5`); `main.rs:36-43` cites CR-001 and conforms to the amended CS-11 |
| F-03, F-05 to F-12 | Minor | Closed (unchanged since iteration 3) | product blobs unchanged |
| F-04 | Minor | **Closed** (Verified); lien L-016-1 discharged | INSP-028 APPROVED on blobs `718a0246`, `f1b302bc` (unchanged) |
| F-13 | Minor | **New; Lien: fix before PDR** | `main.rs:36-40` comment stale after decision 108 (CR-001 step 2) |
| F-14 | Minor | **New; Lien: fix before PDR, and before F-01 closes** | `tools/sw_gate.sh:316` single `--paths` with three values (IT4-5) |

No new Major finding: the only product change in the window is the run 3 report and its artifacts, which reproduce, and the ruling-driven edits outside the product conform to their rulings.

**Lien table (post-SRR-ruling delta; carried by the package as Routine items):**

| Lien | Finding | Item | Closure action | Owner | Due |
|---|---|---|---|---|---|
| L-016-1 | F-04 (Minor) | CK-CODE-H2 | Discharged: INSP-028 APPROVED | none | done |
| L-016-2 | F-13 (Minor) | CK-CODE-I4 | CR-001 step 2: reword `main.rs:36-40` to cite CR-001 as Approved and the amended CS-11; `CR: CR-001` trailer; this record verifies it | Claude (software lead) | Before PDR (earlier if FW-B1 starts first) |
| L-016-3 | F-14 (Minor) | K6 | One `--paths` per path at `tools/sw_gate.sh:316`, with a known-answer run showing the step reaches `tools/complexity_gate.py` | `tools/sw_gate.sh` maintainer (Claude) | Before PDR; needed before F-01 can close |

**Cross items (outside this product; for the owners of those files).**

- X-1 (owner, as rustos maintainer and CCB): merge `cwht/wp-sw-licence-manifest-safety` (`2ec64c0`) and approve the CR that moves the `tools/toolchain.lock.md` section 3 rustos pin (run 3 B1, B2).
- X-2 (07 owner; tool owner): the CC counting convention for CS-17 and CS-38 and a rule for halt loops (the analyzer counts a bare `loop`, IT4-6), then CR-001 step 3 (per-file allowance in `tools/complexity_gate.py`) and a TV-012 fixture re-derived from real analyzer output (run 3 B9; lock section 1.4 findings 9 and 10).
- X-3 (owner): approve or refuse the `rust-src` component on `nightly-2026-08-24` and the Miri sysroot crate download, or disposition G5 Miri for the FW-B0 exit criterion (run 3 B10).
- X-4 (owner): accept rustup 1.29.1 or direct a reinstall of 1.29.0 (lock section 1.4 finding 7); both it and the removed `rust-src` downloads (finding 8) went beyond decision 109.
- X-5 (Claude, conductor): file TC-SW-TOOL-001 run 4 with the OA-1 and OA-2 raw outputs the minutes promise, then the gate run to exit 0; this record verifies F-01 on it.
- X-6 (package author): package section 15 candidate RID 52 and the section 2 H12 row still describe F-01 as "gate exit 1 at run 2 (2 FAIL, 5 MISSING)"; item 53 still reads "CR-001 Submitted"; item 54 still lists F-04 as open. Update them to this delta.

**Verdict (post-SRR-ruling delta): NEEDS CHANGES.** One Major finding remains Open (F-01): the rulings it waited on are applied, but the FW-B0 exit criterion (gate exit 0) is still not met, and under the convergence rule the record cannot be APPROVED while a Major is Open. F-02 and F-04 are Closed. Two new Minor findings (F-13, F-14) are liens due before PDR. `readiness_met` is true under the decision 115 (b) waiver. `record_status` stays Open.

## SRR close-out delta (2026-09-26, reviewer:fw-b0, new invocation)

**Basis.** The SRR minutes section "Close-out decisions (after the first close-out run)" (`dd39332`): twelve items put to the owner with recommendations; owner statement, verbatim, "I concur with your recommendations"; items 1 to 12 ruled as recommended. For this record: item 1 (merge the rustos branch; CR-004 moves the lock pin to the merged commit and regenerates `firmware/unsafe-audit.md` in the same commit), item 2 (`rust-src` on `nightly-2026-08-24` and the Miri sysroot download), item 3 (rustup 1.29.1 accepted, auto-self-update disabled) and item 4 (complexity counting convention, applied by CR-005). Convergence rule (charter section 4 item 3): only open Major findings and ruled work change products before the gate; new Minor findings are liens due PDR. The decision 115 (b) readiness waiver still holds, so `readiness_met` stays true.

**Review baseline.** HEAD `3b45ed7936c2e08ca53feaf080a57271c8dd2261`. Search: `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` first (INSP-016 F-01 state; the 07 Miri scope); `grep -n` afterwards only to pin lines. rustos was read only through `git archive` of `2ec64c0` and through `git diff`/`git log` on its object store; the owner's rustos working tree was neither read nor written.

**Commits since `5e9506a` that touched the product** (`git log 5e9506a..HEAD -- firmware tools/sw_gate.sh docs/test_cases/sw-tool docs/vv/reports/`): three.

| Commit | Files in the product | Ruling or finding cited | Hunk check | Result |
|---|---|---|---|---|
| `37ae576` | `tools/sw_gate.sh` (`54b13800` to `52b9f803`); run 4 report and 13 artifacts (new) | F-14 (run 3 B8); SRR minutes "OA-1 and OA-2 performed" (`0a6f461`) | `sw_gate.sh`: one hunk, the invocation line replaced by a two-line comment and a two-line invocation with one `--paths` per root; nothing else changed. Run 4: steps 11 and 12 and OA-2 as the minutes record them; owner statements quoted verbatim; `result: Blocked`, `credit: false`, no requirement status changed; deviations D16 to D19 disclosed; section 11 leaves the record to the reviewer | Applies F-14 correctly; run 4 honest and reproducible. F-14 closes |
| `5792350` | `firmware/unsafe-audit.md` (`b232d77a` to `18ef484b`) | CR-004, close-out item 1 | 37 rows re-keyed to the `2ec64c0` line numbers; the same 37 sites and items (block 16, fn 11, impl 1, extern 3, attr 6); every "(none: CS-06 violation)" replaced by the SAFETY text; Reviewer and Date empty (no row was signed, so no signature moved); header unchanged. Sampled rows state the invariant and cite the RP2350 datasheet section (rows 5, 13, 16, 24). Evidence outside the product: CR-004 section 1 lists the seven rustos files pulled in; the lock section 3 row moves to `2ec64c0` with the superseded pin kept | Applies CR-004 correctly; reproduced byte for byte (CO-2). New Minor F-16 on the lock rule against G0 |
| `3b45ed7` | run 5 report and 20 artifacts (new) | CR-004, close-out items 2, 3, 4 | `result: Blocked`, `credit: false`; clean layout of cwht `fb22b7a` and rustos `2ec64c0` with a clone for G0 (D20, disclosed); gate exit 1 with 2 FAIL (B9, B11), 0 MISSING; KA-0 to KA-8 MATCH; UF2 files byte-identical to runs 1 to 4, so steps 11 and 12 stand on run 4; the ELF differences are confined to debug and symbol-name sections and explained by build paths; no NCR, with B9 and B11 routed to owners | Honest and reproducible. New Minor F-15 (B11) |

`firmware/` other than `unsafe-audit.md`, the case (`fee1e724`) and the run 1 and run 3 reports are unchanged since `5e9506a` (every other `product_files` blob equals its HEAD blob); `git diff --stat fb22b7a HEAD -- firmware tools` is empty, so run 5 ran the HEAD product.

**Reviewer runs of the delta** (clean layout in the scratch area: `git archive` of cwht `3b45ed7` into `<dir>/cwht` and `git archive` of rustos `2ec64c0` into `<dir>/rustos`, `.venv` linked; `RUSTUP_AUTO_INSTALL=0`, `CARGO_NET_OFFLINE=true`, `MIRI_AUTO_OPS=no`, stdin from `/dev/null`, the run 5 `rustup-guard.sh` first on `PATH`; no download, no install; the layout was deleted afterwards). The full gate was not run: its G0 needs rustos git metadata that an export lacks (F-16), and the brief requires the export; the steps below are the ones the delta changes.

| Run | Command | Exit | Result |
|---|---|---|---|
| CO-1 | `git -C rustos rev-parse master`; lock row by the G0 `sed` expression; `git diff c54d35a 2ec64c0` over `*.rs` and `*.toml`; `merge-base --is-ancestor` | 0 | `master` = lock = `2ec64c0f15c8cd2dbcaa241abffdd72f8cae467c`; `c54d35a` is its ancestor (fast-forward); 7 files, 200 insertions; every added `.rs` line is a `//` comment; manifests add only `license = "MIT"` and `publish = false` |
| CO-2 | `tools/unsafe_audit.py --check`, `--check --gate SRR`, then `--write --audit-file <copy> --date 2026-09-26` and `cmp` with the committed list | 0 | 37 sites (block 16, fn 11, impl 1, extern 3, attr 6), 0 without SAFETY, 37 unsigned (note until CDR), `PASS`; the regenerated list is byte-identical to `firmware/unsafe-audit.md` (blob `18ef484b`): B2 closed |
| CO-3 | `cargo deny --offline --log-level error check bans licenses sources` in `firmware/` on pinned `1.98.0` | 0 | `bans ok, licenses ok, sources ok`: B1 closed |
| CO-4 | G5 complexity, fixed form, then the superseded form | 1, then 2 | Fixed form: MSR-17 functions 52, max CC 5, mean 1.46, none above 12; one failure `FAIL CS-38 firmware/cwht-app/src/main.rs:30 main CC 4 > 3` (analyzer 2 plus 2 `let ... else`; allowance 3), the run 5 result and CR-005 section 9. Superseded form: "Found argument '../rustos/api' which wasn't expected". F-14 verified; B9 reproduced |
| CO-5 | `cargo +nightly-2026-08-24 miri test -p api -p pico2 --lib` (the `sw_gate.sh:326` command) | 1 | `api`: 0 tests, ok; `pico2`: `error: invalid Mach-O section specifier` at `lib.rs:149` and `lib.rs:539`; no prompt and no download line: B10 closed, B11 reproduced (F-15) |
| CO-6 | `shasum -a 256` of the 13 run 4 and 20 run 5 artifacts against the report front matter; `cmp` of the run 1 UF2 files with runs 3 and 5; `cmp` of `kat-target.elf` with the committed fixture; `cmp -l` of the one-byte copy; SHA-256 of `kat-target.uf2` | 0 | 33 of 33 match; both UF2 images byte-identical across runs 1, 3 and 5; fixture identical; one byte differs at file offset `0x1002f` (`0xab` to `0x54`); UF2 equals the `uf2_convert` known answer |

**Disposition table (SRR close-out delta):**

| Finding | Severity | Delta disposition | Evidence at HEAD `3b45ed7` |
|---|---|---|---|
| F-01 | Major | **Open.** The finding's criterion is the FW-B0 exit criterion of 07 section 3.2 (gate exit 0 on the pinned toolchain). Run 5 on the pinned `1.98.0` and rustos `2ec64c0` exits 1 with 2 FAIL; the reviewer reproduced both (CO-4, CO-5). B1, B2, B7, B8 and B10 are closed | Closes when: (1) the owner decides B9 (CR-005 section 9, the CS-38 allowance for the main loop of `cwht-app::main`) and it is applied by CR, with TV-012 re-validated; (2) F-15 (B11) is fixed; (3) a gate run on the pinned toolchain and rustos exits 0 and is filed. This reviewer then verifies it. Not a lien |
| F-02 to F-12 | | Unchanged (Closed) | |
| F-13 | Minor | **Lien, unchanged** (`main.rs` blob `e32006a5` unchanged; run 5 D8 confirms the comment still reads "owner disposition before FW-B1") | L-016-2 |
| F-14 | Minor | **Closed (Verified)**; L-016-3 discharged | `37ae576`; CO-4; run 4 `complexity-invocation-check.txt`; run 5 `sw-gate-full.txt` |
| F-15 | Minor | **New; Lien: fix before PDR, and before F-01 closes** | `sw_gate.sh:326`; CO-5 |
| F-16 | Minor | **New; Lien: fix before PDR** | `sw_gate.sh:117-121` against the lock section 3 rule; run 5 D20 |

No new Major finding: every hunk applies its ruling or finding, every run 4 and run 5 claim that the reviewer re-ran reproduced, and neither remaining FAIL is a defect of the cwht workspace or of rustos `2ec64c0` (B9 waits on an owner decision; B11 is a gate-scope defect that fails safe).

**Accreditation.** No TV record is covered by this record (`tools/sw_gate.sh` has none; its TV is due CDR, lock section 1.2), so this delta makes no accreditation extension effective. TV-011 (`tools/unsafe_audit.py`) and TV-012 (`tools/complexity_gate.py`) are outside this product; their outputs here are developer evidence.

**Lien table (SRR close-out delta):**

| Lien | Finding | Item | Closure action | Owner | Due |
|---|---|---|---|---|---|
| L-016-2 | F-13 (Minor) | CK-CODE-I4 | As before (CR-001 step 2) | Claude (software lead) | Before PDR |
| L-016-3 | F-14 (Minor) | K6 | Discharged (`37ae576`, CO-4) | none | done |
| L-016-4 | F-15 (Minor) | K6 | Narrow the G5 Miri step to the 07 section 8.1 scope, or the rustos `cfg_attr` change by the owner with a pin CR; known-answer run; gate re-run | `tools/sw_gate.sh` maintainer with the 07 owner (Claude); Robin if the rustos route is chosen | Before PDR; needed before F-01 can close |
| L-016-5 | F-16 (Minor) | K6 | G0 export mode, or the lock rule amended to the clone method of run 5 D20 | `tools/sw_gate.sh` maintainer and the lock owner (Claude) | Before PDR |

**Cross items (outside this product; for the owners of those files).**

- X-7 (owner): the B9 decision of CR-005 section 9 (run 5 recommendation 1). F-01 cannot close without it.
- X-8 (07 owner): with F-15 fixed, Miri on `api` runs 0 unit tests, so MSR-08 is empty until `api` or host-compilable `pico2` code has tests (run 5 recommendation 5).
- X-9 (TV-011 owner): in the run 5 KA-8 copy, `tools/unsafe_audit.py` resolved the rustos symbolic link and reported resolved paths, so its `--check` failed against the committed `rustos/...` paths (run 5 D21). A layout detail today, but the tool's path keys depend on how rustos is linked.
- X-10 (package and baseline-record authors): baseline record section 0.1 P1, P2 and P6 and package section 15 candidate RID 52: F-01 remains Open at `3b45ed7` for B9 and B11 only; F-14 Closed.

**Verdict (SRR close-out delta): NEEDS CHANGES.** One Major finding remains Open (F-01): the gate still exits 1 on the pinned toolchain and rustos `2ec64c0`, so under the brief and the convergence rule F-01 does not close. F-14 is Closed. Two new Minor findings (F-15, F-16) are liens due before PDR; F-13 stays a lien. `readiness_met` is true under the decision 115 (b) waiver. `record_status` stays Open.

## SRR close-out delta 2 (2026-09-27, reviewer:fw-b0, new invocation)

**Basis.** The SRR minutes section "Close-out decisions A to C and repository protection" (`786822a`): three items put to the owner with a recommendation; owner statement, verbatim, "Done and added. I approve the other recommendations"; items A to C ruled as recommended. For this record: item A (CR-005 amended so that the +1 CS-38 allowance covers all three CS-19 unbounded loops, including the main loop in `cwht-app::main`; run 5 B9), item B (gate G5 Miri on the host-compilable crates of 07 section 8.1, today `api`; `pico2` host-compilability through `cfg_attr` a lien due FW-B1; F-15, run 5 B11) and item C (CR-004 and CR-005 Class I; CR-002, CR-004 and CR-005 logged in `docs/cm/deviations.md` and their impact reviews performed before the tag, closing RFA-SRR-008). Also the minutes section "Run 4 acceptance and repository protection detail" (owner statement, verbatim, "I think the github settings are fine and yes I approve the results"). Convergence rule (charter section 4 item 3): only open Major findings and ruled work change products before the gate; new Minor findings are liens due PDR. The decision 115 (b) readiness waiver still holds, so `readiness_met` stays true.

**Review baseline.** HEAD `738da038d4655caa0dfa4ad7c58383423ab6c50a` (the reviewer's gate run used a `git archive` of `68a44ed`; `git diff --stat 68a44ed 738da03 -- firmware tools docs/vv docs/test_cases` is empty). Search: `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` first (the INSP-016 record and F-01 state); `grep -n` afterwards only to pin lines. rustos was read only through `git archive` of `2ec64c0` and a local clone checked out at `2ec64c0` for G0 (the run 5 D20 method the brief allows); the owner's rustos working tree was neither read nor written.

**Commits since `3b45ed7` that touched the product** (`git log 3b45ed7..HEAD -- firmware tools/sw_gate.sh docs/test_cases/sw-tool docs/vv/reports/`): three. No file under `firmware/` changed (`firmware/unsafe-audit.md` stays `18ef484b`; `cwht-app/src/main.rs` stays `e32006a5`); the case stays `fee1e724`.

| Commit | Files in the product | Ruling or finding cited | Hunk check | Result |
|---|---|---|---|---|
| `495a0c3` | `tools/sw_gate.sh` (`52b9f803` to `29a37127`) | Close-out item B; F-15; run 5 B11 | Two hunks: the header G5 line gains "on the host-compilable crates of 07 section 8.1 (today rustos api only; see the G5 Miri comment)"; a ten-line comment above the Miri step (reason: `pico2` `link_section` statics at rustos `2ec64c0` `firmware/pico2/src/lib.rs:149` and `:539` rejected by the Mach-O host; scope from item B; end of the exclusion at FW-B1 by `cfg_attr` by the owner as rustos maintainer plus a pin CR) and the command `miri test -p api -p pico2 --lib` becomes `miri test -p api --lib`. Nothing else changes; `sh -n` exit 0. The scope equals 07 section 8.1 (Miri row: the host tests of `api` and of the host-compilable `pico2` decision functions, of which there are none today). The same commit edits `tools/README.md` (one sentence, same content) and the lock section 1.1 `tools/sw_gate.sh` row (a dated 2026-09-27 entry appended after the 20:48 entry; no earlier text changed) and adds the evidence `docs/cm/tool-validation/evidence/sw-gate-miri-scope-2026-09-27.{sh,log.txt}` | Applies item B and the F-15 fix correctly. F-15 closes |
| `2ee4868` | `docs/vv/reports/TC-SW-TOOL-001-r4.md` (`f90902dd` to `572c0f94`) | Minutes "Run 4 acceptance and repository protection detail" | One line: section 12 "Authorization of acceptability (owner): pending" becomes "accepted 2026-09-27", quoting "yes I approve the results", a verbatim excerpt of the owner statement in the minutes, with the minutes section named. The signature field was a placeholder, so no historical line is rewritten | Correct. Run 4 section 12 no longer reads pending, so no lien is carried for it |
| `68a44ed` | Run 6 report and 22 artifacts (new) | Close-out items A and B; F-01; run 5 recommendations | `result: Pass`, `credit: false`, credit row `SUPPORT`, no requirement status changed; clean `git archive` of cwht `bb2485e` and rustos `2ec64c0` plus the D20 clone for G0 (tree equal to the export, before and after); gate exit 0 in both modes (stopping run ends `sw_gate: PASS (G0 to G6)`; `--keep-going` 29 PASS lines, 0 FAIL, 0 MISSING, 1 SKIP, the emulation stub); KA-0 to KA-8 MATCH; UF2 files byte-identical to runs 1, 3 and 5; the ELF differences are confined to debug and `.strtab` sections and explained by the layout path (D22, method disclosed); download check 0 matches over the nine logs; section 7 closes B9 and B11 and keeps the FW-B1 lien of item B open; section 12 authorization pending | Honest and reproducible (D2-1 to D2-5). New Minor F-17 (run 6 owner acceptance pending) |

Work outside the product that the brief names, checked for this record (not re-reviewed; each has its own record):

| Item | Evidence at HEAD | Check | Result |
|---|---|---|---|
| CR-004 class and impact review | `docs/cm/cr/CR-004-rustos-pin-2ec64c0.md`: section 7 "Class confirmed" reads Class I confirmed by the owner under item C (`786822a`), keeping the 2026-09-26 proposal; disposition history row 2026-09-27 appended (`31272e0`); section 6 filled by an independent reviewer agent at `8b86c16` ("Concur with comments", findings 1 and 2 Minor, liens due PDR; its finding-2 is this record's F-16) | Class and review are the item C ruling as written; no earlier history row changed | Correct |
| CR-005 class, amendment 1 and impact review | `docs/cm/cr/CR-005-complexity-counting-convention.md` (`106bc3a`, `0da559a`, `8b86c16`): front matter `class: I`; the Class II rationale kept with a dated "Superseded 2026-09-27" note; section 12 quotes items A and C and the owner statement verbatim; section 6 review by an independent agent ("Concur with comments", findings 1 and 2 Minor); 07 revision A.7 (`bfe05f43`) names the three CS-19 loops and the per-function crediting in CS-38, section 8.2, MSR-17 and section 14.3; `tools/complexity_gate.py` blob `ddf10798` credits the bare `loop` of the top-level `main` of a `cwht-app` binary crate root only, once, to that function | Read every hunk of the tool diff: the credit is `f.main_loop = 1` only when the function is not a halt-loop function, is `main` at depth 0, and the nearest `Cargo.toml` names `cwht-app` with this file as a binary root; an unreadable manifest gives no credit; a second bare `loop` adds analyzer CC without a second credit, so it fails. The accreditation extension of ACC-COMPLEXITY-001 to blob `ddf10798` is effective by the INSP-015 re-issue 4 (`0359409`), outside this record | Correct; B9 closed by a ruled change, not by a gate edit |
| Deviations entries 2 to 4 | `docs/cm/deviations.md` (`31272e0`, `bb2485e`): entries 2 (CR-004) and 3 (CR-005) appended with the 05 section 5.2 departure, RFA-SRR-008 and the before-the-tag closure plan; entry 4 a correction line for entry 1 (entries not edited); closures 1 to 4 appended citing `8b86c16` | Append-only; entries 1 to 3 unchanged; each closure cites the recorded impact review | Correct (RFA-SRR-008 closure is the owner's and the log owner's act, outside this record) |

**Reviewer runs of the delta 2** (clean layout in the scratch area: `git archive` of cwht `68a44ed` into `<dir>/cwht` with `.venv` linked, `git archive` of rustos `2ec64c0` into `<dir>/rustos-export`, and `git clone --no-hardlinks --no-checkout` of the owner's rustos repository into `<dir>/rustos`, then `checkout --detach 2ec64c0`; `RUSTUP_AUTO_INSTALL=0`, `CARGO_NET_OFFLINE=true`, `MIRI_AUTO_OPS=no`, stdin from `/dev/null`, the run 6 `rustup-guard.sh` first on `PATH`; no download, no install; the layout was deleted afterwards).

| Run | Command | Exit | Result |
|---|---|---|---|
| D2-1 | `git diff --stat bb2485e HEAD -- firmware tools docs/test_cases`; `git -C /Users/robinonsay/rust/rustos rev-parse master`; lock row by the G0 `sed` expression; `diff -r -x .git` of the clone against the export; `sh -n tools/sw_gate.sh` | 0 | Empty diff (run 6 ran the HEAD product); `master` = lock = `2ec64c0f15c8cd2dbcaa241abffdd72f8cae467c`; clone tree equal to the export; clone clean after the run; syntax ok |
| D2-2 | `sh tools/sw_gate.sh` (full, stopping mode) in the layout, 2026-09-27T13:30:16Z | 0 | Every step G0 to G6 PASS, `sw_gate: PASS (G0 to G6)`: G0 `rustc 1.98.0 (88d9e12ae 2026-08-18)`, rustos HEAD equal to the lock; FLASH 1608 B, RAM 8200 B; G5 complexity `COUNT .../cwht-app/src/main.rs:30 main CC 4 = analyzer 2 + 2 let ... else`, `ALLOWANCE CS-38 .../main.rs: 4 (2 CS-11 failure arm(s), 1 CS-19 halt loop(s), 1 CS-19 main loop(s))`, MSR-17 functions 52, max_cc 5, mean_cc 1.46, `complexity_gate: PASS (0 failure(s), 0 CS-19 report(s))`; G5 Miri `miri test -p api --lib`, 0 tests, ok; 0 `INTERIM` lines; 0 lines matching the run 6 download pattern. The run 6 stopping result reproduced |
| D2-3 | Loadable sections (`rust-objcopy -O binary --only-section`) of the D2-2 `cwht-app` against run 6 `cwht-app.elf`; `picotool uf2 convert ... --family rp2350-arm-s` and `cmp` with run 6 `cwht-app.uf2` | 0 | `.vector_table`, `.boot_info`, `.text`, `.rodata`, `.data` identical; the UF2 is byte-identical to run 6 (and so to runs 1, 3, 5 and the run 4 load); the ELF SHA-256 differs only by the layout path, as run 6 D22 explains |
| D2-4 | `docs/cm/tool-validation/evidence/sw-gate-miri-scope-2026-09-27.sh` on the D2-2 layout (clean) and on a copy with the seeded out-of-bounds read test appended to rustos `api/src/lib.rs` (KA-M1) | 0, then 1 | Block extracted from the HEAD script (sha256 `cd804ba0...8dcf1`, the value the lock row records); clean `PASS G5 Miri`; KA-M1 `FAIL G5 Miri` with `Undefined Behavior: memory access failed`: the narrowed step still discriminates |
| D2-5 | `shasum -a 256` of the 22 run 6 artifacts against the report front matter; `cmp` of both run 6 UF2 files with runs 1, 3 and 5 | 0 | 22 of 22 match; six `cmp` exit 0 |
| D2-6 | `unittest tools.tests.test_complexity_gate`; `unittest discover -s tools/tests` | 0; 1 | 27 tests OK; 424 run, 1 failure, `test_repository_exit_zero`, caused by record drift of this record and others before their re-issue (this re-issue clears the drift of this record) |

**Disposition table (SRR close-out delta 2):**

| Finding | Severity | Delta 2 disposition | Evidence at HEAD `738da03` |
|---|---|---|---|
| F-01 | Major | **Closed (Verified).** The closure conditions of the close-out delta are met: (1) the owner decided B9 (item A) and it is applied by CR-005 amendment 1 (`106bc3a`) with TV-012 re-validated (run 3, `0da559a`; independent review INSP-015 re-issue 4, `0359409`); (2) F-15 (B11) is fixed (`495a0c3`, item B); (3) run 6 (`68a44ed`) records `tools/sw_gate.sh` exit 0 in both modes on the pinned `1.98.0` and rustos `2ec64c0`, 0 FAIL and 0 MISSING, and this reviewer reproduced the stopping run (D2-2). The FW-B0 exit criterion of 07 section 3.2 is met | run 6 sections 4, 5 and 9; D2-1 to D2-5 |
| F-02 to F-12 | | Unchanged (Closed) | |
| F-13 | Minor | **Lien, unchanged** (`main.rs` blob `e32006a5`; run 6 D8 confirms the stale comment) | L-016-2 |
| F-14 | Minor | Unchanged (Closed, Verified) | |
| F-15 | Minor | **Closed (Verified); lien L-016-4 discharged.** The G5 Miri step runs `-p api --lib`, the host-compilable scope of 07 section 8.1 (item B); the return of `pico2` at FW-B1 is the owner-ruled lien of item B (L-016-6), not an open part of this finding | `495a0c3`; D2-2, D2-4; run 6 B11 |
| F-16 | Minor | **Lien, unchanged** (G0 at `sw_gate.sh` still reads `git -C "$RUSTOS" rev-parse HEAD`; run 6 again used the D20 clone; CR-004 impact review finding-2 says the same) | L-016-5 |
| F-17 | Minor | **New; Lien: fix before PDR** | Run 6 section 12 |

<a id="finding-17"></a>**F-17 (finding-17), Minor, reviewer (SRR close-out delta 2), item K7, `docs/vv/reports/TC-SW-TOOL-001-r6.md` section 12.** The run that closes F-01 and meets the FW-B0 exit criterion reads "Authorization of acceptability (owner): pending"; run 4 carried the same state until the owner accepted it on 2026-09-27. The gate result is reproduced by this reviewer, so the finding changes no verdict and is Minor. Fix: the owner accepts or rejects the run 6 results and the acceptance is transcribed into section 12 with the minutes reference, as for run 4 (`2ee4868`). State: Lien.

No new Major finding: every hunk applies its ruling or finding, every run 6 claim the reviewer re-ran reproduced, and no defect of the cwht workspace, the gate script or rustos `2ec64c0` remains open.

**Accreditation.** No TV record is covered by this record (`tools/sw_gate.sh` has none; its TV is due CDR, lock section 1.2). This delta is the independent review of the item B change and its re-validation entry in the lock section 1.1 `tools/sw_gate.sh` row (CM plan section 9.2 step 4), but it makes no accreditation extension effective, because none is recorded for the gate script. TV-011 (`tools/unsafe_audit.py`) and TV-012 (`tools/complexity_gate.py`) are outside this product; the ACC-COMPLEXITY-001 extension to blob `ddf10798` rests on the INSP-015 re-issue 4 (`0359409`). Run 6 is `credit: false`, so F-01 closes on the gate result, not on credited evidence.

**Lien table (SRR close-out delta 2):**

| Lien | Finding | Item | Closure action | Owner | Due |
|---|---|---|---|---|---|
| L-016-2 | F-13 (Minor) | CK-CODE-I4 | As before (CR-001 step 2) | Claude (software lead) | Before PDR |
| L-016-4 | F-15 (Minor) | K6 | Discharged (`495a0c3`, D2-2, D2-4) | none | done |
| L-016-5 | F-16 (Minor) | K6 | As before: G0 export mode, or the lock rule amended to the clone method of run 5 D20 | `tools/sw_gate.sh` maintainer and the lock owner (Claude) | Before PDR |
| L-016-6 | none (owner ruling, item B) | K6 | `pico2` made host-compilable (the two `link_section` attributes under `cfg_attr` for the target) by the owner as rustos maintainer, a CR moving the lock's rustos pin, then `-p pico2` returned to the G5 Miri step with a known-answer run | Robin (rustos), then the `tools/sw_gate.sh` maintainer (Claude) | FW-B1 (item B) |
| L-016-7 | F-17 (Minor) | K7 | Owner acceptance of run 6 transcribed into run 6 section 12 | Robin; Claude transcribes | Before PDR |

**Cross items (outside this product; for the owners of those files).**

- X-8 (07 owner), carried: Miri on `api` runs 0 unit tests, so MSR-08 is empty until `api` or host-compilable `pico2` code has tests (run 5 recommendation 5; run 6 section 5).
- X-11 (baseline-record and baseline-check authors): `docs/reviews/SRR/baseline-record.md` section 0.2 P1, P2 and P6 and `docs/reviews/SRR/baseline-check.md`: INSP-016 F-01 is Closed (Verified) at `738da03`; INSP-016 holds no open Major and its verdict is APPROVED with liens F-13, F-16 and F-17 (and the item B lien L-016-6); run 6 (`68a44ed`) is the FW-B0 exit evidence for entrance row 20.
- X-12 (package author): package section 15 candidate RID 52 and section 6.15 (INSP-016 line): update to APPROVED with liens at this re-issue.
- X-13 (owner): accept or reject the run 6 results (F-17).

**Verdict (SRR close-out delta 2): APPROVED.** F-01 (Major) is Closed (Verified) on run 6 and the reviewer's reproduction; F-15 is Closed (Verified). No Major finding is open. Minor liens due before PDR: F-13, F-16 and the new F-17; the item B lien L-016-6 is due FW-B1. `readiness_met` is true under the decision 115 (b) waiver. `record_status` stays Open until the liens close.

## Completion criteria check (SWE-088)

SRR close-out delta 2 (2026-09-27): met for the verdict (F-01 Closed (Verified) on run 6 and reviewer run D2-2; no open Major; F-13, F-16 and F-17 Minor liens due PDR and the item B lien due FW-B1; readiness met under the decision 115 (b) waiver). `tools/validate_docs.py` passes on this record.

SRR close-out delta (2026-09-26): still not met (F-01 Major open: the run 5 gate exits 1 on B9 and B11; F-13, F-15 and F-16 liens; readiness met under the decision 115 (b) waiver). Post-SRR-ruling delta (2026-09-26): still not met (F-01 Major open: gate exits 1 at the pin and on the rustos branch; F-13 and F-14 liens; readiness met under the decision 115 (b) waiver). Iteration 3: still not met (F-01 and F-02 Major open on owner rulings; F-04 a lien; gate exits 1). Iteration 2: still not met (two Major findings open, F-04 open, gate not passing). Iteration 1 text follows. Not met: readiness R3 is not met (inherent to FW-B0), two Major findings are open, and the gate does not pass. `tools/validate_docs.py` passes on this record. No unsafe entry exists to sign.

## Verdict

```
SRR CLOSE-OUT DELTA 2 (2026-09-27, HEAD 738da03): VERDICT: APPROVED
- [Major] F-01 Closed (Verified): run 6 (68a44ed) gate exit 0 in both modes on 1.98.0 and rustos 2ec64c0 after items A (CR-005 amendment 1, 106bc3a; TV-012 run 3, 0da559a) and B (495a0c3); reproduced by the reviewer (D2-2).
- [Minor] F-15 Closed (Verified): 495a0c3, G5 Miri -p api --lib (07 section 8.1 scope, item B); KA-M1 still FAILs (D2-4).
- [Minor] F-17 Lien: fix before PDR (run 6 section 12 owner authorization pending).
- [Minor] F-13, F-16 Lien, unchanged. Item B lien L-016-6 (pico2 cfg_attr, pin CR) due FW-B1.
- F-02 to F-12, F-14 Closed.
MEASUREMENTS (delta 2): turns=30; minutes=45; new major=0; new minor=1; closed=2; liens=3

SRR CLOSE-OUT DELTA (2026-09-26, HEAD 3b45ed7): VERDICT: NEEDS CHANGES
- [Major] F-01 Open: CR-004 (5792350) and close-out item 2 closed B1, B2, B10; F-14 fix closed B8; run 4 closed B7; the run 5 gate on 1.98.0 and rustos 2ec64c0 still exits 1 (FAIL G5 complexity B9, owner decision CR-005 section 9; FAIL G5 Miri B11), reproduced (CO-4, CO-5).
- [Minor] F-14 Closed (Verified): 37ae576, one --paths per path; CO-4.
- [Minor] F-15 Lien: fix before PDR and before F-01 closes (sw_gate.sh:326 Miri runs -p pico2, target-only, on the Mach-O host; 07 section 8.1 scope).
- [Minor] F-16 Lien: fix before PDR (G0 needs rustos git metadata; the CR-004 lock rule requires a git archive export).
- [Minor] F-13 Lien, unchanged.
- F-02 to F-12 Closed.
MEASUREMENTS (delta): turns=28; minutes=45; new major=0; new minor=2; closed=1; liens=3

POST-SRR-RULING DELTA (2026-09-26, HEAD 5e9506a): VERDICT: NEEDS CHANGES
- [Major] F-01 Open: decisions 109 and 110 applied (b2d3538; rustos branch 2ec64c0 not merged), OA-1 done (minutes 0a6f461); gate still exits 1 (pin: FAIL G5 cargo deny, G5 unsafe audit; branch: FAIL G5 complexity, G5 Miri).
- [Major] F-02 Closed on SRR decision 108 (CR-001 Approved, 07 amended at 4364ebb).
- [Minor] F-04 Closed on INSP-028 (lien L-016-1 discharged).
- [Minor] F-13 Lien: fix before PDR (main.rs:36-40 comment stale after decision 108; CR-001 step 2).
- [Minor] F-14 Lien: fix before PDR and before F-01 closes (sw_gate.sh:316 one --paths for three paths).
- F-03, F-05 to F-12 Closed.
MEASUREMENTS (delta): turns=30; minutes=45; new major=0; new minor=2; liens=2

ITERATION 3 (2026-09-26, HEAD adcfe09): VERDICT: NEEDS CHANGES
- [Major] F-01 Open (owner rulings: decisions 109, 110; OA-1): gate exits 1 (FAIL G5 cargo deny, FAIL G5 unsafe audit, 5 MISSING).
- [Major] F-02 Open (owner ruling: decision 108): CR-001 Submitted, not dispositioned.
- [Minor] F-04 Lien: fix before PDR (tests written by the code author).
- F-03, F-05 to F-12 Closed.
MEASUREMENTS (iteration 3): turns=22; minutes=30; new major=0; new minor=0; liens=1

ITERATION 1: VERDICT: NEEDS CHANGES
FINDINGS:
- [Major] K5 tools/sw_gate.sh: gate exits 1 (FAIL G4, FAIL G5 cargo deny, 9 MISSING); FW-B0 exit criterion of 07 section 3.2 not met.
- [Major] CK-CODE-D9 firmware/cwht-app/src/main.rs:36: second decision in target-only code (CS-11, CS-38) without CR or deviation.
- [Minor] CK-CODE-C7 main.rs:56: panic handler lacks CS-12 content; deferral not recorded.
- [Minor] CK-CODE-H2 tests written by the code author.
- [Minor] CK-CODE-C4 gpio.rs:77, 83: no comment on the arithmetic choice (CS-14).
- [Minor] K6 sw_gate.sh:176: G3 may compare stale JUnit files.
- [Minor] K6 sw_gate.sh:21: --keep-going description omits the G2 stops.
- [Minor] K7 report: G0 and --quick scope deviation from 07 section 8.4 not recorded.
- [Minor] K7 report section 5: UF2 rebuild claim lacks its artifact.
- [Minor] K7 report: on-board LED instead of the cwht pin map not recorded as a deviation.
- [Minor] K7 report: coverage cited before the cargo-llvm-cov TV the lock row requires.
- [Minor] K6 .cargo/config.toml:9: persistent linker_messages warning in every target build.
ITEMS N/A: CK-CODE-B2 to B8 (no unsafe), C3, D5, D8, E1, E3 to E8, F2, G1, G2, G4, H3, J3; R4, R6
MEASUREMENTS: size=678 lines firmware + 300 gate + 117 case + 170 report; turns=36; minutes=50; major=2; minor=10; unsafe_sites=0
```
