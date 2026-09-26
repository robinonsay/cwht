//! Tests of the mock GPIO pins themselves (a mock is test tooling and is tested before it is
//! trusted; TC-SW-TOOL-001).

use api::common::{Read, Write};
use cwht_hal_mock::gpio::{HISTORY_CAPACITY, MockGpioError, MockInput, MockOutput};

#[test]
fn output_records_writes_in_order() {
    let mut pin = MockOutput::<3>::default();
    assert!(!pin.level());
    assert!(pin.history().is_empty());
    assert_eq!(pin.write(true), Ok(()));
    assert_eq!(pin.write(true), Ok(()));
    assert_eq!(pin.write(false), Ok(()));
    assert_eq!(pin.history(), &[true, true, false]);
    assert!(!pin.level());
}

#[test]
fn output_history_saturates_at_capacity() {
    let mut pin = MockOutput::<3>::new();
    for _ in 0..HISTORY_CAPACITY {
        assert_eq!(pin.write(true), Ok(()));
    }
    assert_eq!(pin.write(false), Ok(()));
    assert_eq!(pin.history().len(), HISTORY_CAPACITY);
    assert!(pin.history().iter().all(|level| *level));
    assert!(!pin.level());
}

#[test]
fn output_fails_after_scripted_count() {
    let mut pin = MockOutput::<3>::failing_after(2);
    assert_eq!(pin.write(true), Ok(()));
    assert_eq!(pin.write(false), Ok(()));
    assert_eq!(pin.write(true), Err(MockGpioError::Injected));
    assert_eq!(pin.write(true), Err(MockGpioError::Injected));
    assert_eq!(pin.history(), &[true, false]);
    assert!(!pin.level());
}

#[test]
fn output_failing_after_zero_fails_first_write() {
    let mut pin = MockOutput::<3>::failing_after(0);
    assert_eq!(pin.write(true), Err(MockGpioError::Injected));
    assert!(pin.history().is_empty());
}

#[test]
fn input_reads_set_level_and_injected_fault() {
    let mut pin = MockInput::<4>::new(false);
    assert_eq!(pin.read(), Ok(false));
    pin.set_level(true);
    assert_eq!(pin.read(), Ok(true));
    pin.set_fault(true);
    assert_eq!(pin.read(), Err(MockGpioError::Injected));
    pin.set_fault(false);
    assert_eq!(pin.read(), Ok(true));
    assert_eq!(MockInput::<4>::default().read(), Ok(false));
}
