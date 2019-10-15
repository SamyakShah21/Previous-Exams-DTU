# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 15:29:00 2019

@author: HP
"""

import numpy as np
def dataparser(data):
    if data[0]==0:
        if data[1]>np.size(data[2:]):
            return np.array([])
        else:
            return data[2:2+data[1]]
    elif data[0]==1:
        if data[1]*data[2]>np.size(data[3:]):
            return np.array([])
        else:
            return np.reshape(data[3:(3+data[1]*data[2])],[data[1],data[2]])
    else:
        return np.array([])
        