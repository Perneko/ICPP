# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 12:21:21 2018

@author: Dr. Neptune
"""

# 5.4| Functions as Objects

'''
In python, functions are first class objects. They can be treated like objects
of other types, such as int or list. 
Using functions as arguments allows a style of coding called 
higher-order programming
'''

#%%

def factR(n):
    '''
    assumes n is an integer
    finds n!
    '''
    if n == 0 or n == 1:
        return 1
    else:
        return n * factR(n-1)

def fib(n):
    '''
    Assumes n is an integer
    returns nth fibonacci number
    '''
    
    if n == 0 or n == 1:
        return 1
    else: 
        return fib(n-1) + fib(n-2)

def applyToEach(L, f):
    '''
    Assumes L is a list, f is a function
    Mutates L by replacing each element, e, of L by f(e)
    '''
    
    for i in range(len(L)):
        L[i] = f(L[i])
        
L = [1, -2, 3.33]
print('L =', L)

print('apply abs to each element of L:')
applyToEach(L, abs)
print('L =', L)

print('apply int to each element of L:')
applyToEach(L, int)
print('L =', L)

print('Apply factorial to each element of L:')
applyToEach(L, factR)
print('L =', L)

print('Apply fibonacci to each element of L:')
applyToEach(L, fib)
print('L =', L)

#%%

for i in map(fib, [2,6,4]):
    print(i)
    
L1 = [1, 28, 36]
L2 = [2, 57, 9]
for i in map(min, L1, L2):
    print(i)
    
'''
lambda <sequence of variable names>: <expression>
'''

L = []
for i in map(lambda x, y: x**y, [1, 2, 3, 4], [3, 2, 1, 0]):
    L.append(i)
print(L)