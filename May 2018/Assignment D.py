# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 11:16:29 2019

@author: HP
"""

import numpy as np
def polygon(x,y):
    c=np.zeros(np.size(x))
    c[0]=(x[0]-x[np.size(x)-1])*(y[1]-y[0])-(x[1]-x[0])*(y[0]-y[np.size(x)-1])
    c[np.size(x)-1]=(x[np.size(x)-1]-x[np.size(x)-2])*(y[0]-y[np.size(x)-1])-(x[0]-x[np.size(x)-1])*(y[np.size(x)-1]-y[np.size(x)-2])
    for i in range(1,np.size(x)-1):
        c[i]=(x[i]-x[i-1])*(y[i+1]-y[i])-(x[i+1]-x[i])*(y[i]-y[i-1])
    return c