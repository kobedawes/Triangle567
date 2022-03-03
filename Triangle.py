"""verifies if the three inputs can form a triangle"""


def classify_triangle(a, b, c):
    """verifies if the three inputs can form a triangle"""
    if not(isinstance(a,int) and isinstance(b,int) and isinstance(c,int)) or a > 200 \
            or b > 200 or c > 200 or a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'

    if (a + b)<c or (b + c) < a or (c + a) < b:
        return 'NotATriangle'
    if a == b == c == a:
        return 'Equilateral'
    if ((a ** 2) + (b ** 2)) == (c ** 2) or ((a ** 2) + (c ** 2)) == (b ** 2) \
            or ((c ** 2) + (b ** 2)) == (a ** 2):
        return 'Right'
    if a != b != c != a:
        return 'Scalene'
    else:
        return 'Isosceles'
