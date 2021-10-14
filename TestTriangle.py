# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from triangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class Testtriangle(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangle(self): 
        self.assertEqual(classify_triangle(3,4,5),'Right')
        
    def testIsoscelesTriangle(self): 
        self.assertEqual(classify_triangle(3,3,4),'Isosceles')
               
    def testEquilateralTriangle(self): 
        self.assertEqual(classify_triangle(1,1,1),'Equilateral')
        
    def testScaleneTriangle(self): 
        self.assertEqual(classify_triangle(4,7,9),'Scalene')
        
    def testInvalidInputInteger(self): 
        self.assertEqual(classify_triangle(4,7,9.9),'InvalidInput')
        
    def testInvalidInputNegativeValue(self): 
        self.assertEqual(classify_triangle(4,-7,9),'InvalidInput')
        
    def testInvalidInputZeroValue(self): 
        self.assertEqual(classify_triangle(0,7,9),'InvalidInput')
        
    def testInvalidInputOutOfBounds(self): 
        self.assertEqual(classify_triangle(400,700,900),'InvalidInput')
        
    def testNotATriangle(self): 
        self.assertEqual(classify_triangle(7,4,1),'NotATriangle')
        

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

