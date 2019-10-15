# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 19:20:25 2019

@author: HP
"""

import numpy as np
import math
def rotateScale(co,ce,t,s):
    n=np.shape(co)[1]
    b=np.array([[math.cos(t),-math.sin(t)],[math.sin(t),math.cos(t)]])
    d=np.vstack((ce[0]*np.ones(n),ce[1]*np.ones(n)))
    return np.dot(b,(co-d))*s+d