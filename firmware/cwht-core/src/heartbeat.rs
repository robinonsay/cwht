// @design cwht-core/heartbeat
//! Heartbeat indicator: a two-state output toggled once per call.
//!
//! FW-B0 toolchain-proof unit (07 section 3.2). It exercises the whole layering that the
//! firmware depends on: logic in `cwht-core`, an output reached only through the
//! [`api::common::Write`] trait, a host test against `cwht-hal-mock`, and a target build in
//! `cwht-app` against the rustos `pico2` GPIO driver. It implements no `REQ-SW-*`
//! requirement.

use api::common::Write;

/// Spin-wait count per half period of the development-board heartbeat.
///
/// The same count as the rustos blinky delay (`templates/pico2/src/main.rs`, 5 000 000 calls
/// of `core::hint::spin_loop`). The blink rates differ: at `opt-level = "s"` this loop compiles
/// to three instructions per call, while the blinky's is unrolled 64 times, so the cwht image
/// blinks about four times slower. Both rates are uncalibrated: no clock is configured, so the
/// core runs from the ring oscillator (RP2350 datasheet section 8.3.1: nominal 11 MHz at boot,
/// 4.6 MHz to 19.6 MHz guaranteed).
pub const BLINK_HALF_PERIOD_SPINS: u32 = 5_000_000;

/// Two-state output generator: each [`Heartbeat::step`] drives the opposite level.
#[derive(Debug, Clone, Copy, PartialEq, Eq, Default)]
pub struct Heartbeat {
    /// Level most recently written successfully (`false` before the first step).
    level: bool,
}

impl Heartbeat {
    /// A heartbeat whose first [`Heartbeat::step`] drives the output high.
    #[must_use]
    pub const fn new() -> Self {
        Self { level: false }
    }

    /// Level most recently written successfully; `false` before the first step.
    #[must_use]
    pub const fn level(&self) -> bool {
        self.level
    }

    /// Write the opposite of the current level to `pin` and return the level written.
    ///
    /// # Errors
    ///
    /// Returns the pin's error unchanged when the write fails; the stored level then keeps
    /// its previous value, so the next step retries the same transition.
    pub fn step<P: Write<bool>>(&mut self, pin: &mut P) -> Result<bool, P::Error> {
        let next = !self.level;
        pin.write(next)?;
        self.level = next;
        Ok(next)
    }
}

/// Call `spin` exactly `count` times (bounded busy-wait, CS-19).
///
/// On the target `spin` is `core::hint::spin_loop`, which keeps the loop from being
/// optimised away; on the host a test passes a counting closure.
pub fn spin_wait<F: FnMut()>(count: u32, mut spin: F) {
    for _ in 0..count {
        spin();
    }
}
