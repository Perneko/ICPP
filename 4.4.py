# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 08:39:36 2018

@author: Dr. Neptune
"""

# 4.4 | Global Variables

def fib(x):
    '''
        Assumes x an int >= 0
        Returns fibonacci of x
    '''
    
    global numFibCalls
    numFibCalls += 1
    
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

def testFib(n):
    for i in range(n+1):
        global numFibCalls
        numFibCalls = 0
        print('fib of', i, '=', fib(i))
        print('fib called', numFibCalls, 'times.')