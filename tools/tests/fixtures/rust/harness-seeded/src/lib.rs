//! Decision under test of the X10 harness self-test.
//!
//! Decision KAT/D01: `permit = a && b` (two conditions). Its MC/DC independence pairs, in the
//! form 07 section 9.6 item 2 prescribes, are the tests of `tests/harness.rs`.

/// Decision KAT/D01. With feature `seeded-pair` condition `b` is masked (the seeded fault).
#[must_use]
pub fn permit(a: bool, b: bool) -> bool {
    #[cfg(not(feature = "seeded-pair"))]
    {
        a && b
    }
    #[cfg(feature = "seeded-pair")]
    {
        let _ = b;
        a
    }
}
