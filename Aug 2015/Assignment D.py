# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 22:17:15 2019

@author: HP
"""

import math
def starPoints(a,b,maxi):
    
    
    n=3
    while True:
        area=n*a*b*math.sin(math.pi/n)
        if area>maxi:
            break
        n=n+1
    return n-1
        
        