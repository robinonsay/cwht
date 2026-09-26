//! # `cwht-hal-mock`: host implementations of the rustos `api` traits
//!
//! Host-only (never linked into the image, 07 section 1.2). Each mock records what the code
//! under test did to it and can be scripted to fail, so `cwht-core` tests can assert both the
//! nominal and the off-nominal paths without hardware.
//!
//! FW-B0 (07 section 3.2) provides the GPIO output and input pins. The mock clock with 0.1 ms
//! resolution (ADR-011) follows when rustos `api` gains its clock and alarm traits (work
//! package WP-SW-03, 07 section 19).

#![no_std]
#![forbid(unsafe_code)]

pub mod gpio;
