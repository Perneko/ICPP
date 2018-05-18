# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 12:35:29 2018

@author: Dr. Neptune
"""

# 5.5 | Strings, Tuples, Ranges, and Lists

'''
seq[i] returns the ith element in the sequence
len(seq) returns the length of the sequence
seq1 + seq2 returns the concatenation of the two sequences
n*seq returns a sequence that repeats seq n times
seq[start:end] returns a slice of the sequence
e in seq is True is e is contained in the sequence, False ow
e not in seq returnes True is e is not in seq, False ow
for e in seq iterates over the elements of a sequence
'''

#%%
# incrementally builds a list containing all the even numbers in a list

L = [1, 2, 3, 4, 5, 6, 7, 8, 9]

evenElems = []
for e in L:
    if e%2 == 0:
        evenElems.append(e)
        
print(evenElems)

#%% 
print('My favorite professor--John G--rocks'.split(' '))
print('My favorite professor--John G--rocks'.split('-'))
print('My favorite professor--John G--rocks'.split('--'))
print('My favorite professor--John G--rocks'.split())

'''
s.count(s1) counts how many times the string s1 occurs in s
s.find(s1) returns the index of the first occurence of the substring s1 in s, 
      and -1 if s1 is not in s
s.rfind(s1) same as find, but starts from the end of s 
       (the 'r' in rfind stands for reverse)
s.index(s1) same as find, but raises an exception if s1 is not in s
s.lower() converts to all lower case
s.replace(old, new) replaces all occurences of the string old in s with new
s.split(d) splits s using d as a delimiter. Returns a list of substrings of s
'''