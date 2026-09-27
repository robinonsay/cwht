// @target-only
//! Fixture target-only code (CS-38; CR-001, CR-005).

fn main() -> ! {
    let Some(board) = Board::take() else {
        safe_state_halt()
    };
    let Ok(led) = board.output(25) else { safe_state_halt() };
    run(led)
}

fn safe_state_halt() -> ! {
    loop {}
}

#[panic_handler]
fn panic(_info: &PanicInfo) -> ! {
    loop {}
}

fn spin() -> ! {
    loop {}
}

fn wrong_arm(board: Board) -> u32 {
    let Ok(pin) = board.output(1) else { return 0 };
    pin
}

fn extra(x: u32) -> u32 {
    if x > 0 { 1 } else { 0 }
}
