"""Seeded complexity fault: cyclomatic complexity 16 above the limit 15 (expected code C901)."""


def over_limit(x: int) -> int:
    """Fifteen if statements: complexity 16."""
    n = 0
    if x > 1:
        n += 1
    if x > 2:
        n += 1
    if x > 3:
        n += 1
    if x > 4:
        n += 1
    if x > 5:
        n += 1
    if x > 6:
        n += 1
    if x > 7:
        n += 1
    if x > 8:
        n += 1
    if x > 9:
        n += 1
    if x > 10:
        n += 1
    if x > 11:
        n += 1
    if x > 12:
        n += 1
    if x > 13:
        n += 1
    if x > 14:
        n += 1
    if x > 15:
        n += 1
    return n
