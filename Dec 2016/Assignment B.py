# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 23:14:42 2019

@author: HP
"""

def nextleapyear(y):
    m=y+(4-y%4)
    if m%400==0:
        return m
    elif m%100==0:
        return m+4
    else:
        return m