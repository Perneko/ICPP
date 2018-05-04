#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 14:42:43 2018

@author: michael
"""

import random

# 13 | Dynamic Programming 

#%% Fibonacci Sequences, Revisited

def fib(n):
    if n == 0 or n == 1:
        return 1
    else: 
        return fib(n-1) + fib(n-2)

# this does the same calculations multiple times. We can store the value and refer to it. This is called memoization

def fastFib(n, memo = {}):
    '''
    Assumes n is an int >= 0, memo used only by recursive calls
    Returns nth fibonacci number
    '''
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fastFib(n-1, memo) + fastFib(n-2, memo)
        memo[n] = result
        return result 
    
fastFib(120)

#%% 13.2 | Dynamic Programming and the 0/1 Knapsack Problem

def maxVal(toConsider, avail):
    '''
    Assumes toConsider a list of items, avail a weight
    Returns a tuple of the total value of a solution to the 0/1 knapsack problem and the items of that solution
    '''
    if toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getWeight() > avail:
        # Explore right branch only
        result = maxVal(toConsider[1:], avail)
    else:
        nextItem = toConsider[0]
        # Explore left branch
        withVal, withToTake = maxVal(toConsider[1:], avail - nextItem.getWeight())
        withVal = withVal + nextItem.getValue()
        # Explore right branch
        withoutVal, withoutToTake = maxVal(toConsider[1:], avail)
        # choose better branch
        if withVal > withoutVal: 
            result = (withVal, withToTake + (nextItem,))
        else: 
            result = (withoutVal, withoutToTake)
    return result 

class Item(object):
    
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.weight = w
    
    def getName(self):
        return self.name
    
    def getValue(self):
        return self.value
    
    def getWeight(self):
        return self.weight
    
    def __str__(self):
        result = '<' + self.name + ',' + str(self.value) + ',' + str(self.weight) + '>'
        return result 

def smallTest():
    
    names = ['a', 'b', 'c', 'd']
    vals = [6, 7, 8, 9]
    weights = [3, 3, 2, 5]
    Items = []
    
    for i in range(len(vals)):
        Items.append(Item(names[i], vals[i], weights[i]))
    
    val, taken = maxVal(Items, 5)
    for item in taken:
        print(item)
    print('Total value of items taken = ', val)

def buildManyItems(numItems, maxVal, maxWeight):
    items = []
    for i in range(numItems):
        items.append(Item(str(i), random.randint(1, maxVal), random.randint(1, maxWeight)))
    return items

def bigTest(numItems):
    items = buildManyItems(numItems, 10, 10)
    val, taken = maxVal(items, 40)
    print('Items Taken')
    for item in taken: 
        print(item)
    print('Total value of items taken =', val)

#%% 
smallTest()

bigTest(10)

#%% 

def fastMaxVal(toConsider, avail, memo = {}):
    '''
    Assumes toConsider a list of items, avail a weight, memo supplied by recursive calls
    Returns a tuple of the total value of a solution to the 0/1 knapsack problem and the items of that solution
    '''
    
    if (len(toConsider), avail) in memo:
        result = memo[(len(toConsider), avail)]
    elif (toConsider == [] and avail == 0):
        result = (0, ())
    elif (toConsider[0].getWeight() > avail):
        # Explore right branch only
        result = fastMaxVal(toConsider[1:], avail, memo)
    else: 
        nextItem = toConsider[0]
        # Explore left branch 
        withVal, withToTake = fastMaxVal(toConsider[1:], avail - nextItem.getWeight(), memo)
        withVal += nextItem.getValue()
        # Explore right branch
        withoutVal, withoutToTake = fastMaxVal(toConsider[1:], avail, memo)
        # Choose better branch
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else: 
            result = (withoutVal, withoutToTake)
    memo[(len(toConsider), avail)] = result 
    return result 


    
    