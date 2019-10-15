# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 19:07:14 2019

@author: HP
"""

def rgb2hue(r,g,b):
    d=max(r,g,b)-min(r,g,b)
    if r==max(r,g,b):
        h=60*(g-b)/d
    elif g==max(r,g,b):
        h=120+60*(b-r)/d
    else:
        h=240+60*(r-g)/d
    if h<0:
        h=h+360
    return h