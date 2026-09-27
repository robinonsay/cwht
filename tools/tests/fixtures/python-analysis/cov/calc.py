"""Coverage fixture: one function with one two-way branch (4 statements: lines 4, 6, 7 and 8)."""


def sign(x: int) -> int:
    """Return -1 for a negative x, else 1."""
    if x < 0:
        return -1
    return 1
