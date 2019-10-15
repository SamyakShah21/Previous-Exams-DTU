# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 11:24:12 2019

@author: HP
"""
import numpy as np
import math

def approximatepi(n):
    x=np.zeros((n,n))
    y=np.zeros((n,n))
    k=0
    for i in range(n):
        for j in range(n):
            x[i][j]=(1/(2*n))+(j/n)
            y[i][j]=(1/(2*n))+(i/n)
            if math.sqrt(x[i][j]**2+y[i][j]**2)<1:
                k=k+1
    return k*4/n**2
    