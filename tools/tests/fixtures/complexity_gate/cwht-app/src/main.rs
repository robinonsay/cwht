// @target-only
//! Fixture composition root of the package cwht-app (07 CS-19 main loop; CS-38; CR-005 amendment).

fn main() -> ! {
    let Some(board) = Board::take() else {
        safe_state_halt()
    };
    let Ok(mut led) = board.output(25) else { safe_state_halt() };
    loop {
        step(&mut led);
    }
}

fn safe_state_halt() -> ! {
    loop {}
}

#[panic_handler]
fn panic(_info: &PanicInfo) -> ! {
    safe_state_halt()
}

fn idle() -> ! {
    loop {}
}

struct Runner;

impl Runner {
    fn main(&self) -> ! {
        loop {}
    }
}
