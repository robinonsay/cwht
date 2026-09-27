//! X10 known answers: the clean run passes 5 tests; `seeded-pair` fails exactly `d01_c2_false`;
//! `seeded-mock-fault` fails exactly `heartbeat_through_mock_toggles`.

use cwht_core::heartbeat::Heartbeat;
use cwht_hal_mock::gpio::{MockGpioError, MockOutput};
use harness_seeded::permit;

/// On-board LED pin of the Pico 2, as in firmware/cwht-core/tests/heartbeat.rs.
const LED: usize = 25;

// @mcdc KAT/D01 c1: d01_tt with d01_c1_false (a varies, b held true)
// @mcdc KAT/D01 c2: d01_tt with d01_c2_false (b varies, a held true)
#[test]
fn d01_tt() {
    assert!(permit(true, true));
}

#[test]
fn d01_c1_false() {
    assert!(!permit(false, true));
}

#[test]
fn d01_c2_false() {
    assert!(!permit(true, false));
}

fn led() -> MockOutput<LED> {
    #[cfg(not(feature = "seeded-mock-fault"))]
    {
        MockOutput::new()
    }
    #[cfg(feature = "seeded-mock-fault")]
    {
        MockOutput::failing_after(1)
    }
}

#[test]
fn heartbeat_through_mock_toggles() {
    let mut pin = led();
    let mut heartbeat = Heartbeat::new();
    assert_eq!(heartbeat.step(&mut pin), Ok(true));
    assert_eq!(heartbeat.step(&mut pin), Ok(false));
    assert_eq!(pin.history(), &[true, false]);
}

#[test]
fn injected_fault_reaches_the_unit_under_test() {
    let mut pin = MockOutput::<LED>::failing_after(0);
    let mut heartbeat = Heartbeat::new();
    assert_eq!(heartbeat.step(&mut pin), Err(MockGpioError::Injected));
    assert!(!heartbeat.level());
}
