# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 08:41:52 2018

@author: Dr. Neptune
"""

# 8.1| Abstract Data Types and Classes

#%% 

class IntSet(object):
    '''
    An intSet is a set of integers
    '''
    # Information about the implementation
    # Value of the set is represented by a list of ints, self.vals
    # Each int in the set occurs in self.vals exactly once
    
    def __init__(self):
        ''' Create an empty set of integers'''
        self.vals = []
        
    def insert(self, e):
        ''' Assumes e is an integer and inserts e into self'''
        if e not in self.vals:
            self.vals.append(e)
            
    def member(self, e):
        ''' Assumes e is an integer
            Returns true is e is in self, false OW
        '''
        return e in self.vals
    
    def remove(self, e):
        ''' Assumes e is an integer and removes e from self
            Raises ValueError is e is not in self
        '''
        try: 
            self.vals.remove(e)
        except: 
            raise ValueError(str(e) + ' not found')
    
    def getMembers(self):
        '''Returns a list containing the elements of self
            Nothing can be assumed about the order of the elements
        '''
        return self.vals[:]
    
    def __str__(self):
        '''Returns a string representation of self'''
        self.vals.sort()
        result = ''
        for e in self.vals:
            result += str(e) + ','
        return '{' + result[:-1] + '}' #-1 omits trailing comma
        
    
    #%% 
    # s = IntSet() initializes a new IntSet object 
    # s.getMembers() calls the method
    
    #%% 8.1.2 Using Classes to Keep Track of Students and Faculty
    
    import datetime
    
    class Person(object):
        
        def __init__(self, name):
            ''' Create a person'''
            self.name = name
            try: 
                lastBlank = name.rindex(' ')
                self.lastName = name[lastBlank+1:]
            except:
                self.lastName = name
            self.birthday = None
            
        def getName(self):
            ''' Returns self's full name'''
            return self.name
        
        def getLastName(self):
            ''' Returns selfs last name'''
            return self.lastName
        
        def setBirthday(self, birthDate):
            '''Assumes birthdate is a type of datetime.date
               sets the persons birthday
            '''
            self.birthday = birthDate
            
            
        def getAge(self):
            '''
            Returns self's current age in days
            '''
            if self.birthday == None:
                raise ValueError
            return (datetime.date.today() - self.birthday).days
        
        def __lt__(self, other):
            '''
            Returns True is self precedes other in alphabetical order, false ow
            Comparison is based on last names, but if there are the same,
            full names are compared. 
            '''
            if self.lastName == other.lastName:
                return self.name < other.name
            return self.lastName < other.lastname
        
        def __str__(self):
            '''Returns selfs name'''
            return self.name
        
        
#%% Make use of person class
me = Person('Michael Rose')
him = Person('Itsy Bitsy Spider')
her = Person('Kelsey')
print(me.getLastName())
me.setBirthday(datetime.date(1991, 12, 2))
her.setBirthday(datetime.date(1996, 1, 11))
print(me.getName(), 'is', me.getAge(), 'days old')
mother = Person('Holly Somers')
mother.setBirthday(datetime.date(1971, 9, 26))
print(mother.getName(), 'is', mother.getAge(), 'days old')                  