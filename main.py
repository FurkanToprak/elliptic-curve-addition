from sympy import isprime

class EllipticCurve:
    def __init__(self, a, b, p=None):
        """
        Construct an elliptic curve in the format
        E: Y^2 = X^3 - a*X + b
        """
        if 4 * (a ** 3) + 27 * (b ** 2) == 0:
            raise ValueError("Error: Singular curves not excluded. Ensure 4A^3+27B^2!=0.")
        if not isprime(p):
            raise ValueError("Error: Modulo ring is not prime.")
        self.a = a
        self.b = b

    def add(self, p1, p2):
        """
        Add two points on the curve.
        p1: (x1, y1) or "O"
        p2: (x2, y2) or "O"
        """
        if p1 == "O":
            return p2
        elif p2 == "O":
            return p1
        x1, y1 = p1
        x2, y2 = p2
        if x1 == x2 and y1 == -1 * y2:
            return "O"
        lamb = None
        if p1 == p2:
            lamb = (3 * (x1 ** 2) + self.a) / (2 * y1)
        else:
            lamb = (y2 - y1) / (x2 - x1)
        x3 = lamb ** 2 - x1 - x2
        y3 = lamb * (x1 - x3) - y1
        return (x3, y3)
