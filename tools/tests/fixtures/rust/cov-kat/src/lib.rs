//! Known answer: both arms exercised gives 100 percent; feature seeded-gap drops the else-arm test.
pub fn sign(x: i32) -> i32 {
    if x < 0 {
        -1
    } else {
        1
    }
}
#[cfg(test)]
mod tests {
    #[test]
    fn negative() { assert_eq!(super::sign(-5), -1); }
    #[cfg(not(feature = "seeded-gap"))]
    #[test]
    fn positive() { assert_eq!(super::sign(5), 1); }
}
