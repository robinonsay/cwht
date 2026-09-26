//! Fixture crate for tools/unsafe_audit.py (known answers in tools/tests/test_unsafe_audit.py).
//! The words unsafe { in this doc comment are not a site.

/* A block comment /* nested */ that mentions unsafe fn is not a site. */

const TEXT: &str = "unsafe { not a site }";
const RAW: &str = r#"unsafe impl "quoted" not a site"#;
const QUOTE: char = '"';
const ESCAPED: char = '\'';

pub struct Handle<'a> {
    reg: &'a u32,
}

pub fn good_block(p: *const u32) -> u32 {
    // Reads the register once.
    // SAFETY: p points at a readable 32-bit register (fixture datasheet section 1.1)
    // and is aligned, so a volatile read is sound.
    unsafe { p.read_volatile() }
}

// SAFETY: callers pass an aligned, writable register address (fixture datasheet
// section 1.2); the function is the only writer.
#[inline]
#[allow(clippy::missing_safety_doc)]
pub unsafe fn raw_write(p: *mut u32, v: u32) {
    // SAFETY: the caller upholds the contract stated above raw_write.
    unsafe { p.write_volatile(v) }
}

// SAFETY: Handle holds only a shared reference to an immutable register value.
unsafe impl Send for Handle<'_> {}

pub fn bad_block(p: *const u32) -> u32 {
    // A plain comment, not a SAFETY argument.
    unsafe { p.read_volatile() }
}

// SAFETY: the symbol name is unique in the fixture image.
#[unsafe(no_mangle)]
pub extern "C" fn fixture_entry() {}

// SAFETY: the declared C function has no preconditions.
unsafe extern "C" {
    fn fixture_c_function();
}

pub fn let_block(p: *const u32) -> u32 {
    // SAFETY: as in good_block.
    let v = unsafe { p.read_volatile() }; // trailing comment is not the argument
    v
}

// SAFETY: the section name is reserved for this table in the fixture link script.
#[unsafe(link_section = ".fixture")]
static TABLE: [Option<unsafe extern "C" fn()>; 1] = [None];
