//! Known-answer fixture crate (tools/tests/fixtures/rust/known-answers.json).
//!
//! Without features: three passing tests and no lint under the project lint configuration.
//! Feature `seeded-fail`: adds the failing test `tests::seeded_failure`.
//! Feature `seeded-lint`: adds `above_max`, whose comparison `x > u8::MAX` is always false
//! (the clippy correctness lint `absurd_extreme_comparisons`).
//! Feature `seeded-unwrap`: adds `first_or_panic`, which calls `Option::unwrap`; clippy allows
//! `unwrap_used` by default, so only the project lint table (`unwrap_used = "deny"`) rejects it.
#![cfg_attr(not(test), no_std)]

/// Returns the larger of two values.
#[must_use]
pub const fn larger(a: u8, b: u8) -> u8 {
    if a > b { a } else { b }
}

/// Seeded correctness fault for the clippy known answer.
#[cfg(feature = "seeded-lint")]
#[must_use]
pub const fn above_max(x: u8) -> bool {
    x > u8::MAX
}

/// Seeded restriction-lint fault: proves the project lint table is in force.
///
/// # Panics
///
/// Panics when `values` is empty.
#[cfg(feature = "seeded-unwrap")]
#[must_use]
pub const fn first_or_panic(values: &[u8]) -> u8 {
    *values.first().unwrap()
}

#[cfg(test)]
mod tests {
    use super::larger;

    #[test]
    fn first_is_larger() {
        assert_eq!(larger(3, 2), 3);
    }

    #[test]
    fn second_is_larger() {
        assert_eq!(larger(2, 3), 3);
    }

    #[test]
    fn equal_values() {
        assert_eq!(larger(4, 4), 4);
    }

    #[cfg(feature = "seeded-fail")]
    #[test]
    fn seeded_failure() {
        assert_eq!(larger(1, 2), 1);
    }
}
