#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 11:09:44 2018

@author: michael
"""

# 21 | Lies, Damned Lies, and Statistics

#%% 
import pylab
import random
#%%
def plotHousing(impression):
    '''
    Assumes impression a str, must be one of 'flat', 'volatile' and 'fair'
    Produce bar chart of housing prices over time
    '''
    f = open('midWestHousingPrices.txt', 'r')
    # each line of file contains year, quarter, price for midwest region of the US
    labels, prices = [], []
    for line in f:
        year, quarter, price = line.split()
        label = year[2:4] + '\n Q' + quarter[1]
        labels.append(label)
        prices.append(int(price)/1000)
    quarters = pylab.arange(len(labels)) # x coord of bars
    width = 0.8 # width of bars
    pylab.bar(quarters, prices, width)
    pylab.xticks(quarters + width/2, labels)
    pylab.title('Housing Prices in the U.S. Midwest')
    pylab.xlabel('Quarter')
    pylab.ylabel('Average Price ($1000\'s)')
    if impression == 'flat':
        pylab.ylim(0, 500)
    elif impression == 'volatile':
        pylab.ylim(180, 220)
    elif impression == 'fair':
        pylab.ylim(150, 250)
    else: 
        raise ValueError

#%% 

plotHousing('flat')
pylab.figure()
plotHousing('volatile')
pylab.figure()
plotHousing('fair')

#%% 

def juneProb(numTrials):
    june48 = 0
    for trial in range(numTrials):
        june = 0
        for i in range(446):
            if random.randint(1, 12) == 6:
                june += 1
        if june >= 48:
            june48 += 1
    jProb = round(june48 / numTrials, 4)
    print('Probability of at least 48 births in June =', jProb)
    
juneProb(10000)

#%% 
def anyProb(numTrials):
    anyMonth48 = 0
    for trial in range(numTrials):
        months = [0]*12
        for i in range(446):
            months[random.randint(0, 11)] += 1
        if max(months) >= 48:
            anyMonth48 += 1
    aProb = round(anyMonth48/numTrials, 4)
    print('Probability of at least 48 births in some month =', aProb)

anyProb(10000)