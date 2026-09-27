# SW-04-wp-sw-02-sio-snapshot: rustos work package WP-SW-02

| Field | Value |
|---|---|
| Sprint | SW-04 |
| Module | rustos work package WP-SW-02: GPIO input sampling through SIO: `InputSnapshot`, one `GPIO_IN` read per group (07 section 19) |
| Work package | WP-PDR-41 (PDR work plan section 3.8), wave 1a |
| Build increment | FW-B1 (07 section 3.2) |
| Criticality | safety-critical by inheritance (07 section 14.1 drivers row: GPIO (SIO)) |
| Design record | ADR-054 (`docs/decisions/adr/ADR-054-wp-sw-02-sio-input-snapshot.md`), Proposed |
| Product | rustos branch `cwht/wp-sw-02` at commit `38434b2` (revision 2, Major fixes of review iteration 1; revision 1 at `f85a190`) (a scratch worktree of the rustos repository; not pushed, not merged; the owner merges as rustos maintainer, OD-23) |
| Status | Open: phase 1 done 2026-09-27; phases 2 to 5 open |
| Author | Claude (WP-PDR-41 author invocation, firmware developer role) |

## Phase 0: pre-flight (software lead)

- Predecessor: SW-03 (branch base). `docs/lessons-learned.md` read (entries 1 to 17; no `software` entry yet). Lesson 8 applied: the author self-check against `docs/templates/peer-review-checklist-code.md` is below. Lessons 4 and 12 applied: the products are committed and frozen at the commits named here before any review.
- Baseline counts (cwht `main` at `b77a9e5`, 2026-09-27): `tools/traceability.py --report-only` 245 requirements, 173 test cases, 0 violations, 2 warnings (SYS_UNALLOCATED REQ-SYS-125 and REQ-SYS-148); the two generated files were restored afterwards.
- `tools/sw_gate.sh --quick` was not run for this sprint: it builds against the rustos path dependency, which is the owner's working tree, and no agent reads that tree (plan rule C3). The cwht firmware is unchanged by this sprint. The gate runs on the pin-move CR branch (plan section 6.2, PCR-4) against the merged rustos commit.

## Phase 1: author (done 2026-09-27)

- Author files (07 section 3.5 "rustos driver work package" row), at `f85a190`:
  - `api/src/gpio/mod.rs` (`InputLevels`, `InputSnapshot`, contract SNP-1 to SNP-4)
  - `firmware/pico2/src/gpio/gpio.rs` (input record, `input_snapshot`, `GpioError::NotInput`)
  - `firmware/pico2/src/gpio/snapshot.rs` (`Rp2350InputSnapshot`, `check_snapshot_mask`, `read_inputs`)
  - `firmware/pico2/src/gpio/mod.rs`
- Author developer tests, in the same crate (the host-compilable decision functions and register sequences of CS-38):
  - the `#[cfg(test)]` module of `gpio/snapshot.rs` (6 author developer tests)
