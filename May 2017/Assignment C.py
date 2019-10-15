# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 23:06:24 2019

@author: HP
"""

import numpy as np
import math
def partialCorrelation(x):
    p=np.zeros((np.shape(x)[1],np.shape(x)[1]))
    c=np.linalg.inv((np.dot(x.T,x)/x.shape[0]))
    for i in range(np.shape(c)[0]):
        for j in range(np.shape(c)[1]):
            if i==j:
                p[i][j]=1
            else:
                p[i][j]=-c[i][j]/math.sqrt(c[i][i]*c[j][j])
    return p