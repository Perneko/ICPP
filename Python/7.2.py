# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 12:49:33 2018

@author: Dr. Neptune
"""

# 7.2 | Exceptions as a Control Flow Mechanism

#%% Finger Exercise page 105
def findEven(L):
    '''
    Assumes L is a list of integers
    Returns the first even number in L
    Raises ValueError is L does not contain an even number
    '''
    for e in L:
        if (e%2 == 0):
            return e
    raise ValueError()
    
#%% 
def getRatios(vect1, vect2):
    '''
    Assumes: vect1 and vect 2 are equal length lists of numbers
    Returns: A list containing the meaningful values of vect1[i]/vect2[i]
    '''
    ratios = []
    for index in range(len(vect1)):
        try:
            ratios.append(vect1[index] / vect2[index])
        except ZeroDivisionError:
            ratios.append(float('nan')) # nan = Not a Number
        except:
            raise ValueError('getRatios called with bad arguments')
    return ratios

#%% same as above, but without try except
def getRatios2(vect1, vect2):
    '''
    Assumes: vect1 and vect2 are lists of equal length of numbers
    Returns: a list containing the meaningful values of vect1[i]/vect2[i]
    '''
    ratios = []
    if (len(vect1) != len(vect2)):
        raise ValueError('getRatios called with bad arguments')
    for index in range(len(vect1)):
        vect1Elem = vect1[index]
        vect2Elem = vect2[index]
        if (type(vect1Elem) not in (int, float)) or (type(vect2Elem) not in (int, float)):
            raise ValueError('getRatios called with bad arguments')
        if vect2Elem == 0.0:
            ratios.append(float('NaN')) #NaN = Not a Number
        else: 
            ratios.append(vect1Elem / vect2Elem)
    return ratios

#%% 
def getGrades(fname):
    try:
        gradesFile = open(fname, 'r') # open file for reading
    except IOError:
        raise ValueError('getGrades could not open ', + fname)
    grades = []
    for line in gradesFile:
        try:
            grades.append(float(line))
        except:
            raise ValueError('Unable to convert line to float')
    return grades

# test
try:
    grades = getGrades('quiz1grades.txt')
    grades.sort()
    median = grades[len(grades)//2]
    print('Median grade is', median)
except ValueError as errorMsg:
    print('Whoops.', errorMsg)
    
    