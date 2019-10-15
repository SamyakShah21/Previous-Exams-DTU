# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 12:45:54 2019

@author: HP
"""

import numpy as np
def fitpolynomial(x,y,n):
    w=np.zeros((np.size(x),n+1))
    for i in range(np.size(x)):
        for j in range(n+1):
            w[i][j]=x[i]**j
    a=np.dot(np.dot(np.linalg.inv((np.dot(w.T,w))),w.T),y)
    return a
