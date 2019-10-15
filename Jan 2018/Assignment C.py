# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 17:57:07 2019

@author: HP
"""

import numpy as np
def chaos(x,k,t):
    s=np.zeros(t)
    for i in range(t):
        x=k*x*(1-x)
        s[i]=x
    return s