# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 22:24:59 2019

@author: HP
"""

import numpy as np
def matrixCleanup(m):
    rowi=np.array([])
    coli=np.array([])
    for i in range(np.shape(m)[0]):
        if np.any(m[i]==0):
            rowi=np.append(rowi,i)
    s=np.delete(m,rowi,axis=0)
    
    for j in range(np.shape(m)[1]):
        if np.any(m[:,j]==0):
            coli=np.append(coli,j)
    s=np.delete(s,coli,axis=1)
    return s