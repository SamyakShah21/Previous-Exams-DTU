# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 11:24:52 2019

@author: HP
"""

def medal(age,p):
    medal=""
    if age[0]=="B":
        if p<=20 and p>=10:
            medal="gold"
        elif p<=9 and p>=5:
            medal="silver"
        elif p<=4 and p>=0:
            medal="bronze"
    elif age[0]=="P":
        if p<=20 and p>=15:
            medal="gold"
        elif p<=14 and p>=10:
            medal="silver"
        elif p<=9 and p>=5:
            medal="bronze"
    elif age[0]=="G":
        if p<=20 and p>=17:
            medal="gold"
        elif p<=16 and p>=14:
            medal="silver"
        elif p<=13 and p>=11:
            medal="bronze"
    else:
        if p<=20 and p>=19:
            medal="gold"
        elif p<=18 and p>=17:
            medal="silver"
        elif p<=16 and p>=15:
            medal="bronze"
    if medal=="":
        return ("You got {:d} points.".format(p))
    else:
        return ("You got {:d} points and won a {:s} medal.".format(p,medal))
    
        