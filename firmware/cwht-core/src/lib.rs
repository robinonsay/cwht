//! # `cwht-core`: cwht application logic
//!
//! Every decision of the cwht firmware lives in this crate, written against the portable
//! rustos `api` traits so that it builds and runs unmodified on a macOS or Linux host
//! (REQ-SYS-128) as well as on the RP2350 (07 section 1.2). The host tests in `tests/` drive
//! it through the mock drivers of `cwht-hal-mock`; that is the `HostUnit` evidence class of
//! `docs/process/04-verification-and-validation.md` section 4.
//!
//! Build increment FW-B0 (07 section 3.2) holds only the toolchain-proof unit
//! [`heartbeat`]; the modules of the software design (keyer, sequencer, safety manager and
//! the rest) are added from FW-B1 under their own requirements.

#![no_std]
#![forbid(unsafe_code)]

pub mod heartbeat;
