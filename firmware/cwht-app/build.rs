//! Build script of `cwht-app`: link configuration only, no code generation (SWE-146 is not
//! engaged). It asks the linker to write the link map next to the ELF, as
//! `target/<triple>/<profile>/cwht-app.map`, the input of gate G2 of `tools/sw_gate.sh`
//! (flash and RAM use, MSR-18 and MSR-19; allocator symbol check, CS-01).

#![forbid(unsafe_code)]

use std::env;
use std::path::PathBuf;

fn main() {
    println!("cargo:rerun-if-changed=build.rs");
    let Some(out_dir) = env::var_os("OUT_DIR") else {
        println!("cargo:warning=OUT_DIR not set; link map not requested");
        return;
    };
    // OUT_DIR is target/<triple>/<profile>/build/<pkg>-<hash>/out: three levels up is the
    // profile directory that holds the ELF.
    let Some(profile_dir) = PathBuf::from(out_dir).ancestors().nth(3).map(PathBuf::from) else {
        println!("cargo:warning=unexpected OUT_DIR layout; link map not requested");
        return;
    };
    let map = profile_dir.join("cwht-app.map");
    println!("cargo:rustc-link-arg-bins=-Map={}", map.display());
}
