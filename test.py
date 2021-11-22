from sympy.functions.elementary.trigonometric import asec
from main import EllipticCurve
import pytest


class Tester:
    def testInit(self):
        # should raise
        with pytest.raises(ValueError):
            c0 = EllipticCurve(2, 2, 1)
        # should raise
        with pytest.raises(ValueError):
            c0 = EllipticCurve(0, 0, 3)
        # shouldnt raise
        c1 = EllipticCurve(1, 2, 7)

    def testAddInput(self):
        fixCurve = EllipticCurve(1, 2, 7)
        assert (5, 5) == fixCurve.add("O", (5, 5))
        assert (5, 5) == fixCurve.add((5, 5), "O")
        assert "O" == fixCurve.add("O", "O")

    def testActualMath(self):
        inputs = [
            "O",
            (1, 5),
            (1, 8),
            (2, 3),
            (2, 10),
            (9, 6),
            (9, 7),
            (12, 2),
            (12, 11),
        ]
        # table from textbook
        ver_table = [
            inputs,  # identity
            [(1, 5), (2, 10), "O", (1, 8), (9, 7), (2, 3), (12, 2), (12, 11), (9, 6)],
            [(1, 8), "O", (2, 3), (9, 6), (1, 5), (12, 11), (2, 10), (9, 7), (12, 2)],
            [(2, 3), (1, 8), (9, 6), (12, 11), "O", (12, 2), (1, 5), (2, 10), (9, 7)],
            [(2, 10), (9, 7), (1, 5), "O", (12, 2), (1, 8), (12, 11), (9, 6), (2, 3)],
            [(9, 6), (2, 3), (12, 11), (12, 2), (1, 8), (9, 7), "O", (1, 5), (2, 10)],
            [(9, 7), (12, 2), (2, 10), (1, 5), (12, 11), "O", (9, 6), (2, 3), (1, 8)],
            [(12, 2), (12, 11), (9, 7), (2, 10), (9, 6), (1, 5), (2, 3), (1, 8), "O"],
            [(12, 11), (9, 6), (12, 2), (9, 7), (2, 3), (2, 10), (1, 8), "O", (1, 5)],
        ]
        c1 = EllipticCurve(3, 8, 13)
        for i, input1 in enumerate(inputs):
            for j, input2 in enumerate(inputs):
                assert ver_table[i][j] == c1.add(input1, input2)
