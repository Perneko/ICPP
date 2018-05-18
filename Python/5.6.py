# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 12:45:45 2018

@author: Dr. Neptune
"""

# 5.6 | Dictionaries

#%%

monthNumbers = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May':5, 'Jun':6,
                'Jul':7, 'Aug':8, 'Sep':9, 'Oct':10, 'Nov':11, 'Dec': 12,
                1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May'}

print('The third month is', monthNumbers[3])
dist = monthNumbers['Apr'] - monthNumbers['Jan']
print('Apr and Jan are', dist, 'months apart')

#%% 
# add entry
monthNumbers['June'] = 6
monthNumbers['May'] = 'V'

def keySearch(L, k):
    for elem in L:
        if elem[0] == k:
            return elem[1]
    return None

#%%

EtoF = {'bread':'pain', 'wine':'vin', 'with':'avec', 'I':'Je',
        'eat':'mange', 'drink':'bois', 'John':'Jean', 'friends':'amis',
        'and':'et', 'of':'du', 'red':'rouge'}

FtoE = {'pain':'bread', 'vin':'wine',  'avec':'with',  'Je':'I', 
        'mange':'eat',  'bois':'drink',  'Jean':'John',  'amis':'friends', 
        'et':'and',  'du':'of',  'rouge':'red'}

dicts = {'English to French':EtoF, 'French to English':FtoE}

def translateWord(word, dictionary):
    if word in dictionary.keys():
        return dictionary[word]
    elif word !='':
        return '"' + word + '"'
    return word

def translate(phrase, dicts, direction):
    UCLetters = 'ABCDEFGHIJKLMNOPQRSTUVQXYZ'
    LCLetters = UCLetters.lower()
    letters = UCLetters + LCLetters
    dictionary = dicts[direction]
    translation = ''
    word = ''
    
    for c in phrase:
        if c in letters:
            word += c
        else: 
            translation += translateWord(word, dictionary) + c
            word = ''
    return translation + ' ' + translateWord(word, dictionary)

print(translate('I drink good red wine, and eat bread.', dicts,'English to French'))
print(translate('Je bois du vin rouge.', dicts, 'French to English'))
                            
#%%

keys = []
for e in monthNumbers:
    keys.append(str(e))
print(keys)
keys.sort()
print(keys)

#%% 

birthStones = {'Jan':'Garnet', 'Feb':'Amethyst', 'Mar':'Aquamarine',
               'Apr':'Diamond', 'May':'Emerald'}
months = birthStones.keys()
print(months)
birthStones['Jun'] = 'Pearl'
print(months)

'''
for an object to be hashable, it has to have a hash method that can convert it 
and an eq method that checks for equivalence
in python, all of the immutable data structures like tuples can be used
mutable DS's can not be used. A tuple is a good choice generally
'''

'''
len(d) rreturns the number of items in d
d.keys() returns a view of the keys in d
d.values() returns a view of the values in d
k in d returns True if key k is in d
d[k] returns the item in d with key k
d.get(k, v) returns d[k] if k is in d, and v otherwise
d[k] = v associates the value v with with key k in d. pre-existing values are replaced
del d[k] removes the key k from d
for k in d iterates over the keys in d
'''

