# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 10:39:07 2018

@author: Dr. Neptune
"""

# 3.3 | Approximate Solutions and Bisection Search 

# approximation of a square root

x = 1
epsilon = 0.01
step = epsilon**2
numGuesses = 0
ans = 0.0

while abs(ans**2 - x) >= epsilon and ans*ans <= x:
    ans += step
    numGuesses += 1
print('numGuesses =', numGuesses)
if abs(ans**2 - x) >= epsilon:
    print('Failed on square root of', x)
else: 
    print(ans, 'is close to square root of', x)
    
# approximation using lgn time 

x = -25
epsilon = 0.01 
numGuesses = 0
low = 0.0
high = max(1.0, x)
ans = (high + low)/2.0

while abs(ans**2 - x) >= epsilon:
    print('low =', low, 'high =', high, 'ans =', ans)
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print('numGuesses =', numGuesses)
print(ans, 'is close to square root of', x)

# finger exercise

# the code would consistently decrease and run on forever 


