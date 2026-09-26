// @design cwht-hal-mock/gpio
//! Mock GPIO pins implementing `api::gpio::GpioPinOut` and `api::gpio::GpioPinIn`.

use api::common::{ErrorType, Read, Write};
use api::gpio::{GpioPinIn, GpioPinOut};

/// Number of writes a [`MockOutput`] keeps in its history.
pub const HISTORY_CAPACITY: usize = 64;

/// Error reported by a mock pin that was scripted to fail.
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum MockGpioError {
    /// The operation failed because the test injected a fault.
    Injected,
}

/// Mock push-pull output on pin `N`: records every successful write.
#[derive(Debug, Clone, PartialEq, Eq)]
pub struct MockOutput<const N: usize> {
    /// Current output level.
    level: bool,
    /// Successful writes in order; entries past `len` are unused.
    history: [bool; HISTORY_CAPACITY],
    /// Number of successful writes recorded (saturates at `HISTORY_CAPACITY`).
    len: usize,
    /// Successful writes still allowed before every write fails; `None` never fails.
    writes_before_fault: Option<u32>,
}

impl<const N: usize> MockOutput<N> {
    /// An output at level low with an empty history that never fails.
    #[must_use]
    pub const fn new() -> Self {
        Self {
            level: false,
            history: [false; HISTORY_CAPACITY],
            len: 0,
            writes_before_fault: None,
        }
    }

    /// An output that accepts `count` writes and fails every write after them.
    #[must_use]
    pub const fn failing_after(count: u32) -> Self {
        let mut pin = Self::new();
        pin.writes_before_fault = Some(count);
        pin
    }

    /// Current output level.
    #[must_use]
    pub const fn level(&self) -> bool {
        self.level
    }

    /// Recorded levels of the successful writes, oldest first.
    #[must_use]
    pub fn history(&self) -> &[bool] {
        self.history.get(..self.len).unwrap_or(&[])
    }
}

impl<const N: usize> Default for MockOutput<N> {
    fn default() -> Self {
        Self::new()
    }
}

impl<const N: usize> ErrorType for MockOutput<N> {
    type Error = MockGpioError;
}

impl<const N: usize> Write<bool> for MockOutput<N> {
    fn write(&mut self, value: bool) -> Result<(), Self::Error> {
        match self.writes_before_fault {
            Some(0) => return Err(MockGpioError::Injected),
            // CS-14: checked_sub rather than `-` (clippy::arithmetic_side_effects); the Some(0)
            // arm above returns first, so remaining >= 1 and the result is Some(remaining - 1).
            Some(remaining) => self.writes_before_fault = remaining.checked_sub(1),
            None => {}
        }
        self.level = value;
        if let Some(slot) = self.history.get_mut(self.len) {
            *slot = value;
            // CS-14: saturating_add rather than `+` (clippy::arithmetic_side_effects); get_mut
            // succeeded, so len is below the history length and len + 1 cannot overflow.
            self.len = self.len.saturating_add(1);
        }
        Ok(())
    }
}

impl<const N: usize> GpioPinOut<N> for MockOutput<N> {}

/// Mock input on pin `N` whose level the test sets.
#[derive(Debug, Clone, Copy, PartialEq, Eq, Default)]
pub struct MockInput<const N: usize> {
    /// Level returned by the next read.
    level: bool,
    /// When true, every read fails with [`MockGpioError::Injected`].
    faulted: bool,
}

impl<const N: usize> MockInput<N> {
    /// An input reading `level` that never fails.
    #[must_use]
    pub const fn new(level: bool) -> Self {
        Self {
            level,
            faulted: false,
        }
    }

    /// Set the level returned by later reads.
    pub const fn set_level(&mut self, level: bool) {
        self.level = level;
    }

    /// Make every later read fail (`true`) or succeed (`false`).
    pub const fn set_fault(&mut self, faulted: bool) {
        self.faulted = faulted;
    }
}

impl<const N: usize> ErrorType for MockInput<N> {
    type Error = MockGpioError;
}

impl<const N: usize> Read<bool> for MockInput<N> {
    fn read(&mut self) -> Result<bool, Self::Error> {
        if self.faulted {
            Err(MockGpioError::Injected)
        } else {
            Ok(self.level)
        }
    }
}

impl<const N: usize> GpioPinIn<N> for MockInput<N> {}
