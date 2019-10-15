# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 13:38:28 2019

@author: HP
"""

import math
def voldif(r,n):
    return ((2*r)**n - ((math.pi**(n/2))*r**n)/math.gamma((n+2)/2))