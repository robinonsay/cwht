"""Seeded gap: only the non-negative case, so `return -1` (line 7) and the True outcome of line 6 are never executed."""

import unittest

from calc import sign


class SignGapTests(unittest.TestCase):
    def test_positive(self) -> None:
        self.assertEqual(sign(5), 1)


if __name__ == "__main__":
    unittest.main()
