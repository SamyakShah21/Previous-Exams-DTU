# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 12:42:37 2019

@author: HP
"""

def climbCategorization(d,g):
    if g>8:
        if d>=12:
            return "Extreme"
        elif d>=8:
            return "Difficult"
        elif d>=4:
            return "Medium"
        elif d>=2:
            return "Easy"
        else:
            return "Beginner"
    elif d>16:
        if g>=6:
            return "Extreme"
        elif g>=4:
            return "Difficult"
        elif g>=2:
            return "Medium"
        elif g>=1:
            return "Easy"
        else:
            return "Beginner"
    else:
        if d*g>=96:
            return "Extreme"
        elif d*g>=64:
            return "Difficult"
        elif d*g>=32:
            return "Medium"
        elif d*g>=16:
            return "Easy"
        else:
            return "Beginner"