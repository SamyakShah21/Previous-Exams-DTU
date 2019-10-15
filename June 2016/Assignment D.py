# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 18:22:12 2019

@author: HP
"""

def greenEyes(m,p):
    if m=="brown":
        if p=="brown":
            return 19
        elif p=="blue":
            return 0
        else:
            return 38
    elif m=="blue":
        if p=="blue":
            return 1
        elif p=="green":
            return 50
        else:
            return 0
    else:
        if p=="green":
            return 75
        elif p=="blue":
            return 50
        else:
            return 38