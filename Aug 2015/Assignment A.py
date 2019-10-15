# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 21:45:19 2019

@author: HP
"""

def classifyBMI(h,w):
    b=w/h**2
    if b<16:
        return "Severely underweight"
    elif b<18.5:
        return "Underweight"
    elif b<25:
        return "Normal"
    elif b<30:
        return "Overweight"
    elif b<40:
        return "Obese"
    else:
        return "Severely obese"