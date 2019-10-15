# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 18:15:13 2019

@author: HP
"""

import numpy as np
def survivalTemperature(m,g):
    if any(m>500) or any(m<50) or any(g<0.04) or any(g>0.45):
        return "RangeError"
    t=np.zeros((np.size(m),np.size(g)))
    for i in range(np.size(m)):
        for j in range(np.size(g)):
            t[i][j]=36-(0.9*m[i]-12)*(g[j]+0.95)/(27.8*g[j])
    return t
        