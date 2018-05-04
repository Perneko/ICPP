#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 00:37:45 2018

@author: michael
"""

# 11 | Plotting and More About Classes

#%% 
import pylab

pylab.figure(1)
pylab.plot([1, 2, 3, 4], [1, 7, 3, 5])
pylab.show()

#%% 
pylab.figure(1)
pylab.plot([1, 2, 3, 4], [1, 2, 3, 4])

pylab.figure(2)
pylab.plot([1, 4, 2, 3], [5, 6, 7, 8])
pylab.savefig('Figure-Addie')

pylab.figure(1)
pylab.plot([5, 6, 10, 3])
pylab.savefig('Figure-Jane')

#%% 

principal = 10000 # initial investment
interestRate = 0.05
years = 20
values = []

for i in range(years + 1):
    values.append(principal)
    principal += principal*interestRate

pylab.plot(values, 'pink', linewidth = 30)

pylab.title('5% Growth, Compounded Annually', fonsize = 'xx-large')
pylab.xlabel('Years of Compounding', fontsize = 'x-small')
pylab.ylabel('Value of Principal ($)')


#%% Set Default rcvalues

# set line width
pylab.rcParams['lines.linewidth'] = 4
# set font size for titles
pylab.rcParams['axes.titlesize'] = 20
# set font size for labels on axes 
pylab.rcParams['axes.labelsize'] = 20
# set size of numbers on x-axis
pylab.rcParams['xtick.labelsize'] = 16
# set size of numbers on y-axis
pylab.rcParams['ytick.labelsize'] = 16
# set size of ticks on x axis
pylab.rcParams['xtick.major.size'] = 7
# set size of ticks on y axis
pylab.rcParams['ytick.major.size'] = 7
# set size of markers, e.g. circles representing points
pylab.rcParams['lines.markersize'] = 10
# set number of times marker his shown when displaying legend
pylab.rcParams['legend.numpoints'] = 1


#%% 11.2 | Plotting Mortgages, an Extended Example 

class Mortgage(object):
    '''
    Abstract class for building different kinds of mortgages
    '''
    def __init__(self, loan, annRate, months):
        self.loan = loan
        self.rate = annRate
        self.months = months
        self.paid = [0.0]
        self.outstanding = [loan]
        self.payment = findPayment(loan, self.rate, months)
        self.legend = None # description of mortgage
        
    def makePayment(self):
        self.paid.append(self.payment)
        reduction = self.payment - self.outstanding[-1] * self.rate
        self.outstanding.append(self.outstanding[-1] - reduction)
        
    def getTotalPaid(self):
        return sum(self.paid)
    
    def __str__(self):
        return self.legend
    
    def plotPayments(self, style):
        pylab.plot(self.paid[1:], style, label = self.legend)
        
    def plotBalance(self, style):
        pylab.plot(self.outstanding, style, label = self.legend)

    def plotTotPd(self, style):
        totPd = [self.paid[0]]
        for i in range(1, len(self.paid)):
            totPd.append(totPd[-1] + self.paid[i])
        pylab.plot(totPd, style, label = self.legend)
        
    def plotNet(self, style):
        totPd = [self.paid[0]]
        for i in range(1, len(self.paid)):
            totPd.append(totPd[-1] + self.paid[i])
        equityAcquired = pylab.array([self.loan] * len(self.outstanding))
        equityAcquired -= pylab.array(self.outstanding)
        net = pylab.array(totPd) - equityAcquired
        pylab.plot(net, style, label = self.legend)
        
        
#%% 

a1 = pylab.array([1, 2, 4])
print('a1 =', a1)
a2 = a1*2
print('a2 = ', a2)
print('a1 + 3 =', a1 + 3)
print('3 - a1 = ', 3 - a1)
print('a1 - a2 = ', a1-a2)
print('a1*a2 =', a1*a2)

#%%  Three subclasses of mortgage

class Fixed(Mortgage):
    def __init__(self, loan, r, months):
        Mortgage.__init__(self, loan, r, months)
        self.legend = 'Fixed, ' + str(r*100) + '%'
        
class FixedWithPts(Mortgage):
    def __init__(self, loan, r, months, pts):
        Mortgage.__init__(self, loan, r, months)
        self.pts = pts
        self.paid = [loan*(pts/100.0)]
        self.legend = 'Fixed, ' + str(r*100) + '%, ' + str(pts) + 'points'
        
class TwoRate(Mortgage):
    def __init__(self, loan, r, months, teaserRate, teaserMonths):
        Mortgage.__init__(self, loan, teaserRate, months)
        self.teaserMonths = teaserMonths
        self.teaserRate = teaserRate
        self.nextRate = r/12.0
        self.legend = str(teaserRate*100) + '% for ' + str(self.teaserMonths) + ' months, then' + str(r*100) + '%'

    def makePayment(self):
        if len(self.paid) == self.teaserMonths + 1:
            self.rate = self.nextRate
            self.payment = findPayment(self.outstanding[-1], self.rate, self.months - self.teaserMonths)
        Mortgage.makePayment(self)
        
#%% 

def compareMortgages(amt, years, fixedRate, pts, ptsRate, varRate1, varRate2, varMonths):
    totMonths = years*12
    fixed1 = Fixed(amt, fixedRate, totMonths)
    fixed2 = FixedWithPts(amt, ptsRate, totMonths, pts)
    twoRate = TwoRate(amt, varRate2, totMonths, varRate1, varMonths)
    morts = [fixed1, fixed2, twoRate]
    for m in range(totMonths):
        for mort in morts:
            mort.makePayment()
    plotMortgages(morts, amt)
        
def plotMortgages(morts, amt):
    def labelPlot(figure, title, xLabel, yLabel):
        pylab.figure(figure)
        pylab.title(title)
        pylab.xlabel(xLabel)
        pylab.ylabel(yLabel)
        pylab.legend(loc = 'best')
    styles = ['k-', 'k-.', 'k:']
    # give names to figure numbers
    payments, cost, balance, netCost = 0, 1, 2, 3
    for i in range(len(morts)):
        pylab.figure(payments)
        morts[i].plotPayments(styles[i])
        pylab.figure(cost)
        morts[i].plotTotPd(styles[i])
        pylab.figure(balance)
        morts[i].plotBalance(styles[i])
        pylab.figure(netCost)
        morts[i].plotNet(styles[i])
    labelPlot(payments, 'Monthly Payments of $' + str(amt) + ' Mortgages', 'Months', 'Monthly Payments')
    labelPlot(cost, 'Cash Outlay of $' + str(amt) + ' Mortgages', 'Months', 'Total Payments')
    labelPlot(balance, 'Balance Remaining of $' + str(amt) + ' Mortgages', 'Months', 'Remaining Loan Balance of $')
    labelPlot(netCost, 'Net Cost of $' + str(amt) + ' Mortgages', 'Months', 'Payments - Equity $')
    
#%% 
compareMortgages(200000, 30, 7.0, 3.25, 5.0, 4.5, 9.5, 48)