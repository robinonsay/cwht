# ADR-053: WP-SW-01 time base and alarms: `api::time` (`Clock`, one-shot `Alarm`) on rustos TIMER0, with missed-match and failed-arm detection

| Field | Value |
|---|---|
| ID | ADR-053 |
| Status | Proposed (for the owner's review and merge of rustos branch `cwht/wp-sw-01` as rustos maintainer, OD-23; FW-B1) |
| Date proposed | 2026-09-27 |
| Date decided | not decided |
| Decision class | 1 by 06 section 14.1 item (c) (TIMER alarms are drivers of the 07 section 14.1 keyer, sequencer and scheduler components); a work-package design within TS-002 alternative A0, as ADR-027 requires (see ADR-051 section 7 for the class question) |
| Decision authority | Robin (safety-critical scope; rustos change merged by the owner, ADR-019) |
| Author | Claude (WP-PDR-41 author invocation, firmware developer role, 2026-09-27) |
| Independent reviewer | Pending: `docs/reviews/PDR/checklists/adr-053-wp-sw-01-timer0.md` (design checklist sections A, B, H) with its software assurance pair; code in `code-wp-sw-01.md` and `code-wp-sw-01-software-assurance.md` |
| Life-cycle phase | B |
| Baseline affected | none now; the rustos pin moves at merge by a Class I CR (PCR-4) |
| Change request | none for this ADR |

## 1. Context

The keyer times every element and space from TIMER0 ALARM0, and the 1 kHz sampling of the key, paddles, encoder and buttons, which is also the scheduler tick, runs from ALARM1 (07 section 5 item 1; section 19 row WP-SW-01). ADR-024 assumption 1 names TIMER0 alarms as the basis of REQ-SYS-042 timing. rustos has no timer driver and no `api` time trait (`docs/research/rustos-toolchain-proof.md` F7, F8, High). `cwht-core` must be tested on the host against a mock clock (ADR-011; 07 section 1.2 `cwht-hal-mock` row), so the time trait is also the seam of every timing test of the keyer.

- Driving inputs and expectations: SI-018, SI-026, SI-033
- Requirements that constrain the decision: REQ-SYS-042 (element timing within the larger of ±1 % and ±0.5 ms), REQ-SW-KEYER-017 and 018 (2 ms (TBR) input-to-element latency), REQ-SW-KEYER-019 (sampling every 1.000 ms ±0.010 ms), REQ-SW-KEYER-033 (sidetone gate within 1 ms of key-down), REQ-SYS-128
- Hazards in play: HZ-004 (unintended or stuck transmission: an alarm that never fires can hold key-down), HZ-005 (sidetone gate timing), and the other hazards of the 07 section 14.1 drivers row (ADR-051)
- Research consulted: `docs/research/rustos-toolchain-proof.md` F9 (TIMER register list), F10 (tick from the crystal), "Driver extension map" (`time::Clock`, `time::Alarm` shapes); `docs/research/emulator-accreditation-and-timer-irq.md` (timer IRQ in the candidate emulator); RP2350 datasheet section 12.8 (p1179 to p1189), extracted into the rustos ICD `docs/icd/rp2350/timer/` by this work package
- Guidance consulted: SWE-134 items g, j, k; SWE-219, SWE-220
- Assumptions the decision rests on, and how and by when each is confirmed:
  1. The TIMER0 tick is 1 µs from the crystal once `ClocksReady` exists (ADR-051). Confirmed by the WP-SW-11 dev-board check.
  2. Handler entry latency at one priority is a few microseconds at 150 MHz, well inside the 10 µs of REQ-SW-KEYER-019. Confirmed by the Bench measurement of CS-22 (MSR-26) before CDR; this ADR fixes only that alarms are scheduled at absolute instants (a periodic tick re-arms at the previous target plus 1000 µs), so latency never accumulates into drift.

## 2. Decision

rustos gains, on branch `cwht/wp-sw-01` at commit `a1cd160` (on `cwht/wp-sw-09`):

1. **`api::time`**: `Instant` and `Duration` counting whole microseconds in `u64` (no wrap-around in practice), with checked arithmetic; `Clock::now() -> Result<Instant, Error>`; and the one-shot `Alarm` with `schedule_at(at) -> Result<Scheduled, Error>` (`Scheduled::Armed`, or `Scheduled::Due` when `at` is not in the future), `cancel`, `is_armed` and `take_fired` (clears the latched fire and returns whether there was one). The contract, clauses CLK-1, CLK-2 and ALM-1 to ALM-6 in the module documentation, is checked by `api/tests/time_contract.rs` against a reference model, with three faulty models (late fire, cancel keeping the fire, no span limit) detected by the check of their clause.
2. **`pico2::timer`**: `Rp2350Timer0::new(handle, &ClocksReady)` releases TIMER0 from reset (bounded wait) and writes `SOURCE` (tick), `PAUSE` (0), `DBGPAUSE` (reset value, pause while a debugger halts a core), `INTE` (0), `ARMED` and `INTR` (all cleared). `split()` returns one `Rp2350Clock` (`Clone`; reads `TIMERAWH`, `TIMERAWL`, `TIMERAWH`, `TIMERAWL` and selects the consistent pair, the SDK's race-free read of section 12.8.4.1) and four `Rp2350Alarm<N>`, each raising `TIMER0_IRQ_N`. `schedule_at` disarms first (so no fire of an old target can be reported), decides from the time whether the target is due, more than 2^32 − 1 µs ahead (`Err(TooFar)`) or armable, enables its interrupt through the `INTE` set alias, writes the low 32 bits of the target to `ALARMn`, then re-reads the time, `ARMED` and `INTR`: still armed with the time past the target means the comparator missed the match (disarm, report `Due`); neither armed nor latched means the arm failed (disarm, `Err(NotArmed)`); otherwise `Armed`. `take_fired` writes the `INTR` bit only after a read saw it set, so no fire is lost. The three decisions (`select_time`, `plan_arm`, `after_arm`) are pure functions with MC/DC pairs; the register sequences are generic over the `Regs` capability of ADR-051.
3. **Register ICD**: `docs/icd/rp2350/timer/` (index, overview, programming model, register map), extracted from datasheet section 12.8 in the rustos ICD style, and a row in `docs/icd/rp2350/index.md`.

## 3. Alternatives considered

| Option | Description | Why not chosen (or why chosen) |
|---|---|---|
| A (chosen) | One-shot alarms at absolute instants, fire latched and taken explicitly, missed match and failed arm detected after arming | A keyer element end or a sampling tick that is in the past when armed is reported (`Due`) instead of silently waiting 71 minutes for the 32-bit comparator to come round; a hardware refusal becomes an error the keyer can fault on (SWE-134 g, k) |
| B | Relative delays (`schedule_in(duration)`) | Re-arming a periodic tick with "now + period" accumulates handler latency as drift; REQ-SW-KEYER-019 is a period tolerance of 1 % of a millisecond |
| C | A latching `TIMELR`/`TIMEHR` read | Unsafe when thread code and a handler both read the time (section 12.8.4.1); the raw read has no side effect |
| D | Periodic hardware tick from SysTick for the 1 kHz sampling | SysTick is core-local and its 24-bit reload runs from the processor tick; one time base (TIMER0) for elements, sampling and timestamps keeps every interval on one counter |
| E | Do nothing | No keyer timing on the target |

## 4. Consequences

### 4.1 Requirements created or changed

| Requirement | Relationship | Note |
|---|---|---|
| none | | The `SW-HAL` behaviours cwht relies on (07 section 4 item 1: alarm `Due` and `NotArmed` handling, absolute scheduling of the 1 kHz tick) are written in WP-PDR-35 and may cite this ADR |

### 4.2 Interfaces, design and code

- ICDs affected: none of cwht's. rustos gains `docs/icd/rp2350/timer/`.
- Design elements: rustos `api/src/time/mod.rs`, `api/tests/time_contract.rs` (new); `firmware/pico2/src/timer/{mod.rs, timer.rs, tests.rs, timer_tests.rs}` (new); `firmware/pico2/src/common/reset.rs` (`RESET_OFFSET`, `RESET_DONE_OFFSET` for the `Regs` users), `common/reg.rs` (`RegAddr::TIMER0`), `common/board.rs` (device `timer0`), `lib.rs` (module list). cwht side: `cwht-core` keyer and scheduler code takes `impl Clock` and `impl Alarm`; the handler of `TIMER0_IRQ_1` calls `take_fired` and re-arms at the previous target plus 1000 µs; the alarm lives in a `pico2::critical_section::CsCell` (ADR-052).
- New `SW-<SUB>` modules: none. ICDs created: none (cwht).

### 4.3 Verification and safety

- Evidence at the branch commit (author runs, 2026-09-27): 30 new host tests (25 in `pico2`: the release sequence and its timeout; the four-read time selection across a high-word change; arming order; `Due` at and before now; `TooFar` at the span edge; fire during arming; missed match; failed arm; latch clearing only after a read; alarm-to-line mapping; 5 contract tests in `api` including the three fault detections and the `Instant`/`Duration` arithmetic), all passing natively and under Miri; target build without warnings; `tools/complexity_gate.py --max 15` passes, with no function of the package above CC 12; no new `unsafe` site.
- Mock in `cwht-hal-mock`: the mock clock with 0.1 ms resolution (ADR-011) and a mock alarm on the same simulated time base, written after this ADR's review fixes the trait, against clauses CLK-1 to ALM-6.
- Dev-board check: `firmware/devcheck/src/bin/timer_check.rs` by the independent test author, report `docs/vv/reports/devcheck-timer-r1.md` (`credit: false`): ALARM1 re-armed at absolute 1000 µs steps for 60 s gives 60 000 handler entries (counted) and an LED toggle every 500 entries observable at 1 Hz; a target already past returns `Due`; the counter read at 1 s intervals advances by 1 000 000 ±50 µs.
- ACC-EMU-001: TIMER0 alarm interrupts are inside the candidate scope for event order (`docs/research/emulator-accreditation-and-timer-irq.md`); the register-sequence comparison is recorded if the emulator ADR accepts the emulator (WP-PDR-42).
- Hazard analysis update required: no. Safety-critical software scope changed: no. SWE-134 g (the alarm state read back after arming) and k (errors returned for a refused or impossible arm) are implemented here; j is served by absolute scheduling.

### 4.4 Cost, schedule, risk

- BOM and lead time: none. Gate: PDR (FW-B1; FM-4 keyer prototype). RSK-013: third of five minimal-keyer packages. TPMs: none.

## 5. Compliance and tailoring

None.

## 6. Decision record (the decision memo for this decision, charter section 4)

Not decided. Proposed memo wording (Form 1): "Owner (date): I merge rustos branch `cwht/wp-sw-01` as reviewed, and ADR-053 is Accepted."

## 7. Related

- Supersedes: none. Superseded by: none.
- Trade study: TS-002 (see ADR-051 section 7)
- Related ADRs: ADR-011, ADR-019, ADR-024 (assumption 1 rests on TIMER0 alarms), ADR-027, ADR-051 (`ClocksReady`), ADR-052 (vectors and `CsCell`)
- Review where presented: PDR
- Revisit conditions: the Bench handler-latency measurement exceeds 10 µs; the firmware architecture ADR moves the sampling tick off TIMER0; TIMER1 or the Secure/Non-secure split is needed (the driver uses TIMER0 only)
