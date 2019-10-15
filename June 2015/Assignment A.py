# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 13:50:58 2019

@author: HP
"""

def computeAgeGroup(a):
    if a>=20:
        return "Adult"
    elif a>=13:
        return "Teenager"
    elif a>=3:
        return "Child"
    elif a>=1:
        return "Toddler"
    else:
        return "Infant"