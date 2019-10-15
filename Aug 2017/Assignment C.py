# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 19:16:12 2019

@author: HP
"""

import math
import numpy as np
def polygonPerimeter(x,y):
    p=math.sqrt((x[-1]-x[0])**2+(y[-1]-y[0])**2)
    for i in range(np.size(x)-1):
        p=p+math.sqrt((x[i]-x[i+1])**2+(y[i]-y[i+1])**2)
    return p
    