#![forbid(unsafe_code)]
//! Fixture: a crate that forbids unsafe code but holds one site (CS-05 seeded fault).

fn main() {
    // SAFETY: a SAFETY comment does not make unsafe acceptable here.
    let _x = unsafe { core::mem::zeroed::<u32>() };
}
