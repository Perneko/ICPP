# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 08:56:00 2018

@author: Dr. Neptune
"""

 # 4.5 | Modules Circle.py
 
pi = 3.14159
 
def area(radius):
     return pi*(radius**2)
 
def circumference(radius):
    return 2*pi*radius

def sphereSurface(radius):
    return 4.0 * area(radius)

def sphereVolume(radius):
    return (4.0/3.0) * pi * (radius**3)