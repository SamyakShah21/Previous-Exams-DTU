# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 12:42:38 2019

@author: HP
"""

import numpy as np
def polygonarea(x,y):
    p=0
    for i in range(np.size(x)-1):
        p=p+x[i]*y[i+1]-y[i]*x[i+1]
    p=p+x[-1]*y[0]-x[0]*y[-1]
    return p/2