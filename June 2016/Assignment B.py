# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 18:09:33 2019

@author: HP
"""

import numpy as np
def danceClass(v):
    if np.size(v)<10 or np.size(v)>30:
        return "invalid"
    elif abs(np.sum(v==1)-np.sum(v==0))>3:
        return "invalid"
    else:
        return "valid"