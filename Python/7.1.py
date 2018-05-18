# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 12:02:24 2018

@author: Dr. Neptune
"""

# 7.1 | Handling Exceptions

#%%

numSuccesses = 10
numFailures = 10

successFailureRatio = numSuccesses / numFailures
print('The success / failure ratio is', successFailureRatio)
print('Now here')

#%% instead use
try:
    successFailureRatio = numSuccesses / numFailures
    print('The success / failure ratio is', successFailureRatio)
except ZeroDivisionError:
    print('No failures, so the success/failure ratio is undefined')
print('Now here')

#%% Finger exercise page 102

def sumDigits(str):
    '''
    Assumes s is a string
    Returns the sum of the decimal digits in s
    For example, if s is 'a2b3c' it returns 5
    '''
    try:
        digits = [int(s) for s in str if s.isdigit()]
        return sum(digits)
    except:
        # not really sure what to catch


#%% 
# consider
val = int(input('Enter an integer: '))
print('The square of the number you entered is', val**2)

# better
while True:
    val = input('Enter an integer: ')
    try:
        val = int(val)
        print('The square of the number you entered is', val**2)
        break # to exit the loop
    except ValueError:
        print(val, 'is not an integer')
        
#%% 
# if there are many places where a user is asked to input an int
# make a function

def readInt():
    while True:
        val = input('Enter an integer: ')
        try:
            return(int(val)) # convert str to int
        except ValueError:
            print(val, 'is not an integer')
            
# generalized, for any input

def readVal(valType, requestMsg, errorMsg):
    while True:
        val = input(requestMsg + ' ')
        try:
            return(valType(val)) # conv str to valType before returning
        except ValueError:
            print(val, errorMsg)
            
readVal(int, 'Enter an integer: ', 'is not an integer')