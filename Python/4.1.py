# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 11:28:06 2018

@author: Dr. Neptune
"""

# 4.1 | Functions and Scoping

# Bisection search to approximate square root

x = 25
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, x)
ans = (low + high)/2.0

while abs(ans**2 - x) >= epsilon:
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2.0
print('numGuesses = ', numGuesses)
print(ans, 'is close to the square root of', x)

# maxVal

def maxVal(x, y):
    if x > y:
        return x
    else: 
        return y
    
# finger exercise

def isIn(a, b):
        if ((a in b) or (b in a)):
            return True;
        else:
            return False;
        
# 4.1.2 Keyword Arguments and Default Values

def printName(firstName, lastName, reverse):
    if reverse:
        print(lastName + ", " + firstName)
    else:
        print(firstName, lastName)
        
printName("Olga", "Puck", True)


def printName(firstName, lastName, reverse = False):
    if reverse:
        print(lastName + ", " + firstName)
    else:
        print(firstName, lastName)
        
printName("Olga", "Puck")

# scoping

def f(x):
    y = 1
    x = x + y
    print('x =', x)
    return x

x = 3
y = 2
z = f(x)

print('z =', z)
print('x =', x)
print('y =', y)

def f(x):
    def g():
        x = 'abc'
        print('x =', x)
    def h():
        z = x
        print('z =', z)
    x = x + 1
    print('x =', x)
    h()
    g()
    print('x =', x)
    return g

x = 3
z = f(x)
print('x =', x)
print('z =', z)
z()