- Evidence: 11 host tests pass natively and under Miri; no new unsafe site; `gpio.rs` 546 lines (512 before; CS-18 cross item). Target build `thumbv8m.main-none-eabihf` dev and release without warnings; `clippy::pedantic` clean on the new code apart from the rustos house-style `module_inception`; `tools/complexity_gate.py --max 15` over rustos `api` and `pico2` passes; `tools/unsafe_audit.py --check` over the worktree passes (report kept in the author's scratch area, not committed: `firmware/unsafe-audit.md` is regenerated on the pin-move CR branch against the merged commit).
- CS-24 tags: not applicable to rustos code (plan WP-PDR-41: "Code in the rustos pull requests cites its WP ADR in rustos house style"); the commit message cites ADR-054.
- Author self-check against `docs/templates/peer-review-checklist-code.md` (lesson 8), done once for the stack of five packages; items where the answer is not a plain Yes, each naming the sprint it concerns:
  - CK-CODE-A3: `#[cfg(target_os = "none")]` gates the target-only constructors, trait impls and `Mmio`; it separates host from target, not test from release, and changes no target behaviour.
  - CK-CODE-B4 (CS-08): offsets come from `#[repr(C)]` layouts through `offset_of!`, and the only integer-to-pointer arithmetic is `Mmio::address` in `pico2::common::reg`; the access is a word at `block + offset` rather than a field projection. Put to the reviewer (ADR-051 section 5).
  - CK-CODE-B6 (CS-10): the two `asm!` statements of `critical_section::with` are in `pico2` but not in boot code (ADR-052 section 5; applies to SW-02).
  - CK-CODE-B7: the unsafe audit list is regenerated at the pin move, not in this sprint.
  - CK-CODE-C5 (CS-15): the remaining `as` casts are `RegAddr as usize` in `Mmio` (the CS-08 location) and `Irq as u16` (an enum discriminant, SW-02); every numeric cast was replaced by `From` or byte destructuring.
  - CK-CODE-D7 (CS-18): every new file is under 500 lines; `gpio/gpio.rs` was 512 lines before and is 546 after (SW-04).
  - CK-CODE-F1 to F3: not applicable (rustos code; see CS-24 above).
  - CK-CODE-H2: **No** until phase 2: the contract test file and the dev-board check binary are test-author files (07 section 3.5), and the independent test author has not yet run.
  - CK-CODE-H3: the MC/DC independence pairs are in the author developer tests, named in comments above the pair; the `// @mcdc` tag convention is a cwht convention and not applied in rustos.

## Phase 1, revision 2: author, Major fixes of review iteration 1 (done 2026-09-27)

- Findings addressed: INSP-098 finding-1 (Major, CS-18; INSP-104 concurred). Minor findings of the iteration 1 records are not addressed (plan rule C1); they are fixed at a later revision or become liens after the first APPROVED verdict.
- Product: rustos `cwht/wp-sw-02` at `38434b2` (revision 1 `f85a190` stays an ancestor, so the delta is `git diff f85a190 38434b2`; merge commits bring each lower branch of the stack in, because each branch is merged by the owner on its own).
- Merge: `5d4637f` brings `cwht/wp-sw-01` at `58fe739` into this branch; no conflict.
- Fix: `input_snapshot`, the `NotInput` error (now its own type `snapshot::NotInput`), `Rp2350GpioIn::BIT` and the input recording (`track_input`) move to `snapshot.rs`; in `gpio.rs` the input record replaces the `_private` field and `input_from_handle` calls `track_input` in one line. Files: `gpio/gpio.rs`, `gpio/snapshot.rs`.
- Evidence: 81 host tests pass; target build clean; `rustfmt` and `clippy::pedantic` clean on `snapshot.rs` and on the changed `gpio.rs` lines.
- File lengths (CS-18): `gpio.rs` 512, as before this package (546 at revision 1; the excess over 500 predates the package and is reported to the owner as a rustos item); `snapshot.rs` 177.

## Phase 2: test author (open)

- Independent test author (never this sprint's author; 07 section 3.4): contract test: `api/tests/gpio_snapshot_contract.rs` (author draft, 5 tests); dev-board check: `firmware/devcheck/src/bin/sio_check.rs`.
- **Open item (independence):** the plan names only a firmware-developer author for WP-PDR-41, and the author wrote the contract test file listed above as a draft so that the trait contract could be checked while the trait shape was settled. 07 section 3.5 makes that file a test-author file. The test author either adopts the draft after checking it against the trait documentation only (without reading the `pico2` implementation) and records that in this sprint record, or replaces it; the adoption is a change to the rustos branch before the owner's merge. Reported to the lead SE.
- Mock in `firmware/cwht-hal-mock/` (author file): written after the phase 3 review of the trait shape, on the pin-move CR branch, because it compiles only against the new `api` trait.

## Phase 3: review (open)

- Code: `docs/reviews/PDR/checklists/code-wp-sw-02.md` and `code-wp-sw-02-software-assurance.md` (plan WP-PDR-41 "Records"), product rustos `cwht/wp-sw-02` at `f85a190` (iteration 1); iteration 2 (delta) reviews `38434b2`.
- Design record: `docs/reviews/PDR/checklists/adr-054-wp-sw-02-sio-input-snapshot.md` with its software assurance pair, product `docs/decisions/adr/ADR-054-wp-sw-02-sio-input-snapshot.md` at the blob named in the review brief.

## Phase 4: gate and assurance (open)

After the owner's merge: pin-move CR (PCR-4) with `tools/sw_gate.sh` G1 to G6 on the merged commit, G5 Miri with `-p pico2` returned (SRR lien L-016-6, drafted on rustos branch `cwht/l-016-6` at `5b39e8e`, the base of this stack).

## Phase 5: closure (open)

Dev-board check report `docs/vv/reports/devcheck-sio-r1.md` (`credit: false`); ACC-EMU-001 register-sequence comparison if the emulator is accepted (WP-PDR-42); unsafe audit entries signed (CS-07, before CDR); measurements appended to `docs/plan/measurements.json` (MSR-11 unsafe sites, MSR-17 complexity, test counts); lessons learned; this record marked closed in `docs/sprints/index.md`.
