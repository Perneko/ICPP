# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 11:30:12 2018

@author: Dr. Neptune
"""

# 6.2 | Debugging

#%%
def isPal(x):
    '''
    Assumes x is a list
    Returns true is the list is a palindrome; False ow
    '''
    temp = x[:] # this creates a copy of x so that way we don't get aliasing
    # aliasing is when we manipulate the same object, thus changing temp also changes x
    temp.reverse()
    if temp == x:
        return True
    else:
        return False
    
def silly(n):
    '''
    Assumes n is an int > 0
    Gets n inputs from user
    Prints yes if the sequence of user inputs forms a palindrome, no ow
    '''
    result = []
    for i in range(n):
        elem = input('Enter element: ')
        result.append(elem)
    print(result)
    if isPal(result):
        print('Yes')
    else:
        print('No')
        
'''
Usual Suspects:
    1. Passed arguments in the wrong order
    2. Misspelled a name, e.g a lowercase instead of an uppercase
    3. Failed to reinitialize a varaince
    4. tested that 2 floating point values are equal instead of nearly equal
    5. testing for value equality (e.g. compared 2 lists by writing L1 == L2
       when you meant object equality like id(L1) == id(L2))
    6. Forgotten that some built in function has a side effect
    7. Forgotten the () that turns a reference to an object of type function
       into a function invocation.
    8. Created an unintentional aliass
    9. Made any other mistake that is typical for you
'''

