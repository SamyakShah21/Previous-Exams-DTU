# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 23:40:43 2019

@author: HP
"""

import numpy as np
def submatrix(M, r, c):

    
    S = M
    
    
    if r>=1 and r<=M.shape[0]:
        S = np.delete(S,r-1,0)

    
    if c>=1 and c<=M.shape[1]:
        S = np.delete(S,c-1,1)
    
    return S