# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 11:06:47 2018

@author: Dr. Neptune
"""

# 6.1 | Testing

#%% 
def copy(L1, L2):
    ''' 
    Assumes L1, L2 are lists
    Mutates L2 to be a copy of L1
    '''
    while len(L2) > 0: # remove all elements from L2
        L2.pop() # remove last element from L2
    for e in L1: # append L1s elements to initially empty L2
        L2.append(e)
        
#%% 
def isPrime(x):
    '''
    Assumes x is a non negative integer
    Returns true is x is prime, false ow
    '''
    if x <= 2:
        return False
    for i in range(2, x):
        if x%i == 0:
            return False
    return True