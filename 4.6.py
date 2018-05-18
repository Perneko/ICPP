# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 09:04:32 2018

@author: Dr. Neptune
"""

# 4.6 Files

# open file for writing
nameHandle = open('kids', 'w')

# enter file content. In this case, names
for i in range(2):
    name = input('Enter name: ')
    nameHandle.write(name + '\n')
nameHandle.close()

# open file for reading

nameHandle = open('kids', 'r')

for line in nameHandle:
    print(line[:-1])
nameHandle.close()

# open file for appending

nameHandle = open('kids', 'a')

for line in range(4):
    name = input('Enter name: ')
    nameHandle.write(name + '\n')
nameHandle.close()

nameHandle = open('kids', 'r')

for line in nameHandle:
    print(line[:-1])
nameHandle.close()

'''
    open(fn, 'w') - write
    open(fn, 'r') - read
    open(fn, 'a') - append
    fn.read() - returns a string containing the contents associated with the file handle fn
    fn.readline() returns the next line in the file associated with the file handle
    fn.readlines() returns a list of each element of which is one line of the file associated with the file handle
    fn.write(s) - writes a string s to the end of the file associated with the file handle
    fn.writeLines(s) - s is a sequence of strings. Writes each element of S as a seperate line to the file associated with the file handle
    fn.close() closes the file associated with the file handle 
'''