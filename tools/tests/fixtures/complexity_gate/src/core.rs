//! Fixture host code for tools/complexity_gate.py; the CC values are in rca.json.

pub fn straight(x: u32) -> u32 {
    x + 1
}

pub fn branchy(x: u32) -> u32 {
    if x > 1 { 1 } else if x > 2 { 2 } else if x > 3 { 3 } else if x > 4 { 4 } else { 0 }
}

pub fn at_limit(x: u32) -> u32 {
    // Fourteen decisions: CC 15 (listed as such in rca.json).
    match x { 0 => 0, 1 => 1, 2 => 2, 3 => 3, 4 => 4, 5 => 5, 6 => 6, 7 => 7, 8 => 8, 9 => 9, 10 => 10, 11 => 11, 12 => 12, 13 => 13, _ => 14 }
}

pub fn over_limit(x: u32) -> u32 {
    // Fifteen decisions: CC 16 (listed as such in rca.json).
    match x { 0 => 0, 1 => 1, 2 => 2, 3 => 3, 4 => 4, 5 => 5, 6 => 6, 7 => 7, 8 => 8, 9 => 9, 10 => 10, 11 => 11, 12 => 12, 13 => 13, 14 => 14, _ => 15 }
}

pub fn with_closure(v: &[u32]) -> u32 {
    let f = |x: u32| if x > 1 { x } else { 0 };
    if v.is_empty() { 0 } else { f(v[0]) }
}

pub fn ping(n: u32) -> u32 {
    // "pong(n)" in this comment is not a call.
    if n == 0 { 0 } else { pong(n - 1) }
}

pub fn pong(n: u32) -> u32 {
    ping(n)
}

pub fn fact(n: u64) -> u64 {
    if n == 0 { 1 } else { n * fact(n - 1) }
}

pub fn uses_string() -> &'static str {
    "straight(1) in a string is not a call"
}
