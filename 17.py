#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 13:28:26 2018

@author: michael
"""
import pylab
import math
import random
import scipy.integrate
# 17 | Sampling and Confidence Intervals
#%%
def variance(X):
    '''
    Assumes that X is a list of numbers
    Returns the Variance of X
    '''
    mean = sum(X)/len(X)
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return tot/len(X)

def stdDev(X):
    '''
    Assumes X is a list of numbers
    returns the standard Deviation of X
    '''
    return math.sqrt(variance(X))

#%%

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

def makeHist(data, bins, title, xLabel, yLabel):
    pylab.hist(data, bins)
    pylab.title(title)
    pylab.xlabel(xLabel)
    pylab.yLabel(yLabel)
    mean = sum(data)/len(data)
    std = stdDev(data)
    pylab.annotate('Mean = ' + str(round(mean, 2)) + '\nSD = ' + str(round(std, 2)), fontsize = 20, xy = (0.65, 0.75), xycoords = 'axes fraction')
    
times = getBMData('bm_results2012.txt')['time']
makeHist(times, 20, '2012 Boston Marathon', 'Minutes to Complete Race', 'Number of Runners')

#%% 

def sampleTimes(times, numExamples):
    '''
    Assumes times a list of floats representing finishing times of all runners. numExamples is an int
    Generates a random sample of size numExamples, and produces a histogram showing the distribution along with its mean and standard deviation
    '''
    sample = random.sample(times, numExamples)
    makeHist(sample, 10, 'Sample of Size' + str(numExamples), 'Minutes to Complete Race', 'Number of Runners')
    
sampleSize = 40
sampleTimes(times, sampleSize)

#%% Effect of Variance on Estimate of Mean

def gaussian(x, mu, sigma):
    factor1 = (1/(sigma*((2*pylab.pi)**0.5)))
    factor2 = pylab.e**-(((x-mu)**2)/(2*sigma**2))
    return factor1 * factor2

area = round(scipy.integrate.quad(gaussian, -3, 3, (0, 1))[0], 4)
print('Probability of being within 3', 'of true mean of tight dist. =', area)

area = round(scipy.integrate.quad(gaussian, -3, 3, (0, 100))[0], 4)
print('Probability of being within 3', 'of true mean of wide dist. =', area)

#%% 

def testSamples(numTrials, sampleSize):
    tightMeans, wideMeans = [], []
    for t in range(numTrials):
        sampleTight, sampleWide = [], []
        for i in range(sampleSize):
            sampleTight.append(random.gauss(0, 1))
            sampleWide.append(random.gauss(0, 100))
        tightMeans.append(sum(sampleTight)/len(sampleTight))
        wideMeans.append(sum(sampleWide)/len(sampleWide))
    return tightMeans, wideMeans

tightMeans, wideMeans = testSamples(1000, 40)
pylab.plot(wideMeans, 'y*', label = ' SD = 100')
pylab.plot(tightMeans, 'bo', label = ' SD = 1')
pylab.xlabel('Sample Number')
pylab.ylabel('Sample Mean')
pylab.title('Means of Sample Size ' + str(40))
pylab.legend()

pylab.figure()
pylab.hist(wideMeans, bins = 20, label = 'SD = 100')
pylab.title('Distribution of Sample Means')
pylab.xlabel('Sample Mean')
pylab.ylabel('Frequency of Occurence')
pylab.legend()

#%% The Central Limit Theorem

# Given a set of sufficiently large samples drawn from the same popn, the means of the samples (sample means) will be approximately normally distributed
# This normal distribution will have a mean close to the mean of the popn
# The variance of the sample means will be close to the variance of the popn divided by the sample size

def plotMeans(numDicePerTrial, numDiceThrown, numBins, legend, color, style):
    means = []
    numTrials = numDiceThrown//numDicePerTrial
    for i in range(numTrials):
        vals = 0
        for j in range(numDicePerTrial):
            vals += 5*random.random()
        means.append(vals/numDicePerTrial)
    pylab.hist(means, numBins, color = color, label = legend, 
               weights = pylab.array(len(means)*[1])/len(means), hatch = style)
    return sum(means)/len(means), variance(means)

mean, var = plotMeans(1, 100000, 11, '1 die', 'w', '*')
print('Mean of rolling 1 die = ', round(mean, 4), 'Variance = ', round(var, 4))

mean, var = plotMeans(100, 100000, 11, 'Mean of 100 dice', 'w', '//')
print('Mean of rolling 100 dice = ', round(mean, 4), 'Variance = ', round(var, 4))
pylab.title('Rolling Continuous Dice')
pylab.xlabel('Value')
pylab.ylabel('Probability')
pylab.legend()

#%% 

times = getBMData('bm_results2012.txt')['time']
meanOfMeans, stdOfMeans = [], []
sampleSizes = range(50, 2000, 200)
for sampleSize in sampleSizes: 
    sampleMeans = []
    for t in range(20):
        sample = random.sample(times, sampleSize)
        sampleMeans.append(sum(sample)/sampleSize)
    meanOfMeans.append(sum(sampleMeans)/len(sampleMeans))
    stdOfMeans.append(stdDev(sampleMeans))
pylab.errorbar(sampleSizes, meanOfMeans, yerr = 1.96 * pylab.array(stdOfMeans), 
               label = 'Estimated Mean and 95% Confidence Interval')
pylab.xlim(0, max(sampleSizes) + 50)
pylab.axhline(sum(times)/len(times), linestyle = '--', label = "Population Mean")
pylab.title("Estimates of Mean Finishing Time")
pylab.xlabel("Sample Size")
pylab.ylabel("Finishing Time (Minutes)")
pylab.legend(loc = 'best')

#%% Standard Error of the Mean

# SE = (std dev of popn)/(sqrt(size of popn))

times = getBMData('bm_results2012.txt')['time']
popStd = stdDev(times)
sampleSizes = range(2, 200, 2)
diffsMeans = []
for sampleSize in sampleSizes: 
    diffs = []
    for t in range(100):
        diffs.append(abs(popStd - stdDev(random.sample(times, sampleSize))))
    diffsMeans.append(sum(diffs)/len(diffs))
pylab.plot(sampleSizes, diffsMeans)
pylab.xlabel('Sample Size')
pylab.ylabel('Abs(Popn Std. - Sample Std.)')
pylab.title('Sample SD vs. Popn SD')

#%% 
# compute the mean and sd of the sample
# use the sd of that sample to generate the se
# use the estimated se to generate confidence intervals around the sample mean

times = getBMData('bm_results2012.txt')['time']
popMean = sum(times)/len(times)
sampleSize = 200
numBad = 0
for t in range(10000):
    sample = random.sample(times, sampleSize)
    sampleMean = sum(sample)/sampleSize
    se = stdDev(sample)/sampleSize**0.5
    if abs(popMean - sampleMean) > 1.96*se: 
        numBad += 1
print('Fraction outside 95% confidence interval = ', numBad/10000)