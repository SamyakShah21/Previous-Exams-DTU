# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 23:49:03 2019

@author: HP
"""

import numpy as np
import math
def timeDilation(t,v):
    m=np.zeros((np.size(t),np.size(v)))
    c=299792458
    for i in range(np.size(t)):
        for j in range(np.size(v)):
            m[i][j]=t[i]/math.sqrt(1-(v[j]/c)**2)
    return m
