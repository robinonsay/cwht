//! Known answer: the clean tests pass under Miri; feature seeded-oob adds one out-of-bounds read,
//! which Miri must report as undefined behaviour.

/// Sum of the first `n` elements of `v`, read through a raw pointer (checked bound).
pub fn sum_prefix(v: &[u32; 4], n: usize) -> u32 {
    let n = n.min(v.len());
    let p = v.as_ptr();
    let mut s = 0_u32;
    for i in 0..n {
        // SAFETY: i < n <= v.len(), so p.add(i) is inside the array.
        s = s.wrapping_add(unsafe { *p.add(i) });
    }
    s
}

/// Element `i` of `v` read through a raw pointer with no bound check (the seeded fault uses i = 4).
///
/// # Safety
/// `i` must be below 4.
pub unsafe fn read_unchecked(v: &[u32; 4], i: usize) -> u32 {
    // SAFETY: the caller guarantees i < 4.
    unsafe { *v.as_ptr().add(i) }
}

#[cfg(test)]
mod tests {
    use super::{read_unchecked, sum_prefix};
    #[test]
    fn prefix_sums() {
        let v = [1, 2, 3, 4];
        assert_eq!(sum_prefix(&v, 0), 0);
        assert_eq!(sum_prefix(&v, 2), 3);
        assert_eq!(sum_prefix(&v, 9), 10);
    }
    #[test]
    fn in_bounds_read() {
        let v = [1, 2, 3, 4];
        // SAFETY: 3 < 4.
        assert_eq!(unsafe { read_unchecked(&v, 3) }, 4);
    }
    #[cfg(feature = "seeded-oob")]
    #[test]
    fn seeded_out_of_bounds_read() {
        let v = [1, 2, 3, 4];
        // Seeded fault: index 4 violates the safety contract; Miri must stop here.
        let x = unsafe { read_unchecked(&v, 4) };
        assert!(x == x);
    }
}
