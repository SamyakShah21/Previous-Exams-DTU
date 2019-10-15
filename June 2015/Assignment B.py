# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 13:54:22 2019

@author: HP
"""

def computeShirtSize(c,w):
    if c<=42 and c>=38 and w>=30 and w<=35:
        return "Small"
    elif c<=44 and c>=40 and w>=32 and w<=37:
        return "Medium"
    elif c<=46 and c>=42 and w>=34 and w<=39:
        return "Large"
    elif c<=48 and c>=44 and w>=36 and w<=41:
        return "X-Large"
    elif c<=50 and c>=46 and w>=38 and w<=43:
        return "XX-Large"
    else:
        return "Not available"