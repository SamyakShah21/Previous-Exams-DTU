# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 23:43:06 2019

@author: HP
"""

import numpy as np
def nBest(a,n):
    b=np.sort(a)
    return a[a>=b[np.size(a)-n]]
    