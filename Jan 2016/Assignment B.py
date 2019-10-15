# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 12:08:56 2019

@author: HP
"""

import numpy as np
def loadBalance(n):
    abse=np.zeros(np.size(n)-1)
    for k in range(np.size(n)-1):
        abse[k]=abs(np.sum(n[:k+1])-np.sum(n[k+1:]))
    g=np.argmin(abse)+1
        
    return g