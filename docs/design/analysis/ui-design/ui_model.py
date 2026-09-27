"""cwht UI design model: tuning law, menu tree, display layouts and UI timing (WP-PDR-33).

Analysis note: docs/design/analysis/ui-design.md. This is an analysis model: the flight UI is the
SW-DISPLAY (or SW-UI, named by the firmware architecture ADR of WP-PDR-32) code. Results are
developer evidence (docs/process/05-configuration-and-data-management.md section 9.1) until a TV
record covers this model.

Display facts: Sharp LS013B7DH03, 128 x 128 dots, pitch 0.18 mm, viewing area 23.04 mm square,
reflectivity 14 percent minimum, contrast ratio 21 minimum, fSCLK 1.1 MHz maximum, full frame
16.8 ms at 1.1 MHz (docs/research/display-and-ui-parts.md F1, F2, High).
"""

from __future__ import annotations

import math
from dataclasses import dataclass

# ---------------------------------------------------------------------------------------------
# Display geometry and bitmap fonts
# ---------------------------------------------------------------------------------------------
W = H = 128
PITCH_MM = 0.18

# 5 x 7 font, author-drawn; '#' is a dark pixel.
FONT5x7 = {
    "A": [".###.", "#...#", "#...#", "#####", "#...#", "#...#", "#...#"],
    "B": ["####.", "#...#", "#...#", "####.", "#...#", "#...#", "####."],
    "C": [".###.", "#...#", "#....", "#....", "#....", "#...#", ".###."],
    "D": ["###..", "#..#.", "#...#", "#...#", "#...#", "#..#.", "###.."],
    "E": ["#####", "#....", "#....", "####.", "#....", "#....", "#####"],
    "F": ["#####", "#....", "#....", "####.", "#....", "#....", "#...."],
    "G": [".###.", "#...#", "#....", "#.###", "#...#", "#...#", ".####"],
    "H": ["#...#", "#...#", "#...#", "#####", "#...#", "#...#", "#...#"],
    "I": [".###.", "..#..", "..#..", "..#..", "..#..", "..#..", ".###."],
    "J": ["..###", "...#.", "...#.", "...#.", "...#.", "#..#.", ".##.."],
    "K": ["#...#", "#..#.", "#.#..", "##...", "#.#..", "#..#.", "#...#"],
    "L": ["#....", "#....", "#....", "#....", "#....", "#....", "#####"],
    "M": ["#...#", "##.##", "#.#.#", "#.#.#", "#...#", "#...#", "#...#"],
    "N": ["#...#", "#...#", "##..#", "#.#.#", "#..##", "#...#", "#...#"],
    "O": [".###.", "#...#", "#...#", "#...#", "#...#", "#...#", ".###."],
    "P": ["####.", "#...#", "#...#", "####.", "#....", "#....", "#...."],
    "Q": [".###.", "#...#", "#...#", "#...#", "#.#.#", "#..#.", ".##.#"],
    "R": ["####.", "#...#", "#...#", "####.", "#.#..", "#..#.", "#...#"],
    "S": [".####", "#....", "#....", ".###.", "....#", "....#", "####."],
    "T": ["#####", "..#..", "..#..", "..#..", "..#..", "..#..", "..#.."],
    "U": ["#...#", "#...#", "#...#", "#...#", "#...#", "#...#", ".###."],
    "V": ["#...#", "#...#", "#...#", "#...#", "#...#", ".#.#.", "..#.."],
    "W": ["#...#", "#...#", "#...#", "#.#.#", "#.#.#", "#.#.#", ".#.#."],
    "X": ["#...#", "#...#", ".#.#.", "..#..", ".#.#.", "#...#", "#...#"],
    "Y": ["#...#", "#...#", ".#.#.", "..#..", "..#..", "..#..", "..#.."],
    "Z": ["#####", "....#", "...#.", "..#..", ".#...", "#....", "#####"],
    "0": [".###.", "#...#", "#..##", "#.#.#", "##..#", "#...#", ".###."],
    "1": ["..#..", ".##..", "..#..", "..#..", "..#..", "..#..", ".###."],
    "2": [".###.", "#...#", "....#", "...#.", "..#..", ".#...", "#####"],
    "3": ["#####", "...#.", "..#..", "...#.", "....#", "#...#", ".###."],
    "4": ["...#.", "..##.", ".#.#.", "#..#.", "#####", "...#.", "...#."],
    "5": ["#####", "#....", "####.", "....#", "....#", "#...#", ".###."],
    "6": ["..##.", ".#...", "#....", "####.", "#...#", "#...#", ".###."],
    "7": ["#####", "....#", "...#.", "..#..", ".#...", ".#...", ".#..."],
    "8": [".###.", "#...#", "#...#", ".###.", "#...#", "#...#", ".###."],
    "9": [".###.", "#...#", "#...#", ".####", "....#", "...#.", ".##.."],
    " ": ["....."] * 7,
    ".": [".....", ".....", ".....", ".....", ".....", ".##..", ".##.."],
    ":": [".....", ".##..", ".##..", ".....", ".##..", ".##..", "....."],
    "/": [".....", "....#", "...#.", "..#..", ".#...", "#....", "....."],
    "?": [".###.", "#...#", "....#", "...#.", "..#..", ".....", "..#.."],
    "-": [".....", ".....", ".....", "#####", ".....", ".....", "....."],
    "<": ["...#.", "..#..", ".#...", "#....", ".#...", "..#..", "...#."],
    ">": [".#...", "..#..", "...#.", "....#", "...#.", "..#..", ".#..."],
    "%": ["##...", "##..#", "...#.", "..#..", ".#...", "#..##", "...##"],
    "'": ["..#..", "..#..", ".#...", ".....", ".....", ".....", "....."],
    "!": ["..#..", "..#..", "..#..", "..#..", "..#..", ".....", "..#.."],
    "(": ["...#.", "..#..", ".#...", ".#...", ".#...", "..#..", "...#."],
    ")": [".#...", "..#..", "...#.", "...#.", "...#.", "..#..", ".#..."],
    "+": [".....", "..#..", "..#..", "#####", "..#..", "..#..", "....."],
    "=": [".....", ".....", "#####", ".....", "#####", ".....", "....."],
}

