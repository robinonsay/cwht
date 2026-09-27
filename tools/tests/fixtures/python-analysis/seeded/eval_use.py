"""Seeded security fault: eval of text (expected code S307)."""


def parse(text: str) -> object:
    """Evaluate a literal."""
    return eval(text)
