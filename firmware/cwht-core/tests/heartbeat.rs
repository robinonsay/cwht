//! `HostUnit` tests of `cwht_core::heartbeat` against `cwht-hal-mock` (toolchain proof,
//! TC-SW-TOOL-001; no `REQ-SW-*` requirement is verified here).

use cwht_core::heartbeat::{BLINK_HALF_PERIOD_SPINS, Heartbeat, spin_wait};
use cwht_hal_mock::gpio::{MockGpioError, MockOutput};

/// On-board LED pin of the Pico 2 (rustos `pico2::common::board`, field `led`).
const LED: usize = 25;

#[test]
fn first_step_drives_high_then_alternates() {
    let mut pin = MockOutput::<LED>::new();
    let mut heartbeat = Heartbeat::new();
    assert!(!heartbeat.level());
    assert_eq!(heartbeat.step(&mut pin), Ok(true));
    assert_eq!(heartbeat.step(&mut pin), Ok(false));
    assert_eq!(heartbeat.step(&mut pin), Ok(true));
    assert_eq!(heartbeat.step(&mut pin), Ok(false));
    assert_eq!(pin.history(), &[true, false, true, false]);
    assert!(!pin.level());
    assert!(!heartbeat.level());
}

#[test]
fn failed_write_keeps_level_and_retries_same_transition() {
    let mut pin = MockOutput::<LED>::failing_after(1);
    let mut heartbeat = Heartbeat::new();
    assert_eq!(heartbeat.step(&mut pin), Ok(true));
    assert_eq!(heartbeat.step(&mut pin), Err(MockGpioError::Injected));
    assert!(heartbeat.level());
    assert!(pin.level());
    assert_eq!(heartbeat.step(&mut pin), Err(MockGpioError::Injected));
    assert_eq!(pin.history(), &[true]);
}

#[test]
fn default_equals_new() {
    assert_eq!(Heartbeat::default(), Heartbeat::new());
}

#[test]
fn spin_wait_calls_spin_exactly_count_times() {
    for count in [0_u32, 1, 2, 1000] {
        let mut calls = 0_u32;
        spin_wait(count, || calls = calls.saturating_add(1));
        assert_eq!(calls, count);
    }
}

#[test]
fn half_period_spin_count_equals_rustos_blinky_delay() {
    assert_eq!(BLINK_HALF_PERIOD_SPINS, 5_000_000);
}
