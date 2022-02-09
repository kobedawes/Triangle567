# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest
import math
from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right')
        self.assertEqual(classifyTriangle(5, 12, 13),'Right')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4), 'Right')
        self.assertEqual(classifyTriangle(13, 12, 5), 'Right')
        
    def testIsoscelesA(self):
        self.assertEqual(classifyTriangle(1, 1, 3), 'Isosceles')
        self.assertEqual(classifyTriangle(3, 1, 3), 'Isosceles')
        self.assertEqual(classifyTriangle(5, 1, 1), 'Isosceles')

    def testIsoscelesB(self):
        self.assertEqual(classifyTriangle(3, 1, 1), 'Isosceles')
        self.assertEqual(classifyTriangle(3, 3, 1), 'Isosceles')
        self.assertEqual(classifyTriangle(1, 1, 5), 'Isosceles')

    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral')
        self.assertEqual(classifyTriangle(3, 3, 3), 'Equilateral')
        self.assertEqual(classifyTriangle(5, 5, 5), 'Equilateral')

    def testScaleneTriangles(self):
        self.assertEqual(classifyTriangle(1, 3, 5), 'Scalene')
        self.assertEqual(classifyTriangle(7, 5, 12), 'Scalene')
        self.assertEqual(classifyTriangle(6, 5, 8), 'Scalene')

    def testNotATriangle(self):
        self.assertEqual(classifyTriangle(5, 7, 10), 'NotATriangle')
        self.assertEqual(classifyTriangle(20, 5, 7), 'NotATriangle')
        self.assertEqual(classifyTriangle(5, 6, 20), 'NotATriangle')

    def testInvalidInputA(self):
        self.assertEqual(classifyTriangle(300, 150, 200), 'InvalidInput')
        self.assertEqual(classifyTriangle(200, 300, 150), 'InvalidInput')
        self.assertEqual(classifyTriangle(150, 200, 300), 'InvalidInput')

    def testInvalidInputB(self):
        self.assertEqual(classifyTriangle(-34, 150, 200), 'InvalidInput')
        self.assertEqual(classifyTriangle(300, -34, 200), 'InvalidInput')
        self.assertEqual(classifyTriangle(300, 150, -34), 'InvalidInput')

    def testInvalidInputC(self):
        self.assertEqual(classifyTriangle(.08, 150, 200), 'InvalidInput')
        self.assertEqual(classifyTriangle(300, '150', 200), 'InvalidInput')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

