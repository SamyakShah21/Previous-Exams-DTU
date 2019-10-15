# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 21:49:06 2019

@author: HP
"""

import numpy as np
def cumulativeStock(t):
    s=t[0]
    p=np.array([t[0]])
    for i in range(np.size(t)-1):
        if t[i+1]==0:
            s=0
        else:
            s=s+t[i+1]
        p=np.append(p,s)
    return p
        