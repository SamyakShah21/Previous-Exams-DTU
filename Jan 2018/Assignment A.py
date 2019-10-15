# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 17:40:33 2019

@author: HP
"""

def health(a,f,s):
    if a>14:
        return "CERTAIN"
    else:
        if f<=6:
            return "FREQUENT"
        elif s>10:
            return "LIKELY"
        else:
            return "RARE"
            