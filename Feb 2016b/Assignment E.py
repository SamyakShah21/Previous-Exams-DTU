# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 00:10:43 2019

@author: HP
"""

import numpy as np
def taskDispatch(t,u):
    a=np.zeros(np.size(t))
    for i in range(np.size(u)):
        for j in range(np.size(t)):
            if a[j]==0:
                if t[j]<=u[i]:
                    u[i]=u[i]-t[j]
                    a[j]=i+1
    return a