# Seven-segment frequency digits: 11 x 23 dots, stroke 3 dots (note section 5.1).
DIG_W, DIG_H, STROKE = 11, 23, 3
SEGMENTS = {
    "a": (1, 0, DIG_W - 2, STROKE), "g": (1, 10, DIG_W - 2, STROKE),
    "d": (1, DIG_H - STROKE, DIG_W - 2, STROKE),
    "f": (0, 1, STROKE, 11), "b": (DIG_W - STROKE, 1, STROKE, 11),
    "e": (0, 11, STROKE, 11), "c": (DIG_W - STROKE, 11, STROKE, 11),
}
DIGIT_SEGS = {"0": "abcdef", "1": "bc", "2": "abged", "3": "abgcd", "4": "fgbc", "5": "afgcd",
              "6": "afgedc", "7": "abc", "8": "abcdefg", "9": "abcdfg"}


class Canvas:
    """128 x 128 one-bit frame buffer; True is a dark (written) dot."""

    def __init__(self):
        self.px = [[False] * W for _ in range(H)]

    def set(self, x, y, v=True):
        if 0 <= x < W and 0 <= y < H:
            self.px[y][x] = v

    def fill(self, x, y, w, h, v=True):
        for yy in range(y, y + h):
            for xx in range(x, x + w):
                self.set(xx, yy, v)

    def invert(self, x, y, w, h):
        for yy in range(y, y + h):
            for xx in range(x, x + w):
                if 0 <= xx < W and 0 <= yy < H:
                    self.px[yy][xx] = not self.px[yy][xx]

    def text(self, x, y, s, scale=1):
        for ch in s.upper():
            g = FONT5x7[ch]
            for r, row in enumerate(g):
                for c, b in enumerate(row):
                    if b == "#":
                        self.fill(x + c * scale, y + r * scale, scale, scale)
            x += 6 * scale
        return x

    @staticmethod
    def text_width(s, scale=1):
        return 6 * scale * len(s) - scale

    def freq(self, x, y, s):
        """Frequency string of digits and points in seven-segment digits."""
        for ch in s:
            if ch == ".":
                self.fill(x, y + DIG_H - STROKE, STROKE, STROKE)
                x += STROKE + 2
            else:
                for seg in DIGIT_SEGS[ch]:
                    sx, sy, sw, sh = SEGMENTS[seg]
                    self.fill(x + sx, y + sy, sw, sh)
                x += DIG_W + 1
        return x

    @staticmethod
    def freq_width(s):
        return sum((STROKE + 2) if ch == "." else (DIG_W + 1) for ch in s) - 1

    def dark_rows(self):
        return [y for y in range(H) if any(self.px[y])]


