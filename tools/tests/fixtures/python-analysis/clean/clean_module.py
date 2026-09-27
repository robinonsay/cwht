"""Clean fixture: no finding under the TV-024 rule set."""

import json


def load_ids(text: str) -> list[str]:
    """Return the sorted ids of a JSON list of objects with an "id" key."""
    items = json.loads(text)
    return sorted(item["id"] for item in items)


def at_limit(x: int) -> int:
    """Cyclomatic complexity 15 (fourteen if statements): at the limit, not reported."""
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
    return n
