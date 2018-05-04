#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 09:43:47 2018

@author: michael
"""

# Chapter 10 | Some Simple Algorithms and Data Structures

# 10.1 | Search Algorithms

#%% 

def search(L, e):
    '''
    Assumes L is a list
    Returns true is e is in L and false ow
    '''
    if len(L) == 0:
        return False
    else:
        for part in L:
            if part == e:
                return True
        return False;
    
#%% Linear Search and Using Indirection to Access Elements

def linear_search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
    return False

#%% Binary Search and Exploiting Assumptions

def sortedSearch(L, e):
    '''
    Assumes L is a list sorted in ascending order
    Returns True if e in list, false OW
    '''
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False

# binary search: 
#    1. pick an index i that divides the list L in half
#    2. Ask if L[i] == e
#    3. If not, ask whether L[i] is larger or smaller than e
#    4. Depending upon the answer, search either the right or left half of L

def binarySearch(L, e):
    '''
    Assumes L is a list, the elements of which are in ascending order
    Returns true is e is in L and false otherwise
    '''
    def bSearch(L, e, low, high):
        # Decremenets high - low
        if high == low:
            return L[low] == e
        mid = (high + low)//2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid: # nothing left to search
                return False
            else:
                return bSearch(L, e, low, mid-1)
        else:
            return bSearch(L, e, mid + 1, high)
        
    if len(L) == 0:
        return False
    else: 
        return bSearch(L, e, 0, len(L)-1)
    
# Finger Exercise : The code uses mid + 1 instead of mid in the second 
# Recursive call because we are splitting the list to the interval of [mid+1, high]
# and we already know that e is not mid. If we were to say that mid > e we would
# have split the list on the interval [low, mid-1]


    