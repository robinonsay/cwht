//! Fixture: an audited crate whose every site has its SAFETY comment.

pub fn read(p: *const u32) -> u32 {
    // SAFETY: p is an aligned register address (fixture datasheet section 2.1).
    unsafe { p.read_volatile() }
}
