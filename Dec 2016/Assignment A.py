# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 23:08:51 2019

@author: HP
"""

import numpy as np
def cvrchecksum(cvr):
    cvr=(list(str(cvr)))
    w=np.array([2,7,6,5,4,3,2])
    s=0
    for i in range(7):
        s=s+w[i]*int(cvr[i])
    return 11-(s%11)
        