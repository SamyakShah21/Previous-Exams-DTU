# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 23:17:47 2019

@author: HP
"""
import numpy as np
def zeroCrossing(s):
    c=0
    for i in range(np.size(s)-1):
        if s[i]*s[i+1]<0:
            c=c+1
    return c