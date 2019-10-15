# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 18:28:24 2019

@author: HP
"""

import numpy as np
def bestBuy(p,m):
    for i in range(np.size(p)):
        if m<p[i]:
            return i
        else:
            m=m-p[i]
    return np.size(p)