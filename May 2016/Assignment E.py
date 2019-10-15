# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 10:44:18 2019

@author: HP
"""

import numpy as np
def matrixSearch(a,x):
    i=0
    j=np.shape(a)[1]-1
    while i<np.shape(a)[0] and j>=0:
        if a[i][j]==x:
            return np.array([i+1,j+1])
        elif a[i][j]>x:
            j=j-1
        elif a[i][j]<x:
            i=i+1
    return np.array([0,0])