#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 12:37:17 2018

@author: michael
"""

# 24 | Classification Methods 
import random
import pylab
import sklearn
import math

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

def accuracy(truePos, falsePos, trueNeg, falseNeg):
    numerator = truePos + trueNeg
    denominator = truePos + trueNeg + falsePos + falseNeg
    return numerator/denominator

def sensitivity(truePos, falseNeg):
    try:
        return truePos/(truePos + falseNeg)
    except ZeroDivisionError:
        return float('nan')
    
def specificity(trueNeg, falsePos):
    try: 
        return trueNeg / (trueNeg + falsePos)
    except ZeroDivisionError:
        return float('nan')
    
def posPredVal(truePos, falsePos):
    try:
        return truePos/(truePos + falsePos)
    except ZeroDivisionError:
        return float('nan')
    
def negPredVal(trueNeg, falseNeg):
    try: 
        return trueNeg / (trueNeg + falseNeg)
    except ZeroDivisionError:
        return float('nan')
    
def getStats(truePos, falsePos, trueNeg, falseNeg, toPrint = True):
    accur = accuracy(truePos, falsePos, trueNeg, falseNeg)
    sens = sensitivity(truePos, falseNeg)
    spec = specificity(trueNeg, falsePos)
    ppv = posPredVal(truePos, falsePos)
    npv = negPredVal(trueNeg, falseNeg)
    if toPrint:
        print('Accuracy: ', round(accur, 3))
        print('Sensitivity: ', round(sens, 3))
        print('Specificity: ', round(spec, 3))
        print('Positive Predictive Value: ', round(ppv, 3))
        print('Negative Predictive Value: ', round(npv, 3))
    return (accur, sens, spec, ppv, npv)

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

#%%

class Runner(object):
    
    def __init__(self, gender, age, time):
        self.featureVec = (age, time)
        self.label = gender
        
    def featureDist(self, other):
        dist = 0.0
        for i in range(len(self.featureVec)):
            dist = dist + abs(float(self.featureVec[i]) - float(other.featureVec[i]))**2
        return dist**0.5
    
    def getTime(self):
        return self.featureVec[1]
    
    def getAge(self):
        return self.featureVec[0]
    
    def getLabel(self):
        return self.label
    
    def getFeatures(self):
        return self.featureVec
    
    def __str__(self):
        return str(self.getAge()) + ', ' + str(self.getTime()) + ', ' + self.label
    
#%%
    
def buildMarathonExamples(fileName):
    data = getBMData(fileName)
    examples = []
    for i in range(len(data['age'])):
        a = Runner(data['gender'][i], data['age'][i], data['time'][i])
        examples.append(a)
    return examples

def divide80_20(examples):
    sampleIndices = random.sample(range(len(examples)), len(examples)//5)
    trainingSet, testSet = [], []
    
    for i in range(len(examples)):
        if i in sampleIndices:
            testSet.append(examples[i])
        else: 
            trainingSet.append(examples[i])
    return trainingSet, testSet 

#%% 

def findKNearest(example, exampleSet, k):
    kNearest, distances = [], []
    # build lists containing first k examples and their distances
    for i in range(k):
        kNearest.append(exampleSet[i])
        distances.append(example.featureDist(exampleSet[i]))
    maxDist = max(distances)
    # look at examples not yet considered
    for e in exampleSet[k:]:
        dist = example.featureDist(e)
        if dist < maxDist: 
            # replace farther neighbor with this one
            maxIndex = distances.index(maxDist)
            kNearest[maxIndex] = e
            distances[maxIndex] = dist
            maxDist = max(distances)
    return kNearest, distances

def kNearestClassify(training, testSet, label, k):
    '''
    Assumes training and testSet lists of examples, k an int
    Uses a k-nearest neighbor classifier to predict whether each example in the testSet has the given label
    Returns number of true positives, false positives, true negatives and false negatives
    '''
    truePos, trueNeg, falsePos, falseNeg = 0,0,0,0
    for e in testSet: 
        nearest, distances = findKNearest(e, training, k)
        # conduct Vote
        numMatch = 0
        for i in range(len(nearest)):
            if nearest[i].getLabel() == label:
                numMatch += 1
        if numMatch > k//2: # Guess label
            if e.getLabel() == label: 
                truePos += 1
            else: 
                falsePos += 1
        else: # guess not label 
            if e.getLabel() != label: 
                trueNeg += 1
            else: 
                falseNeg += 1
    return truePos, falsePos, trueNeg, falseNeg

#%% takes a long time

examples = buildMarathonExamples('bm_results2012.txt')
training, testSet = divide80_20(examples)
truePos, falsePos, trueNeg, falseNeg = kNearestClassify(training, testSet, 'M', 9)
getStats(truePos, falsePos, trueNeg, falseNeg)

#%% reduced time

reducedTraining = random.sample(training, len(training)//10)
truePos, falsePos, trueNeg, falseNeg = kNearestClassify(reducedTraining, testSet, 'M', 9)
getStats(truePos, falsePos, trueNeg, falseNeg)

#%% 

def prevalenceClassify(training, testSet, label):
    '''
    Assumes training and testSet lists of examples
    Uses a prevelance-based classifier to predict whether each example in testSet is of class label
    returns number of true positives, false positives, true negatives and false negatives
    '''
    numWithLabel = 0
    for e in training:
        if e.getLabel() == label:
            numWithLabel += 1
    probLabel = numWithLabel/len(training)
    truePos, falsePos, trueNeg, falseNeg = 0,0,0,0
    for e in testSet:
        if random.random() < probLabel: # guess label
            if e.getLabel() == label:
                truePos += 1
            else: 
                falsePos += 1
        else: # guess not label 
            if e.getLabel() != label:
                trueNeg += 1
            else:
                falseNeg += 1
    return truePos, falsePos, trueNeg, falseNeg 

#%% 

def findK(training, minK, maxK, numFolds, label):
    # find average accuracy for range of odd values of k
    accuracies = []
    for k in range(minK, maxK + 1, 2):
        score = 0.0
        for i in range(numFolds):
            # downsample to reduce computation time
            fold = random.sample(training, min(5000, len(training)))
            examples, testSet = divide80_20(fold)
            truePos, falsePos, trueNeg, falseNeg = kNearestClassify(examples, testSet, label, k)
            score += accuracy(truePos, falsePos, trueNeg, falseNeg)
        accuracies.append(score/numFolds)
    pylab.plot(range(minK, maxK + 1, 2), accuracies)
    pylab.title('Average Accuracy vs k (' + str(numFolds) + ' folds)')
    pylab.xlabel('k')
    pylab.ylabel('Accuracy')
    
#findK(training, 1, 21, 1, 'M')

#%% Regression Based Classifiers

# build training sets for men and women

ageM, ageW, timeM, timeW= [], [], [], []
for e in training:
    if e.getLabel() == 'M':
        ageM.append(float(e.getAge()))
        timeM.append(float(e.getTime()))
    else: 
        ageW.append(float(e.getAge()))
        timeW.append(float(e.getTime()))

# down sample to make plot of examples readable
ages, times = [], []
for i in random.sample(range(len(ageM)), 300): 
    ages.append(ageM[i])
    times.append(timeM[i])

# produce scatter plot of examples
pylab.plot(ages, times, 'yo', markersize = 6, label = 'Men')

ages, times = [], []
for i in random.sample(range(len(ageW)), 300):
    ages.append(ageW[i])
    times.append(timeW[i])
pylab.plot(ages, times, 'k^', markersize = 6, label = 'Women')

# Learn two first degree linear regression models

mModel = pylab.polyfit(ageM, timeM, 1)
fModel = pylab.polyfit(ageW, timeW, 1)

# plot lines corresponding to models
xmin, xmax = 15, 85
pylab.plot((xmin, xmax), (pylab.polyval(mModel, (xmin, xmax))), 'k', label = 'Men')
pylab.plot((xmin, xmax), (pylab.polyval(fModel, (xmin, xmax))), 'k--', label = 'Women')
pylab.title('Linear Regression Models')
pylab.xlabel('Age')
pylab.ylabel('Finishing Time (Minutes)')
pylab.legend()

#%% 

truePos, falsePos, trueNeg, falseNeg = 0,0,0,0
for e in testSet:
    age = float(e.getAge())
    time = float(e.getTime())
    if abs(time - pylab.polyval(mModel, age)) < abs(time - pylab.polyval(fModel, age)):
        if e.getLabel() == 'M':
            truePos += 1
        else:
            falsePos += 1
    else:
        if e.getLabel() == 'F':
            trueNeg += 1
        else: 
            falseNeg += 1
getStats(truePos, falsePos, trueNeg, falseNeg)

#%% 

import sklearn.linear_model

featureVecs, labels = [], []
for i in range(25000): # create 4 examples in each iteration
    featureVecs.append([random.gauss(0, 0.5), random.gauss(0, 0.5), random.random()])
    labels.append('A')
    featureVecs.append([random.gauss(0, 0.5), random.gauss(2, 0.5), random.random()])
    labels.append('B')
    featureVecs.append([random.gauss(2, 0.5), random.gauss(0, 0.5), random.random()])
    labels.append('C')
    featureVecs.append([random.gauss(2, 0.5), random.gauss(2, 0.5), random.random()])
    labels.append('D')

model = sklearn.linear_model.LogisticRegression().fit(featureVecs, labels)
print('model.classes_ =', model.classes_)

for i in range(len(model.coef_)):
    print('For label', model.classes_[i], 'feature weights =', model.coef_[i])
print('[0, 0] Probs =', model.predict_proba([[0, 0, 1]])[0])
print('[0, 2] Probs =', model.predict_proba([[0, 2, 2]])[0])
print('[2, 0] Probs =', model.predict_proba([[2, 0, 3]])[0])
print('[2, 2] Probs =', model.predict_proba([[2, 2, 4]])[0])

#%% 

featureVecs, labels = [], []
for i in range(20000):
    featureVecs.append([random.gauss(0, 0.5), random.gauss(0, 0.5)])
    labels.append('A')
    featureVecs.append([random.gauss(2, 0.5), random.gauss(2, 0.5)])
    labels.append('D')
model = sklearn.linear_model.LogisticRegression().fit(featureVecs, labels)

print('model.coef =', model.coef_)
print('[0, 0] Probs =', model.predict_proba([[0, 0]])[0])
print('[0, 2] Probs =', model.predict_proba([[0, 2]])[0])
print('[2, 0] Probs =', model.predict_proba([[2, 0]])[0])
print('[2, 2] Probs =', model.predict_proba([[2, 2]])[0])


#%% 

'''
model - an object of type logistic regression for which a fit has been constructed
testSet - a sequence of examples 
label - the label of the positive class. The confusion matrix returned by applyModel is relative to this label
prob - the probability threshold to be used in deciding which label to assign to an example in testSet. Default is 0.5
'''

# RETURNS ERROR: TypeError: Cannot cast array data from dtype('float64') to dtype('<U32') according to the rule 'safe'

def applyModel(model, testSet, label, prob = 0.5):
    # create vector containing feature vectors for all test examples
    testFeatureVecs = [e.getFeatures() for e in testSet]
    probs = model.predict_proba(testFeatureVecs)
    truePos, falsePos, trueNeg, falseNeg = 0,0,0,0
    for i in range(len(probs)):
        if probs[i][1] > prob:
            if testSet[i].getLabel() == label:
                truePos += 1
            else: 
                falsePos += 1
        else: 
            if testSet[i].getLabel() != label:
                trueNeg += 1
            else:
                falseNeg += 1
    return truePos, falsePos, trueNeg, falseNeg

examples = buildMarathonExamples('bm_results2012.txt')
training, test = divide80_20(examples)

featureVecs, labels = [], []
for e in training:
    featureVecs.append([float(e.getAge()), float(e.getTime())])
    labels.append(e.getLabel())
model = sklearn.linear_model.LogisticRegression().fit(featureVecs, labels)
print('Feature weights for label M:', 'age =', str(round(model.coef_[0][0], 3)) + ', time =', round(model.coef_[0][1], 3))
truePos, falsePos, trueNeg, falseNeg = applyModel(model, test, 'M', 0.5)
getStats(truePos, falsePos, trueNeg, falseNeg)

#%% 

def buildROC(model, testSet, label, title, plot = True):
    xVals, yVals = [], []
    p = 0.0
    while p <= 1.0:
        truePos, falsePos, trueNeg, falseNeg = applyModel(model, testSet, label, p)
        xVals.append(1.0 - specificity(trueNeg, falsePos))
        yVals.append(sensitivity(truePos, falseNeg))
        p += 0.01
    auroc = sklearn.metrics.auc(xVals, yVals, True)
    if plot: 
        pylab.plot([0, 1], [0,1,], '--')
        pylab.title(title + ' (AUROC = ' + str(round(auroc, 3)) + ')')
        pylab.xlabel('1 - Specificity')
        pylab.ylabel('Sensitivity')
    return auroc

buildROC(model, test, 'M', 'ROC for Predicting Gender')

#%% Surviving the Titanic

def minkowskiDistance(v1, v2, p):
    """Assumes v1 and v2 are equal-length arrays of numbers
       Returns Minkowski distance of order p between v1 and v2"""
    dist = 0.0
    for i in range(len(v1)):
        dist += abs(v1[i] - v2[i])**p
    return dist**(1 / p)

#%%

class Passenger(object):
    features = ('C1', 'C2', 'C3', 'age', 'male gender')
    def __init__(self, pClass, age, gender, survived, name):
        self.name = name
        self.featureVec = [0, 0, 0, age, gender]
        self.featureVec[pClass - 1] = 1
        self.label = survived
        self.cabinetClass = pClass
        
    def distance(self, other):
        return minkowskiDistance(self.featureVec, other.featureVec, 2)
    
    def getClass(self):
        return self.cabinClass
    
    def getAge(self):
        return self.featureVec[3]
    
    def getGender(self):
        return self.featureVec[4]
    
    def getName(self):
        return self.name
    
    def getFeatures(self):
        return self.featureVec[:]
    
    def getLabel(self):
        return self.label
    
#%% 
'''
def getTitanicData(fname):
    data = {}
    data['class'], data['survived'], data['age'] = [], [], []
    data['gender'], data['name'] = [], []
    f = open(fname)
    line = f.readline()
    while line != '':
        split = line.split(',')
        data['class'].append(int(split[0]))
        data['age'].append(int(split[1]))
        if split[2] == 'M':
            data['gender'].append(1)
        else: 
            data['gender'].append(0)
        data['survived'].append(int(split[3])) # 1 = survived
        data['name'].append(split[4:])
        line = f.readline()
    return data

def buildTitanicExamples(fileName):
    data = getTitanicData(fileName)
    examples = []
    for i in range(len(data['class'])):
        p = Passenger(data['class'][i], data['age'][i], data['gender'][i], data['survived'][i], data['name'][i])
        examples.append(p)
    return examples

examples = buildTitanicExamples('TitanicPassengers.txt')
'''

def getTitanicData(fname):
    data = {}
    data['class'], data['survived'], data['age'] = [], [], []
    data['gender'], data['name'] = [], []
    f = open(fname)
    line = f.readline()
    while line != '':
        split = line.split(',')
        data['class'].append(int(split[0]))
        data['age'].append(float(split[1]))
        if split[2] == 'M':
            data['gender'].append(1)
        else:
            data['gender'].append(0)
        data['survived'].append(int(split[3])) #1 = survived
        data['name'].append(split[4:])
        line = f.readline()
    return data

def buildTitanicExamples(fileName):
    data = getTitanicData(fileName)
    examples = []
    for i in range(len(data['class'])):
        p = Passenger(data['class'][i], data['age'][i],
                      data['gender'][i], data['survived'][i],
                      data['name'][i])
        examples.append(p)
    return examples

examples = buildTitanicExamples('TitanicPassengers.txt')

#%% 

def summarizeStats(stats):
    '''
    Assumes stats a list of 5 floats: accuracy, sensitivity, specificity, pos pred val, roc
    '''
    def printStat(X, name):
        mean = round(sum(X)/len(X), 3)
        std = stdDev(X)
        print('Mean', name, '=', str(mean) + ', 95% confidence interval =', round(1.96*std, 3))
    accs, sens, specs, ppvs, aurocs = [], [], [], [], []
    
    for stat in stats:
        accs.append(stat[0])
        sens.append(stat[1])
        specs.append(stat[2])
        ppvs.append(stat[3])
        aurocs.append(stat[4])
    
    printStat(accs, 'Accuracy')
    printStat(sens, 'Sensitivity')
    printStat(specs, 'Specificity')
    printStat(ppvs, 'Positive Predictive Value')
    printStat(aurocs, 'AUROC')

def testModels(examples, numTrials, printStats, printWeights):
    stats, weights = [], [[], [], [], [], []]
    for i in range(numTrials):
        training, testSet = divide80_20(examples)
        xVals, yVals = [], []
        for e in training:
            xVals.append(e.getFeatures())
            yVals.append(e.getLabel())
        xVals = pylab.array(xVals)
        yVals = pylab.array(yVals)
        model = sklearn.linear_model.LogisticRegression().fit(xVals, yVals)
        
        for i in range(len(Passenger.features)):
            weights[i].append(model.coef_[0][i])
        truePos, falsePos, trueNeg, falseNeg = applyModel(model, testSet, 1, 0.5)
        auroc = buildROC(model, testSet, 1, None, False)
        tmp = getStats(truePos, falsePos, trueNeg, falseNeg, False)
        stats.append(tmp + (auroc,))
    print('Averages for', numTrials, 'trials')
    if printWeights:
        for feature in range(len(weights)):
            featureMean = sum(weights[feature])/numTrials
            featureStd = stdDev(weights[feature])
            print('Mean weight of', Passenger.features[feature], '=', str(round(featureMean, 3)) + ', 95% confidence interval =', round(1.96*featureStd, 3))
    if printStats:
        summarizeStats(stats)
        
#%% 

testModels(examples, 100, True, False)
# look at weights of the features
testModels(examples, 100, False, True)