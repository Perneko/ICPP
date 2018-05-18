# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 10:12:48 2018

@author: Dr. Neptune
"""

# 3.2 | For Loops 


# changing x inside loop does not change iterations
x = 4

for i in range(x):
    print(i)
    x = 5

# double loop

x = 4

for j in range(x):
    for i in range(x):
        print(i)
        x = 2
        
# Find the cube root of a perfect cube

x = int(input('Enter an integer: '))
for ans in range(0, abs(x)+1):
    if ans**3 >= abs(x):
        break
if ans**3 != abs(x):
    print(x, 'is not a perfect cube')
else: 
    if x < 0:
        ans = -ans
    print('Cube root of', x, 'is', ans)
    
# sum digits in a string

total = 0
for c in '1235678':
    total += int(c)
print(total)

# finger exercise

overall = 0
s = '1.23, 2.4, 3.123'
s = s.split(',')
for c in s:
    overall += float(c)
print(overall)

