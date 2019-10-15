# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 15:39:27 2019

@author: HP
"""

import numpy as np
def temperaturemonitor(T):
    w=np.zeros(len(T))
    for i in range(len(T)):
        if i>0:
            if T[i]>5 and T[i-1]>5:
                w[i]=3
            elif T[i]<0 and T[i-1]<0:
                w[i]=2
            elif abs(T[i]-T[i-1])>2:
                w[i]=1
            else:
                w[i]=0
    return w