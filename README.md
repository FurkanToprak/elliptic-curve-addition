# Elliptic Curve Addition

Well-tested implementation of the Elliptic Curve Addition Algorithm in Python. 

<html>
<img src="coverage.svg">
</html>

## Usage
```
elliptic_curve = EllipticCurve(2, 3, 97)
p1 = (17, 10)
p2 = (95, 31)
new_point = elliptic_curve.add(p1, p2)
print(new_point) # (1, 54)
```