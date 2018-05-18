# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 07:59:00 2018

@author: Dr. Neptune
"""

# 4.3 | Recursion

'''
Recursive Definitions have: 
    a base case that directly specifies the result for a special case.
    a recursive (inductive) case, typically a simpler version of the same problem
'''

# iterative

def factI(n):
    ''' Assumes n an int > 0. Returns n!'''
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

# recursive

def factR(n):
    ''' Assumes n an int > 0. Returns n!'''
    if n == 1:
        return n
    else:
        return n * factR(n-1)
    
# Fibonacci Numbers

def fib(n):
    ''' Assumes n int >= 0
        Returns Fibonacci of n'''
    if n == 0 or n == 1:
        return 1
    else: 
        return fib(n-1) + fib(n-2)

def testFib(n):
    for i in range(n+1):
        print('Fib of', i, '=', fib(i))
        
# Finger exercise: 3 times 

# 4.3.2 : Palindromes

def isPalindrome(s):
    ''' Assumes s is a str
        Returns True is letters in s form a palindrome
        Returns False otherwise
        Non-letters and capitalization are ignored
    '''
    
    def toChars(s):
        s = s.lower()
        letters = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                letters = letters + c
        return letters 
    
    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])
    
    return isPal(toChars(s))

def isPalindromeShow(s):
    '''
        Assumes s is a str
        Returns True if s is a palindrome; False otherwise
        Punctuation, Spaces, and Capitalization are all ignored
    '''
    
    def toChars(s):
        s = s.lower()
        letters = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvqxyz':
                letters += c
        return letters
    
    def isPal(s):
        print('\tisPal called with', s)
        if len(s) <= 1:
            print('\tAbout to return True from base case')
            return True
        else:
            answer = s[0] == s[-1] and isPal(s[1:-1])
            print('\tAbout to return', answer, 'for', s)
            return answer
    return isPal(toChars(s))

def testIsPalindromeShow():
    print('Try dogGod')
    print(isPalindromeShow('dogGod'))
    print('Try doGood')
    print(isPalindromeShow('doGood'))