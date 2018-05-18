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


#%%
def abs(x):
    '''
    Assumes x is an int
    returns x if x >= 0 and -x otherwise
    '''
    if x < 0:
        return -x
    else: 
        return x
    
    
'''
Rules of Thumb for Glass Box Testing: 
    1. Exercise both branches of all if statements
    2. Make sure that each except clause is executed
    3. For each for loop, have cases which:
        a. the loop is not entered
        b. The body of the loop is executed exactly once
        c. The body of the loop is executed more than once
    4. For each while loop:
        a. Look at the same cases as for loops
        b. Include cases with all ways of exiting the loop
    5. For recursive functions, include test cases that cause the f(x) to
       return with no recursive calls, exactly one recursive call, and more
       than one recursive call.
'''
