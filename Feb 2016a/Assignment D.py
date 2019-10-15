# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 19:54:53 2019

@author: HP
"""

import numpy as np
def similarityMatrix(x,y,d):
    s=np.zeros((np.size(x),np.size(y)))
    for i in range(np.size(x)):
        for j in range(np.size(y)):
            s[i][j]=np.exp(-d*(x[i]-y[j])**2)
    return s