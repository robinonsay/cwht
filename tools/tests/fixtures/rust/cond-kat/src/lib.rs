//! Seeded unexercised condition outcome: in `both`, `b` is never evaluated as false with `a` true.
pub fn both(a: bool, b: bool) -> u8 {
    if a && b { 1 } else { 0 }
}
#[cfg(test)]
mod tests {
    use super::both;
    #[test]
    fn true_true() { assert_eq!(both(true, true), 1); }
    #[test]
    fn false_any() { assert_eq!(both(false, true), 0); }
    #[cfg(feature = "complete")]
    #[test]
    fn true_false() { assert_eq!(both(true, false), 0); }
}
