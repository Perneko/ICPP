#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 20:50:20 2018

@author: michael
"""
import random
import math
# 16 | Monte Carlo Simulations 
#%% 
def rollDie():
    return random.choice([1,2,3,4,5,6])

def checkPascal(numTrials):
    '''
    Assumes numTrials an int > 0
    Prints an estimate of the probability of winning
    '''
    numWins= 0
    for i in range(numTrials):
        for j in range(24):
            d1 = rollDie()
            d2 = rollDie()
            if d1 == 6 and d2 == 6:
                numWins += 1
                break
    print('Probability of Winning = ', numWins/numTrials)
    
    
#%% 
checkPascal(10000)

#%% 
class CrapsGame(object):
    def __init__(self):
        self.passWins, self.passLosses = 0, 0
        self.dpWins, self.dpLosses, self.dpPushes = 0,0,0
        
    def playHand(self):
        # Make playHand more efficient
        pointsDict = {4: 1/3, 5:2/5, 6: 5/11, 8:5/11, 9:2/5, 10:1/3}
        throw = rollDie() + rollDie()
        if throw == 7 or throw == 11:
            self.passWins += 1
            self.dpLosses += 1
        elif throw == 2 or throw == 3 or throw == 12:
            self.passLosses += 1
            if throw == 12:
                self.dpPushes += 1
            else: 
                self.dpWins += 1
        else:
            if random.random() <= pointsDict[throw]: # point before 7
                self.passWins += 1
                self.dpLosses += 1
            else: 
                self.passLosses += 1
                self.dpWins += 1
        '''
        throw = rollDie() + rollDie()
        if throw == 7 or throw == 11:
            self.passWins += 1
            self.dpLosses += 1
        elif throw == 2 or throw == 2 or throw == 12: 
            self.passLosses += 1
            if throw == 12:
                self.dpPushes += 1
            else: 
                self.dpWins += 1
        else:
            point = throw
            while True:
                throw = rollDie() + rollDie() 
                if throw == point:
                    self.passWins += 1
                    self.dpLosses += 1
                    break
                elif throw == 7:
                    self.passLosses += 1
                    self.dpWins += 1
                    break '''
                
    def passResults(self):
        return (self.passWins, self.passLosses)
    
    def dpResults(self):
        return (self.dpWins, self.dpLosses, self.dpPushes)
        
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

def crapsSim(handsPerGame, numGames):
    '''
    Assumes handPerGame and numGames are ints > 0
    Play numGames games of handsPerGame hands; Print results
    '''
    games = []
    
    # Play numGames games
    
    for t in range(numGames):
        c = CrapsGame()
        for i in range(handsPerGame):
            c.playHand()
        games.append(c)
        
        
    # Produce statistics for each game
    pROIPerGame, dpROIPerGame = [], []
    for g in games:
        wins, losses = g.passResults()
        pROIPerGame.append((wins - losses)/float(handsPerGame))
        wins, losses, pushes = g.dpResults()
        dpROIPerGame.append((wins - losses)/float(handsPerGame))
        
    # Produce and Print Summary Statistics
    # pass
    meanROI = str(round((100 * sum(pROIPerGame)/numGames), 4)) + '%'
    sigma = str(round(100 * stdDev(pROIPerGame), 4)) + '%'
    print('Pass:', 'Mean ROI =', meanROI, 'Standard Deviation =', sigma)
    # don't pass
    meanROI = str(round((100 * sum(dpROIPerGame)/numGames), 4)) + '%'
    sigma = str(round(100 * stdDev(dpROIPerGame), 4)) + '%'
    print('Don\'t Pass:', 'Mean ROI =', meanROI, 'Standard Deviation =', sigma)
    
#%% 
crapsSim(20, 10)
#%% 
crapsSim(1000000, 10)

#%% Finding pi

def throwNeedles(numNeedles):
    inCircle = 0
    for needles in range(1, numNeedles + 1):
        x = random.random()
        y = random.random()
        if math.sqrt(x*x + y*y) <= 1:
            inCircle += 1
    # Counting needles in one quadrant only, so multiply by 4
    return 4 * (inCircle/numNeedles)

def getEst(numNeedles, numTrials):
    estimates = []
    for t in range(numTrials):
        piGuess = throwNeedles(numNeedles)
        estimates.append(piGuess)
    sDev = stdDev(estimates)
    curEst = sum(estimates)/len(estimates)
    print('Est. =', str(round(curEst, 5)) + ', ', 'Std. Dev. =', str(round(sDev, 5)) + ', ', 'Needles =', numNeedles)
    return (curEst, sDev)

def estPi(precision, numTrials):
    numNeedles = 1000
    sDev = precision
    while sDev > precision/1.96:
        curEst, sDev = getEst(numNeedles, numTrials)
        numNeedles *= 2
    return curEst

#%% 
estPi(0.01, 10000)

