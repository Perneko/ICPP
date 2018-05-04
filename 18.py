#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 19:11:28 2018

@author: michael
"""

# Ch 18 | Understanding Experimental Data
import pylab
#%% 

def getData(fileName):
    dataFile = open(fileName, 'r')
    distances = []
    masses = []
    dataFile.readline() # ignore header
    for line in dataFile:
        d, m = line.split(" ")
        distances.append(float(d))
        masses.append(float(m))
    dataFile.close()
    return (masses, distances)

#%% 

def plotData(inputFile):
    masses, distances = getData(inputFile)
    distances = pylab.array(distances)
    masses = pylab.array(masses)
    forces = 9.81 * masses
    pylab.plot(forces, distances, 'bo', label = "Measured Displacements")
    pylab.title("Measured Displacement of Spring")
    pylab.xlabel("|Force| (Newtons)")
    pylab.ylabel("Distance (Meters)")
    
plotData('springData.txt')

#%% 

# polyfit finds the best least squares fit for our data with a polynomial that minimizes the residuals 
# pylab.polyfit(observedXVals, observedYVals, n)

def fitData(inputFile):
    masses, distances = getData(inputFile)
    distances = pylab.array(distances)
    masses = pylab.array(masses)
    forces = pylab.array(masses) * 9.81
    pylab.plot(forces, distances, 'ko', label = "Measurement Displacements")
    pylab.title("Measured Displacement of Spring")
    pylab.xlabel("|Force| (Newtons)")
    pylab.ylabel("Distance (Meters)")
    # find linear fit
    a, b = pylab.polyfit(forces, distances, 1)
    predictedDistances = a * pylab.array(forces) + b
    k = 1.0 / a # a is dDist/dForce, k is dForce/dDist or a inverse
    pylab.plot(forces, predictedDistances, label = "Displacements Predicted by \nLinear Fit, k = " + str(round(k, 5)))
    pylab.legend(loc = 'best')
    
#%% 
fitData('springData.txt')

#%% Try a cubic fit

# finger exercise

def fitData(inputFile):
    masses, distances = getData(inputFile)
    distances = pylab.array(distances)
    masses = pylab.array(masses)
    forces = pylab.array(masses) * 9.81
    pylab.plot(forces, distances, 'ko', label = "Measurement Displacements")
    pylab.title("Measured Displacement of Spring")
    pylab.xlabel("|Force| (Newtons)")
    pylab.ylabel("Distance (Meters)")
    # find linear fit
    a, b = pylab.polyfit(forces, distances, 1)
    predictedDistances = a * pylab.array(forces) + b
    k = 1.0 / a # a is dDist/dForce, k is dForce/dDist or a inverse
    pylab.plot(forces, predictedDistances, label = "Displacements Predicted by \nLinear Fit, k = " + str(round(k, 5)))
    pylab.legend(loc = 'best')
    # find cubic fit
    fit = pylab.polyfit(forces, distances, 3)
    predictedDistances = pylab.polyval(fit, forces)
    forces_extend = pylab.append(forces, pylab.array([15]))
    predicted_distances_extend = pylab.polyval(fit, forces_extend)
    pylab.plot(forces_extend, predicted_distances_extend, 'k:', label = 'cubic fit')
    pylab.xlim(0, 16)
    
#%% 
fitData('springData.txt')

#%% 

def fitData(inputFile):
    masses, distances = getData(inputFile)
    distances = pylab.array(distances[:-6])
    masses = pylab.array(masses[:-6])
    forces = pylab.array(masses) * 9.81
    pylab.plot(forces, distances, 'ko', label = "Measurement Displacements")
    pylab.title("Measured Displacement of Spring")
    pylab.xlabel("|Force| (Newtons)")
    pylab.ylabel("Distance (Meters)")
    # find linear fit
    a, b = pylab.polyfit(forces, distances, 1)
    predictedDistances = a * pylab.array(forces) + b
    k = 1.0 / a # a is dDist/dForce, k is dForce/dDist or a inverse
    pylab.plot(forces, predictedDistances, label = "Displacements Predicted by \nLinear Fit, k = " + str(round(k, 5)))
    pylab.legend(loc = 'best')
    # find cubic fit
    fit = pylab.polyfit(forces, distances, 3)
    predictedDistances = pylab.polyval(fit, forces)
    pylab.plot(forces, predictedDistances, 'k:', label = 'cubic fit')
    
#%% 
fitData('springData.txt')

#%% 
def getTrajectoryData(fileName):
    dataFile = open(fileName, 'r')
    distances = []
    heights1, heights2, heights3, heights4 = [], [], [], []
    dataFile.readline()
    for line in dataFile:
        d, h1, h2, h3, h4 = line.split()
        distances.append(float(d))
        heights1.append(float(h1))
        heights2.append(float(h2))
        heights3.append(float(h3))
        heights4.append(float(h4))
    dataFile.close()
    return (distances, [heights1, heights2, heights3, heights4])

def processTrajectories(fileName):
    distances, heights = getTrajectoryData(fileName)
    numTrials = len(heights)
    distances = pylab.array(distances)
    # Get array containing mean height at each distance
    totHeights = pylab.array([0]*len(distances))
    for h in heights:
        totHeights = totHeights + pylab.array(h)
    meanHeights = totHeights/len(heights)
    
    pylab.title("Trajectory of Projectile (Mean of " + str(numTrials) + 'Trials)')
    pylab.xlabel("Inches from Launch Point")
    pylab.ylabel("Inches Above Launch Point")
    pylab.plot(distances, meanHeights, 'ko')
    
    fit = pylab.polyfit(distances, meanHeights, 1)
    altitudes = pylab.polyval(fit, distances)
    pylab.plot(distances, altitudes, 'b', label = "Linear Fit")
    print('RSquare of Linear Fit = ', rSquared(meanHeights, altitudes))
    
    fit = pylab.polyfit(distances, meanHeights, 2)
    altitudes = pylab.polyval(fit, distances)
    pylab.plot(distances, altitudes, 'k:', label = "Quadratic Fit")
    print('Rsquare of Quadratic Fit = ', rSquared(meanHeights, altitudes))
    pylab.legend()
    getHorizontalSpeed(fit, distances[-1], distances[0])
    
#%%
processTrajectories('launcherData.txt')

#%% Coefficient of Determination

def rSquared(measured, predicted):
    '''
    Assumes measured a one dimensional array of measured values
    predicted a one dimensional array of predicted values 
    Returns coefficient of determination
    '''
    estimateError = ((measured - predicted)**2).sum()
    meanOfMeasured = measured.sum()/len(measured)
    variability = ((measured - meanOfMeasured)**2).sum()
    return 1 - estimateError/variability
#%% Using A Computational Model

def getHorizontalSpeed(quadFit, minX, maxX):
    '''
    Assumes quadFit has coefficients of a quadratic polynomial
    minX and maxX are distances in inches
    Returns horizontal speed in feet per second
    '''
    inchesPerFoot = 12
    xMid = (maxX - minX)/2
    a,b,c = quadFit[0], quadFit[1], quadFit[2]
    yPeak = a*xMid**2 + b*xMid + c
    g = 32.16 * inchesPerFoot # accel of gravity in inches per foot * foot
    t = (2*yPeak/g)**0.5 # time in seconds from peak to target
    print('Horizontal Speed =', int(xMid/(t * inchesPerFoot)), 'feet/sec')
    

# Common Pattern:
    # 1. Perform an experiment to get data about the behaviour of a physical system
    # 2. Used computation to find and evaluate the quality of a model of the behaviour of a system
    # 3. Use some theory and analysis to design a simple computation to derive an interesting consequence of the model
    
#%% Fitting Exponentially Distributed Data

vals = []
for i in range(10):
    vals.append(3**i)
pylab.plot(vals, 'ko', label = 'Actual Points')
xVals = pylab.arange(10)
fit = pylab.polyfit(xVals, vals, 5)
yVals = pylab.polyval(fit, xVals)
pylab.plot(yVals, 'kx', label = 'Predicted Points', markeredgewidth = 2, markersize = 25)
pylab.title('Fitting y = 3**x')
pylab.legend(loc = 'upper left')
# predict for 3**20
print('Model predicts that 3**20 is roughly', pylab.polyval(fit, [3**20])[0])
print('Actual value of 3**20 is', 3**20)

#%% We can use transforms to make exponential values into linear values

xVals, yVals = [], []
for i in range(10):
    xVals.append(i)
    yVals.append(3**i)
pylab.plot(xVals, yVals, 'k')
pylab.semilogy()

#%% 
import math

def createData(f, xVals):
    '''
    Assumes that f is a function of one argument
    xVals is an array of suitable arguments for f
    Returns array containing results of applying f to the elements of xVals
    '''
    yVals = []
    for i in xVals:
        yVals.append(f(xVals[i]))
    return pylab.array(yVals)

def fitExpData(xVals, yVals):
    '''
    Assumes xCals and yVals arrays of nunbers such that 
    yVals[i] == f(xVals[i]), where f is an exponential function
    returns a, b, base, such that log(f(x), base) == ax + b
    '''
    logVals = []
    for y in vals: 
        logVals.append(math.log(y, 2.0)) # log base 2
    fit = pylab.polyfit(xVals, logVals, 1)
    return fit, 2.0

#%%
xVals = range(10)
f = lambda x: 3**x
yVals = createData(f, xVals)
pylab.plot(xVals, yVals, 'ko', label = 'Actual Values')
fit, base = fitExpData(xVals, yVals)
predictedYVals = []
for x in xVals: 
    predictedYVals.append(base**pylab.polyval(fit, x))
pylab.plot(xVals, predictedYVals, label = 'Predicted Values')
pylab.title('Fitting an Exponential Function')
pylab.legend(loc = 'upper left')
# look at value for x not in original data
print('f(20) =', f(20))
print('Predicted value =', int(base**(pylab.polyval(fit, [20]))))
