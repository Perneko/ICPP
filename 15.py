#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 15:09:16 2018

@author: michael
"""

import random
import pylab
import scipy.integrate
import math

#%% 15 | Stochastic Programs, Probability, and Distributions 

def rollDie():
    '''
    Returns a random int between 1 and 6
    '''
    return random.choice([1, 2, 3, 4, 5, 6])

def rollN(n):
    result = ''
    for i in range(n):
        result += str(rollDie())
    print(result) 
    
rollN(5)

#%%

def flip(numFlips):
    '''
    Assumes numFlips is a positive int
    '''
    heads = 0
    for i in range(numFlips):
        if random.choice(['H', 'T']) == 'H':
            heads = heads + 1
    return heads / numFlips 

def flipSim(numFlipsPerTrial, numTrials):
    '''
    Assumes numFlipsPerTrial and numTrials are positive ints
    '''
    fracHeads = []
    for i in range(numTrials):
        fracHeads.append(flip(numFlipsPerTrial))
    mean = sum(fracHeads)/len(fracHeads)
    return mean 

#%% 
flipSim(10, 1)

#%%

def regressToMean(numFlips, numTrials):
    # Get fraction of heads for each trial of numFlips
    fracHeads = []
    for t in range(numTrials):
        fracHeads.append(flip(numFlips))
    # Find trials with extreme results and for each the next trial
    extremes, nextTrials = [], []
    for i in range(len(fracHeads) - 1):
        if fracHeads[i] < 0.33 or fracHeads[i] > 0.66:
            extremes.append(fracHeads[i])
            nextTrials.append(fracHeads[i+1])
    # Plot results 
    pylab.plot(range(len(extremes)), extremes, 'ko', label = 'Extreme')
    pylab.plot(range(len(nextTrials)), nextTrials, 'k^', label = 'Next Trial')
    pylab.axhline(0.5)
    pylab.ylim(0, 1)
    pylab.xlim(-1, len(extremes) + 1)
    pylab.xlabel('Extreme Example and Next Trial')
    pylab.ylabel('Fraction Heads')
    pylab.title('Regression to the Mean')
    pylab.legend(loc = 'best')
    
regressToMean(15, 100)

# Finger Exercise : No, assuming she would move in the opposite direction (50 as opposed to 45) would be an example of the gambler's fallacy. 
# A better prediction would be assuming that she would be closed to 45, e.g 45 +- 3

#%% 

def flipPlot(minExp, maxExp):
    '''
    Assumes minExp and maxExp positive integers; minExp < maxExp
    Plots results of 2**minExp to 2**maxExp coin flips
    '''
    ratios, diffs, xAxis = [], [], []
    
    for exp in range(minExp, maxExp + 1):
        xAxis.append(2**exp)
        
    for numFlips in xAxis:
        numHeads = 0
        for n in range(numFlips):
            if random.choice(('H', 'T')) == 'H':
                numHeads = numHeads + 1
            
        numTails = numFlips - numHeads
        try: 
            ratios.append(numHeads/numTails)
            diffs.append(abs(numHeads - numTails))
            
        except ZeroDivisionError:
            continue
            
    pylab.title('Difference Between Heads and Tails')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('Abs(#Heads - #Tails)')
    pylab.xscale('log')
    pylab.plot(xAxis, diffs, 'ko')
    pylab.figure()
    
    pylab.title('Heads/Tails Ratios')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('#Heads/#Tails')
    pylab.xscale('log')
    pylab.plot(xAxis, ratios, 'ko')
    
    
random.seed(0)
flipPlot(4, 20)

#%%

def variance(X):
    '''
    Assumes that X is a list of numbers
    Returns the variance of X
    '''
    mean = sum(X)/len(X)
    tot = 0.0
    for x in X:
        tot += (x-mean)**2
    return tot / len(X)

def stdDev(X):
    '''
    Assumes that X is a list of numbers 
    returns the standard deviation of X
    '''
    return variance(X)**0.5

#%% 

def makePlot(xVals, yVals, title, xLabel, yLabel, style, logx = False, logy = False):
    pylab.figure()
    pylab.title(title)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    pylab.plot(xVals, yVals, style)
    if logx:
        pylab.semilogx()
    if logy:
        pylab.semilogy()

def runTrial(numFlips):
    numHeads = 0
    for n in range(numFlips):
        if random.choice(['H', 'T']) == 'H':
            numHeads += 1
    numTails = numFlips - numHeads
    return (numHeads, numTails)

def flipPlot1(minExp, maxExp, numTrials):
    '''
    Assumes minExp, maxExp, numTrials are positive ints, minExp < maxExp
    Plots summaries of results of numTrials trials of 2**minExp to 2**maxExp coin flips
    '''
    ratiosMeans, diffsMeans, ratiosSDs, diffsSDs = [], [], [], []
    xAxis = []
    for exp in range(minExp, maxExp + 1):
        xAxis.append(2**exp)
    for numFlips in xAxis:
        ratios, diffs = [], []
        for t in range(numTrials):
            numHeads, numTails = runTrial(numFlips)
            ratios.append(numHeads/numTails)
            diffs.append(abs(numHeads-numTails))
        ratiosMeans.append(sum(ratios)/numTrials)
        diffsMeans.append(sum(diffs)/numTrials)
        ratiosSDs.append(stdDev(ratios))
        diffsSDs.append(stdDev(diffs))
    numTrialsString = ' (' + str(numTrials) + ' Trials)'
    title = 'Mean Heads/Tails Ratios' + numTrialsString
    makePlot(xAxis, ratiosMeans, title, 'Number of Flips', 'Mean Heads/Tails', 'ko', logx = True)
    title = 'SD Heads/Tails Ratios' + numTrialsString
    makePlot(xAxis, ratiosSDs, title, 'Number of Flips', 'Standard Deviation', 'ko', logx = True, logy = True)
    title = 'Mean abs(#Heads - #Tails)' + numTrialsString
    makePlot(xAxis, diffsMeans, title, 'Number of Flips', 'Mean abs(#Heads - #Tails)', 'ko', logx = True, logy = True)
    title = 'SD abs(#Heads - #Tails)' + numTrialsString
    makePlot(xAxis, diffsSDs, title, 'Number of Flips', 'Standard Deviation', 'ko', logx = True, logy = True)
    
#%% 
flipPlot1(4, 20, 20)

#%% 

def CoefVar(X):
    mean = sum(X)/len(X)
    try: 
        return stdDev(X)/mean
    except ZeroDivisionError:
        return float('nan')
    
#%% 

def flipPlot2(minExp, maxExp, numTrials):
    '''
    Assumes minExp, maxExp, numTrials are ints >0; minExp < maxExp
    Plots summaries of results of numTrials trials of 2**minExp to 2**maxExp coin flips
    '''
    ratiosMeans, diffsMeans, ratiosSDs, diffsSDs = [], [], [], []
    ratiosCVs, diffsCVs, xAxis = [], [], []
    for exp in range(minExp, maxExp + 1):
        xAxis.append(2**exp)
    for numFlips in xAxis: 
        ratios, diffs = [], []
        for t in range(numTrials):
            numHeads, numTails = runTrial(numFlips)
            ratios.append(numHeads/float(numTrials))
            diffs.append(abs(numHeads - numTails))
        ratiosMeans.append(abs(sum(ratios)/numTrials))
        diffsMeans.append(sum(diffs)/numTrials)
        ratiosSDs.append(stdDev(ratios))
        diffsSDs.append(stdDev(diffs))
        ratiosCVs.append(CoefVar(ratios))
        diffsCVs.append(CoefVar(diffs))
    numTrialsString = ' (' + str(numTrials) + ' Trials)'
    
    title = 'Mean Heads/Tails Ratios' + numTrialsString
    makePlot(xAxis, ratiosMeans, title, 'Number of Flips', 'Mean Heads/Tails', 'ko', logx = True)
    title = 'SD Heads/Tails Ratios' + numTrialsString
    makePlot(xAxis, ratiosSDs, title, 'Number of Flips', 'Standard Deviation', 'ko', logx = True, logy = True)
    title = 'Mean abs(#Heads - #Tails)' + numTrialsString
    makePlot(xAxis, diffsMeans, title, 'Number of Flips', 'Mean abs(#Heads - #Tails)', 'ko', logx = True, logy = True)
    title = 'SD abs(#Heads - #Tails)' + numTrialsString
    makePlot(xAxis, diffsSDs, title, 'Number of Flips', 'Standard Deviation', 'ko', logx = True, logy = True)
    title = 'Coef. of Var. abs(#Heads - #Tails)' + numTrialsString
    makePlot(xAxis, diffsCVs, title, 'Number of Flips', 'Coef. of Var.', 'ko', logx = True)
    title = 'Coef. of Var. Heads/Tails Ratio' + numTrialsString
    makePlot(xAxis, ratiosCVs, title, 'Number of Flips', 'Coef. of Var.', 'ko', logx = True, logy = True)

#%% 

flipPlot2(4, 20, 20)

#%% 15.4 | Distributions

vals = []
for i in range(1000):
    num1 = random.choice(range(0, 101))
    num2 = random.choice(range(0, 101))
    vals.append(num1 + num2)
pylab.hist(vals, bins = 10)
pylab.xlabel("Number of Occurences")

#%% 

def flipSim(numFlipsPerTrial, numTrials):
    fracHeads = []
    for i in range(numTrials):
        fracHeads.append(flip(numFlipsPerTrial))
    mean = sum(fracHeads)/len(fracHeads)
    sd = stdDev(fracHeads)
    return (fracHeads, mean, sd)

def labelPlot(numFlips, numTrials, mean, sd):
    pylab.title(str(numTrials) + ' trials of ' + str(numFlips) + ' flips each ')
    pylab.xlabel('Fraction of Heads')
    pylab.ylabel('Number of Trials')
    pylab.annotate('Mean = ' + str(round(mean, 4)) + '\nSD = ' + str(round(sd, 4)), size = 'x-large', xycoords = 'axes fraction', xy = (0.67, 0.5))
    
def makePlots(numFlips1, numFlips2, numTrials):
    val1, mean1, sd1 = flipSim(numFlips1, numFlips2)
    pylab.hist(val1, bins = 20)
    xmin, xmax = pylab.xlim()
    labelPlot(numFlips1, numTrials, mean1, sd1)
    pylab.figure()
    val2, mean2, sd2 = flipSim(numFlips2, numTrials)
    pylab.hist(val2, bins = 20)
    pylab.xlim(xmin, xmax)
    labelPlot(numFlips2, numTrials, mean2, sd2)
    
makePlots(100, 1000, 100000)

#%% 

# scipy.integrate.quad finds an approximatioon to the value of integrating a function between two points

def gaussian(x, mu, sigma):
    factor1 = (1.0 / (sigma*((2*pylab.pi)**0.5)))
    factor2 = pylab.e**-(((x-mu)**2)/(2*sigma**2))
    return factor1 * factor2

def checkEmpirical(numTrials):
    for t in range(numTrials):
        mu = random.randint(-10, 10)
        sigma = random.randint(1, 10)
        print(' For mu =', mu, ' and sigma =', sigma)
        for numStd in (1,2,3):
            area = scipy.integrate.quad(gaussian, mu-numStd*sigma, mu+numStd*sigma, (mu, sigma))[0]
            print(' Fraction within', numStd, 'std =', round(area, 4))
            
checkEmpirical(3)

#%% 

def showErrorBars(minExp, maxExp, numTrials):
    '''
    Assumes minExp, maxExp, numTrials ints > 0, minExp < maxExp
    Plots mean fraction of heads with error bars
    '''
    means, sds, xVals = [], [], []
    for exp in range(minExp, maxExp+1):
        xVals.append(2**exp)
        fracHeads, mean, sd = flipSim(2**exp, numTrials)
        means.append(mean)
        sds.append(sd)
    pylab.errorbar(xVals, means, yerr = 1.96*pylab.array(sds))
    pylab.semilogx()
    pylab.title('Mean Fraction of Heads (' + str(numTrials) + ' trials)')
    pylab.xlabel('Number of flips per trial')
    pylab.ylabel('Fraction of heads & 95% confidence')
    
showErrorBars(3, 10, 100)

#%% 

def factorial(n):
    if (n == 1) or (n == 0):
        return 1
    else:
        return n * factorial(n-1) 
#%% finger exercise

def bin(n, k, p):
    '''
    Assumes n,k are integers, n > k, p a probability (float)
    '''
    nchoosek = math.factorial(n) / (math.factorial(n-k) * math.factorial(k))
    return nchoosek * p**(k) * (1-p)**(n-k)

def rollSimPlot(min, max, numTrials):
    xVals, binVals = [], []
    for i in range(min, max+1):
        xVals.append(i)
        binVals.append(bin(i, 2, (1/6)))
    pylab.plot(xVals, binVals)

rollSimPlot(2, 100, 10)
            
#%% 

def clear(n, p, steps):
    '''
    Assumes n, steps ints > 0, p float 
    n: initial number of molecules, p: the probability of a molecule being cleared, steps: length of simulation
    '''
    numRemaining = [n]
    for t in range(steps):
        numRemaining.append(n*((1-p)**t))
    pylab.plot(numRemaining)
    pylab.xlabel('Time')
    pylab.ylabel('Molecules Remaining')
    pylab.title('Clearance of Drug')
    pylab.semilogy()
    
clear(1000, 0.01, 1000)

#%% 

def successfulStarts(successProb, numTrials):
    '''
    Assumes successProb is a float representing the probability of a single attempt being successful
    numTrials is an int > 0
    Returns a list of the number of attempts needed before a success for each trial. 
    '''
    triesBeforeSuccess = []
    for t in range(numTrials):
        consecFailures = 0
        while random.random() > successProb:
            consecFailures += 1
        triesBeforeSuccess.append(consecFailures)
    return triesBeforeSuccess

probOfSuccess = 0.5
numTrials = 5000
distribution = successfulStarts(probOfSuccess, numTrials)
pylab.hist(distribution, bins = 14)
pylab.xlabel('Tries Before Success')
pylab.ylabel('Number of Occurences Out of ' + str(numTrials) + ' Trials')
pylab.title('Probability of Starting Each Try = ' + str(probOfSuccess))
    
#%% 

def collisionProb(n, k):
    prob = 1.0
    for i in range(1, k):
        prob *= ((n-i)/n)
    return 1 - prob

collisionProb(200, 50)

#%% 
def simInsertions(numIndices, numInsertions):
    '''
    Assumes numIndices and numInsertions are positive ints
    Returns 1 if there is a collision, 0 otherwise
    '''
    choices = range(numIndices) # list of possible indices
    used = []
    for i in range(numInsertions):
        hashVal = random.choice(choices)
        if hashVal in used: # collision
            return 1
        else: 
            used.append(hashVal)
    return 0

def findProb(numIndices, numInsertions, numTrials):
    collisions = 0
    for t in range(numTrials):
        collisions += simInsertions(numIndices, numInsertions)
    return collisions/numTrials

#%% 
print('Actual Prob of a Collision = ', collisionProb(1000,50))
print('Est Prob of a Collision = ', findProb(1000, 50, 10000))
print('Actual Prob of a Collision = ', collisionProb(1000,200))
print('Est Prob of a Collision = ', findProb(1000, 200, 10000))

#%% 

def playSeries(numGames, teamProb):
    numWon = 0
    for game in range(numGames):
        if random.random() <= teamProb:
            numWon += 1
    return (numWon > numGames//2)

def fractionWon(teamProb, numSeries, seriesLen):
    won = 0
    for series in range(numSeries):
        if playSeries(seriesLen, teamProb):
            won += 1
    return won/float(numSeries)

def simSeries(numSeries):
    prob = 0.5
    fracsWon, probs = [], []
    while prob <= 1.0:
        fracsWon.append(fractionWon(prob, numSeries, 7))
        probs.append(prob)
        prob += 0.01
    pylab.axhline(0.95)
    pylab.plot(probs, fracsWon, 'k', linewidth = 5)
    pylab.xlabel('Probability of Winning a Game')
    pylab.ylabel('Probability of Winning a Series')
    pylab.title(str(numSeries) + ' Seven Game Series')
    
simSeries(400)