# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 10:36:23 2019

@author: HP
"""

def genderGuess(n):
    if n[-1]=="a" or n[-1]=="e" or n[-1]=="i" or n[-1]=="o" or n[-1]=="u" or n[-1]=="y":
            if n.count("f")>=2:
                return 0.35
            else:
                return 0.87
    else:
        if n[0]=="k":
            return 0.69
        else:
            return 0.25
        