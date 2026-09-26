---
test_case: TC-SYS-002
run: 1
requirement_ids: [REQ-SYS-003]
validates: []
verification_method: Test
type: Bench
credit: true
result: Pass
date: 2026-11-02
conductor: claude
witness: owner
article: CWHT-A-001
firmware_version: "v1.0.0+0abc123"
source_commit: "0abc1234d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0"
firmware_elf_sha256: "9f2c4e6a8b0d1f3e5a7c9b2d4f6e8a0c1b3d5f7e9a2c4b6d8f0e1a3c5b7d9f2e"
requirements_baseline: baseline/cdr
procedure_commit: "0abc123"
procedure_blob: "5d41402abc4b2a76b9719d911017c592ab8f3e21"
toolchain_lock: "tools/toolchain.lock.md@0abc123"
harness_versions: "n/a"
instruments:
  - "NanoVNA; NanoVNA-H4; 144-148 MHz 201 points; datasheet; SOL on dummy load 2026-11-02"
ncr_ids: []
artifacts:
  - "docs/vv/reports/TC-SYS-002-r1/power.csv sha256=1580aac152e16df4dd9f000c658b5f67fe02391b16dad1583910b31818aa4637"
mop_values: []
---

# Verification report: TC-SYS-002 run 1 (fixture)

Credited Bench run: indicated power 5.1, 5.0 and 4.8 W at 144, 146 and 148 MHz, all inside 4.0 to 6.3 W.
