#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 10:22:31 2018

@author: michael
"""

# 10.2 | Sorting Algorithms

def selSort(L):
    '''
    Assumes that L is a list of elements that can be compared using >
    Sorts L in ascending order
    '''
    suffixStart = 0
    while suffixStart != len(L):
        # look at each element in suffix
        for i in range(suffixStart, len(L)):
            if L[i] < L[suffixStart]:
                # swap position of elements
                L[suffixStart], L[i] = L[i], L[suffixStart]
            suffixStart += 1
    return L
# garbage

def selectionSort(source):
    for i in range(len(source)):
        mini = min(source[i:]) #find minimum element
        min_index = source[i:].index(mini) #find index of minimum element
        source[i + min_index] = source[i] #replace element at min_index with first element
        source[i] = mini                  #replace first element with min element
    return source

#%% 10.2.1 | Merge Sort

#1. If the list is of length 0 or 1, it is already sorted
#2. If the list has more than one element, split the list into two lists, and use mergesort to sort each of them
#3. Merge the results

def merge(left, right, compare):
    '''
    Asumes left and right are sorted lists and compare defines an ordering on the elements.
    Returns a new sorted (by compare) list containing the same elements as (left + right) would contain
    '''
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result

def mergeSort(L, compare = lambda x, y: x < y):
    '''
    Assumes that L is a list, compare defines an ordering on elements of L
    Returns a new sorted list with the same elements as L
    '''
    if len(L) < 2:
        return L[:]
    else: 
        middle = len(L)//2
        left = mergeSort(L[:middle], compare)
        right = mergeSort(L[middle:], compare)
        return merge(left, right, compare)
    
#%%

def lastNameFirstName(name1, name2):
    arg1 = name1.split(' ')
    arg2 = name2.split(' ')
    if arg1[1] != arg2[1]:
        return arg1[1] < arg2[1]
    else: # last names the same, sort by first name
        return arg1[0] < arg2[0]
    
def firstNameLastName(name1, name2):
    arg1 = name1.split(' ')
    arg2 = name2.split(' ')
    if arg1[0] != arg2[0]:
        return arg1[0] < arg2[0]
    else: # first names are the same, sort by last name
        return arg1[1] < arg2[1]
    
L = ['Tom Brady', 'Eric Grimson', 'Gisele Bundchen']
newL = mergeSort(L, lastNameFirstName)
print('Sorted by last name = ', newL)
newL = mergeSort(L, firstNameLastName)
print('Sorted by first name = ', newL)

