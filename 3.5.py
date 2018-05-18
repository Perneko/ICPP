# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 11:18:59 2018

@author: Dr. Neptune
"""

# 3.5 | Newton Raphson

# if a value (guess) is an approximation to the root of a polynomial
# then guess - p(guess) / p'(guess) is a better approximation 

# This method works by successive approximation

# Newton-Raphson for Square Root
epsilon = 0.01
k = 24.0 
guess = k / 2.0
numGuesses = 0
while abs(guess*guess - k) >= epsilon:
    guess = guess - (((guess**2) - k)/(2*guess))
    numGuesses += 1
print('Square root of', k, 'is about', guess, 'Completed in ', numGuesses, 'guesses')