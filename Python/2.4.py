# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 09:34:28 2018

@author: Dr. Neptune
"""

# 2.4 | Iteration

numXs = int(input('How many times should I print the letter X? '))

toPrint = ''

if numXs == 1:
    toPrint = 'X'
if numXs == 2:
    toPrint = 'XX'
#etc
print(toPrint)

# Square an integer the hard way
x = -1
ans = 0
itersLeft = abs(x)
while (itersLeft != 0):
    ans = ans + abs(x)
    itersLeft = itersLeft - 1
print(str(x) + '*' + str(x) + ' = ' + str(ans))

# finger exercise
#%%

numXs = int(input("How many times should I print the letter X?"))
toPrint = ''
#concatenate X to print numXs times
xIters = abs(numXs)
while (xIters != 0):
    toPrint = toPrint + "X"
    xIters = xIters - 1
print(toPrint)

# break statements
#%%
# Find a positive integer that is divisible by both 11 and 12

x = 1
while True: 
    if x%11 == 0 and x%12 == 0:
        break
    x = x + 1
print(x, 'is divisible by 11 and 12')

# finger exercise
#%%

L = []
toIter = ''

for i in range(10):
    numInts = int(input("Enter int"))
    L.append(numInts)

x = 0

for e in L:
    if e %2 == 0:
        continue
    else: 
        if e > x:
            x = e
print(x)

