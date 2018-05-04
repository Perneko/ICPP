#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 23:26:54 2018

@author: michael
"""

# 19 | Randomized Trials and Hypothesis Checking

#%% 
import scipy
import pylab
import random
'''
Fisher's approach to significance testing can be summarized as: 
    1. State a null and alternative hypothesis
    2. Understand the statistical assumptions about the sample being evaluated
    3. Compute a relevant test statistic
    4. Derive the probability of getting that test statistic under the null hypothesis
    5. Decide whether that probability is sufficiently small to reject the null hypothesis
'''

#%% Code not provided in the book. Taking it from github

treatment_dist = (119.5, 5.0)
control_dist = (120, 4.0)
random.seed(0)
sample_size = 100
treatment_times, control_times = [], []

for s in range(sample_size):
    treatment_times.append(random.gauss(treatment_dist[0], treatment_dist[1]))
    control_times.append(random.gauss(control_dist[0], control_dist[1]))
control_mean = sum(control_times)/len(control_times)
treatment_mean = sum(treatment_times)/len(treatment_times)

print('Treatment Mean - Control Mean =', treatment_mean - control_mean, 'minutes')
pylab.plot(treatment_times, 'bo', label = 'Treatment Group (Mean =' + str(round(treatment_mean, 2)) + ')')
pylab.plot(control_times, 'kv', label = 'Control Group (Mean =' + str(round(control_mean, 2)) + ')')
pylab.title('Test of PED-X')
pylab.xlabel('Cyclist')
pylab.ylabel('Finishing Time (Minutes)')
pylab.ylim(100, 145)
pylab.legend()


#%% 
tStat = -2.13165598142 # t statistic for PED-X example
tDist = []
numBins = 1000
for i in range(10000000):
    tDist.append(scipy.random.standard_t(198))
    
pylab.hist(tDist, bins = numBins, weights = pylab.array(len(tDist)*[1.0])/len(tDist))
pylab.axvline(tStat, color = 'w')
pylab.axvline(-tStat, color = 'w')
pylab.title('T-Distribution with 198 degrees of Freedom')
pylab.xlabel('T-Statistic')
pylab.ylabel('Probability')

#%% Compute and print the t statistic and p value for our two samples
from scipy import stats
controlMean = sum(control_times)/len(control_times)
treatmentMean = sum(treatment_times)/len(treatment_times)
print('Treatment mean - control mean =', treatmentMean - controlMean, 'minutes')

twoSampleTest = stats.ttest_ind(treatment_times, control_times, equal_var = False)
print('The t-statistic from two-sample test is', twoSampleTest[0])
print('The p-value from two-sample test is', twoSampleTest[1])

oneSampleTest = stats.ttest_1samp(treatment_times, 120)
print('The t-statistic from one sample test is', oneSampleTest[0])
print('The p-value from one sample test is', oneSampleTest[1])

#%% Words With Friends

numGames = 1273
lyndsayWins = 666
outcomes = [1.0]*lyndsayWins + [0.0]*(numGames - lyndsayWins)
print('The p-value from a one sample test is', stats.ttest_1samp(outcomes, 0.5)[1])

#%% Monte Carlo Simulation
import random

numGames = 1273
lyndsayWins = 666
numTrials = 10000
atLeast = 0
for t in range(numTrials):
    LWins = 0
    for g in range(numGames):
        if random.random() < 0.5:
            LWins += 1
    if LWins >= lyndsayWins:
        atLeast += 1
print('Probability of result at least this extreme by accident =', atLeast/numTrials)

#%% 2 tail monte carlo

numGames = 1273
lyndsayWins = 666
numTrials = 10000
atLeast = 0

for t in range(numTrials):
    LWins, JWins = 0, 0
    for g in range(numGames):
        if random.random() < 0.5:
            LWins += 1
        else:
            JWins += 1
    if LWins >= lyndsayWins or JWins >= lyndsayWins:
        atLeast += 1
print('Probability of result at least this extreme by accident =', atLeast/numTrials)

#%% from ch. 17

def getBMData(filename):
    '''
    Read the contents of a given file. Assumes the file in a comma seperated format, with 6 elements in each entry: 
    0. Name(String), 1. Gender (String), 2. Age (int), 3. Division (int), 4. Country (String), 5. Overall Time (float)
    Returns: dict containing a list for each of the 6 variables 
    '''
    data = {}
    f = open(filename)
    line = f.readline()
    data['name'], data['gender'], data['age'] = [], [], []
    data['division'], data['country'], data['time'] = [], [], []
    while line != '':
        split = line.split(",")
        data['name'].append(split[0])
        data['gender'].append(split[1])
        data['age'].append(split[2])
        data['division'].append(int(split[3]))
        data['country'].append(split[4])
        data['time'].append(float(split[5][:-1])) # remove \n
        line = f.readline()
    f.close()
    return data

#%% 

data = getBMData('bm_results2012.txt')
countriesToCompare = ['BEL', 'BRA', 'FRA', 'JPN', 'ITA']

# Build mapping from country to list of female finishing times 

countryTimes = {}
for i in range(len(data['name'])): # for each racer
    if data['country'][i] in countriesToCompare and data['gender'][i] == 'F':
        try:
            countryTimes[data['country'][i]].append(data['time'][i])
        except KeyError: 
            countryTimes[data['country'][i]] = [data['time'][i]]

# Compare finishing times of countries

for c1 in countriesToCompare:
    for c2 in countriesToCompare:
        if c1 < c2: # rather than != so each pair examined once
            pVal = stats.ttest_ind(countryTimes[c1],
                                   countryTimes[c2],
                                   equal_var = False)[1]
            tTestOut = stats.ttest_ind(countryTimes[c1],
                                       countryTimes[c2],
                                       equal_var = False)[0]
            if pVal < 0.05:
                print(c1, 'and', c2, 'have significantly different means, p-value =', round(pVal, 4))
                print('\n', round(tTestOut, 4))
                # Japan is much faster than Italy for our small samples of runners
                
#%% 

numHyps = 20
sampleSize = 30
population = []
for i in range(5000): # Create large population
    population.append(random.gauss(0, 1))
sample1s, sample2s = [], []
for i in range(numHyps): # generate many pairs of small samples
    sample1s.append(random.sample(population, sampleSize))
    sample2s.append(random.sample(population, sampleSize))
# check pairs for statistically significant difference
numSig = 0
for i in range(numHyps):
    if scipy.stats.ttest_ind(sample1s[i], sample2s[i])[1] < 0.05:
        numSig += 1
print('Number of statistically significant (p < 0.05) results =', numSig)
    