// Same mechanism as rustos firmware/pico2/build.rs: put this crate's directory
// on the linker search path so `-Tlink.ld` resolves to ./link.ld.
fn main() {
    let dir = std::env::var("CARGO_MANIFEST_DIR").unwrap();
    println!("cargo:rustc-link-search={dir}");
    println!("cargo:rerun-if-changed=link.ld");
}
