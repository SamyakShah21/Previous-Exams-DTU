# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 21:28:45 2019

@author: HP
"""

import numpy as np
def sudokuCheck(s):
    i=sum(np.sum(s,1)!=45)+sum(np.sum(s,0)!=45)

    m=np.zeros((3,3))
    for j in range(3):
        for k in range(3):
            m[j,k]=np.sum(np.sum(s[3*j:3*j+3,3*k:3*k+3],axis=1),axis=0)
    
    i=i+np.sum(m!=45)
    return i
            