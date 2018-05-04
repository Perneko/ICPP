#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 07:58:43 2018

@author: michael
"""

# 22 | A Quick Look at Machine Learning
import pylab 
#%% 

def minkowskiDistance(v1, v2, p):
    '''
    Assumes v1 and v2 are equal length arrays of numbers
    Returns Minkowski distance of order p between v1 and v2
    '''
    dist = 0.0
    for i in range(len(v1)):
        dist += abs(v1[i] - v2[i])**p
    return dist**(1/p)

#%% 

class Animal(object):
    def __init__(self, name, features):
        '''
        Assumes name a string; features a list of numbers
        '''
        self.name = name
        self.features = pylab.array(features)
        
    def getName(self):
        return self.name
    
    def getFeatures(self):
        return self.features
    
    def distance(self, other):
        '''
        Assumes other an animal
        Returns the euclidean distance between feature vectors of self and other
        '''
        return minkowskiDistance(self.getFeatures(), other.getFeatures(), 2)
    
#%% 

def compareAnimals(animals, precision):
    '''
    Assumes animals is a list of animals, precision an int >= 0
    Builds a table of Euclidean distance between each animal
    '''
    # Get labels for columns and rows
    columnLabels = []
    for a in animals:
        columnLabels.append(a.getName())
    rowLabels = columnLabels[:]
    tableVals = []
    # get distance between pairs of animals for each row
    for a1 in animals:
        row = []
        # for each column
        for a2 in animals: 
           if a1 == a2:
               row.append('---')
           else: 
               distance = a1.distance(a2)
               row.append(str(round(distance, precision)))
        tableVals.append(row)
   # Produce table
    table = pylab.table(rowLabels = rowLabels,
                       colLabels = columnLabels,
                       cellText = tableVals,
                       cellLoc = 'center',
                       loc = 'center',
                       colWidths = [0.2]*len(animals))
    table.scale(1, 2.5)
    pylab.savefig('distances')
    
#%%

rattlesnake = Animal('rattlesnake', [1,1,1,1,0])
boa = Animal('boa\nconstrictor', [0,1,0,1,0])
dartFrog = Animal('dart frog', [1,0,1,0,1])
animals = [rattlesnake, boa, dartFrog]
alligator = Animal('alligator', [1,1,0,1,1])
animals.append(alligator)
compareAnimals(animals, 3)

