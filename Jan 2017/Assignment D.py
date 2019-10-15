# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 13:41:35 2019

@author: HP
"""

import numpy as np
def predictability(x):
    q=np.zeros(5)
    for n in range(np.size(x)):
        q[x[n]-1]=q[x[n]-1]+1
    r=np.zeros((5,5))
    for j in range (np.size(x)-1):
        r[x[j]-1,x[j+1]-1]=r[x[j]-1,x[j+1]-1]+1
    pn= q[x[0]-1]/np.size(x)
    for i in range(np.size(x)-1):
        pn=pn+r[x[i]-1,x[i+1]-1]/q[x[i]-1]
    return pn/np.size(x)
        