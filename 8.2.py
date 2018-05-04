#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 20:06:47 2018

@author: michael
"""

# 8.1 + 8.2 + 8.3 + 8.4

#%% From 8.1, Person Class

import datetime

class Person(object):
        
        def __init__(self, name):
            '''
            Create a person
            '''
            self.name = name
            try:
                lastBlank = name.rindex(" ")
                self.lastName = name[lastBlank+1:]
            except:
                self.lastName = name
            self.birthday = None
            
        def getName(self):
            '''
            Returns self's full name
            '''
            return self.name
        
        def getLastName(self):
            '''
            Returns self's last name
            '''
            return self.lastName
        
        def setBirthday(self, birthdate):
            '''
            Assumes birthdate is of type datetime.date
            Sets self's birthday to birthdate
            '''
            self.birthday = birthdate
            
        def getAge(self):
            '''
            Returns self's current age in days
            '''
            if self.birthday == None:
                raise ValueError
            else:
                return (datetime.date.today() - self.birthday).days
        
        def __lt__(self, other):
            '''
            Returns True if self precedes other in alphabetical order, and False ow
            Comparison is based on last names, but if these are the same full names are compared
            '''
            if self.lastName == other.lastName:
                return self.name < other.name
            else: 
                return self.lastName < other.lastName
            
        def __str__(self):
            '''
            Returns self's name
            '''
            return self.name 
        
#%% Make some 'Persons'

me = Person('Michael Rose')
kelsey = Person('Kelsey Rustin')
madonna = Person('Madonna')
colonel = Person('Colonel Kernel Kernelson')
print(me.getLastName())
me.setBirthday(datetime.date(1991,12,02))
print(me.getAge())

#%% 8.2 MIT Person is a subclass of Person

class MITPerson(Person): 
    
    nextIdNum = 0 # id number
    
    def __init__(self, name):
        Person.__init__(self, name)
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1
        
    def getIdNum(self):
        return self.idNum
    
    def __lt__(self, other):
        return self.idNum < other.idNum
    
    def isStudent(self):
        return isinstance(self, Student)

#%% Make some MIT People

p1 = MITPerson('Barbara Beaver')
print(str(p1) + '\'s id number is ' + str(p1.getIdNum()))

#%% 

p1 = MITPerson('Mark Guttag')
p2 = MITPerson('Billy Bob Beaver')
p3 = MITPerson('Billy Bob Beaver')
p4 = Person('Billy Bob Beaver')

print('p1 < p2 = ', p1 < p2)
print('p3 < p2 = ', p3 < p2)
print('p4 < p1 = ', p4 < p1)
print('p1 < p4 = ', p1 < p4)

#%% Multiple Levels of Inheritance

class Student(MITPerson):
    pass

class UG(Student):
    
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear
    
    def getClass(self):
        return self.year
    
class Grad(Student):
    pass

'''
Person > MITStudent > Student > (UG, Grad)
'''

#%% 

p5 = Grad('Buzz Aldrin')
p6 = UG('Billy Beaver', 1984)
print(p5.getName(), 'is a graduate student is', type(p5) == Grad)
print(p5.getName(), 'is an undergraduate student is', type(p5) == UG)

#%%
print(p5.getName(), 'is a student is', p5.isStudent())
print(p6.getName(), 'is a student is', p6.isStudent())
print(p3.getName(), 'is a student is', p3.isStudent())

#%%
class TransferStudent(Student):
    
    def __init__(self, name, fromSchool):
        MITPerson.__init__(self, name)
        self.fromSchool = fromSchool
        
    def getOldSchool(self):
        return self.fromSchool 

#%% 8.3 | Encapsulation and Information Hiding

class Grades(object):
    
    def __init__(self):
        '''
        Creates empty grade book
        '''
        self.students = []
        self.grades = {}
        self.isSorted = True
        
    def addStudent(self, student):
        '''
        Assumes student is of type Student
        Add student to the grade book
        '''
        if student in self.students:
            raise ValueError('Duplicate Student')
        self.students.append(student)
        self.grades[student.getIdNum()] = []
        self.isSorted = False
        
    def addGrade(self, student, grade):
        '''
        Assumes grade is a float
        Add grade to the list of grades for the student
        '''
        try:
            self.grades[student.getIdNum()].append(grade)
        except:
            raise ValueError('Student not in mapping')
        
    def getGrades(self, student):
        '''
        Returns a list of grades for the student
        '''
        try: # return a copy of list of student's grades
            return self.grades[student.getIdNum()][:]
        except:
            raise ValueError('Student not in mapping')
        
#==============================================================================
#     def getStudents(self):
#         '''
#         Return a sorted list of the students in the gradebook
#         '''
#         if not self.isSorted:
#             self.students.sort()
#             self.isSorted = True
#         return self.students[:] # return a copy of student list
#==============================================================================

    def getStudents(self):
        '''
        Return a sorted list of the students in the grade book one at a time in alphabetical order
        '''
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        for s in self.students:
            yield s
    
#%% grade report

def gradeReport(course):
    '''
    Assumes course is of type Grades
    '''
    report = ''
    for s in course.getStudents():
        tot = 0.0
        numGrades = 0
        for g in course.getGrades(s):
            tot += g
            numGrades += 1
        try: 
            average = tot / numGrades
            report = report + '\n' + str(s) + '\'s mean grade is ' + str(average)
        except ZeroDivisionError:
            report = report + '\n' + str(s) + ' has no grades'
    return report
        
#%% 
ug1 = UG('Jane Doe', 2014)
ug2 = UG('John Doe', 2015)
ug3 = UG('David Henry', 2003)
g1 = Grad('Billy Buckner')
g2 = Grad('Bucky F. Dent')

sixHundred = Grades()
sixHundred.addStudent(ug1)
sixHundred.addStudent(ug2)
sixHundred.addStudent(g1)
sixHundred.addStudent(g2)

for s in sixHundred.getStudents():
    sixHundred.addGrade(s, 75)

sixHundred.addGrade(g1, 25)
sixHundred.addGrade(g2, 100)
sixHundred.addStudent(ug3)
print(gradeReport(sixHundred))

#%% Information Hiding

class infoHiding(object):
    
    def __init__(self):
        self.visible = 'Look at me'
        self.__alsoVisible__ = 'Look at me too'
        self.__invisible = 'Don\'t look at me directly'
        
    def printVisible(self):
        print(self.visible)
        
    def printInvisible(self):
        print(self.__invisible)
        
    def __printInvisible(self):
        print(self.__invisible)
        
    def __printInvisible__(self):
        print(self.__invisible)
        
#%% 

test = infoHiding()
print(test.visible)
print(test.__alsoVisible__)
print(test.__invisible)

#%% 
test.printInvisible()
test.__printInvisible__()
test.__printInvisible()

#%%
class subClass(infoHiding):
    def __init__(self):
        print('from subclass', self.__invisible)

#%% 

testSub = subClass()

'''
A disciplined programmer can simply follow the rule of not directly accessing
data attributes outside the class in which they are defined. 
'''

#%% 8.3.1 | Generators

#    def getStudents(self):
#        '''
#        Return a sorted list of the students in the grade book one at a time in alphabetical order
#        '''
#        if not self.isSorted:
#            self.students.sort()
#            self.isSorted = True
#        for s in self.students:
#            yield s

book = Grades()
book.addStudent(Grad('Julie'))
book.addStudent(Grad('Charlie'))
for s in book.getStudents():
    print(s)
    
#%% 8.4 | Mortgages, An Extended Example

def findPayment(loan, r, m):
    '''
    Assumes: Loan and r are floats, m an int
    Returns the monthly payment for a mortgage of size loan at
    a monthly rate of r for m months
    '''
    return loan*((r*(1 + r)**m)/((1+r)**m - 1))

class Mortgage(object):
    '''
    Abstract class for building different kinds of mortgages
    '''
    
    def __init__(self, loan, annRate, months):
        '''
        Assumes loan and annRate are floats, months an int
        Creates a new mortgage of size loan, duration months, and annual
        rate annRate
        '''
        
        self.loan = loan
        self.rate = annRate/12
        self.months = months
        self.paid = [0.0]
        self.outstanding = [loan]
        self.payment = findPayment(loan, self.rate, months)
        self.legend = None # Description of mortgage
        
    def makePayment(self):
        '''
        Make a payment
        '''
        self.paid.append(self.payment)
        reduction = self.payment - self.outstanding[-1]*self.rate
        self.outstanding.append(self.outstanding[-1] - reduction)
        
    def getTotalPaid(self):
        '''
        Return the total amount paid so far
        '''
        return sum(self.paid)
    
    def __str__(self):
        return self.legend 
    
    
class Fixed(Mortgage):
    
    def __init__(self, loan, r, months):
        Mortgage.__init__(self, loan, r, months)
        self.legend = 'Fixed, ' + str(round(r*100, 2)) + '%'
        
class FixedWithPts(Mortgage):

    def __init__(self, loan, r, months, pts):
        Mortgage.__init__(self, loan, r, months)
        self.pts = pts
        self.paid = [loan*(pts/100)]
        self.legend = 'Fixed, ' + str(round(r*100, 2)) + '%. ' + str(pts) + ' points'
        
class TwoRate(Mortgage):
    
    def __init__(self, loan, r, months, teaserRate, teaserMonths):
        Mortgage.__init__(self, loan, r, months)
        self.teaserMonths = teaserMonths
        self.teaserRate = teaserRate
        self.nextRate = r/12
        self.legend = str(teaserRate*100) + '% for ' + str(self.teaserMonths) + ' months, then ' + str(round(r*100, 2)) + '%'
        
    def makePayment(self):
        if len(self.paid) == self.teaserMonths + 1:
            self.rate = self.nextRate
            self.payment = findPayment(self.outstanding[-1], self.rate, self.months - self.teaserMonths)
        Mortgage.makePayment(self)
        
#%% Driver

def compareMortgages(amt, years, fixedRate, pts, ptsRate, varRate1, varRate2, varMonths):
    totMonths = years*12
    fixed1 = Fixed(amt, fixedRate, totMonths)
    fixed2 = FixedWithPts(amt, ptsRate, totMonths, pts)
    twoRate = TwoRate(amt, varRate2, totMonths, varRate1, varMonths)
    morts = [fixed1, fixed2, twoRate]
    for m in range(totMonths):
        for mort in morts:
            mort.makePayment()
    for m in morts:
        print(m)
        print(' Total payments = $' + str(int(m.getTotalPaid())))
        
compareMortgages(amt = 200000, years = 30, fixedRate = 0.07, 
                 pts = 3.25, ptsRate = 0.05, varRate1 = 0.045,
                 varRate2 = 0.095, varMonths = 48)
        
        