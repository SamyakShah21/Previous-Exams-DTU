# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 12:05:54 2019

@author: HP
"""

def bookPages(a):
    if a%4==0:
        return a
    else:
        return a+4-(a%4)