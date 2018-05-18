# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 11:04:55 2018

@author: Dr. Neptune
"""

# 3.4 | A few words about using floats

x = 0.0
for i in range(10):
    x = x + 0.1
if x == 1.0:
    print(x, ' = 1.0')
else: 
    print(x, 'is not 1.0')
    
# The decimal equivalent of 10011 is 19

# for printing equivalents, use round

# sqrt 2
print(round(2**0.5, 4))

# for comparisons between floats, comparing if the 2 compared values
# are within a specific range is better than ==

# use abs(x-y) <= 0.0001 rather than x == y if x,y are floats

