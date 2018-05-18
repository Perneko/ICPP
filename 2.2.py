# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 08:50:31 2018

@author: Dr. Neptune
"""

# 2.2 | Branching Programs

# even or odd

x = 9
y = 10 
z = 12

if x%2 == 0:
    print("even")
else:
    print("odd")

print("Done with conditional")

# nested conditionals

if x%2 == 0:
    if x%3 == 0:
        print("Divisible by 2 and 3")
    else: 
        print("Divisible by 2 and not 3")
elif x%3 == 0:
    print("Divisible by 3 and not by 2")
    
# compound boolean expression 

if x < y and x < z:
    print("x is least")
elif y < z:
    print("y is least")
else: 
    print("z is least")
    
# finger exercise

if (x%2 != 0):
    if (y%2 != 0):
        if (z%2 != 0):
            if x > y and x > z:
                print("x is greatest")
            elif y > z:
                print("y is greatest")
            else: 
                print("z is greatest")
        if x > y:
            print("x is the greatest")
        else: 
            print("y is the greatest")
    else: 
        print("z is the greatest")
    