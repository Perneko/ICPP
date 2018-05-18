# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 10:02:55 2018

@author: Dr. Neptune
"""

# 5.3 | Lists and Mutability

#%%

L = ['I did it all', 4, 'Love']

for i in range(len(L)):
    print(L[i])

[1, 2, 3, 4][1:3][1]


#%% 
Techs = ['MIT', 'Caltech']
Ivys = ['Harvard', 'Yale', 'Brown']

Univs = [Techs, Ivys]
Univs1 = [['MIT', 'Caltech'], ['Harvard', 'Yale', 'Brown']]

print('Universities =', Univs)
print('Universities 1 =', Univs1)
print(Univs == Univs1)

#%%
# test value equality
print(Univs == Univs1)

# test object equality
print(id(Univs) == id(Univs1))

print('ID of Univs =', id(Univs))
print('ID of Univs1 =', id(Univs1))

#%% 

Techs.append('RPI')
print(Techs)

'''
When there are 2 distinct paths to the same list object, we can that aliasing
'''

#%% 

for e in Univs:
    print('Univs contains', e)
    print('\twhich contains')
    for u in e:
        print('\t', u)
        
#%% 

L1 = [1, 2, 3]
L2 = [4, 5, 6]
L3 = L1 + L2
print('L3 =', L3)

L1.extend(L2)
print('L1 =', L1)
L1.append(L2)
print('L1 =', L1)

'''
L.append(e) adds the object e to the end of L
L.count(e) returns the number of times that e occurs in L
L.insert(i, e) inserts the object e into L at index i
L.extend(L1) adds the items in list L1 to the end of L
L.remove(e) deletes the first occurence of e from L
L.index(e) returns the index of the first occurrence of e in L, and raises an exception if e is not in L
L.pop(i) removes and returns the item at index i in L, raises an exception is L is empty. If i is omitted, it defaults to -1, to remove and return the last element of L
L.sort() sorts the elements of L in ascending order
L.reverse() reverses the order of the elements in L 
'''

# Cloning

#%% 

'''
It is prudent to avoid mutating a list over which one is iterating. 
This can cause side effects 
'''

def removeDups(L1, L2):
    '''
    Assumes that L1 and L2 are lists.
    Removes any element from L1 that also occurs in L2
    '''
    
    for e1 in L1:
        if e1 in L2:
            L1.remove(e1)

L1 = [1, 2, 3, 4]
L2 = [1, 2, 5, 6]

removeDups(L1, L2)
print('L1 =', L1)

#%% 
'''
This mutation can be aovided using slicing to clone (make a copy of the list)
'''

# 5.3.2 | List Comprehension

L = [x**2 for x in range(1,7)]
print(L)

mixed = [1, 2, 'a', 3, 4.0]
print([x**2 for x in mixed if type(x) == int])