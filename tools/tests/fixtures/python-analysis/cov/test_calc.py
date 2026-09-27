"""Executes every statement and both outcomes of the branch of calc.sign."""

import unittest

from calc import sign


class SignTests(unittest.TestCase):
    def test_negative(self) -> None:
        self.assertEqual(sign(-5), -1)

    def test_positive(self) -> None:
        self.assertEqual(sign(5), 1)


if __name__ == "__main__":
    unittest.main()
