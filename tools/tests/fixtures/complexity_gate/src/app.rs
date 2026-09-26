// @target-only
//! Fixture target-only code (CS-38).

fn main() -> ! {
    let Some(board) = Board::take() else { halt() };
    run(board)
}

fn halt() -> ! {
    loop {}
}

fn extra(x: u32) -> u32 {
    if x > 0 { 1 } else { 0 }
}
