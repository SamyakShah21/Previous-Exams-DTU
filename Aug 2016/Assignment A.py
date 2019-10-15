# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 13:20:29 2019

@author: HP
"""

import numpy as np
import math
def confidence(x):
    m=np.mean(x)
    s=0
    for i in range(np.size(x)):
        s=s+((x[i]-m)**2)/(np.size(x)-1)
    s= math.sqrt(s)
    return np.array([m-(2*s/math.sqrt(np.size(x))),m+(2*s/math.sqrt(np.size(x)))])