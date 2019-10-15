# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 12:37:57 2019

@author: HP
"""

import math
def trianglearea(a,b,c):
    s=(a+b+c)/2
    if a+b>c and b+c>a and c+a>b:
        area=math.sqrt(s*(s-a)*(s-b)*(s-c))
    else:
        area=0
    return area
    