# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 13:34:25 2019

@author: HP
"""

import numpy as np
def symmetrize(x):
    y=np.zeros(np.shape(x))
    for i in range(np.shape(x)[0]):
        for j in range(np.shape(x)[0]):
            if i==j:
                y[i][j]=x[i][j]
            else:
                y[i][j]=x[i][j]+x[j][i]
    return y