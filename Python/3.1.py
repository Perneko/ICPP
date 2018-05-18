# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 09:59:44 2018

@author: Dr. Neptune
"""

# 3.1 | Exhaustive Enumeration

# integer cube root
x = int(input('Enter an integer: '))
ans = 0
while ans**3 < abs(x):
    #print('Value of the decrementing function abs(x) - ans**3 is', abs(x)-ans**3)
    ans = ans + 1
if ans**3 != abs(x):
    print(x, 'is not a perfect cube')
else:
    if x < 0:
        ans = -ans
    print('Cube root of', x, 'is', ans)


# maxval

maxVal = int(input('Enter a positive integer: '))
i = 0
while i < maxVal:
    i = i + 1
print(i)

# finger exercise

