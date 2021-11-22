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

    def testAddInput():
        fixCurve = EllipticCurve(1, 2, 7)
        assert (5, 5) == fixCurve.add("O", (5, 5))
        assert (5, 5) == fixCurve.add((5, 5) == "O")
        assert "O" == fixCurve.add("O", "O")