"""test cases for triangle assignment"""
import unittest
from triangle import classify_triangle


class TestTriangles(unittest.TestCase):
    """test cases for triangle assignment"""

    def test_right_triangle(self):
        """TESTS FOR RIGHT TRIANGLES"""
        self.assertEqual(classify_triangle(3, 4, 5),'Right')
        self.assertEqual(classify_triangle(5, 12, 13),'Right')
        self.assertEqual(classify_triangle(5, 3, 4), 'Right')
        self.assertEqual(classify_triangle(13, 12, 5), 'Right')

    def test_isosceles_triangle(self):
        """TESTS FOR isosceles triangle"""
        self.assertEqual(classify_triangle(2, 2, 1), 'Isosceles')
        self.assertEqual(classify_triangle(3, 1, 3), 'Isosceles')
        self.assertEqual(classify_triangle(1, 5, 5), 'Isosceles')

    def test_equilateral_triangle(self):
        """tests for equilateral triangles"""
        self.assertEqual(classify_triangle(1, 1, 1), 'Equilateral')
        self.assertEqual(classify_triangle(3, 3, 3), 'Equilateral')
        self.assertEqual(classify_triangle(5, 5, 5), 'Equilateral')

    def test_scalene_triangle(self):
        """tests for scalene triangles"""
        self.assertEqual(classify_triangle(2, 3, 4), 'Scalene')
        self.assertEqual(classify_triangle(7, 5, 12), 'Scalene')
        self.assertEqual(classify_triangle(6, 5, 8), 'Scalene')

    def test_not_a_triangle(self):
        """tests for not a  triangles"""
        self.assertEqual(classify_triangle(5, 7, 20), 'NotATriangle')
        self.assertEqual(classify_triangle(20, 5, 7), 'NotATriangle')
        self.assertEqual(classify_triangle(5, 6, 20), 'NotATriangle')

    def test_invalid_input_a(self):
        """tests for invalid input"""
        self.assertEqual(classify_triangle(300, 150, 200), 'InvalidInput')
        self.assertEqual(classify_triangle(200, 300, 150), 'InvalidInput')
        self.assertEqual(classify_triangle(150, 200, 300), 'InvalidInput')

    def test_invalid_input_b(self):
        """tests for invalid input"""
        self.assertEqual(classify_triangle((-34), 40, (-67)), 'InvalidInput')
        self.assertEqual(classify_triangle(12, (-34), 30), 'InvalidInput')
        self.assertEqual(classify_triangle((-45), (-23), (-34)), 'InvalidInput')

    def test_invalid_input_c(self):
        """tests for invalid input"""
        self.assertEqual(classify_triangle(.08, 150, 200), 'InvalidInput')
        self.assertEqual(classify_triangle(300, '150', 200), 'InvalidInput')
        self.assertEqual(classify_triangle([2, 3, 4], 6, 9), 'InvalidInput')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
