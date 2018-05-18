# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

pi = 3
radius = 11
area = pi * (radius**2)
radius = 14

side = 1 # length of sides of a unit square
radius = 1 # radius of a unit circle
# subtract area of a unit circle from area of unit square
areaC = pi*radius**2
areaS = side*side
difference = areaS - areaC

# multiple assignment

x, y = 2, 3
x, y = y, x
print("x = ", x)
print("y = ", y)