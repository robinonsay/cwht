//! Fixture host code for tools/complexity_gate.py; rca.json is the rust-code-analysis-cli 0.0.25
//! output on this file and src/app.rs (TV-012 section 3), not a hand-written value.

pub fn straight(x: u32) -> u32 {
    x + 1
}

pub fn branchy(x: u32) -> u32 {
    if x > 1 { 1 } else if x > 2 { 2 } else if x > 3 { 3 } else if x > 4 { 4 } else { 0 }
}

pub fn at_limit(x: u32) -> u32 {
    // Fourteen arms, `_` included: the analyzer counts every arm, so CC 15.
    match x { 0 => 0, 1 => 1, 2 => 2, 3 => 3, 4 => 4, 5 => 5, 6 => 6, 7 => 7, 8 => 8, 9 => 9, 10 => 10, 11 => 11, 12 => 12, _ => 13 }
}

pub fn over_limit(x: u32) -> u32 {
    // Fifteen arms, `_` included: CC 16.
    match x { 0 => 0, 1 => 1, 2 => 2, 3 => 3, 4 => 4, 5 => 5, 6 => 6, 7 => 7, 8 => 8, 9 => 9, 10 => 10, 11 => 11, 12 => 12, 13 => 13, _ => 14 }
}

pub fn let_else_limit(x: Option<u32>) -> u32 {
    // Analyzer CC 15 (fourteen arms); the let-else the analyzer does not count makes it 16 (CR-005).
    let Some(y) = x else { return 0 };
    match y { 0 => 0, 1 => 1, 2 => 2, 3 => 3, 4 => 4, 5 => 5, 6 => 6, 7 => 7, 8 => 8, 9 => 9, 10 => 10, 11 => 11, 12 => 12, _ => 13 }
}

pub fn with_closure(v: &[u32]) -> u32 {
    let f = |x: Option<u32>| {
        let Some(y) = x else { return 0 };
        if y > 1 { y } else { 0 }
    };
    if v.is_empty() { 0 } else { f(v.first().copied()) }
}

pub fn not_let_else(c: bool, o: Option<u32>) -> u32 {
    let a = if c { 1 } else { 2 };
    if let Some(v) = o { v + a } else { a }
}

pub fn ping(n: u32) -> u32 {
    // "pong(n)" in this comment is not a call; nor is let Some(x) = y else { z }; a let-else.
    if n == 0 { 0 } else { pong(n - 1) }
}

pub fn pong(n: u32) -> u32 {
    ping(n)
}

pub fn fact(n: u64) -> u64 {
    if n == 0 { 1 } else { n * fact(n - 1) }
}

pub fn uses_string() -> &'static str {
    "straight(1) and let Some(a) = b else { c }; in a string are neither a call nor a let-else"
}
