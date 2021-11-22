from main import EllipticCurve
import pytest


class Tester:
    def testInit(self):  # testing non-primes and wrong A,B.
        with pytest.raises(ValueError):
            c0 = EllipticCurve(2, 2, 1)
        with pytest.raises(ValueError):
            c0 = EllipticCurve(0, 0, 3)

    def testAddInput(self):  # testing "O"
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
        # verify the entire table
        for i, input1 in enumerate(inputs):
            if input1 != "O":
                assert c1.onCurve(input1)
            for j, input2 in enumerate(inputs):
                assert ver_table[i][j] == "O" or c1.onCurve(ver_table[i][j])
                assert ver_table[i][j] == c1.add(input1, input2)

        c2 = EllipticCurve(2, 3, 97)
        assert c2.onCurve((1, 54))
        assert (1, 54) == c2.add((17, 10), (95, 31))

        c3 = EllipticCurve(7, 8, 101)
        assert c3.onCurve((31, 76))
        assert (31, 76) == c3.add((7, 20), (79, 35))

        c4 = EllipticCurve(5, 7, 7727)
        assert c4.onCurve((5904, 5297))
        assert c4.onCurve((1574, 3249))
        assert (5904, 5297) == c4.add((317, 878), (119, 1426))
        assert (1574, 3249) == c4.add((317, 878), (18, 77))