def fmt_freq(hz: int) -> str:
    """146520000 -> '146.520.00' (MHz.kHz.10 Hz; 10 Hz resolution, REQ-SYS-058)."""
    mhz = hz // 1_000_000
    khz = (hz // 1000) % 1000
    tens = (hz // 10) % 100
    return f"{mhz:03d}.{khz:03d}.{tens:02d}"


# ---------------------------------------------------------------------------------------------
# Screens (note section 5.2). Each returns a Canvas.
# ---------------------------------------------------------------------------------------------
def _status_frame(c: Canvas, mode="IA", wpm=15, freq_hz=146_520_000):
    c.text(1, 1, mode, 2)
    s = f"{wpm}WPM"
    c.text(W - 1 - Canvas.text_width(s, 2), 1, s, 2)
    f = fmt_freq(freq_hz)
    c.freq((W - Canvas.freq_width(f)) // 2, 20, f)
    c.text(1, 119, "MENU", 1)
    c.text(W - 1 - Canvas.text_width("FUNC", 1), 119, "FUNC", 1)


def _battery(c: Canvas, y, volts=7.6, bars=3):
    c.text(1, y, f"BAT {volts:.1f}V", 2)
    x0 = 104
    c.fill(x0, y, 20, 1)
    c.fill(x0, y + 13, 20, 1)
    c.fill(x0, y, 1, 14)
    c.fill(x0 + 19, y, 1, 14)
    c.fill(x0 + 20, y + 4, 3, 6)
    for i in range(bars):
        c.fill(x0 + 2 + i * 4, y + 2, 3, 10)


def screen_receive() -> Canvas:
    c = Canvas()
    _status_frame(c)
    c.text(1, 48, "RX", 2)
    c.text(W - 1 - Canvas.text_width("1W", 2), 48, "1W", 2)
    _battery(c, 66)
    c.text(1, 84, "KEEP 0.3M", 2)
    c.text(1, 102, "N0CALL", 2)
    return c


def screen_transmit() -> Canvas:
    c = Canvas()
    _status_frame(c)
    band = Canvas()
    band.text(3, 48, "TX", 2)
    band.text(W - 3 - Canvas.text_width("5W", 2), 48, "5W", 2)
    for y in range(46, 64):
        for x in range(W):
            c.px[y][x] = not band.px[y][x]
    _battery(c, 66)
    c.text(1, 84, "KEEP 0.6M", 2)
    c.text(1, 102, "N0CALL", 2)
    return c


def screen_tune() -> Canvas:
    c = Canvas()
    _status_frame(c)
    band = Canvas()
    band.text(3, 48, "TUNE", 2)
    band.text(W - 3 - Canvas.text_width("0.5W", 2), 48, "0.5W", 2)
    for y in range(46, 64):
        for x in range(W):
            c.px[y][x] = not band.px[y][x]
    _battery(c, 66)
    c.text(1, 84, "KEEP 1.0M", 2)
    c.text(1, 102, "ENDS 4.2S", 2)
    return c


# REQ-SYS-060 status set on the three screens it names (fields drawn by the functions above)
SCREEN_FIELDS = {
    "receive": {"frequency", "power step", "key mode", "keyer speed", "battery state", "transmit state"},
    "transmit": {"frequency", "power step", "key mode", "keyer speed", "battery state", "transmit state"},
    "tune": {"frequency", "power step", "key mode", "keyer speed", "battery state", "transmit state"},
}

# REQ-SYS-067 message table: ConOps Table 3.4-4 row, ConOps text, proposed two display lines of at
# most 10 characters at the 2x font (note section 3.6)
MESSAGE_TABLE = [
    (1, "KEY CLOSED: check plug", ("KEY CLOSED", "CHECK PLUG")),
    (2, "KEY?", ("KEY?", "OPEN KEY")),
    (3, "PADDLE?", ("PADDLE?", "RELEASE")),
    (4, "HOT: wait", ("HOT", "WAIT")),
    (5, "TX off: low batt", ("TX OFF", "LOW BATT")),
    (6, "TX inhibited (USB)", ("TX OFF", "USB POWER")),
    (7, "TX guard", ("TX OFF", "BAND EDGE")),
    (8, "Lock icon RX only", ("RX ONLY", "GUEST")),
    (8, "PRACTICE", ("PRACTICE", "TX OFF")),
    (9, "RESET: <reason>", ("RESET", "WATCHDOG")),
    (10, "RESET REPEATED: switch off and report", ("RESET X2", "SWITCH OFF")),
    (11, "The failed item", ("SELFTEST", "<ITEM>")),
    (12, "TX CUTOFF: report to owner", ("TX CUTOFF", "REPORT")),
    (13, "CELL SENSE: report to owner", ("CELL SENSE", "REPORT")),
    (14, "CELL: check polarity", ("CELL", "POLARITY")),
    (14, "CELLS mismatched: replace as a pair", ("CELLS", "MISMATCH")),
    (15, "CHARGER: report to owner", ("CHARGER", "REPORT")),
    (16, "USB fault", ("USB FAULT", "UNPLUG")),
    (17, "CHG hold: cold", ("CHG HOLD", "COLD")),
    (17, "CHG hold: hot", ("CHG HOLD", "HOT")),
    (18, "BATT EMPTY", ("BATT EMPTY", "CHARGE")),
    (19, "CELL HOT: powering down", ("CELL HOT", "POWER DOWN")),
]


def _banner(c: Canvas, y, h, lines, scale=2):
    band = Canvas()
    yy = y + 2
    for s in lines:
        band.text((W - Canvas.text_width(s, scale)) // 2, yy, s, scale)
        yy += 8 * scale
    for r in range(y, y + h):
        for x in range(W):
            c.px[r][x] = not band.px[r][x]


def screen_key_inhibit() -> Canvas:
    c = Canvas()
    _status_frame(c)
    _banner(c, 46, 34, ["KEY CLOSED", "CHECK PLUG"])
    _battery(c, 84)
    c.text(1, 102, "TX OFF", 2)
    return c


def screen_id_reminder() -> Canvas:
    c = Canvas()
    _status_frame(c)
    c.text(1, 48, "RX", 2)
    c.text(W - 1 - Canvas.text_width("1W", 2), 48, "1W", 2)
    _banner(c, 66, 34, ["ID NOW", "N0CALL"])
    c.text(1, 104, "ID EVERY 10 MIN", 1)
    return c


MENU_L1 = ["KEYER", "AUDIO", "TX", "SETUP"]


def screen_menu_l1(sel=0) -> Canvas:
    c = Canvas()
    c.text(1, 1, "MENU", 1)
    c.text(W - 1 - Canvas.text_width("1/4", 1), 1, "1/4", 1)
    c.fill(0, 9, W, 1)
    for i, name in enumerate(MENU_L1):
        y = 13 + i * 18
        c.text(4, y + 2, name, 2)
        if i == sel:
            c.invert(0, y, W, 18)
    c.text(1, 119, "BACK", 1)
    c.text(W - 1 - Canvas.text_width("SEL", 1), 119, "SEL", 1)
    return c


def screen_menu_l2_keyer(sel=0) -> Canvas:
    c = Canvas()
    items = [name for name, *_ in MENU_TREE["KEYER"]]
    c.text(1, 1, "KEYER", 1)
    s = f"{sel + 1}/{len(items)}"
    c.text(W - 1 - Canvas.text_width(s, 1), 1, s, 1)
    c.fill(0, 9, W, 1)
    for i, name in enumerate(items[:4]):
        y = 12 + i * 18
        c.text(4, y + 2, name, 2)
        if i == sel:
            c.invert(0, y, W, 18)
    c.fill(0, 86, W, 1)
    band = Canvas()
    band.text((W - Canvas.text_width("<IAMB A>", 2)) // 2, 93, "<IAMB A>", 2)
    for r in range(89, 111):
        for x in range(W):
            c.px[r][x] = not band.px[r][x]
    c.text(1, 119, "BACK", 1)
    c.text(W - 1 - Canvas.text_width("SET", 1), 119, "SET", 1)
    return c


SCREENS = {
    "receive": screen_receive,
    "transmit": screen_transmit,
    "tune": screen_tune,
    "key-inhibit": screen_key_inhibit,
    "id-reminder": screen_id_reminder,
    "menu-level-1": screen_menu_l1,
    "menu-level-2-keyer": screen_menu_l2_keyer,
}


def render_png(c: Canvas, path, scale=4, caption=None):
    from PIL import Image, ImageDraw, ImageFont
    bg = (200, 206, 190)   # reflective panel, light state (illustrative colour)
    fg = (34, 38, 34)      # written dot
    margin, cap_h = 12, (28 if caption else 0)
    img = Image.new("RGB", (W * scale + 2 * margin, H * scale + 2 * margin + cap_h), (255, 255, 255))
    d = ImageDraw.Draw(img)
    d.rectangle([margin - 1, margin - 1, margin + W * scale, margin + H * scale], outline=(0, 0, 0))
    for y in range(H):
        for x in range(W):
            col = fg if c.px[y][x] else bg
            d.rectangle([margin + x * scale, margin + y * scale,
                         margin + x * scale + scale - 1, margin + y * scale + scale - 1], fill=col)
    if caption:
        font = ImageFont.load_default()
        d.text((margin, H * scale + 2 * margin + 4), caption, fill=(0, 0, 0), font=font)
    img.save(path)


# ---------------------------------------------------------------------------------------------
# Menu tree (REQ-SYS-062). Level 0 is the status screen; each entry is (item, kind, source).
# kind: 'setting' (a stored operator setting), 'action' (with a separate confirmation step),
# 'view' (read-only). Operator settings not in the menu are listed in NON_MENU_CONTROLS.
# ---------------------------------------------------------------------------------------------
MENU_TREE = {
    "KEYER": [
        ("MODE", "setting", "REQ-SYS-040, REQ-SYS-056 key-input and keyer mode"),
        ("SPEED", "setting", "REQ-SYS-041 (also FUNC plus the tuning knob on the status screen)"),
        ("SWAP", "setting", "docs/conops/conops.md 3.5.1 item 3 paddle swap"),
        ("SWITCHPT", "setting", "REQ-SW-KEYER-009 Iambic B switchpoint (decision 48)"),
        ("MAKE MS", "setting", "REQ-SYS-048 debounce make (decision 48)"),
        ("BREAK MS", "setting", "REQ-SYS-162 debounce break (decision 48)"),
        ("HANG", "setting", "REQ-SYS-044 semi break-in hang"),
        ("PRACTICE", "setting", "ConOps Table 3.4-3 PRACTICE flag"),
    ],
    "AUDIO": [
        ("TONE HZ", "setting", "REQ-SYS-045 sidetone frequency"),
        ("TONE LVL", "setting", "docs/research/keyer-verification-and-key-input-network.md F14 sidetone level"),
        ("UNLOCK", "action", "REQ-SYS-074 level cap acknowledgment with confirmation"),
        ("KEEP UNLK", "setting", "REQ-SYS-170 persistent unlock selection"),
    ],
    "TX": [
        ("POWER", "setting", "REQ-SYS-063 step, 5 W only after a separate confirmation"),
        ("ENVELOPE", "setting", "REQ-SYS-014 operator-set 10-to-90 percent time"),
        ("TUNE", "action", "ConOps T12 tune carrier, menu action and confirmation"),
        ("KEYDN TIME", "view", "REQ-SYS-171 cumulative key-down time"),
    ],
    "SETUP": [
        ("CALL", "setting", "REQ-SYS-006 operator call sign, up to 10 characters"),
        ("BENCH TEST", "action", "REQ-SYS-179 selection followed by a separate confirmation"),
        ("RESET CFG", "action", "REQ-SYS-136 configuration reset with confirmation"),
        ("INFO", "view", "firmware version and stored call sign"),
    ],
}

NON_MENU_CONTROLS = [
    ("frequency", "tuning knob turn on the status screen", "REQ-SYS-058"),
    ("volume", "volume knob turn; push mutes", "REQ-SYS-059"),
    ("guest lock", "MENU and FUNC held 2 s, then a tuning-knob push to confirm", "REQ-SYS-066"),
    ("keyer speed", "FUNC press, then the tuning knob sets WPM for 5 s", "REQ-SYS-041"),
]


def menu_depths():
    """Depth of every operator setting and action from the status screen (level 0)."""
    out = {}
    for cat, items in MENU_TREE.items():
        for name, kind, src in items:
            out[f"{cat}>{name}"] = (2, kind, src)
    for name, how, src in NON_MENU_CONTROLS:
        out[name] = (0, "direct", src)
    return out


# ---------------------------------------------------------------------------------------------
# Tuning law (REQ-SYS-058) and band crossing (REQ-SYS-164)
# ---------------------------------------------------------------------------------------------
STEP_TABLE = [  # (minimum detent rate per second, step Hz); the first matching from the top
    (20.0, 10_000),
    (10.0, 1_000),
    (5.0, 100),
    (0.0, 10),
]
IDLE_RESET_S = 0.5      # a detent after a pause longer than this is a slow detent (10 Hz)
F_MIN, F_MAX = 144_000_000, 148_000_000   # REQ-SYS-164 band edges (receive tuning range)


def step_for_rate(rate: float) -> int:
    for rmin, step in STEP_TABLE:
        if rate >= rmin:
            return step
    return STEP_TABLE[-1][1]


@dataclass
class Tuner:
    f: int
    last_t: float | None = None

    def detent(self, t: float, direction: int) -> int:
        """Apply one detent at time t (s) in direction +1 or -1; return the step used."""
        if self.last_t is None or (t - self.last_t) > IDLE_RESET_S:
            step = STEP_TABLE[-1][1]
        else:
            step = step_for_rate(1.0 / max(t - self.last_t, 1e-6))
        self.last_t = t
        nf = self.f + direction * step
        if step >= 1000:  # land on the step grid in the direction of rotation
            nf = (nf // step) * step if direction > 0 else -((-nf) // step) * step
        self.f = max(F_MIN, min(F_MAX, nf))
        return step


def crossing_time(rev_per_s: float, detents_per_rev: int = 24, start=F_MIN, stop=F_MAX):
    """Time and detents to tune from start to stop at a steady rotation rate."""
    rate = rev_per_s * detents_per_rev
    tu = Tuner(start)
    n = 0
    t = 0.0
    while tu.f < stop:
        tu.detent(t, +1)
        n += 1
        if tu.f >= stop:
            break
        t += 1.0 / rate
        if n > 10_000_000:
            return None, n
    return t, n


def usability_run(start_hz: int, target_hz: int, detents_per_rev: int = 24):
    """Scripted operator: fast spin, slower spins, then single detents to land on the target.

    Phases (rotation rate, stop when the remaining distance is below the threshold):
      2.0 rev/s until within 20 kHz; 0.75 rev/s until within 1.5 kHz; 0.4 rev/s until within
      150 Hz; 3 detents/s to the exact 10 Hz target. A 0.3 s reaction pause separates phases.
    Returns the phase log, total time, detent count and final error (Hz).
    """
    tu = Tuner(start_hz)
    t = 0.0
    log = []
    n = 0
    phases = [(2.0 * detents_per_rev, 20_000), (0.75 * detents_per_rev, 1_500),
              (0.4 * detents_per_rev, 150), (3.0, 0)]
    for rate, within in phases:
        t0, n0 = t, n
        while abs(target_hz - tu.f) > within:
            direction = 1 if target_hz > tu.f else -1
            prev = tu.f
            tu.detent(t, direction)
            n += 1
            t += 1.0 / rate
            if within == 0 and tu.f == target_hz:
                break
            if (target_hz - prev) * (target_hz - tu.f) < 0 and within > 0:
                break  # overshoot: go to the next, finer phase
        log.append({"rate_detents_per_s": rate, "stop_within_hz": within, "time_s": round(t - t0, 3),
                    "detents": n - n0, "freq_hz": tu.f})
        t += 0.3
    return {"phases": log, "total_s": round(t - 0.3, 3), "detents": n, "error_hz": tu.f - target_hz}


# ---------------------------------------------------------------------------------------------
# Legibility (REQ-SYS-061, REQ-SYS-165)
# ---------------------------------------------------------------------------------------------
def subtense_arcmin(height_mm: float, distance_mm: float) -> float:
    return math.degrees(2 * math.atan(height_mm / (2 * distance_mm))) * 60.0


def luminance_cd_m2(illuminance_lux: float, reflectance: float) -> float:
    """Lambertian reflective surface: L = E rho / pi."""
    return illuminance_lux * reflectance / math.pi


def fresnel_r(n: float) -> float:
    return ((n - 1) / (n + 1)) ** 2


def legibility(E_lux: float, rho_min=0.14, cr_min=21.0, lens_n=1.49, surround_rho=0.8,
               with_lens=True, R_override=None):
    """Background and character luminance, contrast ratio, with an optional plain lens.

    The lens transmits (1 - R)^2 per pass and the display light passes twice; the veiling
    reflection is R_total times the luminance of a white surround (reflectance surround_rho) seen
    in the specular direction, the worst case (note section 4.3 assumption A-U4).
    """
    Lb = luminance_cd_m2(E_lux, rho_min)
    Lc = Lb / cr_min
    if not with_lens:
        return {"Lb": Lb, "Lc": Lc, "CR": Lb / Lc, "weber": (Lb - Lc) / Lb, "veil": 0.0}
    R = fresnel_r(lens_n) if R_override is None else R_override
    T1 = (1 - R) ** 2
    Tdisp = T1 * T1
    Rtot = R + (1 - R) ** 2 * R / (1 - R * R)  # front plus back surface, repeated reflections summed
    veil = Rtot * luminance_cd_m2(E_lux, surround_rho)
    Lb2, Lc2 = Lb * Tdisp + veil, Lc * Tdisp + veil
    return {"Lb": Lb2, "Lc": Lc2, "CR": Lb2 / Lc2, "weber": (Lb2 - Lc2) / Lb2, "veil": veil,
            "R_surface": R, "R_total": Rtot, "T_display_path": Tdisp}


def illuminance_for_background(L_min: float, rho_min=0.14, T=1.0) -> float:
    return L_min * math.pi / (rho_min * T)


# ---------------------------------------------------------------------------------------------
# Timing budgets (REQ-SYS-067, REQ-SYS-068, REQ-SW-KEYER-014)
# ---------------------------------------------------------------------------------------------
FULL_FRAME_MS = 16.8          # F1: full frame at 1.1 MHz
UI_TICK_MS = 20.0             # proposed UI task period (50 Hz)
UI_MAX_FPS = 25.0             # proposed display update rate limit


def fault_latency_budget(lc_response_ms: float = 500.0):
    items = [
        ("detection to KEY inhibit report (REQ-SW-KEYER-023, other causes by the same rule)", 20.0),
        ("wait for the next UI task tick (20 ms period)", UI_TICK_MS),
        ("render the message into the frame buffer (assumption A-U6)", 2.0),
        ("wait for a frame already in flight (one full frame)", FULL_FRAME_MS),
        ("write the changed lines (bounded by one full frame at 1.1 MHz)", FULL_FRAME_MS),
        ("liquid-crystal optical response at -10 C (assumption A-U5)", lc_response_ms),
    ]
    return items, sum(v for _, v in items)


def id_reminder_error_s(interval_s=540.0, xtal_ppm=50.0, lc_response_ms=500.0):
    """Worst early and late error of the reminder instant against the requirement nominal."""
    late = interval_s * xtal_ppm * 1e-6 + UI_TICK_MS / 1000 + (2 * FULL_FRAME_MS) / 1000 \
        + lc_response_ms / 1000
    early = interval_s * xtal_ppm * 1e-6
    return early, late
