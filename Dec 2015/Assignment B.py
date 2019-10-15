# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 21:09:48 2019

@author: HP
"""

def hireApplicant(x,y):
    if x<5:
        return "No go"
    elif x>=5 and y>0.9*x+1:
        return "Too expensive"
    elif x>=5 and x<8 and y<=0.9*x+1:
        return "Hire"
    elif x>=8 and y>4 and y<=0.9*x+1:
        return "Long term contract"
    else:
        return "Unicorn"