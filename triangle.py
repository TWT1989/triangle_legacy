# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""
def classify_triangle(a1_,b2_,c3_):
    """
    Your correct code goes here...  Fix the faulty logic below until the code passes all of
    you test cases.
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
      BEWARE: there may be a bug or two in this code
    """
    # require that the input values be > 0 and <= 200
    if a1_ > 200 or b2_ > 200 or c3_ > 200:
        return 'InvalidInput'
    if a1_ <= 0 or b2_ <= 0 or c3_ <= 0:
        return 'InvalidInput'
    # verify that all 3 inputs are integers
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not isinstance(a1_,int) or not isinstance(b2_,int) or not isinstance(c3_,int):
        return 'InvalidInput'
    # This information was not in the requirements spec but
    # is important for correctness
    # the sum of any two sides must be strictly greater than or equal to the third side
    # of the specified triangle otherwise it is not a triangle
    if (a1_ > (b2_ + c3_)) or (b2_ > (a1_ + c3_)) or (c3_ > (a1_ + b2_)):
        return 'NotATriangle'
    # now we know that we have a valid triangle
    elif a1_ == b2_ and b2_ == c3_:
        return 'Equilateral'
    elif ((a1_ ** 2) + (b2_ ** 2)) == (c3_ ** 2):
        return 'Right'
    elif a1_ == b2_ or b2_ == c3_ or a1_ == b2_:
        return 'Isosceles'
    else:
        return 'Scalene'
    