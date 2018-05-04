#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 10:41:33 2018

@author: michael
"""

# 20 | Conditional Probability and Bayesian Statistics

#%% 
# Finger exercise: given a normal distribution, we can see that the probability of being above 180 is P(within 1 std Dev) + p(above 1 std dev (positive))
# Then we get ~.66 + .33/2 = ~.82. Then we multiply by the probability of being male, so 0.5 * .82 = 0.41. This doesn't entirely work
# because we only have the weight distribution for males and not females, so the prior and the support are not independent at all

#%% 
def calcBayes(priorA, probBifA, probB):
    '''
    priorA: initial estimate of probability of A independent of B
    priorBifA: est. probability of B assuming A is true
    probB: est. probability of B
    returns probability of A given B
    '''
    return (priorA * probBifA)/probB

#%% Calculate probability of A die given rolling 6
priorA = 1/3
prob6ifA = 1/5
prob6 = (1/5 + 1/6 + 1/7)/3

postA = calcBayes(priorA, prob6ifA, prob6)
print('Probability of Type A =', round(postA, 4))

postA = calcBayes(postA, prob6ifA, prob6)
print('Probability of Type A =', round(postA, 4))

# Revise estimate upwards

#%% Calc probability of A die given not rolling 6

postA = calcBayes(priorA, 1 - prob6ifA, 1 - prob6)
print('Probability of Type A =', round(postA, 4))

postA = calcBayes(postA, 1 - prob6ifA, 1 - prob6)
print('Probability of Type A =', round(postA, 4))

# Revise estimate downwards

#%% What if 90% of the bag is A dice? 

priorA = 0.9

postA = calcBayes(priorA, 1 - prob6ifA, 1 - prob6)
print('Probability of Type A =', round(postA, 4))

postA = calcBayes(postA, 1 - prob6ifA, 1 - prob6)
print('Probability of Type A =', round(postA, 4))

#%% 90% of dice are type A, see what happens if the die is actually type C

import random

numRolls = 200
postA = priorA
for i in range(numRolls + 1):
    if i%(numRolls//10) == 0:
        print('After', i, 'rolls. Probability of Type A =', round(postA, 4))
    isSix = random.random() <= 1/7 # because die of type c
    if isSix:
        postA = calcBayes(postA, prob6ifA, prob6)
    else: 
        postA = calcBayes(postA, 1 - prob6ifA, 1 - prob6)